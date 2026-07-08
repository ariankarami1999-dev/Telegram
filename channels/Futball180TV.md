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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 613K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-99041">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسخل‌بودن که شاخ و دم نداره
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/99041" target="_blank">📅 15:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99040">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
ارزش دانلود 1000000000000
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/99040" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp021JLC_ewVeGP_w3ai6feL2j4OoC5tSG2c1gf8MqTHOBwfQ0XP8nQzDcjGIS3UkbgX9k78sHKqCdqhXzeksXKwcIhGLVGz6C4yFRCcL-a8pODy83U_unJ7-0k7DsrzRytWulpicx1jLL96R36T8CfNERbNmEWA54-178hFyOObWA6U66AyI_QqBb1LsQcIj0ihP8MLWInh4dUKdrchn5-u_NC-taCfL-xlVFJLDd1ZyjrLvJTJz2z_TB8neS1r9FzvkAleLL0aqvmX9IfPkh7fbeP6W1XqfyP5NNeEVKmSDSOoTxDFo35uapm0i7ApYZY1vBHReIEsyQDap6uyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین پاس گل تا اینجای‌ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/99039" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدرو پورو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99038" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99037" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/99037" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/99036" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👀
نظر دخترای آمریکایی راجب بازیکنان منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/99035" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5LW7wThjKzTwUzDwCknV31_GdbhWpE_y4uZaQaAXv751pzQc5G0G2ShzL_VItiwepsssYunBWZkYx4cwaw1ohZWkawWHmt95G5DgxjUIJQCSLZiJ0IS_8GeuJYGue55PFq5OuwsvwuOIa788PK5TpXFAInO06vC5QvZwJIPF4bz_z6mCVKIMMWU7BPBAWRBaoeKQgwZBmRt26kHKSoeequxjsARwTxNRZqJiwtkftHjA3c_sF7dWmnqMIie4rVB1VzkWRGq9zFzQ4TBGsvMYm6D6Pgwn_dCeowwEl9zNZJL5qbcVF-g1N9WXJYNvCdC61hrndfQqFM0UATWBwoASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
تیم ملی کرواسی از جدایی زلاتکو دالیچ سرمربی این تیم پس از 9 سال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/99034" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=MOnwfpWrO1Py29GyVI4yvjE8klnMgTl2J_S9j-JJIp4i6yaTfMm-w6yeqVIjkT-Pv8jLDWb7Uq8clGWK9UE9gqhsp6kbYNd_jkLl0U7GQ9ygCrcjQFDnf9BXZ4Cg8t7ZqwYTqYyBLDI4XrqgGUdszNJzY2bhKw1XDeIA6JmYiUvBZfQAfHoCC94EaFFKLKs-GdF3S5HzisQ3B9GwB7j9xvCVRymK9sRN3er6K5rXGqDMequGRonDfIFgGvylBgNL6e8Wf_Hpi7HXI5MzJeaxCJl11G-g5dnyk6cgxiSsRZQ8oR3isWQ-suMPIBF1CyO7-S-hdJ3h2yJAfznaweNJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=MOnwfpWrO1Py29GyVI4yvjE8klnMgTl2J_S9j-JJIp4i6yaTfMm-w6yeqVIjkT-Pv8jLDWb7Uq8clGWK9UE9gqhsp6kbYNd_jkLl0U7GQ9ygCrcjQFDnf9BXZ4Cg8t7ZqwYTqYyBLDI4XrqgGUdszNJzY2bhKw1XDeIA6JmYiUvBZfQAfHoCC94EaFFKLKs-GdF3S5HzisQ3B9GwB7j9xvCVRymK9sRN3er6K5rXGqDMequGRonDfIFgGvylBgNL6e8Wf_Hpi7HXI5MzJeaxCJl11G-g5dnyk6cgxiSsRZQ8oR3isWQ-suMPIBF1CyO7-S-hdJ3h2yJAfznaweNJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تمجید لائوتارو مارتینز و خولیان آلوارز از مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99033" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdqI739o4PiSNGosCy1o8U6QkOtP5_Cy2pXwsMVXkzLsOkKBnwWYUEq65kDR1xvwScFvFbQl4O0Iy7jX2MfzxTSaYcN11GhOxpPlj5Z_kO8AtPMZ947GAYKLxZrPhCRADsESH-uxoUFek4sDeGhs9u4lWdVaWH5XIOAcbOhN_IO2MxL44VTZJTIRYROTGdgWKkvpHtEAOVYOFCM5zFWxf51gd9_JwEAi9oEc2bEoteAnThGKXf4Ym8aaBWcfGDuTRvpQy2RMBU2ZCUHJKE_Vw2PauWWN0krEafUO2M4PqCiW4D7Sy9XcwYQJU-Ptt12tUvpjQ9A1gnRL7CIL2_cAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وضعیت قلبی برخی از طرفداران فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99032" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=K4yoEpqwZ24v02HUizEClFbRrmfcdarzpx-yhKN4L8lN-lXlxoQHzkBUt4wMcBcj1Gh_mcY4jMxMd7UVfTBqJqzDYahb2_V6tIONJufF9QDgy4FSZTLRqflwx79_JXtPTdfH-aRcOp48wZY1eBEV1kAJpNKbsKmcA635T9u7JTfzV2gyTiMq_v_-QXop6J-wqIyVUNDcMTW_kqytwLlqhQ3bko4NqM3Q4Mj_PIwqEsdDH73z89u4ZfKtay4Xkest3OdISmsOdzqReAUTgcigX8ibIBp3wz7f7LicXYhDo6OMkJdNeTdrXHRTMZMOLkvFy_aBkA8fCC1hM7BblQygLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=K4yoEpqwZ24v02HUizEClFbRrmfcdarzpx-yhKN4L8lN-lXlxoQHzkBUt4wMcBcj1Gh_mcY4jMxMd7UVfTBqJqzDYahb2_V6tIONJufF9QDgy4FSZTLRqflwx79_JXtPTdfH-aRcOp48wZY1eBEV1kAJpNKbsKmcA635T9u7JTfzV2gyTiMq_v_-QXop6J-wqIyVUNDcMTW_kqytwLlqhQ3bko4NqM3Q4Mj_PIwqEsdDH73z89u4ZfKtay4Xkest3OdISmsOdzqReAUTgcigX8ibIBp3wz7f7LicXYhDo6OMkJdNeTdrXHRTMZMOLkvFy_aBkA8fCC1hM7BblQygLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ ابوالفضل جلالی بعد از مذاکره با مدیران پرسپولیس، بدون صحبت با خبرنگاران، محل جلسه را ترک کرد. گفته می‌شود کار او با پرسپولیس را باید تمام‌شده دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99031" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifH4DOq1XJTy569CYaI5i-LfHvxhmgWOxMrWUhy3h7WSumzHKQ12IfcLUh-Xe9vczIUxhhZ9jcVbBz7GN4PRjLrqcvj9btsIx9YrW4G5qGjtLZhzsUMbpmS3S4MATM6o_rfAA2eNpyQyPMgb1_Rb527JOClf-o2X34JvYpCjZJDlhjJwBwMDCYzUvLjHbOKxHLLf_1yUuDus98sGosDWxYWA9Hth3OgfcwT8y4QNEEf9lZCcL1UjsVqROQoYnf3y-8RBze2muMScg6uP6aInzU5KHLzMu-BVVUuVzKLQsDil7eeKpyYHVnro6iIscV0wAYF8AxEa48anDR3u-S4wBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇦🇷
#فوووووری
؛ بدلیل توهین‌های نژادپرستانه هواداران آرژانتین به اسپید، فیفا قصد داره فدراسیون فوتبال این کشور رو جریمه سنگینی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99030" target="_blank">📅 13:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=SxNbn42o3s1P1-BiP36DGvCICsfSHRD1mbrkxWXWWQKPJdqFHz15S1YeQe2iuwDmo9tsScwivxYraY5Fw60Ao5zXTOZXKAg11_6Zbr2oZ6-BZkodLGFGpLorlbhEJKZZOEeHTJfy4XEv_kemvCrVRrM6xkNqfRejHa52SQMhRVk2gQb9w9raouXmk65fdtY3GS_1UQlY4hXoYDnmx7nqbvmJigleA9MkNj4nwWAsX5LpzpxkiyMMzJAlz1H3P4jBR1FaMJRZLHoEy4-OmwzGmkPc8zFrqjCCmFjw6Hmt3G0BBhck8c81VcPl-pGZqETumwC5RjUg7yiZNByRScrh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=SxNbn42o3s1P1-BiP36DGvCICsfSHRD1mbrkxWXWWQKPJdqFHz15S1YeQe2iuwDmo9tsScwivxYraY5Fw60Ao5zXTOZXKAg11_6Zbr2oZ6-BZkodLGFGpLorlbhEJKZZOEeHTJfy4XEv_kemvCrVRrM6xkNqfRejHa52SQMhRVk2gQb9w9raouXmk65fdtY3GS_1UQlY4hXoYDnmx7nqbvmJigleA9MkNj4nwWAsX5LpzpxkiyMMzJAlz1H3P4jBR1FaMJRZLHoEy4-OmwzGmkPc8zFrqjCCmFjw6Hmt3G0BBhck8c81VcPl-pGZqETumwC5RjUg7yiZNByRScrh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🐐
نیازمندی‌های خونه هر مسی‌فن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99029" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
⚪️
#اختصاصی_فوتبال‌180
؛ آرمین‌سهرابیان مدافع استقلال که از حضور در تمرینات آبی‌پوشان منع شده، پیشنهادی از گل‌گهر سیرجان و مهدی‌رحمتی دریافت کرده که در صورت توافق مالی، این بازیکن بار دیگر به سیرجان بازخواهدگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99028" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99027" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bzr0OuGwvOv50IX7Z9pn5VXdPjkpD5OcNqdDk-qNLx4n50CIu5GljgPdSl-RcgJvGsCEZn4pj4ZeuQP7ni-kP7_HtYgqdMUgRJ5EgmgB_pwQ-Aza1tmH8XCu7vckuwQrmQxM847EMTkNwKoBgstC9QREPDld6BrQCUlwGVpAqVqEWRxVoC3YKbN0C4NrdctNduWcZYOMdBodmH596Vni-9usbU5MTCv9v9jBWmTavZ7ZQq6pbxLXT7uJ90VWxd6Bdv3Za3UUv26onNTQRKVmHxMlOYd0dwgBB991qhHAP-o5f_u1ImhJDNzLYdZTdu9Uu6FIZOO2U-vK4l9WHBPF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
جمال شریف، داور بین‌المللی سابق:
- تصمیم داور مبنی بر باطل اعلام کردن گل مصر، تصمیم درستی بود.
✅
- تصمیمات داور مبنی بر عدم اعلام پنالتی برای مصر، تصمیم درستی بود.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99026" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ2lQ6NPOhFbU3BcJUMq5I7a_5B3BJUSeSB7PcviSkR0k60paxCWUiOfb61F25SfJqB0WwlXObylD-lS-vlbaaYfAdxtHzNcMtXqexjzi56aiUepgHWp7c6WuK_hofIeTCQDMzlO7_avFJjiUfpx50VylJFWdHmgrCBPpV35DJ_8ga1xATUfvoWFTqonmp-6cuTxPzcNdk36pqKsYk_6bQAJvIQrKPc7eWp64fzcL6NXFz7w9SuZNPA2z4Ne4kWj3dw6JvGmkhqzLhc9Ii8X3mOLbTT_YVANR0ONEZq4XWiSkBFT77IE_et8ucW17G4737FiG_EPi-_HMcQTb1-HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
تعداد دفعات اخطار (کارت زرد) دریافتی تیم‌های راه یافته به مرحله یک‌چهارم نهایی جام جهانی
:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس: یک کارت زرد برای هر 7 خطا
🇲🇦
مراکش: یک کارت زرد برای هر 9.8 خطا
🇧🇪
بلژیک: یک کارت زرد برای هر 10 خطا
🇨🇭
سوئیس: یک کارت زرد برای هر 11.5 خطا
🇫🇷
فرانسه: یک کارت زرد برای هر 12.2 خطا
🇳🇴
نروژ: یک کارت زرد برای هر 13.6 خطا
🇪🇸
اسپانیا: یک کارت زرد برای هر 17.5 خطا
🇦🇷
آرژانتین: یک کارت زرد برای هر 22 خطا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99025" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=qcCSlorhrvzvgF2HZzyl7BHTVG9J0Rybp3nqfS4pouqxo5sup9cc7iZAet3XX1dbhS9V2JkA7AuW8dojUud5tx5MxJEKbhnMUWp7nGd8Wv3ekymZDoL3q1Y_eslD9TbCQPkwyeYURfbu0lnGjx8vUDqfwvRmkmTCY6JMv56u8mfCBZ9NUyyjh_Dynm0hggvCH_P4M8IMZIyi3ZQdPeL3IxkaOXk37evNe8-lUKhVoWnpL1G_S0OP0zrXC6M6FMh2__vrWol0TpILyTYntKDZf0H17PrOS0uw95klQzOmSKujJE7GpXdLVeSCqJv6bynVX-KmmSmiMvTz_i3DPbq_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=qcCSlorhrvzvgF2HZzyl7BHTVG9J0Rybp3nqfS4pouqxo5sup9cc7iZAet3XX1dbhS9V2JkA7AuW8dojUud5tx5MxJEKbhnMUWp7nGd8Wv3ekymZDoL3q1Y_eslD9TbCQPkwyeYURfbu0lnGjx8vUDqfwvRmkmTCY6JMv56u8mfCBZ9NUyyjh_Dynm0hggvCH_P4M8IMZIyi3ZQdPeL3IxkaOXk37evNe8-lUKhVoWnpL1G_S0OP0zrXC6M6FMh2__vrWol0TpILyTYntKDZf0H17PrOS0uw95klQzOmSKujJE7GpXdLVeSCqJv6bynVX-KmmSmiMvTz_i3DPbq_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره تاریخ فوتبال لیونل‌مسی
💀
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99024" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=JU8z50IGXz8PVYcZOIbgk0004isHYAQ3e0PeK1wy6YXXVm04SE9YVWr-7Eiye7y3U2A6puqwo8EE8GNla0wuu4nHe3YD4vbF4dsUBjnp718-e9DEIB9ivqXCl0iJG8arOi54-9FxRp_ooX5KL_eAEAQ5ebQbRSIUayWeIlqON6a9hHTzqGjfgU-GrYRZ_VQ9IrFCMaRy99zckfWELhCd95kjHQ7JWmgexqnSEt5jGItn--Z1CzJVL2S_urE4xy2gzQUOT3cCy0oS4ZcGGwPVKRe-yDrq8DE7-ZLVKPILiuWPUXL19fRrPtEKGrxm9hsLZGS4-qFrbz8EQUcqZh-Qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=JU8z50IGXz8PVYcZOIbgk0004isHYAQ3e0PeK1wy6YXXVm04SE9YVWr-7Eiye7y3U2A6puqwo8EE8GNla0wuu4nHe3YD4vbF4dsUBjnp718-e9DEIB9ivqXCl0iJG8arOi54-9FxRp_ooX5KL_eAEAQ5ebQbRSIUayWeIlqON6a9hHTzqGjfgU-GrYRZ_VQ9IrFCMaRy99zckfWELhCd95kjHQ7JWmgexqnSEt5jGItn--Z1CzJVL2S_urE4xy2gzQUOT3cCy0oS4ZcGGwPVKRe-yDrq8DE7-ZLVKPILiuWPUXL19fRrPtEKGrxm9hsLZGS4-qFrbz8EQUcqZh-Qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
تو یکی از لیگ‌های سطح پایین ترکیه جوری داور رو کتک زدن که بنده‌خدا نای بلند شدن نداشت
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99023" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇧🇷
فدراسیون فوتبال برزیل حمایت قاطع خود را از کارلو آنچلوتی اعلام کرده و این سرمربی کهنه‌کار به فعالیتش ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99022" target="_blank">📅 12:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=J8pNtpGkSRtwLHvHf8p0pVjXrAiAji12C0TLaGj9oPnenzi7CqDsPFudejjYYR2IzUknNUOeCEEQHh6CutIVpPXecgwmLC0KYiCRbpNu9rfJxWWunz04Wd7XmRm8BCodzEeIRiAOHGz24oXSP-eLemzSCP1sr3PwNIUcieohg0g90ggQyq439hCM3ycG17MA0TWn3XoyRPC5jaaR720bZkQNknxN4ugUXEJCQ-bcJteru72QTDE15Va0SoLLAb9aNan9ROPQU0KNV5mLBai81adJCibGFwx1lZCyaNQ4lS3IFiJLL-EpaNidVrIJ-9adB4rMfsNqCFHrJcMUodJj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=J8pNtpGkSRtwLHvHf8p0pVjXrAiAji12C0TLaGj9oPnenzi7CqDsPFudejjYYR2IzUknNUOeCEEQHh6CutIVpPXecgwmLC0KYiCRbpNu9rfJxWWunz04Wd7XmRm8BCodzEeIRiAOHGz24oXSP-eLemzSCP1sr3PwNIUcieohg0g90ggQyq439hCM3ycG17MA0TWn3XoyRPC5jaaR720bZkQNknxN4ugUXEJCQ-bcJteru72QTDE15Va0SoLLAb9aNan9ROPQU0KNV5mLBai81adJCibGFwx1lZCyaNQ4lS3IFiJLL-EpaNidVrIJ-9adB4rMfsNqCFHrJcMUodJj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
لیونل‌مسی با این طرفداراش محکوم به بردنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99021" target="_blank">📅 12:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99020" target="_blank">📅 12:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENIITlLlJKaCoFOkCQGDtRy41pVhMBTtrurPTFIDKq57yk2jaT-NhikpNR8EXAtPVwGuFkkBnlDKPXPzBa9AEA3Avi7OVLsq98VBbUGWxRee1J8tj2dlDdlahGIzatLyxP3bOtw6m-qDJD5yuDy1vgvOI7MGm9zvwXz9x3sbDQUqXtiCcrWyTsquhwYoLNPd4cTvCUbbkDyvje8UXcYPwUPiaH5IIZZ9c0iTWy8ZxSY1wAXuDXd_WdugZTJMe6dbAPqvvraQdIl-UBeFFquUU20afRc1BNuAl0dO8PLc0NdnP1O2sKn-KlbrJwuIaagN4vkhvAVTm3G4b0GD-EKIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز:
منچستریونایتد به اورلین شوامنی پیشنهاد قرارداد پنج ساله داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99019" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOnKuG2utZDmdFxMlIDkfnRkRH-GlBEDsQQjbF6QowDB3x-7IWBReSt9KDzO2sG1p7ey1e3ahnDTN52YI5GJqnnKluIxdvM2Qw_Vn1OhDginPGiOk6flfZgQ4Wq6VnLQ1RQSb6ldnaqgQUHNXOM0JKyXK5lia-J2_v2hB5XP9nZ69qQLbfXs2YdjqBid2a2kvqZehO9KmRBvY7eeoiTdbWCV-2YwK-HTfcHsBIghj1xnYo5S5Rh5UAWtR9n6V_zjQzQ7lmCFyXA_NEtXQseGWl0Tz0cu4SATHtJ_93mSTaW7DiJ6ugPAZF8f3sAUdSxEYgoengNTNKe9WzdMsBbq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند
🔺
مصر شجاعانه بازی کرد و باید به آنها آفرین گفت اما این سناریو مانند فیلمی است که از قبل نوشته شده و برنده داستان هم قابل حدس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99018" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYEtGnJ_5lg17obi0YEJt7FinufdCql4awRP-uHoSLh1Xd1fRbwi-VDhEAoG_YRx515ZvxvAt_zM2R6maSTtkCogT7y3NTp7WL4mDMR3_Sd7_9kz11TCXaTBEM5de7T3Ezvurc2oj9M2kS959IQ5urBJ7pNcxVHebVsppuha5usRr1SXf5azxWH9TeSKg5rvRCbUxitfPm_FwHba5NpscIxLWxx2r3AXCMt7cYqFVlZpCogpCSFdjA1mcVQR10ayuIICy3uXvj49gRDZdnz4xpS99JtXF4-7qQo-7aL4y29i5R_u7oJKFkZT8CXHu-P7Bhs6EPk6Qsu_RXF8I9zcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99017" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: تصمیم برای ادامه مذاکرات را به کوشنر و ویتکاف واگذار میکنم اما از نظر من دیگر تفاهم‌نامه قابلیت اجرا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99016" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99015" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/99014" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد.
🔴
آن افراد بیمار در ایران، چیزی بیمار در ذهنشان وجود دارد. آن‌ها بد هستند، من آن‌ها را دوست ندارم، هیچ‌کس آن‌ها را دوست ندارد، آن‌ها شکست‌خورده‌اند، وگرنه تا همین حالا یک توافق به دست آورده بودند. ما رهبری اول آن‌ها را از سر راه برداشتیم، و حتی رهبری دومشان را هم. آن‌ها افرادی بد و بیمار هستند، باید از ریشه نابود شوند، مثل سرطان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99013" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J57A29XGKfpUATq3ZCXCPKi1QFQ0HkgeBNm0c9WjKG9ZOTc-dcxlWh554dFafe1JvtIWXIgVvXeXatZIDtLRW5RZUsyLijhZ_eN6L0YtWQhYBq7CT-8oK4vN2NbVWH6sLsQTwVDmSPgf1EVt1-4964ErSGuYZzeIdJHbkfTqw8DemhxLFwDvi2KIzwv3dkNpW3heD0gmwBQoDIovlzdZ8-8S41j6doWxFzOvy7Hq8lg4x9qX4WspGyvSRvFh3uo2mfNSLqyx5yMkJNi6mX8U_0bLYjGweeWa8NEdiE1JTYC3ZBVqftb9wQhTLAqRZzb30FLGYeylfUHlvZI4Jk3Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیک: رئال‌مادرید تصمیم گرفته که در کنار داشتن کوکوریا، آلوارو کارراس را نیز حفظ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99012" target="_blank">📅 11:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv5umIhJ1oy_hjT_3oTmSMWs7yDXQyaytFNiV_1GSkanFVdRgUwa1Un3N7sU1htsz7THXh33oEFL8qc9d1o7YM8fcwRzwL-ADUApVgTB5nTpltOnmx446V1uKO2HOvZ1rki2gRQXO27lOzy7s9aOViwgyjE0sdGGlCuAvUfKQ8xnVYi6DVpUhbNDlylXwC43v6CDMgh6LguiNdnF6ozeAXBUJaw7sRuMMQbaKsX9dkwgxnrHgiWo52i2bjzJ6i79fVbtJaJQ6_nRspBCjE6EQaU-RTtMOqAbRvlES_ppbPxzGrkNr0-be26sXq_AJGTFTb9ppt-VhA1lAtuBNjzPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99011" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99010">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37082570ef.mp4?token=q8mYBlNxmMKh4ZseUgkmhYekRQsGZ_Xk7nnWkCDybscwVYlMV7tUGG04vicv8q8hUPYWSfWiPo4qnQUcwQDDfFxZQ9Q8Iyx_lSkBXDaO04CYu4L2k9AXSR7SIIy496e1bk6TuxelwF1uytexm76EsZ07jKSDpP_-QKa8PHGHgsJJQNdLopFI3GDBxRsMftqIs9Fcy_rcUqNe5zJOQZaOpSKT9sDM8Tbml_09FNap2sD624PxLKxRJbaYQNN-jIsNVRYZ3kVXhO4LsyW6QESrJnCSr9sb7ajZM7sVTQYeRRL0L6fwq7ftvCf7mJ5R8rf1N-aYvrV_vIlhJ_lgWgFDXGH4leMU1P9nI4Izs0ahRStF-88_fNDWcFdQN6AQEYd4Dr6rmQGS8ohV1Wo7LeDRqaX5oNP8q0VkDeFTrDQYNeO3bH57v9hTFqo4EhkwLPnfOcKRQHxsJW90Iz-5L-IdZz47jMdgQDAMe3V-CNO6cOSwvnJv7vQpqFpZemOOewRgD3sCK3cpsHb_p8cDHHUGtFfY8tqtgX6OuEWMOhHhTit4QKRZkMu5-GCO13a5np-u4swalJU8OGOVjWnllTTm6CzIPlaw0OGSO8C7DWgXLMmUWOHbrZaCgiRY8k4YkWj4Y_zqJpA28RpaZaZokJR4eIZupKW6NbgwNWdI2r_aTeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37082570ef.mp4?token=q8mYBlNxmMKh4ZseUgkmhYekRQsGZ_Xk7nnWkCDybscwVYlMV7tUGG04vicv8q8hUPYWSfWiPo4qnQUcwQDDfFxZQ9Q8Iyx_lSkBXDaO04CYu4L2k9AXSR7SIIy496e1bk6TuxelwF1uytexm76EsZ07jKSDpP_-QKa8PHGHgsJJQNdLopFI3GDBxRsMftqIs9Fcy_rcUqNe5zJOQZaOpSKT9sDM8Tbml_09FNap2sD624PxLKxRJbaYQNN-jIsNVRYZ3kVXhO4LsyW6QESrJnCSr9sb7ajZM7sVTQYeRRL0L6fwq7ftvCf7mJ5R8rf1N-aYvrV_vIlhJ_lgWgFDXGH4leMU1P9nI4Izs0ahRStF-88_fNDWcFdQN6AQEYd4Dr6rmQGS8ohV1Wo7LeDRqaX5oNP8q0VkDeFTrDQYNeO3bH57v9hTFqo4EhkwLPnfOcKRQHxsJW90Iz-5L-IdZz47jMdgQDAMe3V-CNO6cOSwvnJv7vQpqFpZemOOewRgD3sCK3cpsHb_p8cDHHUGtFfY8tqtgX6OuEWMOhHhTit4QKRZkMu5-GCO13a5np-u4swalJU8OGOVjWnllTTm6CzIPlaw0OGSO8C7DWgXLMmUWOHbrZaCgiRY8k4YkWj4Y_zqJpA28RpaZaZokJR4eIZupKW6NbgwNWdI2r_aTeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این 45 ثانیه رو ببینید بعد بگید هوش‌مصنوعی خوب نیست و بی‌روحه. خاطرات زنده شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99010" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99009">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=r5w7p9tnJ4BIW08YAbi6QpFOKr39zd9nG8H1yISk-bAA5S4EIwSBAqib8hYbJ9I3Bxgzs4Bi_AINPDjjFD6Onkqq9ccGXSO0n-2-FdSQZi5mV0pMl5xstCAOIQG-xzMBWzRoa8YjKRln1EzvOqCEWaF30oi8dcxAyv9pxDCd_48fe2Q7TcBL5xjdP4W-aZOqcjK4Tgog3jV51mIM9SxBQUB786ea1veJ8STILtZ3KsP9JBc4HYJlEaLqfsdwDGQx5Tzi4RW65xhSotjrCEi7l5mSqCOAKkWju0TdphOzaTAAFEkx-NCNMgFyDTYsY4KHiCOVjMS_rHYDiOB5ZNi3WZNAIKgfGdNAIBQDHEnovxfRXAOWhsXEjkDjaAJ7RvXf145JtqwRvWHSI-caMEDQIuXXKx1Fs8weq4lNv7JwH8ElaDGmfn2Sm4LHfn0YkQUDXdq6DqfG75AibLZoNOthAneti8tR0XX-Tc790SEZFo_Mi9h9URI4QUj7-fTIEFZM46w7-7ZW9RkEt43DJo8hXX4XyUEfSNsB1sc1d5wDXBI73w2NNCi55ru2e_WKFx_PhoNAG2DqDpUHVo7vO9wugUtr4wezrM0jelk44HWjEopqFQK82lYQqfvGUsyH9HOtGtLqIhxH7_7tQ-GKiwbwkvM-jQZCAVBNcC1htZglkJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=r5w7p9tnJ4BIW08YAbi6QpFOKr39zd9nG8H1yISk-bAA5S4EIwSBAqib8hYbJ9I3Bxgzs4Bi_AINPDjjFD6Onkqq9ccGXSO0n-2-FdSQZi5mV0pMl5xstCAOIQG-xzMBWzRoa8YjKRln1EzvOqCEWaF30oi8dcxAyv9pxDCd_48fe2Q7TcBL5xjdP4W-aZOqcjK4Tgog3jV51mIM9SxBQUB786ea1veJ8STILtZ3KsP9JBc4HYJlEaLqfsdwDGQx5Tzi4RW65xhSotjrCEi7l5mSqCOAKkWju0TdphOzaTAAFEkx-NCNMgFyDTYsY4KHiCOVjMS_rHYDiOB5ZNi3WZNAIKgfGdNAIBQDHEnovxfRXAOWhsXEjkDjaAJ7RvXf145JtqwRvWHSI-caMEDQIuXXKx1Fs8weq4lNv7JwH8ElaDGmfn2Sm4LHfn0YkQUDXdq6DqfG75AibLZoNOthAneti8tR0XX-Tc790SEZFo_Mi9h9URI4QUj7-fTIEFZM46w7-7ZW9RkEt43DJo8hXX4XyUEfSNsB1sc1d5wDXBI73w2NNCi55ru2e_WKFx_PhoNAG2DqDpUHVo7vO9wugUtr4wezrM0jelk44HWjEopqFQK82lYQqfvGUsyH9HOtGtLqIhxH7_7tQ-GKiwbwkvM-jQZCAVBNcC1htZglkJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇮
کشور شاد و بی‌غم فنلاند یه مسابقه راه انداخته به اسم حمل همسر که میتونید ببینید
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99009" target="_blank">📅 11:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99008">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=QHdmALx909WJX0FQ4zsngeZk2lXwGmEFasHXcVU8y6JN5gefkpbO2uWyhx3-WGtde5n5ov3IrhQtuXAdzCj4ou5DljRWQtFFnhbIlOGswkP2rx9eUGVhhO1kUU6k4xsNuSlYZWXaw4iKyyxs44d6XMVhpRcVZp0TPN1UKNQheGZ5r9J3Xx1N8Q0q4nqlZ3VsaPnPYglt_Mi0RoXWdAQdmCMcSWRDlRnWxj4CUvwAmztBJQ3oAEFIErIXlJTBvqgLYQWI75qWdP9z712YpCODYv2JeF72IJr61r8wl0YL-rcyvet2ekfEkibjmmSaEqkICnjkUwcZ2WwkRVB6LhwzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=QHdmALx909WJX0FQ4zsngeZk2lXwGmEFasHXcVU8y6JN5gefkpbO2uWyhx3-WGtde5n5ov3IrhQtuXAdzCj4ou5DljRWQtFFnhbIlOGswkP2rx9eUGVhhO1kUU6k4xsNuSlYZWXaw4iKyyxs44d6XMVhpRcVZp0TPN1UKNQheGZ5r9J3Xx1N8Q0q4nqlZ3VsaPnPYglt_Mi0RoXWdAQdmCMcSWRDlRnWxj4CUvwAmztBJQ3oAEFIErIXlJTBvqgLYQWI75qWdP9z712YpCODYv2JeF72IJr61r8wl0YL-rcyvet2ekfEkibjmmSaEqkICnjkUwcZ2WwkRVB6LhwzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
تیزر تقابل جذاب انگلیس و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99008" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99007">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYPZa6H7UeYXF0fopgDOwPU-7XT-SYQzAaE0J_qw34-1qHwoxKeyQS-Cr5mtxtKXl9sd-SrmR-H1Y3BdSSZOC4RLn7J0XLGUAqE429ancOVItC_F2TJ5OkvzVNG-Ljr-AUSCVewQKEYKr8v48PWJq7x8tnowgFqj9gyHwyPeGaDfcSmej1oEA2SpKh3pa9Ld0_RawVk29fxAaEnEW-qUw9rQ8QBWEzf4r7OX71uSezjCkCch07YcOkxMxTPa-nPxANuV2boSKk8WagmWQNxWhqoEYH7xeJd00ACClrZsB6PEef-Zum4foJ9mELZLdIOJZdL4BzbGmE2St_umfBioZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
♨️
مونیرالحدادی ستاره استقلال در آستانه عقد قرارداد با اتحاد طنجه مراکش قرار دارد. این بازیکن که با آبی‌پوشان یکسال دیگر قرارداد دارد، به استناد به شرایط جنگی ایران و بارداری همسرش قصدی برای بازگشت ندارد و احتمالا با توجه به تعلل مدیران استقلال بزودی قراردادش با تیم مراکشی را رسمی میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99007" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99006">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99006" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99005">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=t1HjxV0HjxFQFiXHCmAH3RFzRiSx87p0EvFH24NMp_8UZGrrU6usPhjWZnU5zFgpQ98shUm9Lj1oxaKGWF52-XJat9Vn_7LHh1oAmnaPN9QfQQqFSqAq03EELXZ0o4v0fTt3is3IiVtqCYRD1xR3peP08p9qrlZDroIOHs37IN0a6BXAHTHvy3zz_Uh2VaAF1dRAdWlm1ZYFCQ3cGrwIA5Te9e6vLPmsOlz1RlVA2PNWDoXCHLTDihkgEaI3y5VX-EsA1-KK6m-PaU4ymvsKFIpyjHkWXYSXIdGCTxiXHCk8C1o7lkcReYnno11nk8KAAIe1e1b8kNZK0yuYlkdQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=t1HjxV0HjxFQFiXHCmAH3RFzRiSx87p0EvFH24NMp_8UZGrrU6usPhjWZnU5zFgpQ98shUm9Lj1oxaKGWF52-XJat9Vn_7LHh1oAmnaPN9QfQQqFSqAq03EELXZ0o4v0fTt3is3IiVtqCYRD1xR3peP08p9qrlZDroIOHs37IN0a6BXAHTHvy3zz_Uh2VaAF1dRAdWlm1ZYFCQ3cGrwIA5Te9e6vLPmsOlz1RlVA2PNWDoXCHLTDihkgEaI3y5VX-EsA1-KK6m-PaU4ymvsKFIpyjHkWXYSXIdGCTxiXHCk8C1o7lkcReYnno11nk8KAAIe1e1b8kNZK0yuYlkdQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تیزری جذاب از نبرد مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99005" target="_blank">📅 10:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVpUuOghCTio3QzCdpka0B71VeVDzb5b7dqeKgiATHh4q_1PCqwYQDq53vXwcb8BSQHpdCpAeHTeMcXPbLdG_DLq2_aeEPmSs-GQHzFb5HTvO_IJGhEdM5lG8Ai0_jgSifaOMfEBAuGhiN9iSyaQWUkJ05J_ovs1xF3L_IAbfbLVkN1GYvNcUClYQ3rDiqn8lQLQ2oUfMzG38AVIkJyn9p-gaBEX8qRVmEjIbN5MhvDWnot513RTdTq122S-4_oBvXRbWmFpwMMD-MtP9axkWNW4mn1SWPAH8A-KFV7henwSjWKauGOEsGnkvJBUtpM4LJCG6wYLpW_IfnYXwhgL3X4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVpUuOghCTio3QzCdpka0B71VeVDzb5b7dqeKgiATHh4q_1PCqwYQDq53vXwcb8BSQHpdCpAeHTeMcXPbLdG_DLq2_aeEPmSs-GQHzFb5HTvO_IJGhEdM5lG8Ai0_jgSifaOMfEBAuGhiN9iSyaQWUkJ05J_ovs1xF3L_IAbfbLVkN1GYvNcUClYQ3rDiqn8lQLQ2oUfMzG38AVIkJyn9p-gaBEX8qRVmEjIbN5MhvDWnot513RTdTq122S-4_oBvXRbWmFpwMMD-MtP9axkWNW4mn1SWPAH8A-KFV7henwSjWKauGOEsGnkvJBUtpM4LJCG6wYLpW_IfnYXwhgL3X4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
لیونل‌مسی ورژن جام‌جهانی ۲۰۱۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99004" target="_blank">📅 10:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99003">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
❌
با اعلام کمیته جهانی المپیک، تمام تحریم‌های مرتبط با کشور روسیه لغو شد و این کشور میتواند در مسابقات مختلف نماینده داشته باشد. بزودی فیفا هم معافیت‌های مختلفی برای روس‌ها اعمال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99003" target="_blank">📅 10:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99002" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=AUM8t6Yu4cuDxkcxGWxLwH6fG6lDpkonBsus72VKsJu9rXvcYQdk0G15f-qx34gWvMTz6QoW8OajyGmi7k5fhwk6rDQFvBJmGpxgqYgBbUFuHH4e_fuwq-w4upyZ6iUtNKem2ISMc_XPH36QEjyIrZ0ZrxS-iUOrmQHWJtR-ddzG52ecXy_YZKZZrO71Mx0ON0g_Xzy2MTu713XAzikKadswlrDBHCxU-Zmf-KtPMyEpH5p2hjMu9iPkQi_SyEIgMk1uyThAK21A5K-oOwTyDUxBDgYgPl0mvr9xHAX7cy7sGgfjqhCktvoQ1LCJoSHR83cClQUOVlHBBLuqkymmRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=AUM8t6Yu4cuDxkcxGWxLwH6fG6lDpkonBsus72VKsJu9rXvcYQdk0G15f-qx34gWvMTz6QoW8OajyGmi7k5fhwk6rDQFvBJmGpxgqYgBbUFuHH4e_fuwq-w4upyZ6iUtNKem2ISMc_XPH36QEjyIrZ0ZrxS-iUOrmQHWJtR-ddzG52ecXy_YZKZZrO71Mx0ON0g_Xzy2MTu713XAzikKadswlrDBHCxU-Zmf-KtPMyEpH5p2hjMu9iPkQi_SyEIgMk1uyThAK21A5K-oOwTyDUxBDgYgPl0mvr9xHAX7cy7sGgfjqhCktvoQ1LCJoSHR83cClQUOVlHBBLuqkymmRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
دیشب هواداران آرژانتین برای فشاری کردن سرمربی مصر با پرچم اسرائیل تو ورزشگاه بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99001" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liMg6miKno3k0-0uIxAwdu0YKuphHOAMQplrQ6aj20N6gfZfLRAmlsFMwepyIx8PGkEmjW32qHxMycVZwfnw0zFi-ZD2rkIPnpf3abPYCyed8upMs8iDPhmIEOasWMNp1FFmmzZV8rOiV6dNPavDsLN-p5EBLvfBDpNk5vSxaRjth861HMd_39mzynAivgQpKmX1iiQGVZLXu2m1bDknUNHgID9UMSeg2EBW0dfA2MHnfuBaPVbov8wUjJqk9D1BofJZcaJ_c95qPjeVvIQzg9KoSrfFNfVHM769t_EC3WN_hii_RnWpJ9IQHXu3mMkPkUuQry274mqGbNkDKrt6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🏆
🇪🇸
مایکل‌اولیور انگلیسی داور بازی حساس بلژیک و اسپانیا در ¼نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99000" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=YOTnI7vOWN0HkyNEuc0AQ0ZZewl8XNfInCKVqirmERt1ychMLdy8cJg-IAThhBwsFHolnEDCt3B3F0QeE3FnKenV2-FBvvjcxT29Rk0PQ4pAMQRPWEMGKFhow8tJVK4y-6UkUmQZo6OBFNQw4Y2LlYuxwzsoaYzStvy5tIU-lQFtZCBVCt_KNdRVStp5qEz-huhubn_BXELmkLox6UGiOapLsY5C475E9jM_L9bgAmt8gpAEx7FwUOzQrNxG53VATgCjHW6yMlIHwP4NVd3qAjvzBWzlJX776vn3FWlmNLP5VZe-zGCBwddb2gtwp9ALbBssgHAPlJ3kPjBZXePWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=YOTnI7vOWN0HkyNEuc0AQ0ZZewl8XNfInCKVqirmERt1ychMLdy8cJg-IAThhBwsFHolnEDCt3B3F0QeE3FnKenV2-FBvvjcxT29Rk0PQ4pAMQRPWEMGKFhow8tJVK4y-6UkUmQZo6OBFNQw4Y2LlYuxwzsoaYzStvy5tIU-lQFtZCBVCt_KNdRVStp5qEz-huhubn_BXELmkLox6UGiOapLsY5C475E9jM_L9bgAmt8gpAEx7FwUOzQrNxG53VATgCjHW6yMlIHwP4NVd3qAjvzBWzlJX776vn3FWlmNLP5VZe-zGCBwddb2gtwp9ALbBssgHAPlJ3kPjBZXePWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتین به یک چهارم نهایی رسید.
🔥
🇦🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98999" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYoXSI__zPEJdeeuZg96-q3Qu8cv4ob4AssPuykjxcpGP7tHxzazeTtS78p1tdjE4-j5aKcQWnnDay3t__60gCH8Fx-lvkO9Gkfsl_WA0hhlcrsMj8QvpOmD1CywGwdazjt_-hwPkhCl2_AyJOIMGDNtAo39mRkq8ndjfMX7x5wBoRlYke6VIRqKls1P0wmXFv_7jzH2To0g5IKdItU025AHCzfKlRb9AqYwWLrYOUCgEoX-eRUpB9hZ4W9ryEJZWuRVFStzGeF5VCoq-KDp5BYuHFIJ6DPlwHnW5auAWmezNQkGx2RpoS_9aeirsusU2WC5ZCyeeThdEbhUZ9lE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO-GlPESKAk2oG3sX-xzVRNI4YY1NbWDDCynVrj4mARlJ9C8dU1rak922Tj4U7Kcrfse6S1LvsZzkbWjsU_ynMhtKID1UPOhmne0DwrFmxPHBkZUctTUO4Yyl58NuYTkiw55vsbjkG6X1Xia4N5OpMy8NlSm16WrCDNQAuEwU7S0PNTlLT9qNC2YtdBNmJLhkV2ImQjCmG9qy00Fjpyl0bDFRGn0qo9XQ2amuBN3HmyCpV7dsUfEaSJLg2ZTSKq5s1QQriS94Uu0XDn1FDqDmFb9Bsed50kK2j0FviMyF7atWGUJZkpANokJGTzzu_MxK6piv-t2cJT_lLL_2qsLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای خیلی از پسرها، فوتبال فقط یک بازی ساده با توپ نیست بلکه پناهگاهی است برای فرار از شلوغی‌های زندگی، جایی برای نفس کشیدن و رها شدن از فشارهای روزمره و فرار از دغدغه‌هایی که شاید هیچ‌وقت درباره‌شان حرف نزنند. وقتی بازی شروع می‌شود، برای دقایقی تمام نگرانی‌ها، استرس‌ها و خستگی‌ها رنگ می‌بازند و فقط یک چیز اهمیت دارد، عشق به فوتبال و تیم مورد علاقه.
🔺
فوتبال به آن‌ها یاد می‌دهد بعد از هر شکست دوباره بلند شوند، امیدشان را از دست ندهند و تا آخرین لحظه بجنگند. و در این میان لیونل مسی برای میلیون ها نفر از مردم دنیا شاید بزرگترین تراپیست دنیا باشد. برای خیلی‌ها، تماشای بازی مسی فقط تماشای ساده فوتبال نیست‌ ، تجربه‌ی آرامشی است که در کمتر چیزی می‌توان آن را پیدا کرد.
لذت ببرید از سالهای آخر بازی مسی
🩵
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98996" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
12 سال پیش در چنین روزی تو جام‌جهانی ٢٠١۴ یکی از تحقیرآمیزترین نتیجه‌های تاریخ جام‌جهانی فوتبال رقم خورد؛ آلمان ٧-١ برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98995" target="_blank">📅 05:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts_t-3jn8AE77OezH-NUFGBRwDBYUx-H_KBGvmfauHA3M_-9QTGGveChhHmr-3uRh9R4fE43LA2Py7qh8ugMHb0OAbH14XYnPDMbvhxaDD4asAMK2ITq3_Hc1xqmNxfm4ND_tC0CAT17v0AzzltBcYtgdQIAXds2AeGm2T0S5FXrzAN8uRlpC-50ziTzPu6KUldfLs8PpkXUYJn4gJiB4z-c7zAEWK-qkcxlfHIUOYyeBF9MmP0Y0V8rni9_3thtQnc0upEqJ-LxiQYQielzOL5k8JIOLgYKQBFLRFDvK3N7JtEZGIktBJt5zUbrm1AoEXJ9MkjEehleux4JWae8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
💥
لیونل مسی:
«من گریه کردم، چون احساس کردم که هم‌تیمی‌هایم را به خاطر پنالتی که خراب کردم ناامید کردم. اما خدا برای من یک اتفاق ویژه دیگر در پایان این بازی در نظر داشت. من خیلی خیلی خوشحالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98994" target="_blank">📅 04:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1z5eXfMKK2ChUj2C2lSCsNO3oDwqlbXg7caO3Rc32ePmij33rwzCczciHjw1nDONO_Iuu3K5bj9zDJGRPdUlpSj2yHFoQCr-1CgqHPS5dYJgFCfP6AAGBYo2w5PoGJiJ8mvGet0yJXh4UcplFjzb-felipU2fJ3RsEtV8LykIw5-fcQYya3xqM_Nn_LfsCx96NKy1frrlnX_EkAl9hjmZKAXSmYF73zhKULLAITbaSVv7aXIYhG4X_uTJ3OavGLcWMyG1UZjmWnEZJzgUIQGsxgPDUuAhTIvFpWtMcj91WEbzZ1xQyUTvd9Z1bxNvKXFQsnWFFAjQ72HJ9T9eRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC4S29JAPm5tbH9eQ4nhs01MNq4rMiw96GpM-5maQ0-CmkswXFiSnpFEoYwvu47CUhNMNSYWS843NghNaS6iE34qeQ_3FtjDvA7FR8c76eQsaAlbmYOYhFHEtmKjhkRk0GLDYO2V_CywoB13j1CXffwGlf022GAs7RYf-m44khv5tUZk3obv7TJW7N-5bBcP5Ebp2F-USeOX3gE8cIpyag_5w_Wvtbdaxp4S27eoIMiyH54HFxkbE6RSUKDiOpbgh6-H3YbzOQB6oGqu332tfIz9JLuCsYf4MdhIUnMPjSclRKxku2LeOPpaALe0W63SlFIbpkp_HNc7Djj_ILRPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRCueTDZ6mhvD71_WPCHlR8y6raQ09lqePIrxFhO7Tx1L_E27UKEXZKW2p0WsiNsS4UxnqXO5B_Jq3K0K5FSAUHsn5zxbMi6QkjeJjUAX7q2hz22_c7mWDOBljbDZ8S4nkOLbpoO3j-V7ySwRr7W7Va57fvAWD-c8FDWwepsCtNphzt_bMwp9je4uD9lAHxUPL8UtRygSOHogBgdo32p2EGR5Avp1xVa6nQyyifV9uLbDCcyFXsraqQqloz-TrJne_CJ4B4toOh9yqw0eiOStkDdcOYOYKUxK9bTOiyh404QjG-sli4zlguQla8i6-U-sKbgq0hTo0zHPVS5A2gDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ezmqXtubYyJSDIu7UnYDih-u7dWHfOUv3qlWls8imJK31TjYdc7xiVNuVUbOZ_ZKkdxBKvxQBlsDEvJVQPyQ-2fdtncWfSaYo7tvtSgZsHxUMOybdg3D5kDsN4inBPV211bFfSjjdy5F-pU7-N_yLKE7_HmEB2dxouVn8TTP7mnIAVGqLn1fLLF1gP7R7eqfWjv2B0WTKc52BfVWfYRBwqrTs6XbF00H0kRWZ5Dqq86gcdgwDBET_KmqFx6yTsCPolvf4ahxyxeSOc2lKBdnD_1tWvBhgtaGKaex0sIRYMStUD3Mi0-G_3E4zJ5heQ17t3IcF2aZPaqOeoBJ2TEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کلمبیا نزنه حذفههههه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98981" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/Futball180TV/98980" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگگلگلگ سوم سوئیس بالاخره شددد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98979" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98978">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/Futball180TV/98978" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پنالتی چهارم کلمبیا و گلگلگل سوووم نشددددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98977" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/98976" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98975">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلل سوم سوئیس نشدددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98975" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/98974" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگگلل دوم کلمبیاااا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98973" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/Futball180TV/98972" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلگگلگل دوم سوئیس</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98971" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/98970" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگگلگل دوم کلمبیا نشددددد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98969" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/Futball180TV/98968" target="_blank">📅 02:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98967">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگگلگل اول سوئیس</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98967" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98966">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/98966" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98965">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
گلگلل اول کلمبیا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98965" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98964">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/Futball180TV/98964" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98963">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
پایان بازی سوئیس و کلمبیا
بازی راهی ضربات پنالتی شد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98963" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98962">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsCLW79Rkse9LV-2uzbMkNc_AOjxp1iZzZZgQ82SzM1NBNqXhFghdvta_vazzUFovVTXQ2sq9WVSuUnbuDx06vq76WooWlIyMe-NDOWRYmIAlfYFp-E4Irqz2MCZL-q__4Ps5zFaSv9KudKel4kqo6CJFQhIdJgkxC6Y_tmiD9LrumoNOKyKh7f67-vNSL7npsbh_rxGC_bfyCaz3EUdWuIMjhcGIY06qTWGomi6CQuE528aZMBsthEtgqDEsDjiV4j1NtssCn5nWc47M5NT_TzunuvZ45GaWOPeozpVYB36vWDqZ00rtwJlRjmjI-jVyk6B9kZuqr9uslgdWpbx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلمبیا چه توپی نزددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98962" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98961">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارش‌های محلی از موج جدید حملات آمریکا به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98961" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98960">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ گزارش‌های تایید نشده از آمادگی همه‌جانبه نیروهای سپاه پاسداران برای حمله به کشورهای عربی و پایگاه‌های آمریکایی تا دقایقی‌دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98960" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98959">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وقت اضافه اول هم مساوی تموم شد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98959" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98958">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=B3H6jPEj81fupYIFmd5c-BAEhdNgpc-DDobQbjsVjurF5IOVAA5jmA4IFZGza-0X79I1lUifxqkDw-2lGQm7dk2kAPsbR1GLAteJYDK0xHDZEnaQQyRtxYstXQKjL5Z6gWMBMRRUZL43TP_vukvAX3Q7avle4qJNnJRG0YpMz0ZtKY5q-ET3GI-iqqVxat0jP5-3LoX8OdwjUn5BEWDLvmlZomz3wQOOMW243Q0prVrC-pMKQOSvxoF0AYSTHNlpLUUgqB3stuHxTWQE5EInLfgg6PuAG1r7PiHXo0mmFBYcQNcz1qiWqnXFgfPIOwRAxjF1mLiyhNsZQhVAqv53YaHH1Z2_nOfcvn5SDQ748FHejhOdJ_VfhMTwyJP1JA6H8i7ngBFVg6-401oFn467L48roWn2mE0LjkhFL-iVoala9RDIQQ6_EuL3yR7RtjHlC_hHIQXukLbIZ4D19rUN1wE6wNIU0OE1aUw2WmVXJHoL_MvICses84FtCOki8DcA_fh7QaAxiKg-Gxg68OekXxH1TeFWtwdrX0BmaM3-s7krvxNeOqBUn1QPvxayfZa9VHqN8lf8KKThzCqQwwa0s1dTF4xGl1LkcXtEg6yCjYfsXoi_icSkZGztlnBp57h1y3KC4irXaQqtHnhgZink82AntftKg-bXAajO93gr7as" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=B3H6jPEj81fupYIFmd5c-BAEhdNgpc-DDobQbjsVjurF5IOVAA5jmA4IFZGza-0X79I1lUifxqkDw-2lGQm7dk2kAPsbR1GLAteJYDK0xHDZEnaQQyRtxYstXQKjL5Z6gWMBMRRUZL43TP_vukvAX3Q7avle4qJNnJRG0YpMz0ZtKY5q-ET3GI-iqqVxat0jP5-3LoX8OdwjUn5BEWDLvmlZomz3wQOOMW243Q0prVrC-pMKQOSvxoF0AYSTHNlpLUUgqB3stuHxTWQE5EInLfgg6PuAG1r7PiHXo0mmFBYcQNcz1qiWqnXFgfPIOwRAxjF1mLiyhNsZQhVAqv53YaHH1Z2_nOfcvn5SDQ748FHejhOdJ_VfhMTwyJP1JA6H8i7ngBFVg6-401oFn467L48roWn2mE0LjkhFL-iVoala9RDIQQ6_EuL3yR7RtjHlC_hHIQXukLbIZ4D19rUN1wE6wNIU0OE1aUw2WmVXJHoL_MvICses84FtCOki8DcA_fh7QaAxiKg-Gxg68OekXxH1TeFWtwdrX0BmaM3-s7krvxNeOqBUn1QPvxayfZa9VHqN8lf8KKThzCqQwwa0s1dTF4xGl1LkcXtEg6yCjYfsXoi_icSkZGztlnBp57h1y3KC4irXaQqtHnhgZink82AntftKg-bXAajO93gr7as" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو دیگر از حملات دقایقی‌پیش آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98958" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=jXUszJK2UPtRoEq2SBbHiF8XVTxX1eFW83dQdb4Q5lHzImA9JI3ZT0_Rcr61pbREgVKW3pXd5EV4HC_t7iR6sJ0AVtq7hooskbYXCp0fNFWC75YYlMHghcnBWb1rwlPZ2nVR_vJZroCSo0aeAi6afkOOYGdiwbjMkTKJBjSUaZHqKxz-DtkjUnJ7OpSfc56q-Z-EsFcdHQDm1tWR6ib2MESDdfW8Ww4F60DeAuZSxgCiPtKwgnuu-jvqelh3aAprEf6riJgkma9kHRBAor5arOgP3Z02E-Oyy1utEkAJw_n_TCY-mkFFXlOgY9Uro85gh_9YtjKXycvfUePsxd3t6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=jXUszJK2UPtRoEq2SBbHiF8XVTxX1eFW83dQdb4Q5lHzImA9JI3ZT0_Rcr61pbREgVKW3pXd5EV4HC_t7iR6sJ0AVtq7hooskbYXCp0fNFWC75YYlMHghcnBWb1rwlPZ2nVR_vJZroCSo0aeAi6afkOOYGdiwbjMkTKJBjSUaZHqKxz-DtkjUnJ7OpSfc56q-Z-EsFcdHQDm1tWR6ib2MESDdfW8Ww4F60DeAuZSxgCiPtKwgnuu-jvqelh3aAprEf6riJgkma9kHRBAor5arOgP3Z02E-Oyy1utEkAJw_n_TCY-mkFFXlOgY9Uro85gh_9YtjKXycvfUePsxd3t6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو‌های منتسب به حملات آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98957" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98956" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjjDt5fi5XV7k-m3fwNjUWOKxbYTZxh07_QMy0S8VeavnoIEGrxtsI8WtX1pFFQarFc5eNaLLMI8VdLNI3Zt-zURapYLMeoLzxDNDJNV_yjfPRsfBo11BIiyyO5ZYLA2mZFLOHNBNVDR4a2uigUsKlf6e20tuqUewXM4x6TAxI9pWj9_ktyV5U2MzY9tRNNV-sk8EcwC0B6_D9-Wjqpkll47nX7pQ693Kwb6nhLgQCBXeRlHykSHoVmA08uxh-pALmCaHFec3K3XE123KGiYqUHNpaGXsWTsr2M7CGA-oBg522YxKAFQ_rPSwicewRZWZTE3EEUcvsClBR49E0fieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98955" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98954" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پایان بازی کلمبیا و سوئیس در ۹۰ دقیقه
باید شاهد ۳۰ دقیقه کیری دیگه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98953" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اینقدر بازی اونور کیریه که اخبار جنگ واجب تره پوشش بدم براتون
😐
😐
😐</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98952" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛
سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98951" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtH3u_p0f5ghTx1AreHk3RPLMMeuNtjTYCttOM2zzMrDAEi_KTR5-qSgGyVUFiPmTOX6D4GdFoB72_O3UPnpV29nWBt7KMQBGFUq8Mk14cOpl61sucZMSuHtfjcQouVb96xv9zSWj3UDucd3q8gJjquL_VmrHss26gs-t8AH1Cb3BPnIovNYtBIrxNXhkXoxC6FNtElsZMZkiYclS8zxiKnLP3EHyzjshixVc3OpEdUQMsE_jGoFoBr2T8qEEFY1PjNtioNByUGTdE_5WmgNJeoN_bmeBtDfM4tKF_wPq32tetLJMzH_ASN6J8liy5tv0IUgRjKqNeJbV2MVUkp-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری از حمله به دکل مخابراتی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98950" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=gNr3nUuRqycGqGkWM-JTD3SG5r_FAXB9JH-y9VL5tNP7m0xC6NsSPPLRDjSzqsMG1pTA2GgH8HOB316CA4ynxhfnfRilInwHIwiVBP4zMbz8RLZ2gwRLBJWE0si5Hk_8aiQKVVBmY1D5yudZpeXVl5SjxVV7VWoem2439x4MAbxIoVvlC0EU-NFBbXCfP2sqiRGXE3yB1lE61zQiMTjj7oIR4DbhfDNAkhWWgdZpzogMB7RQ6qg0qRbzO1qJG3M2VpsFjyBJlP8MWvAQYMsVW-t4dU8wApL0GbjvFVBIU3QTrEG0bipKjDPKrKKbgxqGLpwy6T6UfcdEQBpEMW7jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=gNr3nUuRqycGqGkWM-JTD3SG5r_FAXB9JH-y9VL5tNP7m0xC6NsSPPLRDjSzqsMG1pTA2GgH8HOB316CA4ynxhfnfRilInwHIwiVBP4zMbz8RLZ2gwRLBJWE0si5Hk_8aiQKVVBmY1D5yudZpeXVl5SjxVV7VWoem2439x4MAbxIoVvlC0EU-NFBbXCfP2sqiRGXE3yB1lE61zQiMTjj7oIR4DbhfDNAkhWWgdZpzogMB7RQ6qg0qRbzO1qJG3M2VpsFjyBJlP8MWvAQYMsVW-t4dU8wApL0GbjvFVBIU3QTrEG0bipKjDPKrKKbgxqGLpwy6T6UfcdEQBpEMW7jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
اشک‌های زیکو بازیکن مصر از ناعدالتی داوری در بازی امشب مقابل آرژانتین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98949" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJGdmQ9U7uZRrrLk2nFo8YB9-lq052igrcp2yZ81sow8FAy7sc_AqgAIGl8FFZkbwLjVHA9NArvzwlds_RnzP5j_D16hqc0aJ1ybB30l9l4Rdv_PGiKYl0ULGUYxmPjdvG-95jRKeOskLpMn84vy6poXXoOkcmqH3aI__7JshEyeYddCz7kAVPEpFp0k5f5OlqOoZulYkx_FJ4LfNbQQ4AOyf8xXufs7TR32e2N-mLESndoFJW5NqNePXM8gBAfkitr0vZq7jKFiLMfhuCXuthtNPr5nrBDOXvPNmPZ5lWyhSwf85uEoiaj1F23lHkhUaJi_L_nHPDzU1xA4keHObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم‌ملی آلمان درحال تماشای بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98948" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQa4Njiy_R5MnaS5m1RA0GQLGvMJ0MlIoJpFc-ZoyU4xLeIVosJdVKoFn0n-mF6_Fvh_mVu8QqZiu_1tAA2KVj7-09OEP_xXV4ft79Jo3m2oHf9HmffN41DmOAKaHFuNg-qlfbPpP1MGJuvvXIbSGCUdFeIi7zhz4Jq87ERy2Wh0HAojlLeFCl5iDvL37UoeZ9lsRVneHwjFMmlcaoCdSfSY7UVBjUoQ9r-tasXE8iDLGvUHNpV_WxPniylaeb5Y0YR9d9KTvnKJ24FC5FzSACkIu7Z24bZhvFaqpt7yUY6Cwzde5JbCj48k_EWxJnXJNnO6Rq-bb0ocVDdmDwwguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به شناورهای سپاه در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98947" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری ادعای سنتکام:  نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.  حملات…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/98946" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98945">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDvaOEzBb8LBFL2gNJwWr_LD3bEjLglsP_GFD9N67vUSWcn9g-9sEp0XEKdFsgHv20kxcVhK3IBBylnTiw0atRD3VpzTXt96WIe_qjtbfEhnlz1s48dGdAwXX81Mr6ach3YFVSyOnlrv75rE7gjVrmlZkXAfKfLhBy3TPi1HV0Xpaiq2vbKzSSSfpK8pGfi6ZaQJ9uQ7sOrmpecDxnnamxgVsRLcLlLUtsRrol7xfwNsgDj22wr4QwnDwzamxB7I2q_PHiQiw1qhJr6QtaOWXDoVbEJVKtiftOBqFk2dxCfmm7i9RzYAbp0XJNgmZ0sx7e21w47CVLar8Cb4YHCXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
ادعای سنتکام
:
نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.
حملات ایالات متحده در پاسخ به حملات ایران به سه کشتی تجاری که در حال عبور از تنگه هرمز بودند، انجام شده است. تجاوز آشکار ایران، بی‌دلیل، خطرناک و نقض آشکار آتش‌بس بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/98945" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98944">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101717de02.mp4?token=u1veLabt8-89ReQPmgbVWPNjV5yRUKCBH9oKm68Y3cS7GERrK0zKeKq7yhbcMd0S_NtsCewkhmDXZl0upaDOAvbFr7AC7FGdb4DnJEmhCsO_UWGxq-IlXyS6bmUc2fhSFHKH-FC62vhC_Tl6RXxzQaNau_gdCITfCrKbLf51V6hgZ5mqIAamzZZSiGU_HnHJqOEoghw2ThqyPb4ZTBXDmWjS9WuSK2UXH3VkBy2ri9ONqYRQuoy7u0_smV-LVZRfMi4h8MmiReg8c_TAPSacHMO3AGwtXbvT3wvktE2Rt2I4AaJDJlmI_rUvCmGgG2GOA67hR1Ytqmi-9ADywwedtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101717de02.mp4?token=u1veLabt8-89ReQPmgbVWPNjV5yRUKCBH9oKm68Y3cS7GERrK0zKeKq7yhbcMd0S_NtsCewkhmDXZl0upaDOAvbFr7AC7FGdb4DnJEmhCsO_UWGxq-IlXyS6bmUc2fhSFHKH-FC62vhC_Tl6RXxzQaNau_gdCITfCrKbLf51V6hgZ5mqIAamzZZSiGU_HnHJqOEoghw2ThqyPb4ZTBXDmWjS9WuSK2UXH3VkBy2ri9ONqYRQuoy7u0_smV-LVZRfMi4h8MmiReg8c_TAPSacHMO3AGwtXbvT3wvktE2Rt2I4AaJDJlmI_rUvCmGgG2GOA67hR1Ytqmi-9ADywwedtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تفاوت توجه بازیکنان آرژانتین و پرتغال به دو اسطوره؛ یکی محبوب و دیگری منفور و مغضوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98944" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98943">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ شنیده شدن صدای انفجار در جزیره هنگام و سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98943" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98942">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/98942" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98941">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/98941" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
