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
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 19:01:30</div>
<hr>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=M66buIgxHRfuAZz-PV3cBXnktohN_lFSNVURIFWhyNx0oN64F4vuSAT6osYH1M6-cytSuv9Y0dSJqR3xCzgm70JSmBLwb6vXSXPhZhmo-l22gGTQwgHlC34W_06FjZnO-iGZu5MmNWiWyp6EMW31INaSuyKgaHR9zq2s7rxRIvj9lBawEDA3wbQukdH2KEusn8W8ZMWPBAhxK5LfFcPgBnjJGmO-uEkmm5Dda9dXIt-BuXAY1XydKKE94lrMEZU-6PoBf1-VZDV3BqoePnxtTFSkLkg1aLDJo-FHcBtcCDDcMUI8S9zlR7CSD7oCJ6tKwSSum5v_3rGryYqwjjnbmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=qFpYyyGPRNHrt3NDdZPuko8_Bo0LvNOF4hOFhH2d5upmQHGHYy19-_zTK-huU7jDRakzQpI36ZP6Da1u4Nk0wt_Ukx7NUdeNnZvt3X7g9eoNuq1l7Xc9TIIR_vd98CSt0YIk-p5qd-G5_3BNuoNq1xe-smgxBHVtRklJ6K8q1gsAfVV1l9MGmss2hVAJ0JXUripZmzpNrXfdUsgC020uMP3dTXftDmyyXApbdkfwV89_a1PqERv9hCFINnbCLFnOlXZ2tTSKCOOPnlkYsA3ZNpOChe36W2CUY71GCBsUavRJtgNGuN2CyxxhOB9T9lTNx0muEX5-2BcpQPGJ4HTyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H96Cylua4WSBm4lBT13xREJimfg3cRtT9ijJRN-QqJgwBgdrpXxKL6pFEYeYKlusU3G3j7TWGtOZS8IVHyxmjHSlU9IBEgTsAf7oxG-5syrClWWMLP8FLTXzeFoa47Q6c0EJGDJDUApE_XYa4MovOtRTh-DBwP8zExW83iTxg0rSNSz9Z4hYHcgPy-2o1yau1UL32N773jC-rKGxOWXcOcCalI-hR4lzfe0CLDYtfP2eTJvbtGGRGJgfQ-GJAueUUHltKP5kJqhIV69OrzA60BH0CTCiln-brGwAsxI-uOozp8Vh-bNkXaYnXbQ6ogJkfFTdIpRdJYpMvGjQNW1UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf4-LB8Y5bsN3LBqYKK3_PbcTeLiUclKCV3XivvZE9sdLb-1U0oyMpHAAMmXAZG5U6cpEbFMhWvTgA5p7d_CahF4s1alVi3PKWeClJEN-LlGRPMe_M0po0thqigF03-apIBrzxS8RKyzbiU-zeSd4VRmUAxfAIVjzqER7jsvCTPWngKHEgo2HzJuFEf91MCnTjv0W6fur7oV_YnJJ4sBeRtkdRwD6XfAT7iq4vF1lwt5A-DQRey4jF0sAzGj-_h5ilKImYntur5Uw9LXL_oGvfd4x_Qi60BGc8qp6nFXZNcEB6GRkpYqv0Z1BYDUr9yhEdg4WnvmwIWni6PotGA4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=OwyF9utrGm83req8IWl1KhrT3qy4kGlYjYhjKh6Jh9fbAn_K857Avq6ByVznMPRfqCP88aRGQK2MtVrOUcgmUbMdYKkDsGpCQUn70Of6mKT8Hg1tc5OeJ8hF3y5rfQFTwL3iA4QZ1BV8Lo6A8VBtsZRMZagK4bQ3TrbPgVu_rKYV5laTUdFVPUx1JA7f2T4-8MUQeOn-W2YVkhDe1r2v5lslS4vl6890ua-k0uZ0RsRaWw0TiJMMITErpQKEPzCeDgKaJYGiv7s_s4eW2Sx72RkRlC8pFHiBU9Uqz_0ynC7myUi-j6o8qKjUG9XtgQ-Q6iM1BNRe3_9tdMBs03qWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwio9t5C9X3LQdA3Tfgk8XL4aHUAAgQB5Jmf46RJGRUqs58Qk658mjwptzZSI92TA2iHI_JrcOW6Hh8MJkXRa5PlHh5DhxC4Ou9OS7AdGjPfGktRM57V9gpGGlWyuVsEkal3zCKxf5InmSrRNH1hRHUzhV31P7_lzLcjt8moPI9pJQmgM1asj8bur7wzOoXZ5gmhjTvLFQrcXQt3N-zHltQkFvwRYixz0gNNzbgAmGRqIJNeYdk-ExgZwwEDlWgfpMamyW7mZTJbbaYCd8ys36Erw2sice0WrTmTYH_-ReA2VXampyUbg-Q-s6qne8HM1LtQeSLm9OlKpd3td_p9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3eMdtcErg7lfvLaHY-V7WmcqeyLesbBKHy1DFiYHjziIPe3ofpy8thW_eG0t2tCC8pybs0pgy2HlTl6hhyNsJN9dt7MQS8USIJOgmA8ekrqoB6NZAbE-PK3gXEF4wQl25TmiFTzhwWYA6hQAhA_7vTzNqKWvEzXVuqQvoyAXoTIuIcQ6hQeGb48Phd76PaS5kU-gaGtE9XSkPjjkhhIZLYWnf7nxvoNvYkIi_Br4yudumGsd4VrOlKw53xtuzzf5rgD9TIUCUZO8AA0vDmcVj-t5Jsuz6IKIhZwcNjvjNr2kLkYglwCqHd36C3eqz7JHj-bKCXx8fxvvlBnv_25uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcPULsn7ddD5ww8HjOBCHMQuR_rNAJi8vrB_P7u9Qety7Bz7iZ_CdxEmjn58KV1SPwiwp5V3iGcbUO8dUwezDRLoyWGXTJi-m1PGaddqon_VWEcFy3AT60SJBOYJ0vYLdFS8qKQAA2n_QeFvNs47wr7OY2W_8HvFjU9563zB50nK1l6nCJgZ2k2JK6n_KeBlbNwyVM4KpLzTzswL4oWyNzoVWlUECeYBMM8LkFFgXQ1qBkjfB-9DPOs7Mmtye5MYeHTXLHWuSC2p8B-DvSMcM_LbmGaVa3cT9wg-0MG2VsnUrmPKZ7bW4JZOqfyPAb8q_8jQSjKvWhrXcpWAEoKqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IkecagwPNTwX3YevLrB9Ozv0giPuDryIny7MRDP8V8w4KCxTsOr2YXFNTwcWHMPcUlAOzAPn6kKtwRjVkXmQnY7Da2taeGmeyT2IxGKKjhLYawTj4FwRqJFGEgTOLvFlgJpdP5U1phv5dtM4hxKTJplmmLByfMLGFF9ZubYMQwApIIXXVVOyqQcr31ZoJ9Yq4UXUhjlGLauOoAdoal6T9I96sez6xidAS8YxnQ0tXEj43TLVJcSLWQuamHkuj8VEPCOfAW8yi8R8DC7eVG9l0GYX37wUF7BSswHcHK4uEwKOZbPm9aXABxorAsz8z6Lhaw2Ff9iNOueUEfsVxmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkd21A56mnjRl6zQ4T67xpO1kTusTrS4S8_V2nfycRZeg6ACOscBp_i2GIpvTayMp3K7osmYDWk151e1BMJoXw8OAKH79Hb-vfTe5Ir3CwhpFrJwABgTc6xhaphxWNEyZm0bBlEQoHp-FicbMpxDcVdZCo66syJKCXzI4OxFsOhTtSffmSGAsi0xyL6FcC7X_8yOyKtk_TZrfFw3ISKWYEKoaoJ7MXChRnXSCzbGLjcWoHlmiZRnyH_p2PSZYwb55m3uOYqg12pNX_xVxW5QXnTCSSweybFV-j3Fh6RLJ05n6NUbXOhf1L84Ct9hB3W5KW8ppps50yX-Z7MFR9TOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y8d-Apnj4uCZFyZGMa795bUq3dw_otqwNiFa8b7__2frfG84DTtQVJwds4dh4M91BY5WzUdqUHq_8kqQel3QIb_moQQrNUoS5r9FoYDY18Q2pVbF0xbAOa4tHHeplG0dtK3PmTIyzkoQccD6rk6_Yh9ieXgjyCbkearMvl5Ds1F9M8mA0egxKlr_Gw2cUE1u3dAZc29LxvjqPAdlW-QL2t3V4zW5GTUObIAeVRl7-YGuhcebFufgXTc-1R-p2jQTyuXSmsmlU9ujvDAyeXBwQ_r0xrEjm1-L3B7JKlhUr3-Fs6umxTzwqpF2p1w_Wo09OywCPlecSY6UdJcx9wuz_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8Lhzh4SMe-tfd52BcnBg9W8Slt-Pw4ifHa1_i6wsghk2FLgyEtKCphRK_1UlRbJhYzBHWtoKYFff4e4CPhiEuBDJkgNtDchKBwSP4Sjjq4Ucn32j9NIPxfe4ekqs1kPbWVwzzTIdjoCTiVw5UdV1-EqayZu6lPGtv12YXGrCj_dREHy3_xcN44DM4-R2kpdY5B4d9WY5pA7HEojD_HSSm2BajKK-ZitAYwgZjbcHmJWnM1RSsJfRewZjx9gKDNwSw-PkaWENUeDc32WE-0MkCULcvKeSTDp10ETrskcUAi4HNwAFSSqYUKgZm1Q1QHZMVN8WZPtw2lASfTt_T1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔺
استانداری کهگیلویه و بویراحمد: ساعت ۳ بامداد امروز یکشنبه یک موقعیت نظامی در اطراف شهر یاسوج مورد اصابت پرتابه پهپاد دشمن قرار گرفت.
🔺
استاندار لرستان : دو حمله به شهرستان ویسیان (چگنی) در شب گذشت رخ داد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6045" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6044">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prw8Ygxxr191XrhUD3ZK7CNTqgHS7Kx4tB_v1pmAwgtN4v6FxAq3EUm_eDPaWyvKbSHCJ2dm3KB-SfABpv3gf_5wYrDCA1fyDMFHbYrzzIMF5XY_1B_6IirPXeudayEo67yPAjhqntq7tahzK0_SuFVlKHImLbOpvdVUOY6eiZKow6SH4CZL0gBKMO4_whNNEE1CDwUQDXhVOueJ9hdhVMTz7O_gN3BnhKLuvM3YWhvdsaDKX8VR_hVbavXJGh-PYm-v4LmNrUSVIMrfv4cB2Awk-OZCCy-zbmhnZj5WivM1PBmR2ULmDpP5nZr-WhhVajpHpKlMLalc8XfM7Sc0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر  و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)  که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6044" target="_blank">📅 08:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6043">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVI-IOdvEAZx6-9-CopNdi5IZCOxhXNsw9SnoT5dEYcsf9LtT8Qg0FWn8moSQL__-sE2n0qhox37_dHUgn1F_IfWlunkm3PG4FYSvEMuF7XxdUof_lNIYqxkCDGHcLmnmKgPWmcEbjmz5i3FTWHacDdbnwFFGhqTmVOzbxKuYy7fy5lAQsXGQ6UE6oWFMZjzxUI3RIqZSvY3y_1IKMvtq-eRuEUJ7cmtY-TdqbvA-u4fsj8-q4qFKl3nRLLQEYfQrKKeB4rh3vvcrntoXfSsAbcd3tSj68IvWLIM55HLMm2AjaAZ60w_qR0XT88G3iZJkU2W7rAyx97I1X6YvIQrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیفه بن حمد (نشسته) امیر سابق قطر
و پدر امیر کنونی قطر در۷۲ سالگی گذشت.
🔺
در سال ۱۹۹۵ پسر او «حمد» (ایستاده)
که ولیعهد بود، علیه پدرش که در سفر سوئیس بود دست به یک کودتای سفید زد و خود قدرت را گرفت. حمد معتقد بود که با ثروتی که قطر دارد پیشرفت‌ها بسیار کند است.،
🔺
خلیفه بن حمد از اقدام پسرش برآشفت
و این اقدام را «غاصبانه» خواند.
در سال ۲۰۰۴ با یکدیگر مصالحه کردند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6043" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6042">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
جمهوری اسلامی از شب گذشته چندین بار با پهپاد و موشک به بحرین، قطر، امارات و کویت حمله کرده است.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6042" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6041">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏خبرنگار صداوسیما:
دشمن در شهر بوشهر ۷ پرتابه، در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد.
حملات تا ساعت ۴ صبح ادامه داشت.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6041" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6040">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihhm_IhjjvavgxSbQFbTdek37HDY4aTPikaDQsAAeB0-As_pRaMnpbLPgAlw5m5JlyPK7LDXVBwjkicWWQvXQICXoh4WhZjt6M4nKLUaPXCFTiUTh6Hq98ArMDZ03Eh4n1uZTmRFP0dpapfy7ylLLVg8Ii50lgijBYv5XndEoP385EWypka531QfKwcLTCnTarKq-PEiqyE4_v81ELDmJcr2w8gpcv_gHNkHi86ZMg9Yp6KZVUKMIxuIV3oemBtNW8sUal9_4rrIs5NOoBYI4eX53MHJFc0A8Xlce14DTMWpLLy1_cEHFKRikTIlkdob2ImcZHoG_zSP4DdaOW6tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا :
در طی ۳ روز به بیش از ۳۰۰ هدف در ایران ضربه زدیم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6040" target="_blank">📅 08:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6039">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3ZJ7CBFz-tQ4HKUjs0LmB50z6KLwoEr2MDSJjvJfIbfBe-E_sTWFGrKncDiiBbL6MgcGeY-27BLyx2MeOyi0Ef4gRfBtUA_PNnhVAy74jH8GVhMLEILF09HOHzexp-5mts5CSgFvh8cojnubsTNuxnszS9ETk6czlAexpt-MTHeTEZlbBs8ZlgcZWWQ3x1ordyOOsYaCSYul8kSfJADnQgCLWN607cOp-wlqYfizzcEzXLJuJ_1ba4uBHjcIeIULoQht_J9tpzUZLeZBfEvwNKGhI6S4hLhpUfIpp9IyTM1GHcpxDiWlqON6e-mcX_JZ8vyKs8i9QS1nKSKk6KYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نقشه‌ای که نشان می‌دهد تمرکز حملات شب گذشته، شهرهای نوار ساحلی جنوبی بوده اند.
🔺
معاون امنیتی استانداری خوزستان از حمله به سه شهر این استان، آبادان، هندیجان و ماهشهر خبر داد اما در خصوص خسارت و آمار احتمالی مجروحان و…. چیزی نگفت.
🔺
‏معاون سیاسی امنیتی استاندار بوشهر نیز از حمله به سه شهر این استان خبر داد : بوشهر، عسلویه، دیر
🔺
جاسک و چابهار متحمل بیشترین حملات بوده‌اند، بیش از ۱۴ مورد حملات موشکی.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6039" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6038">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏قالیباف:  دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6038" target="_blank">📅 08:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6037">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏سخنگوی ارتش :
آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
مداخلات آمریکا برای ایجاد
مسیر غیرقانونی
در تنگه هرمز باعث ناامنی شده است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6037" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6036">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏فرماندار بوشهر: چهار منطقه در شهرستان بوشهر مورد اصابت ۱۰ پرتابه دشمن قرار گرفت.
‏ در مجموع ۱۰ پرتابه دشمن به سه منطقه در شهر بوشهر و یک منطقه نیز در اطراف شهر چغادک از توابع شهرستان بوشهر اصابت کرد.
‏حملات یادشده بین ساعت ۲ و ۴۵ دقیقه تا سه بامداد ثبت شده است.
این حملات تلفات جانی تاکنون نداشته است.  ایرنا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6036" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=S4uubJZDr0hzK3NpHNTlUPGLsBXE7kafxh-hy0mhpfLWvMSt6Cjho7N6k1fpziqj6wUR4WxysLO6s2yeYzAqzDtuse7_LWgiFPU3ovRq22bHX1p7WqaYcdO7HhThp0deQZgHtq3P8h4ylsbJ417SfcJix4TB7lTNBNUhCYN40Gs9KqV1UD_MlJ-qbz51IoaYPKpkYpUx3BoX34Y3Uis82fBC3dnUCot0SzuMUPliTDj4-IpT4ki5OK9INYM03OQBO5jkJoDidGBc9JOzMIKdXb_bL97apmKmYrZkR9DhkGiQs7WFkqbqgw509tT2RNk5rLTos97x1pfWjXkkeaEqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf289ef5a.mp4?token=S4uubJZDr0hzK3NpHNTlUPGLsBXE7kafxh-hy0mhpfLWvMSt6Cjho7N6k1fpziqj6wUR4WxysLO6s2yeYzAqzDtuse7_LWgiFPU3ovRq22bHX1p7WqaYcdO7HhThp0deQZgHtq3P8h4ylsbJ417SfcJix4TB7lTNBNUhCYN40Gs9KqV1UD_MlJ-qbz51IoaYPKpkYpUx3BoX34Y3Uis82fBC3dnUCot0SzuMUPliTDj4-IpT4ki5OK9INYM03OQBO5jkJoDidGBc9JOzMIKdXb_bL97apmKmYrZkR9DhkGiQs7WFkqbqgw509tT2RNk5rLTos97x1pfWjXkkeaEqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش ج‌ا با انتشار این ویدئو :
با پهپادهای انتحاری  یک سامانه موشکی پاتریوت، یک انبار مهمات
و یک سایت راداری متعلق به ارتش آمریکا در کویت را هدف قرار داده دادیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6035" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6034">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
شنیده شدن بیش از ۱۰ انفجار در چابهار</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6034" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6033">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
صدای وقوع انفجار در شهرهای بندرعباس، سیریک، عسلویه، دیر، چابهار
سنتکام : پس از حمله موشکی جمهوری اسلامی به یک کشتی، این کشتی دچار حریق شد / حملاتی را شروع کرده ایم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6033" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
بسته شدن کامل تنگه هرمز، یک معنا و مفهوم ‌بیشتر نداره :
راه انداختن جنگ سوم!
هسته سخت جمهوری اسلامی مدت‌هاست که از تفاهم‌نامه با آمریکا ناراحتی است، در حال سرزنش شدید افرادی چون قالیباف و عراقچی است به خاطر این تفاهم‌نامه،  و بر تداوم جنگ تاکید و اصرار دارد.
جمهوری اسلامی به آمریکا پیام جنگ داده و باید دید پاسخ آمریکا چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6032" target="_blank">📅 02:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6031">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6031" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6030">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEEQqCdB-e2hDybKQef1fxAcRNrQBNXGic5IRH3d-uwhaFsANI7RHHdYM0RMgMzEjB_DHuCVyLx7c6iqnz5BbF1IQ-zSaduBksZicEk5Y4vNrkIqYlLhe3GkPsqtvLuMfcEkHg8ZSkxyMS6g7VU0BQW-Dijny0fxR1x9UivL1q8ZyPGMhrHF_O8wGKmCugowtObMcPIFQA8GjhnxZqLRwCEXdgLakFC7IOt9p5V7e91n6ASmxZem8Ax6ikpKj9OL-6YCvtv0p_Rlme4uYJqfOcBsCqJUJY8zwCnI2Mq6mXGbd_cv7N4DTK4VcA0aSSGT0ItfCFVSnYYyy1Q_7LydkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد روزنامه همشهری
زیر نظر زاکانی - شهردار تهران
اینقدر فیلم و سریال آمریکایی دیدن
تن اینها هم لباس زندان‌های آمریکا رو پوشوندن.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6030" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6029">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sNYhzSXc9eVtg7zFd7nfhh-MpNknY7Oi0a906Igr2S4J1cW_HbmWfZsLsTkvnsE7-hU2v_E3Y40NaqvH8xM3IQvDVg3mIFthCA7UUX9OUNjFOJnRu-zx23-SktkNcsiOhPBxAZ_6ud7vdyG_ore1SPDd9Xn9IFgvDnz3ZbmJeR_ZeIeZYID0Vc70_thn_Wx6z4EXMICEHX8-hERQlHu24UA4xDnsabP3WMe58CDox5mWaEdmkOw9Zje8qOvqthUstmr_bcYDrc40W-jEUIOk86t8kQQRm7Co9YzH89M9GZxnHaMoGtxUefiWnXsyTc8IO8a9InULfnuIh5N6WvVsMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f51d55200.mp4?token=sNYhzSXc9eVtg7zFd7nfhh-MpNknY7Oi0a906Igr2S4J1cW_HbmWfZsLsTkvnsE7-hU2v_E3Y40NaqvH8xM3IQvDVg3mIFthCA7UUX9OUNjFOJnRu-zx23-SktkNcsiOhPBxAZ_6ud7vdyG_ore1SPDd9Xn9IFgvDnz3ZbmJeR_ZeIeZYID0Vc70_thn_Wx6z4EXMICEHX8-hERQlHu24UA4xDnsabP3WMe58CDox5mWaEdmkOw9Zje8qOvqthUstmr_bcYDrc40W-jEUIOk86t8kQQRm7Co9YzH89M9GZxnHaMoGtxUefiWnXsyTc8IO8a9InULfnuIh5N6WvVsMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در غزه داشتن برای مصر در مقابل آرژانتین جشن می‌گرفتن، که یهو مصر شکست خورد و… :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6029" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6028">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpVJdz0diWC96flj4VlvfPeVEBfM59FzsYYHvOd0ScVac5TdYz_Sq4fCSphp70CoG-4jiKxz2gGFv4Mreyp5KNs-jPEFaCNgYvhUiqVPEzq8F1WY-QCFtqfSOE1wxeRl6ozNc08B2Eu4K5OtQ9EsHvIW1Y7dYPZxLx0sCp9jocQGE8fHbVAj8hexY53lhBpCLyyQfpirxdl-E-DkDe5xrPiUEt8c7vtyQYnZDRpGH5BWPaGCGz_pyKOlQck-tIhkHc2p71LpVndo-mK9TVgxAH9iWdQHp0dG-mZ8ab-jPzoS6bVdh_LAl02D4iyuJvWKMb0csfDLC5JF03W628q3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075957731576426859?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6028" target="_blank">📅 18:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6027">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجتبی خامنه‌ای در پیامی به مناسبت تشییع و تدفین علی خامنه‌ای، رهبر پیشین و پدرش، تاکید کرد که «انتقام خون» او و دیگر کشته‌شدگان جنگ‌های اخیر «خواست ملت» است و «به‌طور حتمی باید صورت بگیرد».
او در این
پیام
که روز ۱۸ تیر ۱۴۰۵ باز هم به صورت مکتوب منتشر شده، با اشاره به کشته شدن علی خامنه‌ای و همراهانش نوشت: «عهد می‌بندیم که انتقام خون پاک شما و همه شهیدان این دو جنگ را از قاتلان جنایتکار و بی‌آبرو بگیریم. این انتقام، خواست ملت ما است و به‌طور حتمی باید صورت بگیرد.»
مجتبی خامنه‌ای همچنین تهدید کرد افرادی که در کشته شدن پدرش نقش داشته‌اند «آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد» و افزود که این موضوع به حضور یا عدم حضور او و دیگر مسئولان وابسته نیست. به نوشته او، «ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این ماموریت الهی را انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6027" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6026">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItEgcOAWyolcp0SpNTUXPLjRfbp7P7GnIdbgG95SCnDMRuP2zXo94qMjMDByVl-vqVTsKAtdXBR_8jI_0yfC8_i53qgM3T8bOEWQ1V0C49mCbX1wDigqkyxeGBPtHEcfwYS2IgcawMk7hU1n_GM7JnvgOAGdcalp4oX_MSqfSMBZ0yZK5FDFLs7nQG9jJL3dBeAA71ZcZfetf1Z_uFFNPhYhSdAitf-ZgspQvIvXVqxDkFQ9w5hNu6IVyI8vyI-RP6-KP999qucWvFexX1MDL8Y3A8EItLAHzHEM-26yqcptVUwpy4PrLbi-Z_BY0qUGEWN0AcvN6DcaDtcMV310Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6026" target="_blank">📅 11:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6025">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=Tos6eg9Dm4AXupCodRR8TSyaUth_w0t8Tuh1SEA1pasEhsPpzw9UcPum9nQeyNYmBX8xrkSoGSJNe60GLxhV2YUxl5nFt0tOiirH8c_7XE0j0-PMdezrJKTIHkzqU8srcYafrDOZR7MZ6107XVeVuJyz47MotvPszoqM8SAjs6_4YeQouQToU3YboORgyrbvbDmwwm9ehk29JqI0xSX_nXNbHutWZJH-g6IyPduygV5KTQccSLnIEg29OqiH6WKlBJvqh9QPE1rj55sFnZKO2rwQwNz6Hd-WprHzn2_Q3RDaokBzk2qb_5hcm-kavI7wCsSNyR-r4faasBNTwd0Y3pREjkVDd6tNRidzot_D5Kp_00F8qL2BgTyetjCb87DDDhbmbS_kvADKJZLJcP86sqB5KDRISdU_EeiIvh0xOUfO7efAL9HF2OTmcM1iF8uahMdvVGU3wpKTpOpIHY_6B4uyQ1E45OWjQEl8AoXyVLVSVh0KZdjc6okQZcXbaqJ1GAeZvnOpiD9Fp_fnOFpBWGtfC8jxAGAFz-ABE8cKnTUjX7clvWnm0tmMmcM21jWhIMgBqdpGWEIXzSsc7B0WfQhqtzxu0s8LLZvjOs3ZdQCZPNYo3iwZFxQny_7Zmg_UpYBT7hKhHwskCMum3_pimhgQVqGqnPmqo3IXmu3DOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2adc09f41.mp4?token=Tos6eg9Dm4AXupCodRR8TSyaUth_w0t8Tuh1SEA1pasEhsPpzw9UcPum9nQeyNYmBX8xrkSoGSJNe60GLxhV2YUxl5nFt0tOiirH8c_7XE0j0-PMdezrJKTIHkzqU8srcYafrDOZR7MZ6107XVeVuJyz47MotvPszoqM8SAjs6_4YeQouQToU3YboORgyrbvbDmwwm9ehk29JqI0xSX_nXNbHutWZJH-g6IyPduygV5KTQccSLnIEg29OqiH6WKlBJvqh9QPE1rj55sFnZKO2rwQwNz6Hd-WprHzn2_Q3RDaokBzk2qb_5hcm-kavI7wCsSNyR-r4faasBNTwd0Y3pREjkVDd6tNRidzot_D5Kp_00F8qL2BgTyetjCb87DDDhbmbS_kvADKJZLJcP86sqB5KDRISdU_EeiIvh0xOUfO7efAL9HF2OTmcM1iF8uahMdvVGU3wpKTpOpIHY_6B4uyQ1E45OWjQEl8AoXyVLVSVh0KZdjc6okQZcXbaqJ1GAeZvnOpiD9Fp_fnOFpBWGtfC8jxAGAFz-ABE8cKnTUjX7clvWnm0tmMmcM21jWhIMgBqdpGWEIXzSsc7B0WfQhqtzxu0s8LLZvjOs3ZdQCZPNYo3iwZFxQny_7Zmg_UpYBT7hKhHwskCMum3_pimhgQVqGqnPmqo3IXmu3DOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخوند غیر ایرانی در ایران صاحب خانه است.
ایران، منافع و ثروت‌هاش، برای همه است، برای تروریست‌های غزه و لبنان و یمن.
برای آخوندهای خارجی ساکن ایران.
سهم مردم ایران اما فقره و سرکوب و گلوله</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6025" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6024">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUUh0vFD0MQz2sTkVIKGovpWp2L-_Di5vCljTjZbN4Usv7yHvJhVVtNoYp2zZNMJpNtcAzjAgClMVJajhDVCi3cK9LiqoM9--dJ7LQEKvlNXa-uOj3zxo_4-xGH2p4Fn4h5x6jFrCwR3QCdEAUKsLQDdm9FfK7zl_vRZiuXZxc9vhsvJ4fQjKpsMDeoStG8E2vNkuoOU-C80l5qol-yqVA-5R5j9ZjOzdg53yzSrlbDPN5lRsm3fGHcLC4k4GnOKieD7J6qfIJ3CnpXkUYA2Ns7utHfJPZDijpakeZoWTG6NcuBT7gxxksnDf1uHBUmTrKE5LZ54-9jlR0vA7UBEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6024" target="_blank">📅 08:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6023">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anvynIqW3iZ5WIAHyVUWHz84u0DMLwCiaxrm2TwU8Chm302dvexNXITuti8fJKCeXdCLNzbG4L7UWj7e-IpMF4lw71OpGP88NNhYXYOxeoKrTE4AFs-2Z7evTookgycjxalYTHumER4XdMmx_zNfeIxFh4mx89EDxx0UYWrz-irKLPTzLLsb7O_FYeelqY1lTt_NqOcqnCRmrgynO-orCJ7xjDdXxFbmZh0qZWRTRxpnk3wIpO9pfACPBzC7cn8oBrGjtjgjM3SL7ULbwmaG-jdNjegbOraiGeqLcszGBYWr_GppL5t6NyIR7UIq5TS4PfHez_TZgDpiFF3QRn5qfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئیس جمهور آمریکا در «تروث سوشال»:
‏هزار موشک مسلح و آماده شلیک، جمهوری اسلامی  را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور ‏کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — الحمدالله»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6023" target="_blank">📅 07:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6022">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py5pVBAHjciZdQDxDeXlebKT_mn0hToihK0H8ZD-O-vPCxzgWarx6Wwpy284gXP_I5pInK_xlh2jMO0sR2aqbOEkeQNcjvoMrANxhTgZ25q7x5NVERH0a7bF7aivhuOMq3p4epzR0c5klumgmFuuJav2INbmZq57RzGV50zgnwAHyYYFIm0CoVWCg09v_HYeeF4oEwmj9fe-TLVE-2SV6AoQ4oDGTLUcMsAQw72EEMJPJQe5ZxHodwLvnOOmY9-ot1VtbEBS4NUKurcI7xVFd0BjnA1HpLQlUuQBCa1ezLq5lQJD-dv38ZnyMyO_cfy9wWVcSeWwqWTv-UB9OhweBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه رسمی وزارت خارجه آمریکا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6022" target="_blank">📅 01:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6021">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دولت ترامپ از ایران خواسته است که روز شنبه با انتشار یک بیانیه عمومی اعلام کند که
تنگه هرمز برای عبور و مرور باز است
و همچنین متعهد شود که
دیگر به سوی کشتی‌های تجاری شلیک نخواهد کرد
.
این خبر را مقام‌های آمریکایی در جریان نشست توجیهی روز جمعه با خبرنگاران اعلام کردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6021" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6020">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=UaWfdcF-zFoI07Zh0pAU3NDzUj4jYiM_a4kYC0bfz1g7FPzKTKpu5IjK14i2_r1sHbWgmCHpN7xI88BPrCw14WaoCoV6hslwFIXZacItNkpoC-bW5wn9ACGr3USHrIW3Ls0goNzqaqGxKzQrdbW8i-7Z-2GODaRqFMWa6UnwCiyF_kvKhMU2VROXh92FuGs3brJJAfJ6VIdsfDtFqnFY9pdumydunfBOkvcs78HXp1KP2YXrbrK_EzGxSrK9Zwt6NeP_3xgd49vtE_uidH_m1SJDH2FhGRVveqD5oWZqTLp0Bv4DZslrOElshXWWaCGaD9t42fZJIPbzIFIX33Qx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03c66dc8.mp4?token=UaWfdcF-zFoI07Zh0pAU3NDzUj4jYiM_a4kYC0bfz1g7FPzKTKpu5IjK14i2_r1sHbWgmCHpN7xI88BPrCw14WaoCoV6hslwFIXZacItNkpoC-bW5wn9ACGr3USHrIW3Ls0goNzqaqGxKzQrdbW8i-7Z-2GODaRqFMWa6UnwCiyF_kvKhMU2VROXh92FuGs3brJJAfJ6VIdsfDtFqnFY9pdumydunfBOkvcs78HXp1KP2YXrbrK_EzGxSrK9Zwt6NeP_3xgd49vtE_uidH_m1SJDH2FhGRVveqD5oWZqTLp0Bv4DZslrOElshXWWaCGaD9t42fZJIPbzIFIX33Qx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:  مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6020" target="_blank">📅 23:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6019">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">علی‌ خمینی، از اعضای تندروی خانواده خمینی:
مذاکره به قصد صلح با آمریکا خیانت است.  هر کس پیام دوستی برای آمریکا بفرستد دهانش نجس است.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6019" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6018">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3_-qgVHB5p3L-REwXZeP8LSmfgRHR1kZUe9WDUf3rBIrWa0GTJp_pjH9Yim7UJ8_uZXezmbcYWjUjZ76jq_SFZLkizfDuyN9eFMjRbRHuOSe3BfwPxM91cSo7OGy4ec4vtw305yMgBt9ZwGdeiXo5BpTL4ZSAX_sz7BlPqePgn6cl9Z5I2_RQ6kJTLoQsawapaqdF_qt6RzvnM86tuVGO7Yim8DbfB5WM-7wX99GZDyi0Dxz69CMPW61kZCAIavRiZeab4g_qxuMCcB4e74dryeTVxwYqoTtM5jlcp81s8_rVno687Bkhpfd3U546fEDKnjGgHPD8NVopyrXq5rfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علویه، خواهر بزرگش (ناتنی)  در سال ۱۳۹۳ در سن ۸۹ سالگی درگذشت.  ۳ سال قبلش، در ۱۳۹۰  علم‌الهدای معروف مشهد در یک سخنرانی گفت که زن حاج شیخ عباسعلی
😅
می‌دونید که علم الهدی اسم زنان رو نمیبره حتی اسم زنش رو روی قبرش هم ننوشت! (ببینید حاکمان ما کیا هستن!)  خلاصه…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6018" target="_blank">📅 20:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6017">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe4YCXF8Y-OiHwocVgRt6nsBmbDbbPasfwbOJ6PSgKwbYAh4oUww-2mJcJ93aO5l70ltcItuvdPYkY5qKjl_f3I7a8XIdQA2t2mtUImziJg9rg-aMSjJvhvhyFgawHvHh4aWSt9wxmazJ836QRQejIjccjnWTGlofEiAap4uc8x-eR_MPzilmdV6wJ-MfqBHJCmfiBof5vzJo23wnwBroF7NOftQam987z9zi_1F7f4OQZrb9Q2xywr6UIevOxZnaSCcWbp0GcfkNszqj1hX0FuWt4fF4-E-cFkraswO9Q_RvfturqsV_d5Fs--XqmtKcfsQhbVnrLmqWtU4j2-jdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد، پدر علی خامنه‌ای،  پیش از ازدواج با خدیجه (مادر علی خامنه‌ای)  یک ازدواج دیگه هم داشت و سه تا دختر داشت.  از خدیجه (مادر علی خامنه‌ای) هم ۴ پسر و یک دختر داشت. جمعا ۸ بچه بودند.  اون خانمی که ظاهرا خاطره ای گفت که «علی خامنه‌ای وقت به دنیا اومدن گفت…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6017" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6016">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پدر خامنه‌ای، در کنار زن و بچه‌‌هاش غذا نمیخورد!  خامنه‌ای می‌نویسه که پدرشون در یک‌ اتاق مجزا شام میخورد،  مادرش برای پدر آبگوشت درست می‌کرد و اون رو توی اتاقش می‌برد اما مادر و فرزندان معمولا نان و ماست، یا نان و خرما میخوردن.   «ما بچه‌ها در اتاق دیگر لحظه‌شماری…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6016" target="_blank">📅 20:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6015">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJqeGgnUgFsLYEGoF0wjtOZjP2qe_2TP2VRrv97QhG6uTnpybpsTh3HXKgsPeGpT7TMYYMsg38-9U4z4BMNk_8LXPoTRe-rzqkp1cWcai0W2sdfpYvKAMfkTMdCFATiKyAJt5aXrHdmA9pFsjm5nKy4Q_vIzFB8GsHxaHi00LyGzkC3Geehz9yYc0sTLGLNopQz1WU9wEwZiJZXrg5lgw5dqXpQ3g1BYKq-kI9ULJql5MF-pV_zMbQ4z7LPYiCCOMKsdhJGuTHi6A4eOeEL6dS7kszNlZz3O0yckf6_rQjbODb-zn6U34E5CjjgKoauQ7Vf-UpnvUbBzuv4iIry7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای و مادرش - تابستان ۶۰   علی خامنه‌ای از سوی دیگر، هر از گاه مجبور  به کتک کاری با همسالانش می شد که او را مسخره می‌کردند و نامش را «آشیخ خُردو» -به معنی شیخ کوچولو- گذاشته بودند.  در این تمسخر هم پدر نقش داشت که کودک خردسال را مجبور می‌کرد تا …</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6015" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6014">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvLGhycBxtAtFCr6l2RJ5Gfs6P8I3AjLsx47RCGiytp3w3D_nkyMRBF8ESu3t012plktENXgqtzU0aYQVGF1LSEN--xQJ-PCcSvJeinb8YQs52RNKPYryT1ggJKQQG-Gvi0kxzPNjVUhPxr5Urjj0q1D3zuKHh4rmQJuUWHphytObEwaFKU_j65e1i1g844rHVm0YxTIdIb3t7ckF5Njcv1vcSjhlQ12kdH1TYRfaGP2LsSxtJzYfiCPbu4uDq_kmvd61yAIKvKT0BmN7YaLew5BRINJT0pb8xzxEqOPdR4eaFf7xheNNemteaRimR49rfGXgBUnGbegaU5swqyLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای در کنار برادر بزرگ‌ترش محمد خامنه‌ای  علی خامنه‌ای در خاطراتش ار جمله روایت میکند که  او و برادرش محمد،  در هنگام درس پس دادن به پدرشان  (جواد خامنه‌ای)  که «دست‌ سنگینی» داشت، مرتب کتک می‌خوردند.  علی خامنه‌ای نه تنها برای اشتباهات خود،  که به…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6014" target="_blank">📅 20:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6013">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6e3EMTxUL_Ng3Ifw8Cu7RuhfDQU53Fp0O5Jb5tC8Oj3aAvBhFgc8_mJTIUpX_D0Ixvu9JbsQY8GiH1mExO_NG97sx4q8XwYdxd4ZCMhKLXVw3Rmj2L9XtXgUdzyfd3nRMEDJpuS6wRmi-WrXGky-NyTVHXdaUSngrcMYLXpNSGDRirigA8VfydiDIYvEIQgJdc2Q_1DOLP6PLZJqjhNfn9jpNwTbKGlbLlCFj3y7aOuSoAm14aBTovp7r_Cylhl-qhGthgaTHoyu4QqlNoHKq2h2mqO0V9pbRHXkph35pBlifugI9O3_PsKaBDd_Ie5aJAmqmwqMLsJvN5ROquKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب   پدر خامنه‌ای فردی بسیار سخت‌گیر بود! جزو آخوندهایی بود که مخالف «برق» بود! و اجازه سیم کشی و‌برق کشی به خونه رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6013" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3-3RKnnG_1k00l9BVdS9QXAv2CsUkezX1wVCMM2y-YjHTqOwCTQtAooe4h2lAhIqpBzZmNfw5HJgP9HUzGif36uaD-lzr-jqlnVADJaJf2Ecri5s7rvSVleTBNVD30n15VWDpk4J0m7UtguXpqGV8TFTpoLTIvjv3kS6DqDr1nKtVy4xZv--ULSRUQK0eqr6e2KcMNjeNtIUPhKG_nJsLLHPv-qjpdUGH8abz2luAhDEfxK44MAC_zU2dOy5xxXL_vkIEPJIu4yyAmjyDuLptTDtgCNkG8Rdl5YTDck1yxCep3FJNsPJeNMz2HZsPsNvJEV7Cu2s4VKENkOPgwLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر خامنه‌ای - قبل از انقلاب
پدر خامنه‌ای فردی بسیار سخت‌گیر بود!
جزو آخوندهایی بود که مخالف «برق» بود!
و اجازه سیم کشی و‌برق کشی به خونه
رو‌ نداد! اینه که در خاطرات خامنه‌ای اومده که از چراغ موشی استفاده می‌کردن ‌و مادرش معترض بوده که وضعشون از بقیه آخوندهای مشهد هم بدتره!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6012" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینکه خامنه‌ای گفته :« ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم،  آنقدر کلمات تمسخر‌آمیز شنیدیم که این پدیده در نظر ما عادی شد.»   خمینی هم در سال ۱۳۵۸ در جمع روحانیون کُرد، دو تا خاطره تعریف کرد که روی وبسایتش هست. لینکش هم اینجاست .</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6011" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSFiboc7bki3BM5Zr9lyE0iIa4jun07-GrIBo79wNq8Dcuv2EDTXmAjcHl0Nn0nUQTAQCzfMHUwYPJ4dMu4AMYwZcicPyL26ZpbmIZQdp3D-mpSDJz2A32LxxKi8AZwDlf9-0UycRa8DxBTZcaGST2tbHV8Q-MDtiizPoMoK5iS3XA4xSOpco8RnjdRLJPsy-ju1nV4mr6Vk-UMLmxopQnMoyXshSKGOQfw6-30Sz_sv2-GfbRIt1Qm8QZB-4uRnWcvxIxhJ-BCV9PtZyrZ3we6S30tqnYfYdGGfQlT23uVB-lV7dEbBR0dyipJ8UeyO2bJpJJP_x56h9n7k2rg_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش  اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه  آخوندها رو مسخره و تحقیر میکردن در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر  لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی   او در خاطراتش…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6010" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6009">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeMGQVAOuld_2NXFjhBSmCQNaJt2jg9c5YVFqbnLwoPzn_I7A-BZo2tNXjbmWS8F73SWnmnicJi20m2Bk9uShK24NV0z6jGUoEg7jf4V39HT0qBq_fPBfQpmlKnlDwBPO2p3P4rPJLm-rn0Z54NdBjEMgzHFsFK726PnBl5lqzKVL-NMFg7mLYjDXvM83VhtLAz9EM1o28lwPlAmY6X8H8gy6DNt9a3Z5fQq6LWg8y_VA-Q0PQKdDcLDPlWyceagmOetQMtRsXrw5VreSjcXVN2pSSFDiFdsKTM7UskMFEGw0Fl3pO7HpU_uL48RNkOQ1X2zXk8kThmIoQ_GmmScxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای بارها و بارها در خاطراتش
اشاره کرده که چقدر از اینکه لباس آخوندی می‌پوشیده و مردم در زمان شاه
آخوندها رو مسخره و تحقیر میکردن
در عذاب بوده.  چه در زمان کودکی که بقیه به خاطر
لباس اخوندی که می پوشیده مسخره‌‌‌اش میکردن، چه در جوانی
او در خاطراتش می‌نویسد : «یک روحیه عمومی ایجاد شده بود که و را مورد تحقیر و استهزا قرار میداد...
ما از زمان کودکی با پدیده مسخره کردن عمامه مواجه بودیم، آن قدر کلمات تمسخرآمیز شنیدیم که این پدیده در نظر ما عادی شده بود
... هیچ معممی چه کوچک و چه بزرگ از این پدیده در امان نمانده بود.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6009" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1CavngLtwOAEJoeApaE3O_xQigO1N9XgKU034SZz7rLnsq524MW5FKVRVuSydbBwKNqnlZ5d87MINwVFglCpWwgtq1MdleEhnDPAB3y1xCweH76wkL0bKJ2x6yLrkXYWA9ceuLnyehD08j31aoc5tDDnjH3QovV8j9m-jnxrOAEBeP82fOriEGYB5f7tEUSssF8j1ZQnlPL334V2_X5JzzwEfGw9JJ0eD9sLLguC2wN5bE1p7zyYkrpMKaIiMFzVXr-fT-WuuZ1yZE8-9kDYwvZAdcpmXCjBO9276eOqwZX9PqHD-ar7yZZQ6_hIvOITxbHlqOIvQCMNkC5Z15QUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IGvJ-GdtgnqptETBYeodqJbKttywmR64-4dZ_pmy7x1AtMI-ZtoNCmKCCy61-f3GzRndrQCK8ppzvelrA2wMjZdpYWVVxLqe7LHpi9Iw_UhA2RulrNd6Syeg_v9HeGoEUbetUSYL99HbwmJyLzHrJ7HxF2gxLSL9znTWXORwEHuth3VxB7NsYg5OhS7WjX6xi9R7mu9M6waOCfNqazqeB3Pidfx9npwtzGHWxgvoJB-jOxhwTSORpKdqWHdltR6GOMytYnMhtlVdXvxN9UprkhUjISaaypmg0wbptp30glbdbjmrrjGqulXEhkm67SqqtxOjCkFDuZ7iE06sT0LyNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=vKbPAT9-obivwcjUmonLq1BnuBiPAN_N29-hQzFCiEi71hz4Ufcp5mXRs_OzTHan-ulmu4Vw5X32p6Tiy6hQ0Sno2FZwZf3VMBadJ8A16VVdYXCf9WwIf41lNW4KM8T9YyLe_fam9ZFG8VVVHA4EMgURUfc9O5ny1fLMTHuNayYEIml26SkYD5RPBciJ0_OECBtXpgQeTfPZWI2WF37VN4Fqx8lUTeKsOUCIanKMDITsrfktaV0PW3aYE_SGQQxPhMo1ZjnUJ98E-tcYjzzQDy8gJ5pAPsM09yJwmKW8_O_GezJCiYPJwGNCglS2EwW5SlOjhEyJD2bXU71GAhimaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c19fbc0a.mp4?token=vKbPAT9-obivwcjUmonLq1BnuBiPAN_N29-hQzFCiEi71hz4Ufcp5mXRs_OzTHan-ulmu4Vw5X32p6Tiy6hQ0Sno2FZwZf3VMBadJ8A16VVdYXCf9WwIf41lNW4KM8T9YyLe_fam9ZFG8VVVHA4EMgURUfc9O5ny1fLMTHuNayYEIml26SkYD5RPBciJ0_OECBtXpgQeTfPZWI2WF37VN4Fqx8lUTeKsOUCIanKMDITsrfktaV0PW3aYE_SGQQxPhMo1ZjnUJ98E-tcYjzzQDy8gJ5pAPsM09yJwmKW8_O_GezJCiYPJwGNCglS2EwW5SlOjhEyJD2bXU71GAhimaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=c1kMn6dzsAGCS0Rb1n7B7Y47lqLdrtXmM-W7qdpDnNfbyr1TsK_k6N7G7QtwDF_5ZT8pa859Z45wDUG2WbOfyRPaV-5hSONz4mCUFUGS3RyGPbR9fF1Rr_RTtVPpUIAReOqPUl9OBEteLlZSUTg4EmUt2whBbPLDWKU1JC2t-LAc1D70vWdMd10AG1Ox81qOsSUrPItjx5o_qGAIrireoXD9Q7Zs-kbvwgfreN83J3mG0PH50yrC1eeVBf4t2iL2L9ZmDUuVksRMh4leK2qGCvV-kHHzgoNbzgQA-SMseoQig_VtK7qqkNUg2qIYyHHz8YD8QtqT-QaRR7MxpBkVvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906dabb08.mp4?token=c1kMn6dzsAGCS0Rb1n7B7Y47lqLdrtXmM-W7qdpDnNfbyr1TsK_k6N7G7QtwDF_5ZT8pa859Z45wDUG2WbOfyRPaV-5hSONz4mCUFUGS3RyGPbR9fF1Rr_RTtVPpUIAReOqPUl9OBEteLlZSUTg4EmUt2whBbPLDWKU1JC2t-LAc1D70vWdMd10AG1Ox81qOsSUrPItjx5o_qGAIrireoXD9Q7Zs-kbvwgfreN83J3mG0PH50yrC1eeVBf4t2iL2L9ZmDUuVksRMh4leK2qGCvV-kHHzgoNbzgQA-SMseoQig_VtK7qqkNUg2qIYyHHz8YD8QtqT-QaRR7MxpBkVvYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم مسابقه طناب کشی برگزار شد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6005" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اکسیوس به نقل از میانجی‌گران (پاکستان - قطر) : حمله جمهوری اسلامی به کشتی‌ها توسط بخشی از حکومت جمهوری اسلامی طراحی شد که مخالف تفاهم‌نامه با آمریکا بودند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6004" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwpOi6vMsDRA740I9s-mKS138hVTxxGfQksgBBOmoY-ILbT23TF2OPFPlGrKK20soTtQbsWkrO1frCqKy9g2bBzXf90RdsxtLVvPsRRzNN6XKAdXMNHjgIC6zKbqPUOSFNBKCwBD2Mq1hUCBlPXsoNXvHqWNNBpJFu8lAfd-vLqVltt19SJoksnxIwnZHNWBMT-EYy3DoYQylToVauxiFX7pb80_rgFT9gqb15sZChITTc31-qcA7rejLthMNY9RBhIDzESb5H_GnPBU6KhjribWhryLOm3S3_WW48xmAqo28rTsa1-zJhyfWCkuOWA4mDnW59w1Lo0iUasS19NXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBoQp8_vTeJBnEe-dPxsWXKg3XrmrwcgWlOjdeRXEloz-4vCarXzSLTujpHYdDiuOh9aVDN3WyzyDFzOWBserKJzqXQvXTcejPcVblULXKNRdPIkJ9COuI2EhOtkfMkhCQbWVtuJN397ImFMrpiVMw3VqGROBPqc-o4iVlylwbHxvnx0L27tKBMZiLCXTCGXQbYyTQ3Us3ce00qszyg5reukrNRicaaMks6FEipTj51-U1HGPZsNud0G4covNGqs7eJXqO_VGKBJBmtADOslNUnpjV6us-_guLocNHRR1fJZPssFOzazd3LJniMAr6THM_2BP-t5xAhupsht3YTKpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کارشناسان و منابع رسمی شما  که این آمار و اعداد رو درآوردند، احتمالا همون‌هایی هستن که به خامنه‌ای گفتن در سراسر دنیا دارند «سلام فرمانده» رو میخونن و خودش اومد اینو گفت!  همونجایی هستن  که بهش گفته بودن  نفت آمریکا در ۲۰۲۱ تموم میشه امروزه   در ۲۰۲۶ آمریکا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6002" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDMUWcOMxmdzzZDYmXiulMW6U4SyQI1Ej8PyTrZUfctT2j7mkv1CBATn0u3ztPp03_eUDUIC4Zrc-b-CMn0G48Ky5lV6-wTYOtvmQjh_9YEY8Q2BN-vP9sQnpqTRBoRWODD7WFi6BtIzlKZ0qPuHXDqwCKQiV3CvMUQMwvW2LquG7pWDszCg-pUXl_gLvth9RcknhY8-dzEturON7inHUoK2XW1QNDr5wtBjblLBzCYD0EruKLNcNsgKgYufSc59JpaFvL_gN0dPKRLJWNncpIAypg9-BR_Ktdac6aUl6YOhDsAbcrB7WcMgXtlNffKReCvQ-1tsqVrxBPKRslF3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlqQLKNDZ7A3OkZL0TAuXuEnWRNAqcMxyOi_6OVKjv5nTTJNbyZVRGpGE1QugsdaavrN4fkPfEB51hSL-bTKHs4NTpn0SWp9wF1VdwnX9b9aShTqQjg2O_PK3qIER7k2DLtZXRdbuOQVQK6etoIgF7T159bsmCIF5T5XOc6zwxrkvNTkngbl_rfJw-x8MzBNsDKIIn_XOPcxcgYg3tdmCnOBQg63Vmve1hO2RnMD6GheUW5-RIjSb5Cqu5F-H8wq5d0KKaOp_5zUCxpFSHyIsYBkX3ZLxDZlUr1_wIqvtoCNr9d3is3aaeqxP6DALSsFUBMuW3wASrW76sfsJ1c-XjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e9261a0.mp4?token=PIAjzFfeC6s3zJ_k7g0EflWH6l5gRMQ-6B5wPok1d6GW-cMsfP7NasuhFI8dg5dlowTUrsjfFSaWdze9NTI5Hay8VKP3VjVqVCWLKJK7vMIXRSg2kqDQajXJnMu3Uj6jzH2cA2gJBzePgW3n8UuOvaXIc5dFSQa1x9OAJ_vHNEYb2Y90r87XEiMYDZJP2TRHOchMWcbKaVhkzvSEWgFugiFpo10ft0v3PPAue8d8mRYfKGoC28deKYXeP7TUTb54BArFCFImwZ5amn0jUgrzBJJFMFlkU3a71-RTDMe6IZ_YPT1CgvV93a-LMvTZunRVnZokZdttfAKRHrA177FqlqQLKNDZ7A3OkZL0TAuXuEnWRNAqcMxyOi_6OVKjv5nTTJNbyZVRGpGE1QugsdaavrN4fkPfEB51hSL-bTKHs4NTpn0SWp9wF1VdwnX9b9aShTqQjg2O_PK3qIER7k2DLtZXRdbuOQVQK6etoIgF7T159bsmCIF5T5XOc6zwxrkvNTkngbl_rfJw-x8MzBNsDKIIn_XOPcxcgYg3tdmCnOBQg63Vmve1hO2RnMD6GheUW5-RIjSb5Cqu5F-H8wq5d0KKaOp_5zUCxpFSHyIsYBkX3ZLxDZlUr1_wIqvtoCNr9d3is3aaeqxP6DALSsFUBMuW3wASrW76sfsJ1c-XjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6000" target="_blank">📅 09:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WyXqaxseZHWCeUcNF98vfky5tGed7FC5EXSK_f1-pj8dYfIs2ZzItUdCe0Aw7axsKTBhO51f78fqBeXz-m9RQ0vBEqqy-NimqjSlAvCL6bTo44C_a8SJCBZHEe8Od1x65zlJxRW409uBEtidB5FPi4yUOwMG-4RFZ7k6XAqYgDhspVBeq0sSXnGwS7R3d8TY-4s43y2vEilSYXBvMbGLmzney-NeBUl47CpNm7AqvNL2Q3T3Aft1SblxaYb8gVQIAtxflq-ychLgaQuxy2wrMjEq8QmC9E1Fdb635rYXLgOleHuzUJoHZndUax_KeITMitiUsEZmJd8HrZc7dEUWHoWafPewCzTKwu2FGEMcOno0dQplB1e90QxKQ0AbooEYiImfDuYVLlwbLVAAJk1ZGRsiRq0Qhc7VpC2OoScjSkXOFlqDTzAtQ8h_IdmwWz3-xpXpBsapp9oWYJs4RI5KgA50rmFz7FYpjFwFd8FtSRH38kgw5Sq34xFYR36t5cVyRzSN_JowkhzmACbUbR6plLcgoj2--ZEeFG737YHi0jaKIhtt7ExWshaJBY6K-Uz-sGvh2NBLackK4qxHpWxsOXyqLT1Bvu242rvSnXFazzUu45415mvncs2ec4_pH7lCEhqdQBPK55qETemzDH3eqv4g2AxDIzpSQ2Y9w07xsvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067cd17a67.mp4?token=WyXqaxseZHWCeUcNF98vfky5tGed7FC5EXSK_f1-pj8dYfIs2ZzItUdCe0Aw7axsKTBhO51f78fqBeXz-m9RQ0vBEqqy-NimqjSlAvCL6bTo44C_a8SJCBZHEe8Od1x65zlJxRW409uBEtidB5FPi4yUOwMG-4RFZ7k6XAqYgDhspVBeq0sSXnGwS7R3d8TY-4s43y2vEilSYXBvMbGLmzney-NeBUl47CpNm7AqvNL2Q3T3Aft1SblxaYb8gVQIAtxflq-ychLgaQuxy2wrMjEq8QmC9E1Fdb635rYXLgOleHuzUJoHZndUax_KeITMitiUsEZmJd8HrZc7dEUWHoWafPewCzTKwu2FGEMcOno0dQplB1e90QxKQ0AbooEYiImfDuYVLlwbLVAAJk1ZGRsiRq0Qhc7VpC2OoScjSkXOFlqDTzAtQ8h_IdmwWz3-xpXpBsapp9oWYJs4RI5KgA50rmFz7FYpjFwFd8FtSRH38kgw5Sq34xFYR36t5cVyRzSN_JowkhzmACbUbR6plLcgoj2--ZEeFG737YHi0jaKIhtt7ExWshaJBY6K-Uz-sGvh2NBLackK4qxHpWxsOXyqLT1Bvu242rvSnXFazzUu45415mvncs2ec4_pH7lCEhqdQBPK55qETemzDH3eqv4g2AxDIzpSQ2Y9w07xsvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ بر دیکتاتور یک شعار نبود
آرزوی یک ایران بود، برای سالیان طولانی !</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5999" target="_blank">📅 09:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مداحان اختصاصی خامنه‌ای،
که توی هواپیمای اختصاصی که تابوت خامنه‌ای بود، از عراق بردنشون مشهد.
نقش «مداح» چیه؟ مدح قدرت رو بگه
و بگه شما بزنید توی سرتون!
اگه یه عده از شما نپذیره بزنه توی سر خودش
هم حکومت میزنه توی سرش و سرکوبش میکنه.
اینه وضع جمهوری تباه اسلامی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5998" target="_blank">📅 09:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHs4ZyKD3s1M1-1A8R9Dn_T8BquouPkGyCPXB6W1T4bMbz2c1O0K6avH3EawFW8RZFAge-YZ7QTB2i9MEdzfA_6piefECZGPRYi8RvKgGT9VwPR9Cu6EnUSVGpUFZ10L4_zv8hKBZ7e3fuyPMFe5ksIvLDGKRUhsoA03PJsycgVn3kshCtj92Rve5ZloIY0CKRTO94ToiJoLQ5TGt3mO_cWul8gkOrn-sIQC1H3Z_HmN1irq8xKr_Ivf4yLLZl1WHT_8SG6mowj3TZFHbuy65EUeJsR5b4yHnpX5rKgcfxHkGeIfhA9iFLFgzErKNBUnoFUYU1C2DO-YjLIFzJ0-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان : اسرائیل اطلاعاتی در اختیار
آمریکا قرار داده که نشون میده
جمهوری اسلامی طرحی برای ترور
ترامپ در دست داشته.
(این چند روزه در مراسم هم پلاکاردهای
بزرگی به انگلیسی در دست داشتن و خواستار این‌ کار شده بود، مجریان تلویزیون، مداحان و روزنامه کیهان هم همگی صراحتا خواستار این کار شده بودند.
ترامپ نیز در ترکیه، زمانی که از تفاهم نامه خارج شد، حداقل ۳ بار گفت در لیست هدف ج‌ا قرار دارد.)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5997" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5996" target="_blank">📅 01:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فرانسه ۲ مراکش ۰
دقیقه ۶۵ بازی
تیم فرانسه در ۵ دقیقه دو گل زد</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5995" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttM8P2V4qMaq-KMu7PflhxZlMTFCfdSChkdyn4AEObW_5fymOvrVCTdYoKzJvTzqWcEHBIYjPR8mT_VLpihQbZ__IMw-Za9Y8pYWtiQ02yDoXm-h6hhS1VFyKMPHnt0q20C-x8i1djyQQ7pHliKz1-PHB47XGthwvAstvkHhDeEJKNL5FmGlHNv_ZnR7czcB1SuPVAzgu5ZYsQ35OeTxKpCoJwk6fXqqGh0xeIKh5jR3H3OCw0od0t5iyclO2ycjwxAUrOAdsFfCepXSidAl675vEQArDrzxPipTu9iRkLm8c9SrD2E4Y4NJ83zPnS28TQFPBw3-5a3YO1Flhb6a0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju_5XSSpcUJhs4C7Vo95WIxz0GIyJnktxPl98KNuyVm5264sAShjJsD1fnUxm_KxZ5m_E7r_1KNLzZRvoYffNBneKAcf3e6cfqYlPbr_wbFzti9Plx-I5fSu_RnDK17BCZ-PYqi6zHFzXBKPkZAk5FXJc4p2qgcKpdzZPzBy7DsRq9dEsUZTtmvcTY62K4JO8I8kD-37Uhy-J2kXmv9XJGYgF7_7kw_cXbNCvoMJQofVJ_W2RE4kVfaZPxgiz9d6WQHq6_Zrst2F72CcIzUveHlk1cStl7eN-73sxaiI9WDem7_Cz-tqEUBSFuqGi4FX8Bg3E-0_2mLwwUHIcAPE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های حکومتی از حمله مسلحانه به بسیجی‌ها در مشهد خبر می‌دهند</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5993" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=j-UFX_jXO9PvZhtChRoaYKZrj8QzROTMBXvPfLzRcNWj_63pD-sEHkpE4A02MqoA0Q0HkI6l13iyGobEfpDelKFeTMK5rKdQQvmjOZ5dQg6csBs6FkfgJhl-OnRyoAeHwVp_Mhy7-SOwsg6gavjd1vI6To8fVGgdA01Gb35q6G2Yy3ff06xlg_ByjPzecoeSlkP_hXP7eEeHod03ljj0l06VKkI6_sQq0OzToFADidXSPl_uMqHfDsZYoU69aiAcrOqHSob7tB9Kbji7mVdcsbwLgJDfaNUUtDr8jLcP8IS97RPmE6YGbzwmrWiiP0AoCqpqSf5T1VGP0HZ2PLwsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=j-UFX_jXO9PvZhtChRoaYKZrj8QzROTMBXvPfLzRcNWj_63pD-sEHkpE4A02MqoA0Q0HkI6l13iyGobEfpDelKFeTMK5rKdQQvmjOZ5dQg6csBs6FkfgJhl-OnRyoAeHwVp_Mhy7-SOwsg6gavjd1vI6To8fVGgdA01Gb35q6G2Yy3ff06xlg_ByjPzecoeSlkP_hXP7eEeHod03ljj0l06VKkI6_sQq0OzToFADidXSPl_uMqHfDsZYoU69aiAcrOqHSob7tB9Kbji7mVdcsbwLgJDfaNUUtDr8jLcP8IS97RPmE6YGbzwmrWiiP0AoCqpqSf5T1VGP0HZ2PLwsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbfkukZi-4A6NcqbCN-BEUf14jOJjRCWCfp86Rmy6FPve-MifId90d-mVyBoWULn-sE5UhSt85bHeKle9G7U4rv7-_DR12u5GMkpX08Tk-nta0827bQUXtkdL0vAwlPfj6FcvXUejXvF80fnO4U9l8b1anXzRadxmkSwZQgSuFYMFu5ifH0EeYlc_g5s9_XDoXMvvI_fAcsR23bt3M4A3KygjlbNEOUPYC6JWfgsVUVxX_KHEUoQq8PjGDXIIzRpIQ0y4E8a7s9baXyZME4Uvnp2Lq6nDd9THLl5zKFanPWN5UH-o3j9f_yJKUiCvldhoNm-flpjSbt2Ho0kptjS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=OqBJAb_rj7kP2ISG5jKepDMEkGIrA_LW2E3XUxG9s2Q_L3CfmxSAE94iJruyt-C6hobDen2BcqBGeL-b8nLlxPqUMLJ8Q0uptMYYB0F7VFZf2-Kdo0X7Nm2DMw33OCuOr527Y0i89zy--yWE3jcm1PJ5h3IObanemK3rQeq4RF6UOW5K4fdcYazslAYh66CVlYeTFYQ12YsnlASArrANFehXOrIfWLf2oviw_FbHEC9SM48b4ZdarmwcmPMuba1CZAX4ZMBvktYsFgeiuwTTRE54NwAG8RSgzOxRcwzQQZDIAdnBH-m-PdfbNjOfg8lR3OCgM9FQQ4ahEOdv6U23xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=OqBJAb_rj7kP2ISG5jKepDMEkGIrA_LW2E3XUxG9s2Q_L3CfmxSAE94iJruyt-C6hobDen2BcqBGeL-b8nLlxPqUMLJ8Q0uptMYYB0F7VFZf2-Kdo0X7Nm2DMw33OCuOr527Y0i89zy--yWE3jcm1PJ5h3IObanemK3rQeq4RF6UOW5K4fdcYazslAYh66CVlYeTFYQ12YsnlASArrANFehXOrIfWLf2oviw_FbHEC9SM48b4ZdarmwcmPMuba1CZAX4ZMBvktYsFgeiuwTTRE54NwAG8RSgzOxRcwzQQZDIAdnBH-m-PdfbNjOfg8lR3OCgM9FQQ4ahEOdv6U23xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icxFNe1pyp__Wf6D8l156ty0_MeZeEywZ909wyk0jU83BgRoL4Umgl-1FKYGga7TwHvtAbyCLlvm6zIkCJ7mI9-O2yFglmjIUvT_SgZEz1AYf4wyS8hxDw9vO3cGCCoYgqYWdIswaDgZ2hNCWSUzYGsI6IaTKcMgu5mqSOU0udjnzJ1m8Wuu-J_bYNDUvDdXgzZafa8cxSLFDzB383lDetVIUMk-p8isrodlq7NzIe3mebVtaq6OLsGFO4_a4PTHFlUI7fivA0gqj61NVo_XsyVVlUbO-OQU0cj4-o4PnYySTqsBMLL4atl05CCppm8DaMnhjCd22KlMEuOrFnxbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cheJAaXDpFiKhZZZFnXRIlETQ0pAvk3eLN_c1o_krjxEGkeqvv68mB3YLNujwo4LvhGBjxIGuG74Q3U8_nKdyO3v8aKxo1QMWsNG7IRM5CppXRdxLW9jEO2UYj7MFMpWw8LP6aMO5T8l5xBFr7iF6RMZOi72ULbRDDgy6E415Qing30QkBeruZfCky8ixFLdR4ThlUZWJ1JILJGhuS5qO1XxlY-LXq9Spzqq5HG0KUad7bAXzSXI6po1i487v2U0IcG7txfIEtDUX9tpLsAS6jqswCGL2IRURIQKhW-SN2LDygw69iREFIAbhJj43Elp9uYPZWjNCQgnR__NEgVeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=EDnqBLEgd8zTs4x3JLDSB324qoAYjUbph87rEwOITrsiFPv_9cW_ReHAAAbgYAZ9ehDRtiC0amnPDgX8b6BB6hWQxwaPLfFW1qB2pMuAj79jw002jDVL1Iegz64p6rOkwiREWYKuK-qGyb7sWbdmTCThlWYVfyV3nuQgCJ8muYfrDVSg01cfGuGMtqch1LVvnk9G3Z_xHUUjbBdNhxq_Vgr48w2609h7G1BvUpxmAdwhTaFlXAZCEFTkXQNVTIr0LYBU5RGAjyyiWaykCDgwiF0zdXWZYlhPV-HNyS39WtrV_JnQ9V-276bBVPoQrArXnViMaM__nCrw887PIqy77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=EDnqBLEgd8zTs4x3JLDSB324qoAYjUbph87rEwOITrsiFPv_9cW_ReHAAAbgYAZ9ehDRtiC0amnPDgX8b6BB6hWQxwaPLfFW1qB2pMuAj79jw002jDVL1Iegz64p6rOkwiREWYKuK-qGyb7sWbdmTCThlWYVfyV3nuQgCJ8muYfrDVSg01cfGuGMtqch1LVvnk9G3Z_xHUUjbBdNhxq_Vgr48w2609h7G1BvUpxmAdwhTaFlXAZCEFTkXQNVTIr0LYBU5RGAjyyiWaykCDgwiF0zdXWZYlhPV-HNyS39WtrV_JnQ9V-276bBVPoQrArXnViMaM__nCrw887PIqy77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ekdAKr-YHJMDuyczSlWIZpSrlAOHBz-sRC8VO3dqB0Oko8Gno3F-RoXFq22mGR2LXhnyRwuTHVQtytaj_nReXlnuXJp3MfiUY4r9GzgE3q60-8sCiTGjQ3QoKmlR73HTldp2hBmaK64rs_NbzLpPMVhYDLOdU0k5iWD4PI49a8hl0WsvrxHkpkr6IIvlBPiWheA376Y5VhBSEvxu1G8L75DfXF1GH3E2PToKx_28yFt4wxw-bnf1OI5W_HArocslGEA9PHouZc9c9nDe_an5p7ey-jjsfcPmLwHWRk6Z8ijupUKG_kSZ_DFWQ9UaGEKlXhuaN-MfyWbuyRrGubUXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=ekdAKr-YHJMDuyczSlWIZpSrlAOHBz-sRC8VO3dqB0Oko8Gno3F-RoXFq22mGR2LXhnyRwuTHVQtytaj_nReXlnuXJp3MfiUY4r9GzgE3q60-8sCiTGjQ3QoKmlR73HTldp2hBmaK64rs_NbzLpPMVhYDLOdU0k5iWD4PI49a8hl0WsvrxHkpkr6IIvlBPiWheA376Y5VhBSEvxu1G8L75DfXF1GH3E2PToKx_28yFt4wxw-bnf1OI5W_HArocslGEA9PHouZc9c9nDe_an5p7ey-jjsfcPmLwHWRk6Z8ijupUKG_kSZ_DFWQ9UaGEKlXhuaN-MfyWbuyRrGubUXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=asxJgYCrUIUpN9QlDZ4BVy_oRJ6zcx3V38ZYOP21XqSvltCELlPvTPqV2TuJPiFVkMe_-vABHicAcmSbU17OhATsBUsuUyVzx47rIz3HKhhr2YqW7zlIQyWkDwcZRx5YsExf8MeK33ozlum8Q4rANuEE9tar1eR_lVRfK9-OAQG9Y6WAlD4JNa9Sk5mctZ838OwrUQGWVxVGTa4VERhGCjj7UUB4GmKjOO9XuOoWi_glz9rS7CW4qreIjpNOlk-XQMK32It8dlzA45NU1hksUxEvahA6kjgRfgS4-CnxWcTwrvgZJvK7gXiO--S_Dq8tkGlOMGjXKurOA6OJHO1fyE32K0SF0RQL9-XceylvrwPWN7G5L-3HBnPlHzXaApXBSJyQh3rk4ANO5bwxYaQbFs9UGzT3pixy1slWGHwiqGD65carp_pgufO_Ks7vMF22FGk7qfoRFEinniCwaVcOE3feCRgEPnkeEImNBB8xxyF4blB7n_q8M4tJ16tlv71zmH6rM7wLuwK70spQOHTD5S5pOEFU4apnWqsitHtzyqozNQXXT8T-96dQ11IEi2aIuy6rLQSR5SGFVemAUyqyb-F3GWAruBRyc3EkTkarA3E2eWxWazXgL-O8vTugcxWyjIq6qS4Ug5Gz6eLf88G1f2bS89ksKATcIndbnxSzDiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=asxJgYCrUIUpN9QlDZ4BVy_oRJ6zcx3V38ZYOP21XqSvltCELlPvTPqV2TuJPiFVkMe_-vABHicAcmSbU17OhATsBUsuUyVzx47rIz3HKhhr2YqW7zlIQyWkDwcZRx5YsExf8MeK33ozlum8Q4rANuEE9tar1eR_lVRfK9-OAQG9Y6WAlD4JNa9Sk5mctZ838OwrUQGWVxVGTa4VERhGCjj7UUB4GmKjOO9XuOoWi_glz9rS7CW4qreIjpNOlk-XQMK32It8dlzA45NU1hksUxEvahA6kjgRfgS4-CnxWcTwrvgZJvK7gXiO--S_Dq8tkGlOMGjXKurOA6OJHO1fyE32K0SF0RQL9-XceylvrwPWN7G5L-3HBnPlHzXaApXBSJyQh3rk4ANO5bwxYaQbFs9UGzT3pixy1slWGHwiqGD65carp_pgufO_Ks7vMF22FGk7qfoRFEinniCwaVcOE3feCRgEPnkeEImNBB8xxyF4blB7n_q8M4tJ16tlv71zmH6rM7wLuwK70spQOHTD5S5pOEFU4apnWqsitHtzyqozNQXXT8T-96dQ11IEi2aIuy6rLQSR5SGFVemAUyqyb-F3GWAruBRyc3EkTkarA3E2eWxWazXgL-O8vTugcxWyjIq6qS4Ug5Gz6eLf88G1f2bS89ksKATcIndbnxSzDiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC6r8Luxjfx4UuPOBgjnZ7MMjw_nCR4UapIw1PL0FuqAaznZpzpa3GQtLBKX5Z25692MHTprojgx7R4bZX3YC-DLaY41WUJAkIkrtzeiYqmn4_QqhwsTwex1H-MeLAFdRQHUzY7SBs79EiUSdlT3cYt3FFEqgiK_8UeX3vlFl3SXyR8wmNLBtPNKwO267mDoTICSRor868RKzClIYudp1bnHuQWefwTYr18xSIpgQ06X8IMhOeB1CPIK5Vvy73cV2MFOXbY7vFJleBom7LURMVWOBVGNJtmoAiL6U1Evw3EnhysnLDoRER_ZFIfCxepgx4Mm4xrLw3Ht0n7IRgiehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRVB3mPqSmFofgUY8Fpqh3yH6BTu81S2n7DT5oDlYN5vdXaylYYeNE6qrXg-v-pD7JtuMUtpf_J1Lw3QsA4KVHhxDz6_GoRyW-qOKByCoan_Z0EZIqxr5vpe7KTUb2rmJi94Ui1bE3TUnRpVgCrDhrnP7szS0-5buw3aQabXCVq8zYy3PmhnJ_AjT1o-7RqHKn0kVn9r1C3mud9qemx-c-ulpA_kKYVj4_CfP5d8nrXUzrtObVtKP7SUmcGk49cFjkkPRsjnTO_FCMCPF-Zp-ONdTRVe6c_V_vxmlhgqmbDNXrmo-hFcljRJ5CX97eNGl4eKbEVRUuDtrD2j-9oArg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bltjl0bftsMRgZJCIAeKm72YaIEPC_p96SOItt8gwhms0LpDA3BFdhaztoHX4dulF12GUrq2BeyRDWj-yhcsAz41MSv2_IBwyem-0kEk_G-rGYoPTf0xXxyDybJ-ic9KW6glgCqXIClJxCTQkUJ4_G7H72P7Gps6G2WD_p1PeonL2QZTU87TqfzqLLdUYn6ndKo_1d-9YDv91sPmiARseD3uF_WcZw7aPhuwn6A3RZfQSLiegDfGrQCx1kqvYcg-fRW1p_Jar2zt7xr5gI8irw2ycYN-sIoeMaw5q34XSsf1w4QvDUao2Uk2GUfJwaAo3Hr4WG0tQUWABApK_-DFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=upTMwx1XPs9NlV2OeBEbZA1AaX48hV5YomJXzAS36KXyRKbqinH1Y34-Ph39trarUoizuEHr3p61CzcaFkchr75vviJdtPR-b_iq9L1UZPiAx1DHH_lKSw1rRCtX5KJH2dlzGo0-vJjwDnm7Hd3t4yvz7veXfjuu0AxqQtsdEgDoHumEapQlA2VKLlqNptenHOGpMS3QpP7RVSwxrkAKxI_WW43j7bIS4GlTtewdPmTRnBVcA0hNTz-3yBNo5SNx2YSUTbvd4o-5PjoxCECd0ku1XDsq0EiA0AAMqjjiLEglxJKovTjLe954BDNrcMmrj0WkTliAb1GfA2p2jJxcdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=upTMwx1XPs9NlV2OeBEbZA1AaX48hV5YomJXzAS36KXyRKbqinH1Y34-Ph39trarUoizuEHr3p61CzcaFkchr75vviJdtPR-b_iq9L1UZPiAx1DHH_lKSw1rRCtX5KJH2dlzGo0-vJjwDnm7Hd3t4yvz7veXfjuu0AxqQtsdEgDoHumEapQlA2VKLlqNptenHOGpMS3QpP7RVSwxrkAKxI_WW43j7bIS4GlTtewdPmTRnBVcA0hNTz-3yBNo5SNx2YSUTbvd4o-5PjoxCECd0ku1XDsq0EiA0AAMqjjiLEglxJKovTjLe954BDNrcMmrj0WkTliAb1GfA2p2jJxcdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Rw7mCU4t_6tDbwo_EewhCNc5Kb38pfUorFaFqokwrZdmLDx6Z-rsBYmVjUx4HbGJhSm1GVC7yMRF1eJCWTUQRALnGs8WjBDjmDtoRuBL1wAJdkxK9k4uej9X4og91dHXC2MYiYVl-d4lRMcpKlGDaQIoyfmOrEfR_qTx89BeBwVQgkGO6npaGRNz4wofKFNzSkMMAypAbxzOvxyYnvYjYArqlFAxQv_vS9o8Og7ue27kyWIS0wnZzgm6C1d18rczXu_y5dzL-B2SxdVJSIMWQWvAtAAaC_vHqc7wa1wNkmRJeUI5PmjL6CyCVYDBgk0F5Zva921_QGnsZWTnokHEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=Rw7mCU4t_6tDbwo_EewhCNc5Kb38pfUorFaFqokwrZdmLDx6Z-rsBYmVjUx4HbGJhSm1GVC7yMRF1eJCWTUQRALnGs8WjBDjmDtoRuBL1wAJdkxK9k4uej9X4og91dHXC2MYiYVl-d4lRMcpKlGDaQIoyfmOrEfR_qTx89BeBwVQgkGO6npaGRNz4wofKFNzSkMMAypAbxzOvxyYnvYjYArqlFAxQv_vS9o8Og7ue27kyWIS0wnZzgm6C1d18rczXu_y5dzL-B2SxdVJSIMWQWvAtAAaC_vHqc7wa1wNkmRJeUI5PmjL6CyCVYDBgk0F5Zva921_QGnsZWTnokHEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=vB_4PsvKXplCGlyR1EuWualoUDzX02IdAWvomAGwVbAEcimUKyPKnzHo-n5OZ5bm_xfpzzG6Wc85GcquE0-B5SWvIB7Qkio3pUM-rUdcMSCDG2rOwYV6ecHbjUnhMf0nRfyER0JtXuZ0baXJu8J8rNjl5ont5suwwFVF1kQf6tVspnIY33LHm1vQd3nkAMs3rlBu5V1VvoPSmq3fEadVhY2ytKczwlQv6JdZo1hq2iMAoPdHieDzCJa2-GcNJ0LiJxW_xU5_7O5nFcwkl_QgYep5ojY6J-vdGPA34q4ioqUW4I4LcedbYP-x9FtsQvDlg6LPptB7jwz_HxqH0m3nXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=vB_4PsvKXplCGlyR1EuWualoUDzX02IdAWvomAGwVbAEcimUKyPKnzHo-n5OZ5bm_xfpzzG6Wc85GcquE0-B5SWvIB7Qkio3pUM-rUdcMSCDG2rOwYV6ecHbjUnhMf0nRfyER0JtXuZ0baXJu8J8rNjl5ont5suwwFVF1kQf6tVspnIY33LHm1vQd3nkAMs3rlBu5V1VvoPSmq3fEadVhY2ytKczwlQv6JdZo1hq2iMAoPdHieDzCJa2-GcNJ0LiJxW_xU5_7O5nFcwkl_QgYep5ojY6J-vdGPA34q4ioqUW4I4LcedbYP-x9FtsQvDlg6LPptB7jwz_HxqH0m3nXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ul-iUIQ-_rwZFWCjughYmxr5P36tB09mELDMf1tbb-YQfZipUk7m195xpK8mPpQGT3ww0P0idL4h69Iw48mPizDofhCoxrUL_oAZWaxrJLTiLQYXaf4pJBHriAevx2YMeZKxEWv7aq_A-V-pnDmnppm18BdwJPBZXTjklrBlSJg2SOGZpRGTodOB0wZHcdtIeF9VoEncoU5I44LDO5IlOFX1YizJ2fvYVv47I9TMDpBxzXtODXtFU-2vXoI8rUtpF3D03NhKpZ5zKCYfTIucmjmh8Ap5U7cITP9wKi6CjlvzS8aSGyEL70nLjXsB27g1qFX_tZ04wc1sHDcQdjzhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=ul-iUIQ-_rwZFWCjughYmxr5P36tB09mELDMf1tbb-YQfZipUk7m195xpK8mPpQGT3ww0P0idL4h69Iw48mPizDofhCoxrUL_oAZWaxrJLTiLQYXaf4pJBHriAevx2YMeZKxEWv7aq_A-V-pnDmnppm18BdwJPBZXTjklrBlSJg2SOGZpRGTodOB0wZHcdtIeF9VoEncoU5I44LDO5IlOFX1YizJ2fvYVv47I9TMDpBxzXtODXtFU-2vXoI8rUtpF3D03NhKpZ5zKCYfTIucmjmh8Ap5U7cITP9wKi6CjlvzS8aSGyEL70nLjXsB27g1qFX_tZ04wc1sHDcQdjzhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjnQ-X2CzgA5MYKnFJPgFZaRojJBz1IyvcApTntwjs1wpiUDTjQl-G4Jl7M6FMURI5qfNs9dAUwhZolVGrBGjrmsngcyrjkh921ePvwJnBFpWbQZEZmcndUwf1OfU5Wt-Op8vrgloaRiKjlD5PqzgemfFgLjj8HiM1pVySOO0GBpuLwrLxGlFDn256sSQAjwO7peKseDtrxF2KmwIjGc7H8bhElHL3AKnYXkSpx4dkJiRogMRaReiL45OKymo--PzofTKOhz0mCKFKQB5iBX3Jqc2d9uIW-Vg8H3eOM-hEEHN8V3XEXmWy1OpRpVE6CfscOm2mnF1x58j2_xdgUD-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=eouayl3SeHtZ-wnCwgGaCYrAewwkM32wpN9m1mZUJOrcF6SvExRuPQuYN1HoYbAdIrKWBxJ5L6UtOovA2_X-xtDXsT_AhJRyM6SRxV0kg70jRNKinM6aSQcGInUhd79PGNcWO1jEdXtjdT4FoAG0L9zABjMfPnnXpq67RBrGHHZ4aedYhHhK5GjsE1Juy_J8fVBtd7zQ36-U2Vc9Bu5ch2zRWbKvd5JS9-Oo6vVab2sn3rSqlWyn1WyWXxO_YdJkJ2V2asyMMIIhdv0xzTxfcc4quBKSshK8JS2oPGQOfVJ7x33DILqC67xsUed1iOqSWZZo218o7jbvp_dWfkV0uJuAmkCkirXlNUo4gujeTj8XkQPRz9qUL2e7lPTGxGx9x6Yj8C4YqgqzzVUP2SKABJJkLuZQIJj3j6TCcF1so7tuSJYGfyqhsLcjoMIQQ-JJfBHB9LfkSpHLZMZlGqVROp_vAVhvCJYkwxh1NkbQkUqX_diFUrvaibhzgNmnFE_7juOiFoL120iSRE1qnRXVV9bWPnSHrhqFVfsvs8rOewGy8IJxA3XfkVkYDevxPINKiA5w1w5Seatgn9yOHEzYP3e4FMstbUSoouUEhfSXwilFeuPZBJSsKhDUJFOq0e5v53lkWiBAO0pTsmu_x-bsxCunt5tyAMSjXW-mmkp1Tcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=eouayl3SeHtZ-wnCwgGaCYrAewwkM32wpN9m1mZUJOrcF6SvExRuPQuYN1HoYbAdIrKWBxJ5L6UtOovA2_X-xtDXsT_AhJRyM6SRxV0kg70jRNKinM6aSQcGInUhd79PGNcWO1jEdXtjdT4FoAG0L9zABjMfPnnXpq67RBrGHHZ4aedYhHhK5GjsE1Juy_J8fVBtd7zQ36-U2Vc9Bu5ch2zRWbKvd5JS9-Oo6vVab2sn3rSqlWyn1WyWXxO_YdJkJ2V2asyMMIIhdv0xzTxfcc4quBKSshK8JS2oPGQOfVJ7x33DILqC67xsUed1iOqSWZZo218o7jbvp_dWfkV0uJuAmkCkirXlNUo4gujeTj8XkQPRz9qUL2e7lPTGxGx9x6Yj8C4YqgqzzVUP2SKABJJkLuZQIJj3j6TCcF1so7tuSJYGfyqhsLcjoMIQQ-JJfBHB9LfkSpHLZMZlGqVROp_vAVhvCJYkwxh1NkbQkUqX_diFUrvaibhzgNmnFE_7juOiFoL120iSRE1qnRXVV9bWPnSHrhqFVfsvs8rOewGy8IJxA3XfkVkYDevxPINKiA5w1w5Seatgn9yOHEzYP3e4FMstbUSoouUEhfSXwilFeuPZBJSsKhDUJFOq0e5v53lkWiBAO0pTsmu_x-bsxCunt5tyAMSjXW-mmkp1Tcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=ZPGnFBBt5Z9e-aeJUzIEkgGOMSK0dKzFIVDVGZbbzanlKQL15dOI0ZMJSHP791ehKaAKlNZg1mn3Fn2qY0ipMu-0bLh25Dm4QcfcAEdOu7P9WIcOF9BdxvPH9W_sE5KB24jSWZivnPkuDEU2-C8djqvPj3_oHGZ6Yuht6ulmR_eI86UjjvbBUgd0VI9u7MHsS0VNK8104RR-ge9R-dszI8ixU892hfrA6bYkLx32dkq8FlIU9jlTHCsfHcME6nvmGl5VI-ejcmFFX-OH0OM-8FY6bzRoa3FEA69jcgnb-jg6oiwoe1nz8Iv_TOXXkWSkyfzmYRZyD9x6TkAR_AEjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=ZPGnFBBt5Z9e-aeJUzIEkgGOMSK0dKzFIVDVGZbbzanlKQL15dOI0ZMJSHP791ehKaAKlNZg1mn3Fn2qY0ipMu-0bLh25Dm4QcfcAEdOu7P9WIcOF9BdxvPH9W_sE5KB24jSWZivnPkuDEU2-C8djqvPj3_oHGZ6Yuht6ulmR_eI86UjjvbBUgd0VI9u7MHsS0VNK8104RR-ge9R-dszI8ixU892hfrA6bYkLx32dkq8FlIU9jlTHCsfHcME6nvmGl5VI-ejcmFFX-OH0OM-8FY6bzRoa3FEA69jcgnb-jg6oiwoe1nz8Iv_TOXXkWSkyfzmYRZyD9x6TkAR_AEjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJShu2kpL_FrIssLAHsQGLLbHAesEaATVwMDUdWaweaoJaMOBA6LYeiTPNRlk2q3lHeSUyMbmw9B4K0CsZeIakqox_FD8CWR7T97fnXIiWGAaV_SVJlgJMaz9kuMsOyGzRPH4SyM0z-IAxIJf5AnFHmTGuRrHLfP0PG2TsZX7kp4WA0emjjIeE2a7CeQsp1IydpeSxSgjcF_dnAHHQwTpyjq4ePuaFiT-7zdxgAswqdqXY0WkadKij1Dx02SdnpQf2GP0sidNC9em1v7t3fHfPB_z4gimVfHjTLWyREd0OUzsMdGGi6E2lU01ylvLFnekpYkG7VyDxRyyIiEajWmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=TsVDWeJoOk6I_hRS8WM-hcTUqWEYfxloz8zxvdqDlzOw65s6oZWXMHd13gT3P0GipPYTCRii927nkF_TwbuJ4Z-WdI4ivX9oz_H_PRfYd8L4ZlRYwtHyXWI3THMAARAJ4FoVkaE7uzakFZywOiU8JmXvbZCYaMmEeIMbzruka5Q7EKeW0C2uKyoZUAfvsmRoUBbHvEVLrJ7QzW2Smkep0auFv0y8uzmUNAR3F34cNH2FNx7qcjPh4FFc94brMbpKGCq9V9r8NLQ0HaM4RLe0gcg0sSJElHl2Yf68I9P6VmN9huxb_Rni0DvjZTLmihRy_jNbXDYaffUzqjA01aeXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=TsVDWeJoOk6I_hRS8WM-hcTUqWEYfxloz8zxvdqDlzOw65s6oZWXMHd13gT3P0GipPYTCRii927nkF_TwbuJ4Z-WdI4ivX9oz_H_PRfYd8L4ZlRYwtHyXWI3THMAARAJ4FoVkaE7uzakFZywOiU8JmXvbZCYaMmEeIMbzruka5Q7EKeW0C2uKyoZUAfvsmRoUBbHvEVLrJ7QzW2Smkep0auFv0y8uzmUNAR3F34cNH2FNx7qcjPh4FFc94brMbpKGCq9V9r8NLQ0HaM4RLe0gcg0sSJElHl2Yf68I9P6VmN9huxb_Rni0DvjZTLmihRy_jNbXDYaffUzqjA01aeXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=S9m1QmKFzfeCpzx1xfkbG2a5OQ9RIyawBchYcZ-mOvpNjSALrcUUaH8ptvUHvotOlQOW874ICdXl4zDFW5x6T4YigprZXVVIy_iCYrmLlPUhNqC_xDPZQOOrEh0Jcc9_lwPJ54OtriaEFtrNx5sFgAU_zPeWDAF_nBIK8A7vP75jOPYUm09VdbE5v2dKpLK5yq39l_zqLwE4dX7ircMZC9sNWa30ld3Gd7CyFnt5-FGSD-PAIiuopEqhZwIbyoYazKptxFfvfIEkXevuJBqojvh3oNisPA8pTqLb_s3IO7Z-IWaZZCOD0RkmwcvwiGU7OC48JLUo8hK8SQMIoefECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=S9m1QmKFzfeCpzx1xfkbG2a5OQ9RIyawBchYcZ-mOvpNjSALrcUUaH8ptvUHvotOlQOW874ICdXl4zDFW5x6T4YigprZXVVIy_iCYrmLlPUhNqC_xDPZQOOrEh0Jcc9_lwPJ54OtriaEFtrNx5sFgAU_zPeWDAF_nBIK8A7vP75jOPYUm09VdbE5v2dKpLK5yq39l_zqLwE4dX7ircMZC9sNWa30ld3Gd7CyFnt5-FGSD-PAIiuopEqhZwIbyoYazKptxFfvfIEkXevuJBqojvh3oNisPA8pTqLb_s3IO7Z-IWaZZCOD0RkmwcvwiGU7OC48JLUo8hK8SQMIoefECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
