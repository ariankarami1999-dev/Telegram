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
<img src="https://cdn5.telesco.pe/file/NlRYHpfbA9eTs8I9V2rRcsntGC62IRydWo03sd5Zt6THfZ4NUaU_peuzXCT7svTbwHxXR3tc-ad6tUBsaWwp6ZGQwVArUloMGg8-C908ojgR3vG7kVuzJ7XTheoNCyYTvPeydYmyDGhoJ-VaWE4Cc-I6o3kqMwRgO15HAxAj6dMPWV-x9WRD5Xvfg__z6D_eit_stShGKDM_XnOKb-93AlG4ZzzbP1qICZKZNbRMETzYwREHiFlSC_IXNFrKL4KQdGzZRBc6_twA2zSCOzNQlMn63LDObI4Be0e1FCLa_OXBX6bN9PnkL6wbHk7ZDsJ5SHpnUMTayf73Bve2o_EhCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 723K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-95442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c332525e0.mp4?token=WnpE7l-cPDkii00-pbBykuziOrzuwh70IG5rUG23Wj5MFjxc-kNdt_HgPC1aJ6N-cE75IH5ZJmGs85fdq6tIXy8lzx2C65qDUWnfBxdFOmEFM8w_hlyVRQchNDMBVDgp25cdkoFe3VUnZGRGhkeWmTijdmAbEnQpMrazC-GpQwjQk1DqgP9JD0Gf1vol5qSbPBVjAAOkxplhXMrqieiq82IEcHBsbvOycsDfDVHRyM2xTJfJwt724_RHmGNIpV2vtJbjfnlwRJOWxRd4NxgwJfEnm2Rw8o3SRWCqiFESeGxjXwE1YtAuioDjNl5JXNjG7lASwosrqjmXcs5PA3RCmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c332525e0.mp4?token=WnpE7l-cPDkii00-pbBykuziOrzuwh70IG5rUG23Wj5MFjxc-kNdt_HgPC1aJ6N-cE75IH5ZJmGs85fdq6tIXy8lzx2C65qDUWnfBxdFOmEFM8w_hlyVRQchNDMBVDgp25cdkoFe3VUnZGRGhkeWmTijdmAbEnQpMrazC-GpQwjQk1DqgP9JD0Gf1vol5qSbPBVjAAOkxplhXMrqieiq82IEcHBsbvOycsDfDVHRyM2xTJfJwt724_RHmGNIpV2vtJbjfnlwRJOWxRd4NxgwJfEnm2Rw8o3SRWCqiFESeGxjXwE1YtAuioDjNl5JXNjG7lASwosrqjmXcs5PA3RCmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
واکنش جالب مسی وقتی خبرنگار در مورد بهترین گلش در جام جهانی میپرسه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/95442" target="_blank">📅 17:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95441">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMXz2mSpOvH8mcBwBZg-ArB4KpEC4nNNAHbFQlVP6N0L0IurdkbD28Ma8mzcjCw9Ruo4aN0A_l-Nd9GYUt69hiyAQFmmBWqV7KGrXtjT68pCHWkLD-p7xVMEFSQue1x52nvbhAD9Vz0w78sJ67FE_QCED8612agZ-3rBbBQ6v0KzYd84aNwU6eQXVD7xX3Wyy_8ApAaTya6vpdxyMmzgzElUrwbWvh0s_3Et6-YSrVaigqzCgiSguy-xTwWSQvaKLnCBNmGVS6NRX9-SKwi1MFMdM-SosG-j1hgPoqFdd4CXYPUh_aMp3DHep6MbElgAnBF-WYICSXFHb3F9saVT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتو اسپورت:
یوونتوس چند بازیکن از رئال مادرید را زیر نظر دارد.
دنی سبایوس، فرانکو ماستانتونو، فران گارسیا، گونزالو گارسیا، براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/Futball180TV/95441" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c26ebe56f.mp4?token=j45ay5LmYC2GR6vuVX5jE7PnS32TlOy4ZeIBFx13wVQKl4H4qldtMlpgxMhQG3_vS9n6K1YWiLYm10neu6vgCED6M2tH0JRd7nfHdO1Pfz6pMBjUdkVNINwi0JNFnGA2I6FXAv-RGDn-V7H0FOJ-tjaCLzv4HjZTkkU-AY6UOA63WvV2HV5-nsdPkd7JsZo_Gb1jnOpyP4DhQC3dg4PLX_oEq7xbVv73UQ_ukLkfs9scs5nAkvaPvDv-E-2mI7YCafZzd_in-BJjzHgIddQKxEHOqzMVDsP_KOCTXhQBF-3R4VpcAay0Hv_kcrpa6Ob2wzbLbH5n2Gbft0PX8_e4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c26ebe56f.mp4?token=j45ay5LmYC2GR6vuVX5jE7PnS32TlOy4ZeIBFx13wVQKl4H4qldtMlpgxMhQG3_vS9n6K1YWiLYm10neu6vgCED6M2tH0JRd7nfHdO1Pfz6pMBjUdkVNINwi0JNFnGA2I6FXAv-RGDn-V7H0FOJ-tjaCLzv4HjZTkkU-AY6UOA63WvV2HV5-nsdPkd7JsZo_Gb1jnOpyP4DhQC3dg4PLX_oEq7xbVv73UQ_ukLkfs9scs5nAkvaPvDv-E-2mI7YCafZzd_in-BJjzHgIddQKxEHOqzMVDsP_KOCTXhQBF-3R4VpcAay0Hv_kcrpa6Ob2wzbLbH5n2Gbft0PX8_e4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون خاطرخواه همیشگی مسی هم دیشب تو ورزشگاه بوده. کسی که تو بازیای اینترمیامی بارها به مسی گفته بود دوست دارم
🤓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/95440" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3UEQYmb0u0f4C4rajWCsm_Kd5cygkRor0JKvwcyyllhdYK4YezZytCCCmskdYcbUKcH6BKhGq-I9of8cRzRdn-LvQzvIMHqB_j_N-1sW5VDOs1IOpVV9Coi3NkWkc94gzpqRWpV2B7N9hQvI1LB3v1BLyIpoxTcwnLTVVEs7w0k7mcEOz5wTT0RZXoM3dwAFr2I7JGjrKkKZTM4kfxZdR5ZgVGTPA-pGNoZn1Hi7h4NmAWtB1JjVwsw9cpWm4fwV3dtMY4csYreZBOR9bE4vgERQ2qwH2_dCuAJwsHNbZAXYl5GSIA8v_2S2zd0ue3fPgJni7Ph56nyeIH1eAaBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اروگوئه تو 10 بازی اخیر بدون سوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/95439" target="_blank">📅 17:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ba609d7a.mp4?token=a3DWzBo4h1CYA_qj0lsXXmydLrC4RVUY6lPhuLGuf6sORUiEJt5bk7lq-xXtD66PUf-qyjZfGW-43bZ6Eg318IJegAUAJ19vRZ0tvUbtRM2qPfY08ioCdyBA_pieHn4ENsvyP7oVfD4-fgTKLNcNcdGFWAsMmPRa1Ys5cfHQtuSQ4xwJZIs-VR_LLIGGQ_YvZyi7ySr6Rv9vOaieytkQvU6PO_Gyk026qCfQzN3UIHKMN2bkuxqZepl7Jxx8VQwniK3eLyv0pw-ZeJsqOzb0r4j76lLcW_IYtsKk66xo79h9YxSfSJhrXEOJrwXxmVECbgphsTxUgDSTgB46n1DzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ba609d7a.mp4?token=a3DWzBo4h1CYA_qj0lsXXmydLrC4RVUY6lPhuLGuf6sORUiEJt5bk7lq-xXtD66PUf-qyjZfGW-43bZ6Eg318IJegAUAJ19vRZ0tvUbtRM2qPfY08ioCdyBA_pieHn4ENsvyP7oVfD4-fgTKLNcNcdGFWAsMmPRa1Ys5cfHQtuSQ4xwJZIs-VR_LLIGGQ_YvZyi7ySr6Rv9vOaieytkQvU6PO_Gyk026qCfQzN3UIHKMN2bkuxqZepl7Jxx8VQwniK3eLyv0pw-ZeJsqOzb0r4j76lLcW_IYtsKk66xo79h9YxSfSJhrXEOJrwXxmVECbgphsTxUgDSTgB46n1DzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ارلینگ هالند:
فکر کنم گل زدن تخصصمه... راستش مثل خیلی چیزای دیگه، من فقط توی گل زدن خیلی خوبم و خب، یه‌جورایی خوش‌شانس هم هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/95438" target="_blank">📅 17:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EwsZTjzjI_WmVS_DOfMaA-EebcFB_-zkM5c8puovIAZKze9sZ69Bc79UUJVmVkdYjqCDRXHDjuH5nJYQnIfNuRl-4hO-M6fVLReiBy7Ksup3zq7gO5bfWmH29Fh6NJFwJSzqx1zvyKTmDZqXoVGeQ3jpgmzQQk-6RKmq-e7c06bm-Igz6HfU5hbUmZATY8uj0nC7a6ggXFRLsF_4xY8lrv77YBBRjLb_wUfrv-zp5eOcKAR58OSU6K9Lv4OPTPZFztmuVd4cs-fNW3x2dOyQG5T_8tHmQ1RjIRU7QZjJXWvPZmwGV5gbQ_x22Jx3gzhoCE-uU0sBpEiGb_e1zwRZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⁉️
مطالعه‌ای در SSRN با عنوان "هویت سیاسی فراتر از سیاست" نشان می‌دهد انتخاب بین مسی و رونالدو شخصیت را بازتاب می‌دهد. این مطالعه شامل ۱۰,۶۶۱ نفر از ۲۶ کشور در آوریل و مه ۲۰۲۶ بود تا بررسی کند این انتخاب صرفاً سلیقه ورزشی است یا نشان‌دهنده ارزش‌های عمیق‌تر.
🔵
نوارهای آبی = تمایل به مسی
🔴
نوارهای قرمز = تمایل به رونالدو
👤
چه کسانی مسی را ترجیح می‌دهند؟
◾️
ایدئولوژی پیشرو — چپ‌ها و پیشروها مسی را ترجیح می‌دهند.
◾️
علاقه به سیاست — کسانی که به امور عمومی توجه دارند.
◾️
تحصیلات بالا — افراد با تحصیلات بیشتر سبک تیمی او را می‌پسندند.
◾️
شخصیت متفکر — کسانی که عمیقاً قبل از قضاوت فکر می‌کنند.
👤
چه کسانی رونالدو را ترجیح می‌دهند؟
◾️
محتوای کوتاه (TikTok) — کسانی که تسلط بر محتوای سریع دارند.
◾️
اعتماد به نفس بالا — کسانی که به خود بسیار اعتماد دارند.
◾️
گرایش استبدادی — کسانی که به رهبری قوی ایمان دارند.
◾️
جنسیت زنانه — زنان کمی رونالدو را ترجیح می‌دهند
❌
خلاصه: مردم جذب بازیکنی می‌شوند که تصویرش با ارزش‌هایشان هماهنگ است؛ مسی نماد آرامش و تیمی بودن، و رونالدو نماد جاه‌طلبی و فردگرایی. این ترجیح سیاست شما را تعیین نمی‌کند، اما ریشه در انتخاب‌های ناخودآگاه شما دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/95437" target="_blank">📅 16:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b088ab51e3.mp4?token=AU_5B9rIOn9yJlAarBg9lXMuj3OcB7DUA8CPlDly9vAMtc-j526r0lJFbQQBv9lugO-q9iohT7WaU10kTZ8TFltVw8R2FAh_HK-BwsP9U3oNx7DESjGRXgwMPzZW8Z1OPRA0DzO96LUsrJ3TeFgqWOT8_9cTMGcUicwlCjopMpiCrSZgsDhPzuou-R5EZrG6z0EaFPsXfq378CYJeMZ4itw_U6XYeO7W4KU8EXsn--ElcqeHzoA6giUxTJUyZHxucqObWxqjdjKTTG5v4JucIjZQnr9QOhEsF3r95NLZh8ZYr2B1kSrVWO-eHNBNIrKLypbNKRE9V8HeGZdqpCbCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b088ab51e3.mp4?token=AU_5B9rIOn9yJlAarBg9lXMuj3OcB7DUA8CPlDly9vAMtc-j526r0lJFbQQBv9lugO-q9iohT7WaU10kTZ8TFltVw8R2FAh_HK-BwsP9U3oNx7DESjGRXgwMPzZW8Z1OPRA0DzO96LUsrJ3TeFgqWOT8_9cTMGcUicwlCjopMpiCrSZgsDhPzuou-R5EZrG6z0EaFPsXfq378CYJeMZ4itw_U6XYeO7W4KU8EXsn--ElcqeHzoA6giUxTJUyZHxucqObWxqjdjKTTG5v4JucIjZQnr9QOhEsF3r95NLZh8ZYr2B1kSrVWO-eHNBNIrKLypbNKRE9V8HeGZdqpCbCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
حقیقتا مسی و رونالدو چقدر خوشبختن که چنین طرفدارانی دارن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/95436" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbf8afa2.mp4?token=EnUjuUg9_HL7Xzc77gP32NERQ2ku3C6sd9shoY_LLC2Hgq1BXNICcwcx30_YYtykwX44T7-HylX1JByfivZ5eVw5ZZ1HLqbFr1hhh1Txszpf12f-5KQjYpO-VBow-xolmPZHLvAhTqSK6gXo8nnrp_sKaItWk_DLfEwaQh2ZoloTBvZoDkCrDKBKPnuafZk-cDjmxMvCfXOVYdzqMh605GTOItLYNbGgJfQJ5n_OavLA-ZCNLpjx7MdiT8yzO1dtt41rJYGRlmJgrJ9To0SfnS0fOdeJGsouVbgy3YeHzaxi0UyRX59LzYc02WuUZ_1wpoKqSw8833NT0zxBSixVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbf8afa2.mp4?token=EnUjuUg9_HL7Xzc77gP32NERQ2ku3C6sd9shoY_LLC2Hgq1BXNICcwcx30_YYtykwX44T7-HylX1JByfivZ5eVw5ZZ1HLqbFr1hhh1Txszpf12f-5KQjYpO-VBow-xolmPZHLvAhTqSK6gXo8nnrp_sKaItWk_DLfEwaQh2ZoloTBvZoDkCrDKBKPnuafZk-cDjmxMvCfXOVYdzqMh605GTOItLYNbGgJfQJ5n_OavLA-ZCNLpjx7MdiT8yzO1dtt41rJYGRlmJgrJ9To0SfnS0fOdeJGsouVbgy3YeHzaxi0UyRX59LzYc02WuUZ_1wpoKqSw8833NT0zxBSixVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
صحبت‌های شنیدنی ستارگان آرژانتین درباره درخشش این‌روزهای لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95435" target="_blank">📅 16:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95434">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofO817xT_EjQCZT6q29HOcL6kroQhyryI9KASlzB5hA4_WQH48g2HZY73dOidy_FhH0mjJ9Qm5Us1c9feux109r9lV1nbMmIZJATm8gDCG3j226Xeky-kH3j8yTFUqQ5TMgN17kaue3W3UxiMS3rl_tl1EL-HMCuwF0JBAZFSAhmrPPUMUlIV-EbUerOnNoI350GBebugizlDj8Cd-WBpa48dDhzrbm3IZj5JVyHrIEPK3DQSLe9wFKI97J3Fv-kNiE2eOGAgdXVLGV6S7wuU8TyYuhG62JjiLt8XGo_mUkCSapH_0A50EEU3ZOpSfU1VBkohsAhAjPim6Z3WSJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نبرد امتیازها در «همراه من»؛ حرفه‌ای‌ها جلو افتادند یا خوش‌شانس‌ها؟
🔹
لیگ پیش‌بینی جام جهانی در «همراه من» وارد فاز جدی شده است؛ حدود ۴ میلیون کاربر در این رقابت که جوایزش شامل سیم‌کارت‌های رند ۹۱۲ با کدهای ۱ تا ۳ به همراه گوشی S26 Ultra برای نفرات برتر، یک میلیارد تومان جایزه نقدی روزانه و قرعه‌کشی روزانه PS5 است، حضور دارند.
🔹
در صدر جدول، کاربرانی دیده می‌شوند که بازی‌ها را به دقیقه ۹۰ نسپارده‌اند؛ فرم تیم‌ها، ترکیب احتمالی و نتایج قبلی را بررسی می‌کنند و فقط بر اساس علاقه انتخاب نمی‌کنند. پیش‌بینی دقیق نتیجه، امتیاز طلایی می‌آورد و می‌تواند چند پله جایگاه را جابه‌جا کند.
🔹
در کنار پیش‌بینی‌ها، ماموریت‌های روزانه و بخش «تیم دیجیتال» هم به ابزار صعود تبدیل شده‌اند و صدرنشینان با سرعت در حال انجام ماموریت‌های امتیازدار هستند؛ امتیازهایی که شاید در نگاه اول کوچک باشند، اما در رقابت ۴ میلیونی تعیین‌کننده‌اند.
🔹
همه این رقابت در اپلیکیشن «
همراه من
» جریان دارد و لیدربورد آن لحظه‌به‌لحظه به‌روز می‌شود؛ جایی که هر پیش‌بینی می‌تواند چند پله شما را در جدول بالا ببرد.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95434" target="_blank">📅 16:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95433">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔥
خیابونای بوئنوس‌آیرس آرژانتین هنگام گل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95433" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95432">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9ke4DB1B9MSl6j768a06QYLrE82e5pDRmeJIuUEp1JEqQQt0uqzuHB8F4ZpXgxBmOHcbfn3lgo8nyAPbkfyW6vk9WgdWGc7WFzTW9P31TDMaIzvZGmcT-wVKwdThONGxEn2AAN1sMWn0WMj50qN5yYioHuFzLylfyKc1n0O8-mH_TuLFsPb3kyzFA8rEPVPTIXrKU8X3OwYRsMA4FlHxvTp_uGOu2A3DjIb8lGsKABdG77gI4BrcrtD3uoscUhJKdpahc9E4ca2C57uGOLDND61iCmcbG2J2kt-mgc551ncxpiu3tb1boS3CgiWXFtUI-ZyP8CGQ44-Q0sN-SDmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇬
🇮🇷
#فووووری
؛ سیمون مارسینیاک لهستانی داور بازی ایران و مصر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95432" target="_blank">📅 16:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95431">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgDgzarS2tTwOhYd2nnZsN2D2ZPufYFnlmQhr_zWAhH6GynPPoT4sTSSBMpR1it1tnaZVk29PiMWr1Aa9HuepcSlilRSnCWdfAJjf0QNxDj-qJR8LvVqMGqZygxLgGWfdsJu5dQG_JyslmJxcHecpW1pgKwfnpZa-EQ7kSM8zaLn2zaTgmZJVEKug7PRhHoJ7sCXCDDFCr9VWOYmWgT9lgnhGwEQLiYTu2NXG4n8_HS0R0NBJW38ExFH0fOID0zIxWvDfcQkhY0YP3hyETfbVHsLGetth3cAXeB-U0jyslTD2MPi2YJtz8MN8LMWuOB62ZH53c8CsXDyoLry4vHdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
از وزیر ارتباطات به خاطر عملکردش تو زمان جنگ تقدیر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95431" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95430">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf62186867.mp4?token=XnUnRYLgHccUF-xRN8dQAq5902oyVNaBunjolbXq-qz4C566UCWJucv4bB-CtJeVODwXALdeK7S0KMPnLi-0zQ1R7kBNCQNj9lR1A7AbERK3yWDlcIeLY2uQJNaxivPWxXoGLbbPz-yUFDbX0UVUI-_vhu9ZUTbdSadEEkNx4tAbrmgDqoXwLbROiWCgOKEVa8vflQKIUm4-MT5GOEny2oi0r58sJlLRbWlccfTcuysT4PDspwylsJvrpOys9qufsNoEdYV7U0wXT7AumEGTEfPfITFdE_hhunIZqLrMypz9dA_P7TAakfiQdSGA-AiafLNzKyxCKesfKYxpKFUqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf62186867.mp4?token=XnUnRYLgHccUF-xRN8dQAq5902oyVNaBunjolbXq-qz4C566UCWJucv4bB-CtJeVODwXALdeK7S0KMPnLi-0zQ1R7kBNCQNj9lR1A7AbERK3yWDlcIeLY2uQJNaxivPWxXoGLbbPz-yUFDbX0UVUI-_vhu9ZUTbdSadEEkNx4tAbrmgDqoXwLbROiWCgOKEVa8vflQKIUm4-MT5GOEny2oi0r58sJlLRbWlccfTcuysT4PDspwylsJvrpOys9qufsNoEdYV7U0wXT7AumEGTEfPfITFdE_hhunIZqLrMypz9dA_P7TAakfiQdSGA-AiafLNzKyxCKesfKYxpKFUqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید لاشی وقتی دیشب تو بازی آرژانتین مسخرش میکردن صدای سگ در میاورد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95430" target="_blank">📅 16:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95429">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiiH9XZTfnvEhMDPjfvLfYUcBLTNb_0k21A6ZLEsDJgVUkbXBHbAk841caVRVffpXmWVc_tNIiMgX7frrjEfAYx8vHqWkhwgkaPbq7n_6hV1TwDssFaMlOiBXO2HkopeC8umnl8p4xiSzA5Ovylg4fWSjDh0CzihEQG3kSUGJstLC9n-0yM1DvztIBP0Zn-btU7h7hPR_OcbYgvpJ975uJ0mpXFyTci2Wr4lDRiwBaRuz-3J5TcRnKzBfliG2g3TDQRVi7PyJ7FlPMDFy1K9g_9GVsX4LiIamp1jl6J5nGLhT7M4J92BfhaLe_FFGUGuuhmq0KpQcrVmvb58d_Rt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🚨
🔴
فوری - بیلد:
لیورپول درباره فلیکس انمچا استعلام گرفته و مدیریت باشگاه از عملکرد این بازیکن خوشش آمده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/95429" target="_blank">📅 15:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95428">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aeb7842be.mp4?token=J3oKyVyhqSIGe0pK8LnslQ7NLA4rQngJWuS3lm-sKSXDssxA-wS6rrJEmbYFcDRE2kJybXDP-DBOKOsHooC3_LvMqmyYrQC08F3_RXOl5Ecr86r3YAdFaa4PIiBAGxQpQ-_kitzMRszu0acwi-IhOCIyk9mPyPd91af62k_vXfFFdpyaOgjjF2N1RX2sYM0-EcMAjB5W6GFjZSL1z4XMcMXaxYrwulZlI50TVwrKhsFgOhAOzbMAtaOugmFY2-jBb6BIdmN-pPDcpcm1uNfeWmo13BBuKu6EC3-r-kvo2DCgCUkUKoVZZMkOyVipIWMPbC57KwexdVCd9UsP8hmr_UYBAVxDCl-Jaj9S0dOva3Tq4mEHZQQoLLX4jJ_XlR9gFfn8RqrVWpYCEG2A9QRt2USgF3ReHIppNswwByxVNND0_jYKFIbsjCtp3bDeBWCNKM9rU7MlEX1od4Jw1HuKQJ_RpmvLWhlNNipnb2TvSfF-LC2jL71PTO2j_6B-gWGu3oZUN2VQKAaMbV5wZMXngEwHX71HVgfiD3QVKQO8J27WGj_ZRZeM-miHZF4iBtQkqQJ_e-oLpuC0kOrJE8Hvy_x-mMKX016kGSYluNMLqcGrQoGlhivqs3dta_wz0Y-O0akWSdpuyZ6RhzlL7irHJZjzhEg8T2otmV5MHgJFx4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aeb7842be.mp4?token=J3oKyVyhqSIGe0pK8LnslQ7NLA4rQngJWuS3lm-sKSXDssxA-wS6rrJEmbYFcDRE2kJybXDP-DBOKOsHooC3_LvMqmyYrQC08F3_RXOl5Ecr86r3YAdFaa4PIiBAGxQpQ-_kitzMRszu0acwi-IhOCIyk9mPyPd91af62k_vXfFFdpyaOgjjF2N1RX2sYM0-EcMAjB5W6GFjZSL1z4XMcMXaxYrwulZlI50TVwrKhsFgOhAOzbMAtaOugmFY2-jBb6BIdmN-pPDcpcm1uNfeWmo13BBuKu6EC3-r-kvo2DCgCUkUKoVZZMkOyVipIWMPbC57KwexdVCd9UsP8hmr_UYBAVxDCl-Jaj9S0dOva3Tq4mEHZQQoLLX4jJ_XlR9gFfn8RqrVWpYCEG2A9QRt2USgF3ReHIppNswwByxVNND0_jYKFIbsjCtp3bDeBWCNKM9rU7MlEX1od4Jw1HuKQJ_RpmvLWhlNNipnb2TvSfF-LC2jL71PTO2j_6B-gWGu3oZUN2VQKAaMbV5wZMXngEwHX71HVgfiD3QVKQO8J27WGj_ZRZeM-miHZF4iBtQkqQJ_e-oLpuC0kOrJE8Hvy_x-mMKX016kGSYluNMLqcGrQoGlhivqs3dta_wz0Y-O0akWSdpuyZ6RhzlL7irHJZjzhEg8T2otmV5MHgJFx4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
گل‌دوم لیونل‌مسی در بازی دیشب از جایگاه بالای ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95428" target="_blank">📅 15:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3912f4917b.mp4?token=KrMx1sKhTgCC2uOp3VEcztjP9llrl5y8cktNqf2jiRBDklc7TOgApEiAd0hM91pHF5Yit1LtAoWEkPs9FhJnbdjPZp9IpY72OPE7iRyeMT5s0xa2UOaKtHQdwsp4tZyV5vBT9i2FsX_HZ7wJAcnYP8GSHdjg867XPs4vxQQnDxiYJW0_RgjG30h832AdgUHj2knvlanH-N1MWOAlcvzR4xroHsP-KwPn6CgXCmaQK4MCmANVs77_i3o8hvPtl7IDsQwvnbSCIu7ZdF5G3gRWAZ6af_xsuJpHkzeJodwGpI-vhfeotfVg6L-8-6lQTW0ER6HkFXytmGd3KAY2G-_Kjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3912f4917b.mp4?token=KrMx1sKhTgCC2uOp3VEcztjP9llrl5y8cktNqf2jiRBDklc7TOgApEiAd0hM91pHF5Yit1LtAoWEkPs9FhJnbdjPZp9IpY72OPE7iRyeMT5s0xa2UOaKtHQdwsp4tZyV5vBT9i2FsX_HZ7wJAcnYP8GSHdjg867XPs4vxQQnDxiYJW0_RgjG30h832AdgUHj2knvlanH-N1MWOAlcvzR4xroHsP-KwPn6CgXCmaQK4MCmANVs77_i3o8hvPtl7IDsQwvnbSCIu7ZdF5G3gRWAZ6af_xsuJpHkzeJodwGpI-vhfeotfVg6L-8-6lQTW0ER6HkFXytmGd3KAY2G-_Kjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇦🇹
آنالیز گل تماشایی آرژانتین به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95427" target="_blank">📅 15:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4rdun3qulRCPKGWIkH9xU2el0LYohQ6okEkWU-Dfs09dbGFmb5-IZF8xo8-19nfUOPZxc3Ke8e2extj6Nf9qUqXWVd2wknzrdk6b6R4JGVmkQqVdlYsEt59L_pDSZB8M6C4C-Vjv2UujEpFrrFhBOee5sakaYLp3BS6fL8O2TZywYUdKvh3Wys_7vRcT1KJg_JlCnX5SkAcwaLPS_nHo9xuYFP8dFbFLPOaBSetZQzdqP5jQhDtO8uJz7tT8I__LYH2T-O0ojejBNgTVOuqyB8fbzRyynLe51xXxm_xL0JTu9JBUNCsPyB0IptKf-Lq9a7zZVdcp_0lLMAFoQW-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
حمزه عبدالکریم بازیکن هجده ساله الاهلی مصر به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95426" target="_blank">📅 15:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5UyrfckzpTWkryG2LZnGhc4ULlLkUttPRhrf8d8WeH63yZUQRHCj9yWA2RtLb9dYboEolGyzYTjQGZZoCXROxwv77-uLVU-GRdc8DgdsC4M-ME-tG6L6ZrDGnlbjvWrw9fBVWnf8oZrTA9OyQM3px8Y6ssZOzPivkcPBNBHpLCzTC-s-rxemNjY7yLF6UxCsXmf1UKasj0eeCICIRiJiWo9lCq8sgZiewnwdf7GoH047m3IhB0lg50MxBGLVxa6315ntAQZOkThaiajhh-bf3EzdHmhi3ehnPuac_IuQRp-J7CQfqiSPlGwhU2e2c_06fmXZ5rC1Q3zHInbPE71Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روزنامه پرتغالی A Bola یه نظرسنجی گذاشته بود که حدود ۷۰٪ هوادارا گفته بودن دوست دارن رونالدو مقابل ازبکستان فیکس نباشه و حتی تو بعضی ترکیب‌های پیشنهادی اسمش حذف شده بود. خیلی از خبرنگارای همون رسانه هم رونالدو رو تو ترکیب اصلی نذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95425" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
تو حاشیه بازی ایران و بلژیک، یه بلاگر خارجی تو استادیوم میخواست مخ یه دختر ایرانی رو بزنه که مادر دختره سر میرسه و پلن پسره میره رو هوا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95424" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC86VlvY_W_0UyhbqQBB2nHZI02zAsdHivfrjRDwk5gLG5cjpK_ndjpJRnhezjZVTYyQvRLUIvA_egm-e8lp03XNYQS7fi8mMX7G4qOkuOLW7smMqztmalcw76GZkVjJjtir3JwIvxLzAhFqbMlUYHTyPKSz_RRRhGbro5TEEKuY4WSyGw5Pt1Y8cOtm5Dy-qx9nIaGioTjBnNJCQesxP_Wf0BfYoWZxgEqmlrX-VU-1P_qhXwI_yaBkeceeaIqPvyYIjeBaI0eMP-IKkYT6IWe5Pcf-nhepufXcvoypLlF3R45OhbHprXKB2t5lg72JE9ZqFslwlOrIPUkZ0Wc6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
آربلوآ با قراردادی سه‌ساله سرمربی فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/95423" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5r-vCPBASfkgC-9osaUEfVVceCnVwG3Y5m5JnLI9T-litllrz-fgSCm5jP9PHL403rVkv5gD8tnH466Ja8Kim7SLmTm1jFGiLcspk6_hKcaQuWKW4GVDlX5TyyhglCeyPYIr_c7-dE1sgsxaWCd_DNLo8OuGZHRJ_VSzVoqhdKDsej6rep-ZDHMbB98CGr8QTjQLPcZ10qOmuwzyMePJ-ztoiGcMVnuHnIeYKoAfgBe2vjZWGJHn7pdmNHTBtDw5xsTsU7TcYXt3T0g-V4oyNGPUtyoAxD3grw6ir1BZT5ae5Yo158I1_-KWLwNY0DeuvykxwKBUgy3T-nMDIJH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ستاره ها حسابی خوش درخشیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95422" target="_blank">📅 14:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
خوشبختی برای خارجیا يعني اینکه آخرین جام‌جهانی مسی رو از نزدیک تماشا کنی و لذت ببری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95421" target="_blank">📅 14:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS-d1vrMxt6ISQ9C4wxKc6vQKyYx_xUrlmcfERQNdRlklxqD1rC_ZsiN95mY22OM_3KryctMuErBTQ4Mn-IsnNLhTLYbl5-FH3CTehqj6Khb2SmHu4N1a9Vdk-8YfpjMAH8MICUjw8vT2-zWF79InMp1jGk0d0khkT1yP7l1cSmuz4pSEHQOBYMu6mCq9zapIBmb1CyIjTcS6gxN6mtDX5yXe6lnH773E2-swq_3ztfwgN1NJodES0wPQnXUDLHVXx9uBgnqmWFAwGucPgO9VvL9MNK2dMyPIn9_vnWrUdVhXJF3Z6vxRQCxGO9ol9CguuM5FQLZTzFKdwLsg2XcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دکلان رایس:
ما می‌توانیم هر حریفی را در دنیا شکست دهیم، اسم آن برایمان مهم نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95420" target="_blank">📅 14:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raApuMSaDlgjBwJvKFDL8gpFitW7Dfd7MG_BFfzVI8wgCPHD38qI9PNqJVmJ0pR-F5UcYr3zPgJw02cFk6XOxQxv858WJKWLNGVx22FkjoVRywnpjNIDW65AGdybxW0Bct5KkfCcW5pUyD0cimPa77J14tvIcDIWO3VfBVvgqhA8GH9W8HRw47mbI3FumeUsY0ZHyoGZfW2H8FR3x7DON2fC_LDtAgHitxH6EnZE8DskUuTrC97LyLkf3DkDo14nD86JbH8LXf-RVTCsxArhJMs0v3DxZfZ4Mt19vJAQigQHD7a7UPCWnbBpPfMtVeyxsUdJhIoxwajVpn94a26tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
آاس: انزو فرناندز به رئال اطلاع داده که از طریق وکلاش، تمام فشار خودش رو به چلسی برای جدایی میاره و مطمئنه که فصل بعدی به مادرید میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95419" target="_blank">📅 14:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95418">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLp0WtFb2ekjA-Irl61DD7bqvNbdPJ7qotUZbcJ09AsOOx3CT7vN8VITCZSejL9EnG7cRHqMT62rKrAZS7YhRSdzrmd5PG7t7jNbYA1_XOwKz_lHkJvaSfa3E4hImLswVaDWeas5NHIflLKRsOY0eMwNIpUI8T97EuebVnAxVSxXN70EVQVXVAkWI3a6fVFlaXrhWOW2cb9kHxei1y38YcBeQW5_3xdO4HzNohRI3KyxP5BKYk6RG-79oyLAwmWKRA7pM07mqX8SAePbMIVrrJyQV2ZaMLu922mZzy6GglGUdGCp8DESEmd9RwwCDD0AAFnMGTHxKOdAQkQfBIMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ منچستریونایتد در صورت دریافت چراغ سبز از رئال‌مادرید، قصد دارد برای جذب شوامنی به عنوان جانشین کاسمیرو اقدام کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95418" target="_blank">📅 14:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95417">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a7dac311.mp4?token=kYJcP7oAf3IM3BTRSvGDENPDx1He2FXa0R938dseDhWoNEOPCygUp230vdYfEdcKu2YXRPp58mxHf3yGa-eCcYTH04hpdT1-N0_BbFKJmtVihaXLdTF3yWWT6XRUVPvbWcA-4e3gy17dAmSZ_0tfo1giKPPgU7CxvY_w_wryEwzWrfco_ypmhcWswax-zRe2Zk-jLc56aGkuWyLI9LFqS1zDDSAeZ2aVmJXEYCnC-sfzUsSMY4j1jCTVQYnBJzHhKBcvrAALRL872vl_9oDKg0S_goA00KL5RVQ3ph1Uc-XW9rBvAQh0hZLyaZcBrkF8rtBhYBHXb1wPY_Pi34viGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a7dac311.mp4?token=kYJcP7oAf3IM3BTRSvGDENPDx1He2FXa0R938dseDhWoNEOPCygUp230vdYfEdcKu2YXRPp58mxHf3yGa-eCcYTH04hpdT1-N0_BbFKJmtVihaXLdTF3yWWT6XRUVPvbWcA-4e3gy17dAmSZ_0tfo1giKPPgU7CxvY_w_wryEwzWrfco_ypmhcWswax-zRe2Zk-jLc56aGkuWyLI9LFqS1zDDSAeZ2aVmJXEYCnC-sfzUsSMY4j1jCTVQYnBJzHhKBcvrAALRL872vl_9oDKg0S_goA00KL5RVQ3ph1Uc-XW9rBvAQh0hZLyaZcBrkF8rtBhYBHXb1wPY_Pi34viGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
خونسردی خاص اسکالونی موقع گلزنی مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95417" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95416">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaS49AT1ssMtRHnGAD4pmCFW_NGWi2OnEWaALl09gp9BlNNa4xnGrpiQnX9Il-Ce7bffQ_bvXhGnFwjpcyBTd6WPxD5DtgPKyyfQNjzcgpL-vdEiWL_2txnEh2_SyxJ_utxfiSU0LFOs_ZMvnaseUGYsoPJPowkOSBz4wSrWW35C4J62y9cU__2bEoh1ilttYdTCBxtSkG85ffqvmegijZKQP38U4k_DXla7lVsnYwCEIzJ0UNm3zPFBWs1Yk-15OZNgGT1u3Xr3x9UUIpo9bXTZrStWayNYxD826_KvzKyAUenl7EBZ1P0DaWuQ5gv6URjFb_l4252r2YdoV4Syjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
خبرنگار رسانه بین اسپورت در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95416" target="_blank">📅 14:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95415">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTKWud0soaf-CiURftqHx0EBYsxhJY-6H0h74tRQzPN0r6SxJnfplKucwCO1-lXobyXcUhtKks9EMrGkkaUlX8gejTMjbwO_7BT9AIB16jZOQxOT8-tDRmrv2ihzwoUh246ifIklhOvyrv4826J_My99n4eGABVntcvlKBBjLao8PjUZC8DRcvz5vZVww7lzxDOCviHJRu6airZxVEdgHjC0zJXxZfJjb09K3X-U6jw9tP3I1Ly5GzKRk67Pj3qV0ZgBTCSC06zGjZbhJLRWmReYgoxU92SIj4HTqjwy00Bh-eQVKKtHLLRL0GnZb9raUpXu8PS7fIfQl9BDgNLnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🤣
هواداران خوشکل عراقی که باید زود با جام‌جهانی خداحافظی کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95415" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95414">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCdKnjnb1iWlDNr_10r1dTF8_w6BTMkbHNYN_AEYC77qz8ZKe5tVscXpNSfizg2cpgA2Pcej2IqJvuIabJVcGhWiK-9omtjfnh3xBeyLLivL1kMkeyGpnKwQPRYMJQBPVQFoAn1_g6kqp4zmSFOp4NoQBXYH6BDO8HP2x6Mu6eloVXMPYQ0rcR6xYoCIyZzipcZpVkC7GTr0HUeo6nmhRA3lcE0s_QqTVbPxE7JJMAKwwJCf4Ae8f9rShcpaxB8o78BOLY0wFG6d8O1ZNgWpGnXaeoNj8uSDpzz-IpN0cnFFXn2r70lgtFypKeFUYEg25B6uxB8Dq-Ri-JedwRSJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
وقتی آرژانتینیا با بازی مسی ارضا میشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95414" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95413">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95413" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95412">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=aq6wS0S24Z5P3BSBy_GB5VdAECzJ_AMG42izD3_kdgwcCahMuS93C4IIHrdD29oKlO7DlGnHdUS7K9sZEVYruwMFJb1upknODrBP-BkAFOSFBApa9V7JDmFcj2FevGHsb3jx_2aK4hxwODE6T9nR8kNAiQXz_UwQud0K67r0VI7_VNhgsjDy4JOwRKxvpcrqc_TyRT0JaPaV-AeVYNrqoMZMpMTcEnsKdtybucS07xpVRt6u7eIaJIAIy41pyWcRsYemoAHWR0aMYGn6Kbgq8dJRj5PBR6Ilz-AKe8mXYWlrMWXtbwuOPfN-BHzBA82HzA7C5Q5-zib-4q7D_9scuGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=aq6wS0S24Z5P3BSBy_GB5VdAECzJ_AMG42izD3_kdgwcCahMuS93C4IIHrdD29oKlO7DlGnHdUS7K9sZEVYruwMFJb1upknODrBP-BkAFOSFBApa9V7JDmFcj2FevGHsb3jx_2aK4hxwODE6T9nR8kNAiQXz_UwQud0K67r0VI7_VNhgsjDy4JOwRKxvpcrqc_TyRT0JaPaV-AeVYNrqoMZMpMTcEnsKdtybucS07xpVRt6u7eIaJIAIy41pyWcRsYemoAHWR0aMYGn6Kbgq8dJRj5PBR6Ilz-AKe8mXYWlrMWXtbwuOPfN-BHzBA82HzA7C5Q5-zib-4q7D_9scuGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95412" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95411">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc538548d6.mp4?token=OLIHxcooOp9le98DDX7hDRhR9OJIRXzZqxtt8nWol4lexcFeb8EUym5cUiwTDO8o2xApdtfB2-75rlAGfmugJZSOfV2zopSwS7lFLUK5hpSpk45qQUIK4zB3y8zfF__hm-SjnDWRQIL3rmaREhZLZ-SsmkIP2CtXdpYJ_9342hrfY5CYf16JpCCY3vkcBYLUDhHJBBAByM-T1vN85MrOSPfpsVazcZS1jwmWUps8TWvmZ94nvMnRetB4Pv6y7foAh55dil6rZovZG5v75nl24e968nizKwJ4fG-YO4-eab_KfWaN1oi0_1KENWstY5pZh2zhBHp4wDC1Iakw9zU9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc538548d6.mp4?token=OLIHxcooOp9le98DDX7hDRhR9OJIRXzZqxtt8nWol4lexcFeb8EUym5cUiwTDO8o2xApdtfB2-75rlAGfmugJZSOfV2zopSwS7lFLUK5hpSpk45qQUIK4zB3y8zfF__hm-SjnDWRQIL3rmaREhZLZ-SsmkIP2CtXdpYJ_9342hrfY5CYf16JpCCY3vkcBYLUDhHJBBAByM-T1vN85MrOSPfpsVazcZS1jwmWUps8TWvmZ94nvMnRetB4Pv6y7foAh55dil6rZovZG5v75nl24e968nizKwJ4fG-YO4-eab_KfWaN1oi0_1KENWstY5pZh2zhBHp4wDC1Iakw9zU9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇲🇦
هوادار جذاب و خوشکل مراکشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95411" target="_blank">📅 13:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95410">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎙
‼️
نظر مردم ایرانی ساکن آمریکا راجب تیم منتخب ایران. مصاحبه جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95410" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b6ab3616.mp4?token=Wh44oM7nK0Ylfdm4HNn0TkC5Hx-UqEBlsoZfAaOjkmCtTePvGDqUgTaudRK-FNR1KKplZJRTcvNtYXDMhnZuK6tlJR6Rg34eBVYNgk01CPEKMo-fQE9ukQ08-kE86mrOzCUkOtUGsNR40fSU2hv0PQfcWJvjJUsS5Oka0QA4wn10bILxgY7qHUdPqlb75DGoa7co9xcFIr9AxwMgv0u_UkEqjdPgygtFc4B-vpjUUftBQbGJy17Xbs5fl03v2NcVYyVSQelBnXdimmJbR18SmE2DZJ_tkXcoNre3aY6nNurCHlX7aOsMWdkndbEDv7Ln5N9ZX3R1IpUevCWXYJpgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b6ab3616.mp4?token=Wh44oM7nK0Ylfdm4HNn0TkC5Hx-UqEBlsoZfAaOjkmCtTePvGDqUgTaudRK-FNR1KKplZJRTcvNtYXDMhnZuK6tlJR6Rg34eBVYNgk01CPEKMo-fQE9ukQ08-kE86mrOzCUkOtUGsNR40fSU2hv0PQfcWJvjJUsS5Oka0QA4wn10bILxgY7qHUdPqlb75DGoa7co9xcFIr9AxwMgv0u_UkEqjdPgygtFc4B-vpjUUftBQbGJy17Xbs5fl03v2NcVYyVSQelBnXdimmJbR18SmE2DZJ_tkXcoNre3aY6nNurCHlX7aOsMWdkndbEDv7Ln5N9ZX3R1IpUevCWXYJpgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حضور شیما کاتوزیان، اینفلوئنسر مشهور ایرانی در بازی منتخب قلعه‌نویی و بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95409" target="_blank">📅 12:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95408">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPpZBHZ12ODXOfSlzwQtyXZHAr9mJDevnjoXjBNK6ZEyaAptUGJ0kN_bz1lSBH0tndAUHl_vSSYusT31NnQIqkIUMiNrS8cJ7dihgy8pJ3eG4TBIrWAmmB0qZ6VMOEA5RuP7wmmu2fbtlZeg4HGrfzjuxjox8Pku1Je5TFSTsdyk-wGT21_X4sYMuFtWJkis3awyFgmVook4Jp73v6lkAx36moA5DsrSDmM-euXar_p453PSPVz5vRIPetM0NQGxmlQRo5ouPxbrhiLW3GzUV7jgMPDGuT459fV6PcRACuY7RjYdyM6Nnbqi4vKrxbzlWOCKGorIxCOXAwGdYI1kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر غنایی:
هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95408" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95407">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d84bc94f.mp4?token=YujPpKjSoevs4bn4R70NI4Swd0LSCekdsWJS_zLWtEjFMORlamtu9NtsEUQVdirvSePtqaSIqpwqnrxACPW9cWiuQRbzl6-nVhvHFj1NOmmEl4-fxwlXB2FMqeVYzhtshE32BCbzjCMRNzNvDcljXwKa4UZwZbCb7OvEsa4lm3aMEbT-gc7cyfpOxU8M0qhR1CR2K66bq74128rLTghR4MQgfWxCjezxu_YSsd9wTAT9UiTtRgEutFdzHp29CBsw0rHANMLk2JWi4J1KtJq7Pldrb4TYnWPNW_JELk0k2sSlug-XMaP7WdA530Ik_qfj4MgGUQsj2lmsSbTWPPXoug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d84bc94f.mp4?token=YujPpKjSoevs4bn4R70NI4Swd0LSCekdsWJS_zLWtEjFMORlamtu9NtsEUQVdirvSePtqaSIqpwqnrxACPW9cWiuQRbzl6-nVhvHFj1NOmmEl4-fxwlXB2FMqeVYzhtshE32BCbzjCMRNzNvDcljXwKa4UZwZbCb7OvEsa4lm3aMEbT-gc7cyfpOxU8M0qhR1CR2K66bq74128rLTghR4MQgfWxCjezxu_YSsd9wTAT9UiTtRgEutFdzHp29CBsw0rHANMLk2JWi4J1KtJq7Pldrb4TYnWPNW_JELk0k2sSlug-XMaP7WdA530Ik_qfj4MgGUQsj2lmsSbTWPPXoug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تبلیغ پورن‌هاب وسط استادیوم جام‌جهانی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/95407" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95406">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هوادار مصری رو می‌بینید که بعد برد جلو نیوزیلند شورتو میکشه پایین
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95406" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95405">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشماممممم چرا بخاطر یه پرچم اینجوری بدبختو پهن زمین کرددد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95405" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95404">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این زاویه ندیده بودم عالیی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/95404" target="_blank">📅 11:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95403">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تقدیر جالب قلعه‌نویی از بیرانوند در بازی بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/95403" target="_blank">📅 10:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95402">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
چالش هوادار ایرانی تیم‌منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/95402" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95401">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c544153.mp4?token=I4yH70vrI_1yG6C-Ecq8vLrk-WESkVk3LnrmxGqC_UwmGXb1dTqMOvVBRzRz7NgLW7nVudH06lLniyw9TNDLSPqUKsYJAXnTiLwj9w_znA5Q8ycjyQ1Jup2MjgUCRZR3aZHeVO469gKOGzkCkie_5Zx5c5EnJB8_PQJcR-eeKTqX6VK0pWeUiJUfa-5kDFFjEd0-bUvfv6aKvBFIqK2HcD6mZae45O58EwQ1bJizv4Bc6v_jXow5zRIueolmyMxgOOYJY3etpjbCTl_TIgy3U9f-4hJ4U7VmDije2UIxI2poHWqAmjgIdwdicixGSFemFLeuZVzcG1fmlDXcJeIEGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c544153.mp4?token=I4yH70vrI_1yG6C-Ecq8vLrk-WESkVk3LnrmxGqC_UwmGXb1dTqMOvVBRzRz7NgLW7nVudH06lLniyw9TNDLSPqUKsYJAXnTiLwj9w_znA5Q8ycjyQ1Jup2MjgUCRZR3aZHeVO469gKOGzkCkie_5Zx5c5EnJB8_PQJcR-eeKTqX6VK0pWeUiJUfa-5kDFFjEd0-bUvfv6aKvBFIqK2HcD6mZae45O58EwQ1bJizv4Bc6v_jXow5zRIueolmyMxgOOYJY3etpjbCTl_TIgy3U9f-4hJ4U7VmDije2UIxI2poHWqAmjgIdwdicixGSFemFLeuZVzcG1fmlDXcJeIEGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
پادشاه اردن امروز در ورزشگاه شاهد حذف کشورش از جام‌جهانی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95401" target="_blank">📅 10:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95400">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇪🇬
هواداران سوپر مصری در بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/95400" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95399">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95399" target="_blank">📅 09:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95398">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=B5GXhy_RoCbC17eDjxlXtKrlWuUKiX8cl5ccByY8DliXGzFBFLldKe_vAEKFj2WEm99H6Mz_GVCcxaU5azPbcamQN8Al6N66D4ExQEUdD8cdOfKYT6PIxM0KMFMqnKYHNYzi4sQeUDdLIv7tlMwP4b4my1D_Xv4cWwjUkBIL18d92AIeWO0yCU2v7rBXJXSh2fuQnvcR3rWPQpulgeGW8HfukSESQ8pohEXbrObb_sbss8MwzXDT9AjrPT09eABjSzxdMcdcQpoLsOBqRdrJiPRrpbA8qamV8FtLNl13lpQmN6COcODYkAagdOywfw_nzSGrKEeFMGEdb2npPQ3qLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=B5GXhy_RoCbC17eDjxlXtKrlWuUKiX8cl5ccByY8DliXGzFBFLldKe_vAEKFj2WEm99H6Mz_GVCcxaU5azPbcamQN8Al6N66D4ExQEUdD8cdOfKYT6PIxM0KMFMqnKYHNYzi4sQeUDdLIv7tlMwP4b4my1D_Xv4cWwjUkBIL18d92AIeWO0yCU2v7rBXJXSh2fuQnvcR3rWPQpulgeGW8HfukSESQ8pohEXbrObb_sbss8MwzXDT9AjrPT09eABjSzxdMcdcQpoLsOBqRdrJiPRrpbA8qamV8FtLNl13lpQmN6COcODYkAagdOywfw_nzSGrKEeFMGEdb2npPQ3qLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بررسی کیفیت تیم‌های آفریقایی با کاوه رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/95398" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95397">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=K-9Q0buEZ4eu5MkLvCnr3dZi75Dyp488vfRTozArWBysvxwrHxAWiScK6YYYTWePDxereTS5-Kdss-xgSVBbP5m4BWhveFwIhb4XeYTKNhAqjDWz2L_cqDuXCB4UyaLRL4e5goEcJ8lOhpD5YMG632yFCGLWQF4suogF8QGN0nQobRcLA7u3scet_bYyRXZILHZi7j8B7d7HyLhcVkTk-ZrMy7B82JD41nebEtoKJ6ZCazI0qCOUZWxNAomx43GPgXAkd4H4UqgKRly42vZRSAzVWoBKRi3SMQkQQVkDE-_7EhqiIKeByVT3EtPVaEKYhNAdpL2VIVMLaMdXOihEtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=K-9Q0buEZ4eu5MkLvCnr3dZi75Dyp488vfRTozArWBysvxwrHxAWiScK6YYYTWePDxereTS5-Kdss-xgSVBbP5m4BWhveFwIhb4XeYTKNhAqjDWz2L_cqDuXCB4UyaLRL4e5goEcJ8lOhpD5YMG632yFCGLWQF4suogF8QGN0nQobRcLA7u3scet_bYyRXZILHZi7j8B7d7HyLhcVkTk-ZrMy7B82JD41nebEtoKJ6ZCazI0qCOUZWxNAomx43GPgXAkd4H4UqgKRly42vZRSAzVWoBKRi3SMQkQQVkDE-_7EhqiIKeByVT3EtPVaEKYhNAdpL2VIVMLaMdXOihEtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طارمی تو رختکن قبل بازی بلژیک دقیقا چیزی که می‌خواستن اجرا کنن رو توضیح داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/95397" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95396">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aca2671.mp4?token=mVQmFHHBNdDIjx-8SXoOljBD7QhghsDLd3BjbW3JPFMJF6BT0F9JwywD1c5M7ON2egm-_yx3hrD9xsDDbR-QCPXVfYvXdxQ1tzaftCwNgN4_uhw-Pfu1JSAHPTtZJs5Zi0pOvHTzCORHOakOxJGy66YGRSpHTUleCrO5LcABUlUJU6UlV8CfqZ1raQeVpUfE9s2Gf9FPqrB401AfTbNNNJ0_0Pi9hRVlJHwakvMT4UEHnwUFgKhMklb-v0kwRwhUkbcJmV1Xvkq_yhCbFen2zhrWUxMyMO4N96m0NOcxDWZXRytWhFwt0kEla1LkoBZhgOsm5nBznHG9PKtWtF-QSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aca2671.mp4?token=mVQmFHHBNdDIjx-8SXoOljBD7QhghsDLd3BjbW3JPFMJF6BT0F9JwywD1c5M7ON2egm-_yx3hrD9xsDDbR-QCPXVfYvXdxQ1tzaftCwNgN4_uhw-Pfu1JSAHPTtZJs5Zi0pOvHTzCORHOakOxJGy66YGRSpHTUleCrO5LcABUlUJU6UlV8CfqZ1raQeVpUfE9s2Gf9FPqrB401AfTbNNNJ0_0Pi9hRVlJHwakvMT4UEHnwUFgKhMklb-v0kwRwhUkbcJmV1Xvkq_yhCbFen2zhrWUxMyMO4N96m0NOcxDWZXRytWhFwt0kEla1LkoBZhgOsm5nBznHG9PKtWtF-QSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇳🇴
احتمالا پس از موج مکزیکی و تشویق ایسلندی باید شاهد رواج شادی نروژی‌ها باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/95396" target="_blank">📅 09:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95395">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcacjzRU1lnZRdbReni_CqowcMYzLSdFVbI4XpEhsdMEk8LnUGyWPkdYUDPwwFiIrEt5uMgx0Hz35echU_Q6km2iJ3xlWeSRLzTDqXkXQ8isuz3zUBUMn_wJxHMvOTLOwXAII2Ckfe3nAiowpFgjIe8y0Hz23ZONXaK-IhL45uHGAPN27TI50l9c7lUjCW3EfGkf3O5BiowI8PYjDZ1wuscRZjY8Ow5hQiSVoV1zvEekIyGVpMD6zQ683SZrzevsN89tWB-f8R5U0mtpkuLY7wk7zp-wmkTaV8O4yL-iDBJPerE82lblGn567ts9naLNs62pGoW4ZX4jnoVgfEnWLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇴
تیم‌ملی اردن از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/95395" target="_blank">📅 08:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95394">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95394" target="_blank">📅 08:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95393">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=rMj_FFA2godiTGCkSuE2UALnFWoEbRarY7LQHnhodU045byyXAfba1XkZQ2m2OwWXduGIhrUuDV7SfHG5DfRoa4dB5MQ9XOdebU8agKHdwXfP8BJkGn25zW0cuKqf8RywASO213-dH2by-dk2o6GziIRUgKE1-uH3TzIfkczBGcPYPDwDEmsLe7xjbRYC_Og0Plwq-nLYycnHW8b-yUrQnWeG4F5zaaXvQihnDzDobfTGi-qQXwPA0hCqaGDEPqxUhhuRdqxVcNeqSXNeEnjZcXLLsN1yGOBEKuPkQ90T6_FFeuFQJFehSyoB9s8B-ZofX8MIMkjP5H5Z3Zhu8xEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=rMj_FFA2godiTGCkSuE2UALnFWoEbRarY7LQHnhodU045byyXAfba1XkZQ2m2OwWXduGIhrUuDV7SfHG5DfRoa4dB5MQ9XOdebU8agKHdwXfP8BJkGn25zW0cuKqf8RywASO213-dH2by-dk2o6GziIRUgKE1-uH3TzIfkczBGcPYPDwDEmsLe7xjbRYC_Og0Plwq-nLYycnHW8b-yUrQnWeG4F5zaaXvQihnDzDobfTGi-qQXwPA0hCqaGDEPqxUhhuRdqxVcNeqSXNeEnjZcXLLsN1yGOBEKuPkQ90T6_FFeuFQJFehSyoB9s8B-ZofX8MIMkjP5H5Z3Zhu8xEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95393" target="_blank">📅 08:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الجزایر کامبک زددددد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/95392" target="_blank">📅 08:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=h1FLH7tJFpc9LWFFkWZPpwoJXBQ7FGM2mS_C4cXE53p-1AxKrnM5UrGqQQRnefKEbp8v0Y_rcb1Poyt5eB0apr5l0LifSCgeZoq6K5eXHXZd6CrWaliDjtKN10IU0iJe27wRz71vmJeYwMKszGVFtvkfzQw-eaBH51MOS0Oto2bS_yJClP9DZpBS59jI41UczN9gX_lBZLnVcyFiV2iUWVM549xd5s9ScudT10AKjiUt2lWxy345uwV8LAFShlPlPNYZOUBIkyx-PRjAOglKKa-rTTDqyXpVgOzgdLfvMf7lPbI2QQnvZo7cvKn_WnljR9xA54h5wbKLZHY4xb1kHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=h1FLH7tJFpc9LWFFkWZPpwoJXBQ7FGM2mS_C4cXE53p-1AxKrnM5UrGqQQRnefKEbp8v0Y_rcb1Poyt5eB0apr5l0LifSCgeZoq6K5eXHXZd6CrWaliDjtKN10IU0iJe27wRz71vmJeYwMKszGVFtvkfzQw-eaBH51MOS0Oto2bS_yJClP9DZpBS59jI41UczN9gX_lBZLnVcyFiV2iUWVM549xd5s9ScudT10AKjiUt2lWxy345uwV8LAFShlPlPNYZOUBIkyx-PRjAOglKKa-rTTDqyXpVgOzgdLfvMf7lPbI2QQnvZo7cvKn_WnljR9xA54h5wbKLZHY4xb1kHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌تساوی الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95391" target="_blank">📅 08:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگل اول الجزایر به اردنننن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95390" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucJwWenbCPiC__kxl0v-gEn-1qDei67nvxSolgr1e9h4v0vIoWvkUjptW2myw7YiBBp_sBT-Ft2iup4t0oChgwocrJO-GT7F_QPcaJti1oX2NnF9NwNqaVv0TCXmrvg2wuk_aJdisR6CtC8rN4DoSyOu_r-yCjdC6u4kL5uVBYRcY4NoeQSbs7IbhBHIK2FPvWpu3pHgLoRZh0VvPt304xsOXPWXLRWqLRY8YbWP0Q5cue46oICJhomqiQgVa3CyN0iqyyhVG4lkaoyB9R1XA8EDpKAPTSMhYhqND5JlfUMvfu-wLgZCeFep3J6Rcw9xl3iGdPM7Pmg_a76eGhS9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxotf6uw_MnSisu_R4xFi4_JbpRTRJwyScooE-Wx1UfZo3OBJugoAapPchMeuVWCCJGjr65QU39vzJLgAtkH-cdMLVML0L5z0KJeCM7GjZsyK1bmpLn5rrA4_Mf8FOsiQnG6Po7SUXy8fFyLR3uPdVBSpI4NqNRjKEil_LOAYVSQ_1v4hRd-dOXPGDobG8Sf1ivThQHhbE2IfMjrK-7USy0zcyTRVazbEKQBKL8q6CiokG1OaeVWqwoAEiF2mom0lzMtu4Ub8uC1Di9B5Ueq3r2YJtVsZSOySTtrOw3lc1Kc6uRC-Pv767olovR47FzNsDqjegTJVqlyZL2nseNEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
کارلو آنچلوتی: یک بازیکن هست که من او را خطرناک‌تر از کریستیانو رونالدو می‌دانم.
رونالدویی که در آخرین بازی‌اش گل نزده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/95388" target="_blank">📅 07:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95387">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09b400e516.mp4?token=no4JT0EXu4qdpaR9zWPEqjiakCfJqZxWAI_XRaTF6axUTkUEO-H72xueR1gBWbiVAM8brKaQRtlfpDm6FGNOinlHEPCExI8Lpf8NHtUWfWX0Ji6Q5-IN5XbtNM6fNVMlf4d48oXAQ-GBgbD9E5TXjeduSVi88Zv-wJ9JWid7GhAl1pQsjrGTwbFOHFaZB3HcOAsXrz6ANMTwaFQTACI9fVBqOLdGsq_FjRLK6vGyGyiC8eSe_FPQcsywu7Q_yYvmdb7CkOT7-xJEjwg6pyhKVaDvukLq8Yj5kAHHsHUcgRnq7rWd4Abbw9a8e3XHfCh0BtSVHe9bZyIIhEjTTxLi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09b400e516.mp4?token=no4JT0EXu4qdpaR9zWPEqjiakCfJqZxWAI_XRaTF6axUTkUEO-H72xueR1gBWbiVAM8brKaQRtlfpDm6FGNOinlHEPCExI8Lpf8NHtUWfWX0Ji6Q5-IN5XbtNM6fNVMlf4d48oXAQ-GBgbD9E5TXjeduSVi88Zv-wJ9JWid7GhAl1pQsjrGTwbFOHFaZB3HcOAsXrz6ANMTwaFQTACI9fVBqOLdGsq_FjRLK6vGyGyiC8eSe_FPQcsywu7Q_yYvmdb7CkOT7-xJEjwg6pyhKVaDvukLq8Yj5kAHHsHUcgRnq7rWd4Abbw9a8e3XHfCh0BtSVHe9bZyIIhEjTTxLi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول اردن توسط محمود الرشدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95387" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گللللللل اول اردن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/95386" target="_blank">📅 07:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شروع بازی اردن - الجزایر</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/95385" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/95384" target="_blank">📅 06:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUOpiaKbMqLLkvv2tUK58eXXZrLOoGPXknCsBYFAwGiCW4Sq2R3ouI2PnsKsWAYItgw8TZpIVMmruA0fjVS7RVkdgS3o-b6urE0Xo9w9fb3HACxuR4-LeaH12MruhpdWdgOdbNX3CFCTlQBZC6qxKzR27_ooHTxlbnU7IhYnEopm2MF_vpIMKEEqHueY-GQ0o7z87nzeEomTQWYRiDfkuH0skd8EbpSYd9iBGHuigeLTV79TfDOXMHeBOT5p5REmfY7wU8bUCCh6lugFQJsSi1oQqU1gH1TT--jMwUmV75ci7hTjqbO5c00Bv8yd9-ocdlFK6wBRcsTqpsp4nIzaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی نروژم اینجوری بعد بردشون احساسی شد و از خانومی لب گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95383" target="_blank">📅 06:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hshVPYDLI2zlAiT515g8Z4Y8Gk5VT4SZYjypxWZPnnjVQpjLdB8gdQPsQHC8YIv0HW7q22cN993q-BrbH9Nof7AAs2NFWce3kF-e03Ik23MBcTu_TxteWrMaBuHXwOCj-ixyisNb37C5z-1OnP5-uM7G-a6NpGKX6sOf2DkdaCJgv9a141dsb5Blrw59IbUNsMB7x2xC-irx3v9tqWZn-iQiIJVsDEqSbByFaJ5gVCH5yqLKEGO-FzIH8bk-62smfDeGCce_Dhmj6QjZWIl9MAQruFVaYLEeMLzvJ5q8SP9M4Sl-6kAGHEgCsC8OLRVFZ1ZZ4XDkjmKgT9pYf4r3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابلی که در صورت دوم‌شدن نروژ و پرتغال در گروهشون قراره ببینیم
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95382" target="_blank">📅 05:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZEWCEyYLij1-wDt2dCBWus-Qgz2iVOawQZk9G1hQDtisSHXb1hzWUIuaoGsy3WHmVOYh_HboWVM7VYRsPPP4U5IenuKOk0XyctMHD9RSdmBKw4qqh7vOsCxqpglHTd7IRMv6GhnwETpjQD3KA8_fRTkJg6p4QFpR8SroUMZUIxG5ab9_JoRq_kVQ_8R24H-Iql4VUtd4BT0gF3vZiIe_gJpDaJqYVg-2bN_NHU9EHQyx8zTkMv4NPXr-eSGSpERuLSpHm91LFg1Gqk9v99rQCKpQHeO8_MEu0x6n3yuJhJoFAloRAGbo3xgkF5rplbptFSloyumu-N_OLBRzFIdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
در جام‌جهانی ۲۰۱۴ و ۲۰۱۸، بهترین گلزن جام‌جهانی تنها شش گل به ثمر رساند درحالیکه بعد از گذشت تنها دو بازی در جام‌جهانی فعلی هر یک از این سه نفر حداقل چهار گل زدن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95381" target="_blank">📅 05:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم از جو پشم ریزونی که بازیکنا و هوادارای نروژ بعد بازی رقم زدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95380" target="_blank">📅 05:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjIJtEXx2gEktVbDv_l0d3CiB4O3nqpvkg1uE69sC2r_eCTHh0jSLhJ117GjB5EW7Q5ShAfUUh2epKimnGgNmy9KnS1zOoPLAbeYht5LWbwezzmuK31B0-iHFiDP23Kz7FkskQaR1qWKAh5vUjWDd_zeiFli4dD5q_04Zv06xA3uH-aV_fQiMygb7vuRWJpJli_vnWBRSnPPm3nRh88Mb28WFmvEMWsAdXbcsz8Qy66XMK6-xwHMOCdjtwRGvIyzMmYqreb2zTOGf6siORCN7NNrFgh9ZytdSmjdD8CWp3gaHyMbNdtJnArP2trVYErsAYj9eFWIj0X_MxoOQYR5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ارلینگ هالند در کریر فوتبالی خودش:
⚽️
‏• ۴۱۶ بازی
⚽️
‏• ۳۵۶ گل
🔥
‏• ۶۶ پاس گل
‏۴۲۲ مشارکت در گلزنی در ۴۱۶ بازی!
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95379" target="_blank">📅 05:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbiYlDLYi8WOjcf_StzJzLoKx3CocOBc_0YPVB2xyWY8FI6p3NUkqpXzcFfLg3BfMQZ9mpopL_CXdoa6_FeNekwNY_c8-0n5-9iFEruUSJRUc1IyzCo1UaL-nDAYI0vtCLeAALZeOr9uLijGPNn2CUmLNK_yXENqYnvxiEfAvgmsiJf4ODxWcLCrIlBqA1ha-A-g2juSNh7D7qfXpCliup__sOkq2IIhqKHi6iIlAGM8vtpOY_RROKI6QrjPdUHTXJ5nFpDofH9EQRIhTWFx55OZgqbWD8RrJr9AhdT65nKP1R9lyI232PlkfASELEav93vj-J-NbWtXjz9dJ3X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95378" target="_blank">📅 05:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVLTZkn0C_3ITka7r1id2--AAtbwVcgpqqdPVRdgilKCgAeua3s0RuJz7wsq_9lttjhzKYmMWNHilAjL2klEryC7hsATbgXr3FX0iFNq3p5Fp4HR88pnjDyIWFiw2_16Y316RNbPq6x3F16w_nBi_ZweBp9SscaplZTK28fSDt6qp_trRKx__XWGGZAy_v3iyuoj3qBp934BQrZ2Gsg9Ys7svi7oSaBymWa5BWpuRxQwQrWC24mqdHqh0bOoWLARFxQN0D6SKhL4VandzniYwNfr4izrfVhjbXblDf1ibM0dFyHvIq74AVqKSSSw6VtkNJPQNdmEZJzH1ro-e2Gg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود وایکینگ‌ها با دبل بچه‌غول
🇳🇴
نروژ 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95377" target="_blank">📅 05:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=A8MI0y5nVWiF9XhiGLpyh4bdVbElAQKZDBjRdzd4bcsUUwb4xsxaZWN8DM4IdYzgxmhjnmOJrJYqozDgA_rm3ZtANKP7XDJJrmaY1Yu2zqfHjS636YkXa8hC6XKXYbRXv78V9tuLwoHpSm9JSnKliWMF4UlF2K9ZbrtiSpt-ItFJaqiJlrHULtqpUYl7DQXCv0Zo3aqaXIdygxlLyVOyNi5LI7lMKss9n_7jI6JchWD9cOFgXpndEChYCk8VdbxTwtjFKtNkaUjt1SEROfU7adGgfNhX6xCL6fsOmx067OrarY9hzdvQBPOVMfFk0Wh20_3LQBMW3zDcrPbQrCIdFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=A8MI0y5nVWiF9XhiGLpyh4bdVbElAQKZDBjRdzd4bcsUUwb4xsxaZWN8DM4IdYzgxmhjnmOJrJYqozDgA_rm3ZtANKP7XDJJrmaY1Yu2zqfHjS636YkXa8hC6XKXYbRXv78V9tuLwoHpSm9JSnKliWMF4UlF2K9ZbrtiSpt-ItFJaqiJlrHULtqpUYl7DQXCv0Zo3aqaXIdygxlLyVOyNi5LI7lMKss9n_7jI6JchWD9cOFgXpndEChYCk8VdbxTwtjFKtNkaUjt1SEROfU7adGgfNhX6xCL6fsOmx067OrarY9hzdvQBPOVMfFk0Wh20_3LQBMW3zDcrPbQrCIdFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
دبلللللللل سار مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95376" target="_blank">📅 05:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سنگال دومیییییییی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95375" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلللللللللللللل</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95374" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq7vyw-rrvvFlOigRz7yFeSMyvK2j-brjRgRzVk_PXhsX9nRhi5ya1XfHL5cdzkKmKcjGnZ4XIrM1EV5uhhEgBIQxJHi40YhwFrcU_SveOSjiN_wMZrpb-MHRrFJ0iaeL2l-LPWrCNKA6tCFkPBLtpubPc03XyTEUqHj3CTWcutJwTU_zBFpGpcbxO9FDR2rDoBt4v_cogFqiBYKr8WOsqhePsS3RtRyhbmEE--wQqy1VC68tYTJIQPo930DD8A7MnVvvm1GqftHCWgiTvYUrDqO_Qr3cq3TMKQarXhfMks_T5TO4-Yn5QHQdPApaIoYfZPggsBao7yl1JFQkqlAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0ZKyMW0FJZd9TC1vifUZAu2zemXcBQJEjoAVqBc2SdOCVNEDK_Y03CapyAqf4bSzLaQDM86qs4U7YlAtl5xbgKUq7VBjbSmjqLpmWh3uXHGSqVcF9HHokMykeehxnh-fjT4rLpg0IqQwsxtEtb3bYEBmJ9TkTW8YkUbn9wslZxwJR98Aedhil9QJwl7cdtV4ZI3v7MdxVah1mfr0U_mMgP8nKpQsgFE50FyLw0opGb5HFjsFx696GMACAeaVUJN-2yznNVYy0Woc_37gyYQ-7ZnXNYwOoAa7DdD0aU7Sv1QU4myvB1Wf0P-TmqBvuFFOb41AtxRta6u781UC1cpuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇿
🇯🇴
ترکیب اردن
⚽️
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95372" target="_blank">📅 05:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95370">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8wrq-NhoJE2EeXccdmRQlX8UinjxSNgy3lTY150eMJ2mKFyeI6ZSFgphBnCPnPxm5iII-MUqM2o9fLaApJNTcLS0VyyyScZ8b46RkE1CceWLGf41VLgV8u9QLEO_LyoBHOkHTzrGio6F8_hZV9B2A0DWGjAPD61hV-6H7j0GRJAaVAr4INTua3kbAWnsTv5jlOOHqdt3byZDtz1PiwHmyf80_E37z5-no2FO9mV6aK-ko4FtuwGlRwC24RU-QFkUl4tRO5pXUhmindyeuzLzp3epl_zj33Dr39OjnlaVWdB0ViKxvupPxpFpPgGYE0Ut1_nMM77kxisz0Tbcv0M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyJx-g0c8SZr9HisXZJqTbB833zyJzCeg0n7ZiAjnmfdOi5x_R6xRnwtM44d7nis78y4J9PS43NkPatjPP2TvKAtMpNFooDG9ZFNrypKbpHMcpl59KQqH0ZJkG8Wn7N8Q2P0MKIc0E4rThTObQKJANu8TCDj0NnALjQSZos9k8YyOMSvkI5VEipYNJpdoGvoztS0EBw4y12o4h2StYMf8UHTxgXkzb_Mbt9nlDaRjPkexr7I0l0awnBGzcC__VeHdEsP849QqMb_g8AsxLcC7P15W7pxOygFVnTy2M8fQi9NwBoaHefEOpHG4hc8lA244doatdWUR6Kgf9JCeLB-AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Haaland x Ødegaard
🇳🇴
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95370" target="_blank">📅 05:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95369">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZpUjtlDXMQawFyjYz77u16rH8-1KQuNcTnFMNFRDr0GuYbPqdEp2f6CGcfSzjsRhKjv7hNGN2sm1zWJH854ugXjkBM5hihmEr9vR_f-7DZUPAlAHeL6tNOm55K3Nfxr35g11xv3IfTJlR3XmD_dBp2sl2pUdH3Qw-63FW_YOAzfp-IIBBt5TQP08MSsccF1X87bbVzv91ci1P8-IiM5iuJpJCWDMNW9w7I1SWcChsB7HH8AQYk0rOFYQs50FCKUY3vAZaCzpbw8pb5njDQR-qXnzY_IY-N2-1rMI-Hm9-uO4T90zF62eoPPVkSuO97J_8ohjoy1sXttmzZYEMHtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسط بحثاتون راجب مسی و امباپه این وایکینگ نروژی خیلی سوسکی تعداد گلاشو به 4 رسوند.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95369" target="_blank">📅 04:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95368">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مندی گلر سنگال مصدوم شد و دیا به جاش اومد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95368" target="_blank">📅 04:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95367">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwKpyB1vGCLSc678Uht2_kGE5vIFsCzyPrOqhBmeZg9fXpGRKNN0nwFOMT5ItKDzbmAoYAtY1I4pEHowV7131skL_BuDzGyqzs-ksBi_J65dcZefpZ_n1bSMAvMEyML16LUiop-D9MGi9SYj7zvh-vqLMnfGzyKlCNpT53XV1o1df2R05mxfF9fizqIxZw_l5KJb32LL75hPzNxxfkU7UK37ciOFLThdnEnDnU1-YocNwqgm51MsfB2hWHQSozryZPY9RjbvSl1U4As4p_jrDZTvE6kqZHFDWMvd2HHAta9D2UXLXPKe4j5HQ7CsFq3Qvb6II79H_zJ-SQFpb5nqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پشم ریزون ارلینگ هالند در تیم‌ملی نروژ
❤️
🔺
ارلینگ هالند به بهترین گلزن تاریخ تیم‌ملی نروژ در جام جهانی تبدیل شد و در 2 بازی برای تیم ملی نروژ در جام‌جهانی 4 گل زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95367" target="_blank">📅 04:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95366">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=VNO83umva_L3ZawCEusYUvrApt55mCBQVPV3YVvpYnTcCyCmUTKTC487FDgrb_de06zP88hyhdOyHhpunCfvZf0N4bHJCNV8TzSfIKLwcd3j03mjuqyB4QHn_IINHpMw93DPVNEzoZPkWdnev26fAjDW5lBBuNHPnJdQw1kwf9xbK108FDjtX65tCHr3VWLGk3WMdh-2DnrsNwu9EW-nykvULXh-ibNvTWJEnP-hqRJ0t0KFSkAap_wAZtLQ3QOqA_To9yaCc_EqC5JQnn5XO8TTm-0RunFjB6EF_I1bZNKZLCX9Lq2dLWS0RBhRU71oEPUHsvlcsoawn2jJulzCBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=VNO83umva_L3ZawCEusYUvrApt55mCBQVPV3YVvpYnTcCyCmUTKTC487FDgrb_de06zP88hyhdOyHhpunCfvZf0N4bHJCNV8TzSfIKLwcd3j03mjuqyB4QHn_IINHpMw93DPVNEzoZPkWdnev26fAjDW5lBBuNHPnJdQw1kwf9xbK108FDjtX65tCHr3VWLGk3WMdh-2DnrsNwu9EW-nykvULXh-ibNvTWJEnP-hqRJ0t0KFSkAap_wAZtLQ3QOqA_To9yaCc_EqC5JQnn5XO8TTm-0RunFjB6EF_I1bZNKZLCX9Lq2dLWS0RBhRU71oEPUHsvlcsoawn2jJulzCBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
دبل بچه غول مقابل سنگال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95366" target="_blank">📅 04:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95365">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عجب شب سوپری شده امشب</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95365" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95364">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دبلللللل هالند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95364" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95362" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC5sWPTRKF297Brdlmif8N317sr72mOhyrnEhvEmiQPQn2FC-C-t0A6SMjMBYmcaTFlStKb7K1_GbX3GQp_4Zm160O5C28ea43sVaoBwyeseJhUKssP1zsbaYtjCpb30p8zQ8ezEkob2xEJNtfKG5GdDM6ocpGNR9pLYLzD2ZDkQiA4c-QGFW5RiNpM5cc0rvuAd1_RQIRtRgJt7doo2-tYLznzJpG0TaGA6a7Jnh9EPAeanCEbHyIVfHig61udPkAaoqN0wYybB4FCMhgzDOU1FAryu0vC_FHlL6QyGJzjreiy6CZs0AsjXWe0NwYxDmrF7hUaKpJ5CLg3hEUcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95361" target="_blank">📅 04:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzMFvSV_8v2-SSE1eGHC04HSIUkLXqqrBvCU55MO3XMV4we8OrquvQtu7J_EEawa0ggZKhyCvqAihRanFDuMEffkLnt1VEpbZnfUwYQpJ_et0GHG1PXGrvPVH9EO4My6WfP8lHwEJ6PoAaPfOAgBUcLkGLoAsr5xLMMkcSsHZQhBpEcz16dSTl562ewX3I5LQ0M2SbhWw3fMxbjvc-Z0o9LuWjrhNaBARljAlRUQEgB7JiTi0Ye0oLdpGcjVA5nePPiIiQ7jGUDY0Vjb-MwWWA8yAVpijuhMkacPTmtbr9WNTkNjlB0gSjzlTBIQmnfvhjMyHYCyaI6aQwV28XXskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مثلث توقف ناپذیر فرانسه مقابل عراق:
🔺
امباپه: 2 گل
🔺
دمبله: 1 گل + 1 پاس گل
🔺
اولیسه: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95360" target="_blank">📅 04:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR24P_blXKb7NvwFckwn9UmOB3h3RePc_5mMWxgzJ4ucDoz0l1IMBYC9TVFEhvHkliyyqIrrNvFedBZG9Q7LiLeXDfehVIpEIQvuoShaYSnWD-9cSuC24DOJadkIq7Y3G2Zsb1Hk0Y4EFaHPDJxhz208rlthG4NhyW2hOcI-fBoKpIiWYG82g3SMYs6nbCvXcEA3kCTDpVIzsT3Lzkqw3KUskNibl7sIRZ5UtkjeUBQTmJb5ZeTWuWSy1_9F84-urSCf6utYiFEFd69fIESE5joVXyRZqaWf6U15swpvIVzbHFekCgAD9IlDGO_Fkoxd9yg-eFOT_MuYtxCoWgqkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95359" target="_blank">📅 04:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=GJMM9D3vMU6Tqr8H8xBx0AHU0Dw2cpPfu8gw-50ztnu28t8itw7Hdz26KYwvhuM90sQFbDQLN6cHbQg_MAsGWAyvvBALuokvSHMN_2yHHpgBqeBckAckuuuspGkrEliPSVefsPjlskYHiHcVqaJZRZR3H76aB6OUzeOY2bK8k9yOHbepxnynnHUD_ePrsq23NQoKcYgilV17TlNOe0UC1iqAukrs-j9jeAbRFD2G8klVq-wTIf_Sls8Ns9Oy6QMhlg6bU5xmaHSt8AzgE0_wzKZL31MlkqOVr863OwT5y7RHEgONgQBbdGMDO2m6l1Yuchfr2VexDJnq4zL9SEN6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=GJMM9D3vMU6Tqr8H8xBx0AHU0Dw2cpPfu8gw-50ztnu28t8itw7Hdz26KYwvhuM90sQFbDQLN6cHbQg_MAsGWAyvvBALuokvSHMN_2yHHpgBqeBckAckuuuspGkrEliPSVefsPjlskYHiHcVqaJZRZR3H76aB6OUzeOY2bK8k9yOHbepxnynnHUD_ePrsq23NQoKcYgilV17TlNOe0UC1iqAukrs-j9jeAbRFD2G8klVq-wTIf_Sls8Ns9Oy6QMhlg6bU5xmaHSt8AzgE0_wzKZL31MlkqOVr863OwT5y7RHEgONgQBbdGMDO2m6l1Yuchfr2VexDJnq4zL9SEN6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95358" target="_blank">📅 04:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdxMG0R-XZcwEGi4s9DQ27KY6CMTLOYn-fxmOJuHupXsLwRLKKd8hqpRc_W-ohMJYuV9kbKcSPkt34Ee0CCyDMgI5LJxuHayCqr5XadjHvPiebgOe-YubTAs6UFyRiXxLE3DjYFroyYGYQuQWstj0gPM0elUSjuIcXtqe5q-C0Z3bn_YntqZUqKBK3HkBqQAY33ocF-d3o50_cTAWoEzqS-vBU7SBrYQjtiWo9_-IjaXB4qb72xCnXB7851Kl8mXYsW4mgF79wJOIrrFuyX1JC2kWr-aixJlsHnsXybWbo3OJN35Xfu1yzk53KZ9LznmPMJR41GzGm23ZoAMp3LX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | جوابیه سریع و خشن به مسی؛ صاعقه‌‌ی اصلی امباپه بود
🇫🇷
فرانسه 3 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95357" target="_blank">📅 04:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxqb2V5OaASkIXc74iEps308ff_tzvAf2aF6QFZnAEeZvSkIRLUqzekj-BnoDxJlwEtFetZ7r_fh-UlkFD-vQ9d3UKjNm7_q0DzteJYR1kbM0zXmNtkpU0EPMN_8QK8lGGDL1Pr2KHp9m3_IZStQ2d5FSAYV-8nkJr0e422nMib4KAQ4gFmkvy3Io-DK2AqnkIbhdaZu5pUMaoM0k1tY27sWjJnymZ5akDLFyaA8IAN9Rji27u0aPbrtXixuxHPufbKe7KxszJDCMZuYs85-Ml4zSUWoI0bKKdPobZRfQaYp2RHCgIT32fCa-DAsYsE5xWKJypLnjXcqMppMO53Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از ابتدای فصل ۲۰۲۵/۲۶، اولیسه در بازی‌های باشگاهی و ملی ۳۰ پاس گل داده است
‼️
بیشتر از هر بازیکن دیگری در پنج لیگ معتبر اروپایی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95356" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=C_rlJPxrRT3MRC7-wWdX4QeD2BTsEVPC9wVLugmwCkUJIWMCqui9sbdZCEd7TSoMuThWwXyGtbSkQa0AS_33EPPlGjoeYxQaMr0mdSuamuXq_lQgdvh466tC9m-FG5A306qGbZEiUfidfV4CrA_bD9VUwlD0zesJOFwBPAe0eyPR2QfwOscybOEUg46noyCWh-kGgvqi2d38nDdMyrEnb_AOPeWJfOfyZoSf9sXT9V6zgCNOUZLz5TyTwi1bUdF-SaGlP0sTMDab2GTcFSfWJuCwwBeyFsPxNmTv8Xi32re9dRu-eRgwZj58xioeOgxr_f8NaG3h860qJbjdNRtcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=C_rlJPxrRT3MRC7-wWdX4QeD2BTsEVPC9wVLugmwCkUJIWMCqui9sbdZCEd7TSoMuThWwXyGtbSkQa0AS_33EPPlGjoeYxQaMr0mdSuamuXq_lQgdvh466tC9m-FG5A306qGbZEiUfidfV4CrA_bD9VUwlD0zesJOFwBPAe0eyPR2QfwOscybOEUg46noyCWh-kGgvqi2d38nDdMyrEnb_AOPeWJfOfyZoSf9sXT9V6zgCNOUZLz5TyTwi1bUdF-SaGlP0sTMDab2GTcFSfWJuCwwBeyFsPxNmTv8Xi32re9dRu-eRgwZj58xioeOgxr_f8NaG3h860qJbjdNRtcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دمبوز هم به عراق رحم نکرد و اینجوری بهشون تقه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95355" target="_blank">📅 04:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=BBqK4my6-T1g0Q4hpTmmpjU_9sU6BxllOMKgmKKf8_KGpisqMWW7biQZ-SHe3m3q5mQrJqEekyiF6zG3hZ0zXgLrr3Qs-bvaXRPHerO-LkA7fjWA7kyu9pV5KNbkWeHgLrc4TP_hY5U4rTsFlL8dPhZBGxrhnjcVnjzKRaqdLBGH7zPZgeHIaO16g_qPQ1x2lANbkk8WOA44GWnY_pMfrcCkMyR7aeKic03fKEVLQcxbqIvbH7xv4h8N-ylSmbRizmOrJwELtgcK1dv9UaYDvRaBIjiXljWnEgXEHxqfA2_FiZuXH-3WVLK9ig4d619litQH6AYV-muW3iN6E39xOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=BBqK4my6-T1g0Q4hpTmmpjU_9sU6BxllOMKgmKKf8_KGpisqMWW7biQZ-SHe3m3q5mQrJqEekyiF6zG3hZ0zXgLrr3Qs-bvaXRPHerO-LkA7fjWA7kyu9pV5KNbkWeHgLrc4TP_hY5U4rTsFlL8dPhZBGxrhnjcVnjzKRaqdLBGH7zPZgeHIaO16g_qPQ1x2lANbkk8WOA44GWnY_pMfrcCkMyR7aeKic03fKEVLQcxbqIvbH7xv4h8N-ylSmbRizmOrJwELtgcK1dv9UaYDvRaBIjiXljWnEgXEHxqfA2_FiZuXH-3WVLK9ig4d619litQH6AYV-muW3iN6E39xOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دبل امباپه مقابل عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95354" target="_blank">📅 04:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95353" target="_blank">📅 02:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95352">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHdinqkjyF0wDeXAucR0XAl9d9RYT3IfuTtlO3UIebpgZUVvZKa6E91eoHgAQeHKUY5C3v-VH1tpn0guqB26feBtQemWkhgU-g2ri9aIdXrXo6oTTOi_uCfm39EqO73LiSP3UDsYF-4dapAZvpaVGiViNdfgEWxMjJkKQpxNX4KBwy4ijBBfpJsEYJsop0KCIaATW-w8OgPbi1I2eu5Y4nKtH6AVLr3ibKaUNbIQ1MVTtyGBb06v8R8hkDdBCMG_zgos8xdS6D-doFtjLS_n6UNKrneeqFXfzD5W7zeDoBjO-yidlrVs8E7fPuZoal6Qh0K9wrTXc4oZ6pQj2klU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95352" target="_blank">📅 02:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95351">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwjMpX157DW9vfYLVwxoa2ZzGriNs_dWg3rZ6R-iLZEkaiJ2MB7OSe98LSieKYe5yFXRKToaE0lp3WecSp-mePdIhEN-1fv0rZAbMc-sTD-ePK8XJgEGjFSTp0Cr6QXnMnrehyXsZH1rHGAsL9HOHQ00Q4lC8XDTkcvJfJgqSpyk6d9e-_2CYzh1EuOxUlytbi3c4gzndFCL08TM8gdUlqgpwixRUmXrJCC4D57CA7DV9RKDpK4w6mfQ0zz_moP_zp_SnpjbfYxnGYCHZbdNAX1JZPt8mdVXao3AOu1ZjeIhTEvTlLSJAui4QaLzYq5axTTuNmepTSqWYQM-FUT7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو :
خدای من مسی 38 سالشه ؟ من از اون کوچیکتر بودم از فوتبال خداحافظی کردم و وزنم رسید به 120 کیلو، بیاییم اعتراف کنیم که لئو بهترین بازیکن تاریخ فوتباله، همه باید اعتراف کنن، غرور رو بزارید کنار و این جمله رو به زبون بیارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95351" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🏆
#فووووووری
؛ با اعلام فیفا، ادامه بازی عراق و فرانسه ساعت ۰۳:۲۰ به وقت ایران آغاز می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95350" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95349" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l_s1wJ4WxU-LNsed1z2YIP3ZAqRywsirSszWHjV2DkLYZDjhdbJhx6c3mGzWC4m5blCCpWTKJ0DFdR1PaPgdOAVjWAQgK7Q8soMhE7sfzIRdrQo2wePqReuIVLzUYiwZPImuWEBmHAx20EzDknMte5TOXPApsFYd1AFozqtsxGoZdrsKd90QQMDzNVb2XVxCW6-vm-g33p8SZ3cNjcmeDfdpsdoq29TNvQS1HEveOXACZfWruAsbvgavLEf23y5jRfOFmde7iLU332SdReUWQAn2ajjTkd4H_CM_dzgN9YVuaz6F_h0q1Sc7MtqOHD7iuSfkuZDMzz-Q2w9hGIqUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95348" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
#فوووووری؛ به گزارش منابع خبری، احتمال لغو بازی و موکول شدن به فردا زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95346" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QraNisGmDO15kY220ZE_ytYzxpTBTgfDW5HtQ3PhIQfMzGkuN7UZwpLvLz8t35IC4nKw9RXRO1ghngoKqiV8Hx53WRKJa0kO5UgHCXcWoEokAf16Y2FTGYYKbOnxDnQr50efHQ-VbqqPUt7wnh59h9bFxv7AmNMrnwP_FDuiTTuQBPB6VXCKmbfFm3_BsLn1uNz4X_DnMvhjA6TmxV_3ChrAlVwhaaN1ZhproxCnjdnzUVouEYASBozs-SN198jdvFEQVygknew6PE0inlmvvN_LeZAl5CMw9V0jrlDumMZdYYtRJCkeQ7fnnHhkH4Baf5ueFV6JNTwOKnEKiZNN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
سوزاندن پیراهن آلوارز توسط هواداران اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95345" target="_blank">📅 02:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StR47lTkEmVytvmLax88GiwIvaZzqiiayFfBqbZ7r0ArDCjfPhmz-WTr479KPDbp2EWddoQTm2ZwB5dU9ujMnVSwokeBn_MRZd8AWHcx7FwHq9pfT3b70sVEE5kYN2p0O9YQ6uCmEbkaqZbobdMuONTKwNvLk7XkGf0qWVIr9kot8bTyTrDY-tDKDoeK1zlK26EoQvql62HsvZ7cQVHJ9r_lzO2RdQ5Xlowo_-lcqFLCjaxgXxR7g6RixJXaQa2c0mE6jQUxdCHM-9vZMi7Xe-aLKLHDvCZqLTamsAV4kDJjhqr_Zu7_kbLLfo_LFxvN9eerWhbSTcOSBwavy7wntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇪🇸
❌
تمرینات دقایقی‌پیش اسپانیا بدلیل شرایط جوی بد لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95344" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
تو بازی سنگال - نروژ هم بارون میباره اما فعلا شدید نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95343" target="_blank">📅 02:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95342" target="_blank">📅 02:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95341" target="_blank">📅 02:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am5UNt_lpGrR5jy9v5jLmT3pvrmGZTSljKkMtlQSLMEHIqwBBponyIs5i-9ehitNzWu41kG2zEUfb9niKO1xS0HnXPptejnLdFTHTC-diez_33spu7Jg9hwbAFnsP-cgaTVjzqUJSxMa-Xbe3mdk7GvfdSBgQLzZl-n9IS9jnfGruvUBgCmn8Qx00_QS75XIC1SFjl-sUKhwpygJKu9pkhOI-UUpZED_1onKrFk3NEfN2lMUxhpLHy4VuCn5zWOvn4THeDywb8jANR_KZBebWIm5E7oNcxfkBjGBCHewWacssbO_UigB6GuHdgXk5yVdUa0t9vr47xiTLYOgcBj1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/95340" target="_blank">📅 02:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
لکیپ : بازی حداقل با 50 دقیقه تاخیر شروع میشه، حدودا ساعت دو نیم به وقت ایران بازی شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95339" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95338" target="_blank">📅 02:09 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
