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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 23:32:14</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPPFZmdwXD_9Rpbv34-6erneVGM8b8YLTtrlpTt20L0O7edy49lA8GoPLexOgOZjCU7W4wuDb1mvOxGxd6Py2RvDpDbjHjsLcLOGJo6UgCjAp7-grYIUHf8FowMaZQjq64TK-adnyZBJfv_PAS0WGUPuUTX4N0hz7P8beE2Ie1AGXDEIBFWfWeIP9SJ4igLTm4VO7sTuawNkJceLI2dW1t46CRPF41cF2MWGJVMZM1t_491zO85M72JrRjd00tnvExeM-zItfeLDPjZPj_4eJUnvdhpHqqG046y55h3XkWBa6_qIDKsX4ZzabWVW8UHsFE26GYCXap4Plf7A0xrf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXjCeqSktn43iwfdrddbiRJphKF7jTGGeyQkjem_uqk9akgWCXiKHgcgf4CwtFr6to9NV0GjvphvqN8MRHypCVlrEuP79ty-NIBtlkMyjLwQfyssb1YAtXZIl9ztWDPo63wRsrQ619CsxrDkCjPQMTIXwtAIfkxBnOLDqqgMn0D42aEB9amZvWK4JUJWqrtw-thwT8rKv-AZv6HuWKUwFfx04JJQznMH5wM3ADrMC5MJzZ5Evk5SEqJXbxzUPRV9ippS071O5y9EbcdnBvtSRg9rLEExN3yAmZSMgbUDzF1MxVYUTDSiDdM4p1cS6MTQPPN1XFDnLQ1ftHHZ6QlfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaIO4g_xwkBfJZGkmzHdXoqdabUOjfCwU8eigLdrZ8bEQ_hg91kOCkKm-ry9VEJwAkVYlJ4lezXgV0ZBi-ZHXWQYlsF8L0DEZlm8yN_o1WdWO_xUO5hljnk0nEq3ArNdsRDqdUCEAfFQQfLNHbSDAPhN0XFJzRku_blXaaWv1KAITNtpvKr46zgHjjmweUE1Vvz1eD0rL8t31T67GNqnvaUdZRodMR-B1zUSqEBONClyRQq-XsP8ut5M98RI-xnH5RAqmlc6fhQyvRTITmGl-YRHjOSIvKTWJaW3EOBi5hLAXgTb7tGiCnxebBI2rF4UMer75Pj0VNTcxM2DwI25nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1a3Rai77DNmYqvNBg6-6Bv65-0dlLcqdDsyN0oERx5CQ8BMQuc931PblQUMgf0t3iW-2DCNIjiu54vT9nGAUclpkwu2Pt8dwipJnJBsQK9m8ADqwE5BmGQMbl8Cn-GiO0ZJqkZYUItC5Mr4RQptlSnYf6Gatfbncwi71kPoQbglT8OeYMQfeAB_epAh25V4tNTqAGnrprOgho5_ecE-Tgn9bkPYUbuPbioqopRH6p0YdShTbqoU0bjxaibXZW1KoMDOT31Z8QcRULMFKHZm6V8BNgVaYrKydei2h27nZjBL5tjISziZmc6h_hrnbMLjyMjCud9Twf4XkUu79fePsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHPID0oc0G2Eg7GAK2XJA6_jtXjIMFyuqXTV3EVvPdxPUgHv73x8jydULJVU3z2dwDaKDbYr4PbBD-bcO6cuFchw5FydsKwyrnJzQlJo7ppWOwnAz0kGead7_TGHurh6I9W0BXp4MHhdCXvlXNOC_f5uJaqc3AKUKfN9KW-8zK0GmWr_q5qCjv7cN0ugr_wX_bolnDogXmvZgjbfUddPBhgXoe6AuzMw6F8p2lDuE2MNwf0jnMrZf1wjhs9KFasos2NVlXZ2G0sUbZvm5KyhoRmb06U2Mg7ic0yrW0z2Rf5Y3wYgr8ozaH49NISF7jdV5iURRi8tvyLFObi_tEpqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=RSZuXjN5qg9ujd1Auv-qgMerDYMR25QKGHOGOH1qlb7Z0X3bnAF-NG36jGrA4XEvA0R-KvWPNAtS5uEZGPwP6mSgWtYI0k7zkT8nnhXjoYsRmDKkaX8WmX2IGKGhZIcGdb5u8uE8nEv4QG6XLQqVtaYIH-kuJC6-YeHD03EWmUZQ-bMGafrkQRhecMOR1mV6V3rBYjtxuQ1uygXjtPZKhIrjYbcBoRWp7eUl2U_pIOhdviYbCKTgIHhR-JNbSCqOfvMiL3kQ2VNyhKonSOisziv6RPgkyWf6hvzhjLKvOX75iR0u5w-OmP1zGUEaJTbkQdFydyc7EKa6bLdw3vMKMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=RSZuXjN5qg9ujd1Auv-qgMerDYMR25QKGHOGOH1qlb7Z0X3bnAF-NG36jGrA4XEvA0R-KvWPNAtS5uEZGPwP6mSgWtYI0k7zkT8nnhXjoYsRmDKkaX8WmX2IGKGhZIcGdb5u8uE8nEv4QG6XLQqVtaYIH-kuJC6-YeHD03EWmUZQ-bMGafrkQRhecMOR1mV6V3rBYjtxuQ1uygXjtPZKhIrjYbcBoRWp7eUl2U_pIOhdviYbCKTgIHhR-JNbSCqOfvMiL3kQ2VNyhKonSOisziv6RPgkyWf6hvzhjLKvOX75iR0u5w-OmP1zGUEaJTbkQdFydyc7EKa6bLdw3vMKMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTCqrBNjyH84cEtkMuwnsCTXgdxF8E_xZJ5Ij2Mj8uT0cS-9KkxNk6OVrGh_czWZuBLqiWptAIp_TZPiNIUGJjUvTTnq6uxUApXPLXVI08835rUmuuA3RU6s3jP_AKEE_udltS-o4MSqcGrmToo8BHqgXnfNeK9bHN6pUnJNQ2WRJfaqsOwTyFTV-YKxMyEggbi7-SXUglTwg8Ri-fk3KqtO6FEvEz_L9pfTqU8Id99OmdcLZzsZZ-2rxlsKW6mT_yea2dy_3oLe0yKXxsG-CZXeqbNSCin0YBdc3FfZDVNnsUEw5qw7H2T89Oon6tPY0ATsqUy4FaLi8Dy-Phn3qQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=DGh4sC97Kxf8v_rDtr_DzSeDa-H8rWNCmfr537Cq9-jOYCW8fCttbadVwT4c_8pU0KGWmekSlhq4wIdQUWv5k-LaFv-Nu7MHlwhyhucyCroWe5O0ekJp5Dxbc1S5QTbe_7C5wxl1JiEN_-K9SrKRzdFzK-N8senIMnvDBwdMKK02gPwPQ9JH12dFdVXrouDp9rQCFWGf5d7R6cWVT1K1drXbCpJxdOoLQICV0q_1oJlMW2et86tgsUwgYZdQUnBV4QKCIR5LvPmZdWvYiuADfFEOQq89bBpygA29xZjK_DKP2FPGaXONE04jIqSWoF9I1Vm0uCvjRcDuMBCL_Zx9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=DGh4sC97Kxf8v_rDtr_DzSeDa-H8rWNCmfr537Cq9-jOYCW8fCttbadVwT4c_8pU0KGWmekSlhq4wIdQUWv5k-LaFv-Nu7MHlwhyhucyCroWe5O0ekJp5Dxbc1S5QTbe_7C5wxl1JiEN_-K9SrKRzdFzK-N8senIMnvDBwdMKK02gPwPQ9JH12dFdVXrouDp9rQCFWGf5d7R6cWVT1K1drXbCpJxdOoLQICV0q_1oJlMW2et86tgsUwgYZdQUnBV4QKCIR5LvPmZdWvYiuADfFEOQq89bBpygA29xZjK_DKP2FPGaXONE04jIqSWoF9I1Vm0uCvjRcDuMBCL_Zx9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rja9g8Znhb_U-DVZQrLTG4V0-NNygos33tKz5jgcCxyEQiiQx3fvacIhAUnfQU4JWIX8rnDQTC7rlEyBE1JXXsvWoNaNKqgZ1qWOxyqkLEZvdgomC68JwLjCeEYMjkTpe9EszsdIwmFR6xScSt5NBpWptPuX74MgUPELmC2T92SHSH6KH62R0GMxzck1W97AXuNllMvV8GEiG6WOI1y2aqXOtDDFZZnCMaULX89Z7slC-9R7Fa8FWX5Z7-89skHj6_L-vB23oJe-umzmWEw3sAM-_4MOG6J6I7tSxuKPBHlktcLLfvoAFj_HXBGMc8kKgBYCLjRi6U-g37hxU8-BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa5RuV4ve_7OmTNvJK48XsPICD9fudqfTvRqxmEJKWPsMBgIcVtaHAs7Xo3sN9_Mcx4pYTpCfyNlXc8xmdZPZyDHRVZ3fMc1bjJEyGt2xOwnOB3hrVU6Ajn1sKtR7XNzUR18Iq50P5qvyASjDuspY60oDS7Irg40KfhtDq5tbf6WMwjz-5S_gIKq-kii3NoeNag1O-oWPjP33Wqcv2ZyBNFP_nxC0O1UCsunX7RfnOBMmNOmEM8zGL1wElAa0118qV2_39m7ApsSWbKsdEpvauATpiUJZ1pr4-7uqkqfxr-RcigTsnvAcFjKrCL3OrOamgk0SUKpcmMk9cmoETqVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=KgudLcsooC89e_M4-jJfRJTE-F7f26Xnca9d3k8ZApEB7DCbiLJTER7CDQr7lOXtuIswq6ZQhUIdmUcJokr_Rq_okz_WD-jDBStubEGOIdZ9lxTmt8N5-bxfBdvZClNUCnhI0-B07Cy5GOzdv_c7FkFnzJZGYw5m9uENGZfUNHJEbFBZFQdsuwNmcuVM5lz4_W9UAyF8OOc_j4aHoxLq2_ISaPqeFNwnhkvgSn0il21PFpbbl8VkI7vm89CoWMMxD_Thw-I2-gpFVON6oEZ2w4d_sJiEWDEUIx8qVPw6QgI7XUfJ7SlE4fSfdZ3--jSrSuM1lDlNLwR2d44nbemw3oFaG2eRccknzrUmxwDNPCKzXDx6tvpOnCkFAeJCTEM1ElLuPWg0957Hx7yIVytDmGVElyHgEbkIKtJ9uXcCo5g9Xd74neHpe1Rq19i6hMmPRXKR4Krs7AXBmO6uL8mHYa7xwwr9l9S4k1Qt7rbGu8s-T7GY8VcakvPk7Tm3P6k-JSUhFKZWD72b4_dxXNzrb8k_OrzpDUDWbyDWfKkzOwN2z03BYLTYg2Tg3XUt4LpQSZFdzMpen_HwG0Z2bNCfcBUMsIIMXSvKv4EoFq0jWgEk8ry2NT5JKZREZwoCnrb_LrlMuj8qVl-dnwHBSOf5Q0sWa2Rcz0NSvMQ5f6Zw3yE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=KgudLcsooC89e_M4-jJfRJTE-F7f26Xnca9d3k8ZApEB7DCbiLJTER7CDQr7lOXtuIswq6ZQhUIdmUcJokr_Rq_okz_WD-jDBStubEGOIdZ9lxTmt8N5-bxfBdvZClNUCnhI0-B07Cy5GOzdv_c7FkFnzJZGYw5m9uENGZfUNHJEbFBZFQdsuwNmcuVM5lz4_W9UAyF8OOc_j4aHoxLq2_ISaPqeFNwnhkvgSn0il21PFpbbl8VkI7vm89CoWMMxD_Thw-I2-gpFVON6oEZ2w4d_sJiEWDEUIx8qVPw6QgI7XUfJ7SlE4fSfdZ3--jSrSuM1lDlNLwR2d44nbemw3oFaG2eRccknzrUmxwDNPCKzXDx6tvpOnCkFAeJCTEM1ElLuPWg0957Hx7yIVytDmGVElyHgEbkIKtJ9uXcCo5g9Xd74neHpe1Rq19i6hMmPRXKR4Krs7AXBmO6uL8mHYa7xwwr9l9S4k1Qt7rbGu8s-T7GY8VcakvPk7Tm3P6k-JSUhFKZWD72b4_dxXNzrb8k_OrzpDUDWbyDWfKkzOwN2z03BYLTYg2Tg3XUt4LpQSZFdzMpen_HwG0Z2bNCfcBUMsIIMXSvKv4EoFq0jWgEk8ry2NT5JKZREZwoCnrb_LrlMuj8qVl-dnwHBSOf5Q0sWa2Rcz0NSvMQ5f6Zw3yE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbXcu_4dTeryEUOeeKXAD4JubKjw-q7_EFpZ5SBi7K7_QHhzMkV0K16wr0yhaCVOl4i2yqk0LNomKsGOx4q0kDdBZ3BFaZdOUUVtmepLDK4ywEjuRzvzVrgiKJCcs99tjzIiq1OAU-vpU6Vw86NjslWpZfakI_q1l33nRTUJc3NEUVTcvhgNEs8KzBjihu9-E4OF6GLPq0-s226rkbr9Zb7LAm1znlT4ETOrhZNQzkidYC9sOo5Y4zczQlavCIuKIQTNQtehS5sTaAGMKhXBi0nl04H434U7dM1Y-bRT3toYScUttSFnPOgIJolLBvxwcVfDjIZ5-2961isUiKjtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiTfZ_sz_L5lRSH8HcKVTC5O7lZOgZQNaiUgF0JfSuS5OtYzdwUd1q3j5a2Eur0Bk6a_Tq1jFvuZFZbI636SGHlKxxjYFWV8svzkr_Fyty8kRdqgI98i-8JVraspJh4QL_VkvaB1cd4NyOXct_odtrNc9G674ZnT5s673OmSz8kJQ2sXpRvUXeZs7phEU0NkJL9RsN5z4ySDFqQfN3xjYfc-LiL8hNEL9WUfyQMohWSIrW3lTH4okMo1D8YCGL2qrg-PcYQ8kKI0h_Ub_V02C1jBztsHGpVOM_MDzT2j92VCyfH38oifNaXl4_hZ90KrPq_PRbWHDk-mu_t-C6ycgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFq1QkcAmlkZBzpUspUrJmRVZ52obeiTD56gQLie4ifBAwYE1sX2yncGBK6ckCcI5Wy-yDO9-C9Ye2ah3w6e6ppGGfS37QAI8jBFQrdUOVpHnjeiay5zB6RKceu-5Z9d17ACnLgDMnb4PyPuItHRa9XsiY0IaId1n6mkpUo5HIq2CbEk-0x5xTwpq7z_9NpgDeDOv-aFhC42AFyvlUbgI2oci59JSo3y9bYip8upYeelVp9Fbz5gNBaPyuUeNvVCOdk3pgZyD0KdEjDLqMhOoKrv9Wt3ZafItYdWnJUGJ6TvB_TB4LjyrZTBEDZNvuadh1iK4_fbba7ArgQ3aMBkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=M8q-xftf9IN5M63O3_xY1eJEZmZpk--jbh10biz8bDeHhngFR67kVCGjHubEzxovpiav1kS0qDWCCedi20fyNpUxkrc5Za-m1IcLjYeusiEKd8iIUelVqjEEKOK8ZJRFePoq434MYhzvKITEtJB_WsVnOQJm70N5Yg9PJ8Dx4-ZdEMhNUfCCrRcwQlwCxRm98TqBlWjUIEtlAMu6FYdz8WdGWqZZBd0O5xT-ROWV3NjHh0vBlr5gnmgWYbzkC_8fjjNeuJGzgp3xLzV6arO4Tvr6_GZvFCtTdKPapCbqi8zqWzH7NBxyIi0VXMVAdaIPaoKmbVzMB4L6xe2RH9atfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=M8q-xftf9IN5M63O3_xY1eJEZmZpk--jbh10biz8bDeHhngFR67kVCGjHubEzxovpiav1kS0qDWCCedi20fyNpUxkrc5Za-m1IcLjYeusiEKd8iIUelVqjEEKOK8ZJRFePoq434MYhzvKITEtJB_WsVnOQJm70N5Yg9PJ8Dx4-ZdEMhNUfCCrRcwQlwCxRm98TqBlWjUIEtlAMu6FYdz8WdGWqZZBd0O5xT-ROWV3NjHh0vBlr5gnmgWYbzkC_8fjjNeuJGzgp3xLzV6arO4Tvr6_GZvFCtTdKPapCbqi8zqWzH7NBxyIi0VXMVAdaIPaoKmbVzMB4L6xe2RH9atfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFCvih2nynyxalnCB6-FNOmEPYjO25DwiLcUc_1vrJuztuGkPMZFSQMDOmmWGVWuqhxkY7UT8AVzuXtCQvaIp55gZbC-Al1QXCay6xaCuCEl-Bj-kqAF2GzrrcfXZuHj0j1KcAlx3GrF_u-Czvfhv_65goZbnBh8hFGAK8ynezbaymJz1iGJBaSVLokBpTwuztO8SeCbAq-K2XMjEMWGo1b4oVcUZf1hJ3wjD2hDP8nWAXIIiiZ6L_gW1cUjSOHN2mdLnjODIIsAKaumGSjGx5GM2-ZUoQfkJWn9JHFY5kEa7KxXWdEAkXuuC0Zy4iBLJAr61GeOS3D2l3po5WJBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vydyr1y3wFii4prQMKmn4Xcn9ja5HVNtZKeC9lAe3cuFJ7etc6zh70agvAx6Vyr4WygYr5lQ5U84jZY5PNLxkVOwahmQTXGbU0k-3MFwxUDEDvHagPtMixNA9eoZQKZJbKnu5SCKPigaRWU5XOtACc-ZLbuOWDTtPaUNPF3JHG1lzlNivSkStVmmmKNM196j7m9fvmWtJAanbT267vNpuAAZ0TJixiPTi8PGNNP-SwS2dze0kW4_eTQWtKgvl6RBU6ix9o-hrWMDcUMb4X3NMZbeXV9-zgms7N81H8uiuGs741vdvkJkiG9lAJ-viqTRNJRdkDFceiN3KgFLE-vPJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQRBhHV9w_s6QOuVb1sOAtbuNpd052NqSP7I8mZeEq7r-fc_fzYaADsWQ-Ngftr7GycOdJ3DPy2dUlQzw1vUFWDOG1r83rIREYrNJdyjSqyS_lWe8SqxF7mAkH26_l5cj4EGzPwfBUt7LxkT948XrTuQfPasOrCurBzyFTtKg7cmbXSKUg_M0EzXz3S6qInCh0Y-m1HhcqTXiIeYvHUO50pR1TeqSj6bBbmNuVGzU4OijT78SzCUNdtd-Tv7f2Nua1RtPnmDOC6U3eFabDV-U4xZGEsdap-M8bIqd67aC8QX_352uSZfqngKVxhZFwNEn8rycZI_NsiQI2kGGC3LxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTWci3YmkaHAB8aWZWVBSSCsKcYq2SmhDHMdcQz61iurawl-QJuxRKnjPeHNSpDlpYFzrV8efKCBb4JBv3dCIJlIUKdUi3a6XXzAO8OGF6Qyrkrt_OFjcH7u5QlmNN3xFDtXrAwRtqgp-VpJSBzf5s84fcT41roXEi8XxRwXFEIPy5h0nuYmximERNXjvFrXX9b6TUgnn6-caSZwWZudws7Q7-wzRBbuXW-Af-rjvaU4D7axly9cx1DhF7lFvEKw6FPbjfb3gqDfSD8Kx6uwSqBkv3CZRPJjBQzNME8lwrlGYPtng8KZ-clGzi2Ld8kCYijTSJ_xfBJ69peM7z5Eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2vckZTXXYVJjreeWLy21lqZxi_MVbEKal4jgqJ-xU6dIU1JVkh8D_S6w62Lr70EylhDJyT8kSi_vP1aT-ZBdnIBNCPTjiWmoYvMEv9QTN0tnxbW3andW1ek3ucLYeNh25j3mosZF9TB3YZ2KHth6HuBKF7Y6JEl_4FTEZ7ErKUL921n6v_ondSFgjqks0wrO9iu35s2S4ug7Ncy-CgWux1-mW9jq1EOEBZb7q8EBw-P5TqfYGGXCQUpqoULklGdNfHljgsTKk-z3wM-PCok72AWPcT6viHzrnJ-AseqHrnRASc6CfDsffOesI5TREZ1s4Cj0skj79Uo0-quBGsksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmBBfLI6okKL36p5PESq2MHTGEAQZufs8vw3CDIFWpFCo2n3_Etc4fxNbkgzP8LBuk5SaPsGsI0gi1IdkxXwpBbjdJpKd2khkJ5ehBWSXxwFNcG-E2JE3CO4_6gBMeo21UncWf1A2vr9YPexP3e3zOgKlK9dR3bYW1ZzPRFNWtcclE56sm19VCEPZ7MsUJAIhb3ZFb8wOA8eRNajziyt5u1qjTSF2QT3olQoqFVjvTdux2yqV0EVzYhXCZXwI2163H9pXgYL_fIoBJKroxNNuHfLN3f2kh6BAnioO8ZvCcIb5Zx-FACUQHU4xDbd81BB0huMlTTTJxZGxk-j-WIZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFD-4oMUO7FiBom32DnN983zJElyigtCCo4H_-X4TDTDRoAZcc_kkDu5-idLTmGF0658FZDBXBwqyt8niBUgEta4OlbTj1JmovG26i-RNt0ckTP1dsiuwitNRCdM6wNJrTMMq-lqxk0AK5fhqbjhiacJVmkNFeKszUBicZfluEqg_IlRH2FkxpSOV4CWtNnq96ymG-X2W1ywmg9M0Dg3T8YPXCRCMF_HGgGGu3AydfVynFTm8qurUQofIhyJh9cIkU-RRPT_vGuoNK46gakUEDb5yW_B0RAQLOLKAoB7TZSwgopAwws0kmRvIw1kBIAtOfTA_lAHIBosgLIAS5_DYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVXWFts9RTx_XECBr82vwwQpLIdGi4U3rip5sw4xfoTQbF2iCKkgms74NvfucdeTEMzieTuLqgPQIGHcVQA6NDj4LdfekfaMAiCsxXXRwuK1AoJCHyRK2a8xWQOWTk0lcwofzAm058wgjWcX1V2htzdLkVG5e2pCTg4bz7fWAAxRYI7SizzLu8Vd-HkkQbYMJcbdJlN1E1Vi0Fo2Sa7DG5t7qS8_HZ-11AGfMhxtUYa0J3W7c_qBsculrZjMjbi1qJjgjdVpRdA3iCDchEBd1OJdtWsVd_JzlBgrM-S43wvHZD-YrYvcNcIeMdDj6Nr-vXL0j1Ltqx6yu9l29RreEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kePe0G_EgiN5_N-Me3kiKkBuej0xFKYjbnLKr_-cDUI-8_CL5zD2HhPcEY93a1i4Kv7xJCgR4DON6MRURqdFFR-_Kzu4D40WL1zcQGE0KcS6_CFh7lZ5cABVdxPEPxtXTUDxXT9jnvpNFD2W1GuWJFZpyrYyWlJr-M34C5FrGyZBfkv9iU583-VDxsGChUwM20Fsr4cj_kg5ps9EzPkP6KNhCJFPZ-4fdA_Cv1gZBrn99hpGXapBBQf-B1_lEWclG1TVvyVGi4oyqqy6eDIf_hizfCd_lWaXy1j_B95i5sb0QJwszUxPhfWBq0rkEJFbqlnOX52J2CpDhcDpUFtG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JApLVms_qo8aMLfpMlC8or83IYBtkDVZHk-KZ-Pmw_i774Yb4RAGQrrVYTcMJg6WEe7OQcI1nwrnSPlkzx1xoYczhQN-1Zn5hP7tqIHaGMSBKDeZcQBS5Gy2tBMyCgGzB4kHmzSyI6p48ykgfeWpk3iBcjxpsPn4V3gimvgAGCAMC5oDrffalcxrrvr_BRhFkK-7xiuUoARlS4swmSJNxFAzSpagDCBKLp61SVRLz4EH6kUDz7_CLoMB3k1nXnHZ8Y-HBTFaMW9wA6k0_S-vyqsdpUBryex-MeAL2m_C5Gx5rFtEq7pB4qxppymdTC2WZ2s7hjZbpOByayjQiauA-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=NeNiEfGbJ1X2qi-GT6Ojg-d-fKR4NhIxOfHbElgLoy8F2HgxaXjE_WjzeIOW1ryMBdFbXbqpO9C8Js42q3Cq3b9q_XffNRddAX0o4PWojHUCXNCYLO0Brf5sHryZVranD2rQdDoN3Yy990ppsatFlix3yZfpR4EH85ORBrbxB6LhkBuEPhmE2QrniyQqBg3qb9xMlSIRwskcUVX7hxPuKwQUC858EK3yr05754ur2pase78XAkIIsHXRmEgJcp9zsNHEBaox9Fi4MKqharBNbWyQtqBwC5MuZCidmk0B9axV9T4G4lYR2eNG5VauOHtgvjJyUJEoti-syp_Gd2IsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=NeNiEfGbJ1X2qi-GT6Ojg-d-fKR4NhIxOfHbElgLoy8F2HgxaXjE_WjzeIOW1ryMBdFbXbqpO9C8Js42q3Cq3b9q_XffNRddAX0o4PWojHUCXNCYLO0Brf5sHryZVranD2rQdDoN3Yy990ppsatFlix3yZfpR4EH85ORBrbxB6LhkBuEPhmE2QrniyQqBg3qb9xMlSIRwskcUVX7hxPuKwQUC858EK3yr05754ur2pase78XAkIIsHXRmEgJcp9zsNHEBaox9Fi4MKqharBNbWyQtqBwC5MuZCidmk0B9axV9T4G4lYR2eNG5VauOHtgvjJyUJEoti-syp_Gd2IsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=i9zMVWwXX7-gjduNA0E9Q1a3kD6aSlQo1tjzbm_C4iUkDsNTY4-_aQ7HNl3JTsw9uQkT1itQAAQHddNoCPEksuiyanHr0hq86FkxnzcWifn1RuT2BvgCxb07WUvj4YLzgaFW7aSdcpdyd75a__wJxrKYETg1g2BEsohRCHJtN6wrMOaAiPR07uTe9P5yR7EKxq-5X0chnc0bP_0jYhD2Vpv0Njl_foen2N0HoIOTLm_CQinVJElPyVAsdW0uzlN-bi5FKYBEPtzouww7pSifo1gFQi75jKg3cNXU320H9mvpNgwGohgmTnHnHZqWjhzmnQf2g_MhCgVas-wkCplAoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=i9zMVWwXX7-gjduNA0E9Q1a3kD6aSlQo1tjzbm_C4iUkDsNTY4-_aQ7HNl3JTsw9uQkT1itQAAQHddNoCPEksuiyanHr0hq86FkxnzcWifn1RuT2BvgCxb07WUvj4YLzgaFW7aSdcpdyd75a__wJxrKYETg1g2BEsohRCHJtN6wrMOaAiPR07uTe9P5yR7EKxq-5X0chnc0bP_0jYhD2Vpv0Njl_foen2N0HoIOTLm_CQinVJElPyVAsdW0uzlN-bi5FKYBEPtzouww7pSifo1gFQi75jKg3cNXU320H9mvpNgwGohgmTnHnHZqWjhzmnQf2g_MhCgVas-wkCplAoYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCEDm7pHh4T--BdsumPu0piQ4Q4FpkQzHKDBLS1WpKBjDIV_RT0dSKgiq1vThfRITtjzvf4WNv5asbBQsY1AXT63xlqxnfeNu7jireRL2CW8UK7MP40ewi-0hreDBZp8AX-2N5MD-HDEkLr-dxwl3R9ABArnT1G7_MZZnSdrHRC835Vpn4JptduG45NqIFDESu2ERvqUnT3AhyfNVrajZoG1oC4CSSX_T0balaGJpHKzNs6e7fmbpKux6c3-7rhOA4nneyRRd1YnPF5TQjohHYbIjs2eauJ71Fj7Wb7CqGrZNpGR0IT5LT75I6TdY1tSQkziDBBjvmOFIbLxrqjXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHf6B1-jdOfkPGGvP38gfsRZIho0-A5Jcx_IGNTWU_Oh4_okHKr1MgTYiV2AV-t_oy43ZSikBfjwnBgkTTbxa8a9J9WIWK3YUWXAbaZ66L9RbMH9IcA8Be-HLrSsVblKV76GBFxZAZr204DHSap7cCWCnPVLoNQK0F3FoTtCSjufH9Z3TWBAc78aGUUKrliHPbIMBOWmBmFdLX81eSs8RGtIOvGitq88UHf5i9OJF2-GkmLppW_TVLz2e8clpxtQEji5I1OUAMjU8OCS6VfghhkCv2bC1ccieZLgTnCRLwL7o3tmgjdXkn9yRFZrQC7KVpgw5vSSd2Lywz9exwKPgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alTYOtcovb4b4PM0FiS35Esq3NfKTr1-KhhqItHCEH6TdNXIPl_r-ySRG8Xopxz_HLxW-ZMoDDNkJlI8MeJsgQBpWCYt2ZyzzkYN1O0u_s4vlnNcsB4fNf_h2OxNk9PjVmAKpta9oEbF-rBYv4RS3XegHWYulYmPoYj8lujsrKt-O8QxhZjSAuRm_7_gU4UMJo9wcT-SyRZvIvQOV6bVVA7522g7ntG-VnjP8oDutzgdEtVM0tQP8xvzL6JTY0Apta_3VY7Yi2sbhWtGGiYXA4uiHx1vYHbjWfiX55GKEkQXiu_4qCNPXkR2_uTSAGS1nV5AbiZ--YMCWPeZTdnSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlkEBSq9WB4e4NSxTvGCIFSBWI9lbZfncWBOEclpdKAPvUu7roQ64oZD54XGRG-1asTyYf37_O8MwI5kzlNIFGlQM7K7oauuiWhsLjGWotigoRwjEkYjNqkBF4KTGyGyfhuCSv5me4FSpY3_oeWs4Y2hILFlgHNPB6qCzzcYWOvXX-GsERSH7z1zAhuuRi8-gASfXBDTBumkjxzSZaFtv2bjCJRt0fOWfiO0XB_VanlGHva_5GzRm2iI_s_8BQjZM7xgObtYrA5iyN-d4L6-OaRAEjTQKwYEr8F_B4cmf7mTV9SFDb0TLRagOWzK5MJC9T65WgH_oBhgYb9RFam5W4tU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlkEBSq9WB4e4NSxTvGCIFSBWI9lbZfncWBOEclpdKAPvUu7roQ64oZD54XGRG-1asTyYf37_O8MwI5kzlNIFGlQM7K7oauuiWhsLjGWotigoRwjEkYjNqkBF4KTGyGyfhuCSv5me4FSpY3_oeWs4Y2hILFlgHNPB6qCzzcYWOvXX-GsERSH7z1zAhuuRi8-gASfXBDTBumkjxzSZaFtv2bjCJRt0fOWfiO0XB_VanlGHva_5GzRm2iI_s_8BQjZM7xgObtYrA5iyN-d4L6-OaRAEjTQKwYEr8F_B4cmf7mTV9SFDb0TLRagOWzK5MJC9T65WgH_oBhgYb9RFam5W4tU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OQBV0a-xroZQZC4M0EVtCq6bsbKW-BelqFYnDswwQA9vkx8wBPud9ekNKet772N_rdSCqWbfZd-L6Po58ujugBd6QQbJSFfCeHup-tna3hJWp11YCJiPIK7FfENMCDA1yDc5orwvSOXs2rQCtg4NLfX2DYjjFrq2KvJ9Kp_Bxew2Ck51tpED4Y4IEsy374GLl3cwgBrHfBixAYXhTW3i4MY7MhgtIGoUY3v2lg8shRiE48szZUTrlXO1RPi_oYfa58iNzxZTnvTjQVq78Yui9ZsWY1DUKVh6K_ls-Vneyz1L4vTIcP-6grIZ8xofiZiiZYDnihRemxIG4M3nvEMJDTeu6xE5ffMS4d94I9VxSMddxWwA542iZ_ePd6R_PgaEs1jKfD-thJdxRnRCUbxeLO77W705BvYZ2A2sfRn25XHIA7UIdYBACBTHXQ6Q7VnTe-En1scdAwoDmAoikUvnzgHWVmP5C-_jl_qHynKI6ybabbGNpNlT_aIOPqgu5T12kELqpekAB4yox9hKcOKG525lGTgywQbEYtHZKzqz_37UePStIu0mksboYTgmXb2G4uLcXG3eWrdkSdmIQPg_-Ia-Ace0ZHf4DmjEPBXgYDylPjtdAaKG09z_mUPkAxjBieOcGqUloVVu99f3mNeDMkG_vlKCdv_tKOWAsQHZZd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=OQBV0a-xroZQZC4M0EVtCq6bsbKW-BelqFYnDswwQA9vkx8wBPud9ekNKet772N_rdSCqWbfZd-L6Po58ujugBd6QQbJSFfCeHup-tna3hJWp11YCJiPIK7FfENMCDA1yDc5orwvSOXs2rQCtg4NLfX2DYjjFrq2KvJ9Kp_Bxew2Ck51tpED4Y4IEsy374GLl3cwgBrHfBixAYXhTW3i4MY7MhgtIGoUY3v2lg8shRiE48szZUTrlXO1RPi_oYfa58iNzxZTnvTjQVq78Yui9ZsWY1DUKVh6K_ls-Vneyz1L4vTIcP-6grIZ8xofiZiiZYDnihRemxIG4M3nvEMJDTeu6xE5ffMS4d94I9VxSMddxWwA542iZ_ePd6R_PgaEs1jKfD-thJdxRnRCUbxeLO77W705BvYZ2A2sfRn25XHIA7UIdYBACBTHXQ6Q7VnTe-En1scdAwoDmAoikUvnzgHWVmP5C-_jl_qHynKI6ybabbGNpNlT_aIOPqgu5T12kELqpekAB4yox9hKcOKG525lGTgywQbEYtHZKzqz_37UePStIu0mksboYTgmXb2G4uLcXG3eWrdkSdmIQPg_-Ia-Ace0ZHf4DmjEPBXgYDylPjtdAaKG09z_mUPkAxjBieOcGqUloVVu99f3mNeDMkG_vlKCdv_tKOWAsQHZZd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEak_peSknRVnF0mKkZREej_VMJx0JEguYYHNrrieyrX_O4Nw-D2TM_gasLFVGP9KwcN2Z2J526kEw5eqJ-97d5RJPIndHq9P-DnYq_cbVXabzPL9_lDpgsCpgolKniP0_g-av7fcOSeMlxIPwfo3ZQcBfe1dFNGXLPNUbSETY6giv0wJqo2H_xYbtuxBN42Ob-7-GtJR2zy7sQzI7NmzDZ25wAx9KcAD7bM4gu0AHbOOn4IFrrQtnp30QD4FiZrToXJBix7FC6nDrK4wpxugYvd7cV7rBRmlYnhuloVXvzgYncZESlRoy4b-PDOPH9wGi0VbEMn2YDljudNKXkXrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrqQ2pT6KJP7wrMQXZ3xPRJM8di1GeovD6qyyORIW27WYR0z55HIncYCY_kMYAq1dcYQiRTTZcKfCL4Ec9oehBJLVu8TB_5RYz3r06lQqA9k0Gx_9azYlgZYv3MZXoAe0nVHPaM9iGrMSI3uLuiCle88Ui3vVVOn_oa8_LvNJl7Ua-BRAFvf2Do8N81mdVm_W519x3-6Qw9zISJAOhiRj043TjNUGBs2YrkkyMt0HhyvMame0Aq8Cn44sGf174MhSHqlqdVylO6ltmsrIzTFTm_HyR2TDsOEJnbdGEV0aKB-RdYs8YmV_OP6Gu3yyKMsvOe2wmLdTtWz9njoMBE62Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upZrRnuvSogPKqW5UY_vb_AXSE66Kg3rouGHJUs1fsJB2vX_1tW-87tw53xyNi81sYgMFD38alIdOGw7TNXCap9wsCcoxMB7DSAid-8FFb9nErkmro5sFAq8i_q5l_jjLiyy56Pkno2meZxaQGSVDSayQaDOUwiAGLMY3tgMCm3w8pZCDJ0IRbhW3hIFrIMGTI6Zp2Wb4hVYPV6T6ayt4a8aDQLKNU2pyxmek1m5TbNViwIu4wabVZkhaJZKVaxt3UwwSCjaHf0S8my1J3WfdDsg_JIrNI6DH03jRT7I7Q1F046d21d0KOniHAS5wgJhl0KNvb1ylI66dVulMSZhVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=O2cQGxXsgI_RBJUWoQiY2VuU9oXnB2b4nVAxbMqToYoCSc3YSAhBWS_fvgB7qi93fIRJWZjjvaXLsIAa8_B0A7VkyqKSXrT1_r_0dQ4RLZekrX1oItwy2g20-ZFDpzjbkyMIUJupTSNUZeL0-xUomPZ77BroPL1st1Fv8qvVoPIu7Fj8fo0OqmEzv1qZDUZKEHh0SjqS65bLqvjAovzAdTphTpGzUhyqmB5cihaVd09W_4YB7uWnCm69yF4RcGY9ppW5KA7TnRf-NPp4lbstQMU15Xu2a2j8XshgCPYOxbt410AjhiJqWfaSO7xRuIZ2sViWYxLooS4Q-Go2GkxAiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=O2cQGxXsgI_RBJUWoQiY2VuU9oXnB2b4nVAxbMqToYoCSc3YSAhBWS_fvgB7qi93fIRJWZjjvaXLsIAa8_B0A7VkyqKSXrT1_r_0dQ4RLZekrX1oItwy2g20-ZFDpzjbkyMIUJupTSNUZeL0-xUomPZ77BroPL1st1Fv8qvVoPIu7Fj8fo0OqmEzv1qZDUZKEHh0SjqS65bLqvjAovzAdTphTpGzUhyqmB5cihaVd09W_4YB7uWnCm69yF4RcGY9ppW5KA7TnRf-NPp4lbstQMU15Xu2a2j8XshgCPYOxbt410AjhiJqWfaSO7xRuIZ2sViWYxLooS4Q-Go2GkxAiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIaB_zi58uziSFF39xJ3GhGcOB3GkTN1sDAbXnHwOjarLOtan5H2DcZ4HqwfaQkVIB-RULOflBTKDLi0r-8LL_jUyOGkY8Koy_QEN-fSE2PITNfXNuwpA-ly0XDWDgRX54CyptRso-WmloMnPHoIKNXUlHhEzSA7C6Wp3jumEF5nqPiShCP8i6kx1hxY7gcrt6icZldtucBdO72Ta4_IkljcEdoJnfx1SR2QqKB45N9auJjhf4YVSvhptdx8Y2sQO9U5JDNdHv8trBaZnC0hpPjvDOsMd7iDvY_KbJc67vR2dKvZOBdiOIG483JMnFxNNmZM7zKVMrflJh5DZPUBmQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=XjPJLV-wVV7LPHMESt9acwvPbPdZdYwK-aQyd8Fg8mAWx4PX-u3YfALJAki_2u8AI-FTgJmT-J35_ec0b2pywVAFyjlVmUudBRpP4stYa68jhak1l7XY6TlNRkyaraxsQEgllapqNG9JYgvOsl2Hg0kyTB0dHzmraR2nQW5iby1Ai-UBfSvnqNQHyBVSVNuDnor_j6wcw2stEfKh2B-lvMBmtQCSZIwbFRgT8pSC-la_OhgAIYTRQC__xZsFIpp_1O78dYdTDcuzLbK2hCedyKo_Er38igk_dFIsOY4_VfDhkj1LN0pEtudIoPUHXm8UaAl4SWCNHZ7VdETD9lB7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=XjPJLV-wVV7LPHMESt9acwvPbPdZdYwK-aQyd8Fg8mAWx4PX-u3YfALJAki_2u8AI-FTgJmT-J35_ec0b2pywVAFyjlVmUudBRpP4stYa68jhak1l7XY6TlNRkyaraxsQEgllapqNG9JYgvOsl2Hg0kyTB0dHzmraR2nQW5iby1Ai-UBfSvnqNQHyBVSVNuDnor_j6wcw2stEfKh2B-lvMBmtQCSZIwbFRgT8pSC-la_OhgAIYTRQC__xZsFIpp_1O78dYdTDcuzLbK2hCedyKo_Er38igk_dFIsOY4_VfDhkj1LN0pEtudIoPUHXm8UaAl4SWCNHZ7VdETD9lB7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsAeHfDDCDuzmCZQySL-A-D_WR_fpral8miGZuBrVB3DguA5DsqDvCljAbyEgoCqo6WI1-KXimA2_sl9hSFBmXOtn7UgUhaDTxJ8_oC0ASOOSj38u0cWW1ak93NInzfjnRANwGyMnWQmSC6ghKWQhMLGRgtUPV9e_pMPwPVsIEzSCw8eX6a1-EDumo76yf0XYhnXQBdeBEJ_Q4iybrM8NA4OEvDShEsuv2oHvAgjI97ACwkB75FD1eGEidCoTUQfl5bJuOZwb7BhWJaQdDUn4f4NM9ev4b3LBKdPxWIPz_-arKvvLgAvaTh5DMQPXcPbLrRqUmQNSLWuXsz5Gqen-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5FGR0p7RIodld7rdbmODml1ksEAuUd5j_n9rTkCRxIkXscTLJ3ZHXyeC3I7tfL7V1XNzfhIpTpHFzgY2S-XC2vU-RAE2H0_fy6JkgCg_xJtkbfcJI6Rj6glEMwAe4ROl4siGsMgpCO6Pfl0DOBQ5ITxc_EPCoPB2ZYfyosNJvssBcsDZgExPSttLoI0Awpiu9feHyQSv_gCqaHcLYHwyvI4yWz1NvJZWCS0k4zYNdYmeTEzkbHTovjuiWNEeG_ZTwEYhx8nsaMoP-nhlnNW6nuvS575gGK_tLwMzlM02BeFo--5DN8vq3V7boH0slyQvD1uQix6oCTvsIIPVF5CJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=qn2V_5rPIE9LUtvqRL3xODY--chnfZp9cfJJkdd3kphMmceWLRmOppnVY1ULWhzSeQnOD5JaO9H5o8iEp1PhWZ36Ui5bVbcsL1rxAkJVLrJFXqQeSCLLkPsHHR016UhiLVn5jV6vevcXolZPq7UU6lxeefIwoR5m3g70Ik8A2p1ZjbVMSL1-nlVx4K_PIQ5Nr8xQW8boOxvrMzjdylu_ocFC5HSPWRSLrcXmbedLz8xGbpkr_wf0jtKAABRSjDsAi1tZ0QsVviy_4GbfOeRDflWMjBAUg3_gj7vMRKgxMOCGDoJUvOa1UnVoCXeiEDW9MIeUPy0UfMlwfAcVSuHENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=qn2V_5rPIE9LUtvqRL3xODY--chnfZp9cfJJkdd3kphMmceWLRmOppnVY1ULWhzSeQnOD5JaO9H5o8iEp1PhWZ36Ui5bVbcsL1rxAkJVLrJFXqQeSCLLkPsHHR016UhiLVn5jV6vevcXolZPq7UU6lxeefIwoR5m3g70Ik8A2p1ZjbVMSL1-nlVx4K_PIQ5Nr8xQW8boOxvrMzjdylu_ocFC5HSPWRSLrcXmbedLz8xGbpkr_wf0jtKAABRSjDsAi1tZ0QsVviy_4GbfOeRDflWMjBAUg3_gj7vMRKgxMOCGDoJUvOa1UnVoCXeiEDW9MIeUPy0UfMlwfAcVSuHENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ilLMpU8BqSWAT9Kky25Nz4q7SnYHKS8y6PIvUcm-ZvU_YMXNaoajucBrfTj8anMHJtSaxPrR2hWEdg3MFAxNpk95RoiwMOy7rhuR-bvddg8ciHEu_xm8O0y-Qe1y31NsJdcbABxEk2uy2xBVavgwbUhwlZxM9MDRTMbOGXx8pS6aUKMrx-jlJRbGKaIoZAauDlfHx45Lz4dDkp78qBKCfSwRcvwKqKL_uzSs8m6YksJNBVEKJD1FEWY08E7DGG2q65yHqLMennVyD2QLy_FnMSrihFJghwgVT4TVuHa1NQtpKOuVV6X9WBZ3QumdR8gK84w7K6EcTQQMNt7rIdKfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ilLMpU8BqSWAT9Kky25Nz4q7SnYHKS8y6PIvUcm-ZvU_YMXNaoajucBrfTj8anMHJtSaxPrR2hWEdg3MFAxNpk95RoiwMOy7rhuR-bvddg8ciHEu_xm8O0y-Qe1y31NsJdcbABxEk2uy2xBVavgwbUhwlZxM9MDRTMbOGXx8pS6aUKMrx-jlJRbGKaIoZAauDlfHx45Lz4dDkp78qBKCfSwRcvwKqKL_uzSs8m6YksJNBVEKJD1FEWY08E7DGG2q65yHqLMennVyD2QLy_FnMSrihFJghwgVT4TVuHa1NQtpKOuVV6X9WBZ3QumdR8gK84w7K6EcTQQMNt7rIdKfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=FKVMSHQSPNMNLE3Sfr_vRqc5wnsYh6xWpWAtKUVfQEADSzG9K0YLUTksene4XiFKsDtPIUVufirDtQUumxhvp0uohhlOenhIgvCohHXWnKeTmOqybazjmIhWR7kvH2mKNO5TgAzxJS5lZSc6lQIVTloT7Au1FYH1UBITNFD73AWdgUXwFvwrR_2-RBehdC_PNs1lvdetYZmduZAhPrKOTYhGFkckgGVDFUanQtw7DibKiHtgDmQs61TLKEfSL7x_3N2o5zFx2ZDavDELJKaHxJODvkILj4jgqUUCieB6UMNOlUV9xmvYyRpCaoA_dbUIAyj_EPqFTgutYkf4T3SwPTyu_gheGwlEwamnUKrT_NbRy49gRrLIrXFY9xxlinRNyW7OnsdoM04gX8AP4fPi437HHKGFb7OV3w34vMyJeklgxdVYBUMMu3IZY2BiVGaZ3rl2T_R5c2WIDw_pGhQ1ZFomIVRErfz_X5GfuKqc4vnXL3-l5vvRAf9AUwzR9S6W6Yh553ZchWS0w4Jp-fUwmrLbkm6aP3ldnS2UGsPzARuTl2sEvdmr8YqM2I3qbxaGh1RUt0P6pvn_L6NjnzDbyQADHjzq2I75IvfRlA3zVMg-rsPLXufldX0paOsu2rxYFPsg1-vcEDdTchtWNA3M489fCGhMAPMajJkvjua0zok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=FKVMSHQSPNMNLE3Sfr_vRqc5wnsYh6xWpWAtKUVfQEADSzG9K0YLUTksene4XiFKsDtPIUVufirDtQUumxhvp0uohhlOenhIgvCohHXWnKeTmOqybazjmIhWR7kvH2mKNO5TgAzxJS5lZSc6lQIVTloT7Au1FYH1UBITNFD73AWdgUXwFvwrR_2-RBehdC_PNs1lvdetYZmduZAhPrKOTYhGFkckgGVDFUanQtw7DibKiHtgDmQs61TLKEfSL7x_3N2o5zFx2ZDavDELJKaHxJODvkILj4jgqUUCieB6UMNOlUV9xmvYyRpCaoA_dbUIAyj_EPqFTgutYkf4T3SwPTyu_gheGwlEwamnUKrT_NbRy49gRrLIrXFY9xxlinRNyW7OnsdoM04gX8AP4fPi437HHKGFb7OV3w34vMyJeklgxdVYBUMMu3IZY2BiVGaZ3rl2T_R5c2WIDw_pGhQ1ZFomIVRErfz_X5GfuKqc4vnXL3-l5vvRAf9AUwzR9S6W6Yh553ZchWS0w4Jp-fUwmrLbkm6aP3ldnS2UGsPzARuTl2sEvdmr8YqM2I3qbxaGh1RUt0P6pvn_L6NjnzDbyQADHjzq2I75IvfRlA3zVMg-rsPLXufldX0paOsu2rxYFPsg1-vcEDdTchtWNA3M489fCGhMAPMajJkvjua0zok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYAEVy82qBJ7S3_WgW5JIkvptYhJGR8h9p6aUpVBEU5V4RYJJOpFplYbuUszTda46dT7MoiA8taeR4BjpaIH5pHBCwOlObTNjwEkTPHLwOn-2xqflXXVIgy6IV5y_MWjjKS5ISkz0X4LCHzongyVuNTNFyLpclB1SZdDcSkpK5L6BumeEUdwoUe1mMCqTsAObZvZYo8hAEsOvz7YcUqb_4m-Nj9tqOrZ14nq0XigKfnlw5jt0AeSlW_bnk1mA08rVjHs4mTOmrjwf2Jnf46lAUcn_WTI7_Ah9-7ztQdtAqM8W69Vn_CLW6SSjfucCzHLEOmTNPJLBTvuGGdeyGyyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTu9wpC7zVWUhbAohkp15nw2k3tOdlI7NRzcxUALM8yobghyn0qplbVz86WzgvjagX7wSaaSAA20TzhE3KAe013N1mYeQS68BWYZ2zb9SgL0JB6as8mwn9jcroljDfkvs6uwtsLURWVjXQv8qyQ-Ez5GUSeMwy-rAJj2bPSYlLbv8GfxR3c2XXu8JIVmUb1OqDiVUmsDarqMhv6CRvYq8mR1v5WUiDgizylUuHadRPZfKpgT5v_lDw6SYcv8QeQKGRjw9TYglkrNNqJP3Us4bTztDnUVBeOoOd149L2V-6VuYKMiMwo6KMOKxGfmyDOooX0pkLlitceZktyiNWvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcS7zKIi9RDw_A0RghtXSD95_CK30pi-dLp0TJKuZb6zlFx6Z2WVTj3_rN5Ciu9XHjYZSiLhR8Wr286Tl_hfcvHNjfR7eQySmqVmhhkktYSJLgq-YYWaOn2TSNXXwFYcQZEkyFlU1lu2QK3xukJvYPTb6GEeH6ei_2u-4xQXPJnGzvU3zxZJZC6cCddGP9VQ96D3pAWjdoJ2XJAwfdVc8UrOb5sBxq9H0CKxV5G_71DF686Q9GMHmbhnWRSwtoKcmcBQ050KR9IimLGThFDQlSk6SK8KNUryFN-dh0x6CGd49sRfOIjDcG8w6ykubgIpB1znO-3jOSlHr0mW_BQ6vw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=ihPN0m8PzZJs-o5tf1Xk_mQSUoNYgAz1jHJ0M3mrX0JA26AIdwKRd5MhsZqnLyKtJDCm-HvlVz3AJEe__e-TUuXtjJ6NjW2W4SE-xL8TY29kN-hBRlrkTVNlSFwvLTrtNCgGrHcI4ulzgZ9x_taj3HMFg-etnfWQYX-ZetcJwRiWzY_eoRoasSam_jMXp6UPYKGYZwva5Eskm-Irvb0zm-8QujVpkJgrGglV0ZuIi1zbF6zq0y-ntpz840TOvCEbYdTu1ERNECaRylh3g9v6YQHxLOXqwTWubw1ZMLUtdYa0KxoPU30NZ4YeQ_mUckGiqbuAQtEL4cZ2Q2m-ZqR-6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=ihPN0m8PzZJs-o5tf1Xk_mQSUoNYgAz1jHJ0M3mrX0JA26AIdwKRd5MhsZqnLyKtJDCm-HvlVz3AJEe__e-TUuXtjJ6NjW2W4SE-xL8TY29kN-hBRlrkTVNlSFwvLTrtNCgGrHcI4ulzgZ9x_taj3HMFg-etnfWQYX-ZetcJwRiWzY_eoRoasSam_jMXp6UPYKGYZwva5Eskm-Irvb0zm-8QujVpkJgrGglV0ZuIi1zbF6zq0y-ntpz840TOvCEbYdTu1ERNECaRylh3g9v6YQHxLOXqwTWubw1ZMLUtdYa0KxoPU30NZ4YeQ_mUckGiqbuAQtEL4cZ2Q2m-ZqR-6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=tS2Xak8370CpWkNGBPrLOw7xvhnRPxRxuzrI-Y8NqP-GjLO9JeiaIPriNFg6I4lgs6Wi56FctzrrEdPkM5Q_9UBHhywEksIZQ-qL7v45Qc8b4QD1i_WspBeb0FVt4xEqknLllIVELI8m6EoublA8-QB77wKpqm2hwAmIwbuMslSGkURL9BM40BU-k20AJbwXE4MVudYl1pw7b3G21U4U7oLcqbAF6tk2olO7lCMwBIyIR9jKTJ3sydJOYJiXBU1SnWAYlCzBOYsRFudpNg9DPvoE7AuqG5EIAfWMJQb5zGToJ0QGjsdB2Zt_AYANI71zwaSjI_9UfUsVSxBchyvraw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=tS2Xak8370CpWkNGBPrLOw7xvhnRPxRxuzrI-Y8NqP-GjLO9JeiaIPriNFg6I4lgs6Wi56FctzrrEdPkM5Q_9UBHhywEksIZQ-qL7v45Qc8b4QD1i_WspBeb0FVt4xEqknLllIVELI8m6EoublA8-QB77wKpqm2hwAmIwbuMslSGkURL9BM40BU-k20AJbwXE4MVudYl1pw7b3G21U4U7oLcqbAF6tk2olO7lCMwBIyIR9jKTJ3sydJOYJiXBU1SnWAYlCzBOYsRFudpNg9DPvoE7AuqG5EIAfWMJQb5zGToJ0QGjsdB2Zt_AYANI71zwaSjI_9UfUsVSxBchyvraw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VYxH9i6w6aFmlqdw5id_hSV9q5OwfxTW8x9RMKHGOy9RYfWzlQ8nExDUuJwi4J_wN4YPF8GHQz_jmV1Z1wzcGg3wV2jDjcLB5oBRFC5Tc0ehGB8Jm51MXQZ4IuRXV6S_u1QlNw_tj2cxRyTTFoxV9pV7ytJrubApyq0wb5PUm5B2s53LXTF3DFgKRBElvGMfr1IYyzJH4RgLoaC2_Ecc8ObFc-QQ2dD7PWe_-nj4edvqsA5nEiO_m3Gw-ujwq2alMs0akb9H-O-5BKpQexX_Bnf0OIPxGq5P8Faw_rih3aPNA5j_SynEkNnQBbDfKA1cjHxA6V4juWFH-zO2rvt1Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VYxH9i6w6aFmlqdw5id_hSV9q5OwfxTW8x9RMKHGOy9RYfWzlQ8nExDUuJwi4J_wN4YPF8GHQz_jmV1Z1wzcGg3wV2jDjcLB5oBRFC5Tc0ehGB8Jm51MXQZ4IuRXV6S_u1QlNw_tj2cxRyTTFoxV9pV7ytJrubApyq0wb5PUm5B2s53LXTF3DFgKRBElvGMfr1IYyzJH4RgLoaC2_Ecc8ObFc-QQ2dD7PWe_-nj4edvqsA5nEiO_m3Gw-ujwq2alMs0akb9H-O-5BKpQexX_Bnf0OIPxGq5P8Faw_rih3aPNA5j_SynEkNnQBbDfKA1cjHxA6V4juWFH-zO2rvt1Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=IlLFyGJ4TIFGO8qUj8hAWp9oaAKdJBqbzju90VWesdUo2uf22ptzPPKgpbd1-8mLcU90GvC0QZMxZu6SK7RHfzusM6ZiMNBZLZyicRPTmLEvDsSkVWXnyrECSY1D1Mx8DI1vTGp_qP6oNV2jzPRI7lV0x_3ZWp9G2DZSwgShkMRa1dbbBE1Az9A_yLohrUuSU3g48aqofkPfvRhbh2-rTSa8cAixTZ2IjRUrsZwDkSkq5qlZCspmJRBN-ckut_sVXRVozOKygI8mNlpwLx30rYs7tXG5N7ncBfEjjc-XnzokPCOMZdG68ojJ_etKTLyVMuU7vBHaj6BqBOuTb-yAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=IlLFyGJ4TIFGO8qUj8hAWp9oaAKdJBqbzju90VWesdUo2uf22ptzPPKgpbd1-8mLcU90GvC0QZMxZu6SK7RHfzusM6ZiMNBZLZyicRPTmLEvDsSkVWXnyrECSY1D1Mx8DI1vTGp_qP6oNV2jzPRI7lV0x_3ZWp9G2DZSwgShkMRa1dbbBE1Az9A_yLohrUuSU3g48aqofkPfvRhbh2-rTSa8cAixTZ2IjRUrsZwDkSkq5qlZCspmJRBN-ckut_sVXRVozOKygI8mNlpwLx30rYs7tXG5N7ncBfEjjc-XnzokPCOMZdG68ojJ_etKTLyVMuU7vBHaj6BqBOuTb-yAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtFtomZm2tWF6_lJm4ZVqN30JGauzdQRYxWWi-ar9xReU7uA0dpygJJRywfDjh2I-2C-fMO5OOOsaZaSMQ8gp2DHEx5Bh9q6Fs88wJMxHwlJlkEfWpiV_zPqP-Mt8ZSCMVxiIJGhDPOyKXO6rULNUfbFSssEiymPRVEkgEZfcmNDRoi5w5TIMBEtlmOi50eS2FFPZXQ7dm1sBRQIz_IudfgFTlE66GkTAuxF1UYqC8uZKIeBgmsWSdlQOSGDp4l5hlWOxLpdZRiBrIt3i-QUCHtecdGhADRiK6gKRExmMgHRAv8WRGvHFceZ8NQ8U5MpD1aGhhQQUZYdz68vPoOU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=pE4GA13LY-sxf9jHnNuEva-ArBOfeVYjhucGgSRUuaO1oGVNmt1waihkQNffKQGNe-XMzgJBE5YFcLrOJTqmAnk-LISWtrjw9nQGjMpLVxuqQ9HbugXj9TrVGov23OcsHyxwSYkPPAf0eWjdqKVL8kLusSf6wT6BTUnAwfD8lmccA5PEI4O2OHXPlhEqLCJZZ-jMh3A5tszhVshxQsXuOqIZhnNG0JQCrCcEAhj0AaDenuSFkVvp-p-Qo3liZ2Wuf_DgyWlTK5EbiMg5X5rodo-BuoPzAUISeAjRk_MF3eBE3VymN9wxJb-0-LE7c3b4Z8vgUfbp2YvS_HiWH-CCAgqqsjgXq7Q0XK9smXHh3CgQQdL7qWXFznjsYAJoyXwYY0_tFecHLM-KvpVcDhJgVRrx203endXu0byrVsjqXmQw8W4_bINBEkGxASQAcnTRN2ofIa9_mJpmju7oJrjZRpVx2T7ri3MTPb14UdGvDZXPuvV1izREqkGKqegcKEJAmrd_rFL8bAgx_dKrP60oV-uueygyomI0NSWUzpBnaHuGeFvaYgiZ7U1E0Iee2r7gM-JlXzZvQXd57g6Vsx-2zhT_iep1ywMbR-KXzsTGWrXCZlxpe_hpOJlMoTZlGT1JKsK5f5O8K5Ug0ZkrfN19cmWji6A1-_eMg5d-HY1ZFUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=pE4GA13LY-sxf9jHnNuEva-ArBOfeVYjhucGgSRUuaO1oGVNmt1waihkQNffKQGNe-XMzgJBE5YFcLrOJTqmAnk-LISWtrjw9nQGjMpLVxuqQ9HbugXj9TrVGov23OcsHyxwSYkPPAf0eWjdqKVL8kLusSf6wT6BTUnAwfD8lmccA5PEI4O2OHXPlhEqLCJZZ-jMh3A5tszhVshxQsXuOqIZhnNG0JQCrCcEAhj0AaDenuSFkVvp-p-Qo3liZ2Wuf_DgyWlTK5EbiMg5X5rodo-BuoPzAUISeAjRk_MF3eBE3VymN9wxJb-0-LE7c3b4Z8vgUfbp2YvS_HiWH-CCAgqqsjgXq7Q0XK9smXHh3CgQQdL7qWXFznjsYAJoyXwYY0_tFecHLM-KvpVcDhJgVRrx203endXu0byrVsjqXmQw8W4_bINBEkGxASQAcnTRN2ofIa9_mJpmju7oJrjZRpVx2T7ri3MTPb14UdGvDZXPuvV1izREqkGKqegcKEJAmrd_rFL8bAgx_dKrP60oV-uueygyomI0NSWUzpBnaHuGeFvaYgiZ7U1E0Iee2r7gM-JlXzZvQXd57g6Vsx-2zhT_iep1ywMbR-KXzsTGWrXCZlxpe_hpOJlMoTZlGT1JKsK5f5O8K5Ug0ZkrfN19cmWji6A1-_eMg5d-HY1ZFUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=My1IG2Ya3oprAFAcLXP3akTms1sFaYGXcXwA1tU3gCG-EFPCizfljGVwaLI2KWqJxExtMbvb-LmyVfj_rnMO4iDMGjgmMerQdP8BUdMujZr5ruoXVcXHGX7g-bR_XOVQ0PUu4e4pAil9AoE-72-DWUSaURWw8QlEb72BpipbrUdlYr162jUyUXwlAV7VBoFegX2dlAxSY3sLawwa_NPFd12tc8FkCoXWKJ55C2j68WwdOZSCo9bjyPX55vOjN5E1_pai2DwxLhcnA-wVKnR7_xBXVvtOqJmmTyxciXmbLQ0pacc_7wS3Y0m1IBPlSn61uEqQodQSEok6crAqjtpmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=My1IG2Ya3oprAFAcLXP3akTms1sFaYGXcXwA1tU3gCG-EFPCizfljGVwaLI2KWqJxExtMbvb-LmyVfj_rnMO4iDMGjgmMerQdP8BUdMujZr5ruoXVcXHGX7g-bR_XOVQ0PUu4e4pAil9AoE-72-DWUSaURWw8QlEb72BpipbrUdlYr162jUyUXwlAV7VBoFegX2dlAxSY3sLawwa_NPFd12tc8FkCoXWKJ55C2j68WwdOZSCo9bjyPX55vOjN5E1_pai2DwxLhcnA-wVKnR7_xBXVvtOqJmmTyxciXmbLQ0pacc_7wS3Y0m1IBPlSn61uEqQodQSEok6crAqjtpmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
