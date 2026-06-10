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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-65658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=d1XRe_MBiLx8FHaNfcSMrI2qyJopjNf1hE6e-VIMzSbdcBHPb9eb0IMvyMTHZS8937ZaQuA0IBZnM4vbxehcjwFbhhPmXU92QScuA41OwSbJq_osOGNYix5aoqxf4h3KemwNnGjiNX1890f216qCvOeNSvAj98sIa16I2KXcKpxrMkZAxHSiID85Xclnhz9cXJgWA-AbrAGbpOoHW3aw3PY-_5H_FIa155HheqFU-jQ0wshGijrGywFxs1bGWGfla_BUVGw30SVibRbI6VBWTZNkklYCB0Qg8ccjfQVb6-DhxbrEiGO9q2LDbeOOXf852R6CE79pCluRuaP99Y4jRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=d1XRe_MBiLx8FHaNfcSMrI2qyJopjNf1hE6e-VIMzSbdcBHPb9eb0IMvyMTHZS8937ZaQuA0IBZnM4vbxehcjwFbhhPmXU92QScuA41OwSbJq_osOGNYix5aoqxf4h3KemwNnGjiNX1890f216qCvOeNSvAj98sIa16I2KXcKpxrMkZAxHSiID85Xclnhz9cXJgWA-AbrAGbpOoHW3aw3PY-_5H_FIa155HheqFU-jQ0wshGijrGywFxs1bGWGfla_BUVGw30SVibRbI6VBWTZNkklYCB0Qg8ccjfQVb6-DhxbrEiGO9q2LDbeOOXf852R6CE79pCluRuaP99Y4jRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگ جدید تتلو بنام "رفتم که رفتم" از تلفن زندان که آخرش می‌زنه زیر گریه....
⬇️
دانلود ورژن کامل و MP3 آهنگ
⬇️
@News_Hut</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/news_hut/65658" target="_blank">📅 14:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b931b462.mp4?token=N0FLrDiL9GHH08Kffik7dHlE8GXk6w4BBup-dK_chA9NZ3MDAS9fF06UtwJLG4NN_Das3Dafcy_hhiW2sOCVUG_kJz5mBvgLMTVTuSfqKQ79hckHEsz5JB_fOirtTptSpIcDqCRigt2ri7glcdwdbnQ_Uecno3H6PV49faIwAb6YgJxRK8fGDRupAwI_kpenxyx-O2Atmeq_RwLOhcnIG8C7dzDxVtAjsWoIpgq87AMV4oDh0Fw6zONs6cApqqLyQGHm8G_RhH6tmruQJRBt3CLdel94q43Ru4fvRH43a4FKX9TSF_a6nD6ePfNRjqAU0Myu5XExdmOQGr7U8zeGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b931b462.mp4?token=N0FLrDiL9GHH08Kffik7dHlE8GXk6w4BBup-dK_chA9NZ3MDAS9fF06UtwJLG4NN_Das3Dafcy_hhiW2sOCVUG_kJz5mBvgLMTVTuSfqKQ79hckHEsz5JB_fOirtTptSpIcDqCRigt2ri7glcdwdbnQ_Uecno3H6PV49faIwAb6YgJxRK8fGDRupAwI_kpenxyx-O2Atmeq_RwLOhcnIG8C7dzDxVtAjsWoIpgq87AMV4oDh0Fw6zONs6cApqqLyQGHm8G_RhH6tmruQJRBt3CLdel94q43Ru4fvRH43a4FKX9TSF_a6nD6ePfNRjqAU0Myu5XExdmOQGr7U8zeGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که این خانم از خودش منتشر کرده و گفته؛
«دختری که مدنظر پسراست واسه ازدواج»
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/news_hut/65657" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=L4OuYFsXom7CHwJ8AcnOnD5iO_aujADNGGpj6A7E94G4vMV0pZheHqsbYe8T25Ji8u14kaV_d5sBNbFzUL2oDeWDmGLs60VYfnufEACclFEjAW7y59D6LXjJIRPIJ_6bC86WyT-3rZsvA2XN92EHqhsL2a3kB4t4WPq9hsSi79Bd5X8VZ8It1wDhLJ-cKC3vFf-0bVBL3d_L9S03bNhsH4P1AgwSy-YqxuJbq-k-oCGhzatcUzBPnKeWRhCRJTIZ6Fur53rKQyqNL7ILT7aFFX_zrFVSGB9i_TpzCHnYmwcLA6-IAnmOLr9_zbYC1O0vjbwRdWImMBdRxPQp9nwZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=L4OuYFsXom7CHwJ8AcnOnD5iO_aujADNGGpj6A7E94G4vMV0pZheHqsbYe8T25Ji8u14kaV_d5sBNbFzUL2oDeWDmGLs60VYfnufEACclFEjAW7y59D6LXjJIRPIJ_6bC86WyT-3rZsvA2XN92EHqhsL2a3kB4t4WPq9hsSi79Bd5X8VZ8It1wDhLJ-cKC3vFf-0bVBL3d_L9S03bNhsH4P1AgwSy-YqxuJbq-k-oCGhzatcUzBPnKeWRhCRJTIZ6Fur53rKQyqNL7ILT7aFFX_zrFVSGB9i_TpzCHnYmwcLA6-IAnmOLr9_zbYC1O0vjbwRdWImMBdRxPQp9nwZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران شهرک حومین‌الفوقا در شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/news_hut/65656" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqzKX6PiJd39QXZd01yy3v5CobqSgQ542MtOydlgXWWviBwF2vbPS1j1QzLwmh6dQrJxhjabm8OJUk0Y7mBmbcnp0_G3YO-sr8TUaliFUvGCzd4vd0TdKNnC7cSdexSKO33JIPnPl_y0kOkOFFosC5vOa-f6h9Ru0O-t8twS792I8NNApUfMeeKaK0XeJCfWlYdqf7aIY71Wb5Bg6GcZeBLt3oVXA_8a2RF8c3Mw1_CUKubxGUAUbldeUtMMWH6ITNOXgvzO2j3g51YzjIH_wHTu-vlDhAMcgu7PFzROiliruFOsK7qTRWaNyA-CKvPnFe-c2LwMcMO3rlVd2FkdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/65654" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/news_hut/65653" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2qpmb7NrM1r2uoEO-zBtQ5UKCLNk69KeUJR9HhR07oMySu5Yyw1-IiTAD_KuFHb3oCZQwaU0nBcXlH9FpBuIsCZ79_DhR0fH4_RGe5pZnkAO6GaycSeKADjbsMsnX47r8VYpDyn307hrQsT9FMaHqznfrFTKXeAOpa-numP3z3NrpybUdvZFkAgzyIrtNbPph6cM4RVUu37fQu5RVk4-YUYMKIyrnCdTjF13YPLmIzVBAzbCdWzxZgWdZMG8Jj511F13NIsKdQoYDBTkEnjtEJZL5wMwm9WmiF5p0M75cLF8ivUbOKwOlnJoOJyVOq3vV3cY8m7SIgiQM62EzhtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/news_hut/65652" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXmpoX7TeW0cUTDLSA35rABosPDOIJEOF69PBcW1QpGwCAn3JwA60WG565KgeZjedfaZBZnxuFPMQbAUpL2DF3h6xR1Hkf8I0vW-2ZUSh5Sl0N2bNK0F7PrLRyvFh3k09COgRYN5ApVKVtQWoEK3dnBR2vDt4RWytkaSBHMAgtsGLd5w3QeD5HOkerjPnqGLhM-7G_jvS8h5gbhdsOs3WkxiHRClYT2Z-YmaH8UqUxVDi9CkrUwKVius-vEBLLk46kZspFxE2dHbbU3F_ko8CLRHffg42sbEsuNzZCjyusVY2a9nuHy7iLIMRN76ZDVipdAWgcffMryKBh8TptyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاتو پاک کن عزیزم
#hjAly‌</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/65651" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم  این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/65650" target="_blank">📅 13:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده:
اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/65649" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSmJK5qcOWT5pqFOa_haESPbSNq3lgQ-VatUln00Rx_4nAXBZNxgHiDpkIrbKbn0rS1sfKQMAvNvHJVJSqty8-b0-22GMH9x8GDSWdKF2x5swEInsVHY0G6ufnXDsUus1RZJaV9lxXNe_6dZJc9UmjrU70d7RyfTCzVpZEPSfTyBwsDk4BTSDc5wtF--gyDKM1YYAjmjp0KBJhrKCK2OB11l7B3JYMK8boyBl__OaQDvUijQTDYUyI4uVT-M0IW4oSojrgMShDP1XnbJsLST9PlG9M-hXbokdno7AZu3jLNsu6WDvG6qyFzHOcHqms2KxJKwxejRT3J6vVao13Aaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI7tSIhsPSbEnG0GMUlPXoGYokcDnnEF4zLeaYVEhRtnnZAY5Qcm24uHCnQvK-iBG03ehjUWTpc-EVHSaiflWEhQ6IYwRIwKFqERyaMcpQKeaPCX-EJBKzXNtkgfyBmcdU6hh6mvZt_EYs1KeXDx6LvluX_YS_B1XLCCGeYwvLh6il-oEAkCnb0rOv9VmSOeSCETz4MAVqvAcqg4fNSqPrRfkasOgvRAZCeWfE1udb9auxbtM-UaHQwbuqU8d0pifNIjCWxXwVF0v4vUSgjoJaSnPdNm-WHUh8AB9IQz0JwT6uZqUpFsYL__cSEq5yRB6RldIZn9pT1R4KkZED4U2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKWF0Jcx5mBAx-praFamabCwespJopNE89WIxmCxL_v9Ky7DICpJc00En0taP7bjkPk9ZkH6d-1VqIc8HvlczjGITcBmMZkCKV0olyNJV6W86M69WEZF1lB5dM0NoPHTntETE9bUQ-UzZefUMxf8CRoZq2syl1henx5vWxACWmZibwgxjGmBVRR4jh5uemJr2DvUKqBYb7__TlRMmHCnCwPoDJsVMXMds6gVbW8lhcHOuqw0GoXPsYja3maoWTsv2vNMfHpPTZzrZ022-Hs5G0Ck46bXP0zD_kCsBQhugQc6ihgo1_TB_EeROXRxqTK1nUhH-Wsvi-V31l8DGJDtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7thS9_Xp3OtpMPnGunUpuuDEmiUwVtxkuZmJk3-x04I5StpdM6LDyLWlnIcXGH47D-KFM3L3FWDMY7gyBPUJup2hv5FV2thWXNP5EgJPD759PrvYLNR68PhHtGVoTDBUt4_h7myB0yN4ay2Y2AGfNOmawD1BZ5md3NAD8eJil_W7G6LJasT9QdZuxU3oByjDfw-I1zWWkJPPyKwUcnx6Is4McR_wpw7MB9aDAzcCpRrRoAy_3kNqEA_XBjyEejThvCkyBNjp52TUkko7-U7MXUoMg6EyPi7rNXR700-J3BjSyPNMbvJ5t9c2C7IhxLmhU2wPkSfJ97RdEnJwfWNRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حمله به منطقه طیر دبا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/65645" target="_blank">📅 12:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=kvomGkYencikX1s_BhZO0ps27VBXarxg9l3K7_QXY_F4Hvl5ciUOLNZor8m0qxYvKzBORC5ejtGDbz0l8RqHYq3Mg_Ox-PNeJtX_ZYG5K0op8j7nz6XHP7dLYhB5XkumgXvcpvGsIZ7FfdLFSM5Lfb-qAFj5rtStz46P0ohZbGLH6PqoITUUmbwMEJRE8GhspEcXajGAzQKWF1YPy8ghghhJ56yIKI8Uhot6nss3GxCuDju_D8v6AZGYqyoch-R2YOgkJfKWbC9ffSaH3LPu54YRmXRyIL-F0E1W06CZjhHu8dygQJwl70Bglle2HpHHK1_WYxXinVHj5fkygCeF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=kvomGkYencikX1s_BhZO0ps27VBXarxg9l3K7_QXY_F4Hvl5ciUOLNZor8m0qxYvKzBORC5ejtGDbz0l8RqHYq3Mg_Ox-PNeJtX_ZYG5K0op8j7nz6XHP7dLYhB5XkumgXvcpvGsIZ7FfdLFSM5Lfb-qAFj5rtStz46P0ohZbGLH6PqoITUUmbwMEJRE8GhspEcXajGAzQKWF1YPy8ghghhJ56yIKI8Uhot6nss3GxCuDju_D8v6AZGYqyoch-R2YOgkJfKWbC9ffSaH3LPu54YRmXRyIL-F0E1W06CZjhHu8dygQJwl70Bglle2HpHHK1_WYxXinVHj5fkygCeF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
با توجه به اتفاقاتی که دیشب افتاد باید وضعیت مذاکرات رو دوباره بررسی کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65644" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65643">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=WRXMcQfyBsis4mMfkb3qZQ1QMXHDyaGCpwM0MLVNPdHMdDHdcKPAqwuVbfsw6wUK_qVAEJ1gfcZefEv6IxZVgVlBtwB6qdYoUEIfyflh-9rcsdyLI7XLsx-DMJmxNJJipErWr9MFaIfxdwxCteix1jq39cUM7C_JNwjahaPO8CmFUYUTjzAI_gVI6-Z1cYEWYkgI83x7l_cJonwTYJfDVGzo4zQGG1TYg7um0K4Hq4z3z2OwvfJM-USsH_AHRJ38pwa_e6dfSAQyPdQsmaEbUicEwbJsvRBVPDZcHYqMGQdPL4-CsmpiEwF9Izq3R4j4fDH5PQATMs_zaMTMBfLfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=WRXMcQfyBsis4mMfkb3qZQ1QMXHDyaGCpwM0MLVNPdHMdDHdcKPAqwuVbfsw6wUK_qVAEJ1gfcZefEv6IxZVgVlBtwB6qdYoUEIfyflh-9rcsdyLI7XLsx-DMJmxNJJipErWr9MFaIfxdwxCteix1jq39cUM7C_JNwjahaPO8CmFUYUTjzAI_gVI6-Z1cYEWYkgI83x7l_cJonwTYJfDVGzo4zQGG1TYg7um0K4Hq4z3z2OwvfJM-USsH_AHRJ38pwa_e6dfSAQyPdQsmaEbUicEwbJsvRBVPDZcHYqMGQdPL4-CsmpiEwF9Izq3R4j4fDH5PQATMs_zaMTMBfLfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای از صبح امروز که حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65643" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGs7-_vb_pO15R2KMiUrY62SB0gJWQnJLBldSkPqyrKu6YArEAkdPUJ9lW0tWAlIRI1M7HcbSKOD30m9fM9-1I-tGPB_wrcfSzOY2zSzrj8KDipSm9cGno0kS6sBmyk85BYENDgs9tenrXEqYfICQMrcpbJkb9q1JdRYZxR8K4FBmdrGssBycvIa14zNsNl-pz7Za5rrcezzzb9HrnRHnPYtlRcWcnFDpTbJZE8IzYvMOKf41GOXbCmF1eoIDkhkjxm3fPDJgcjH_kLTFo6nnn42A7DxlsYImlmiRcuSV8AO1vP0aAVs5H8HX9olU76qsAZrtfFXgCpv0bQ7GDcjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONlQf_8bxVyUEbobcH6gnPHeNLPrq9E2V-yZcQQd1ZnPA4PgXFMckbkVE9PdzJHm-qcEtbydmfdjsAU_bStrRO59D2Eqog1bCAaabKKLc_x_iwx7uHcfavPwke3g-a4Tfl001DMaDI6l1NheN3Co_JfANtTe-lVa92IaQOIwz-xRWv9mr4w1HoIa8Rt2-EcqM02YHa7Q5GIJqALjEPN3oEKDPp9y7M6LYQ38s1qA4GOGlD3psqU3dTRs_n7Jmfgj70XF1zgb1cWlE6B7e8Bl9zSNtBFcEf_GBMMLBfoIC7Gk5gVWJBjikMPeqXhWdNHNKAdvtgKbTgAONU-HgP0tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_Pojb931FbqkXplbNNKMMYdxq7teArtAPzqMfuq-Ff9dm1EcnO8uiFSRRj1nHYlFH7htIs2uWSFxgHn4Em2Wledgn0JxKgA57jJFzF0rQdcCMGWiv9BvsYooaLypDeSLE_AOp6YgDLOO1MDLxxdnPpkvCRCCEgxallm_Dog2L-iITW_sRNHqWSgtGtpC4KAKHjqQLjx9-QSiHKsGE4WbOGfpr-33lejQeynZ3HxHxBh4V6hmgsAMczcysvApKeEMhAKpi9jY3rmWD8yUaIeOy3EVZOxkmCuUGsUiOptcx1PI9r3fxRSvVt4xhvO1mHwHSLjG_wFjDByhEMSsq4Zrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqP01Smcl_lKIlKGpkUJcmEpShkfiFfLJiYWddOsyq27757rhL5HZMASx2iDwVcZnaIWr0OTDygJWSm_OcYoHM5pAdRqI2gAv83h_iykV_VHTBLDQSENLZgai04YgQskbTWaltzubMBWeCQj11njmOEHMXqcddOew7HFe9fB6Gsh5dhvDvmS8PnH6QGxOLzOqSMBiVDwWRsLxjp3sGuxeQnS0G61zmQJVlvDcz8xVQP1NYQlcv1TAZIgc-kUhXJDZtbVlpPbVdS45ymRKEGmZFJ7wvDTwh5mgVvh7nNroBtfsBYVSBJsvFxfHZGo_4AifxSyazXZAO3Dn-Mhsw2Amg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حملات صبح امروزاسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65639" target="_blank">📅 10:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دعوای ۴ دختر تو بابل
😐
@sammfoott</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65638" target="_blank">📅 10:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7m4Vl89uS_GkE3jAluG-7cRbvoT2xcMqZWlPYP8VK-sNAzvNM0cciABCr3xVdKI3P1ET7OB5KQpGlDzTDfVzqSoJjRjFQAGpz-c-pPraWvOTSjKx_vtS6q-hoAQuwEAf0JNSLLb0Q_FUIRodkZfs-hNqeuJMna4tdhkRQisAgkvAmtWLuWi4_8O-PcNlqUo_xU-x59jdn6nSbNdmijdVbaBw1jMAdMnWDFtb_fLK70MMPwvR7lq5N-pPt_Kzy9pRuia82Y3pE_1eXaeyMJmYnDPkJf5E8i2chhHc4tbzHHafEO3x4-Jlebc9mkjfUa0pyeyrkhNKc_Z911XlHHezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری که فاکس نیوز از آرایش سنگین ناوگان دریایی آمریکا در منطقه برای «اجرای محاصره دریایی»منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65637" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">😁
برا رفتن به باشگاه بهونه نیارید. از بی‌بی یاد بگیرید با چنتا کشور میجنگه ولی ورزشش ترک نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65636" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWo3UuwhMdbbbyzFPkCXQbmE5G-lHzI4w2q9IPwFy-TmP74g0Oy--q2I2aE5K-lEHrC1TDvUXkQ6x_GGE1WyLRM0F3kgjhbv_D-E940c-AipohnqLyCKZHkjTzcEkvDNhh4vk7ZH5A_s8BferVzKiOx5Gg-frLWWgDRkYAWAFol0q84vJWU-45jVmYQLLUHKnlGggxgwBOVQxnMpAm9QU2wH3BEESWx9cKANnxRirnCeCe7Q1-mAcKpH-NUUV5HcGrzwYKc1owNAofip6ghpspGh-pITUEeFGCT9zkUE6VqhSoAgQ-Q1aTw-WvRfBloN1wBnHu49YFsk5ftJ0R8cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر دانشگاه صنعتی شریف‌بدلیل آویزان کردن موش روی تنه درخت‌ در ایام اعتراضات، با حکم شورای انضباطی این دانشگاه به اخراج و محرومیت چهار ساله از تحصیل در تمامی دانشگاه‌های کشور محکوم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65635" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwoYlKNrdXpz-CjO7uyr5I6qMrEcW1yPLd3alr4tVM965e5Pj-egdMGngikwVXy68yQ97fN29KTGr9-062ibUxyQ2r9tD0QuhiHuxq6usSOK1ckRcixPBOlEDq4XYaK3hGSRJuQGd4bcA260eyaM7aqUl6F2-BWRps9usimMiUTT8Yfk5EbsB6PVLexGgO3I5T4G0tPyXL45YMqOp0Aq8ayg-Cg5TA41KxSuGBesS7XhQ0cROlQi61wiERIdsucJrQzwGF5o4Ik3p63dVRlb8g7fmSw27z-Jvx7cJoP4CgCLqeqy2SFDNgoBmNiTEHEnIEXE9WwuaNu7LYF3E0e1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویر منتشر شده از شهر قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65634" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=I8WRoiNZMeLpT4zzqO_HoG_7wbdHqS2uKJaVxJItIpGbkn_lJ_4sFng8bvVd846QM6SqIrRQMAtEYXe4BPsUVP-pTBkC3K2WGzF9B9MgYHk59AQyYxsKBgtHjGH0kuIefP60MeOi0sYWcX-v4mEVVCD4Ryjd9HNDL8nCqwDAFWKsmRwwNwr9s4ybxNfamF05bOp4ZmfGZQ1IRw4y5v32Ekkvq7S4pfOuewaybt86dGDtG3hNjN1zlamRdKLPeYWXmEghoRBSYe_hq86RAUhewhfCX06tuoZ_rPsceoMMuPKoHM9Pmem8gZOaRCkmbrlZlT73LEgBHU-7erPpSHVfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=I8WRoiNZMeLpT4zzqO_HoG_7wbdHqS2uKJaVxJItIpGbkn_lJ_4sFng8bvVd846QM6SqIrRQMAtEYXe4BPsUVP-pTBkC3K2WGzF9B9MgYHk59AQyYxsKBgtHjGH0kuIefP60MeOi0sYWcX-v4mEVVCD4Ryjd9HNDL8nCqwDAFWKsmRwwNwr9s4ybxNfamF05bOp4ZmfGZQ1IRw4y5v32Ekkvq7S4pfOuewaybt86dGDtG3hNjN1zlamRdKLPeYWXmEghoRBSYe_hq86RAUhewhfCX06tuoZ_rPsceoMMuPKoHM9Pmem8gZOaRCkmbrlZlT73LEgBHU-7erPpSHVfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک‌های پدافندی سپاه از جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65633" target="_blank">📅 03:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام ارشد آمریکایی به کانال 12 اسرائیل گفته؛ هم‌اکنون موج دوم حملات آمریکا به ایران همین الان در حال انجامه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65632" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwWK13XEROMKWKNyr_Tmgy1n2puMt_-qHTtmRb0jd7My8O1ofNoHte8xyosWMBow0w8j_LOe0f3pAli4mXCe3waySNMVr3axizNz-r9h43b45ZWP2z6TI4KiwgXaq8a_21BJGPM8ci3iqpD8Oam4bBvl9zIaI8-gwf0Vvda6lro-fqMcCNUbasUAkytyTcmtONCG_JtYjsLy-Xf9tlNDTdsS1Bc8WQiOAUVg06-tYAlzdcuqkSkxXXLUjj7Ymp2HnF2xZ8tjed3j3X6xB-IvzxmTlDcNOYC1Z_v_7r4NakTBmXO9uvlLqSLDFG3uIUHPtDTvRI-AZtMoUMdtzdUB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🗳
کانال رضایت ها :
@AtlasSmartTrust
🌐
وب سایت رسمی ایران :
AtlasArbitrage.ir
🔥
ربات رسمی  :
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65631" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65630" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vd5I-gVCnnoYAfwJlGTAn0L7Wg4WcYOSbXIh6BU4XKvSvgWAveWqiSKrQsdCpx0Kdd3Wbzh7CC0D2PJOscKLJuy6aC3vJCOlNAUniH2d-koC8j2BxBYjH1s5pqjjuAEALg5qKbQXlYRkTfSutRd0omiezuev1DfS2MIRpJlTO-Cxa9UPlet_QFFT0rQ2uC3VYqigkt1jWv5ccKgIPboelgDaXLFrJ1eTKNLVZFtOapWN2uVNfGCqG1oglG0Yuc0ByyIcccwCHyWbzqbCZiOg8rQRQcGRQlmCxDQVKubmKXOrBwX05aSB6h0k41meOPyEWmeWsWawAXSagpoj2-KGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65629" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
گزارش ها از حملات ترکیه به شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65628" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65627" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پهپادهای سپاه در آسمون عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65626" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUqU0avyjjYd0KVs7pCDynP4qzsMFInlv-Z2AO4i1MjFWX0P15qxKUEfeYJW2fCtcyY_yaF2lNX_ymJR4COkkQs5Y7uFN8MDsRqN1olWe7R3XoEzwk1BIb6hWOiOG1ezHGqTvX8RFoQAU8CphnAALCVbW_oSfqyR6g3q6ua0ANOolReW69YsvTy_I_GRndVhPTwP1KFHpbl5S69ma7MunNVfvq7UnhSdM5bUK8wvY6_r8NJrzHJDfWMIxy_CY2F4Q814XEMPXSLpj2SOrM43giF0TqKMzPAonMmtcihPxHR6CxtwNpFpsQsHfMDlbiH7AMv43PCEAxg2wUBBrAJ4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار تخلیه سپاه برای بیکینی باتم
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65625" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2yplze-8QHgZqgrmlJurDcadxdiJbtb1gQ2JvZv9HmvRUSUJ2B_xi-wrg4HH0Izm-RAozOnzpJqgqrg3aZg24zbf_bgXcDJnq4AnuTrZFl2CbhloHGSwOatHFgTH3fGZuL6lJNqs6ihQQAP5Ssc83v40DPCEeqdezhZ_VW7mzO0dI03mcQ_lAuA4O_qSHucDNrf2edUJ4sMSSK5tWFkbtvTj3juTLoNa1S0Q66pRSozw2lVRQLpD6CuhmMrUHZte-Nwisoyh3Qsghd4Yodz4-GOSrblHTogNDnyAg_aigu3J3ctcxl8iyY44CcbCQQtiHDo56-6OksLkEtTYd2NjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
علی قلهکی: برآوردم این است که سنگین‌ترین پاسخِ ایران پس از آتش بسِ اخیر به آمریکا داده خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65624" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhu9oPYe1YL-fe1OusLJB-gdlyzl7-SSWt4Dncvb0tyLaz67xYgY3bLU_DvcOS5e3ZBNeYVdZMngGZQskktaDN0c4ZAO6_eyGty1VNJD2QVrpe_AUue7jou4_HpKnBrb_eKot-nRyj2lZ7k58wnSzL976fL0CK1J0ugSVuvCofF0iGfJfaKWz_g3F65tvKc5eISE6l0Q6DVlOiAQ4AIvDo6kzwpcN9V8Xg7Dbw6Edi5L0uZIrlxcLk0-RMzF5kLF1t7_5R0S6UcNyMe2dwMunsnB8RsEdQpSzBk6B1QUN1m0_6PpEc590fX3tFe6I79fjUCUyIrKeDkQBVUOg8zR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شید برید سر درستون کنکور به تعویق نمی‌افته
✍️
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65623" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65622" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
کویت و بحرین هم حریم هواییشون رو بستن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65621" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
حملات پاکستان به افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65620" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4g-HZcM2ETs-g0V8hiQosk1vSJD-fprzV-vjeV3KNFBqMks-1tbSTvWd3oeCfZOHOrSgYQ2LxrnQTVp4uyIk3ySn8qH1z6JdKp1b40x36LH0fihhqyz_h-6ze_NWQOo27gAX91Jx31mtHvy1MuccLLjXzDlPW4hdJudu_piRpTacBZXCpKTKbCxbZJ7gaAsloieYoM7tjs_ZKmbtUMyqb6KcIVSiLvLxgmXkv1cxRpNSFv9xz7HkpCK5v_JPe41sV41tjCsGY8Hh_BztSfLGWu_-HPpg7YSXbUrQ7L0HLmz5x3ovJYS40iQ7hFuRtwGwkwCXcS9tWGPmLlKzCD5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65619" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65617">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی قطر بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65617" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65616">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇱
گزارش‌ها از حملات اسرائیل به لبنان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65616" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
سنتکام:
حملات نظامی علیه ایران با دستور مستقیم ترامپ انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65615" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود! #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65614" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛روابط عمومی سپاه پاسداران:
ارتش متجاوز آمریکا به ۵ نقطه نظامی در خاک ایران حمله کرده است و باید هزینه سنگینی بابت این گستاخی خود پرداخت کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65613" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ناو آبراهام نه تنها نرفت قعر دریا بلکه با موشکاش قعر مارو داره میدره
🙁
🙁
🙁
#E</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65612" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65611">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیمای جمهوری اسلامی گزارش می‌دهد که در چند دقیقه گذشته یک مکان در جزیره قشم هدف شش حمله هوایی قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65611" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65610">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از هدف قرار گرفتن پایگاه دریایی ولایت در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65610" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65609">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
ترامپ :
فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65609" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارشات رسیده از حملات به مراکز دفاعی میناب
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65608" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65607" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
آمریکا گفته حملات با موشک های کروز و تاماهاوک انجام شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65606" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhBV_3Kq3mq-new_XYThGUqu-TEwYJOBEF-cCQTSS7pW9U16sFA93agZLdDucPMSuEaDmmXNPC3k5nL4Kvx3wMrU58E7s7-aw3tx5qkZ1PEfPJDae-WSdJa6Euvia6PCxW9BVB1X65bTnceLsQgaFoRJp2eDGWPC0AGTBGax0bQ0mTEoq_gZdIiVE0TIBu1ELD1LJ-MM33yiHMtAJhptXMWxqN4s1vqCrsNXy6imO9lqw0L6Ogd2vHq0nTMbyuV1n-zmV_10MnukLJ0ofc4FerxyHpY3X1B_uUQX1p2QDp6wPvLNUGTUAQGbwS4nDgPgJ4j7tUL1Y2D48_DkWKA-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65605" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65604" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaleh</strong></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش
اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65603" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65602">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7J9ZObRgaw9XXG5Ho9wMFVfWZKVT8tTiQ_AQZESpbDnAUeKRY-Dt07v2sMSGk32U5Fiuwm5WPHZCgg57YdU1sGNvckr_Ey8roJ12X4-3ioHNDfLgEPY2Pi37tqRh_WRdCA45E2Dd6aw_Q_QacZltPNxJs4mlVYBS1aq8SS7MTTgZ8-VbSC3QFw1cUu53PP7wlY6vc77ZnJWfTlwn47KrajJYQ0_GtyvqrjJs-1A6Qw2mQFHO4rFYIYIHBGt2rV7Gowcr5MADlyDQDRBYF1CX43JHCE8OXRqePEM7j5jPkpZQLVjXYyy3FZWuYQxdsTxEWNL_qbFJVTLCFPxIlHIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65602" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65601">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
گزارش ها از انفجار در پایگاه نیروی دریایی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65601" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65600">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3BGRfcAKoZ7dzDs5gwkUQyaV2eW-naI1WhMSic46RoODNMI1IW4Y9u3lkW06mN_IEi8xTTwkMq82Qc7wWLlxYq8sA37N4pY3YGSY7mTzctSSHeeq7b2OF8ptF3I2_27pK7Er4BdgMKoS7H1NghZCFzX9dKxPUreSTsS3DQw7HBJShS9e5bJOgw9_e4_Ode8Wjz_0E5-vunxnEewpmm52qiMLqMrlkJ7MIgJAbUNxXhVWhURvjhyzIPZSZlOXSob2m4AOMwFCPwfhY9jnkMPHle7W3AS5wd9rcirA-K9avzVuCxdFxKcflqXjSXceNhOPxttH6-HwsKMxpqDDwGFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65600" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65599">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65599" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65597" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDXBypjVpwawHnvOiln_XOviOb5ocB4qINsSJn_uey-0ml0YbUdZpSXtsRweEki8l3AwDB32zAxkJPxHFVGQcLTd6IapNan2OqhwTLjZ_W2pw7XwX8vD_lMDrD8cdnJBIwayouL7SFyrTPHXfazovUpPQxg9pzlw7eeGujCMgZhaqQFx_1xHwYzM74DEPb5hjZxC_ykDKkAhuaRJx6bFiontniDEOtHWPtR4vjcCgnweDq1qJQhbwt7DN-JFuGgAMpWp9j8pKEQ_ZMOH6WyFa5YaSQABNsQVJgyViQQEuX30RdxYDa0TO2Xzfkl-Kd73AZrjgA2SfqT490rz6Xa2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده سنتکام، رسما آغاز عملیات در جنوب ایران رو تایید کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65596" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65595" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
انفجارهای شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65594" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس حکایت دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65593" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65592" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش حزب‌الله به شمال اسرائیل حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65591" target="_blank">📅 00:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی: دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.  «هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن»  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65590" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ما که از بیکاری و بی پولی رو آوردیم به مجازی وگرنه که تخمی تر از خودش نیست
🚬
#E</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65589" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده #hjAly</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65588" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده
#hjAly</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65587" target="_blank">📅 00:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:  محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65586" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ کاکولدزاده حاضره برای رسیدن به توافق، ملانیا رو با عقدِ یک صیغه‌ی یک‌ماهه، در اختیار کینگ‌وحیدی قرار بده #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65585" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htpveBQEFH3s_Obc674lL6hVnkQhD0XKZ3eg50TUdIcfO0GrlH7S-4mKYZoWOqXbCyFrX9rHApvKnoTdCPcNgWkYnkgAh_N3Uq3vveYbujnCccZzYKHYU9EvGu9tDBcxPZCk6bYz8MWxMTljTapi2gjAkm8VkJ-mgzWhgDd9YPP-QnloxjtwxmcdTXPGY0drNpvr2eJ09yuTdx38UV8F_2_hpkOzqlp6SRW1vnViFVV_KGEsiBnY06tgS9mcOkbyoXluaIB1JEABlyaBliXMIsdoPujzHupuYZQAYynix2tYPN08FS4YKjXn0cHJ-iTnp8TfgZbiM-BHT8G7JiskdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی:
دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.
«
هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن
»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65584" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه پاسداران: هیچ حمله‌ای دیشب از سوی ایران شکل نگرفته و اخبار مطرح شده کذبه و ترامپ داره دروغ میگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65583" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:
محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65582" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
شلیک موشک از خاک یمن به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65579" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65578" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65577">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
شورای امنیت سازمان ملل رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ ها علیه جمهوری اسلامی ایران را تصویب کرد. بریتانیا از فعال شدن تمام تحریم علیه ایران استقبال کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65577" target="_blank">📅 23:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65576">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود که هیچکس حتی فکرشو نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65576" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65575">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYAKs47deCaE1pDcujVgG0uTuokgGgh-wSayVUaIUQlkoqNt9Uquiaw7XzF-HB1ff4PFhPJRI89krBbLTlqnpIX2Ns4k2lr35Dv0QARWcFeHO-PF3NvdnpMMdRyoGER0tBxfdEnEBPRWsFmAbTG8WNqBEffy1RHJCJWuFt8AYo_UWyBEe3Z3-tfMk_j9Taf62LaycndlgIOSPvXHTA1raHg4YNKPE7F8SLUpp7vxnC_rkTIiP99cDQJ_u5nzemHedd_78c_mpuUgTESRRF_-H4GddcnyVw6g6H1FWQCykGPQctbvGKmK68dj4BLztaCvLvMkcKZ3O5czY_vH65EWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
لیست ترور منتشر شده منتسب به سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65575" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65574">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZBPGGiDZcgqlf9sYKJkqUMwQH_c2HaNQg43GxRDZLOMZ5Va7KoI0rbPfAityuRGVyxddSYnircMgxMKhm2xzsIZSDkS11_yn9hOf2orm5YU3FPVG5gQE9cINGj8-AG6D98gaiwwbdnwQMWomSwGONrlzR_kH89DMwsGsPguquqG5JQFg_t0rAzqR51jyU0bv3NNIcXyqSX_y8EwXwHsqOXw04SvU2OBIVeuMT4NPPxOIB2kE1MIMYYiTi1KqKjzaWlGDXuv79gbWUyriGVBdhHwINkg0Tq73v4nUGDZVWufZz8_5B1rVU2-EeWM9h_QoGDGAmuYXSBudAGOeO2LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فضای پروازی ایران کلیر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65574" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65573">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
العربیه به نقل از یه مقام آمریکایی؛ شواهد و نشونه‌ها نشون میده که جمهوری اسلامی بالگرد آپاچی آمریکا رو عمداً مورد هدف قرار داده بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65573" target="_blank">📅 22:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65572">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
♨️
حمله موشکی سپاه به مقر کردها در عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65572" target="_blank">📅 22:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65571">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=Z4vFwYSFdBxJI-co8PemtEiMLQxv5qelLf0efs1EseoJA5MKl3_zm7z9u9OS1RpEPrIrWW-Gmzd-SCA6qwChcc0j8rKPMJ8ZrxnWJtG9D70p9iccZTqQViMhRftksS1PMNUEFZyboeY8YYjp0hDk19RHmH6E-iXo5y_nrr9tXvl7XfEUBPztaXfhKZp8cJJbIKrbCyBV_u8RQ5j8oxeCMXKFjpxVfRbDMYPDUdDRPnEJ6Wlv1XcjIwJLbSERfAxss-6NwwdT0ecq4ImljYS8LD2DjKRM-hQjJjrBMJ46h0sLo-3fE8NzVRHF7lQbZ17926-pblfrBg_fF8FLmOPJZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=Z4vFwYSFdBxJI-co8PemtEiMLQxv5qelLf0efs1EseoJA5MKl3_zm7z9u9OS1RpEPrIrWW-Gmzd-SCA6qwChcc0j8rKPMJ8ZrxnWJtG9D70p9iccZTqQViMhRftksS1PMNUEFZyboeY8YYjp0hDk19RHmH6E-iXo5y_nrr9tXvl7XfEUBPztaXfhKZp8cJJbIKrbCyBV_u8RQ5j8oxeCMXKFjpxVfRbDMYPDUdDRPnEJ6Wlv1XcjIwJLbSERfAxss-6NwwdT0ecq4ImljYS8LD2DjKRM-hQjJjrBMJ46h0sLo-3fE8NzVRHF7lQbZ17926-pblfrBg_fF8FLmOPJZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
متکی، نماینده تهران: قوه قضاییه حکم اعدام ترامپ و نتانیاهو رو صادر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65571" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65570">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZ11vVeGxr9XOn1jlo0a-P0Esc4gZNvcripnge17j23fW2b8HDjBTqF1CL6su3uS8bg_Pr605sFgb6blbAPPqKPSCRmnhLppUlF0HZwm_b6XppgIoju68D90Hy2tc2hYZjcRw1YohdvEDiK1skI3SnK3Tm23rOCeoN3Is9vEyLrrIHgIhWPkdbfCu4p9yD9Cj_Gnmn3h6VitV6XXjGlWlMch1fZu26snRscCpE-_-ClHODHvLjirLNoK9_2pjfelJ_zQfVVNX5GwWtTdcqLbgurS8ktKzJeEEjozELDbyTJQMZ7rBQwXvTO2W7zQs6aK9_Uv3az9rxllZaO1y1VjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
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
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65570" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65569">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
♨️
قالیباف: در صورت نقض آتش بس توسط آمریکا، ایران دیپلماسی را کنار خواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65569" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65568">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=FW7b3b7TO_zpUij-JtDRbgVr_9ckwFMzxCQfhgfPNUP8-vvm_dgt5DUrxBX06g73enewi27qgUO1hGXyIeqrvB0GdvQPRwaJwd0UGlrf-BoxntknYFWFqCNbWQalZyRIH5tU6CIfQ7AtrNrmIhxXt65uvy6x_xv3TGSEfnTPKz0l6jcEha-DYui44QfSPAWQBCNcvtXyq8vIoYfilVYpdoXV-nZMXWFS0-Y8ePW0SfHTiZFLOVxdgow2Ujsrk8m2gxifwVZemNq1a-ThYuZb1dKyH4rX88etU4-jURwvUHjrvx5ejlGcqcvDBcj_7GvS305uu5lPo41PyfBcYcuM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=FW7b3b7TO_zpUij-JtDRbgVr_9ckwFMzxCQfhgfPNUP8-vvm_dgt5DUrxBX06g73enewi27qgUO1hGXyIeqrvB0GdvQPRwaJwd0UGlrf-BoxntknYFWFqCNbWQalZyRIH5tU6CIfQ7AtrNrmIhxXt65uvy6x_xv3TGSEfnTPKz0l6jcEha-DYui44QfSPAWQBCNcvtXyq8vIoYfilVYpdoXV-nZMXWFS0-Y8ePW0SfHTiZFLOVxdgow2Ujsrk8m2gxifwVZemNq1a-ThYuZb1dKyH4rX88etU4-jURwvUHjrvx5ejlGcqcvDBcj_7GvS305uu5lPo41PyfBcYcuM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت گسترده جت‌های جنگنده بر فراز بصره، کردستان عراق و مناطق متعددی از جنوب و شمال عراق گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65568" target="_blank">📅 22:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65567">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGWkgjjwj0PJNss0Z_DJRUlywO4iXjku2U8JtNAdKE4EzfExs7A5wFJty2kTsv475wQq__LS_Xikuu-SqMNJJ8u3mg1v_ZDiRMzFVZQ2EX9QBJDIPwOu-tWDikJWw_1CntRvy00VjCYvHBDhvgDnjIcW79gMHKDHFsuVu2gzcpRBi68j8tsQ1IFVIBYocT-RxUJsPmCjyr1bWInNrYpwYUyEmFm9cZX08iFua0STgDeAIC-opAB09tMQ8rEuRd_VLZU3Smq_mDMjtLh0JIKQ9qmLzX2x0Ka1XoJe15oncVSm7lNAU3XD279Hue9jkihoXoJ32XwEjxODHkEvx4Pgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فعالیت حداقل ۹ سوخت رسان ایالات متحده در خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65567" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
صابرین نیوز رسانه سپاه: امریکا به اسرائیل اطلاع داده در ساعات آینده حمله را شروع خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65566" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به ای بی سی نیوز: ایران اگر احمق باشد تمام زیرساخت هایشان نابود خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65565" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
رسانه‌های اسرائیلی:
«اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65564" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=VaPlxd443DHGPnjI1Ljp0_HbVZ0i3CvPpyE3ylktxPOkjH8GCp_JBouKWIG2WWrt-yCbBoDdTCgoctLe8LejnOuaV6kplziJ17SWf_r4u8pbnQPqL71SCMrRnmcJXL49hnwl_6nVvzhBIMqOl3xrBgl6_jKbISeTSud3l_8ZTRdu7iOgoxSXRRDbzkCPQH4fhuPh9wU4CeQbPJfhHPR0EX6rMfHF_BeAZhfBvrCZaUrQdJebFQcZm8FYOeO1ozmbI9GF3SPEMPRv57iaPdO6TTq9xeD6cUSgkxrrIVa9rO3vWCwlP_NbsFZYwg_qtE7JyQVorCD1-JFNRgm7UF2doQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=VaPlxd443DHGPnjI1Ljp0_HbVZ0i3CvPpyE3ylktxPOkjH8GCp_JBouKWIG2WWrt-yCbBoDdTCgoctLe8LejnOuaV6kplziJ17SWf_r4u8pbnQPqL71SCMrRnmcJXL49hnwl_6nVvzhBIMqOl3xrBgl6_jKbISeTSud3l_8ZTRdu7iOgoxSXRRDbzkCPQH4fhuPh9wU4CeQbPJfhHPR0EX6rMfHF_BeAZhfBvrCZaUrQdJebFQcZm8FYOeO1ozmbI9GF3SPEMPRv57iaPdO6TTq9xeD6cUSgkxrrIVa9rO3vWCwlP_NbsFZYwg_qtE7JyQVorCD1-JFNRgm7UF2doQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از سوی اورژانس از لحظه اولیه حمله آمریکا به شهرستان لامرد فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65563" target="_blank">📅 21:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">من از این کانفیگ V2Ray گرفتم، سرعتش واقعاً عالیه
🔥
حجمش نامحدود واقعیه
، بدون قطعی و روی همه گوشی‌ها کار می‌کنه.
تست رایگان هم داره با ضمانت بازگشت وجه.
تک‌کاربره حجم نامحدود: ۲۴۹ هزار تومان
دوکاربره حجم نامحدود : ۳۴۹ هزار تومان
پشتیبانی
👇🏻
@khadamatsup
کانال
👇🏻
@apkdownload_sup</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65561" target="_blank">📅 21:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
♨️
فاکس نیوز می‌گوید رئیس‌جمهور آمریکا دونالد ترامپ «در آستانه دستور دادن به انفجار یک چیز بزرگ در ایران است»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65560" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrF_MlfNoEQF4SKqRC_gaDF2O0vlfJC5IrL1TCftYMNYXlbqsawRRShY4ljaiXEcGSGUsoJvnMF5FdJM3QnFbdnSUjeIRU2YkcC9s3URhrFJlWtNTHaG7x0SRC3Ou-KJMAFjNfMS2dd9XVmRd6dDC4qyBEZdXuFbOPYLE5KsYLQKArc7t3CYQFuUfnm8cYCMjFGms7WKeXYpFSjewRdkofMCNhDJH1neBQonVDtTg6_yyMoR18McFri0VIosAU_YuQxnflJAqrZdxD3MnliDExiXVNEW7UTOCSJoXug2WHT7S3b0hKMwoYQIUcbNXzrrC8OoSogqXeaQDjc6tIKesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اکسیوس و‌ سی‌ان‌ان:
یک پهپاد (شاهد) این بالگرد آپاچی رو منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65559" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
منابع خبری آمریکا: احتمال یک درگیری کوتاه نظامی حداکثر ۲۴ ساعته از امشب وجود دارد. آمریکا در آستانه افتتاحیه جام‌جهانی قصدی برای گسترش درگیری ندارد و فقط می‌خواهد پاسخی سریع و قاطع به عملیات دیشب جمهوری اسلامی بدهد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65558" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
‼️
اکسیوس به نقل از یک مقام آمریکایی: تحقیقات مشخص کرده است یک پهپاد ایرانی به بالگرد ما اصابت کرده و باعث سقوط آن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65557" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02089086e7.mp4?token=DAD2460e8VLoVXKwqolsOZfbN_dr28g3GhC-DLlPoRDP5foKQzYKC35UCl1DeZqlt02zZX4jEGigcFfql-Lzqjjz3zv6pLTp2RIyr6K5caVHM4R86la1Zs9Tg8C6bS1GJveqyXlp1Yl5L-BsKb-JL7ycQLkMT7hwfwllXUstIH16pvkjLmyaKnGb7obh6VlLmqelN0tRZi4K2um92npERyha5DXD1YLBcJfOU3_eEs0YJsOEP1DydSwsPt-yLGqROJlFfGlaYs21bf1BoUPxG2fhv_TTEzvtVkeJQL93fdZ_Ek6AiMZKXEVjSMmHgYsocJ9QSzO5STlhfJNG6ua8OSBt7eTo73MEMLzBa9sdLGKcmIum5XfMBczts4G_zuACQktorLSTXXVGmHdJ-Bvn3k8j9zzPrO3JTG4hzY8IfhXvL2OHawbWeupzulnO1ZYnD_Tbn5aKVhrixqR1nmYTHLcBeFQr_Y3WB6nVRmAL0YP94KpJN8XrkHMzUOlHzR6c8LUXGWkoJTptHgvNqg6POFAxD0hGdsTCBRdwhKM5D-8vBG0om58UN0sEM41Gz24dVPhMn6Zq2ZfYwtwVHDys3fUNsy53ETYxbnm_mDYPyiYUCqerSasxJaR-zFTiNwbai1Q2TuDgKfUETvQFQGkJCsdAAcg-ru4cY6_BhW51zDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02089086e7.mp4?token=DAD2460e8VLoVXKwqolsOZfbN_dr28g3GhC-DLlPoRDP5foKQzYKC35UCl1DeZqlt02zZX4jEGigcFfql-Lzqjjz3zv6pLTp2RIyr6K5caVHM4R86la1Zs9Tg8C6bS1GJveqyXlp1Yl5L-BsKb-JL7ycQLkMT7hwfwllXUstIH16pvkjLmyaKnGb7obh6VlLmqelN0tRZi4K2um92npERyha5DXD1YLBcJfOU3_eEs0YJsOEP1DydSwsPt-yLGqROJlFfGlaYs21bf1BoUPxG2fhv_TTEzvtVkeJQL93fdZ_Ek6AiMZKXEVjSMmHgYsocJ9QSzO5STlhfJNG6ua8OSBt7eTo73MEMLzBa9sdLGKcmIum5XfMBczts4G_zuACQktorLSTXXVGmHdJ-Bvn3k8j9zzPrO3JTG4hzY8IfhXvL2OHawbWeupzulnO1ZYnD_Tbn5aKVhrixqR1nmYTHLcBeFQr_Y3WB6nVRmAL0YP94KpJN8XrkHMzUOlHzR6c8LUXGWkoJTptHgvNqg6POFAxD0hGdsTCBRdwhKM5D-8vBG0om58UN0sEM41Gz24dVPhMn6Zq2ZfYwtwVHDys3fUNsy53ETYxbnm_mDYPyiYUCqerSasxJaR-zFTiNwbai1Q2TuDgKfUETvQFQGkJCsdAAcg-ru4cY6_BhW51zDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو یک سرباز چینی در حال تمرین برای فرار از حملات پهبادی FPV
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65556" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگه بت میزنید هم اصولی بزنید!
با این ربات میتونید هروز بین ۱۰ تا ۳۰ میلیون وین بشید با کمترین سرمایه اولیه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65555" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فووووری مهم برای دوستانی که بت میزنن!
یه ربات پیدا کردم که بر پایه هوش مصنوعیه و کامل شانس برد شرط‌بندی هاتونو بهتون میگه! یه هفتست دستمه باهاش ۸۰-۹۰ میلیون روی فوتبال و تنیس وین شدم! هم میشه ازش فرم گرفت هم همچیو با هوش مصنوعی آنالیز کرد تا هیچوقت لوز نشین
😐
•
@Algo_Winbot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65554" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFxi9y2yEB5KKq22HNIwjKCNGJHUSzmGT0MTajVvIsgqn6PIjycF_rH-d35Ww2kKsiZGBpdAG1eraFsADByt9gNCkimb9tCJO2XC0CXr-zvdqtFi00ziCQip-zMVeT3A-iARJEDPZPrhVf95P8sEJCyF14Da7qB7A6jy3t9raev_wobqRfOLZ9cMPaUhm5iRyUQEJ2IeX03tS2fQ3g53LyU3066nxvDb0LBpQvvWDzDVDw9XX_7XL8LsiQgwzZYz-XH_iYh0sbJgYQLoQ_oayanUEmeQqqVPy3LRm-EJmiyOhCscLwEx_UAOwkazBJVe2dMk34FczzUxhdnmqzxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کان نیوز: ۳ میلیارد دلار از دارایی‌های ایران از طریق یک پرواز از ابوظبی به تهران منتقل شده است.
بر اساس این گزارش، این انتقال در چارچوب توافقی انجام شده که هدف آن توقف حملات جمهوری اسلامی علیه اسرائیل و توقف حملات اسرائیل در لبنان عنوان شده است.
کان نیوز مدعی است یک پیام آمریکایی نیز همراه این انتقال ارسال شده که شامل تضمین‌هایی درباره توقف حملات اسرائیل در لبنان بوده است.
به گفته این رسانه، تبادل پیام‌ها با میانجیگری یک هیئت قطری انجام شده و هواپیمای حامل این دارایی‌ها در تهران به زمین نشسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65553" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=aHv2tHRUE0rz8yT61UdWai1t4phLd4ty2rLqXukWdMB6iWlhNsZEig5kl_rKUXY7ddFe-BTBIK8-Cwn8jVJsmEou4F4sWpB1GPaRKesU0ISYiDFFHNKMFg_tTlQuAgkH4Rvqr6cgG-02ijkJtGMm4GbzqbV3LljqAeYG1RmBk5nzZFPmmwgVqRaBpxwxfo50XaqHMoCz8k_-vkLtrg6rvRMw7iUtUI6GKuTmsJm0ZKGDo64jjq-iEhv2BKzbk72nTh8ytiUFwxSaTJlMGLjfS_NkYkUQlM5XbSZZvbP-hPwdAJwyltg5JGLg3PtG_KaE7xIHmz4j_WPc_TwTm5K-XDyUOW1FegT-2pO8-jdtnIrlPwHffSIeAuk85VI8oI06oaIaFs14IqLXrDNLWGvv3V2ayqJ0qWpKN_DpIPDrExP9dlBzwsrEq3GU2V342gCi6rLHUlgkykLSnpwYD7MoSy5Ovk9wRsjpsYnrRwnaOJJ5UmRZA0nT7U4Sf_8Pd4IAKM8L9-kyBmHGzYsrTnhSLmQkxSWllp_CuDstw5FR6asnoz8BrmDUC2P3Er6BRxaRvRZ3ZcDPEQsWHPef6_hnW-DKsO9bcR40gHAlVV1IRloybetWhTPVdJtfjaHeR6n77Y4aoRqrf_UyDS_u4oQA5JTjxXYO2cxcq2aci0c6G78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=aHv2tHRUE0rz8yT61UdWai1t4phLd4ty2rLqXukWdMB6iWlhNsZEig5kl_rKUXY7ddFe-BTBIK8-Cwn8jVJsmEou4F4sWpB1GPaRKesU0ISYiDFFHNKMFg_tTlQuAgkH4Rvqr6cgG-02ijkJtGMm4GbzqbV3LljqAeYG1RmBk5nzZFPmmwgVqRaBpxwxfo50XaqHMoCz8k_-vkLtrg6rvRMw7iUtUI6GKuTmsJm0ZKGDo64jjq-iEhv2BKzbk72nTh8ytiUFwxSaTJlMGLjfS_NkYkUQlM5XbSZZvbP-hPwdAJwyltg5JGLg3PtG_KaE7xIHmz4j_WPc_TwTm5K-XDyUOW1FegT-2pO8-jdtnIrlPwHffSIeAuk85VI8oI06oaIaFs14IqLXrDNLWGvv3V2ayqJ0qWpKN_DpIPDrExP9dlBzwsrEq3GU2V342gCi6rLHUlgkykLSnpwYD7MoSy5Ovk9wRsjpsYnrRwnaOJJ5UmRZA0nT7U4Sf_8Pd4IAKM8L9-kyBmHGzYsrTnhSLmQkxSWllp_CuDstw5FR6asnoz8BrmDUC2P3Er6BRxaRvRZ3ZcDPEQsWHPef6_hnW-DKsO9bcR40gHAlVV1IRloybetWhTPVdJtfjaHeR6n77Y4aoRqrf_UyDS_u4oQA5JTjxXYO2cxcq2aci0c6G78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر ارتباطات: سیاست وایت‌ لیست در کشور شدنی نیست؛ به طرفداران آن گفتم ماستتان را بخورید!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65552" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65551" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afh6jEXsd1FPoMeUH7yEpD_AkmqSkf_2cYrapjzJNmbkHNeUhIZ6cRa7ZiJFd4pd5Q42ixaJrfDQOCCT5PQRr-0K6YG8qCPeAfsmNG4tUs1Epl64XK1uDf6v6E7xedaWgwjdqEJY9DvC5T0kf96G3O_8ECMBbXTUGd-JfFU2wMsNHCLh1sBwMo1euePc0p5FqCnqtUK92g0XKhuj7yZLMQLUpSrNVXTwcK64SgJtmNNsP67YKltXoFe3okpnF0JOhe4QykUInrHWn3mzskVViHvulP16L6UnglKYSkmZP1p8DW23P6eYEemLaiMMQ_626_ZUHBwnW3ncDGB8AF7QYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65550" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui2fYupQsQhbk5g1x03mpasc0mvpWoOAnqIrvLEk6u28MJzgwFWsABTUyraNGgqlXFzyvO3f44qBuSOjHTqtqLuh_YVD2H-Ei9kypZN_sdESd_X7SNxAcgLLsRpeijzSRSMOnTvy9wHFCixWize5Xb-0seyXPf7ktD2D32Vp4gWMA484Sroq3CRLkT6WiXmb-nPaEeKkg4nZFgZ_mJgt8wiiWnIla_QyJfdCGN1txJOs2XSjuAnCATVWjaRFeY4uqUELVbUAZ-kUrnr0JnbzRwBYx3WCIq5qBqMrj76i2fpS3clXFnbQA4uwMZ_I2bxCr1CqEKRNqGSqOQFxOXafqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛
رئیس‌جمهور ترامپ از طریق Truth Social:
من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده باید به این حمله پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65549" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L178x9Gp-KTM_BjUa5FJS3mFlLaO10I3KZg9GMfmU6mZkQsH-Fi6nreuQYJc9lNZbjuZg8KQQqcGI4LuJiZZ-Thj04MsBOl1jjXFkg8saDRbZP_kjJDQpotYhahMp6EXkjpzZoKb3E-JzXbXxJGNznZ1BoERCJV__HpwBGYKJa27ZDZPSwBDzuzBy0warI_-wCps_R6YQ5lgT6BxXuka-BUsg4ELEUc2v5NTqedwlW8newCve3vOnVG8L5SAALSSc_I4LQK4EJOU5qPF1-2y9lJlYsq4l54TlEgGnQf0KqG8wrJMl8pz9R22Qpj6RBZ3_CryIz-aBZ1AKgDNl8to1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جی‌دی ونس معاون رئیس جمهور آمریکا:
جنگ ایران یک سال دیگر به تاریخ خواهد پیوست.
ونس اطمینان دارد جنگ ایران به باتلاق تبدیل نخواهد شد و یک سال دیگر به تاریخ خواهد پیوست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65547" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
العربیه:
حزب‌الله اعلام کرد دولت لبنان باید روابط خود با ایران را اصلاح کند.
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران برخلاف منافع لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65546" target="_blank">📅 19:35 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
