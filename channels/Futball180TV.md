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
<img src="https://cdn5.telesco.pe/file/Aj2aWSJG0UXKpRu9MOq0_S_E2bDOfE9AChne8WTpd6SndE0yl1ggeGJDztFQ_tR4qJDIRXnYA6K3WB8sdMCGgnxfh9HSFRSIw4PZAJ9aUx5d5J6XFfpJJ4eDI9K0xdvXa15QNiEVmt6g2BCgUC4FC4i3a_MvDD6v9UV5viPXNzsUndc90McBwz0E2WsUFVI6VnKe0t7dBOx1nRb76MOhyrCQ-vwTg3icGQ_YnMxAISUK9R20sL7npEq0MQZWuiq9GiVNqwnUnaTD6JNJ0ysGUq4lmUFWHo2c9W9n2zwP5OHZ_HxLzLhDOM83XkZtUtpIRemM0paNxwKNsuhFm6NyCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 393K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-107767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انگلیس هفتا به کرواسی زده
😐
😳</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/Futball180TV/107767" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3svZS0ooJ2I66H3WhLNCP5FQvLaHkCkNEmtC9qwPgat-zRI8cxubJxyd1Q30pIaQ5ZDhqh_ktszUs14OHor96u1cx9lT5z8Vie5TMDqwzZxHL9dPxAPAhKr1HjWfXlStCy5GOQS43DXGSXmsCJv-62LcUdRd_M42nMesy2uOWJJSuPuj34oFBT9VWPybAWKlrq4PKDKdv4W1gmAvepozmzltnWyV_M1SQxj4F0LYuxG1B1DtjIE-dv2G0wEIyzn9pHBHExKTLJBKkgPQT6nmY-zhq6VEXGJ4J9oJ2Ng4jftequaAZ5vThuDUAM_iyDEwIsNRYgEQR7qjQzILA6bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب تیم‌ملی اسپانیا مقابل جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/107766" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107765">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXph2F0NtG56tvfXdaYrsWwdfGF8Tq6eMMTFSEyfY72QmKc4ifGw3Q25nW0y6xv21Wdei6VBs7cNCpIKfiPe6sQyxg8ycu_cerkB1PIRvHQySD4R7Zy3UxCkVSqMVCksUZimOdvtry1gPCyjZyexRTaN4hDWUIYjN4XquuwBE9K_MnCHRtI0B6qiXt2E-VKar9eTGNFd9WUOHk6cGq0ZJXhLsB0LrY12kSx5K_QqLDKyAVIj43kITJF-iTsU-mOkD-Rc_n-vcGn0TM5PCm_8p7xWxoBOEiWC1Qs52AT3mCiguVjDqom3O_mgzAPWtcfX_1kPcY899i_HUOdIIUS7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇧🇷
در سال ۲۰۲۲ رافینیا از لحاظ تعداد گل های زده شده در مقایسه وینیسیوس بسیار عقب تر بود اما او امروز توانسته دو گل بیشتر از وینیسیوس به ثمر برساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/Futball180TV/107765" target="_blank">📅 20:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4IltgvkgfwZtP624X-YKWY2STuc_aHA5pxBCTHT1P25fdIKr1gInNmFpGjFHCpI6P2j2WYIjX3OGTp0zfnXr9INHXKPhsyPzMAikrerWH5FXI5-OzNIj8uDZw-blvReApwus7bFsC3AwEi05v0kdottScn3jE-TD-hGYyLYiPSW-L41msI-M_gA-uAuS7Hge2r0UpZecMjBmm4JoguKlrZtE2MyOct-gSlb_cBGBXbsbEWH_QOo0dHkm08KFvplRoJqmtGinomf9IgPQHK3D6QxA-qsopwziyN1YJ3VURLA5rb1M-lW_-BfNmqRoyEJ0ynCLtb4jSDNd6IpdlKcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ویرجیل فن‌دایک در سال ٢٠٢۶ به اندازه کریستیانو رونالدو گل ملی بثمر رسانده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/107764" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsLc39PKvNz5b9njfPK9FwSIqKH-oqO-UgdOj6e2J6sJIzuZhjULRo2CldxIgdnZ4Ifzske_G8NlWdFbTnTpJNDaya2yWMPGZTiMWYm4JwzILzUzfqxXtFvNTRFseRZ0qPC0YEgoggXGYdgqDdfCa6uWbwTo3mrha7Uk-gxPApsBGd0YCp64S_Z-HGdx0IEQ_ljUuifDTCkzfQLso1n1OpPrvA4lvbOuArIy2UiiAiteg1GHloyCdLkN6T2wKaeJamCRa0jsndADa0GsRRT66cdEzHheMIV6ksqOnU-XbSG_u8LGaSbBvZzydDF6gMRFlCySfQpxCLn8k03XRz66IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
روبرت لواندوفسکی پس از هت‌تریک برای تیم ملی لهستان در بازی امشب، شادی گل معروف لامین یامال کنار پرچم کرنر را تکرار کرد
🥹
🚩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/107763" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107762">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=j7NdWejDYgSIe5ojRH6qHcBBB2ewl_2FxqvEf04sSz4KhMfGxLrGqqGExWJnlmd-JDhHqgaLReDEJtd8tWhe-TRDWkRJIabFcOCA6rX-HXtzb3lVg5_VY22ikk-xqEk-eDzRdVUB6W2oNKcXTAOX27e5LWL5vRFiuWAfJKUm37UrAM37h4xaeM_xO49ioNjbiXgadtGILbSsKQnSMAZ0wwGCq5JAo8Zp8R-TGTWuYX1HcyctkIguDuK7rAYoincZphxUVVni4YuAaikZKPwSzOGVz3MoXcfn3thF9PRJz4HNHZl1rmirsLYbXeJRszeO0Y8CN-vrnGS4fveCLTdQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=j7NdWejDYgSIe5ojRH6qHcBBB2ewl_2FxqvEf04sSz4KhMfGxLrGqqGExWJnlmd-JDhHqgaLReDEJtd8tWhe-TRDWkRJIabFcOCA6rX-HXtzb3lVg5_VY22ikk-xqEk-eDzRdVUB6W2oNKcXTAOX27e5LWL5vRFiuWAfJKUm37UrAM37h4xaeM_xO49ioNjbiXgadtGILbSsKQnSMAZ0wwGCq5JAo8Zp8R-TGTWuYX1HcyctkIguDuK7rAYoincZphxUVVni4YuAaikZKPwSzOGVz3MoXcfn3thF9PRJz4HNHZl1rmirsLYbXeJRszeO0Y8CN-vrnGS4fveCLTdQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ترو خدا هوش مصنوعی رو از ایرانیا جدا کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107762" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107761">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsYaius3CufDqDDgnewrZ87grfdoop6QP-_y444OL5tvk6O1bO5tKq-4tgrrNBmHtTRUteawlICM9X-rjKs1iEDIHEaGIw_kpUqDlLGwTwEtEUV2TaOqMAPjCx2UaU2qM6KwxJETp0ykzL-x5h7HKuJW3dIlTah7rvlLpKTnSjXDM_kSUV7tKIuqsP5IdWaBMO08jotXEJk4i6dzGfkGkUzviR67RP2fuBscT4fPdabPQAOo9379GeZh-zYYLG_Mg9lqeTnFKGGERk44DWdiIgIvU3ZGGqSy3q2cjnxwSl0GfYc-l0F03EwGgl8ybr5Kh5iIiRW1N6EXVp0fFKQUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب انگلیس و کرواسی؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107761" target="_blank">📅 18:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107760">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=Ohc1y4YZn7OUhMrFUXNcVN3s57N4y1vgTLkfRtTC_ttH8-VGbUuqvGoUJb8BmPmRiVX_DDts7cXEW8AP1X8gl2FhPywjyX1aVcHL9MVY2Iw8Ze3yE1nB2IO0klBuPGc3Wl-85ex_GHgLHQRVSwl_d8hUJOw7zZIp9okO0Hw3EFL3ABD0mhDarvU2l3DUupKp7LWh1Dz8mPex870n_OgghuvtUWnBhp0Pz7U8PbJ0MPBp6Il_foEobeo83HI0I109ezyQDaaL8QTODml0RF4kxy0WM1YRsj4Y-eN_1kUmcxh69z30j5EBn3jfdBN8Ei1j9xl67nDXPA4PPqbMB17XKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=Ohc1y4YZn7OUhMrFUXNcVN3s57N4y1vgTLkfRtTC_ttH8-VGbUuqvGoUJb8BmPmRiVX_DDts7cXEW8AP1X8gl2FhPywjyX1aVcHL9MVY2Iw8Ze3yE1nB2IO0klBuPGc3Wl-85ex_GHgLHQRVSwl_d8hUJOw7zZIp9okO0Hw3EFL3ABD0mhDarvU2l3DUupKp7LWh1Dz8mPex870n_OgghuvtUWnBhp0Pz7U8PbJ0MPBp6Il_foEobeo83HI0I109ezyQDaaL8QTODml0RF4kxy0WM1YRsj4Y-eN_1kUmcxh69z30j5EBn3jfdBN8Ei1j9xl67nDXPA4PPqbMB17XKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
احسان حاج‌صفی: سعید الهویی، هومن افاضلی و رحمان رضایی جزو بهترین‌ها هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107760" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107759">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
کنفدراسیون فوتبال آسیا برای فصل آینده مسابقات تنها ورزشگاه‌هایی را قابل استفاده می‌داند که دارای سقف استاندارد باشند و بدین ترتیب تقریبا هیچکدام از ورزشگاه‌های ایرانی شرایط میزبانی از رقابت‌های آسیایی را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107759" target="_blank">📅 17:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxdopRhKSpNyt5SVK5505vsG4h4V9gexyPWOA_BGSsW-1OiinOBnCfmB-YD_5vHOGvS92RssmAlH5Otv2kxCV7St_FvtxRJn800OjN12RySVkHP4f4AQxTNAEuFbgo_yp19onc1yJXplwXZkkxMeYUDcdGWpSOGLjiawhkSVsoO0Fop5UuwH0gC-R7QcBnQ63btg-yyROLH-rozWQB32vEwnUQYekuSR-LJ_luZJIY2bYOVV5puhfR3Io_OctcChSHp3P6iDOzGAMmzIk2tBvC6pgI8TSrYz7JGE1DreIkgXS_i6uQg7m8n-M-NueirDDrsRXdYV2TY2Du1RcCeCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-mC8QtVw2gRC9xgiV4hmgXs5_HB2xyk5E_AKUSYY7jDdVwgN4vgw5J7S7PdHz-XV_r2C0J0tyjzF0PmUFF3RY_LMvCKZAZewY_CZl-t8QDTlLFbyevew84_9FHpinu1Sv6I9g5Hbu16fBpRAMSuAd87z6gPa7z9GdYjzt7dzU_TdQzccuYak6PEGQAYJ_3-uYIJaRQ0kATvuCrkGOHHapRdbYhWLx1agttjfcgYig9GnV5_0o_LMXJ0XU77yQjhWbdPpRYSXpgXp59vVAdx-DdkK9tqjS9iKgmRe3shMsXNcJ1M0ZnovZEJn8Z8Qu1e_-EG65AVQBzQhpRbVaPckjdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107756" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107755">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUxqxVTh9N65Pu5ENq3nEbyOAOEfIaMaFku84JJ5Hhb3v2XIXWScHwigRkVT5HiAsQk8bfWm8HHTdkaQ3SgTggLLY8-kDNap7xH0BI_g3h6LKPYlYvwN-GkgmbGfFAsOg_ETRlkol7F4UrN0tSzo7MiW999zNlqEQGG_iLwqWabZ40c93L58iKo2D7oLYxNO0jCUDhQTDwL28WXImNbCbVQen6K7TF8q_ANXXmO4tMvbOtrA8x7q8vUCmxi9bFVHsOvsONUEZYhLiwAMCvKUjKNVYW1nEWV8cSlXA3Zl7bOLqKOTZpbGWcVBtNsAIqvvEX1V1uDHN0nVI3xxxwOiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107755" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=jGxO8HW_Aw_YqMQ1OvjzPQ5YcY2wua0Vr8nATI-sED2DiRonGZ3nicTztTq2qfa2lpLzQenc3w5cX9TmzJEIyqEzGwfSny2IiN344zXbUrOvAm1fsTnVDEz2haWEgkXvBsdvYOzi40e-g3xoeUY9JnS8TGXYH5WaMFUY78s9ZacMyN3dNpo7otwfneAvTNrq8L-kyZcTYRxdXY5-1J4TRYAWXoMma-qeov_sQ3K1Jffa-rZBjd8YOoURYl-Mv9oIgAojsMTENNKeRH5NgluUWjK579o6jOPr1U--MtLXInXVCsiRmEu4a1P09Eon7XEov6JGGkUut-O9z8sktr_nIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=A8a7_Z-c11gu1NoNk49UkO8xbt8AlRXM3KQfcJmkENalqg5zVStqq6EtLd7XHp-kqNxyYvxrJtoSn2qPl8UOTugmY7YLq4RbPwHGfNPbBh_ydgKqyy8UOP8qByICEYtpQJ9KfGe2iZg2V1UWCvPnsYXW8x1C414U5NQW-KRab1pb9fPyAy8Xcb4A4WAtazXNcllIkQA1TsBikpZk21EHvAb5FqztivuXISUqoT6d7JhjJU7tDXsYGVMV9oMzJboOpKYtLlGZBlnTr46zd_wVYIcWmoKwPMxehs9c9w-PNKj3Kg9SR2bCoS73zoK8cKFL6yZBd69ucIfKmOIF-DL8Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=e5nDSRW9PjIXJSF7POIo9mORgBDJWJQBFUO22o6-z69TwHb9ekQFQUMJm6dBpkVkBSiv030HeLOl7cM24_h6D6Fl_YI2q0Y01anIhKex9cNYDtSNDH2aoWwJbl_gDbtYDqu7xLIJEPQFm5llVs9jJ0Oh2YDwpOG_dR3sfBKZUQupmwUAyJQzMsfgFBFOH5B1nUVAd9js3oBS0-WlmwV9dVmiQ7HrrPaA-9YApyv6OGKmpH9JLxxcZB89ExGKK449hcpfOtP9aKEd0evU8fMm_B5L_qL330EIFoJ1HIMv-DFQvcqKZHFopmjshuf8Hv8_iZPCLFO8vyl5_hmz0b62zx3W0fpusrpp-B1piQVNFxLUajXokuV0dt7Rnf0ubODnXNI3uonH4-BuDp_p0OeBEV8EplUtFy2fJUrW6VRjfJO3vbqzk-EN3vry-UDq-q-bB5IM_06b3PLy3lbA6xJN1yR-vtkIrsk92qiSNCQIHGZugh_SgwQ8vblOQsw_eX6lQlDc9ccG1G7W7dpup3rQ3TVQ4BzkbMgXWnQrPAtolQYKEDJ_zyyUR0CCtZipDNNLdElZnLk2T5c9z130fXa71mQtbG9C9HO6AM63pRG1IxfhBbeBr6qc_96Sg0VxdjoEKLyY2TQ3oslihh0MgHnZYBWOCwu67-PaHkYGgiYL3TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=ALhoXvt3fGD_5MIrVfF71E8NZ73wZXvBrMYAUjU75WSJwb48GCqd1LwHntC-vdMxhtSsll051ysUadAYykDM6guOMksjwwDz5H4CheZJBD-rj44HcJVefDHDWqVbjReTlaom7LD_7jkoko5FWP0LEmIu6DXbRl6tdl1m59kBBNG1X8vHcgu3mT4deErGprLlwEn5Xc_6DrOVl5txg2hvE05Oqxv9E1D-9tdO4a_mXAH2Dn1nUeXLlsoKpXVywxnVubXkiMsl7BPyz-igFETHeXXQai5a4rF_HyfpvC8Cft7jrRysZ1ek37LsSiUPnw6BnDCrMvyM0n8VDfxqqXuKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107750">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhy9EdnXRPc30bmjUsTtWZru-EjOOS9xEHmlyN5UHuA_uupXHeeCZ1rUnZEl5-CPgmvTyeGruy3zw1fckzZmZW4QRclOUlyu6NYJgU8qm0a-5WgI5_JOsWHO3f9vWg9bvDFq4dXK41ER3F0oROaKI5xiQRJ2fd45P0sfzUmUmhPzrNz0z2tVt-6A26TeDDuUS6X8CjiKwn1HqGzfcvms2FxJh_vkObEIhPK1Shbl0_wbTklFmhJDIFt5NqH6xRf4ZJKf97ZfkYB1VxqcHcOJp_YEO7Gd4gEZ53Teo133Fq8oYeaOMmMnz96II0Hlhs6p--OTDtTDboq8QsLDsPl_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇺
میسا رودریگز "تحت تاثیر" قانون "پنالتی به سبک مارک پوبیل" قرار گرفت که اکنون توسط یوفا اعمال می‌شود.
❌
در بازی پاریس و آرسنال در لیگ قهرمانان زنان، یک حرکت مشابه حرکتی که مدافع اتلتیکو و دروازه‌بان موسو در برابر بارسلونا انجام دادند، به عنوان یک خطا (پنالتی) اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107750" target="_blank">📅 15:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107749">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇪🇸
رومانو: بارسلونا پس از فیفادی قرارداد سه بازیکن یعنی رافینیا، برنال و ژاوی اسپارت را تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107749" target="_blank">📅 15:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86371ca1ee.mp4?token=n_slhyvr_8X-4mH85LnbcxDVZz-9nW9anS-9cf9ZauP3C_hJKsNubCGucXpqHVBHJa2cl5agX6FinPUP7YAcRHDU-q-Xe8cNNCYeolErPSX4FWBJZvzANgNLUGmaGOM8b7nhjALDH0aTPvdXFS1q7RnN3nwlBRLO2Yuj9arnPTDJT_IjROTBFbuGY7dSFMTsZOoOGa7-rhuSwhQxuKxzp16Au8k4NoO_3BgzfTby9nfAikRSvYd9-j_P2qkLmf5BNkw1pMUqyLS0TejzD_dIrK6x73rCTpjHXU6YOADyLv8zPmWI0fGuspJJ89-bbWxzy0TkevljKhLt66kWqGsCxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدوی‌کیا: دوره پرولایسنس در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107748" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e10be0d86.mp4?token=KdxyZRvbHH1Pr9MAw2ZNOWR0X_jxsXUVJcnxqB6I8YTMuw8f5EPpzmfmO2bt17VENpVQHyam6xTdaPDL1XaEHoLYZU8WpkGQWJUGvSTHT1t33KidPZD340rMOlN7-a7LlJLdrPH9iMckD3wiFMOXfuPGQpD86BiEpzhUZQOAjdSAtqJ2QwLr6fpmk0FZlBIxG1sKxb0Z2zIQZkKpmSoaT1-pJklq8Zol-HsJivwPJO67ctsUzbIysLwTtAnPfG0_EDGMttZ0Odh7fHb_gpHL7sXtMByLbwV4p0M_OFu-MNhK15Tf9rqv3q__oRn-SdvkoFvl2yC3QpAVUTW4CrlUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😳
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران! این خانم‌ها برای تخلیه احساسات خود در کلاس‌ها پول پرداخت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107747" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b89af76.mp4?token=AJH3ByaB5mn5Z-aLqqLREFN52o-_Lrd94FCNVwB0tp3YxkMkGO7syxzMY0Qj6JjjunvVB_R9UccYcjhpValvwxR_UrqRsX3uJq5DVQ-4Fu3qIHWZhnTT0Xq4EANN00Wke1K5ZVjpbYb8UpVPbTkSfpbnoVeqVi_taO8QWUWhpJ_Q3AxFZ3FsFtkO_MKYyiaTH5E5IWz_EexMhwVmROi6WRD_gjSxCNjAua3fHhPerAnDKSyThAJtTgigH-BrOLJosUkIAd1sRSEETEUNI0iuC5PT6Oa5JipXswEV-4hAb_lxnNHkBaZ1BRDl_KorWLvj8De0IEuGDiTxZ_68jP-oQLZSryAWF5FPJVo9BsYoxAy_-5wDEaLikEJywRyJB-ciVCCkM35lDwzjpLZjkLdzhVlAnveyZBelc_Y5U2qedIDZ9e1GYEheeGiBzZrib9gfImdJ9eOVI00LrvGkhBca2b_PQhzV9nqrovwlTBhkWypwlQjT2ZFGzjkGftjDRs2Cu8NAsynpLJkhYd01modT0K77uVq4IOzBTRRMng-Wpyvfct-1ImUglxPDsp-WuwM_5Pw-RbjhAr2FYpQHErSBQfFC8RXAOFu1OYqNdgNqBPjP36lupn5D291zxEksljnX_55jRTFIhC8a2zZMMf1-OT0MCsEEHKvwk5XN8T8e9ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
یکسال پیش در چنین روزی برتری پرتغال به رهبری رونالدو مقابل اسپانیا در فینال لیگ‌ملت‌های اروپا و قهرمانی در این مسابقات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107746" target="_blank">📅 14:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9decbe8c9.mp4?token=quFPAjmM8fI3S56DEj3NruPLnnrJ7B-POa4WE3YeqjseQKCJoLK7zODJgn6qWMc9M273K0dnam6hIACd_6e9_pQsjET5pYWzpetMGUHiEnPWk-yc7b7B2fXJF9FifGv96t_ci23m9qy5WFH1XlGjHkJCtojpflEbNy-VLmU6axI5YHnB5gyt4oKwFJHNXbVtif6CZ68N5FDGcLxIOF1lGluf-ncJu1WSmxo1dOraWIfjG88gw11HJc9KNOgzn5eFb-y-3f-Ae9msPUrItn60OHOquVXO-ySe2UugBiRxhDKOwmgqDfxDyqhdRCVrofkHBPekmitRaaqYMtmM-wTIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
یک شرکت فرآورده‌های گوشتی به این شکل کاملا منطقی تبلیغ سوسیس‌هاشو کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107745" target="_blank">📅 13:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197e3a2a3.mp4?token=rP-Y3J9rz7LqNcHjb4k_tItCfk_7ymL4RxL_ghvMQ0rkLXXJRRnrYbZVBjPXHEY9Tgje1L_hdUFTogdbJelAZzxR39r8r1tr9iI1Kv-drRZAhDg731nGb9JYl5FYBrJGoeLDCvRgHbJE9oEISiKDMUxhqU_4Jhk9O_9PLOQ0-R-dE1IfBAU95N6Lxrs2jKtoGDCvLU6mimE5v8Z109e_LvZ8RXdpnK_kr08T9IgJzExOxc6cFB_Z010YgBoqmTwd6541_WRM9g4xyCvfNUqUno68a_psUrvgc-vssQ9Azk_by30Wd9ZMDjw4nVjlujd6EFCHOmCeElrr1ZgOWW6XwKnrrYBNU-oecVOph83VZng1XfUE1BBYoGdu-zSHHV9RV-Qrd719O1sH2WAVKH1eRWBVUhBWQfrEcahht1__elhstBUOQ9af9pmRxaxWGnIupVr4Fp0cYkE88GF7EiPeB2gUFnwuLuRBkJvW_5EkpVg00sKB9BgeTfRoU_Yiw7RrLE16L6l3r0qFb967zOeRjDmw3Y-X1IEEmorpuTXXfn6p3C3rZgpG8NG4E8X-n6gLU6n1x_dWQ4pmZKC9l6RmpXDvIkcsqJL2bN04SLo_eeNWX1i2gM5_PRwwGwcFdRH8E_DYt-ryycI-GjZNLsU_akz6mDWUXfJQe3JE-fgGnAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🥇
کامبک جانانه یونس امامی در مقابل کشتی گیر ژاپنی و کسب مدال طلا بازی های آسیایی ناگویا با گزارش ابوذر کرمی نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107744" target="_blank">📅 13:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnpqjvDqCg6qCRet0Oxw78HIKw9QzmWSsElcEBbBX7Hx8EXufmnjxu-ORASRVAaZOlvjjCORLYCI63iOWnQ8km2_FJU18Q8lYUwk-RNZaq6dJdpnLZe16XCuILPYrS9sA3OZ0XKqWz-7eej0dghHx1RfsX6FYwCGHAE6SUoiqYvYvppeCFnMg9zMiICwD4SWfWG-gitcYlaGmW2cpBTsP8UTAZX3DOZaMMkpBW3Us6jciZ6-i3vfY79jYOxT3iTsCNH59RJhFF0Mba31ALGsXjvSlKT2mIF4R3xoLfEpx4MiCGulci5A9LaZo662TStNGz2eFdSvnicImyPIL5PUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
رافینیا در این‌فصل از مسابقات فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107743" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096e7cab86.mp4?token=f4z1qpXfllLXGM2mrIbL89Pc7UHwbPJoi4VxOgoJbMYjQ5n5ws0pxpZhoV44aF3vHr33l18pfPT_hrOkpuhmkrKE0Vl5eKWQIecrJaT8jU5cmqpVMMv4YrHU5juknYRyesizZhV6ckLxTC9bdZjPwb1oFddzdT2-7jTF80EOq12vGF9eUX0GjlrFuK_ufEhbsvZVopbtThzxHB4LMHddnDmXZBExahcUJ2Di7Lzhq5a5_i-mhlgZL1KYXWtx3L8SGY-yQudK-HbC5ScuDsVOBpTGgwKpymdq3jiTTXfQcZXDsmmRL2n6-jLiOMpql7SsHMxsOm3b2obx_NmRh0Hlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
میکروفون باز، کار دست گزارشگر داد؛ جمله جنجالی هادی عامل علیه حسن یزدانی!
🔻
در حالی که پیروزی امیرعلی آذرپیرا مقابل آرش یوشیدا یکی از مهم‌ترین اتفاقات صبح کشتی ایران در بازی‌های آسیایی ناگویا بود، صحبت‌های پشت صحنه و خارج از گزارش روی آنتن زنده، یک حاشیه بزرگ برای کشتی ایران ساخت.
🔹
❌
👀
هادی عامل: صبر کنید ببینید اگه (یوشیدا) تو مسابقات جهانی به حسن (یزدانی) بخوره، ببینید با حسن چیکار می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107742" target="_blank">📅 13:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107741">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35b732453.mp4?token=rdSplSXen1FHjiH_m_hEB3faK_W71fMk4nxqfc5FO56Ao_oLIK8G-B6c02RbrlpEUyvaVJiOC2un7XMz602htAhyeHATfMHRig8j2WDVvI5BEWysvnPXexpW2i-ScAMFWPjXva11FSXoGmwBoxKa3ndcAFg9Rqbn_fsUUbl9o9jQ4zY2IQ1JhKFSYmCkiqDruenYt0nTzetiI8JGqv1SkUIBybJfX_EvOc37zDLdAn2cO2O09RS6y0vTKhhh8gdNBNqEgoxT3CXosqqOL-MbnF-WioNih6jB_bQ9N0rXMIRoe3Nri8i98AFWwNEmRfMCrc0yIaoGa_FtSSHWCeZFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گزارش‌های مستهجن و عجیب گزارشگر تکواندو صداوسیما در بازی‌های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107741" target="_blank">📅 13:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107740">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isQPH-Id727fmrJcJyBQSxwg8ckipGb1uxk7QfLPaMd8ka8pBWfJ68OExDfFKUtZK7uv4Dxd3jlI_2aHG41Lah6cKsvYsfdcTiFwJagOWEAUoe66qDAkBerDex6Xvy1vsSf8VtveTUyaGs-7zAQajUBEG1EsIjD22bJMvEr9jsKb-wVqDSk1o2ClF5Bid2UqHApqEkINPtjEylc9uDQ1rFyAxAJcqwkVQOHPi_wa67m7IyZ7x_o4aZuZV7cMS62v49rnifZZTIB-vlxAw4kgS-lxu8MeWXIyZf2EXg8eXTT-Md6gJe4aezm7fXU7dupZHL6YTzsbLEcAxb-NdxG37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
برترین گلزنان تاریخ‌بازی‌های ملی؛ حضور اسطوره علی‌دایی از ایران در رده سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107740" target="_blank">📅 12:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107739">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888405197c.mp4?token=GfQnryFQ76cXq4EGywq7-kdMMWuLSOrZJ-Iy7x_RGk2whjX1e3T6bWt7Cr5ocNurFBCgjj7DLTm5mjKn6G5scv1aQP8ezkFB56gp1acUbyyE_REPLrl_XM2XDABe8j3J5xLxmqDxb79XhKcOX2GLsO71SsJBsVFMMGJH6wnxbqEshP6RIOKYs8chLIfiuw_yCo3BRHTcs81C9f8Bii0i6vfb6O8nxRwRQZeqwTG6BI8L8ifMvdP9p1hITWZU_OohgX3oimuC1uHgeN5eCANA5MlltOoG6lHNk7u4gJxs9zFZjba9ff15FqBsASHW74VIIX1qimKTlTCb6AVR5XBPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ناراحتی‌ و گریه ناهید‌کیانی بعد حذف شدن از مسابقات آسیایی تکواندو ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107739" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56498866f7.mp4?token=BkqWI7ZKrTw6AQSgamgBHvczdFeqW3ZlxDzjmj1R4AQYBySYk2cWnEr2-EfXFPqQgWf_970IkXG-rjyMzbqVmgPlb_1-qYaAnPqi7q9MhyGJEY_mj3M4Ji4Ia_E6kGyk_F9DvEx3O7HKj4J-ugsYrTpf0B2106sje4f3TZqaA8sCfDSjru8btFdUyTY-R9PwzAlr4DzkLN82ISFoJM1uGiFGuTOafm1RqSM56noHqUE5ThMDM143cqvKAzqzt-9mGWpJ6Iw0g3K6vMD-kQgvv9jsRpvafqEoHUYPQ4-lILbmgBi7Y4pP8hRdRP6W1nXfJAUShaBkrphJ0euRLLWJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56498866f7.mp4?token=BkqWI7ZKrTw6AQSgamgBHvczdFeqW3ZlxDzjmj1R4AQYBySYk2cWnEr2-EfXFPqQgWf_970IkXG-rjyMzbqVmgPlb_1-qYaAnPqi7q9MhyGJEY_mj3M4Ji4Ia_E6kGyk_F9DvEx3O7HKj4J-ugsYrTpf0B2106sje4f3TZqaA8sCfDSjru8btFdUyTY-R9PwzAlr4DzkLN82ISFoJM1uGiFGuTOafm1RqSM56noHqUE5ThMDM143cqvKAzqzt-9mGWpJ6Iw0g3K6vMD-kQgvv9jsRpvafqEoHUYPQ4-lILbmgBi7Y4pP8hRdRP6W1nXfJAUShaBkrphJ0euRLLWJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
👀
گزارشگر تکواندو رو مشاهده میکنید این چنین در اوج در حال گزارش است
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107738" target="_blank">📅 12:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1I-D5yIZ0VYU3RZg8whvpipAkemamzrUCeSU04viw9iiywIkMXfDLPk8KQ7lw6NEoMwrhj5QolzJTVBbIEBfs_PspdDZV-jXlXUWZHYIKLapnuC8QQAKtUj9Yqu7YhQLk-1rv9TkKJpLH79yIQRGe17n5rE6nKeEyzca9UShiRoqCKbwM8huPoi85F92qepIGQv02sGEThwKYWu-WkUyZ3hcfybnuUqJF-kSaFAzqVStFgtyYB4TGrtP4kpwaG6NP1O2vkbRymGs0lI9LoF2TKkRaWkOgIpD2QGpS9sFccz2Ax4uHWl9wxAK-QWqxuzS0MIbHiDr0OhMlbijeLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسابقات لیگ‌ملت‌های آسیا به شکل اروپا قرار است از شهریور ۱۴۰۶ آغاز شود. ایران در سطح یک این مسابقات قرار خواهد گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107737" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc8cRPXD8vsV3f9-IrstFqcWlEWMiTCMUSpZuw-ToL7NfbTLx1lPHS3rNegw0AN2fPTwqWwjbZTsPrHmCpL_7tiFFrtcm9AtNSAp80D8CncJan5yjVTzGEbUD-ERQXfH3Bve26XDUqRJcqewk9VFbAR5Ll4iXOedy5st4F5m3RcI3oTcakW3fMY3-OiZpDkcuY5OjvNpCJrH0mjVbaAW-BVf8AWA2Sy0YTqh1wjD86EWoVGJWPLv4hPEs-dLowSKxMR8ZxjG-TfdG5MI8RUi4Yx0qZThpjKSh1JqaOViJiVzFj1bh12hJzDkBoEvYjraTBXs0ysI2v-Fv2EC3FiV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسامی نفرات برتر آزمون کنکور ۱۴۰۵؛ نتایج اولیه برای تمامی داوطلبان تا ساعاتی دیگه اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107736" target="_blank">📅 11:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=flybz9ItoMS6sEBPiVVe5YMVMHyFkXWH5AneycrGOHlTm-4i9HF94tay19CgSEYpaKcWPPUUnd36Rqm6-m94nJYRWl1_-_AHe1mb0ejvpWcmRUA8NJxTvK8ux_dGBkQNFXDfmSXHbxvJQ9VRQy-gyL0VhXWIFZsvagK0aFBWXynRvYhnmrw0GFTdE32pD-ZKAVPGtqcoZVb26nJ0bAP7aMcvxhfcpmQHPmFGolrneVZr3eIZddNYR7cDhfY2zjHbU0SaDwOAAqoDaEp4F1XcBgf3-Ke0JRiKjmwTSorh4AcXBIFjVVuMJDlPUIJ5u63REoJ_YU2tbNzISCY4Moflag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
شبکه سه اومد بازی جودوکار خانم ایران تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول درجا بازیو باخت و حذف شد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107735" target="_blank">📅 11:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107734" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6FLNldS-KgCaXRWgOxluArANTbFmBadjYmxRHU5ioCQkzjfvK8n2QmMWcvl0rKUHOElazl8bZJdx6pHkbhkA1PLchF7Oev6IIxNPNuWnr8LCBSwz5LSrgzHWF5jJGU6yLzWXB1HiJgnmEbaFpwd0cAbsyjx5BlNU7ELcvGVsHZnsEywKTV_TcWn48m4IfsAxEQeCZe0YTRe2rC50mWLkpgoUtKq7P4-oLyayyKPzFKQmCtSk5Uwfo42ikb8whFsr5wjPiPtxZRofKUPePmyeNjiWtE9NuI90DJ-XRIeBcBxjVqDK4PeyZW00RabjkKZKvfla6FezLlyVzKNHF8yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107733" target="_blank">📅 11:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d8475315.mp4?token=MSdH5QxzSQhmqIijbCimTdhrNbHEkZGpfBCyFiRrdI8gzHHs5Y8e17OA7fOo4VfePf-Et8tgCRT6aKlfCgHXuLnTZwOWmxdMxmVd4EZ0XLVoMbHFd_M-CWOgOvA6Lw-DDter9dJfAzSW_jkUjRXNU11ANMyTk3eCQYCOLlFG8R06ZdUEx0j6ltdRuwOHe9RZP2n1Tb_k0QjX_XlTu7IGc7ZpZ2lU-LM_E09vZlYW6hD1YBQDQCy760bwTOdxdK2HrI81GmAHz1ZtqT2DX_kNYo6nvYN6L9v1A2uVDmFihfQJ2rQMYm5bCpirqfAAaKSpDiq2RepzrlRPwhgSW0I6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d8475315.mp4?token=MSdH5QxzSQhmqIijbCimTdhrNbHEkZGpfBCyFiRrdI8gzHHs5Y8e17OA7fOo4VfePf-Et8tgCRT6aKlfCgHXuLnTZwOWmxdMxmVd4EZ0XLVoMbHFd_M-CWOgOvA6Lw-DDter9dJfAzSW_jkUjRXNU11ANMyTk3eCQYCOLlFG8R06ZdUEx0j6ltdRuwOHe9RZP2n1Tb_k0QjX_XlTu7IGc7ZpZ2lU-LM_E09vZlYW6hD1YBQDQCy760bwTOdxdK2HrI81GmAHz1ZtqT2DX_kNYo6nvYN6L9v1A2uVDmFihfQJ2rQMYm5bCpirqfAAaKSpDiq2RepzrlRPwhgSW0I6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
دو قاب از بيژن‌مرتضوی به فاصله ۴ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107732" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbb258d04.mp4?token=oB3Bv6Wnx8FOQ5x1wAj9GNxcbVY8duNjG-ZqGULbAmF4PmkKzzs9M0mxEE6sJ-8qEU4rbx0WTfsSqxJAO81EVUOsJzk_MXKLfJpU8H0BctUwlzb-AjZR_CtjrhHJRJJRF53Qu2AXKbDyZIlUNdGdreGd7hZlxrlP85hP7McMPLz97WpODZ-kWjxuIM6wOFGyFK8ATZWjWpwi4GES-49WtYKtGqcDBk96dvBmqfOaLPzk1b1IZfcl6Ou8qIWyeyNRMTDNkN1qbMRtKnxZQYqNadrbYWw62ctJGkaftcZJB7BzK0KcK-06DaC6mm_1xDD2GV_VGYEFRXv8N8hvg8Xn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
نه به تیم‌ملی چیز جدید اضافه کردن و نه تونستن جام خاصی به ارمغان بیارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107731" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8086af61bd.mp4?token=foUEFXCssXbEJ0msFbbNHl6di65p11sKGUGU-bcY2KmpuMq9zAWHOi0nQ1lwC8i4ZtKs6gv17Cz6LyItHIkLsC2pRj5_toW7SN1uttkg2J0UCaXq1bRvHmV06XJEwWeUDhjPkxo4IjT_o738OT6xzD1j_L-r_1iwAMcQFXd2IMCcuSdCfBRYGd7HNIqAc9Y1Y88L-iLCh-PAzFDmADa2c-10BkYcxFkf4uGy1X5yttNrv2jyIvr95TJ3wOxOzc723sC03ZdUbVqBHFTZ8QQ5tPrpqXwT8ZpcLtERxMM_mDHLS-GvirxdPdrZgbub8NWza26Xlyn_BnKraD9TH3ii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
تلخ‌ترین صحبت‌های مالک موبو نیوز در گفتگو با امیرحسین قیاسی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107730" target="_blank">📅 10:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdae91c6ba.mp4?token=oekTctRr4nbHlsQxdeitvMqQdCNaZUrHImR-dwDerAGkCouyaRSufAfhbDQdheNK55vW6mcIxkSnET8jdU8pHb6nvTwW4v4yaH-GhtQQkS0ektW0xG1izpi2eu1aioy6IfVtb_kBHjtGZ05gExlPd7QGAnUrdbVOl_21QILBYmMB1lSlBvfefS7aFQwh18HwkUIhcMNQUHdHACsdVOD8DhWFOitoY_cnD5fV7HRsQ0ad0XoE7YN9pE8SmwKpchrrlr2_R0TewyTqLksVSkMgaecpftjZ_PlgHgdRNZks_mg1ApE2pTkybEfyX_hgNF94wZzVlNbWsgeqqVEO2YytIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
یه راه خوب برای کنترل هزینه‌های اینترنت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107729" target="_blank">📅 10:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c37b6c6ac.mp4?token=MWjERDyw-tg7WEaQ8ylhRboQKa5FCxxTzIAYtRIlFqh4qY0LxOtOmXNaNix7IuIRMJxCPsjZTmVZjiUbZTxGQ1lDe8TbCFfjLiGKG7FV3th2_LvXN2aXUiqCTcugqgTWP7hHzS7Aa48TEBPlcwuctozmOhvOJ7F7lHxCikCkdXqWlw6ujwDORDA9qbZOOg09wqILrR0fOZJ5UIzPnQGM14XX-qiH1ILi0WjJIfCTmnyr2YqGktkYwaPBM-K8LpFwOEnc_mYhMCFYHLpR8Hp9G_dEny5HvPr8xOHK1wpRmGZFjLdTkBDQDNSX66GzdmseghlPsHRkNgqmTQeRg_qfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بیخیالی بازیکن های پرتغال از رفتن رونالدو دقیقا یاد این سکانس تاریخی میندازه !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107728" target="_blank">📅 09:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYO-XKbO5e1sInzAhcdJnIomB17yPqzwCj_5IH0NSmUamUIx9yx4otO8bQnJRHygtRZkcbwV8btrwITEQKxvqEWVkMZcqTshFUgR0YxJgRqGsoIRhHvTfSWrZZXPRYprKQNngqVh7JavDEnOSK-mPRs7R4tlLW_T_GYC3peRb19uYXtt1BINKVDFdBbd3umCLjM9k_7JQsAxPpapFlIr_a-gM3t4DcHi36DPkoKanjl8UCXczTojlHN4H-OKAjhMvYkziheggIrCd9GEPPZxiupHWH9OagtYyvqLbSaDTdAYdTFT7mQtu_UxGhiff-lBhKhb7UhY4FIlZ7FYXEFjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
با اعلام‌رومانو: ریاض‌محرز با عقد قراردادی به الشمال قطر، رقیب استقلال و تراکتور در لیگ‌نخبگان آسیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107727" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c7684c2.mp4?token=X_OKzcp4JD9HRtRDSfxlmDRgsBPub-reCxStULcNXLTOE5BqBeJT8oFzTWb6PzAw8KKc_caLR9n9fRVfLdqPYjw5tv-mbq-1-x3zkRANnABLSVM-MPU7-NKGaDbbTzhVBC4BtrJQ2ukl8bQe-R-ynMf1JWHfYqngVNs5YJENmqgcu2RyGuwQT1ZbS4HQrcGcUJLSWFpRULcDt8D742BrWGfjovsYuNr9VcoXD8GddYhvDVVNdEY-7PF8qb0OJDdnrTG0KceHHCxo740kAYHjLwBcCTZjZeau0sWIpS5Y0V5PnNs3A266XRWZbfxJlpkRalKPf_CAyrihXzyvo-jPjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
سقوط تیم‌ملی به روایت اصغر مازیار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107726" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=XyPoY8Y7j-gacsKBZlnHdGFggMjHTxMftZ7RwuEf0ZQtg1IP2yIfx9IHnNcWtik_AnSw4_q0KzQ-9F9DD0XoMkG_DagndQRgk1dIBW_d9pT8_I0x6eusg2BucakihVo2HXatFCkqrvRYjaq_IPZ663D85PaZkdtomLUbMOoZIHUIKBxcbEZpognOE0qhoeik2A1Hg7-i_PNlub4ZY7U6iuV-9Zcy4VYLjazROeWOnTtm6NslXK3kPSNjfAVDZveu9rFczYIrpXV9Nuie-Pg0FY6yqb3h9QepZcJNe4pwjaAabP_7A4xCv0qb7qzPHXSpFTnDQbFzmHBfYMqhopos1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d02e44cc.mp4?token=XyPoY8Y7j-gacsKBZlnHdGFggMjHTxMftZ7RwuEf0ZQtg1IP2yIfx9IHnNcWtik_AnSw4_q0KzQ-9F9DD0XoMkG_DagndQRgk1dIBW_d9pT8_I0x6eusg2BucakihVo2HXatFCkqrvRYjaq_IPZ663D85PaZkdtomLUbMOoZIHUIKBxcbEZpognOE0qhoeik2A1Hg7-i_PNlub4ZY7U6iuV-9Zcy4VYLjazROeWOnTtm6NslXK3kPSNjfAVDZveu9rFczYIrpXV9Nuie-Pg0FY6yqb3h9QepZcJNe4pwjaAabP_7A4xCv0qb7qzPHXSpFTnDQbFzmHBfYMqhopos1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای این چه سمی بوددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107725" target="_blank">📅 08:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107721" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGelMiLKyW_3vvrZsaOSCusuK9NymL0e_5z1tiIxHhHVvp3onKYPIzLtu-p0NEQEjl7WnyB4NlAVcmiT1DAmsSuv2I-HAT2a8fiYnZm773HTRvhQFh6_OtMzF87mJyyB5Bi0pqSVQKUskjE-VA86KnuJBltCFL6ygIJGhA96SoEiG_2vIOjE7tIhcpv5YdOiS-MwnmZeRl6XP81gxTgK2CrPdMEIZ9dm9BvbZ7TbRlfU9zo0zRVmnPAiRop5x-thQwCu-3q_gdTR2zMHSN0oiUWBGvglS0REY_eax7lsqExOPCppMv8_tROAe-cLWVPKyV9RKWR3imY7LiaKNEKwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بنر هواداران عربستانی برای بازی مقابل قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107720" target="_blank">📅 00:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇹
🇫🇷
هایلایت بازی فرانسه یک - یک ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107719" target="_blank">📅 00:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107718" target="_blank">📅 00:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=Q8qCo6KhrLil6d9txcAbTs-0slFR-MediAx3KUwnjfKFppP-fjhECdgbs4IqljiuTdg7VIbsRU50r_wRw7wtbHc-FX_SiUZWhyY1UcVOR1t38JexbqQ2imFij7fKv0K_TFCbkHWP-mxbU_dooGhl82HG5wNLAt2wjTUzFje0fa2ReA3ucxTVPSbRJss_hHVVKXYRZCgZWgYikISADUBj8dTraidApBEC-WqZJLHyYJnlzBWeIC1Ib0N1GJdEF5zTEI1jvnLcDoF9CsxQQwx1iZNn2jRbisRXRbMoBLYBKKRPf554u7CYYpFNu-F1uS2ZiWzanW0zv1R2h5MbZxQFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b540d3428e.mp4?token=Q8qCo6KhrLil6d9txcAbTs-0slFR-MediAx3KUwnjfKFppP-fjhECdgbs4IqljiuTdg7VIbsRU50r_wRw7wtbHc-FX_SiUZWhyY1UcVOR1t38JexbqQ2imFij7fKv0K_TFCbkHWP-mxbU_dooGhl82HG5wNLAt2wjTUzFje0fa2ReA3ucxTVPSbRJss_hHVVKXYRZCgZWgYikISADUBj8dTraidApBEC-WqZJLHyYJnlzBWeIC1Ib0N1GJdEF5zTEI1jvnLcDoF9CsxQQwx1iZNn2jRbisRXRbMoBLYBKKRPf554u7CYYpFNu-F1uS2ZiWzanW0zv1R2h5MbZxQFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇧🇪
گل‌سوم بلژیک به ترکیه توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107717" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=DKxnIB4f_-meptBiYosG6GGnsdr_56Sm93aajvSO-QbnwhtSB7XklQI9uYM1KnD8J5A4LZWnC7Z6NIY84_GV-tUzkCwObOY5DjwJfwFxKtixzXyVzaM3SAcb0bM1JlCtWORniHQKZZczc4zDPj-jf__xhpnxddsK9Htg-0l-mFxKqWgWoO1w8vlC7Cn9zCEj6doY2K8A5K8jAEReCK0R45NolfBHjnzOHvu9fnASAHXh3V7XrvO7vt9dRKwVRClbgySmUoHwqeCaA6Qkj7cNt25hMw1us8DUgoypgnbgM5ZRbr2RS3jDAR4GocEWpzZUR19lKuMftg85_aTtjjDZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cfe007c4.mp4?token=DKxnIB4f_-meptBiYosG6GGnsdr_56Sm93aajvSO-QbnwhtSB7XklQI9uYM1KnD8J5A4LZWnC7Z6NIY84_GV-tUzkCwObOY5DjwJfwFxKtixzXyVzaM3SAcb0bM1JlCtWORniHQKZZczc4zDPj-jf__xhpnxddsK9Htg-0l-mFxKqWgWoO1w8vlC7Cn9zCEj6doY2K8A5K8jAEReCK0R45NolfBHjnzOHvu9fnASAHXh3V7XrvO7vt9dRKwVRClbgySmUoHwqeCaA6Qkj7cNt25hMw1us8DUgoypgnbgM5ZRbr2RS3jDAR4GocEWpzZUR19lKuMftg85_aTtjjDZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول ایتالیا به فرانسه توسط باستونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107716" target="_blank">📅 23:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=M1J-RuKW6HGYq6lDvfIHbZQvtsRo7Ujo6sPe4a067O4JuqG68ANJ1GNvJf9Mkp6Tp2Tp5Wi9l7HX_zmdE9ZcGfdjHYHGryn8tHILiQMr7yDFD8bAgE_qsB7fBwLfWHy01jmk9pni1jvhm48cZUs0g_IuoLbfuiGPE8wBzDrIISeLoyBNXsqYKLpzh18K_IO_eBDKo_By7qSwsa8viG2KfehTmbJ8JgrcHaIhOdt2s7Jzbyav-36H1e-idK-gHf14HiQGqcfRgOOsTDYKiiT92EKuxoMNFbXQlb87yCyY_AkFXmJl87W2X1u8ASYPynAndHGsSpSCnRcPhtvxqMG4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f73a4fb35.mp4?token=M1J-RuKW6HGYq6lDvfIHbZQvtsRo7Ujo6sPe4a067O4JuqG68ANJ1GNvJf9Mkp6Tp2Tp5Wi9l7HX_zmdE9ZcGfdjHYHGryn8tHILiQMr7yDFD8bAgE_qsB7fBwLfWHy01jmk9pni1jvhm48cZUs0g_IuoLbfuiGPE8wBzDrIISeLoyBNXsqYKLpzh18K_IO_eBDKo_By7qSwsa8viG2KfehTmbJ8JgrcHaIhOdt2s7Jzbyav-36H1e-idK-gHf14HiQGqcfRgOOsTDYKiiT92EKuxoMNFbXQlb87yCyY_AkFXmJl87W2X1u8ASYPynAndHGsSpSCnRcPhtvxqMG4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
✔️
گل‌تماشایی کوین دیبروینه مقابل ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107715" target="_blank">📅 23:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگلگلگلگ دوم بلژیک به ترکیهههههه دیبروینهههه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107714" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=TEKCAq9GH_AesNxCXdsIASwmmv5DfTfdSNtnuwq99lKBpi95TLgpYrpYQ-tEI-l-8Nm7xG2QvgxSRyggw23Ev_h4VjGHdRzN--XzF3K830N-YSmQKt7fPt9A5hEehIRxt7UWpoqedHCOld8munDfv-vXTffwQ4Kg4CzP3vEEDnXh_cVbsQZzeMt8b8jxCLRcUKyjpfjViYfFzYcU1p6fNQqwJ8fiAWgamy974SQY46xnpZjuPeUOHEl9NFJb0gIlx102USbUdmDHNYTPTzzbBRfBswoolQv_mmzxXPL4By-lGKj7U9cUSVxsSKRch7ex8gRTtOWntIPDTi6b1CiEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3dc430d99.mp4?token=TEKCAq9GH_AesNxCXdsIASwmmv5DfTfdSNtnuwq99lKBpi95TLgpYrpYQ-tEI-l-8Nm7xG2QvgxSRyggw23Ev_h4VjGHdRzN--XzF3K830N-YSmQKt7fPt9A5hEehIRxt7UWpoqedHCOld8munDfv-vXTffwQ4Kg4CzP3vEEDnXh_cVbsQZzeMt8b8jxCLRcUKyjpfjViYfFzYcU1p6fNQqwJ8fiAWgamy974SQY46xnpZjuPeUOHEl9NFJb0gIlx102USbUdmDHNYTPTzzbBRfBswoolQv_mmzxXPL4By-lGKj7U9cUSVxsSKRch7ex8gRTtOWntIPDTi6b1CiEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🤯
سوپرگل دیدنی اولیسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107713" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سوپرگل اولیسهههههههههه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107712" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فرانسهههههه زددددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107711" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107710" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=tGVl9avxmlEyASijhOqIZ2kAW5b8JtEixP97KvlcCdgm3Hk3oNRxJlTrbl25kwxm9-RnQZKqisU9qxpkEBYPHdG2VxmV7q1Zra_v-o972CHml4hIIWDzntUoUc6IBOw-L25AmQcfZ4el4JlZlmqmvyXOJR5Utw6bMuwk1I-uXAsDeURRP-wpK2w-BMm6lK0jYGiBcnEr2aLphRo6qvtgyW_gCzyPuxbFutsTv5UsT3US3vVaVPXYeiV2iWtqTlXopGB1SMGEsC9CcDESzw4mfQpNXl_Kry0ENV4ib_sN9lMUoW32eJatmiJQ-wMVef-ZXaC48NcHl4xZWET9StUEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e970c7c18a.mp4?token=tGVl9avxmlEyASijhOqIZ2kAW5b8JtEixP97KvlcCdgm3Hk3oNRxJlTrbl25kwxm9-RnQZKqisU9qxpkEBYPHdG2VxmV7q1Zra_v-o972CHml4hIIWDzntUoUc6IBOw-L25AmQcfZ4el4JlZlmqmvyXOJR5Utw6bMuwk1I-uXAsDeURRP-wpK2w-BMm6lK0jYGiBcnEr2aLphRo6qvtgyW_gCzyPuxbFutsTv5UsT3US3vVaVPXYeiV2iWtqTlXopGB1SMGEsC9CcDESzw4mfQpNXl_Kry0ENV4ib_sN9lMUoW32eJatmiJQ-wMVef-ZXaC48NcHl4xZWET9StUEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال بی نظیر و خوش آمدگویی هواداران به زین الدین زیدان سرمربی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107709" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=DTFJapExweuMOy9p0lil7dcaDH6Y4d-yebKRdZnJRWZjXX4zbb4TMFec7ZgX11071eSmPlp8YtBOlCVG35oweHgIfD_RwcPM0apGTptXcyoFqT3l6Jh5xJpoX6RsfKE1ep1m5qPNLzWuHixH5KYKOItmlD4CERL05QaIuxILlzsdfg8svasczD0trgBQahGqJP7JZsjso0hzXfxnTpqEJnWIsDjv81feO2wsr7gsNNt7fX3BjMaDxYnVNayy6nCdc2brBzNoN6HKDwBOFaFaphmPJLQymJdq18HAaYosdmHnrq9WJz_KboEc2yiMTqRk-FX_TZpUptERVPqUaJgfUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0312a011f.mp4?token=DTFJapExweuMOy9p0lil7dcaDH6Y4d-yebKRdZnJRWZjXX4zbb4TMFec7ZgX11071eSmPlp8YtBOlCVG35oweHgIfD_RwcPM0apGTptXcyoFqT3l6Jh5xJpoX6RsfKE1ep1m5qPNLzWuHixH5KYKOItmlD4CERL05QaIuxILlzsdfg8svasczD0trgBQahGqJP7JZsjso0hzXfxnTpqEJnWIsDjv81feO2wsr7gsNNt7fX3BjMaDxYnVNayy6nCdc2brBzNoN6HKDwBOFaFaphmPJLQymJdq18HAaYosdmHnrq9WJz_KboEc2yiMTqRk-FX_TZpUptERVPqUaJgfUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول بلژیک به ترکیه توسط کوین دیبروینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107708" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=j6N125AT5DS9AjXq2XAtJWEuM_2VyHOHowmYxKE8iezH7izX_c07VD6Dhpr711sDa21tIAigcwVD9fBn87QBzV_iG_biQqruBGn1YY9UzN_h1oI0ZmPYPWllP_udmzsBtmTZOEl0oJ6sUmyMl_ikDpmYC6AGGH1YPg34An8_5mauOnHrY8Vo7mqzGXar_T-LWK_vXrnqp03rDtJCzwCGkfb4LOKwNXcKa2aTeA4DGmpJQ8P1WHg5meVj9KADei8-cDoku2gGIF4MkNtrDLpYjJkA0YEJQ3XkBgpSc-gz8JpjMlMsFKjb-Q6bDW7WCzb38eZA_N7MmjDLmnbtP0WzcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5c780577.mp4?token=j6N125AT5DS9AjXq2XAtJWEuM_2VyHOHowmYxKE8iezH7izX_c07VD6Dhpr711sDa21tIAigcwVD9fBn87QBzV_iG_biQqruBGn1YY9UzN_h1oI0ZmPYPWllP_udmzsBtmTZOEl0oJ6sUmyMl_ikDpmYC6AGGH1YPg34An8_5mauOnHrY8Vo7mqzGXar_T-LWK_vXrnqp03rDtJCzwCGkfb4LOKwNXcKa2aTeA4DGmpJQ8P1WHg5meVj9KADei8-cDoku2gGIF4MkNtrDLpYjJkA0YEJQ3XkBgpSc-gz8JpjMlMsFKjb-Q6bDW7WCzb38eZA_N7MmjDLmnbtP0WzcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
علوی، سخنگوی فدراسیون فوتبال: استقلال قهرمان فصل گذشته نشده و بحث جدیدی درمورد اهدای جام به این تیم نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107707" target="_blank">📅 22:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3539953949.mp4?token=bGItDJ9afwrDLIjWTasBP60cN4tNXteTVNHUWuCPUArCzme1Nz0tFfEoH8q_6Mgk6Kfgz6_S4oZJZ0JEf25VC5z-Xzm4pwmVM_Sutja9aqtT_pDaY9eEJ_dIpSJOEdRGTtAxEc6XJN4U9a9xSjX8L0OF9yopQP5gxN_o94PmWlQn1JTLs0SrX6t4iK90rWercg6z6K-_HRoDC-nUWP4dTBKYVEX4qDTdCktLfekc94Hc3obTV--ZLxSHh0mTrWMm57FOSASgwqCfc8fbBVn3UAgI-TQt1uWAWAwWeKDn6PZt22NwfYZRmGrvtweVwjkFPEJlo-iKDdGMSHNjUt_p1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3539953949.mp4?token=bGItDJ9afwrDLIjWTasBP60cN4tNXteTVNHUWuCPUArCzme1Nz0tFfEoH8q_6Mgk6Kfgz6_S4oZJZ0JEf25VC5z-Xzm4pwmVM_Sutja9aqtT_pDaY9eEJ_dIpSJOEdRGTtAxEc6XJN4U9a9xSjX8L0OF9yopQP5gxN_o94PmWlQn1JTLs0SrX6t4iK90rWercg6z6K-_HRoDC-nUWP4dTBKYVEX4qDTdCktLfekc94Hc3obTV--ZLxSHh0mTrWMm57FOSASgwqCfc8fbBVn3UAgI-TQt1uWAWAwWeKDn6PZt22NwfYZRmGrvtweVwjkFPEJlo-iKDdGMSHNjUt_p1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حاج صفی: می گویند آقای قلعه نویی با یک نفر(جواد نکونام) مشکل دارد که من را به تیم ملی دعوت کند تا رکورد آن فرد را بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107706" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfpNhIQlyq24hGDBlpFdBAYjSJncCXOPkWATxqeOsRJhxZp6-kn3r0bkpW5bEsoEaiZdC9XWjPjHlOCU6wAkamSjifL11_dbNjjetSCiMuILSYe68Ts7av-AFdo_o2A9NspCaLXCzIRM3665OehLM1OLLJ-W8XUVkgcdDQ1arqEs0J7Dh1DoIdsMA9Fb7rvu2_DrKWjNRfuyOVphTEYKMsDFCd65m2fp6xVuUs-1PfHrtK2cHwRWgJV6xMyI2kNCR4NB5bUSH_xaW04XK3NMLDtwLYOqY_k0YdtOCV5d8sTckDQLTZ2EI7kFCO1yxuN8Vb3GziS6ptBew01ccM4FWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107705" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbdRX-27g5d6yd2XagL9OkVT4AaMWiTpAdewPpkM1gw34HxQllqk5Sy4mb1dPbDPCEztlT-3RrtojEUlkf2_6-sV4pmwegRu56UdnYWadZrdOPfgCpLqV7JOtJ2hnDTkDdTm82d3NHQi_3ow1fDWNZ9l0D44lncuKuCuQy_lOYV4yctG9SpuHjKCH9o8Axv4y8LAix56_YgaWCUWelh8m3echxc3i3PCmB1dm5U3zZPsynYpkp9-0rqeaGVIL_1MUEte8sCsqUhxx7HxrMZHmrhUJBKSsUzwmVe10_CSrmbLh_BF3QqxK1dYkrLLLS2CX89r4aARjF4heyNm84G0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پیش‌بینی‌های زلاتان از برخی نتایج فصل:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر انگلیس؟ منچستر سیتی.
🇪🇸
🇪🇸
لیگ اسپانیا؟ بارسلونا.
🇪🇺
🇪🇸
لیگ قهرمانان اروپا؟ بارسلونا.
🏆
توپ طلایی؟ لامین یامال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107704" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107703">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbE3Kx-htcwdC_btts5GVgsMD1r8NYdDdk9XIFpIwemh46wy7sxrFzzIYbvY_YutNstd10kweTWum0Pvp0W1Egj8_8q_XpF04bExE2B1XRKeWb7qU3DEZzNSFIQea2gHu5pH7LS3Fhxxdz3tZ00fEjQDnQY6iELiq1vqv_yPEROf7fMfAj5KCjNVssbnOxOO87ki7zWO1XB-mkp7N2EZSpXD6iu2kYElpm0CG92Ek2_3QDlW6qZqjyhU2DBXFVnZ7Q5QJyjcOLklppLRkC3hy3R5o2nUp33OEOvf_r8Ev-Uh_zGTeeN84rE-pQKNQC098b6V6091qT2uXtXSpOfepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107703" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbJAMuAlDv1VFVR6p96PgrdHAv93sVEBDUQj7pNR5wsKVWz5YinbhBViqt6yg9Ecqw0NQqzkSwI2sjkSN-KbHw7ETXTkn5MxHrisGb_AsjLN3dUaXcS11ecONdwblpGuY9y4SxiLedTF4QNQMBJ-H6XcD5SRTyB7TqKPQJLx--mhsjK2S0RVhK-XByJRxlvFtdyhbArxEXAtVAQ99uCfaGz_ly4KfxQBp_S3WNS2ec_4e7TMPoukxxcVofgklXzSfw64pUwKKRQdl7mNXmnvA7LPrEdt3dXFAooRuUuJEfv7GtJTsXm7yCCySL-21lcsja3As0fnqqPmBNP0YU_ltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
نشریه The Athletic
در فصل 2017/18، گواردیولا اولین عنوان قهرمانی لیگ را با منچسترسیتی به دست آورد.
منچسترسیتی حدود 100 میلیون پوند قوانین مالی (PSR) را نقض کرده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107702" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af474384fb.mp4?token=pfeDKHr6ORbq56ps7S0DG9XgTEtHm-z34Vs6t6mtzXle8DyPuvU-6y0G-GqEXSNk1OZiTtIyx6mPHitHyQgOI4-9Ijv4pgqj2dfCH0RcmTcuk3PqtahGM2O5Txbm9CO8GhV2Kp-6o9PG7Ly0gFg832XqVi1U1VO6cKRWmoMLQqwFGyjPsM_0wohH6gc8rCBX-23q4Hr0pd6FOpa_W606M7J373XXg1cn8jrqfRKQ1Va1jaVy2mytGU_LWundBjrNnP42aMsYix9X0pR1tSCZp6AduK2_iS5V8v_x7CQZiz4BhqScLMEAXvZLSDSRcyFu2DOpXupXZJT9hPhSvQgJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af474384fb.mp4?token=pfeDKHr6ORbq56ps7S0DG9XgTEtHm-z34Vs6t6mtzXle8DyPuvU-6y0G-GqEXSNk1OZiTtIyx6mPHitHyQgOI4-9Ijv4pgqj2dfCH0RcmTcuk3PqtahGM2O5Txbm9CO8GhV2Kp-6o9PG7Ly0gFg832XqVi1U1VO6cKRWmoMLQqwFGyjPsM_0wohH6gc8rCBX-23q4Hr0pd6FOpa_W606M7J373XXg1cn8jrqfRKQ1Va1jaVy2mytGU_LWundBjrNnP42aMsYix9X0pR1tSCZp6AduK2_iS5V8v_x7CQZiz4BhqScLMEAXvZLSDSRcyFu2DOpXupXZJT9hPhSvQgJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رضا علیپور، نایب‌قهرمان سنگ‌نوردی بازی‌های آسیایی ۲۰۲۶ ناگویا، با انتشار ویدیویی در اینستاگرام، به پخش نشدن مسابقاتش از صدا و سیما اعتراض کرد: «همه مسابقات را صدا و سیما نشان می‌دهد؛ سکو، فینال، چه برده، چه بازنده، اما به ما که می‌رسد،‌ نشان نمی‌دهد. قضاوت با خودتان.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107701" target="_blank">📅 20:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107700">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=LUJNCFHDWhqkzDiPiIz7csAtRANOtwh08sgFsC7qrxt-g2SCjyquVQgu_UXBAhaeqKfJOKvvnItVaxbaWF-k_zbkBjOJwNVrRyMrKGGtyOnpy_WwmxeUNRBQ2Y8YgtNbeZmW1ZT8MGoo14fPIhOlRiBRp-RVXog4lc8U8qgkXck8eoJeab5adyy4cPA6eyfxjFi5Q07UJCVg17tcuRd4fH6kGubDWXcbJzJxRLqTTTdKz6jfsQupncCGLjaZo2PNiIyVUXUjMBqcCDdLa15KjYJD_CSy68mssJFcrJ0dozrzkrIjxQmZQ8zOtRdt1P6WpCG8i1omx_trgTPxqXY21g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5607ff2b.mp4?token=LUJNCFHDWhqkzDiPiIz7csAtRANOtwh08sgFsC7qrxt-g2SCjyquVQgu_UXBAhaeqKfJOKvvnItVaxbaWF-k_zbkBjOJwNVrRyMrKGGtyOnpy_WwmxeUNRBQ2Y8YgtNbeZmW1ZT8MGoo14fPIhOlRiBRp-RVXog4lc8U8qgkXck8eoJeab5adyy4cPA6eyfxjFi5Q07UJCVg17tcuRd4fH6kGubDWXcbJzJxRLqTTTdKz6jfsQupncCGLjaZo2PNiIyVUXUjMBqcCDdLa15KjYJD_CSy68mssJFcrJ0dozrzkrIjxQmZQ8zOtRdt1P6WpCG8i1omx_trgTPxqXY21g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
حاج‌صفی: در کار آقای قلعه‌نویی و کادر فنی تیم ملی اصلا دخالتی نمی کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107700" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107699">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=fWK0qarWIcRrni6shBbBZNw0v-ItOQV47SMvYYOgeRC1cpA_r3nuHXRqq1qJ0xbmtA6p7MhxduDOoQhgsGZGLD0LFXDx9RlR4unKZUUZr51HXdmlZ8P1FB5IrllTD9N3MA7rNbPpDkqS6SRd6v9uY5J0OwFhOd8UvTd07XtMHQ_fQREsqJsoNTyLD2ECNGxPFGkEga1kbBZvGTM6NGKSnFHBiC_d2BDHnh-X-E8nDo1AL-LD8UaP5yuanuNztOzxWA9cjVvH6U9HEQChZVamc-8Gg9el0g9vBStmpptLKa0x_roRtVA--Lm3y9k6HKBHyoEuQc6CQeCm86CQ-3OpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60d798d01.mp4?token=fWK0qarWIcRrni6shBbBZNw0v-ItOQV47SMvYYOgeRC1cpA_r3nuHXRqq1qJ0xbmtA6p7MhxduDOoQhgsGZGLD0LFXDx9RlR4unKZUUZr51HXdmlZ8P1FB5IrllTD9N3MA7rNbPpDkqS6SRd6v9uY5J0OwFhOd8UvTd07XtMHQ_fQREsqJsoNTyLD2ECNGxPFGkEga1kbBZvGTM6NGKSnFHBiC_d2BDHnh-X-E8nDo1AL-LD8UaP5yuanuNztOzxWA9cjVvH6U9HEQChZVamc-8Gg9el0g9vBStmpptLKa0x_roRtVA--Lm3y9k6HKBHyoEuQc6CQeCm86CQ-3OpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درآمد ۲۰۰ میلیاردی مهدی شجاری مالک موبو نیوز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107699" target="_blank">📅 20:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107698">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8956163759.mp4?token=qE2rzI0F2o5iH8KiraWRGd0OoSzyGBqhRgBBGSVHFdLb6XTLQCmJyFSvLLRwZ2fgzCpO8286Lx5H8XJW75QR5BQ_DMD9yZ8m-F7OsV8E4LbQ6xmO6c8ecKE5fy0Tz7mCL35NVaqdiBEKIAPHniWFGHw6LJYFqArICDKINZcs5UD30TrQIWy7HASEIqj8vTNXJxuvgAPKyvNXFU0hhd2_3SF8jq5omPLNa8hlLYxOhDMTPduxIOmDgv5iYZrRpPfblwcaaHcFBCvkOAlZdnk_gAZcVEF7aMpeMKCkLt2tkndDiyg5AusdgBAOxlbYjSYZU8uPD84NpVn6uPltN46gVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8956163759.mp4?token=qE2rzI0F2o5iH8KiraWRGd0OoSzyGBqhRgBBGSVHFdLb6XTLQCmJyFSvLLRwZ2fgzCpO8286Lx5H8XJW75QR5BQ_DMD9yZ8m-F7OsV8E4LbQ6xmO6c8ecKE5fy0Tz7mCL35NVaqdiBEKIAPHniWFGHw6LJYFqArICDKINZcs5UD30TrQIWy7HASEIqj8vTNXJxuvgAPKyvNXFU0hhd2_3SF8jq5omPLNa8hlLYxOhDMTPduxIOmDgv5iYZrRpPfblwcaaHcFBCvkOAlZdnk_gAZcVEF7aMpeMKCkLt2tkndDiyg5AusdgBAOxlbYjSYZU8uPD84NpVn6uPltN46gVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
کیف کوک ژسوس بعد جدایی رونالدو از پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107698" target="_blank">📅 19:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107697">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263935f09a.mp4?token=nxDh59c5WrCLdSVvM6GeEOHgOOJjt4vcCBwRKYoclCzb7jvEhtTN6iYl8M1TgIAAuK5gcIV5KwykAvwmNE-J-biS9cslN6wqsQN15XGI6GiecQv3LMymD-CYAxh0dMmkwY0uPEzr-hR87N70_HIt7XzeEK2z4shc9N1Nn67TEy083_0oWOLTJeK5rpigf0_UYl6gpo_5OO79fK2f_ZEAg2vNqtYzr-4yE_sJeL4UqSU2JxqITxIPh3syNCfvLtS3PCOxAY-mxWAdeNZQNciMp2hOB9aMqkX571awo8dMT5yjtHBVDzYOZtZJJPoHy231f6wNI2kI4QVPevylPma47A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263935f09a.mp4?token=nxDh59c5WrCLdSVvM6GeEOHgOOJjt4vcCBwRKYoclCzb7jvEhtTN6iYl8M1TgIAAuK5gcIV5KwykAvwmNE-J-biS9cslN6wqsQN15XGI6GiecQv3LMymD-CYAxh0dMmkwY0uPEzr-hR87N70_HIt7XzeEK2z4shc9N1Nn67TEy083_0oWOLTJeK5rpigf0_UYl6gpo_5OO79fK2f_ZEAg2vNqtYzr-4yE_sJeL4UqSU2JxqITxIPh3syNCfvLtS3PCOxAY-mxWAdeNZQNciMp2hOB9aMqkX571awo8dMT5yjtHBVDzYOZtZJJPoHy231f6wNI2kI4QVPevylPma47A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقادات از صحبت‌های عجیب احسان حدادی رئیس فدراسیون دوومیدانی جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107697" target="_blank">📅 19:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107696">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=TVvTtxVt279tawhulFHuA-NvO0sDNRyn59DylJOohzMRdDEVR8B1-zwsbjpCQ3gQwsnwmYGdB6enTMZwX7Mm7unFWVfrIv35VlVR7yY_o8ENpLmUACxaYqoCl-pnd69ZBzNXAXY2z8LULLiorNzLClXVH7XD1kZlRfQvbv4MGaXNbLVHc-Rv9gzhu1QExFjkCJvcUD32ZjxMiqD40J5LrTm3MGMYECqz-hqQLv0aR9yJQ1nwjXVRFdKHqXrSIYwM-pxEm3NzAeBkIf6dElqlGL9xVxGxLL-p_3uv2O3i2p_IHuxgHybhAWYbBSv3HD9KYU1U5zWJKAqEYykfhoAEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a8b7a5dd.mp4?token=TVvTtxVt279tawhulFHuA-NvO0sDNRyn59DylJOohzMRdDEVR8B1-zwsbjpCQ3gQwsnwmYGdB6enTMZwX7Mm7unFWVfrIv35VlVR7yY_o8ENpLmUACxaYqoCl-pnd69ZBzNXAXY2z8LULLiorNzLClXVH7XD1kZlRfQvbv4MGaXNbLVHc-Rv9gzhu1QExFjkCJvcUD32ZjxMiqD40J5LrTm3MGMYECqz-hqQLv0aR9yJQ1nwjXVRFdKHqXrSIYwM-pxEm3NzAeBkIf6dElqlGL9xVxGxLL-p_3uv2O3i2p_IHuxgHybhAWYbBSv3HD9KYU1U5zWJKAqEYykfhoAEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
✅
کیفیت تصویربرداری با آیفون 18 و یک سوپر دوربین فوق‌العاده از سونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107696" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107695">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuQnYHhqCysYex9RogjEfTRQf-VkN6qYok71KXRAggxQqMAAgHsuSeCkct2uakpSoFVs3Hf7bvC2h8V4lKQGl_X1ZP5ErbSUxHcynOFlQUYTTYVltb1916osc-Nvojbi3X8f8Twzcyh43WLOhIeIQm8uaxyjYnZgWb8WDqvhXo29s9B7Y7wg5zAMLjOFq3p3QXkscMIA81E4DVY4xhX5aGsCFZbwq2-KuMxfIg5pwMhpkGMJZSnSTLvnC6syZwYjmiFNeJygGXTByiePkoJFSBfJr8w26CG0Nkqw77QTw1U2CdsnS_PYSzpvjSrOW9XF-A_bYP3D1gd_miiPuj-OTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
پرسپولیس در دیدار تدارکاتی مقابل گل‌گهر سیرجان با گل‌های محبی و محمدحسین صادقی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107695" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF6n_dKef5G510nancT8miJ_Gwlce5jt4g-uNvxt7eF7jBD24UpFs9uu-T9atLmO87wjc05TRjtRi05IwbCspAMcEDpadNCuvxn-nB11VQyYURiIA9vkqP7N1gcsj9QdA4Hxag3rVAecBgBHeAHJ3xoU4dZJg1yymYg66MM0Akpq9EgmCGHUR895HSu4Yz3vwceL8kUrZCPsMmwDgNhc6TRQlRKuOUSWulDZlZPJ_J5mOJRrmBuRnpoiLYRiVsrmBeJsjB2tYq65UYg6hSRulZksiZTAvPsqxYUPfEiYHvQOHjaptqCP1G9Cxkid_3Fj231cwHEAALIGMQKH3ympZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
یوونتوس قصد دارد تابستان آینده به عنوان بازیکن آزاد با ویرجیل‌فن‌دایک قرارداد ببندد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107694" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=UUrMEkTwblCQ_Gt3g70kZuftoUmemwWxQyhTTArq3GY3PFKfjlPaziko3LJjtWmVACmIA36OJUhDZjoDJ_-fL22ep6JcrUWOdwkoLiF4f2dv_Nr4DG6sPrQDAH9KKBNtFryfQnWNyLwfp7IZ8GAt6ax5Dcw3fXyS9zxz6cz842S2MDRj8jK8zH3m4cU7Nq11W8xqZxvQ6lUFG5AbY775VkquyY7CHFafCtrgwPEFSoNuJSy8MVyEgzuusx4M-B1_vAArwMeBpzjHPwkIELfB5EPNi4hekUeapwjzs91REJpKWbnF3TBjcY6PEmH7ThLv9Jn7lzR1KCxJVu8UPA8ooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dbd5bf2.mp4?token=UUrMEkTwblCQ_Gt3g70kZuftoUmemwWxQyhTTArq3GY3PFKfjlPaziko3LJjtWmVACmIA36OJUhDZjoDJ_-fL22ep6JcrUWOdwkoLiF4f2dv_Nr4DG6sPrQDAH9KKBNtFryfQnWNyLwfp7IZ8GAt6ax5Dcw3fXyS9zxz6cz842S2MDRj8jK8zH3m4cU7Nq11W8xqZxvQ6lUFG5AbY775VkquyY7CHFafCtrgwPEFSoNuJSy8MVyEgzuusx4M-B1_vAArwMeBpzjHPwkIELfB5EPNi4hekUeapwjzs91REJpKWbnF3TBjcY6PEmH7ThLv9Jn7lzR1KCxJVu8UPA8ooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین صادقی: علی منصوریان بهم گفت چون شبیه نیکبختی، یا باید زن بگیری یا نمیذارم فوتبال بازی کنی! با حاج محمود سفت وایسادن تا زن بگیرم حتی شاهد عقدم بودن که خیالشون راحت شه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107693" target="_blank">📅 17:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=k77FPbW_rqCwziRDevJmYDnVDoHpQ0hmiH469b7PN-rycKUwwAaVg2D84Y2mcfSstg4ENUvqmJNTGgK6LL25dlYBmbhIU8h4TPHTV0CAc1CLVzq-BVPbHbZnNsEk60Ts7AbDebPQPukh-EO5rCyPpDBucz-Edh0QeHV5DHx9TQyQAWLFGZgt_XWA2jRPVfwlucYftpJkQQ8P5OC-1kpzD331S-9eg-XCMgoJwPhQ-jr8N8gXG0ly8VC_OLa8yq_b0GCizeuvDI_PsbZB17IPtjS_ZJqEQUyRGKaMRoOAdRrg2bvkOc_FeDq2kjVA_qP-frYRmSNkY2Ql57f0UDB9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4517b308.mp4?token=k77FPbW_rqCwziRDevJmYDnVDoHpQ0hmiH469b7PN-rycKUwwAaVg2D84Y2mcfSstg4ENUvqmJNTGgK6LL25dlYBmbhIU8h4TPHTV0CAc1CLVzq-BVPbHbZnNsEk60Ts7AbDebPQPukh-EO5rCyPpDBucz-Edh0QeHV5DHx9TQyQAWLFGZgt_XWA2jRPVfwlucYftpJkQQ8P5OC-1kpzD331S-9eg-XCMgoJwPhQ-jr8N8gXG0ly8VC_OLa8yq_b0GCizeuvDI_PsbZB17IPtjS_ZJqEQUyRGKaMRoOAdRrg2bvkOc_FeDq2kjVA_qP-frYRmSNkY2Ql57f0UDB9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تعجب و عصبانیت قیاسی از قیمت دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107690" target="_blank">📅 17:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=n8vIvnHD3KZLdbgcOilCdZ63HbAPj8wtC6kjDuOcoIFUQ30nPbCigYmg93TMAzqUmdZmh_KOga_weV2IsGN7nXG6y92a-z1euicgVJjTXorE7gx4pPTohcBYT8FQMcBTS86m0s6V20l88Nb2EOkTgr4JrdcESOFfFmUVj_Teu4TfONRBtuv54763roknIews9xZ1H9_RjjsgHP5xoBa3q4pbJLaRCj4krCmZHM1qGDRcjUKCBHQ_ZyvOt2LHbAlZ5dLZRFN6_omYFSQzHWwh-j2kdHoFLVq2saO7X0in6ApTDngZsuCC6XwYC1i4lBntCdpwRU8FU85Qp7BF02Q3-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac9f22f0e.mp4?token=n8vIvnHD3KZLdbgcOilCdZ63HbAPj8wtC6kjDuOcoIFUQ30nPbCigYmg93TMAzqUmdZmh_KOga_weV2IsGN7nXG6y92a-z1euicgVJjTXorE7gx4pPTohcBYT8FQMcBTS86m0s6V20l88Nb2EOkTgr4JrdcESOFfFmUVj_Teu4TfONRBtuv54763roknIews9xZ1H9_RjjsgHP5xoBa3q4pbJLaRCj4krCmZHM1qGDRcjUKCBHQ_ZyvOt2LHbAlZ5dLZRFN6_omYFSQzHWwh-j2kdHoFLVq2saO7X0in6ApTDngZsuCC6XwYC1i4lBntCdpwRU8FU85Qp7BF02Q3-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرمحمد، خواننده آهنگ سنی نردن گوردوم رو بردن برنامه تلویزیونی ترکیه، اولش براش دست زدن و کلی تشویقش کردن،
ولی به آخرش که رسید دیگه نتونستن جلو خنده‌شون بگیرن و همه زدن زیر خنده :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107689" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=coIPiqDjlQfwkat7KM3ExVls-NhYnHJmEx5KVYJ4y47XL44v8uN3umUYFg4siri6AiBW7GLjnAnEJiathOJknRUwzRm05MZLadW5xv9kGYaDMWctLP_07WnS-qpFnrZ3FI-sKORJnDTbIrnrRVt6NKud8C7rArxGC7KN4bWRizG9JWxn-NaLrESZ7Zfxd_bkKhQFy0Y8hyB2W7xQz25MBHoPcWj2OZ8qImuiSxmUwo4QK-xKUKu1X0QU0S43mUytc_P4AXG1yop3d2Tj1vToj095YeVGQVun8FeHCjxNvapHGRUhS9mK_Vr_ENT0FmaoiI6NLZlW0OUoNg_W4QCk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c643f6bb4.mp4?token=coIPiqDjlQfwkat7KM3ExVls-NhYnHJmEx5KVYJ4y47XL44v8uN3umUYFg4siri6AiBW7GLjnAnEJiathOJknRUwzRm05MZLadW5xv9kGYaDMWctLP_07WnS-qpFnrZ3FI-sKORJnDTbIrnrRVt6NKud8C7rArxGC7KN4bWRizG9JWxn-NaLrESZ7Zfxd_bkKhQFy0Y8hyB2W7xQz25MBHoPcWj2OZ8qImuiSxmUwo4QK-xKUKu1X0QU0S43mUytc_P4AXG1yop3d2Tj1vToj095YeVGQVun8FeHCjxNvapHGRUhS9mK_Vr_ENT0FmaoiI6NLZlW0OUoNg_W4QCk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
خوانندگی فرزند محمد شریعتمداری وزیر اسبق کار و صمت و مدیرعامل هلدینگ‌خلیج‌فارس مالک باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107688" target="_blank">📅 16:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=dGa5ZwgkJhjRwtaxnQBRasCORuPbRdsDy6rmu2gJVMpdIYUTfXc3-KKK-k_QnLZe6LIm1KUWv7LVlB17gWLJeW257ZD1m9j8EYUOIx-DetJkta_BADV1x94aScpe8V1NdbxEn2yWDUKPp09cRzWOvbxYEb2lLzFPKo7rDBYx-zPaJ2WEW5_2MzMv-z_oBJ-OopxKe5cqIoC4irPS-6kWBvOnUbX7iajvKlIjmJgoSwRc7o417Momxfr8BkCsLrbPLG3RLREeszM9GaLw8d4wlG-bWfsIQXOymDXshlozdsdnh8Fcb6e0DKGXLbiF5nz_F3-a7J5Fq-D6Elwq2vR1egW4BmInmA769nQRPCXT0Vl9xbB_08iJuHT7CdMFvmlOQTWsUvi06clRHruWTy4C2GizgyLMD9uKUCKx0dhesBAmK24LLA8y2gApO8I_Vugl7l7wdlrcGEZ1zNX9IxTDSRb4edmAN7I2sdf3Xo2zOKmFv5nV_KDfXHpv5F_Te1tTVpEWIkJhrQWZG1M2YVzYgnxJNcE3jhajKMWUqXP_B98-sKhBRnI79xWNXcqSDIcAbycp7OmZuiAcSLz4RjCakTrwNvBoJKJCzy6xXonFRpofONQl5cByNQdV6dzRnT7zVSZSgj4-kz3R4ZeSn9R1cZp22ToRpQT-zuJz2-nB1q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc463f33d.mp4?token=dGa5ZwgkJhjRwtaxnQBRasCORuPbRdsDy6rmu2gJVMpdIYUTfXc3-KKK-k_QnLZe6LIm1KUWv7LVlB17gWLJeW257ZD1m9j8EYUOIx-DetJkta_BADV1x94aScpe8V1NdbxEn2yWDUKPp09cRzWOvbxYEb2lLzFPKo7rDBYx-zPaJ2WEW5_2MzMv-z_oBJ-OopxKe5cqIoC4irPS-6kWBvOnUbX7iajvKlIjmJgoSwRc7o417Momxfr8BkCsLrbPLG3RLREeszM9GaLw8d4wlG-bWfsIQXOymDXshlozdsdnh8Fcb6e0DKGXLbiF5nz_F3-a7J5Fq-D6Elwq2vR1egW4BmInmA769nQRPCXT0Vl9xbB_08iJuHT7CdMFvmlOQTWsUvi06clRHruWTy4C2GizgyLMD9uKUCKx0dhesBAmK24LLA8y2gApO8I_Vugl7l7wdlrcGEZ1zNX9IxTDSRb4edmAN7I2sdf3Xo2zOKmFv5nV_KDfXHpv5F_Te1tTVpEWIkJhrQWZG1M2YVzYgnxJNcE3jhajKMWUqXP_B98-sKhBRnI79xWNXcqSDIcAbycp7OmZuiAcSLz4RjCakTrwNvBoJKJCzy6xXonFRpofONQl5cByNQdV6dzRnT7zVSZSgj4-kz3R4ZeSn9R1cZp22ToRpQT-zuJz2-nB1q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یک‌دقیقه با اسطوره رونالدو در لباس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107687" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=El-c_zRtNYysmUH8OPEEF0WVc2uVBp2NRipIDCV6fw3ISDR92BLvpu_ebw6OTIzX95e2x2mb-41aSX3JJcmqKnfSjpahOdGzvkwFiWt3XQgkiBkXOkz4u5lSgYYXjpy-47BodvvKKyoOYsFT-Eb6_RuPDWxOsKQzf92lYnjafatOaHkbNUUNZDrncEZZ9Waoo9pF--7o_-udndX3XRYF9H3qekU1fvUrg8CyOP2OH2Z7ncRLtbaZ8-aMxAilNHdsJG3zC5DZaZdXzyNl-CfYasNJzZon7VZ2cY8lwAXuT3IOVN13HxreU7nhk7js4u_OK-skB0YceuigbG8g6Oub7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098c9ea234.mp4?token=El-c_zRtNYysmUH8OPEEF0WVc2uVBp2NRipIDCV6fw3ISDR92BLvpu_ebw6OTIzX95e2x2mb-41aSX3JJcmqKnfSjpahOdGzvkwFiWt3XQgkiBkXOkz4u5lSgYYXjpy-47BodvvKKyoOYsFT-Eb6_RuPDWxOsKQzf92lYnjafatOaHkbNUUNZDrncEZZ9Waoo9pF--7o_-udndX3XRYF9H3qekU1fvUrg8CyOP2OH2Z7ncRLtbaZ8-aMxAilNHdsJG3zC5DZaZdXzyNl-CfYasNJzZon7VZ2cY8lwAXuT3IOVN13HxreU7nhk7js4u_OK-skB0YceuigbG8g6Oub7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ابراهیم شکوری تا رحمان رضایی ...
‼️
در جواب ناکامی بگویید: یخورده سرما دارم
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107686" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086fe81733.mp4?token=ss77_uZFXigvOe2fXcbTR52wpvspAZrn2ZS_JPh9o9tKmNpHRnmwG-PWrfSQ-s3goOHb_ciRXYH5Ki7bsYRyMPfUV5n-sDKNqyxl0a5mqOpyBQzPR4U2Fc18c4I-bQK6hl4mvtTjYd3t-FXuSmXOkR6goZaZKhqtBOhEnEqooV9eAc9n276bzBOvm20RiOnp5rFK42rR4DPJJ1C4y1tRt6v9KxDlg0fvwO1kOJjJJrPKpQGuiavhtlozu6mG4w9zFnzXmYpuWSUzxPdkADGGrdmyp1HyCSxaYUiRXixsCpAZt-82ra9zWvHG1ZPwaPAqUHDOOi0hf53i5MLsg80BbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086fe81733.mp4?token=ss77_uZFXigvOe2fXcbTR52wpvspAZrn2ZS_JPh9o9tKmNpHRnmwG-PWrfSQ-s3goOHb_ciRXYH5Ki7bsYRyMPfUV5n-sDKNqyxl0a5mqOpyBQzPR4U2Fc18c4I-bQK6hl4mvtTjYd3t-FXuSmXOkR6goZaZKhqtBOhEnEqooV9eAc9n276bzBOvm20RiOnp5rFK42rR4DPJJ1C4y1tRt6v9KxDlg0fvwO1kOJjJJrPKpQGuiavhtlozu6mG4w9zFnzXmYpuWSUzxPdkADGGrdmyp1HyCSxaYUiRXixsCpAZt-82ra9zWvHG1ZPwaPAqUHDOOi0hf53i5MLsg80BbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
رونالدو رفت و پرتغال تمام شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107685" target="_blank">📅 15:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq48SvBKGmfe9KBelAj4WOPReUflRxjzb9S9dRL8Vu2HJSkEmGYPzjgRB2VItbil55HScT1YxfnntEYdvotsc0MAWuEsj0EVYpXhWJxfqe-KFiJNm04J8H8-m9nCmepWyQpxBJfSTYhthLdnqB3JB5gRoLajaB1_Y_kYD_50Se3OUq_e0d9h91ucte4yDSar-Mt-AIF03tq7OQTe_Vk3WMVjqRuPaIJuY1ktqg8QnOPBMt5Kqe5BbA40MuY18j8SZZCGX1ThuDTrTyz6gt_RZOuUPTc3NxCeSK14oeiCpN-IfPx2NnvH8vrWp2h5m320oPaOXHHXQdZ5Z44D6Li_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
🇪🇸
فابریزیو رومانو:
🔻
نتایج آزمایش‌های کادر پزشکی بارسلونا تایید می‌کند که مصدومیت عضلانی رافینیا که در اردوی تیم ملی برزیل دچار آن شد، جدی نیست. رافینیا از هفته آینده در دسترس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107684" target="_blank">📅 15:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=XUgtRfE960fxPyUPnzRodjQzCbmm07DnQUEHJ1T80SHoJf0i_whtKDPR3EF3NWmGdZ9SC5gQIaHEenOeRquakMmUeuBYeaOkw8YBnwjTYGUjyXWLzHbDn9O0l9zvrUu2siG03dufreAYWOCqX2pyud9BI9cHrr2phUPUi9FxYy7uoOa1x0zE8ry3s6pO9Cy6adgfIuRw5Cd7nS37GehDJhQQowRzTC3LTswGNdgOEOda6RRHLmoiUntWcIWejD3rXPKaK4VbfNytoD9ZKLW6C0xArgoe2Mr9jNhUc9uRKLI1Y4oLl0PzHW4hhYaVy3QANrrnQjlUjoCUv7pQxT3_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fc633f5.mp4?token=XUgtRfE960fxPyUPnzRodjQzCbmm07DnQUEHJ1T80SHoJf0i_whtKDPR3EF3NWmGdZ9SC5gQIaHEenOeRquakMmUeuBYeaOkw8YBnwjTYGUjyXWLzHbDn9O0l9zvrUu2siG03dufreAYWOCqX2pyud9BI9cHrr2phUPUi9FxYy7uoOa1x0zE8ry3s6pO9Cy6adgfIuRw5Cd7nS37GehDJhQQowRzTC3LTswGNdgOEOda6RRHLmoiUntWcIWejD3rXPKaK4VbfNytoD9ZKLW6C0xArgoe2Mr9jNhUc9uRKLI1Y4oLl0PzHW4hhYaVy3QANrrnQjlUjoCUv7pQxT3_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
🌟
رسانه‌ها با انتشار این تصاویر مدعی شدن که نیروهای خنثی‌سازی هسته‌ای آمریکا همراه با یگان 75 عملیات ویژه، شبیه‌سازی و تمریناتی برای تصرف و پاکسازی تاسیسات هسته‌ای زیرزمینی ایران انجام دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107683" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0274908694.mp4?token=nqgki_4MEERvCZVw-yiXpcZFQpkvqZGEZZg2tVyvd38SoDD_sDfU6TLsgpepa6XLe_WrMFDv2xBaUPteQoWqh7t2uxzXacu-gccHAokGpV0OgBCmThZAO64xVKnSiQodeUFNa1tXOAs0FHFb-l9VaOG20qd0pChhFdwvpDzXnY7d16FtuU1_dknAj5-MKx1LXwwAtF2s0qNjw6w6KY3xxWMSsVwZQexUgwOEfFFnhh1LuNRT1q7wgTENmhtRSv1k4ZtB_BPxnXxnPv8oriOgd6Nljrrl0jQCAz5mJv3-c7rfqN5rN3QjjIyVxUSgA9ntEpumu1zERR2TuKCM8f5ePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0274908694.mp4?token=nqgki_4MEERvCZVw-yiXpcZFQpkvqZGEZZg2tVyvd38SoDD_sDfU6TLsgpepa6XLe_WrMFDv2xBaUPteQoWqh7t2uxzXacu-gccHAokGpV0OgBCmThZAO64xVKnSiQodeUFNa1tXOAs0FHFb-l9VaOG20qd0pChhFdwvpDzXnY7d16FtuU1_dknAj5-MKx1LXwwAtF2s0qNjw6w6KY3xxWMSsVwZQexUgwOEfFFnhh1LuNRT1q7wgTENmhtRSv1k4ZtB_BPxnXxnPv8oriOgd6Nljrrl0jQCAz5mJv3-c7rfqN5rN3QjjIyVxUSgA9ntEpumu1zERR2TuKCM8f5ePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚽️
پایانِ متفاوتِ دو اسطوره.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107682" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApadJnVQcb2nK8Jh0u7g1PqOUOo1zkzXODsCHaaeH0rivrvoGXi_NNp4MiJNnd_vQGxKpuX4FPlLkikq7pSfY3TqU653BaYShBXEOUfBtcOlhPj8xpKICQ_A8ANtjRS2i02IbiiN2mwC7TUqKQIpp3-EVcQGNCBOF6DPNm72Kqr-tMSLC9O3rhzYbuwxdP4YPRfNQ-0b_2hg6sRIZ-52t2114Man8eUqAX79Fqj7aw7CBcNycEXaAtyy18oDWbk2dB_sDVdKNwNPloH7GstkUOtICVCMngHxG9ow-8tKmJZcPIg0h9P6RRmwALjR-EPCUA1QcWyYaTVp2mKEKCkhxc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApadJnVQcb2nK8Jh0u7g1PqOUOo1zkzXODsCHaaeH0rivrvoGXi_NNp4MiJNnd_vQGxKpuX4FPlLkikq7pSfY3TqU653BaYShBXEOUfBtcOlhPj8xpKICQ_A8ANtjRS2i02IbiiN2mwC7TUqKQIpp3-EVcQGNCBOF6DPNm72Kqr-tMSLC9O3rhzYbuwxdP4YPRfNQ-0b_2hg6sRIZ-52t2114Man8eUqAX79Fqj7aw7CBcNycEXaAtyy18oDWbk2dB_sDVdKNwNPloH7GstkUOtICVCMngHxG9ow-8tKmJZcPIg0h9P6RRmwALjR-EPCUA1QcWyYaTVp2mKEKCkhxc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
😆
😆
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107681" target="_blank">📅 14:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyGNivDMPkh0PgHKhSgRlOc61jvlOhwzE3E78bMEGQuDZKggFYNVHHyaBpUhqJkyc_a2QJoGzaBAVgbp6RYJ2GFIypWpNrN73S2WSp0yOVLmQ_EhnQX8lzC0zViUfgoh3ZV-fRSaGzZwDE8vA3eT7ATLUawtH5qvrwjfYbIXsAHkaroDxwTT8sgkLDmnagnuimP-SZyLz72H1xGkNJhHXUBJWb3vSuLKThamdrGQaQpqkEgMUigLKvs5aw9JwH0nSPUqmS3cQiaXpE3Pax5EudhoO4y3Uh1VlGIjYjGzE1Z6KMrWPnsjoJ7E8yS03J68uGl6WJSSYEZjHKixqGG3ikWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353ac7dbfb.mp4?token=utvD3Pc_1LzRFIU2m9L9f5qF47hAtkkVhWKIAW4-6ASOV5jje_6b_FPJJCbluNYIvfIAo6OETWl2po-6cc69B_7k1gxX3Q3zoLNt4K-EOGI7j74PZajJACF4rHiNgry_i-kKNmkoBlM5hcAB7RlzamWBQU2PKpLDV3MnfcTuqROpdOK44TDvzLclE16O5_k-RvOSCGhhFny99QI4BlcfaZFqZhGTeMMB_YcmD5LIvPsocWxI_2ZU0uvjcjLBFXm-X8dvZRfcbGeJqeTiJ3wW538EE_nMb5vt9oCdtNhSQ0LzoDOLfypSgRNnEoBCqXbcMm7N73oYE1Lll5N_gS3qyGNivDMPkh0PgHKhSgRlOc61jvlOhwzE3E78bMEGQuDZKggFYNVHHyaBpUhqJkyc_a2QJoGzaBAVgbp6RYJ2GFIypWpNrN73S2WSp0yOVLmQ_EhnQX8lzC0zViUfgoh3ZV-fRSaGzZwDE8vA3eT7ATLUawtH5qvrwjfYbIXsAHkaroDxwTT8sgkLDmnagnuimP-SZyLz72H1xGkNJhHXUBJWb3vSuLKThamdrGQaQpqkEgMUigLKvs5aw9JwH0nSPUqmS3cQiaXpE3Pax5EudhoO4y3Uh1VlGIjYjGzE1Z6KMrWPnsjoJ7E8yS03J68uGl6WJSSYEZjHKixqGG3ikWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط امیرحسین زارع با شکست حریف چینی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107680" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
وضعیت عجیب عدم پاسخگویی اعضای تیم قلعه‌نویی درباره نتایج ضعیف اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107679" target="_blank">📅 14:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruw7tFVj8i58EkKnGYCLHsW7lti1VVYkcp_WcRscgXbsUYFTdIagey7ouWG1YUMasR9uYlixaIJ_fMQf6IlPMZwfo3NLjNLDtPFV86udq9cNEucm7LOiXXvhW0zqY8Z3FmTwnLOxW9DDGftBtkAdq7eIpl2hlEqsVyfqbyjqe45UV3mQmp-0B86IRIx9T1dEUNUxLoI2bYAcTSQfLAdzaCR45qjGYeRf-Ye8U1luAQ6S37z1nrkeHK3jmKqqqBReRaSkXoMLCAE45v09YXGQ42wwGVb3GQt6kObEOwgf-2YRbP1vsGeqlbbxHK3rhuVRp7l-5smVEZj792RlwUw87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
⁉️
مسی یا رونالدو؟
👀
🤩
توماس مولر:
"در طول ۱۰ سال اول دوران حرفه‌ای‌ام، همیشه کریستیانو رونالدو را انتخاب می‌کردم و همیشه در مقابل او شکست می‌خوردم. اما وقتی به کل تصویر نگاه می‌کنم، متوجه می‌شوم که لیونل مسی، بزرگترین فوتبالیست است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107678" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=pkq6Bq9vVH1keaqgUJidA3Dke29ol0HbABzm84UMGGx3FwPGT9Ih09HN4F8x97ucHmeFl4yg0zVXFsaTEwI5ZFBwdG7XPQFnReJy-aoPzIomrEkKQI1nncewcL2nYl_1lbvJVm9Cz2tZ_M-K_gz-EmP8f3y2pX1o4qqHknLFfH4rtiqS7NIo_OvM4XHVIvp-o8KdqUpcaSjfjkXWVHzKdZD0frnaB-ICK8hU2-YbAVEDsrYiXZwfaOeIdkCnuA1_dG22-GoDUA9ZqeYvNN8BczWJhRBuIPBEhEB0ECJuQ2-Std7_6RRqxxfhbQ_a4MKwH-1HYGFyzpd6XSvFy62Icw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3d0d9fde.mp4?token=pkq6Bq9vVH1keaqgUJidA3Dke29ol0HbABzm84UMGGx3FwPGT9Ih09HN4F8x97ucHmeFl4yg0zVXFsaTEwI5ZFBwdG7XPQFnReJy-aoPzIomrEkKQI1nncewcL2nYl_1lbvJVm9Cz2tZ_M-K_gz-EmP8f3y2pX1o4qqHknLFfH4rtiqS7NIo_OvM4XHVIvp-o8KdqUpcaSjfjkXWVHzKdZD0frnaB-ICK8hU2-YbAVEDsrYiXZwfaOeIdkCnuA1_dG22-GoDUA9ZqeYvNN8BczWJhRBuIPBEhEB0ECJuQ2-Std7_6RRqxxfhbQ_a4MKwH-1HYGFyzpd6XSvFy62Icw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
دیس سنگین ژوله به قلعه‌نویی بدلیل سوال عجیبش از خبرنگار ازبکستانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107677" target="_blank">📅 14:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eade000140.mp4?token=Oy_pb-8opnPqVbfpP96wpZ53HsyCNHb39FAz5dqg2Jz2Cc40Fj-LYbA3ryohuYdeKeQ3VZAGtVHJUr-Ji7R802AFSJ3WFCV5yrEzbhIdh1z4n4U0KLl-OSkG_xvbK9EwJTawXeBOq7ohSUDquL3mOWdM2SCoRdLGkvL_SA9XV4bsDDZbOBzuIxtdnNpOnhMIaBpwU5AxaYaVqPFa5g5Tn3P4-CV82OWhn0JRT5srKvCTLEdN5Xl4oU1McIoxU_zK236UU8xNIKdkFDVh5mcopf38JGoEkbl-YpHymOXW7Xu0R47spUGueDdMY5i_k16c6AdbiqZE-ZuB785Jho3iGiCU_NL-1woURVq8_AdA6vjudNAWq0WkJ-2T5lSAnoNrcampv5tuGGDw5BGq_UB8GWMqJVqdmSOi-z9_ssqRfI1MDi7igPhWWa1JJhBuNF8GckJlhWzQH80LFLHnSvbXPyF5yD7nXKqyC4c8YRjOwhkaQo1z_9t68td9GwEB4vvCius0jxukj9zFKzLOFPtMNIQbhVYozMW7MERPiYYcnXnvgyb9L9TkXA5dFKr2FnAoUi2WUwILGPmru8WGGw4YcTesC4MQyNwb0G00Izfdw_xkKrgcqv4z077U9vxVT0o1okOOITrLjF6orpR85R7DWjpl5dGta3h4m8yWqFJgtE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eade000140.mp4?token=Oy_pb-8opnPqVbfpP96wpZ53HsyCNHb39FAz5dqg2Jz2Cc40Fj-LYbA3ryohuYdeKeQ3VZAGtVHJUr-Ji7R802AFSJ3WFCV5yrEzbhIdh1z4n4U0KLl-OSkG_xvbK9EwJTawXeBOq7ohSUDquL3mOWdM2SCoRdLGkvL_SA9XV4bsDDZbOBzuIxtdnNpOnhMIaBpwU5AxaYaVqPFa5g5Tn3P4-CV82OWhn0JRT5srKvCTLEdN5Xl4oU1McIoxU_zK236UU8xNIKdkFDVh5mcopf38JGoEkbl-YpHymOXW7Xu0R47spUGueDdMY5i_k16c6AdbiqZE-ZuB785Jho3iGiCU_NL-1woURVq8_AdA6vjudNAWq0WkJ-2T5lSAnoNrcampv5tuGGDw5BGq_UB8GWMqJVqdmSOi-z9_ssqRfI1MDi7igPhWWa1JJhBuNF8GckJlhWzQH80LFLHnSvbXPyF5yD7nXKqyC4c8YRjOwhkaQo1z_9t68td9GwEB4vvCius0jxukj9zFKzLOFPtMNIQbhVYozMW7MERPiYYcnXnvgyb9L9TkXA5dFKr2FnAoUi2WUwILGPmru8WGGw4YcTesC4MQyNwb0G00Izfdw_xkKrgcqv4z077U9vxVT0o1okOOITrLjF6orpR85R7DWjpl5dGta3h4m8yWqFJgtE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
کسب مدال طلا توسط محمد نخودی با شکست حریف ژاپنی در فینال بازی های آسیایی ناگویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107676" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=unElaLKGAfkAX1OdM8ZzQHTNWw6gEn9cRYryebtpyBVoo2s5aITJSAiVlLZYlSGfEKlG5cwK1LUObiovIEvuG13xFXSqBbk8947Wz1nPscYnQOrbh7IZxBR4rgbODnu27Wlqh6pu80STpS5sB76yMzqOll9K2LgXDbYJL_bLYbQL3j6u3XgJsoBZgxwYMkQ5o8Yf63KAyVr2pPlFI7qXCCXPUAc349XbW949nuYKEd708sxvNPJKNa-m_FJLxWl3yoEddvExJmS_LBgzW8iUbM--vV8wwPbUcjzTucxUiDLB9vQnxbbq07RKirTTWVvExvB1yLgVzq_02zmNhBLFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46780b4e7.mp4?token=unElaLKGAfkAX1OdM8ZzQHTNWw6gEn9cRYryebtpyBVoo2s5aITJSAiVlLZYlSGfEKlG5cwK1LUObiovIEvuG13xFXSqBbk8947Wz1nPscYnQOrbh7IZxBR4rgbODnu27Wlqh6pu80STpS5sB76yMzqOll9K2LgXDbYJL_bLYbQL3j6u3XgJsoBZgxwYMkQ5o8Yf63KAyVr2pPlFI7qXCCXPUAc349XbW949nuYKEd708sxvNPJKNa-m_FJLxWl3yoEddvExJmS_LBgzW8iUbM--vV8wwPbUcjzTucxUiDLB9vQnxbbq07RKirTTWVvExvB1yLgVzq_02zmNhBLFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آخرین اردو تیم ملی قبل سربازی =))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107675" target="_blank">📅 13:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107674">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDka2OXH5R-x-TWY3IfZPt8v1oF_Om6P5IZvPLsT2j5A--0_-jyjdo57pQZH4Pp840gYjHhGymx2ZBPFQwqcVBIFHMXLYyAOnOJP_RiSYHH2doNJywQlWYK7SmGo1DjDJoCOYdowoOTnz9MEn2lzeJ6P-hV_tMo5DefJQ_jVHudg2fcHx6LHBg1yva-NFpQxZ4CVV7WtY5YetYA-CHtEMCtwYFf9WSoeDV-9DdBeCOXf0_os77W4TDv7ZAejxtdrtWpREX0E7U6GFCf9OEN-R2JhSC1Ui3UecLp6YN5ix_opqoUi56NqE6eK7ChAoneTxm-Syug-HSwzbY7hcBVV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
هویلند بازیکن تیم‌ملی دانمارک: شادی دیشبم برای ادای احترام به رونالدو بود و هیچ قصدی برای توهین به بازیکنان و مربی پرتغال نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107674" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107673">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=fO7flhMFOzQ_Op_1iTzeChrhUsakkPa-f8Ig2R8oCifI0HzAYfwYEJIbqI3XZ3jDVUM6OSr2ERq_FTnqJvZqD6sZsDP6X39UKImSeZJEE4wdh2QiS1NOfm9KGKgn67-ae-2YbqV59fzKL6bIZar-S4ba82CpFBmgU7o6YSkbHbsVNOt9xYwABoRaujFryYO4ZnZ5pH_VIF4R2kFg_X7-cYrH-vUxJVdkWYnSa5segLK3n4vbI_ILHLTIdREhyNM3FlcFw0FFeNEd4ZYpbuNl7iyubFqHgtmgTQZqlrNsvCh4jbwHgGgW04RcOoT1pOS6adXnKPVX-JiumT9bE5tO6JGLWkZbKh-4KtwrhGiCsQ_dZ4RT0cnKnPLgoRIuLw-q0iLi5DsLl5KkCm8NPHOfskNFeUTyYDl11aLWqnXchXT9WWvUg1C2FIT-wuFoJbbpIfHc-qiFExM5NQpl7Ua5NrECGNE8l0ZesK555HtiiC7mW1j5_mPcZGJ1i4eb4GkH-nOt7x0GK3S1OVkeTbuKUKPRiAdoo_GRBahMJ9B0RaN9CqbYUpUy1Elj8xkVATU45_pbvRSVi5iFJhrm8GmefAkbu63fSO9yKlyLM9h2yd_4KeO3WZlcdBacWqa1m8cOwOpHOUeLTR94QUxwmvOrREGLbkaIEgY8gagoVUp4taQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817ab8c188.mp4?token=fO7flhMFOzQ_Op_1iTzeChrhUsakkPa-f8Ig2R8oCifI0HzAYfwYEJIbqI3XZ3jDVUM6OSr2ERq_FTnqJvZqD6sZsDP6X39UKImSeZJEE4wdh2QiS1NOfm9KGKgn67-ae-2YbqV59fzKL6bIZar-S4ba82CpFBmgU7o6YSkbHbsVNOt9xYwABoRaujFryYO4ZnZ5pH_VIF4R2kFg_X7-cYrH-vUxJVdkWYnSa5segLK3n4vbI_ILHLTIdREhyNM3FlcFw0FFeNEd4ZYpbuNl7iyubFqHgtmgTQZqlrNsvCh4jbwHgGgW04RcOoT1pOS6adXnKPVX-JiumT9bE5tO6JGLWkZbKh-4KtwrhGiCsQ_dZ4RT0cnKnPLgoRIuLw-q0iLi5DsLl5KkCm8NPHOfskNFeUTyYDl11aLWqnXchXT9WWvUg1C2FIT-wuFoJbbpIfHc-qiFExM5NQpl7Ua5NrECGNE8l0ZesK555HtiiC7mW1j5_mPcZGJ1i4eb4GkH-nOt7x0GK3S1OVkeTbuKUKPRiAdoo_GRBahMJ9B0RaN9CqbYUpUy1Elj8xkVATU45_pbvRSVi5iFJhrm8GmefAkbu63fSO9yKlyLM9h2yd_4KeO3WZlcdBacWqa1m8cOwOpHOUeLTR94QUxwmvOrREGLbkaIEgY8gagoVUp4taQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✔️
نکاتی‌که قبل از خرید آیفون دسته‌دو باید بهش توجه کرد؛ برای رفقاتون حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107673" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107672">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv7sgoV7umJT96ORweVq0e2ZVKRHUlNE0HHMzNtbE3N3PhbGy5V0mf6NSWWcekw9R4f8orXoJqz3TM7aj_0ZxNW0emHAqOLS_c129uMVQ9EQJA7sjkxHlDi9qPwaHtOohGD7hCGTYtr91DF7QXFyZqakE3vfRa1K47Vp_80n8aazbyefpKPylnPwRT4FKxtP3rW_cKlE2g9_ckSE7cfU0dIiknJK7eGBPfpBd9STX0OLZg7AaIvK6E9vVZIt_ShHzEqdQP74owXwnziHERvi7tmXzqCU3obJyUym1dZBJsNh7f0fkCcXGgxMnv-R9txaEK_3MwDBlbfd-j5uvIh9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
استوری همسر رافینیا ستاره بارسا!!!
فوت‌فتیش هستید دیگه چرا علنی میکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107672" target="_blank">📅 12:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107671">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=pzF29Xzu8jr29EuRndQPXVjCHxkYwVaTFyPXidTpQK2eT-Ctmr_MUsLpXw70s631BGudQKfp2D3cG-vpoTO0HBmfEOQK-wteFOEPg5m9aRtNOfL7fo3mAhsX15WerM5_yTOTtZMI8_wC8XNFbTzz4r5aikuab_c58qs0V97m5pbkK9N-8pROlYYcXC-oflCI-uN0mS9N-LfwS9HuSbHV9vrmezls5BE3ZzgMTrwkF2AacReHgfuhKuG7SnK5Au7ecHQ4b-ghG-NpU0svNOGH9DTY1DMp1kYLgU5D4hFZ-9LZIBV5-5BOhdJGv5ECokgHVsKVpHxsOT3ewkX-Lqnc1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eef6851e.mp4?token=pzF29Xzu8jr29EuRndQPXVjCHxkYwVaTFyPXidTpQK2eT-Ctmr_MUsLpXw70s631BGudQKfp2D3cG-vpoTO0HBmfEOQK-wteFOEPg5m9aRtNOfL7fo3mAhsX15WerM5_yTOTtZMI8_wC8XNFbTzz4r5aikuab_c58qs0V97m5pbkK9N-8pROlYYcXC-oflCI-uN0mS9N-LfwS9HuSbHV9vrmezls5BE3ZzgMTrwkF2AacReHgfuhKuG7SnK5Au7ecHQ4b-ghG-NpU0svNOGH9DTY1DMp1kYLgU5D4hFZ-9LZIBV5-5BOhdJGv5ECokgHVsKVpHxsOT3ewkX-Lqnc1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
‼️
🎙
واکنش متفاوت بازیکنان تیم‌ملی پرتغال به خروج ناگهانی رونالدو از اردوی تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107671" target="_blank">📅 12:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107670">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ6J6Dn1PZOfDtJoOIONL2weTqMRqvrLzFh0V4EXjwwM27gK6GRyUBc2kdvXfm_-gBMKO1XsAWa0OHIVF6A2EX4LlYh37emP6MzfswpMfKi-ODk3FV0HAGvbPILPZNAj2ifPhotEw88ThmMXifYXbTqrSOzTIB-p8_rj8SeByFskZH_xX8CZM2ahsQo8Gjhi5e8x-_7rRLuTqESt6oagnGcW6mlHZv4dcoHzqXEiTkSq1n4-YXOskHGxh_FkrC05amzmAKUUrMAsWTI-5Iu3APpLehPy8bMAgmglAA6Fp9fVOKG-_0LRf1uVBY446Qn4WsJv3XzebwHOe5buh8H4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تایلر، د کریتور (Tyler, the Creator) هنرمندیه که تصویرش روی پیراهن بارسلونا در ال‌کلاسیکو رفت مقابل رئال مادرید قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107670" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107669">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6fko5z8KFOX6mCUOEzCfjgjqXmSwILTcB5cMUbUIkfZwx4mwuphhsVxhDTZkUYdTSFc4vWIN636BP42tQnMxlslGa8FikDIDxf_RLE2Sfm8rXVJ3seY1IZ-HXv3_ube6FCmt_ylfN9q6WVvuHawxb0Ltx8Y4wIv6fFUBBdNb983jm2Qk8dIB7pYFH9E32UlNYNfQB44kakR4OTgMwMBI0vSyWCtqQ4dSt19un-vE8EMecjpTC_8kcWqmnUdlUkIfPx7UXlTvkKDvitoHxgrv3M8emlrniB8O8OTOyt34lOqhCZa3-CctzNaFdYiM8njoBXM74vSx47AFEOI1u02Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇵🇹
خط‌حمله پرتغال بدون حضور رونالدو:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107669" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107668">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoGWK8IoDZztP0z-_PxrD4dT9pKIeBQUag_v7JoNFgH_OzJ5tcfDNS5ysphbMGYc2P4CL1LFMaFge-ycqI69YSACi6aNsLK-cqe8cTWwPv9r_39KuSdMCc8jd1rp-ezXgjx5zlCTGTZ0z6yoaR-cohGeqeDQOIh_SgexQMAUz5_2phJLzKTXreg-ZJYaSe-Pzoyv59_1CmC7vTYem-y-VTmFe6ybncAxlHIZRu0opQr6RoTufzpG5e2c9J4D7uZQ7sgIidKjUYgXpLNb3Hm84QnLGwBtfEMQGDKIzlhqmpqTOAKzx9eQwoZS4c8zIUHiA6CUksFIWPIk2uU5Zs6xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
📊
بر اساس انتخاب  بلچر ریپورت ، لئو مسی بهترین بازیکن تاریخ فوتبال است.
۱.
🇦🇷
لئو مسی
۲.
🇧🇷
پله
۳.
🇦🇷
مارادونا
۴.
🇵🇹
کریستیانو رونالدو
۵.
🇧🇷
رونالدو نازاریو
۶.
🇳🇱
یوهان کرایف
۷.
🇫🇷
زین‌الدین زیدان
۸.
🇧🇷
رونالدینیو
۹.
🇩🇪
فرانتس بکن‌باوئر
۱۰.
🇪🇸
آندرس اینیستا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107668" target="_blank">📅 12:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpS3y8SJFrxQcH46YpSuh_x86mfD5Je8Vz-diVVuXXXDfytM6IKVFA6N_yt-H-N5vuGZg5E44ljzj6mU_9FF2QTOZn0uHPxvf0FssXvePVXb-XduViOQMekelHOy5gUo3IcvW7Yu949WakuMin657KdMVmcRNKVaEek_zNBuV4re1g0khSmP6irxj8VRSmQjaf8JqQXozgQbsrrIDj5bgZI-vi3SDs1efaya4kDX0KnL8dteTSo4NihEyV6rEq3_pr2xmE4fm__w7njLBxvdx8ly6wgiHtjBMdPmz79GPQK07GEK9Hktj5lBjS8e-H-OXy2nf6S71cQpWYJ8x6lhkAs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721222cb0e.mp4?token=OVLfjw0JAxgsV_Jq_N6EfSoEhIoohRnnrI8-fg-E8FkaBM6iU75yH5_q_3620vH91WUI7zVg-thSGx0xwQ0gL7mw8ZDyk5ij8ZJojDL5GbUxOxVM4JtSIN1oa5OHBhniWx9UXbtsTS-z_zk0g44OhH7POTYSD9A5a6pmiX7zYA9CaqtmMR5mEswxgcURYQ7I-AfzMIZpScqTvdFPrAJJ-WUjmkG3chf2bRjHz3ODaUsWWa9uXjNuwRfHhrqNkSMXb2kOlnRcxZJcTySDy6YRSuaDUolTS2tiR7VmqntyvbV4c7-LcYx-5JNb6G32pAR0cmZnR3c9XYWqGy9-wRvXpS3y8SJFrxQcH46YpSuh_x86mfD5Je8Vz-diVVuXXXDfytM6IKVFA6N_yt-H-N5vuGZg5E44ljzj6mU_9FF2QTOZn0uHPxvf0FssXvePVXb-XduViOQMekelHOy5gUo3IcvW7Yu949WakuMin657KdMVmcRNKVaEek_zNBuV4re1g0khSmP6irxj8VRSmQjaf8JqQXozgQbsrrIDj5bgZI-vi3SDs1efaya4kDX0KnL8dteTSo4NihEyV6rEq3_pr2xmE4fm__w7njLBxvdx8ly6wgiHtjBMdPmz79GPQK07GEK9Hktj5lBjS8e-H-OXy2nf6S71cQpWYJ8x6lhkAs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
📊
راز شروع بازی‌های پاری‌سن‌ژرمن چیه؟ این آنالیز بسیار دیدنی رو باهم ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107667" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oig0a5NXfPc8LunAFWz6qy-mHOA7P86ebUjngltzd7v7NJdCcWkNCQo-v0RZpmi4o3L8-kWSu7j2g_IeVLbQB9gR7avo_9c12TDyoom4Mb5Zgh801Jw4_9DkDcTkG43XEvFVPIONE-JnQiNwlGwEZaefLoV5kvNRaNMoN5e_WNTd1mDnuZ7n_D5ZJZSvb_8_DFOUTZJJxP5h3RY0xXk1p-U4ja5v6In82h8WtkVnOYQDsFs1TO-FMm45Nq3WzPUKnT7Tk51OFqHNpuIWXlaWPyPLWZleRlkEoVtcJcuG1uaA3_Vt3cQWD1TcFm305A7nnj8JHAQfmX-FZ5wYayEJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تیم‌ملی والیبال ایران با برتری مقابل پاکستان راهی فینال بازی‌های آسیایی ناگویا شد. برنده چین و ژاپن فردا به مصاف ایران میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107666" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy8OMKvMMUtpXtVutS7X-7vh8yHWv1b9KwQJk4t3-PJiKXH7xHcRNDfvLNo2-zf6pVmtbZ49T05v515r8TiedA5obyOU-gKABBe13EQ5RQqAQh92hVX0MVUZTInRz3XH4uToDXtckVC25pdRxzyVSpcRmQpzmOKnof6LXhHILUFYCtssT-flj69wIWHnhyiukEes5a6cDs4M1jhnqq4_gFmzn_KuZHJiFYAv9HGm4CgUBbNG5dRQohh85q5iglk5zjxUm26jK5cHDN7V4469wXi6xN9U_EuNaIx4w9aIzTS9Xqbd9HDef9Vh-J51EfBBNGG5SW9_XqhglYjJX8nqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال نباید فراموش کنه که رونالدو عامل کسب سه جام ملی مهم برای کشورشون شد:
🇪🇺
یورو
🏆
لیگ‌ملت‌های اروپا 2019
🏆
لیگ‌ملت‌های اروپا 2025
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107665" target="_blank">📅 11:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SelWqJWFdwcxEqBvdxoHPhCGFTfJyYwTBw6zbW3qXWApG8eXSkWDR-7w_giPasSjNDjMgWWGR3MoLFAunx8GMZ9b7CF6GrftYmDpFM_ibAK-UYd7hTCkCMXYTFAaYn3AVTKwvptavXrmKAIgoUEijhjdPg43OntGnpQ6uwX5LeHkIuEeDWpHszpLIrHNSoHKaIPM7_zebUOygvj-lur4PTd6F8ZTnDxZTcsqX1Gd0A0cPkEUon0ZIrMr0v5HKLEDedwloFSw1xr9P5jmhrPz56Sr0tnnlcqQPKC2bdrxyvPRv7Zk9YRTkbky-2qyosWV5jYcbg0HdD158tNZTDWY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری یاسر آسانی در کنار وریا غفوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107662" target="_blank">📅 11:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312a800413.mp4?token=J07r3XLg6s79B-bBTxY6o9SsGSHWoU2-mfxUe3jgW8e_Ym07yn2nBZd4J8jrXs0P98eNu7bVQ0IvOeTAfTnaS5Wn4TgiuxP_DlNSPZ2c7v5R91nbRFK0FNd-BGI-dHuqO2YUZCj_YNc0X7rutmP9vAekXJ5KzyD-jNqrU2Lrnxl-kF6h6HwOPbtV8q7Fi_43ahZabL0VSPJDcseZpfiotZV8tVISWKIIHYel5qJf9oYtWDi1rpu503OHMWq_NtuIFkkBmdUSDoHK1YP-eIRkbjTTGzR_gpkjNm7RytDwlKgMUIkAyGqLDjPOxkZQ0dNbdReEnAHgeniGWhLhkLayybznF7Y_Cw4kKEWbKkSN-oDjev7__Tqmar6VsihVifBu1ULODtQR5cPlsdKmNRiDVphsnB5jaNZrxC4Q72boS6bAk5LI-3VgPINBIVeBjT4C3cCmGCiaglNqPaUUEmxR2IT8VA2HOkC-ol-0IPBM8TTstNg_qHO-yoO_2s91we63n98oaFo5TJjRqr4f-nBYHSxYmOuLqudP5vyE3ENhndTrH1GfwYD35skFsonCTorGseWOnVdgfAPyejir43aLaaceT1bQDA77oA7nwKjVN8gw8_79JPhoW_6gMDwRcLxI3zqcChcqrl85tP1ttigcH4b4J1ukWN9ZD8pKGRTBXXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312a800413.mp4?token=J07r3XLg6s79B-bBTxY6o9SsGSHWoU2-mfxUe3jgW8e_Ym07yn2nBZd4J8jrXs0P98eNu7bVQ0IvOeTAfTnaS5Wn4TgiuxP_DlNSPZ2c7v5R91nbRFK0FNd-BGI-dHuqO2YUZCj_YNc0X7rutmP9vAekXJ5KzyD-jNqrU2Lrnxl-kF6h6HwOPbtV8q7Fi_43ahZabL0VSPJDcseZpfiotZV8tVISWKIIHYel5qJf9oYtWDi1rpu503OHMWq_NtuIFkkBmdUSDoHK1YP-eIRkbjTTGzR_gpkjNm7RytDwlKgMUIkAyGqLDjPOxkZQ0dNbdReEnAHgeniGWhLhkLayybznF7Y_Cw4kKEWbKkSN-oDjev7__Tqmar6VsihVifBu1ULODtQR5cPlsdKmNRiDVphsnB5jaNZrxC4Q72boS6bAk5LI-3VgPINBIVeBjT4C3cCmGCiaglNqPaUUEmxR2IT8VA2HOkC-ol-0IPBM8TTstNg_qHO-yoO_2s91we63n98oaFo5TJjRqr4f-nBYHSxYmOuLqudP5vyE3ENhndTrH1GfwYD35skFsonCTorGseWOnVdgfAPyejir43aLaaceT1bQDA77oA7nwKjVN8gw8_79JPhoW_6gMDwRcLxI3zqcChcqrl85tP1ttigcH4b4J1ukWN9ZD8pKGRTBXXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
عشق به مارادونا، با توصیف آقای گزارشگر
🎙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107661" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
