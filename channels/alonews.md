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
<img src="https://cdn4.telesco.pe/file/P51VLA4qgQyjtRxaVuHC1fmxf2ysBx0m8tIDEcC9uGD0Q_-4blU9TISMfK7KT54DfBTshgea86UDJlh0RNEdZw8WAz0KS7ibSc7MJwiWhpjnm8mQQp7whHO5AGRvX7MlrV_UEi76NoxO7P-DGFF3PjGSu2i3-C-j5gWCyybGBkYZU2YBP_VpZzrvgDYSkwSbfkSK27OU03COijcI-9asCbFtF26Jp64N5uakODyptAwBzX52wHm5iVDfkaLdzWuu230H6IOeIdxh5CqlrLVETzjYcIhR4szb3WRSrQBlPDmssYL8GH_Bw3FfJP1L1EmxZ2ZLWwSOYtDGnOa5pgQSkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-148072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / ترامپ: "باید ببینیم" که آیا ایران نابود خواهد شد یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/148072" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عربستان: ائتلاف دریایی دفاعی با مشارکت ۴۱ کشور عملیاتی شد
🔴
وزارت دفاع عربستان از عملیاتی شدن ائتلاف دریایی دفاعی با مشارکت نمایندگان ۴۱ کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/148071" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری /گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/148070" target="_blank">📅 20:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ در پاسخ به سئوالی درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/148069" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ به شبکه نیوز‌نیشن: با حوثی‌ها در حال گفتگو  هستیم. حوثی‌ها نیز تمایل دارند به توافقی برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/148068" target="_blank">📅 20:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/148067" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjq1dr3eN2ovwZcFnv_Zy88IfecrwyQiVry0OxLHp-KQyWmSa9R12CJvy2zXn2Gr0yyf8w03mhoGQlH6V3F9S5AcbRbXAjVr-yfhxRgRci09_huEFSbU9JUgas-JBhXrcWY7sdtKRXEB8g_y-jYE3B8jci3WPWDslY4z3GaVNxTWiG5s5Aabdoy0UR-IURxno2cboAp3f9tZ7Y_Vp8NP_MU52nhmwdgbb5gvgu9tRizZ2OFkfNB52S0cURotsL-eXjknLDYKzfJsH3joAi_v4cC5P3TzV5EafppGdzesliHjnMAK1z4LKucOMc4i7y0jFWKYHZVxrxpe7ey877X_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148066" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مشاور ارشد رئیس‌جمهور آمریکا: ترامپ مصمم است جنگ ایران را به‌زودی پایان دهد
🔴
شرکای او در منطقه نیز همین‌طور هستند؛ هیچ‌کس جنگ نمی‌خواهد
🔴
او به مذاکرات و گفت‌و‌گو‌ها فرصت می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/148065" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148064">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX2ZnWcCRAQEUqaZ0wVbx0j4ZigA4jVy2PdpUW5x6xbHGLZHrP-epceIWIJqlR6ggMoRykd20m6NicuBwWIFdb-JTSx7L3Wbz0IuHXzYG4Np1CK77ptiFsaJHaEkAIPs4f-Jv1D4dR2LozvNKUNeUxR5dkd7qd4zntaZ9KYUgMxoC0KZGvw4rDrEr3STP-qbZhdo-4W2nqixf0w8QPRmYsSReQQDOckm054yjOEN70ebG0cBQkUeRkgSaZ1j8lvjK6O1FH_BXMOFFmKnO79q2vJmRR0XYaJmXOh3J5CBT-AJnYuzG8pm5JuIzmVLN0FUnzmwAsY2NaOBubmXsMrBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زین واکر، بازیگر معروف ایرانی هالیوود و برنده جایزه نخل طلایی اعلام کرد بزودی به ایران خواهد آمد تا از خاک کشور دفاع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/148064" target="_blank">📅 19:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148063">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فرمانده سپاه: آماده‌ایم به هرگونه محاسبه اشتباه دشمن با قدرت پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/148063" target="_blank">📅 19:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148062">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nt1yM0LWBk7H2whOtqjOplFu9U41L5gedAQI8F-C1mgRaifMWcJGr1IqVYipY4foc7J3r5iMt8by99MxKIkCnVozsCzPJt77Oq4H5-JhVpJzcvMo2kXDPgzQxDIgEhrVv7W_zqptHpbFcNmeAIQVlXzrgHBBkL3PXpTKOT4Tb78NX0GQu_RSxjq4V-4H6bpPTnjS5qejonjymBv4HDR-7d8titsOFg0kpnWKpxTumLEWhji1cnjEAKi0sbR1MevCmqpJbOpAHVyRpgVEYlAFwqZUQE5Yz6HD6dHMxMv7foKVX028xYpOtVzW0OgFrqOoz4uiRNx2bDRUI5IGmJ1WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش از این، نیروهای ارتش اسرائیل (IDF) حملاتی با استفاده از توپ‌های حامل فسفر سفید را در منطقه القنطره، در جنوب لبنان، انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/148062" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148061">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=Fk67hscHpOt9Ea2u2WIzHXBqjqP83n_F_NaOOijODabJBm3pLXcjz0E1RESxcRpQwf0hxFIlalhCizYVCrBvqVMjtGum0wxC6XCuhGLypHH5yBWh737Tbt1IT9XW2Zpc9BHce8AlItERsMve4oWG87xW16YkmMZRMrC7UlZuqSiy8X0h6ejpNE0JSH5C5lKIlDblJPPHVAI16UebQXr0xyqpuXTxhKXhTCoHdO7oNnmU11jQfXrRN27GEhjsqRG9gEvBcfmCx7Rgojf982IxMaFhmuIagoyg5ar5Iwo7EiHjBkfeXoZ1z1uiv3YZ4R5nDj9cPE12xSWICDQFVasQf2j2YD24Trg0hSDXtlzHcrvX7be6TPZgX7t8svMO5DyuTpVb7SuUXTOOJ7h_cLnPQFmVqYZF0zpLqXTAV1TRicjGdaBSm41juCdDWWXjEbNH2eZ2BdU1SMIUsef8QYTIK1fIsz_IBPuCo9iSHnBJ4a2eBESUgdapc6jSF08733sQHRyT9LfkY6YSQQFn_2zfxxY_WHo230qHD8w5shrHv7Mq_7Lcw63P3wotJRY0ynwKvvSBDZco8P6OT-tf_vxZqeaKHRi_EHUZ1sM7mZD3RnYYW_RsI62zoec63FhBU09Gf-RBGYfJI4zqVT8zHEyj29m-ekFpBGLvtTSAvNhh5zM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=Fk67hscHpOt9Ea2u2WIzHXBqjqP83n_F_NaOOijODabJBm3pLXcjz0E1RESxcRpQwf0hxFIlalhCizYVCrBvqVMjtGum0wxC6XCuhGLypHH5yBWh737Tbt1IT9XW2Zpc9BHce8AlItERsMve4oWG87xW16YkmMZRMrC7UlZuqSiy8X0h6ejpNE0JSH5C5lKIlDblJPPHVAI16UebQXr0xyqpuXTxhKXhTCoHdO7oNnmU11jQfXrRN27GEhjsqRG9gEvBcfmCx7Rgojf982IxMaFhmuIagoyg5ar5Iwo7EiHjBkfeXoZ1z1uiv3YZ4R5nDj9cPE12xSWICDQFVasQf2j2YD24Trg0hSDXtlzHcrvX7be6TPZgX7t8svMO5DyuTpVb7SuUXTOOJ7h_cLnPQFmVqYZF0zpLqXTAV1TRicjGdaBSm41juCdDWWXjEbNH2eZ2BdU1SMIUsef8QYTIK1fIsz_IBPuCo9iSHnBJ4a2eBESUgdapc6jSF08733sQHRyT9LfkY6YSQQFn_2zfxxY_WHo230qHD8w5shrHv7Mq_7Lcw63P3wotJRY0ynwKvvSBDZco8P6OT-tf_vxZqeaKHRi_EHUZ1sM7mZD3RnYYW_RsI62zoec63FhBU09Gf-RBGYfJI4zqVT8zHEyj29m-ekFpBGLvtTSAvNhh5zM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد کشتی گارد ساحلی چین با شناور فیلیپین
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/148061" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/148060" target="_blank">📅 19:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر کشور پاکستان طی ساعات آینده دوباره به تهران می‌‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148059" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس:
ما تجاوزات مداوم ایران علیه کشورهای همسایه و تشدید و هرج و مرجی که دامن می‌زند را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/148058" target="_blank">📅 19:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148057">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=Bc9kz94GwKodPmO1ymC4pxHsfe5vkywhELbCSxnyEBJnGBss0jc9AU6HPgWl7e397Mp7GXX-vXYdYqJC_igmlL7UCiW7rbU-hK7aE0FZ1WycUoXZaipYhy1cMxz8ouCGJX5MTgkQDI_fExpaEnGxGHnxgvSUxfF2wXymRD56Q0N41lQP-n43qxyWq_gO_KZ-fmKNgS3tAT4x2sf0hqnGcbbjQsWL-yydBp84rPtjwAAm9YZ6Z1_F9xkFDl5QrMgZr_nRUEbDp8--r0-U6hENsp03nzbYJa-RsKpP6KDaPRe-6GK8dMnG6xMRO1JE1rRyVyrMsJN3PRg1V2aLQaeB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=Bc9kz94GwKodPmO1ymC4pxHsfe5vkywhELbCSxnyEBJnGBss0jc9AU6HPgWl7e397Mp7GXX-vXYdYqJC_igmlL7UCiW7rbU-hK7aE0FZ1WycUoXZaipYhy1cMxz8ouCGJX5MTgkQDI_fExpaEnGxGHnxgvSUxfF2wXymRD56Q0N41lQP-n43qxyWq_gO_KZ-fmKNgS3tAT4x2sf0hqnGcbbjQsWL-yydBp84rPtjwAAm9YZ6Z1_F9xkFDl5QrMgZr_nRUEbDp8--r0-U6hENsp03nzbYJa-RsKpP6KDaPRe-6GK8dMnG6xMRO1JE1rRyVyrMsJN3PRg1V2aLQaeB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148057" target="_blank">📅 19:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTfWZQMpUI3x7hfYss45Co42BEOJNigFGPXWK9yCKSSu96qHGLiR3cjCV-VVJWAC2AtauONN740wSzDecUCly4ncKHf3OJ6NmOD0Ig8QE9UbqXsRUF5a28ziNlAcrgPu5jSEAW-e2WnFNH8vuDKlgh1Xhn-joAeQpSplBOJ586Gwaz-SfWLB79NaoHnWtAMD7-qJoXBvCtwGDl30aBCg_WgRuv-1zvzLwncpNapSifj6BflXXSVjGAMfe7-aTBx3536h3AgLl6iGQH31DGwOZ-zeyZ2i_xaLBIHae6oEE4xhfWPr0iZ9u9P0f47kVN9V1TNdNmEw5RDgJEVbqoOgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkOFnmPDNnFvrVf56tn5e7v8cFo_A64C9umOmbwRgVg6vT3ZHNpkQ9qKa16gY7rYPzgFq56LK59PScbdnA2QlqjD46ujjTMEoW0x6KjV3yp-82B86jVrjCBXpr0zUOOVSIdeER4j44EKdmco0jfZZQdGN1nGFpJ7bI_vlrcY8ri0uUW3SJOOLhjxH-TyRbu2hfbJxR3-qtIXlZhUGt5yIDA_qlSEOuoRzqzkj_AOCX1DGZcgFib61cE4qB7yA5op-uVdUA1EMGXdHh3a7x1WL_XVkrRHnfQFq0rtJjohmIuWpEzzfrynnz7dUq8pTbIsLTzgyxNi0SfXu-ppEgJPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAAHihLFLWcm7DqZ5g99qnX4I5z4pOJkoDq5OrnM0OBjDN3lXLcR0XQFPcUV-CPaRFdDh8WHoxZBhHsStWgX7sXzAUm6mkCUYNcjaPnVkMZPUWc1vKffDx_UwOM7QIBy4keyMHLiNzPIaBMbI9oV8Veb0s-zZsshKrAJCq_zJod13zSrVHnSAgIQyrab-X9BXyAsPY4cwKvNrnWahV4hu1oMJGRcQx9l1NYGYCADZFem-NMT84XodLhQlPqp0AIwaPKWnhaJuRhc4pcF8ejVRX3c2uDa3DTXKBaFxtiqnExfAOlo4Z0zi34Fxm2LD14k5G2dWHdYmlC-NCwCLKwxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKemG9CvrZBPP5mGbbI4cTKGnQ52GlrUfYUS95ewY73nYpuAlrIh5BGByWFQDd0H_H2u5nnxFLlGhN-rcbJjpn-l1i2DgVRh7cS1dPBotreim0yJd4GidBngeCzSN5YKhRUlpO-JFCRod1PXckKi5J2U5wu042uZ2Jrte8nT7Lsf7xXdwQBV2vONBRpUMMOonPBHOullMyxHgOmBT9GLrbYiHcbLkBG07Uk8n1siny2BQHVqjbL5jmRpkc2FPyNy90-HeFR9q3jmR2UCSQRfpEg9n1PsC-3ybW2I5FyM_dSDBEVYVrevTq6WEMDN05a1nuO89EqbCLHCzLMLf9qN9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یاشار سلطانی این ۴ شخص رو اعلام کرد که حدود ۸۰میلیون بشکه نفت رو بالا کشیدن
🔴
۱٬۹۳۲٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148053" target="_blank">📅 19:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=eRILR5P4uWb625CtpcwKJx5m0RudoSMYJBXtef22-HFRpE_SphdaVkuuJUzmVN79LwAYjhHe2MYBmXAlNrt_AFATI5vy588vGPgsAwL8mxam3hmUj2SM5LrBb__sdMz3OZfHGTIFRYcxdyxXLguUoDfM-lrxp0tvufWSJNeSxZ2NeEcR9LSDH0s7WEZcNE_kkR3xP1jvZ7jBuVwC2xLh3bBfBhsM6WRUSHTlXInVTFySgRFto9ujAeCI2zSInqckh3xeamP7KwssTDFN1gZOBa403yF77vopVsQFTsCDNxj5giCY3CGF_7fIvHDt3uG3fbv_D4D7JWMjy21GV6Qrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=eRILR5P4uWb625CtpcwKJx5m0RudoSMYJBXtef22-HFRpE_SphdaVkuuJUzmVN79LwAYjhHe2MYBmXAlNrt_AFATI5vy588vGPgsAwL8mxam3hmUj2SM5LrBb__sdMz3OZfHGTIFRYcxdyxXLguUoDfM-lrxp0tvufWSJNeSxZ2NeEcR9LSDH0s7WEZcNE_kkR3xP1jvZ7jBuVwC2xLh3bBfBhsM6WRUSHTlXInVTFySgRFto9ujAeCI2zSInqckh3xeamP7KwssTDFN1gZOBa403yF77vopVsQFTsCDNxj5giCY3CGF_7fIvHDt3uG3fbv_D4D7JWMjy21GV6Qrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی، خبرنگار:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148051" target="_blank">📅 18:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
منابع العربیه: محسن نقوی، وزیر کشور پاکستان در ساعات آینده به ایران سفر خواهد کرد و در تهران تشدید تنش حوثی‌ها در یمن و پیامدهای آن بر امنیت منطقه را مورد بحث قرار خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148050" target="_blank">📅 18:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIMrAjFgZiyJWnfhXYZp3VXrop2qSKngR6qKrz9G0BkJgvsjNgtl7GOCWBoFfPsbICQy5M-FrdlBsxlHEmvPnnSaGP-csp4p30vhPPbfnRMNy7fk8l1SDTXbnYY4pXomw6KX7k6MlSldisjs3ItmAgCJy9lzM6T0jG8zvgeMnfaSaDjCWx8p5tHFLjdh8MEgnSxB1Ta2h62twzQjNhRXa_hxhFdQxFY1v2oAcp1Heu3RRiegXmhHdE8FPijGUr1N-7n6gBiysNUCKxhPSjw3X70Inv7vDeHYB3Eekz4o9axKZYoCIeN-PA9-IiYqVvPecz60q8MWZ2-4jCrkInWPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: دولت و شهرداری هماهنگ شدند تا از ۵ مهر قیمت برخی اقلام اساسی کاهش ‌یابد و تا ۶ ماه ثابت بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/148049" target="_blank">📅 18:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فیلد مارشال مخالف صد در صدی مذاکره و توافق و صلح بود و تقریبا معلوم شد چرا و به چه دلیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148048" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA_UIspFG0v66S5QrOzjjL3Prj9HCwsm5NGqu4MQbYISFEKaq7iXhJ9L-d0uAqJIK-g6BMcPdC66she-E0O6biVNLCX8DRlLcp2iwTmQAGpAx1iVWbF1PaK6gPVEQW7RV_ufvyVxfTbCtUrfsMqs1pij411eEY5dJ4DgY3MHCkpVyNZolE5O9urD6ISt9VjJMvqKRGwHIxcqCVcaiwBToVSUSyl9wxzezwu9GGlK-uwBq2NIbZioaRKtqCSIOqOtWZcGaD9XdX1ooHiooaBpfyRhlFZ_77AoV1kL35zevRbzZlxsHaQwTVpI_z3Nw3HcRXL7RNFmXAfEFWoWYuG69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148047" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/148046" target="_blank">📅 18:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148045" target="_blank">📅 18:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=PgVUNpT88iY-GdmndyDe8tdpnPplCahUKnP1kUZPB9BpSatGzLXEmfHz7gFvqQTtX5Gmz_hDiP7b7pOP5sBHKnhAPL08OAqAlIi0_YKPVG-Ebw7RSsW3MQgvAJGa13r1kFdXRwCZG3jm9HHYaDWYY7t2Ofc1Wk7kYmPgL32Ag4MQjy_2BgJKFYK6MDkXwlhnYvcBuhoitxCxKC-WEt6s2pTrDUb0aZhmk1N9y9gErqdrRwxoljMYNp-ktysh6LOYHi-uAwhtnuj7wQCxQYONmr1omiPA3XmDbaA7YKF-g7MHnSQOmVXkyJdAo_JczJyKk14q3pP7D1iO5y0XEP7jPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=PgVUNpT88iY-GdmndyDe8tdpnPplCahUKnP1kUZPB9BpSatGzLXEmfHz7gFvqQTtX5Gmz_hDiP7b7pOP5sBHKnhAPL08OAqAlIi0_YKPVG-Ebw7RSsW3MQgvAJGa13r1kFdXRwCZG3jm9HHYaDWYY7t2Ofc1Wk7kYmPgL32Ag4MQjy_2BgJKFYK6MDkXwlhnYvcBuhoitxCxKC-WEt6s2pTrDUb0aZhmk1N9y9gErqdrRwxoljMYNp-ktysh6LOYHi-uAwhtnuj7wQCxQYONmr1omiPA3XmDbaA7YKF-g7MHnSQOmVXkyJdAo_JczJyKk14q3pP7D1iO5y0XEP7jPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لباس فرماندهان ترور شده در رزمایش امروز جانفدا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/148044" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر وقوع انفجارهای متعدد در تنگه هرمز منتشر شده است و این گزارش‌ها حاکی از آن است که ۴ موشک کروز به سمت کشتی‌های موجود در این تنگه شلیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148043" target="_blank">📅 17:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=VPmGA1wyUArE03q393Tv8zfQVAB0wSpouphXhw924cWH7Yiw9VxkgPzokPOkj2mIpNMDsjc8tpODOFdllsbht62N1pdOnFWTEISteQZJRIOyG0XEuyHPOJ4EUUKVJZQ6GZXMcyKY1KzuZ1Ht1AHDV42RqXSK8JXRiHVVOR9ketXIDobcmz9ty_P342OHods-mmnYwEhMvFCClKL-NazQC2fsWpssrbv7nrYHFBmhA-ErFDmBMGCpwxo8OJNP_opYWjn9of8b8JQKY_h0JZF-koT4rSsQ_zey9hlIYaWccjRt2uVCIrfXwgd35VcOj4lcGuGa9FDMvCdggw_qBzmF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=VPmGA1wyUArE03q393Tv8zfQVAB0wSpouphXhw924cWH7Yiw9VxkgPzokPOkj2mIpNMDsjc8tpODOFdllsbht62N1pdOnFWTEISteQZJRIOyG0XEuyHPOJ4EUUKVJZQ6GZXMcyKY1KzuZ1Ht1AHDV42RqXSK8JXRiHVVOR9ketXIDobcmz9ty_P342OHods-mmnYwEhMvFCClKL-NazQC2fsWpssrbv7nrYHFBmhA-ErFDmBMGCpwxo8OJNP_opYWjn9of8b8JQKY_h0JZF-koT4rSsQ_zey9hlIYaWccjRt2uVCIrfXwgd35VcOj4lcGuGa9FDMvCdggw_qBzmF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت صداوسیما با 65 میلیون بیننده روز به روز داره عجیب‌تر میشه؛ یه آخونده رو ورداشتن آوردن توی پخش زنده تا این صحبتا رو بگه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148042" target="_blank">📅 17:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صداوسیما: تا الان بیش از 600 هزار نفر برای شرکت تو دوره‌های آموزش نظامی جانفدایان ثبت‌نام کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148041" target="_blank">📅 17:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQC1fFIMklsOOFiZCnXACdy-Fg5WXezxh_eGizVmVykcTAHQnQNv4mcV0bzKq9JT4Kq0TaoLFX--9ZbRR62fhxPKMadFFpYDfznCP2FC1XNtE4fqBlufmVjswCughbHNqjG0KK4hQMxH96uTA8cTFrgGlSUWLzqeYAmfZQg0cNyA339Az3Sy8G_Gvwg1d_wxI4RQR0hDu0GfuHv1grE8JfU60r1iL0BLIJJZ--kvHBBkKpt7rorA8CDk7Ri4xsvX1jXgwEqKaZPf_SXQ03ebKQLF0oGj5Mlp0xq-fKhKPggCsagAuR9LkQpIELdY-bTyHXffDS_qNHS8N9j6pOUTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبار مهمات در منطقه "ایاش"، واقع در بخش غربی شهرستان دیرالزور، سوریه، امروز صبح منفجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148040" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148039" target="_blank">📅 16:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f37NfM-6Z4me4we1LEB-YmHDci109cmpI_NLD0vVzyXzhh6WXSBxA2upGXa2wVnHPAqsQb_E7SO9S2OvQ2ttZC_EUPJP8_nCWOk0eCC5kASq4Ozou9swhr6UUSZUj6Lp0RjmTOj8Lu6wFTRnWTB7c49cRPRrkSX0Rc73lJnwD5A5p5TyPJHFuHTMMITd7tbWwTrWO3SBmiyiU_eI8P-J0xN1Z3tHhYtQ_dbPi5yWC2FkQ9ff-Voh2Q7xh_ztsd1gZsI4FqRNUIFfcNeUJLCwG5C1jaN1Gh10ecyS6dD-vrfRHLbVPztM-D3ETbNNIeXaAGzmMPRgbq-gQNxEu0WOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کایا کالاس، رئیس سیاست خارجی اتحادیه اروپا: حمله‌های حوثی به عربستان سعودی غیرقابل قبول است و اقتصاد جهانی را به خطر می‌اندازد.
🔴
اروپا در حال کمک به حفاظت از کشتیرانی در دریای سرخ در برابر حمله‌های حوثی است.
🔴
با توجه به وخیم‌تر شدن وضعیت امنیتی، عملیات اسپیدس (ASPIDES) اتحادیه اروپا سطح هشدار کشتی‌های خود را افزایش داده و همچنان وظایف اسکورت خود را ادامه می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148038" target="_blank">📅 16:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / عربستان سعودی از تشکیل یک ائتلاف نظامی دریایی بزرگ از سراسر جهان برای بازگشایی تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148037" target="_blank">📅 16:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
اروپا به محافظت از کشتیرانی در دریای سرخ در برابر حملات حوثی‌ها کمک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148036" target="_blank">📅 16:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا در خصوص سفر هیات ایرانی به آمریکا برای حضور در نشست سالانه سازمان ملل:
🔴
ما اجازه نخواهیم داد حکومت ایران از مجمع عمومی سازمان ملل برای یک ولخرجی تجملاتی در فروشگاه‌ها استفاده کنند
🔴
ایالات متحده همچنان مقام‌های نمایندگی ایران در سازمان ملل، مقام‌های ایرانیِ در حال سفر و افراد تحت تکفل آنها را از خرید کالاهای لوکس در اینجا منع خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148035" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: چین در پیامی خصوصی از ایران خواسته از نفوذ خود بر انصارالله برای جلوگیری از گسترش درگیری‌ها در دریای سرخ استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148034" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه:
«تنگه هرمز عملاً همچنان مسدود باقی مانده است و هیچ توافقی برای بازگشایی این تنگه وجود ندارد.
🔴
در واقع، وضعیت تردد و عبور و مرور نسبت به چند هفته پیش وخیم‌تر شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148033" target="_blank">📅 16:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEEyZu3FIB90QD7p6O-mwvMVITDqi1S6xtp6n9nrJDS3RztckpwnDChsp98yhxSzV6QfftrsNvmfGWihTXGL1Mj0ZIDbq-XpOPRQpmiT540Bj7GMHK1-648g2BgHv2segnnIlQsVfnj3CPQ1raZioddrhDD_vLOkg1i02D661h-EeY9IQ9UqGEZ_72Wyb-p2rlYgG0xtmypUYesO9Y4f_IKCrFXb3phoZsW8V70FKJ13cyNkAOoADC8rwKEJ__KwPo_V6NjhKwgWhZA-PUgAAVsJz176PYty-dFGSSX2B0dNA1XmkS-W7uDxVHUMT_XGneWrMoTVnmGY8xciXaDQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا با قرارداد ۲۴ میلیارد دلاری فروش F-35 به عربستان سعودی موافقت کرد؛ جامعه اطلاعاتی آمریکا نگران است.
🔴
نهادهای اطلاعاتی آمریکا نگران هستند که چین از طریق جاسوسی یا روابط امنیتی خود با ریاض به فناوری‌های حساس دسترسی پیدا کند؛ این نگرانی‌ها همزمان با پیشرفت روند فروش ۴۸ فروند جنگنده F-35 مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148032" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3k2fXxIXizEG7trasyEF5Qt5zr6WRIS4aWVBOeX58cviu7ExjBddEoZoTduFJdUruHPxgExbdJGfO2EbZ7KQrQCD6zLpurlAd-jIJYAK8ru2Q2K3GBmsAgShuHKiXzPNWqSthDlEp1Nrr8FBZjykHT96fIWfA76uZbO-z5dcn98DPXivEQsszWCqsr2PGgYmET2am5SFIMriEJ1CjdOXcd7oKBCIW0YVEO0GbRqzM50YCIn0YPjjuwgw9NrXSWfn0KSy4lSulWQhifvuHlF9Xy102R52sKZ-wVgh5w8PxA8dfTvL62ZNiwBjf8wLetfbdb3R_E1Z1Qe6GP4vqVXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZt2S9Eu_T3WuH5Ul0yOpRA3YXeEBeNAVk3uanJRlimd-bt3_yzK7JR9qONj5Zgqzuk9MM16HRIAmiIieYe2E8xC7LvLRSIeLxY6_D6_xfmvAxqf9DuKhZ3LSinYaDv3rLDlUtvvk0Gx35NjhXophfwRVb8hC4kA6zHnb6Al53j1kPolNVXEYcA54s6ehFkieoAuyqzlcgq3x0wUWM5gXx8sTdaV8hfagzEkcVocqpAX144cLjMqv85DSvWZc5HGNMKNLJIzDISmnyDaauEs6HY4VVLZDAcqDgOJP8VtrCxl9CVtiBC8f9kaT2qvARwvwJAPwRVi3879u_CEeMREKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cA8iq5ysXo2l9PtQQ9GPBdIehy3Eh61VxoYayNFBd38fzPmO00TC9_fdmwXWqe3xtS2NPhWG76CmFOwBOtNr7VJnRETLvrw22tzO3XDO1vOHpR8whHbKAE2GvGHMq0E9jmUPnrizxuU8pzKuc49UdGM6U8Bpbfp6tfNae3vKHfJ9YUsmAXRYUluzNQPprgbElisO3ItJZoeYlCtyDy3rhBX5bsEN9SkezJQ4Kd47YQk3aFLIdGxTsVGhYKIVytMtita1vQv3_VFOeUMweROvZKWsou98Dremg9QGIzoXnCbkEolYjfkDk7GS_5O5l0JjLRjbVkSblBmbukfw0fHQag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای متوالی در نزدیکی یکی از انبارهای مهمات در حومه شهر دیرالزور در سوریه رخ داد و آمبولانس‌ها به محل اعزام شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148029" target="_blank">📅 16:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مکرون: فرانسه در چند هفته گذشته، هدف حملات ترکیبی روسیه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148028" target="_blank">📅 15:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUMlq54iyZouXtf9N4e2ZKQH3CakMNvz1_HENCNR27IdsDqCejz2HSettOmT_QFo04IieHm91PfbAZhAtumBa9LyyzinY70UWwTHCRnR7lzFQnStrt7VVByUp4WnkCRf-QA3Jl4-FqUvXob5U_RPSEN3x0_Ry74T9QGFHE99eVsvXomQgV-qcgWu43TW5Ymfol9lWICLZRrvLs3OtSqjNSxSgGK75RQFVE47ZusuaqW992AktGb7WT44bmMrzECALhIv7KUF57dBwgm_wogm_rAH4fEIZ-rLJvXHVHPui6VuU1y0PepnBVUPbaGMBSM737PFMvp4K8s2mBoyqYIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ: شرکت آرامکوی عربستان سعودی به پالایشگاه‌های نفت اروپا اطلاع داد ماه آینده نیز نفت دریافت نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148027" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرگزاری فرانسه به نقل از یک منبع اگاه: پزشکیان، رئیس جمهور ایران به نیویورک سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148026" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مرتس، صدراعظم آلمان: دوران دوستی بی‌قیدوشرط اروپا و آمریکا به پایان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148025" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: مدارس امسال حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148024" target="_blank">📅 15:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn8PdlJ2TWiJFRWWAJCoMn-ipQlG028UKCwD6_vpb4H9kfcU6io_AVfoiSQk-XDH6IsxJqa3ni7LoU2QdyvtQNeXHmk2uQ_W8QJTaKiH3XeRBDzu4LBqz9GFpZ7z6UliLRbsFhFWjPrAKIOk8ogWJn-3uMBlieOPWAmojq9CtOCE8-VwnahW1gLC6ojYUGLD9CBqY4sK1Q4IOAc6V0Zk-Ic4xYIgkvf3odH8qdk89qMwJnJZPhDvPdnta3WCP7IoL3dhsHedIM51qvp9ShWwgulFFtCfQEsg6HJ3rjyJLH4ahZcufupNiJHpN5gaYXnwISii7i6xc9jLeO9N_y9opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای باری مدل "بوئینگ 767" که از جیبوتی می‌آید، در فرودگاه بین‌المللی صنعا فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148023" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دراپ سایت: تحریم‌های جدید هوایی ترامپ زنجیره تأمین پزشکی ایران را تهدید می‌کند
🔴
اثرات تحریم‌ها بار دیگر به آسیب‌پذیرترین افراد در ایران لطمه خواهد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148022" target="_blank">📅 14:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رژه عروس و داماد های جانفدا تو رزمایش امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148021" target="_blank">📅 14:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بلومبرگ:دو محموله گاز طبیعی مایع قطر از تنگه هرمز در هفته گذشته عبور کردند و یک کشتی دیگر نیز در حال انتقال بار از یک کشتی به کشتی دیگر در نزدیکی سواحل عمان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148020" target="_blank">📅 14:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پزشکیان: با صرفه‌جویی جانفدایان در مصرف بنزین، گاز و برق، می‌توان از توقف چرخ‌های کارخانه‌ها جلوگیری و مصرف انرژی را کنترل کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148019" target="_blank">📅 14:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فایننشال تایمز: پاکستان بر اساس توافق امنیتی مجبور به دفاع از عربستان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148018" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUcHo7EHjpibhKfZbjY4qrSlhFSinNN97woKueG0Tp_ppI0uy8OkeMBr4VmPcbBCWfFjBnOdkcxReCSbDKXXQ4sXHb4hhgsE6c3kzZVpjX_gz8UjZORUX-DySajFbphellRh6wF_wWcml-RZBKFhXL9oO9k_sAEfP3BYmAGn9U0ly4-KWiUfgpBB3keZrbXO-X0KOI4p86_AomctEe2i0YNmvnUDFE8qWsiNB1jNXKPcvCJVpIb9Ezl1AQAQh8p-tlIoTt2PXw6JrRcRXPzDzK2QkI7OtGyu0HZhnZrmEccXbyQbsEAV3_oI_3tynEzMrGT88ZBfkzvq059IiYOpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطیب جمعۀ تهران: تجمعات شبانه به دستور خدا انجام شده و تا هروقت خدا بخواد ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/148017" target="_blank">📅 14:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148016" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: با وتو شدن قطعنامه ضدایرانی توسط چین و روسیه، آمریکا بازم شکست دیگه ای خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148015" target="_blank">📅 14:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFUhikIqHA4CQz1obZPZIm2XokzfVWrSLdMylp-YRDUXDiwbXuEC5h5Ebil9SSALCBosWTjku1BH3_uf28H3CcUP2AHbCE6q-wm-0Xa9SawcVX-J3_DQDq4pacTJgfxtYdTrzGnjqs9DUoBYjd0ET-ObWnWwLoKPnAjVqZTePI6womf5dU_FHkHqPxCASPXm_X5x8uec4JUSMikq64w2RnWpJ5P4ZmktVEoAL4RsTsegTCd0LxfmGmfemeTTgdycdaPaurJmFxWCBEBlV7UpZO9_MvdojRQADkGibWao-6b_rXJcDSm9blA_SPUsHlXiCGU4-hW9uR9-R1uUnwVBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت امروز با قیمت بیش از ۱۰۳ دلار در حال معامله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148014" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148011">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی فروشندگان نفت را لو داد!
🔴
از داماد سخنگوی پایداری‌ها بگیر تا خانواده فاسد شمخانی
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148011" target="_blank">📅 13:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148010">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
منابع داخلی: در صورت جنگ زمینی تمام جان فداها به خط مقدم ارسال میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148010" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148009">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148009" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148008">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXMnhGI13vLBmmAauXPZJYNsy-MoY6HKQHUGMcDU_IXkEQBYr46jAG7vwRnfHAEtupA4Im6r7jYkjAgSE11yApOQzF2JVyQg0_Z8V825ssUHrpef73XQnMn0eL3lVld62dULyowHuCXsJuaAbn64pji-oV3jnFh7eOPlfQN8ZZZ_2q_Zxl2BbsW9w6DR1-Cu9-9UQmJ9po57-KlmpFdWTcr59h_tNs_3zx0TRj9i8rO_q4qlN5-f2NMI_50zbKkaa-JGLhgnhNhBY9_iP_noyK_gAAN1zGxoY4bZNCYwW3tE6zKiNqHgz5S0j6ygunBSEYFmlWQUmyJajnZ606tJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش اتاق جنگ اسرائیل در مورد تصمیم مهم ترامپ در مورد ایران:
⏳
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148008" target="_blank">📅 13:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148007">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciOKOj9l5W6XgA11a-zxJUVJB1sjFFJoPSjcWNyqPr8h9Hv8AGmN76snBYkzUUCbFRlpsMH74LbPG3WRcaFfVxdB3z6m3eD37vH1BEBEoklD9j9ZsaSKOxuSvcbqyfu79a0T3Ut5yWoCb2bOIO_Ri7UY-pu0nnMClJzSCp9qLS4EtOluGQFuBuowJNnq9AcjJsV-lSMnftS5ad6-vSdGV5iekx6s6kVlRp8yjnpPzo5AHj_mLbJxEfxJNHviK7Z2PnaDgR0Xqk_KeeKb60fqJwLrhAY7KFjiC3uo7C_wG6_IIXfTQgjE-jINCVYkIMd-ZwUCZS_8wg_1VsL1fnPIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان از یک موضع تازه‌تأسیس در دیر میماس عقب‌نشینی کرد؛ این اقدام همزمان با پیشروی نیروهای اسرائیلی به سمت این منطقه و سپس تفتیش خانه‌های اطراف انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/148007" target="_blank">📅 13:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148006">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
فایننشال تایمز: ونزوئلا ۴ میلیارد دلار ذخایر طلای خود را به آمریکا منتقل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148006" target="_blank">📅 13:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148005">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1xpm2_qske70rvGChwXONi7k85lK9YI7F5f4ALfgV3H-O2kFSPWbSEGF_aYLucXAknvXK3f8tFEmBuZmfZBN-jljKXTICkbbsDrzQ1xoLIyt1dcUaoaZEv_GpqGf6c1CrSCJW9-LKU19uR9W0NpvG_WiMhLetxyCFKSc43zcIWwLuJu13R1Zls0o54j45SflkWk3HKknJ2uWnjing-bKLp1u4tqz6LCpTNonhlF8BGjTH33uRipx2IZbDPjbV8aShLDfUT9FkEjAKwH7Pf8cn15P-99a9P_Ta4zY5GezU8fl-QYHccKGgaGTnpkBrsOt1bi0xSShnYiNmj-fS-10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
غریب‌آبادی: آمریکا نمی‌تواند با خروج از شورای حقوق بشر از زیر بار مسئولیت خود شانه خالی کند
‏
🔴
معاون وزیر خارجه: تاریخ فراموش نخواهد کرد؛ در میناب، مدرسه‌ای به خون ۱۶۸ کودک آغشته شد و در لامرد، زمین ورزشی به کشتارگاه غیرنظامیان بدل گردید.
‏
🔴
اکنون همگان اذعان دارند که وقایع میناب و لامرد، نه یک خطای عملیاتی، بلکه جنایت جنگی آشکاری بود
‏
🔴
آمریکا نمی‌تواند با خروج از شورای حقوق بشر، از زیر بار مسئولیت خود شانه خالی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148005" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بانک مرکزی ژاپن روز جمعه نرخ بهره معیار را از ۱.۰ درصد به ۱.۲۵ درصد افزایش داد که بالاترین سطح در ۳۱ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148004" target="_blank">📅 13:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33da215b97.mp4?token=HHUoMj14-PVSaaypF4tlVzA6IbKAz-gwdGwRbktIDy2MhqQctEPu2YsGOmHsOj2hEqU-sfl98BegdLCTQ2U4wS9SC62Yp0tyUTKwta96JrFfG7PGuFt7A0kLs79a7c1xePtgnj9ZtJaIp6EiRW8bMnGyOhym5adoinRWcTA4J434m6NgMcJQRLY7CBii_78TBdOFyeExQan0CcKJERYRxYiNweNg8bPr92-7HTWI8n3hGe4aEVPpDrb3CTYhDfeDJP3zSrH6s9PMsqwJhub7Q7iF-M8ZGFCkvShRSPoOUR_0YW5y6ybuRZOFBhlhzcpxBJQY3bnqQS-lpbyyNRWdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33da215b97.mp4?token=HHUoMj14-PVSaaypF4tlVzA6IbKAz-gwdGwRbktIDy2MhqQctEPu2YsGOmHsOj2hEqU-sfl98BegdLCTQ2U4wS9SC62Yp0tyUTKwta96JrFfG7PGuFt7A0kLs79a7c1xePtgnj9ZtJaIp6EiRW8bMnGyOhym5adoinRWcTA4J434m6NgMcJQRLY7CBii_78TBdOFyeExQan0CcKJERYRxYiNweNg8bPr92-7HTWI8n3hGe4aEVPpDrb3CTYhDfeDJP3zSrH6s9PMsqwJhub7Q7iF-M8ZGFCkvShRSPoOUR_0YW5y6ybuRZOFBhlhzcpxBJQY3bnqQS-lpbyyNRWdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148003" target="_blank">📅 13:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انفجار در مسجدی در پاکستان/ اعلام وضعیت اضطراری و احتمال تلفات
🔴
شبکه‌های خبری پاکستان در گزارشی فوری از وقوع یک انفجار قوی در مسجدی واقع در ایالت خیبرپختونخوا خبر دادند که تعداد زیادی از نمازگزاران زخمی شده و برخی گزارش‌ها از احتمال تلفات انسانی حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148002" target="_blank">📅 12:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSyrpVupzrKfRdISVNQNz4xXwG-gPwFFFIdoeuQnGX76T_P5HGAwhb4nKrLk8WTyggr8uUTsk6s76bnWmFvut5RiHR6RWXLQXFyxphRUzKplYcDVg87MUaGG7-cpMdAAUSi0q4fzvRbTu-wNb2JEAgGd9lhvbIJZFSB0Ofoo55vgI-78Z6Xw8KPQQxst8qnBM2LnnxB26b_BWa9gfV1Z54sP5Y4vPohPOEA73YrviemO3WSvCJnnTrEBRCl6zFtad0oblL3PYmmY3bKXuHkMCXjzcWn66EhYbFhV6dgOjmm9NVJe-WMyGBGI0M1xQETt-TPinfi9cew0Ub2b76Ry4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ورتکسا (Vortexa) متخصص در تحلیل داده های انرژی و ردیابی حمل و نقل دریایی اعلام کرد که از ۱۱ سپتامبر 2026 (۲۰ شهریور 1405) هیچ محموله نفتی از بندر ینبع عربستان سعودی خارج نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148001" target="_blank">📅 12:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148000">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر دفاع ایتالیا:یک هواپیمای جنگنده ایتالیایی مدل یوروفایتر F-2000 در جریان حمله به یک پایگاه هوایی در شهر طائف عربستان سعودی، شام پنجشنبه، آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148000" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147999">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lkxhql6-FJs9TAn1udPEMKPtOtCt2SDkUbM1dsRshN7c9sV_U05NqrpFXZO7EtHou-mpwfX_NPLKM1cOig1MAk1UCi06VpyFNAgkJ45qvu5bYE7V8zu-20WSy5I_udevMYXWcPG5ayNWqH7gkcpRo_YClZRkAzdFtSmNfsDrcXUErK5xrA4koF35In7CqJDrJCJilm8x5Xl0SLra-XCdQ8hGZl2FBAvFrOmOg_HDSVsxmEtytfg9IMkiWvbs1hzKB-fYKhOLD6t1G0BuiSPgYzQEkVaOwKMKN_wqzkIzlRmr0Dl9PD9E4dlzUUiByXTdhfPpu5gJ0BBhpyBq27N0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در شبکه تروث سوشال به یادداشتی در واشنگتن پست اشاره کرده و نوشته است: بسیار جالب است. حتماً بخوانید! به افشاگری ادامه دهید ای سگ‌های کثیف! وقتی پیدایتان کنیم، بهای سنگینی خواهید پرداخت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147999" target="_blank">📅 12:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147998">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جی‌پی مورگان: بیت‌کوین احتمالا از طلا جلو خواهد زد
‏
🔴
تحلیلگران جی‌پی مورگان در تازه‌ترین گزارش خود اعلام کردند که اگر سرمایه‌گذاران از لاک دفاعی خود در صندوق‌های قابل‌معامله (ETF) رمزارزها خارج شوند، بیت‌کوین فضای بسیار مناسبی برای رشد و پیشی گرفتن از طلا خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147998" target="_blank">📅 12:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147997">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز به نقل از دو منبع آگاه از مذاکرات اخیر منیر با عراقچی:  فرمانده ارتش پاکستان بارها از رهبران ایران برای توقف حملات انصارالله به عربستان و زیرساخت‌های انرژی آن درخواست کمک کرده و تعهدات کشورش به ریاض را بدون تهدید خاصی به آنها یادآوری کرده است.
🔴
ایران می‌گوید این درگیری بین عربستان و یمن است، اما به نظر می‌رسد که تشدید تنش، اوضاع را به نفع ایران تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147997" target="_blank">📅 12:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش ایالات متحده:
نیروهای آمریکایی باید برای جنگ‌های آینده‌ای که فراتر از زمین و شامل اطراف ماه نیز گسترش می‌یابد، آماده شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147996" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز جمعه بازار جهانی تحت تاثیر کاهش قیمت نفت و تضعیف ارزش دلار اندکی افزایش یافت.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۲ درصد افزایش، به ۴۳۴۶ دلار و ۶۵ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه دسامبر با حدود ۰.۳ درصد کاهش، به  ۴۳۸۵ دلار و ۷۰ سنت رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147995" target="_blank">📅 11:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147994">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkOSKR5uUsJmZa4HMdbr6NsuuDc_VCtM2tI208pp1CV5ZZAOkUFEnI0XuKn4S2veZK60GlBmxRfArV9FqfD5wbCEu5b3LpXThKnY-Ek-bBwoJfjpSkk4yv_ycUNansKdGJ1P21-7l-PHJAVn1PVcd0Xf1-qQRPDuAXTF17UI7pat3Zp4VIL9ix0A1hGMxgHiAIC2nB-XNqdlEsHjLcN4L7MRsMefouHUYGMVBNbWlPD5RRtW51lD7SqPbjd18rd-G_eOl3tzW0aWG_jn2pC3BprW_4KIBZJPaSmoTlxqP65eiDQm0AxJRcco04165FMqKCf9FfVMiTx-MJpg_wikwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران از جدول سرعت اینترنت اسپیدتست ناپدید شد
🔴
ثبت نشدن اطلاعات ایران در نسخه اوت ۲۰۲۶ لزوماً به معنای حذف رسمی کشور از این شاخص نیست
🔴
در حال حاضر توضیح رسمی درباره علت نمایش‌ندادن اطلاعات ایران منتشر نشده و بنابراین نمی‌توان دلیل مشخصی برای این وضعیت اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147994" target="_blank">📅 11:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147993">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: جنگ ایران تقاضا برای ابرنفتکش‌ها را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147993" target="_blank">📅 11:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147992">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رسانه اسرائیلی از آغاز گفت‌وگوهای محرمانه میان کویت و اسرائیل درباره ایران پس از حملات منتسب به تهران به کشورهای منطقه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/147992" target="_blank">📅 11:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هند: از منافع اقتصادی‌مان در برابر تحریم‌های آمریکا علیه روسیه و ایران محافظت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147991" target="_blank">📅 11:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فدراسیون جهانی بدنسازی و پرورش اندام شب گذشته در فدراسیون بدنسازی ایران را تا اطلاع ثانوی تعلیق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147990" target="_blank">📅 11:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تسنیم: در جریان تبادل آتش میان نیروهای امنیتی و چند فرد مسلح در زاهدان، استان سیستان و بلوچستان، چند فرد مسلح کشته و نفر سوم بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147989" target="_blank">📅 11:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔴
سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته که در آتش می‌سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147988" target="_blank">📅 11:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / ایتالیا به تنگه باب‌المندب ناو جنگی اعزام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147987" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ درباره ایران: اقتصادشان در حال حاضر در سطحی است که هرگز پیش از این ندیده‌اند، بدترین اقتصاد تاریخشان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147986" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8836c88e.mp4?token=FNvOjrGGKSEs9l3hZkv4tKwFCXrWinp1Z6a2px6cu5OWST_KrsvWzeNqZljI_rDeQPCeeOuT8I3wfCdxM_8ANatMKJYAEgVw2ALdxOxNpzmHIX0vDm4TXDkr_Eaigb-cRU3hXGpvRj_AKInc8nUBZzvJ_D1gI_UuRN8adwXYUyVN_GmSGgE2TjPcESHz2TVDXE63tgJHchmB-SWFQs0bn2H3zlLmiBvww-bFsI1gjQZdwpenAdWpr7Kg1B3BxLgMirkV_IJgyGF692BlZSR5ue_jec-xNMk0j04bTRpEr-tAIqp0jSuTV435qqUCWWMiIM0ZRVLL0QYetMOoh1VtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8836c88e.mp4?token=FNvOjrGGKSEs9l3hZkv4tKwFCXrWinp1Z6a2px6cu5OWST_KrsvWzeNqZljI_rDeQPCeeOuT8I3wfCdxM_8ANatMKJYAEgVw2ALdxOxNpzmHIX0vDm4TXDkr_Eaigb-cRU3hXGpvRj_AKInc8nUBZzvJ_D1gI_UuRN8adwXYUyVN_GmSGgE2TjPcESHz2TVDXE63tgJHchmB-SWFQs0bn2H3zlLmiBvww-bFsI1gjQZdwpenAdWpr7Kg1B3BxLgMirkV_IJgyGF692BlZSR5ue_jec-xNMk0j04bTRpEr-tAIqp0jSuTV435qqUCWWMiIM0ZRVLL0QYetMOoh1VtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد جاسوسی متعلق به عربستان سعودی بر فراز پایتخت یمن، صنعا، منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147984" target="_blank">📅 11:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nB5K2ShYhBSLBkbnfhwHOD-6qViquejN0SYGQXobD-YBc04DrF5_Fbpl-DVLrU_Cq0iKVDhDKp787oVSNs50XbONcdkqplfaPUlOsnKFfwMe7Im8NfHPsdP9xGY2ueWQniK_4YUqMH_I8Lzwgz4GCyf8ikscODQzpLzaGnqiQxTRwW_BeVUJhmIxX7iuQzf4Ex6fpc6kEXCTC4sDsYgeTq0dNsJVz5l_wrJKyQgDGrq-6Wtu595zLvnV3C9EzKhGn2AiSub15-VPCs4vG6E0VY85Th1qlkcT74rdcNTiCJmVvJaNmK9D5ZerENPIsvDBB26XA3LWU7pI6oubHQtuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش‌چشم: مطلع میگم، آقا مجتبی تجمعات شبانه رو میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147983" target="_blank">📅 10:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
الشرق‌الأوسط: لبنان در حال بررسی گسترش «منطقه آزمایشی» برای دربرگرفتن تپه‌های علی طاهر و شهرک‌های اطراف آن است
🔴
همزمان، قرار است با حمایت آمریکا یک پست دیده‌بانی بین‌المللی ایجاد شود و استقرار ارتش لبنان نیز در این مناطق انجام گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147982" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ و صدراعظم آلمان درباره تنگه هرمز و دریای سرخ گفت‌و‌گو کردند / برلین:
🔴
این توافق وجود دارد که این دو آبراه باید سریعا بازگشایی شوند
🔴
فریدریش مرتس صدراعظم آلمان و دونالد ترامپ رئیس جمهور آمریکا در تماسی تلفنی درباره جنگ در اوکراین و تحولات تنگه هرمز و دریای سرخ گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147981" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147980" target="_blank">📅 10:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147979">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1uTtK-Kf7-BTEKxH_V7NSgdyD1M6AAPRtPMGmbROulUbqEpT3ZwpPJSlvqIE8neephRIRuCwEgDUAu-rfSGR-Ot9sgwP7q3TbL0ILabMtpbihPSNC6sabRa82uSpA3niLy2EqfBQZKzCosWEi9tCHxCgrOiGHyRGdaELv3WWru7eqz3cE1fmV1wf5M77fo-fffJ7G5TuABCpfKt1wV85wAOMRMAAaonwJyF54s-EcjqCD8xfR4ZRkxlzvp2j-lslfz5AiJaViZ8P59e0hG5QHZaiiubvU35WtOy5TlG8CCOPGwpJaXbcsVMXlotyQEfbszUDNuYGkbepOiTv_xvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی(حوثی ها)، سلسلة کوه‌های "الأغبرة" را که از نظر استراتژیک اهمیت دارد، در منطقه "المضاربة" واقع در استان "لحج" تصرف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147979" target="_blank">📅 10:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147978">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد!
🔴
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147978" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147977">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز به نقل از مقامات رسمی:
پنتاگون در حال بررسی طرحی برای خروج حدود یک سوم نیروهای آمریکایی از اروپا، شامل ۲۵ هزار نیرو، هواپیماها، کشتی‌ها و تسلیحات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147977" target="_blank">📅 10:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-mdJ4C1FUQnTtZDgdke4qbVMUZaAJz3bXxCpCCpcXFuENPMDJtkVZiZme0B-69Z3qO4WepK6zm7DUHXcOtSgvFEfUwvUb5lZaQMj01Gygp_tGRhakO4grw-UaR_XMUqXS9VtgHznCIMOKxbY1SnbCHB09MOT1Y9SP3clE4WWfFJAFN469NnazDZgr0lsx_RAMr2zQb5Go0lINkqGMz2oGSOT_6fS9BFiJLaZB5VWJKelnuCpJsrmh8sKYRSt-edguvNkjL50W-EmyAlxNNFCD_gl692Aw18o1waBsZSYFigXz9iLI9VlgkBgSPOftJxVatrl39yzaZ3KZv2GJgKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۱۸ سپتامبر، روز جهانی خایمالاس
این روز رو به دوست خایمالت تبریک بگو
[تصویر تزئینی هست]
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147976" target="_blank">📅 10:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZQnq6ZlXZMc928zrDuQLRI95n7gaTCHHYMhrmEN0R96gGC5Y1owRtoXJcVgkOBMumq6ydVGIrplsT4WgLAgOxNGbo9Zo6_c2N4JkEPmBtbukhrPIF6vhCJk05lpuOOhYN0wwoIa2qeMXhvP3GLDJ5G-riBBzn6iZYyJd0H0JAUiWUh1oqC_frcWxlvWfpD0GKXKMntmF3YHr6wnmdD5RjzjPXwmN5kE0f0p4WZq0FxxoorcHpoUEbKXMr7n53Jpf_Gf_PFa-gMZSTXndIs_ydSvnTuksDekLEL6dHRc_-Mz_FKWqQBtBqpr8Nv21epUYVGOSoqLD0eYRKlBXY0wdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtSwVatCpsHUmtB8gweUMortc7Ut6OyRhwlRLAu2LMMJ3mdyYzDSIvVCa6rys1dGQaBoJyYwONnFJzPCXFrUkOAOxjd8FdT3ERxAdPgU5C6X7qTBo36xN2nz1ThhX-fFlOM2sBKNWHaRBEDib67fFdiJdi-b2Psfpzzdpq3qPq6cMGnfXTbAIgH6GvgudV0tKEFFEtsKgYs6LtSPG1p9uAM82Ts-hYLzQRkbdP9RpsLqp1Rtg2LD1YRkT6jcJyWotCM-ADIVBNF5eMhcjjKBm8UY1Buo-5_EEJO5p5Kb4nmoYHy8Y00ZXierriOHdbTKRx9zQlTgsIpn69-n3_-1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJeiyRfcxBzXsRsNYkJkSU3WHwoMb9Bvpcc5awesubOhWZwxzZSy3q9lnEDtvxRdG5BiQxWbpLiD7c-A9wVE73HRLAkmRf9v3VpLpCW0oB7igJ06MzYr6tV9tRjeq6hAuX-aD1OKM-rGnZ5sfYOE5Zx_DrIpG81V6ci5x9MP3bMUPMwTMod4aIs3pjRYX63u3lOr3jhmK0S_kWHXyBicEm-Y0oUzkrqWvtzzveTVxlskNnLNcJCHj3MKP3RmYLOxilJPXT94P07ojBa9V6EaY2H_QAd1UjnD_5Vwxi0Mf5ZXi1UouvsCiPwPy-150Lsw1p3eNh4POHYGbE-NyjfsbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انتقال تجهیزات نظامی آمریکا از عراق به اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147973" target="_blank">📅 10:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
مقام سازمان ملل:جنگ آمریکا و ایران در ماه اول، ۱۵۰ میلیارد دلار به اقتصادهای عربی خسارت زد
🔴
این خسارات معادل حدود ۴ درصد از تولید ناخالص داخلی منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147972" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=AYbxYXfDklL2bxSsI8T51WBDKMV7jbEQsLJzkm78HqpeorYWSQ1MkjPI5rnRCyJiIdCGiasH3tcxfWk_GesatYICv5V1VI4W6kEsJboBzmVGiDbFwK90uGrmZng9cxe0UXLbb39yiwpQrqyY-2Hj9KTFVS5C_smUtaOIEnj2LsA6EwJ3wiqqTuL5kcNTjRmkI0EIPJTAB3nxW2l8sOqM2STGSSDU0v3nEHmnHPngKogEywNxQiABDq4b2Rp-bgPyKtjNKwM7Zn8afwT7MC5Sg87SXjEfms1kxTNftspYdSLKh-dXYOULDaCmZHS1T2EBhHAXMAiNyDOiASO4lgU0OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=AYbxYXfDklL2bxSsI8T51WBDKMV7jbEQsLJzkm78HqpeorYWSQ1MkjPI5rnRCyJiIdCGiasH3tcxfWk_GesatYICv5V1VI4W6kEsJboBzmVGiDbFwK90uGrmZng9cxe0UXLbb39yiwpQrqyY-2Hj9KTFVS5C_smUtaOIEnj2LsA6EwJ3wiqqTuL5kcNTjRmkI0EIPJTAB3nxW2l8sOqM2STGSSDU0v3nEHmnHPngKogEywNxQiABDq4b2Rp-bgPyKtjNKwM7Zn8afwT7MC5Sg87SXjEfms1kxTNftspYdSLKh-dXYOULDaCmZHS1T2EBhHAXMAiNyDOiASO4lgU0OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: تا هر سطحی از عربستان دفاع می‌کنیم
🔴
ژنرال احمد شریف چودری، سخنگوی ارتش پاکستان، گفت اسلام‌آباد در برابر حملات موشکی و پهپادی حوثی‌ها به عربستان سعودی، از این کشور «تا هر سطحی» دفاع خواهد کرد.
🔴
«پاکستان کاملا در کنار پادشاهی عربستان سعودی ایستاده است؛ هم از نظر دیپلماتیک و هم از نظر عملی. ما تا هر سطحی پیش خواهیم رفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147971" target="_blank">📅 09:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رئیس‌جمهور کره جنوبی، لی جائه میونگ، گفته است که سئول تجهیزات نظامی را به خاورمیانه یا تنگه هرمز اعزام نخواهد کرد، مگر اینکه این اقدام خطر وارد شدن کره جنوبی به جنگ با جمهوری اسلامی را به همراه داشته باشد.
🔴
با این حال، دولت او در حال بررسی امکان گسترش نقش کره جنوبی در حفاظت از کشتیرانی در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147970" target="_blank">📅 09:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
صداوسیما: هر شب بالای ۶۵ میلیون بیننده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147969" target="_blank">📅 09:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مشاور ارشد ترامپ درباره تلاش برای پایان دادن به جنگ با ایران
🔴
مسعد بولس مشاور ارشد رئیس جمهور آمریکا در امور کشورهای عربی و خاور میانه مدعی شد که دونالد ترامپ برای پایان دادن به جنگ با ایران تلاش می‌کند.
🔴
برآورد رئیس جمهور آمریکا این است که جنگ شعله ور شده در سراسر خاورمیانه به زودی پایان یابد و وی برای تحقق این موضوع تلاش می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147968" target="_blank">📅 09:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ادامه روند نزولی قیمت نفت برای سومین روز متوالی
🔴
قیمت طلای سیاه همچنان بالای سطح ۱۰۰ دلار باقی ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147967" target="_blank">📅 09:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: داده‌های اولیه نشان می‌دهد که تنها ۴ کشتی باری در روز پنجشنبه از تنگه هرمز عبور کرده‌اند که نسبت به ۶ کشتی در روز قبل از آن، کاهش یافته و بسیار کمتر از میانگین ثبت‌شده در ده روز گذشته (حدود ۱۶ کشتی) است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147966" target="_blank">📅 09:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: ترکیه و پاکستان هیچ کمکی نکردند، آن‌ها فقط می‌خواهند سلاح بفروشند
🔴
«از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147965" target="_blank">📅 09:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رادیو اروپای آزاد/رادیو آزادی (RFE/RL) گزارش داد دونالد ترامپ ممکن است از فردا قانون «تحریم روسیه و ایران لیندسی گراهام» را امضا کند.
🔴
این لایحه پیش‌تر برای امضای رئیس‌ جمهور به کاخ سفید ارسال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147964" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld3hkFVJ8k0l8lVj8iBLZCPQ_wXlQkJrCtLT4qtXv6biIvhzoazJGQyWuEPqqwAhba6oNBNmiKDZ9QsAJ2IW9tWgLfW80wR-poElZY60K8BlIF8DXWeIct6e8JsfkLxUVDs6TEIGwuJoKaboCDhO1u1pzgxiBUX5YmIpKCvv97O2AGGTrsDeQwSTnYmSVUBfoAcyil_RK7hoKrTuW6IgNpHTr_IjI9QsUZBjZc9ZJoxqeV4jFEbmmrxEJTlYhEjY4jEAma1oGR1ZLQX_siJmkkUbyHFnfc_x5xt9osUeAH5-OxljG1lYe9wUsBrrNCIy7K5foZ46KxJo00JkkYjXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/147963" target="_blank">📅 09:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نظرسنجی شبکه فاکس‌نیوز:
اکثریت رای‌دهندگان آمریکایی معتقدند ترامپ استراتژی برای پایان دادن به جنگ با ایران ندارد
🔴
۶۰ درصد نیز اقدام نظامی آمریکا علیه ایران را تصمیمی اشتباه می‌دانند ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/147962" target="_blank">📅 08:59 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
