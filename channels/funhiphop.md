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
<img src="https://cdn4.telesco.pe/file/uIm0T3pqXlX0hc23FIrGPxlJLeKuXvfe0ignZCdQokZy-GW2J21jvP_-YP7Vmlj4KX_iHGG1AtCyx3a0qc78GVEraDJ-DVxCYSWquFSn-LBfXfiTdjrSulepeghzHEB5SYSXOHxQukzQLpZzMoBlursnDpxAzpbHiVicUnc2yvuJ0JHJcQ6FSQfrwrJvz8hT77LdyAt4Qx0Lq8aVdwXp2dXPIFDo5XY3Bn6N94meXlYDHlOHzIgFS2IleA5F8YkD7aa17E82rt-WUk__1gpyS7ANVMMt_jG_W2y_6jqGS2l5DjmITIDuMOfm2pTvPiHwog3eoUGWk6CVLc9ZAYFK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 175K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 01:40:16</div>
<hr>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzUCNVp-51euRBBm8ASzTL0ghnZ51_Ycz06FF5nVklg2kzLrxwS5xXvdMi9G4BH2fz8ylrDGN1YonJrq4xlMvdLG9ROBs7uJVZye-RgxH2dALXdLDMrofcc6xrZGeUQEpHmr6Aterr3uxHPfK4HGhvlthY6IrwRoJYBlpOqtnWXDz_5lTG-lSFlw5QOefOXbDE0f2cNZYumo2fijRJQ2borCLSRx4WX7KQW-3VjTHACtKcum2UrA7UcIgcEhyel2be0Hk56YfkqXc4_C3bAl0MzWF_WjL6RsKwbI996ZjgKVADymkWViuOQvGxkPAyHc2PhCpi7IHyjXnVUm1eW7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbjRaHXMnong5r-Y9A9Fi-D19ZBRbpKWSAyACHe4yQ6iCoZ-hZvdk_52BO8i944Abk3O2PBdvkdaubATsDz7QOH_G5AblxqGgC49GcDNGIfmcsB773dnkj0etwxSwWCA1PGyVwaVi44jRNGiHaDggQWKBC2X0HYdZD3PvzjduiQ-GKxwqpmbzEqK2STMFCOK1nLakR3NZb41GsMacKzz0uuP8ndg6qfXyEvSPokESNThuhiobs-2FLJ64xlJVnQbNLiRJqVqgEHPPZVwckANK85L_pBgrEthfAGv-WxRzukIgvmLrWfs5cPEpouDj_6oI53fnM1zAPUK1ch4oq_HXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=HXj5IatdA05ixK_sPMaHIVSa0s87rpQlJZhiRJtQ2xE8YGo55VC2A0UShk0FltVtihiWajhFlpcpxw_PgeddNjZqoG89us6JGS2M-9qLjkn_-cCGJq9mR1rxbEAvPlGDBjRtZzOcywjj0UR7cxiOOVFZbSWRGIo48a6RaG87jdEFcVDWc6gebTqIdayIz06UE7bxvxl4BD9qVbGaQp-_ilXaEIVLHHjWGoUwxdpvMGXF4gLGsr4_KYOnmoYPYk81iR1BDBuKAk0KQ3Q-iAaHrF645Cwc-lwc10gQXwtEl4sUA-fwnQoGvITKkamUeyoXGdYDPl_qHzpSEfTpvvlHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=HXj5IatdA05ixK_sPMaHIVSa0s87rpQlJZhiRJtQ2xE8YGo55VC2A0UShk0FltVtihiWajhFlpcpxw_PgeddNjZqoG89us6JGS2M-9qLjkn_-cCGJq9mR1rxbEAvPlGDBjRtZzOcywjj0UR7cxiOOVFZbSWRGIo48a6RaG87jdEFcVDWc6gebTqIdayIz06UE7bxvxl4BD9qVbGaQp-_ilXaEIVLHHjWGoUwxdpvMGXF4gLGsr4_KYOnmoYPYk81iR1BDBuKAk0KQ3Q-iAaHrF645Cwc-lwc10gQXwtEl4sUA-fwnQoGvITKkamUeyoXGdYDPl_qHzpSEfTpvvlHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=Ejf4Vkh7GNW0z-zMPOGu8FViWXNf1ksB1jDnvW-Z2Souya5l-nI9ohmfUc4IVI3w3f7XL8aOH5wWR9YH0rd4XHTKfH5rxgpTVylVjJNObDiMiLl8ITkjn9DHrKkWTtNaZF026d6fNJ8utGMDOyHrmZR2xFRiVq3b4T3fElnEMWINaKziXUauDNiHeBUp9gh6P0gckQCirx0zDasWsGDuT9IiveqeI3yhz3aHx0AAEcdXE4iROFE_HO-u1DiXEH3io7zhwAXz6DMFFOWyPpRo2vqIi1Ei3vTjLvAfDgEwzHt9XlO5EK_qVVrGqs6zyFPC2tHAaxkBAMn_bO6YdHzF-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=Ejf4Vkh7GNW0z-zMPOGu8FViWXNf1ksB1jDnvW-Z2Souya5l-nI9ohmfUc4IVI3w3f7XL8aOH5wWR9YH0rd4XHTKfH5rxgpTVylVjJNObDiMiLl8ITkjn9DHrKkWTtNaZF026d6fNJ8utGMDOyHrmZR2xFRiVq3b4T3fElnEMWINaKziXUauDNiHeBUp9gh6P0gckQCirx0zDasWsGDuT9IiveqeI3yhz3aHx0AAEcdXE4iROFE_HO-u1DiXEH3io7zhwAXz6DMFFOWyPpRo2vqIi1Ei3vTjLvAfDgEwzHt9XlO5EK_qVVrGqs6zyFPC2tHAaxkBAMn_bO6YdHzF-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH5_eC7uXy-tsuYl76F-ugn3H3bB4dnqs4EkRIFkMkpyMVDCcuNgbgZuVWj3csPJftgcy0ZY3IuiSlQYlxr8he_moRCy_hHfYLOHhH1m0zOApaTFc-Ot5lnwwFnaDIml7S8Ps9SMeqPTJSiH8GN1BMZoEhWhzVVhg22Uwe0N3w_ZNCDYzxGhpXBpJ06O_tF_5S3g4s9ulYwFFqaJ8KiVVfUAoixdaq19x_d51tbC9HBX4s84LiniiXqORq_QohL7xJKqgAOmXAvO8LCMWW3Z0tSc9bIOOWg9Ju7aIkDbssyC8U23Ve_wPMMDZxsutPE7MYkywde6hBdh7JiZhQF50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=BQkaETSmyx8gJwAExFXQlpQNIbBF_sLzqGsuQL9AJZk6iIIa9YceyiOinoGqD0clfe5yi1LdtEY6sTC5f-5bjEWMEscrsvZAHbc8a13c6SkNHeHMmoGqGz_OvA_aHm0u4xKEEH-OykTERPoAWnfKPn7MFE58QbvczWvj3ElYTI-AciTNcYlneLMrAkozW-X05mN1o9VPQJzxnJQuuaBVfBprRTGh0P3aWiZrM2XPPfYQE0OvHYT6cSbSq3o8iKoLFyXHmbwhd7T2DMGPFt4MR7VN1ydiTXhDD4XKa6fFFt-Y5eTZQBj8M06QYQcnHYogvAMjqGApxaxVI3vysAONgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=BQkaETSmyx8gJwAExFXQlpQNIbBF_sLzqGsuQL9AJZk6iIIa9YceyiOinoGqD0clfe5yi1LdtEY6sTC5f-5bjEWMEscrsvZAHbc8a13c6SkNHeHMmoGqGz_OvA_aHm0u4xKEEH-OykTERPoAWnfKPn7MFE58QbvczWvj3ElYTI-AciTNcYlneLMrAkozW-X05mN1o9VPQJzxnJQuuaBVfBprRTGh0P3aWiZrM2XPPfYQE0OvHYT6cSbSq3o8iKoLFyXHmbwhd7T2DMGPFt4MR7VN1ydiTXhDD4XKa6fFFt-Y5eTZQBj8M06QYQcnHYogvAMjqGApxaxVI3vysAONgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W62onPAL0JU4UnPlNaz1uDlE-BxPxxDsXkFYiuu_eDzInc2AlKvHOP8o8QqJrqYDXjxTg9EZlHKKjzJjFUMQZFRdXCArNmyBsIZCH9BAUsWlTI-3QHKAC7fhoIFuB1jaKSwZBB3yAY9flXoJz7mNfotCG1Q-Xgj_7a8EicPJSV2zIRQRtY2lHllGUKshjeiQEIQLaRo91TolqWocPAcrnCV8y_iTzUR4R276-yuahwALM1kL5Nh_i6_buA38IqCoFxihW5FjrsWOftr5n-zA9g_cx5JW_rCBrRjLFHNukLmPLcDan9HRQuSJK5n3ic18pfuTQSIbb8wUdVIlL5Nf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2Cc-zJ2Ph16MmdICqhQE60h_sjTVadbj2N7YsZjnfKur9qxbj0eBWu4zMqhh4_UNLDsU5IHaJ-lI8ocJn212lk8NVc2eCJEGrc8Y9YLp0G07aB5qyZWxLwu-seupM3cQ2DXkSYBlBfzfH0xqa1Gp7Is8spnctVdKqwecrEmZUA22siAvoXd7Mp2rShwnjCi9gyJSBVJcj7o2Qw-JXwgYLeZu_P-jOzjvOuF5VepTT1t4PRMRifHusxy9oocOzk-S41eiDpPljyRJjaoZTqwThTml0tuXM7yFLduGv_g54pD5pGYu_jIxkIRFzkwetMEHx5DNQPrbEmFfhHXfqSw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=NSf75J1TvHD_DyOmqzuSzkv0iLEP6VCBcsX2bkeI1Swqa6FpBPhQB4NzUvg6ShWKRzEqQwpvOmsbEQkbZAjP7xqwCrP0Dyx4yDpSsegSac55Ty3p8jAeVxCoWwYM0tluJ6xFKxa6LiX52rJS-4VMvzrvdwjBkfaG-j05qGjhRUojRhWCDurXEzZlGQ8OCA_pDpfiXxSU53prOPaFzpIHJKQOEyQZcrQbA5sv3uUt1XOM9mgciWbK_hKHSIgmaHI_b75VJaXSxQkKzN4QQoP8F_A9VfWVh9RjlRvUCu0Aarwev-Sf3GqcwdoB7LX6XfeSxbx4NZ80bUsoD2UMQOPk0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=NSf75J1TvHD_DyOmqzuSzkv0iLEP6VCBcsX2bkeI1Swqa6FpBPhQB4NzUvg6ShWKRzEqQwpvOmsbEQkbZAjP7xqwCrP0Dyx4yDpSsegSac55Ty3p8jAeVxCoWwYM0tluJ6xFKxa6LiX52rJS-4VMvzrvdwjBkfaG-j05qGjhRUojRhWCDurXEzZlGQ8OCA_pDpfiXxSU53prOPaFzpIHJKQOEyQZcrQbA5sv3uUt1XOM9mgciWbK_hKHSIgmaHI_b75VJaXSxQkKzN4QQoP8F_A9VfWVh9RjlRvUCu0Aarwev-Sf3GqcwdoB7LX6XfeSxbx4NZ80bUsoD2UMQOPk0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAo6dBuR26LzYtVao7vZ58w8yzPFVNOZ-Kdk7OfeuUd5R9KrZXgZnTB2hjJQiX1S95BjH44g4-fbbj8ZxAWZdeV5jvZRkiOTnfcFSX3MopbcM_Bqe0t5Uav6aYsFsaMPEJPYyKynGgsBURS0WOttkntC9Md_h1d62-PmURuwv_SCgpwPF9IctKuF-Xoq183sJvlc-nfVxC4Tc9HAcompRc6F5lH3g3hdppPDRiqz4qa9X43VpVhxNANMWQBmFDJUuFsSfIkD6_PsJZcFGskCfoyfYCNWpfRQnU4aKpqX4TWbQZkEbYsAH3TTNhxS9lJiPaeVmXll8WigwaBBLD0avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry1XI0YKVHrfysBFTiGMCIbd1vIULvVvNRhUPXN4LfaD5MZFoTk1xp5VsBZ-Zt60mlZwqJyQP1NdHZkit7tTi5s3tUTZpU8AIEN3NCpVbFB_AW757wXYeZ7_jjuNSKMNa-jc4fxlzgcikxZQr2OS0S8ArShGiTNwnDKiZeIig2hk7C3v46K7whPYgQsf8pzgFTMHaLMvrJqumvlkkMN1WgmLc4c2rQGlEbXEqMy1HFn3ZoqSBaG7A8xPaKCeCbXV1fmASKNr5ye3XRPIpyXbr8miH-z062exYioUv9-5SJesD9KDGMRvFa-AP8y0D--FB_bvLf6buNm8mKLFnNTU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/76901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76901" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGv2dg5t81dVk4MeeTc6sSO5VqQs0gb0GNVqk_lMx0g28j8GFfxNjq98Iv__E3XDdeoDaF-8FJ10ec0sb9VwpJm8zWYb8knersR8cRHy2B6c7ONimpZptjN5GuUaF8vjmv_n-Rx8zKbr5Nv0aXtlgpih_dl7y_osG2MS1Kbff7CuGdsgk6aVZlVvprSDkFTrRnmGdmhda_fHOeqR2Ydul340Ap61T1xVxfdj1SklqK6ZGSqf7UnuzaPL2ublW4vK1Qsl5cMSDQa0jDOURF0cli2Fd61-b4w8lwUiM635aLixpGa4UcT03CcKoAmOyPskBw0hn3hUoDKg6m-cZDk-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g15
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76900" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucKU9akFke5XlWXkCXg3ym50j7Oisrxf8z0SF9pcZu8wMyHA5-pobXUvEINtyMNKm7S8wotg5kmWDMFJZtwHPo2DiECL_VW82j1vPzWbFxHJPXFSaDQseea5Z9Lfy-BnOvd0VIRi15Nr25ITafV5E8jt3xN-nZhRErk0mrxSWwqZkXLGyqlrqojdNobCPg7soQYxechWAnIhoY08aNMCv5GbcxvLi8obksytj2wTQoBhTNasL8FT8iwoRnBXTNZKlwj0eES3dDrSQCS3JMC1ef597eESX6WVkYHsk4uTEezyweduNY4t1z9SyUgF4ZU61LmURW6f1m5kCNP8SlZ0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUmPXyAk7XI5Vmfo1q9I7VfIJ6l3IlQG_Xqw8xWVlReCzJGj8hQhKkOsJ26Yz7pc0uXTp9ZPdWNbIhRK5TRtZ_UVrg4r3MBN7bVHzKxaawvZB1zIRniKN9v2R7pZ6wo-pSApzB8xd44mhClIy5ZA6gOz8CSVJy4tK6Y5t95rXjBmH2MrPP5793GoErhuBeHkcTp04xxIeQLy-SU-SAo86TMrPtkRMEHVpTswsbSX5WfWV_XdJMkMtkmfJhzlFZ0BRH7ULk0HmwVPZ1-wDotdHleOS3_CF2SHaMyeoYv6gFGL_vISrlkW7-lTHvdokzzUzg6xSNSqtRxEkVfgmvYTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrOuheZ41HRXd6IxqKxKwgqES9F6zjTO88QvXx_xD9w8u9EC2WiT1m7Y_5zbRt92RjKJFICrqzTkIjKIBTammJY-jSxxmfA8Nq-Qfh-E9trQZ3WHh0GTvLQ_Spmzodc2IwIdxcRqgbLobcKqsT6oGYoYI3Q35sufI_MxX64lDT25Fk7WjzEe0OYaulvKZI0o6Cg9RxyUtZBkJ36ZT7bWDjIS32AtgSDWEoRmXJBATXANH3iBATiOfGlGqJv2X4gngrRsR8zJAbqASWelrbyHiEsWawvHHt3EhVWrfntScYa1V84vnhszpggd6pnQk3r3zHxAVt_ok4JPyE0rOBVmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=sVvXaQP-OVyZ0FAs0EU0DPuE_7KwKo2m9QQ6LfeDkwIwc2A-RbpRJKcvbpFq-Lw1N1BfuyeDvdmfEUzVb6EIEJirUNQP_q92WkRBxK601BJ4qORke5z5n2mxHz71g6uehoV0w_bpMeFjQPYQcMCZxCtZOKja2VhQF-fQdHupU7i5Xske0bdpON_hIZBAxmzRE5bEHfD0SRJqwGbX8YLXNRB2to5Q0srmPFahVwimbApiZt4U14fr_qETT7DWCUgEQAaRw1LQxrcyUituo7mLHCZ5AxLiF6wtE2FXoZCNMkS_V9AVeRxlIMBeAhQvC391-9ZyDuKrlmYuAUqfcFJV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=sVvXaQP-OVyZ0FAs0EU0DPuE_7KwKo2m9QQ6LfeDkwIwc2A-RbpRJKcvbpFq-Lw1N1BfuyeDvdmfEUzVb6EIEJirUNQP_q92WkRBxK601BJ4qORke5z5n2mxHz71g6uehoV0w_bpMeFjQPYQcMCZxCtZOKja2VhQF-fQdHupU7i5Xske0bdpON_hIZBAxmzRE5bEHfD0SRJqwGbX8YLXNRB2to5Q0srmPFahVwimbApiZt4U14fr_qETT7DWCUgEQAaRw1LQxrcyUituo7mLHCZ5AxLiF6wtE2FXoZCNMkS_V9AVeRxlIMBeAhQvC391-9ZyDuKrlmYuAUqfcFJV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvePTFxagqvmVOuFLygK9omv5dui8n0mKWMhafnn48tkUewoFl5vmeNXWIpnuiwwTPlX0cDKoGUQraaezlMJBm9v08D2F8N_GXMmBiBCXjF3rajf_fVzIsh7PqrmxpcOTfdrZ3M-_3ZupHa8ujvNpR4lShbgDPVX01mGgY3hhjiSd_1nkb3ZZtc6WcorgG4RYgotaNt2viKjbZvG7XytluoqTcB7SZrpp1gWoq7ZhyiabWgotIaarDJh0K8fUsae5nsV-joeYssRe114YdP9Q86D5Zs4yhtoST6QtxZBPzJDb8QyWayF1Q2OuChravC83bimK6hh6N9Fei2H6e29dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3rjGyimQlhK0fNNs9NmcHaSITvYMrfcd34U1C-7mq_g_VZTetlRRjVBuKj6eIbqlSVhoiDYunCCScSgGyJFsUfOtX2_noIbhjRawvItrtBGtwcKZVS3fw859v95NOlKYvb30hthpy9ACKKAWic6GBypWX_n5z4V2eGlEgSHym2r6EediqyztaJ7kM42E2X5LTMPUAeUGyPt9L-G6jxXVcj4ITWlxtFEsanwfTroM1Y6QR3xLkxU68ijnvQyTbW4hKxvwjSNaS1OISMr8lTGGo2OzjV5ZKt_zpC3cTz7WJGkmq0qPlA9BreTKDnajFJ4cD-DsmWyHqHleLWrnuSCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jya6jIyz_RxW2AT9QQykrLl8ZdAqtc51UEl1E7q8ks04LWgdVMzsZKPemOP6C2q9URGJFfHDTl5vxBIZNNekCR-nnKZFDByG9OXxILAwlnA4pjK6ZZdobuRBDhYTJarQlSTUiBW5VcHWVqIXmv3wCjBGFKufMboz_xfY07D1_VA4I5384BFOU-9GB6xmH_WFl-b3Q9bTdgstZCKTgGwgGsbqg89nfydL9M2TktHmccyoHq-wucVIJR5y0VtV1TjsLVsMJrilLlRS7j7qte1nktT51odi08-gu1X-Iuy1qa-gox7S1FiBneUS72J2Xc-ecfzR2mbfletfs8kbxF_3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhzBei9n6mnNws-c9HNPAzYRMJ8GzhfEd_O47p1ycwqtAzSczKAGVi7yBF1tFQ-bRFCbhqCKAaLG7QrRTPNpIU2RI2SkrOWR3HUOt-AY6EnxjLnq5hTcdEQQ0HzRrf2IeMsT8c29HjkVR4WXpppE8EqmHg4D489EPY9mDM_uHynRgCXPgbvqPz1P-YEFwYJFUfxXIKBw9zXuP0mvrupfsAYH2w71f2GloqBwSIUGxs9vZn538_I_s2eatBll9fEmAqysMKNxMfzEV72wvlSWWrvuJwh1xH26ATwtu5IXQ2m171HzHWvi4oQpIViYDzGt08huwTQ5JzFET62cCYIYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQEu5qFZ5aZ8ODOPYaaeVbwPkjkkVChNZ7VD_c2VO4naRvEnhaQa7Jva5eHvx0PbY4nGVaka3ojZgeFJYbdm4rtcgaGV5XQdvDIlqgPBX9KHaiB_spf--d88obXP4yRgGEl8C3h2yKh2tfDFbRqxFtgSaNFqzahBX8J5QKL75Fb-4uf1e4q8O41nTelrRU9gbbkQ8AOBAw7HcC4wP_rdu7RW2B0Ig_2tNJvuNLKjivflRmc3bL3xwhUyAFK3eo6QBlSZsZXx3xVqycKHXHoS6fKGbbhh8r_UFZqY2aHsuwRnOtT8AjrkO769gfYCz3CUfr2sZNcHyu48dAoN6T5xSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4oRAoYaIbrAiW0tQ6trFBOxveQUekZRKIEgf2Pn07MSDVyrbQiHYj4uKyvJM0TJZEVbQ4Z_mqNcUzBq4bBQ66UbGDgAiYek1MxjrOfz9ctV2YWL2TVO4_pv3RVQZ0zBqx2VVv4MOKpWFH1nsqx0SqMqsRVDCb9OGc_Ml3RIw9NeMNuCVhHhfJh5LeFm68AyUOzpFYVZKd38EIgxHkQyVkB4r9YKJbvFmOeTEyCAlH_0fwdHcnh2Xd6bzrZ8jLxENHotU8X8irnh7QtvtauAzk0S2glgQBcFFvDmHnBYjoQojeg5wUTfsYz6NTwHOAr-eRzoqtwhxmdPAJEhx4Uphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR7Fd8deI8jCupELobSV3xPdV4FzFSLDr93ED63rKhdJ6b2J4A4OJpb61IhHsHByP7pOL0VCQ72oglT4XcPRFxO91KxJfI90H8VWp8vEveTf212sKfMoNuao6FI3ILsgrkr6c9ABaOMs6CMmDDRvvlie6iII4udhcGlaZW4N0mHa0zdezk_6JzlPtw3zLBj8puy6gcxgpRazfSo_EFBBlt8kgYmV3FODokLqhN-1l128NAWw-AUbmDKJMPZ_hEYsE-v8iUb97VD0toLsN8ARRRPArNlHMzWDRwGDGsXekfsx_PdcvD46T_v8DYsabXtJcBZ6byJyr9lH4tKCqsRYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNqHPBCiuCU17lBYONmoRheMX1jvgTBnLhZeZ_kcI933StUsP272pylY15xsywbkRTNwY1VLX8ss0W5WwqIbkkVxmynk0_8plqzGg5cKff0dBzUy8NSwvnZbnaRmqA56rp0ZzhMUE8OWyX-9DWc1HZn3uNsrQnEuvS7aUGyO22ZmPV2CEN0Z_ISxWmf2DtnfYXUuASBvso8L6CVP_ubXpy31eUKHZ3GNd8HuXFAW31NQaOgpa7tElX_n46eQl1JfISn6xNLWIEN6v7jvpWm8pnCOHA-W2LlIAg1Lv1jE0lNvonwpATlgrnnyEi7lsDmJh6mCzGNjeAO7yhpIj9UCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A34YtUXb-wxhQ3Q6x7rZZfmxSl_gQdjTzSQSlRJ1QIPr8ye3-183jl268kSfdIZ9chscGiJF4Yitvi5GzNetGdKX0i8GtEPeGdDwXlogP_rBb5H24bV7Od9z44AOCAe9CGYSeRzSpsX9aJdtmnSXhWe2WeDUUPCMdaGWk-S9SCrRQOisnuON8jkA_RwAnvlrtKm8cRJql7kqu5SLbRhsBCpCbB-8uFhSOaMEApSGACqQGmeLU7ZVeBPAwMikD-Y26Aqkvw4Z63SvQ26Ap_xITipb4D_tOUcIXCEDWjp_PLjuGaK22Tze2BPbq9cvGRE1IXWILi2jTVrHqsLS_CRauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee4e9n7srU_3PtsIIeHScZPOP85cXXVwEai8L9L30DkS_KMjDbJTvh4KklJd_sIpcF_ITwrcnPp4NaoK4lWcDbtkz_fk4fscTckZ_HShEwFA39kL9y7T97zwjTIGCcQNM6JT0B3Kg_L45Gvm92UjkzUZy6sQN0VfN99ZcgXv-trHiTFmVIm5DFpKsh0YViUCksuy_SHqqu42UdvND_vNBVhm_1NYukCVauGDN7SQvHUUsVcDCZSlxe4uKpb5mNCf3sR84Q7Aip0bu4mOm-uuv1XowFLJOMe6Y5TIFK5cJaP18F6yZuyIl2aSbegb6yIIUjeRKZXzAy8wDoJLIqj0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن نامحدود فروش باز شد به شدت محدود
🥚
هم براى ايفون هم براى اندرويد
🍏
🤖
600
تا اکانت شارژ شد
📣
قیمت آف شدید خورد
🏧
فقط و فقط تا پایان ظهر قیمت 397/000  هزارتومان
( )
➡️
حداقل خرید به علت محدودیت درگاه (
٣٩٧
/
000
) میباشد
💓
جهت خرید ریالی از ربات زیر
❤️
@V2boxinobot
اينم تخفيف امروز
💓
تضمين بازگشت وجه
➡️
➡️
➡️
بدون يكـ ثانيه قطعى
👍
اپليكيشن تخصصى
🤖
🍏
💻
اكانت  ٣١ روزه تكـ كاربر
✅
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76865" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH31fiKONhMmvURX8saMp_40iLFmm-m6hae_WU-frzeZP4R8t_vguQytcQXdTjfVZTvs-pxGUV496rLf5k8N7qEFILsnNcKrnFwsB57Nwg3Mfi4HYIOM_16_jX6a_--xFRUozcORnLDas9A0BgLC-jANHSsHViyUfcR4IpmDLvjJABxVjQhyjo38zZbkwpluJOAaKtWAib3Nni9VWILIR_GnDY1UxOwg-TfsJoY0cdO3hkxv_Qmq5qrM1rSak7XdbSDamOeLAOJXXKmiuL9lmv4OOT6Wz-y0dwoV5J65aVA6gx5Zn46mRVy8UB8yzDJvgfyidolGPllHsuvdRCVSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxjOcI3IfMI3-yW68mMSbtuizQu2Sc0SuPjTQ7HMpfeLu_LY1tJnjYFB0RyIUm1AdqXG3R7cSHSsvdN8ZdcyndVehQvmqcSt3DB0dODpmqprpGiOKRtqwYTylk9NSO31Kl1oloIu36-JWIfDM_1vJeQSiWXoI-_MNJ61HpPi8VZ0o_xb1XdvnOFBOgB0-6v9mu4R74tSBJQvTlHTDBHJ0_vI1HOql9kTrJby-ffZleE-6sWU9GnErzM9UpJMaFCxMlgR3SSm7iESviOYdzJodLlp-6M9_6v6nbpSSeIybqBICD0TAOx23IC2-OiEdQkjX7f9bKwKEpY6kroI-SYEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq0oG2qSnzNKEWTUADZZx6t4OrWzJR1qhNUQSQNxq2sFlAhs82mL0Xbh0h_dDGeYkEJR3NZKkff44NqVZCtUedHLi60i5dtyUtE0Xw_8I86pPBgrHkLDQ5Rwxa5lwDRxugSXunSYb20LdwsSWftPyBJzTR-7nm-pz_EzfkfME_bpda33hqWudVWjgdOxBrQEbJRaarksh12f3MrWnvo-9OjuGJ40PSLf-AiS21_vZTfzGV1pAthq10JQhy05hB-HV3pk9_BqfGAg_IXDhcEcFJ75NV21cK50QN4ImN4TzGsXCsyxJDsv6aouAmDTuGOUDVQ_Ng0tcDGEdZjbzlw-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e570681.mp4?token=jVITEzoFJprmgDIorBrFixWobaSNBrSO3057SOZx_XXGMYIu2R1Ffr-ZSLBIlKcixC24jTfA8K1NUh3KJkPXuUDyGVOC233m5PmHwx_EEtOW3r2ZI6GiuuWZTnooeQfniM5-o2CGy63RkXMREvCVQSiQDcPJemuW-3x58vauDZplO8bD9PkMGjGaRZYUN1Skzs_AzGv4u0u45-2ET_v7ci7qJ7X6mVg02YnFtZuCd5TZTFU2jPD9XmeWuiUpNOLRg8rX7Iop7sKMzBeQNnd8mI5d_EhwuCGkrI3OVJy4DpjCYk9tlMceqbxzu-Sb_yu0rZO9fbtX_k0wJFx8A8EKJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e570681.mp4?token=jVITEzoFJprmgDIorBrFixWobaSNBrSO3057SOZx_XXGMYIu2R1Ffr-ZSLBIlKcixC24jTfA8K1NUh3KJkPXuUDyGVOC233m5PmHwx_EEtOW3r2ZI6GiuuWZTnooeQfniM5-o2CGy63RkXMREvCVQSiQDcPJemuW-3x58vauDZplO8bD9PkMGjGaRZYUN1Skzs_AzGv4u0u45-2ET_v7ci7qJ7X6mVg02YnFtZuCd5TZTFU2jPD9XmeWuiUpNOLRg8rX7Iop7sKMzBeQNnd8mI5d_EhwuCGkrI3OVJy4DpjCYk9tlMceqbxzu-Sb_yu0rZO9fbtX_k0wJFx8A8EKJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر جدید عصر یخبندان ۶
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76851" target="_blank">📅 21:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🛍
قیمت به گیگی 8 هزار تومان کاهش پیدا کرد
🛍
حراج ویژه تا پایان امشب
⭐️
💎
30G-295
💎
50G-470
💎
70G-590
💎
100G-800
🤩
لود بالانس شده و مولتی آیپی
🤩
🤩
بدون ضریب و محدودیت کاربر
🤩
🔴
ظرفیت به شدت محدود هست
💬
خرید
🚀
کانال مشتریان</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76850" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شهر صور در جنوب لبنان بمباران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76849" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdiVpqoIyvvkEpZ_6SnwCvKJ-etTk1HeKK_fqSTWRglSv-6OBuPhNPWlJYPpHgEYQzYwFHDK8T8Y1WNfKrVHNowj65tLxMvWWQMh54IcUdc96G0Ho3402x9IF0IiZQKsmTcQDIiefflJx_KsxCTopFSlvu2rlvc1CJAIShUVrVCAgI_QKmA2dq4HjfQXM1l7stuxIKFy5UET1AAofcehPfzd_dlMpATYBlJpyW4-p2hj8xqU9QJRMXfOOUkPbBVJ7sgdm9yRtGaiaPQORSQSnjVRjERjRvAXpWPTkNS6RcFjKFHH07JoVhxi7uaUrzSdFS4wzcI1WyPIGAfxYRbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6cLBw2ZzwgbDqBhZGBKUmQK_PuLfChT3JmI_VZaBcWdAMJHdmjYTkQmoIrfQq5_lT_NZ7mzHbAzMc3WtdAsiX3sZnnl9nD371lWdm3axo04FIVcOcfJxMELSptZsg3Q4SILf36x66gJlV0xQqRga7GmYVRNNZ8mLzL_8S51cE7TFkPOyNbHHKl-2aUA4RZJm_xn2LkpihVBkpNaRfaDaXg7oRTBx0oX6tb97yzOMEszseV7oPNgwJ7UfDfun5KpEW0aO81O2NfHPB4mBsZdBXHgbNdXM96E8helVZaXXWybi9xKEjlDvDfBGKeeMY-OtaU6akVNhAqJR6JBYY3xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=ZWznKWvJn5BDvfGu6dOF-yoQB0edJMpDmVT4djjh_v-0AakpaNQLEURGKBgAGkMv1VDtqBGvIjJAbqQWtEV3j1X7QuU1fdF8FxrKYNfpHK6j1TyyzfNAyU1SygMACHEhNrV-pyY2qk1Wi10983W99-N_KMyAyqrJwX0DNK4pu-T2L5rB7W5Ic9qdxVfqb7w4-bx1sZaqxUqcdhKk-482et5H1RBX8n7M37-wFjVqEzAwwSaZvXCSOjHZ-EBDsI3xzmnMWdBtH6U-GC5TC32yKcpBvrAO4o4fWG17KVMcYCZW9lvY7hIFixj8bY-vgyBe9bw5ehlm9-D6AoQMsdqiiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=ZWznKWvJn5BDvfGu6dOF-yoQB0edJMpDmVT4djjh_v-0AakpaNQLEURGKBgAGkMv1VDtqBGvIjJAbqQWtEV3j1X7QuU1fdF8FxrKYNfpHK6j1TyyzfNAyU1SygMACHEhNrV-pyY2qk1Wi10983W99-N_KMyAyqrJwX0DNK4pu-T2L5rB7W5Ic9qdxVfqb7w4-bx1sZaqxUqcdhKk-482et5H1RBX8n7M37-wFjVqEzAwwSaZvXCSOjHZ-EBDsI3xzmnMWdBtH6U-GC5TC32yKcpBvrAO4o4fWG17KVMcYCZW9lvY7hIFixj8bY-vgyBe9bw5ehlm9-D6AoQMsdqiiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=Q3t5rX539brddZ0En4LDIdLdAcvyI4jnEn7-Ahyo-zYOS28l-n1WcJ5X4oIxIwDdC7giA5_qvy5AlAqAWql4POaJ0Ms9G2JJFPVCauQZ9YpK1khg8QinZD7rr7qt6BSDCnY5SPK-MXOaURsEk53DdGgHm1cQis-Ogzd-ShOZgbCglf77T3SoriacIJkzaKQRX3dvWfPu6a83L44rAKhCi5RRHC9ffq6-_-JD-0mnFYl4O4fXK3T2VXiTrNehfAvEcuteWxFQH5RbnpKwCnHH6-WCZRVKRdRTkTLy7pWmtFbtOaKJOHdKG8BgbcOay6HIK3f86FU2h6E8ehHT1i70sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=Q3t5rX539brddZ0En4LDIdLdAcvyI4jnEn7-Ahyo-zYOS28l-n1WcJ5X4oIxIwDdC7giA5_qvy5AlAqAWql4POaJ0Ms9G2JJFPVCauQZ9YpK1khg8QinZD7rr7qt6BSDCnY5SPK-MXOaURsEk53DdGgHm1cQis-Ogzd-ShOZgbCglf77T3SoriacIJkzaKQRX3dvWfPu6a83L44rAKhCi5RRHC9ffq6-_-JD-0mnFYl4O4fXK3T2VXiTrNehfAvEcuteWxFQH5RbnpKwCnHH6-WCZRVKRdRTkTLy7pWmtFbtOaKJOHdKG8BgbcOay6HIK3f86FU2h6E8ehHT1i70sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=CTecRELMRHKTBQdP5YMgTjFVq29NP30QuSPiCkAyrekizR16UxtQA9xJAB4cMXMeVAyTfRJ5j8zpkPGdqRiyAuXTx8depfIQ2UlY6Opf0LXoya_IbnFljuhq78tK6dsmeamglwPvrMyW7x3sZgwACbOjeV1onYoBTNTIQ328wmkCWr1Ctjqv2YFgnXJ2xaao7ksv3oh22qQMLGV7wFcdywHPuwkBlp8Ia08l60Duec4qN0Tgxyyx9Emw-E9fbpEGVG5zJIbzzbk_KrjWjVTRVdpfoJFAyut9ocKIZ70MOcw_BkpUY1Bx7p2FN8n5ohmSh-etIMV9q6IqhDLVDbmeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=CTecRELMRHKTBQdP5YMgTjFVq29NP30QuSPiCkAyrekizR16UxtQA9xJAB4cMXMeVAyTfRJ5j8zpkPGdqRiyAuXTx8depfIQ2UlY6Opf0LXoya_IbnFljuhq78tK6dsmeamglwPvrMyW7x3sZgwACbOjeV1onYoBTNTIQ328wmkCWr1Ctjqv2YFgnXJ2xaao7ksv3oh22qQMLGV7wFcdywHPuwkBlp8Ia08l60Duec4qN0Tgxyyx9Emw-E9fbpEGVG5zJIbzzbk_KrjWjVTRVdpfoJFAyut9ocKIZ70MOcw_BkpUY1Bx7p2FN8n5ohmSh-etIMV9q6IqhDLVDbmeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIpWjw_aGFZ8e23Bu42XYENgf4X9t67hdvwBf0Xyrr0nYnAZsZy1xL6tvr-DrSOD0BSN3VTCdU2nVSLdoHCCarfDrqw2Fut56v_uKKEPYp--bZdyQgPWdrSq3AXB5FrhyHMnBEr4keYm75gNsY89dPGNek2anuQoy7XiCBCyGRb6DVHAj5ZFRe5AruSq2O6P5HaU-xm7AXzcalDA91F1JIAW0IdmQ3yPdbuvzfyJx3qJjmZsX87PijcmT-T67aGffYaVTwaP7d48QkfX8ZVbqnhxy6FmwF7akwaAzEY5AMcfAby1hG7YNApdPxKwURKOfsom12oKoEtCivB4kfkBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2Ut79r5DY_5IuGSuyCDnWBnWXbY6pJEvIFoNJtt582i5v5YWeeAItAoxEYYlWNhebQVTUim8_DiIkSuepJFLbpOS-yaQfH55eeD-9o0bk01XIhvhD4WqBbi0QdpxbgOMemDG6rYEk6j70oRHzycUV_hnHWVG011VNTWrBS3EztCiEbbxU1_6CZYHInmoiBGZTqBuDR34WeX_jJzwzM_fxl1p9_doxXLrBUk2a5J03vOzO1EttCo420vP99PcarLvGgmRZqEQ3vR4g-enswaMcpHZnywYOGF1-HFLR7-JJaEunJcpPZh8j3B_ccB5lSdW1e816JRRcwdX3L8JAaC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SugrbAQCdAkdi1dgtQGeq9GKOXrN5-OOTSD2lyHVhWjYc59ARX-sex-RtkuZkMUAPY3Jkr4AIPQ-oyNMgXoMJY1HM6v4__Wx399ZRR_SLu-Xq6umv0h2A7od-eZxqDfJPF4JHekbkDgJ9GulS31tnsyWjidEwJpa8HIFkNJwHxs5PKhbVkZmYXxEO6SDq_xagkk7x-U-fGE1BeJH4b5p-6bB2MD8zhPkHeS4-iSlFhX8k3pzYUxaUHpQgoqhVdcFigag6YdTcukBlZqko4Pn4cURTvcTdR4hK7rcqIjU_sirAE0TNREDvMOPUz19foN4ZzuPt4rJlIk-kcxHL0QHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
