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
<p>@farahmand_alipour • 👥 64.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 00:41:58</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSONVIsp26_1VDcqhFLnzcDyIwODMlvU2XWQl4yxR-9ySxvQ9YEQeetztBtB6wbEzXjQI_aiNnZ8N5wQ4VV_hKcmzSmzCSR-Hlm0MKFZAwf1XPK5lKvPF-pD79AD-lYOpM0_3SW22gdN80LeGvMfCO_TsA-I4q7R0sorTyCmQcRCzEkh8RMkAZHXyTji6OuckOe8Sit5VXbJ8V5VAo8slTQOlxN2PByEaN01Lnownp91m8GD65Smnxz5xc1Dn7PBhAY3I4rpBf8QTOdtsskmNv0bXd-sUy6oCp2Wkdlt_AXLOhoy6lB0nnUDwG84mIRytGvBoqYu6x2sRD236ehT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhTL8ErttPnft7J2BrI318LtzNJKOudjelb3EQc8kJGTjRG6HnHbvXA497CHFz27nztXUEhXQ0rENq5Oyqt4vG9nAstl0FcyfZW_HEMRoBUoiT7zFgiA1A5U0GZmA7MvWVKRz9wgtPGdqRqkaxwjYlVQfB7l5_pBoYIHM4wO-YnjU2yOU6Fpj_OnOebiKgnrpkQEWBKJI_sVqgljE8SnzUrhrolk0DimMSur5B-qAsjdOzI7gNfV-qB-6o7Bdp8wB9ZaJ3kK6MOs4f0Ift9rqiEwV0BSNdnd8Z8woSDosskvWeTpZc9zuIqi2IJNRV7w8RDlV3d79-euQV5Zn_DjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEki-oJbblWpnCgzbOgJZ-MkPZpJySiR6IVze5DsDfbIPqQHWN36c9wMO391LkDbSUbOWcCsM6DMQ-SBEXlR-n2e8wxf_2i-rBdE9rSbfOUEbws8_sKOFEv0dG6hYS8cGpzd3r5mbvAXmPpCxLYiPdjrXsVz1zFyWjOWYwGiybW20E8lB--Am-zLYejTwygaedtwro8X1aDh_trnh-mAfcMxR5ryHMtQNsTFd8IhdV9cMK3BIZ4CgRH3lpxUVxanRZi1pp8Zrr77yZ7qHV9RkgT5aAw-RfkKw4NyotB9Q4YN82zcH9GtvZQOxWsMAIB7RqMmNheEv8AfYG1ebYnWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7tV4-8JVF8fm2x4oLRuERcGFMQjcZFXccyw1V_v7XticMuDPFc-Z0tjmJeoUm7ShfaxKBmFTYMK_AWz0Qu9B-SmqPA8yx6c11p1YyXpxXfvSKfl2RanNQIYGL7f4hQcD9UlESgSFBPNAcHq6N2RVrkWGxtJF-YFTO-eLKaU6n-PFQOfe_qohEpHcc6AkY61qM5XbrDEamY6qNF8V05RSP-WWNnlJrS2yszz268_evdbOZhviz_HjBtywd6jJcDewdD9MA5TyRZnW0WrpOZQxlcgxuW6iIFlFyi1H3wsqux1CBUowPPaO23s50rDE0HZZ743QtgXdq9m6KuETM9qTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu3kGq5ySqMqV1auwWXL8CqTCv2C2Wj3PrJBRWxvALfu1vXsxX4G8-D-fIWN84dq7-CzYjDui_Klb0By-gfrvBjR3XYPWtf9xTbgolh5_LNcZfZjbY0A0PlS4YZP7EVUdGoQ4IOujQqUmZEaXFHERfuBUs61tMKauFJznC03oxk2U6IWEa8XiswMO0epStuVZkbmi-EmofJ2309Gzzxss7o2Sl2O8uM0a1_uEgycYjjbK0GkGtYa0QOAnpOqfglXE2Z4Ak9G5BBxmw8UsrZw3C2ZHnCAOeuXVp7yE-LbBVfOyyB7m8u0bM-6PSht7FU93KjTE1ATY4ziyHOe_i4NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=GfjrqtovNlMuwMZIX0RvmRfdWLdqEYVSbl93jN4qoA1OetaoFMwQZrewLyqOtS7T7oLw8VQGIih6LDkkA8XcvXJRv4MxVTqjjOPT_Yy6nWFCGLrUekIDMlTYxyBrBV1DNdwwLqiMrr7DmXwWvQx8bRycYBl7mMqxeo9mSQjG6IlG7hvxVLKJPvzFARAUX6VgcswlPC5PWmELomp32YXYg7n1ow5BGyvjGrY0lj0L8iPQX3Nn5zhBonb3NAQynJIsUQSHkInwfSqP88KDS8l9KpfEzANjtKqUdL1ULlhxRnBenv3Hs2JGsACSZ29JgnJxnm9Lv5rpDxZC78Uvh9XaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=GfjrqtovNlMuwMZIX0RvmRfdWLdqEYVSbl93jN4qoA1OetaoFMwQZrewLyqOtS7T7oLw8VQGIih6LDkkA8XcvXJRv4MxVTqjjOPT_Yy6nWFCGLrUekIDMlTYxyBrBV1DNdwwLqiMrr7DmXwWvQx8bRycYBl7mMqxeo9mSQjG6IlG7hvxVLKJPvzFARAUX6VgcswlPC5PWmELomp32YXYg7n1ow5BGyvjGrY0lj0L8iPQX3Nn5zhBonb3NAQynJIsUQSHkInwfSqP88KDS8l9KpfEzANjtKqUdL1ULlhxRnBenv3Hs2JGsACSZ29JgnJxnm9Lv5rpDxZC78Uvh9XaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu-iXV5vRHSQewG5WpkCUCLa79TlqCYmvVX5WKOs1p3Lvel37xL5f9NW5aAC9165kvZ1WcGQLBsFW7ItE2BQbHw3w8zvSpEnt0NAMhDXktNXr5m3Kfq44SzRwV2GqYbeMB9jb0i_76FXpm1VFNoVORua6G66kXQgjqh7oP9YQFT2YAnt3xxf4x2b60VGAaTxLuWNBlLNRGrnRJ6EwKwlRWcvqyN9I968aNousuWnTxlIb2HsT0spiflrmoxiuSw97pMR-ZztlcfJE_Re3dkW7ndjDgocBnegF42NkXQh3C3a0wpUy3euK9-Dd6ZPIbWplAYmQKa8FX46J2-jcP2EWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuNp7tGDbxGmnWKRji56J3PYKel5MjJ2RlVna03dtS2RFLqVlHgHLfvnLj0WM2RHUxQnvJ4FRY1xKEelnCycG_tvY1x7Jq-MgY23YSBKXbpNxFHgG2gBzqvFAtTaBfbP0szc1xvDPyb3DGQ1sDYXeIdZspAVUp4YRlRspS9KYRbyeRlprFz5zCVOyQI5125Zucw_dUECFC4PDz4-PzzaMFM3UwniLn104-XOaZkVClNKky4QofgpDVnO3VHrKaX0Em3lQcw-wUzEMaMze7AcgqjacdDrnJSQDWWPMagaQWOFzhwWK9OXF20OZeDUwCidKtqr2ydTnTTGSLUujaePgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPQUHQ34FTDXt_4-d-0QXz7Yn503oIl1dKOJmwx1NX3aLt2h00UiRRY-ORbN10JAMRElmi0DVf-Vh1477T8setf_2uIDF5TS2xnpvGs5oRbVlSHPphEIMTJOU8X8vSPI8w4DfAQxNUprdJ3FLq2XPugmrV3gpNcVoZGPWndzjKw5NTKPhja5HcBC0WDuk31dXA0ZnGmGl2-CsLQn2rq79DQiumMniJEbPVCCtN7hWB0NcTtp-_q6uusaBMqFT2T3WDscUdHScpMmqBn8NfzSPbfMsfVwLv5Tiy6jl1h6yxf3TmXNpAD71GrM2ooycvIG6yR1nTIhjFdzaDcYvaPabQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=JPnI_lZBNQoLTAvF1Bylx24rsfSAiwC4bjGchunMck1LOa7SOLZzxvpKaZdgzFoftTJj4hp9Wi8pn8_kEQSUTgfqT6RyjnmbrbwRUN6yinvPa3l6iXm2X8fyJtMuoymCIT85Cy5gfIQ4KgA6Sx6Az4uc8W6greON3Pj6CUelP9or21Co6ZTGeZf5xQxsTK07A-rLHe7sKy37nT-YFMmSo9ybF8myrOYXtp5ImhRcuTn0OEXwco-94xT9LAKdXZ5NEZKVAwClAacFkpMNW0bFoQ_GJFeZbgmZRxbjN_HRdD-Izizo-wIqy0eOYp322zZLHNpNY5JTvcg8faBnCtzipqTTRKNargN5kUFfg_NKkDxTW7Z0TmTAMTz6sgVXi1aH9RojABDtLPe791GOc6bQrE_lhvWPSjFOQs-kf1liy7BXq2t3kBMpvqwVBTMOG213RIT6SUvDwMgfHJJjhJklAzKBKfXKdZRBv5_hb8nqItUNeVUPeBWBmyWWskUn8T6TUNcBQc09Rh1VxZwmnmgSbyteIWvRRbkvfWNPfrPiwbT-kn_frFgZQE4oxIq824Xmhu57dFVJQLi9SneH7lE4uUxIrRL0NnxBpwr-iHwBHnjN7hnIhGPWkg5hTmDoG_z--IWtMtdTE1eZ7-1zUxd7APjMi_sq9OYnVLDEeaIKyyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=JPnI_lZBNQoLTAvF1Bylx24rsfSAiwC4bjGchunMck1LOa7SOLZzxvpKaZdgzFoftTJj4hp9Wi8pn8_kEQSUTgfqT6RyjnmbrbwRUN6yinvPa3l6iXm2X8fyJtMuoymCIT85Cy5gfIQ4KgA6Sx6Az4uc8W6greON3Pj6CUelP9or21Co6ZTGeZf5xQxsTK07A-rLHe7sKy37nT-YFMmSo9ybF8myrOYXtp5ImhRcuTn0OEXwco-94xT9LAKdXZ5NEZKVAwClAacFkpMNW0bFoQ_GJFeZbgmZRxbjN_HRdD-Izizo-wIqy0eOYp322zZLHNpNY5JTvcg8faBnCtzipqTTRKNargN5kUFfg_NKkDxTW7Z0TmTAMTz6sgVXi1aH9RojABDtLPe791GOc6bQrE_lhvWPSjFOQs-kf1liy7BXq2t3kBMpvqwVBTMOG213RIT6SUvDwMgfHJJjhJklAzKBKfXKdZRBv5_hb8nqItUNeVUPeBWBmyWWskUn8T6TUNcBQc09Rh1VxZwmnmgSbyteIWvRRbkvfWNPfrPiwbT-kn_frFgZQE4oxIq824Xmhu57dFVJQLi9SneH7lE4uUxIrRL0NnxBpwr-iHwBHnjN7hnIhGPWkg5hTmDoG_z--IWtMtdTE1eZ7-1zUxd7APjMi_sq9OYnVLDEeaIKyyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB3A9p9mrRY7nfia1FJOWUyHGfPSIJSj_dHf84lXPRpinKOe6hWFOtpz1JFNjjT6esjOZGswhUOmEhCrM8-P1m1pY1m1x2z2lPxt6aSJBf2HA2Jua-PgRbHV-WPqMhhyU8P2MuSg6Bw_BMd0FiVX8Wz3S2ll68eDyCKaINqbnz586duAy49w2LoI-xg9zbuGfHeBvc8xWx-QzAE1mOOSgs6iq71bgfVkl_G7C6RwdzGUHkc4vqYDqL4G3Ogz3xJFOIeKz-BKtYbtt5UiL4e71MPqdTgfMvLW4qzKluWphCpJ9a3XpTfoICk5jt6ztCPdCx-sR4roR7epCjPvJq9kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtSoBOzmotkXstioW_GTqBhQkxl3SOQjf3gtl2uYLvNVInY1ZmyrolEWxiTqncebNZ9zuIeHBhVXWHbr3Vzl-bk49XA0hS0orMt4n0xjymK7uN4Wnyn06BPbfg0GlbugxJRvZ_QVnGTBHDM01XWnY9E309sxiRnorQK7t5K2dz5udkFgkkaJUoVSbBFAQTBbX7Kf9sCNxE2x__eqEsl42Uqr6jTMPQjeYJHfctPwDCE8PAl4JCV-GMdNdCW_8Cp2ctWtfIYgWApG1iUK1RDgr-ckv6OjaS-IofTIOQhbd3e-mxJaPVmvHl1rtGTSJ6Nito0dq1EOy3pnLoRHrAnsaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q20ZwjYzf48u8YeuRfqX3JdXnXlzxR3QCOXRo16U25z7lhJkK4UUuMbI5NHieHOmNYYjK2diyZNgxdacZcwxlMZ_JhJDQHm2HxOhLZK0_uX6J5uVgU8rX0Xf3lLXAtmmBNUpPIn5hKsfSqk2xTl0_wkwhGv_2CgG2HoxddtpQNy41vGOmUfvctZ_eg1MVC0fbOvtEaub2i9zNno22cOt7g1cJkWT5uVS_73fqGu__DXyBSByiP6i_3qGCElBPgIqUQa4b4smiW4wJA0bAoxHfRuunpK8woYYHVR1uEVnyORLtUddIwYWYgdy6BDtU1RDbNJlDRlsHFZYdee7Hs3u0Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=Xaquc9xVgHT0XLKn_yJaYAA8lJ80sODUU8O48GhJCGCKd0YNSmIyQq6la53nx3bR-fYiocgcYCAKk4csXRH96dCtLqkV5uHKnu3L26lQdb0HHCz_kbaZ_r52G-E8ISOIGCXrGJ7t6tP5b5akVufzfeyB6cf1J98JkEQRGCGOQGfdGfFPvvzuRfD9RLL0xhPufjfcGmy_4IFLZczKNXgQgs_2qGKMM1_kONnXO5yJmreVF_JkRFC7-RoKaHeovkEjCEJVIiXptI8-59o6HEqsPduda_YchmSDBGil-uPSh77ujJQ76zzNWGDlsrw78VxA_K_7Xf6U91m_FqKjwhALtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=Xaquc9xVgHT0XLKn_yJaYAA8lJ80sODUU8O48GhJCGCKd0YNSmIyQq6la53nx3bR-fYiocgcYCAKk4csXRH96dCtLqkV5uHKnu3L26lQdb0HHCz_kbaZ_r52G-E8ISOIGCXrGJ7t6tP5b5akVufzfeyB6cf1J98JkEQRGCGOQGfdGfFPvvzuRfD9RLL0xhPufjfcGmy_4IFLZczKNXgQgs_2qGKMM1_kONnXO5yJmreVF_JkRFC7-RoKaHeovkEjCEJVIiXptI8-59o6HEqsPduda_YchmSDBGil-uPSh77ujJQ76zzNWGDlsrw78VxA_K_7Xf6U91m_FqKjwhALtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVEpr7UgeskzKuHazp2PD-MemoyaZ5-wqgKwbksuJwk-EVKblRvZ_fmFWzdo15S_4ALRdqOaUuOQnpQWo3ykAS3hVzaOrPkVUNt1rKBihuwaAbeEpReduapnvDzAatn3bU2vpEgGCKOgBqeZxY6dwo29zmpqED1nz3BbcEB9SlIl-rxJYNkAWvTvLWMHIz1P-tSiKhXw4ccZcVq_JVtNOc-_2lj_9DHJAxhSZCLG9AQ7f5fPeb6YRA-JocNy2tSlM13VaLBaCoOB_0MOBZ71yWXJlg03LDkd5DZtMcRZFV6xAKMPbEyfGmzwL2J4p4kCHoLF72eMYtKhOL5ld9TPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XReavAP1Y-GvUEnfrFxjQkenMd2wRFHg3h3GOUfo5dHqN2l3yWhF7-AfenqHNTB-UQT_aLOFRzOl6mXM6wX-mJ9iOxF3avzv0ucZ08hjIwdxdNoL-rXpMV-RMcPyHRpDdMycSAz7Z1UZXrRAe-o3wetecDibQhbRZbbqjZQTmwp30B0bNJ2F4WNt2QDZjuEC1duxvQ-ETdSD4OyrwYGu2sHkJUdmGavt-3eToDzDLR_blwsUgm3lfkf_hEgTBy9QozzLQYQHL3LKYoZY8NMQSCTQI3lm6Bm9GM5QzVMzW44UkOsRK_2OxwFCOVwsQy_chxXH_MH-V7T3rvkaAx3Crg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeuk9OiPOaY8jUY90rQyuBd4FKITssurwGqDzX28dNjTg99p6j6P3psVLGt_ZF4x1lLhxiiG5bxo7r8eftXN6lby4pHuywM_ULBsmY3-OrrkKJwnp4MOQMSA4P_IPLgNfpU579s-VjMYWx4uBcUaM9a7As8K1BbCABcCcBeYTMj8JtkiTykUOpi2h5fQMQJjxNOsthlwoitHh8r_JvMIlTcmKExv5Pwx2LNBHfJFPyNVnR1D3SjUpFIHQwYTkWlG1-OPZ-Htc_kIqh8Ah8nd7_SewbjIvSAfJizYCgrxeQOF3N2rEunxbHxtUulRz1v6kNDEhSdEk5NZPi-HR9sUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3gJ_sFl7H3YEJU6fTTsY5rg9KgWB8tqOblXPSfIQuSY1_eoCgE7wlB70j6oCsXQiNZNU7TQsdb1DYgUwWACo25QOVyfQpCanIWHKpqXn-gndkxZHskH7YGFfGF1Zp9s6rZI1uiCdWZSr7FwaXrYD8LvtRe194xrxyD5_kbhXtf-fDb87htxAHRMHGFq2f3shxJvrYpGIsm_dwqUkmQMYvJ_Cjr5Qb4WTNRn6b32Bb7CMxWNxUB3IuljEc6Cs8hUZ8NLkAQYTKS30WYT9t6w2o05BDgSNLz8iYJilouYRLHITEKankzkCJezuJBUJD2-rV-DWTYqIPn11Q_DaBEzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM9ciL1LReOc3rz5PSICtavE4rQu-cx8Ak4fNjKkdJtAufhdcRl1MXdMgpTsHq4naqFdZjJWVcGYKb_21TACt9vS_PjgAGed9ycuERJQ2C0TEuGv_VZXyI4FwhMVVBE2KCDZfy12XaGa5Zc63GoscqkkTiYEDnUaxO2n2UTxommW9Qr2D2MbdLsyrYCw2Fin-R284xFyW4Ckk7J5Q_P2uV8gupOBUa-X_zkva8p8XWKeyIxYCE6rI79XcT5aqdbVDzZ0XnRqTqRyz34Y0QQHKd8AZnoWvf2xFd0LLpRZIXl0ZW__PjurfDSYQFkZCaqTRtLeYJ4TkxfdbKHdjCDW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9F-a1HF0_NUzRelphgOMgLbsiQ-WVBBdeDEn4qd2-EOxYWkfRc7ADC14mu5P7qG7_71wZ4ku6NYkEuBPtbMGkYWVvgkbPahIqhNhhe0tyCHGbspGLOxH3JVZoEN8Azs2_LkHizUqsSRbA4735Dh7yJ9h2ix05rDy5cryXIe3eR_eAXVY1BRv0U1OZdakRAVmrdwGjtDGR3oRaBlldZ4J9oVqglOxqTvfddmOEKC-G0lL2tEOsBByi_wHn3v5EIXdR2EZlubXBGwGYphxkOPLF-dd7aQGp4_RU-Jo5nHaNVbM-On2fges0dVIARbp8Z_OxPhHa5ZXN4y_aiSnAlI7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxaIfz50wAf7hGhi5-uypc7qtVCOkBgURZIJFFBKCPDZoEcITwbE_ZXR_VUlvYSaWFSxP8XelcR_gUzTvULAy_FFXrQkDee7bxO3L1SFVK521ewGL5_rV_2LMwbC4_FefSxFPwBs-lfG7uue1tja83Dd0QbKzOUiWRiJ7Dt2NLyUh9OP1DXTgjhEt4m_8DoufWS7_AGAaKuBGtEiAoeo7uHJmZoHjnr1vHoKCNbFSvi1_ga4tAob3ldNutJblNqAcbvoxWCr6ccYGo3_L-nYMalO0XEVQaOC3-Q4ivgMlf1CjT4-f0TyJvFbhSY_AdbaG3paJ0zZIknDg4ktRXgECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzpccnThZUo5n1baUs_cOjUnphJDjwVApUlNq_K7dBf9VdmVr7zggWZKSjtwSYzlJnF02XEiPCB293e_m1GxDZriHO6ZG7NUjMcr7HtdUewfdMOx3WYQ86rMu8BuYOLVHgH4Jg8SyxkNJl2C-nw9iFgPLHuUaNJmDHTDhPAXxaBPncuIQ7JIsYvIEEISmAB59s4L_yNwbUqNRu2JyjfVDR-0q_c-b_m8Z3yyOwsv46ZWyY4cYymJYf90c7PzjvFzcHAnO4UCQobLgG9cy_LoeJU0p02l2WJTu_oWf8Y1KJAeokeaXN7TGNLhgO72Vsqh9vO6gW9Wid0geahiGnM39g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6wgowa4y5R67F9e3Gzt1eJh5YfGsa1QrHcKvnPFEoI31HwE4pnhvueMfPPh9zeUAnyYtpgqysgfVMoVq1lD8eGNCGnslcDNUt6l-VbOR5aNeMhJGO82OnMknnuxFy1ux5bEQEW0ArydbJrK7Mu8mCUMtjpWF_4CKbeQPmVLASQ7CHDv8e4QV5G2JCgGnaZXW1S7sTb_UXdLirfUnL3mm06CaYkPGbGKDO5NI3LijanOWzA9lvWhqF6XVk21IMQLh_S_thZ7_mkLkKT-6t_TuNyJTH-ntwifk1rL6_jeWZl6PV9opVeBnRzeGHkzSPCEVdNLvzPtYKX1HX7QgYsZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zmf_HURc_nFTaJyfcDnb8yKwScViownkVMYIWUmUHsurzXZs9Y3QBRl1TYwmwbMqop5tPtLo9UJmu4T6hOne2DX4mUm-HuMfLRcgioAvr4W5opLWjzCUa0F3u7pJfve9pEcBom1tjjC00Gc-pOSnzHipzjWRbnBnRy6Yxc1lJydeiaS4DeNyo_u0SblIy_9ro3DVPlkuV89lNHhXLivrKon6X6IOJ22kvW15QAvFdSQRTBvgyOLBb6uMPc8ZGtHf29sFfVfNSziFqeQpY2owBC4ktDANRGhDe4JrXWci5VKDg7FXGKANDU6W0LOTJbh-8qtYx5g7_K9F4jX51Cwi5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=S6jaISymXumsVX1ezFUWSLBsOhCj9dWfYA0-TzmazmhB4qlybAMDFUTvcUQglvFwg27AgWpn8tsQEYiPXWlEwOafmC9MX1lC-90D7qE4ZWqMXJN5Yf0F_e0oJlx4BrEW1Su81Bn1u1R_kXJRNXK7Bo5qmFQNkW9234IAwOu8XANVrpvE5VKaCZ80K4Eu_EKj1vVCwskeTr1VVCoaJDgHsQZjSGKQXO5bvwxU-_FcN3PU4WlDZC78Op5NA7YD4LzVgoX5DU2FFFSamqXWHs1BdnVYxPfQ6nMLcX-h9br5T78m4KK2i9APpp7G5-WTatH-3AHWr4_QSRj5g0FZ48rGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=S6jaISymXumsVX1ezFUWSLBsOhCj9dWfYA0-TzmazmhB4qlybAMDFUTvcUQglvFwg27AgWpn8tsQEYiPXWlEwOafmC9MX1lC-90D7qE4ZWqMXJN5Yf0F_e0oJlx4BrEW1Su81Bn1u1R_kXJRNXK7Bo5qmFQNkW9234IAwOu8XANVrpvE5VKaCZ80K4Eu_EKj1vVCwskeTr1VVCoaJDgHsQZjSGKQXO5bvwxU-_FcN3PU4WlDZC78Op5NA7YD4LzVgoX5DU2FFFSamqXWHs1BdnVYxPfQ6nMLcX-h9br5T78m4KK2i9APpp7G5-WTatH-3AHWr4_QSRj5g0FZ48rGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=DlbmVK0IX7fxy2txNi5VIuy8hRA8kWAMH_kRHBOd4H69z9KphgxVw-jpZJTJrDjb7INtOXNngjL8iLF1jN1WQ5GE20Yo9vgkPL9vTU8oJnRbk8dwpZdvIg44iQZ26NPlAZYyn5SeQpq_xfIIFQ0xzXiwQNj426p8G28euroPsEEEUNzpBtuTBaaKbM0aoaftfbFtQerhZjssEjYvYGkeCrKV_ha3T-x9BAT50N9h_mih55A1ZX3EwP051j5xTQbc13R2lQLF49br8bk9y_mAK19cUynRen1HH_jyYZKxdDQhpE__mwDKDJ4BWyVIzGN0jWzGJqasR1aZSATwGT15AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=DlbmVK0IX7fxy2txNi5VIuy8hRA8kWAMH_kRHBOd4H69z9KphgxVw-jpZJTJrDjb7INtOXNngjL8iLF1jN1WQ5GE20Yo9vgkPL9vTU8oJnRbk8dwpZdvIg44iQZ26NPlAZYyn5SeQpq_xfIIFQ0xzXiwQNj426p8G28euroPsEEEUNzpBtuTBaaKbM0aoaftfbFtQerhZjssEjYvYGkeCrKV_ha3T-x9BAT50N9h_mih55A1ZX3EwP051j5xTQbc13R2lQLF49br8bk9y_mAK19cUynRen1HH_jyYZKxdDQhpE__mwDKDJ4BWyVIzGN0jWzGJqasR1aZSATwGT15AYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmSboZmvyNXOSKTGsicUA01nhvbyT_ptQbvDLixkNVdaNmt5gRUocC7uBOWL40wZHKU_CzO5V1jhaotJHtEV9C9A8aOqdJoE88IAxzvfa3dNFkxm1oTnLyXq2zF0glMouFI3sUxh6M_mZb8OkDACNUyR4vxiASBwYKuDU56ajPDrfnc0-h1KO904KSe4kd2k-LLU8Pdpp00uSn88vKhy9ufzJHNKkqCSRxC99NNP7WcAOa8PZycLKwNb8PEX8RGTJk6DpQyQyIXVxmDU-EAkMCOpcLmhMY4Oyp1vvIuN0kO41mNjBAmMlkN3UP2_9UETxcF57LfOkepKzRmMtDKKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kt51nUDFwF57esty6_dNwg6JbII-8DaW81V8SlHd2PNoCQHtV4k4N3plDHp5JD7YFVLDZQ2dH8nEqDa_Kg-v7V5LV1OYEPR6iKPEv6oJAlx-JwrXj821bwPTFPtiHB2N_hjgdkeB1rVFrWDejmQY1t_2Inb1VwON6ApUwWVM7tIWw9n9285T9r67VWdYhiqAQxnc7eU9s3V86hH6i_w4p4aRYPiX3WbisQZ93GXRNIyvS1twjCebE6067fLPCurPzy88UgDExbdKn0wPr2kmDUBTwbCftlZJA32TWmfLLQl61jHOihQxuJQ8rOETtidOai-S7skkTsSoy6SSypLqhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKhDAAsx7GXNZZkU0tFFft6mSGLpRgGTlzB0wRA1lNHhksr_G389G4S5t0ETTn-x8OEjUkMCBWwk242ZdKbWOZBO4uPnSo-tqTJ6s2DkuIqwfSrkiaRgbztd5tm6Zq0ONpt2U1BZvzyswxSvJHLRcM4vT1XTHUx_HaEx_eZmLEqsaqPksaCU71GqCVNYPFwXIoMzuQbR50Qh80mcbK954sKf_eW1Y-2A4FC7OmYrdGHsJKKLnHeS2gwJN-S7DU6tdXE1GX53FK_6PkrSvgEHHu0A5pV56uXmwkye1ltTFPAcBhNS9c1_c7o7KhKINe8ASHCQ6vLT7Rbr-OZWnKrqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlmAi-j8LDCrqAbFq2bhbhMJlTHwQbcgfWTIXqYWrymokpKyizlh4PyJ8miNMR4mvqZMbKVCQhtI-klvsr6Ojuj_ppC8htgjD9w707lmKOT3uwRWkevYmHVmFhM3xfRnjXEmzPhOnDxp6TTQoOlWKkT7ueCCV9IB0kMkOjC82SM1NjuDfeDQXDIH7eQoH_42hVRaswWrymf7ENjd-C1TCDGEJPu2Xt9h_qHQeUsszTYsDb8bVtRIHtlJDIAgguY96WszCLRkjhPDuxYJ4zDlDPcDct5d5OuUWomrPepjRJI41HWm41cBMXPZ7sHPEhRdV6Mi-Sm33gDMKQt4AKgzjYU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlmAi-j8LDCrqAbFq2bhbhMJlTHwQbcgfWTIXqYWrymokpKyizlh4PyJ8miNMR4mvqZMbKVCQhtI-klvsr6Ojuj_ppC8htgjD9w707lmKOT3uwRWkevYmHVmFhM3xfRnjXEmzPhOnDxp6TTQoOlWKkT7ueCCV9IB0kMkOjC82SM1NjuDfeDQXDIH7eQoH_42hVRaswWrymf7ENjd-C1TCDGEJPu2Xt9h_qHQeUsszTYsDb8bVtRIHtlJDIAgguY96WszCLRkjhPDuxYJ4zDlDPcDct5d5OuUWomrPepjRJI41HWm41cBMXPZ7sHPEhRdV6Mi-Sm33gDMKQt4AKgzjYU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=FwPghDCccpOZoQYqoDNVlyFJcrvXh4N2ze55nXWsHJDM4MtPzabLTiEkHsnj3OEC06xx2xLOFIy4zJyqSwa4h5umY-5Vw62VcEbhD1QeuH1usUupfCr5iVcrxRSAomQlXxKkxClskOXyo10fXHfOBlXTJ246EMMnd6mJF0X-D5rcYQcWUXxf8mstte4cXAAdCJRGq_qRNuIaSCHd9mUVeeQ7teif43e57q1YX09ux0fjoWHcPHQa5HvabOJT7XhpAyKKdNeRh4S5dvKL8RYxal2Tr7Q0F9_9x1rZGkLc2F6SxTUP8Kiy1UjcJL9IEfzdEP3il5G2mb9fomG7vvUFBStOsMpp0S5PF45viWtAYBpjfjIsOwQHVDNnkCZJKPqC_KN6-ikK1v6NNIxPgn_feJ5wiUHzI1wLQarUbMK-HDOAejhTU9OgV0ubrVOWvd3lMg5eHpVeoWCFi9PvaVGway9PhvrJf8G8ytN40T6BBOhbOHZBBjIZZRm8srCnNgFNfEfODtqFXXx5LRcKcLx6AL6XzZkYdYLhxeYRH6MswGuyjzDYjSZ9LEc_uT3YIs0rnEityTC3v4m_FcUtKtwsoYGFlL2rxzvWiOTxFPCWGUxNHbbfPHvioN__U1Y1JdUB9HDDwasjCM7sOQzT_6RHPO5oemHRtQTHRA9XlRN0ryI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=FwPghDCccpOZoQYqoDNVlyFJcrvXh4N2ze55nXWsHJDM4MtPzabLTiEkHsnj3OEC06xx2xLOFIy4zJyqSwa4h5umY-5Vw62VcEbhD1QeuH1usUupfCr5iVcrxRSAomQlXxKkxClskOXyo10fXHfOBlXTJ246EMMnd6mJF0X-D5rcYQcWUXxf8mstte4cXAAdCJRGq_qRNuIaSCHd9mUVeeQ7teif43e57q1YX09ux0fjoWHcPHQa5HvabOJT7XhpAyKKdNeRh4S5dvKL8RYxal2Tr7Q0F9_9x1rZGkLc2F6SxTUP8Kiy1UjcJL9IEfzdEP3il5G2mb9fomG7vvUFBStOsMpp0S5PF45viWtAYBpjfjIsOwQHVDNnkCZJKPqC_KN6-ikK1v6NNIxPgn_feJ5wiUHzI1wLQarUbMK-HDOAejhTU9OgV0ubrVOWvd3lMg5eHpVeoWCFi9PvaVGway9PhvrJf8G8ytN40T6BBOhbOHZBBjIZZRm8srCnNgFNfEfODtqFXXx5LRcKcLx6AL6XzZkYdYLhxeYRH6MswGuyjzDYjSZ9LEc_uT3YIs0rnEityTC3v4m_FcUtKtwsoYGFlL2rxzvWiOTxFPCWGUxNHbbfPHvioN__U1Y1JdUB9HDDwasjCM7sOQzT_6RHPO5oemHRtQTHRA9XlRN0ryI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPcTkj_smCECT7LuByXbPGWFEDj6qjSNZ5RTjMwfz4GV65BNBu2IBRSM_8i_HvJAhT8B7N5UroAKFWNMJFO-guEKk1SQLA70j1wHUv9RsingC4YzykkXcuprQGpefecUuTrFCHG1BN7RqFCBddESyy_YxXqsMXnwKKAVGqWUsvJB5psW41Z0cusFeN-y_RbDJz7CZPpnwsLwp_ckL6KNQZoBWdcirOskYaWIlzpkeTZklv910EYdjI-lEW3txc4bFVIC8eL0eZWrbQmDEodMNZCYC49j6woSE9jk9h9hsF6xuZRIRhEscdCki8UHsshsZB478oK4xPIq6gipaFh8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRtyQ8wlfOPqVfEt73zZm3KXm4KEEii3QtQG401ulnso-xcLys3uFhszHGes4jBK_wAaGr6cjcZGIuEmmIIS0rWyeTh_DXYzcUvPATjE0I-C4BTg5PWzR9vxNvuNeA05xI5sghMEaWbimhGDpbHSYu_NNOyhtXWVdaU25lppQThnV3y6z7j7X3FypamLcr8Uzktdp9bLu1fbRSR34zwrtoVT9VCpawsyl0_0CIpBIGOCk0uapFKmIawVv7pGzhAvZ4JKCvnrPiaTr6LPYrw4Q7lepFju2xoxxott56J4BCRRfjCOkeEWTkLYUDdqWw0Ids233bls9PQiR5E8rA7phg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNpZgYH0Qd0WMxegY48MjRooCRNneLLt748gEw-tyt4CwKNUe2V8KYCSRvYtkMLcLr97iS_WSMYRQfpu7s4cDVdus4hWU42-sKWq2Gmdtk9scsgCmcmhn3RhKlIaU9MoDTnpyCBXpAp9jrvUXt0MUPWcFBGkScN0QRY_sTEe7rzZFefIQuCj2tGkmzsRAaH_nb0lVyRjrCc5LXj-p9xN2fJwXScpHXam2xGog3uxQYEvFxkQ1HJTs8SBWID-ftRWccqbS5Ct59kRNziaoLP_UC1MakCTzM3Fc1uQGqYk0i3-c9a_JzdJ4SliNgiHtnS7D-pwHVBltstbxW4VIG0XcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=nQ2atJ4w6o6vl5Hl2_DtGnmrYlYgssA_GidCTFF0PhVPjd2qIR-Wpz4Q1ZQr25BNIwwWnZfiIL6WLcfv9aboa1mdm4tPBpX1w8c6yMBUAoystEHMsCK_lEo-dSV2V3BNTTcKK9u5fGDN9BtNGL9V_XrNFVqB9-iAFiVZZ_dblJlige3_rm3Ior-Mb5SSsiV9kopKddAKyaLqrPt7lnPYSxIxbJ7ew3vDdXZUrQrWTPowhB7WSG7Qjbmw1Dc8Do3Yk3iroJ4HUatgBoQsyrjL-6QSgd4beahtk766-BtL0e_1DRIb_ymf1CkeehUdbV3UgCtjBarBPv8QhkgIbZxGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=nQ2atJ4w6o6vl5Hl2_DtGnmrYlYgssA_GidCTFF0PhVPjd2qIR-Wpz4Q1ZQr25BNIwwWnZfiIL6WLcfv9aboa1mdm4tPBpX1w8c6yMBUAoystEHMsCK_lEo-dSV2V3BNTTcKK9u5fGDN9BtNGL9V_XrNFVqB9-iAFiVZZ_dblJlige3_rm3Ior-Mb5SSsiV9kopKddAKyaLqrPt7lnPYSxIxbJ7ew3vDdXZUrQrWTPowhB7WSG7Qjbmw1Dc8Do3Yk3iroJ4HUatgBoQsyrjL-6QSgd4beahtk766-BtL0e_1DRIb_ymf1CkeehUdbV3UgCtjBarBPv8QhkgIbZxGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwEQ3WJoYT0gwIzzGAtvhnanmxiBf7UhhRnfvJgiqScYK_QmjE2sc0qOpc6jyptLc4GHU8kHOwJTFbSAzaICnucw5gVdpZp-vPJ_fhww4K4SKxWkPPIJz_leSCsk_2Y6ejfwmTTfNAWly4OigifFLcIfWr-BCUsBgaZzBqbO54x8AQ6cK7692Cys9Vh-QtEfHGZMrM0SANsRJEXRaULZeYss77rvctsdfwk-yA59js7dQl9XaCIdmAy98be1n4-ey7PXGwmj1IWI0__Cyamtf08BjryDvfu-LQmSnlbFgu7Ey2hMwMucYWdY2qdFO35cIWFoj8u1US2pBQzzbYez4Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=uSK-0e0IGGqC00gMPKRLCGhJaPd7l6si0bE_uLJgMkCOQcKCkYqgol8QGKKds8cQbTHljzcfO-LV5HrZDDa5fAYuh_dbZOjKNJelEZEoE6uLGAYNzjbA-3HwEM3z5TNAFwgAu88jFv_Qhw0GFCwShC3d-HcxzzOC_TX1qpKcixDoul8JpxHVQ6PEoI75WveqMYCEkrjy81rm3zT7suR435wsKnSqRd8zJSxu1gVRzTO9GdfemXpO61QI9N6qXzF_BipRQSG8IYwCGNhEETk4fmNbqjsJQG_PW1-FdMcb9_hueWE6mK0QOfBx2jPjQdjxHnvWVvcZuSwiE3JuymP10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=uSK-0e0IGGqC00gMPKRLCGhJaPd7l6si0bE_uLJgMkCOQcKCkYqgol8QGKKds8cQbTHljzcfO-LV5HrZDDa5fAYuh_dbZOjKNJelEZEoE6uLGAYNzjbA-3HwEM3z5TNAFwgAu88jFv_Qhw0GFCwShC3d-HcxzzOC_TX1qpKcixDoul8JpxHVQ6PEoI75WveqMYCEkrjy81rm3zT7suR435wsKnSqRd8zJSxu1gVRzTO9GdfemXpO61QI9N6qXzF_BipRQSG8IYwCGNhEETk4fmNbqjsJQG_PW1-FdMcb9_hueWE6mK0QOfBx2jPjQdjxHnvWVvcZuSwiE3JuymP10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGn_vj0qpMUa64Qx2q6hDOuyxt2XBYol2FNzNRDv9-U7-Gmz0JIy7-Kdv75G4Dtes3SOow0GnYvaR0jqzoEGNgPi2TlULlEDiw9MqddKzUA5Rz9fyc79a_Bz7jtOoGXQmd4mjfcBUsGN-5V8HF-jOJsxhHSUHIVGVn85Byi-R-ln4Kcf--laHdyxtudUtzkWkhTwW8IjMuekHI0dsT0b2aVP80InjL3kpiIsh8mR7bGDXVgppxMoCc5cS6ras-Xz7Cobo8TiAbXYNXnJSRxQd1cEYfcAanFTJz6RGRXF9PPHDNxAqzGT8DBHycRSIVlIqzUFajdsnHl0pgZKLPbcrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfP2-TLJl-nlWwcU1k8urNKpv_G89X4d53RR88cacG_XmEmtF4lDP8RFeMMN6-kaWSt6aFQ_acfnAuty8WVvFDmpiQGUjcN8ozavUc1oEtXoa0tdUGlQUbf0EOCK8MtpnqH-mWvQyawIDvO_QfEDZZpIuw0eQbE0CtxYYXG_3v3uHgM-5JI6amHcDT9AN8CX2yhuWdujAEwg8QqmaRlqgMX1qbQexN-l5xBEsWnthAiWRq8M1dIkFPc3gtEo2yQH9zIF5sUviE4YDKeLefQjCIrTMVQBgWQLPP9YCNwif04RTI0LVpRjMRH4Kh3cHuRmOfupDJan99ruaSiYd8C40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=bC1Ni0Yz2hn85OepR7f-K-P_f0-Vk3Ri8nzdzzQAm3oRid5pHi3NJjE0O9tZ4b5e1Ns5TMVU0S8cmagACTUtwvMkKBJJfjgni2P8EpMblCiq8c7_wAX98vxf3a3-VZqElaI_ab8q91ITGu4XBQp2SBdeiLEAwIKYz1tJrvH0upoEnLCRrNLnkUDJ1m5Cy0rIjKAgZ6AQxcB5hAlt8LU0rZQyCzrT6O8H66cKk2n2vGFtoTyamaXS_oJJadfB-8DytgUelyWGJmF7IituKMTHJ7FIzOYLLez5t_199cNq4ctJB-FO4fvaXwT2y__lSkUiCvEqZP62pMvWJXWphFepIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=bC1Ni0Yz2hn85OepR7f-K-P_f0-Vk3Ri8nzdzzQAm3oRid5pHi3NJjE0O9tZ4b5e1Ns5TMVU0S8cmagACTUtwvMkKBJJfjgni2P8EpMblCiq8c7_wAX98vxf3a3-VZqElaI_ab8q91ITGu4XBQp2SBdeiLEAwIKYz1tJrvH0upoEnLCRrNLnkUDJ1m5Cy0rIjKAgZ6AQxcB5hAlt8LU0rZQyCzrT6O8H66cKk2n2vGFtoTyamaXS_oJJadfB-8DytgUelyWGJmF7IituKMTHJ7FIzOYLLez5t_199cNq4ctJB-FO4fvaXwT2y__lSkUiCvEqZP62pMvWJXWphFepIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=YyBkdasgta1gZjW9XGsbVSj3vadSZIVAVF9FcEsAnJcVz-ZKBW1ER8Hnk15BTuLQpPX0uLyiVeAQQqXU47x8RJ3jyOU71RRPzX0PUjxoRC09-gDaEUvhOfUeFWvewaVzQYvmFPwoogI6D3y_Vusno0uF-JXmxpTSupPgfIh2mEsaLwfCwz16vQYtnW6XPtUm4jgvat_2q-mffzBa91geZr2mNhUfM0ItECNJ1g-qEfzi6FZiWbyghrlBxcQb7Ah8JIFa8dZpyhtjDtVlL5SI3UR9DYL-U4NVtoPQKkavqjI1Rc6C1ITiJx2FVE58jGbec7p4qgGAW6I5-hhJRF7wYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=YyBkdasgta1gZjW9XGsbVSj3vadSZIVAVF9FcEsAnJcVz-ZKBW1ER8Hnk15BTuLQpPX0uLyiVeAQQqXU47x8RJ3jyOU71RRPzX0PUjxoRC09-gDaEUvhOfUeFWvewaVzQYvmFPwoogI6D3y_Vusno0uF-JXmxpTSupPgfIh2mEsaLwfCwz16vQYtnW6XPtUm4jgvat_2q-mffzBa91geZr2mNhUfM0ItECNJ1g-qEfzi6FZiWbyghrlBxcQb7Ah8JIFa8dZpyhtjDtVlL5SI3UR9DYL-U4NVtoPQKkavqjI1Rc6C1ITiJx2FVE58jGbec7p4qgGAW6I5-hhJRF7wYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=cFw-yGG4lGBMOYZULAQaqFQlvR3yi2yHP8iAuPtlMm6Bm3IX6Bt_Ka7Xzvb5x2cZ8Vt1enJbwoUC4j4kruDVrPWBHQpmoeWEwoAv_B_4dFMANGlwCymzeWHsdFfqTb_h_4EmjC7BH8TakK5BWqDa8zbkCxvvHEwIb9yJecXOuYaQrIoJJVATuJdvXYTGv-u-0fUVGt-ZeQ7PqiSUGu-jOxs-z-ILOmByy01BPLTLJdR91SuAhEMTx90tNSeRfcYngZQ477F12n3QgqtFbpiC033MlI_5C_aFbQC4vP8Jjzup8dwJdk-WZFNF4n6Xu1NgcXWIf78Z49GWkpjwV3ZP_yFS1Ugwh1YfwsFGD3_5ecLKoWPLQdbB0AEpj0hXa6GjuB9UkiG_erSuPYmcCqAU-2Gzd37NKLdHOV2_aM0zujp60hYM4AIv9cq3EANjFDcuTqm_IKwyc5vZuIwP5XV_AOPGmp2lNHZvZzlgalZ9VtvY0rXyPEFWNMC7XRtbJ0_PqkXNv11bTlaGGFdwbckvM1JefDPPgWEN5hIqv6t8F1HlS6hC6u-tdLzhSO1eEeYHPcrTQtqlORhurdW0FhQoTMy20B3GO8FF-a7jKS1hybPFsxEL6NWt_DCATHfikVG1TFZn5WRCtmcdd2jRQhOazezSCIYFq2Z2nVUoKRhv8A0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=cFw-yGG4lGBMOYZULAQaqFQlvR3yi2yHP8iAuPtlMm6Bm3IX6Bt_Ka7Xzvb5x2cZ8Vt1enJbwoUC4j4kruDVrPWBHQpmoeWEwoAv_B_4dFMANGlwCymzeWHsdFfqTb_h_4EmjC7BH8TakK5BWqDa8zbkCxvvHEwIb9yJecXOuYaQrIoJJVATuJdvXYTGv-u-0fUVGt-ZeQ7PqiSUGu-jOxs-z-ILOmByy01BPLTLJdR91SuAhEMTx90tNSeRfcYngZQ477F12n3QgqtFbpiC033MlI_5C_aFbQC4vP8Jjzup8dwJdk-WZFNF4n6Xu1NgcXWIf78Z49GWkpjwV3ZP_yFS1Ugwh1YfwsFGD3_5ecLKoWPLQdbB0AEpj0hXa6GjuB9UkiG_erSuPYmcCqAU-2Gzd37NKLdHOV2_aM0zujp60hYM4AIv9cq3EANjFDcuTqm_IKwyc5vZuIwP5XV_AOPGmp2lNHZvZzlgalZ9VtvY0rXyPEFWNMC7XRtbJ0_PqkXNv11bTlaGGFdwbckvM1JefDPPgWEN5hIqv6t8F1HlS6hC6u-tdLzhSO1eEeYHPcrTQtqlORhurdW0FhQoTMy20B3GO8FF-a7jKS1hybPFsxEL6NWt_DCATHfikVG1TFZn5WRCtmcdd2jRQhOazezSCIYFq2Z2nVUoKRhv8A0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkCk-96JAHj1E2QTY0_HckXZa0KzFfLAsmea3PPSnOb9Lh4O1pFv7NvlQLq8sn5JwkpqyxZIO6VIQcxu8K2Ej49sfQeYZHTB5nHuoMs5RZ-tlyLRN17GU9Z_QSbPYL1ftSgvDPUDwUf6fqnO9UaBwiR6x66PSOtDu6ltkRp1mKJl3u5E2FzM32KTTD7Uy02Of8ParueBqAQAudTGzqKAfZrOm0Nu4TJOEw1XQwLb8_1gpnc4fP4l93TomtZx8Rm7KIzoLG-vhpymbc4b-TXgXyDQBtyZJATLb_TV5OvVOZLUBdl5oWvL1pwZtn81_d6Km_Hc0D2UwiQZtrxyjKmmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXYApKGuhbnOX6xKo8VdbuXdTO6vQXJrHcID6ch7QEtwPGcHWnuTsuTWOAFUFT_Pn-BYWnZDONRtBR0UvmdES96i0KxTimhbVuFh6bISYIWT5FKveMKfQfM95DPtBJg8np5s-lagcIAColWcA17YHKpL-1LGjLlMRwD3owBvynG2Dh7q3ZC7bCkD8X1Nk15F2eHLK6gjVwCLROTENWYUYyUb6oJwTAwPqXOeeB7URCajpC-kv6lO3DutEKOnnnVimhkPUd9J5ZxE5cTrEUifWvRit9-LljzvXE0YGDy9tYv4fyNB29mOwEDh8RFgtbOjpqun0haI52_ctfZZnIqKhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAxSjRXbDE3yHnsNF2BlcafJg6FhqNTWWc6APnxRo2hlSPqz1kkRxUJ7MJeNVqxjjvqtrW7K5noGeFNhpwWRR-uOV9Danmw-lrNewbbwKZQ4t-VozJ09aJe-0dEhAklnxfyGlhHgo42J2rtFjCvvgEIPChOlwCjDIdp8Ti6Jnpm6pSp4YMy05TQ8S-e4HmocgYMbyFdfU8XyN2HU8IrRltWUypMMwTu4oNC5cvGd2q3AObVstXqw6dzNHgS5-b9d1ppiu9grrmnKF7wbdpqzZpPKI2Og_vO3dBZeGhNgWtMeBaqXGQiREjUHX7-q2VVicvYnVxYwVpR2UVLIS-k_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=KtcNgzhbmOLzz7LtBTM546lE0u5GMrWHX_-uVX2TKPO_aFEvo7pbYG-MEKfgi8SU0KGWrCkHkrBCjXt8yTNGguJSn_tfmZl4TcIbncPvUr1xJN3bO819edHBGL5pBmUTBlOpqAO1WrwdEvompqekxMYysuj21OacGLxRm364BnnlbiA5050Sly79GgBsXmiMZ-7G0yOyFOSAsq0VMVFBp3hekkyDXHdGTaqLqp4bzbuTNMnLmK33WKfdwDJzFalWa5fgzsaucpZkVa4JuSHJvxQprIpesDnCC86KsEF75SSrmU2FZhJlxoLcBs3nIQeEHGTA-F_d9D7APBnRVBwDH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=KtcNgzhbmOLzz7LtBTM546lE0u5GMrWHX_-uVX2TKPO_aFEvo7pbYG-MEKfgi8SU0KGWrCkHkrBCjXt8yTNGguJSn_tfmZl4TcIbncPvUr1xJN3bO819edHBGL5pBmUTBlOpqAO1WrwdEvompqekxMYysuj21OacGLxRm364BnnlbiA5050Sly79GgBsXmiMZ-7G0yOyFOSAsq0VMVFBp3hekkyDXHdGTaqLqp4bzbuTNMnLmK33WKfdwDJzFalWa5fgzsaucpZkVa4JuSHJvxQprIpesDnCC86KsEF75SSrmU2FZhJlxoLcBs3nIQeEHGTA-F_d9D7APBnRVBwDH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=N4c8cZj_eR5x74y7XHsgJXwgFUtqVZGhmA2RU9AToFKjeRHeJ5qleVQgj9StoWeGByzj6pNq1zO62qSK8dsjh7qMrGX0ym6Jjz312dVW9mzaOqqDDJd3QnE1EC4zFOkoCL8qqu0VujFI4We5mazHAPtq0u65UGYMcYuxzJ7Jbdx4pSrMj0WuHWivM7HQAJiNyxZU-VTWLMKwxMADob0R7lh5_7fQb6ywBIh8g95NNlzlVh1VP8-SgOpJj00PvPTZb8BysaW-GtbQz2ucknsPiaTmSn4US88E1a86QRaa4pQ8cpYIfwVMCjwJ15Ocd6CAP57atvY4EzYjgxTUxtIKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=N4c8cZj_eR5x74y7XHsgJXwgFUtqVZGhmA2RU9AToFKjeRHeJ5qleVQgj9StoWeGByzj6pNq1zO62qSK8dsjh7qMrGX0ym6Jjz312dVW9mzaOqqDDJd3QnE1EC4zFOkoCL8qqu0VujFI4We5mazHAPtq0u65UGYMcYuxzJ7Jbdx4pSrMj0WuHWivM7HQAJiNyxZU-VTWLMKwxMADob0R7lh5_7fQb6ywBIh8g95NNlzlVh1VP8-SgOpJj00PvPTZb8BysaW-GtbQz2ucknsPiaTmSn4US88E1a86QRaa4pQ8cpYIfwVMCjwJ15Ocd6CAP57atvY4EzYjgxTUxtIKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=WrQ7kpl5bCkr6THh1pJIezD9YGf56iXe2DKfPQvVNfobryY7obfDZhGx4urMCndCZFEA-HeeNs4FUDGkNsqFCP6lRWdWKILiL27pvqnfm6V5CXPZK5g9hkXrC6yzKpTJWmsfBfAUXfoiHMTiaR_e44A8Sprkuqei8po7Rxf5QTA0jUjBBZk-P9D1iJAREqU6PLE106REfbROAwRREVx5nljTzOFHxrATJR-1G4FLCxhqqGGq-KECpk74qvEZHifdUvjwVuusqI3Cdwlsdhmw3AAlPTFVQdt6bJC067Yr4cNhPTvOn8eRPZvkb6_wH6r0DFKuPb9RXISZLTEaQjPueg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=WrQ7kpl5bCkr6THh1pJIezD9YGf56iXe2DKfPQvVNfobryY7obfDZhGx4urMCndCZFEA-HeeNs4FUDGkNsqFCP6lRWdWKILiL27pvqnfm6V5CXPZK5g9hkXrC6yzKpTJWmsfBfAUXfoiHMTiaR_e44A8Sprkuqei8po7Rxf5QTA0jUjBBZk-P9D1iJAREqU6PLE106REfbROAwRREVx5nljTzOFHxrATJR-1G4FLCxhqqGGq-KECpk74qvEZHifdUvjwVuusqI3Cdwlsdhmw3AAlPTFVQdt6bJC067Yr4cNhPTvOn8eRPZvkb6_wH6r0DFKuPb9RXISZLTEaQjPueg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=V2fwxW-uQjNG5NqOL_DNYKSWXZUK5UnJUt69VV3g2rSUd7GVBxJupf1es7QkZiFvYrblxJg66u3tMHfDlFZ4DosQtl5Xm3hfAdvRuw94TWoPpgwO_WwQZNOKmZFCjA4vf0sD-_R5MjqGfrdPRMfncoL2VaHljA_pNTES7nPE7IbQI-VRoxmg1EBbm8gHjoj1WVspUf7N5HEL2b5fpg904KHCQ7kHVJhN7UuqBHO8w5gHkEu2nxyFu015bBOgzqOsslyQljzLmdwtIkj9rCErXOrrStC_9-FnMsqLViqw-eTY66g09qP3kkYUaWCZH2P8KoqRPvVIN4ZSGBt_71YcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=V2fwxW-uQjNG5NqOL_DNYKSWXZUK5UnJUt69VV3g2rSUd7GVBxJupf1es7QkZiFvYrblxJg66u3tMHfDlFZ4DosQtl5Xm3hfAdvRuw94TWoPpgwO_WwQZNOKmZFCjA4vf0sD-_R5MjqGfrdPRMfncoL2VaHljA_pNTES7nPE7IbQI-VRoxmg1EBbm8gHjoj1WVspUf7N5HEL2b5fpg904KHCQ7kHVJhN7UuqBHO8w5gHkEu2nxyFu015bBOgzqOsslyQljzLmdwtIkj9rCErXOrrStC_9-FnMsqLViqw-eTY66g09qP3kkYUaWCZH2P8KoqRPvVIN4ZSGBt_71YcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYsQAkT8mw5An_6ELlpp7eIt_n2_OTxIAypTGe-eUsHB3zpOkTB_qg8kLM-zkk3fyUTJjiV4dkJyDfM67ZlfnekAa0FOE9T-iQATkD0SUXujaGwMo8xbkluO2a7IYmm9WHoI4uxhIAVCjWDKbw90Hi8FI92SeIqYFzLmwOvHtwD8b29KEQcQCwK__9byXcLazUBnecnaQcdtN9-83db68ytWHiLgajoDAcR8ZROQowOqZfUNGI5KMQPvMOBLzGhdt-iOIdsIu0z0L90MCFxzLSejurWT2ILvS2ZqzwE8rruYC5RDrZXoRWBc1AQi3Pm2vddq8QNJdGsZiigE7SWv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ZLgkLTdB-YzdwSPPHnQONewBASO-LZmB47NrzDrgifYal5UOwtAgQ28bwkw9LAc63YNDfcaTjPQjL1Z_qmjT--YRiO-bmzL9gEc4tvFibF4CIkYa-ufULSbq-zbo5qHLF30xCmf4xBAjLF4bGqvDDHJ9b1TYITaStbNto2wnqoHQvPXNYh-DnZaY48R5BNhJhYiiw4CoNI98B1_OJ9f5fNCz85FvMikThE4N-T5VPtAHV0ECTJgWWkEE9pa4tZResddCGq68H7IeX0-L1BAUET-hgXuWnC_5luvrJoLmcAX0FIdi_RrX6AlIRdrmyl4yvoAaEDscBGnMJAJ3JUHkuhk4bG2Svh3VzOM_I9pte6i9E_-sBsN5sGpKkFzEiImhd-tdp4zNY3ZnvKQ0WKU7cG9wz2DCxcGSwBEcxNzD9KQLYnwJ3UfTk0SX5OfyVUwMVKiqjvqrtNCfyeVkY0Q06PuVyp_TZZTolc4MLOuJ9sB5ct7If97phQ5-wbJTdGbqBNXjCqY2kwz27fRrQ2Vwc7uSZQhacpmcpNi5T_WIzv9qQJldKqMp34hXOjPZ6MQ9DPHtFHhdq4qOs0IulhSs5m_ZdfxcuTQLtgARwFCQ7VqvyDv3OaWDYzv74bDsgvz_bgErjqf66btT9mszEgtay4-lOrri0MFTngZGTEEPNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=ZLgkLTdB-YzdwSPPHnQONewBASO-LZmB47NrzDrgifYal5UOwtAgQ28bwkw9LAc63YNDfcaTjPQjL1Z_qmjT--YRiO-bmzL9gEc4tvFibF4CIkYa-ufULSbq-zbo5qHLF30xCmf4xBAjLF4bGqvDDHJ9b1TYITaStbNto2wnqoHQvPXNYh-DnZaY48R5BNhJhYiiw4CoNI98B1_OJ9f5fNCz85FvMikThE4N-T5VPtAHV0ECTJgWWkEE9pa4tZResddCGq68H7IeX0-L1BAUET-hgXuWnC_5luvrJoLmcAX0FIdi_RrX6AlIRdrmyl4yvoAaEDscBGnMJAJ3JUHkuhk4bG2Svh3VzOM_I9pte6i9E_-sBsN5sGpKkFzEiImhd-tdp4zNY3ZnvKQ0WKU7cG9wz2DCxcGSwBEcxNzD9KQLYnwJ3UfTk0SX5OfyVUwMVKiqjvqrtNCfyeVkY0Q06PuVyp_TZZTolc4MLOuJ9sB5ct7If97phQ5-wbJTdGbqBNXjCqY2kwz27fRrQ2Vwc7uSZQhacpmcpNi5T_WIzv9qQJldKqMp34hXOjPZ6MQ9DPHtFHhdq4qOs0IulhSs5m_ZdfxcuTQLtgARwFCQ7VqvyDv3OaWDYzv74bDsgvz_bgErjqf66btT9mszEgtay4-lOrri0MFTngZGTEEPNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=R_NDCuz5RWKykCK5xJCPn_VklKCLRW1Chx-q0S1ueNdIkFlgQmcN9ljxp6EB-NmGxyEYir_Kb5_qb65AL2obK9Af_Ie-iV32ToPKVl_2jmrjmdEz8v-Up2a0UyexM1bBzZtANVSQEZu39Cdshl5myDZun4JohMceH6vzhjNZ40XUHYghvGFAtzAswM5Osz7XIEhQDxjRG_GrZzpO8RFJwmTJQMzCHZ3GGvFhgpJxKcKZ_BOipepdYHML2Snksr3f9Sus46tE5rb6Q9QgUeDnWBBj4-R9Ysy9P_fzGJt5uSzShv6UQNaWckld43bQgXl1wRXzVIgE0a6JNUH24K7o0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=R_NDCuz5RWKykCK5xJCPn_VklKCLRW1Chx-q0S1ueNdIkFlgQmcN9ljxp6EB-NmGxyEYir_Kb5_qb65AL2obK9Af_Ie-iV32ToPKVl_2jmrjmdEz8v-Up2a0UyexM1bBzZtANVSQEZu39Cdshl5myDZun4JohMceH6vzhjNZ40XUHYghvGFAtzAswM5Osz7XIEhQDxjRG_GrZzpO8RFJwmTJQMzCHZ3GGvFhgpJxKcKZ_BOipepdYHML2Snksr3f9Sus46tE5rb6Q9QgUeDnWBBj4-R9Ysy9P_fzGJt5uSzShv6UQNaWckld43bQgXl1wRXzVIgE0a6JNUH24K7o0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
