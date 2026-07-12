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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 01:42:33</div>
<hr>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=NCLRBwhZlKLI_fQ-f4Yfqh7BkRbyhbkngqZLsXttCSlu4vr0mN2J2w4z-8sRd5yJs1UFGXENFAt2ooxUo1U5G7DJwA7viHlajx-SCeidNvlE6E0gRPcmgXwgDt2ClOtWhDkPsbNV1UcoB4WuYLgnKB5R0z60FLZSXYYuGWFf8yRhhVUsPwyVoyti0C-rWrWL89chHYRHS_4Xf2vb3efku_3PUF0f_tLdCoHDwQ9t_IbLVewkCzyedgIjq_skeW9YWGZtNo4a0DWSVHhRBfW8YHUVG_VEBo1xkahA8E5SsEPLLTT4Be_vF-vwAyWT2i8LKTRIKeFt9fzEF7LW0yYC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=hXJyW0voCcIHYGHIXA2kZpImc4L39cxxn2xaxQCz4Eq4Re-9Zu4qShCxI1xpPJHKAbW9LFZERxNJPE-2bz0FxCT-bfdjmrWiBUQ14ZIFp_TiBXU0b3YfDFnNlfZLcuVy26crvHBbPw3os4tXpLplsjyY3kTeMnEPVMfEsJW1k1i8wU7hjgkG_2nP3ZuJBrJOIgAP3wSpBVDctqO1aKJo4eVkfkfnneoGHrJDBr6PvbS-AbmjbgtN9wCUaEnrvFZIrszsHLZ4lQaGgImsuUbXwhXC3C_BVC5INFUjRv0DYHRQpclSOqKYHcbL8ZecAvwCQo8kQVWeyJQc78Zn9xJoyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96Cylua4WSBm4lBT13xREJimfg3cRtT9ijJRN-QqJgwBgdrpXxKL6pFEYeYKlusU3G3j7TWGtOZS8IVHyxmjHSlU9IBEgTsAf7oxG-5syrClWWMLP8FLTXzeFoa47Q6c0EJGDJDUApE_XYa4MovOtRTh-DBwP8zExW83iTxg0rSNSz9Z4hYHcgPy-2o1yau1UL32N773jC-rKGxOWXcOcCalI-hR4lzfe0CLDYtfP2eTJvbtGGRGJgfQ-GJAueUUHltKP5kJqhIV69OrzA60BH0CTCiln-brGwAsxI-uOozp8Vh-bNkXaYnXbQ6ogJkfFTdIpRdJYpMvGjQNW1UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn6N62rRFW96BDhGOXJ15SVjT7tiGRcpbRfq8qakacwoYOtF0NP7Ztpsk_IScrAz7EcHMeC7HY0vZSMYL-7cpWYJ4a0XpRUn97yOS-2A7ZG3AzKr4TGMXXlsNzkyC00EYYBwG96MlepfA7IekrX920CdX-mJjTB5wLWRiIjTa-sV1a_3zKgu80b20SFLESXlXQAJM56LBGDsE39GSNXID3xH6WhYOQVxnxH12YpmdVg3VWAD4WrN9IAsx063e6cGSP29Iqmh0c-Au6EurARe62kmIeJBOc4a__ZtYPBxrVNNoriv4qRO6tGGbej6vjaa5_OfAzLRJRI8CeOB-_3tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ_zHou2COgcJ9EagcxD2nJCLkqxhdnj4BVVArg2CHRFvGFfXJ4SdsJAbkzJz3h4jKreybPN__v2JhDbEdhhElrK1EkRaaniTl0oEZ0iR91z1ogPXv7HO33s1QdB1UBOItwh40ykESzRo--Tv4D4WEQu7kv7Fuvq9_syzFcnpfYzvHppoch_8c_nlEHsMsDoCI8VoRvw922JYDGN0A1AWCjlq5qdt97zcCeLkgd0LLZyiavgLGjIT1FBSPbEyVpi6fRxX9cWTa7WuP7Uk0E1pOFSi-kTN4oXivgTuvHMvW-3ksLOb8dOSPNvbYnTkbxVhE6LGW3A43BNDPpBp3p6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqGV-jMQBuGCrMUfHsB4rGqG3j49Ire9VSWl3kA1TYVUxqdXtrAPabR7vu-Rjw3n1dXx16UzIrF23sUMbMDtuloz9IS23fPWehJFo_WUBWcKqzyECQFmfxM7cIPITrBL5oU1siNOoi23o5_ld6qJ3iAIH0jUwx_KkKBNfjoxIxLIfqUXTSzzlCJfjQ77MRslR8s_B_17SkjmqZREqXY0-jAxJw7v4Pht8xTBpdBko6EofqjX6CiMJm0tjwWf8CjE1JEpLW581HkwIOR0gEbMFuEEq-PyItOQIS0ETzIm1Nk1Cmchiynv3FYjoHk7J2SmBT5Tp3DyYDu4rnwLYZRp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzU-IJGq3lqczMIbUrHrL0tU7-i3HP5IQnptetiBAtuSYeiphxWr37S257JvRV00WeGfVAr51pNh9noZtMps_TF3WmaQm5UqmNRKAJuwTbXgDsbrCSICaPM6g8xVCf3i43glHPO890SZJaey1mk5J5ynmhmcHOE0EGPulM9yRpvJlbK6_c-TId6db-x3F_UcbRa6kp_FvcdzdyppfOEKKmIvrYhbZws-IiJfWZsgubIxIsY7FCPbynXmZlARW0WooGakxmbtIu896QvdsBI5JaZ_uuFs1JF0vFQB8hBwx3jzzawQfJRxkPoe3UpF7aU39TeKxY9vZvxUi-uNH3ADgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMLCI-5k6JyjOQd6qFErgJ3bHGO6u4buoAh2VKuBcGoEbH8sNbulwOoHz4tGCzXbl2ERNUVxCXe79SKcg_IRgrcFSWaAdExXKSHRgf6B_-qO9r1SFOLekhg_EmM4NMGIwRrwwVaYn3Peq6yQZHb90iPWtnsbIiFWN9LLlhRjmtnYdgfeRE4zjjUt3eJh4AKA0R1Zcph1VvOUMfXQ8HXXZvl-mcxK4mldoW5pWWoksEWYoCoe80BlasUHWaqw0sAvoNE9sZChbeZl7_xP78YTZCnkxTIFAY1YYDUUofw5fqf2VZ597enUPrN44uGRSXlbdquAfcLiyUW_amdABxnEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XvFut1uTZefixZf4YD3mJQCrwCHsqouuFMLhMjSLzx3X1moupDPRl3rRMJywimSI0CiOvS25ef-jxNF_jg16CV548lsw4VF0bf8Pjdk2iWCzpTEDARoEULwdAdYK-MrDnnqNI2xOHuYDkVUO59B_hyxQuKagzOsvaTttX8DUr9B_pCpAzhI43s5ebHc5gRgi9JvaLQ01MlZyx_xzXmo8kkry9sJcA3Vn1QDA9s2u9yelOb6Yj1GjmbgWlH5emxURzwB1iNQACzVD_UEd_CYtDEoTKmcN9nSa9w3Q5qMC3i25Ws2cvRJy9uxrpT0NC6epGih-4VishodEwiEtaCP9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=XvFut1uTZefixZf4YD3mJQCrwCHsqouuFMLhMjSLzx3X1moupDPRl3rRMJywimSI0CiOvS25ef-jxNF_jg16CV548lsw4VF0bf8Pjdk2iWCzpTEDARoEULwdAdYK-MrDnnqNI2xOHuYDkVUO59B_hyxQuKagzOsvaTttX8DUr9B_pCpAzhI43s5ebHc5gRgi9JvaLQ01MlZyx_xzXmo8kkry9sJcA3Vn1QDA9s2u9yelOb6Yj1GjmbgWlH5emxURzwB1iNQACzVD_UEd_CYtDEoTKmcN9nSa9w3Q5qMC3i25Ws2cvRJy9uxrpT0NC6epGih-4VishodEwiEtaCP9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaaLOd1yvNrpEPGZiZt8i7qqtPW_UC2c5zgY3ygfyvQQo0tl0BMIw6U6KI-qaLNgQGiOjOJGzQ9oVggjW9_ThIyWsVSrP_Pa-NnEajiO7oih2S0KVb3NrnR_ruo3x5-Dqmhyj4J_lzt1lDejWhvP0g4fxW4QvImb3c0CrVjqN6--SZ_DGCZyv6iXmhXJUkborn5yO6h1sWJrm8U63bg4yOasV_vTYXuXhQdBmvPsleAmJcy8218TFK8jYswG28M0U1GO5PfBaHUWLcbEmzjglcvVrcxLYplFAAmwsv1Q-1b5QUzur03QcbbqryC2ZcZaerz2ccNsf9GiVthCB4_Jyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=FoO8WE8w360OzkG4Dgc9IApz6LW1axKz92PQSN5exqDd4Ls3X-n8PUOpGTgjx1Fmig4Rse6QY9kpxE8VNf-MX4nBw3geWW2LKQk0RbmJiJZWtvfoC_hczzEp1Lx7yhgbI8v8HdY-88XT5Cy8PD0m6FBnmGsWYDoyaBdHYrZUVJhWC07UIJz3iQsyZx7q4CWBJlI8Q2wDQJ_AtwFRN2xmNfQJqFRi9oYM23Om9lRDRsT3V_Z51vL0ppFjCePI5G1PKZzOEqA-MLtd58N2YYLHP6bIPSqJ77sdgfDhJzsOolxdgPXYhK-49uY-v6j-g_8C8nLygEPmDDT1yQWqcl6b2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=FoO8WE8w360OzkG4Dgc9IApz6LW1axKz92PQSN5exqDd4Ls3X-n8PUOpGTgjx1Fmig4Rse6QY9kpxE8VNf-MX4nBw3geWW2LKQk0RbmJiJZWtvfoC_hczzEp1Lx7yhgbI8v8HdY-88XT5Cy8PD0m6FBnmGsWYDoyaBdHYrZUVJhWC07UIJz3iQsyZx7q4CWBJlI8Q2wDQJ_AtwFRN2xmNfQJqFRi9oYM23Om9lRDRsT3V_Z51vL0ppFjCePI5G1PKZzOEqA-MLtd58N2YYLHP6bIPSqJ77sdgfDhJzsOolxdgPXYhK-49uY-v6j-g_8C8nLygEPmDDT1yQWqcl6b2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrh8HYgDz61cQeWC-jbE5ZdrDMANtF8b-t74ARsoBlC0tZ_lFZwUdbuaoeXri9WuIZcag0y4MKUF-gk5GqZV28xNR9At7i1eHKT84jjL4YiM9zOLybztZB3KPQzOSMqNisCAjLbddwvNXKcHDmUNOFQgj6v-cf5pKfH9BMUZRNhZJsslmteP5GJJ0uTYJq-xDOJ2212-VHMz7sDj8Wo0ubXBx2hplwFWqiFd1v4PtIT-w4gY0qMNru1YJ56NjA38OQxe2Tq_fS0_46nJ0lcIxP_BF4jNcs1-G1TDyNeVpyNgMmBtRKllxT6GPR_CgVYxf2z2nXKrWZCW3_dbXZ7WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVSyOhFQuE0o4yPkGzhfsl5qfguuNyyCfsUUkoQDp2fyj6BK8VFbtZMtkxTJStFz9QUyCeX6G3P59l6P7CPSrMUz3gWT7Ifjw5s34dLqOOuuQsgumSexzrB0P1ZO5aIn2SYtAmk7S8F9-k-JbC9oV22hQk5BJQbM77fxUsZAE5HsLkiuBXAx3cHhxEoxQFGbsdbR7HBvft8aIajnyquR6cFUePcOj3CQFhY_2hV80fO_jZvi30Qg_dxUwDW5wBRB80oO9Xq_-DOaCYvC01zXYEsJmvjKJznoU9i9tg8hW8756fG3JMYLucOH1rp5AiDMm8cRouRxTWl_KGKkU7ukhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=t8P2YW1kCCWbABTHIG47ylZ25-wK0xbHn3Q-HVGwBNDp9j4DuKrVVNNKEWkFC-LJ2mC6DcneAhRL9rQ6jGzZP50YxzkC1kDi2AqLgDT867HjReYPqkd9TchnGX_115hfhEegMXQ6QbLCjPexVIB39PGnOxHo1AlbpkEq6DnSvXOIQ03miBOBma5ANQUqxG09865UmEz6JHpGWmh6NhjNLf7C4QwEQR195j2HSecrzG3UWEv5Sxv9CmQaz0hHmAzJ-fq3Y5hltUYIhRXRo0ovQwn2cIhMxLo9mnjc4EsTez6DdGBJGYhls65YCST2eaHM4lV6EL5LOVs7f1IbdvqeGBIqlKaDt-L-GItF0mAuSYOBKKZwtkNFX0p2KH-pq6Pd1yibdyJGgr8ANBDs4XMEkF_Yppt4chz11yqQaV3_IkSvcsRTcVhN8K74aupUxURLkzrXWHGben9aZRricOyReolud1akgP1gXzoCoqO6Qif5sa-2XmzGxkbEfRENnnHGd-IMkEsXCDjNl5SKxGl1Ew68pcwyrFB2FVv4YViG4sByCfeWFs8kGbgcXrkP9LdCsdWcAo68mvhco_S7mJROJvRHUPh5BxOi5BWAAK_WuP6mirbHTXKrq1XlzgxDji4AilWbYlUDYKlyQlYU2J6aDP_clDrDKI8YUIbFk9mEmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=t8P2YW1kCCWbABTHIG47ylZ25-wK0xbHn3Q-HVGwBNDp9j4DuKrVVNNKEWkFC-LJ2mC6DcneAhRL9rQ6jGzZP50YxzkC1kDi2AqLgDT867HjReYPqkd9TchnGX_115hfhEegMXQ6QbLCjPexVIB39PGnOxHo1AlbpkEq6DnSvXOIQ03miBOBma5ANQUqxG09865UmEz6JHpGWmh6NhjNLf7C4QwEQR195j2HSecrzG3UWEv5Sxv9CmQaz0hHmAzJ-fq3Y5hltUYIhRXRo0ovQwn2cIhMxLo9mnjc4EsTez6DdGBJGYhls65YCST2eaHM4lV6EL5LOVs7f1IbdvqeGBIqlKaDt-L-GItF0mAuSYOBKKZwtkNFX0p2KH-pq6Pd1yibdyJGgr8ANBDs4XMEkF_Yppt4chz11yqQaV3_IkSvcsRTcVhN8K74aupUxURLkzrXWHGben9aZRricOyReolud1akgP1gXzoCoqO6Qif5sa-2XmzGxkbEfRENnnHGd-IMkEsXCDjNl5SKxGl1Ew68pcwyrFB2FVv4YViG4sByCfeWFs8kGbgcXrkP9LdCsdWcAo68mvhco_S7mJROJvRHUPh5BxOi5BWAAK_WuP6mirbHTXKrq1XlzgxDji4AilWbYlUDYKlyQlYU2J6aDP_clDrDKI8YUIbFk9mEmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP6B1uGbEzUeFGyRIthxctQNk6_C8CJCSDgVv4etDhCZ73_3xG6lKZEp40MMNTCUYfT4gZg1Tthz6uDO-46KiPNcR9c8nYXJkrgbKqdF62AzA6fQeoodtyrhIfONDVVSPBuR37Cf-rvZmgBicorpUg-we-25FVV2AM0z_9expolUXOGYMCz-2_59qNDMjyi8vrCaOBQCk4dXqnfkbH65rTKjnqM_oIUaXH3OfZFaDUa39-c46tY1x_VqmtnbG-Fk7CtqlIlazLB8PX1K2Q8MjlRrfUKnSfjIMIWBgsMMIvTZe-u0y14SBcHvw1k-0m02hWOwB2zAjzeBGaMITTKrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6sQPmH67GunxvBf4hPDIqoCTCiiVH-zW3vKgAXujPke8FaSv-bZV033eleSWyBp-BIO3uFZbMXtNQhehHmMTeWYYl3jtAvnRB6x2XnUMrrESRLspW4LRex5GieINjVsQ9YpD_O3L67swVMlJaTzaag0-Scl5GPMt-9Vhr44RnkqJ6xS7hvOyweSjlgJnbfgXB0CqzRdU4Jew-akd2dc0X2X3ceCCXHNF8pWagBelY0UefxxwtiQ1a3tfGnqjNnIE1-Qjdm88Q8A2duH1jUVqbPmGNl8jAsOXZ3S3oSSontAkZyf_Wblxk72hCphxy3bS9KXcpWUyZE2EdM4O9dtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q20ZwjYzf48u8YeuRfqX3JdXnXlzxR3QCOXRo16U25z7lhJkK4UUuMbI5NHieHOmNYYjK2diyZNgxdacZcwxlMZ_JhJDQHm2HxOhLZK0_uX6J5uVgU8rX0Xf3lLXAtmmBNUpPIn5hKsfSqk2xTl0_wkwhGv_2CgG2HoxddtpQNy41vGOmUfvctZ_eg1MVC0fbOvtEaub2i9zNno22cOt7g1cJkWT5uVS_73fqGu__DXyBSByiP6i_3qGCElBPgIqUQa4b4smiW4wJA0bAoxHfRuunpK8woYYHVR1uEVnyORLtUddIwYWYgdy6BDtU1RDbNJlDRlsHFZYdee7Hs3u0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=k0OfFdEzJkK1Ri1zYfFQFlkqo9SLO0FfoncOl5kL5kB_9TCIHtgT_wTwcoX3LQ03qpcs1j88KWvps1F1jySLy2bFvY0J2LE3cNPN2ZVP22R8l32p52VwazPW3mYPwHhNzzJ0j5JEk6ba1uVdmF_0VLBYq_zKKTKo8fRdgU1C57FOmPSUFjDA2QFBikMRNYttwTGhpRgVu5E7cnfFFafGvIPRcpxOgkbzWY2FnKTl1D7IQrHA6su4C2YhC__TncdtuLzcazik_0lgFOjryfYTohqAZzPKX22v207i0ArmqBrTtpSE3jUuOq3Nl2Z6-iG909GjUsW1GdRV3A9R9xTsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=k0OfFdEzJkK1Ri1zYfFQFlkqo9SLO0FfoncOl5kL5kB_9TCIHtgT_wTwcoX3LQ03qpcs1j88KWvps1F1jySLy2bFvY0J2LE3cNPN2ZVP22R8l32p52VwazPW3mYPwHhNzzJ0j5JEk6ba1uVdmF_0VLBYq_zKKTKo8fRdgU1C57FOmPSUFjDA2QFBikMRNYttwTGhpRgVu5E7cnfFFafGvIPRcpxOgkbzWY2FnKTl1D7IQrHA6su4C2YhC__TncdtuLzcazik_0lgFOjryfYTohqAZzPKX22v207i0ArmqBrTtpSE3jUuOq3Nl2Z6-iG909GjUsW1GdRV3A9R9xTsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpLJjbea1dbWUAvlwi6-vudM0EqPqHv2D88_BvGAAlfScSbxM7zjD1zBuTk4LkYXost34vzswqwwgN9h2Og4iwlM1i-huTrd1jpxzm9ah0Ebv1YyFW3XUlIUcyff2MrIdi16dmigciPB6nn4k4qCT84g-n5mQRI4AA_oqscwR5OHcWrgrBRp0kk6Wm32nxb2bjR4SuZAkN3dHKn8NTp8wz74GnVDkUKutmAyshE_6-GmOBAHho4sowUad-YWGdbDBVcLMhL0PxdlZDMXxrtGIWQTl6rcmocf-x0bfM2QHg954WPGqyugM0b0eR0T9JSBLh27SlhuUbkwLyf_DynLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Noxlt099Q4AeP-MdZboxd5MQvGQlP8G5bnlvVXVJknmO8xFh7eckPDq2ISxuXTqRjFlvVGweKW6k5XvBH69MrMU3HlK7toT7gdhO9Za472IcPzX8J4y-l2wbuVRTh8E9mkMqBo5DHYnFCHiBIH8OodCDj64UNWbo6E5SXBLXKveZP9tBvjObI00m1qGbuOe3GyKlQ629fUZ2B-7cgwpXdmWe-EPTxT-UjoTAl20QX5ygNWTnVdEbx6Bdj-5d1i0KuwfySzNleZ8aDmTvUGKUfVCrJJ4CA84eB5sFeHJwt_FA_2e3W3QmHrVtD6zGNcYtZMwQyTg-f65twtvlZlRAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeuk9OiPOaY8jUY90rQyuBd4FKITssurwGqDzX28dNjTg99p6j6P3psVLGt_ZF4x1lLhxiiG5bxo7r8eftXN6lby4pHuywM_ULBsmY3-OrrkKJwnp4MOQMSA4P_IPLgNfpU579s-VjMYWx4uBcUaM9a7As8K1BbCABcCcBeYTMj8JtkiTykUOpi2h5fQMQJjxNOsthlwoitHh8r_JvMIlTcmKExv5Pwx2LNBHfJFPyNVnR1D3SjUpFIHQwYTkWlG1-OPZ-Htc_kIqh8Ah8nd7_SewbjIvSAfJizYCgrxeQOF3N2rEunxbHxtUulRz1v6kNDEhSdEk5NZPi-HR9sUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGrzHyDKSm-t_wepuvar3FJIvbLLvTKTiMnLS5_j-6LGia0JcqWRzIZXIOQShzM4OYj2V0xp8qWw1vV7TDxcCXgxYQ72a8ly59oImpqW7CPWWUHqz9eUPCJj2tT9AWiaTWkV7pilaCMswV6yX-QmzWSEIF52N_SmVxCJMVnvcPX1JDMtAZUgnkdIcTANQLx2xlRRiJT4S72IYj6YprHUDwN9NJHzgLghw3VgzgV6IPQRmDV2soRDLvW-QVCrYqfKzqshoBcs3B0saytYU-1NiSQzyp6OkYieidUDUrsGUCV6LGt7_3OkESk3xGL-y8CoUBtDDrtkAntD4Vkgkfxgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM9ciL1LReOc3rz5PSICtavE4rQu-cx8Ak4fNjKkdJtAufhdcRl1MXdMgpTsHq4naqFdZjJWVcGYKb_21TACt9vS_PjgAGed9ycuERJQ2C0TEuGv_VZXyI4FwhMVVBE2KCDZfy12XaGa5Zc63GoscqkkTiYEDnUaxO2n2UTxommW9Qr2D2MbdLsyrYCw2Fin-R284xFyW4Ckk7J5Q_P2uV8gupOBUa-X_zkva8p8XWKeyIxYCE6rI79XcT5aqdbVDzZ0XnRqTqRyz34Y0QQHKd8AZnoWvf2xFd0LLpRZIXl0ZW__PjurfDSYQFkZCaqTRtLeYJ4TkxfdbKHdjCDW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhjg78hjsUVwAt9QtQyBxABEdVzoxoB5iqR7IW8GAZPOaQVxM0on_f6t93CjaURiBltHfPuP9318I451PI6O_ismdJlxqna0O4UaUFb8I1t2HF_U095a8w38ZF5AOe0JPDiYbUfe-DtIvDDGe3-pQJZG7yOV26752-8HtPDlUQYWLutatcVuXnTXanj0XCORcDIeYX1m5kTzv3Q9pfBMK5RyuqdSkW1bi48OP0ke1divKHElpIH-9krDktv8jGxql8QcEqU2Tgsz_FWSxGmGtqPb71BfhTeOmSBuhX175rMn25jfg98CZhB0X5nmHEQKfzNQUMIFBql4c8a8TTNEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1hLjSxE--0VcdpNBoarmDQpX4aOzTNCljJ4MgUbIubcIH5Znc8RhSFKk7NiZne-GNPcQyVKXC1gGoxfH35OBW1i3r0cq2s7VFPe0I6U06s83QQWFTSVIUiuYh2vMxYR7YB9TDgh0I5aqathRSnjHYDFHU2KRtFAMW5SqqkgMxlcDymyzLm9vh3X2iU6MIOJhD3AH9gCbckhlVq3m-zuUys7xEYqTEzmK8TM5InqWeNC9ELs76sEg_y7Gxz0Zf-zyZJHdXg3QNUMAzCB3tvhNfDKB7Q1G6_YajznRvuYsWNkVjmqFYleQMyh1g5VnbHiyagkEqnPwbbIxSJiQS9Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9tTf0rmirhf1dcsQUDMEWNtyW7YDCUGh-yhYfi8nozDQc9J3i5blz4eTquo5AkQxa-yEct5BrhgmmUc7cxE6QtkS3yhsHxTR6InGYMnCEia6tqq6hjYyhHE2AN-sK1Y665sbF-uCG-G2XS-VchXYnQBHeAtiEjpkRR2D9SWBPi0-YsLLJUOwykdDpaLYzuI_in8cs-m6k9qgZuJHSgWvq6kt6FzPLw2XoWljTXK1gdBMZ8QfTGHvZahaUDMFvvDUk4EfP05YMoJquaYQcUoADbeNg4C6W_-sj1wJzqXTOfobDO4vvrtI4qYY8AJH7FLW-o2QBEMR7BpuJ369D8l7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwm12z0GYnZImUTr8Jjets5F3DkJJciqwIP3R4NuUeqsKBswcUjC-gP44_3h6UilA05HLKx5k8phD7t8FoGgNiu_4DYxMEx14wPaUjVlCzYx9si7RQUs-vboqXkTSk2ORa49aemZZ2VdGwDayGpMHL_wZuw090ppOnR9I77lorvS-5ORIQQ0oqVklHtRDuLYj_LXITMhmv5eM32W-jqDreTSYHrPBSjDxZP0bGw52x961TeqrUOvGPtStFC5lM9xjhy4TbswW0ZQp6XQQ4SHruKcEPivPHI_naa2QtpF8v_0Yz0x_M1bVyAazEUiWpwV7g_s2VihWaekRbBVckGn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKBXXab30MXf_XnYp10q4aZWjUZXCm-gHtYZF25QaUO0ys6fx7jrM7gflsWpGms2Z224VUax0-IsvvFdHheXHmcZt8dk1w2QYzWkD_hOEil0Y0_vz7SBVfw5L3XJuTMBjJi3fF-MHG0ad1mjPE6C8MZkDmff6p_ER2ZAaVJN59ghRbIQj9bF4y8hwqyOFpG4jsE51LjjFO4ebuY9Q7d6vKiWwwl8MnqniayPWwTlfqs22Mx2BZltIg1s67ytZbAlL2w8e0mT6tvUadJ6C4E68gQt-Nwacs18ntEw6A2k-HBhgQBSbIAjjjKYMp-CJPYJwsVyLWYzjPsBUbfHrblyjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=hOkx-ljPJ50B9NTTbU1Qdy1YWDFuU-0zVJz2W9HGdVTsnY47GOlk-_iA8JEwDRpukzY2iSmm9OHc0kB_-SWr-eSQ1PHA0X4c6lJ0rJ1xYgcDmJab4OgDa9lcDkDji_6jZpiL0wqdA4iOXfcoaW1bFtYSZVkrIOXET7wZd8c3OECrXRHxHuT0LMw4oNCFkF1_V6TbZcyW20LFqLgx2rVwM6er_Ofp_HgcsNBTcanKuZnqA-eCpcbq7rdHdii2el2V0r84TKuJj_uc6CVi5HcpBedqtTF95p-e84DfMOsPatXNI7vtIOpnTvTvkrqGNRVY6i5nKb55nQBoz5MS1L7GVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=hOkx-ljPJ50B9NTTbU1Qdy1YWDFuU-0zVJz2W9HGdVTsnY47GOlk-_iA8JEwDRpukzY2iSmm9OHc0kB_-SWr-eSQ1PHA0X4c6lJ0rJ1xYgcDmJab4OgDa9lcDkDji_6jZpiL0wqdA4iOXfcoaW1bFtYSZVkrIOXET7wZd8c3OECrXRHxHuT0LMw4oNCFkF1_V6TbZcyW20LFqLgx2rVwM6er_Ofp_HgcsNBTcanKuZnqA-eCpcbq7rdHdii2el2V0r84TKuJj_uc6CVi5HcpBedqtTF95p-e84DfMOsPatXNI7vtIOpnTvTvkrqGNRVY6i5nKb55nQBoz5MS1L7GVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=AiZ2kVO4Yt6qc5ntsN6PgozaFt85kdt7w1sml6VIMPmtuxl62I5Zs4V7Nw9auN5arJ_HLfPIIY5QD3GbMpZZYe9Nx5vehYsvbCbgWzS7UVRXeZ7pi16REnt-ccIb_4mnQgycmhFyC6cHeAQ2IW7jMCofkWodpaeT37ijSfAgevx1Wejks6eqq8kaxnApnbXm-Nix6o_VaEGUbWXt0Bz56STI3BTKHks-aTbSvjbTjltcjcG2Clwncuo8DkZxIqLwmaJhY8XE9howi2f09zHKAbrG32HDvdE0zDNcvW9vGGKGQx8-pW_eCtSGF4vYXEIGq13_SwDwkuY3lo_i8TluUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=AiZ2kVO4Yt6qc5ntsN6PgozaFt85kdt7w1sml6VIMPmtuxl62I5Zs4V7Nw9auN5arJ_HLfPIIY5QD3GbMpZZYe9Nx5vehYsvbCbgWzS7UVRXeZ7pi16REnt-ccIb_4mnQgycmhFyC6cHeAQ2IW7jMCofkWodpaeT37ijSfAgevx1Wejks6eqq8kaxnApnbXm-Nix6o_VaEGUbWXt0Bz56STI3BTKHks-aTbSvjbTjltcjcG2Clwncuo8DkZxIqLwmaJhY8XE9howi2f09zHKAbrG32HDvdE0zDNcvW9vGGKGQx8-pW_eCtSGF4vYXEIGq13_SwDwkuY3lo_i8TluUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSRP3XZ5goGF5iCoEHh_McuvAAFJlZCid4F7pymG3M0amlPePv2dkB3Wt3AYoZWqsvepHEdJi9cFUwijh0cKLQxo34snIo-y9Od2ij3aZancjnRs8raUsqX5vLfgNIsGY8k3ITGeIBjM5jW13iu248jphoqFOmxmgH6J1tDa6N_yiaNBMJaec5gbhGptJ2MnVX8zPzahXwW5_506OS_zy4TzbDcY3vQQ_2jUPXPE5RJXmC-8wjfoDcHtPaBZaPPpCf696PSLBWxDtMTmm8_xQwPLdtRg5PaVQL9xVe9s9NmhC72m_3K0e5IOzlia6hrbkTsfjpKtnBSZQSJNSi983Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Og72AXVCa3BI6LmvsRhB1LBITUqQC88jgQCOE6Tkfs1arq9jcl79PiR0Ryr6XTEaHPgcTCnuORJtV9tqrnFgeJpRv7t3mdsxDtUfKzlBIGo1zwiwws5Bn0M6WA14_GWv7b2cip-GT8kiYLhtBHHgxWktAgqEpVjp1Rv9NUF0jGrEaoKNEu69irn_RX9zVEZl05D--WWozZU_KkABKPQvp5c_99U2XRHhg0E6lo8PM2Lw1fnbpLczh_OGRDvqTx3mLHMjBqEgcRMVzs9eLTxJhb9rBtvIotgFYj_EBIWNPVA7sKA3FYVUPHpdVoOQR7bK7I0g-LmW7WQrKdZtCoCrFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGdSq1Fd5aVMd5ESnQ6575_UWfaZW7O4TlaOIkRd2ZpLhPFpUtbepEL35DnJnq_1hhIBqna6dr29MRifikWAY_6xMf801ug28nowhRQg1fG4hgSjuY81g2b1Hxn3OWAvfCPWMO8nRXosQ_tp2m3HrdEb_WoTaJKOalz-kCBXz5oIf4Qkbq1qesF6pt77JcshoDFvrS6GTEAGmi_f4oDFZA2FVk3S3bkuaFrPTJHwYBlV45s7PnBg1PmQ4IFK5KAuLYV0RxqACICnM6J_vq6W6JV6njiO8hnFUdj_qh1tuNj6Uk5owjY_S7Js8WfDBWqy4rwxrbm3Hp8Cxdm0Km93xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lQoIxz4VKrbtLh5x8nazT1KVPS4CNermoXG1LKelYCa39ruDAlbnV7EKgqOSHoSTpmDhNQfzjdWCwPo77311lM_T3TCnq_vTgpWM8LvblipGpChmxULTNuWM7aUhrPwmBgEJfXtxtsAS36a7ADYNLPi7SYssSsu0unxlXyDiT01wVZUEv2uaH9Be-vAeFyv-R5HG6BEw3zN437c1y0AucC-kzZKRqhjVrXb-UYXeQvUkj-owiXm9gcxpWO1HMe43k6C-MAdxnfnCzH6rSeMHOO1iGEE4wjrH5j-kYD5o1RaveyTiXb8PR0XZ7iRpPERPDzLqutUX6oqnxLw3eyGC0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=EggTrDRvJ3VcBgef6OaBDyOK0j4x_Pq4LoS3j_pVPDeVvI1ezG3WYXFJwnM58w1wm1tp1KEs_eXfxo8piLZGLc5NsLsGa1-zSN6dfkvzbDXKLHBtT3FU38u9CTFQB7RomhXjG5qF11jB6ps9gd9te4QEMmHQSTdDGX-zKWD0gHuFMU2Ff3A_64jkdKpl1zxj2HGjX0_kwMLJ6QEal7tosMOsZqbvSgC44b_e2EpXyOYVgvqopB26Rz_pvVBaXUg-koi6z0r6zuovnoxG-aqeRcNfYu56Yd6d0BlEVYcHJv74xAy-k728rKOtUXYRbjzcTSkeVnvjwsVxti4cJHO7lQoIxz4VKrbtLh5x8nazT1KVPS4CNermoXG1LKelYCa39ruDAlbnV7EKgqOSHoSTpmDhNQfzjdWCwPo77311lM_T3TCnq_vTgpWM8LvblipGpChmxULTNuWM7aUhrPwmBgEJfXtxtsAS36a7ADYNLPi7SYssSsu0unxlXyDiT01wVZUEv2uaH9Be-vAeFyv-R5HG6BEw3zN437c1y0AucC-kzZKRqhjVrXb-UYXeQvUkj-owiXm9gcxpWO1HMe43k6C-MAdxnfnCzH6rSeMHOO1iGEE4wjrH5j-kYD5o1RaveyTiXb8PR0XZ7iRpPERPDzLqutUX6oqnxLw3eyGC0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=kBcdPYA8TPil_OcSS2XpLsvGZOsTeYA7DGGOn976H3bONyPw5akx9nCTO14QpV2MfxNoR1BfGcqVLhabWuuhjJqtKNHDj0R2XyHxU3YgtHLqx6KFfFXFVX0fp63tObn4MHCZW-mayeGZPTXpOJDJ7HSBvUjlgS54Qx5gyk4_UhofSNlHq6X-ENCoKnZGkbcWmt4UWy3RTo8nBDUJiYdP47QBi4vlXrUjIoofSaiR9-yZ6vgunwLd6s9eaiQWudleKVlqBckcwSPpS7X0TItkoi7FZNrX13CaguyXgbaWkfCbhGWUzZuS_PCP5la7JYTrxBX1zISOZMMs0e32itj85YFLtBRDaqOwLFtDYtO-PjYnCV7X1HmWDzOKbz2brhl8G9XAcV1mblHuYmTuq807OMdW9dj1bcasV7TLYf9QUbRoNsefLKucTjkwoQPWF1LVroqaXmeOuWJ1-ZO3e_uzueiznbN2rlKkXu9PyhVSxqKzcwOujV_QsC65owdGRKax8FRjjKHZ_VrFK9zcXGzm10ZJNGfO1RLLOVjueLFeXnqVEE-JmZVQG9W2OqLXNp4oeWEfiAN-bXZpFzS-UTd4dljC6Zra4rUWvtzCgCIMT4_PisHK10ie75CylPWLekZDsjofcuBTDuwU9Fl_4KyiGH749z1iQL6kvbGXFSQbZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=kBcdPYA8TPil_OcSS2XpLsvGZOsTeYA7DGGOn976H3bONyPw5akx9nCTO14QpV2MfxNoR1BfGcqVLhabWuuhjJqtKNHDj0R2XyHxU3YgtHLqx6KFfFXFVX0fp63tObn4MHCZW-mayeGZPTXpOJDJ7HSBvUjlgS54Qx5gyk4_UhofSNlHq6X-ENCoKnZGkbcWmt4UWy3RTo8nBDUJiYdP47QBi4vlXrUjIoofSaiR9-yZ6vgunwLd6s9eaiQWudleKVlqBckcwSPpS7X0TItkoi7FZNrX13CaguyXgbaWkfCbhGWUzZuS_PCP5la7JYTrxBX1zISOZMMs0e32itj85YFLtBRDaqOwLFtDYtO-PjYnCV7X1HmWDzOKbz2brhl8G9XAcV1mblHuYmTuq807OMdW9dj1bcasV7TLYf9QUbRoNsefLKucTjkwoQPWF1LVroqaXmeOuWJ1-ZO3e_uzueiznbN2rlKkXu9PyhVSxqKzcwOujV_QsC65owdGRKax8FRjjKHZ_VrFK9zcXGzm10ZJNGfO1RLLOVjueLFeXnqVEE-JmZVQG9W2OqLXNp4oeWEfiAN-bXZpFzS-UTd4dljC6Zra4rUWvtzCgCIMT4_PisHK10ie75CylPWLekZDsjofcuBTDuwU9Fl_4KyiGH749z1iQL6kvbGXFSQbZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olw2IWzCe6jlXsBL_INRvFty7SlOeZhk5nvhot6RTeVb1qzOZXYPWcL6T6iJkq098dViXcLtXUywl0YYc11lZtMrxKtfLXTj5T_4hA1imvtVBgWmyVo8i4BqY4frHyVrVAHE0pheLWGC7NkOccnRQ1FI3wS33XMOwVOodJwwam3A5xDIv8EaXOUOvPXyJA8BrTnINGDgkpJ45HHS5IOz43_W2rlebBjqhoN90jiDCf3P3H8YLGqukPLxweDTOgGsVA0kT996RAfqzywmD71rppM45RkLFmXfc0frDUt0KS010ucZohzqT26Q6zd2q2OKW5cP60Uu4SffjlQX9H4obA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wff1JqFNGUKfW2baXPDIzPqhzLZdrchuSpSGyjYO3ZghJDUU_EEJRAMpjXuSyPkbXzm5qLZQ_i6G5Ujq2vTH_Rnv7098KxVQYEwtFpk1_hNyNR9zqnhuaqBxoNmp1B99BTIEm7d5DsjGkIPNBHkxRtTEDjXQPyfSZssABz0pD1b0R-AppvMnZJmWDETLdyu6Ija3uuzr3T63p0MuRyXCnkmOnDyCMsvpLdvw4KIYO3jGreqlJnA0YQV1IBOHbbmhaktmRziP06gpt8wNzzMIU53SquMN-hp4qe7EaoxW2SdW15dhv8IIkAxgK6MdvejDu_3b-lgPfp7EDrLAhcoXYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFgTxnXltmev0mNMseI3mxRgnlGbx31Qlf7SL14C0lohy7WAGWZSkja8ArSGAM18QFqnZEuRQzWS8WLrKkSMGmo99Tshgavu_szwN1ReuKs8DdRbZeBxyDAGiG7-PSiIDCYrwvjnmOPYKTSy81oLk05Az84VbYUzUKg-KRuYZq6ESFXuIHqC3zdCFf-rVGFCu2kqJjDKFN4IfGlgOze1J3O5AZmjuHu1TSrBcp78jzQ75F2q0uUi42rAQDnDsw__IyrcGc6ftCHbb_mYIgKTFcwQqi40mEMuxhKQvxA3r-88nvoJ_DCWFLosFVoy3_-gqLgSH26n23X4QKogJDBNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=eS7kdYeEx0TObaCH0NGbraC4znPOEjXd7YoXtGCqkdzZRsmga0npFxH8fOrTcpzY--aJajKwuqbZ3l246rzwKGrM7oTwSxrtBnejb6smXn9Ky2wB2GrC312mMLUahqpH4E-o4ll8QlTf7tm2i3a3S6odSN4mOGzhQ6Ogwb62bIjtADV4IB9BoqisfeX5xjpf9trcJO_FErTHFaxkMkv3ekf4shxWidhA2lhJDwHZTJ5FklrZbjuT4OENUFh5TWIVg-6rsEdnKlvT7JStt38DWXXuZAr8eQkjh9enOF2-lUpTxBeDm_vTk8SSZEU161-kQXwX6zFtASA13-KSLBRF2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=eS7kdYeEx0TObaCH0NGbraC4znPOEjXd7YoXtGCqkdzZRsmga0npFxH8fOrTcpzY--aJajKwuqbZ3l246rzwKGrM7oTwSxrtBnejb6smXn9Ky2wB2GrC312mMLUahqpH4E-o4ll8QlTf7tm2i3a3S6odSN4mOGzhQ6Ogwb62bIjtADV4IB9BoqisfeX5xjpf9trcJO_FErTHFaxkMkv3ekf4shxWidhA2lhJDwHZTJ5FklrZbjuT4OENUFh5TWIVg-6rsEdnKlvT7JStt38DWXXuZAr8eQkjh9enOF2-lUpTxBeDm_vTk8SSZEU161-kQXwX6zFtASA13-KSLBRF2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DabO33xJJaNQBcfvxaSsDGDsvKJhOXnxxF_Sv56YNEAP0EzZ7CXNRnuvUveY7dpmvLY5xSAM_2uURwI4AjiZWZ2XX3vlIbNE-opn9DNITrAhuE1VXMLdgH6jKeq3hrggtpJgxsGb_xyln2lPSAtR7LAAgsDWwNQJP9yZpu4OQhaBkqIDnAhKuTmZU6Iebz0RH8nTT7BeWnI6dj-9fZQncMbfjpHk4Wt0UP_mOlO9jqHh0EQMpsnyf4cFcJ1ZfhM_t44ekWSmhdxUU7tVSwnZDHkAm-Tzu88CdSRkxHE858tox5LMSg2jdbiAZ2hcaBV2vY2m3UFo1FRmVO7eJ6A2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EZeTzMYFLg_6ibTPxk3HzdOKMZWpqu01eZZyLPiPj6JtKc7UmQOgHjVa8IkjDE84iuDdVQrbVXA2js3D2DnpD4RW4H2nIXG3CJ9N-1ndzrR8StOUZnYJjx09QRSbcJQ5tMU6E77FMuR3Jv9ZAioXPs___iEN2p4NTcEb3Dfp7WM2Xj9cTEQTBu8MFnsoA8gBB8q1retoLdCnjmIyKp1PZHJR9CLZKDvjxs9OsSsQEVqfPNaWASDyeUosluJR4KhvCzoQrFMnnl3N0Bz-mvvAF-M1jbcQl88A3MaZUy7WkIXvq8CkQMd9H3mLAbWd4FCjdMpQJJ0sXFZHVAeop4emxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=EZeTzMYFLg_6ibTPxk3HzdOKMZWpqu01eZZyLPiPj6JtKc7UmQOgHjVa8IkjDE84iuDdVQrbVXA2js3D2DnpD4RW4H2nIXG3CJ9N-1ndzrR8StOUZnYJjx09QRSbcJQ5tMU6E77FMuR3Jv9ZAioXPs___iEN2p4NTcEb3Dfp7WM2Xj9cTEQTBu8MFnsoA8gBB8q1retoLdCnjmIyKp1PZHJR9CLZKDvjxs9OsSsQEVqfPNaWASDyeUosluJR4KhvCzoQrFMnnl3N0Bz-mvvAF-M1jbcQl88A3MaZUy7WkIXvq8CkQMd9H3mLAbWd4FCjdMpQJJ0sXFZHVAeop4emxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH6GhmHm5N0l_7ILWsX-WhdsEiU0vzlflAbrSfavrKXQ1Y-ibiOkQfeShbQv8zguSWnkCWjQii91ciZ-j8UlQDU_jjt63kPRq2PSJUib_JnZfGULUw7MEo5TrdoShjijfgK7DQXlPG7Vd5WP0SkgayLWRbnY14Qh4JyPVaOH6NluKdpNFDKLtaXudyQszCpRne7CgWTyCSdVRQCR9Btshs5zL6eN2LCQLCYH5trGMb_pImAwt9FozbkI4U-_23d-TsfW-UchuqlmlRPPeQu-M-sX5mbN2Q8ZXixvvu1lzJGU3-HFPmR_ofQiLWxq8lU5AzcY9FR8BTseq8RCFpgakQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKHZwS-TV92YFglHORjEwd5XB9-XTdD9K-XZ7QDh_3EggINJS8EfOmI-vzt1vv_JD7EQqgdu5Cx_BZQKexS33EQQdo1O5BDnZnh0hR3e9imLyOIpbWtct91qaac9_5YxuYpebvYw_4Di7CBxRZTI--V7O7IOIKegQXZ-xZiiOLbB-Ax2rNj9p1bGVo2s9o4VwuKEWP1_5-uEWSVBbRd0HaTUhTuK0RsEV1c0WZY6XJbkZdTBRHdHVPsulOXNyOo_jWVFA9_8Bz3w20jNVjfQpnSpue14Dw6vzjBw_q9oYMfgAJ_ybrw20azUXesnhenklj6pMXYeLudmn7YhIEGwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=fnSoTBjDiXCS71jnXPcbV5fLzeocZ5VxAhgBIDnTDdCHPS4szb3Pd31lo6sEijRQeTy0GMhiuYSndKgi8KfRvkN1qBnNyaRJ-AF73F9I6Svv1A4eogUmtVGT3G1hBy6IbVZSF9t4DfH1gYTzKujmO00thVqlDodHOF3K7WlQrn20gPwIszHvjR61eac41qgbq_HFIqiFdh1f4mvHdXqViWVs1hFXB-2i__4OCuczNQ7MQPGLg77e9sJCT9LrA-Xpw9zByUnylQ2rQEjUz41rOrtBUHKuR1ud0CB8wtvxo-c0U6KB0yNac00H-LdWbnDXujr2h2ft6ReHMOGJim53lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=fnSoTBjDiXCS71jnXPcbV5fLzeocZ5VxAhgBIDnTDdCHPS4szb3Pd31lo6sEijRQeTy0GMhiuYSndKgi8KfRvkN1qBnNyaRJ-AF73F9I6Svv1A4eogUmtVGT3G1hBy6IbVZSF9t4DfH1gYTzKujmO00thVqlDodHOF3K7WlQrn20gPwIszHvjR61eac41qgbq_HFIqiFdh1f4mvHdXqViWVs1hFXB-2i__4OCuczNQ7MQPGLg77e9sJCT9LrA-Xpw9zByUnylQ2rQEjUz41rOrtBUHKuR1ud0CB8wtvxo-c0U6KB0yNac00H-LdWbnDXujr2h2ft6ReHMOGJim53lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=CwQGOyz8aeqf8TkiOXCURZ06nqTVz-1m6VK1tda44Ou2Jwa2n-Hji-7pWgaw5V4ecnoc5M2V_5qzFdfYR_ZKGRMIHCWJa6Bgvp_XPVmPqUDdn4rCOAOfvvcbdck4BgnR3XKsRdQJu6zxXJwIOFawHskNra8snVHPxAAy6Dt35RVtPVXNvmZr4N_6MURPZ7WqXsU1oiblIqqIuhwKthk4C33h51P8GEB-RDs0cW3iywfwGvJQk67QXkUxpXyqULGvz0PuEK-J-IraBmrwqzbpSNwxMA4fKiKnM_zVADk-qYf-Uj3AFAGS5ECIV-_iVfkZtqaKI77nhehn-2_QPdLm4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=CwQGOyz8aeqf8TkiOXCURZ06nqTVz-1m6VK1tda44Ou2Jwa2n-Hji-7pWgaw5V4ecnoc5M2V_5qzFdfYR_ZKGRMIHCWJa6Bgvp_XPVmPqUDdn4rCOAOfvvcbdck4BgnR3XKsRdQJu6zxXJwIOFawHskNra8snVHPxAAy6Dt35RVtPVXNvmZr4N_6MURPZ7WqXsU1oiblIqqIuhwKthk4C33h51P8GEB-RDs0cW3iywfwGvJQk67QXkUxpXyqULGvz0PuEK-J-IraBmrwqzbpSNwxMA4fKiKnM_zVADk-qYf-Uj3AFAGS5ECIV-_iVfkZtqaKI77nhehn-2_QPdLm4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=PQjwy-NfZFK_ySjdjG7a_QfwH4oXI97XTLn1u6Qvozsugicdt6tMJY972AXwfjh67aAZQVJONL6eti2AD95atRXi25XQ3IoGxfrFef9xDQQA4o_-zIhCf9VO7Dpytopz9AZCeTiSxKM5wTX2OgXSWRpBGrZuGW0_gHdbM7M5sgDKUWN2zkEKjQFJNh9hWRNpUSDE0WRVvbz_Su07YnGoUfGSodHPWONPmog3c2uG_yCmUcK5H0czPqGB4Xx-aoxN2B8hHZvPNkJUElsjvlv99IAc8MS-12aL-4llQOAj3qyrmWb7dobs9pFima3cmwscEz3llpBx9NPb3dVdw2DYPhmRUK3eDBZZEuQKKyuQ5Tig2faRk-hXIDftpeAiLcjeaewydxzNZpmK5D_uArCQE1Sfc1K7uGbeHzxIgFGaVzxGJ2tHvQrTgryWZU2t0QFbW9j2dn69PWeI5tXpamj6ZoUN5-cvK2E0PFbn6j5dZCAp7fYVq_wpHEe9GkvfJjLWLFpz7WlKhwkCHwI5EFWwQRyOFVsY5_z-B6-UGIwP1dwDhjjHOk9iDOpyLL1IUgphPMcyRx342-u9jni-Il2pF1rOP45HrlGYi9uRA45xIrwu92c40y6icjo_FxzeBD3ehXYWMBWUWnE7WGL3yF7IpNiAwIJlwROjBeJpTzSCrHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=PQjwy-NfZFK_ySjdjG7a_QfwH4oXI97XTLn1u6Qvozsugicdt6tMJY972AXwfjh67aAZQVJONL6eti2AD95atRXi25XQ3IoGxfrFef9xDQQA4o_-zIhCf9VO7Dpytopz9AZCeTiSxKM5wTX2OgXSWRpBGrZuGW0_gHdbM7M5sgDKUWN2zkEKjQFJNh9hWRNpUSDE0WRVvbz_Su07YnGoUfGSodHPWONPmog3c2uG_yCmUcK5H0czPqGB4Xx-aoxN2B8hHZvPNkJUElsjvlv99IAc8MS-12aL-4llQOAj3qyrmWb7dobs9pFima3cmwscEz3llpBx9NPb3dVdw2DYPhmRUK3eDBZZEuQKKyuQ5Tig2faRk-hXIDftpeAiLcjeaewydxzNZpmK5D_uArCQE1Sfc1K7uGbeHzxIgFGaVzxGJ2tHvQrTgryWZU2t0QFbW9j2dn69PWeI5tXpamj6ZoUN5-cvK2E0PFbn6j5dZCAp7fYVq_wpHEe9GkvfJjLWLFpz7WlKhwkCHwI5EFWwQRyOFVsY5_z-B6-UGIwP1dwDhjjHOk9iDOpyLL1IUgphPMcyRx342-u9jni-Il2pF1rOP45HrlGYi9uRA45xIrwu92c40y6icjo_FxzeBD3ehXYWMBWUWnE7WGL3yF7IpNiAwIJlwROjBeJpTzSCrHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkUPonf8-mjENeOOYyzRanvC6kYSJYFfBCXpaFmPGFQBbiy1KQb--z0QvogG4bTrUfHa_urmQIO7yn3NI3zoHWv52-gtHS0MRsS1i9-KqDHskVxJQf8VXbJteXdhyMib2zkX7eI2jClySsvgriN-VCD5V_YlkdsYnUYIZH7-hM2cMriK-LZVgLbf-aSrlrCov0RZkxRDBx7DtL5cZIROOzxKWmwlPXollP-BaK_gq7RmtE9pCO6M2DwxdWMEXsp0B43OBxsIsYa7ZuJNsokuAkAo_okNmv_ixstXfDXDaoNPJN0mui562e30S-2ZD4MwI4VxXsoKASMm4i7playJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGvgj4DCfTPww9AyG5Ia8nw4P6ntoN_GsB9Ekh3FV1YlpHKLUZ2XtGI4zsriTiXo4nHEkuJTQJ9ev8CIoC5aZ3agv0Z-298t72xcSwG0lT5jL_AmyQuEgp7-fopTjvL6aLS1Zf4pLvIE-1RrbB3BjgvpL6e0Ewtb9XIgFhs6fe_RWU-3hy0cpCxzXH0vsjc65pTsZDp9uay3ZN-bGfcspoQJSdQGPB8ANI44rFRitqRwSr9y1nuO2UpXkVTfmzp-uNZ9sUiTg9NCVf997ufvD4rvrJMbtpDgXTzQY26hlluzJF2gRDjbC-PQZVshc5YmwaC6a5x35gUtAlkwNdVixA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaAoN-TqezoBAqBr3O42pSQTJfDaKkv1x3FJZWcTbnivPgvfno8khUulTdoS9sA9vBGEktOuqGwxgfGXKx5qdTfWXVeSmsTVc8MMQaSZ7vMDJhkxnmzn4XUNy8Vl_KhqUrcUfSLDz-LL-tmi4F1VIVSCma9zRXHYkVE9WAjUYN8k-EQo7ecUZfZC5I9xll1Z4lr2urAEOUOmj2gzC-ab-dBOHc0hKlDF0n5ABvU7YVVl6V91c5t3gD5aeWuVqN2huc5eLnswnziJi8p0vWXZ9xJ9zi-83yyx44-4qw8eXlhxrFXcyNTqdc7G6c8YE4Wpr0GMzIaOF4S5hSys5EvSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=QB3xI7pBf5YojPdYgws-5Xvc4SMS8he-HHGRd1ar0O6P1GZf0xVMBgDpoocv_b8eRrvdJ0Rd2c6nPZTmrE0g7brB2LrlaEDiI2NqiuJTxJYmXn17Cc3AFpXFSg6lAvRs5rVT6DIiT1qNXmaZZPM_WV5ccvdleNvBBB_nJituIWPQxIkJviyqN80onygisOduVM6CMZC3Aa1MrtbnxoUraUgCFdq77NEvkqIoySMiOF6jsuRcCLsKOLxMitKxQ04HeijYO746l8p2amVNnxkxWX8dR4sYmiRajjjgh7AnZDLQQ_vfG8ZgnE6RqSbqPbuL4GhQcvlb-lXROKu9SikSLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=QB3xI7pBf5YojPdYgws-5Xvc4SMS8he-HHGRd1ar0O6P1GZf0xVMBgDpoocv_b8eRrvdJ0Rd2c6nPZTmrE0g7brB2LrlaEDiI2NqiuJTxJYmXn17Cc3AFpXFSg6lAvRs5rVT6DIiT1qNXmaZZPM_WV5ccvdleNvBBB_nJituIWPQxIkJviyqN80onygisOduVM6CMZC3Aa1MrtbnxoUraUgCFdq77NEvkqIoySMiOF6jsuRcCLsKOLxMitKxQ04HeijYO746l8p2amVNnxkxWX8dR4sYmiRajjjgh7AnZDLQQ_vfG8ZgnE6RqSbqPbuL4GhQcvlb-lXROKu9SikSLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=S5gagAmKZ4WQErpgP-yK6KHbZC74M8nTCcDGGzELmWPmQpLM1JXAaKWolvzJqKY7ejTmVc5DhElXBcfimeG-fEMZw1UXRer3YXYlrmKQV-bQlJO5Fvfu6_AjNVO2BCIRIOR_baB-VX3DrdL-e7fup-MYiGhPu_XDdPXw6MAN1i3hxIzdNFL2w3lqXEvQuY1gDjQzTfOWvC63zVO1T9nj_d_yAW1NZfhVX2IP0RfXoL7UK5FxmgtP3TMm-FdFJ3a_xYuOIL-jU9H8XrwkSCSt86fHJkMmWrP3ME2aPatOdDG9L6W6rqAhB7F3j9bFJxfIyyDZg3vTuFsoAWnLVVx_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=S5gagAmKZ4WQErpgP-yK6KHbZC74M8nTCcDGGzELmWPmQpLM1JXAaKWolvzJqKY7ejTmVc5DhElXBcfimeG-fEMZw1UXRer3YXYlrmKQV-bQlJO5Fvfu6_AjNVO2BCIRIOR_baB-VX3DrdL-e7fup-MYiGhPu_XDdPXw6MAN1i3hxIzdNFL2w3lqXEvQuY1gDjQzTfOWvC63zVO1T9nj_d_yAW1NZfhVX2IP0RfXoL7UK5FxmgtP3TMm-FdFJ3a_xYuOIL-jU9H8XrwkSCSt86fHJkMmWrP3ME2aPatOdDG9L6W6rqAhB7F3j9bFJxfIyyDZg3vTuFsoAWnLVVx_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=oaiMZQmuGbepS_Yih3qAz3AIOzlhxepwzo1POwqa44ZTEE9ynV_Xd72NXygRiwHTxCsDFtxRm3x0Dtp0COt1p1TkSK_6qpiQEga84a2CgDddImKgitLcqa8o0HgASwOoSC6qtTQTiJgUvUi_-BZWBqJCvR9OM3kTSAw8X-0zNcwNwL-88AjrDSfgeExLhxBSAxJXwrvfBJ5h4O3R3dfoUkFqUT5E1gq76IappF9PGy3ntelnsu4WaZXI-bHVVGmpsNIO97pJ5Zr_cRZQD_rphPicGH2MDGt1CK6XTmBO9b-bCzNHr3bS8xrQ5FuiNOUm34bhuxZk_9tNH23tBUR6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=oaiMZQmuGbepS_Yih3qAz3AIOzlhxepwzo1POwqa44ZTEE9ynV_Xd72NXygRiwHTxCsDFtxRm3x0Dtp0COt1p1TkSK_6qpiQEga84a2CgDddImKgitLcqa8o0HgASwOoSC6qtTQTiJgUvUi_-BZWBqJCvR9OM3kTSAw8X-0zNcwNwL-88AjrDSfgeExLhxBSAxJXwrvfBJ5h4O3R3dfoUkFqUT5E1gq76IappF9PGy3ntelnsu4WaZXI-bHVVGmpsNIO97pJ5Zr_cRZQD_rphPicGH2MDGt1CK6XTmBO9b-bCzNHr3bS8xrQ5FuiNOUm34bhuxZk_9tNH23tBUR6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=dwu8EhuUrbzEwg9RHpOOcPjFuWCn6rruelnPfChX3zcFjWeGl5mMKeFyV4z9AomUpwr5wOKKx45UnIW9-WvCAfbSugBA8itxG3XiexDKt1V-NicWYezKtRcg_0C6OXMxCvArN-4coWkWxZStQPS9xpb5tKkEH_mFhcp73Hj8K5jG3cgD5RkMN0WSFRup-yuGQmAENtXXBpirfYoDcuRoi84MzMcrjncEQYX4-DIx-Wm_tH-feNLsh8jobE5RCOqtiGeH5b6mFG7SA0A_QEJDmkqxx6MVRRcxIjNRUwWefGgML3VIPH6_elychey2_Ab6OrQWrYT7iVk_9TAnHXUTLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=dwu8EhuUrbzEwg9RHpOOcPjFuWCn6rruelnPfChX3zcFjWeGl5mMKeFyV4z9AomUpwr5wOKKx45UnIW9-WvCAfbSugBA8itxG3XiexDKt1V-NicWYezKtRcg_0C6OXMxCvArN-4coWkWxZStQPS9xpb5tKkEH_mFhcp73Hj8K5jG3cgD5RkMN0WSFRup-yuGQmAENtXXBpirfYoDcuRoi84MzMcrjncEQYX4-DIx-Wm_tH-feNLsh8jobE5RCOqtiGeH5b6mFG7SA0A_QEJDmkqxx6MVRRcxIjNRUwWefGgML3VIPH6_elychey2_Ab6OrQWrYT7iVk_9TAnHXUTLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIHGvAvNKKN7G2-EgYqSVLeQWVpuqFaRgpWa7U4uFyfeTa_rCF_31RjazYLrDmVWqUkW8qRG4jA5XNNiyDxsXcJ1e5EH1vS0XMp7sCsOLrSAi_9k1tTuh2vW8EnPwzqYacpJzV3Wn6ZDhpcdMvKemJB9p3cDEe3xXy-gVc0ihhg3Pm5k_VTV9XUblDrM2VMNfdG9gheD2QuMcMJkpNB_gs4c1YH0QZtaqTcnqTQIF89_bNExz0J8XD3F2ynILyqUUkCeRy1_JOxSgspOS6yCfm5fjVdgyAmaYX76q5O9HIf5GiL934mBZ75BhuP0ZwE3r1xVxZSSjLNh0cuC4Bxe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=o63hZPbJp09h6afI2zFxAP_XEAxQ7GbziYQ_6FFsZxR1EbF4vZdITkkjdRaOg96_9ErT22p80Wj1bpuajqpBXVM2UM5H_F6W3opRM48Fl1odqulDhv2gFzIYGvbxEApkU0rnRkrIzi4VVSISRMb0Ux1bPSwIdGfZHZgtSZQUZ6-VG83WRl-ne1yygi2NvEayg1C-phQjQcUykAzlQXAQ3Dq5hZ8bUS10ZsgRXid15AZ8MdfTxUPWpEXk8B495cR0PdRJYNnasORJiJQ5nAxzyUjjrniY87RrIBMcTJT-GYsjBXxk2-BqJplZn94YSABxphHNgdxK1gMjdeoXOllC_r54ZRryivSji5F3gyxwFjXAlD5je3UMVrIulwc2b6hMO6XSwnwJcJO319J72fvrFH5L47ICNJZbqXjM1JY27a8YuQbTiMhwZk3tzyJ-J_rNRzWD_JvzZF8KvRYZLfvrc7hmVW0AheVIojwEoiOCZEM4JhlyqgKhTSBtw02GzQxQjs1JyPriGXvVIOuqxg5Qwrt2Mz3jEkk80GDpTJppD5giw9mPTRjznussuq7WRXNkim3dqK6Otzs88VnP_uhZUvCuOktwEsLVDmeP-ju5RszDqpqk_yx3MoyWgmYLeOKUqPYNn82pGKaXdyly4dz1mDLIt2N9B-5S8rgYXhZDv-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=o63hZPbJp09h6afI2zFxAP_XEAxQ7GbziYQ_6FFsZxR1EbF4vZdITkkjdRaOg96_9ErT22p80Wj1bpuajqpBXVM2UM5H_F6W3opRM48Fl1odqulDhv2gFzIYGvbxEApkU0rnRkrIzi4VVSISRMb0Ux1bPSwIdGfZHZgtSZQUZ6-VG83WRl-ne1yygi2NvEayg1C-phQjQcUykAzlQXAQ3Dq5hZ8bUS10ZsgRXid15AZ8MdfTxUPWpEXk8B495cR0PdRJYNnasORJiJQ5nAxzyUjjrniY87RrIBMcTJT-GYsjBXxk2-BqJplZn94YSABxphHNgdxK1gMjdeoXOllC_r54ZRryivSji5F3gyxwFjXAlD5je3UMVrIulwc2b6hMO6XSwnwJcJO319J72fvrFH5L47ICNJZbqXjM1JY27a8YuQbTiMhwZk3tzyJ-J_rNRzWD_JvzZF8KvRYZLfvrc7hmVW0AheVIojwEoiOCZEM4JhlyqgKhTSBtw02GzQxQjs1JyPriGXvVIOuqxg5Qwrt2Mz3jEkk80GDpTJppD5giw9mPTRjznussuq7WRXNkim3dqK6Otzs88VnP_uhZUvCuOktwEsLVDmeP-ju5RszDqpqk_yx3MoyWgmYLeOKUqPYNn82pGKaXdyly4dz1mDLIt2N9B-5S8rgYXhZDv-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
