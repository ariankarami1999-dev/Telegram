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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfeD03qy1tcb-6wbXOcoz_OBjZmtacSKMqVRxY8QDwNIZpNFMpyRAKWWAQQ6eG3khOREu0301xJUSMo00ZVYSd-zAh3l4JDEl8Dbwu6lPsgOeoRLWAGJK61KTbmTVUbUNiT5t3Dh3-kb8iiSidlpQSYhfkVTqZMJSO17Ez8s3xu5PsOH5ZuT-cxHnIPPPqAYkE_oplROqjZd20FGecKFGmtRf8-G6TV_v9p1tkrm7q4-_Pc6hjcldlXEBXVmJDQ7DvsbT7wfUsIQzwbBydy6Nu7_gF9z66W1oPD0ffKteTg5bzF_n9ymcby_YvvP4BzZ0xjoh2mvLxo2e1o4aQacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/23086" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CmPKkCYd1EIodInutxIk7_QSzFT_GjyZRWFluSl4Bqc_lXaAq8Zk1w-ENeYirS8g8piNQ5pktsLqmIKUcF510RzwY0pN7GtntIonCagxAeO09G3wHbT2xMNQ2iTpQyVVljuRFuqb_IsMvd3GHCF2G6pm2kxNdZdNGwQFTF_YzBSVanB78C6Zew1fWQV14w0JWBi8GEJxVx-YeOHGLJmMNUqSoZdXNuRGn3bwWtP-ykjsz1zLJDNKfcrspNTwT_2aCf_FLydFvmeQVjcztEyAhaWrFao1Ta7cgj0_KPXC93TO1uu0Yx0djSz_Y8-S9GEt5RUTTMkeM5NwGQ5xpLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m84KOmFAZll9W9oPfFSok7x24ob16TLN10dakY8CyH2KQKKQPVt4nf1RTa1TBLd2uJjeRbbS0z9gZbfEHOJ_7KIiJAAY_c3er1qmt5DrZD__2M8XF0jNC7fnd8M0lNh7Z3-2oQA9Sxf08krPiIMUUG4y2xo12oDWxv4bHw1OBtRqN8jp9kN6KlrOpeGWns4o6lswjH32MiXfCUwQGwE24OJSUJlOMinnWz17x5VKZ_835VhLP4F-kqPtJ_vebZEzfbnW_tXsIxsL6HtzADy0_iEI2JS9AJfnY5dvRd_s9tBt8FgChQYkWKkpXMARhaNjaEPWrQFrucAsa5ZxNzvUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbtQpMFb69pQY29TrKXa38ea68p0KD_Aq0eKWTwUetTrvZOIsyLYcvNVHOV_hPUqQiVnIt_CsG2qYZC9AntLbg6I7QI1qKjU-amS7jO9olLmhUwLQvQMqGgOqoU3wMGJIheqw6BQToMO10l4CzszTxnDuNTWlgK3Zl5oXZ946WWqNDiLyjad77-EX6rTyCrJRyEQRUPBqS2ycbYHZPJDBmeO37oaxF8krvnc8jeEMaXzcO4IuElJscABbFj0lOLiA4xLGmsKA9-02cZO3wemZS5i5f6HXSDjOo7kNR7x5TxqDHuhFQyWqT4DUqu9z-qo5XxY9POsldj3XuBsRaLpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZejtzpaI82aaI1L3M4xYLVuLelSrmSjbIFqzyo7kmr5SMXITBCuamZccrapxWXeAxVjB1HtMgkbjm0K83xHaenG8jaDRZsOc-WHd-NA_8ITGUrJtx4yIuOUq_DmvoFj1fgl3Zxvtm9iAkgVg8STLvERcqY2wAbgXwJOax1EVdhROOlwkOHZMVinLdD8BfL-7HxShlxZkxsrLJRA2FWT2QiolbcFg7NHy5VEVPu02gHIwSiV9KYymPsejDrhqiGUjPvFWY8IVeBfg3uFF4q6RfOzK4HjdQqaP25I26QhNQu9_pBBiHfGnwFmRa7xJ_EWIPifnrpB-I1hgQFAwDZUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyF-7Z2LvhwUKK-Nny-1LCkegydzNKrJDJcUjpclvw4FTdsm94KkIyiizIrN-L462RBPeScC-pOmk2eQS3_gMsaZe15Xw_Foi8NVrUyi5xsa_Qj4PRLqmNKi-qkIng8icRbuQDqEtRo6kQCoctPzfG_4h8O0khe1pfxQN55mXxRtszOP_b-e86naHZsSafGBz4KyF3yGjOoZ9RZjukVvO40sbGg25BYbpTJMwIX7jaZMvij-1VTxCzz_dYmOrnLElhrKlFVymSYS4xv4lH7Yxis9wqGk_9X8w3b2dAB7LmrXXyDESnGFhnDZ_M9HODRzUgtCsPisD7m94_DDFGzTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp74hPxsVbXsmDwIUx9pm7UbUrNYaROSdmDMIHFFqqL3jREpwkoVF5mfi61Mh9GKR_uMiLsK7-Jww4lWToJBDdtCzsfAajt1d6VtMdj9HAXZMSi_rOvvBIaic3H7AOAkVgiDHuFcwiH9BR18LiDjDdTqhjupVLRNRciavus97q35CQ0Vyu2q54uJFIbXa3pgEFRWz_BmT5ms_7DoHBDkgpDvyaB8p-uwa5evW9KN8XvnQVqdBEUQrY8PKYomv0JhuJDI2C34iTjqKww8sSYsYluepBpkD8WxclWsI0nVhNu_LOjhGPTK3KxDm_8H3CCS-0MbPsLqluO_JUqAkA8BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23063" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTWHWs0hptYdxNwH2yF3Sgn_PdYQObFWrw4Km_815OnKCUMOWqyPbBG3OsGb8Clx69_SK_D2cGjYQonKW46BExemizFDwj732piKn8a_p-KNQPH94V1TDIaN8V-0hBiLrKHgauRMJyLZn9z85bD3oYSx6rnJL18aQq1loE9XOhE6nnBx86AUmSk_dz3LVQz9Qvt9L6MSSzWkm5UXGAFO8uWGNrVlAGi5RJskndudBW_wXVeZCe3OpP0_KFD-Sv8x8ZuyjpfgImndsFgT27j0HuZqlhmOa7xPVwriDFOVg5RZUX5IkMNzifnoyORCuX1IKr0NzFXs2UEuRd0ma5SYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8TtL6ajxX0Bly-4B_RCIl2jeKthBgrSQDnLW6-vxyLJQ7PCEChhkCFZR1z6hLaBrApN5X6T8AniZIjGUQItNODW9N1u4zAa_pbP7ANF5yD5XC_tNDwSDvcihd7xYbIXv9Ve13VO7WOKvCs0-vUSz-Edn8RRQaN6RxAGap-2T1v-nnX61OFWbE1nXpyz668H-7JpPtGjQAef_GqswRt3ftmtbtnB5r2ziwDKOW-Ugto3exzEmVpTVnaY8nHP7o3Q7ygT3iMH8g3W-QzZQ-xbPj0kb2mD4TB5DHxCEoDKDE8rDD_kyGphLvmv6J2C0464vrJ5pH2ci83LRj7kUyNmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKEXbwrP73nV1zpDd7UsaS1Oi2IuvU88z2fxotFTvLkpDwOKbXfTlqKn0fRfyZpYDLrqiKAMw_KY9MPPTH_jGavv8MzzK6WkqkJLqQGESjLBafdLmuskMtc5PomsB9p3qlMj7tItRRsLleMwHuY8WI69HFGFjHMPUG_YOXSGjY188-OyGVihvczrC-MUGhhXz9FSGruiWCP7BoNyoRsuE3vNNbL1Y93ZSm5pMZrDM8C-4XiObgfBgRHE-7Bi7p02OrMkJjitD280tvHaLhlRSxBKxiZVaVYqmpJ-nG3Y0wfltCHyum4tODknNdvB01AoWbVkYNyiuNephljiLWnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVt4e-We8f5fJOsYq3ZVzQzi8staSJpS_BMoXe5ke4W40oOnPwPcLJmcUIexi5I6gHx78VA2xUtwiCm5cCbRpDKM0FhEH9crTOSrB6GOeLd8k47kIuO_kI5nsaGK3uvQ74hV3hszZI0GzQcpZo1wJDzCNb9B-EA5G9jplJTKOi6NhirjOPG4V0FwCRYXLA71a2TcCIR8gv3xmhSQM7_EtaC7Ez5w2OpQlDu-yLNFAD3XaqOTwDa0nBwSzYrr7d2zdEmuxJudRHTE9u8qnRVDhgi_NKgj30R-QHkSeJYF09ji6yUV77wi-i8a9l00gruaSMU_D3gJjJUolKhDZIGeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK_TarTXIE6DQwKSb1IflMaugbj6Wttv5FXCL8GAGzCUKEvIthGrx0FF2jFGGzV3FW-6q1zaL_HAk3xhI3UTWVOzFGOe_uxnUYnIHwMChu-le-i8cotuAwH2FJ2W9QQVIufKs7DUE3YQy7AS--oCwm4bBx3ZEHbyt5nw0GW2--KYfuEgquOL1AaLH22Wxozonhi6bVtsvH63mok_-Cyo2pkIfgPCUS9Tk0Grq0OOPC7mXgppM4iL65s2vrQHCsW6l_tPnxK8fr2rxaujilj-if4IntxAElQoikgsuiNTAzlhr5cJQeLIT77jfLMw2zSAS1-bgRTghRkuKgJZsj19Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=dHL6L1MSYYrm-SeLC7sxtm_JmiG5BtO7j5c7Xr3gDVmKm2o3Bybo9rngsLiKzIs84aXsDuEWF3ZACx8X9DVZl8uyYrINqjQnrBg24f7uxIrjTz1bZIDSSX5u9F9T5w5TmQUE1CRFPXef9KB9z8TKDqzMveW1KVf4mbYGvV2dSlZ7oXC6p1Ya8CoZsNq4SalvTGcoDdxYVvZICtJgf7CIWBkIOLvRdWeacioMW6XaZm3YpBzV4cviEE874ToBPAcGAGrr69XmHO2EL25LO0ANYka6G3OE337taqIiZd_8-xYd9JQF_HrsDZo9aL4dnKYNe7S9Yihff8UYSi0p3tikDpiQ8A9FTEN7WTuUxW3AcvqqIKd7MFaJEm-qHtRTgT80tC2aSMUJJu6Wug__wfKhHUIc8sXaXnZFIBbzk3FmJVI_x-RSame5ygTKIY7PttfPBjOfU5LeKGBWN1zGnZhJe4ToG4nuE9R_gAiiF2smusdYauN6I8GAPhnP7TN1HjXEsVxkGFUUB2n0MUXEpYUPbzKozReqHCaQMpBaD1D6iAo8RCSwfNreCmS2X8ZG2c_fB3BG_VClxfzHfY_IHsLfSPe5T5XPXA3SgqqGp82VDhUmNYCpoecBHc--l1J3ersZbSmw6IdpexULibkhES-O1vWi_6MJFgOXevjtN-BZo3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=dHL6L1MSYYrm-SeLC7sxtm_JmiG5BtO7j5c7Xr3gDVmKm2o3Bybo9rngsLiKzIs84aXsDuEWF3ZACx8X9DVZl8uyYrINqjQnrBg24f7uxIrjTz1bZIDSSX5u9F9T5w5TmQUE1CRFPXef9KB9z8TKDqzMveW1KVf4mbYGvV2dSlZ7oXC6p1Ya8CoZsNq4SalvTGcoDdxYVvZICtJgf7CIWBkIOLvRdWeacioMW6XaZm3YpBzV4cviEE874ToBPAcGAGrr69XmHO2EL25LO0ANYka6G3OE337taqIiZd_8-xYd9JQF_HrsDZo9aL4dnKYNe7S9Yihff8UYSi0p3tikDpiQ8A9FTEN7WTuUxW3AcvqqIKd7MFaJEm-qHtRTgT80tC2aSMUJJu6Wug__wfKhHUIc8sXaXnZFIBbzk3FmJVI_x-RSame5ygTKIY7PttfPBjOfU5LeKGBWN1zGnZhJe4ToG4nuE9R_gAiiF2smusdYauN6I8GAPhnP7TN1HjXEsVxkGFUUB2n0MUXEpYUPbzKozReqHCaQMpBaD1D6iAo8RCSwfNreCmS2X8ZG2c_fB3BG_VClxfzHfY_IHsLfSPe5T5XPXA3SgqqGp82VDhUmNYCpoecBHc--l1J3ersZbSmw6IdpexULibkhES-O1vWi_6MJFgOXevjtN-BZo3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFzmYVVUlZzhKmesRRExf_31xtqkBYZzT-FFWI7OVgNpEq-knt7S7oRbZknLUYwLCnUX6CLRvGP_p6xSpI_cuWBRxtD-Rjn-E-vwrKWbcQ_f3WTBJltAxj9YsTssKfkq8DBsNGwUsyxgwhRmqgGCXFvFMcG3zBNk49R-v5LWOMYMZImwVYXr0W9qvGx1p9Ll_V1mj0D6ioTMu7bUdJ4nDgBsDh1Pa8eJjrH9mOcKeQe_-LOJJchsaB_HI0UecPUZfkyWnvikT1R3UaHie88hb2InS1_0pQvgxQbGm675kc0yIT27cy-EMuW9xkY7c6_Yp8JFahym-88S0B38R4tUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC1zQa59ePLvuGc4_F9MQnpWgGmSq2Sv7Wdv6nj5CwovRbT3gepsE4FDF4JQ9Spy9TLQaNa7kFhe-iSr0udrejSNIiPIrUdEOqhlLHalN0uEsejlDzeXdVaV0XZeLdL7-vHbNFFyWV1s6nUjg7PQH2URJRujZx8ZSAvgWt_J6gCaCfutC8RzERg6XijHgRmQVr1YQYCEKHWxmyjXFkMfHXUiY6J6ZIFTx4_NECKl1fGpnfnWgmunLzUrC7OFzm8pQ06Smfms33m9nLMWgbVzK-y9xbq_OgYby45Re2CKjGidmP3mab8ZzdU9jtw-7QGgHewVBtRF19R0htmJjqlUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr_C6RIsmtzdNySy48NR4-IrQBR64dq53ASA4bJc532lQEh09HHT8TVA2sRXw-a3EKAyerYfgwkBodsnbqLzoj6erkjFLpTBcEwVyfa_V-UurWauC0-_zkFIkkqpWj2_AqX1J9N5e18qt8TOq-veL93IPqUtmw4OK_ivCrxwdh5QJd60Ay3Kqvp8O6R9AzAE5wB9BG7SGPqFidm-OSoKwWhG-dTYhO-n47QxL6jMp-GqUAP6AkScBQTr_sn6wNcg4Ism86UkGU2q0wB64uypBkLMyJGetY-ejwpLc_Cv43Uvjna0odcOX7I9f29EngnACp5gSQL_ygcuoDmzJAOwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf3ENjxfYQaO1O6yyYiwKyKUIdJONZ22r-iCuDHGdNU-t6EE4kVTAA8AECY5EzRDAxp1V1ZW8P6dGmsiZJccDatkKJ6WE8cZhi5gzuV9oDDRyMbIlpBXhioccudP4q48npc-zoiNHDDK7ZoslWXPorhREyzcNVr8xILffpotNtpEVAeLIyrxcfzvTJd8gURoI2Njwbetsq5iYHrISexBOldCtUuJwOd9qR6nSbC7ad0WHxM3elt7h0oyAiGBZXAj-xWXueE6yHingiGk6BTB8Tymnn2XfN1oM45PKbmozWmWVTdUXVob7GauOOXU2zoqMYkeCs1ORSJ6uqrOlrT9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4bKuvr7bqiS2Tvmq6I2wjmzeRd86aQysKAtlrIqyyBp8ckMhlf3KHfzdgzgwcHax03YznDCFaJrqQDPgthg_d45tf-aJOBBcKVBX2-mPHUqOY94TAVbi6Il4axhQQiEZ5wDjadh1sYALryxpb7WfOhN9MaIgrrS7w8lnSq1AhIQCFvpjMFliksDSIcRI_MH_Owsd5oECNaiyZt0LPPwCLpi1VITyZvcgmZ2lZ6HQcEJEExBQNqL0qIcAa0w4r5XHkAsE7LoZUyrdpgXcUZCnjX-j9qEwB7W-TAUuzqqsQqpY-2qeE6HTKtSt3DFMwOnYHfy41EP3Mdzf1GYy-9avQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxiujuup-DHwCcGVKITpwrzaELHTnwtZIgy9zviY-p1FL3PJmYEVhiINToP3q4UKLwgfAigEWUvQ5OugFg4T3yar3HJnOGSq-WKe8tOjWUQqs1DIS7DsrOrJaZCk4P8ivQDkB0cbDaVjivYRrm0FaAk2nG-HkmjJg2mXUtuMzXk4N4TMssSIHat-DXpxMslFb8RCJ8GxvuBgisvjIAKxe2B15lYORMMJs1vOuB3hza1udkr5q55Q2u_Ls4eOd18ThlvLZ0RCQGZXS_6gTMjZtqFm-D4--qbpJWjGNlxXYRjFxBGR592a7JllXPWFMpbSATXIbAVeZUmo_kcY_QDwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PraBeMWdbjjbnXo0VTUl-fid4QRFFUJOzdR99ZwFnTse55GJ_dlJooRG-3GXiMaferkKXI0oX05H3cnEhupk-O_ZhCgevGd500yUShuiO859mMBPORIoExm6qE9F23jpr1yLQZTa3jYcNU8Bl_6_MotVPNj4aq1V2LRGVoLydksbFsR9lTBvmkF5BwSdHRPbfiE8Tnv3HOGM8vxt5LB84BavNoLylp3Xf64J_972-5IhUPxKr6mnRdW9BKYF2B62BTt80X8jUpPswuI0FObth405WyHbTEWQgkzoywYeY8HMaquJocKuqoCFBhxWQtsJGtnK5WR-KvNgiW4ETv_dFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFgkfChBCfoGPW9bSjmcgsTr3agDq5h9ajjl4jDnAJTHH-9lBe_u6V-6zgJ07JsJorThYNCXFusUVK6z7UuiuY50o7IQ65ixCQNVR0-QZbJrsQUiNRC3_wOcpE9vXryTMl4mXurNXCMxCIFjK9XfRfcTNAsYRQ0EMkZX6b6KsAWseMHtGd3LfG8b-_H4oqVg1SqAOdPrMknkcLwxFK7U-FXp9LE2-fBJNgSQ0hggB0wkPm2KHE293k02GSZ4n15Nl8qZL2BoIMS8n28Thvsd9GthDqXLiEXEVY_AQwNqeJyvPCryp5MMU0wb2xE2k54NDvxS4u1qwBLQvvnsqBuSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoBCF5WcnlqCyqudIeMLc4lKP0e78FhLOmwi-jz49BKfWRQEJ8aal_Z7ft37LxEFUZ0hu_CSRZ06L8rbN6Le80gZLyyt41rtMD3DdzYHLMBPhgvY3OMUwLUQtElszzEIBOlRVWrTYabISgW8uyxf-IFcHWgBbIM63Weq8CTGh6gzcd_dF_Zo9sTSJS11kTSisNtxLFTemveIGfkpGDo1Y5-LWZjVreJN8zNrVBWRkK0g83iI2U4aQS5NJiPOikB8E3ocTzYEClSoHGU8BR-hli6SKrq6MH-rDsVAg2_WL1bWKx8tQBwzL2yu7hv0XKOZBGm0XHeh21oyELHQtQJi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxsG1mfH43zr90ZJ5C11XaFFINmRvLX1XaYqqKtKw8zqvmjDA6i5ZKPqL51N4UjGbt69dL4dBFZ5Mge3b8qEihJI5qJTM8Z96pObBmCnKMoQgGavq0uHjEDEKOfgcDOVtZvrY7ApZyAWX7uswZwhKbQiWyZ0cBC6Y4zE8HjADhy9gFv4ohaggox5dcmFi_Pk3OqL8WljQaLumm43JUPS2atgeraD5i7KcU3bYYkTAxeqF-LRcwpBy0XEPzCz1Ze8EDH44amo1kaFxzWDAfjC1U0Fmv1PV7ZK6HcCCKE1QKfYuQKHGIJ4cTbG7ZCuuPdtvEGcov5727hTcK4RKslZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl1SKrP2C1o4L3yJrpX7K31qVJfOPOp5U2nJWWSsz2x0xyPiNrc25jfCBUAlEQo_qD0oHR5RGtodLUS82XvLQfF-Bp5vp5TZgu1UkblEtnk8wu9RXGDb3rv7IYwAlWxubcm7WpGhLmV8xtMeqEJLXz_ri9SRnh55o8NP_m8o8dOv_HsJy-nkmqTjdJ3cujK2pILbxUP7UwVQ5740dA5Zvpxg15zqpI3usc-T52vHNr4mBg14CpPZdF9UqjrVRE4Tkx1OCqUFnWOSDwcY524OEp9z7joEG6JpjsiUv7D9KwvGcfTyFLegYlOEJk9tGLCNz1RLNHDPdKMz9QiBS-Buew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_nnP8Qc7XF9PkIVOgSDiinkjjKAXYkPWijrdoCfk-HcKD9znlbJU0dEAmAAdVRYjSq_LFKYoh03aHb-a8OQnQtvQrY14L5tnHCSAByja_1jUakViTduavEhqP-CeYca4e5ZUw8qG8uwQM7YuV-Om9_ZAc6erOOS6U7dS8CTsEhuXyYNyMbhr3mTj5d4JSvYy9OmFtPzKWzzT5RIt4Y6Y22drCRBFMhTNQQDnyvid15YtM84v0f3yeiEEb90ddvtK_imngyGqtnh0Wvj2jcLO8oBtf61ySRZntHpQRda_JPPsQqIfmC1F5Krq2OQZIwCvIoIdsqGoyArx_tHLNyobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEHWiKsMBYaGyAA1DAnPX7qG9KTc1ER1iKsL1NpsjArGsRLHoewDMsvrbxtvmSFSNgC66HiM9ECR_ZNb2dNS-WtiJgb745M2tV1XcWlMR9NK_Fuqd5ZAezXAwKshrpleKCJe3AvqSwx7qByfqJ39_1vu4nasVteQ1NR9XavYK-h2G11n5ZRUu0Gm_BYpePfhfa09_HkHoEV-3dLTBuTHoIz1LgNKmKqnTggA64_g0TJR_2hSGaEPuDU3uo1xQv36NfrtyhpFkK-yKgYKSIbGEU9r67d_9maJqrHhr3xNZ4ZFm3Mlc9gxFnZYYytdgS1OpHMgDmIsJgjmmwLqqvPOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4UPzZE3w7Ny9sKpcDQUPcM8HOed-OPKWkXSoszXdI8_UxtpigalziGXYRpvdrmYN1RaGSq7rOi4DBDc1P-G-TeQKEzZ5tuQ9qLWbHfRPCdOpsGuBrs7iUQ0T8dQ8dkymKH1QxdqjRyCW4x3_N0IIvM9RDcftSjg_C2635Oi4uXS6bcJtGZcaMNofbVGVb0mTk6xkF65CF7HvZVse1NlS-qNAzpGsfx4DXf74o4E2P7WSuUE6t4SbWvUhWD1jU0I0L3MGOAOfq3eRvYggfI7I9d4ve5Udb14R3BtsZ5bI3vlwrLQhFdvsps-vVskzduYUt29tmzuQHMxItz4P1ZErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzm5AGHcA53pCy-7cVk54Hoq8ioz6m5oWXsgYcUIcTCzFiIievttkPa_Xtm8aVD078TmbV1qB3IXhNLjpTB4tbKvbF_IwX6YZyfBNlaF4ndTEKSMS7DuErJVg4lIMZUaBuXpMm_x-qEMYc5aUKy9reCRfQqYDbGcSjZRRNT8KAp4Nx0wqdYKDajHe-R4pvLn7HZjZerDteXCjlnZ4BwtKO-tW8BOJJ9I65q7kLLeRp2mQ95vte41-FwY6Q4tUAFu50dqne3cbVKISbjHRccAgz8B0ccpBxuVkQNBxTHXUQowtxEAjX66t9jS6n0VVT2RmM-p4g79l8HGRX4inAA1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OThc-DYPK3LVVDk9S3R82yE9oh9bP7rXX6aulIPkkyVll76PPKuAhF5Wb7mCWH9rBKGa0HrGm8awWxaxkNd1dtdJBufj9dD0plRk2D4JTG1TDSRKpDMivrB3Q8SrSrrt8fku9RYjxl-s-gDBh4AUEVqlNo31LDqaZMA_syNYj-wuDkzlnlScc-6Db9JTbhb1AETBeG9wIiO7mCzAtpa56nrmO5vH0bIDBacWIgEqYedT-CVZ6Td7WUrO9tqNEXHXd_RnqIl-cvbLTA78bKRML-Ud-hfibDF4Aoj_NOkRnivVmNeKYcBqOgd_GTf0Xfwzj91B-V_ejCVPiFTE8Fd7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpG0vy3ar_rzglOmkvTaQWH5FC-S2mDpHtiBn52Ct39Ytdr3vK-ObEggh2cH0zuPdbANGz8w7tpQ1XFljY-mGhfd9tnN6aC7HwedAM9Lk2oYDZS6nYr-9Z6v8PafVhgdyVZPY-j5cXcb-ruTHxE-TzmNNxbQJ7-Mjr4Eeh6zWglLInG_Spl_YSgVP9jKmk4niiBT8XpM3OMLHj2xGMqqezx4REdCcrJiuL0JmbYsKZ7ug5f4_SePWl-nos32Q16sh2owWohdb4-M8d_htqQtzIE7aY0lPs78AwGNlJMg7P5s6yHc1Lwm_GFZ0aHJ_AR4PchpzoLihjvR96eBJrnpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgqn_eaT2-XgjdTlrfMqoESbMoGmCYq84Cz3Bo58mZxQfBeTC80QMHr0pfRh_dpFRymoQhBW6eWoS9_5TAqKC73BR1lHwwIFtq3Z23vuU8JnHwZYMNwxEaIX67jmPSpXrO03JY2uPbfYDEXBncikJn3zHJg-__UN8klglM2w6c1f9eRH8DgfuRf6wuZ5FpNzATvwqMst7A84oBfQFGUg_Fwt9zJZTdN3yFubghevzcuHXMGSQuoo5UCkpxshLFcKl2cTfg4nHZPiU-w5FVBR3nrvGH_DGooRys9UP-VbfrpcqPu_sd7Ig5SJrjGTb6QW9K9ns4EHYkMaZlyY7lPHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=FOXFcTRTCW8ERVaWmZPuLGEu5jijcaXy_XMWUaaTZgLyo8v7RKn7U2Vv-FzhWwD46H3mhIbIcn7oCnON78GRA13Au9o5n5Tx8P1SKyVgyPO6JScTVyIj3ZCP0X2crVbEHhZNbp5n3qRYZjPxy4plvEV_qNSqNoYF5mKyF6TXeppSN_l--UjDKXNLKBqbjjBx-u0rUb7z1Wt548u2_DPLJTE3pIH_NJLia5LCRpo42aWmC6bfNDjLMuhyYLtgOY2UkjQIuwnhYE6n9G4TxEuAMw6bVvhVHso6nLOE5B_PsyykZwrGbgcMTX7PRYZ3xb8mJIFv2GqUb-bsJA96aJAfFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=FOXFcTRTCW8ERVaWmZPuLGEu5jijcaXy_XMWUaaTZgLyo8v7RKn7U2Vv-FzhWwD46H3mhIbIcn7oCnON78GRA13Au9o5n5Tx8P1SKyVgyPO6JScTVyIj3ZCP0X2crVbEHhZNbp5n3qRYZjPxy4plvEV_qNSqNoYF5mKyF6TXeppSN_l--UjDKXNLKBqbjjBx-u0rUb7z1Wt548u2_DPLJTE3pIH_NJLia5LCRpo42aWmC6bfNDjLMuhyYLtgOY2UkjQIuwnhYE6n9G4TxEuAMw6bVvhVHso6nLOE5B_PsyykZwrGbgcMTX7PRYZ3xb8mJIFv2GqUb-bsJA96aJAfFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1oqLzEIlVlM92bscvYvJhpthjEFHLYIppLM1nK_BbTXk3bhgwnreU56QrMz6tLFA1c0JITCrh41hOLAmH6kwN66xDnNfyHMqY0RXSYuMhAYcJnLiggdwrDoAiOS8tTfU2jH3A-oBiyzVnftlD7BCrdpd1aJ48tHo0JxFCS1NefbskcyIztOAHttLNnfa6Kb2WvoKG9T4qnMqI8jo0Rn2AeUtxBl8hu933t1924xdMRr_AjXFBLrqDM1N8k4XoQtlZEBV6c_8-NTwcKG83uVWJIeIJJ4cMRDdiohAMqhKBgazHNcYGRWagZcf67N-fEw5fdCci-ty_l_IgPOoAtifwEsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1oqLzEIlVlM92bscvYvJhpthjEFHLYIppLM1nK_BbTXk3bhgwnreU56QrMz6tLFA1c0JITCrh41hOLAmH6kwN66xDnNfyHMqY0RXSYuMhAYcJnLiggdwrDoAiOS8tTfU2jH3A-oBiyzVnftlD7BCrdpd1aJ48tHo0JxFCS1NefbskcyIztOAHttLNnfa6Kb2WvoKG9T4qnMqI8jo0Rn2AeUtxBl8hu933t1924xdMRr_AjXFBLrqDM1N8k4XoQtlZEBV6c_8-NTwcKG83uVWJIeIJJ4cMRDdiohAMqhKBgazHNcYGRWagZcf67N-fEw5fdCci-ty_l_IgPOoAtifwEsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYVrqircK-mrF-1JXUJq3NZB5x6Qe7pK5IcFFxzIvtO9XlbELL3uv1jycaisVB07l0El2DIKe0ouEhIgPCAAbBKILMhGcUVDQIHbwxyJzmvOCbH7cXw2ux2j0VRggdC7f-419cVt1flJ1zHSvwRuRS3kr__Sc8JVWqz5JI5g6kgYNSx6S1cwGPtS3W3f84c_Psu0yiq6PTYjpLQG-swf3Ax_WYLbbtjt4FuDTyC3fHHBuljGbyZmkT4GTsaeO7tEoctqYN9gxBVJ2aSrIrZTd_ZYFelulyvjt91FsRybqj8qJcRoR9jVGP5IkLRix8iuCD3EkHhpDJ7Ij_VJcAM-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXtUUXFX5YW8Xqyvi_IlcsybQpj71_f-_XI-nuwhhCNDQOW-TiYFZV19ezw4gFbiReywjC3KkFGNHspLOBwkdz4qxSh36Mp5azjRISp4q2kqxz7SlKChjgItTY91WB1Mql26hg_mvcjzna8VBmbnN5x6KYa_moXzXZscfEqmwO3TyN3jZVi0M_iXs_Zw57edjtb0px3hNjzR0CFrYMGxV3omMshR2q45x0z6w8D1mKkahT-ZgEYL7CfGp8qsPWdbqw2vwqSDP-GTBIo_zJW5LwEeNTe0h7y_Trti6QK_O4JU4WkAxURhEhFKb6BC68JBsfvHMSJu3NmtidQ0ajmRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGG9tF4dBD7Rli-YGYP__Izj-MC6sg9bo1RvoirzcxKl_arqHYoCIozsobu4NFRp1EiemE63dwbgWCaMHnW9UpcCwIseikCgEgL3HIu267nVWBUnFM2SO8qnZMOUygaAMOxE8AEw_BF_9tluaupAvB3KS-yZ41QwICs3_nGE0zglx2zSXiKXEro-ehNvfjLKxSXp2D0VQGIF8Saj07RdtgdKAKa-Wz8VSS8ml3K2DujkaHgDDK8inoniouB7SVAzT_DLzkBuccWiu6SutTOp30aMIoeuDbXjSUmU2578VrasO09tst86_NMFXjjPLUCPkZdUuOoTTrRkHJ-tctGTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpTzPWr0GjW5SmbRhiDspA9QVzQZXiy30Z8MCf6cayer947GhkIcf-vYygTWiCNqEi9Hh7NrDzn4ofjyBDYsIpMXxKhsiC8ms0JU8gBasWFvX5q4U-MA7_7xlC4BtFrZjS2y28jwW77uEQgzsge0DwL926yXUaC56RjZkoeajCcbLcJ18q1EZhhUVNsNLstqxYPnLlruao6cWPAkAIrHDhCnBLydl-1gnI0YUbo9xQzXIa6YfB87Lirerl-FAxhcJHMHpKS_SAWhlj22X6gzSQak3m3fnbwGAGx-LUvczeSTwt1ukrnkiKwouXoQnE_331qRyv1rUzeDYXoRif_q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdCTF2QOWvg07jc9voD4F39tES7vmJ4JCSO5jMbhsX5_A_MxqH03ScgZEHgFj5ntJZ7ILUI1G993G7BJmt1ZsrRWqp2V0qbOWuzrh34WIPsIYF1GfuOnu6ujk1cdZZfmNVJvp7oFJ8pjDIy_hxrIsDRb3SBhLd1kTIjlcLMVA53Ii8MgJ93MD1PvBEoN0VKsdCqKfnEROSTn8m9PqK1Kvrt4LwoziKg9KGbZPz6yEmSN888EUm5OhbW4g3dpxD5mA-XOFR_E-Tx-r91C-jObSekpEYbuKMMQ94W1Z_qbCxvnTsETU4vMhZ8qeQLMgtGEiNDVMpsvpJobEyNYpzbVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ2BAYaqZFQVfMeBsuZrLaytu0m_JjDjVTX0n5jumDuetatBjdHSjeUoswG1KzGkRMX5H91aJMtx_Di9JFoNs0TuaZjuD2zeyPVhU64zz6d-6vp-Cy4zYyv6MwxoJ90Y0vmhv_z0rd11MtsQOa08CQhyGBXJkqNp_VXS-oAW8i6FLRWIHjzyvQOlUe5lq3BlEl3nH1FyrdAi5lrLVwILOeVKbBfNexWjLzf5XwS-1zSBiLfrzO1rZZCH2TMB2_Z8t7KOaW43P_0-mtJ-asG6W1zTtOXX2pZPipvpTAg9plxOTlGdL-XpBJuW5nmHGC5Mun5OJrJIknAI6G-OfcBWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crzH7z6mlxBBE5BshGYQVQwOQ3iaEvQsfgfBfv2IbmRztll8p3fCwLWkdCsGYoLKnHiwHPVyd31XdEz2bmxBlMLUV6w-R7T1df09WzwC11GDfpCVBeSZdCTq59CL20qS2rI9nwQiF0XXczzaOsIWVS5W_kRdeMuw0PhznPhMSIIsNa8bHGNrfPWyUKt5AuwH7OQTmXzEqZqHYz7iweH1f3lpOKe24GmI9jp6CQEj_eKo4uhZ1h6E-C_alIKqofeP-STTWpqFS81DQlRVKIk0-Kq32R1eiRtNBe8hYBowZwDVQknpDM-ERDVzuPhs20p_c2Wlaje_zol4eNXaYg8eFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaIO949g8dTTlcHYuEbnoftmSyIhYxyv3vSOSat0hRtpsFO1RfXxD9XZxejPtd1o1RNezq3tItqGHEUjY6pSfu4Uakov60DHL_u1ZlzGSY8o8tCmPOhGCjnjQrQtmO54GOwSR_R8BT9Fn4W--6NWgiuD5DIs9P2z8IuKD7zO-WunBsJa_z3Z4Q6PSbJ5uAlcPK9Wycjnb_Z-yp2qtxUATYPlzphKaSDFJnwHbiZ5d1OhEXdRP7psAqkHq_RkiEBflQLpWq7gHky8qOfV7gxtwXHlW_iXK9a3dEny64tRzwpYOVkscn_aFCymo0UQLLeeDAhTwjYVb1zFfpPPo42njg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=JPjzB7OFOno3BLp1_JxuObwlwrfY3Bj3fQBvI8wQ1R5dyOkzZuU9jy1IKNqZETjOrwIUvHnhvt-2jrrgkwDDQXg8qbz6RwQzbECbIl9BpSN37JqhKcBlPJGLlWIWLYeuYm_iu8cnARNIj5RJ-s3j4UWKulY05YUeDTttxu9TdkJzG0ZzGCaJH4kZibp1Gn4Y6wEl1rrEp3QiHVw8MC2cXY_H5r_I2ZUQG-U7ogdEw9h0fYB5s139xpaLpIF3hNudludzegPBypyNWa124w_DGDgyWaluYc-GL1O59R0ofuzozxnGUjWv9lpSyZsemz7GjfUM7oWe1KK9t7qDbVY1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=JPjzB7OFOno3BLp1_JxuObwlwrfY3Bj3fQBvI8wQ1R5dyOkzZuU9jy1IKNqZETjOrwIUvHnhvt-2jrrgkwDDQXg8qbz6RwQzbECbIl9BpSN37JqhKcBlPJGLlWIWLYeuYm_iu8cnARNIj5RJ-s3j4UWKulY05YUeDTttxu9TdkJzG0ZzGCaJH4kZibp1Gn4Y6wEl1rrEp3QiHVw8MC2cXY_H5r_I2ZUQG-U7ogdEw9h0fYB5s139xpaLpIF3hNudludzegPBypyNWa124w_DGDgyWaluYc-GL1O59R0ofuzozxnGUjWv9lpSyZsemz7GjfUM7oWe1KK9t7qDbVY1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKp9wSS-RE88GsAqbQjyCDCl-5YM45E8FU8DucC3SfKNZC1hFCegkGfhRe4_g-FHPaAwBImh8X00mhl6JqBum28BNvIrBmtUEB0Bjzm2SsDIYS1P59VMumHG_mBJySmDE79S1haOLIpYTIOGVBoJq8BueH-b70mzsZkaRUvrvF8YfHhMNx-OJ0KXOOU9vYz1cZphx1SY5Kq9feuwvFbST4HoEqQosB-6RnftmUwwuJL_fiorRN3EVrDtEIWwJibrY8GQB1q-eI0qFUYvJL2djWyaHlT51QBgCO2XQndz3eGfeG5JLuImFu-eAZhZOhDTkY1sl-uarKGb9yFyC0AU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sV4D8UbyktRpq1S5w3Df2Qy3tQKul_dmL7U9cj26qEQKgQq2SZv1VE0aRlySfQA2_g1dCRiPhzRHMFuEV4a8OQRBr0PAGY8pcAhKvKeVoRIQXGjGONZ116HpCr0DaWnTOOKax8viTTiBwGNyUC2Sm2cZDwBOuq-3Sl28DuIUL1IFlRNyUDee-odU-33Xw891QHJ0ZPp1phkI-4q_G4kTzsmBj2lD9Iw-O1qdKkDynGa9GeOCgesYU997NUMQZkpgZ_UaX6icWJl6GHQnSRe7znz0Fy0K9Ei-kTWNOdF1DlT-TXnqJu2DDq4D-RyiLGRSATINwhLxkXtfAEtO0dgOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=ecfnxKu5Ud148iWzC9ailb736MXAW-RDXm4O43uHJmIuOnfxaDIsKGvAbUop1jNiYQHU6ppW__IUJ-baREJpYmzyJ0mGHNKQ9octqbUZXRQ6Rz0tvrN-3CpQiMC9ZFqvcC87fUjLeabprjzXp6-BeVEmJufJrKj77WD3DWLuyyQ5eGUlObsx14GQulqS5Ohe5P90kV5_icz86ztgylBE07aYuPc9k2hsN0aN_vzhq0W18fUEirqaffU4K5BDsA3cSdu2BZFpXhyr9cM1_6xG5u9OLeaGzxunRda1nujoQq_rrnHQVT2drUnjax2FhDEQegqxPPZkR_BWA_OInB0OoGnNmlbkqc3JyCQdFLOwubjYLhnMWb5oL18wSlQK74fNLpadV32Vt1MFASJzNk8tb55SXt7QSSwvcPGvY6CjfBlDRhB4pzQEIEt-gLoPccJmhKW9QH2y0IbzegZLUYhbMd-Ddw7C3CUa8ZvNNmQXR1gTdFq9S1aAnw2iT6j36Vkzxx2h_5iJst7pjmM0gdwXJE1R8Xy5gMRXU4e3C-sguVFxJ6GDlC003_QF_-pUuIhGHVdTEMgX8TKiAYiol3k9eVgQxP9Nf778kyqBE3nqGPaPldZGvIm39zu5bhK7NOBXcsbxebUMdemOFEgu9AvS8vT_YB9xjfyiBoKQOpo2Ga4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=ecfnxKu5Ud148iWzC9ailb736MXAW-RDXm4O43uHJmIuOnfxaDIsKGvAbUop1jNiYQHU6ppW__IUJ-baREJpYmzyJ0mGHNKQ9octqbUZXRQ6Rz0tvrN-3CpQiMC9ZFqvcC87fUjLeabprjzXp6-BeVEmJufJrKj77WD3DWLuyyQ5eGUlObsx14GQulqS5Ohe5P90kV5_icz86ztgylBE07aYuPc9k2hsN0aN_vzhq0W18fUEirqaffU4K5BDsA3cSdu2BZFpXhyr9cM1_6xG5u9OLeaGzxunRda1nujoQq_rrnHQVT2drUnjax2FhDEQegqxPPZkR_BWA_OInB0OoGnNmlbkqc3JyCQdFLOwubjYLhnMWb5oL18wSlQK74fNLpadV32Vt1MFASJzNk8tb55SXt7QSSwvcPGvY6CjfBlDRhB4pzQEIEt-gLoPccJmhKW9QH2y0IbzegZLUYhbMd-Ddw7C3CUa8ZvNNmQXR1gTdFq9S1aAnw2iT6j36Vkzxx2h_5iJst7pjmM0gdwXJE1R8Xy5gMRXU4e3C-sguVFxJ6GDlC003_QF_-pUuIhGHVdTEMgX8TKiAYiol3k9eVgQxP9Nf778kyqBE3nqGPaPldZGvIm39zu5bhK7NOBXcsbxebUMdemOFEgu9AvS8vT_YB9xjfyiBoKQOpo2Ga4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpbJf1NZ8TEmtyeGMBJr8KaxPZ2yIhimkj-a6cDfxuSaFbAmZBt-dQjM_dZznC7z8vxzbfjPNepHsP0OYhnWfoSDaLTdpSTCyfzsa0czTOtxQScDkYIFbsBoPY-ZlB2sDtR4_8t8ElPWp6mipR-kNdnDOR29P1D9ge8QwCtXcEKWx1zbWWK1J9fnJM1xLM9E2JxzFapG2o2w4OB_CeUux_JcTv4ODoiVfPPvREXRA4yS-zD3-cm4QC8Kj6zcitBBMNRa1lATP_KAiD0Zu_FW2uA8wr7AvcRDtgESuCnZF5EuLi1FBE8TtyfcjzFSZx-q_h5jGdxmFtGQJXTvkw0Pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7LEbS8nYUmviSSRdrO7uQ2Aa_dONt1uMzBuoJL05UCZ3_Wrh6LElSJ8alKByrbZLXORr4l7dckizJvLKKEA1S41IlaqvW3JC_TPRrLWes8j1_1cnTdH3hgvsNavkEApk9xr_qNMnT91tXAjpq30XDCA8Lz8Cyh13VFMXCCudc6kCv4P0aEJod5uHQMVaHgRHWF6TBbMKitFeKuwfUnB7L0Ad5x7BipwAU_9BUKvs3FNPa-fGjQG8HdwD5D3gCVkev-xFddrIdDlWVFPMZCSIneqXMzFLoZS08CBsDe1kI2btD8qhlpL2YoGAaNNVV3kc46JPXLgtxK9PCpMjPc7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWg_Qki5owjw4WCtsHGeR_z4G8lnefyauwbdCvlUgRHym1H5EkdWgkpWkKBaWinMkKzQmFp6TweT79Pz5cgggpCYIrNOirZcHsERB1ruUIouOeEK9kfGEgbR7dd4QYJzWOpvYh6t-zmcMMoTGAH9pThRzP-z_3X2oDFY0IQOoINgbsa_2yMjIGwcxv6BC4JQiKfWcnUl0_EEln8FmvlNHjFLqdjQd_0Yw70E6Ux0RiI6tyncyBdL2SjJICiVYn9P-kx6yarbduHme2jtIVYdknUN8n5RsTGsEtJjqeHTP3GGD2lVnQ7yrrOE8xI1nLCxHAnfrJmLS_AMtoftMB1oBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPwExiCK9uiLPtWjFYyofMV3HYlW4eMmY4IXj5bfsFTwnWeFCJqq6MvUAsahJZy9kPkWG-IWCchuZF17IlazntzNDTs_gZyqZFkVdxX70P4weoMDmpQ9FEV8BfdwURAOeIItyz515VZPznFI8StVilir7gzvclpGDGwT8mAtshehA8t1v51xl7KPWbR5ry7j_0ElJy93NNNm2lRzBFv4pDlBCC1P6NUVo2jYEllNhMt1PkxkoPgs-4j6ddFEBrACCsC1PVLjBuhoxmuFEHKbRS8iDzV4Dufhzju0ApWr1UP0Hh9BwWIlyfKJNg4w8rm53uqjllkxDYXVad6JaHjHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=CZd6dFKAIx4kXaz-xPJgFGUI49Pssy0amkJo5p0s0mcDkeEaura5y0ZLtV7bCRQ6LG0n-ce4AINH3gbKlSQrXvzRtGOHZmd54j-KwlEnDczj9fkRm_7Fkdp4VD_kykJ6vnd9UjFmM2gCpVr7NqSj4JC59LfHw6INljsxMIe3CHbik5YArNpoFTkcffZgggb-UxVpJwgJOzBX9WghcULX8mJkH2FyLIrNJ4B8eLbyRgbUmyDhmgEQKOC5ZZCAFmJt3GPXNdQjxmj4cjh515T_ucS-flXZChsu2ljpu0GQOKdjEuIKOTjl1TDKzVX1S8gRuhXAnrGxDKiUCxi-O6ICkYFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=CZd6dFKAIx4kXaz-xPJgFGUI49Pssy0amkJo5p0s0mcDkeEaura5y0ZLtV7bCRQ6LG0n-ce4AINH3gbKlSQrXvzRtGOHZmd54j-KwlEnDczj9fkRm_7Fkdp4VD_kykJ6vnd9UjFmM2gCpVr7NqSj4JC59LfHw6INljsxMIe3CHbik5YArNpoFTkcffZgggb-UxVpJwgJOzBX9WghcULX8mJkH2FyLIrNJ4B8eLbyRgbUmyDhmgEQKOC5ZZCAFmJt3GPXNdQjxmj4cjh515T_ucS-flXZChsu2ljpu0GQOKdjEuIKOTjl1TDKzVX1S8gRuhXAnrGxDKiUCxi-O6ICkYFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=IAXXLJaWm-IM7OYnfxb7q-kfSZYEWEv_i5xOnKTA8ILOzCMVRMEXLLDXuq4c7bFeO8c7eMtDbsUWkaUcH_b7WNqzAILnG4KPZWX6Nh7KaVUkg01qfd988Z1AH9EHvPQitZhKQXz4EfD5TvLrwUGfYvkCQnQV8Uj12jQFrGyHJNlbYRpVvV978dPpjP6EvIbNH8gBDoJMp6uqsoOsH8Cj7fegPaeOYZHcehFSa8gcqXWZ8a4oqtXxZruzK4l4e_2Pe2LO1NFYDsL7ezHRLuXIdGZJohv906vR24npkmhD94ohNtRCUjRQIG3-sCC-0mi7a35-8fVtQ3FIENGvsTkW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=IAXXLJaWm-IM7OYnfxb7q-kfSZYEWEv_i5xOnKTA8ILOzCMVRMEXLLDXuq4c7bFeO8c7eMtDbsUWkaUcH_b7WNqzAILnG4KPZWX6Nh7KaVUkg01qfd988Z1AH9EHvPQitZhKQXz4EfD5TvLrwUGfYvkCQnQV8Uj12jQFrGyHJNlbYRpVvV978dPpjP6EvIbNH8gBDoJMp6uqsoOsH8Cj7fegPaeOYZHcehFSa8gcqXWZ8a4oqtXxZruzK4l4e_2Pe2LO1NFYDsL7ezHRLuXIdGZJohv906vR24npkmhD94ohNtRCUjRQIG3-sCC-0mi7a35-8fVtQ3FIENGvsTkW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgwFrYKPO3Q2x4ywg6YIaNuXyOoXZ8pTaGfDQL0TWCqZhU0G6R8zby3JfEMQsdTO90ef74t2k33MNI-YpVjH9rsoTrMU7XU7_3UYM-tT9Y_Hth64j9oiADp8Q0HJ-Nb5-N6Ulizj031TQYu8DLAXQJST5drmqupqo6ocl-MsLQzkmqxDpfUobzQf2-F3LCFpjzdT31umXmUsEp0paZiy_lMZ7EOTe9VssHxC3EvcexvF51XXat_qOBgIvbfezHSOPt6kXIDKYc2bjNTLE3Vc5eRTf-53wYhKW6y_46k8vz33Dwuz7cgwK3avQ6ZspIuX_1UXtAQdkAU0nyH6uivqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKo59DGB7ZPm2HSwlAFR_I1bwWAy2izr7EOV2QzXZTh5Iyq3COWmsbrTSy66yAdd7JpfXc5r36f77ZJgP5EFLjL9pCCM_q0H_DEB0Ga9kE0gcYgfV4Efj3lWZVNmZY-ESg-fo5MNyag6g75AE7VY7afG5znKWyjGoRH1AYwlJmhcl8UC-P-xXQhRhRCMF4Pq7Zt_YJ1fuZK5BMY6BjOf0GOEUTvUDClb0TnSMGHGr3N8AxNjZY7t_QZrruRNszzY43k07HMa3hHdL51N4DZVjracnAyU8kVGGmhWUKwKckLhoMtOfas8EvZb8LDE2UdzAdRRVuEpZeVpy4JGKR_qiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaaYHHexaYgs1VD8vAAH2Z4TdLOibBLgCelWL8qymJPm-qv0pXzNi0MRTgd-ER6V8cT4uuv2KEyDI57kek7IxJQl5YkQ-x1qRaNw86iQye2b6X01IihncPrUNZ7NkUWpIb7p5RYjfknWIc8pWZvAu4wT3hDhtUcHlHveHRAbWbIXk-adoSCnK6NaxB4gC-QOSlnhh-V3upad-21YWPfHU5qwsSyhqVNUJugX34b8Dv-1ziAaHcfdxTEcrDdILrVCoxoNv90f6wnIThFSlTlt13Pn8MQICT361HslViqrvfxKin-4wC_W4iOuXEvYmYysYBYocApZJPTdhk8KRdR2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9Od4Y-gJNbv8-_z4TFXOVLr8tvVYegWaElmW_0-ofCXJcxjXB4aLiYQ6QAhHd1-Q0cEGrQGkw1fuQRVhd94rIs05hFBDxMD60ZRcRvdfi5ZS--pCHffcXX8euYcOacjg44LYhYOGNDZOlW9KlufxK8lfhOzR8Zj9QwMyAKPIrGPgkH_t5genlJQ9gu7Q1zk_Hbw1kRf6cJDUjUjSf1BE928wEMG8wcIirPdAh5-LWpyMnt4Xaaxxv8gKFNU0gP5hkeqknUplO0_PbZIVYPGlcAz480wZB58alJM-1CoJO5Pj1aOSBkgfbQgkOYId_PLqdPf1QE-MlPvhWIqjT45iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viufsHXjFT_WAEAbMFWXm4b6ov6ZlK0Gmtd9boSiQz0kvLCwUTqLR41LLWDATzkx--6uRNUxDsHzGyHhn7ROjRf2oAshzZgsn-Wu5f8E19hRdwJeOyc2VpmBlsiEZD2shgSEcYDEXLD3LhkbJLjqmAZYAQoOiaZZdy_2Ik_5XvUDHv5PoQeWZmSC2Y619jr15PiS_sSwEG-O3GCLRr2vCnF8pDYNdt-LWN2ELgPty51AHv2tfZzBo2V-s6mtQjeu8CVZliitcTluqb-0VO1p5YS9432hFKINBCLS1otHBEcS7Xas8moH_aGB-KQnU8jRUDsMQA6k5Q3zBpOioztnzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=AzljzA6ZJEve95qnpqkGiRC-CF7b7LpiK8WvseUkyc8r5tSPeovY-fx0eTQqm1bu1Ykj8xw3FtN5J8u_YabxFwa_ICQ4kjEb2GLNJbcmm5a1GALA4Eh4T3LM0Ge0pcWForXc_rsfpPSDvAq87V67cSAmWui0zwowN9vYga7mWrqpFXQ3RjCzH1mVet6ciLBHdVSJMCvta8AmpTVefWZpeq0As9iF3eFGT7TwmH2Bgl3Cu_QDefG9ema6l0vm-x8-wnORZtmq64j01JHuALz8s7j8V7GItp-59WkaHwEtWO2GmJ99Bcxz0_VlJs7jLXbHrdsCaWNp317wuM5l9GpyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=AzljzA6ZJEve95qnpqkGiRC-CF7b7LpiK8WvseUkyc8r5tSPeovY-fx0eTQqm1bu1Ykj8xw3FtN5J8u_YabxFwa_ICQ4kjEb2GLNJbcmm5a1GALA4Eh4T3LM0Ge0pcWForXc_rsfpPSDvAq87V67cSAmWui0zwowN9vYga7mWrqpFXQ3RjCzH1mVet6ciLBHdVSJMCvta8AmpTVefWZpeq0As9iF3eFGT7TwmH2Bgl3Cu_QDefG9ema6l0vm-x8-wnORZtmq64j01JHuALz8s7j8V7GItp-59WkaHwEtWO2GmJ99Bcxz0_VlJs7jLXbHrdsCaWNp317wuM5l9GpyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGYANWgOR5mLR136AdH-nmpd8MKET1rGDIkD3PigN6FvBMCphVXpI_E7632xpGaXfN5libLr6sKCV7EVM2sXdKoHXMoWS8pdqaYL4b7MRWLdO9O5S0B-fYoVU6mrqSXLifKJCt77JzGJlOGD5GyMZ2KdKGJdy6q9jQii19sPLFswK_1nRF6Ek_WlQ4_kQiQHx-eFAE8y6yQfBTQFBj4YTe03_8iV8ruBW6Bri9L-9IJN1CyMUpecGJUhJiZDi9PxVLE1lKVZFfuj7IfGnU7Y9uTTxjtTdrDrXBZksch0E_DI-KUyo8FeNmKlHe0Mf8s34JsB_PKJpFw9wY2W72gIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RL7FPer6YJ3SbPlaNa-PDnP2aXV6PtUNpmDaKjXyThVqzAXKzYqKxfU6E6i_6dL3k10SF7fiw9nYRKkVej1V9t-qVEcaiYcKn-DhBXqTl3LcMflslhi3pf4JteX-miho2eJb6Ls1BLlqAy4JRV_CCgmERwkRmM6fWQr_qyfXMVPeGTEf-pGHALgxRtCXABK_pqzLBmvzDRGKV6oE2Yk9iVdUJ5zXEZ_AflNwEAwfrXuZ1Xgq1eGwWGSs-Oke57irHUBJyQZvnP9nSonhrQZRGeMz7II_Tb5bWO2Gx2oXaLbX1c_OqAEXQOVMs7agpw_yUyt9zO0Rwct8Xl-5ycXlqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=RL7FPer6YJ3SbPlaNa-PDnP2aXV6PtUNpmDaKjXyThVqzAXKzYqKxfU6E6i_6dL3k10SF7fiw9nYRKkVej1V9t-qVEcaiYcKn-DhBXqTl3LcMflslhi3pf4JteX-miho2eJb6Ls1BLlqAy4JRV_CCgmERwkRmM6fWQr_qyfXMVPeGTEf-pGHALgxRtCXABK_pqzLBmvzDRGKV6oE2Yk9iVdUJ5zXEZ_AflNwEAwfrXuZ1Xgq1eGwWGSs-Oke57irHUBJyQZvnP9nSonhrQZRGeMz7II_Tb5bWO2Gx2oXaLbX1c_OqAEXQOVMs7agpw_yUyt9zO0Rwct8Xl-5ycXlqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPhT6EdVz8boSRNmjUEv4Ckjadjd8TBQ5NQ_Wp7ZJtv0gh27NamIFiH0aDTUkIIHNkaDxy-_Ix-57kcuz8Nn90mk19l1ODMjthHMJ0k7f4SW7yutsK801rxaU6LsYSzurDBg_lnsmaZFtqf49LcdE48C1zFMuyB-lSwrMTH95Z-JDyS3FAZZo62Uooxb2lYKuuj4s2y0-Ifq_j9xpHwp2at4equV3Yu4jQPtoO1JPKEBDmo781eHyoXVyD-y50ULZUFtlpYgTinLIJLn1MaoLslIIEPGEXs-fpuK6Ir97x0kiQ_guK7gujWm4uhoZLTk8dXU9fXYspDtES5m3KVyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHc8jsq8lGVRJohRQcBblJo7LYZaHlxd-TlL1j0NgqDMt8AWXG-xvwVjvKsqBN3Vzxwy1TUPWX1CciwmCwxEuFvACJ_VYUmgDxU9fUdTHpzJx_9KeDKKVUXiq2N5Idgm0vPgdHj09EQp0UtzZ9TBEfKJJ5Lvm_oOrrCmah8t5l6QgodDZGnRB0OvbMivanlC8eu2UdzcTFmGjcfGd0s-5JsM605CEj9-bseDT5Tqe6mefFGu9bFOZQLjhKWStNOcHjT7wCjNyJ5c9T24LY6HtdnbTHf36KXPbSvzF0Ghked5K0IOqMbQy4lyrPmh_EnIN7vfkEMv7qNPtTg3Zz3dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=eDEmpLfm9eXw5izIcCM5Y_QLH9WGNvYm3T6rCRLqYuJVgGGFakgpGL2AsXQUhDuOLIfUrreL-4P0cvNJrwfN97cKJ0lLluH6_sX6Wy_3NnTJFraAC3GW1s4_dkErHXUaULNc1D0_gL2Rkke97J0ibu0T_S-y82uhQ-aQJGu0zd2X5D24KZWyRH-Q5_rpcEqHJBIoCdAyak2Y7a4-0CpoQFnS80GEGi8748cZCwyVg3jhGLvK2avRuan9rMrnFAdKrsijJiQYSv2Os411lnhwKgCflKKYdG0zdjJox4YjeQRYeN1jwXxEtRdA4MIYTOnZWU7ycDywepgdof3iIhw2gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=eDEmpLfm9eXw5izIcCM5Y_QLH9WGNvYm3T6rCRLqYuJVgGGFakgpGL2AsXQUhDuOLIfUrreL-4P0cvNJrwfN97cKJ0lLluH6_sX6Wy_3NnTJFraAC3GW1s4_dkErHXUaULNc1D0_gL2Rkke97J0ibu0T_S-y82uhQ-aQJGu0zd2X5D24KZWyRH-Q5_rpcEqHJBIoCdAyak2Y7a4-0CpoQFnS80GEGi8748cZCwyVg3jhGLvK2avRuan9rMrnFAdKrsijJiQYSv2Os411lnhwKgCflKKYdG0zdjJox4YjeQRYeN1jwXxEtRdA4MIYTOnZWU7ycDywepgdof3iIhw2gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFPIHLuz1zhWu9fCMGRD4qFvXq3PfZWvDp-zggrsFAxMVZ7vhsN-cLXhNp8TlCyCmrIJINfQ5cmlK0M-TIPkX3XaPONDBiOI8uuthoanU1Dgn25XG6rkXG06rzTFABxhiju0IzJ3-MbmoC6o2YFn0MDK9jY0-Fc2Ic8dPcI7_pyriktsr_eGsk2avQGx6saLlOtrZk8IkcFspcO5oreJLi7Bhc5Xr_eDmIKpKTgRGqZHNSd1GGZxUEq5DTEra40m9yC9x8pXX58BRV6W8uq786PdBIeSradriKv6vLLEiDjC0yMN8F8MZ1EQA2IWHgcwrnkynd5p2bDrJnZUehemPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdfm-u2YQ12f3RV15iBM8MDoYudQYrnfdrlMtcyC1ouSfcvWuaUHn3PLU9F93vx29Ww1jbXYyHQKnfShLMDY7dQXCGIJ1Hn9AKW0-RpwmmhJX_YPQNg_kL3VO2TCIyQHP0Vk3l7zkcZRZHApcqU-1HEDrd-vGbjIHp4Z-eslTl4kDCR1nmu6O_TZenz6YpE9HG5_SXy4FY2jtJ0z8POtaGQUyXZ99kkni6pNNjd814ohbw8itdLwGLDkLCoi5kVeKE8V-6FQHPx0SIISo9bL4355PWASq-EIY-BZncQtYwZvOwU2m4kteQdjBj2mRS55_M0Ww1YFXECHlUifypGizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=Sy3D0WNX99E9OzSO6orMY5mb19c5wnZivBvIPLMtVF4HNsdU-LbM2VORGpEAGNHFQrjCmZd-EXebNYQkF-JpcrwI2PR0T64C9Q8QqhQG83yn_kM2nGYgUypRuzEQ2HZWXuDW-D8tn-PEaNgSYw2CAX7zY4OFw_yfxzWmMZ2ZmlHQVTW5S5oVD9J8tcME71GG2X3OPH1N1m0bnU8XGh05d3umi2ItB11lxEQB51JeIzHK4e_nbJg6i2kOAuOwJboLBQjUgxwVtmSo56ClCdpCa_gPKxzqA_6oYgATAeXcdD-xYirOJEsTxoqfR_uwThbE_mGndoAP4TL8bNSLHJBiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=Sy3D0WNX99E9OzSO6orMY5mb19c5wnZivBvIPLMtVF4HNsdU-LbM2VORGpEAGNHFQrjCmZd-EXebNYQkF-JpcrwI2PR0T64C9Q8QqhQG83yn_kM2nGYgUypRuzEQ2HZWXuDW-D8tn-PEaNgSYw2CAX7zY4OFw_yfxzWmMZ2ZmlHQVTW5S5oVD9J8tcME71GG2X3OPH1N1m0bnU8XGh05d3umi2ItB11lxEQB51JeIzHK4e_nbJg6i2kOAuOwJboLBQjUgxwVtmSo56ClCdpCa_gPKxzqA_6oYgATAeXcdD-xYirOJEsTxoqfR_uwThbE_mGndoAP4TL8bNSLHJBiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
