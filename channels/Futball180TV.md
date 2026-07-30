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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 512K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAEn909jin1xduxJ_8gLY_Z5cP6ez5UZTiIpxBMsp7V69bKmVj1cFmoZfhelBFg2Zx41ScWxGgGIF1TMFStq76MB3a_pBwy_zXX1CM0wJT6ap8nR6h10H4ro5cpwEZuVf5tSx9IOVYLPrOXutJgJDGnaUwPdmylKY3ri9USZWleEk3YGa69ogyaBCsPwKFxr0sthuQvtv4h3orGDFDx6jXpW51HlyIGf5efi0IXm87jkdtAVGtXRLWFh1NttT1ZflHOHXt7h-Iev6TuquZMEdkX_67A0QbsgjCjynJzDXpThzFCn-pNkX9sSd-tqQbwKqJIRmJbfJDFgOvawe-Dqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO9rfLsecNDs1bF2pI9YNg3DjGyWdfodgK4EMJrjZOt1X1AHva2fmVZxfoXonNLxRG5JsgoxpvQ_vZw7twtVr_5LHviAWZiINEh4NlxgJYOM91FtJNnJz0r18Lu0Ho0zI3bZ6q8K5rsXdN1GjfuWfG4nv7lNaI1wwnmFWZYpS-o_kLEwxsWr_PEWXtWjrYZteoElQD5ZwMATGEVaHTs41YpeaQZrs4g1DdL6eAYOYWLYz7mtK2ncdB8v7eS7XZwra27MkoZoKuRAabMOTOr02Om2PLXJpTRgiI05aI7nuOSBLjWWxwZMW6rwXd4uZeaS97xxuHTOcFE_3TKGAaUFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZodgNJULNP-7Qdfjgzz9-2eiZqO4p6x3H8KIu1xiwOjjBXMobLeqhSh23E6t7sF8zudf4zm1vYgd--raDTA5M4Rhozdn1OatCwIQdkE04KPMDmoUwvttsYHZOU3wNzFQeGpUE3ceK1PzVXv-mCaVpHgsIj1PkkLzFiq8sfqU4uHYIkeent6_S2z8ELLoMF02uNBRPnu7Sq9n7N2oUbnnkxUOjNl3y5fhBuTjKugAt8uV-_SFpMkABvCOrXYXr9SbqnZu4SphXO_TLtIlHlS3hOs8EtfSXVwrFwiYsSfoZ5SM9s6wExgOlF6JNPryJAXn1-s3qxB_ZPHdizcyBHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp52jHaL-tItnLiudaspfSI0RLn81FyHidO6YRvxewx9GYdzQpnWrlNck3vRg6PDcFibzL3QXoAtf6IArTY1b4D_TiLCSa5e3BpCVamdowlSWuJlLCQBgQEliaXFyXHeRL4jpT6xxawAV7LUWLEBj5TxDckWWgM-pjQhhoW69GfeP4TL6vCiWFmf7kAIV53QonSLA1XTDaZqAH6-FPotOscL-DyzoYrv0_4m4SfXSEbLJm5_tYAnWsnQskShaJegn1WIgjpC4jeVsAQdjRWSKY1qvCvvPxQ_rlYqOjrbqu_-Mbmwxuqtxvz6_fYZzOcbbsSwY4JbyeP37HC37bKfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUZUV4WD3eypy4er16uF9FukTFMnxT0fODnLF-gcLsxkbegS4ndj0DmzBMHd8jjVGyoGjOqR38gCUDxYtdxUj3Y6PgbwUa811PQIDiOepzuvM-fGRB-4GDv-veDhL-lXU0RsDV1itlRMmXcDOARbRDv0pFFM4g9R3ZPOm0EABs86pEtMesF4MvXxBeHEQFJ_biOW-IIoHTEXB03JwrLNZP64jQXaY2gNjc1N8xt5P07nzIlQ8UEFNY_KVm_AET22ZwxkaojBMX1ag-aLbvYGMYXqOYxF_wCViVWF6npu6oHl0BPSG7IP8um-opdtzX7uc2oQtRJbltx3pRLZ_RVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcDfqLVoH_HwKLZtXFo_8PbAGmFE2TghnHCnJfUCSQdCKzfftaMSGi1CXQmBdUtWtYaZ9UDwnV0-zb0ehrKf7u2c6Jz1GzGP_kaSk9icpBou25fWpXwrV5xv3UudA0ZhlJBOD2Xp6FnoXs6aVaR6qsvUnstp7e7A4zpFtJeSHlDgmXn8r9EPxox0tTMDiAtGZMpJAWfanQL7uU5bkhpgIHfXB2NdedbvOdxQxRb57UEIuA737mpeSaduCZ1VaiGpngWUPIhK4-CbsuIhu1CWSE96rnMlp8MEoqgyo3xScchyucFePRcO86M_KnVYBhB5ajkxp8ql_KCjud9gzwEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVo-pF9M_5gOhI05D87eEXnaw44hjTWPBJqsljtQ3a_2yoqKcy-pw98jpeUgbEN-jprEAHH7qGSjuSQnxsHnixApYl9WbIXsXzb5P5dvl0qf3YUNLvPG8DWIhZPyeH1V2ZrcVFndAanU_ZftWYT5vS_XPy5HHh4mgNC2_JGNV7FB8COa1j4Thzcs8LpQ9p6uO7EcQpkLvmkYIZvswHD2e4wQy6s9OEAZdI111vi6LY_aELA7vyutZwiMzdiHMRQ5JVY0qATR_A85zrtOO4V6cTnnZvLIRgTTdt2YAJsqS0-hquOyCCDYYBBga7YWgwN8yPAQXv5j6k9t-Fu-S0bqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB1r4dVN7ocAReIXKuzMolPHY8TmkZlmYWoo2L_Ys0Hv1rfu4m51AN3P9M_6aJxunY6mcp5BRicKQSqFBmpX5LZAOfW3WkVDh-T4WDcO5ODClD-IiQg4ZxWA7puE7dgLRtfqKithhR61381PNYKHZpvdQU4mJ4e2umuyfNBlGzZvR3BOf_VUFipDTpPZBNqSz1V_-ohwJ2593sOmC1V8MKuVLaYnfLNNeyKHq9H7rO3T1bXBky4TF243wpMdg6Yc6QxduVBDFuVaYpa4YnVXLUzeaDtD2USSRLfk0YwBT2k2or3Bs8w1DiFFgcHFcao0BY2-ztrtLXkAqsQYJuuU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc3rKHmEU9oGz-PmCOUBes-fpd9cv79OoEg1kHp8SoyUs7ct2zogIJ2cRFSnr_VpDOM4hDU9FPAk13Yi6Ua2tYlO8evgIBARSg3rPMThnwzoopum0_Nk1HZJdJtPn7hafl6rPFTx1r0MGuGgi-bUcXmkrTIKpqTyQ-m86XGtWxJ79U7t9dx3RV_EC7K30QA3Qyuol2nTY-bgFQ0D69HsgT5KKossLuXtaM7KzlAd-t8yyMhujc90rDPN1cm3pp-fPoN7Kawo7Q7gikhqzQ6q1yp6zx0L_WsqZ5IJra495f89HilUW0rCZhxpyOftTdzP79AmTm_tpJjvYKNwQJ8V5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTsGDQfnwY95eoS68iG4owh0p-M0Vr8pjXg7NZm4UUYmgDr_k2fHftzCzqu_tCL4GcuSUbuvfquN4IEzkA-M5LNRtUIVoTOw7SDxhrjjKD5F29V9pDuDb_tNrqC3JPySsmBcZaJTs_zVVQTgQHYtYBUzVsZ74lPaUdmvMhvegCYlCeuZBHGIIX_g4jBcjOP0wiNn98qTpT-0MGqgqx9hxwjma1mfuxO5SlBpPPYqzP85OfBkzb-R7uElDvXv_tBnNiCzRxSa1CZBnJ0KuQ7rw0iavIauWr27n5FlmMU_6rBnWGdLiFFODQjaWR5OJnpbDQx2jbFK7_hebH2Fspqt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9kjejOc8yYSY0z2G3b3_Cd1aAZS64_YkrN7hBT2ExGvGf2-ff-FnBegpCy6r9a5Yhn8ewpkUV0Ipnq6AGfnugV6MhCD1B3ToQfmtgyXRLSuZniErvpfaA65NX2FENTZWIFIzzj2MmuRRcv9Dv4Y2W9EgD1zkHLsZ0kJjnyLgKWAxP7j2C8UWjxT50XZrkJ93lh2DqDrmgGn4ZOGC_iihj-yM5Hp6K1hT8aq7nlSRx9_skRoHN4_OgwP8NQbwHYwEPcQPSbkJy6EYNQLwUxDUlTKm9fwzvQqr_Uqu7tNEPDuZseGWT1cU_F-SqNYMPtlhAZDUanUvQa3moH2J6YVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ULDr2bO23KF1n2QecL3EVvh6rn4e0jSxb_2FX6W73GJvkY9e_zl7-Ff6NNyjYzUfKc05t-9JKkWQ-1F8QGmYtgJk5r0B8mJjNp1QSkOgcGp0_rOpYJ86KMneOWp361DzzH7eKCqCknEg3XxDGm4hOkvvYjBsNT3L-fnZ1z5rPCvzc6p-xpRvhzhmWDElC60IM5cvV8ZRFanN9FvJ2ShAnsvisvLO9VrFrffQxXsL0BV8w1EoAGWKZ136ua399U58jgShsB2DCvcl0L1z4x5N-p-ycYs4pm6_v_6tnreG-bfT_n3bI1BXfPL7kZD1E76jg8SfpbAhRxALZ43iFQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDY9e4LlpCO-exEFsAgtv2zINiYALr8NnRhuhSyCVc3qUrqz7mJmk9xY-DKwL6a67zk30PKUKCM0aRP4ecFe5bF4uG7fR0MX0M4qOAnZrC69BmbFIzi1RJNd1EESAmhB5r95RLxpddAXd4Y6J92MjogtPO-avcOixFe_iaHeNzyYKgLFzMemS5WY_8N43WWj_gI8wHNAu78rCkCjFJ8JSR5pzyxvwF0vLsNBSE1jOrDo_VbwhF4L7nM4Zl272Fn8OwBAVYeOKf9ikGg5KCIwsfHhXHfXkkHzevUXihLXwRIayNJ0v-Cv9ckG1sLZw8jJwgktPcK5zCx4lZviCX_GMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=PA0IUl90Z5AolRm5AGCp12dFeakgWBMA8cpQXeEY4Mus8V9qz9ALsoDhF4lZN-wRlXz0Ty6wKyOzUtX242OVGRMmIbwnYXe0GdXbVJaH7Ni26_fPa82FxH-xKZ2SFduE2rmOW_Q5wCDhhKpa-QaA3Xwp6-7Xz9mmweG8Jc5E_vwWWWZ0QK2iUrzytqHpCrRB4S-Gu5gSfqLJHoVoD1a21jeXppeYQtn-gYngdj4Swx9Br0vb3pW6tOGYtHIvoSVncKz5GfBzg1WQSulMFqJHjoCnJZsy6Hy_UvGHcOm2WeqG-_fKsEOkkFBXQIhI6CG4BYNkzCyO4merQUQfyI-BVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=PA0IUl90Z5AolRm5AGCp12dFeakgWBMA8cpQXeEY4Mus8V9qz9ALsoDhF4lZN-wRlXz0Ty6wKyOzUtX242OVGRMmIbwnYXe0GdXbVJaH7Ni26_fPa82FxH-xKZ2SFduE2rmOW_Q5wCDhhKpa-QaA3Xwp6-7Xz9mmweG8Jc5E_vwWWWZ0QK2iUrzytqHpCrRB4S-Gu5gSfqLJHoVoD1a21jeXppeYQtn-gYngdj4Swx9Br0vb3pW6tOGYtHIvoSVncKz5GfBzg1WQSulMFqJHjoCnJZsy6Hy_UvGHcOm2WeqG-_fKsEOkkFBXQIhI6CG4BYNkzCyO4merQUQfyI-BVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRp0M0fHlwhLVz3iEd5MrgXnb6VfdNVEdn1z-bODn5rDr_olgf2YXQzLR3p-GW4j3yo2HUawZl22mgV9Nr0HJVLgoc9t-06BDRVrJIlpIhjQClFtTn0tjU4YcW3rmLfbXatnR3-pMnGUH4xni0dSZ8H_jQxZ5AtRgbR62sdDHdsTaoan8utitydKYE3do0I2Iz3CAEZZLVIr9PqbmJj-QFlNx75HJ9HmcB56rS3_XWj4V0j2eD2NyGmrDxqprcYiBbXzc3J0MDuMbZpI6lzkcCcQY6yF1Vat03WD9J27bnpINd17kfa3SwZNPVZOnzNp8sQ4AMtWaEt-H0F2Goo2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOh7TKKAdpYcsHC11BjZy1TVaekyqeMBeT_XIzjGzX1h1YiY2xGK8aTpAXusztt6AM5TTcx9D38aio_54DmWTYmNEkl35NkfBCg217vx8FB1ivu9f-foK4JmUWrYsz796hyBdysL5LZhtSvMQKUL5zQKu2i1D8cb9MO9t0uOJ6-hUlendT32aOPTy7m6RRmWVhdCoiTlNire276wdJv3ZfNumvo9nvx5xtMhDcvX4mJjlBGo2QPiYlelz7K_EiDH9Djjh8H7rjDYOC_MfY4VDduWAvc1dfnZPXz0a7HgJxAfubN7lEdyi_smwgqeoaZgGMl6PPpPfGfD6SeBF95szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=T3rjetRo-5PmRNcfZkPD2b6om2aLF2WfmhHYpbqJnQ5kF1If-JhTpM8nf_ojLkl04Er_OvxdOwoHmb7k0li9wRUEOBi9RKREO5nLRULwohE6JWDu1FOaQuZ3iNqPCR1CX8tHAeLKw8-RD6kBagIapAFBUGCUUGGY-r1J6qr8JJG8NTG3mCe2-rB0ZFK_24fduNbivB9enbBsrARHgmd1C8Iu_BiSqSqK3RKvTBFJjCNhGafieFmCL9IGKtYk2UpkB-5neVGDVYVFk-BFmnkiX_q0-Xc8pmYHQuCy68Rt8q3J51z8_IVr1LcWQ7oZ7Po5191uxUkXkFzyQcxWlEr0_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=T3rjetRo-5PmRNcfZkPD2b6om2aLF2WfmhHYpbqJnQ5kF1If-JhTpM8nf_ojLkl04Er_OvxdOwoHmb7k0li9wRUEOBi9RKREO5nLRULwohE6JWDu1FOaQuZ3iNqPCR1CX8tHAeLKw8-RD6kBagIapAFBUGCUUGGY-r1J6qr8JJG8NTG3mCe2-rB0ZFK_24fduNbivB9enbBsrARHgmd1C8Iu_BiSqSqK3RKvTBFJjCNhGafieFmCL9IGKtYk2UpkB-5neVGDVYVFk-BFmnkiX_q0-Xc8pmYHQuCy68Rt8q3J51z8_IVr1LcWQ7oZ7Po5191uxUkXkFzyQcxWlEr0_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=T-utkYg4tnbzeg4VsVqtjSyrgsGk9W5eB4rXksRiisy-t-LQmPqZonPMxx5YYySSnvg6yzSifap7xT83_mH8mQFRwpOnCQm4TOsGgG5iqn9XC6n5Y-bCebrivXK_JwkWw5y2lda5jScRYT61cqNc6__YRWF3Wfdlp6auoTohw5QsoPRhuiOtxH6pwenReslrHtNCOlFCjE82mfzg9eeEfBDkNb4OUKHJ9_Ss3aS2AFJT0VlX2ZTuVxQsxupjxnDHR_q9NDhQMzUR-mgb0YpZ5_252TE4RaSRWfFVq8BjXHG9Ut2upwn_hbEjZuKbDuqBqCXcNeA69TeeRpQanPAThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=T-utkYg4tnbzeg4VsVqtjSyrgsGk9W5eB4rXksRiisy-t-LQmPqZonPMxx5YYySSnvg6yzSifap7xT83_mH8mQFRwpOnCQm4TOsGgG5iqn9XC6n5Y-bCebrivXK_JwkWw5y2lda5jScRYT61cqNc6__YRWF3Wfdlp6auoTohw5QsoPRhuiOtxH6pwenReslrHtNCOlFCjE82mfzg9eeEfBDkNb4OUKHJ9_Ss3aS2AFJT0VlX2ZTuVxQsxupjxnDHR_q9NDhQMzUR-mgb0YpZ5_252TE4RaSRWfFVq8BjXHG9Ut2upwn_hbEjZuKbDuqBqCXcNeA69TeeRpQanPAThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hra5PyE_C46H2aGMpANdpP0SqbyX8n4mTLtQBUOcG8uA9VZVm9yVenBrtETVyE0fj4DvsaIE7YZM-cAGZm_UjompVuabHGqZZdPmQ_ipI7lIyejJULPepg8M4KwxLMkcNRFpnEhtuv9Hf7XfrJP2vpXT89HJrWegJmGZ8UftCLxvizmNJgmDyPjzvz5tw1zfSYaszsrmb1xhmLbHAaTt9PF3jV2-LfarBSPkhpPS7ApUxLWbDHFV4nwGHTKOE0wRBhTkhDWiee_u3PPELK-GxmonCR6GmjJmJddFYsPU0_33bh3kIBDUlXI1ROqifbg9hOKhHG1NVU-g2z-b7P920g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hra5PyE_C46H2aGMpANdpP0SqbyX8n4mTLtQBUOcG8uA9VZVm9yVenBrtETVyE0fj4DvsaIE7YZM-cAGZm_UjompVuabHGqZZdPmQ_ipI7lIyejJULPepg8M4KwxLMkcNRFpnEhtuv9Hf7XfrJP2vpXT89HJrWegJmGZ8UftCLxvizmNJgmDyPjzvz5tw1zfSYaszsrmb1xhmLbHAaTt9PF3jV2-LfarBSPkhpPS7ApUxLWbDHFV4nwGHTKOE0wRBhTkhDWiee_u3PPELK-GxmonCR6GmjJmJddFYsPU0_33bh3kIBDUlXI1ROqifbg9hOKhHG1NVU-g2z-b7P920g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoQUekpev5A2rNCB0epsMpBhrIGzke-kvppxDhLL8XV1ObfYuvUYdFy_HsfztU9ox8B60sj6p3vk3U9pKbho0sMcCUFQtwWcDmM3qadaxXMl-nz8mXFTiQXJkMYhGn1JcybhEFO57hxyLHvz_neOBZhQMD1tT8YsbxAwZPMuqP2tKmtU0dxo2zpa_l933XDXjTZfR7kdvRyFnFCttMyrnkJl9L9Y5_hM9QmAHDEOZ70cq7Spim4g4-82TTrszr9JOXk9XZSMo7mL_7fYWvSI7unoh6IGAYcDGijU6gevuFyfgRKHtM3WHpvCZqmunNjrzPBGtfq8skol1bOLG3t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtrqpHQs9GHXLuhN19y53ogbx2SEID1iTtQ89mmaNPy2a6z8vNBSnlEbSSe4SW8rm8qfCIfsKsELqJzvYtE7cH4LqpCc-VVo_1q_hy-3c8pD51dB29JW5ZSJHhS6eMFs1cKEa4q5LdSQKBAttGnJV3egq5vy0YUFh9-3vY7cjfPTK_Lb1YcOLfMphr420M-Rv8MM-i1k2K6nIyKWSH_90E4AVVOl4mQ5uSXRV4HyuYEEpyBjPfjxluCUAOPpUqSNVwsdU-grqxqZAVzebxu4m-9gNUNBmsk8eZs6P9Fu5s8nb3jStHVxjT7uvf-RNFVRHxRFcF2aOLd_mDuJT3Nv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqq8Xro5QuI2OwgGP8NndRb-XitoknX7Pqdm_IzfyV26BlLRRIb2O6qI7itNRs9xSxDB0oJm5j3Ptr2yKO7nczh0R3tCltFoIT7AEagKgi_hF28ilTuktmkJTNi7fTQXQv5vLk6TPDDWe5lzprO3PF5unj5QF5IO2OOvScxtoBrBJnU3EnfChs2U7zbjk8L-Y-x0epw4lKRQN0_8kppH1o_p1eLyHBFhH36QX8kxSO08qlrqxcwl3Efdl60pg6TX8ScejpEh-wrVzzJJLABlh6YpBFhERcy1rW4pBJsPsDXhRQWymwRfnx5VMMQaNA7D38McW2epcbQFRVpy-xW6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV4AhkDlgPiOXGh0RpyFFn4TYJU3GRa310afhTpKgDtVHovi4P6rtL_vXKxJr3Wr-6auLugwyLSz5BNMIIXOADqzXTnwOo7aulEOeJ8klXsOOpVMCVoIt9nrPTQaYrpkGvJV1_oJkqFz4vY_wtMdy4l55a9O9Gb4veZ3uenprnnn3zsg-kxsBh7XZ2rmI__71bu5JNURnC0ja5oNpy488MtXVLEC6pcwVnu8Qj_h1peEk08ZlFbcThMLFeOzmS0oV4IQj8ewN6AemPFYjlPH1JXX6fOSzbhFOZEBT9imRLUHBrMpWMdppWltTVOqp7G6NSJU5WmC0t8V702uN2P9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHtT-y_X_cX6PRzTV646UW_0Qwt1t4pnt6_3gqtHwIQ3cqV-WJ2RvSDZfJmm5x79d5_X0l4LxDsHqTpBVpB75-2aVtpXeiIKU0Hxljrkpc67QExG7B035_zHjjyHi-0Hm-PS06xfXnKYUaZcQqd47alAVw9ELnWhOJLhyWn2j_wipNTpZ3hAgE7YLn7laKTEFuo9ngN9djxGtvXrXOwujNVxbJDbVe2gX_K9uDKp-jTbEIQn8jc7sX6PkuOrr9lM76ya4MRN6LoVBkgZVxf5-YiC8Bf-0-u4rqPcdE_YFSJ2xtHmDrVK3JOohaPkFHD-RY30HNCdLbv1GB6IKX_tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaU59IX1nwOdmzjysRtNLV8HW7yc09R04xuAC0tl7FqXKNVL4E4wx5JxfB1vn1f2HdGcdk2w1RDLdB3GsXjjjT19lnmy-tiL4VIPrppiwSL5Oxu4Fd9I_f17SsWXFdpcAysbJKXI7aKttLNPfhMycL9HuXOgdVnbqE_cVYUfjgPwyBMaUQARiBg19x8hxx6ExwHGCdXvNrd0J2ApYhgcxanxKugKr8bSUzKX2weeFFUCVlVlMX04fTs1hwCNJi-0Deq4RelAmIvxmsRbFOXnDman9OOrzpIOHMtRZCsJnFEGqSge2Ht4v6tGJy6zVs3fbhle1ejG4GmXnVnlFbcKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=oMVhFYJcCJgLBIIW5fz_7SXH4Qce5svv_zFAteudtTq8AoDvqlfg-Ruabo4NfsSAK-pWPpYWwEa_LdUlZxzsvyBYwKXUskBlsLGih5_usMR4mRCsEGwJ1gQbxRqFRj_ccQ90IW0iKtxAsvHWTLlvaRTxBWNFDYJI5SwNdUXduaynMvJPzAP_Qh6K_Ch5MN2IdePMPnw8gR-ofauLPH3lwH0E2AA0ssPweoorVfbr-safjSc26GtbCj6MoetX43vgkJNuOMohYwPM_PxShhY60IkyqGrhB7bPKtf7n5vKp7regXOu0_zEqe_OY0VjOBEY3SFJqBKZdI0pCf1wI2YV2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=oMVhFYJcCJgLBIIW5fz_7SXH4Qce5svv_zFAteudtTq8AoDvqlfg-Ruabo4NfsSAK-pWPpYWwEa_LdUlZxzsvyBYwKXUskBlsLGih5_usMR4mRCsEGwJ1gQbxRqFRj_ccQ90IW0iKtxAsvHWTLlvaRTxBWNFDYJI5SwNdUXduaynMvJPzAP_Qh6K_Ch5MN2IdePMPnw8gR-ofauLPH3lwH0E2AA0ssPweoorVfbr-safjSc26GtbCj6MoetX43vgkJNuOMohYwPM_PxShhY60IkyqGrhB7bPKtf7n5vKp7regXOu0_zEqe_OY0VjOBEY3SFJqBKZdI0pCf1wI2YV2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbBLhxd4XLMm64TSNujvLeFFDH22udWp7h_9FHYJzSO9Gu4OYI7p40HdTXivxkpn6NZSK1ujP3czmalnFRwU8YSia2ZGdbnGeMY-FXKVkoCGfUUfFg6cXKpJoUy_fe8d5fAIa4EmlsHfh_jBVsH_hvsc3ZqjdqCqox4SY8ciMAsUvx_9MMWlH1Wq8h1P_LZTp9yjDKmT057R60H2WXcfeE3k68xP86Fz_a8T-ZUwSHMUIsU6CZPIHFCoqRO-GlLSlY-HBIicn4GtTMnCyPR3vBasxtC6ufgMWKGtEXrQX9TVqP53-uHtuQkBUqSP9mrU4NLDEDzK12c1pe413pO2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtQOUwBgGqX4776RLVA4qBiVygbdSEz40DP8ohE5gXQWUT2uJA6moO43LES7I2_Uf1CRyheZEvWcANtoH1A-WDDiuxo0f_B79F4Bs-QriRBXd1tEsVx3EY4OAeKz6Z9zAny4b5TEQOWrvmxnx7lHt-4TF3mSWZumlR3ANKDkvaREo-whQwWPqsRozpHbszInXoug21eF_a2D7cXfFAC4Z_ZUfNZYLBgbbxzte14F6XxATAjKWuOx4m72wlfgtzRp_4MGgDQD0n5FaCKPgj6S_ozOia5wY7gg0W0koh2_xL4LB_T6RbqWRx7eQ5hpLwrp1bkK6gEYSimkWt2b91IB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=dAJYL768VJdPEkwYnEiLu7fZxwo7PbQ-v2ZQRsfsJtKeXulIVkAlq04huMkvg961y2bfdZlwWIkDsnUAsnn7x7cltdHQLt2ERMoshJcVeOMrMs6xGdyZP2GvyApxLyxAl558e9BFE6FwRz7oaxDwfJW1pxqg5Er5S84N8fzcreVjEJVhHPL-MSohE6IsgMFWHoGzlSO_3kSCnamYpa5loQfXDW93oxSQbBwlWy4pyXrf5Rqd8KN-s8At21G3WnMB_ZMFWKXKRdtIH4paAj6xnR6yOYWKulwp1XwRy3g1ps4fllR_BI8N5KrNj9O_jrQbZd46mFPMsUTGmO847BPW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=dAJYL768VJdPEkwYnEiLu7fZxwo7PbQ-v2ZQRsfsJtKeXulIVkAlq04huMkvg961y2bfdZlwWIkDsnUAsnn7x7cltdHQLt2ERMoshJcVeOMrMs6xGdyZP2GvyApxLyxAl558e9BFE6FwRz7oaxDwfJW1pxqg5Er5S84N8fzcreVjEJVhHPL-MSohE6IsgMFWHoGzlSO_3kSCnamYpa5loQfXDW93oxSQbBwlWy4pyXrf5Rqd8KN-s8At21G3WnMB_ZMFWKXKRdtIH4paAj6xnR6yOYWKulwp1XwRy3g1ps4fllR_BI8N5KrNj9O_jrQbZd46mFPMsUTGmO847BPW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWcWJ6zep_Dw3et5Zicb-p0cqZhtZ7tl37KqFnSsitJMeXlUqaKi7g0AFYlgvMe72yKxe9jim3TEM8GAkQ_EyAaKBfD3CVAdrZwwrBxhCgheo-biUBNSZ4QPrk8BotJXTAd5u1v-HlwXgnasjXP562vmCa9tqa06oeZuL3nnU1NCWy91OgrcVlPpM2bRO6rZtUHWeWFwf4jjmJiPawl4HIse-5ZXUfAIIH6kRPcvPvARz61TxXV_HQjs-7utyo_QN8TcIvq4QCmqxQ1uSffbzHCJiM9sUZ2G0_O73_wi16ZoSpdQAO3ZG2qLVTOqLOcAmxh2ZfjdCKLE0n-hYP9uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5HCuDaRxZkCmXpZQIfNXXjK5qORnRWMbXO4zyYB3PSI1s8JI7Jrjt8GZfa24TsWwCCEgL9VntGrCWn-EY1Rb4FvT1E7t6CzJheHEKsauPvJoaWbrF1WIIBbvrVH8zH6In2-vBBdab6kGdwuogRESUCRht0S0gZ6a6B8l58PogZ8xA26u5NfXsI0IE7j3fzGjaAa83WVGzrqf8B_njoO-6MxCXTtKnF2bNIQ9wHBvOrUhvMKNBB1hWnDMoyHQ8jo3w2K7sYZMl-F1uY51npO3uhysFLgMiOYfZi_NCQOonw8PVygS1QxQiShHlAK3IlfSd5awYE6fc9VboTfu5hAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phPUQ8Q0gkiuv6F-Y6sSyAsIiki0Hovr4kmgdkM7lN1aSa4zHL28Jp-7gG-9HZTs3Bkv-ZsnPzY3M8Yb4YHVuv5FD9Ja43vIC3KBvztdLb7KuCC6NqepQiCduhK_dtBIsjl-E9yLldykg0VxswhcHLnrx6sIfdVfyn7W6klFKLjNResu9zV6oaccb5NVgbBUxujai-ng-sGg7CkAetwDtqtbWqi81i0C90bfxlYPYW90OauXEZDIByVgN3jzM3GP_A-O1_HhqJ4RF8TVwF0N4VNhLlHH1Um5Glaef2IUFXwqLZqBPNB3JCPF6Z8rIKlI93xE2qQFqoC7RE5qsP9rfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEjk4VZA-QzBCJELgDfBts7Aygq_v6-E54EKCeLc5DK87DjYrlqyfDV4BYASqyoOswccxSjnEQuJtna24WHuQmTDid9YJRcvdIoAAWSCExAm82YPmkMHEHN52AgT9kxCoH-uiWT3vuq2u7P0UqE6N7H143GMIb7IrqhwYzMKd3L40MPTO6X6ttZQX1Modvlf5xw-c8Wj0F9d6hu17EEvTQ0b_kdMnQ8jI3FOxVv4U4qWcDXfx0IwVlxOZ2x26L8VRqbT1Nk83-GuxapHtJctw2RmLuykYGKn2w2bgJDKmnt7FbPwIqnD3i_dzRvd7k3cP2r9Kgdvhy0dZrXdEnw6Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzKEJHRl0BpnsKImU9dWP6v48iOCY7LrMbjWQXqb-7mvRVOSmaob91GBh-o7j0cTNCnCcTY4TgEq5seBCCai9ICJeeEIIDqUuEZinCpS2NGpbXWrJroA1QIMpoSX8J85c3G0SLrFCiWn6NJBje3fX-4bqTErwnf3v0IX7wqCl52I3DIAXCttv4RHc20ra5qikGvOFKz2hJzHpKLAztDiJNGGo8-MufJuz-oFHnjrvF9khSVElLGA_vJ29V2eItHeU031BLMBYNMWmayxvpVdHJEtc4tdckRQoYmR4DhMq8wPd_DFPXvMdEht84BLuQtNLH7nhSZaF5LLMhIwgo1cBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFaT00KWG40TvOeubQ4kB6gm-2bSrNdV5yn9QTv3-0DfRLf1A8jqFSXzacTPQrl8Aw4o3fmmj9PB2YL-po27cOSWzdR9xuSJnotnhnifUTBlN5f4v3h9Jai58fR7N_3IBHo3wy_w8PXWrHCabYpND7eKZtLLNX9JsIGfFBwVgriwfHuGe9rNRdtVmBKGBtaYPwJIPJDO75U1Vnn6LD4_dWq7CoUpU3giIztan0FYCz2JcyzKyvwn1DL1JHC9JtRIzK97-GUwiy6WBAMrODckz_aFJApO1TklTkVYRZUxdoixb8LyXJa6e0IuFflYJJldki0tWZTlEk9G_aj-zeJKuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p263okUtEBvjZaBVV6k6qzda89K1FZf00bupqks5eodtj3xJ6LgsVhejCFI7yhz0TBuR6nQP6wz5luL3sKUqrL8fYs1ONxMl70umj4-LfK2PssQDafcZCPI5CjsfRXpg_KmeeDkQgd_tQvTsbDGssk-q2lfKo3kQSPR3fbMFow2X6tMKVkNzqdbaUcIxtnpR5ZBKZWd9oqWZBefKGkk4G_trTcU473WFxMJcGLNf5pBhwq1V_FBYwV9ZD9c_ssEe7slb_LvfizcTSzllOL27ZJLQI_DUGVPCkQx9_xV0c6YBRYgJMeZja2khD1hdEpVXPYNguV4fp2q79chMrqyO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0Hq_FlSeV0gJ-6HiDkQYDDK3c5lTvq2CpZ2TGckFmPRl8HJLBcrfl7b5s1blWq-Xqg-D_pndUx5w_nvdeNWfWKD8PdqDf63_mhjPKejh4sHDKapLjYauqk85KqcgCGNw7KOWHccn0DXodAzrVg7v-J3A2dy8PkSY56xhTlqrUgBPQzyPsWqnrRB8WGytrbkdzKcm6vfJRH-ygqiXAvb9T26ihCWsxU7cr7wh3npLv4cY4Np3JAyiDXy1Q1FW1l9MZDybdmi2S_gup3P3chX6tcWPlyN30sM7d0Pp15cxiOHMP2YRkyBQJ3cBIr2HranxdcKj_M0OrXTVnL3ddYIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=A46kr0yOB1dE6gFrLLGOzu9eY2fTwcZui4Z2sG9dcVX5avyNt08C2TTestYGj6hUp0jXdOuB_Cbz6itPYrKyLPbf8uxmeZeCb_37989TltByiewfhMLqAcM2cGXYWojBmGcS6Ig7SE8G9pXLL70xOEmXdz0NSC88LwkfAqQaLx0MjczMirojgvlyidBhk8pgjMnq23xTVJwPHKsmA0oqGrXegBCyPTowLIDIgTCQB2dBbf2gjEIVIqiT-npoJ_wx0P7TegQq4u7UJJs-1SR046rs26ejIkk1VaZD0JbF6_nDwskBihseXZNFeIV3gzerWfnJSFvLM_swGFi64Qn6hBhOPn-gyQoJGbUdYU8U6NAGazflZDpUHk_ryjpO4osdXwqNq9MBk3zaLVYWq5XopSTG2XBNKGMbfOgsiJ9PLyZiBf4jiJaWgUupw5doS34tiq1RcCt0wrcjqb3okQB4Tvl-Ysx4GEnsX3tR9ejqugZOOwxMmWHGivtsuK1pbYLR4elihuZCHuXTIacJPlt-JOxTU5jyLJQj10dbwSyXgiCp5hFdhtpnHyNqXmqZOBOCCYH7MQXwMuUwwEFryZS_JEsH3PEH7XKW1OPnSA4-WSesfx6yC3zKoZGlD7GW1MSIY_yTIA2SEPeTal63sLzlTrylUMOWtBnBhOn9QTJ03gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=A46kr0yOB1dE6gFrLLGOzu9eY2fTwcZui4Z2sG9dcVX5avyNt08C2TTestYGj6hUp0jXdOuB_Cbz6itPYrKyLPbf8uxmeZeCb_37989TltByiewfhMLqAcM2cGXYWojBmGcS6Ig7SE8G9pXLL70xOEmXdz0NSC88LwkfAqQaLx0MjczMirojgvlyidBhk8pgjMnq23xTVJwPHKsmA0oqGrXegBCyPTowLIDIgTCQB2dBbf2gjEIVIqiT-npoJ_wx0P7TegQq4u7UJJs-1SR046rs26ejIkk1VaZD0JbF6_nDwskBihseXZNFeIV3gzerWfnJSFvLM_swGFi64Qn6hBhOPn-gyQoJGbUdYU8U6NAGazflZDpUHk_ryjpO4osdXwqNq9MBk3zaLVYWq5XopSTG2XBNKGMbfOgsiJ9PLyZiBf4jiJaWgUupw5doS34tiq1RcCt0wrcjqb3okQB4Tvl-Ysx4GEnsX3tR9ejqugZOOwxMmWHGivtsuK1pbYLR4elihuZCHuXTIacJPlt-JOxTU5jyLJQj10dbwSyXgiCp5hFdhtpnHyNqXmqZOBOCCYH7MQXwMuUwwEFryZS_JEsH3PEH7XKW1OPnSA4-WSesfx6yC3zKoZGlD7GW1MSIY_yTIA2SEPeTal63sLzlTrylUMOWtBnBhOn9QTJ03gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbqTszGhruKTcBZz6spydkSXn1EGrT2HrBnYAp4ZXlIzK7RWZYh63qZGypaJUCXcQS2dF_csmkj9grrTWUOYepiaJCjEW4jJfOBGo2QjkQJvn63pQAkJngFjscd_1u-bBAdqEGmwsw41omzgXHf7optN-F3KLZlfVNiPKlxIAbyYd00eHAk5dF__X4ZvLjudSyKz5wnwx6ZHWvxpitj7X6bLcJUAF2eyEY0IgH1CeIB_mLHLxfAZtmRDcM0aWUK085gvVRxwBkKQu7UeEGV4oO1q1ICGwX_H0omMbuSl1zG6T2iZOSmtbYRwzNeGUhCYgQTOc-XP0urG_vZ8uumJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=T0BCQI7uREVvEpbpsW27k58SFZvJf9qOzA2Zig66ptniptaBWMAwLudPl-WH0Ri04M8FX7Rwba1vjiw29ArkHd2joxJajeLGK_ycNsTULIv_lUszBUGZS578YM5A6Iqo8hFgMorpG-qXl4G6fwqDYLAtcdCGWfuqShTcHFUAuIDwLY6aBTCIjutaC0FSf3EpRtl71Csx0frz9mKVrRUyxuG2IPzb5wS9Xh1t6kPlue6e_utLGc-Qg9hD5DVw-lf9-XNftIIAyA-2oH6xNx2LAvdyXZpeN8mVIZ9iUaWalnZdhUzltKGM_SaZHaX66RmIl61OeY_-NHKEawjGRphCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=T0BCQI7uREVvEpbpsW27k58SFZvJf9qOzA2Zig66ptniptaBWMAwLudPl-WH0Ri04M8FX7Rwba1vjiw29ArkHd2joxJajeLGK_ycNsTULIv_lUszBUGZS578YM5A6Iqo8hFgMorpG-qXl4G6fwqDYLAtcdCGWfuqShTcHFUAuIDwLY6aBTCIjutaC0FSf3EpRtl71Csx0frz9mKVrRUyxuG2IPzb5wS9Xh1t6kPlue6e_utLGc-Qg9hD5DVw-lf9-XNftIIAyA-2oH6xNx2LAvdyXZpeN8mVIZ9iUaWalnZdhUzltKGM_SaZHaX66RmIl61OeY_-NHKEawjGRphCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=Uo1owp3REXuww2fQiFgWU-xhKAUv16K_e0dUAX8v1pGXEAtve6G6irk6uB-mn0STDkOvKY4qTML4gX1fzc5DkbdOD_XMKj1ns1kCr1f8__mlooog4SNFtViI9ky8GPuYl1pb6jO34b977mX30PMB-nrs9U_Asq0mFNC04agcbn82OnVIiivH-BCDOWL7ihkRPm7kOBB_gjW_gKWWyW-3e5kmf5ObxiwijL6JmRJ3K_z-JzjmGYSmlrm3__VD1ABpcZY2tK_mcrY5UP65jFhzKqT_fMnwr_qNpQwx1Il7KMmQ_sPaOs2F9z10sbW7YVWhGBfbsQKM2iDlnqA1mRaB3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=Uo1owp3REXuww2fQiFgWU-xhKAUv16K_e0dUAX8v1pGXEAtve6G6irk6uB-mn0STDkOvKY4qTML4gX1fzc5DkbdOD_XMKj1ns1kCr1f8__mlooog4SNFtViI9ky8GPuYl1pb6jO34b977mX30PMB-nrs9U_Asq0mFNC04agcbn82OnVIiivH-BCDOWL7ihkRPm7kOBB_gjW_gKWWyW-3e5kmf5ObxiwijL6JmRJ3K_z-JzjmGYSmlrm3__VD1ABpcZY2tK_mcrY5UP65jFhzKqT_fMnwr_qNpQwx1Il7KMmQ_sPaOs2F9z10sbW7YVWhGBfbsQKM2iDlnqA1mRaB3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=uCLAEIYO44q7eOcfJpP9dSTP-nBlqk1JzefsVjHVC8KF5ZvqDwECT9NnNRPeV5JwyOZzvRm-j6qwiGpUIoVmz3cwFm4BPManzrTlbdKiFgZAS8OgBJOnYcXYNVXcf4S1uIgdewN8Nmw65IbQnaimWRdfsupzrhRZVjtSQJRhHY5X_yCeY5USOSVmJMCM8dNHY0xjFKreOIMGPbfzd41qNH-zZ2aYWMm7WDF4nxfwBpUN_7Gg3OWhQ4FwGILiwP_UMNfpXU02rdjowmxbfoz285s8zP3cPgoSI5s9GIegPsjLwEA-l11QMbmF_FcCbdAWPcWyJRY4Oxy609O5I0kdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=uCLAEIYO44q7eOcfJpP9dSTP-nBlqk1JzefsVjHVC8KF5ZvqDwECT9NnNRPeV5JwyOZzvRm-j6qwiGpUIoVmz3cwFm4BPManzrTlbdKiFgZAS8OgBJOnYcXYNVXcf4S1uIgdewN8Nmw65IbQnaimWRdfsupzrhRZVjtSQJRhHY5X_yCeY5USOSVmJMCM8dNHY0xjFKreOIMGPbfzd41qNH-zZ2aYWMm7WDF4nxfwBpUN_7Gg3OWhQ4FwGILiwP_UMNfpXU02rdjowmxbfoz285s8zP3cPgoSI5s9GIegPsjLwEA-l11QMbmF_FcCbdAWPcWyJRY4Oxy609O5I0kdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=vpAKGLhLppRAMtCWYn1wT5dLpA-X_ZXPtH-TtDCFPQfjpLAkShAqOsxI9-e4dFRnqi7seigvKWgFpZ9GxF0UVKaowTF4EDXuWrhT7720Dyjt3YqDQIZYDhixOgm0E6x5WTbrmb-IjFwVOnYrBk4v8apaUStBDQ7IdY-z2MAwpYvOSN6UM5lUh9_IFoRSmxp-gAuFBaahv9U6Dk-pIRj0-VjvhBN01PkERCpt1jvSK26TSSw7v_Tyqmr890GHRD2EQry7Uh0MugEKpdC6BfhHc8EYc8xlYFJWFXpsZXhh2udHRw3SpLdwXD-CTi6AOZMVF2QsTGfR0S4gES8hjPNEcIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=vpAKGLhLppRAMtCWYn1wT5dLpA-X_ZXPtH-TtDCFPQfjpLAkShAqOsxI9-e4dFRnqi7seigvKWgFpZ9GxF0UVKaowTF4EDXuWrhT7720Dyjt3YqDQIZYDhixOgm0E6x5WTbrmb-IjFwVOnYrBk4v8apaUStBDQ7IdY-z2MAwpYvOSN6UM5lUh9_IFoRSmxp-gAuFBaahv9U6Dk-pIRj0-VjvhBN01PkERCpt1jvSK26TSSw7v_Tyqmr890GHRD2EQry7Uh0MugEKpdC6BfhHc8EYc8xlYFJWFXpsZXhh2udHRw3SpLdwXD-CTi6AOZMVF2QsTGfR0S4gES8hjPNEcIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxK1mFiRE7wCOrhIW5-jF-WJesroz_HXcABAabwwBQyK_DLD6kaWWQmJ4iD4UHcEYRJYmSrz-RjiHbn2vSivUnYL63LX6yEA1VVv-kznHLK5Ap-Nzg2PH1hWVtqGpa6mH-HZQqFnPa3jIv7cWGlnGr1jaeXbndS47QatmUvR5hK3CmYo6ZKwsq4pOluu83nMe39drssdrVrcfO7oTzikz-C3CyKIJ6lAuQlAdG7VPUOYIba2S6xiZ_OmgfqXgRA6lU3k3361So1fXWGT7Xu8iiQojri1KOkimhbWWMoACCIPFMU3ocu2OKA9eKpxQFuaV88spd_Uaf2dHr3Fd_7ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=N9xMfLudBA-zzMBIOU_4nsq_BTyOWZU5y1Fy1mDDRkHUDls8KXdv9URqClTVkzA1MCp-qPP8fEv2Tf3x1YN0bstd_AGb9Bdiy0HvX_IOdIMWjD_Sl5BnilRaGlKpYGqsSr7AJX9d7DgLRX44f76stFBi8ux-sO-szhZtGLVyE3BALUnpcdeCNEac2iZhzBQm-gnvy_E2JmXjoloho3bo8-d3kftkhpXuibyNimBd3CpumYj_3abp7ugb9o-8xzwUmadt5I0UkoSrSd5NSEX9llPKeQ2vsTy1FWMVH1COPav3kiYzoZEj78GzOonD7xFxB6XxUXX3Bt3RecAOGD-I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=N9xMfLudBA-zzMBIOU_4nsq_BTyOWZU5y1Fy1mDDRkHUDls8KXdv9URqClTVkzA1MCp-qPP8fEv2Tf3x1YN0bstd_AGb9Bdiy0HvX_IOdIMWjD_Sl5BnilRaGlKpYGqsSr7AJX9d7DgLRX44f76stFBi8ux-sO-szhZtGLVyE3BALUnpcdeCNEac2iZhzBQm-gnvy_E2JmXjoloho3bo8-d3kftkhpXuibyNimBd3CpumYj_3abp7ugb9o-8xzwUmadt5I0UkoSrSd5NSEX9llPKeQ2vsTy1FWMVH1COPav3kiYzoZEj78GzOonD7xFxB6XxUXX3Bt3RecAOGD-I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igv65ZGjWfeDN436HIA49s5tSdaFPF15jSoRq8WG0anPDL2d-WmlbHPGn0cOPCU440WT89yK5guSCDHOlWfHVQ8MXZIt5jjBID8vOhFGwy1kKZ5ts422_fosViaRfw-uecUNtQ277SJiDDm-Yp7sS4BR5ItfY5gDyDTIk_ekAhsMzqOZ0-eWKi_MTOOMdgc60RGM-fzSeMGAvGoN0Ho3hbKBwDjVpWQhaWaBiXB8_M315cukoRqtPA4zNhYmkKK7RUmoChC7WWIwlVRx53waVbiIFg_4j89z-3zbksGvz8yZreJEXfaIG-tlwUDqB9fO85g5sMdfgMbHsq5L6RxnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=b9lBpT0lZOPejz328sgZUtmgJ-QBqVSkz71sVLVggBwElDBePEwxY6UnF2lHBHUsYDpBwK7hT0E4qjic7sk10rdDPNHsthm7xG9WbnMrWQ-laghOlNrG1RekoAElKkn5iEdXUiolB0p1sxv6w7ZFlYQpxd8AvpBqgsbrlsJqOBNMWzMLzRYJ5rHZ3jkpnQeuNVyAvO7CQw5LvB2ryNZn-8RCuEHXtI4hexaPJzZZd-1v1PfvoeOGqOWrPeay1t1TrnsfCPVkls56bnKSWsb-vKjxzxRo5_yEdwR359cYZ5XgmyMYk69QDDPpdA-7LuH6QnECHhE_KzCHuQ-2qb7sQoQVLHxR_FPBQglEcW_9raDFwRd0AGNs_UJBXj-aJCwd9zIzhvaHkB1xnzw1bPgwwZAbtGcLpStjV1awOlBj0scC8SSM3VHuhlAfEaMGD704tdCsrVucX-5WtekxkwmTUewjU0n7nDwVeN7q5k7fY3h5TKzXkw3yHiHkl1ZR3VRm5RvKxQW_PHWMoueozVx4V-hLImnWRYfmVktRbd8pHRp3HVLqfNo3QCRM3Efbv1_KlJnXdyxvEFra4HmrpktHWMCmIlr9RcTuKjA87HyY6kKWbLOtBKqh-1jEce4rt5WBBEgoN9F5sCyeuN4xXSCLeg6aUnUM3Xn4Zx3hrguA_jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=b9lBpT0lZOPejz328sgZUtmgJ-QBqVSkz71sVLVggBwElDBePEwxY6UnF2lHBHUsYDpBwK7hT0E4qjic7sk10rdDPNHsthm7xG9WbnMrWQ-laghOlNrG1RekoAElKkn5iEdXUiolB0p1sxv6w7ZFlYQpxd8AvpBqgsbrlsJqOBNMWzMLzRYJ5rHZ3jkpnQeuNVyAvO7CQw5LvB2ryNZn-8RCuEHXtI4hexaPJzZZd-1v1PfvoeOGqOWrPeay1t1TrnsfCPVkls56bnKSWsb-vKjxzxRo5_yEdwR359cYZ5XgmyMYk69QDDPpdA-7LuH6QnECHhE_KzCHuQ-2qb7sQoQVLHxR_FPBQglEcW_9raDFwRd0AGNs_UJBXj-aJCwd9zIzhvaHkB1xnzw1bPgwwZAbtGcLpStjV1awOlBj0scC8SSM3VHuhlAfEaMGD704tdCsrVucX-5WtekxkwmTUewjU0n7nDwVeN7q5k7fY3h5TKzXkw3yHiHkl1ZR3VRm5RvKxQW_PHWMoueozVx4V-hLImnWRYfmVktRbd8pHRp3HVLqfNo3QCRM3Efbv1_KlJnXdyxvEFra4HmrpktHWMCmIlr9RcTuKjA87HyY6kKWbLOtBKqh-1jEce4rt5WBBEgoN9F5sCyeuN4xXSCLeg6aUnUM3Xn4Zx3hrguA_jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRqBhFAQfqB9k9qUWyj7o3DnegiLOj9ltiSYVnH1bCMA_myk-cHxpNLz0vh06b_KzgtaBWKwlZGvHWekYqf3Db-Cu2FbD39SlO3kWT4ydL1tUYgbJ7gAeWj3LVlKxxnRb7G41B2-D5wMNSmnFu63bW8tyD1RgeAa9lJm3bR9G5vSb3GTkP37Caj9uBHGFo-PcUSqJljOhDDORLQnscklF6rIAmX0RJ6hDK3TvIEag_9h59z8jfZJV8dCt6EsrYvy2M55cCECggGqDzhuqTu59BEjLN1t_xdyW0lCDMkxZWB0RfgsdNLfH-JfnwpdbOWWKa8XnvDiNvakg7BlGxHFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orvVbP1wXSZjYPXDBYxSJ4RRFeE88w3p0ldIpAmoba8zOhi2lTHiv6mh9nJ7UpdnToT6vnMUsUNyzPTGTHXWPWgkVOPWuGbG-Pwk9x6veYM_k9x1iHkxNazZezDRHj-0-fWkL3JA56Aw-ndw025MXDwHVMCRh22b4LqSzxRLms9wsbpVQwWsg2Y0FZ59OgRzZUAOrgq3iiBn51NZZFcEEIpG1B4wC7wnkFi4vSqKzMtBklRJ_kchJgnl7m_YNWy5DRl9KSvGk1x5qChjB4goyX2PO9cEox4YjBS5OKB5M9nqBxQbo5YNFarJRQdnHsP74Kebfp3gG4S4fs9B-gRxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgzysJ6QYy6q6wPrl5XyUhMr_LkZTDbW4RKhhlZEqGeno8H7kZRP_fQiMdcEVtePpFufEwNWPsgvIujTmpm7mwjNsw7aZcEGlVPZuVF4CqwpI3OrR6tRWso-sfjVGT0MufQekGf_4EHKNUDq-E74-8W5KTBttqvodP2Qsd2hhmLU-EUwymGs4P7lk-rCW_NeIeLlMuH3nauWmwZrEiXioCt1xBC4wf_sgoCdCpHttwMICZc2S9gy2lC67gCD09g4nHJFoSgHij9jKv_kKvhl0ATwBzT1uVk27xOfOnoSG6j9vTT8O0-w0TY3rVyQur55Bwcd7V5B7ZhQp2Q9vW21hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=qD6w5pSTrVTgDO5_dnLKLbCiSzb-vBGIpiK2cSbBxOC8ix4DPZRDOLP9csjqYaeY1G1xsDXd-0uXgFZCoUImotXEk0OrOf3vEctCcKF2iuo9klxhS2MxKj0XFno6gVm6EsE47BcJWv6i3wOAhpXro6O_uaB3OVw-ObMFoH-rIxfBMtEwWpgbAtHHljAEGPZT_rnrhY1DdV11GtkubUYo6Q2RCTA2zrhFweWVFYitEi9Na7g_auVHEZJf2V1LF_JRpJj23aQeutTEL_M9zeUWqGK7PFp8_uyL1E7p4NCAxaKwzPlOCYyM0wk4EFDSWEysIeWN9DANNVjr1hoJreaHQlFDmoJJhGW5jajElapWFkN6yOKv252J3A_gW43RiXT9hg6K-8POM10mFmZsRVzDJIbbfpy58ckaVh5mEdfeFyGrHQQerZwahMphVqZVX2Jayd8zhAOhy4ZWu45dDtYethJUHHEB9sZSAsJgP5VdlTs00yADVwDdCDMfX5o1WujuRScneFLviB-tLgD6TT1BdgViniMYUY8mq1mz2ggXfjaqin1a1GHjBunXrRcXetOaoayZFi9fge4YVqj2oME0pjGP95dMWYpVr9ewODfARgo7mmorGcdzWr-nwXZ5gd4aHBFJAVb8v2uElB4lsWay9BhYzm4pY2mo4OyyBn_bP_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=qD6w5pSTrVTgDO5_dnLKLbCiSzb-vBGIpiK2cSbBxOC8ix4DPZRDOLP9csjqYaeY1G1xsDXd-0uXgFZCoUImotXEk0OrOf3vEctCcKF2iuo9klxhS2MxKj0XFno6gVm6EsE47BcJWv6i3wOAhpXro6O_uaB3OVw-ObMFoH-rIxfBMtEwWpgbAtHHljAEGPZT_rnrhY1DdV11GtkubUYo6Q2RCTA2zrhFweWVFYitEi9Na7g_auVHEZJf2V1LF_JRpJj23aQeutTEL_M9zeUWqGK7PFp8_uyL1E7p4NCAxaKwzPlOCYyM0wk4EFDSWEysIeWN9DANNVjr1hoJreaHQlFDmoJJhGW5jajElapWFkN6yOKv252J3A_gW43RiXT9hg6K-8POM10mFmZsRVzDJIbbfpy58ckaVh5mEdfeFyGrHQQerZwahMphVqZVX2Jayd8zhAOhy4ZWu45dDtYethJUHHEB9sZSAsJgP5VdlTs00yADVwDdCDMfX5o1WujuRScneFLviB-tLgD6TT1BdgViniMYUY8mq1mz2ggXfjaqin1a1GHjBunXrRcXetOaoayZFi9fge4YVqj2oME0pjGP95dMWYpVr9ewODfARgo7mmorGcdzWr-nwXZ5gd4aHBFJAVb8v2uElB4lsWay9BhYzm4pY2mo4OyyBn_bP_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heprIkpBg4YAJsLKvK3JCjg6W-LsIFKn93fSP19QWHqfnn6-6NEjp6VUKX8JQduHDCkK8wLjjsMPJXBuxX3-SNXrgj5ZtLRFqWj8wFY3leVA1G9GOcoKTcs1vhbiu8DyBk249R73wZJAX2M_SAL-vV6QAjS0WHerTxJfLOCQ9BVr77IPWUp3tI0_euk5CM7rGra7iYIBfK-XqKDPRNQKeS7IxrIDeTWEXJeE4IhMJz9UzL6lwG-FK6SFoeGF7FLQs6WkA1S-ZDrQudRErGRoWeo58Ah3VQmtaM2_KCCkhoxSxkpqpSRq1wdEsqlgGRxPgG1PWnQQq0VYctZ0MDO73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyE7j_xUrBtmufZ4ayGSPUh7Bh_nekruSPs41ZALDjP_qySJMK8n5MSc8dWou3fBm2iFbQmxz7oA2W6jOM9ZMWoVW5A7QGgQ_FTG7OdEzc2wO-8U_x5IGQDTmGbtc0SXmnexH85QZIEMPIpdEL8sSJx4kBN2H2R-6_utot2jK_rIO1lk9x_wpkdYoLf-RM_IJ8aSipya7zYpLS9vtJKtKOZMpNsUYneZ7qqooDe0OhbqvS1mYw10n5FTnQzG8GrQFA-YfB2yxIIBzXRA3vCUWOhhQ1tta4egGeVFvVTj8XsxWbR6fDGtcXpIQvR1aVdh1zG1WaJsIuZBcim9wTid5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGxwjMv9zGudxDOd-b6s3sKi2Clktqgc6WSNGIIB3B_aMxFyXxNLTb154AP5sWDXyROxMFJz4CtCcMhmgcJaUz4ELiTAaI8VAqr2lkG7MJz07Toycr4x5jgWaserEoAfzFk8_m0QRlAYhNXp67nzsqqiokAwjSkBx7gEn6atNudITi8nAo_uWtC6owXQwAOvYQdjIIpadl7yx6Wq0NH_WWb6AuFHTC2YzsUxV5SDOj1NSKyyzQmESZ-RErONIj7Mmy1nVDCLF9Eghktm3BK5cMqvRPr0HvD-_vwuZek_GVFBodt4TfZI6ri7fSPnRON_f25kXfGKQCTBs3hUaYoRGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=odzISVcNJGRpfVzBegGxXdImWjw6N9B_yguHGUXYTaq9tg8RDgq_myiN65F0siG43-ilcDt1F13qiA_KYaaxrp_WCVbbY4Jag_zMiIagdAvT5cUgxAjRYs76JOr8SMXieBNxfLgbz6R1tOITVK7ZIqe3a0sY7s7D1Uki0MUKqhM8H7GvKure7tr9KcjON1W9BQplirN29LKALo8-lqiPfTmc5W0VweEtqM3EQy4XGc9t-R3H-iF0meJHWk9mrSkBm94Ch5kCnZgDa7fGRIrCZgOOKCXrzyb5pTCG-0T6I_YOyA1y5ENN84M4oigVua4bek4tIE9E21qSgIRFrV9k3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=odzISVcNJGRpfVzBegGxXdImWjw6N9B_yguHGUXYTaq9tg8RDgq_myiN65F0siG43-ilcDt1F13qiA_KYaaxrp_WCVbbY4Jag_zMiIagdAvT5cUgxAjRYs76JOr8SMXieBNxfLgbz6R1tOITVK7ZIqe3a0sY7s7D1Uki0MUKqhM8H7GvKure7tr9KcjON1W9BQplirN29LKALo8-lqiPfTmc5W0VweEtqM3EQy4XGc9t-R3H-iF0meJHWk9mrSkBm94Ch5kCnZgDa7fGRIrCZgOOKCXrzyb5pTCG-0T6I_YOyA1y5ENN84M4oigVua4bek4tIE9E21qSgIRFrV9k3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=f3oPYNzcL9FJ2YmI3WOHPGDP6io_bHEYMtt3rucIwaNwvIx3_bKP4OOVHVMEJU933LoyahpDP1ysUjAdeN3YH-X3PAq_2d1fOGFHvGHWrmyE9EtW443k19YkRkKaJrVh_YxUpkHHnLk8bd33QSE1QaVJpp0FcCrM2xYoEMrjG9xJURLfbhcbZm_Is58hKPll2BuYvVikGDMq0QVjQ7d8bmYNOqzrCDBEWlDeKjSw_X5hmdinXW7kmTYUPy-daTIL7eXbeUQpuTM3SNBqMLpaexo32nWIeovzJrhvvz9E2nblhqD3psfpOrCzXngfP5cLs3rEYQa2UTd0xK99fCZmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=f3oPYNzcL9FJ2YmI3WOHPGDP6io_bHEYMtt3rucIwaNwvIx3_bKP4OOVHVMEJU933LoyahpDP1ysUjAdeN3YH-X3PAq_2d1fOGFHvGHWrmyE9EtW443k19YkRkKaJrVh_YxUpkHHnLk8bd33QSE1QaVJpp0FcCrM2xYoEMrjG9xJURLfbhcbZm_Is58hKPll2BuYvVikGDMq0QVjQ7d8bmYNOqzrCDBEWlDeKjSw_X5hmdinXW7kmTYUPy-daTIL7eXbeUQpuTM3SNBqMLpaexo32nWIeovzJrhvvz9E2nblhqD3psfpOrCzXngfP5cLs3rEYQa2UTd0xK99fCZmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drWzb76DQjvanHgv24H9WQ4y2PtouRRHMtoQbF6-4VvIMHxCpeZjHLsyY103ohORYvSwrFvnBjOgpSd2Yrii29WpgUxd5jFF94AX6AxAkyOqe65S98lfu1wRQx5qmdrh6RHdTAfhYhzC212LOXyINuuE1WMUCDjf65RUZEtxBkz5zPHGCVvez85SQ_cx_HZ7l0uAqhytcIHnlOb6Jk-pQvJPOdmsLz3QZdap0lSzGgwz2YWii0NB23RKtfrOALHkpZHbc5nmTMS5Pa0z1TbvYuo09EhxheyanLkT1G-t3xvk7_CdEnuxiyvcleyP-goXZE1y56x7AmxP7bHYJr7y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=Q4LX6-mxsggLEWIPU9MXoQ5YmgZVTOtyCi8DfMDVe5aEn3x9Ynj9Hwip2EGx5NgC23Zuz47PUr5icZH0-gg3SGHauVyKG6QWmNEaFK5iV-aFBAiaPfLJqNRKmwKkBLE9ZZV3OCp_2EIQj7L0Q8DpQrefJmk26PPml3toQ-iuvSwqB45l8utTUdQ_va3WdfIXV9Dt4Fb92McfzxjdC0rV2u25j8kr0w2Ed9su3h0mJRMSc7XEY1263kPWCTcHUVbwor3053ee5V6gAapzLc3IV4hjp5rT6P4r4SjuLSffQZU7Z4d7aW0FuKNRjTphK0TrLS5Z3fE_J1bRKmksg2HecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=Q4LX6-mxsggLEWIPU9MXoQ5YmgZVTOtyCi8DfMDVe5aEn3x9Ynj9Hwip2EGx5NgC23Zuz47PUr5icZH0-gg3SGHauVyKG6QWmNEaFK5iV-aFBAiaPfLJqNRKmwKkBLE9ZZV3OCp_2EIQj7L0Q8DpQrefJmk26PPml3toQ-iuvSwqB45l8utTUdQ_va3WdfIXV9Dt4Fb92McfzxjdC0rV2u25j8kr0w2Ed9su3h0mJRMSc7XEY1263kPWCTcHUVbwor3053ee5V6gAapzLc3IV4hjp5rT6P4r4SjuLSffQZU7Z4d7aW0FuKNRjTphK0TrLS5Z3fE_J1bRKmksg2HecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF1TRgS8xp3hHyHwupWfyLaMEXI3u2MLz_BmnjrM76kQ9Wg3lhr1VbPkNDq_l7bmeaSLwaZwfEKZYfpOMTmIrChszHUW7NAs-R78fFD9dTJErH8h6LrTcfmYZedRPiBR69onDy7z5QYJfV8Sbx8yBLT8EV-yzlCFa8BWSssjxrxukqLisy52lVGjlk7yEVpPe57b10m1yZcfsY73SCN2IYP6qqPLPocneSBTHfyH6Sy4T36gwo-LLWkM250wt8ek6f3XjbA4_nLQNMVqAkwWiqFL9JSLsvLjbjiUniKPec1rL7ZJIREwi01w__Y6UvYokZ1ZmiCFICgHphYnRgEqKho8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF1TRgS8xp3hHyHwupWfyLaMEXI3u2MLz_BmnjrM76kQ9Wg3lhr1VbPkNDq_l7bmeaSLwaZwfEKZYfpOMTmIrChszHUW7NAs-R78fFD9dTJErH8h6LrTcfmYZedRPiBR69onDy7z5QYJfV8Sbx8yBLT8EV-yzlCFa8BWSssjxrxukqLisy52lVGjlk7yEVpPe57b10m1yZcfsY73SCN2IYP6qqPLPocneSBTHfyH6Sy4T36gwo-LLWkM250wt8ek6f3XjbA4_nLQNMVqAkwWiqFL9JSLsvLjbjiUniKPec1rL7ZJIREwi01w__Y6UvYokZ1ZmiCFICgHphYnRgEqKho8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=gFRjPrg3pmDfqAummKdAOI0D-xT7OLiImragcuGhYEuu4tioG1Q91TGGehZJLvHFM3hdUjZDebifmjmYA9Lrv5ABzL-AIoz4LaZVe0NueBvkT-fuGNYQSA_-dblXMqpdC92F-iA72QOgHvOMOJu2FN2C6ytT2SVXeFpNvj1gYoDRdsOmhASJ1szjdZTPQrQkjRmzMhpg_4B9ZI3kybf2OwMkAt6-91dwchd4qq3sMKgHbxweKOryHI63fMPTIk_uxJbuSexF0eJanqupRn_YNB3aTRyg6wMdgst1vTAEHEX_ZU-_TM1f2ZGXFMKI7aHw3kQm0Q4SCBXf19XCkt9Ckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=gFRjPrg3pmDfqAummKdAOI0D-xT7OLiImragcuGhYEuu4tioG1Q91TGGehZJLvHFM3hdUjZDebifmjmYA9Lrv5ABzL-AIoz4LaZVe0NueBvkT-fuGNYQSA_-dblXMqpdC92F-iA72QOgHvOMOJu2FN2C6ytT2SVXeFpNvj1gYoDRdsOmhASJ1szjdZTPQrQkjRmzMhpg_4B9ZI3kybf2OwMkAt6-91dwchd4qq3sMKgHbxweKOryHI63fMPTIk_uxJbuSexF0eJanqupRn_YNB3aTRyg6wMdgst1vTAEHEX_ZU-_TM1f2ZGXFMKI7aHw3kQm0Q4SCBXf19XCkt9Ckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=mUgMuHvN6EaVIqw2eNkO3eEWEg1bLqqFZ74ThhRGh-ch75D5wGRzlrHUgT2O7llaxsaXF7p4Vs5VmWcpfUlRqqUflQZ4uwNRxE5TihDvIcDc1T8YK-OxZg2Xz_J_TSj5Jeo_fTI66Lv7GUKXNLGqUkoMFU3hMrZb8OJkjElAxgfSufnbe_UDZmmrc3oJbF29LhrlfMlR6aWu5Jtgv_Ykrhoi2oiJSbY5Sz22QDr_-oVtYnXaHiOP8uIkgvGpxG_3aMMbb6TS2K249QpX-HXLeDJnT80SOj147-iRTpZbFrdNgIbTnxX8lAYE51pXZkO6PWM14WHJF0WjYT8v-AA2rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=mUgMuHvN6EaVIqw2eNkO3eEWEg1bLqqFZ74ThhRGh-ch75D5wGRzlrHUgT2O7llaxsaXF7p4Vs5VmWcpfUlRqqUflQZ4uwNRxE5TihDvIcDc1T8YK-OxZg2Xz_J_TSj5Jeo_fTI66Lv7GUKXNLGqUkoMFU3hMrZb8OJkjElAxgfSufnbe_UDZmmrc3oJbF29LhrlfMlR6aWu5Jtgv_Ykrhoi2oiJSbY5Sz22QDr_-oVtYnXaHiOP8uIkgvGpxG_3aMMbb6TS2K249QpX-HXLeDJnT80SOj147-iRTpZbFrdNgIbTnxX8lAYE51pXZkO6PWM14WHJF0WjYT8v-AA2rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=IJHhJsWirznFnKyTt3fpta9urqs5y7TVgJD95d4NIRdO3U669YpDWrHyAnCThXnG6va1NutV6hft4QRP4LwsY8ocY1k4Xz8ulopHr_TKuWS5DFneMhhO5-_jFrO5G_5dGbKmDg3uoo4YwkJiRmrqjaRtsMVdJBa4JnQFswiYy_HvIgwpZzuB_1Ywj_EB9bkpbi9yo-ALTaT5QZoZpctxN8Fj92CF3wOVFJtpj6A95QNUM4Qt6vC_K54uVKIOHS2twizKt9Pd2GsdtHE1b5u4Z1LOlPLI1v5Hasa6dTa81ASTgmU0bPvY6FPDK2SZ12n4CZNPaMPxTho2b5aTAbUuITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=IJHhJsWirznFnKyTt3fpta9urqs5y7TVgJD95d4NIRdO3U669YpDWrHyAnCThXnG6va1NutV6hft4QRP4LwsY8ocY1k4Xz8ulopHr_TKuWS5DFneMhhO5-_jFrO5G_5dGbKmDg3uoo4YwkJiRmrqjaRtsMVdJBa4JnQFswiYy_HvIgwpZzuB_1Ywj_EB9bkpbi9yo-ALTaT5QZoZpctxN8Fj92CF3wOVFJtpj6A95QNUM4Qt6vC_K54uVKIOHS2twizKt9Pd2GsdtHE1b5u4Z1LOlPLI1v5Hasa6dTa81ASTgmU0bPvY6FPDK2SZ12n4CZNPaMPxTho2b5aTAbUuITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=QVNBgNaHR633UCO6lODt-NbuSLT9BDodYam2zHZp59-ydvIL9M4Ari4DmBU3kuDt3C7-f7NoQf08JP8i4bvl-NnGotYhfMAVZfZ31LzEkN9IdH9DojWTbel4MX0gbleOWzsTNPU8Em9PbzDZx7LW1CuYZNJV-le_Mai9l-A2gVXPbr_SqNQ753-tQMxDiZOpdaBbG0zOU2Q4vh5PZcY_zRkVB4UDW-rOj_WIG8Jf3joW8UWQrGvDUzty4j5k5uZnppA40XEhNkW99wh-lCbnTqxblQPtsAnHqZfaqG7LPnf1DUMytro8MBakuBVzEsjICuZ4tBsZJRJJKU4csl-H2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=QVNBgNaHR633UCO6lODt-NbuSLT9BDodYam2zHZp59-ydvIL9M4Ari4DmBU3kuDt3C7-f7NoQf08JP8i4bvl-NnGotYhfMAVZfZ31LzEkN9IdH9DojWTbel4MX0gbleOWzsTNPU8Em9PbzDZx7LW1CuYZNJV-le_Mai9l-A2gVXPbr_SqNQ753-tQMxDiZOpdaBbG0zOU2Q4vh5PZcY_zRkVB4UDW-rOj_WIG8Jf3joW8UWQrGvDUzty4j5k5uZnppA40XEhNkW99wh-lCbnTqxblQPtsAnHqZfaqG7LPnf1DUMytro8MBakuBVzEsjICuZ4tBsZJRJJKU4csl-H2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9uNRKxh8p94X7wYNEVN7tzrU2_1AIia_ezAaBy88cMAuDVzzAKMA3XKtqTfRNyf1hMCvpS4sIg4hP72socejxGst7kvE-VXplyhxWloXVg8l1R5oweTV1uwQVC-M2HE7gq9mASdxBMxxv1ZLmCTiSG2zUBvpK60_nnbS1a9csMZjOc3pWGLEHXZuZK6F8PZSOzLFFUD_mzBV-gfJfLGAoL-mNz_Ety1yliqlXA6Kn3uQzKpgtOdnzeBfgXP3peN-u9Edvx96XTj_HSO2crAPfin9M2XtRY9YER8a-yBbQvcbaYvpyBMEhb-31UCml0gvCbrvhxKj5shFHOFckcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1fbqoZ2L64SCFfJhBirqu0nQ5sPlv_E6wwMit9V6ka6NWGlUcuWpU9rsVWka-6mWLG3p0gMu4ZGhnAjC7rAZT0L0YdYM5IQea_DCqKiSZ4Dst3P7noTn4DdiKUWg_UaqbEPxsDKl9V4fBzv7rM3ftFSQSDWaEIKrsVh9fbCbUgdFkm1zWlb5wOw_EWeXN-Vg_tPkAzYjNBAiUpbpod-uryQXGE-USLhRSAqLePGsIZHTCFxcdpIua40vAIOjhxoSqpvyucmncmJ79t69iDtewZlepw-BUE6hdT8RmyYvQQ4fvmHxwwalKS_W8yEgF_uwXBSfLJwxgI9R4ogMuIxfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzwXnwyIslu6P-bSZhy3hwnDeDFkoAoAwoGpNpUC8CcUvKPL_ueP_pcPZ9cGqq_FLXcURkp5IZ5tsC5pSFqCD-KQf4hO2zguOdnnxE67_CuwIOgiKcG3zy4btBrDEbY3WXTl4TO-3Y1NdykWcBOuwYd1XQpwU6BuTVHLdbaDLKX_J5INP-BGONc3CiAIKpyXPsLBBgxLtgQKuWSXe4bcSLTWmHfZZs8plY_e832QEuUUfSLU2EYVYuEVJQ6LCF_NGu_fgtYIZ4KHDhhLFwOTGPVZSFV5a8Tm87-I19hLSZkQCMXwfZW99JPPkYtg11vIPio_1US8BHHiwMhGfth4ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H56SZa268MPBLiCRUUOTRl0n0zhWFPM71IGrAwqFAHs1aKs10yI-prZ3sx-7zMRiyFPY1nThkc3-8g1Bps_GI7RBF-crK2WZzwtBpY8s_aAWaBXf17n6AnJcc3fDOpy0glVZAfeeP5e0xZmH_onBsPEV4Os7aVxTnZiohveITx3mF-x0c9cttFcRcbVJCBICQffDwpnz-jsNV5JV1rQFVkqLhsqf8hWFbfoof_PkmnsN26xR7VmtHshrCL3sPLj1H4HuaME38BnHeQ2cebxVrHWfeWmc_6c6Q5XG-G2yKfBCEhmDiq6lk-sfmhcV3W_lIoxD-8FRCSbuGUoEpCNUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mBWEODzbbpYXC9slW8oV-gG7s_3hoQP8FwTO9xVPHwrpnl1AhSBSBNviRqjlXcvQQfd3ZAxNEH8Im--_juTP-xqNE7qWofvRvcFNEsG4AiKrSAuFtRWM10ktM1s_56GfC3pIdR1-tS8SyIoYtn3a-cNbFjVrWKwFITTM_cI6uvVvpumvmfo1q3XyqDnO57I8fIcmBx6IOkdyBawAkMZPugC8hAkNGIU-VgtSpmJd_0z-oYUc6K_Zhhv8ubjeB7AYfzsA2XjSt41kM1S9KtvAzXPauf7q_UUUMgI7_Rv-FnlKrvfjHXY5SIGRbSkxLchG0-w2SVDvNMXUMXzlvLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu2WwU7aCqxpDtFqqC9uvin_WAR0kaiGbqiGbnnoFY-vXGHoKxMsBZzpFJyuIN9hAfOFli19CC10-UyT2FEUXQm06EvgCNgiuREIZiYeQJ9cfm70MMewhzFrGucWSv3AltmY8vgzwXMDoV2kChnywvi0jOFfXoBd4PuAJSKByxfUidb4fKM2NSYiDfGHNxefL4b5_OpeXLd7qCk5lJQy8TXOQOdDVdXSO1A5WGaOTzg9SurrYzR6EpOCY23CpoLBiSoTylw0PRAKn-7hIgrwcymssAfbB2If503uMuSCJeHeSF-sYAaL5lVK1rNO4oaHagN1VlufxFwaqoivozhxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=OnlBAk6ijsyOd-ldeRJ5ODgMISQd723V5lMZGw9rmH9xSk1fqx29cH9N3LJ2inDttZd70ODsOjO7treN8gyqd6GVje6Yye8r_HTJ-z7vPFtyU7C0CkZTsMewF67ICIXq-305YpmBHuwQOoAQt7dYQejE4OLYt_v1ybjXpqX056WhDxG7jp1jZvWEztmhvf_TnZyMjYTLpOnxW0GGvys4_TaWOTyLGkysy9rigLP7TXdSoOiqZXCU7CWZWMTUhuYxBSA0sOlG86SeGfl4C8jhqb_MRYdXCTzUhAlHcDyPXBuH5uBQVLumZWvBZ-bVRCi1uF0Wkqz1M7Iu9ccJjrSrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=OnlBAk6ijsyOd-ldeRJ5ODgMISQd723V5lMZGw9rmH9xSk1fqx29cH9N3LJ2inDttZd70ODsOjO7treN8gyqd6GVje6Yye8r_HTJ-z7vPFtyU7C0CkZTsMewF67ICIXq-305YpmBHuwQOoAQt7dYQejE4OLYt_v1ybjXpqX056WhDxG7jp1jZvWEztmhvf_TnZyMjYTLpOnxW0GGvys4_TaWOTyLGkysy9rigLP7TXdSoOiqZXCU7CWZWMTUhuYxBSA0sOlG86SeGfl4C8jhqb_MRYdXCTzUhAlHcDyPXBuH5uBQVLumZWvBZ-bVRCi1uF0Wkqz1M7Iu9ccJjrSrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=Tn-ABwGTO6OqQ7zyLJVpQxhkIt2R9rrfL1qnNx_wkzN10h3Bg3TZBuuJTZdN6gxcDxhp_4Bv27n8tbpCAMLoJyJieu2KKnM-NObPXQRLxz0uz7GTjr90G369IXZnXEDmFcovrwfavDSYvLORi24HcPysxCh1EtGjprKxtiAhuj7EPHG9p9O2tH-5TEBb2Bl_sT21OHumAMw3AcOVHFYGcPt5uUV0trorXAIj1Sh3bbN2RBh9X1etDbrzTuh1lTiJUt9nsHjOv7ltXKt6pvr6cABGOFOwtg7P-9s6g_XYf-ePVqQZiyg81l5e3NQq6UvvlI2XevrL8dA8NSz2AXUX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=Tn-ABwGTO6OqQ7zyLJVpQxhkIt2R9rrfL1qnNx_wkzN10h3Bg3TZBuuJTZdN6gxcDxhp_4Bv27n8tbpCAMLoJyJieu2KKnM-NObPXQRLxz0uz7GTjr90G369IXZnXEDmFcovrwfavDSYvLORi24HcPysxCh1EtGjprKxtiAhuj7EPHG9p9O2tH-5TEBb2Bl_sT21OHumAMw3AcOVHFYGcPt5uUV0trorXAIj1Sh3bbN2RBh9X1etDbrzTuh1lTiJUt9nsHjOv7ltXKt6pvr6cABGOFOwtg7P-9s6g_XYf-ePVqQZiyg81l5e3NQq6UvvlI2XevrL8dA8NSz2AXUX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=WEVrs3ftP50H9IPh3MYa7S8q1g1nDDUYeMOFmRdHuNMoR8rZ6ilPGBwPodCbgj1u3_SqDVwPQKUl4AYikHWdzHXROqXFFKuXT7wrGQayxYQYTZpUTXHXhdspY86k9Q1w_SUH7T1MA9KLM-RBWIb-OOjNXo6umxZxF1mcV9aqBZfS0jCP9KOiW8DTkDcDbj1xxBdl1CzPf-h4sTFARZz9xmbrkqE3819YgXBIpYOz7-CzFETCK2VOpdEDLYchgjDIp7qnIzHTDGVeIdx1TJAilYUZqNToJN9miZPBpalLjinLTZWpMNtnMxgqjktZubrNgSJQOslxBjSbPX0TflY27w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=WEVrs3ftP50H9IPh3MYa7S8q1g1nDDUYeMOFmRdHuNMoR8rZ6ilPGBwPodCbgj1u3_SqDVwPQKUl4AYikHWdzHXROqXFFKuXT7wrGQayxYQYTZpUTXHXhdspY86k9Q1w_SUH7T1MA9KLM-RBWIb-OOjNXo6umxZxF1mcV9aqBZfS0jCP9KOiW8DTkDcDbj1xxBdl1CzPf-h4sTFARZz9xmbrkqE3819YgXBIpYOz7-CzFETCK2VOpdEDLYchgjDIp7qnIzHTDGVeIdx1TJAilYUZqNToJN9miZPBpalLjinLTZWpMNtnMxgqjktZubrNgSJQOslxBjSbPX0TflY27w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCei6TVB_WRk3qTFtPl3F7LcCBIdVFxj7vQD8hS9wYHLEacnWLTRoVHlKp0ScKY8d2o0nmUnZTZxLwypzhSVxbac5N--iuxssGLymOvah32j-13pFd91Z8qTrQatqKe8sH_rcGxDy9eN8oN-Pdddc3ewKcFj40WAyPbk0T8iF5sNSPbZcTcmytu946EV3JiSDlPeIkMILhCbxic7vA4i7x4xMd3EucQyacyPWsuKhCB8pOz8KGHb0XbWQZLIz-jLHP5MvKmAuHoVnkDb1g4VFuC47B84P5eFFOe79MkcIowm5SfpxJd7fu1k5I5f4WFWIVRV3M_KQnvXp0UscsA5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iO0OJpv0gTLYePIC6JzMtLE5JPHAXW3sWyYrZ6N5ms5RdzFudh935hda8h1w7Z-OnayBr7_fomoUSGBCM2jxgDVYdydMPDscuUsSxLQbbpQxy46YCS8H2CjvpUsgCfCVRC-Kcsyqv8qQvI3oy7NfHcD9GN0JyNqGpzc4wpxxUB1CISWUZtLKTCbza4LgMREcNvJbNSG0A6D_lteQtMQvTmHycEY1jIgWL-kSeXyeF4fecQWGFFw8AZBMBIsCY31ksqSffPYQ40fmZyHM5Agdvarx64dKdX0PKU3mPKht3594EhEm1Dy3zYhp9_DxiC4_8yFBj-TnA1PcuauJymkFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3zCfWKGeO12Ud9eT0FAcaKG3kwGg4a7u7HIzu-0s_c3zZXrhJfEuc4d5V05ybk91DqLlCMBIow9PfRTfFCJzAFnFKRi6GkRsIwTxuw-wfVrkqkIGPoqdKgq8nLofmFzudx9oLoKEkRZnCNteuWRN013BsfXWcFtVXNYzByumLRlqVC4sEDRjnYSMFpQxBZVDAvtooyV4prMz4pDnZ1dXtem9rAoE0RwIP4ZelIogG8l9Ubh_-teiPk0JoPwS2p5OjahwRLOsiDlcn0OgS6NR2dRuyrwzm8MKUdSrfLS7l-YrElit37niSpLVV17wkheU2MNF4RdST4c-1CUD2q4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODR8vNNhdNrro3trBf78mdE_rO9nOfjvOptM5ikg-J2BPxsYk0ItOkxzZv5EF4pxR5F4CVkIWygtdijt7LjImnWXmZS7IgxDZ5Eay21ijniNPfVwCNtzEKFjHKZg-OTqsXgAlMpcy7Giw-K0filZkmZZqPOyk5JP195WDlAKALCwkvotknRN7450dU11dvyeTIhDbEZbRyRJuAz_gzflT0-2WTx8LE10Pmqxf7OelDlW4bTTMqrcTbVlEcW_8Lg7V5LsmNixp8k9XhYv8_ZaXqCPBZzel2whxIMJC3l6-E_CCQ0bXI1JB8AExFm3xt-JFMCaTaGqaz5n0m_AHupV8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILzVES85_0xrwu0fRF-s_E9kECH-vU0dhuCpGFmkiyrKwT7rk9ceEY4xmXt5d6jmSUlyyRoK7vlkZKbXfqbPN6fVHiNv8TGN9RwKKMfzxXp4M4wmlDZmmWHEoMW4WNAYdkHbYxtwAXBGd1k6mn0Y5L_TQnYKBrjfWRORMopb99XdU1R45VL15ZQol4UveGaNK_-ZwnTYwTN1NnaHt4XI530W8003uXoncAcRia9sUPOW-gs3e09ugyC2kiwSTH5AlGCyCPbX1RuNubooWdB3IPtZpnhNLQK4ofkdQpccaWp2dujvKTpEHCZNkyNbiom4m8Iem9BmFtvdn1XuVJxRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUAdpZBUxEBRarvv9-6eRiJBqcWBdNMR_bF2pyJq5t97lJWcT7A8t_TbpD2fDSh8spZFExccqIEonTy-iDwr3cElV-JxZttrS7LGBwP2hrDlxLfzCcI0hfvI1VFfSt66D0M9nlp15zeyaH3VZcEdidBvFjuyace4rBAhAulmRV3LTRFbuB6p5EIVOUuIfd6GnArEBlcP_OfR7FLgyEGp8eEOSvZroQrWuRkflTMd0mddkIaXwm0ddknreVpiD6SHV6rZr962HxHi6wfu_GnMfzg8NAiGyvWMSNhIm9lEcVQO9m9ggJcOGyIDawjCZyb67KHh_QFv1evLU0Pah7Bfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2pfLTJBwrrOnmT4ZT2oi7mZY6MXerLCwrEiwAo1aInzWhvooJcwLwpJvmmwWyZ9J5M391cuJLW4k-rXVmrCBn-EWelNVMkF4WXXOswLlSTaVXAeXEAb6qut2YcHNgV1g5jwHtxo8lQSwRQvSyR_PWKpQWVpsl_knDsYHQNKkaIUbsC4es_pKov6cBbseGyxlbAatPErjvEOJ8aSv4AYtyyf8gJXYX58xg5BuPctHEzIEcCWAfHKn93KRVHgbZpgwMH02ARfh96yz0sswLA-ctmCHvsdlpp1Caj1hp4uwBNdDZQIR8878iQAa0cUyB7tXraBJ_70J1W8CxhlOyONHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADaY8EQ708MB7G3iOhycGh_mrOAxzIlOiPyGjJ0G_yfkxfBieilB-Mfhvse0ToksAGzwdZfBngPwbcKy_VQdoSzdeSxQKg6cvKri-1w2IYJQZ5qq6P7Ct3PTYXlzXW5pifWZl0-JG5UCBteMpuGdkZke4MOvQrnM2tItZyM1mPvPf294T1cOXA6RlWqlQIH7-RKnW9duXtRXBilXISXVQ9HIWgYsLnsfIM-WdmhE4auTHjo88iID0kT4cRMML0pbZE0EiMlvAv4qu5Y2Lj1XpKiS1LDiG8fnMmoZJntdqS1OK6mvZPeA0ukx1C5vBIUSZsRTW-RrrYAWfDO6zOqrRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHmgzTZgAxQQsLXadvBReEWkL1GBHgk4itU4I9aZAeRXwb6xn5lbmsLatinXDgYDWvRo23z8FEnbHknnkMjPoUnY8JkZkr8Yoyvj9uZuzV9Hsg3pSZa4uoK1LMtzN_qUElpSYwHlnkBXgwxVnfnP41kItqN5mMVioZ5IiqT8smJmCdIYufjaPFnAaNv6T9PGBR2rNOlpXQBEsFim2o6aLNAREwwxKgOhIsInYrfCEf3Xs25TW-kkdnT6G_PI4DchbYMeAeIFiZDWQoN4X2zodOIr-w8mZhQNpbMZam5_n9sD6HdZJ7kJgN0IoaYyWxiqPrJlAss498iPThXfjWJVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
