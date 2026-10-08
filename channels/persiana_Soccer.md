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
<img src="https://cdn4.telesco.pe/file/bC8nGo8IFHZlc0sW81leGcvMS5Uvexffysfy767EXYUttGequJWde1AnYyJ4EFza-qJg4jn_YCXxZpBweT7ow3qkGDa73zsDb4gakyBNnJITcYnse0-XBk_1mPBHP-aBn-f4AvAoNYqH9G0DuPIULpmVKDh81uFmmOghuehFYdDFayqPbBhBB7H93570uKy0CVu5wNxOFiIMkvC0D9EsCDVEj42eOM-ciPx7J6VD9T25lJIAj8o2zJtaYg1TUdonVqU01b1-lMUrJKnpiQ8CMLi3rUterJEgHx04B7IEsA4i9rHjQVfamwiWXc44uwhCYw6qeo_HjgRdzHsp8M2d7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 496K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 01:09:45</div>
<hr>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om6yiWgUfibJjwO_CEdCpLhq-_FNWEyN9679eby9waMcFmuLPtLsgTsGLdIpRJBeSgb0JofNLgiMR5X_Y6qjmf-izX-sMemkcITpvig-jLEcbCHDN_xqKU3c0WOjs5ZCp_W2wE-W8OnzeD7Va2Mf5a6c0sp0OGxDPE7GgEccOYgbVXswx4RYODDlXN7if3ZOh4oO8-U6Aw5pFWt3j-kG9ApjLb2exQH52NkL4-6wJ3YDNXjCvfB-bmexDt4NI6JoEp6OxJrpidKC2UzjLlYfMhuKIT5hRA9-qnvkX8XSFWaj2taA5yDoepSBn9edMMcMK8bYVYLl5P_Li8wZ4wvNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Fh7Hs-2fjnKzjxTVjq5e-5LsgEzcQUut1fWu64zYBl3YGfkBur9c2ufOM_mITBs5QtrYRWw_SR9DaPedIy-jXoo-Q4gd29Fb9IFb_FDtezwrIgxJ72gKMsekhJGH7pzTUXxw8I3Xw3lJ82ucYhVG9j92gXr33iEvGH3Nl_B756erGrtqsBGxQJmcLqzyu_ZP3XkOXPOH_gKGCdC24dDK0yKBXehRUBGeLR5h-6YYDrlIKshDZ4GKULbcdfLBNYls2hsdu4HEdsZVEIBH6H_WICzJE8VU1Vlk6QjIHHO32qGjWvsygkz2zx7o5G8rw6wvElQ5gUh2uBe4hTN9jzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAw2wNidsLIR4VLLl8gHu4JnWfL9SEtar4cuIDdO3BrsKb0_Z8v73CfyWU00l7O5Oq5qF5_UbcPTM2o2IZwqHpb2rvPsLQZ1AETPjqiiSo92xTRVH0AuSdS-tOwUAusqYcZd-r-AY3_fotja_6BouvwD10niTMlCU4qZwwrgN3QJO3iglohkx95F33ebhFkSnm-k4VXbX8D7MHpC908985zTHWjYXSPbk_z0rn9pBRVjt2eFebY_8WmVYwbpo4rJSMVuTJyw95BtroM0OiCIU0r75D74Vbm87Vf4Xc0atyIPNxHz7g6qea-s86yJVT6GsvtNsra2Te964V18CJWJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_EgsKk_5PKAcgAfyakOJDWbkC7ldgHDr5BsYH9RQyfAFWYGrFyW-jSa2-KiQ0PneSq-tB0BMLRRa2yI46XYe0pJsTdheFIfLzQnxUnGo5ibGEkCCWW47b5L_F4GidFv3793f3vcYGrMbM6eEp-R-dKnuIZ0cE6EXjOasHQQ9CV30eUKjorbpraijZyL6LdxeR8Mr8A8BnRowTlZSA3fVoNs6aqxiZ0Qd0Hl2ufu8E4cTNtN8OvRYLeoWb11MZW_AAZ6Ex1fKzXkLfubjp8-wNLAoOg5Ui_fmVdxlp-QcLAnfZ-vUH3ByXREzUwMfvSzUreca1lHc74vIFhDBYZvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upsjjw6-k-BhnW875Dx1XPNB8F_zYzobBAIzlDTP9wXPW4NuQo_C86T3qZTdd0oYWbYKSuxL3uKTR-vHGguiPRbFS0y0haMrzKhaCjYhZskJWKJZXLwv7PkHcxdnZbpJTUbp0mJIpjjNo5V8w0cDoJEhz9dlg8wuHJdSV2ijes-KttAsHVTSPRq0FT772JE1rxsCKd2ter0yEhbIrRur0wVpsle6KxiRNZi4bnc71nNKd_5eSY0i_4aTclo8NsBGwJYVN0pLj5HpkyOd-sJMXxI7XLiRGYrmUBKGy9vxm0FI5joWmA9PeyYjNzDcue5oWSazrXGgAvgfmQktCIOXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSUENjH8-aLB_VQM-igD6hfmwr18DAATJus956WBgUL93cQdCatDlhW5aGFl-UegfEJv-BdX5mzZHef9jrWlwGnJsIQvyhGlCDPx0tOUpl4Q0zjqexq_GMayJab2sfTH9isUBxAfcyUhIybo3I2aDzMryH5cuSquvF_ZvKq_d-uxaKjjuU_n7mPsbYuO_m1MAokh6x-5cuxSmH--dqeFCh3jHT495soIy2x2spIyOnoHdI9jo5BhBssomvyB_PsyHvIlH-GVVtNN9svdlHDcoEx6L6gttmwZOrnwQhTu3AUUKYV-Ry2MS9QAEZeqXPEnOuF8tQ5rOfP0GtMKG0IVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpR1m-y0nEzS8JwnLYZ2N0O1rGFGRjR0o2uXEy4zA_HFeTzRbXxO6dXJ0gQcewUQzcUNHqx6M5Yw5OUEUcWy2ASaD-gdNE3asRCragfJDZhVJgR1qbRW2_JKDdlRZDc85FbCswvD_WoC4qtcTeXIc7iWh7Ztjccu9wKylUNr0h1fXd8MI_HjBrbdAJPSRVcajza6rYS1__khH_fnx9sRCk7X-sepFGKzupzchAjDkz5V4bw6_WSRSOPyV54oJ2P5hsQQgcNDm-3IydDXqvgWbcWnzsw9MzFraX63Hg0T2fCaZ7prfeOxMtsgWI0kuVgjNEAYeuw13w_EsS8m2bpOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=XBidfChwVa0kHEnbwloG5QhsYIy9FCnlAyO0ZMQH7ldZvkPVr1GjBNXgt8ZldDXyiohsEN426k6xlhK8QUAUYBK-MRuYVaw_6qkvrOdQmlvzwTPndvQPkHw9_QpJzwc6X4mvBENW9elBEZVVwvTXPZrqsKwK2jKndVmvbbzrIeX_HEhYxMGVvADUfnXvLI0PXqPgrII_fpTjz1-jWJew9RcKIMYsViYI-FKC3InYt9oBy_jEef5J69rgZMPec_DAs54qMrW5sVAMSHM6LtcwbwG63eY1wFqJW-qfYz8jqZUThSR5t914y0UuVy5C2TF3GfMMfTXCvYUypAcBHl7-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=XBidfChwVa0kHEnbwloG5QhsYIy9FCnlAyO0ZMQH7ldZvkPVr1GjBNXgt8ZldDXyiohsEN426k6xlhK8QUAUYBK-MRuYVaw_6qkvrOdQmlvzwTPndvQPkHw9_QpJzwc6X4mvBENW9elBEZVVwvTXPZrqsKwK2jKndVmvbbzrIeX_HEhYxMGVvADUfnXvLI0PXqPgrII_fpTjz1-jWJew9RcKIMYsViYI-FKC3InYt9oBy_jEef5J69rgZMPec_DAs54qMrW5sVAMSHM6LtcwbwG63eY1wFqJW-qfYz8jqZUThSR5t914y0UuVy5C2TF3GfMMfTXCvYUypAcBHl7-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-F4Sv2JPKvI3Jw6VdaDlT5A7UFatw1ydRVlZVAjsWOEFoxtqqfkF65szgWb2qT_56KnsqqavnI6LSmJDzwAZxgenQiiJ0yImBpxwLLBHBZLiGCkYfhNNwDE3HjmL9_P3aOXeKIKfJAuGcluPCeV6d4CVz5hikSTKeAiNGCFK2YHUoI9tkdpaSNnOMP-_ECoFpX6Rm3MRTWEBafO1EohZsTaorE3G3kqEYKcwspTBGLhU8QfAChSJ7uXZOPZEYMqqBWn2ip-hBSYQR6XCIvGTfFpLOULne5BYxB1xvtlqzXKEDtgRSkir4JRRNU5C3W1YGMRoVxS5ZoGU_-egN2klQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wiz7CK6HacdKc_YsuYVfKIqzyHz-bqs-8ksJc_zlySX20qDYny8m0EpBfFwVz9YDD5IiviNpc5jcUJAB_LFk1AZZRl-1MNpafMxfVw6uZx29_japZC4EYpVj-SxXYWrhZLVRLEpeqJ3_BwmntRvucUUL-gnkqQL_BfCMKb1ienB1osnT5BmLf8pfXGidkPIcH7x0BA0cz1UX1xIiEM7ByTT5jg0gjrzHIKmtkgpXLD9JJDc5_2AyHQrLurap-qiMjg153XxKgcgRkptgx5HlFI2if3lB-yPXctHOmDv3MsYK4uq9w1qoBEgueZexFBTC64KGFiqS4Adlfsynj_HidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vK2bcJiD_hhInAiHsLSiL7bBwlgclLzSMfFi0uLvLo7qntUZh14GxDgrOEupuwZb8ab0F57ZeosGs-tlpmjXdrw6hWSN60nx9SxACZQ2rMhyeU7pGPK-qhFpaE48FCeZ-JJ7j21pZ5c06TO9iJjETAJEsnmqj37i6L9h2aP2-2BU9acRVADQGVcL7klRZhEcKl0g_c6mG2cEvkq8wIskWMKoJG6f0SH87soMfOWDzGRfCvqlalCLkCP1eFySXgaiA5QHcf0-H-Pz4ja6uDMPA84Mrv-vcB3y3BSIOChkNriqL1NibuX-kgQu7o_6mbsOvWKWtb8ipMb8umgZjKpxAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=fnctLGFDE00axwLWYxAVhpophiVp7ado9CZ3w_wpADZN0Iarf4s0_gP_2O1MCgpLYLTeawsYtCJ3JuFcKI4Z4Zwe7t87q6yO9MYx9wYQ30AbbS_jqAczhSJJhB499mECr5ocea3Nw7dycSwz_RmWf1JorQrVjkB3k8XpHVXCMj8gy8HgCAs2nGO8qEbN5og9L0m-f3wRdC2RWq1CO-4CdXtjnaMoY7GotWAdmccLa1sVofPiRECuQJPHMMwxZdKm3c5kRr77QwkEcTw4HLdE3PaGCRFoSAXBD5KmM8CTOpLZo_qs1g24L9z8Gau0FEDBCnuRU9vsQjYcTTW3B9E0hYWbe4hZGPhaRT8gDDhwstNUNETXLPDigYhdKmRImcLOtb9IJSCY8A_wFygf4ovory9icR9PFdhWhqZ8w7zOQfgCK0gx8KDBbkQU0RYc6m_Ib9WYFHLTf_LZBtdh8uCoxJ959UDX0uXAEU9zCgPi3KnnODef08LIjHqyKXG2qX-5DZOQ5vNTHyz2TIMratMuw8HfTF0P9pC6ndQtCxRsPk010z8D2vkQTLLkVJGc-jQBQ-3qvKRZTCXRAURlzfQyM0O_947FQRMWUWHoec0EtI57uXsBAo2PvaUeDWWodO1XbtbWyIzwJaM5V24st_LrD2JLnoMwpAluZxCTB_2VQ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=fnctLGFDE00axwLWYxAVhpophiVp7ado9CZ3w_wpADZN0Iarf4s0_gP_2O1MCgpLYLTeawsYtCJ3JuFcKI4Z4Zwe7t87q6yO9MYx9wYQ30AbbS_jqAczhSJJhB499mECr5ocea3Nw7dycSwz_RmWf1JorQrVjkB3k8XpHVXCMj8gy8HgCAs2nGO8qEbN5og9L0m-f3wRdC2RWq1CO-4CdXtjnaMoY7GotWAdmccLa1sVofPiRECuQJPHMMwxZdKm3c5kRr77QwkEcTw4HLdE3PaGCRFoSAXBD5KmM8CTOpLZo_qs1g24L9z8Gau0FEDBCnuRU9vsQjYcTTW3B9E0hYWbe4hZGPhaRT8gDDhwstNUNETXLPDigYhdKmRImcLOtb9IJSCY8A_wFygf4ovory9icR9PFdhWhqZ8w7zOQfgCK0gx8KDBbkQU0RYc6m_Ib9WYFHLTf_LZBtdh8uCoxJ959UDX0uXAEU9zCgPi3KnnODef08LIjHqyKXG2qX-5DZOQ5vNTHyz2TIMratMuw8HfTF0P9pC6ndQtCxRsPk010z8D2vkQTLLkVJGc-jQBQ-3qvKRZTCXRAURlzfQyM0O_947FQRMWUWHoec0EtI57uXsBAo2PvaUeDWWodO1XbtbWyIzwJaM5V24st_LrD2JLnoMwpAluZxCTB_2VQ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=Ug5RUaV-vvg0yAydkTAkqzrmyuXZqBlBJBpsn7hJ_DyPuCPKoDBe1fN9kT4ytFDy8Ntk8dG-y1SQlZQ-CM3Cdij9J2WdPKndof6pqLb6ux_2QP7YE4Tt1kYd2__4NoZdw9_KfKdVArzhc-la-BE701ACoEsoI03Hj9cE2TQp0aRN2yOox9eXvKH0jTVKsj6aZ_xnNszXHI3nV_XA-BIo_LcWshhEzqBu8WH66WqL7sMnQUnOHafNi0bvRhegIqOUfRz4_iM0KU5kYUC2HMxuoMdeCYA2bhc4AGzzsaVpCRSBhg3bDsP-t2xo0HYFadU_7U6xwuMWmbomacnRdicwXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=Ug5RUaV-vvg0yAydkTAkqzrmyuXZqBlBJBpsn7hJ_DyPuCPKoDBe1fN9kT4ytFDy8Ntk8dG-y1SQlZQ-CM3Cdij9J2WdPKndof6pqLb6ux_2QP7YE4Tt1kYd2__4NoZdw9_KfKdVArzhc-la-BE701ACoEsoI03Hj9cE2TQp0aRN2yOox9eXvKH0jTVKsj6aZ_xnNszXHI3nV_XA-BIo_LcWshhEzqBu8WH66WqL7sMnQUnOHafNi0bvRhegIqOUfRz4_iM0KU5kYUC2HMxuoMdeCYA2bhc4AGzzsaVpCRSBhg3bDsP-t2xo0HYFadU_7U6xwuMWmbomacnRdicwXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDwve4ppfYWgKQGTxq-nw8g1fwPX646WulJA9Hxpbphxz_lUDGFggMvjbzhcdPENy5cpFzDKl7PEIJU7d9q-LxTxACT7rfPLN-dZRsWhzguD0nWSrH4v_JlhXxa8YcPlYgbTiVMb-eFUHOsTzwoP_aNcvqse6TFSYKIADe3neMQIthpvsZtT_kcsuqengpDgm9aXbP3V0-iQFVowWzBp9yWMqLr-g2KNySOvKD518l4pUB33GjooE2hB5CZr8UTFsPEqT7A2PSj28hNKK3qQVkVpK-q7vxPBwi7UzfUgHPb0TLK37k3P2b9AalKQN-7oAc5lJVwq4rbOXsvi5ig23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHqHpfYakhoDVTBUfmlODAtGA1NdnWm7EBK1CvNMkMO11kidqmgRGxPfARNK0bcN_7d-_E79J-wDZnitpaDQUWFruWybFBmr_VhBTw6MxwM7ibqkuzNEKDHiJfpRWSOxtSQBoUwxw1P_t25-zhs0PoKopSAGBj-oJnObXjWSpNlSUGe_TRdCjJStlZsKoqdZ4eTof8eb6Q7NUCG_tlYuK3ardLTkeO4eQuo3N646fV-saLuJmPa9IqiLDr4dooVPV1RYzfHyTEglWje7ggWPuMo3NkC8x-O0anT0oVAUuGswFjjw2F9hKnKWfQC2gAu1jtZ16vsexqArZrdsEE3_QE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHqHpfYakhoDVTBUfmlODAtGA1NdnWm7EBK1CvNMkMO11kidqmgRGxPfARNK0bcN_7d-_E79J-wDZnitpaDQUWFruWybFBmr_VhBTw6MxwM7ibqkuzNEKDHiJfpRWSOxtSQBoUwxw1P_t25-zhs0PoKopSAGBj-oJnObXjWSpNlSUGe_TRdCjJStlZsKoqdZ4eTof8eb6Q7NUCG_tlYuK3ardLTkeO4eQuo3N646fV-saLuJmPa9IqiLDr4dooVPV1RYzfHyTEglWje7ggWPuMo3NkC8x-O0anT0oVAUuGswFjjw2F9hKnKWfQC2gAu1jtZ16vsexqArZrdsEE3_QE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFMqi4p7NulyZI266KXlG0B-bDoNilO_tANKEzjeU2r62-gu3QeNAMKcJtXGzhCQZXsas_nkLeiL81zR-HLWfHqEij1Q9cYl-knGqCRx-tm72Xk4f08n9aju_IwrSFNAGBekKck3GW7oq8dqzKhIkuupw7_RFlsfYZjKtEmwqlgrdpYmX7IkZbiUcSM7iEZkrOMz9nWG_JcbW7_RMPnidwyLkZV9jed88awooFUfM2O8-vtZUCjVYS7jUlgCfTMOe2aph-2Wn8gHWhVgT8wORVuVs-t9zdSrEPtfw7CO3s2CNuxU0Ufub8RReV7Q4Bt4b8jtYGVWr3jNKceHSLyVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLJNDEmu3Ch2skcHs6xqp11KUvd6f87V9miTvKFmDCMeqtR07pVlMz0GF-cbnSEiBMPuZhcfyhGKVkQ8jh3P-QLjhF2BSkRQ_E9CwG8BjWHTuQlgOSt1qs0bGflSTJd9Wpby38O2TELoGPuUX2b_zinzuMllFEU9xl1ZU4vjzwpIKixvR7slrFqtnXsUY4gZ7dud3DQyVFh8tqj1UZpZEgARGvZWwZYnR3A5VqqHsvRpW0g-7EWwgghe1vR8m8qQpHqf6wtQW9omVO2M--IX51YqjuvK12L8hhmOlqtm-3-l2mlYiB2tItFMmydkQEshkOafJLQeynX6PQTO4BA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=acjvlU8kZ_kMgZuh1BFfOda9MRBJvwl3ZoJRnAezjf37g_o2iJUnMkOW8NXK7H1ht7Y1tRy-BWt0xNnuCebNyYKpieayrEwC-T588fUBfy9xTQNGoteAmNi_ofiWxwnlbCJje4tpcFINv3EhkJJVxbfv6qapLmzEGsvgP-zWu98Heg2aHqhNFcN7RI5P-y6en9vzsXPZpFTzQC9RdPYBPDl9eSmo01fpzk3A8loHoEbEw7BzFRItwz5WjO2X-eqBQs93qnII6lmkk1Fwe1_-BTg87bT7NOrkRsg-yVXJXw5Xsw810Km0xAHyrWwwFPutER1nLVVQqwEEodfhPoZ3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=acjvlU8kZ_kMgZuh1BFfOda9MRBJvwl3ZoJRnAezjf37g_o2iJUnMkOW8NXK7H1ht7Y1tRy-BWt0xNnuCebNyYKpieayrEwC-T588fUBfy9xTQNGoteAmNi_ofiWxwnlbCJje4tpcFINv3EhkJJVxbfv6qapLmzEGsvgP-zWu98Heg2aHqhNFcN7RI5P-y6en9vzsXPZpFTzQC9RdPYBPDl9eSmo01fpzk3A8loHoEbEw7BzFRItwz5WjO2X-eqBQs93qnII6lmkk1Fwe1_-BTg87bT7NOrkRsg-yVXJXw5Xsw810Km0xAHyrWwwFPutER1nLVVQqwEEodfhPoZ3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsC_rsAsxqwFueO1tzh1gubQqPZu8ZfxLosfQFnG6FXhSHkpEL50TYyFs8ZvjvVfu6mEtU7ogJZPhaAyOgSbbBT534uW5sMkLAjQC-w522HujyCShkFJinq2rz0ipJ9qIoNNsOMtR_ouIS_3GJ9M9Re5Yy6UrrOl_9a562xkd4LZswcegFcc-F3F71C6rrhThjb7TgVBD8orPfJZYkE4ieCU3NpyRI_USoAo7DBdwKUjtmuhyGnpfUw9ip7ZBWlrq9_Bg-UK6BqFAFkX80w85ikxSYqult8J9YlzZQu9RLz9ikEIDcJytlkTmBqur71l9VEJEmU5oNaXiSkMbe-T7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVKQU3UFImzyd5xIGGfzcfAt3ErVevc6kw9fvHDoQjF73iTKTCtRRoPXpJ1cpTM6RinqmKjSrLuf7ZY1Qx5cwN4bCXgsBRufI3KS3SvaIARJzI4bREJEdMKELiTKWHZTYI8TMLbkbNIT-jJ-6Gixhwsa5tsfj2xaq_h9HyJnseVu8uEjzYHl_yBv8vJnsnww098T-xlPV_821R9p4Me8Kd67tHWHgJ493puWKGD81jFSMEC3Bk3Wqt9mEC5EyilLqN0a8EUZs7OwEYospQIw7LPdR0zO8vCmd6azsU6sv2Q8wm5_nlM7JSiU0-NbAbqVmdhPq0xgnr3Qb_L0x9G4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXGrRlaub0GZOrrsojrW7PzxcxtV6EtLcJxhfPd2Hgq1EpXnhTm1LcO-NrVGYQybHmF2aDzqwTma5Wo16YGJWphFzZuHwoZwgZTxPKnpUCP6C9Clm51o3pyOg9zfl2ZUiEKiV0pO3RxWTOB0WwP8ys_LuqsNovwLYnTt5gzC1XsQWY2zx8aePC5PtuyE-zBp0j1evp3mLgl5Tpvx4VPY3QHIyfSl-VvuIWTNJ2rNoiyEwsNxKmNrsriFyC7aCcc7_Qy4euaKTA-oPkqPUmZCce4ZBE9mNxre4X8d32IDSooVE_FSFvJVt4cyMkDLmw3CmGHq5vpoJsNOeiXxNVWYBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abUn3iZsAgHB_-ULtqt_cR4_4tWPQPtG1AYT9ZyxJVyAnoFEJ_9L047-5bkVnjmT2xGPmL-LC7WQvT_taOmCFfZh2-fDtzrUiHzzP_tuXsbLZxOQhjJgK5ztyQjxzwZ_aoTtjFnQtCeaWuRZFRLgTOJVO-GFtqtcVINxYJfwCqm6v_OIqHTzLqIf4IyN0pbMpMXfbDPn_caBdRUsCZHBCfRezJ2Kz29F1cdMX8XruRmlgbd53N2lcP2LczQvSckPxFteNblUYkaOCRrCY-obXTdc2bqSKHgo6c71G6MrxwQj9Vt863AfeGeeMpQqeOFWiqLl6mC98UDIIqGzIdjydg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5UwhbCmReQZZdplv35jhMFtPODMOxaXPELMeo5dtETgeFHNMTSHBnmAtB9h3HtJWLL2OMosVlaWhrPHZG6yFJMvBL9jj7vZxqxzRmKGnE_qOfAgjKOEV5Jz_fw_O53lpoGGWF526XGqfWMpgq20DtQRZ6-M_vcy2Yzkft8YBzazjk4WLF7S1j6unoYCl2CHBiVx-TUQsP-fOaiuXlEjhWP9SDNmEMWFYKYE-I0mzr909264hq812dJIUlvYiQpbz50WIzLNIWddYdMLhjdSH4IIjEWTxevzQfjOid3yFSOI3GozBkWRyxJ3Y4QcWD3uSxK-_MHrjfPYu7_ohsvMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=DaQKpE5dM8LSN8zF6fYEZi6Mm06nuX4Xx2ce-xoFolAsDT3NllSTxax_lO0MoiOLoyV9lu-MLs9V0K74GAfsNxPQRpHSKw5rGq2ChnKhbKwKzMTArtkxt95_0ksjQAg3hNHdsLvGyUVzazoYtZm4PGsOzTAylDSHkUlWOO9yfvjn0z_OpjCRSTdfy0X5bE2w6rSDkaGPS9N8Vp7nw12wc-vYElywhPexI8MvIrvu3oib_F3QYGBNCQo4htuoaKB3N7r8kAjt1Gukh0B-qXcYOC0Sej3R3MSaM3hiFWUUwqVx_kf7L2oPWjRTFD4K4Z14Rx8N0OZIivnSNG8cLc3C7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=DaQKpE5dM8LSN8zF6fYEZi6Mm06nuX4Xx2ce-xoFolAsDT3NllSTxax_lO0MoiOLoyV9lu-MLs9V0K74GAfsNxPQRpHSKw5rGq2ChnKhbKwKzMTArtkxt95_0ksjQAg3hNHdsLvGyUVzazoYtZm4PGsOzTAylDSHkUlWOO9yfvjn0z_OpjCRSTdfy0X5bE2w6rSDkaGPS9N8Vp7nw12wc-vYElywhPexI8MvIrvu3oib_F3QYGBNCQo4htuoaKB3N7r8kAjt1Gukh0B-qXcYOC0Sej3R3MSaM3hiFWUUwqVx_kf7L2oPWjRTFD4K4Z14Rx8N0OZIivnSNG8cLc3C7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Bj0XN50YnqgXIhQ9pv1yd4Ssz52DsZz0yFe2zvGRarxHE2nJnl9nO165Laz9l8vfMNlXJHA12tJ9_8HXZIUXqGw_y720RSFFIunO7G8eefsS65pBcbXoScAakqAM_1tMgLzpmFHQdLzumsh0rK4VAuWfgz8STQKAE50dijuNqKSkBj4mPyN2SNv_Tl7bcUBU5y-XhSyD3kWxPRxRxLoff_-OzHP_mfNAA22raBISLYzwB7i3p_YH1G1Hgk6kNVnTPE0vHA0kPZU7q9v7qSGyKo77g_EziYWBz5sD7jBs_fMrmQ7w1PMm3_zBfGZRI-3rD2do4r2g5SolcN975kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLLG_lAOd33JpKa2V3UzQ2xbVS7ieacM24-YdJsM5QSZP7OaFNzpvPhhD3EmCHOnOehyxDxG_2TBODCmNx4f6Id9lkYrEswP_VbSlHoKHoTbE91gSrkF7EDB2dxqtYiIKO3YUMtZgACPhRMrnjDQIOTJTS_CWQgYJPvN9eIIVqKq0Nu8Ywlq-8ZE2px05hR3MAolb65SSvsK39sQBZuX8_fPxWe2MfKJ4XzlxP5fwxLgm_95Gr1kuwVE_lJxzfk9jqLVt8N5pm-H0yXF008nN864yEP6-L9a7cDJzNiJdP-tyTS6xuPGHVEqo9jSUOz0vy-1y6ngzAopmiGxs1mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmKjVtE1vdI1xuRsy8kkuoD4_T7tIxKhuGI_9FArKaiG8wYrOdmE-j6PWuyrLNpBMGlWfRw8a4qGwF1Dua1RrjpoW7CQhlv1DlZQ-stEwmJFR3fGbjgyng7UYLusuqn2vmcFx7nX3X6onFImR3fEBrb9fJUDZaYlkhHlltp4gTP75H4QQ2phH_ge_ILDJJB6rSNHAdCuJqlkJatSznj_MzFB9ow4OQ6faMWpWLkInexv58htuz2tzGCQ_or9tutWmlrvpMIDfk-DiFQItA0JF_cN0aWIu2iMAoBJ_JBcNUf2ZG_27FJLtc6oFXH3lxVRNkqxuiip-neo6iYwa5OFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ63jdLzobLayL9V01MAIcoXB1KFEosKYdMxmVGXgkUVIm2w6bmPKopSSqiIr09tL7gG5CG-4VYerfQDRBByv_wxu29ZJZyC0tV1ZBLik6uUpXP3oLcJZr9oUngVfonz8c0ZAoFolfYqTZ2IeJk2fql1MXoizpGod2QaNqsPaLt8-AQYidW5o0GRwv-6D4KzzlfjYpm2WcYCPVHIu5UXI5i679WiJ-yZFFLeBmqtemq9-ucnxntGI3SOVW5pK_Pzlj5KEa7pyuahJQ08DAoGcHaJMimQ2TVKc95B1tU_mnpRp2RfT1vS6FlWaGr8dGinvxhxBjFMKfJljZvOkJiaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp4xoo_EP0idF42-hn-PZTbS_4NYyrR4wUA9xKSUuN3aQDLWyPk-r7AKRvps3O7mwzsbftoEnJQGPBGJZzzE4PaaOZUbQUXHitP-GMjg33apPpkwXItnYuyKJPA3OE1vJIiuj3xg6At0hfk65TOlsfykaCu-P8EHvz13iI11Ymn4uJGTqrf8AGu1s6CqJaHLFpYkNzmyQxR79eCe7UKkYYMVP6MM_HJXIfo1OR2y83vbarQkhGGCDM8RPqzol0IK_JOqMS94ZR7a0P_xGbrnrQOsNS6o3rkTWhk0ZJdlxPFNNHaHFy9Ul0sdyGMtud0bhAJ0L7tlZVhwitR1s6EL2brQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp4xoo_EP0idF42-hn-PZTbS_4NYyrR4wUA9xKSUuN3aQDLWyPk-r7AKRvps3O7mwzsbftoEnJQGPBGJZzzE4PaaOZUbQUXHitP-GMjg33apPpkwXItnYuyKJPA3OE1vJIiuj3xg6At0hfk65TOlsfykaCu-P8EHvz13iI11Ymn4uJGTqrf8AGu1s6CqJaHLFpYkNzmyQxR79eCe7UKkYYMVP6MM_HJXIfo1OR2y83vbarQkhGGCDM8RPqzol0IK_JOqMS94ZR7a0P_xGbrnrQOsNS6o3rkTWhk0ZJdlxPFNNHaHFy9Ul0sdyGMtud0bhAJ0L7tlZVhwitR1s6EL2brQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افسانه‌یاواقعیت؟ بعداز ۳۰ روز در قبر چه اتفاقی می‌افتد؟ روندجسد انسان‌ها بعداز مرگ به این شکله.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31184" target="_blank">📅 15:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4rrCwIYpavfo4vIMek1sxLLLdi4DMqq-5zGx0NZ8Vjx8r8L42LbBrDtORZ7EoxpgQKR322f4V9j7bf9z9fP_SgPtdshiANM7NNlCqNX8Tv9rSWLvE2aT4pShqpL-0RLLt3BPNRzbeUzGsPB1erfIFRq-5qZTqLiYrYmDYPXlrzu7mAUkR_7Eblid_cTm_1p7LhVRz2-cXHFYFbRq6SE_hLg4O1iVn8tobXHc7jptzoMW0mD2qILWbkVoJwtnRgqYpBuhKhPzpRPGGJrORPJzoJYNRbO3c4IbAjc346id0F-O5Xw5Qag56wwKeWFxXdOALuPG60mfWitCLk6PIAHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌امتیازکسب‌شده در تاریخ 5 لیگ معتبر اروپایی در یک فصل؛ یوونتوس در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31183" target="_blank">📅 15:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JCcpFdgDA0FA-dynA_LM6nt6M6BS3ZQEgppUw-V0iosHaoiY6Ct7IAMAdsFZ7337_VYLZgfM9Yo5VXDQ6uTD8N_HNRCwguo6EQsuLurC-lZmPmgJg5nm8K-5EJr93rF73-dl7i_aSYUGrkrQkaynQ8v_OwrWxRe6R8F7H3Mbuz-f2b4tuTWT1Dc-5d_rBBipPZVZaGzi-Kij0f-G5c9nk-d31-q9BA5F3rJGZ6b1bQ6I3-N4HsrYWgtqFMxruSF-cYsgF052Aaj61eo0HuxVZSCmDzLgoejjdFYiDMAWu4nZ2Uepzm0gGjJ26R-KJSeSIKhry8kv5hOY8hUOHTPdtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JCcpFdgDA0FA-dynA_LM6nt6M6BS3ZQEgppUw-V0iosHaoiY6Ct7IAMAdsFZ7337_VYLZgfM9Yo5VXDQ6uTD8N_HNRCwguo6EQsuLurC-lZmPmgJg5nm8K-5EJr93rF73-dl7i_aSYUGrkrQkaynQ8v_OwrWxRe6R8F7H3Mbuz-f2b4tuTWT1Dc-5d_rBBipPZVZaGzi-Kij0f-G5c9nk-d31-q9BA5F3rJGZ6b1bQ6I3-N4HsrYWgtqFMxruSF-cYsgF052Aaj61eo0HuxVZSCmDzLgoejjdFYiDMAWu4nZ2Uepzm0gGjJ26R-KJSeSIKhry8kv5hOY8hUOHTPdtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زرگری حرف زدن جالب و عجیب و غریب ساینا کریمی ملی پوش تکواندوی ایران که در مسابقات آسیایی ناگویا مدال ارزشمند برنز کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/31182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjAquGmFGvjHkProacQxYopNyIxEl_UiAh9jCebB5rtyRehGcXPNoNKpegebtk8h8ZQKwGLQp67ziGtIqdjV8S68UwqkYYZD9qZsXaercvu7xYcMBz4L2S2F-h_y_0om-a-93zYWXUxqMVz1Izx4FS8DJGz4AnO_lMMD2CSqghKtajX5nThJue0uuGbVpZTBI5Wqc17ruta4GB5vjKMs_PEGKEKt9VoN1qB8fEJNsHt51unYp6oYv9eFQFJ4xgnJ6H3p4wl0xqfZ_odtvMdGjnSkREgoVDDUKtgficIKD4ZVt-F91d9UuKFw_vWbo6KlZV6xIY92wE51gLV7lVoRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31181" target="_blank">📅 14:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMGi0ydpixFO_GKqhz699dgWGefWt2Hj40SGoHiZchHkUKzZOrFML_SK_acLOLi1bQSq51oR_8CyigQa_Y1XzrMnnOhps9p3mw4PvCw0nd8_Nt6eaOsYhuLFdOA-NmZBrneQAPOSBigwf8B_aYFEdctrg2jzaEB5gcKIScbsxjVuk5bP0pDOK9nQcd7g2XPb1FqvZ3Pf14ffrDDB1ODsjQsAeUPo2wYaQyNpHoQGvczOLYup9Wpl_npRh6iyhUUOye5Vf2cltfSUE7RKijQSHJ20VcakSe70lHAMquvXoSVZHvSTLWfoGrXNWYdh3okrddI1jOplaDsYA_NeIeWM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31180" target="_blank">📅 14:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja4AzGK6C1sX-uUOwSfsXQH6gDExuh-J46S2vvG6L-id-kinIHfbt3I0e4H-jb6R2dCu_eTSP-doYAqCsReRLTTB49ZzblJ2SmWLYWJMGhxB3Jfju-DVt2wMRhAfJR1Sm45Wq3RRxJnKp6Dnv0JUkk3AksRmuVu0dXnjM7xFbkeG1lndra2wrqdCUrtniRASKjpSxfV7eKqNyNkdRY51nYd7Lk33C3e9xQ59GgO95idpo0AFxcZ2B1yUlxUMPfZpb3FnGGN6dW-WrOlCKma_X0TnnPDtE4sPzo32UoJ2hwY9_x-puu32ed0FYM7MBNGWOmIJl0cDRvrUoarvoluDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیب تیم منتخب دو قاره اروپا و آمریکای جنوبی درقرن‌بیست‌یکم از نگاه هوش مصنوعی بنظرتون اگه باهم بازی کنه کدومشون میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/31179" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4CwrmkgJ2Y6rWdjD_uRPcwNNvXYe5wWwZeY3BeLZ9WESkcCcVbYyCcgiAEzDkq9vR3AxZjolaijaATrPxZGjiYVqonhQUo8gISIcVwIH-lSKa5Oq-fc-SnDwyvVWuhhsI4F0yXG3_zUMC6qpUp9d3Hz7kU8c0ptV4q3bFFPMaMveyPQ6uDFpP4Z4YSzAE2pb1WP4jcukTmfpIRQXWxKOIturt4oNswKoerEn5UcdjCBKPuTdEZCxfa5JQPWGz_kdsxR-5-1YCutyr0RVyJoKTDgx91tdMYHfXCZ39ff8ZaUhDgyF-ZALI93S7vcWjh6Yy9YEl6W-qeUOITeJe9Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwpPvKQOW6wtj0HGnNSYSJRmO5bx6yFHojSK_jkJ1P5GWFwAvexPpa5WcDADrHJ7F-Kvtk8Xtyn3IxXyKrJhCd8dQzPSGaRYVc41_j1uQ_eH0YZ4ysH9Zayp10mh2YiDO0_x3PuZAMNf3dht3krNN13bC199ldLnI6HM2sIIsHaknu9WF18F3f843JchOKbMkh473rGbkcyvqrtlMiBttF0yO5aKdU9fh7LT3EdBL3uI3TXdnbI_2gldxxufZZJmi1k8VUrW5sMYDTiIqpbFDXGHwp1msaCuIN--ZP91DuJzq1moP9rkxperjFtEu2qLGvB6yBDFlcKPChEhuGocvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج‌بازیکن‌برتر قرن‌بیست‌ویکم از نگاه هوش مصنوعی در دو قاره آمریکای جنوبی و آفریقا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31177" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_TrZeRST9JinW3iB6wbBAEx16amX3EcvR7X_MjLhnOGT1fV-MKmgpFktPSzdjLqxEXPoaH0giIcvkBCYB5uhTB-kiWISsKM5VjDbEVqm4R3TMikv2u3ay9T8U46SFBH7nAKpOErk49NSVaTbO21WZiNwnLinMHh81Q5nJ7GOB4wRErlYrceRbtnLjysC90XD7DpLxWWzL27eBj86j1wV1haHt9K41P1tuWYe9J8Jt2IC3Z-eoIhNy0lA1Kfiud-9K6bd9uSZFD2lTKYVPM5Kqmg94oDvzitO2Ez809NFC-kpkLVOvcXPAlUQOye-Vkb2Iyx2Xm7YZHLyriI-Hs-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31176" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31174">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psjP_7q9IeNRtU-CdIZ_o_3j4yn-E1pc_4sJuyl0ZJEkF2rS7vL1knWux3ti10hJD75V4_QIr_qHx2rF47uHeqFRnHAr_646ZPw3h7aMX6NQaTZJp2m3OQRpNzdqs2HXtqLUrZ4bDEf4YwQwwlPxCDlEU160KbAPI_PHrbEdwH1rbJTazsJ2q8vrS4wY_p58moRUQHSaqkooHX646inl6B5xj3ZHaACTD2rBwa6lCyeFZJQtLHnWK8H-2uZi46vy9Zc6eZ43tcYLJJDJqxHkDYYYWip7bCe-duWes_U16C7dQoqYbCeFVorbCZpUeGzOsRKWsy4L05Aa1qS8E-iolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد پرتغال، هلند، کرواسی، ایتالیا، فرانسه و المان در فیفادی مهر ماه با کادر فنی جدیدشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31174" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31173">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=NGs0Nk9cldYjKDy9FV61_SUM72q7hYTB1jeTbn-9Fj0fbsAfqk4pKTt_YuVGkgbzVBGepYQ-boynfSjXUTfZvdbB17rZnMvjEPmofUm0n7Etkx261I41wn7glcrdvA9ISozPopwcUqpW9oZZsZ7wBq01bU44VCm3_OyHjK0DKoHoPiD9sDkPj9lDwICC8xeAtFMg-PxPYVIE9tKtdUteXKj4ERMT0zLzQ0Sax0opQI8l3xyp1QKEBkzxpjQuHgld_Imitkb7HH4nIwrvOvwcZyd039O6GHUt80YYysDxUu45P-7yVOVuTGWmyaJYkUJrWJih9OkNtz_G6dSbgVxuNXj-x65BecmQDT-QW5OYek66jSVlEnZy7qCQ1A3i-VBCVMHI6prGpWbUgokO0B27QEAovgTRSSUgFoB2sqLIQ7JGaVPAns-IeNuL4fFIGw6TaFDMgbGmUEWXnBlGeF9bahTwuKFtTm7fX0x3XDjXNCMHINMorxaiSTPLpMaSVI8Ld9gXN9pPtc1cTvGVit3KDHEL03_kymgkfGNERu42mvzqObwxzjcPYL4R0YBzh1hg7kpQP2SfBYM-3VBaVEzFJpYw4lz9H8Tg7bAALOiEmVHtOJGmf90Ygjmvc2-g4iFS8q2XkTqaONQkdGpXA3I7IYXNf6be4aeeABeGt6IknLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=NGs0Nk9cldYjKDy9FV61_SUM72q7hYTB1jeTbn-9Fj0fbsAfqk4pKTt_YuVGkgbzVBGepYQ-boynfSjXUTfZvdbB17rZnMvjEPmofUm0n7Etkx261I41wn7glcrdvA9ISozPopwcUqpW9oZZsZ7wBq01bU44VCm3_OyHjK0DKoHoPiD9sDkPj9lDwICC8xeAtFMg-PxPYVIE9tKtdUteXKj4ERMT0zLzQ0Sax0opQI8l3xyp1QKEBkzxpjQuHgld_Imitkb7HH4nIwrvOvwcZyd039O6GHUt80YYysDxUu45P-7yVOVuTGWmyaJYkUJrWJih9OkNtz_G6dSbgVxuNXj-x65BecmQDT-QW5OYek66jSVlEnZy7qCQ1A3i-VBCVMHI6prGpWbUgokO0B27QEAovgTRSSUgFoB2sqLIQ7JGaVPAns-IeNuL4fFIGw6TaFDMgbGmUEWXnBlGeF9bahTwuKFtTm7fX0x3XDjXNCMHINMorxaiSTPLpMaSVI8Ld9gXN9pPtc1cTvGVit3KDHEL03_kymgkfGNERu42mvzqObwxzjcPYL4R0YBzh1hg7kpQP2SfBYM-3VBaVEzFJpYw4lz9H8Tg7bAALOiEmVHtOJGmf90Ygjmvc2-g4iFS8q2XkTqaONQkdGpXA3I7IYXNf6be4aeeABeGt6IknLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31173" target="_blank">📅 12:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31172">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNoyY5VEroJ1ZXhL2dkK2i7SsZ7j-CsrOirtdYMf37gbsfH_LFmcfo0Xm5VPp1pKPIGqgWlOw3imO0nNE-R27m0pNjIaLQy3IxqeK3SqLKbtx5YoriyIRs8B-WDpG5aJ5C106mGU_qN9prjETH8IV0JK-b91tQ2EPnb99D9jKc-uGWnkHWq3KnwmhF2WRagsqYJTvWHcJNsS6P6hVxC0m8gwZWpiTGawsnLfDAfa-y2zp5HnD5QPT7spgrDbi0kGySDW1rwDGHQyz6-cA047Z-m3QcoSFNxI4MAkOxhBTRV8Z_dhqcuwjn33NselUPzGet9ofC_IQuYjwmX3Bi9SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31172" target="_blank">📅 12:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31171">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efee-nEy6c1gFeiu0l2u5_y-C5rbH1BCIpvky9j3vSXhHbkHd92Zwvs-1kLJiDJWxAc_apvEOZI_rS7AIMKOmJq0y1HEQcO6Gj4JRLm9l-TJDy1NPpZF114uZQOSRT3iPJJqrHiy5qNr73bAv_rrsYsGGaO3lfarrJnM-yQViyMRewWjdggWq-G7nML_28fo7sZzpjhR3byFjEvdXmjDjDM174D-tCTxtmkKORh6wOG_or4z6wjZLH7eYEnCJDSZ19gDHSH2C54cK8QnooOOSr1ovH825WcMaUKhmXa66cEt_ptqjgHQCXOMzNL_DM_bvJCpClQ6lm-9SIsb9Iet5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:
«من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود. اما می‌دانم که به‌هر شکلی در مراسم افتتاح حضور خواهم داشت؛ چه جسمم آنجا باشد، چه روحم بعد از مرگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31171" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31170">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiSigPPwAgtaW2vkwZT6zH3ytnzx1n1EfJ7sxeso1MAzoHpt8seopNupLu-zAKvr3m0nnFzDm48deoKnhuu96zJVm1wfMzQS2A2WGDw4U9Zs7NiMyY_QqbmHxOaN90-ZK_pIbS2xFi83EYIUVGiQG1noE4eVBb4sNIeqbD5wQhdh5LeXjsH2bmp81_HtyEzmTl6Y1j7vefakL4irdkVePKbRxYIFGBNPP6_eUPABGknIgXQI2RZCftXvIShXJ31PyZ9y0_isLuGmFaV6MOkEKkUM4FuryUuaW2_6QrWZQQxDsLJcbYLoQ7Xwm1mbIS_604-PT1adKxus6EQb3azKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31170" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31169">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1RP5pEPeJwrBB5NQejZzcX1ZlBWDDACHXLYn4QQbh6wOdk_RU4NcmZcq96IWlJr2-ahWPJgHfoopOoPbABbz62wkiNlWGIa5BEUhcVbq4QoCpAc7k33gDsI9-G9faXU59u7-0YG8y-WaOOATX4pmFtdmNOYED66FG3ZY3HcZ4LQZPH4YwPzILGXGJqPzQnj2CXAdqIlPL5dxFyeBNJa8nUw-pVWXKt8IVeR_6ATWJH0-RBTZGZAWbC2TfuGhP-lP9Nz0z4BQgABQl-6MgviQ044K2uziu6uWlQ7Izq6umpiGrpmPWdVD4A1GDfBvbJ5D2ekgSno-9F0nurOvXqoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل تراکتور در هفته هشتم لیگ: حبیب فرعباسی، صالح حردانی، سامان‌فلاح،عارف آقاسی، رستم آشورماتف، حسین گودرزی، امیرمحمد رزاقی نیا، روزبه چشمی، اسماعیل قلی‌زاده، یاسر آسانی، سعید سحرخیزان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31169" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31168">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=m_IHD7eyWTfAxE1HOG6Jqq6gGA3onjge58WrkxcpMbRk0ejakAwkyBimB_i5H0GVXRqXfzJL60T43KCYLxhtVL-J1o_0tMKHp4iytWUyp2R7CS1gsSuL_BU5hZLrlsHdnmq0_k69AnKdec2PyXfKou0_NW2gQ7JYpaCJT_nK_lPi-bT6rCZyRqqc62OYdunHSXvkfDcghgNZY_cuMEGG8bMXtriqFB_EiXzOGfMnv-Tg6H0UJBH_NHfY8AbKAglfoldzTdWtK93e3CHME_pwpia1Y-w9WxEvNaakN9-Md5yx4_D5uJPJmhZSU5H2N-qqAGf-Ju9cbCGWcpJkAF51qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=m_IHD7eyWTfAxE1HOG6Jqq6gGA3onjge58WrkxcpMbRk0ejakAwkyBimB_i5H0GVXRqXfzJL60T43KCYLxhtVL-J1o_0tMKHp4iytWUyp2R7CS1gsSuL_BU5hZLrlsHdnmq0_k69AnKdec2PyXfKou0_NW2gQ7JYpaCJT_nK_lPi-bT6rCZyRqqc62OYdunHSXvkfDcghgNZY_cuMEGG8bMXtriqFB_EiXzOGfMnv-Tg6H0UJBH_NHfY8AbKAglfoldzTdWtK93e3CHME_pwpia1Y-w9WxEvNaakN9-Md5yx4_D5uJPJmhZSU5H2N-qqAGf-Ju9cbCGWcpJkAF51qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استایل‌جان‌سینا و همسرایرانی‌اش دراکران «مچ‌ باکس»؛ جان‌سینا و همسرش شهرزاد شریعت‌ زاده در اکران فیلم«مچ‌باکس»محصول اپل تی‌وی درکنار هم ظاهر شدند و توجه رسانه‌ها را به خود جلب کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31168" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31167">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=M_cP_v8NG8VBWfudFAxhT7sTbHbI7Lt1GBJicmLtY8xatpMLREwDKCWtFqgETISy8qQBwLd2scLGofGrR-dvnozo3xBnbuGuHi8DWjrOrEko-52T2tjEnDpnQWhM3-OlAk7xWoTOX7zx6wqy_Pu5FnaYqAhMdsJmuuJY3No3bv9fvd1TCvL2MxX75x8b6UR9a0uzk_FJhyRPeVUKBZOqQZOO9rWDLkw-27lGlBKB4k6A0yGzT3bLVm-fVZZWLAuNQ_QtntF9eoGraqnGAXSy_4qhD7lQJWAdnBqj7gWULkE3IkfY4jLHRjXQzaWm2TwmiYvsDQA2DaXQY7NDWzRFZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=M_cP_v8NG8VBWfudFAxhT7sTbHbI7Lt1GBJicmLtY8xatpMLREwDKCWtFqgETISy8qQBwLd2scLGofGrR-dvnozo3xBnbuGuHi8DWjrOrEko-52T2tjEnDpnQWhM3-OlAk7xWoTOX7zx6wqy_Pu5FnaYqAhMdsJmuuJY3No3bv9fvd1TCvL2MxX75x8b6UR9a0uzk_FJhyRPeVUKBZOqQZOO9rWDLkw-27lGlBKB4k6A0yGzT3bLVm-fVZZWLAuNQ_QtntF9eoGraqnGAXSy_4qhD7lQJWAdnBqj7gWULkE3IkfY4jLHRjXQzaWm2TwmiYvsDQA2DaXQY7NDWzRFZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31167" target="_blank">📅 09:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=uxTj4pL2vgWjpyTdGog2MDQDN3C9eoz-6HhanFQL2tywhMC4JSMQUgmFUMAmrO78tIW7Lcp7Zr0LX7rVUZ1lBew_CHEmXCxJs5H-RVb4lTHNYtxlabUqGRMsaZcvTrj0Qq_Nl2GeECEwtlWKO2CUdbEApiip8m-9_zTdWhjbwARc5ixlTw1m7KMZGGt1xIZi-vV83lP1RpO-WfB3GhjF6v5rAWtk_RorfiHHAk9qhacwWnij_uddt-y02RFthQkszfz0cWJ1naXLVXMAQXNs14JZ8c0wkU96nZaAwjKifLJdvo33YoQapkiwPPYdzVZ0f-UuMl8EM75zAyIL6UKoFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=uxTj4pL2vgWjpyTdGog2MDQDN3C9eoz-6HhanFQL2tywhMC4JSMQUgmFUMAmrO78tIW7Lcp7Zr0LX7rVUZ1lBew_CHEmXCxJs5H-RVb4lTHNYtxlabUqGRMsaZcvTrj0Qq_Nl2GeECEwtlWKO2CUdbEApiip8m-9_zTdWhjbwARc5ixlTw1m7KMZGGt1xIZi-vV83lP1RpO-WfB3GhjF6v5rAWtk_RorfiHHAk9qhacwWnij_uddt-y02RFthQkszfz0cWJ1naXLVXMAQXNs14JZ8c0wkU96nZaAwjKifLJdvo33YoQapkiwPPYdzVZ0f-UuMl8EM75zAyIL6UKoFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJQU-y5Z3AvpIWA2Umx-O6-pmJw65c3CVStOwWePIDxIXhkIOaBsdnBZ_EQGMVAFjWxO2TMYnrXb5D9_VhxU5WFZFtQJgxrOX_FSF_fXZ2Fj74-7GUbnW8Dzp331L8D3BTlq8K0aYRoli9Q1J5woGxWQrf0cs9HK8KCPIuZrTkQ5H_AHsvk7UPKxPwkIzuWymvQiNOf5tIWV2K5E_s0OSEmnTltih3PKF-9omeCnVuLtuV0kfzuYXqxNBl9P34i83Ex5bA60aMZOMANq9vAQksZPphcAMU9gON1hV4ixf5D5WaQgCgIcT01aG525zx3QvU6AuCfjwgOraJfPaXxDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIGFvSCZ7nex9cOkey2XQSXnhbDtBIL0z5hQsz2i0Gkv_6IFNbleMOiuuL5cieWEVfwn40lifN8iF6Y5u68Vln10xrMF17Rrz0kIbiUuwt7S7th_aQVvuxEOhP1aDQi5waycX7bOJLTMb05JBbJyDQVHGmMnlBcwZa3UTCdgNjFwahjQe5-7_QoeDh35uNpxDaktp7NhjBgcL0UpQI8Py5RBCjFLJOrRf65gTf5ut69WUXKA_vqABfq2pZsxxipRUpJbp9qZfeTrJYkMWBtuPw_UlAsxTnZ_ijYzhBaP1bBa_aVsXVkvd4lCf5rwU5Nojc03bn-5-mnK0pXEM1EMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKEHdBo7znaU3tlGQxx2pCWx38i8kZx8JWVvYfTcOFN0YjSrFqY_qgqp7uNBKBuYc2mqEgfqpNtT-zUOsSQJcai5Ji9Cp2rNl4la40sUA6x4_s0Po5c2Khus72HBlzO-az7qSCl-NYkzNrVVWWeAJrLPbmlNUD4nFKLt-SfOMmDtywU6CTjil6jJkCGhE74OlU47KRR6fTg_sAWiTREN6DFr9cIUYDkD7npPiFv6Idrs9rHNC5EDpKYfGX1OUISk73T-Zj0Jd8YCl4RM2Cw9-3v2rLEHjcGdV46_GQj5L1246oM8X-WZw8OXVIk2Xq2g2ASoQvrKi8_4P0zfNBOnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqPpaCkd4b0UK_hOJtGAMo96T7ed2YGuulP-KEtnasljCuyYZ-nq1VC5PZNct0LavFthEjD0uUlKxtmPSgGWmgKSIZJWW0Xy4RAfhD4Ip1-MGWamtgr5m-wIXXpI6KAK0o25R0d0l8JjuH3IdSipKcvJjoefse2l7Enu9qgDiO9XcPeuQOxaLq8MFdbHc1QQmbSvlXk6qsBsDWEnAo0ZV2iRLDd_WPqo8FNwjtweFSaDJcRMmBBWJE4LPhma4yDMQ2I56AhS-nn1ZMbbIky0r8D3c30pbZIZeRhx1-dNYLF_YbklA4Kgkhhb6Ad4wd3H5NdRlyGgPO8gPlHx570A4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=majchZJULD1Ji3M-1MxpBBOANIYbDo5m_756Nfg90PQOgpzz0TPkbgh596yv0Fd6WMHazoStnOMns85U6MPQ95TsXJdvs75-SE17TxrOx3RX3epyW4rgapqD-OgzcKDuO8N92d2jobQ4O-kLyJNI0wC3zIjKF1YNLIxdV9tJmVDJGXfkHEYhQgRR20n5M0WAW9ubc7GAZjwLYbCdQUZ5qWq7BQnNvIePO9j1jR6sZKU_1FNTi-pWFTT34MmJs46z4tMkiC0IoRmRIOtV8GuDHJcz6p1bEpNFRkoO_GC5C216e9AB3clSvobqw9oRm1N73NsZdJLrSc3ry24AYwdnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=majchZJULD1Ji3M-1MxpBBOANIYbDo5m_756Nfg90PQOgpzz0TPkbgh596yv0Fd6WMHazoStnOMns85U6MPQ95TsXJdvs75-SE17TxrOx3RX3epyW4rgapqD-OgzcKDuO8N92d2jobQ4O-kLyJNI0wC3zIjKF1YNLIxdV9tJmVDJGXfkHEYhQgRR20n5M0WAW9ubc7GAZjwLYbCdQUZ5qWq7BQnNvIePO9j1jR6sZKU_1FNTi-pWFTT34MmJs46z4tMkiC0IoRmRIOtV8GuDHJcz6p1bEpNFRkoO_GC5C216e9AB3clSvobqw9oRm1N73NsZdJLrSc3ry24AYwdnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObrAUvL_lqk_3rIcREvYpFXG6d9yjhQuC9bIC7bAhI4JSwUb5Q-HRvO3yX51DYQTTYvll9egtTSkPerKITgvE8rhOFI2KSrs3i2IyQOnV4ADZWHz-umcdvLbP_PEq_V27hF6FGfipmevtwzLktdDrTbEB4dcWGPT2IItZ4ewSjUqv7yD3YzQob74K6BgEn5t-6dDSWBV59QMYAMYwl_YE9LBsNuPJg1-R-_xGehCTJMbHIByDvxHKdTgF6l3jMLTpEkZ7RCtCTsq7cnQA71VZDgyqHYQoAQn0AL34EwQaqfJzDAfi_ikAfGozyhSA52mI5WIYeG38CodoefCXkdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzbiIKJcD_OezEg0Xay0pnnyXR-0IA8bBaHvrJ8JiaUHaTPrb9wRXkaZttHHfFSyGTySfcwK7OJe4lxvpYbIou09bsDRTWUIei-epCpyUKBYTYN9RHGbEwLE-PbZnj6ks5Ir2z6eIXySAsPJW0G5FQLorx-UKPEn-nXGN0Y2zjefAMMpBW6tZeCocYOW2ACg4dowZvvvywqXBlfwYI-_ghVi1X9T_i79x69VODPe_bp-908e7RFgElbqMefAHG81PeC8SQFTsJNW8muESOhHPAhNPLeKNIOuV61MXGRtakqkADyxJS_oeFsyDwEX3qOHXf8v4WKwHawJPOI7JTNbwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qODbbdgnG7TQij6_Qx0XJS3N4EESoNY3_e8KjJ5y30LCerauiOOTZgrXJgGGmoltskOlkXleCsc8lWC9-JPOC2o4Xg5v1p--8F4po8N63bnLipJ9mEY1p9CPULi1Abg_dUJB-1K8rZ33jHZ4t97ZYmv2hvWejbFt849YeKF-Qn-WWsfs4wRSdksAgIT_Ba2uEgAIvkP0cc8EjQwVY0qj8K5_CkwTRMDd46ES5tFZFHSgKE4ZYnnibZp8UW-xQxelhuererZWyFrjTKAmjk8AKvWIrQm58zLQJ_QgTfysA7S3WtMUFDQNtUEwu5_8uL3MgJ3UrVcv1d4R7r_SSjPPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ7P8NLpeCCx26PD_ndaKOvRflT2gyog1YwbfgWU4_7tocj94kDmDasEOHZ6FY4MRQyuBb-ZmpuL9Ya8JA-6v4llaCjvyG0NknxuXHRxWCJUCFyB29cTHZ9-bS3u4r5d8goXxsuJV9ciStBJT3Gvc--HU4T_H1_pKFvHq07VtW-qPS_hgh1d0Qya3zKYVmZaAI02D70-GAtjWzX7s53ZMezDqshCUHsb2wKUet-hCjfMgt3Z2X_k6-C0tKpHSLmMTVLE7xgDjchV6-vncIvgLAoD8nl4VKA5aHKH4cIJDfUxdw7fR2bzqqKS3hA6sFa4_lBz_Ky54z81broP_XRKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5cDut8Q6prpyU_m9mIZUWEvTWYuS9qEzMM98AwjtuPl63Ka0sqUbgqQ29jkdqzL4mKK0wunp-lzHLxcJvnybL9Y1AQSoUu7KYtbZ0Fkh3e_8sBPKAnqaMl7XbGRENN5zq4uDlEDofZ32RaqWKnkXhp3MFJHY0Hsznpfn3yO8R3wbM22mvubFyjAAItFqwHN_cJr930JoK6FYJoWuV5iUUcz6BAPs3i_A95pfAtJP3ldPL-f4B2QfWDF1p6pmhmY7q7GCoAIDl-SR0g_AtlcOhNBNbKiDZ9aIMz7VsDOzHfW9J3RsHnEYshI2ZcBVNyB-Sc6WppOP7kqOmDOyP8BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=AwKJYngGX_jEaQ67FelYxZMMmNlNX6afgKXq3nW7PJKy8mIGYEyKDV-Fr9R8gKtkrZc4WdwMgdJLvmLerSUkfOXapEvMbnPkqaIrA1xNe5dpnaeWesJUWIL9AFXv1jJMug35tcdQxdITVp5trMDetLa0pvYMIUyTfp4X10hZtukaPzJRl-YwpIcjmeKC-bcd4mqCgWXAwwt-Mut1Efv2SudCGWkoPaclQKXXLZU6nClFWbVQYYs6wP1sO97GVtHHJfluutBlJFbjGafcu1ygN-umD0FS6q-3UNt4tc3t-SLc336yEZa1WJH9kVnRHO14tqEn39icEXhpOAdTgzDsdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=AwKJYngGX_jEaQ67FelYxZMMmNlNX6afgKXq3nW7PJKy8mIGYEyKDV-Fr9R8gKtkrZc4WdwMgdJLvmLerSUkfOXapEvMbnPkqaIrA1xNe5dpnaeWesJUWIL9AFXv1jJMug35tcdQxdITVp5trMDetLa0pvYMIUyTfp4X10hZtukaPzJRl-YwpIcjmeKC-bcd4mqCgWXAwwt-Mut1Efv2SudCGWkoPaclQKXXLZU6nClFWbVQYYs6wP1sO97GVtHHJfluutBlJFbjGafcu1ygN-umD0FS6q-3UNt4tc3t-SLc336yEZa1WJH9kVnRHO14tqEn39icEXhpOAdTgzDsdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxMp2hmXhZP9Kq1vyjIgUwymqXZZ-m4HS6HIErm1_4-qubQSyWizq4yYsavreyvSIZoK_kHmG_0-GnbfXJPk3MnmmyFaWR0gcznOW95XtVfFtK07TzQ0-QO_kIAyerHnMXukh9tv8lJmlN5Tkx98AlE-Jra_mv8ZUHq8YrNCCsQ2YWR8Emy-kPPGe9NZpVqTp-PxSfXoroyEOkoM8E2LvS2YIB9yhaVREk-eGNA-2VFMWmF9hl8sP1d_bLvjj5_5h_2BcA8WpOvNmcukSagIjbIdx-iAOdP83frd-l5wel3esgiO2Wt8MaaD0Pa1VWw8IQz7w5qqueGv1kND1XcNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=j4DxWC6lrXjgXdB_RjDVqgbm_cKJoVHHxvUb8pkPZhbK69nuD_aa5OFvadKoms-sTEUEK-Cm_KvCaRvB3bKovOWBK6Tx4lldR7qPxs-gJIRtxQh_s2s7e_gqzxjZWWLBbvmgM_x48sRdxNZrFkFQO7bVltm_GDOmzEFcpIXUJgyaDZHGnHGAOSoGSpzf56pBvQ-PyUfvK5DhmOy1ST70zpIckH7obJI_AfM5Wm6ZU_NbexKlZUW6toJ2MSR_dMdOBIQHqEryO6OqNdG2z2SjH8oi_AcuC_85q6gZmZtqBZJYWm6pdtPpX0i6FLha_Om7tpQYfTvEqIjg7U5umlCRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=j4DxWC6lrXjgXdB_RjDVqgbm_cKJoVHHxvUb8pkPZhbK69nuD_aa5OFvadKoms-sTEUEK-Cm_KvCaRvB3bKovOWBK6Tx4lldR7qPxs-gJIRtxQh_s2s7e_gqzxjZWWLBbvmgM_x48sRdxNZrFkFQO7bVltm_GDOmzEFcpIXUJgyaDZHGnHGAOSoGSpzf56pBvQ-PyUfvK5DhmOy1ST70zpIckH7obJI_AfM5Wm6ZU_NbexKlZUW6toJ2MSR_dMdOBIQHqEryO6OqNdG2z2SjH8oi_AcuC_85q6gZmZtqBZJYWm6pdtPpX0i6FLha_Om7tpQYfTvEqIjg7U5umlCRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzrj0vNp-75VkpP78XL63qFONe1GTCVzpl4Ky1SsRiqU7QpIQzf2A1DiBvdAG-M9i1oA2FDmkJr3tsL89cwZcwULm0NKbr0PxeQpy_3z-0oMIEYifes_xxYOfKV2VMiGH71-zY9wvs7k0r7pzeDflfUGMAHkNrBQqmmVZVf3xTqkccB5WSwKl005GTJtsctz6NAq6S9RLif3yysZVsiNq6WeQUJMLwEPeKiB1YUPtiwoeOAu9chkQ9pCPH8KwLL0g3qPMsq3e1X4xgaRVSezLC-KoFJYHWjqFF0WEdDcGzdkQkJHHINGPGjuIQ6zAkDH6XrLO78QdtT9tQSReR0n3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNU5YF0x7sJUcIxQq2uRUnOZDHwfJ4yuEtoRj0y01L27STHglxM3KgK0Jvw9IF6-OvAFsgvdeMt5uYgem-5-WOaKn_RLaXDoDc4mqK3rz36D-C6HMGSiV50ui6F3pBjBuGfWp6CnMaa9aM5jJKF2-1AJkzlJJtuxnC3xP_Zib7YZM8FyFnmBk6NezO-Horb7w3zbkPRHAlVTIIe5ZBQfiIKf5wspEtR7WPPWIr2nzGKmvv-Poy95uj3jVexwpDGkmfxVqIE-MmDz1g0XaOriqoV3TpCKZaRBvSrHpkpFjDESVnrTtfih0K4rQQQ60t5X5koBy0J7h9wPoLPiiwdjTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=dCGUJbp52Jx3bHAmn7oKLXFCnDFJWvoevJwkrRNPGYvuWiFuOsPdnKUo1Bosk_7_EcfS8vAQor7Mb_iVDnCKn25Qa-N8v1JkieSBy3yIptnd3-RBEusOqiTb8RRwOk-ddOJuWpaBAwAZ6GhdsHUUEgGc5asr_5Z63K26hfco9HB72bL5xYRlto0bbcOFpsHjTguHg8cmxoqe0ZoLjkc_ZuyUAVe2Dfnus0yTx0EXUPZOAZ5Cg4YAUFp0rUEkp05hogl92ajxTlVYRGeP1HhnswG9kOxZPbtAcDg9HbHdgZor-xlSdadt53fhl6K-CssKy0lLF8Y6UwaaIhpbg-3P5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=dCGUJbp52Jx3bHAmn7oKLXFCnDFJWvoevJwkrRNPGYvuWiFuOsPdnKUo1Bosk_7_EcfS8vAQor7Mb_iVDnCKn25Qa-N8v1JkieSBy3yIptnd3-RBEusOqiTb8RRwOk-ddOJuWpaBAwAZ6GhdsHUUEgGc5asr_5Z63K26hfco9HB72bL5xYRlto0bbcOFpsHjTguHg8cmxoqe0ZoLjkc_ZuyUAVe2Dfnus0yTx0EXUPZOAZ5Cg4YAUFp0rUEkp05hogl92ajxTlVYRGeP1HhnswG9kOxZPbtAcDg9HbHdgZor-xlSdadt53fhl6K-CssKy0lLF8Y6UwaaIhpbg-3P5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWcoad8fbLlbzLR0mbZEOua3VAZIvDCsz0XvS_tFjXXQCa8x2LUiMO7-MSdjB7RB8AG_0_cWMvfZMP7_tcPHUHpsNC48VLQNyYfdzrLnyIW43sToiB6v3iNVQs4PncV29TQJJNqELYbnPXKmZO8A7qbWcWAuRzbzy0WGcO4ilqNhwGrHvzqMIXsIyxUxRfl6ITm91CVsWWjQdPS06PLjBvvG8S_tvkqg9-qPiBBqsWsHOJWmOF1MH7KyLorh6tF0SYMj1bXiu3wYRRpUep_lCs_nSb1U4PLXzDfQ66decoiIng11JUXv1dfitcZCXTFX9XL0TGI_gb_9OniKNhTwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=tVaVjHSEtI29w1fsk67OH4ozscyvCqTZY42RxV15vAyiJYKAZWVDrooXSqSMJe9hT36tMLQsf99vKP4jQb5nLAegzbTtJUmLym007B5eSiJP1mx1ZeASu2XU4hY9FHMI2vUV5IcitALmlAevCLMrDv50ULrBngUedZWBWnQIDiQOrsH7x4K3xV_t0ejocBB9EV9zBmw9t8lOgqzDHtz1LFwQOHsWvxTuLb-Z_poP0y1OcDMbAcxW4jedrR6ZOOK2TQREc5P7b86Ny5bHrNS2MFmaa5pKxRS9qxFtfjvBl6_8PrrdYV9SbwygDSh9Z_B866oieO76oV7wnChIxqlE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=tVaVjHSEtI29w1fsk67OH4ozscyvCqTZY42RxV15vAyiJYKAZWVDrooXSqSMJe9hT36tMLQsf99vKP4jQb5nLAegzbTtJUmLym007B5eSiJP1mx1ZeASu2XU4hY9FHMI2vUV5IcitALmlAevCLMrDv50ULrBngUedZWBWnQIDiQOrsH7x4K3xV_t0ejocBB9EV9zBmw9t8lOgqzDHtz1LFwQOHsWvxTuLb-Z_poP0y1OcDMbAcxW4jedrR6ZOOK2TQREc5P7b86Ny5bHrNS2MFmaa5pKxRS9qxFtfjvBl6_8PrrdYV9SbwygDSh9Z_B866oieO76oV7wnChIxqlE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=RIk2TzZ-Z2jm-t4gKKOj5Mn6w0vCdjxR9n_QGJIE2SvF5sOSS7lhdnjgLBlibiG6GhNEuFsoGepSivUCsWeelTbEmACngAdLOvI-w9WHtlHNnAKhthn2HXoXf0WtfNDbQR49zSdgJyp8rVS4vilZSmAee8tZr_05uus6DaUcts2j7ypic7XSdJyhwMFqLqTDldEeQRhVNqfSYgLDWVzFxcKge3-M-AZfAQgGx9O5k6dAph4W4JJq5E1_vpsFO8ZgiYMPfH1LHhTikY_aMhF4CAXs21p8FCXeo37qYs5YAcPfv-vwWlybOTNMS824dLw_LtrsRfOnP9JmHZ9N1sDHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=RIk2TzZ-Z2jm-t4gKKOj5Mn6w0vCdjxR9n_QGJIE2SvF5sOSS7lhdnjgLBlibiG6GhNEuFsoGepSivUCsWeelTbEmACngAdLOvI-w9WHtlHNnAKhthn2HXoXf0WtfNDbQR49zSdgJyp8rVS4vilZSmAee8tZr_05uus6DaUcts2j7ypic7XSdJyhwMFqLqTDldEeQRhVNqfSYgLDWVzFxcKge3-M-AZfAQgGx9O5k6dAph4W4JJq5E1_vpsFO8ZgiYMPfH1LHhTikY_aMhF4CAXs21p8FCXeo37qYs5YAcPfv-vwWlybOTNMS824dLw_LtrsRfOnP9JmHZ9N1sDHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRguizuymW6_AJIGqWrkyFdZ94Ghf2ecv4QSY1J6tPLqhsVjuCqHz5YuDq9ssHqV8OqHEDD9eFgQOMWRbyN2xdjsMY36j9mWUyc8cZ1E3LiMy6Y-3qLd7W5Cx-nhp69TQ7cbWVIdMNLkourHCrgCPVGiahPFVidCSWP607VkxbGXDp8M5nMp-uBeUWFyp1vgDcerAZUJsLlVQTiUIgx_sFokmSYNOWkJEVPDQq2gZJjNGgwuwY17bOBR5JswIdYt2BXWAekothed9uRlJyJBDHH8YrtxHcoPTkovJXZVJpG7X3e_UFmRJ2rETL8Ba1Hf_cXM3AE8rFA-JkYXjD6xNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=hQxyA07mG1-PUCAeaS62sJvXMO9CfeWE8P6I6f3dPdxuwkake16DRTOi-unonMEf7NZ9s_-d2HrhQQctPoWhSlzNO8eRBcG9-PiyzExdFXjfMDHCyUnxoY8CXtsj9SxVyWJY2aze6OtC5MrgCKnp0jFi2VW0RmgtnRIht8c1MlxVw43FrhnZKui2uujVjz2weYJjoph0M_VVyn7qNhtGNVfxYWj5pWb7HjOQjXB8YIKeWgq5lGKBLf3FqGhjLHamdS1Fnvz1uyF7P0Q9x1Qa32VcPX9OWnvho47fGRlJEeC06PZ8XM57O70e6E3rkUdH3UpWVkPoBZY5GZZIiw0ULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=hQxyA07mG1-PUCAeaS62sJvXMO9CfeWE8P6I6f3dPdxuwkake16DRTOi-unonMEf7NZ9s_-d2HrhQQctPoWhSlzNO8eRBcG9-PiyzExdFXjfMDHCyUnxoY8CXtsj9SxVyWJY2aze6OtC5MrgCKnp0jFi2VW0RmgtnRIht8c1MlxVw43FrhnZKui2uujVjz2weYJjoph0M_VVyn7qNhtGNVfxYWj5pWb7HjOQjXB8YIKeWgq5lGKBLf3FqGhjLHamdS1Fnvz1uyF7P0Q9x1Qa32VcPX9OWnvho47fGRlJEeC06PZ8XM57O70e6E3rkUdH3UpWVkPoBZY5GZZIiw0ULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fghlMOfi3GGj1NP_UkovSK3lPqsdqJRadbR5Qk1z8pWkzebJlPIbvBDmGR2jwYOBhq-kjMj6qH98HgBe3Zy5H-m1uqLveZH0auIALHLUTjBCAtNwK7kpXAAE1agUDQzSSztzXPzPlHEUqIweg_jLwL_XfZstHK_FiY4UDo31Bf4Ks7vvtXJjMP9BeHde95yrm7xw8wAFY1zeuCLZepcDLofzApF9ZS7WAzOxsng-PGf6VBKZc-WM4SJrtvz_hxAHbyOkO8KFDYndDWmwQlmPncGVoUM0D3TF11xNg_PL0uik2-B63uBwONDuCng_fAYArxc96HOtltDZG-TsMN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oalBzgnh7jk5JNYvwWI82WlwazU0BHFfFsAPVCjiqC5k9x59vXRQFW1ck3lZ2RQTG1Pt0Ch6cIi-wcl3bFc0PPsHRqBuqvp-SWDfpF-Q6o4G5HNyiKUCwprTr6ePgBgzv6OxMvXbs6ZK5ObGcw_iUmsjsmJ6-DIaC3F-ZZUGXNxnGlClH8EP07Ugo3ydFgGcsv8liJH5ZroqOvOVwgA3sHoWlenAuuMXPtzW_kc8HCmyu6BD9jkdaoFYhtFXXacNwcGseuVGe1y3iuBnwyirUtYjVcfOlmMpj_O-1okgJlLYYp8ApoSIY_SWZUz4nH9m2kFVBAdR2JIITZ3rj46-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=tQbZjifHTTgWlp9VNgHjjw5p11VUy1i0UN0wrqNql7s7cqs91p3CVno_F9l5tPG23OhYwOOunPGUOIT6D-ilNG-DMIVShQ9jw9LEcBC45OZuAh758LIK_S7qpLkJqHS47guR7U3CbFl2LjIWt9OjVQlWrdCZvysqbardLa7Amn-AabpmYJbqf9_TT3mjNFlhbpx1dD9aEgort_GmT7xurmwEkfM-WjhBO8-CrK4JK3Njiytickg7_To7miu6w7nLXXImT0n5z4EfJ1MNekgPeLD2w79HF-QXrjJqwpeKmslDgbk2UO5budyx0QQMWUR59yX0FejbNk8-c38oe3DvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=tQbZjifHTTgWlp9VNgHjjw5p11VUy1i0UN0wrqNql7s7cqs91p3CVno_F9l5tPG23OhYwOOunPGUOIT6D-ilNG-DMIVShQ9jw9LEcBC45OZuAh758LIK_S7qpLkJqHS47guR7U3CbFl2LjIWt9OjVQlWrdCZvysqbardLa7Amn-AabpmYJbqf9_TT3mjNFlhbpx1dD9aEgort_GmT7xurmwEkfM-WjhBO8-CrK4JK3Njiytickg7_To7miu6w7nLXXImT0n5z4EfJ1MNekgPeLD2w79HF-QXrjJqwpeKmslDgbk2UO5budyx0QQMWUR59yX0FejbNk8-c38oe3DvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nobiAO552Chy8E2cQGn1yLlgK2Eoj0ibefHMYi74AhcWbetuB5WiTy5Wksv1FJEw7w-JHHRM__YdvDcu33s9lsMQhwg5wwcVLKk49zlBFdSRaikH_SlZzCMB5HUw5_c73s_a3onGIN8Yi5ppvQmK31Ccv3VqKHbE2Tmf5-D1RLsMU6PPMYZL4QtDFMdXIJ4HrAryBvOXTm3w4N5uoKPlIeVXveNR6kLAFGx0BtLF-vSVX2XCU_BYhLxiM5B1gZtT2u_k_A_u6kCq5F6t1FTlcicicXji-QKzlhcajisNHE2ubmm-KMooGYSFkRoypLCdWieAADqyB27_tuq01Maa6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4lAGFY-D0Cd1fysXgCCzNX-7451hg3EXvZstk22_XnomzRr0yRnYgxrvS06JRqcXEapRleMNOzG566mG5avV5HaMaseqVxa1MHNmW5EQPyxA06Ud4ksg_MJPubmMoe_ijS4sP06fY3-NiF5xmNKJ6grAITOv0YqpqKm5La_JONyxiaFxQe_NifiwXxvRyF_L91wnH-OltTwLsFoROrSQW9UKc7DpjzoxfyzHwXAD_MecKhCrCAzL0psfuHLgO9RmnhKBmL1R-sRudIvQmtC9BDSusN33VZKcxmOfK5cNrDmDkkdBFGtkhuDleeHISLW7in8UkAp-DBRu9QD0mliEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=PHF1vgpTZMH4Lhez_ym9lH176DluCWM6PtByZvwoul2OkrIBb4S1UuAc8WLdOhbHYsTX9ApQsUJfIndfLd-g7YxKRb8mIWvld05xGyeFCGdCNVicERojEXgEnHRoQvMlv9fwnoxEMpKSxSmtucR7kBcIBVRAUw6eJjFIFi2jT4vxW1ojkVyKzdiXJW-GXXZ71U64f1O4vOs-e7K03IA1jqvAmUGX9_sTh6lF2mWuHIne9sbnPs6uCZjlbfMdPp9zI97bulzZ8qi8M-JClviZA-Xz6CZQW3lvdrgDLhC46BynurlFYBgyGXX2vwnJ6Teiml9KeCQAcvqhfoMcLEpq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=PHF1vgpTZMH4Lhez_ym9lH176DluCWM6PtByZvwoul2OkrIBb4S1UuAc8WLdOhbHYsTX9ApQsUJfIndfLd-g7YxKRb8mIWvld05xGyeFCGdCNVicERojEXgEnHRoQvMlv9fwnoxEMpKSxSmtucR7kBcIBVRAUw6eJjFIFi2jT4vxW1ojkVyKzdiXJW-GXXZ71U64f1O4vOs-e7K03IA1jqvAmUGX9_sTh6lF2mWuHIne9sbnPs6uCZjlbfMdPp9zI97bulzZ8qi8M-JClviZA-Xz6CZQW3lvdrgDLhC46BynurlFYBgyGXX2vwnJ6Teiml9KeCQAcvqhfoMcLEpq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=hQVKICbVOoJhILXSvNerkmfdHZPpUrhz2u6V3bIM1NSlC0YrUqOvMhqrXxHTdNwPsrZm34q5bnA5QW5djcuCrQ6mqZtQVH4i3H6-CvgXloxoAQvtTvD9P1HCRwB40cu4VsBj3ayfYyzaRNrLyPGJ0b7WE8fxbR1VH57qE0cZF7xE1mshoMdx6cgdeSpQ26qEOVR4Ko1r2RM4WhMLwkG3aS1mvOwaxWqrmOhBCQPw-fRrI4VhnhnNrnMkpYGqWIayrVfWY4C_Ky6udu1q_Hm8EXOZTJLrCzcvu2xhY1Yoi6F5_Zb4ggCDLPqT9hHEnmyR5xBYbNeLPBwusLVludusK2F4nOHtuTLr8GjnBMKU3rx2cH2SYmxCjrOrCgeHjthuKVSI5bh5eJuYbO-HjovIHftearQEWePwqTdlpMjgSz-wj32mjttAGjA0m4P2miV5iaHk1nSbyZesJ1yfNKIOlWR8qBaxfnS4SIhqbsaStNsvPLMRg_ipE8phItN1aMjYd17Egn-813zG6MgUePKwFlJZhbo7Bd1-5efkZoyPrL5KRUN3E6XvrT8e12tj7RP_8ZJ8DwlOcJsvs_v2ROOpIXThnidGvZYdu7rjcj-2yNWdeVS_lnJpE3HgAYEXIXMAmoohOhR0tBfIaWrh34BZgNqQbCr5P-e0jWCVKYvSVvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=hQVKICbVOoJhILXSvNerkmfdHZPpUrhz2u6V3bIM1NSlC0YrUqOvMhqrXxHTdNwPsrZm34q5bnA5QW5djcuCrQ6mqZtQVH4i3H6-CvgXloxoAQvtTvD9P1HCRwB40cu4VsBj3ayfYyzaRNrLyPGJ0b7WE8fxbR1VH57qE0cZF7xE1mshoMdx6cgdeSpQ26qEOVR4Ko1r2RM4WhMLwkG3aS1mvOwaxWqrmOhBCQPw-fRrI4VhnhnNrnMkpYGqWIayrVfWY4C_Ky6udu1q_Hm8EXOZTJLrCzcvu2xhY1Yoi6F5_Zb4ggCDLPqT9hHEnmyR5xBYbNeLPBwusLVludusK2F4nOHtuTLr8GjnBMKU3rx2cH2SYmxCjrOrCgeHjthuKVSI5bh5eJuYbO-HjovIHftearQEWePwqTdlpMjgSz-wj32mjttAGjA0m4P2miV5iaHk1nSbyZesJ1yfNKIOlWR8qBaxfnS4SIhqbsaStNsvPLMRg_ipE8phItN1aMjYd17Egn-813zG6MgUePKwFlJZhbo7Bd1-5efkZoyPrL5KRUN3E6XvrT8e12tj7RP_8ZJ8DwlOcJsvs_v2ROOpIXThnidGvZYdu7rjcj-2yNWdeVS_lnJpE3HgAYEXIXMAmoohOhR0tBfIaWrh34BZgNqQbCr5P-e0jWCVKYvSVvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSEuD_OHmx1qQKt57o5SatjX1LNxKlpOShXEz_FjFRMcygHMRANe3ye9Gfmxa65Uu6iaVcZOOfjY6xZTGNcKMGp1SwyWVSMOTAy4n1smfGgmNzmWQ9aDnTba6simhRbTmoxw36ys64_p0sGORsccVxyIalwcUrVRczby76sh7oxn2UaIe7sdIRFK0FWGaT8DNwZ4Y-Wf4iK8FHUuQ2H7YgePNGoupHm6b6TuY0rRlQB77TghjD10nYK27BtZhgjhojFUF6E-207ALDbA8HmRNO55t4Gbyuhw_KIgO2PB3DjrXtMETAbdOMD15sP64TpEr3GTY3x2P3Toj8eKNOCVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT0Ms5SXJ1rR6QGaSS_FxQvis9T_Gl33yOrOJ3WmybqBrH6Sd-EEakN_BPSLJaEQ0K1k5hBUz01wbZ_EbyDUKgAgqntL5iDxDEfXx9fFujonnznSxDFK3bARh2KypsLGmSShed1STg0pUzjye18MwbSVF7ms3UJJa_wrg6-409flJRzBUVRgrzcFu4M4xq543veKDw7m9JPYGDNe925jtIjalfjkY2kcFk18tH8MLL-zyaiVDoBc_oCBgwfo_k98qAZaP008_3GqMNIDdzZQ_rvQC9_9_9cUOTtfZ3gcZc9ka6jPAFZLn04XhekRotnsndBnehW2upY6Icygox8jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=Pr0TDiRQz42xwzxPAMAHAMfgPNYgCEEjX2i0JbXmBnaRF6Cy-1w3DKPv8Us6m5924JBnyIiArEZlDIPCd6d8c0nv3_1OhYXY91u9zLSBPu5NBN9uTZxcOrgdYFKJsXlqXds3Zt9KKyOu8z0WmcdJlJNTLcC7t158z1l5GNvOKo5r8TbhAkLLpVHuLlbzCe9KAofpWoS0SvR4i5cPQ3DKpLC5oPJ6wjWgLnxL-DVlA_lAJtPipGQCbYQ27f5CVfoxgce8TVv-436iea7vtOpmuhAvCALhivd3Rt1CekW7O2GZ8Sf665pZGLM_PJHC3ns5JCwkxSa2DUIfDl_DViXRyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=Pr0TDiRQz42xwzxPAMAHAMfgPNYgCEEjX2i0JbXmBnaRF6Cy-1w3DKPv8Us6m5924JBnyIiArEZlDIPCd6d8c0nv3_1OhYXY91u9zLSBPu5NBN9uTZxcOrgdYFKJsXlqXds3Zt9KKyOu8z0WmcdJlJNTLcC7t158z1l5GNvOKo5r8TbhAkLLpVHuLlbzCe9KAofpWoS0SvR4i5cPQ3DKpLC5oPJ6wjWgLnxL-DVlA_lAJtPipGQCbYQ27f5CVfoxgce8TVv-436iea7vtOpmuhAvCALhivd3Rt1CekW7O2GZ8Sf665pZGLM_PJHC3ns5JCwkxSa2DUIfDl_DViXRyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN7BQe9nZeiO5XMg7JPR7sLXqiIDLCK6NolZ49qasBVaWWl3iyvRFdWBerx3VsJUGTE5_4aDXJNJQ5LBt8leAFDifsOPq2ow0SGYlm_zBPEboDjrYrZrNXnLQFE2jDeMMows89mdu8Wr_tdFzFAS9YsybZpEolCvtTMu51RiUNNGt_kJ8w3CCau6O217Jxd-pyLsWjREDYLKoEcKLf7n8t-cLJLMj0egrCS1kls69N8IMXSDIaRtBWeFyBfgiwOsUpYDNK6pB2lpDt18tW2wgY-fufjQZJ5LpFgKu5xjjjs7Q02K4BJFV9PQ7hH3TXBcDtZwz-YgRL1P0npYOeZiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFUBLNJ7Dzs4bao3-zGOVe9AgnUvVfV3IuCcc_uf4H1ZQcsbbTdczyzTcZ4dzAPdUGarUOObHgL456aLKXkzJQx3hGei9VpTOSkDvCiyO55sJdJzDcSxjuFFlTnZ9NHo61DKkXdG-4HmytjUVs-XsZ4UwjlQ351J-5Ys2iudltdjKF_QnVYgQJLxVzIPYsZlrVOzPsRMXDkzLxaNbTSlAfvZJkW5IKj51eMOHTnJm4NTXDh344T91yLoxTpPEE4DEoeViCoehrewFFb86zTfQ3ZTLQ5Bx-qU8m5L2MYx8oV7LkRRXELY2EiO_SrdmGKWgVdABfRvXnPUNmR_7-pVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=JThSOytWQDQ9pdZlNkQQ8e8giKVC4tNNcOSF06LKfgppuBVr9SORhdMCeeO6gHNLOTBQNkfEoNLJmWOncCRbYG_ItmU9NySaUjydxMIOqtXZ2HV3QFDjSgwKUoVdivX1AdCDfjTWIZlLi4mhras0ez2H4rEbnzvGOsB5PcReEbUt4jESr6AVBS1juQxPM2w5gnNEFtf1uoZsMe2PQelur3AWsZ_FR_gZclZOPyEYhOXoA7UtaYaDsW3xmm73IU5VFy6OU00jIwKrnazYCIqCq6Qj_KDg408osG4brJmwOSuyNEXZCYMdmPuslq27MKOlyW_JInvGfVV0q4V9GrFWqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=JThSOytWQDQ9pdZlNkQQ8e8giKVC4tNNcOSF06LKfgppuBVr9SORhdMCeeO6gHNLOTBQNkfEoNLJmWOncCRbYG_ItmU9NySaUjydxMIOqtXZ2HV3QFDjSgwKUoVdivX1AdCDfjTWIZlLi4mhras0ez2H4rEbnzvGOsB5PcReEbUt4jESr6AVBS1juQxPM2w5gnNEFtf1uoZsMe2PQelur3AWsZ_FR_gZclZOPyEYhOXoA7UtaYaDsW3xmm73IU5VFy6OU00jIwKrnazYCIqCq6Qj_KDg408osG4brJmwOSuyNEXZCYMdmPuslq27MKOlyW_JInvGfVV0q4V9GrFWqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-d2qR2NVfDAgRARp2BSa110VUvR-ufG5cDyHQeYYRDCdhtuJChc44U6qWh1pfGVFHupCRa6OjNk8-Iuk-CSpIZ1j_BTK5soE3G49MmwKUv4LdmbIPGU-fT7OfwWwYTXBxssZPiPsn_Gu2GpExZwun0m8qMEcL-y2S67kaMWaGHzCCHXeXQqB5tKIkZqokKlzXtfCswDQOURr0_Isqy-ycwx9UfZWEltAXKsl__WldEHDGQadnmyDltIivjjGdISje9mvMwntNbvahxuX6ZbpSYWaTvzGwbuOrTQ5Ubx5DzawCLPoi2FkTAzJQ32cn5zm9yOe3QvujNITEBAk-Kjkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb7YS6dhmWEkQXv__J10pUFDytoAZu5wJG5vF8SeR7hUYWxnojgQtVRBMkvYFPxv7MgdT3LUjh_YDtQJFosTHk_f-fg1dE95f7CLai2t_7PQ-NyUj7PLqg3-PGCpClVarM-y6oRkzeqs10ZW3vvTdWIujRHpNzVPRp0WIff9jU3qIwQmN_P8Rf6wHdv3HJF40gt1P-ieQ6YiX9oC2NGIPIM-qNSXXfB5fNswX9vdDJWIydJRefr29pcnky-DBaKEvlcYlikXd6p3T3qfZWiyklubQBuAGFbUYFtE6m35TkFDtswBYtEHIIsiA-Q9-0OEQ8p3ZmdMx-7ZinyEPd8J3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN6w_BGNRhpNJ2iI_BoqHT6Rc5PmW45-t6l7xIlHS7TFdiZeP_jvRxk2-WbKAh99smzaGKi9Eb6xinVwfpDkTcMVP8SQz-OYD2WVuujwukkcLLjSBELECplz30Jihf0XWfa1aDiGq8jYSzpFqAauq2uTgWklWTzN8Z1kVoK80dMaGnXL67qtgw469Vk9HfzZ_Temg3qK0Jxorl7OqfnKDShLUKHJpdz5iy8nX_2iw91MW73kzPd41MXIw7sgR0fkS8gl0f8hCdb2on1N4PuJdTn22GDnvvxlscexdMQZ_iCmUhQkVlejtcJzxLftd7fwKTlkGLS3E2l4FkROy67RLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR3RXd85dqE0ulLLZChsJ5t-JTG1019TVGA0Gp5tUhBly3pYa1jL81SwjUZPMB-8BSGzNFzjD6KByQVGqZwhLzsb4NU-_3rEFt-BKmUxVqakTRnDmto5NyIVcGomKn789M1Rzo7YXZGKnqeuxryidkGxwJFgp1dICMgRctFtIBacVHYPdbxnz2VzlBdCb68L7IT2v8ppJx7DhcuY-NGDDUQrwTCtEYKk7379VhFXyZyKpkw5QmcOSOfVZw0QFr_GCeBWWhh9ofpJHp8woLcZGiabL7ZLKcU-mDZ7s7MlGLw2i-wRr1FFoB29_P0JzoM2swGc25nUVOG93DWaEJd1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEu0Kv-D45B0z2StyQ3Na-mPl2Kgu99V89JPJToGoIIzsiYdFZcMWzh5sBsN6ZqdO7xWo4NclRFDNjfXMzSbhQlmGffxDwtg6zAfarvRwz8FsgDCmTonAhZAlFnswOECHKTV2farXtNkKdIUhWSKgSmN-Fwlm4IWgKwOc9894y3d7gLPPLA9XyW_D09L_hwnCNH7W10WgpsZEHcPIv0MTqwY82FFY5MChtUv-217HrLBn9I7k30aojfoMGkdakwWaz64qOS9rktKx-vQTEuf_v1433AEstSjGEnS-R5K_lXFDIrQ4BB8ajkqZQ5_4iQNuDc15l_maqlAw0gxq4mCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZmmrwkpniMXfOtMDasmo7DAskUIune_bw3wOEvBt0e2Eu9aHd1YAuM6GhvzpUqjiUGZivrFc4z1yQ6xIfRi7N3LZH6sXithw3xXaUkhwxsdHMYmqOSTi1jWdRZDt26xy7xmIeD_YGsM48D5252w9kZJz_w1oXkQoNvkU3wBtUO99y2ZZ0fOMYr9za7YCPtOjb-3ep_BTdLXxQg3Bx2URS3oJ_-fCUzGsBgAh2tZV6kLc2nnlbWK1FvTucfFryYeBl5mtgApANZQ67UlknpbmvvmWAwuZHHEApXIZ1sV7akr7MbN5qV9mQNW7Pr6wtmGDhxSqk9-Bj-BcWv2rdUgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLaTtXzTZ9ogphm3Fs1OKGjVizpPhrYsvLwxonS9ZTVHXeZJdAeRkq6vF_drJPBz7D6ggJKepAp1auby3w0P0EpICMVSGdRRNHDwV8jD8dKryrcY2tUXmZUvJv0u67Fr5-vru-4g4plqKT5d8h3v7-uCLn-wk2eeAFBdKNfdse6xumiSPcA3zRsL8OaLcwbZB9igVU0gBMrDTJ-G-iWHqAlmf_ekatdBeyOXoBEhPCoYiFYF736XiGlSeTm8ZdrrvhTOcJAf82GAQChJeXw_IAwhRPH8fUvG3Ew7hK1QalwddlOPF4UCXMVkbcy_0JOD2P35-2Fz_dfJMDFYv_BTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwsmIb9NBJkiV9Fbe0yKQgI9GBnL21XG5a7lS108PDeNPeH8GEVS1XSdN9YSV3G2jMK_bcN1dRxeueu__jZ6OQCLjGA6Yxgj2vPQW4TgrEztA2rH7NmxCGAAqAY7UpFqjBqIIWCmk0g3NpMitbCRPHf2fpsuPGAB-ZMbq3bDW1cCAC4Wdh7QD81C5VEb3KftXumfRTYSx4YoA2aNtVqH998qHi94kXN4hf06qDj6NU4SBO8IaxCzkyq7nlUyEjGU4E3lXXZg_gkD5B8D4LtEykl7OwJjyoR8FlYa5yXjn8YbvE13zLSHBASPg_w7SxqLdlQV-Z3q2bxQf72LE87pZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
