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
<img src="https://cdn4.telesco.pe/file/GxKcpdktsIiDvt-fsU81J4jZq-TNfLdMFPeUMGbwaArZ_tPGUruJFFoij4nuMIeQOJ26nULM2vda0lN7VpZ9Mebm77hGmVdwI1JWJ6Ltll-Ubm2qNT8O-fP07p2rYEG7UfkTogE4HFivSk_97IGEmad1gZuOC71TtUThnSKtRiPwrTCuSr_VFIwjTIXd92xQsrHAPZk3ICHjuzN8jXGG23-pEs2AyiKdGrzqqSlqgaJCDH7sVZ-iabJKnvyuXW48qMsgaaWKOzcjbH4pfl8GUMLdwPYunL22u9EqO2akNFWME5fRv1wo1UGltxmKnkiDMkZnSOgMxLktJP_Cp04xTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-93195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">لحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام
من مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط - 10 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/93195" target="_blank">📅 20:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
مشاهد للناقلة النفط التي تعرضت للاستهداف بلغم بحري.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/naya_foriraq/93194" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇦
‏وزارة الخارجية السعودية تدعو المواطنين الذين تأثرت رحلاتهم أو تعذّر وصولهم إلى وجهاتهم نتيجة إيقاف أو تأخر بعض الرحلات المتجهة إلى مطار الملك خالد الدولي إلى التواصل مع بعثات المملكة في الدول المتواجدين فيها، وذلك لطلب المساعدة وتقديم الإرشادات اللازمة.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/naya_foriraq/93193" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
الحرس الثوري
: استهداف سفينة في مضيق هرمز بلغم بحري.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/naya_foriraq/93192" target="_blank">📅 20:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93191">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7241acac33.mp4?token=qUKOyF2w4lr1PmOp_ucGD9xyY6sUn57hCuzEBiFpPK9CEzXqF3HQ1b5JWONCFm5EIp5TvomVk1_HpDArwyzjcfAczBqonEH9ZxrhXdoxsY7yHv4wzsxk2bDAA0WzVU96K03e5jG-v_VUSPi0S43swPXhwuKgZS6bOtG6i3W8IoCq7wFjPEtP4EsScbmFHdoj4NgCfh7u0wJpWcvtwKAcydjmL87AOZiCGlKd0D5FWJMPlACwx3dplPxp3rc9_8yleOORhz2WXEayahI8jJqJXSkGeK8Bz59bugRm6aNPEyCE6H_iJOgxcf3Ja2WVQC-jJUINi8bNLJgpJ43DZdWdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7241acac33.mp4?token=qUKOyF2w4lr1PmOp_ucGD9xyY6sUn57hCuzEBiFpPK9CEzXqF3HQ1b5JWONCFm5EIp5TvomVk1_HpDArwyzjcfAczBqonEH9ZxrhXdoxsY7yHv4wzsxk2bDAA0WzVU96K03e5jG-v_VUSPi0S43swPXhwuKgZS6bOtG6i3W8IoCq7wFjPEtP4EsScbmFHdoj4NgCfh7u0wJpWcvtwKAcydjmL87AOZiCGlKd0D5FWJMPlACwx3dplPxp3rc9_8yleOORhz2WXEayahI8jJqJXSkGeK8Bz59bugRm6aNPEyCE6H_iJOgxcf3Ja2WVQC-jJUINi8bNLJgpJ43DZdWdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: لقد مُنحت جائزة نوبل للسلام لشخص لم يسمع به أحد من قبل. كل ما نعرفه هو أنني أعتقد أنها معادية جدًا لإسرائيل، هناك شيء خاطئ في النرويج، اسمحوا لي أن أخبركم.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/93191" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93190">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
تسلل طائرة مسيرة من جهة الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/naya_foriraq/93190" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93189">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba43f57de.mp4?token=lwdGG-k6E99p51FkqO0ZyseAEbyFCiyFJYA5342kTX6a5vYpmUNmgVy-g_PurQunUWxmaa_0P96__JS1j8bscQMcJwOhL8uSz0mKQTfzQ463BcwdQumyzDFojw7wru4jkcWsQQECjH5lAjpKCd-YtzOpvPJkH9K8HpoR0TnCYE__BuoHqCnxYraWOxOADbRm2xGaU2ImVzQlzX6tJGStCPCYPRt_NL3gQhVhupS-5Pn0K5cNXnm5zKL_lddBADXqbKdvRN6uUaq1KtMws79ZoVe6tDAtsorpZR_DghIchldqwC9dQWfLAlAXxunl3KwqYE-F_1etTgyWDSs8oW7VH33gpFzuw5pFqFkQKJJOYH5c_F31cLpIr6pbHNy-YkxJVxLxjo-Mr8MGdauRtuwgKuKOaMCFknHUtrkowI0nSSfkYOtSO8Ft2ObmqgTvwyO1Ac3sb3qeq5jLZpoJbJnwcWniG-kJJsPu78T_9NmaHgoxRZtRUcdzl4HaXaorlPokuqJVjI0iSeZCv4gsqM_-lS_WeW0YdhaKEa7dKfh-pwR3r69So5908SoY2IgTuXVI1vbwaZD82pLzo-rUeDe4fxZYvBXhWu_cFwLbzpyYOCHX3-7pFHbVj_G8NaSOnX34cTGQoJV1nLg1KVX8kJtqcJ9xTUrlAcw8qhL7ENsLeg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba43f57de.mp4?token=lwdGG-k6E99p51FkqO0ZyseAEbyFCiyFJYA5342kTX6a5vYpmUNmgVy-g_PurQunUWxmaa_0P96__JS1j8bscQMcJwOhL8uSz0mKQTfzQ463BcwdQumyzDFojw7wru4jkcWsQQECjH5lAjpKCd-YtzOpvPJkH9K8HpoR0TnCYE__BuoHqCnxYraWOxOADbRm2xGaU2ImVzQlzX6tJGStCPCYPRt_NL3gQhVhupS-5Pn0K5cNXnm5zKL_lddBADXqbKdvRN6uUaq1KtMws79ZoVe6tDAtsorpZR_DghIchldqwC9dQWfLAlAXxunl3KwqYE-F_1etTgyWDSs8oW7VH33gpFzuw5pFqFkQKJJOYH5c_F31cLpIr6pbHNy-YkxJVxLxjo-Mr8MGdauRtuwgKuKOaMCFknHUtrkowI0nSSfkYOtSO8Ft2ObmqgTvwyO1Ac3sb3qeq5jLZpoJbJnwcWniG-kJJsPu78T_9NmaHgoxRZtRUcdzl4HaXaorlPokuqJVjI0iSeZCv4gsqM_-lS_WeW0YdhaKEa7dKfh-pwR3r69So5908SoY2IgTuXVI1vbwaZD82pLzo-rUeDe4fxZYvBXhWu_cFwLbzpyYOCHX3-7pFHbVj_G8NaSOnX34cTGQoJV1nLg1KVX8kJtqcJ9xTUrlAcw8qhL7ENsLeg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من داخل مطار الملك خالد الدولي في الرياض تُظهر حجم الدمار والأضرار التي لحقت به جراء استهدافه من قبل قوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/93189" target="_blank">📅 20:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93188">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇾🇪
حزام الأسد:
في حال انخرط الأميركي أو الإسرائيلي أو أي بلد في العدوان علينا فلدينا الكثير من الخيارات للرد.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/naya_foriraq/93188" target="_blank">📅 20:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93187">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81359a42c.mp4?token=MVGszKJGnMtk4B6VxNDXTvOYwinhJanlRssf0g7Tng1vFQI_c0xHloWy7rC9cQ_6C30DAqnLi2KzVkteI7VdMpODgwtl3hlAvZuigEhoCsbAS95OmCc6xQqh7di5tgvlrloXcLib7Nv3pa55LBXtEenOhUqtJ0XC0ULlZ158MpbMGrsSA6wVyaNI0bHeC8naXIyPD6tWmrX44Ym-XFPkRbc2i8xfSC_HImgjAWqZyKiFBJM60UUeCxxUaIJ9huaaA9ejPB55UbLKSqYilxeRctOs0IFX-7xYeVJ8rrU2w3lCFUh_sBeDw9Ihg_Iz_hXH9MVK4o2uj2kJ3yTmW_WeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81359a42c.mp4?token=MVGszKJGnMtk4B6VxNDXTvOYwinhJanlRssf0g7Tng1vFQI_c0xHloWy7rC9cQ_6C30DAqnLi2KzVkteI7VdMpODgwtl3hlAvZuigEhoCsbAS95OmCc6xQqh7di5tgvlrloXcLib7Nv3pa55LBXtEenOhUqtJ0XC0ULlZ158MpbMGrsSA6wVyaNI0bHeC8naXIyPD6tWmrX44Ym-XFPkRbc2i8xfSC_HImgjAWqZyKiFBJM60UUeCxxUaIJ9huaaA9ejPB55UbLKSqYilxeRctOs0IFX-7xYeVJ8rrU2w3lCFUh_sBeDw9Ihg_Iz_hXH9MVK4o2uj2kJ3yTmW_WeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
ترمب: علمت للتو بوقوع هجوم على مطار الرياض وسأتخذ قرارا.</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/naya_foriraq/93187" target="_blank">📅 20:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93186">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fa8a96af.mp4?token=guB9qtwn2BdGStGYzcqGxjSANM3EID0qqjpZMAIIUcrqMGsedTT0fyXvYvGleH0Lltpe5Rn9ZB_oez6VqMEI_t-Qy-qt80Wg8AtsgcLrSm-bzhsDS2mal_OPhaXOj5lNvekRV0jYQGfNa6opwnJQ_OF5ZzHiVylAoJx5cRgIkK4T1qHoeMSN1D3H3AXwDWmNfbeRe5IoTKim56r9xw8Wz_HxTYN2vD6mxQc4nEzipA_bGNyDL-9Y2fWdcq30GRppqkhzoLc5wiTs-SktdCw0Gmb3lDwb1mkEP5iBfevyzjFPCkDcXGmuxPw3noKYMdxKktkpGbHJoxPG65M8kzPCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fa8a96af.mp4?token=guB9qtwn2BdGStGYzcqGxjSANM3EID0qqjpZMAIIUcrqMGsedTT0fyXvYvGleH0Lltpe5Rn9ZB_oez6VqMEI_t-Qy-qt80Wg8AtsgcLrSm-bzhsDS2mal_OPhaXOj5lNvekRV0jYQGfNa6opwnJQ_OF5ZzHiVylAoJx5cRgIkK4T1qHoeMSN1D3H3AXwDWmNfbeRe5IoTKim56r9xw8Wz_HxTYN2vD6mxQc4nEzipA_bGNyDL-9Y2fWdcq30GRppqkhzoLc5wiTs-SktdCw0Gmb3lDwb1mkEP5iBfevyzjFPCkDcXGmuxPw3noKYMdxKktkpGbHJoxPG65M8kzPCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اترامب
: يُريد زيلينسكي إحداث مشاكل للعالم. إنه يريد إحداث مشاكل لمزارعينا من خلال استهداف مصافي النفط الروسية."</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/93186" target="_blank">📅 20:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93185">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
🇸🇦
ترمب
: علمت للتو بوقوع هجوم على مطار الرياض وسأتخذ قرارا.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/93185" target="_blank">📅 20:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93184">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ec687fad.mp4?token=CoNn-7G8XarJbjGJVFQsucwf5sILcnMyLZErR5ZXatpBhVNATzxIUpcBhiWF0X9bl6lPGh20EHSCBZ-vjDpF3uDBr5PQCL8KCtx8BkWWz1J4O6ObvUcO0x3n9VSYeD08iF4QdPsAzX8IzJjaVwFm3cVyNYS7ILIbkKSJ6rne406880gkc0BaFGvnxqanG8U7i4Bh3ADim5Yz_MO_Qbo9Go3TAiHu0V8zCeeXrKh8ynL53E_jKo6p2bUdm1wHE_kGVtY59HL1-LJDm2LhDom1iyAb6YuUh3Y6goNKyiPkI5Q_BP6l3E62T1Y_wO4FZvppWP6dFohSvNPNt3O2uAHL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ec687fad.mp4?token=CoNn-7G8XarJbjGJVFQsucwf5sILcnMyLZErR5ZXatpBhVNATzxIUpcBhiWF0X9bl6lPGh20EHSCBZ-vjDpF3uDBr5PQCL8KCtx8BkWWz1J4O6ObvUcO0x3n9VSYeD08iF4QdPsAzX8IzJjaVwFm3cVyNYS7ILIbkKSJ6rne406880gkc0BaFGvnxqanG8U7i4Bh3ADim5Yz_MO_Qbo9Go3TAiHu0V8zCeeXrKh8ynL53E_jKo6p2bUdm1wHE_kGVtY59HL1-LJDm2LhDom1iyAb6YuUh3Y6goNKyiPkI5Q_BP6l3E62T1Y_wO4FZvppWP6dFohSvNPNt3O2uAHL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
طيران المدني السعودي: تعليق العمليات التشغيلية مؤقتا في مطار الملك خالد الدولي، ووقوع عدد من الإصابات جراء الاعتداء الذي استهدف مطار الملك خالد الدولي بالرياض، والعمل جارٍ على حصرها.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/93184" target="_blank">📅 20:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93183">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇸🇦
طيران المدني السعودي:
تعليق العمليات التشغيلية مؤقتا في مطار الملك خالد الدولي، ووقوع عدد من الإصابات جراء الاعتداء الذي استهدف مطار الملك خالد الدولي بالرياض، والعمل جارٍ على حصرها.</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/93183" target="_blank">📅 20:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93181">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af19485143.mp4?token=Tlg0Kuj-W3eP5OS4_HMA_gQ_257tKauf57VRZfOsf5MivPKrzpGFtWj41YZ0XxoT_tOKz1hu3Ncmcigrd4axynPuj7obQBL7FwYIjjcdbnq444Vo7ZW8w8SjqDhUUDwJDdotJP_QCH09tAXTkRY79DtzbDvqLnWkt6KqJztVtQ6bgWcfW8nNHG6sLIFVOK3-oqYHqGR1KMiCW5gfMBQs-GEHvfxBZv0N0EifF_CFUTtZX2-P-58GWehpIU6NNPorV9XhVsq6Y3yycRlprlAyYV9rYKAUDy5JvQQ8Yh1g20YO3e85NarGKz4Fkm5tuRwCKPsPiBSB34kKLy7ciIeI_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af19485143.mp4?token=Tlg0Kuj-W3eP5OS4_HMA_gQ_257tKauf57VRZfOsf5MivPKrzpGFtWj41YZ0XxoT_tOKz1hu3Ncmcigrd4axynPuj7obQBL7FwYIjjcdbnq444Vo7ZW8w8SjqDhUUDwJDdotJP_QCH09tAXTkRY79DtzbDvqLnWkt6KqJztVtQ6bgWcfW8nNHG6sLIFVOK3-oqYHqGR1KMiCW5gfMBQs-GEHvfxBZv0N0EifF_CFUTtZX2-P-58GWehpIU6NNPorV9XhVsq6Y3yycRlprlAyYV9rYKAUDy5JvQQ8Yh1g20YO3e85NarGKz4Fkm5tuRwCKPsPiBSB34kKLy7ciIeI_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد لمعتمرين أُلغيت رحلاتهم بسبب توقف الرحلات في مطار الرياض بالسعودية إذ يناشدون القوات المسلحة اليمنية السماح لهم بمغادرة السعودية بسبب الوضع الامني المتدني فيها.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/93181" target="_blank">📅 19:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93180">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف المجمع الحكومي في سامع بغارتين وغارة على نقيل حوره بتعز.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/93180" target="_blank">📅 19:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93179">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/93179" target="_blank">📅 19:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93178">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇸🇦
الخارجية الاميركية: ننصح بالتحقق من حالة مغادرة رحلتكم مباشرةً مع شركة الطيران والمطار. كما يُنصح المواطنون الأمريكيون بعدم السفر بالقرب من الحدود اليمنية.</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/93178" target="_blank">📅 19:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93175">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APH4gmClvo6Hdy7Sb20KA0z8hjOG8n7qx1ZN4jQIEhHkBgGoQlFC212HDLifi2AROtkFXWqUlrgcU7KaHOHl215AhoFE-J8fRF4ElD92thYRb1RY42TE8XahxOErrEvP5CtoaLwaGi4j2ocpU3x8avtjJyG-oqCEb4pWLQvYoCPmmCO6_q38YXMJdUbj0Hk4PPYnXqaNnlkmijeEGOFlF6dDg-X_JupfEltRfPVuaNTD30MCst7v94imr2KmsdVqHdvbbandQTqZ0kVdNtIT2lZMU-KTdQaqFBIEAm3yr8XmxVfm9KjU_tYyCFJYwQo636SbcN-M5In0myATKS7mPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESEozKIoF6k5EOW63Wh7NESWs_QUlzKXYXAD8u_9FGa8mazpsx_dAJDuty8ed0J50WUQTgRQG6OQ_GNziW-Alsph_QKIpDTTKWLLDX4_fwdj9L5gBNz9wwH4Q8cv-XXFJPATjvrmsGA-EbntCeIVVVSSVOV-aqY4O2y7nEcxP7MyJf5Bwn_A_Q9dkf0nq0SByUhz0dF9W2DnX4JHELqPm06bAQGtmcVv8s5-lFQ0i7TH-wQ0_l2aUes522Gf0zGCwLfPcHViAHag-ZBsm8w75RJBdiNmSzwgoEjz-4LsgIjOmnNIUE2IysoxuXSxrn6JMY11PrBXGlvSSloovO8olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkvNULyXpfGCd1AL8mijC5ovzdRHyw14NUtP1su8hPy1U34i4YeK9KSrlBcRqtazDkNRRu89bCzile0nwHCfC8-7J8xmbkSlAgXAFMwdVVsEL39Cxu6RM3cVz9V9zmgs7OhCKMkFK2XTvw3wJ420w10acMcU4TzavnYCFSTQR3FuT4XrdZ-qWRHKVfXdDb2HREx26nOl7nSTeABoi28U8ZkD6kyjqgKfRAGUUm1ftX07P5e_F-9jWDU85U_tgAv-JLWQk6fXNi1AsyMJumttw2XuRU3VRPW8k6P8mpT9qniysiBETf9Zp5YBFJ6EWvDF4viA8M7ZsWfekR8I-Kq1fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسبب التصعيد السعودي...
🇾🇪
🇸🇦
يعاني المعتمرون إلى بيت الله الحرام من صعوبات في العودة إلى بلدانهم بسبب توقف الكلي لمطار الملك خالد.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/93175" target="_blank">📅 19:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93174">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط ولحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام - 10 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/93174" target="_blank">📅 19:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1545c2b0d.mp4?token=gp3_N3XC5rpe-87_DqVzbUxGDJHtmPStrRUVEge-ZIdWpTzpjbiZxUo9Hz4grB8T3J6F0pn5gvwDNhgkQgmRB-FG42gnjJ6VoSi2Xi53h4o4mqPK8Nu17PcaU_z0mu1BZYdqsM9U3IW_X1iZKtvWdkhZf4v8z0wcPqp9w0LvcmC9Wtw-GQK-9Rt_LFlWf5jmJuKy3f8X71tBKaVHY618JxWBzUo59e1xjOuIq1gLyNIhTZ64i0HaskcntvRyUq22wluwPddaRmM0gs-ZPNkhuiSVwKw1t75WwAr6cktuFKzHeMpaT3l_au-udeM4ZENXv_2xZqsJsayPPOUBlUmQkbXM1Ic05wAqlRaVG-aNB2K30WvQNRavNE2wd9lnDNXB-Y5kgUXcSYyX2CkHaCEvemySzalQEFgLKtugEy_37XaOihmkdAlW01-5oOdcJnHszyiPGPqr9ISmPV2oxRgm4sshxHj6qCtnAxujvdPvlu9bjpz-Y2eWxCkP_zPOhwcHfq2Mj4CWFH3aNo_LVj8fG0LWPnEPQMiDgW4OibMunzJ3qGc7mbtWlvzEM_V-SvuMB6JH2QULh1t-e6vHfCQLyBsfXJPI0T16s-Khs4HkvPkjb8vO_LpSrH9ZnDSfmUM-bPuHzPK_xb30u2-Zg0Z5FSlXN9rDQg4zR6AJ2nQI6vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1545c2b0d.mp4?token=gp3_N3XC5rpe-87_DqVzbUxGDJHtmPStrRUVEge-ZIdWpTzpjbiZxUo9Hz4grB8T3J6F0pn5gvwDNhgkQgmRB-FG42gnjJ6VoSi2Xi53h4o4mqPK8Nu17PcaU_z0mu1BZYdqsM9U3IW_X1iZKtvWdkhZf4v8z0wcPqp9w0LvcmC9Wtw-GQK-9Rt_LFlWf5jmJuKy3f8X71tBKaVHY618JxWBzUo59e1xjOuIq1gLyNIhTZ64i0HaskcntvRyUq22wluwPddaRmM0gs-ZPNkhuiSVwKw1t75WwAr6cktuFKzHeMpaT3l_au-udeM4ZENXv_2xZqsJsayPPOUBlUmQkbXM1Ic05wAqlRaVG-aNB2K30WvQNRavNE2wd9lnDNXB-Y5kgUXcSYyX2CkHaCEvemySzalQEFgLKtugEy_37XaOihmkdAlW01-5oOdcJnHszyiPGPqr9ISmPV2oxRgm4sshxHj6qCtnAxujvdPvlu9bjpz-Y2eWxCkP_zPOhwcHfq2Mj4CWFH3aNo_LVj8fG0LWPnEPQMiDgW4OibMunzJ3qGc7mbtWlvzEM_V-SvuMB6JH2QULh1t-e6vHfCQLyBsfXJPI0T16s-Khs4HkvPkjb8vO_LpSrH9ZnDSfmUM-bPuHzPK_xb30u2-Zg0Z5FSlXN9rDQg4zR6AJ2nQI6vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مبنى رقم 3 في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/93172" target="_blank">📅 19:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/93171" target="_blank">📅 19:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896cc7541e.mp4?token=tAcu2SA5KHsSC50XN7N9j0hJQum10ywoazDPz7v55NDJrbJA2LmEkh1c8GqmkMy1g8OSpSGvkaSXtRBKJxc-hikqjAthLiWgl1KTBwFzGsEYCOrQO82Hl579FMZKPlOZZUp_2mBLJxjpVKxcWI9joUmfN0DDtKfE_yBcuc6UxlihNUJdYac5QH_LTf9Atw6LCpwHxX6oDiapvFuMgoBylAPg8jasqVoncTTP2vACuGsLrXLLuC4k-rxK5q2BDIgWolRhihK7gXjdwV5cjFRjINfKEX_E-QuNqvxclkKxR0kFqCH1psikt_VzNueNUSjxHWeNDb3rmmFGWb7JdN2vzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896cc7541e.mp4?token=tAcu2SA5KHsSC50XN7N9j0hJQum10ywoazDPz7v55NDJrbJA2LmEkh1c8GqmkMy1g8OSpSGvkaSXtRBKJxc-hikqjAthLiWgl1KTBwFzGsEYCOrQO82Hl579FMZKPlOZZUp_2mBLJxjpVKxcWI9joUmfN0DDtKfE_yBcuc6UxlihNUJdYac5QH_LTf9Atw6LCpwHxX6oDiapvFuMgoBylAPg8jasqVoncTTP2vACuGsLrXLLuC4k-rxK5q2BDIgWolRhihK7gXjdwV5cjFRjINfKEX_E-QuNqvxclkKxR0kFqCH1psikt_VzNueNUSjxHWeNDb3rmmFGWb7JdN2vzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انتشار قوات الجيش اليمني في محيط مضيق باب المندب.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93170" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر
انفجارات الان مجددا في ضواحي العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93169" target="_blank">📅 18:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEQIHYvbegc2NB23M0pSDk2oIibqV8UVMR-SlRiLWCf7OeAfPlw86yuEoU9wRxgLYRBqXmCoaOUeH_8w8zzosrZbmRgeesTmgwAU-18OLgL5ghdGl_htW2Qaw8Z5U5dyjFpYd5r3GBqo-RddQk8rfazP0ak1WSu7zIePqsBdMkYSf0yKWNa6gXFCIWd18a9FZd96UAfV4Qa20nUzHZFs3MVWOW1uL8HaSI5G0hUwUuK1EXB2EETqoFb9_9GbwgXikMZOPB8231bkFhW7MxdejNTkqjN-EfHhYqHiVmAeU8ByoBgi1vsFW0_oxW3Dvqa3yhz7KKjGAzJ4RTbzkTYiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ألمانيا وكندا وإسبانيا توصي رعاياها بعدم السفر عبر مطار الرياض.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93168" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مبنى رقم 3 في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93167" target="_blank">📅 18:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01f09c652.mp4?token=qVPL3tW0g8V1hzr17VGUjzEilXDB6jWwycbXfk0GXTgBMzktSGypShZ9JfbhMoK4GTuBf4DNFp0ZqPliAbSGFrDwdSfWzWQuvHmnvvNuPqR0ctk9lmV0bAYCFInqI6bCXPx5tG7HNM2Xq_gkIgfOiJK9t8Faa14qvpSHarYTiUkdYYCkuNhBpxBmp833NonlyNk5tUxTNRSmaqCppPU8NfDwr1-t80MBFPGpSUwR5jsZUuKsI-C0K99fDaMDfKyauhUR8mm1Rwio6ywUsqKXiPkmW9Jn0LVW8F4n8lpUzaxoGkzBRwKnJacB0e_87c4TdCFnC5Wg3NDysY30An774Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01f09c652.mp4?token=qVPL3tW0g8V1hzr17VGUjzEilXDB6jWwycbXfk0GXTgBMzktSGypShZ9JfbhMoK4GTuBf4DNFp0ZqPliAbSGFrDwdSfWzWQuvHmnvvNuPqR0ctk9lmV0bAYCFInqI6bCXPx5tG7HNM2Xq_gkIgfOiJK9t8Faa14qvpSHarYTiUkdYYCkuNhBpxBmp833NonlyNk5tUxTNRSmaqCppPU8NfDwr1-t80MBFPGpSUwR5jsZUuKsI-C0K99fDaMDfKyauhUR8mm1Rwio6ywUsqKXiPkmW9Jn0LVW8F4n8lpUzaxoGkzBRwKnJacB0e_87c4TdCFnC5Wg3NDysY30An774Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاعلام الامريكي: تشير مقاطع الفيديو المتوفرة من مطار الملك خالد الدولي بالرياض إلى وقوع وفيات ولا يزال العدد الدقيق والوضع الحالي داخل المطار مجهولين، لكن لقطات تحققت منها الوكالة تُظهر وفيات مؤكدة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93166" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الاعلام الامريكي: تشير مقاطع الفيديو المتوفرة من مطار الملك خالد الدولي بالرياض إلى وقوع وفيات ولا يزال العدد الدقيق والوضع الحالي داخل المطار مجهولين، لكن لقطات تحققت منها الوكالة تُظهر وفيات مؤكدة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93165" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">النظام السعودي يقرر اغلاق مطار الرياض</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93164" target="_blank">📅 18:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93163">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">النظام السعودي يقرر اغلاق مطار الرياض</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93163" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93162">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">القوات المسلحة اليمنية:
ترقبوا الساعة السابعة مساءً مشاهد تأمين ما تبقى من مديريات سامع والصلو والمواسط ولحظات تسليم مجاميع من تحشيدات العدو السعودي للقوات المسلحة استجابة لقرار العفو العام</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93162" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43ab69053.mp4?token=Io9dJ4fi-BvmWmWqxGbUpdWneU7_0yEknmLk4ZTrd2HArMjmyY6HZzTkwKeLxcLlvm4lpjX6jb8Qk0FwdsL3s265iSKT8ahQFkolBfZEDwYd8tmbMK7OzUNwnjibBmh4uPEr5KStphQg8G6SITgZ-jr7heloJXjR1nTUw3t34VugMTk7-_vk4Ei2ovaoM9lxJCvz8xl1BSbhaEhmOKw1qLa7lRQhaMpApnMiSOjTQajKxVIUJvU0oQ2XbjAJtkhxBpZgNVlKWfzsLWepK0wfcBi8azs7He5yOxM2Iy_jZ_xNpHwUlM3TCvABuYP3b50rabad-MzROTqIZN9Twa1Wcg25OzPbmgtlfmu2VDXfnliqIxkvaE0hlJe9hk8KR-zEAM1fZ6iJLBqG7RPoln8evGJG51SvmJi3rBzhsF4OPerH1q3vTtw8N8l8vmC20NVQf_v7sBFBmiH-2-8PnogxlkHzcK5HFinGDtLh23ewXrt7Cpc81oW5HP1fXkFHJiOs_-K9FuzP3ypCUTZo3DjV4uEcC8hWe6G_pkGSmvxs7ycvqJt7f64nCDOPkq7-QIt5XLO5ETHzvNbWeBiogYWVqYbUyCHUbFDuv3mpG7rtfPJZHDsN-dN1Tt1QoL8yDLuZ-nlH3bLmRsPjUilX88egdZ0k3Gtg_pgPEsOeIG3pZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43ab69053.mp4?token=Io9dJ4fi-BvmWmWqxGbUpdWneU7_0yEknmLk4ZTrd2HArMjmyY6HZzTkwKeLxcLlvm4lpjX6jb8Qk0FwdsL3s265iSKT8ahQFkolBfZEDwYd8tmbMK7OzUNwnjibBmh4uPEr5KStphQg8G6SITgZ-jr7heloJXjR1nTUw3t34VugMTk7-_vk4Ei2ovaoM9lxJCvz8xl1BSbhaEhmOKw1qLa7lRQhaMpApnMiSOjTQajKxVIUJvU0oQ2XbjAJtkhxBpZgNVlKWfzsLWepK0wfcBi8azs7He5yOxM2Iy_jZ_xNpHwUlM3TCvABuYP3b50rabad-MzROTqIZN9Twa1Wcg25OzPbmgtlfmu2VDXfnliqIxkvaE0hlJe9hk8KR-zEAM1fZ6iJLBqG7RPoln8evGJG51SvmJi3rBzhsF4OPerH1q3vTtw8N8l8vmC20NVQf_v7sBFBmiH-2-8PnogxlkHzcK5HFinGDtLh23ewXrt7Cpc81oW5HP1fXkFHJiOs_-K9FuzP3ypCUTZo3DjV4uEcC8hWe6G_pkGSmvxs7ycvqJt7f64nCDOPkq7-QIt5XLO5ETHzvNbWeBiogYWVqYbUyCHUbFDuv3mpG7rtfPJZHDsN-dN1Tt1QoL8yDLuZ-nlH3bLmRsPjUilX88egdZ0k3Gtg_pgPEsOeIG3pZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيارات الاسعاف تهرع الى مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93161" target="_blank">📅 18:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597af4f32f.mp4?token=JFDkQtXX0qD5jsJhKTzc3KDlFuo1Iy2rSpPT6rTXFizwHeoGDAboqkWB1CtlpmeODwSFsSeCHCC3-8T7CgD8KgGqYcukkaoYhssVgzAEXrNOJeEPuCsXoRREyZcmMeq5LVtO8UbDdGQNh5Vwo_GkjSrQWnBIjTnM_1YkUh44zfTLe9UEgxBbzcHsJjwdLtK76Mc_3cE7FiqavrKBlrZG0Fer8wp2ohouDqTZKt-fWmnPnauFJYkND9BEbAxEEel1cgmq9eI7kPBHz26Paqb9cMGdBtJVrcDCZjwaiLaSF-BlFgInkx3qpFkvrJKBwOSGjr77QSyntPKBPpCluhYvkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597af4f32f.mp4?token=JFDkQtXX0qD5jsJhKTzc3KDlFuo1Iy2rSpPT6rTXFizwHeoGDAboqkWB1CtlpmeODwSFsSeCHCC3-8T7CgD8KgGqYcukkaoYhssVgzAEXrNOJeEPuCsXoRREyZcmMeq5LVtO8UbDdGQNh5Vwo_GkjSrQWnBIjTnM_1YkUh44zfTLe9UEgxBbzcHsJjwdLtK76Mc_3cE7FiqavrKBlrZG0Fer8wp2ohouDqTZKt-fWmnPnauFJYkND9BEbAxEEel1cgmq9eI7kPBHz26Paqb9cMGdBtJVrcDCZjwaiLaSF-BlFgInkx3qpFkvrJKBwOSGjr77QSyntPKBPpCluhYvkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدماء تملئ مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/93160" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a34b53cb9.mp4?token=AJGhj0h7Cmb85-MQ83bFza7hgBROdQLa0OzOXXjcXJhwXmZm1_VqTIsOzayl2iCPlxpIcLZg5xWuI4J63k5OH7rjeNcrGuD0jBYd6dXM1Cl63uTp5VT3VNaOX6Rl8QK6sejVhlO5murnPIOSvT00gJjGmU2rPh9CNiX0fwZhMbIR15xC1jucSONtBuaJ8v6z-W09FyFuHwv8TKIMMDtxRrwKcj2iVbpgkktjm67CJg3Iq1CL9aQmmBFPDCaIXesWjiIxz_PyKB3DiChE0drXUnj4R6db-Bhu4J4-6psLIqWtOBGqzybzHPqQprjBNIOO4xEFbdg_Lt8llgRao8HerQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a34b53cb9.mp4?token=AJGhj0h7Cmb85-MQ83bFza7hgBROdQLa0OzOXXjcXJhwXmZm1_VqTIsOzayl2iCPlxpIcLZg5xWuI4J63k5OH7rjeNcrGuD0jBYd6dXM1Cl63uTp5VT3VNaOX6Rl8QK6sejVhlO5murnPIOSvT00gJjGmU2rPh9CNiX0fwZhMbIR15xC1jucSONtBuaJ8v6z-W09FyFuHwv8TKIMMDtxRrwKcj2iVbpgkktjm67CJg3Iq1CL9aQmmBFPDCaIXesWjiIxz_PyKB3DiChE0drXUnj4R6db-Bhu4J4-6psLIqWtOBGqzybzHPqQprjBNIOO4xEFbdg_Lt8llgRao8HerQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدماء تملئ مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/93159" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nmx4-JLlIKVacy_-1UMcP5n8PHYussuI64XFdCNkeutWE2i4JO2HxS_-J5P65ufwlINLTnZzxQb3rTjuSCSnwX_Grgj4wNq5-UdmPFCXgAK8K4L7BSHA4AJ_Bm7lruG_QDWaZzwqZdx_qOnfgZTKmaa2jvbPmfBGHyANhUHAMFyaN-RaBS8GFxAF3EgH5_69NKkxWZ5QfF9T6ufQX_z-ExHqi13rQNDcoLcId9L3c5jSKugx6LgIA5q_gc_5LoLyjd6Q7BJLDle90k4As4v-fU4Q2-wFymMnM2Ya1LQQf9IyzgYRsKuHSvmBn4b4h0k2NtDux8Nhp3mq3Z6afCazTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMkZ2dE5o-8DhK7A4GFCaV_xZA4I3nsboC7lIkYRcKahhiOemLEx-4guiMoucKGZLB3gNVB5yOBVqWjPHzA7gEROIKipL162XvAcTz8A-Ou4UvbD1M9ps77xqVfaOOGNgkK-irYzeMaV3K8lz-bANfucDNzqCficZV4Ektfg3xt69FN6ceD453a3P5Mck8OeVBkJOQLMRBpRxrWZ1p89PWn4zzeXUn0llO1clG-6erV4ilJOYaKosvGFrSHak_u9Ifq-FjwSGiu4aBmmtPhubv7i3VovKna_hNBgQqVdw51xx9Uj_kBIQuptwFfpwoh0emIn0f62wjS3UqjC8UmW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8HuNpr6wGUz_fZgxMkvhnf4Rqn8eq6XzSFB3gI1xUmHOf2pxODKzW1vpHgS8I4dgxzeQM23voI2m2i2PoP7erDY7C7-4xpQTXSD60a58FMu0L9Wf1iQZQkjSZ2JMRkKwvLeCysm9756zF7mcHhtn2wgtj5Y0_tGmL4gh7kcyZXjAd0rQ9orvFNt1as05LBD9EyHasbX5dbgwdFx8IiB-EDznK3_n1W44KnTPkBqbr6ibi9bphichfUiWTJMYRro49Kb5GQnsjAojoI_g_G5LlxUwHGFLDWPs4Eom0FDawCGvOeFTupFsZGXKm7G2h6CTVoHVYLBpvM3qw_Pd0TlIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اضطرابات في حركة الطيران فوق كل المحافظات الشرقية والرياض ومكة المكرمة في السعودية</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/93156" target="_blank">📅 18:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هبوط مروحية طوارئ تابعة لمستشفى الملك فهد مباشرة في مبنى الركاب رقم 3 بمطار الرياض</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/93155" target="_blank">📅 17:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ova0BAAwMpgMCklzOvYUqsRq_OVrwybphPCw5nV6mpK4C2Hu1x9kw_enMouCnJUv80ZozDIYzOH03btHkGi5TMjY5XtDZrlAjis8bktZCLkGsG3hPAVASC3bbpy8QTSGMrQWKmizHNxgpqSXGQ_Cyi5JO6uFWm-38pGzQYHxVRZRLVdPu4SZJuDAaFyC7AacLJnNnMqMZ2cWZYLIQ1_SOVSeq5LokKQHh_h_Ws4GZfNRkAZhSZkI2gxVN22wyhnUtgRDT9EYLv8DN8yno7KmcksE78mPz7VRpfv5mEovDYlf8B_a2C5xCxBPmjWt3yih4cR8KKNi0shB1dc19u549A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسائل اعلام: وقع حادث سقوط ضحايا جماعية في مطار الملك خالد الدولي في الرياض</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93154" target="_blank">📅 17:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اخلاء مطار الرياض بالكامل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93153" target="_blank">📅 17:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnXFT9-2aOvM4GxF9vtLhH8p2dIz6aX8XgUeZyrsiVPg0crwx2BDjT4nO2V6sARDs7Ryoi-odwwEVDLam6Z7636EvO0BO3lVuHVCziQTTIkvqPF7Bian0_LxpjIi8tpHXL_TQgVP8GhHHfKXg_Lx_BXYJPDojKh0cOce8MXJng1hxZcGDeLryw8xyd0Pzr5JCgZt5lE0Gfas5ScSdxgnCQfuwfiCF7zzLz48NiwktYi2glhJK3zpYpFf318tp2FQrKYxf0gxpxfeFaayHgteZRaCblD2WMbUjhdgE7di-jry_guP4NJcab9awsSbQa8BA-qiam6lpkZY3upeAfmaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخلاء مطار الرياض بالكامل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93152" target="_blank">📅 17:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhbqgZDa6EH1upwWlBmuuYKO263MvX3GaJTn5ApPvoivlNBXGGISl1V-RjSbVIWup2VaU6cJjvRNWpcSnZri-Y4SegdiTj7xltBG_nH36YPbMGwiaNOU-9dueNi4yXR_mKV2n4nRtIltxTd8KbIqBo0ylr4pP85iGjE3ofttsej28Awi2HYaIdskFYH96sqFMPM56B2GawtGvLdv0sS6MNXusVzyHHYndwyMbEPAgbiHBLLIrdARiTkR8GF7iTEnCJz5WcKfJtAEkGc5R__kYjrYSU5id25W-9YO6QfmKg_yAxgceTqBeH6ajE-Zd6xBQH3Qj6xZzQWRoFZMLtrgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sd2C80t7nd-3GG5vWHEsLew9HXrUGZ-w3THa2aLmJEAe7n7epfSZhUqVn73BgIih-Nf0VUbfZMMK5kOoALnCgv9In1VemdYCqJ8qVZTZGAqpWO-Iu432B3ai5m6Shn00E5b0dg6j5F44L1zCPJeZY_NBAcahoa4duhawDKCi7dD0GL9F3X2hZxVTcRNhN4t2AVtACRUIH8dLn0yNOgM0B75B-Y2Yt1eKywR1PLt-0xOMCJBoBeNH-zsBETO8T2puTJ_tx0tIEJFk63CAtmcdCkzL3Um5bEfA-zPaWTkeiGtBjN9q6cW5MwCK8EoBRASz72ZPkwaKb4fdjuC5UG_blw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الاعلام الامريكي: نشاط مكثف لسيارات الإسعاف بالقرب من مطار الرياض. يقول الشاهد: "الدماء في كل مكان"</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93150" target="_blank">📅 17:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اصابة صاروخ يمني في مبنى رقم 3 في مطار الملك خالد الدولي في الرياض</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93149" target="_blank">📅 17:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">النظام السعودي يخلي مطار الرياض</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93148" target="_blank">📅 17:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">النظام السعودي يبدأ باجلاء المسافرين من مطار الرياض بعد استهدافه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93147" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طائرة اسعاف جوي تتجه الى مطار الرياض لنقل قتلى وجرحى بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93146" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">القوات المسلحة اليمنية تسمح لطائرة الاسعاف الجوي بالهبوط لاغراض انسانية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93145" target="_blank">📅 17:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">طائرة اسعاف جوي تتجه الى مطار الرياض لنقل قتلى وجرحى بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93144" target="_blank">📅 17:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_K-SLZKd4b1HuLwUoTKljNMi58ge3I7Wkc1-jKYmKfTgFMo_NcsA2EsGO8cCnXRIaphLqgEy6gegeyLZ1UoTb2ece8YS7GtjkjiXeteIEzsFTh8PjSXVp6sosLLN9CSD8asNUNGhQtIQ3o27_bLYr3A9JycQEGacKiRJFjT5ZSBTGZ5pPhWy12C5b1EExbBa6iT7byQoJqAMLS7sHxW1mEbB5EgD0s-bCSXO4KY3p3BiXlm0eNCKqW3hEx7p75AtDdR_Y9JRXMk0PntmxYFgFbPtRw4uSY_kl4pVAKtqlPqSZmuxXMpYhho9R8d3gPCQG9iRLmLbE9H1dZSyCdKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار الرياض الدولي: نود إحاطة المسافرين بضرورة التواصل المباشر مع الناقلات الجوية والتحقق من حالة الرحلة قبل التوجه إلى المطار. تقدر تفهمكم وتعاونكم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93143" target="_blank">📅 17:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
مصدر لنايا: عدة طائرات تتوصل مع مركز تنسيق العمليات الانسانية في العاصمة صنعاء للحصول على اذن للهبوط في مطار الرياض لاغراض انسانية والسلطات اليمنية تفكر في الموضوع.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93142" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
🇾🇪
بأمر من صنعاء.. مطار العاصمة السعودية الرياض مغلق الآن أمام عمليات الهبوط وعدة طائرات تحول مسارها إلى مطارات أخرى.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/93141" target="_blank">📅 16:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzpeltlb2ogOKsoG5qTCHNj5yRBDu5TMqA4J2xnjjvNPUzoNrU0JQsPxhqBfyt2CGy7E-2c6x5-59m4au1f7vzzySf1-29cnS47rRi1ulbgMVJAbO9-fs2IHVSHfO9gXLqnP40bd13_N1Vs85XAyWQa7UcU21tdD8-JEdpGQ0Wjh9MR-7BVV71vJ9zO06kPjKyjuJotFNEbc_3KLVEsa3TkvZUB5qVN1RFE3f1gvLeefH9dK9AEPfX9bLpvRlD3O3G2O4EkBXXzlQswQiTlyHrQgiDCXufFqSBXFr3g7S7l-JbpMUN7bSdX4YsRvtVQjzLqzm4utHErqqF1xCnPCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يتم تحويل مسار الرحلات الجوية المتجهة إلى مطار الملك خالد الدولي في الرياض إلى مطارات أخرى بعد استهدافه من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93140" target="_blank">📅 16:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4665d17238.mp4?token=draRfPMyTV5QWjOfw5V8uBgcnyXilQTarj3EoXpigs3Ut9ufsJmI7WrX73O2j_IWJPAe29XJ3AjostppQbxR4Mm6qd6Pkn9TLAwR9mFAre7t-ORTAe8aGydF4U1OmRl3BZXX-QcHK6OCUce-FeNMfpDjJnDgzftYAFxDquxgA_F9cDdcFmYNAcP8it4BZXRQOUWufVwtLmx92duiUr-KJlFxSKXoFkweP3RmltSl8pv3gJB8PWtY-i7KmSEnSZ4zxelPYEawNED5s5oFTnvGUi81a9Bc2dsE06SbQNI-GZ6Q3j-bYa_-UwkB8wPvX_HuM55buJHvZuLhTB3TToVLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4665d17238.mp4?token=draRfPMyTV5QWjOfw5V8uBgcnyXilQTarj3EoXpigs3Ut9ufsJmI7WrX73O2j_IWJPAe29XJ3AjostppQbxR4Mm6qd6Pkn9TLAwR9mFAre7t-ORTAe8aGydF4U1OmRl3BZXX-QcHK6OCUce-FeNMfpDjJnDgzftYAFxDquxgA_F9cDdcFmYNAcP8it4BZXRQOUWufVwtLmx92duiUr-KJlFxSKXoFkweP3RmltSl8pv3gJB8PWtY-i7KmSEnSZ4zxelPYEawNED5s5oFTnvGUi81a9Bc2dsE06SbQNI-GZ6Q3j-bYa_-UwkB8wPvX_HuM55buJHvZuLhTB3TToVLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
عاصفة ترابية كبيرة تدخل الحدود العراقية قادمة من الاراضي السورية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93139" target="_blank">📅 16:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سماع دوي انفجارات في مطار الرياض</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/93138" target="_blank">📅 16:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات تهز الرياض الان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93137" target="_blank">📅 16:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93136">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز الرياض الان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93136" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93135">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">القوات المسلحة اليمنية:
مشاهد لاستهداف تحشيدات العدو السعودي في كهبوب والوازعية بطائرات شواظ الانقضاضية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93135" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93134">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750f6280c3.mp4?token=sINnDGpb8OPkC3GNh9OwHevQTg9kalu7NGkgnW33X4hIo95sIhry0HoCw9WmShom6vyAmD0vgtz5RaaHLR-TBaap7t5jyC96DKiZdp9wqvAcKECZMmB1rQq4zARF_SfFaf9P6pFcGDU2zu4YyZ1U_5-_1dmgakx5xzXrfYZuPZfVERxvsvTfddJDmWk49dFE132hpjIOvg8YDutgxoFzXmUnSmZFzWcCjNH-LqgevplWtwbeg_pxyKSxK1hMNoHPV-Q_J-NsX8opA6GYTGoTI4Nw931wVvEhNX7bqzIIStiTmCuTtaDpg7hwR8CgWNyf8-Pe0dDP0Xu47vvDGpri8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750f6280c3.mp4?token=sINnDGpb8OPkC3GNh9OwHevQTg9kalu7NGkgnW33X4hIo95sIhry0HoCw9WmShom6vyAmD0vgtz5RaaHLR-TBaap7t5jyC96DKiZdp9wqvAcKECZMmB1rQq4zARF_SfFaf9P6pFcGDU2zu4YyZ1U_5-_1dmgakx5xzXrfYZuPZfVERxvsvTfddJDmWk49dFE132hpjIOvg8YDutgxoFzXmUnSmZFzWcCjNH-LqgevplWtwbeg_pxyKSxK1hMNoHPV-Q_J-NsX8opA6GYTGoTI4Nw931wVvEhNX7bqzIIStiTmCuTtaDpg7hwR8CgWNyf8-Pe0dDP0Xu47vvDGpri8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان مجددا من المنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93134" target="_blank">📅 16:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93133">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhIajvkLlmexNEO8oMgYUAQzoW8yidfvs6Fj1lzZqbHpBCEJJBSrz_gEdN0Sp1GJYnrY-MC9hkhl0VcSX_pqS7EiQX1HAebmzpnbcuteRGqClpYdk-_COe0OxRkfgo-xFpULbLdKSwh7Y6x9a9xpZBUuRD_Zqx_Plydm_Q2E7NicomqankixDZRbMTIO4ba1plaFnS1ce-98oIvmIh64JtyNeQb7OSk_8k_NJQ7JYm1XWxr1jh4y0ZmXRYUyM5woNd7WTD5z1o_2P4uQeJk3Gcq5D_sykS0ocbuSH6aHf8W6AGeustVvoDtZ-CSh02Vv89crS5vP7BStUV__bev36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان مجددا من المنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93133" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93132">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🐖
ترامب:
رغم كل ما قدمته، لم أحصل أنا أو الولايات المتحدة على جائزة نوبل للسلام.
غدروك يا شبل الاسد
😄</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93132" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93131">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عدوان سعودي على مطار صنعاء الدولي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93131" target="_blank">📅 15:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93130">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انقطاع الكهرباء في كييف بعد ضربات روسية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93130" target="_blank">📅 14:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93129">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تسجيل اضطرابات في حركة الطيران في أربع مطارات سعودية: جدة، والرياض، والأحساء، والدمام.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93129" target="_blank">📅 14:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93128">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHGesNeq0gN280tcFmSPW5GLx8N8uV_7hcRvdzGesh4zpKB5D9fvmPHMxvRqq5EAnBj1cLDdnWJZ53jVvJGB46lll1dswNhb6Lev2w7qu13_9z13Z-ysYdUYFwtyaRTXoZwQMRDBQ5YeDDPjRWDQbGZDD-1qDB-Pw0OYqpvV9dnoEpMDZZSKc9qQuEDimF6Tu5XbatEsog5W09CizuiSyl9SEibJi8yYlfPAzJws9yUD0RjiQaNgWuSqIQyAiFlqNXBUUZ_WQWsTDJ1ozdz7s77ONEa8swyMj-7e16_T3zGFxutN7slZHG3GsRTrP-goDMrNwpPgZ3C6kPpfkuYI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسبب فقدان الامن في الرياض..
النائب العراقي السابق ظافر العاني: ولدي وزوجته والأحفاد كانوا هناك أثناء القصف وقد صعدوا الطائرة مستعدين للسفر إلى القاهرة فتأجلت الرحلة لوقت غير معلوم، وبقوا في أماكنهم. إحدى الضربتين كانت بالقرب من مدرج الطيران
نايا تنصحكم بالسفر عبر البر ، المطار مغلق بامر من صنعاء لحين فك الحصار عن الشعب اليمني</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93128" target="_blank">📅 14:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93127">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef27bfce7e.mp4?token=fR9Ebkb1OFEfH_14-5RqC9FPJM3TBtw-kKEZ4O_cnarNPrRCjRUXICVQAt9ISkrG6UpoFoJKFpDCBuOszdXcxZL5aDXP0WGADIraNcy7KofmA_lzdk0yjYSQ4Mmtoxg_bBXXTZh7r3id_KgJFAsS56Xq-xrD4FX8R76wqERTaJKbA0FJ-cxzmML7G9VrOVO7DFr6vtcSso0gGdgcF23QXESPX40dPulUmPyTluePbfVZLiQiVT-wq5C_u9j8EnjUQZhj769NjEdx6Lb2zvsla7gAWBNXdwYr3DVxNDTbzeAUGrnmHKwHLq0XrCH_Ku8m0I8DFqqFQg_1ww9YNXyn5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef27bfce7e.mp4?token=fR9Ebkb1OFEfH_14-5RqC9FPJM3TBtw-kKEZ4O_cnarNPrRCjRUXICVQAt9ISkrG6UpoFoJKFpDCBuOszdXcxZL5aDXP0WGADIraNcy7KofmA_lzdk0yjYSQ4Mmtoxg_bBXXTZh7r3id_KgJFAsS56Xq-xrD4FX8R76wqERTaJKbA0FJ-cxzmML7G9VrOVO7DFr6vtcSso0gGdgcF23QXESPX40dPulUmPyTluePbfVZLiQiVT-wq5C_u9j8EnjUQZhj769NjEdx6Lb2zvsla7gAWBNXdwYr3DVxNDTbzeAUGrnmHKwHLq0XrCH_Ku8m0I8DFqqFQg_1ww9YNXyn5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي عراقي كثيف في سماء محافظة كربلاء المقدسة بعد وصول رئيس الوزراء العراقي للمحافظة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93127" target="_blank">📅 13:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93126">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
الخروج من العراق يحمي قواتنا من الميليشيات إذا تصاعد التوتر مع إيران.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93126" target="_blank">📅 13:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93125">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdJef_ZyvFEd6U3fnyEmxBOOUpRHIksAG2cjmchiIhzUiftQn-XIz5wICfHJjkfJP3MdV3kUrOGTkzTb_kbKS11Aaw1eAZVftHk3GbNNaVYrD7M80sl_xJFHa5HedciTvePwq64QnKhajz8_pZvuEHgZczmJJaI1qwVAjo5uulSwbkMBGMXFV8b34PyKcf2IsV7ZnsvLN9-wwgS-MPhCvVLvOuHSE6t0hQNDPlg3EebxM1ciZXIt5G9OlyPUQcygRBhUfaMng3e-kBEFRT9Vj0oEHKpLR_GPyr15_ixcP4ElKjy41T7yPf8oTLeyiyf9CeBPOJmoDlzt71H2Lnedyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد الإرتفاع الحاد..
سعر الدولار يتراجع أمام الدينار العراقي في أسواق مدن إقليم كردستان العراق.
100 دولار = 163,000 دينار عراقي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93125" target="_blank">📅 13:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93124">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇷🇺
🇮🇷
🇺🇸
الكرملين:
بوتين نقل إلى ترامب بالتنسيق مع إيران وجهة نظر طهران بشأن إمكانية التوصل إلى تسوية للصراع.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93124" target="_blank">📅 12:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93123">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
🇸🇦
عدوان سعودي على محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93123" target="_blank">📅 12:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93122">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93122" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93121">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnh2COScOPEsUVRxWS_YVIRPi0FOzPmEb892MaZKYQvVYY62vJb-G7FXHAPKrCdHmuEc22atnyszM4JRmyJDq7M_Bjch6RxsVlJUtJ4-wgRlqR16oy84EO_XteUg677Pjlp0eqptUc4ijge83RQ1bZWCJPhTbfkCcqs6ZGr_-uOoXwZDprzWrf60067646xrO9c8e3jHY2Pt6PUqWpluyKKbLdLK7daWY5Achg53nGRnjBQUoDeW29TILf4f-vXhhxEcVkOi0rVjuQ7JuhS9v8c58ufZOM1wclMakC89GOisaUaZiM0YvQhD-84RXK1tsPUyEcTHYk6IJoPq2KNMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز الرياض.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93121" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93120">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇸🇦
إنفجارات عنيفة تهز الرياض.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/93120" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93119">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fedd1dc2.mp4?token=AAgMh7YymN_i0-IbHjb_xGBqT8FK2W_LILwppW9yHp5Ysvlo6W5ahNiRtKlbt6DH2FYbPS9uIb2YVm5SMVph4kriyIydyfU9FH_4jS3GgCn7-TJ8NfcdJtUzLwYBWBokm1YDltjxF913Rul8HOa7blYVh_jGHXauvUtj3EwZHMePXQHUORKLMzmM4Bq0kDWJi8uOT2TCeJ75mfjqxfc_wcH8LEvZ2DRQ8PBLgeQBRLo_5WbqV1KmjZ7y_Puhcssjx3JKf-7ekpnUpSg9lFk82LkeyYdMR4MfcPl8ULzDoEaNIIAFROjgLM_78qR9l3jv0Hrum9whjFUw2q65oGLrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fedd1dc2.mp4?token=AAgMh7YymN_i0-IbHjb_xGBqT8FK2W_LILwppW9yHp5Ysvlo6W5ahNiRtKlbt6DH2FYbPS9uIb2YVm5SMVph4kriyIydyfU9FH_4jS3GgCn7-TJ8NfcdJtUzLwYBWBokm1YDltjxF913Rul8HOa7blYVh_jGHXauvUtj3EwZHMePXQHUORKLMzmM4Bq0kDWJi8uOT2TCeJ75mfjqxfc_wcH8LEvZ2DRQ8PBLgeQBRLo_5WbqV1KmjZ7y_Puhcssjx3JKf-7ekpnUpSg9lFk82LkeyYdMR4MfcPl8ULzDoEaNIIAFROjgLM_78qR9l3jv0Hrum9whjFUw2q65oGLrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض ارهابي في قاطع الدناديش  في الحويجة بمحافظة كركوك ،اشتباك قوات الحشد الشعبي والشرطه الاتحاديه مع عناصر داعش الإرهابي وانباء عن سقوط قتلى في صفوف عناصر داعش</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/93119" target="_blank">📅 03:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93118">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a1c88504.mp4?token=B0juG2kGzllwI7BkMNca3j7Qgz5HDkBm_sKGtoxnPy5MfTnX17zR9Cr1m2ygm5Fvk48IY7_x2MvxhvmLDFdiRJQUlLtUGcYue_Bc91fhy5-ocjeKlIuwXQ7pAuJX9dVicCC9pWA0iOrSv06A0-yJH_tvzr_6kDcL8uvszjO-PRbGfdW1pVFEz1aQJm_M7JS63On_VqHoVcGYGna7YaIokzjM6HbdM_zkp6SYr6uxT3uOMxrOb6BCVoQNDVvXvdquk2pGcObhsxhpUrgJu9X8HHMFK4a1omadsuZZtgmKpM1yQl9ZOVSbG-f7GFv24o-UbxgJrXm5dNm3wu9cPlwcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a1c88504.mp4?token=B0juG2kGzllwI7BkMNca3j7Qgz5HDkBm_sKGtoxnPy5MfTnX17zR9Cr1m2ygm5Fvk48IY7_x2MvxhvmLDFdiRJQUlLtUGcYue_Bc91fhy5-ocjeKlIuwXQ7pAuJX9dVicCC9pWA0iOrSv06A0-yJH_tvzr_6kDcL8uvszjO-PRbGfdW1pVFEz1aQJm_M7JS63On_VqHoVcGYGna7YaIokzjM6HbdM_zkp6SYr6uxT3uOMxrOb6BCVoQNDVvXvdquk2pGcObhsxhpUrgJu9X8HHMFK4a1omadsuZZtgmKpM1yQl9ZOVSbG-f7GFv24o-UbxgJrXm5dNm3wu9cPlwcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض ارهابي في قاطع الدناديش  في الحويجة بمحافظة كركوك ،اشتباك قوات الحشد الشعبي والشرطه الاتحاديه مع عناصر داعش الإرهابي وانباء عن سقوط قتلى في صفوف عناصر داعش</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/93118" target="_blank">📅 02:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93117">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3287583d27.mp4?token=WjDRwaJ49zlP1jmaip0wkp4IbWYR3kHBHazfaECPnP96vK3At1pGpasX8ZhqOPNRRnWjETv-1Jr8dtj92LIAEfWLv20YX94sw3I6uJ7ex42x-Je6eXoTSDpRmX4Cr0nkDmHWu1aNEJSUItenAHwRk3uI7rNSuA5ewahAFvpCRWnASulCoeKpePKqzoaHnGME5c_Y9bJmBxWgdWfn4-dPwKDfXmADKzS60FB0E0b_Nm7KbWijm2j0TCn7tU951xxGMuTmTQ2oi7HkInpzn141mQaID8xASOiryWlsr1BEcHnECPkiKaeEO2YWDoiExdcBZwrH_VaETX54OzHNOzRJxHL_Ovuhv_oE2jERCO_9iaZybAw8tpva9mGyMhtuTfLt_cKCrUjBK5tLldvCJusrg1fFLEUE_RwuJ-yvwVva7IP5XiunDGDQPXy5VNH6J4ynI4Jdg2WoUiJu7l9z4UL4BDWGeY-zfuacqG3FBQmepnrwMKuxTseXWxN5CcJV4bvVgJ7ccTYEiB2JD2RqNgk0txc5V5wtV7rdqFoQxCs2y44EB5x7ZQ_warF6py6XZ7TrmBw5XBzEyiMtbkdJ8prjlgrIIN6XcBPJ9OvNHsB-RcZu1a9tTx9klRKVqn_O-fCUzcrLked9cV4XI5U_070NwqsnTLNQAS20PtkG3dd2wX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3287583d27.mp4?token=WjDRwaJ49zlP1jmaip0wkp4IbWYR3kHBHazfaECPnP96vK3At1pGpasX8ZhqOPNRRnWjETv-1Jr8dtj92LIAEfWLv20YX94sw3I6uJ7ex42x-Je6eXoTSDpRmX4Cr0nkDmHWu1aNEJSUItenAHwRk3uI7rNSuA5ewahAFvpCRWnASulCoeKpePKqzoaHnGME5c_Y9bJmBxWgdWfn4-dPwKDfXmADKzS60FB0E0b_Nm7KbWijm2j0TCn7tU951xxGMuTmTQ2oi7HkInpzn141mQaID8xASOiryWlsr1BEcHnECPkiKaeEO2YWDoiExdcBZwrH_VaETX54OzHNOzRJxHL_Ovuhv_oE2jERCO_9iaZybAw8tpva9mGyMhtuTfLt_cKCrUjBK5tLldvCJusrg1fFLEUE_RwuJ-yvwVva7IP5XiunDGDQPXy5VNH6J4ynI4Jdg2WoUiJu7l9z4UL4BDWGeY-zfuacqG3FBQmepnrwMKuxTseXWxN5CcJV4bvVgJ7ccTYEiB2JD2RqNgk0txc5V5wtV7rdqFoQxCs2y44EB5x7ZQ_warF6py6XZ7TrmBw5XBzEyiMtbkdJ8prjlgrIIN6XcBPJ9OvNHsB-RcZu1a9tTx9klRKVqn_O-fCUzcrLked9cV4XI5U_070NwqsnTLNQAS20PtkG3dd2wX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحفي: ما هو موقفكم من الهجوم على المطار في المملكة العربية السعودية؟
‏ترامب: ليس جيداً. إنه ليس أمراً جيداً. أنا لست سعيداً بذلك.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/93117" target="_blank">📅 00:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93116">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44502f8fae.mp4?token=ST7KxdmcHuyKs9yvOQ7fyAAH3dDPqWVX3lz7-_7KO_y9znU3sAsP7CcO-P5jKoFuyUXtyb-IYOfVuPlFNWSldodz0QhT5nvezQCzA_2oXmwORCoK-_kffN6ZClDb52t6f_SykrApuJkh3Y-CrA9ExONCgYZWp39EBK_83cZRC0QPsHboxOKnViUtC3TlrWOSCQEPZKbnKTXYdZc0apCEPZg9yLq0OVfiG30gO1ZVfJw1mOH0g_6uhf7J0enqk5lrULrUolU0l8AuG9Dd2peCESIP7gpieO1FIiEkHQCq-KCJpDOP_B7AqI_E8dLdQf4IUsugi7NNhC07F_d75uwqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44502f8fae.mp4?token=ST7KxdmcHuyKs9yvOQ7fyAAH3dDPqWVX3lz7-_7KO_y9znU3sAsP7CcO-P5jKoFuyUXtyb-IYOfVuPlFNWSldodz0QhT5nvezQCzA_2oXmwORCoK-_kffN6ZClDb52t6f_SykrApuJkh3Y-CrA9ExONCgYZWp39EBK_83cZRC0QPsHboxOKnViUtC3TlrWOSCQEPZKbnKTXYdZc0apCEPZg9yLq0OVfiG30gO1ZVfJw1mOH0g_6uhf7J0enqk5lrULrUolU0l8AuG9Dd2peCESIP7gpieO1FIiEkHQCq-KCJpDOP_B7AqI_E8dLdQf4IUsugi7NNhC07F_d75uwqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد جديدة من النيران التي لحقت مطار الملك خالد في الرياض اثر الضربات اليمنية الاخيرة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/93116" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93115">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEAY30RFKRiIax7GQzOu5Jown8vPD4R0XvVwC0dnExn_em-CgCn5u5gy0EPg3tWcB4i4sXfi0YTIpjktH4JrOMrmTun3jXSKI8Ogh_-VkJMqpDAH6Xp7TyF3zMqL_fbHmYU_AmshlT1wLEyJLZN8hhWGgkLLMpWLrepsxUpvcLQU2SCrDdazCiJ5qtzFrI0FWewfLgFQfHQtM05PTvcrLUatQnObSegNEwkJFQf3_5hkkFdSn2iwQId0C1FlAEa-cvKYS0p1pn1LZGpE_t3M0Es9x48rwm1ka-4tbWWTdwEMD7XtAYKR_ZuUUbywidATFep6J02N_lLPK3s1ZcoO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن وتركيا والاراضي المحتلة والكويت والسعودية.
طوال ساعات يوم الخميس 8-10-2026 .</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/93115" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93114">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaKu7JbQm6pj_hEHTzzUOdyUtDhzCqn7iC-AcTSxvoj_IQKPcY1tzpkkYEzXjuCvlHLnS_lbdanFBEY4CvraFrpqZcD10MiYtK1cHdoz1mEPQKlkgIpV9p7WxqqMH59sLhf9zIXxrffePKbxKbwkdBuEfv7R3jUoUAhJAdPiGf0kPlky64qmyWtMKjEJt266cNoOjbGAVjwNGRcBBgqAXD0lmuwludwMW9XFgExlCUfZGXnXWA1_eEJK2muwRiFIaJnxx7AlWjEaIx-avTiNq4cjCKi47gtpj56wfu20BMNvZpD3O0_D20P_TpfQqYiTasD_XicD0XDEHprtkEBBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب:
لقد اختتمت للتو محادثات ناجحة للغاية مع الرئيس فلاديمير بوتين، من روسيا، حيث تم الاتفاق على أن روسيا ستقوم فورًا بتوريد أكثر من 300 ألف طن من وقود الديزل إلى السوق الأمريكية والعالمية، و500 ألف طن أخرى خلال شهر نوفمبر، ومليون طن بعد ذلك مباشرة.
بالإضافة إلى ذلك، وبناءً على حالة مصافي تكرير الديزل في روسيا، ستقوم روسيا بعد ذلك، في فترة زمنية قصيرة، بتوريد 3 ملايين طن من وقود الديزل. وبفضل سيطرتنا الكاملة على مضيق هرمز، وإعلان هذا الإنجاز الكبير في مجال الطاقة الروسية، ستنخفض أسعار الديزل للمواطنين الأمريكيين، وبالفعل للعالم بأسره، بأرقام قياسية وبسرعة كبيرة!
إن خفض الأسعار للمواطنين الأمريكيين، وخاصة مزارعينا وعمال المزارع وسائقي الشاحنات الأعزاء، هو أولويتي القصوى. هذا إعلان كبير ومهم للغاية. بالإضافة إلى ذلك، يجب أن نفهم أن إيران لن تمتلك سلاحًا نوويًا. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/93114" target="_blank">📅 22:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93113">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مطار الرياض يحترق بعد الهجوم اليماني</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93113" target="_blank">📅 22:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93112">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇱
الاعلام العبري: محاولة استهداف سيارة في بلدة حوش السيد علي قضاء الهرمل على الحدود اللبنانية السورية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/93112" target="_blank">📅 21:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93111">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHQAPZ27VlxL7Bo7b94_1riTqCt7cv6Lq3YNzgF4yH7HWxLq6nFf5gyqJwxdE728HpNutUCTPjYuXLOH04HRkc1zl9F_68aLXUz_eKxnI23L2yDPwjsIvMmLRU11pUE8LgAexjEv_00bVMfowl24IfJZmypshR9qF0jAsN0qhyRaOyPCDMkQHmM1NlYZBFiVJoYrRZJ7Ptq1xoElFUaMQ2rJRIvdPQlXmrRv0F2qqVmki-b7tAnE4scAQ1bJV19gDsx_rJnMc-m7_2ZMp5SLhInGAE_wSlCsRLXKcdT3D2ODohOFTl5PNGvy-yOA6kY3mDssqwnu0ruUBrlzaY7Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2108613399643123736?s=46</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/93111" target="_blank">📅 21:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93110">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 77 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات مأرب وصعدة والجوف وحجة وتعز وعمران وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدنا 1934 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/93110" target="_blank">📅 20:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93109">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJM7zWQTX6veeNxTMr2wIlh4QGIBz04xc8uB8C_Kh3OpllUh0di1wekpOoImsMvmxec_fyZy2-eE5gJAd_6awMYskvz93CVk9F6giHW31njNsyqcn08kdE74EpgfcX7VZBUYV5FVcu5y36f_GGmTzBY6sVwB6s0OSpHTttE32VdsnMBmsKK2RrX3s77qGBzgq_GO9a9Kvk_yGlO1BKwERsWHIYOJZK1Oj1Ysu__s76ws7E1bz_sS78E0W9LConhm27ig81z48KN4eGXWWNJ4tMNBzDhWmWdyGgOjA_POb7NFCcBZpjtZsoxa9U_iEFd6x9uZ_jBnQOeQCD6yeusBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفيهي
النظام السعودي ينشر باللغة الهندية يحذر الهنود بالاجراءات القانونية في حال تصوير الطائرات المسيرة والصواريخ واماكن سقوطها</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/93109" target="_blank">📅 20:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93108">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:
صور غير منشورة للطائرتين شاهد 136 و238 وهما تطلقان النار على مواقع العدو الأمريكي في عمليتي نصر 1 و2 وعملية معاقبة المعتدي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93108" target="_blank">📅 20:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93107">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
اعتقال اربعة اشخاص من الجنسية الافغانية متهمين بقتل مواطن عراقي في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93107" target="_blank">📅 20:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93106">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzTLZdKC2IkBzx2c36N635eNRMQ1VcHT29oJjk2XXc7klkAYExBEkwKKR8aI0eFIRrLsT9Mm99hIzAaekS8fd-8qnv25XZToxa_Y82ELzDV1bksZvk1jkZTNORY6-pchnehUvy6RNIir8MHo_1WxngHyzlKfVIOYgXRwlKLzjckC4ZaFQF1tc1DYz70uGce7RQKnnF4lk-t2tAQ53ZJinf-o1Y5-fMd8wVdMCw05ZdgPrmmle0bLU0oJHa-3relG4VDtX2DK-wIAxt5_e3fwvTD5vi5RoaiCc5nLwIK7u18Jxt2pGg9KzXGgkiNgKUlvI8pWWIwnzgqPnBSqzTI5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المعاون العسكري لحركة النجباء الحاج عبد القادر الكربلائي:
كان الأجدر بالعراق أن يحذو حذو هذه الدول، وألا يمتثل القرارات الظلم والجور الأمريكية ليجنب نفسه مشکلات هرمز، كما فعلت دول كثيرة ويبقى نفطه يعبر بانسيابية، كما هو حال الكثير من الدول التي رفضت الامتثال الأمريكا المجرمة.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/93106" target="_blank">📅 20:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
ترامب حول إيران
: إنه ثمن صغير جدًا يجب دفعه، إيران كانت ستستهدف على الأرجح مدينتي سان دييغو ولوس أنجلس بسبب سهولة مسار الصواريخ إليهما.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93105" target="_blank">📅 19:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
صاعقة رعدية في قرية ابو طيبان ضمن محافظة الانبار غربي العراق تسفر كحصيلة اولية عن 2 وفيات و7 مصابين.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/93103" target="_blank">📅 19:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامب: إعلان هام قادم بخصوص الديزل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/93102" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامب: إعلان هام قادم بخصوص الديزل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/93101" target="_blank">📅 19:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فلاي دبي تلغي رحلاتها إلى الرياض وينبع وابها في السعودية بسبب فقدان الامن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/93100" target="_blank">📅 19:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/93099" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H2rc8yGnwQhs4IUZ2VxE7TU7POWuFGYhf2oghA32F0HAKMk2-xRmwRtKeGIKfTiSZ15lkf9-NjVTs5lVBqtVsBu7Iu8B0XtYgvwCX4dWTCdSFBghSeRo5_QNdfrxZOKMzlhqHg5QgOofwQoPT8aumJYTB5krNPCAa3krLxn83hxQZ82rPYB9yL2hIFdPihzpp46QWYGMu_kgqsuverGBr4G1q5F9LURnpJng-kWd5a_gT9xQO36VXrvUizwZgOxT7yTw7Wc3M_D_05lmr8Ri8Fmc8upPEBJZvmRKY9_wL4X7I4K9bc9u3MsgvR0J7qwjGGAXJogC-EfjbRTVFbo_Rd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2029e25.mp4?token=dYzW1pAH_N95eOpy7r6twzcMESS3LQtgUlMEuEyeU45KOkmIyswd_Gh7-fxjN1fr2UQYjjrX4mht7aegChsSyKhXKzilzJOyaUUcvrwAFdg8tTunciDLLHzQpka4Xf3XjkbSRT194eMnEIMgK2BweJGfYBeNLPskPDlogMEpJDg-xQ2uBX8a6f1vIuEdIvQU2CrpyLgKH2aV76AF9aLSQNKmHkkJy_FXt7I2CnhRPI88usWquq0ZG5-o7wnxd5WkhmvxpGDcCfpfZp9RTXIKVimtbKrmlinVQ5pwW7r7UBnkVOjWTwWx89B2k-lZgm6a25vo-FfFSsLzyRuFTHf0H2rc8yGnwQhs4IUZ2VxE7TU7POWuFGYhf2oghA32F0HAKMk2-xRmwRtKeGIKfTiSZ15lkf9-NjVTs5lVBqtVsBu7Iu8B0XtYgvwCX4dWTCdSFBghSeRo5_QNdfrxZOKMzlhqHg5QgOofwQoPT8aumJYTB5krNPCAa3krLxn83hxQZ82rPYB9yL2hIFdPihzpp46QWYGMu_kgqsuverGBr4G1q5F9LURnpJng-kWd5a_gT9xQO36VXrvUizwZgOxT7yTw7Wc3M_D_05lmr8Ri8Fmc8upPEBJZvmRKY9_wL4X7I4K9bc9u3MsgvR0J7qwjGGAXJogC-EfjbRTVFbo_Rd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في مضيق باب المندب بعد الف اعلان سعودي حول السيطرة على المضيق</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93098" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=DxAZZ0jgbRyrz8jcQoUtz0exXF3iy60I0_rTHU8TtjJn7wI_wZ1YJOLabsG2ddqCidPDFcPQnGMONYrz5oQ3oGdTykg9hdyUSQEDyBiDkBHNXpgvntx8ALkBbJkA0p9td1mDGJhnGLoeWxA8v7px8b_aFd8qFoFcTmiWWpn0tVzLrIbcX4SrNun8uBRmKZl-t0uqvwDn8cqKFkf7gTdZ6TO8dM35KsBYs2ot6inPNauhmJjY90163aYvjdi69pDQfjMNqnf7CjRG4SjKlldHEPpWrl-WT_dUFcIhilZ0ZDWmcsx9PJNbCB2OwDQuwuHIZGPXrjqI1tAxXsKqLRkQuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52c72fd4d.mp4?token=DxAZZ0jgbRyrz8jcQoUtz0exXF3iy60I0_rTHU8TtjJn7wI_wZ1YJOLabsG2ddqCidPDFcPQnGMONYrz5oQ3oGdTykg9hdyUSQEDyBiDkBHNXpgvntx8ALkBbJkA0p9td1mDGJhnGLoeWxA8v7px8b_aFd8qFoFcTmiWWpn0tVzLrIbcX4SrNun8uBRmKZl-t0uqvwDn8cqKFkf7gTdZ6TO8dM35KsBYs2ot6inPNauhmJjY90163aYvjdi69pDQfjMNqnf7CjRG4SjKlldHEPpWrl-WT_dUFcIhilZ0ZDWmcsx9PJNbCB2OwDQuwuHIZGPXrjqI1tAxXsKqLRkQuoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع اشتباكات عنيفة في شوارع الحسكة بين عصابات الجولاني وميليشيات قسد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93097" target="_blank">📅 18:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=JZP1RLcAz6WZa-6A42w5hs6BWsxQicfuXwGE1CM-KJh_q4YhFsEOcaTS-5QHz_AIMYPnjvKbjvMD0fzCJiGnGuDFVAVAWPBAtTfZlWKVfHbAL4_vQmYoP2JJxmqqPZXjwFQdZ6cdTA6OeTm_slNOHS8RG88qKAhekpVRXK2SxT8SDd51kKkOBUBspONqTKZdwAAsaTSznzDkR2gxeeKTDuC4sxbRpmPhoRYF7usov4FvYohE88lVR7fKRxkwrvK3Acs1muSiviWmIX9ZVwbPsga2VGa_idjK_fBfhcZF_lfLA2WN93Ry4ALtOeMLUMpchDNJG-9zLQn6hCSkxeMkiwpMwrca9ySTt0kkvdyB8YVl_EGnexibwKhryR2SH15wD3GWQT8GhrW6n6jOtbicjHKH6KJPcskigGCy0JthY5YrFFNdXn7BzlmJYEuT4--7X99gVqgG2Stf6Zgc58uysfPVjhgJ8uhH5ljtv60kbakRcdDj1_lT-BH01LM8BPH93A1Xa6xMKbJbU5MD9aW3PF6JOT3j8htYjUY1dHHWTcJMPwi7meZxvBDTGReg3Zx-w0SdP0wwqLzSSWcItyaKsC5noYe382tLxI83oTs_d9L_jOWQuhd30DJaVTPnV1ZyEb0GzmpRQ9ZHhdqSgd8toiMRiCATJ4C_6Ons7SpakGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbc462dbd.mp4?token=JZP1RLcAz6WZa-6A42w5hs6BWsxQicfuXwGE1CM-KJh_q4YhFsEOcaTS-5QHz_AIMYPnjvKbjvMD0fzCJiGnGuDFVAVAWPBAtTfZlWKVfHbAL4_vQmYoP2JJxmqqPZXjwFQdZ6cdTA6OeTm_slNOHS8RG88qKAhekpVRXK2SxT8SDd51kKkOBUBspONqTKZdwAAsaTSznzDkR2gxeeKTDuC4sxbRpmPhoRYF7usov4FvYohE88lVR7fKRxkwrvK3Acs1muSiviWmIX9ZVwbPsga2VGa_idjK_fBfhcZF_lfLA2WN93Ry4ALtOeMLUMpchDNJG-9zLQn6hCSkxeMkiwpMwrca9ySTt0kkvdyB8YVl_EGnexibwKhryR2SH15wD3GWQT8GhrW6n6jOtbicjHKH6KJPcskigGCy0JthY5YrFFNdXn7BzlmJYEuT4--7X99gVqgG2Stf6Zgc58uysfPVjhgJ8uhH5ljtv60kbakRcdDj1_lT-BH01LM8BPH93A1Xa6xMKbJbU5MD9aW3PF6JOT3j8htYjUY1dHHWTcJMPwi7meZxvBDTGReg3Zx-w0SdP0wwqLzSSWcItyaKsC5noYe382tLxI83oTs_d9L_jOWQuhd30DJaVTPnV1ZyEb0GzmpRQ9ZHhdqSgd8toiMRiCATJ4C_6Ons7SpakGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات بين عصابات الجولاني وميليشيات قسد في محافظة الحسكة السورية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93096" target="_blank">📅 18:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93095" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله وعونه وتأييده _وللمرة الثانية خلال ساعات_ من التصدي وطرد التحشيدات التابعة للعدو السعودي التى حاولت التقدم من جهة لحج باتجاه باب المندب ولم تحرز أي تقدم بفضل الله، وتم استهدافها بعدد كبير من الصواريخ الباليستية و الإسناد المدفعي وبالأسلحة الثقيلة وتدمير أكثر من 22 مدرعة ومصرع وإصابة العشرات بينهم عدد من القادة
ووصول أكثر من 30 سيارة إسعاف إلى عدن تنقل القتلى والجرحى من تحشيدات العدو السعودي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93094" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استهداف تجمعات الجيش السعودي في مطار عدن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93093" target="_blank">📅 17:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=RjFnImvTujGeqM4oSuTCHtT76xHQfKyYIb4WOKDJPNGIa0tyfY0uGuBMqkiCBlYigznCwoPrLrzDULDTwB7tyEh5F7BtUF82E3bx3nHSgKemPbG-uZpfhGLPSkthzXlBh8dVwSWV_d3pUeP_bi-UffPBmcRYa27XH4tihWyMldK-cpuos7c8EEKAdyPppZTX4JptsgsVqfCny8oHziH_iv1vMtHjiMwuLGmxsHDAvqwld1w--RC82pl4MwrNe3KNBZWqoYkPKoNKy-_4QHBXrxIeMF8d1i3lk64KaD-oTO3JapmtoxNEFl_dvpGGVrIj6gKFSQqevYU5buqKkr0MWjoLvysjl2RdJ6jMpgaYq2Bwt9xffG6F6hv-j02s_uFe3_v9IYnCaXoUDAVqNykix7er_3zLvh6eR0lqrinfgsLiOZzl6fb4d3LeuIKocM-LPbUzj2pq3KwlhOkgBZccRGEzOviGw3wYJZNvRvMf8lmX5nSmhfFUINLBwEkyhYJJ63v9BK7ZX4eqIYdyY731CYriQLhrrEimZmr5ZDzx--FqpTaK7tATMAefT0fJLaJR662AlwrjBCiiSkkCQ5Tfsh45SeAK0037bi0bedyEA91Ztwf4lzScexd2PxVUkIoO4RH3_wgae2qfzkOpU9lx37sD9qaqIjxJZxEIe9zNlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7828e24c.mp4?token=RjFnImvTujGeqM4oSuTCHtT76xHQfKyYIb4WOKDJPNGIa0tyfY0uGuBMqkiCBlYigznCwoPrLrzDULDTwB7tyEh5F7BtUF82E3bx3nHSgKemPbG-uZpfhGLPSkthzXlBh8dVwSWV_d3pUeP_bi-UffPBmcRYa27XH4tihWyMldK-cpuos7c8EEKAdyPppZTX4JptsgsVqfCny8oHziH_iv1vMtHjiMwuLGmxsHDAvqwld1w--RC82pl4MwrNe3KNBZWqoYkPKoNKy-_4QHBXrxIeMF8d1i3lk64KaD-oTO3JapmtoxNEFl_dvpGGVrIj6gKFSQqevYU5buqKkr0MWjoLvysjl2RdJ6jMpgaYq2Bwt9xffG6F6hv-j02s_uFe3_v9IYnCaXoUDAVqNykix7er_3zLvh6eR0lqrinfgsLiOZzl6fb4d3LeuIKocM-LPbUzj2pq3KwlhOkgBZccRGEzOviGw3wYJZNvRvMf8lmX5nSmhfFUINLBwEkyhYJJ63v9BK7ZX4eqIYdyY731CYriQLhrrEimZmr5ZDzx--FqpTaK7tATMAefT0fJLaJR662AlwrjBCiiSkkCQ5Tfsh45SeAK0037bi0bedyEA91Ztwf4lzScexd2PxVUkIoO4RH3_wgae2qfzkOpU9lx37sD9qaqIjxJZxEIe9zNlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93092" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93091" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">القوات المسلحة اليمنية تدك مطار عدن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93090" target="_blank">📅 17:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=oB-7qr2zMHer8SG3yt5b7PNJtMEpcEtesy0EOKEX2uDYidRK1LcjHGUG38bcDSO1vXnRg7AdtdyXOWQ79leTfFD1TO0GIqsY6tETW0pCbpRf0BtAS7ZCR8vMDCa18tH7XDspOwKiq_jJ3S_NnNy6EC3HwGCDm3EHkuToo-Gx-FEiy5-3-bdyLIaZdMFZIdjeYQiTqkj1mMyMLcbjkzMFI6L8JEI3wWKAx5YqVsCMBzDyOYMjDU1EfOuA96n5ITqmpKGnA9muKy8ezrVtAQkLJhpvRbd2lTA4oKpmVW4rmG5x2CL41cP4gvBlEQOGU1K11oq7G-3FGf0c2zfhfXktNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c3880c04.mp4?token=oB-7qr2zMHer8SG3yt5b7PNJtMEpcEtesy0EOKEX2uDYidRK1LcjHGUG38bcDSO1vXnRg7AdtdyXOWQ79leTfFD1TO0GIqsY6tETW0pCbpRf0BtAS7ZCR8vMDCa18tH7XDspOwKiq_jJ3S_NnNy6EC3HwGCDm3EHkuToo-Gx-FEiy5-3-bdyLIaZdMFZIdjeYQiTqkj1mMyMLcbjkzMFI6L8JEI3wWKAx5YqVsCMBzDyOYMjDU1EfOuA96n5ITqmpKGnA9muKy8ezrVtAQkLJhpvRbd2lTA4oKpmVW4rmG5x2CL41cP4gvBlEQOGU1K11oq7G-3FGf0c2zfhfXktNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
شعار الصرخة يهز جبهة الاقروض مع تصاعد حدة الاشتباكات بين القوات المسلحة اليمنية ومرتزقة السعودية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93089" target="_blank">📅 17:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=X5qxLhJR5_UzhdBhqQy9Hpl82gMceC2N9-WLSh2hix69PzZsDUi2qIt81ATaed-hq8gyE9f2rLb7f0aRA59wYILclY6s9EWzkhIFH9VVVPmi0FVAxdCThFeLGvbMMGmQe2SeG_We0-Of3sID1MQCW4dwyXiB7-4mxg5I0u5M5BbSUchTCCLshPcOfqSXcsA_e2Z3i7dUuRRrGW4uzdZJqxqFUh2VmOAJWZDFh-rhPIoZ8C8CSfzSaiBFs7holejRRfxyJ8PL8_pOgjOP_pH4kQCXObtcBjf71UMSSBqR8ww5CcL6TSzrdlBPvweJg-w9tiZaL0-iGs6_55OsRVR7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3629a87b.mp4?token=X5qxLhJR5_UzhdBhqQy9Hpl82gMceC2N9-WLSh2hix69PzZsDUi2qIt81ATaed-hq8gyE9f2rLb7f0aRA59wYILclY6s9EWzkhIFH9VVVPmi0FVAxdCThFeLGvbMMGmQe2SeG_We0-Of3sID1MQCW4dwyXiB7-4mxg5I0u5M5BbSUchTCCLshPcOfqSXcsA_e2Z3i7dUuRRrGW4uzdZJqxqFUh2VmOAJWZDFh-rhPIoZ8C8CSfzSaiBFs7holejRRfxyJ8PL8_pOgjOP_pH4kQCXObtcBjf71UMSSBqR8ww5CcL6TSzrdlBPvweJg-w9tiZaL0-iGs6_55OsRVR7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة السليمانية في شمال العراق لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93088" target="_blank">📅 17:49 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
