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
<img src="https://cdn4.telesco.pe/file/rwRXE1YMoSXfC3MCErMvgNjK2GwHN0_EXer3tsTz3_mxciHhyoE8kfc-KZA3-h3z1P3H3FdaFH4DJJnU_8DAfDFKQ6ZZ8sqzm41S_URoeYDOKH_dlgqo1R0R3X3nBlGHaM3VMvYB94R59THqH9_dpVY8EGFjMM66JF9xpkbW2NNH_sKSAMrninP45rSflDU0UL4tbc4OsQGs88TfuPUJanoHK0Cy0x4TOe1vOoL-OlCWSjQzt0SgH_wjUuUpLXLpnXTKCG1ogteTACxxo-qn6Y3SWHuj5ei3o48Sr3sI2WXPBBvaHKBk1kZUP74gp8oj0M2vKZPCKoREWKqDfyC8aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96Cylua4WSBm4lBT13xREJimfg3cRtT9ijJRN-QqJgwBgdrpXxKL6pFEYeYKlusU3G3j7TWGtOZS8IVHyxmjHSlU9IBEgTsAf7oxG-5syrClWWMLP8FLTXzeFoa47Q6c0EJGDJDUApE_XYa4MovOtRTh-DBwP8zExW83iTxg0rSNSz9Z4hYHcgPy-2o1yau1UL32N773jC-rKGxOWXcOcCalI-hR4lzfe0CLDYtfP2eTJvbtGGRGJgfQ-GJAueUUHltKP5kJqhIV69OrzA60BH0CTCiln-brGwAsxI-uOozp8Vh-bNkXaYnXbQ6ogJkfFTdIpRdJYpMvGjQNW1UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=YZLOrw_HRr89ZAzCut7tIEnwFmHpapY-KS7dKf3IuxN9I3R0DiDPgPjR52gv_pzm43EuI7o14eRo8SOUdkLHaYPhd9mvQ2Sawyp3Kz-ozYROYJ2mHoTXaDRM4xbpoalYH3N4RTM2UwHxxKJUZwyfPW6yiuVM2Sq4D-OmAegqOvnz2HZkx3LXQehSG8CnffPBI25TM5NdWaDPFdX1FCt5i5M5OPR1nAkpPbdNn3zh5X6RrJ2GGxKPz6zPBnpGNpnxdwOS0rjqQaniDpeIzkp6J3Mls1qraqhtpk4_XaWlZZmT7eZeu9NMQBMgRaPrEevym5VkSmMQMpVJFPpDvga3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA5T_yyIkebjp6zSipKKrT8OrtsARS3Y5P5UQqsXqZQdiUYxeR5CtUu4thRTL4RJ-PpZUXPH3oi8t6WGaL-o__k5KAk239Sr0cRS6N_A67wz6CQ5QLuiAjyPYhVquaCpI0jScD77iIHFbv9B_f19iIke7L69Av_aIm146MFGdq52s_q_efk0ScjO2Zk2xwj3DNqbtKKta8irIdWWL6M4hCSOhQU-zAjFdJs3BBXbdqqxV9bEAQREoyv1L_ivy_3mXJnTz5pIuw1ToIt6VGyo9tb16ruMYyJGFeginwdJO4UumNet8L70YdScmwGYToczalz-bJBTIWKZtGIlXg1H7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOrfzogX6pOjWFyW7RJD3jCzvSTUb-UOHLjCm107W7aeSU_d4aO5f4n4wxud6KT7xrPSNP5Uy2xeIAL7dzDXsT8qWH-cplxAhRsWqbGasn9jRTPDdI6k79vhj2e6o7B_2OfSmw94d7oeM4RtxM0wGFMOSe-oGpiVCo8mW2r4mvetSGYNdFW7v7LHJ1RZ4OaDi_cTQAY3FbfuZLQ8roGtrnFEW74yZMqdgRztNZkgxZlQkhWU1gT-0maezJ2evgrABk1UbsIC_RbMhkR2MJYa76y4-DAtux58iU4fb5WmvpDtZF9soNieuXwuOkzo_rwbR_9mC6yUhEM5id6M3jH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu1jHfZ4lQag-DZpc3F1x1HANykHfQGv877OZAMVBUG0lwkaPHL4PBuorkNhJjN3KarqMtyDOvdrSyYBOszzp3AHI0FMJFSuizNAUfhPuSBzONKoFEsJ2Sj3XeV6zLlxnr5tmPH4StKpGFmcUjFv0xVt8ulPY_tprIlCjpg7wBYP2tKqwZgk2RrnZVn7MU8EqmLE3jpJOViXD1zxeFC-1vqpbNBD4e6WE4Ul9Yj8ziptEbehHY39M0KnA3qhiHz09978EzxkiPYh8SgbfnwUePPcGz2VmKQGgUELfqANl7QvV3veynIrGvO3UoULKvySqemTf83L5YKLBYTO029sLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofuw06u4krGBSvDC9eI10VDxAGE4yTPCNY6CryVlXo2DZUjqPKGkMK-phEGYaM5St48BihhFVj3-_aIIEicjiCfknMlrj6bhPVsk0d1Dlf42ycT4gGDTHsOic1FN__yuxMEAh8G90Nz0nLvgEHT10iambpx8IFyftb0rXAtPuBgI0oQOr9Tq78vA1ybRA1PgDGtK6y11jSQ8YtViI2utRVIBhRy55sjkMo2oe_En9pXnfDFCrJv3YUF4J9zz7eUvwoG0eaena0ZANj2TByrJ73YRqOGrjA4S6kQLjagps2FVhL8eb67rY7jvd_-B6JLF8q0Qpa0HcpsVjYHEtWCD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=iipeQb3QcOCx0qufmeolY9ogkEwje5lsrIi8ZsTQS3y-nlTYWBeSBTcYzJ4aK4AxYEr1Fr0SjdAB3ziMGReZfe3PDtv1B6PxSmZmR56JK8t3L-d_PBsYuESjbAxAXJ1Vc6uT-lFaoqm_ytU8wH_m8cUnqVEUPJJ8EI9_Suqde6aTNTv0YWbmc5K027ByX4-n1kr8UTN-dkMKydryzbgLI42GAAsKuip4eBUvIIKlNMP-SUDo8D5MC3GvnsJ1-cC3RIdYCmA6SMh07Ht1_bW4vm1m04vfYU7JOaWVNQZFHmo8XuPChR0h8WS8HXFfCtJdXd0Ywg8trmOuTCf_jDPlTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=iipeQb3QcOCx0qufmeolY9ogkEwje5lsrIi8ZsTQS3y-nlTYWBeSBTcYzJ4aK4AxYEr1Fr0SjdAB3ziMGReZfe3PDtv1B6PxSmZmR56JK8t3L-d_PBsYuESjbAxAXJ1Vc6uT-lFaoqm_ytU8wH_m8cUnqVEUPJJ8EI9_Suqde6aTNTv0YWbmc5K027ByX4-n1kr8UTN-dkMKydryzbgLI42GAAsKuip4eBUvIIKlNMP-SUDo8D5MC3GvnsJ1-cC3RIdYCmA6SMh07Ht1_bW4vm1m04vfYU7JOaWVNQZFHmo8XuPChR0h8WS8HXFfCtJdXd0Ywg8trmOuTCf_jDPlTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
سپاه: تنگه هرمز بسته شد / به سمت یک کشتی موشک شلیک کردیم.
در بیانه دقایق پیش سپاه آمده است که : «در اطلاعیه قبلی گفته بودیم تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت.
ساعاتی قبل، این تذکرات نادیده گرفته شد و
چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند
و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
به ناچار یک فروند از کشتی‌ها مورد اصابت شلیک‌ِاخطار واقع و متوقف شد
.»
🔺
جمهوری اسلامی به زور میخواهد که کشتی‌ها از مسیر آبی ایران از تنگه هرمز عبور کنند و نه از مسیر آبی
عمان.
🔺
آمریکا از جمهوری اسلامی خواسته بود که شنبه - که دقایقی پیش تمام شد - ‌به روشنی و علنی اعلام کند که تنگه هرمز برای عبور و مرور باز است، ج‌ا اما دقایقی پیش آنر‌ا بست
.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhPBUnK9xYMDGrKWPVczIdXDsvmErfoiPyk3-B6pOd-SEcqAVtUmR2Hi5Venv_hxlVu0Biyb8eAedL5jKszzPVxKjIk_llWSJexorhMtQMn2jXvM8K9IbvJsB_bqaWfO0_1lKCEQ1UDrvdGezAhoFAUzvWGR5mFVQrV2HuzyVd5iiyaxEWxcAE6IW9G_ZsUwCmTL05VzNRqhIPtlkNmPyKLbiVwvHCDZXmYWDzKDqaAnmaftj4Uq7THW7z9B0zrEQfqAm6Bsk0QuuGSxXRHNGqhWQPKSpR9Nk9utXPToN0HCvGHsZkDbOkxc0_3WSufOCyxmLcU-uPRF6C8rY2flcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=ci9S9qJ0rnRN2p8n_H7O-doTswKODZxDslP8Kfpd1VqKrvfgtysjAxrafleYdf_DnJ7spYqnDjGkvhjSVPpnL40iL5nw4fy89N6eOYNzgJZ1z6TD4F05PGsjaWi8305fRlAzgacvKVae97UKj0UCrV3eLngBTD1BI5sJcU-WUMWOuMRUsgCOliShGM9IZN7sapHeE2p4n5UXNE2_kuW0rHMmthKfcYvNMPvVyFgAdVtZQpAkIzJUoNgZGZO71ikeNTUD8oBux_V8l36bRgHFtXjclbuK_dS_c0KausyiaecX3AHbnd7NC--ZDU6A_CWiUHytQh1UrlSxZa6W_6uBbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=ci9S9qJ0rnRN2p8n_H7O-doTswKODZxDslP8Kfpd1VqKrvfgtysjAxrafleYdf_DnJ7spYqnDjGkvhjSVPpnL40iL5nw4fy89N6eOYNzgJZ1z6TD4F05PGsjaWi8305fRlAzgacvKVae97UKj0UCrV3eLngBTD1BI5sJcU-WUMWOuMRUsgCOliShGM9IZN7sapHeE2p4n5UXNE2_kuW0rHMmthKfcYvNMPvVyFgAdVtZQpAkIzJUoNgZGZO71ikeNTUD8oBux_V8l36bRgHFtXjclbuK_dS_c0KausyiaecX3AHbnd7NC--ZDU6A_CWiUHytQh1UrlSxZa6W_6uBbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbElpjGg5yoLjoLz-gUSpSedYOF8icwSMX4bGvYi0qaotDICYpmU9v6kzxYAOr4JFnF7kA9SmPvNNfH-oLL--xNXHZNELpy5GFOhaJg_WudpHxOPowUQdAkvRo2QKo0u_Xsj4bIZdmnhTsxfeDexbSoA03-1abV0_LL-xJsyZX_PU9KDmadMbLLPFso7RxU4Ji6xBsY1DOS7SQBHwX1bgV8Whv2IcvJRY-FUdhwMHcrlP5quHHRchu8xHv3j9cDhOkr7sqWr_wOFH9P1UOargJuQzWD77jSaRcnGhhGPDhc9BhSwQ94-mTL51Yq-28PdEK8Th8hOHQObBc8b6mjaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLGtDgx4ybodlUCI4xT-JatajR-xulDqJX55BWOrWtrsvk2ejsv8YMt1_FsPsfDB1Qk3LKEjud0JIsZ-ZEmJ0xqFtW7qU58W7qzNEVoqeg52GV1y48Bpx9B5rbXosEY_arjwk952FBEo4UfWbIgVL8w_kFHL_NX08fMqjl0fCqzU1W5GSJ10sV3Oyn4MkAjdTolqi6C2aDyy6IR6MXPrMnCd_dvljWyFuCNBngtr0fTUvmt4OMgX8yw1Kqaj0D6SpjTbobtCixgNPdP8RAfXfU6x0FTHJ2uBCD3ZSxs7wrvMJGVD89gfACaSsODTqTVWqq9dd-br9gc9Ek8z9r95Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر یک مجله ژاپنی
در آستانه جنگ عراق
که پیش‌یینی می‌کرد جنگ جهانی سوم راه بیفته و…..! رسانه‌های غربی هم پیش از جنگ، ارتش عراق رو باد کرده بودن و بهش میگفتن : چهارمین ارتش قدرتمند جهان!
رسانه‌ها عامدا اینگونه می‌نوشتند
تا خطر رژیم صدام‌ رو پررنگ‌تر هم کنند،
اما این باد کردن‌ها، در عراق هم باعث میشد
که فکر کنن بسیار بسیار قدرتمند هستند
و جهان به قدرت اونها اذعان کرده.
رسانه‌های غربی با «قاسم سلیمانی» هم همین کار رو کردن!
و بعد ترور شد.
تروری که ترامپ هر روز یادآور میشه
که اون دستور کار رو داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=X56ZdRdbFufUTNXP4dlWZPTCZeA0Upa3EcD28_rj2Qx25TkimBtzghjyWC1bgwrCSF-GZWZBmyCN97pu0DFxcYB4-Mxy-39FmpUcnvZNZLLBG14JAn09gQnWdS171uigJvI85ST8xS06DQmoHk62bLnMPHbsjTXImpTGoNyP9U54WCA0EJQFBgTSFAiDgI51JKg9LntldYny7kAepIxpJvi9Bw3O-q7CW6Xgq5WLiWXXVoP1Xd4poQjO0yeq_Rssu_KL8pfjLvyRjNkRqjQy952Y4SAd5MDQC6rxfjMlyKCcCZw4bjRnZjWAflTQNuCW-EjDOmW-ZVA8IjpKfmMYHHH-HZhaPqsLzaOhQP0bH_poHEsgE1vZX9HnsVs_HxH0VH-75NZJqF7Jz3Y7kCeClJFaTWtDshJk_mXEcXyD4AgvqoOkPeDLIFpAS2iU7GqOUSxTeJV0oMAXA_X579Enx8ntN_EPbkrvT-ddz-0-bwYjmuLOus1Qwq4CDyjwiRpK6kelMlFIO583GvKJZCXSum_jldul9ZEJEfkYc6cDuOrfsPywnx_E9A4S708D_ZK_gWbDO0yVXg53cw9hT9Zx8HpZlpi_Of7j3w9Z7FNd8gymt-Qlifz9y0_BOr4PrWUAkI26-49B0ieAM-qnGLMbR_T4n4i9ikVFqebrqd_plDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=X56ZdRdbFufUTNXP4dlWZPTCZeA0Upa3EcD28_rj2Qx25TkimBtzghjyWC1bgwrCSF-GZWZBmyCN97pu0DFxcYB4-Mxy-39FmpUcnvZNZLLBG14JAn09gQnWdS171uigJvI85ST8xS06DQmoHk62bLnMPHbsjTXImpTGoNyP9U54WCA0EJQFBgTSFAiDgI51JKg9LntldYny7kAepIxpJvi9Bw3O-q7CW6Xgq5WLiWXXVoP1Xd4poQjO0yeq_Rssu_KL8pfjLvyRjNkRqjQy952Y4SAd5MDQC6rxfjMlyKCcCZw4bjRnZjWAflTQNuCW-EjDOmW-ZVA8IjpKfmMYHHH-HZhaPqsLzaOhQP0bH_poHEsgE1vZX9HnsVs_HxH0VH-75NZJqF7Jz3Y7kCeClJFaTWtDshJk_mXEcXyD4AgvqoOkPeDLIFpAS2iU7GqOUSxTeJV0oMAXA_X579Enx8ntN_EPbkrvT-ddz-0-bwYjmuLOus1Qwq4CDyjwiRpK6kelMlFIO583GvKJZCXSum_jldul9ZEJEfkYc6cDuOrfsPywnx_E9A4S708D_ZK_gWbDO0yVXg53cw9hT9Zx8HpZlpi_Of7j3w9Z7FNd8gymt-Qlifz9y0_BOr4PrWUAkI26-49B0ieAM-qnGLMbR_T4n4i9ikVFqebrqd_plDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8-7e7bILc6ZaX6vDBSO0qRQT0ApBZJ_E_q66h4pwqJ7naUUtWGwFelzcm0MhsySYiyd_TkI-vj4aCcmVkLj1xSwE9kBEqCGhEWMXV1J-CH2NofdY7AtZUaVjao8ZHcuNsdhpnKYSwBKEeWbwSvruS1raJ_3Aal6xYHAmgyDUAWBIpfGW1Ej5qg8W8hejO5S7eKA_1SXMXDvBz5WTmOuoZyBUozmp-P5wj9UfD3pR2XNrozd_SRD20XnWqqdC9Scv331sdGjODfOgwh-9wlIG13vHpOOdRSAss9-oXMA0SeQztcUS7gdyA9veGQwC7dRQjlHnFd0DCGytfAS8eI_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4juKsg5Q9dRJHJa1NzHJChGysHYOUtJrvkAQwKO391NEox5MDF27TzRfKauN4UPvefZ-PD6KbENiQuJOzrPNoY3MIVT9Cri1W3eMYcKkuW8SV2L7BpV9ZxFsUlfnZfp6XrrjCxVuDokGxSmwIrrTgjCauR3fMqNedSXAHrTE64nFrZQvBfLXzyC2B64v2mlPF89XxsUbZNX6zwKy7cVSwOciRWhotCjhPT4BaLoqcU7bOb2UDkuopLjgXTwdDoNf0Ikcgt-BTqSy5BUoFG390hfCpyN83emPhOG9URYfAVrovFoYvPSEQeuLeFt--54ZqfUuwLG0_FJEunp768maQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=utOu4rGNV3LfnGGmg-r0_hJL1boaagV-JxrnLb6gQ3RNuSGmTP8b7EldOQyvHsLcFUuZDMOw-_QymArZeL-KdHU4N-CzCVy--zZVtVhEOfKZhM37rBNY7DTj7jZ3XPqcFwxjUcz86qRtcSI4hBVMvzQnxWKjfZvTzBwIFhptVeBHPo_LIa6xjaTM4Dync6j6bHXL4oTZZsmausrcQ7hO3SAz4Na9_hO_bcCCXF-yYG80ofXHE_NE4ItTaSo9uhxbeoeuM53Ka18CkaAJdTXxchIlNOufjVUf0aKClk21AILX4RwWuTGdKWjA17X-i7krpuSezN3f-CwDtrgRCW2jLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=utOu4rGNV3LfnGGmg-r0_hJL1boaagV-JxrnLb6gQ3RNuSGmTP8b7EldOQyvHsLcFUuZDMOw-_QymArZeL-KdHU4N-CzCVy--zZVtVhEOfKZhM37rBNY7DTj7jZ3XPqcFwxjUcz86qRtcSI4hBVMvzQnxWKjfZvTzBwIFhptVeBHPo_LIa6xjaTM4Dync6j6bHXL4oTZZsmausrcQ7hO3SAz4Na9_hO_bcCCXF-yYG80ofXHE_NE4ItTaSo9uhxbeoeuM53Ka18CkaAJdTXxchIlNOufjVUf0aKClk21AILX4RwWuTGdKWjA17X-i7krpuSezN3f-CwDtrgRCW2jLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs_R5pc1v79HNOAlN2GzZjsDQV4lZ3zPXc2YSs2MFBTmn0Zss30OrE1q6vt2YV1GvpKCPW_yTqEH5KlR_a61JeA-2neErF4SwpaJESy0Of0I6M2QdEBVCGr_r0DM9yf4itV_kAYEAMcJGBPhf5K11mah17DFxWt744cwFfI4H6XCS5SZzzNcfDsmrYpuv7e3CDhcbZn_7a-DMVx-y5S8ruB9Ly8GYvBeT6wX-1RaJF74YiywSB3M0XpQPTjpvVStZ4mgKLxmYaSGdb6_ekypygkqfFyHaILSgGvbcmNbsFsZK6AMweJevvCuJsapvCGqxqaT7mJTBESRXrC9TsVv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVcRoRHlhsqoM180tjFYrbcCb8W2LRwkWPlxP8S_EZ1gFwzWsrPT7itKNkJRgIya4Iu-hMksOKfrt523kGuOPXgmMPpBz_7RnQ0RPfVLZDjkxEdeczIRCmBKRexXIpJU2qycxKhobp5IAfHh8K1lUCzSX8nzphhFIdL6irWczhL9-XC2o0tDMnw4pyIgGrYvwPmAgFx4vOMkCKl-gs8b-99bJF-SYJ2xkXgqhjNYb8EKT_QHC7ftIoJdlpoRSsteW7vxZavjJ-VT3pJJ02Y3JUgBLUHGQXmytIm96dvUvP8wfygFq6EFzdVIZI_VDTK3tHtZ4YM5LO3N_t2jZZypyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXc0gfDgLYTO8GOW4grtkZohJvQ6hJjgoUYlZKtYGfhkqfcQkV3OrJnQupkYBIFoxtWQkz1YF-oCzswCeqqJT7s34XgDlZH0DYW83_GGq_3TQ9zfho2X_pfNtXYh3kZqwoV3ilQ3NrRfHh3PPPl9wAgUqrO0sx_yp7UyQvykeIWbuYWzyvg789fhijcq525gOXhK2jwxYgRKi-3vOq_pXImMHxV01k1d7pNomYtAv-lJujRoV9cEw1pGYhlNpkr7Dq2iE5Q6n6N0Pv9Dkbl45Xv2UgtzcWGDg_uwezGSLptXu2jgBjHkIyTST2-pzRZJp1uYCrtzUp7clZm_WTK07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njx2vRyFFHxpXl7NMOtvZSgUsWPo4ra8fQ-DF-JFfxmsJeGSiX_UZo3oorKAETMvJohQ2puEFy6i6fu7llilL3q-ThGWsPJlTnIc_xoBXkNmD_jxUrLN29p-EvJ-GZUv2lpvnA8LwJLu_MfcmOOIWNeHCP10K6ft9Aa2_k9tAt7jwP7d7WFuJL0mMRIiTAzo-zqInqOA-sOx3wfmtH75ZF2QvMKgPKqC38X41CjgSDENLabCNxdzK1JAEEKwexux10C1cCUcs2p3u9wadBlLT18uE853OeGupw0kNhQ9UCXq0qxaNxgFjjk6rW7gKaJH45GLritGP6RijonG_VjLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSd7fiVDYoT7_xPkj5G2fYSlcrtnkNQQmSRtDldHfburXABXjnNPTPVdr6qGOgTaMBdYDDHalb_8rPrcGyNdPR4ZSyeLHXawNvPGgJgx647boGZ8fFji9xjrFAZ5kUrZavXUNTvJnjcXFtgR6G2iz-IgIeawwAyPXt2zdoBPh17kCq6UnFzc9akDtxT46LPuPFS-u_pZ1T7Ougdnzk5O3R3k-WlMgh-INtoUiDaSt6BpvIq8wJojI5F5hvJBRiyAysidUAsLikss-r_q3SlM7YeZbrfYGq9JOKrBy2m6hORLaAYABUjyMInIxbEydj2OPkxi5EAVjGNgHCUsCxhv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0jn3lfevotPP_1AkvhzMOkBKNCkUFO6BwLSGMqEM1lArH1OHuk6VXHVw1HM8zCVNaqFHE8iFBuNotz98VNvErTqXhp2e7zj_BO2T56Q17oEwI408qhE2mLAjBO-qB7z5bx5SCZXJLvNushu7LsvSF-dqYrSPBgRaLHssOMB-0HNrEL-PtaRzWRvpsLqJWtSQbAc8QhT_ksRUMgpwAYjq8TWaaBkG270LUzXx3rVOroteTmKLsx3hmBmTcmuIPnm2FUAQKFbQiYUnUaIoRnR-RzqU3-sndSww9El9GI805WRj2nnLsiDl9LtY8vHQKVCVqyPLwpV1seVWorkjY3-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWuWRv9T4ZJgFLcyPjxjwjgH9buYRTFjYibdE0x-auqQ2ffq_W-TxmuRdBRFsIICQtLjr0s4NVS-_a5bYIvhXGhIZUJdUSIAtpe2JwKqSs_n50iLLxk9XRg_GRQ4xc38o1mfpevG3A5IdiR5FBubrKLUmoCbX8jE-CfFbxMHDc1GDcfSXmtCu1x98wx2HQzd1bCUT3QRAjcGy9NuOyRGQOl2ZTB2utf-74oaR_MWpliPr1DxoIjl8brYu9GAM2-3eLnSlys08nSCH74DKdG3rxqToiCeaI7l590Pz-DgXJREaQQgKi7eok1_lGxBMbdW2Nl3K0rtetdcU99BLA9B5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7DfszgeMqZ8Wf_U6G4gL8xm-JotksIAMwHLvIH3U9fWMfqO-G-TM_jcnFykcKJEO7PR1syzkt6DVF6Rr-ybcE2KSVx-7-2OrMxLGn9uzaBsWl7deMIoogkLMG_l4HcveRUbq-CADaWwRCA100OkhbQlC_vs-VK5e84Esu3DkgD88cONedizW3E5aMnHpVFWyyXR6qxaZ3d9_bUQerpLPyp3Burhjon8uLBhTSxEolEo2uB2sVIImJQQ8ODkqa7uejGw3r2y18EVOdMlZJ9IvtBstDOPbw0LGqwA1o13zMzO62gW41M5J9Wx7i_2qx61zEVGnfYE79-dZxl9QxngkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tINJEvQYBhaHT3HOoYerysIVIYihAZVZqUTsiTxGK7X1v5uc9KimPefQ3KP-43nrvdGECRfkAkbRYsXidXgB4RPAKy-LrS1wpQMwwpKZfiD2d8ZgfDAu38uQa1pSjuPm8zBqTT2t7T-dRz_Pj1g-Q7Uhe8Ecfpf-ur8oc0_fwC86sxiXehJ_0V97X20jDqigCZ3I7OA8wrUJo-Pg-uf7oeBezQU_h8JT061VwDfr8jC9eAgwre1SxBMltqK1U8oP11U6K1vxFARSnSNKclCpEVXbvy9quiQPL9GY3uuKjoOoJk1F89iqD-2PBp9XKf1h1fZoWqbOCD3K8F5pcdbtsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=otgyYqG3dj-5IKVwyIK7CUTfpQkCSrumtKPmHFhovgF2ZDzTUpJ_uSHrAiQQYSHv1mziKQSQgKTaXEf6IveNFxeDZc5uTLlnSgDSnBcYClOvdjTxsoKrfsR3AvO4lc0JeL5ToafUi4MTQCcNTKmxpND1iokaQ1LFsbifQw8ibswxbpdHSC9WYo7gPxmeinNSoS3uvHWmJFux1HbX0zxZ7MxbzFH7zTciSlsdukSLlfejX6s_eRyQ6je33VCcHswUO4ofnN63q13uV0JJNWeHkTnc13wzk8p12iS7H6C-UJ1-lBWPrdSKmHYgfAcuOHuooAdTwiNSl2PANGqtm33iTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=otgyYqG3dj-5IKVwyIK7CUTfpQkCSrumtKPmHFhovgF2ZDzTUpJ_uSHrAiQQYSHv1mziKQSQgKTaXEf6IveNFxeDZc5uTLlnSgDSnBcYClOvdjTxsoKrfsR3AvO4lc0JeL5ToafUi4MTQCcNTKmxpND1iokaQ1LFsbifQw8ibswxbpdHSC9WYo7gPxmeinNSoS3uvHWmJFux1HbX0zxZ7MxbzFH7zTciSlsdukSLlfejX6s_eRyQ6je33VCcHswUO4ofnN63q13uV0JJNWeHkTnc13wzk8p12iS7H6C-UJ1-lBWPrdSKmHYgfAcuOHuooAdTwiNSl2PANGqtm33iTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=vAYYzxn7qyclgWVo3PNK1n19OUAftNlG116PFyQa_Egxq-yHaOkyRltvd7xcYzuLi8W1SfFwxCaRBB04nycfVqv6aheurWcvOYLWvsBKHfl0tPIn2Awo3k5x3mOeG4ncdcq_kWYbfhjf-OQSA9yjNY3K-qBOTfmH_j2urFrK3oGTWXQ4XBBzm0Xl4x7s-6c8mCiwVgyVmf5-bO-kXIaFHSMUiYSXiiLJwFv9wRBXQ6A9EsWozM0eP_s2M1GT05Ilzp_LJUsry6h-w95kEFNkD93UoDVQNmqN3-BbHGEhvAU0Tl_gEzL8lTXgGLNLNtr57euYXCtX68XHSawd5atyWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=vAYYzxn7qyclgWVo3PNK1n19OUAftNlG116PFyQa_Egxq-yHaOkyRltvd7xcYzuLi8W1SfFwxCaRBB04nycfVqv6aheurWcvOYLWvsBKHfl0tPIn2Awo3k5x3mOeG4ncdcq_kWYbfhjf-OQSA9yjNY3K-qBOTfmH_j2urFrK3oGTWXQ4XBBzm0Xl4x7s-6c8mCiwVgyVmf5-bO-kXIaFHSMUiYSXiiLJwFv9wRBXQ6A9EsWozM0eP_s2M1GT05Ilzp_LJUsry6h-w95kEFNkD93UoDVQNmqN3-BbHGEhvAU0Tl_gEzL8lTXgGLNLNtr57euYXCtX68XHSawd5atyWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTonQFjRWqyM31RIzbYL0zaEuALuI3NqQgKe6okAhznkU3YJrgbSOC_f32K8EQfEIpKfH_OMIdl9DNuzVXufeEU9RJWIpzwTUd3I1cLQ6quMKmXaMi2E9QFhi8Vjr_0AzYnUbA23vSKxXDgVetl1aykRUpxA68Gmi3NlWIWb76PVJemAyjghaLD5srvwAF0QZO_xwDBKkOAh-EIK4lcUOKv18P4LPwY27gcP1EASZKOXjFuut77YYNzNJYZdj60oIY_kCVuiDvYRu5yYf1ux0qta1UMOkFyIJhznY2GC5LSfa5SrQavMql4YxIwt0kitInRzA-EVPbvp7kmVEg7d7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is8F-RpQU2mVrVKm8JdpXPHdlM6YVBetCOl3UKj-QDz_ic-s8HHCTbdqIwCHtkduXEymWWva6X7yHhMI6wkLJmBoIuTmrJz2J3eM4NMVV0aTwMhfv_2TJ-htmyy9uoMlHQV50kF-TH9dBrKd5s2xhwOBIiQkTe_jCxl6IXpShddM4wkmZ4VhGLmQ57m481Hzrehg6hJ7YbsEsRhFioXOuwf7tTCUEUjdmBQZoJIASN5CRuhmhO26Piw5GSbK8Z3DybypJuK5BjMMv7ces-G99JWcUMgEL885EPyYG9QWT69hmM9-eDCOO205CTB9T-cImJfubUpZNy-7QmZhzkp71g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7hTpxDI1uC4DdNLymqgqx5KC1aKL2vc0VjSgjF61dZ1Lk3f0QqDDV0ZEVCRO-uBswRaVgYm9muUgmUOEDLXhhzbNAthWzX6JI6yvBaiZUjqal80KUkXQZ0A85zRxofpAEKalAglW177zQrcb_OXssIYeWkxJ47rQN7PYqclxhmMJUxmAi6zPpyEB3DPRfGYSYcS50a7fcUMNKMUJaWI2V21zktP2RKxG4Jn9eCBgCprsjy2nFm-iXO2DoEhyB1t-ZWHWBUXbwFI63_fCzAqRZ8MYtwEGQX9YSyxss7z4m0_5Oki4lOuSa3oMCm9SNCI2EjlHAAeipqNkLV87UO2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlnfFSGMpDMe0ZRpbd8aBbTWX27uTjmiwkXkqE64ONRYHPmPyCjCTRK5jDdqZakNA5DfWZBpUd7tIc6GqWilDbhhadw9nd99lnYcW4faLC_zslOzZYFHpQ3MKu7V_yflPVTAM4FQbq2NX4YYgpdnQzYTstpirWKHkoim7j_D4iJLbGAb7GXwKdO96lTshRFQDVPFY8bF_DX4bG0YpHfneB7E4KpDnxnNFxe6qhBnVar16nCNJK69vqH5ZuRgTA0ubBCvTqUgAwoaGRcvzQ5w9EOGXDMrzMKDKbtprjRpTIkDzqk3nEkvpYZQEj-Wyd1KG8UlRq-katNAnALNkXJbCk6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlnfFSGMpDMe0ZRpbd8aBbTWX27uTjmiwkXkqE64ONRYHPmPyCjCTRK5jDdqZakNA5DfWZBpUd7tIc6GqWilDbhhadw9nd99lnYcW4faLC_zslOzZYFHpQ3MKu7V_yflPVTAM4FQbq2NX4YYgpdnQzYTstpirWKHkoim7j_D4iJLbGAb7GXwKdO96lTshRFQDVPFY8bF_DX4bG0YpHfneB7E4KpDnxnNFxe6qhBnVar16nCNJK69vqH5ZuRgTA0ubBCvTqUgAwoaGRcvzQ5w9EOGXDMrzMKDKbtprjRpTIkDzqk3nEkvpYZQEj-Wyd1KG8UlRq-katNAnALNkXJbCk6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما
که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!
همونجایی هستن
که بهش گفته بودن
نفت آمریکا در ۲۰۲۱ تموم میشه امروزه
در ۲۰۲۶ آمریکا بزرگ‌ترین تولید کننده
نفت جهانه!!
سال ۱۳۸۷ گفت بر اساس محاسبات کارشناس‌ها تا چند سال دیگه  دلار و یورو نابود میشن، در عوض و در عمل این ریال بود که نابود شد!
کلا محاسبات و آمارهای شما همیشه خیلی دقیقه!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ipWx08Lt1QCY1xfMFK1uM48DekMKvpc-xiKO9Y6EiUBNuBR2dfbDcHlvcQICLYsxMH3dahKYPiId8E-SSl0K7kc4hLzWe1haSBbT8L981p3UmNwPj9CAZUlGzNjpSkIHvBsa-o-w2CKoi78Yzn2W5_9ONYhUWnJopIN5EEfhQTbR3v63H4Mp45KyGdtMiY570JWH16mQmMSjAJOtV-Sm1RRxliE8qU90403iFkKUJtRr2kT0BM8GNdVaWu5yOg5S1H3E4mpJsCQyb1P6nuHEkJhVDBER4XyFVb5dVCPwpTurh8BCvPOPqo5AS5PVdV0Hw5Yb0acbx-JffhFdQdTzplFEfaCllS6f1MdULnIUX0VhSP2b1xgIgNx0OMrlPH57p2qhHb8rcLzpFpZs_yQdDj1y36CTkLRsdyYAdSYhl7dD6yED38X8hCgLW7-xUgg0BKwFyf00g43ATDL6b8hsC0Z_yrkycpEUMu-o8IZLAUqPgVOkDiq3fyv4IBTVU7FqOyhAs4auyWhEHzDynQKArGz_7nwmd5PA2XOoHc_VzKrCd7B-AR9gtBWjEvCzdc6yuQYgxPrGWZaKxHEvwgK1QLFfrmVJG_y7tuPNmwlurlaauGH4o1DewugAcgU4c6ji9oFf_vEVOpr8iFyQHSthHthRxvnRHMYLuVCWnhIbLgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=ipWx08Lt1QCY1xfMFK1uM48DekMKvpc-xiKO9Y6EiUBNuBR2dfbDcHlvcQICLYsxMH3dahKYPiId8E-SSl0K7kc4hLzWe1haSBbT8L981p3UmNwPj9CAZUlGzNjpSkIHvBsa-o-w2CKoi78Yzn2W5_9ONYhUWnJopIN5EEfhQTbR3v63H4Mp45KyGdtMiY570JWH16mQmMSjAJOtV-Sm1RRxliE8qU90403iFkKUJtRr2kT0BM8GNdVaWu5yOg5S1H3E4mpJsCQyb1P6nuHEkJhVDBER4XyFVb5dVCPwpTurh8BCvPOPqo5AS5PVdV0Hw5Yb0acbx-JffhFdQdTzplFEfaCllS6f1MdULnIUX0VhSP2b1xgIgNx0OMrlPH57p2qhHb8rcLzpFpZs_yQdDj1y36CTkLRsdyYAdSYhl7dD6yED38X8hCgLW7-xUgg0BKwFyf00g43ATDL6b8hsC0Z_yrkycpEUMu-o8IZLAUqPgVOkDiq3fyv4IBTVU7FqOyhAs4auyWhEHzDynQKArGz_7nwmd5PA2XOoHc_VzKrCd7B-AR9gtBWjEvCzdc6yuQYgxPrGWZaKxHEvwgK1QLFfrmVJG_y7tuPNmwlurlaauGH4o1DewugAcgU4c6ji9oFf_vEVOpr8iFyQHSthHthRxvnRHMYLuVCWnhIbLgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieDqwY5novJ1sNwHCtoQGV4aOZIaFUpUt4Sjj5Unh63uzfKipNfOeo_7oygAHxNz6SyRZ1hZfkH_Mp7Fe_-f8f5ShwBH5KYpbV1VSxHlGQ2GOu_awP-e0iRCgu6eWxC61tiC-wrjjs_ZMUsV9lmAwM9xGo9dUgaRrc0GwJn4KA09MdJD1NSRaTqzB5lvWI6VpMnTv4AECGEp7gyYhjKgB2Zny0hIu_-af7BKgSN7cGjS1W9uASQD7WrvO06jtbqedDt20lSac9iaOxAmGXAYd5JAXyqRqrBc2GabGDh9XXvYOSFyd5woKpQnu9BaGqsGC8JehK1iRRdN3ISsd4emAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPMWMS_7uFmt8cwnjMX61Suwsu_3wwXE-kpHW07KidhLa8R3JLkpInflwvalYZ3n9mGQ_8fYzR_9eZGKVbfF3U9evrmD6XyZ68u7Vyepw427H7KmdCJEDkN8S08K31rbekBDSsWIKiG31viPTXSZRe6_WlwKiK5PSR7mK-YuhhMe-78v2qeUYDdy-byHXU1HwlyKZ4Sbv6f-YKF5CoE-ALNCmG9DSRFa5ICT8rOXnct6tj6yYL9ydT1Fdqd85-TPgKFMBxPjQeDvLFFeWEYFGqHgXBiMEh-w9QhYSMexXNAf8o68qOI2w_1jpJSEV_aFXqcd5GQTPXI79eQW8XYUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام - فرماندهی مرکزی ایالات متحده:
‏
🚫
ادعا: رسانه‌های حکومتی ایران ادعا می‌کنند که عبور و مرور از تنگه هرمز فقط از طریق مسیرهای تعیین‌شده توسط  ایران مجاز است.
‏
✅
حقیقت: ایران تنگه هرمز را کنترل نمی‌کند. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از طریق این کریدور حیاتی تجارت بین‌المللی کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5994" target="_blank">📅 00:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5993">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrUm1Qz8azlwVD3ymFb7VoOxqOaAlN6D8F6dVhS30YxTA2huK1YLDAJl9O0EgsbxQggjNPE3HhieyVo9IVcx2gRtDTJOLRov1PsJyz3vSesTHE3WctSVO5MNO45ANVvHCs31_DgG-LoNfAlu_0i5vEsc9E1CHrLGmU8rI_kFy_-Z4CblmxR431OkM6wUrDjKrK8QTa4HEXgnWuWIBN_e5qyxZ9YSs9ZRfvA6ykRXI1FWLaOv0bXfNIBlLc4xZtEfcV1aEeZm1AAK29nR92X5A0uz3ul1Bm34CX7Z_f3j0hShHgmsXIupFhd8Lwo-g2M2GguE0rtX8Md30Q4ztG_Cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=X4U4XgNeoD6E0lZPTh16wmeQ94dnFdXDDQdsV2NV2TQcE3loPix3VnpohnXruY3bVdn7uJXrFG4r8m58RtoRqSu186nSZgiHw7o4ovTAckNb4tMzu4d38La-KCKm6nwCkxumOCLdyUwKXabtzLlHb-YR_Z2tWJvTVK8NJzpLSK1jU4XP_i4hFin7873ytBE5FA62wqWErCv204fmLY3A4css0CNCme5KY2UQNqDrgAC8kIOhsfHxaaZ-jwbICFERwnUZ3C9FF41jc-Ijfoa0sLapBlItkPkB5laRBFt_IVvOJ52XHjhZDf-GkwkmT-akFiJq_r0yKXNOarO2PVy7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=X4U4XgNeoD6E0lZPTh16wmeQ94dnFdXDDQdsV2NV2TQcE3loPix3VnpohnXruY3bVdn7uJXrFG4r8m58RtoRqSu186nSZgiHw7o4ovTAckNb4tMzu4d38La-KCKm6nwCkxumOCLdyUwKXabtzLlHb-YR_Z2tWJvTVK8NJzpLSK1jU4XP_i4hFin7873ytBE5FA62wqWErCv204fmLY3A4css0CNCme5KY2UQNqDrgAC8kIOhsfHxaaZ-jwbICFERwnUZ3C9FF41jc-Ijfoa0sLapBlItkPkB5laRBFt_IVvOJ52XHjhZDf-GkwkmT-akFiJq_r0yKXNOarO2PVy7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHzUj78inDp3KforO6Hto5LpK4VBjyRxo43hjzHvdIqZfxMiD9C5dfDR2mYGR5jF5SdjTvc5hz1nJzHKW6sVpKNx-jUu-u4UWjPnck8cR0CJRG6V4Def20MrLLKSm9ekyAesUgNq11AsFFC0OyNu_trphUBDZq9uZ_zbXkIK5k9mzxx3nC3b1kR34C7PSIk5DnEKjgsj1wRp_anCSyzr6vLbSHAZjKoKW-4mJQRRiAmgv7rsotY7AKfilqpIKcB6JJh3x47OsGw9RZ5b6sND6SnDZThoEVbNQtEND0uGD1VBmlIbIhQm9nNzRgWVFPYaW7lexLCumXuocJW5QLCr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=cFwAEN5eR07ld9Y1dPyv-pNJzk9gQYZAd1HnwwKp8NGy1s_-3fNdUz6xTp86fjzID6j-4WHVOn2sxwQPPuzQw_1-EExmXfFFCggInANBSOcHhJ7QToVf4k3TRYVcVKWhj4zwxQfwfD0anLKJ-KrNA6BsNZRiTjaGRIMF3D9FKk9scvb8tQ4qX7ZjPWx_WaETlTM9D4oomtJWP6q0-bAFpoOLTjg9fbGmnZT6crcmsG-fTfdsmCQSpu8QkmSKuTKuzxXijQlNAFEM1tx01hjH3hyZgjN-WHeR79UkuUdzHkfKYdMzlyz6m_CxEqgzwHMF4-VwYhYJRQQD7KWuWgnJmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=cFwAEN5eR07ld9Y1dPyv-pNJzk9gQYZAd1HnwwKp8NGy1s_-3fNdUz6xTp86fjzID6j-4WHVOn2sxwQPPuzQw_1-EExmXfFFCggInANBSOcHhJ7QToVf4k3TRYVcVKWhj4zwxQfwfD0anLKJ-KrNA6BsNZRiTjaGRIMF3D9FKk9scvb8tQ4qX7ZjPWx_WaETlTM9D4oomtJWP6q0-bAFpoOLTjg9fbGmnZT6crcmsG-fTfdsmCQSpu8QkmSKuTKuzxXijQlNAFEM1tx01hjH3hyZgjN-WHeR79UkuUdzHkfKYdMzlyz6m_CxEqgzwHMF4-VwYhYJRQQD7KWuWgnJmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDTJsdPA6vfhReltF2bbrT9Dlrgbe9iLaYLQZc3k_WJKn-nlouC3XrWWPafywm6BPNe39KoQrYE7n4fXHPf6LcbDUVeLCUorsXuf_I3aYNn2Xgl3iibnjohwlh5gVOyMKxM-Jn-hQzn_annWUcLwAGx1mbxM5ZJRWO3OmHv3oqC51LZCFzdXbTBIX4uNPh13VyEqx3DN_0AAY46VPw--1ADkTrv9Urd3kdzK6_dKtKCHodagMntZylljardIKLWEqo3aoy_S5IV9HfKRbUhDsIlTT5BN7os_OtMzjk-JFL_EnYpkAU5w4cbP5U22zWA7TuvndliSOci0SOH6dUCuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyqlUFcQRCOLevy4aKQ4BDKzAesuUFfPS3pSphapA7UOmlIhMu9FvQ1e3jFNbwWz2a-G8NTzpbsU7LkMX6Tu8Mvlzyby_yWsl1lOP9fW2PRmBDwk7JvRe-bqGgGaaKZdTJJVRIzhSVrdFg_25b96JIp6fIBlOthSJoPrRFMrIwWlMmqu2f-ScpRd40C4UGwGgTTjvr1U_eq7jU7axi_PfllEP21xtZKlqGTuY7FiaoRmXs_hJJ7Fzc3DSL9WdBJ3--UrIQ0QJHS41nN9x4hIzU0p0MTHU0t-xxTS2JrGiEJl4OiTBi85-ILai9zNwynWy_I9OcSVEv1CnzCV6-JjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=cG3ncc23EjWKipZVeC0rmhhD7FSmNfApX6897IuSBwRsILZ602K7yW4WsF16i7NC9RITVPuN8aPybjohaZd48B_dJUQZvVqmE1H0JuOLMXikNz0rh5dIK57q1N0Jm3Nb84nFZmpWhNSguEzHor5DmCVTX6yUny1qCqtT_K-eYZPX7x3u4bIG1HnyktWpJnghWv147U9Oin_13v-37Bzkgv0botXiWOlMluX399tHdjaDnob2qb3UOnBbv25VSftxgB0kUQu00r76pnXSuZ4pL8wK_3lTiD8nlR2HRS5BIX92dpd0NeQvzGZZOASJ1cHxW8s25XaEkJVMM49KidNi-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=cG3ncc23EjWKipZVeC0rmhhD7FSmNfApX6897IuSBwRsILZ602K7yW4WsF16i7NC9RITVPuN8aPybjohaZd48B_dJUQZvVqmE1H0JuOLMXikNz0rh5dIK57q1N0Jm3Nb84nFZmpWhNSguEzHor5DmCVTX6yUny1qCqtT_K-eYZPX7x3u4bIG1HnyktWpJnghWv147U9Oin_13v-37Bzkgv0botXiWOlMluX399tHdjaDnob2qb3UOnBbv25VSftxgB0kUQu00r76pnXSuZ4pL8wK_3lTiD8nlR2HRS5BIX92dpd0NeQvzGZZOASJ1cHxW8s25XaEkJVMM49KidNi-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=PkCdiaj01J0Fe3Xs9CQi7-5cVxg_NA2j4c1B9BZUEZTmK9O7OlUY4j1IshrvkIzZ86OVN2_mPbM004hcwdIL4A2sJyxyCsDz3lCv3Xxnk-GKSi31qAjlt5xphGQ7wI_bgCZlGxUU4PEM19GEA9JtmBtNO1exbfevb9ZViUj66hWmDO8MQUJ81Lq8rgTxKwMAC43Tovm0hUuBNIclFaWG8ebYz8U7TK7ar-JbovOBxuEik4wx54hFNwR2UoVILPyn9i1ug6DLhQPFqosb2drVirqR-KSZaXexD45EJ3eH1M2UGi5fxEerDTwJ4bhofNuGwOE6RpTjrJc3-AmcGGX-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=PkCdiaj01J0Fe3Xs9CQi7-5cVxg_NA2j4c1B9BZUEZTmK9O7OlUY4j1IshrvkIzZ86OVN2_mPbM004hcwdIL4A2sJyxyCsDz3lCv3Xxnk-GKSi31qAjlt5xphGQ7wI_bgCZlGxUU4PEM19GEA9JtmBtNO1exbfevb9ZViUj66hWmDO8MQUJ81Lq8rgTxKwMAC43Tovm0hUuBNIclFaWG8ebYz8U7TK7ar-JbovOBxuEik4wx54hFNwR2UoVILPyn9i1ug6DLhQPFqosb2drVirqR-KSZaXexD45EJ3eH1M2UGi5fxEerDTwJ4bhofNuGwOE6RpTjrJc3-AmcGGX-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=UXqI5-L8-q_UBwyFwrKfcZ6uJJMFA9GJENt7Ls5IVouC-VKZWKKYxSL-KWKl-tKLkq3YEdpAxp6ZxodMV3XJetcOjwnIdJFRq131u3iaoMoQVLf3U0kkFLuuvhfna3B5fclJdwaIM2vwPoUccJdQs831S68LHBMka8lN94mAV5Qx-r121CumjU0Q9Ipf3UQ8_87NkLgGKKcZYZ6BvWcQxgG9adJgFrAzYN-Ryeh8cSbONbc-vDy7oFgfJPWgGUp1yy69dfIVQvkDPXo-vjor79DhYK4PYvA_wefSrsqOuG5FE5f_58pU9x0aQy7gCcC58LaOCr1ycEp1tSr69J4t9W8mAG64O1tIM1cdT7Lwqrkv0DAYwmQrH9ccV0Q627yI8EaXxFF7Obl1OL1NAoOusDHlU9x2XIKOxUMawQjFqAyNoIRBDOU3nKypGaNA37IQykFBCgWCWvHpOkfP6NAkT3v_877JXCOGvJhZjzgujuRyBBWkp7nUGi8EtOmNJSgFTS3eklAUQ3xr4AM8WQIKCitm_v0G5UX_a47GXfJVv6a7EyFEkwuG8NBTsPF8wwbZ22-GR_5TFFG5SHdjGCvwb4Cw3HcPkRtT4r3CGNCgmir8B3XZfkEy4UNwefYmxuP9gIia57twfPRkSzOvosYl3FcELbQtzDswIGk7X6hqyLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=UXqI5-L8-q_UBwyFwrKfcZ6uJJMFA9GJENt7Ls5IVouC-VKZWKKYxSL-KWKl-tKLkq3YEdpAxp6ZxodMV3XJetcOjwnIdJFRq131u3iaoMoQVLf3U0kkFLuuvhfna3B5fclJdwaIM2vwPoUccJdQs831S68LHBMka8lN94mAV5Qx-r121CumjU0Q9Ipf3UQ8_87NkLgGKKcZYZ6BvWcQxgG9adJgFrAzYN-Ryeh8cSbONbc-vDy7oFgfJPWgGUp1yy69dfIVQvkDPXo-vjor79DhYK4PYvA_wefSrsqOuG5FE5f_58pU9x0aQy7gCcC58LaOCr1ycEp1tSr69J4t9W8mAG64O1tIM1cdT7Lwqrkv0DAYwmQrH9ccV0Q627yI8EaXxFF7Obl1OL1NAoOusDHlU9x2XIKOxUMawQjFqAyNoIRBDOU3nKypGaNA37IQykFBCgWCWvHpOkfP6NAkT3v_877JXCOGvJhZjzgujuRyBBWkp7nUGi8EtOmNJSgFTS3eklAUQ3xr4AM8WQIKCitm_v0G5UX_a47GXfJVv6a7EyFEkwuG8NBTsPF8wwbZ22-GR_5TFFG5SHdjGCvwb4Cw3HcPkRtT4r3CGNCgmir8B3XZfkEy4UNwefYmxuP9gIia57twfPRkSzOvosYl3FcELbQtzDswIGk7X6hqyLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKAVTnsPLkU7pNQJHV2n631dCO3THsZJcwpFYasM6vogv4HVuSSqXiBbtMaE4T1nHyRkQxds689OjNWcE1d35MLCPKAoK9pc7KNB9yxiYGLtkOQntWPZk8pj_rXsE66SW8hY-BeIxHMw2ahICHSZpeiTOCfpFrBK3m1lO53pu5aTo6NcJK-gSNU_cBp2VQig9J5ovDqceZxSlxXOHDqJHM_zUeC7vrDOO48fw1ZKZVBdkd-rk58wVXwaqwCb8zbzP4ZDnbndzXDsHs8GUtj3bB2uCaSdv9Ug4NDPJjW1kf6hz8wlIZcOp_UxCEqr0JS8ABUw0CMVRpwz5WGUrU8xMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyYALLNosVJo0lRu5Nhfw94ArV1TzTH4ET4PSNhqFluFuWzxOaY72MULJK2I4Yosw0mAe8px-8H-p8LwINI1N9XnCezSMtksgJt7lyKKDDTacp-6v5BU5gzJEwdFnjHq3WeFG2TD181EEBCFLSKgogCSBlWaHPv8Jd2jlHmWmtESYZ98J5ZP9YmZrzetoGidDbHxbGK2Pvu2igBbeU7WXjLQM38IhzcnhrspDfISXa5-nwbTwkmXJcuzy3sCqwJAqxOAFZoIJWx1j7k8_btAZBGdmD7sOEt9n_TVpbdIqP4jRu_bbbPLRyo22k8g1q4wPQFNLuoInR30iRI9Y2cohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjYJNe4mLZOAs1sD_IZ_YnCYBBHTu-TgIvcfVJ4Ndh6a39x7qYoirr7n1j5Nk4Qnd7wWA4N_c-MtWoizAWD8C4MID-HOI81RH6zqDUTXazNY517-IogqlsASmmLRmnEx7zyVu85791mZPjeLnQ2VEhE3O4jx6gj1-4b0Kmeqg_YzzEKzTjDNNJe3snFU_GNACfBodnOWbK22fZRnCJKSrTVRfEWdyulpU6N7hPj3m_RlIVNP6cFvaFeHFkOqcF8hbG6vL07JB8UC-S1cweXkONuhZ0y7XMHj_cDXzzp_NkF17Ay79IrAvB2ilSmEFTNMbdkHHUKUjsu7rKnwqtFbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=AwUvS_FfhZGccMDn3Pyn8NFYANImVhfsaa3dsYgxqb6zf0XPQAdrsxPBzWQ71yqTOX_Ow47p3RPWP-yMOU5V7thvkIgaSjeOcrVEbJNRE8jNYIZUKJQi7K0a5r8KfYFRu2M1G5t4OQv3bKLlpkwZJZep1t75--YwfjJqa7cuubyvQTIEPu302SztChf2ZAN5EBIFI0VE0inTVmRjaH8Hb5j2mXpnRYyrwGGx5oKv32s6HQ8yjuEpvfBXmq2_D3WUgD-QbDIEIYS2dE2MaQofqhK1hR5Chu13woVHPxWhZQ6aeFbdCzOyUXpBe9HYQxP3_9IyQomh-KngDEml2ePPVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=AwUvS_FfhZGccMDn3Pyn8NFYANImVhfsaa3dsYgxqb6zf0XPQAdrsxPBzWQ71yqTOX_Ow47p3RPWP-yMOU5V7thvkIgaSjeOcrVEbJNRE8jNYIZUKJQi7K0a5r8KfYFRu2M1G5t4OQv3bKLlpkwZJZep1t75--YwfjJqa7cuubyvQTIEPu302SztChf2ZAN5EBIFI0VE0inTVmRjaH8Hb5j2mXpnRYyrwGGx5oKv32s6HQ8yjuEpvfBXmq2_D3WUgD-QbDIEIYS2dE2MaQofqhK1hR5Chu13woVHPxWhZQ6aeFbdCzOyUXpBe9HYQxP3_9IyQomh-KngDEml2ePPVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Tzi5mhjxsPOuuZUlQcrMyk008NjvIUXxUX0iSeVhb3p_k4Fb0D8BT-IGA317RRM4-HiL3JAVPUnrhC6eIVu2nyYdxGEKDtUxGGXlui0FA9vY-5gniloDM57JL1B5RZ7U5_JCIjjClw5SvcawgBZMBPNrDWAq3kW-vi25ad-LRP8uZenrsql-mD2e8edKWfTS2veZezlkTzuQNYE-ELMjv4oeJyE8adLy9h5JNSI5Dg8JpPAzPn67ZZXp0FNNMf-p5HfHyizFZXgzB6vuyXDtM5caXekDD6UFPHy3oqzkyBWGRWYwZ2upU0M6sCRmAofXOFhoze5Qn34kwMHb4z9mVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Tzi5mhjxsPOuuZUlQcrMyk008NjvIUXxUX0iSeVhb3p_k4Fb0D8BT-IGA317RRM4-HiL3JAVPUnrhC6eIVu2nyYdxGEKDtUxGGXlui0FA9vY-5gniloDM57JL1B5RZ7U5_JCIjjClw5SvcawgBZMBPNrDWAq3kW-vi25ad-LRP8uZenrsql-mD2e8edKWfTS2veZezlkTzuQNYE-ELMjv4oeJyE8adLy9h5JNSI5Dg8JpPAzPn67ZZXp0FNNMf-p5HfHyizFZXgzB6vuyXDtM5caXekDD6UFPHy3oqzkyBWGRWYwZ2upU0M6sCRmAofXOFhoze5Qn34kwMHb4z9mVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=QcyLkUkKdbxSv_jwkYAgmkCYBH6GnRvtB4YZylHmf2-w9hXOYbd76IkM0UoNH1rltoluuyOVoYlJo4MvhS9R7rLNRv4dWD7PWtfeTKb12tJmyUtZ_Gfy8fnEn2S5fTXzusbDd-BnYX2z-J_JDK1Pr16C4tKEJMNoF_PVw5tgEbC6iMkxTWMaO-1hyR8iy12Bqs39vsiHRrYXsplnnZYOF4jZRTjqQoFkQ71BXoT9_MKVZbkeyTQzowQe496VQOrYtsfjX_i7euTTn3BN80N7d8fdp6LwkY5ZRohFaTYOHhkA9M-3PCfmovj4ERkdcr3QeFRmNe3sRlrU3MsKwekkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=QcyLkUkKdbxSv_jwkYAgmkCYBH6GnRvtB4YZylHmf2-w9hXOYbd76IkM0UoNH1rltoluuyOVoYlJo4MvhS9R7rLNRv4dWD7PWtfeTKb12tJmyUtZ_Gfy8fnEn2S5fTXzusbDd-BnYX2z-J_JDK1Pr16C4tKEJMNoF_PVw5tgEbC6iMkxTWMaO-1hyR8iy12Bqs39vsiHRrYXsplnnZYOF4jZRTjqQoFkQ71BXoT9_MKVZbkeyTQzowQe496VQOrYtsfjX_i7euTTn3BN80N7d8fdp6LwkY5ZRohFaTYOHhkA9M-3PCfmovj4ERkdcr3QeFRmNe3sRlrU3MsKwekkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=QpjqQ8BD5r3PAcRiUv8xFLDCSBe6b4jSpzzPYlkX1J3dcOvR6Z-kampwALQQZE9MYwD5hEGn9OzKomj0tcH2Ekc9sbyVSrrDT_r-CrlvtCoi44DQDi8L_fHMIZLM214P_NHWTjBKkcuLlqOYL5hiGiNyiIpfz_VulszW7xipag_EPSLOAiE4fI6fU5g69lmBfPqbAFjOgXYoYRA06IwdYAM5vL3bdEbjxVDNyqLl5ysCYxAZUco-JFq7mw8P0h_JOaWKLp7nTvr2iLytwKbLPMDJ9DbFgT9xggkdV0bBBTqYUUjBP1Xmm4AXojf1IOLyXNy8qbBJ1ceAA8O5WIoe_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=QpjqQ8BD5r3PAcRiUv8xFLDCSBe6b4jSpzzPYlkX1J3dcOvR6Z-kampwALQQZE9MYwD5hEGn9OzKomj0tcH2Ekc9sbyVSrrDT_r-CrlvtCoi44DQDi8L_fHMIZLM214P_NHWTjBKkcuLlqOYL5hiGiNyiIpfz_VulszW7xipag_EPSLOAiE4fI6fU5g69lmBfPqbAFjOgXYoYRA06IwdYAM5vL3bdEbjxVDNyqLl5ysCYxAZUco-JFq7mw8P0h_JOaWKLp7nTvr2iLytwKbLPMDJ9DbFgT9xggkdV0bBBTqYUUjBP1Xmm4AXojf1IOLyXNy8qbBJ1ceAA8O5WIoe_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7oRUMowiJOgLgesS-tQjXVXrxU7iIIX0eZPxrVUC09LRpsqkqfpwJ4NCtuY43j69vOEAETeiCSkxSdJ_sH29IgDcly9XV8orpeZ3SMNrGcpvPTiurPwZQwTQFzOSoQeAMWI3L0kAZ3ptlGpnC6BmMLlBz-bQsrmB9wLWsE-9zuzZzvlshdKSYuRNiBcyDApIzDwQBhOJYyr39NWp5N2k2WxXAAS25-Oye6FSe0vbPh5mPq2YFGmiUlvbV8fmLs8i40BdtyiTUE8fXkEQZ36KjicbU0_zTyKRRysNJ8hpHO-EWsnR6UV9bOXAPi-8E9yGLBbDLU8MLkI0eXkt8DjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Htg4wGFGqP6EDRR7pGTSplmo52fo8ymyo9Z-OihWQgr9GmZgRbIhroiOSSFy4oGCD7Nq-UbOc6dEe4YqoBBuIZGAe0537gdA1Vzs4HpzsrbBQJgVj1wcgpk6HDlu7txANJKx03k2vnYLPajZGhoO4rCpoFvhqw-Ybe7jmD6Up2Nr-skIzZLy5SN0U4xuAgzoUQBLt1HyK5vGOhLKon4qV08aoYhva-AOns4PK4LH4YRsYOHy3skH7dUhUxCAKTZ4y0L1h9jJgO8MRPYKUc6DthFk3k3xiIpXsWFtLePPHHG9mR4a_jHW5K-hma0Hixwq5lr2eqY6z7Y9ZpouquK8_GPSbTStDyfU6cGm9intzTXkB92ckQvVbmhCgXsepM30AWhccRS20RIZcHlRhWCIjTNeIYHkzY4V6D-MyMv-GVdJO1iT5YyFb11FmwOuuwPyKZ9HQmXYJtmaVN7LpSUIueDSoZXMSnq5mapVg9cNJNJ1yY-IZG25DtSOavn0yed4gLSIfV9GWMpFI29Vm2sCmhMXYmtQHHvT1vJwptASrbdnuywSWR4j4beBLyZx7MIA4Z9tsi6ry7N--HNjKO_pSJzTqb1kqloU8Dv4TqKgkpq-gEOYaLdERUrhjuwEXIVeoZZhyRIJp9aagjGm9zITu0axVrdlfz1lzATg1inADsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=Htg4wGFGqP6EDRR7pGTSplmo52fo8ymyo9Z-OihWQgr9GmZgRbIhroiOSSFy4oGCD7Nq-UbOc6dEe4YqoBBuIZGAe0537gdA1Vzs4HpzsrbBQJgVj1wcgpk6HDlu7txANJKx03k2vnYLPajZGhoO4rCpoFvhqw-Ybe7jmD6Up2Nr-skIzZLy5SN0U4xuAgzoUQBLt1HyK5vGOhLKon4qV08aoYhva-AOns4PK4LH4YRsYOHy3skH7dUhUxCAKTZ4y0L1h9jJgO8MRPYKUc6DthFk3k3xiIpXsWFtLePPHHG9mR4a_jHW5K-hma0Hixwq5lr2eqY6z7Y9ZpouquK8_GPSbTStDyfU6cGm9intzTXkB92ckQvVbmhCgXsepM30AWhccRS20RIZcHlRhWCIjTNeIYHkzY4V6D-MyMv-GVdJO1iT5YyFb11FmwOuuwPyKZ9HQmXYJtmaVN7LpSUIueDSoZXMSnq5mapVg9cNJNJ1yY-IZG25DtSOavn0yed4gLSIfV9GWMpFI29Vm2sCmhMXYmtQHHvT1vJwptASrbdnuywSWR4j4beBLyZx7MIA4Z9tsi6ry7N--HNjKO_pSJzTqb1kqloU8Dv4TqKgkpq-gEOYaLdERUrhjuwEXIVeoZZhyRIJp9aagjGm9zITu0axVrdlfz1lzATg1inADsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=hhIZK5yZK2PwluVpoWB-zt2m1V2CEDc64Il8Aeyh6wr3fq_isHKySDtle6ytoWFz-Gi_WUE_sf92n9YlWz04_t1s4cowHZmdFSNbI_Xrt1XMU_Wen1eEvzD_RpfaTVkJprpmA1QwdA9itP2Wr0Rs9SxWmxsemlkSI5ItKL1nNA5IWqChisVQgxLVtX0CsGdFGORyzjMgAiCofrkpYvnuyasXcSsBpoSqvPLLftFVNNmkL93Oj9olDOYbKtTo9b69OnKLda0wJz6Q9GXIBXKnG72O5s_oti-gLPaUH8cz2e6uPyh6mIV1LDBvZWsprhVXVHhWPXDOQfy3ut7iem3Rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=hhIZK5yZK2PwluVpoWB-zt2m1V2CEDc64Il8Aeyh6wr3fq_isHKySDtle6ytoWFz-Gi_WUE_sf92n9YlWz04_t1s4cowHZmdFSNbI_Xrt1XMU_Wen1eEvzD_RpfaTVkJprpmA1QwdA9itP2Wr0Rs9SxWmxsemlkSI5ItKL1nNA5IWqChisVQgxLVtX0CsGdFGORyzjMgAiCofrkpYvnuyasXcSsBpoSqvPLLftFVNNmkL93Oj9olDOYbKtTo9b69OnKLda0wJz6Q9GXIBXKnG72O5s_oti-gLPaUH8cz2e6uPyh6mIV1LDBvZWsprhVXVHhWPXDOQfy3ut7iem3Rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
