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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 22:22:48</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAsXU0tlqQXJ62P00-z2hxjya_SzMLbN0gr1Tk1sSl3NlsWJ6Ji716mvw8dhW1wUDbeeDwqEbK_uACG4UH80B01Dzeu_7cW9Sqa8u6TchnKL60MGplLf0qGLOgZlSV7-SMwtgWKUp-2ueRo8-nJ5Goc6T_7yvXTFT9QiRX_E8jwaLVWdZyCF5o9mz6d_Ba1_XuzSvz2JrHBBv9U0MY52bAv8WeeaTsscAzwbKWT2CaUh0PCzlMnmBPAVpGG6nMWDJhHpUbgfHZMuQOSfL-k_ApAwHRmwBxBZWXtQFMxKRpreFuilqS2ZTxD0_UXBy1YLcOe1gOekTCxOxR34tbviEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtRuhkDpLOBoJ8n6-9fv2X_W_s2EUVByGFlVDH1-XmW5Ns00VjNukbEz8QuxMyVaWKpD1xtJmRZa7jcUi8tVwO-bvh0bjQOuvDg0EduIZuvZ_7bK3J5TkVC8SjqDjL7LUAWSe-vppCyI051d9dbKfVPwJQpEUINvO8GYLYd9vz5TykwkSx5p5SUMVi7v9Pb9oxUGvsv-9Mg7WSBIrbtBXTYgjISShkzpZreidcypMGesqJ4S16Le5p3M1zOQ10DkmQOib5YSfy9JPhBv1o_c9Hh_98_Wzfy4LIB9JUwMCNJx9QdLxx4kt34_npcZpQi_4mz7Jzhrrt0pVDMUH6Zjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmZPf4GoNiSH83maAJBxKWmT89yWCD65CwP61v1Fm2jcplCs25tosQYlY4E3a5z6d1jDtKZCeIYd_yxBG0As7UV2xJgKwOzt-B_bm-zoH-dZvHB8xCWXMR-GWxGq9LDTgQgN9XxAN9_WAallzW_2CT8EetPrvi_LOilSwdYsNZXuKIXHZtOCHKn2HO3A4tIeBPtnUwsukm3IuucxeDsM-PC0XNWNBxg-H9doLh4YMAYXT6zdnKbqfyB1vY4At3CwJMeCfEEnQYG_uZ_A_cCflHBs087QzfCKgkQ5ecWECpWEetY8PO3tc2UxvH25Mf-Rckv4BCqmBsvv3iCUmUiosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myJUYtfjTEV6MyJQgS3hmKRH6_0d98Hkjt1xwnoktkON76Y49OfcuQqpcUgMfMEjc38Y1Mw3cSO_VHzbBDn9i3mV6S1gBtlgRG5XMxlEYlWsm2y74RfXSfYCa9dBav4WmLKc-lxhmPExkS_O3howxUAPptWdw71A7k6CWvQWcEsX0cgbBu9sV5kNY96XcvCJY5WG_pZANeHjRuEU8x35HAurnld1ZRj-LUuJk6ZCdq9UjEFZPWzJ9e6D6qyy2eRLZdgvi26wTFtJYYjNuigXaSL1xIT_1WKOQXhnO5fjQo6bt_L0mttLPQd9yVHZ1oMdRIh5hszcZ4Mlt-ey5lhPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=CRPZwgXFeSU_MkDp2_CI40mm5FM3sRHmN_4r3Q7PdR3epYdf1zHBGkOGvArICC-Nw7fhcRiGMP46kEFG3EnYvgwqJ_q31hVY_R0zY-JhzD1EKjvxqItErCH9Tr20mFuFL3j-57Sk7dAm_2dG1czlzdsZvHzFp6v_q8mvrPjjX85CPs_UOH94BWgHFQAJszvNa1B2zur2hEYtTIw3jzOWime17ILGB_u4r12acNXMLLyovY1Ns840obYS1l6l1wCEasV-qPKcq7hqvsKWoGxSbbaTFOFQoAKos2o5guS7CGTlWSRXPS1fEI8ZAUbY6Xij64VsXVZBn3bM_cTC9jXlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=CRPZwgXFeSU_MkDp2_CI40mm5FM3sRHmN_4r3Q7PdR3epYdf1zHBGkOGvArICC-Nw7fhcRiGMP46kEFG3EnYvgwqJ_q31hVY_R0zY-JhzD1EKjvxqItErCH9Tr20mFuFL3j-57Sk7dAm_2dG1czlzdsZvHzFp6v_q8mvrPjjX85CPs_UOH94BWgHFQAJszvNa1B2zur2hEYtTIw3jzOWime17ILGB_u4r12acNXMLLyovY1Ns840obYS1l6l1wCEasV-qPKcq7hqvsKWoGxSbbaTFOFQoAKos2o5guS7CGTlWSRXPS1fEI8ZAUbY6Xij64VsXVZBn3bM_cTC9jXlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3iSdx8sTWgWjs0rfsEqW0OUkTYEBa6kZIea4KWyFXFlfU37QaTY7psFagHqHen2K88X1LvGnBS7Dvhzz9oi1fKATtr8owLrDtmaw1VPPppLnvuj3nxP7PGIaWbqnNLj9cW7hlAbV7mXHNNml_t98vmmrHE7PObODvvuaj5IPNjtIJXkAgwcxzo4AihT7jPX4Ju6Vr6asT6ZZqPkdy6df3jcOgA8V9zBr0EzV7vUfeUoklLf8I4wRNGN2KRVDIWAHbwhjhN86bJKWyAjXpKnaD_KruDF5XY1yKwOdt0t3ahfjMzUtfp3pSzgMrq62Y1p8TKGr3CVZV8e2LMYl5STHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=SIODCkGs27ojUI7QTkXiOllOK1hhQqqfkuXhN0-9ROIdzI5rzUqBGeLSpFqN8e0F8VYSqWwb_-aU9-ktrwWVsS4SzdXGxw6mc-tBLophvkm40I3u2LTajp4xSSbrsW5pl4KOTgBG8-DhQMwVznyxA5jDPLari_zce3m615yqWv2LmztZHi9lG47HMOJ2QVTr1a7B-PTBEV-AEVxU8yPdgC9U5tEaYfpsvfeqrJtBlSCig9G2YAoiDJS0bhKORebBoDX9bnx_9sv0B_D8tRyZE-JKl0fsJ2Gq1VncCNrwFPQwd_jmcdxIkWTGhhDpwxGwnqcN0lRc8n97I9SDB79nxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=SIODCkGs27ojUI7QTkXiOllOK1hhQqqfkuXhN0-9ROIdzI5rzUqBGeLSpFqN8e0F8VYSqWwb_-aU9-ktrwWVsS4SzdXGxw6mc-tBLophvkm40I3u2LTajp4xSSbrsW5pl4KOTgBG8-DhQMwVznyxA5jDPLari_zce3m615yqWv2LmztZHi9lG47HMOJ2QVTr1a7B-PTBEV-AEVxU8yPdgC9U5tEaYfpsvfeqrJtBlSCig9G2YAoiDJS0bhKORebBoDX9bnx_9sv0B_D8tRyZE-JKl0fsJ2Gq1VncCNrwFPQwd_jmcdxIkWTGhhDpwxGwnqcN0lRc8n97I9SDB79nxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkJu2XastD9AKAV5aGs-PdIU7zU6s9MMHeHAkk42EmMcAH5eSs7N538EeeHY0euU_8SxxqIm7FEiZj7bat6u7QQyK8-F6IIaBgo4CeENL8Qrn1Ir2vzEWWWoFct2piCbdTEX3fYhdoZ9KcrJ9w1zo8H29PyJ8lG8euCROY6IfVeaJyfMxAAS-RIR3zK2_-ZheGi3NxPnwDQmnzEt0-gM6d4cg4s2MJxRjXqZarC09DDrOZ33xq0VnEle1Y1uHSr-KxsxSOM0U7wXKp4TeVGDvjACEDdiZjhK7w1eO1N8S4pPZYXiKNbU24zQ51OQqOH9Ssx_gq-SmEGyFMXGtiV07Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhbbZwy1UNcjy-nVlC07C8HIbkEKLZO_PMinGphMOaOi4gep9gNIqkriYs6xJqLK_IlCc0LVpMegj1ugxx3t8oXdGhT1Ku9GkMMCm6crlD8EgarojWznY6infRp78ualU1oBonLEgQ8szZdyoiku0Gvms5glarg1N8bwKm6YSNgJKSNOs1dk3nGoYhpjM10GC5GScxV5OliPcRG1Tf7xYSLO99BDAkwZ3jHc9qWWMiIMoVw4J_lWCBpFtbNtih6n_EP4QPxaIHXnY2yhUDz-B1-ZwmnLq1lMn2ApmYIQYakQLPSz8E7Vsa6uhpGij9OvZmtiHIMW6y7d1iYeieqPag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=e5-Qekxr9FsovFhU8KOffQiafYCfsylBpJQYCJt1e8zjRuQTAOEpaHnzPC7_JdhlL2aPfMDnNhWnc1jPsQHFMn3cbyQAGGp7_1bIdAK8RH22K41GuFAOLFOITOPW_t-_CIcuOpjZnu4wnCNnS9ZLjGajUhWCKZ23qMiVgUL-OYy9QmwUhU9MG3cZO30yBIT6I86mnTNE-x3VA-3Y8xCooZaTR1TalbSWRoOyK_X3EmcQFWDKZLr7ZuR6RWGNUcwnJED_NoKyX69mDsicSZZUSoHERW7djxJmHbL1VltEwYR0QgyLEI6wLI2mMjk3J8ZqF9tSLE0gYZmTUeGWh1oEVDVEMvURZ8OOfNHf5BGpXuDbaUbv2d-y8TIliacYNG8mRzsoGic0W7YFLhF03pDn2wnuzyfx2jFqUAfWtuapkrJ0g--uSO7JTVAr1_f2V5Su2QyepW4oh9SS60Hl7x_MS35yFBKenJc_R9w3LH1biJetlVHZ5VlSLf6Hnrl8niZDTs4SXJakGguQw3bZskEO14IT5zZujyAIAkkNNv6ZjA781_pdfxrAFbhsosV6dGcn7-RZj15fq2OXNZ9dFL-EKgCGCZkCnyj7Jif_-XG0XLoGgRBXTkoULej3XyLEWeXcYUzb5XD8cn7RlN8oSizePWyBglHDUagF_LSSiRmtecQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=e5-Qekxr9FsovFhU8KOffQiafYCfsylBpJQYCJt1e8zjRuQTAOEpaHnzPC7_JdhlL2aPfMDnNhWnc1jPsQHFMn3cbyQAGGp7_1bIdAK8RH22K41GuFAOLFOITOPW_t-_CIcuOpjZnu4wnCNnS9ZLjGajUhWCKZ23qMiVgUL-OYy9QmwUhU9MG3cZO30yBIT6I86mnTNE-x3VA-3Y8xCooZaTR1TalbSWRoOyK_X3EmcQFWDKZLr7ZuR6RWGNUcwnJED_NoKyX69mDsicSZZUSoHERW7djxJmHbL1VltEwYR0QgyLEI6wLI2mMjk3J8ZqF9tSLE0gYZmTUeGWh1oEVDVEMvURZ8OOfNHf5BGpXuDbaUbv2d-y8TIliacYNG8mRzsoGic0W7YFLhF03pDn2wnuzyfx2jFqUAfWtuapkrJ0g--uSO7JTVAr1_f2V5Su2QyepW4oh9SS60Hl7x_MS35yFBKenJc_R9w3LH1biJetlVHZ5VlSLf6Hnrl8niZDTs4SXJakGguQw3bZskEO14IT5zZujyAIAkkNNv6ZjA781_pdfxrAFbhsosV6dGcn7-RZj15fq2OXNZ9dFL-EKgCGCZkCnyj7Jif_-XG0XLoGgRBXTkoULej3XyLEWeXcYUzb5XD8cn7RlN8oSizePWyBglHDUagF_LSSiRmtecQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKGBZXgoijw1Y0Fqdf4ZuhYE8J0I2NmdH9OIQcX-SdYwxWgNM5PiIPjB4W1zBoIbPF3bDcdabquEGGi2lamCYWuXEK1zKzddgPdsIqWF6Qe1TMrF03fPP6-psu64d8hU_OihglDzQGO9ezAP7dNXNuhUJDPGVEBERy2Wz9tDHAPw1JrqoqCsEVorDk3yPqkCL9d6CwRUa9c7K9qD1rP5WJ-1d_oVWfnBQrk4ELNlO1RXxZy2cpKlaxliIJSY-S25PJr-LB1HDvk2i84ELngfxkXGNA8jyJwi20cgvmkNqleIbg1qEMDaaAvuigxiICcCBl5QoVVCj4-3nlbe_zxV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCh37SWak7hPIn4GHGFPIAl3ZqfVsgxAhLnKDEnELEfp-C5Y9pViKT3GjkIGFJuPv68Dc0VrsBVFCeMzcMA_xMDSo5MRIDJuVC4LW6gjqgWzrf3N-jrClg3x7-I926NUPfqjbPvqn0F8KJjRHqqHWundUn-MCgymQpiZ8_8d_RTIUkbpdpt1BwVTnJv5fki0cdvRsEkQQuhr1QjqT-cTI0MwKYqfH5nrd3dEyXtO-Iqb9QIZJptrpbYEWa-R1Vdg0Mn2WTKEetAt5UZ7_EiQndiFMCyn_9rTHjraHltMUlJdhEaoMZAnKyg7zG3rYo-b-cjFZSKvspne6R4J1D7t8Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=GCg5F0C-auh58pWPN-NvpkQI-NvWcnClbk3xNknP4OyS_1UIziwBJ9htCuRUrB1HOK5VkeVyhjYVO-v6CqcfmdwUF9zZfRr-wrsaSX9oWc-E8y93ae0ehF7JVhvdj5lyWe5rCuS4j8M_6khPTFG1iSdN0pIjrBpc5Cvkt6eXEWXM0qBvn-UiKmzA8eeK_CCBd4VfmBuyXsTrEFdQRu5sBRfGxyIYJ4DXMch31j3KOKw5VqttzQR7nEyn1N-PmzmPJcUtgdavuPtMtN0q9XhH-J-5b6FfKOsINp7yf325ghzkXFh5TqxWqqS5CCP9nzc4GGM_5zECiMe1LjQpRLY9eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=GCg5F0C-auh58pWPN-NvpkQI-NvWcnClbk3xNknP4OyS_1UIziwBJ9htCuRUrB1HOK5VkeVyhjYVO-v6CqcfmdwUF9zZfRr-wrsaSX9oWc-E8y93ae0ehF7JVhvdj5lyWe5rCuS4j8M_6khPTFG1iSdN0pIjrBpc5Cvkt6eXEWXM0qBvn-UiKmzA8eeK_CCBd4VfmBuyXsTrEFdQRu5sBRfGxyIYJ4DXMch31j3KOKw5VqttzQR7nEyn1N-PmzmPJcUtgdavuPtMtN0q9XhH-J-5b6FfKOsINp7yf325ghzkXFh5TqxWqqS5CCP9nzc4GGM_5zECiMe1LjQpRLY9eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfrmivZGZ9mKyyks8zTeNHnIEi0Zpj2340EudOUlfaEZBPLfJWmqPEk6RiZHqoHIM-sJyZPCTjI3_BLOOG2sA0pEvPiad6vK8Wx10Qiu6uBtNZBqiuf1XOK9iSYgD43x8InBPzD66pgxrWf6W4jeGFaNwz0bR85ZFv5GcbH-cxg7TlIoDhJB9NxF8ohGIBHf3jnG93WHcnN-Hh6RBl1CMdduJh8KXxwmEHF32YCreucN7YG0CHALv4FQ-6qLvDI1Z2BvYQ0HM-2ta_k9Jlo1ajEbHK-Q0Jbk8lJSxBR2mCqr-iXstBqvaUAVWXzXJzZvbOFJWwnQQLt7wBUSXrRlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZnxcSCWrT1s00LtAurZmedqDyQMnF7Hlc8CUuefG6IVZ15rZ0_6qD4UNsVuNw5GuPZBZSHjZdfKIh3mKj-ufug26APvMn2OCcflYWklNAnZ70Eu-Mu8uUHW70zZUs6za8R7LBkGL0I31NxMaCABFMYAcW-lFSExyQYL4_XlHicmfy8GPSyUGczKNYizTP1ZhaO4jGN1W7r7QPJwZtamhIzL__uVOegsKYnNcSwxLbkdeJRn0lfv1Ez7kLCisOsXHGjnLqACtFt-C6gPYj2-V4rUjyFuUm04jG6FRUvVolPTdsD65JaU1640hur7YeNhqXlzZz6gfm1G6WmomLeH4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD5H0WdH_Wie6KpQfk8q8i3ECYxbmhZ9DsHTStBLHqdM8lyGT34qnlrIO9qRDw0prCwGDNqjPZ8dRcmMZ6HPakzIYh2KiYMevg7D2xZ2jkwpo2mMfMDepYl_jiPLtxKJaWx-UxrcAOxWJxiRaqcCZxqaGe5M6dNq6tWvqzByqislASJq7ShAT9joPfdPkMxOcblpAQhe4lEUSNHwM3kAeTuLIM5aUl2lj8j726_Z2J4VkC_omxRvWUG5nesmhx1RzsRzAheQ_-K3SX0jhREqZRXJC5--Ht6uqEtweocSF38i0v68cTC3o---bwegnuBbWyYNasGhxJCeq4iO0VPKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf1Eqy-7GRn5Ac4F4rj0bfSBBqunqcxZpaPqioVczxwTH6KqBxR4zmLhFOGshxmG3PWv1pge8tR95XC7FOaZsfvomyNO5GW_BnCEXjtslDUd8iJd7CobF48laTfhqaSCPg6Z8swe3WBg2fS4mLp-mvIqBMxuPx7D9VMcyyAJeAv-r6LxDOAIJ-4p53ULkWdY0LGF-UyyyriPRc7Q3Jmi6K2ay9lE6M74__8ZKAh9nf7c_2zBdBJYvUW5_j6ZavX-TwcFTQogmd5bGr7b1gXPJ5Rm09HkHUEVDOsIml3SLsHfjBjznIM-BMMmrmtK5KNwOBQwTxMYXWDwvHL4By3xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enQ7lntZ2bC91VHCCI5CRbRTQT7E6coMSFJcYRMhVFx04nSsBqnxvzp29k5v6LpEBnYowBVC3tX93nCaN5UFiMhjAPJaZwmtf4D-UU6sUwZsSLJ9BULiLjC23nHT70F0tPFN4PhAz0s-WNuqtxlYH-DD_RejGYjhWBZphVoHre2IWjikFWjs8JSA5FlWYMypF4MAGXyZfOY-i38EyvTDT7zRbbTZbC5qcl2PzkY_1oExIDQddjtodjgd3AkQxn7bhFEKHj75XOB1Qqmb2syZo_YAjLLHhInzkm0hRIP_Dy4IGjEzmVejaCxnIE-M6MskLjL7pF4L5x6mbQBEPn9e1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvJm5CxBczPWlackf42K0TddrCj-uwmhGLI_poCqqQ6x7Fx_fHFD5nPNbt_KOdm4HD54kEfdriM8ppZbhuEcC5XYtfQZBbjX9ortNp9U943vVWZo1olrCI9rgOjY4TionMAjHJt6mJdB3cCy9AUVuFMbBntvPRnCtBnuO8-ccRIFnaXfCN8fhBzoI_AicM7ozrOrgRrlIEGb4iqebb6IsmqmLctpj1_39WwS09ca34ioyrZGq8i9IyXopjq9VfE4l4Udv_J5XccRmZkfYq02NvoeeC3VJxCLrjSgkAK9E-zTg2zZUrqv5UOYEyOtTimaHVMo-HaIuITWHhOiRN7aAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glIHcM5iKJVHViZTRBcUMPngpBB9iAhk73JRiBkQiMDroEvQAbY0CXjBmmFCddohGcNhJBlpVdcstyfNB70zof73_gEh53FbJ7xOjUq93VWsXxq7nsyQP29VS6RLAA5mg6_R8jL6YX1vjFioOG-Abz0ZIFFIA1Cybac_bs82M7uShxBOhvqw4QqkmBhGFhuOeSVE0PGmGu8tuPQJPFv6EkcDrGngwEz6iNg-DQ9yueXdM_96It-aR94LnZp9gKgV8uvJMGvXtrDT6pw-d1LurroLosqwZOxrMuz8pW7cMFLYHF1r95497Ca1F_mOhTHU8GMoY7vOofCQNCmhrTrm9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG9JQr2gMPMtXmq-L-7ncbzoOkQTRiV8iohnhka-wieMfIE6BWph4d1zuQGH9VnWLccHb2YOFEIK-OJBhPkd1UtDPcnIAahK1R89K2JVdXfOLFBQM_B5tlAOam2yYmu11XyluBwrzlgJSW67f1RIyChDGr9t8QOMVEXZZ0RxEP0eTGp8H0ta_NrsIZaPf10xxmNZNRdyesW0gNbzqFnM7HBNtgYGWe27w0Qa6MRvHA7BA6xQ1iz1p3w3U92FeEVmPf5dyS07kMLzBwAwR2pwqiC5ulEcwAx0Nv1TdEF1OWv0nPnMH0AvSViv4xnPhKgjrpj6d4tUKrsjOxhO8I0cqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8jyXL2t9fj20UPDLtn5gW8VWyPcCtSH6krFc45iQLIYO20BwvSQqp_mkYjqXfi9rYA-KGMe80mIv_6uJwzHHzUlGPcZY5tecFyj-PS8xnnHwv8JNhuPh0hbvIU0fcP9t26edUAF0Yag4s4zU7zciw0uZiUociCpcujS3F4Hjprbl03V0o7Haex679b8FWDIWlNCaxXNMP6vaynUF-aUccwatdzZBk17tnFOlBxeqUcmVjGLNPdJcyuTnRgqyeegl9kSyCWNdG-MqkRpe5Grt22bwHsyY_86ezoGX8JAUvLIV7Ul_F4rMekpgUI8xxdr70__9Hsg6GCJ9pSkrQYBUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=OMqnVKm_YwT_I-lj2KmLZWDFimpIRgmLJC35-pbtu-hDtGsbQ9WsKS1XvmlAuOQGBtv4Tks9LzLJUWfC2WfLb5orMP5of-OUHD7NWkx1Ayyv5nCrgU0SF8Jzz0XebcCl1v0D5dR0hhuIPpZ2JYuvCXi0ZgAhKdjA5MnQ3f-BMLAzBBEY4BQ1_PGf06y6D7921csR33-YHnJk0ImMID5JdRZsl1h6kZ3P70aSx7QW7BBqObN2n3JYmmfahSdHIrL3Rq2a22cX0bmY21h5LuGYkK7-oNqEdrgrX8AH7girXXTYoVyEDgKYWO3RqVpX6l_E3il4Ox7c3IgeHY1ignNzlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=OMqnVKm_YwT_I-lj2KmLZWDFimpIRgmLJC35-pbtu-hDtGsbQ9WsKS1XvmlAuOQGBtv4Tks9LzLJUWfC2WfLb5orMP5of-OUHD7NWkx1Ayyv5nCrgU0SF8Jzz0XebcCl1v0D5dR0hhuIPpZ2JYuvCXi0ZgAhKdjA5MnQ3f-BMLAzBBEY4BQ1_PGf06y6D7921csR33-YHnJk0ImMID5JdRZsl1h6kZ3P70aSx7QW7BBqObN2n3JYmmfahSdHIrL3Rq2a22cX0bmY21h5LuGYkK7-oNqEdrgrX8AH7girXXTYoVyEDgKYWO3RqVpX6l_E3il4Ox7c3IgeHY1ignNzlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در حرم امام‌رضا چه گذشت؟
از صبح رفته بودن حرم که تابوت خامنه‌ای رو ببین، ولی تابوت رو از در پشتی برده بودن، اینها هم شروع کرده بودن به اعتراض!
از ۹ شب تا ۱۲:۳۰!
اعتراضات که بالا گرفت،
به جایگاه حمله کردن و با خادم‌ها درگیر شدن.
بعد که آروم شدن بدون هیچ حرف اضافه‌‌ای، خادم‌ها رفتن و چراغ‌ها رو هم خاموش کردن و بهشون گفتن خوش‌اومدید، بفرمایید برید
😅
حکومت آخوندی، مدیریت آخوندی</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6006" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=dD7eDIVQuYrVQoeLHPeLXi5cQZMR3QGZ96I0S8SGLo6rqsd74-n-YP7QqqpEtJFk_2enAIo4BoNb9BMUiKkk3tQtEQFVXfH6oYt1TeLoM7jTMD_nPeaDXXsMRReZgNSlTRwxio_AnYrWPN42Oj0mIoVesJMTmTv5TUhSifFnvnzySPRlusfSq3mSMg4BmaEbHcRDNnimNMpUjM-z4o6ZzNeTIpAaWFXd22KAZp7KCtkDcYPwCK0sfJ18jbiiN1Rx4E8w927Hw3PAoOF_xBw-3QHvm5-Dq79UItIBnrqELPlU8Z2UpbTqU1G7ekM5v4wBt3POm4TjCE1JLPWP3O1dMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=dD7eDIVQuYrVQoeLHPeLXi5cQZMR3QGZ96I0S8SGLo6rqsd74-n-YP7QqqpEtJFk_2enAIo4BoNb9BMUiKkk3tQtEQFVXfH6oYt1TeLoM7jTMD_nPeaDXXsMRReZgNSlTRwxio_AnYrWPN42Oj0mIoVesJMTmTv5TUhSifFnvnzySPRlusfSq3mSMg4BmaEbHcRDNnimNMpUjM-z4o6ZzNeTIpAaWFXd22KAZp7KCtkDcYPwCK0sfJ18jbiiN1Rx4E8w927Hw3PAoOF_xBw-3QHvm5-Dq79UItIBnrqELPlU8Z2UpbTqU1G7ekM5v4wBt3POm4TjCE1JLPWP3O1dMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYK5RYXX3iuWU6eedzxfnfMjhmrFh-_r_lTrcuPdkOlCuYfC7LjkXXHETJuXYm7dZegQhhnB_OZ9QMwDdD4XYsaAlu6MN_FuFxb6f1OwgqML_eNZdpsEgChHUt1rB2eTIONB0nJoZSjdOZB_SstUQKOYwAEJ7Mt6HAvxwv7sHOhbrfK4OYhvvtbE-CCXAXQEVoj3fe3or_lXtHi_lx4VOGTumTGA6r2ZBTHmNQas0iDj-xvbsO34DQ9PrxROZv8OlS3WbpieMcM4rSU9NJYDdQBMTxjT1mJRqByJy2ec3ReTD8jY-ONlP7L8bs5HasK_vnqjw4zXUvt4bgKXEfiEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzZF4xQmXZP-uTGngEW4ynizCyrUbq9LK7thLy5B54dqpj4y1lBIyoN-eqtiiVQkP61FTmIUWSrrqQSh-pN1h4ZoiSk0txgHllRkMW2-iiyxF3Ii1MwP6C7n772-6aXkr0I8lIa6n66gxAasX2rYlf4o35gLR0zO71k41CONP7NLu585syzlBsWNni2wi7cEhENgpLDrSuxHOyVWd9Q54lJ8occpXaP-Q0NTfP2TvsKlIK01mRv_DTG-OqqBbQOMAhx9PHxdarMCQjNi_lQARQyITfnaN7h1mUPsYockPstdJd7UkwiSewS1e_RjG9svbsXJUoeQpQlE3SOd4Usw0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6b8LEeTI5c8PHmdocWVWGewoitIaV77FJZCjGP6lEDKOyOxCm10Mh2mC8X-24oPuMfAKvB26xHTNZ8bSBdJJ9XfjCpESazgjXX2bb2ZWelN0bFKlQqCJ0TMy6OiAj8dsTtnWwWnQZgh1o1MYpTGuNv_JApK-4GgC3_vAKpKcS-R1WHXvoPfK5q5MvjI2wFklRVBQQ3PZThhcq1SuAqw-UhkDgV065hUYik4uQs7GDSOjKpopaVS6_wSE955lzUqMZ77w3q4nuMMxwXp12YynUDTqtbJY4dupI01cfizHK1YyWULz44cnUWFMP-coYnaP1tuqRA52MkqokwVjgKsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlnBVnSiSH39af5m10RgwcaUe1ty9KyPYEJzsMj4xMVv6_--o80qJ5R205cp9YL0yvHl7cTomXfnPAoDLIKtL_TcPub05A6AZboRVRxdFOLmPLW0BXYmLbwEFO7PFtXwYd7i8ifjJGdm9tYs6xxVuY0kWmfRUM_rtBAETbOALjtTHy5fcVfxcDzsDqMG4MA0yxLZLbDORZATSbAR1VRtPpNUxf-civtzHTdncrCqPyDShPztk9DNInUU_C6E7Icew0XOcBCaS7aaAAWmePd_yv2iESGPuCDVdf_vyA3D6dPS2KbO4pLlbczf0tR-ifSMj4kqcNbpCEkSJ_mF7do4UxcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlnBVnSiSH39af5m10RgwcaUe1ty9KyPYEJzsMj4xMVv6_--o80qJ5R205cp9YL0yvHl7cTomXfnPAoDLIKtL_TcPub05A6AZboRVRxdFOLmPLW0BXYmLbwEFO7PFtXwYd7i8ifjJGdm9tYs6xxVuY0kWmfRUM_rtBAETbOALjtTHy5fcVfxcDzsDqMG4MA0yxLZLbDORZATSbAR1VRtPpNUxf-civtzHTdncrCqPyDShPztk9DNInUU_C6E7Icew0XOcBCaS7aaAAWmePd_yv2iESGPuCDVdf_vyA3D6dPS2KbO4pLlbczf0tR-ifSMj4kqcNbpCEkSJ_mF7do4UxcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OjZ6J0ErwoI_BQquNfrfQqEGeLLrNP_szyji9DBqpzFHISGvSi8ejPyjWb3hmHFn1GPkz29XlqJQYoacI41n0IvMuuTlvjGOxO-xJ5fGk_IIbS6TcvvTXPtBXiq2T9n-a8huMdHVf2sSpfJcPSMV912AT7UQFDX0lZjfp6HGbCO49eiaQZAu_TPWLZVKoFCAKE5kl_Si9OVOKH4lvNDSXVk-PJr1bNj2JlTivw65atzEtzX_E1RauVBD4M0lqp_-0_lRqvwTjgRBlnjFXaveOVyfM99_zdqVQB9mWgUe31kieSQcaHsS6NUBPPwOfj-7gn2-D1TKaTMz3Dbn7l6IO4lJ-Lw6ItRMfnueRTMqxOxvXPy3E_OUM1JDbu6u5H4XL2BiSLqgQqWCqPnda02z5Hm3ng3vIG1txA17tZYasB4-cRKI88WglsykA_B66bL5d8TFOh0f9fe9gUXdKdeCMjRjY3DnnVBhbUpu-nCpfXiz3NMCngrfynHUjPWamPGWrDY1gS-UtJtB4w3UGWr4L0sBcyjPHNRXguQ9wyfFVe94n_Ug-R0q8BJYcwxnDjYoIHNOi2S_nimecHKATAHGid2HWnq8AfOo4UEHMbcjY2a_9gWztORU_4Js72ygLlZVRh3SVQDC9dMGw5uXBCHzLdefh2L8DhoKsDzVXW01l3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OjZ6J0ErwoI_BQquNfrfQqEGeLLrNP_szyji9DBqpzFHISGvSi8ejPyjWb3hmHFn1GPkz29XlqJQYoacI41n0IvMuuTlvjGOxO-xJ5fGk_IIbS6TcvvTXPtBXiq2T9n-a8huMdHVf2sSpfJcPSMV912AT7UQFDX0lZjfp6HGbCO49eiaQZAu_TPWLZVKoFCAKE5kl_Si9OVOKH4lvNDSXVk-PJr1bNj2JlTivw65atzEtzX_E1RauVBD4M0lqp_-0_lRqvwTjgRBlnjFXaveOVyfM99_zdqVQB9mWgUe31kieSQcaHsS6NUBPPwOfj-7gn2-D1TKaTMz3Dbn7l6IO4lJ-Lw6ItRMfnueRTMqxOxvXPy3E_OUM1JDbu6u5H4XL2BiSLqgQqWCqPnda02z5Hm3ng3vIG1txA17tZYasB4-cRKI88WglsykA_B66bL5d8TFOh0f9fe9gUXdKdeCMjRjY3DnnVBhbUpu-nCpfXiz3NMCngrfynHUjPWamPGWrDY1gS-UtJtB4w3UGWr4L0sBcyjPHNRXguQ9wyfFVe94n_Ug-R0q8BJYcwxnDjYoIHNOi2S_nimecHKATAHGid2HWnq8AfOo4UEHMbcjY2a_9gWztORU_4Js72ygLlZVRh3SVQDC9dMGw5uXBCHzLdefh2L8DhoKsDzVXW01l3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7iMTnsg64qfEr3NhxUk95LUBkF87DZDepZcNp1gG6NbE9MOktLJOJZWRpEJHGm6C4w2rkM5oRR4O2fyBSlU2_dEk10boAedrGr7Gd-72CwdNt8-ZxwFjk1-7gvtDSgS__wT_B5XUzBGbFSlHy14SbsVuQ-rLXSKq4NwtcZ9fY63DSbIWs78gkD9Y-scdiycTEVVw7fXDW0QyKYIPsT52xZnuKmJBQJx-EDj7dZ8Hx7jCh-SSJiy12j6X5ovDfhl6F3zKRJZCbEOUgPWG1cPTMEZ23y56vduoXyQhHOhvBOHPAT-gWYCN1yukEgXDTCmUBQJfabyFSdKDMc9jlp2tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1k-nF_jLSPCXu6MP9qi9GSaRU4JmotrdtaRl4ufe5lHDCWrY99oNtTTw-nyvl-wG-KFxlmUzK5zTE8yV_DAWa7w9Awk5oQDWSIppf3Hb0Wih6GqnloX5bquEVYqGQGTS4sWKnPp8TSMg3NeIgiWI7BkZrd4xO7VTwhMbyK6KHcceJTVUPLe_d7dkOaN_DHh0X-3HSvtmwBwxOtikU3pl6jvvDr4mS4TkJC_Zs20gxEczr0ZKnLHbWTN8yxoihVhQNIyg_J-8zVcypAe3nUC1jlzOvnhDdrJGnIjIGrDXQFrtNrf_ZlxPOi_OIpAqLDD5_40s-9iYJhdd5dkinQS5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVLM-_6JVq25vnSlGz9gXp8IK2xr-RDSxZguqk7wAxg6iP4VuWYGwjASJY5sENZmxlj5wI00Q5cSb4IR8A_RgmWaXcolTsMI6CliekVOEtlcIK3y-OYvQDD3G9BRqL-gALBNrGHOFpIKl6Qwy6Hg4NXi43VaADw0x7GPxaTTTvONYoH-9AeJ5OiTZcOlfl8ggcShZDvgyy7MyLQ1MPANr1vkofg3f4ggKMV2w8rlO0jr0dNZTp7qTKt_hiXa9XUrFL44k8usmXYS3LapLLhdBiKncJcdvoZOzcxW2BH1MKJkJSej6n2HctWSUCbsXO1BzUHxF35t5L0qGYvLpJJQdQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=jjoCRElkHjGMTZeb5udnX1dmNAhBR41TDh8yM-fsoj36gxsWElJoDUWXxrIksduAtV3bnhcIMQZce8fGQL_QltZyN42HNCVlnnvxhTwboGogfMXimjw_hCapUTt30PpBRHzDNy8V6CbQ9RKsnaB7Edcyl_4Zi9S-D-6J1vYpy2ghrd9drTlIorOK6VXXgBer7Ly-PNkKqISR0sW13VMHdE6QoWeD9yyX_uFCkYtdUVfnLpvilNUt-vN-KnVZoJSiSvWhFAz0YGfcp0VM6yMulb87UIZn3it9VCZ3nMdR9olgNKgmdHoFZrDV_C-Q98Af_doGVl5VKtfWCMAH9cul-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=jjoCRElkHjGMTZeb5udnX1dmNAhBR41TDh8yM-fsoj36gxsWElJoDUWXxrIksduAtV3bnhcIMQZce8fGQL_QltZyN42HNCVlnnvxhTwboGogfMXimjw_hCapUTt30PpBRHzDNy8V6CbQ9RKsnaB7Edcyl_4Zi9S-D-6J1vYpy2ghrd9drTlIorOK6VXXgBer7Ly-PNkKqISR0sW13VMHdE6QoWeD9yyX_uFCkYtdUVfnLpvilNUt-vN-KnVZoJSiSvWhFAz0YGfcp0VM6yMulb87UIZn3it9VCZ3nMdR9olgNKgmdHoFZrDV_C-Q98Af_doGVl5VKtfWCMAH9cul-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouxaoUXhmX5IJhU3iO4lg3xfs5QySCcBYGof6tshA3af4WdIYDIsEX8OMJvJ6RNIyYSiVsG_ccllaWhKxvsaleGIuWknCQFKJydllLdXnUqYa9CTcChBazK2pjNUhepQExhcervs8ageH6ZXVH-VDafB0T8wpOjyE8dJLwbcy1dWNlTWDiCWb3e6sXmp99dp8JcLVygv08zQwJn1NN3BVAerWTc__0_zdJpODlVG30teyysJ6hmiw_H6C4vrnF4p7FvtKuUKfCVMrAQQQDq3ET5em5U2tUL4uU5J22fHd1eYS4uFRIJk25YApEl1TQLrPfI8PVwM-ogNsjIrQluJbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=bFyl2tH8lDoUOsg6ynW61f-pVY_T4N_WVejuyY3uNrWyOBUvFejNAVbj-PSDtK_DYsoqF9NkRwpoUR4ucL6AfGcy2wuQJU8iWeDqmxuRVYs2YZPCwW1HJDv9IQHrYsHv4bVv_-k7ZNzqeNiOe5S_vgmqONTZmkPShqbBhxVk_AlgQnP4yfRtROCbqFDliE85XIRw6V6tRoJlo7SWkgL1ALqQBw7Hhuu3BK_z7F7DRH2wAKXYn8jDRL9t7yZniG_BXNeqy4lm7gsWW50IQWyJPVp8K6gOeZumsQNk_SWXIfolpdeMP0-7o_kOo4BoYbabIiE4dyRufGuSVSZ-uvC7Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=bFyl2tH8lDoUOsg6ynW61f-pVY_T4N_WVejuyY3uNrWyOBUvFejNAVbj-PSDtK_DYsoqF9NkRwpoUR4ucL6AfGcy2wuQJU8iWeDqmxuRVYs2YZPCwW1HJDv9IQHrYsHv4bVv_-k7ZNzqeNiOe5S_vgmqONTZmkPShqbBhxVk_AlgQnP4yfRtROCbqFDliE85XIRw6V6tRoJlo7SWkgL1ALqQBw7Hhuu3BK_z7F7DRH2wAKXYn8jDRL9t7yZniG_BXNeqy4lm7gsWW50IQWyJPVp8K6gOeZumsQNk_SWXIfolpdeMP0-7o_kOo4BoYbabIiE4dyRufGuSVSZ-uvC7Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXqMDz7dPPgyDeoFaE0ldycju-8JqffcISvgGKJNUJxDudZu7blph3oP-1YJbUUBhGQhekIpfexdx62PfkqpuakCvzCEp1sehBKh_GvS6DSeDfaQb-Kqw2QRobI6skLsf_yNXPak5HH2taZF8D0YV_ul08Qx_sv1qPdUs1X7Qjkk4gw3VK7LIKOmF-ggGeecuqhTGeCzLbz0jms6GeDfabMn5si7S2alUV2fFQnGjkVmu-24-8B4a9UgRS4VI53yRrEpUauReyi_cRZ-XFIXD4zQgcL10vRiJuwWogJbxQtttRfNszd2fKVoGovYWOUHTRpww4IBT7ws5IMGtlDA-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrHi9GiXavv4W1aT650styC_P96ebWjIpJ6fDU-HQ014hCEJ5l_mplATSGbCloKWVQnH3axG-GdCCMZc1Ox6kO2mwaPvSEyo2yE9zhCqlq-9pWoSh-SK2Z2lb3U0BZyxdEGkWV5d5xrK5fXkLBM0w6cGohMzC8lcobjNX2tFWpf_FewUOs7_G6ClOp1KliR4wTZfqfUTrAT1LYEX5zCqdszTmhFIcVS03DF7hdRaDhNSUYbswwLNKxY15D9qXBE-Z-aRv2N_jhQ_6sX3NgW-doRyH3VurazH1MJeCE8Xpmigesc8q8s4N48nYPH3amoNtkZ1TdtM-_14bxE9FyT_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=C5bjn_u51JqqjaJ4kbyUS9hEOFENZA8BdPlVCWGg5viWT30yp7eluUwzqyU0rFF8qg6gD2WBpcfSzXr376sOG1qCc-9pQrdKhh7S6t4fhMTpthlIAEFvwjSHVL_v5Uvnm3inUgdsBD9AlMnfrpNjsqMFPtTObuaJqYr1Xk4klDNmaNHXiT3KlPB4BYp7HtVirs3VrIstN2rYfTwlOa3bheRuaoTv-j-2wW_NuvcM1g2PBIZamxO-ztqbZaYbpun5s4Qg9qYwRtptTgcC_hAVfhlmV_DEfFlAU-N83S1-sjwsoOHWLncKVIh2DDmI-zNmdHIuyg-zV7fk1ugoGluOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=C5bjn_u51JqqjaJ4kbyUS9hEOFENZA8BdPlVCWGg5viWT30yp7eluUwzqyU0rFF8qg6gD2WBpcfSzXr376sOG1qCc-9pQrdKhh7S6t4fhMTpthlIAEFvwjSHVL_v5Uvnm3inUgdsBD9AlMnfrpNjsqMFPtTObuaJqYr1Xk4klDNmaNHXiT3KlPB4BYp7HtVirs3VrIstN2rYfTwlOa3bheRuaoTv-j-2wW_NuvcM1g2PBIZamxO-ztqbZaYbpun5s4Qg9qYwRtptTgcC_hAVfhlmV_DEfFlAU-N83S1-sjwsoOHWLncKVIh2DDmI-zNmdHIuyg-zV7fk1ugoGluOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=I660bVkuzvgAThU6GlBLHD3xkvGoMxqUDnBfTXG-5RkIp2yKNaOaueMVtvJZaj5T7Dt-5PCRNcro_REx6g7S7iO8nClw_tXwmDtLqBgHbDbwWxFYzMCC63ZJcEB9CApclv4wjY0hzxPBd7lhm6KAyIIA_F0sBDcYCSAyhLdfeEMTdHQOPY56Ck-Iw-mwrpox_IvHVHEdQfUOP9o-6ujsvqjkzTc_JssuJA1KlPvHjszBbSCASUxk6DFdUJajIN5sMofCK1VrRjJXaAwoeoWwh5Ns8bcfEW1kSpAvaq5ZZIhhZ459IjZ88DDlyPilu8aBsgo8a8UB-xrw_2JId1qxkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=I660bVkuzvgAThU6GlBLHD3xkvGoMxqUDnBfTXG-5RkIp2yKNaOaueMVtvJZaj5T7Dt-5PCRNcro_REx6g7S7iO8nClw_tXwmDtLqBgHbDbwWxFYzMCC63ZJcEB9CApclv4wjY0hzxPBd7lhm6KAyIIA_F0sBDcYCSAyhLdfeEMTdHQOPY56Ck-Iw-mwrpox_IvHVHEdQfUOP9o-6ujsvqjkzTc_JssuJA1KlPvHjszBbSCASUxk6DFdUJajIN5sMofCK1VrRjJXaAwoeoWwh5Ns8bcfEW1kSpAvaq5ZZIhhZ459IjZ88DDlyPilu8aBsgo8a8UB-xrw_2JId1qxkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=q1TkPlN6xgvvE3RsIaD5xQPGb_ggJURBzOwMYONusQ1TV96M9VCm1uVzt4MSWVmIgFgfnhEc5g1yUFP_WPe2XiURPyqBngxogxClsoEF8syvaDTUtTf1rQ16dxF4wqZEOMxRpynQ9ERmXNzBCKIU9eLO-IyUAwkwvBzg2k72slfJdNNhdGothtYiMb1gogE2ReyOkaQY2SI-dz2W6gGujrI_k23TQpcZDzJ3svz5i6fHPI3CxFqlqA-kGqnlIvSOaaC_86ubFv_iA0SOsJ51b16C3wLAdLYwkSbjUMi4Y_9bwJSdlykOwFswdQYRGGDUBsDAzXWhf24qISLC4CVtcXczdF7QJww1x7AnakYU8YDfmdvXJk4jQvKOJKKSI8a9B_zcmkA7b5P-oDDapcf5rVGnXHunBN1V1jJbm5tozLucT3__69s90aq_gK8NjJBHNQimpWxQiOOtLPfOieaVst3grKGCMbCEyVZrQbVHsmN9hEezzdJNVPMNfBWr3ir8TLYPqhlokcPNgc0tdcMwttcCQRji02R_lRxu3tv6luUlP8s_LyLED3zzFk3BKX4Ic9890ac_vvzf_6XvbQckwHZL27LSbMxcIh6vpuxtwOTzwiQJHGGDoToWB4HPA1Ke8r4q0LbcGsRPw6QgBbBrNomZ3I_tXS9OIm6gW3AmBa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=q1TkPlN6xgvvE3RsIaD5xQPGb_ggJURBzOwMYONusQ1TV96M9VCm1uVzt4MSWVmIgFgfnhEc5g1yUFP_WPe2XiURPyqBngxogxClsoEF8syvaDTUtTf1rQ16dxF4wqZEOMxRpynQ9ERmXNzBCKIU9eLO-IyUAwkwvBzg2k72slfJdNNhdGothtYiMb1gogE2ReyOkaQY2SI-dz2W6gGujrI_k23TQpcZDzJ3svz5i6fHPI3CxFqlqA-kGqnlIvSOaaC_86ubFv_iA0SOsJ51b16C3wLAdLYwkSbjUMi4Y_9bwJSdlykOwFswdQYRGGDUBsDAzXWhf24qISLC4CVtcXczdF7QJww1x7AnakYU8YDfmdvXJk4jQvKOJKKSI8a9B_zcmkA7b5P-oDDapcf5rVGnXHunBN1V1jJbm5tozLucT3__69s90aq_gK8NjJBHNQimpWxQiOOtLPfOieaVst3grKGCMbCEyVZrQbVHsmN9hEezzdJNVPMNfBWr3ir8TLYPqhlokcPNgc0tdcMwttcCQRji02R_lRxu3tv6luUlP8s_LyLED3zzFk3BKX4Ic9890ac_vvzf_6XvbQckwHZL27LSbMxcIh6vpuxtwOTzwiQJHGGDoToWB4HPA1Ke8r4q0LbcGsRPw6QgBbBrNomZ3I_tXS9OIm6gW3AmBa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIdiN9_gn2RzsGrMaOEVaMxBpBVFtSUynfP4hYZjWj1ymQlRTE3D1XCkhH17rZ173Bww_gF33O_RDxY-fwU4ojlNi6vDudGsM-Md4Vm4BzWR7lOanDa2467PxL9HAUCMrOU_JYY9rHHqibcwNbQwDBfHbe-g6UxOumwWX20jcp7XwViWFty5MVx0uZdBWH9y84SXp4uvfYUloVKSFq7CGf7bXaSc4qkgMjaJuEESDl0UfAprnfl9fpBAKaPEN1Ybk_EFGHyCUVVKqgY7HsHEJ38RP31_PegxvnGXlU3oO7NLZOz4V_kG5gTT2MCGNReqiY_cXLzicZW4ap9wM-nKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeW5Y5kV1SUDHzrnB2pDJg-vzWXG8ojbUrCmWEerzHl3YdREnJsHIjyeaj3OItekFrAbK0PbSiDn_PB6lQEDvU3wXMTKzzKeHa_RtKhfEaek32EjAJsM66Q_KOpURH3wcFWXZ1IV9ZEEpumCkGx9J_kQmj0y5ZugTfcrl4a8E0yyUw9O2wWRXmFbgysDMOXJJr1p0BMnJ38BBpQddebr2bA3rHbhE_fHmH-WXD3AnBTNe_3G8zRjtdFeJZd6em9HZ6kwgiiAjRzwwTKh4FwTFREF9DAwgsDH34Xf7X4HvT_lz128CNYOwISdsInX99Ps3EyQgT3oC9nmbDYXJsIMOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOjaaMFSGN0dslDUJqJ3ZyXqFClIw6PgKCoHjSUHJT7-djidkJLVNGFfIM-NQD4O97Wyo04k0XdQZTKiFMwl6jV8bya7doTFnMDrPPh-jDXeJ6dyaY-jVzqyzhGCfuxpoQOp9UWiZHuf4hUdsdiBH47bGwHKknISzkgVTAZ8cNV84Xs9ZVHAGOVyiAzTSvz-ewBQ5dapY34c6lnlld_zW5qFclmw6ZubaO4txak9mM0bF_IHF2NMrEAV3FNu3cFBEA5VG5RNa0MHSP3FOrB_IQRtMvVRm_jVdDnwxjNHMOhsgAljQWCWhvU-c6Vnj-HNhHr5d4jz27QgnRusvIQq9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=EzDa715fGI1cmzdbaFeen1ICcW-Efnr48G3Mr-_C5S0VUaGjFdqNuCRAl3hjHkEqJOPmod5XJlTHuknkxluvM0MqqvonViDW65uOoOmC8KNSUez1EU36GkSxOGWoPoQrqBB-NG3vSmp_nU4Jqy_WJ6U-wyjC1VOtHLg2QD069ixUSWgblcQhUzBwVoBY-HnUl_s_1qjtufOk8RGClYL1p5sUpvi13-GBgXym0ELwybpE2iCKcc9M8SDW46wCX5OK-zSopmceQXygu4bPlsFY4Ip7lc6PSuYovagAa43qNfu5OrV8Xdy0TEmCe3yLXQOVCHkLUUJ1xRXGNJ04UJ-q84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=EzDa715fGI1cmzdbaFeen1ICcW-Efnr48G3Mr-_C5S0VUaGjFdqNuCRAl3hjHkEqJOPmod5XJlTHuknkxluvM0MqqvonViDW65uOoOmC8KNSUez1EU36GkSxOGWoPoQrqBB-NG3vSmp_nU4Jqy_WJ6U-wyjC1VOtHLg2QD069ixUSWgblcQhUzBwVoBY-HnUl_s_1qjtufOk8RGClYL1p5sUpvi13-GBgXym0ELwybpE2iCKcc9M8SDW46wCX5OK-zSopmceQXygu4bPlsFY4Ip7lc6PSuYovagAa43qNfu5OrV8Xdy0TEmCe3yLXQOVCHkLUUJ1xRXGNJ04UJ-q84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=J0j--uxr-Uv6LDmtdEyzdLPkP0dMe7FMoXri40Zy4sRV6N-Yh1U0BvjCQSo35GCeOUcofoBloToA8tu8laRt09sV-_4UACpU9TENeaP38-i6YBuZ_Cw25h6ZY-nhuxq-v6Ojkz0C3gqoOGTef6htu52knznePRS39swrX50rIHjA7UOPGjsLObk8ZcfiHGZcOCsUUXRjNXj_-xcxdbd0g-YWfvN1nngCT5wz6yeEj_Nzzj_lylr75u9M0GPUZU0m08xXTx0tCXgcMXUOkwsnHt-GvdpNDZ8UGuwrjdkClAbELqdnIdgh3AkItnqof-08dAouqECFiAx_YXR_K-k4og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=J0j--uxr-Uv6LDmtdEyzdLPkP0dMe7FMoXri40Zy4sRV6N-Yh1U0BvjCQSo35GCeOUcofoBloToA8tu8laRt09sV-_4UACpU9TENeaP38-i6YBuZ_Cw25h6ZY-nhuxq-v6Ojkz0C3gqoOGTef6htu52knznePRS39swrX50rIHjA7UOPGjsLObk8ZcfiHGZcOCsUUXRjNXj_-xcxdbd0g-YWfvN1nngCT5wz6yeEj_Nzzj_lylr75u9M0GPUZU0m08xXTx0tCXgcMXUOkwsnHt-GvdpNDZ8UGuwrjdkClAbELqdnIdgh3AkItnqof-08dAouqECFiAx_YXR_K-k4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=mBeT2axwqFnGwcZfe2heMUi6WBHtKoueHDTcHLHi1RnXgM-JfN5dV4EsjfTr6uSgWtz_uY2DKBCqmI94Dd82PmxHTHrfhUhAVYvtB8AcGoqFWZiOtydWAWJFnh7hFxFxksCpcYP_TwMbkcJahGHWZCIuwacKD3XCWHDsFjnLJUnOxeJ2XJeHurlQ-ejuu2dUDGJ4dwPa8Y8SOS5mO7y6CC1z1bUrH0RSx_SZrbjAbDqsHoKRhbLKuCiJJMg5K33mQ_4cjAipg_xY70X_97heeQQ13HHajHAg2gO3mTIVzXklRp0ivsheMQ5LU-cnP1-Q-rDQLFxnfgbExCs1M84agA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=mBeT2axwqFnGwcZfe2heMUi6WBHtKoueHDTcHLHi1RnXgM-JfN5dV4EsjfTr6uSgWtz_uY2DKBCqmI94Dd82PmxHTHrfhUhAVYvtB8AcGoqFWZiOtydWAWJFnh7hFxFxksCpcYP_TwMbkcJahGHWZCIuwacKD3XCWHDsFjnLJUnOxeJ2XJeHurlQ-ejuu2dUDGJ4dwPa8Y8SOS5mO7y6CC1z1bUrH0RSx_SZrbjAbDqsHoKRhbLKuCiJJMg5K33mQ_4cjAipg_xY70X_97heeQQ13HHajHAg2gO3mTIVzXklRp0ivsheMQ5LU-cnP1-Q-rDQLFxnfgbExCs1M84agA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=NO64Rh3Pn4DdSJoZKL_qzzEqHJuyBLw9Z1oGUjYptJT1Yok38hfSetUYCycWGmYAiwg-gKjD_pyRPTf6-MGVORZc6t2n09_YY3jfsoFpCKJSq4Oo7p_pV-Zy7qrKGpkmGV885jhH_o6X8jW6aAHSrJALnni2LEDvSJnLKq_bDhzHlJdEaMd8LqYR5XXw64A0QFifhqBsdgPSnXRLumpv4Qz8x9ydehv0MUVt3qRxWjr-9t3gSeVT2kuuEuc2BcnOiEflQdUC2cos9sdSVJec4XnrljV8rGaG3PxXyTNMoQ49yVc8Rf8GhxJzNeIU7ePJsZgT-XxkNM4z93z46vp5pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=NO64Rh3Pn4DdSJoZKL_qzzEqHJuyBLw9Z1oGUjYptJT1Yok38hfSetUYCycWGmYAiwg-gKjD_pyRPTf6-MGVORZc6t2n09_YY3jfsoFpCKJSq4Oo7p_pV-Zy7qrKGpkmGV885jhH_o6X8jW6aAHSrJALnni2LEDvSJnLKq_bDhzHlJdEaMd8LqYR5XXw64A0QFifhqBsdgPSnXRLumpv4Qz8x9ydehv0MUVt3qRxWjr-9t3gSeVT2kuuEuc2BcnOiEflQdUC2cos9sdSVJec4XnrljV8rGaG3PxXyTNMoQ49yVc8Rf8GhxJzNeIU7ePJsZgT-XxkNM4z93z46vp5pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Zj9Zl6JVvsbKj8T9WXCZtvNpFHEPXYNswNKEHdC3l_eStRrXkAOT2KHDoJUL7gumP4WgOoQWM4c5gapTOLMXx7tUXfJhS_XygVOLTrVRTmPEKJc3KhlgIpkeffHu1rJuvphTeupYa_DzExlJiGYXzgEYtXE7kI2_hDjk6auvfRcqm4EIWIbO42WRcTxSCIwh6WGx1cb-xBkF3LOS14Rgi4sqrLX-BuCRRLgda1iTGQu_XG55oCgZGH7vKE8c6Dw87FLS4RzM-xMEgDsHG6X2S9VyPx9fBgWY4XBkjYAMy-z5lcpEPauDlfsRTn-O1xoonMZgDTT7BaZyippiyDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=bsLEW4fFZiWgjtqaPvJ1w5OniLO2XNpL2fdL5vAIHa6K8-zwYvKF4OYup8MDlsPBkBadrkdeevLEjlHYzj3Dac6l9oEzhT0r7QWzd2Cv8k_a0xARexlmF6oGgw-48wQCDytvgIt9tWIrGulkE0Yh8GVCuOhs5sUoN3bWiDTWXUF-6bDPfcQra3sYyur0KxFEzaNHrv0QwGvUM4_WvHQ7G6AGP58K_XnjvTLhfhD5H3WTE3NSOH4rC8ctAxrvSjVIxChIImMNg5bVAycA5g-GqpEB0089QdEL3McjIJBWB3v5zhFIS9ZdBBM8hvV7K9SWZLQBXamG-x499Zw9t0o9xYJdR8QW1YUQmnLDkDQ2J4sErpzIqk7MwBxMEGWkyw-t42Foi7DCHMqGpyLKuj-ZOv2DIEarEGM_V9vnQSSW-ikYDJwxRyx0AISHTsNGa58a60OKGG3IIXSeR62BVS7E2kuUh5xb9wIw4j36xDewt1k9_4Vip1u3ob2PbI7CBB9EpCGOKU-2jCHoX-cPFqPfx8JdIKSTfATD1X5d8KeYTVU1YHXEyHFZikMCaVMVeBRT4yP1BikfzZCaYC9IQQa2yQSOXw9VCZd2gx3596stmqVPHYL2Py0GrO1vGTdwSrg_jCg4OZ9LQdd5rTh6WJSAic6ZfiWU1UkcbdZZVOTjE-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=bsLEW4fFZiWgjtqaPvJ1w5OniLO2XNpL2fdL5vAIHa6K8-zwYvKF4OYup8MDlsPBkBadrkdeevLEjlHYzj3Dac6l9oEzhT0r7QWzd2Cv8k_a0xARexlmF6oGgw-48wQCDytvgIt9tWIrGulkE0Yh8GVCuOhs5sUoN3bWiDTWXUF-6bDPfcQra3sYyur0KxFEzaNHrv0QwGvUM4_WvHQ7G6AGP58K_XnjvTLhfhD5H3WTE3NSOH4rC8ctAxrvSjVIxChIImMNg5bVAycA5g-GqpEB0089QdEL3McjIJBWB3v5zhFIS9ZdBBM8hvV7K9SWZLQBXamG-x499Zw9t0o9xYJdR8QW1YUQmnLDkDQ2J4sErpzIqk7MwBxMEGWkyw-t42Foi7DCHMqGpyLKuj-ZOv2DIEarEGM_V9vnQSSW-ikYDJwxRyx0AISHTsNGa58a60OKGG3IIXSeR62BVS7E2kuUh5xb9wIw4j36xDewt1k9_4Vip1u3ob2PbI7CBB9EpCGOKU-2jCHoX-cPFqPfx8JdIKSTfATD1X5d8KeYTVU1YHXEyHFZikMCaVMVeBRT4yP1BikfzZCaYC9IQQa2yQSOXw9VCZd2gx3596stmqVPHYL2Py0GrO1vGTdwSrg_jCg4OZ9LQdd5rTh6WJSAic6ZfiWU1UkcbdZZVOTjE-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=nX-aBtj4com53rWVKAcKFIOvg8C4MN-UX9Rirc0oSvd3C_WUsYH71qObOTsEtv95b668Revr-4etzeJKEVHmI0Rr8zQTlNNpK0j1CORwz12C3gyYVHKj2V1msDbX3hlMKXpyhX3brBeNCSWSi3znEIBYkjrEffjNYNCzzpL_tdHuPKVywrF3-pwhOgLw7T5C8j1Ucw4JuzzM0jpj0Fn9ucLouqRQnFUVeKAEmoYbg3Agl9q02ROWpZcw1g7nVTMaioZLEpvSqpagdfXUq8YCWhkYBtEtKUwwVq6SlEGucHqBYMqrVYNc8r-Z5mNI0oYYosZvapeZQiE6Qfr7IMHvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=nX-aBtj4com53rWVKAcKFIOvg8C4MN-UX9Rirc0oSvd3C_WUsYH71qObOTsEtv95b668Revr-4etzeJKEVHmI0Rr8zQTlNNpK0j1CORwz12C3gyYVHKj2V1msDbX3hlMKXpyhX3brBeNCSWSi3znEIBYkjrEffjNYNCzzpL_tdHuPKVywrF3-pwhOgLw7T5C8j1Ucw4JuzzM0jpj0Fn9ucLouqRQnFUVeKAEmoYbg3Agl9q02ROWpZcw1g7nVTMaioZLEpvSqpagdfXUq8YCWhkYBtEtKUwwVq6SlEGucHqBYMqrVYNc8r-Z5mNI0oYYosZvapeZQiE6Qfr7IMHvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
