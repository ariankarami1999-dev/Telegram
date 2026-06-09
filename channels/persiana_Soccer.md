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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 168K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANE26Jvjlji47TEnt24oP7NKGc4OJpokUeBujT-_NtmB37TsLA4xki6XNgOB_4FO6PU6C4l3SPbxXlUUdOHUejN_cXN3JEOp9Yc8GQWcm6fw8SgCLhKgrDO-Ey2KkZPbovuWJ6veguacRrvjnCNljSWEsKZ6KP7cEaRAP4BeRJqiw7SEzshcqhXwMUHAV4Y3Y4Q9zxLndxoG4cR8w-W2y2WkABC1RkZqeXCsbmfTonnCMVOTiLYzgNEOtHZtDvvLono2pL0daM-WDNseQuRmirwWX8WJoL-qG2nFt2kUE5mHEZhNzZbmJIAPMygkRqeKSkyeuoKOEjxtQe70teRTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doe6HpzWEAmBSP9CwHU5QfPf6ThasTg597v4qfLe1S6TTzTqtxravLTib2eTO9czTm2Ah1UvFnPOy0mpiK-AUf05suGVrmKgm0DdSLxdcbD08YpFl2I7AxV5PrRShH7IdshaEONBsN2UPhPMr2ipUbP-9FZ62T2STibAwVFLsVf6rEaFRjwwtRYizxzw2gPg29tIu65fwunauEEr-RoaMfTNMLBJc0wDalZmx8fiHoKcct8xitwZsya_BmV5ZJUMmuBu2gDy40-L9jdB_uA9dLBUGbIy76tqVu-C5TCiIN6n2UoZgHeJRkd7fcLUhxHAgCnSYlCu3d2-QLWIkTfKXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUtERQv1AgZCIzvtSRW2ZINcSj2t_Z_gK9XVuiPf-OvQ_fPehHUcOkAgo0CFTVP-MJt3uymcTJZiZQqf9-x6Ro1hijnvbIfJjRDyqUMD9S4kY9aWbZWxz_yOZaIZWz-XYs22R1Pv6CX_L443FWL84FCGSFXTBAPyX29EaVw4PncBvrzvED7SzIhjnTD5-WdykvYQdV4IW1_cEf2bW-1u4w-SZbtKQfh3VBaKZlsu7Q-Whux8QOeSIMa4OOslJeVu2OmK_ZAD0Qyf4_LydKec_dPenNuin_ZnvI1p6Fh0QRCHStuRIvMKO3arFA9UgaobWOuJ5F9FwwFqjAf2f4tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz4a1_mlJug_vAXN64iUKagOWQDlox8OgPY37iTjBLGm75T9WWabPC594McxfjtVriZYy0rzLOER8_VAUQeMaGRsLUzSGWt4qASPe1-dggs0cPF_UcGfpp936FVh6jtJP6lbsU1OicTaOQDWrCeItb0s0eVdY5oRQeGG0XW7ygGGYUMZeCO8uK_00l0hXs3kSyltx_OBjgbm2ZDpYc2x7nVVKSOQmc4twtcrN-QMjN4akG6WwTUhOV1FaQ34C5VLHALau4e6WcpcoI0Y4MiByV_NvQd1eBZM7Q8xxAWp08ICett3eHZlY4vilNggMLzG87oeup5NmZQ3_ltm4Vjytw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfeD03qy1tcb-6wbXOcoz_OBjZmtacSKMqVRxY8QDwNIZpNFMpyRAKWWAQQ6eG3khOREu0301xJUSMo00ZVYSd-zAh3l4JDEl8Dbwu6lPsgOeoRLWAGJK61KTbmTVUbUNiT5t3Dh3-kb8iiSidlpQSYhfkVTqZMJSO17Ez8s3xu5PsOH5ZuT-cxHnIPPPqAYkE_oplROqjZd20FGecKFGmtRf8-G6TV_v9p1tkrm7q4-_Pc6hjcldlXEBXVmJDQ7DvsbT7wfUsIQzwbBydy6Nu7_gF9z66W1oPD0ffKteTg5bzF_n9ymcby_YvvP4BzZ0xjoh2mvLxo2e1o4aQacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XevjfzmXyK09z3O4UBkLV9jw-ZNxGbk3TExdXVHm_aodB90AF3aWc4D_DKmpbim6t43QDQzslRmN8zRrmZbdYHqPr_OTbQk4EuibAub0zwyEco5fNR8U_uc-RriCcAeKTL34L6k2rXv3hw2wSKeK5rXKoFUl8xU8d7WQEueSC_Aeb9G2bjWAQsLrHRZYSP5dkf8ADBwD5UaawiAX_P8BLUVyigZcQkFLpqBYeKGB_Oe6ey1PkBf20xVy-L2mFIV9ygJ8OQK55bm-xn_UrWRKNqGcLSvKvLNaCHKeoT3qAfRfE6KlItz0KJX3qEqNC0FbyzeI9Y8YPqWVIXYvFI6AlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23086" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CmPKkCYd1EIodInutxIk7_QSzFT_GjyZRWFluSl4Bqc_lXaAq8Zk1w-ENeYirS8g8piNQ5pktsLqmIKUcF510RzwY0pN7GtntIonCagxAeO09G3wHbT2xMNQ2iTpQyVVljuRFuqb_IsMvd3GHCF2G6pm2kxNdZdNGwQFTF_YzBSVanB78C6Zew1fWQV14w0JWBi8GEJxVx-YeOHGLJmMNUqSoZdXNuRGn3bwWtP-ykjsz1zLJDNKfcrspNTwT_2aCf_FLydFvmeQVjcztEyAhaWrFao1Ta7cgj0_KPXC93TO1uu0Yx0djSz_Y8-S9GEt5RUTTMkeM5NwGQ5xpLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m84KOmFAZll9W9oPfFSok7x24ob16TLN10dakY8CyH2KQKKQPVt4nf1RTa1TBLd2uJjeRbbS0z9gZbfEHOJ_7KIiJAAY_c3er1qmt5DrZD__2M8XF0jNC7fnd8M0lNh7Z3-2oQA9Sxf08krPiIMUUG4y2xo12oDWxv4bHw1OBtRqN8jp9kN6KlrOpeGWns4o6lswjH32MiXfCUwQGwE24OJSUJlOMinnWz17x5VKZ_835VhLP4F-kqPtJ_vebZEzfbnW_tXsIxsL6HtzADy0_iEI2JS9AJfnY5dvRd_s9tBt8FgChQYkWKkpXMARhaNjaEPWrQFrucAsa5ZxNzvUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAh6RKnCrrvLOXBQtQCnK3XQGOUrrUB-J87LqMU5nFW75xi01zPojgY2bIp1I0h2aoVwRcLiGtbxq7z22Jj3CRvN94jJGudylfwAY2fx0GSHFddiLSBMskCM26RBp6hCTn1yNnZE_nbEn9kBeYstZuI89VjZG42sX8uFmfEYM10EmG5PZluaKXY6CnF2aWOvFRMz0zZjdmo-uHuqS-0M4eo8RDvROq8Amr-8Lf-_kMbNn9LF-HS7Hn0TWW8e1Rwh71H2eB5QdTEa7syRi5DO_MZNQf4Mg356d2JpPoUlGXNaM2eOPODDD-pZityUhRl8j06BQ0ylBAP2vJGAKeEjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plqo5dYzzZn7C0XERP1tJjpRAE7fNuxvzIrzLkeqba4ol3peoN5tshFzSu65oL_qATS6q0ki2Ftjp727Geelz7XaqpIsGk6ML4K-Ux4mmikM-gI4T9eZkpUPiY8ebcumEJKTwraT5wP1kh9Tb5qRYjUp1cYYTWYx1AMIR4qxI3y-F8EMcDQBQQ23oImcDsIEF0TDFZttlcHcssZ-1R5SlU4rL7ZnN5oRwvY-NSXKaNgSYJ_oXnKLzr_MnQo-y7oeZhH-wd0VrmGOl-O3ZJf9hQJXAPrIecKJn66s18YlywcyddLFwBgdOPg5QoPse2gYjkpzii1REqGnqvC2_dtMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLjS6iW5XOmFxeKOiR4Qr_MJ3N7LeMaeOwzTDWBhIcJ2SaEgPEWCFDvKgjJ2g2nu2sVnhMTEk3UGFDHlc-9no-y2zfAV9SfIkJXNCl8B57GIO8kT-jkXHNm-tWjcq0Yw0zSDTIlSV_ZOlf0giTgtKSW6IXmPCJOo9TP2rX_H3dUOzlFA7aGW8R0kLIjwupvDZJ7Hibaaz-nFqrruIFUvHeBdBA8PVf-9deBdkb2KejT_iAseyo0kV8CyAAZnazpOxYin8FSWRTSXCQcLVDIE8l3VqfgErbKmZxiJ-7e_IkaBSXkY9OjjTOLcLEtoM135itOWypxSGO-CN3sUl6eF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikw1YtQZ3l2N3Pgo9r4W_3I919zdAusA5RJ7zQYsLTEnH8cvADpN_99Q6SA9Cl2m5P1IRMZlb2ZAnJf0IDT5LDgdRM8ELEd0pTTA7YluswZhxE0aUcOWLFjgVIRhJQwXkG_sDRNiYY0tB-FIUeR-pE7e22j1-v-0hV5mVFb6Oe8o7fkFhhBci3OaYFiwxLjbRWDa2LVG0CoPJBnoJBSBZHyGNXiXYRTthXkmRU5ixMKyzmUEMpm--_qTw08HV9TombBx7AjtslgUby12OjsVetKUk8jlnl4E0z4qs7wsBUm5J-Ruund0FXxJoZSWiOJU4s0X4yxpL-NMxZUjZTkfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJXhW5Hj9-nlvwYpTbquMS1InRozyf-0CvB1XlvZ-fZgyWM4ttc0bDcmDkhVfw-CjdEbz2l1PuAUkIrNi-DyH7UbADbNi1x4EaHn5Y79QR-sj3Fssv_SylujUg719Al3kh9_7e--KOYbKi5vDAIiOIsVknPYByPhTQVlcZ6eAlreD7ENHsG_A1fsLRgTSm-DAyrCGRgy6dovJi5zbgVS0XkWzAnG3GKD3GPvU_lCd1XcoGTryr3Qj0iOgwXCrTFbSDaPhHmTMYe3K39CQ3sFn83d7ZgCOkF0mnggkeQLLvdkkNcVNo3m3HA3e5XC5soCsQQ23AGrSEsAGxcd86tprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuPSBR8UKVCJIKtyEEEpY1w4aCTdP3HigiQ7ocSCETfcFhcAkRZqirq3lc3-ymZHRbIDR8_wGLtBAiys92v3xqeMIY7vVMLfUeXdeu0nFYKielemlVaxaENI1LNdV7-Gx8uYdygEIRyXcP7nHZ2uqSVEfOF4G3KwLywgzjuETXXaTMqYEe1r189wkMXzPXmje030u5xTmGpFXlc61KqZEVVrHq-I8bSpv7JcGPGsU061PLsn6O1d1OvxnzY8bsbEmHu-Irv0KN51i0AX0za3leA6MVhc5ovtYX1fPcBFJ3Bk2FQH2OVlsDSLfCUs9VypefPNlpx0GY5uW1tejYQJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzLKiMLJ_AqxtovkpbuiiFgRVNKCT0ST644VGydxJPQdhHgTffwlmlYNPLsFNBGaRvvsUFgqWdvdSwjbjmkBjqh2T7SU9QhAM5DK-e0i_ehnIqhTB7-rfEpVXJT7qBVlPdkOP7229ykCFm1v2Jnl0pO2IL7t3i7b85U-NJyuTjNA3-U64gkrI2yiN9eUeul02bOrP_G0avFBJUnZ8anvKjx0kJsfUgNqmCZP78ulFbdT5ifMCgJgkH-Bx79n-RPDZRpNSqL3Nj-0S8K8ZoW9BCWZp7jxakwN0eWkbCXHV-x4pbSoX4mIt-yOOj08UiVhEl3a98jOuQwDpl71T7OhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbeo5SUk-3EwfvE7C2Bbd4GQRYCS4IH9oecbldJKVY6tuqiiXPOlLRp6jz75RWaP6JHNPYPIPpHjOOr8SWxNTpZn2gyErMSztHrE2FJIqowuNCtk7sKAf0dZCmgQQEyvccEAErhQH1E1QKveT_FQ4MsVV8xaeElO8CObW97kXVnSZ8UYZ-XX6qWimVFwqI0wW0TDMH6dNHIbIrSjhb3ordt31DbmJ6lG3WX21mw7AkLa7hoq2uK0sq4qZD5VZALAFSKON5Ak6bCORhjXJRk4Y08IDi-rpTm52GW5_Nc2S6xpDWlfkfZ3jlMXgXWPykxK90hu0aNRFYxsmqeeLmQrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23063" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucx_P6uuYS9GwoLfxMfV8GaKQ5oEwjO6zgbQn696GdCZyDK-nPze5mrRaS-RtWcP-6q8vOsnXYmkskb5aTy98lgM6gwoBCZEHAV6sP9deT2TdX7a45DOl48G6RSjCX9O9TKp0ATmGEVqrggrT8EGOiARRF1PS_1gz7-_lqTpT-QeT5AD-GEIkX8Dzw8z_6ZxUligHlMPYCl-mBtAI3_lPi2muQAdW9idtV9iVdttF4hMbbQuGTzJ6_Y0kEdM7TJNa81Ac7TAklVyLhHXv-Oh7xPGoUloENBqxIQXMus6H7SW1waFUznBR99s_V4DdJkg-U_QnzaQGqo5vsKJmjHHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERp8XB5qR0oFodPRNObpV7G5V0EFm1w2RNRcUe1J6bvW0vLRKkJ9WtOt3ukjsz0OA8i8FKkfrYVG7Uhuy5Emwfad9_UgexF_0-NkdURoCgR9AtxZE9ETTNxNkKW1Wd8vX4W3TU81DTgsWBZN7EMqugn9cBNigEyghW5mB8VRyj5FbGNaDYEBZLwjm3nnBwD0i0S54d9wKKFPZDBW40EG5tRQXSPFdoCb-Fzp49hqb3XMjOuy_HaYXRiYcorQM4G33L1ssxcyaD8Rww1EjJrZK81fzxz-r9h7jPBroFp_5rID3aWeUprSbXI-lLYwi_vawrnsiFP0spkbDFlfeodZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYuriZaOrGO81Us0O3t3A3L8-wAr3V0MNhZ4VFh7kp5UP4KmkoaSpzDkE5fpelga41IiN7ZmoKIZYDaQYaBJCDpenOIZyY4RGTBT3y8ZWefQ1D3KNHwf2pl9CWs0MyQvVHL-b7qwp144xweLuhDSPRsjBqQ_Oprr7a9mYbrTllI7-AK8MIRqRdfbDzXQCdnheKP7W9MhuAwiWi9dG8NodR1nZNFoubU3UJ84n-FjfEO9HlHwJqbhsg7WZqyi2G50y8Ce5PiEhar0K-glNFRuwsttmuoNb43FQn7olxtFwprV14cbTobAH5eUTwlkWIztoey_YA7aYh3Z1D9OLPPDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKEXbwrP73nV1zpDd7UsaS1Oi2IuvU88z2fxotFTvLkpDwOKbXfTlqKn0fRfyZpYDLrqiKAMw_KY9MPPTH_jGavv8MzzK6WkqkJLqQGESjLBafdLmuskMtc5PomsB9p3qlMj7tItRRsLleMwHuY8WI69HFGFjHMPUG_YOXSGjY188-OyGVihvczrC-MUGhhXz9FSGruiWCP7BoNyoRsuE3vNNbL1Y93ZSm5pMZrDM8C-4XiObgfBgRHE-7Bi7p02OrMkJjitD280tvHaLhlRSxBKxiZVaVYqmpJ-nG3Y0wfltCHyum4tODknNdvB01AoWbVkYNyiuNephljiLWnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVt4e-We8f5fJOsYq3ZVzQzi8staSJpS_BMoXe5ke4W40oOnPwPcLJmcUIexi5I6gHx78VA2xUtwiCm5cCbRpDKM0FhEH9crTOSrB6GOeLd8k47kIuO_kI5nsaGK3uvQ74hV3hszZI0GzQcpZo1wJDzCNb9B-EA5G9jplJTKOi6NhirjOPG4V0FwCRYXLA71a2TcCIR8gv3xmhSQM7_EtaC7Ez5w2OpQlDu-yLNFAD3XaqOTwDa0nBwSzYrr7d2zdEmuxJudRHTE9u8qnRVDhgi_NKgj30R-QHkSeJYF09ji6yUV77wi-i8a9l00gruaSMU_D3gJjJUolKhDZIGeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYzKcbgHGpNxCmhlzRWoc5vVQwS7bkwLAVwajYj-K9Y5FhiT9QGncRhsQfqON9hNGgPu_w1znwu4CPV8k3zpXRdbnmMl3W5HvtaCLJIKI4J03o_ivPFLfdaGNy42azuJ_SdQyu3jewpPZjQi9u5i_n16oQUH3o_rp3XdqktAFB9R2xkcMb_1FAj2EIYcLBhDKFpEuOwA5DrBg9Oh010qoFne3DoFaRaVZ27JDFNuP9XAhhKwbSyrzzR3Dm7ergQZqfB936v7TmvRyS9mJKPp6FS4swNopP_zR49fhdJs2rofas-aU_QA_9N_R8hCIvXalY0Q27Jlo_5cPKPHSI5FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NR0ZuIs-LgNwQ3eKDgjcw67yGZ6FIah8RXvpW6lHZasJ5tGKvJ4nxV15iY2HIyeXLoTTowqvaTE_eRkDWBLh7R_maeJt_NBV5Fbd-srNskknSOdfDW9ncjwhAREO4Jmo4k2ZcLtoYDGYHtLK1cZUKG1n2ul6xTqzre8X5Hub4Aw1PHOt-7v62hthC09gpm29r860tvH4AUJa1JqtSvZppucgQOtz16idyS0lJvaishUfBNVtr5M5ygLBMr1BLFHLU_cQj7lE-xpUr81ykrqKggeJMCB2ifFUT1J_kIRudKRjmnahpBHYpdWitrMcigT5IWbpL81usI8jJSiSESBbmoNJ7Hq0ThXaxr2ZfNpbGzRz2ITEOvwLMXhH7RbvfMnW_IgTs00ktap46t1SUe-URxe-UD1YLz0oLek-6Na_B7kPYi4qZhrCGD1yezgOLjThHd38KaldsKEC0Fc-I7bZ7CGLRYe-alXVkL5iZkffJcQjMqZzmfORaoe-hU-pBUfrfJmbM9Zpl_WX4vpaIOpjBgwYHsK51viywh7menGIhrWUv6v-66F1VmkF_ZkRL8DB_80l3G4hicFOkslvPm7PB_ChGMtwPTCa9Umt03nmFOfbV7p1YRRQN10OgWvmK1eCs0h_mJKVhHpbtD9zysj6kGS6krsD_WxQFxDhl_yLn0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NR0ZuIs-LgNwQ3eKDgjcw67yGZ6FIah8RXvpW6lHZasJ5tGKvJ4nxV15iY2HIyeXLoTTowqvaTE_eRkDWBLh7R_maeJt_NBV5Fbd-srNskknSOdfDW9ncjwhAREO4Jmo4k2ZcLtoYDGYHtLK1cZUKG1n2ul6xTqzre8X5Hub4Aw1PHOt-7v62hthC09gpm29r860tvH4AUJa1JqtSvZppucgQOtz16idyS0lJvaishUfBNVtr5M5ygLBMr1BLFHLU_cQj7lE-xpUr81ykrqKggeJMCB2ifFUT1J_kIRudKRjmnahpBHYpdWitrMcigT5IWbpL81usI8jJSiSESBbmoNJ7Hq0ThXaxr2ZfNpbGzRz2ITEOvwLMXhH7RbvfMnW_IgTs00ktap46t1SUe-URxe-UD1YLz0oLek-6Na_B7kPYi4qZhrCGD1yezgOLjThHd38KaldsKEC0Fc-I7bZ7CGLRYe-alXVkL5iZkffJcQjMqZzmfORaoe-hU-pBUfrfJmbM9Zpl_WX4vpaIOpjBgwYHsK51viywh7menGIhrWUv6v-66F1VmkF_ZkRL8DB_80l3G4hicFOkslvPm7PB_ChGMtwPTCa9Umt03nmFOfbV7p1YRRQN10OgWvmK1eCs0h_mJKVhHpbtD9zysj6kGS6krsD_WxQFxDhl_yLn0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO3c1LS87v8ayKCfwlTJxL32XGyPxzLg3rs6wwSbH3g5D8aJxD3dT3h5NhbrfSGfTKmYC-PN00tKOK8a6NwYUZNrqmIUTFHxowVakYctRY0kgAQaXv9wUWULkgsHnTSZ6z6OvwSbDuV5phouCXM7YNwZG3MJzkP1bFfDkpwNbQCuPzmgL_mXQhHgOkoiurck3Mjuj5BL41OnPO3yb7u5c0YMcF2nPVXCEzZ0IFgMptimLjWHnKhwSR8JqhLiHZzJYc36ktWcplmfXtXZJ5eUtzE1yOgsnLFTdC3bf8n8fK79bjALlbofhtnXdz7lZRyZLAmEeW5NAgiGtqlnbNKDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=gIUeQJPHvEWq5sAzal3cTmseIXkuy-WzJD21StscH7kLtQ2iNDr9I0qydWgqS0qABi-uRKSvCvO6EbYFtB41Fn-3BpSUqfnrz3ZIn5ye01y5xTPMPrPn_tFco5zfFYg9bRWTVcicO7bLToanIylkS8jVbHKvUWUxbLSyIvdFYbnqnc6T1MtJhSpQ1AOO_UqswP8zVp7AU5kAhSBJABPEkstMOG7XT6brxcurcvXqyqrri6EhEKW4b6icOZCnNRAh0TtggbWWo3XCMwBdHQYvG6pgAlPSes8E3g4Y8C8MRRuSYlrxXPyQR1oPn8dBIYAe5TDINnKDiWzaQ3_-McOovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=gIUeQJPHvEWq5sAzal3cTmseIXkuy-WzJD21StscH7kLtQ2iNDr9I0qydWgqS0qABi-uRKSvCvO6EbYFtB41Fn-3BpSUqfnrz3ZIn5ye01y5xTPMPrPn_tFco5zfFYg9bRWTVcicO7bLToanIylkS8jVbHKvUWUxbLSyIvdFYbnqnc6T1MtJhSpQ1AOO_UqswP8zVp7AU5kAhSBJABPEkstMOG7XT6brxcurcvXqyqrri6EhEKW4b6icOZCnNRAh0TtggbWWo3XCMwBdHQYvG6pgAlPSes8E3g4Y8C8MRRuSYlrxXPyQR1oPn8dBIYAe5TDINnKDiWzaQ3_-McOovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC1zQa59ePLvuGc4_F9MQnpWgGmSq2Sv7Wdv6nj5CwovRbT3gepsE4FDF4JQ9Spy9TLQaNa7kFhe-iSr0udrejSNIiPIrUdEOqhlLHalN0uEsejlDzeXdVaV0XZeLdL7-vHbNFFyWV1s6nUjg7PQH2URJRujZx8ZSAvgWt_J6gCaCfutC8RzERg6XijHgRmQVr1YQYCEKHWxmyjXFkMfHXUiY6J6ZIFTx4_NECKl1fGpnfnWgmunLzUrC7OFzm8pQ06Smfms33m9nLMWgbVzK-y9xbq_OgYby45Re2CKjGidmP3mab8ZzdU9jtw-7QGgHewVBtRF19R0htmJjqlUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr_C6RIsmtzdNySy48NR4-IrQBR64dq53ASA4bJc532lQEh09HHT8TVA2sRXw-a3EKAyerYfgwkBodsnbqLzoj6erkjFLpTBcEwVyfa_V-UurWauC0-_zkFIkkqpWj2_AqX1J9N5e18qt8TOq-veL93IPqUtmw4OK_ivCrxwdh5QJd60Ay3Kqvp8O6R9AzAE5wB9BG7SGPqFidm-OSoKwWhG-dTYhO-n47QxL6jMp-GqUAP6AkScBQTr_sn6wNcg4Ism86UkGU2q0wB64uypBkLMyJGetY-ejwpLc_Cv43Uvjna0odcOX7I9f29EngnACp5gSQL_ygcuoDmzJAOwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjTeGJSOfOuZORPvvuzgzBX7kRorref-jt4CGTwtxl7Vbn9DikYZihkNaGEWcLYCm-sNvgWqz7k401k_PqWVl3JFk9LGm4xvAtIhflA3gEiQpcAfjl82ZVt57xboQttUiHYLLDNqWnnOhbtjAPHWe7tyw8TAjONZxi64jPqRVKI7iQLF8KK3Q19dkaPq9x7trxjfLVbiNtkuyJCNoM_ZSyLjudJ-ipExzM1UmsrQfmKNat8OV1NQZInqIHFotfxb2N0AU2ng13i5py5N8AFJeX0vcBZHXu7bFrKaOb2miWaA9UpPRD2dRxx26P2STg09IS4KOMy3CwRsy8gamsGC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfeB44gJuWZwaSTf6DD2X4lov_qkcfa4J1m4M-LQrmNEGSkusOSW54gFRgS_v-ZSvZsh-8lvEMy87zaB65x2m7MBrhvYnRqqI2yXcVN60RoqnOVAC_6jqd-4D4i5eJ4xMckJih5dnFynj5fPOqmo33G3AtwAbVKDYttP_ZQ9EpzkzpTyNA8r_RdwVYO3kEsJI4QOP1Ho-C1kHQNtjTu6d_Ll0R-MZ6B34Kiqsmw7EUoxXaMWo_B8hxQ3OKSfT7t_-lW0HXgsAMsBtoNcouoDltj3dMm48cwBLCBG26JmN6zLqPwV4NycdP2KCu8c7MLPUxvM-1IK1MikbbEd17Fkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=O-x2j60feL90vR3MBEG3PHitdQx_Xldw6DToKqHcKVePvVnbFpIrMaOWLYxgZhnkRZl-DcjVT_l3XTIPcHyMOtzTZHZ3eOFa2neMC5BFozr9WZFgkqLQuVUJHCuhQd0an2PWPXluCF1OTT7lDVPSA2aw43PszKwfpckFyMj5g2A-ilzfF3fafg0574jVVJD7bK2EQdq_9N0YqKr-89Cn3JNoo_54oy0hwrMSOGY2uqCZ81lOBAizJHoZ6ysU4oyeFRUqkDtqwjLd-0cLT53XhWUVYMYIsw0_0vat6j-0ZJzNbaAU6CnhBSCb29rzyKo2ZYTitdA7S45FV3t67ektTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=O-x2j60feL90vR3MBEG3PHitdQx_Xldw6DToKqHcKVePvVnbFpIrMaOWLYxgZhnkRZl-DcjVT_l3XTIPcHyMOtzTZHZ3eOFa2neMC5BFozr9WZFgkqLQuVUJHCuhQd0an2PWPXluCF1OTT7lDVPSA2aw43PszKwfpckFyMj5g2A-ilzfF3fafg0574jVVJD7bK2EQdq_9N0YqKr-89Cn3JNoo_54oy0hwrMSOGY2uqCZ81lOBAizJHoZ6ysU4oyeFRUqkDtqwjLd-0cLT53XhWUVYMYIsw0_0vat6j-0ZJzNbaAU6CnhBSCb29rzyKo2ZYTitdA7S45FV3t67ektTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdAThQPNDybwx038Tdq4PHYdYdJwqwUj-ExqShW9WdDdO9bqxxvWgF6OWVjue77becxWJh4IvSsD7IorXjIULDvAtktXaxSGvyISjaUz-4Bi02v30qmYqPaEjohhTQqZsC4W_XV-N6rE0RMBSiGYkrmU4TFqPmi6Zvv6aUD4WgG-0-jEIuxegOpKFtzHXK86IYxdUMmTqOsLHJRNdAEwcOCGgsCesrcPpgPKI8KZGSF20VS_AW1J7MoIC0naaBKBdu-S8ZHYMmg67upzHRrh7k-uE04b1ZozmOHwKxkH3Dc-y7i8e5BQp9MYy9EyBKcwGQexW9TnhFujIbPUGKik-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS24KkVBCdO82wpqwVVsQFEqbe5qcnwUQbKR9spaC_9fkcj280qaze-YryeDiYh-jTWcsoQVWbPRLbJS29Ssgjnc_ETRW4elYQZqexujiYswo5czAoM9FFPSEnraabIcBD4l1Mhm64OiY5S7ARjE52OFGgOfOQ5W36Hsf-nheOsJWYeHr53P5g6TJjomVL66QypcUjP5IcbD7iTilZqySmeg3RdzBllMcy07RhJgo9aMtmr2tTlPgovMUHMUxFQpPvgJVGY4KjvA66cloVk0ofnY1cvjXw1IAM89FpihfRUtxMp0m0K5UaIedMt-relIdzOCbGfY2wR_a7hcPiegqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUe82yoDKDqc5yKaEtkrcVH8y_9APH5bxRU3EcOliu8bwdAn8ZU_BV8to0cMcfgRRKm2WZm_bxVY66pirW7Q8aRi830ePmYdCozGBPALpr1wdQG_TaWehlYfJV64KxoEOo2hUT-54HISRao9YYDdSo9IdI4ZEOs0o0nbeK1HEXqvvGujypM7159y_MB55tfULhoI0aTA51JRqxOUW08qCKU7PEEFZ8f9074TeCcGxkrP8GFk2M02XYdOQJpd-oGq9y_48qPmN3FEjWGw5T-x0_pty5XQiQOshGw-G3W8WUUqsvyR7tSBfCtos6mphbjhKlwOdrmohg9bgFYPQ9DdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBk-bLV8cV0XT6530HE48ViayMTpZc-aPeqa9exuWSmPS5lZp6ZxjYcuSX9NxejqMcZ75WGZ5dpv8lC2Q4baYlmMiP9PVQLeP9gKa7gZDkb7L4WZM-GjOeC_tljIUL6HvPrEgSgj3Y0ETu5jcMGKwjZDhbvOZoZtjk_mVf_Y7cZ95vyazmUbYdBZv281adfLMi_sAWFqCybzZlAKPX8RFPkRivKaC_hWSOr0uUq1-LvuGN4baQqgF4rRDNXULG19dOfpcONZnB-WmP2zcvY3KAKxJoWcQvfdjpMJ1pkrG8mSCuNfLEI4amAWGkX8D-qUiAvg-xpnaYIxXNzuR5cckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=OsaJ4xUNs272Rl8GJn5kvQ-amXRQWoOi-jpT0jS9QF_1oYvYKtUoQVVvoaSpeYOktmCpj6f7zX1-CRDuh-syMSBG5CrajJTW2JS6Nee9Q9eD_otHotoSFDBLHibnD-1QqdM_ZCq8DIPxROKvj7YR4Mr7ZJuH6TNT2EsndFMR5PukhW6h7GQYRCoyNrW_-YYk5L_tIpQoWF-eM92lzWNMBPjpGmHiMvMnXzW7Pumo_asYqj9DyzPnZHJId0l0XxnB8nfOa8Hjvtx_RcYZLPVrKYinF63DveblzVdgBsMSKELJq20eSWHBGi7lRl6rHIjyQuBDD-RJX8f2_px_2Z34kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=OsaJ4xUNs272Rl8GJn5kvQ-amXRQWoOi-jpT0jS9QF_1oYvYKtUoQVVvoaSpeYOktmCpj6f7zX1-CRDuh-syMSBG5CrajJTW2JS6Nee9Q9eD_otHotoSFDBLHibnD-1QqdM_ZCq8DIPxROKvj7YR4Mr7ZJuH6TNT2EsndFMR5PukhW6h7GQYRCoyNrW_-YYk5L_tIpQoWF-eM92lzWNMBPjpGmHiMvMnXzW7Pumo_asYqj9DyzPnZHJId0l0XxnB8nfOa8Hjvtx_RcYZLPVrKYinF63DveblzVdgBsMSKELJq20eSWHBGi7lRl6rHIjyQuBDD-RJX8f2_px_2Z34kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGHpxwqfStUHNYkmlqGVFRa6TGF1BViH3u5fce3puVg34pgAYH0teGfVp-iGmt_GnUT7HfmUy3aOxcq6VEzC_VODE7cdVOBntCceTHpBemN_gW87haTPrYwNtYD8u7ntwjJCjTlzfneaAih007lEtgoJRn_frF4eBu1-0YOysSKfXhJVWQi0kjoDPxFjQRNdGXN-lym2gysz-u4qndj93NyXXm2qShRZIinkha8M-QaVaR5QrCTEd5D7zIbqfQ0uq8zXVObNJu94rUKuAOq-eY1Kcfq7nZHSIdsO7He_j1XaKk9foQRYk5xNnfPc5Gayx-TToVfAZjqCs65SNTr4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f01k49rxMCORmOFaPO3KksFThcTUglmBk51I4b9Pf97Zwg9pk0syNwzeaz8RWpl4QEEU-OjoE3P6wrFPZx6IV_ejyrUmmJzPfB4K8Wl3KM4RxxYdXKJUVLksg4xw5BEzxkvrvFXiau3MwphgqEXd9pJMxMYJ6itZGcUYfJiCLQOUvlex40inUjLZORiq-kXLZGLAVLGAVaIrLh7-GrgjzNmwnFmjGYLlp0sTdeDdUpi4WRp7fp7JpdP4fyKVHkkhAmoWM4MPw2E4uHlMtpMlFilQzNApY2daiKtg-XAueZQV4wg-FZRni7k8bEduL9gXDnqG8deH7htYWz5P1Rjklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtYfMVhniY2WsnpM-CpEtd0pct4MwV6vbIdW1PuPcrxaH4l_ZDwV1sQGzHL54br1_Qe3dkdu7pIlwQnNhgpN8wZldSm1KzhZFXn9k3FnVS_WAMOz0-b1vrOIFaRrxTY2SCrupAF6r0bI3RAbyvWCU4wcAu6B0Ph3VxEoGZ95nT7vhICnCrIP8n3Y_ZxtVfHJbVNakC6M5nyYhR7AVi8bqBQ1WOd03rPn0ONElk_4znG_NPyMj7Ln21qOhLXebr8vZBMNp2wxE0FRoDiIOgBoN1EzesUiZ4nxHBTm6dXddtv5jDM8BYzmrQE0zfG7xj30vJXHbdKjemjmP5z3-IdacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_nnP8Qc7XF9PkIVOgSDiinkjjKAXYkPWijrdoCfk-HcKD9znlbJU0dEAmAAdVRYjSq_LFKYoh03aHb-a8OQnQtvQrY14L5tnHCSAByja_1jUakViTduavEhqP-CeYca4e5ZUw8qG8uwQM7YuV-Om9_ZAc6erOOS6U7dS8CTsEhuXyYNyMbhr3mTj5d4JSvYy9OmFtPzKWzzT5RIt4Y6Y22drCRBFMhTNQQDnyvid15YtM84v0f3yeiEEb90ddvtK_imngyGqtnh0Wvj2jcLO8oBtf61ySRZntHpQRda_JPPsQqIfmC1F5Krq2OQZIwCvIoIdsqGoyArx_tHLNyobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRYAHXrhxhtPB5Nn1PobApKTQJuGEZNfPOGUYHT6-U9mZS8lXRXX2g_8VCQWDfuHfKbhw6FebdGuCHI2zznVKM-9LeWtZ_CQ3yMFTpwTk-LmuX26USXwSfCQ-kwYSy1C5VaIyi0jNaj8xK3rSVxOZu4Q6N0vuYpEW65aHEhQTUROw718fAwSTBSdAtUrt62tyC7Up-8IQQowVoYd2uPGc7fraFSbFLZnRugmzM-3zwLP4kLeF7nejQ0IJ9HZbyplU0HerZpzq-z06ohD96Q_XvIHpURfh1t2phqKA5n6FPfGIWh4_4O2d0HMylYCClQ8iz5Sy5DH98rlRr_Scnay7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4UPzZE3w7Ny9sKpcDQUPcM8HOed-OPKWkXSoszXdI8_UxtpigalziGXYRpvdrmYN1RaGSq7rOi4DBDc1P-G-TeQKEzZ5tuQ9qLWbHfRPCdOpsGuBrs7iUQ0T8dQ8dkymKH1QxdqjRyCW4x3_N0IIvM9RDcftSjg_C2635Oi4uXS6bcJtGZcaMNofbVGVb0mTk6xkF65CF7HvZVse1NlS-qNAzpGsfx4DXf74o4E2P7WSuUE6t4SbWvUhWD1jU0I0L3MGOAOfq3eRvYggfI7I9d4ve5Udb14R3BtsZ5bI3vlwrLQhFdvsps-vVskzduYUt29tmzuQHMxItz4P1ZErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNlaPDdujOJOD3LH3wNj7An2j2vVz7PsB3vuGgFZ8eoPiDzZEc0Qh4fvcFh4R6TEJmarKV13uJVJBcKGQ4fBlGTUx3nvhOxIyzOX6oGZl4MGkSUcrmIR1v07FcdK0vFMTKobLl1jzZskln_Ogcp1hA2Ab9fQBzE9kbn88tWYg6dbZYlF4_BlTTVRf_OC-h4k5AmMK7fbpiRlsqVTUeQISSOgHAQcGUVDFPThg-YdvRh1buFzhzcA6RVGCsE4u2yAXKCW5yZ3Np9A09PxF-NpaLZoRnc3-OCqBdWZFj8ycvzI8aC4hSSD6vybvQPjpZQIiFy48CSGdNWsdlpfozBS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9smup8tCK5TJQZePHTR23JNnyncRaHKA_qnLvIjX1pJiA2BPwh4rUocrz3Glf5W3jr2kuHwLxCb9fWPIr6yQ-JuaMEuUyFF5rHrmIEcMVSvdYnQ9eCynVbWNFYjnqFmGq45M6QSyTGKDlgEg4IAItaKtB17x2hkUFFenvcLRYDTc3fFzBCBbzsqrbrL6wy6Uue8rrj7ePT3mqIIKriMzDqUBszYYSee87aSudYy8iAQapx_2QhgBiFUMS5x2eOyUbViMNpNFrgNpO2a2yKWPuUzm_cqckFfScIuh54YKbY7__3fUC1cZEIWDFMLHfbB_OXf3ctWSL9mixUeqGzrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP8PDd9GFaGqPCYQiyQgAHkAbM4bjulSrc6iMfGnXzbu7UzU29798_U-ip7K_IoIibWJtykjQm2i31DyHl1t4ZwKqpnt3rXK80G5IssbHsITwCJP__vN_0FkBeVaucwSNcahGAq2ktobG8qFAfT6wh9cyTPshCeKqIB9RN_fMxV6YfW1viPGe51_I4tVOfp6j5V6fG-3v0k3vPOUBr96quCABMO5ECwXWJH9KHeCVUJyccODn7lJpqAe1m8MfYrD8-f2KJuQs3fNJrmdA-iVFfcCteAeeO3rY5ToDCxRB3kGFhi0HL-7qYg4XtwqZzItDIarxZDsaLCSb1dAfa4ZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=iS_cvDM3hiXdehcqncCslOtjWposOEqVQCdlN4PmUeu2feG5w3eYBNxYAb9U_tvFOZJsHwhw3rjDAqhFJhrA1QWLE5_u87UbHIFjPCyxRQpaZoG49svNeXPW_RvBGOX95tqC5iuymhG9FtJGSqq-gCAajzku3-owWoEVFUmZFV3-rEp4ciC6CVd4fBRNr5NQP6mspDWgySsGWcQBucpgv6CqXoBJSRpbykKjV2ua9oT5-LxZyAw5GV66eSXMXohFa93Nn2v18bI_14WAfwdB2Ye2_LM6sGrh5_U6umcm47VW11nNZfDzBoOmNWVPBguYteEGgLt5Yxq6ig53cq1v5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=iS_cvDM3hiXdehcqncCslOtjWposOEqVQCdlN4PmUeu2feG5w3eYBNxYAb9U_tvFOZJsHwhw3rjDAqhFJhrA1QWLE5_u87UbHIFjPCyxRQpaZoG49svNeXPW_RvBGOX95tqC5iuymhG9FtJGSqq-gCAajzku3-owWoEVFUmZFV3-rEp4ciC6CVd4fBRNr5NQP6mspDWgySsGWcQBucpgv6CqXoBJSRpbykKjV2ua9oT5-LxZyAw5GV66eSXMXohFa93Nn2v18bI_14WAfwdB2Ye2_LM6sGrh5_U6umcm47VW11nNZfDzBoOmNWVPBguYteEGgLt5Yxq6ig53cq1v5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfy6b2HQAUSYp17xwr_CemiIOkJY9OLdOeAwFMls47XLqDTMzQTCKfgbN6T6IGCrxikPci5z-2Coxfj_-6RdpRi-958qKaX9u5Jedk18QzApHIY5jvxAVgw28ahZIrlknGG3-Wnam6vcreFTutY2HWiipdgXDlExfS72vzh4o8voORSHXfsaQnUtM4iFsG4X9ZUDb0gruIioZUppNiBXE6iEnpLukKXQd-oHy_D56Hjoz0TXjRP7X3PDd9dIeSaIZkVtyD7lKzR6gI7z-UfkHmOdPkLOXS2uwMxGrs9lA51Co2abfpLJYog__wzH4bXwm7ggjPddUCXZTRBughZomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=dqHSGRRWrkA1-pkFphv37YQY61PRuv6Fnymp40cN6hojRvCse8M3_RDJAxuVuFRDoffqjMx0FTFNpBLRhQeb1nEsIpvvxlGK7mibm889netWfVl2-C0bGATQA9zqvY1XIVInEWC4Icix-5c0OSdScNvcXjfjWn6TQ6HTe6Pe-6p7xIJBUyH5eLyBUnmvkLhj10BNPkLDZOcDbTFTpofbYIv7bq3hU-cnJpA797gmOBtX3cmySseAvJwr_fE6zEMVZAtvme9ttCXOAXRzkoMnkH36b6Wdg6fHxraSask5bzzFsfYGpnC6JRdRGCJxLg5IdbeQvlaqiGpV1MR070IGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=dqHSGRRWrkA1-pkFphv37YQY61PRuv6Fnymp40cN6hojRvCse8M3_RDJAxuVuFRDoffqjMx0FTFNpBLRhQeb1nEsIpvvxlGK7mibm889netWfVl2-C0bGATQA9zqvY1XIVInEWC4Icix-5c0OSdScNvcXjfjWn6TQ6HTe6Pe-6p7xIJBUyH5eLyBUnmvkLhj10BNPkLDZOcDbTFTpofbYIv7bq3hU-cnJpA797gmOBtX3cmySseAvJwr_fE6zEMVZAtvme9ttCXOAXRzkoMnkH36b6Wdg6fHxraSask5bzzFsfYGpnC6JRdRGCJxLg5IdbeQvlaqiGpV1MR070IGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=OToV98DMOHO75zqRlApkB8LFVNDxyTes0sNFTZwSHhPp-jShDcwbsex9NOpcV0vGyLGNCKLfF3KS-6DA5J3iOdMZkfjXFMcbpeFNxOQi1Iiqihkt-kgkW5YGn_VeBzNFJ3RPMjdnORgt9GsrXr-IvJOhRrJsZzvZYd-yX7kyxOBDeGXUs73_bYVTzg4FIbREiLj-ADOXmfgdgrc0AvMXTAs8c555j3X8KF8o_UTJWujTQF6J2YOibpu1I94_shSBB_EGY9FM3ThF-FLZPG6An9mrXHbmeOWBtHcafWq_ml-USbtfVbMH6xJ6Sa_b3dBeMfwZhI5lMd-5dEHcwnCWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=OToV98DMOHO75zqRlApkB8LFVNDxyTes0sNFTZwSHhPp-jShDcwbsex9NOpcV0vGyLGNCKLfF3KS-6DA5J3iOdMZkfjXFMcbpeFNxOQi1Iiqihkt-kgkW5YGn_VeBzNFJ3RPMjdnORgt9GsrXr-IvJOhRrJsZzvZYd-yX7kyxOBDeGXUs73_bYVTzg4FIbREiLj-ADOXmfgdgrc0AvMXTAs8c555j3X8KF8o_UTJWujTQF6J2YOibpu1I94_shSBB_EGY9FM3ThF-FLZPG6An9mrXHbmeOWBtHcafWq_ml-USbtfVbMH6xJ6Sa_b3dBeMfwZhI5lMd-5dEHcwnCWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1onh3iDybbghukTNamzBWlWcZv7KtoVoeF__fRjVu1bHhbfjGd44V7PIOvaPpalSOO9b-gH-rogb779dbcFQlwHpj8w-mzk8bUpqGEJOQli46JCaqxTuKpwD1HESV2B-8DohMoi09MWK4vtDXuwPBeCZ8l6mioM-Xr3taK38CJAZ3M4D0MgVkK04U-JH8x9LLmNOKPO-XD3VMc0Fhn6K9RTRUjI29_YfAic-K9BBbfl32k3bj4o0fqck7oZkFwzZUYx4PF64GJbh7cCc0f_YcgmnB5fI4Ya22K_FBNldg7B3YLh-plWsbQxyRXNkTvDNRuHUgrrozxLmy_RS3XNYbJ90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1onh3iDybbghukTNamzBWlWcZv7KtoVoeF__fRjVu1bHhbfjGd44V7PIOvaPpalSOO9b-gH-rogb779dbcFQlwHpj8w-mzk8bUpqGEJOQli46JCaqxTuKpwD1HESV2B-8DohMoi09MWK4vtDXuwPBeCZ8l6mioM-Xr3taK38CJAZ3M4D0MgVkK04U-JH8x9LLmNOKPO-XD3VMc0Fhn6K9RTRUjI29_YfAic-K9BBbfl32k3bj4o0fqck7oZkFwzZUYx4PF64GJbh7cCc0f_YcgmnB5fI4Ya22K_FBNldg7B3YLh-plWsbQxyRXNkTvDNRuHUgrrozxLmy_RS3XNYbJ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVYzbjUrJsgdDihhVR_8s0Qtn9G0XGV3kUO3KqBSz3ZM6uFGzreB6iUcrzu1TU1AKkn3XxuUWez96aQfVmBotdqzZXgBnIA3fKz8X4-vYZjfV6MiQf5MfvCUAKaIKn60-SGI4MBfG3DYRSfP1o69nDfgFp5mm6zccvD76P5n42ael4OGG_q5bA4OdetRSoLmH-jHeTWlb8v383P9G9IxsEhAl08OVmtW6hQlNDfRE0mj6i7D2r5V4kJSmfW2-9upvSPLsq8iksefknYuTB93UiP-j9b5HelD1hgysye--Hm9eVDtTdj5-SHSehzZB4iwVTk1Jh5quurM_Mtc_qKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0I6ItSndRZV9LQkTK7MNqmfyifWL3f840XpOnEKdakm53Aaa0F9GQe0t7hkhbhnekZSYKHhJNnWittpb52lOGG0RDZ1FXpKPumWrqGVOXG151NXO8uGSgRWyvpqI1sFnYpA9rAVclOlsafsNZ6AB7iCgLdTdOELPYR7hkymzhwla1P6SAIT-B1V8Sf3JQQUQvwOmIbQ3Qjp3PAAfJ9_Uck54UMuBxWhYFgB6vMrB3NUID26U7HrPwNg9W4OiV3rnKa5PwtBrAo5w4O_hHMurQYkmGpjIk9TYrQ74UnyjnAyfwdF9zZHLOnjDcXa8Nb1qm5qOLF1OQMDYRDnwRrVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGG9tF4dBD7Rli-YGYP__Izj-MC6sg9bo1RvoirzcxKl_arqHYoCIozsobu4NFRp1EiemE63dwbgWCaMHnW9UpcCwIseikCgEgL3HIu267nVWBUnFM2SO8qnZMOUygaAMOxE8AEw_BF_9tluaupAvB3KS-yZ41QwICs3_nGE0zglx2zSXiKXEro-ehNvfjLKxSXp2D0VQGIF8Saj07RdtgdKAKa-Wz8VSS8ml3K2DujkaHgDDK8inoniouB7SVAzT_DLzkBuccWiu6SutTOp30aMIoeuDbXjSUmU2578VrasO09tst86_NMFXjjPLUCPkZdUuOoTTrRkHJ-tctGTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=so9Cm7p6t1R3-oNAY8L-EsLA7hKJmqZR9kcg0KWBBx_07mfpRZQ4zalZpebz18Kku6q39pgGAIiEhaqSeq4o1zHpSOxToBV6J8YvPvyzeVkgDJJw_fsIx6PpiKPdZzLfTKRkfjd8MpeZtcHJg4MVpeTAdzVq4NXK-gxTOoIQ1xHx50-_H-1xfJ5GDfbB63jSgvdEPs7v8ujoxfD7aWhwnbT6Dz-8kvh7UdeeGHWbCbjuHaFiMpaco2lOptnuKMzSoj7MPzfOIyFaW5LcPjTqUPxFX6IvNTC7jJEkjg6rqYSpVp4p9eq0nXM-zr3cu8q9CA6xN0wo7DNOc_Qg2K45FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=so9Cm7p6t1R3-oNAY8L-EsLA7hKJmqZR9kcg0KWBBx_07mfpRZQ4zalZpebz18Kku6q39pgGAIiEhaqSeq4o1zHpSOxToBV6J8YvPvyzeVkgDJJw_fsIx6PpiKPdZzLfTKRkfjd8MpeZtcHJg4MVpeTAdzVq4NXK-gxTOoIQ1xHx50-_H-1xfJ5GDfbB63jSgvdEPs7v8ujoxfD7aWhwnbT6Dz-8kvh7UdeeGHWbCbjuHaFiMpaco2lOptnuKMzSoj7MPzfOIyFaW5LcPjTqUPxFX6IvNTC7jJEkjg6rqYSpVp4p9eq0nXM-zr3cu8q9CA6xN0wo7DNOc_Qg2K45FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhhE_M977RisvZTL5b6E9xX0ZxJaL1bd14C2tUWrXvagMvQcOJ60pU9BewEbdalX1eEnzpUyp_Tp8_lbV7eGQowcvlZ3I2-lZI-HBkbu7596pRGlV8i1EA19FfLN0U_KstC5pmots3F3cVgJFZH8ZtMQ1aRacGS8w3uZEbMk4BumgeEXneBjDEHXEJHyTliBSFaMKESqJsAy1zM_J8PxzR_3KKcO5z6JHy2yxaHEwZ-JsNfgo2j7tLVLLrcDQof_eAW65AtzYnkYtzpV8OYhMx-aqfVQo49RVgq-JDPyYKpZe-jCk5ubBrmmyGwfay0utvqga98F49vlZcI6zNTp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M81idDughwV4xBtDJjdSqeqk7WiWTlM4Nv4EYbwto3s5PpIcNnAtM5-i_5E7_RgP17xi0dakXwh85Esi7uN_026AftamCt73Ke3MusOUy7aX1j2a5l_GOgRaJKspaSent0ossXcBlOogxcZu2stFXkdIcBJ1yOCvaqB2Tk-giH1Zv5M9LLFMKjDASWNElYutQC8BYD5od57W8c1jO_Tppt_gaewNALzKnROAkpEw86wkzEWDZFozmPEqvh4q7t6OT7caGweOzamVcGWJl7JglH_gzvNKJGnPIoBDzfuim4HfyZLq4LzvUWOlKy-BO7YIdDE9_FOeBz3frrYC9KPung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5kwXT9IBLlRbYPQvWBau9JMxeKily42BXEIBtXL6m6cUoLZyzflX0ixzvwJ0Vh15dQDjltIbq0Ts2M3JG-P5hV5RCWZFlgjQorcUXnXUvNXkhLIDsnAWNVl9LtG046joolhSp5ROpbvyjK3fJ0zQyC2NuFKvwhkzJLu7jFvjAHQZH8bTe-DlK_ipSQyxPpTSwnjp1dMcPRrxGkq193bPzsPMLJznKd1ggnMOkhslvZcGtHAFm4Sp4BRkQ0GS7Ip8Sgm27Y1P18XEYtJrQ-xVdRZ3I5eUNaHQAdL4T3mWkA9Doxfk4dhq4kROijdBrjm3p4a4bKylnwOQyRR7dvgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zeq-C-Z74ECD-4FffLCtO2TNDcpCxzW-lpzXQ3P_2Rr8M8-zqOf1W4y_QSrwhjOuQ4TkZtHzs2UixjlXiL19nL1gLVqsLo4aeNnGRq48bRU0rWQQkY6rK24hEw83VyFwC499l7DtbheFE-F0nqvlsxPEq6poHf1IDsSwEXAdDAwaf3BrU_xuLzS5fvxrBIEcBb2hBBNyW8ArbqbmjvphiWxaKwYCha_EcnRTvsbRt60U81Ev8Ms_4d_OgMpfWzgzhSoNVDZ7daFv_05QTCKdHnF7EjIUjNy7OLqdiLBRkGVc8BVJXjES0zPVuGXrog9JQLrX6TtpeDQzOz-JupFQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1qT9vMn3_yVzPkpWoLLJQd0Ji-ubjKwBghYkITi_AyK9tl4b_tcku0Eehbz5hFvmF6iurirA46ggzur1vipQU1_oKqE58zWrSCNbrddrg4rQvOR1Tt1RxNu4vJ3FLDVTbokfPqqfTTEB1E8oUPbulsFrs4NrT_i8KsZ8oLy2GrnJZqQNpOpGjWVim-9R74aodgl6s9WV6euUeB8lP4w38Eys1gD0TzsTNnA6g308s0Vb_ulBMwblyPOp6n8_XROxt45Aw2P-JmT0rn4uyMevk0oUX4aVzIsL4NdCzGnbTWY1lpsZxb68zu2YgtHNxYPhLEwfQnhl8K3Rxg5cLpjMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=NlYoF2T3sYYaIYe_BJLMsfcBSwGBeWUrsiyeV2B9glvbGXcVrT9hwBwD0WH_vyBplCvP4J8gucEhNvF5lOWki8pZtN-Djr3BA0MX6pB-C3941bqPeOIRg0mJ6g8UUsN1MSxRqlgctXt3-IJDqPiAf7vN2fxyBZYn5a8bl2kyFtmiQs8w4EJ8ymLEsBep19BDpsUyCCHU_FX0g5-93dpkAs88kge0xXpoX2uVFLMI12c5TXUFqL7rieL5lwzGocVMjxoBdkhPn_9kfhQ3LG1ZbJp4EgY9cE-smRhexWIkMFg-g0wenYTxTn0cCem1CiZNwGD0jYauuLGV44mGIo4P8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=NlYoF2T3sYYaIYe_BJLMsfcBSwGBeWUrsiyeV2B9glvbGXcVrT9hwBwD0WH_vyBplCvP4J8gucEhNvF5lOWki8pZtN-Djr3BA0MX6pB-C3941bqPeOIRg0mJ6g8UUsN1MSxRqlgctXt3-IJDqPiAf7vN2fxyBZYn5a8bl2kyFtmiQs8w4EJ8ymLEsBep19BDpsUyCCHU_FX0g5-93dpkAs88kge0xXpoX2uVFLMI12c5TXUFqL7rieL5lwzGocVMjxoBdkhPn_9kfhQ3LG1ZbJp4EgY9cE-smRhexWIkMFg-g0wenYTxTn0cCem1CiZNwGD0jYauuLGV44mGIo4P8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKp9wSS-RE88GsAqbQjyCDCl-5YM45E8FU8DucC3SfKNZC1hFCegkGfhRe4_g-FHPaAwBImh8X00mhl6JqBum28BNvIrBmtUEB0Bjzm2SsDIYS1P59VMumHG_mBJySmDE79S1haOLIpYTIOGVBoJq8BueH-b70mzsZkaRUvrvF8YfHhMNx-OJ0KXOOU9vYz1cZphx1SY5Kq9feuwvFbST4HoEqQosB-6RnftmUwwuJL_fiorRN3EVrDtEIWwJibrY8GQB1q-eI0qFUYvJL2djWyaHlT51QBgCO2XQndz3eGfeG5JLuImFu-eAZhZOhDTkY1sl-uarKGb9yFyC0AU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of4xhDNnZxnj2nv_oI0cT1N-Yd_B8i4tY6WtbQCTFd5cNPNo_Twhi4KjuCfVh5HoTCw85CH8J_Ahx8RCGE5Hw4jt82hvHXSvmq0Ry7wv1raj78Qhsn4mbGkZkEccL2D_MHyI_Vju05602qhDMvUbh_tM8gknOnyAisEYKSwc1-9smJ44zojeUDCco9QDJ8dN7990l9O2jrFRtFgNMUNK8he6n0VECzpYJKGwi2JvoGI1bfHfzqxPxHSYfkj31eU2udXHA6DL53l3hPRLHEjf0ICjLwzcECkBd3MxLUj_16yX4YYH237avZOgfk_gqkzjmQE2AMTr9cyZjcXPbf9Ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=rEk0ZE7rPXSowdDPhQ5aLgHPI7jNu_WrJ67cExoWRJQF3m6KXVubAIFPgSKDjtRGcyKwhpuUZtMXmAgeF23CSIxfPawA-ovR_ja-ZYFxegKQu2tmxDlhVrBNPzeUjip9sV4h8eTLO69XmEd1zLuLLgAzIyLP4VYdQ_SVnhqJYunzyQxS5NgWtVkip2os4r_6dnX-Ewk2neGaD6Q4AEQR4KewRA0wxyJyJa8UrHYuPEO_sBKaBAG8ZIqvu7yqd1Am54N4APLInEjf5-Cp7Yh8veteYJUGetCtO_GEKZIV4IWbvzTtfKYde_2zSwQof4MoHnq_sPtf_UepLGM8oaaHHYO_mAm-YKZeCEYLu9EOonCTZQa4wlYVMNtm0nDHQXJ8dsTM08_BbwHGFMnpnCQFp45F9lc_EK0aCbptLUUnq82I8_6g4gSsIH6sBY3cCZpomJFzQlhSteLojdnzmoYlbazOX5eyNjoLpR1Hmx7wKMk3oo1WPsIXJBS_9gKGSYsSxPSj6UneEg9PExIrA4oGdbGcLUwzujSmDFIwHgH45puo-7EOcW8DgDm6dEEM9DkcEsxQSE-eWsbEqeQjEWjkpaTeZdptyc1qRhWQd1XrhBJwOXwRRD5LBqQm8pE0zKKhrV-uJI_yZoOxA3kFWOKEgqcZXAd8E225FSj3eiIW29E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=rEk0ZE7rPXSowdDPhQ5aLgHPI7jNu_WrJ67cExoWRJQF3m6KXVubAIFPgSKDjtRGcyKwhpuUZtMXmAgeF23CSIxfPawA-ovR_ja-ZYFxegKQu2tmxDlhVrBNPzeUjip9sV4h8eTLO69XmEd1zLuLLgAzIyLP4VYdQ_SVnhqJYunzyQxS5NgWtVkip2os4r_6dnX-Ewk2neGaD6Q4AEQR4KewRA0wxyJyJa8UrHYuPEO_sBKaBAG8ZIqvu7yqd1Am54N4APLInEjf5-Cp7Yh8veteYJUGetCtO_GEKZIV4IWbvzTtfKYde_2zSwQof4MoHnq_sPtf_UepLGM8oaaHHYO_mAm-YKZeCEYLu9EOonCTZQa4wlYVMNtm0nDHQXJ8dsTM08_BbwHGFMnpnCQFp45F9lc_EK0aCbptLUUnq82I8_6g4gSsIH6sBY3cCZpomJFzQlhSteLojdnzmoYlbazOX5eyNjoLpR1Hmx7wKMk3oo1WPsIXJBS_9gKGSYsSxPSj6UneEg9PExIrA4oGdbGcLUwzujSmDFIwHgH45puo-7EOcW8DgDm6dEEM9DkcEsxQSE-eWsbEqeQjEWjkpaTeZdptyc1qRhWQd1XrhBJwOXwRRD5LBqQm8pE0zKKhrV-uJI_yZoOxA3kFWOKEgqcZXAd8E225FSj3eiIW29E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkBXPv4huicSjr_GQes-XoK4d5Nzg6-KuPmv8lRAsGETLy73yRIEAd29RpOBTY-XoKBP5jr1pOb_sNWBhkK_qgM0PTWBI5iU9cs4_iN6DxmD6ftwBkYHz6ncr-cD7bv_Uh--ssxfC6G6K5sGfENBo-izZAaIX8eMwQhkYaBRSa7_NdA_3JIAv-fMzKbcMq6O1ivNLPOYGfQu_81r-8nkCl4ERxMS5XLHCdURWocPaN4LPgOJGlJQ9LHua0W1YcbNlF-5YTIjQRGjcPdZTF4n4ALPSuXtpA58h28Ws5V-M78icevJMhzYZPzVaK6Ko8GKTsfbDlavgjC37jKhKvofug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7LEbS8nYUmviSSRdrO7uQ2Aa_dONt1uMzBuoJL05UCZ3_Wrh6LElSJ8alKByrbZLXORr4l7dckizJvLKKEA1S41IlaqvW3JC_TPRrLWes8j1_1cnTdH3hgvsNavkEApk9xr_qNMnT91tXAjpq30XDCA8Lz8Cyh13VFMXCCudc6kCv4P0aEJod5uHQMVaHgRHWF6TBbMKitFeKuwfUnB7L0Ad5x7BipwAU_9BUKvs3FNPa-fGjQG8HdwD5D3gCVkev-xFddrIdDlWVFPMZCSIneqXMzFLoZS08CBsDe1kI2btD8qhlpL2YoGAaNNVV3kc46JPXLgtxK9PCpMjPc7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=oqsodnEQZORpPKU8CPF15fMfLOfillJbS6P2AsZ68CpyGwXK3caeBnU5tFu-FKQDEZ5aE271W-RC79L5n3duLRmnj7W6bPG7kugkLEzdfS8vlz3ZjySyCs44jJm-cpl7NrtWKJRMTwCRfPlwoH2Mq4wJvybk9gzFF9-nqyAO_KVRevnZQDZ6dn1oydnQxZeBmsTgKy7xLFWVO5OtMSJyoGOsh99b0gZi4N-P8Y9YMRv5ArnGvcg777FqY4dy4TfvCpyDDpmpq0FoEa_I7UhO7zCVheQ5uY1BfJxzgKrAmBLxm0JqO8n3TfozrXflCMVtrqy9kAihc5yuXJVsb2U7Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=oqsodnEQZORpPKU8CPF15fMfLOfillJbS6P2AsZ68CpyGwXK3caeBnU5tFu-FKQDEZ5aE271W-RC79L5n3duLRmnj7W6bPG7kugkLEzdfS8vlz3ZjySyCs44jJm-cpl7NrtWKJRMTwCRfPlwoH2Mq4wJvybk9gzFF9-nqyAO_KVRevnZQDZ6dn1oydnQxZeBmsTgKy7xLFWVO5OtMSJyoGOsh99b0gZi4N-P8Y9YMRv5ArnGvcg777FqY4dy4TfvCpyDDpmpq0FoEa_I7UhO7zCVheQ5uY1BfJxzgKrAmBLxm0JqO8n3TfozrXflCMVtrqy9kAihc5yuXJVsb2U7Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3zvlLLlrCAW0wrIjdlnoHkqmHazx1AXprqGCHfsIPgBUtgMnUPVmxuk5K28uBq8F6ovPjzc7wa30-QH2m0vLH53JLFrzvJ7q4Tm4WDHhs5jljL_yb1nVJ94eCNp3j0AnS9LFmD803Ca_B8inGXq3hId6Gj7UB9hbIN8sux-1Ack9byEFvoxudGV8kahjNRMqUCcbz21RHVC6dyzuXOhJwzT3J6ZSY4oYgYQNbPqqCxG4XIpL6lEhRmIZFIyAC8XzPShzhuAaWoS3KFtQnEgFOXmXuYHptB7eXyqCnM3AaBrXzccJbSZ-gtJvhVBo5_gSj1-DPIlVKBAau_o2WLQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWIStDyB-HALgMw54ygPz2WVM-wzZiDYCr3oV-F04mKPSV-Rfs8CXvJ8bpmAi-G4LfklB8WDjDNOtJ470FKV7dlfv0b3YQz_KcOh3eiPPp704wWVZQ9pLJpsnuYntW2jVigKcjBfOt7RFfYqOL65SjqWj9KDksWX3Y71YHVHuW8dT3FJ8hqwo6f6BH6othgOa7DEDRAwfB4OuzJSZyDastnV7mbMZEviCwp00OF1bywcbt_XXtA8scalN9L__jwTHkscWpB1_8fLauxajzYCRVkvlBLkptLxljbStBDyR0TqRp5H9jUahbpaokh5bO4GH_i5i6wDCZ0OCdq3rnRGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=AWRQ46B4nBgFSEvRwSnhq7POSYA0bY3xE0JR9GNwBFMUFriOfoNgzyWlhabiEWfYs9xLDzG70s9tBRVsbvdB6IZaGH_3vquQOyanYd8p4CnRCuTpwQyEW6gxikqle3FCjx4X6pg8pqzClME-WBjB6pfUrOBdcG_PXY4C2aBUnnT7OE83YK7S0HZeEJxEP_uFjttNkz9qTNuLED10xoOzypiL4M2NuL4hA6uaUVNexrYtPU33Vu5tqjAIB2vvM8JAhCkpaNLUTmg_tOBMUwmLL0xOVO5JD7qJ1B4k8SdbeAfm8RwznDfWRfW7JY2wvywP0paySJi6B1-zbQgb8-7X6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=AWRQ46B4nBgFSEvRwSnhq7POSYA0bY3xE0JR9GNwBFMUFriOfoNgzyWlhabiEWfYs9xLDzG70s9tBRVsbvdB6IZaGH_3vquQOyanYd8p4CnRCuTpwQyEW6gxikqle3FCjx4X6pg8pqzClME-WBjB6pfUrOBdcG_PXY4C2aBUnnT7OE83YK7S0HZeEJxEP_uFjttNkz9qTNuLED10xoOzypiL4M2NuL4hA6uaUVNexrYtPU33Vu5tqjAIB2vvM8JAhCkpaNLUTmg_tOBMUwmLL0xOVO5JD7qJ1B4k8SdbeAfm8RwznDfWRfW7JY2wvywP0paySJi6B1-zbQgb8-7X6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=jBQS0K4WtIcH-lbgHwRMBeEUCvqkhY6NthdCOh8r71_RjnDzNv0JtPX74WEIdlsbHoy55_dGyvXpk4sT3gm-CLLctHbQ77lwbg7Le2cuymB5Yowm7clOkw-y6cnswtUCeuBLwJyPWNP5eoepLAKpvZWl4kQYCIp2fkQ_gsw4ljYVvJeQ2zByv9DzQFhOKi_WRBO11x21zzOyQ2LZ5Q41b7Ft11ksrlM_e6AyB2B64Lrox_c53xyI32dq4d4afZccjFp_BMKab5MVDEkR9RLB0Ae4xVb67BNVuOoHSkyp4TZ-r_QwXoRnlrCAX3mw2l3ZmdW47YRMvwGuXfWPPEniUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=jBQS0K4WtIcH-lbgHwRMBeEUCvqkhY6NthdCOh8r71_RjnDzNv0JtPX74WEIdlsbHoy55_dGyvXpk4sT3gm-CLLctHbQ77lwbg7Le2cuymB5Yowm7clOkw-y6cnswtUCeuBLwJyPWNP5eoepLAKpvZWl4kQYCIp2fkQ_gsw4ljYVvJeQ2zByv9DzQFhOKi_WRBO11x21zzOyQ2LZ5Q41b7Ft11ksrlM_e6AyB2B64Lrox_c53xyI32dq4d4afZccjFp_BMKab5MVDEkR9RLB0Ae4xVb67BNVuOoHSkyp4TZ-r_QwXoRnlrCAX3mw2l3ZmdW47YRMvwGuXfWPPEniUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g16ecliZryDg3QfHiVuAK6AXKRXbtXmTEVMTwUtlJhfiC4BzNAumPY20itcihy8D3qtXshuQLaBfaRi0Zw6jSgg7p3BuA4k4ca_vYRjEa9vwAm8MELPFoVpi25C0A1gQutvpyqnHQ0rwizFrIAmYRVxVyVeV8UhMhfULL7XVITYA59sZeGd5t3nsSnsUSC3FVAi2IIA18s8aXPcSrG-YsBy9dm5uqJUuZ5Nw1DEEDACop3uRwBlt9ALxHJEBaPnO1Eu0GMFzMO-F25S6nDpPnj6wKW4nJ27pJK09FIggMGL3usoHJgU8vAoYB3qtOx9eZzi0pI4bIavFxzkv--3oLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-Gy4j-Gd7_hB3PjyBz88_ZVuEvMfEy3413HkhxX--XyktGwteuzVEjjEhDhLjFOoJIJfDBLylpDAfawmGfhhOeYsgf7srRUUstYU1-oykAZEoQtv88Mv4_ytJECJQSQxMGeWqMumcMsFuSkxayhNA8Q40FvSlUV-ogkrbkXPdnuSpcmlCCtfSaByFVUNlMJ-bWKRo7iIXRZ_y5P86P5WvcmmRz-CS7xMJAk5H8o-k-dlQAkYyIVZo7u9tJ6S1V-f6DQmGUcq-6nlDks9XYbcJLmiYPCrqeq3JI7woPuuTzbk-xp3n7OJw6CoKzn0SowurdQzq_g-DSrDcymuMUtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Qt7AScsK4G3IPlSr_9JGRM3QqL50mWo4Xkyh8D1rpqnTwxVIAfrWrCFH6F3owdypLgCaBagd7OxuvdisHyJqLoHAtHQpiPnwtLbrgibpGuF0abxgQ6nlD28s9Nk14Y7GNUBbaKtYsVsYyjrzjyrzjzVzAPzB3ipHhL9hg9BoOnJvXWno_3lQfiHCSQzAw6svQEVCMyR8tvi62CsqxmT0eBGnSmgSnAlGTnkyTII2Jyctgk8A7hnDDaTTgOw7qt_IWB5bKRvKeqy0xdV_jpB2KdUHwLhzX96gaQy15HlbLzIgsCsNsUmQXxykmFvvh7iE1yu0GP2W0CQozAzkXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaaYHHexaYgs1VD8vAAH2Z4TdLOibBLgCelWL8qymJPm-qv0pXzNi0MRTgd-ER6V8cT4uuv2KEyDI57kek7IxJQl5YkQ-x1qRaNw86iQye2b6X01IihncPrUNZ7NkUWpIb7p5RYjfknWIc8pWZvAu4wT3hDhtUcHlHveHRAbWbIXk-adoSCnK6NaxB4gC-QOSlnhh-V3upad-21YWPfHU5qwsSyhqVNUJugX34b8Dv-1ziAaHcfdxTEcrDdILrVCoxoNv90f6wnIThFSlTlt13Pn8MQICT361HslViqrvfxKin-4wC_W4iOuXEvYmYysYBYocApZJPTdhk8KRdR2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dv3jdqO3W_nNRgGMD5ZY7OeKdB3sQnoBTg8pYlL2aPtIKXCbrNCTet4k63_0J9ibHioOOGJDiBa7rMmzEanywNdqv4easjHXXus_MEnf-pcQ02XuAjviydJxhC9d05KQCZcRISHIiApjQ1Sz9BVCA2BvU-Q0H7xgBeL8UgXa_U3WMHsPFAACU9JSI9RkZI63vnv1HpQRYsYmxPvGloi4-P-7ATXUBEoXjnmt3iXbagK_aG6ht6HG5z3IH91eUkUH9mt729EACebZ0VXbQbqyMtvBQ7TgOXC-Z6ll2WOOpQoIq6tXXE_PS5q18Zf-Xwmp6RLal1YuaS5TZ4iWtl0kHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz_3TR48Rs7r5H98RV47xn2lSdgOr6DNpGGLMMQNzcL63M5B-IT6oV3UBq0QMWNH6nx2ReDRdHguopcGZ9AV8M2iYFitAYGShtfpffroXa5E-gJ5xxjr__IN-PYr_WCCfS0rLLtJ7V4Ujs02oT_4RTcyM-IUR0BdpfABG2yPfDj8ioGsUI8OJi-Wz_PL1GIK9RLdmw_-BR-hJZ7rTXy9C9hkYacY0PMmE8sjd7FEcIWo5xHBeiKzLjOhP0G4zBizXP5irLO8C2aHpCHDzITaBSQozYYzpgJ82_whunz1ZJvpr9jHxCdGe-sWPb7BSprCsBbPm6r8fuVm6C5CM2qS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=qiBd71ZMA_Dy-THuW9CCUhQ5AuKNbwO5zKBzYp0K1JQdIHJ7feEdkRh8gVXUSLUsPnGR0UgOp26eWBSglNE6pnbgNJVNqORyhHu9oO4dU4d8C11nWJi3Bwx4rwa_jy1HzBU3HTrUlK42zISDBU1LJGi7XSn6LwqEy7a7ARL3t1rWsDkGAwfE0TbQrjeSbP5u-mHpcWG0X6XluK9D66m0JLLz0cVEw67aYgqjRjSGo4LHo1JLS93rCbHTvdKAQYOJFKCbgS5ofYtdzlbRuqLVr5_b6jc_LghCyn3MZGK5JW7zLA6a58TcxynqyiW-_wug9YmPNqOWcyNN-qmJx3VmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=qiBd71ZMA_Dy-THuW9CCUhQ5AuKNbwO5zKBzYp0K1JQdIHJ7feEdkRh8gVXUSLUsPnGR0UgOp26eWBSglNE6pnbgNJVNqORyhHu9oO4dU4d8C11nWJi3Bwx4rwa_jy1HzBU3HTrUlK42zISDBU1LJGi7XSn6LwqEy7a7ARL3t1rWsDkGAwfE0TbQrjeSbP5u-mHpcWG0X6XluK9D66m0JLLz0cVEw67aYgqjRjSGo4LHo1JLS93rCbHTvdKAQYOJFKCbgS5ofYtdzlbRuqLVr5_b6jc_LghCyn3MZGK5JW7zLA6a58TcxynqyiW-_wug9YmPNqOWcyNN-qmJx3VmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfqLa2ZEgNUzvgjs2b6ubJbjT0wIkSs8VqjAEFHcbUiiRoN_-6vdsdnp073lx2AxtcSL4ILja_zQmhmAHhMlzET45lGeVKtE2vOaqLIv7_sKHsKZJT6P8s2Yc1oG_TCaC9J3owYKRSkcY-FSZauyleS9MEV2GnojqbR-OInjd-9kVhc-ARyJ0KhgZkJuRW0soLxIlH14b8pp6qX8U-50RqMd6mhuKKV9gRSez5weRzd7Q2j4EbCJHTnbSFiDCdxw00EXJbfmLvfQKR1FR2Jo6tYTS76EVh1bNAW9TsI9-ZmUbYA9h7pC6y1IeU3vSmw4H2xwVSjlzt-SccZ-dis5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=NC4pEKLUurXOYfYjQ9gWEdABa_gk23r4XcqYqTP1mxMdnnyhtNNZ5UMXFfkzl1fEISPPBOzu2j7xJkKJutg4HTzadGy_DM5xoMA3t7KUccom2pzQ50KHJeHCe2e98EJTF1oxXWd6jAHGof85QpcHnfyGO1bRXeyGAjNhXWKBE_zJ4Z4y9OiVlMYv3YGtcjlkSsJ4XYvix7sx_1s9Ug-WgSG4kv9UpAFz0qXe0RiiAbS3YrWacJqpMWYPJ6ZOlnPLtl7T6IoXMfheYtAjbNz888Kd2EdT9FA6ipDG3Siqo6Lp_RLn4-id6l4ENaT23yWaRvWcDeaozUSXngiGnR_D9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=NC4pEKLUurXOYfYjQ9gWEdABa_gk23r4XcqYqTP1mxMdnnyhtNNZ5UMXFfkzl1fEISPPBOzu2j7xJkKJutg4HTzadGy_DM5xoMA3t7KUccom2pzQ50KHJeHCe2e98EJTF1oxXWd6jAHGof85QpcHnfyGO1bRXeyGAjNhXWKBE_zJ4Z4y9OiVlMYv3YGtcjlkSsJ4XYvix7sx_1s9Ug-WgSG4kv9UpAFz0qXe0RiiAbS3YrWacJqpMWYPJ6ZOlnPLtl7T6IoXMfheYtAjbNz888Kd2EdT9FA6ipDG3Siqo6Lp_RLn4-id6l4ENaT23yWaRvWcDeaozUSXngiGnR_D9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKW_mJYj7jfDy7aBBifiVfO_Mn5wjCGKbVfG0dF_Tx5KNOFF96pjJW_F93xeVnzk54dcfnJ2MelKJBHpbjJDwWQhDZG4c7BsvV0sNWz82mPGxoYLKqcI8795vGQkSfBfOx8AkW_6qRHWvDEPMuvofQC1XWNPyOObzL8cVCD9SPQh0jVbx63bkZUcitMce7FOFJcr_diuGibJ9oYPl5Ojg2rvVFNVWngw5QLT7G2zFPRj2BgzlAbnRkN_9CxkwmA6srLY_uquAqBy1A0_gLzFlcPriOvztmXDWciIDG4kjDgu60D2HH0hD6wUFnCBjWfEFhVHNcRd7ApyCJ31L8GrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXdv-4nMifkdEKZfeoacg1H97xUWBhDgg2JopE_WyqP68nFFkD9k4_SDXz8HbJ8X6P4rV-ewObBJK2ZstXNimJGP599z_MLXWObIqZzNAZnrfgquXJQjSSefc3zxXNPs1ZXuTggYLVZcmz4ULXa7L5OxJh-5Na5oHZnhjHGTho2DkHPV1h4hkWUA25j1rmETHG--8xDZtFw9JN66nVF-92krjCx7zhjy3c0E2hUExigqzldn9NDg06vxXWWE4NieF7fhH8xTVQfcC2N5M_YkwNrjyVFYYEqjO-K50O6YIqd7fsrn-Nc4Ex82ec_INpMjZiky_5jMn1geHwUC-MaGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=jGc9eFKbAV46y9Lj6jjKjiNE-vQeoraW56oQIaEkYWZTpiPD-vSc6nFYU45QAKtoFWEKNBMPgsE1FjPg-3UrJhpAb00wKLJ3WedDDWHnrBKGy6fvGVhQADON8XP9uFeNpWg0L19Lk_k9OkvkpUdfxQbUwlxsIz5Ow-E9XcZmIuIDfWQkZKMjU30xn0eNv4qTBCPdy5LaGGdnO7OK0J_xGiyjePjFK7Ye0OxZUoNM9mzp4Fqv8egb8htmhc14jKzQlJy8AHl_KONeZqCUk04JhKYlvXBhdLaWIbzBeqv3mAy04F4N7vGRDN_HqDbKuLuArGAYfcd-Bwx5oy_xVVad1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=jGc9eFKbAV46y9Lj6jjKjiNE-vQeoraW56oQIaEkYWZTpiPD-vSc6nFYU45QAKtoFWEKNBMPgsE1FjPg-3UrJhpAb00wKLJ3WedDDWHnrBKGy6fvGVhQADON8XP9uFeNpWg0L19Lk_k9OkvkpUdfxQbUwlxsIz5Ow-E9XcZmIuIDfWQkZKMjU30xn0eNv4qTBCPdy5LaGGdnO7OK0J_xGiyjePjFK7Ye0OxZUoNM9mzp4Fqv8egb8htmhc14jKzQlJy8AHl_KONeZqCUk04JhKYlvXBhdLaWIbzBeqv3mAy04F4N7vGRDN_HqDbKuLuArGAYfcd-Bwx5oy_xVVad1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx-YcC_z2HNl9MayZQNXvG85z2iJzbWiCxIup5wiDAzXhy9h2Y97ED-Nwu2gQS7Y_-u_ZKbQiH4MRdJv3y2op1oMwMZEYcGQ2k3tb8fWcvdkGRUpR_Gl5eNhCE1kipEhqx7GSZ-TKMa_oARM7ZBoo7l5erZNIsjqL6r1XVjJb4TRVKo6Usn51s6qCcrmjLJ_eZe62n0NCNiEBCm8l9EU-XX95NCZOCRthiYzl0LHdcrUg-S65poYbKq-h8fTpME0sZ6f2AxU1JETW1B1JrN4ImTZDN41sBdE9CxQ6iNQVoqM35TwMqy2UDB6NoOt_q8b8qvF_XABzCBxHMyY1N8MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdfm-u2YQ12f3RV15iBM8MDoYudQYrnfdrlMtcyC1ouSfcvWuaUHn3PLU9F93vx29Ww1jbXYyHQKnfShLMDY7dQXCGIJ1Hn9AKW0-RpwmmhJX_YPQNg_kL3VO2TCIyQHP0Vk3l7zkcZRZHApcqU-1HEDrd-vGbjIHp4Z-eslTl4kDCR1nmu6O_TZenz6YpE9HG5_SXy4FY2jtJ0z8POtaGQUyXZ99kkni6pNNjd814ohbw8itdLwGLDkLCoi5kVeKE8V-6FQHPx0SIISo9bL4355PWASq-EIY-BZncQtYwZvOwU2m4kteQdjBj2mRS55_M0Ww1YFXECHlUifypGizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=CFC2mlZRj-jx28LOqUtpRvaHkvAXMi7_n7Sm0aAmGSFDpwC2aVY-8UpqetpFcZeJjr5Zvm5NFp52W2c1YimOffMOFb2c8XQgICY4QXVltW632Zh5wjtXK-_Ct_Ob8Rf3tDATE8ZwcpjEanB7YtP-kaS-8r_cew81LMPgk9g5UsCWUu_bxzSKmLFEt7t2ZD9dx30-ECCLYZjDp05YWByd5jpn3RKAnVs6RHKmhuoLAWVW_RHOB5_snlH8fLf_fR-gcM9V1pCM-4KkbE_ervpO9te0zJbYQ_ts3x_RAciWcvfVefPKTN5Iz372sBCwTUNe9Y3ESHG3dCYvrFWMNmLe6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=CFC2mlZRj-jx28LOqUtpRvaHkvAXMi7_n7Sm0aAmGSFDpwC2aVY-8UpqetpFcZeJjr5Zvm5NFp52W2c1YimOffMOFb2c8XQgICY4QXVltW632Zh5wjtXK-_Ct_Ob8Rf3tDATE8ZwcpjEanB7YtP-kaS-8r_cew81LMPgk9g5UsCWUu_bxzSKmLFEt7t2ZD9dx30-ECCLYZjDp05YWByd5jpn3RKAnVs6RHKmhuoLAWVW_RHOB5_snlH8fLf_fR-gcM9V1pCM-4KkbE_ervpO9te0zJbYQ_ts3x_RAciWcvfVefPKTN5Iz372sBCwTUNe9Y3ESHG3dCYvrFWMNmLe6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=Kw0NWvE2J2pr7oyj88XwLixJAtD-MOmtRCLdBnCUAydIayPXwwirUgBOgmqsL5aT8MEAWwOpKV-fRkZpICwae9wLZRJL_uWPsy9hqFkpA8WcH8EPKfPZO3ch49liqOCQnHAC1Dikk9IipkkTaVZJ2RgZTneDit7V_OAHO40sIu757ZSXYxadwbriA2rWecYCFMnsF-0zwM4yFfElSoQH5-wzXfg4ZgjhrBZbazhg63K-hhNcSViD1W5BpCAlt99sVPFaRKD-TCKX4ZJ4LvljBZ1jDXlx7oknx4wPO5evQKqb-_qOoNbJQ7PthzYeGkPOckDaRS9eB4m9LwC0Y_XuJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=Kw0NWvE2J2pr7oyj88XwLixJAtD-MOmtRCLdBnCUAydIayPXwwirUgBOgmqsL5aT8MEAWwOpKV-fRkZpICwae9wLZRJL_uWPsy9hqFkpA8WcH8EPKfPZO3ch49liqOCQnHAC1Dikk9IipkkTaVZJ2RgZTneDit7V_OAHO40sIu757ZSXYxadwbriA2rWecYCFMnsF-0zwM4yFfElSoQH5-wzXfg4ZgjhrBZbazhg63K-hhNcSViD1W5BpCAlt99sVPFaRKD-TCKX4ZJ4LvljBZ1jDXlx7oknx4wPO5evQKqb-_qOoNbJQ7PthzYeGkPOckDaRS9eB4m9LwC0Y_XuJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
