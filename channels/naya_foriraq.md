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
<img src="https://cdn4.telesco.pe/file/AstfgjoVRdBNcp2eyoDxFkiqslyTkqayzZzjQON3y6UzTxV4krkmMDfSC90DwHi2QnuymwPQUB0gwfLU8ze04ZGGy1VMs7MVo7f9NaGLVufi4A4KLnvTuRfPV_RtRD3rD5MOE4orp-i1tp16mXI4W-UkudZeGvgZ_xqzZtR_qde2KTljTXZJKdAkRxSLsmvvfvGlZXSUOZ4LwDvNnlFKEbUnjnWDPL432GTUMytuDHEvNgicb30ZVn_CkgGpqCO_o6VZykna1TEFJvfrpwAi3WiFf-0USUq_RV9uyWgovvm9AmA0i35kvrt3ZtOkt2RAdZNCYI0eP4Qv57BTAU0PjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-89575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
الجيش اليمني:
تمكنت القوات المسلحة اليمنية بفضل من إسقاط طائرة استطلاع مسلح نوع CH4 تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية قبل قليل في أجواء محافظة الجوف، وتعد هذه الطائرة هي الثانية من هذا النوع التي تم إسقاطها خلال ال12 ساعة الماضية، والرابعة خلال ال24 ساعة الماضية، وتم إسقاطها بسلاح مناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/naya_foriraq/89575" target="_blank">📅 19:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/naya_foriraq/89574" target="_blank">📅 19:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
مشاهد مؤلمة من اليمن خلال محاولة انتشال اكثر من 35 شخصا من بينهم اطفال ونساء من اصلاحية الجوف المركزية بعد تعرضها لعدوان سعودي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/naya_foriraq/89573" target="_blank">📅 19:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93c5e7d85.mp4?token=WRfnKOCZIjw00kZ5VN2z8KvyCqTNL5eYT-EPbmE2XCqysFDvE--R7Y1vhC6QUrIbag_YxLmWoVNTuwgYwwFuD8a6oD3uvjX-eO-N_zKL176Lb9Ujt3hFfiCk_LWJeD3Bb2vNZQdE9k_3kOhC9jeqYRESJ1c4460Bi0cMGb1Cm5wjRvppz-hlF3ww2_6-B3IZH5k-ev5rFbXRvi4i0H86vaUNqkBcSfCyMHRsrqizHFNee7EN8u3dnLfyKqWRrLnEfIi4CRhDvFEGxBLEQv-yigv5vxS0nvoFMkWUgs2Enf8Djmq3pJeeFwgOWqZe2gSU1U8tUFq27FTCTIjwduUSiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في مشهد مثير للغضب..
رجل مسن يتعرض للضرب والإهانة لغرض الطشة وجمع اللايكات وسط دعوات لوزارة الداخلية العراقية بمحاسبته قانونيا
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/naya_foriraq/89572" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
مدير الإصلاحية في الجوف: لا يزال تحت الأنقاض 35 نزيلا بالإضافة إلى امرأة كانت زائرة لزوجها إثر العدوان السعودي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/89571" target="_blank">📅 18:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89570">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مشاهد من العدوان السعودي على الإصلاحية المركزية في محافظة الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/89570" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني: لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/89569" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
مصدر أمني مقرب من المقاومة الإسلامية حركة النجباء بالعراق
-النجباء تتابع عن كثب تطور الأحداث بالجبهة اليمنية و الدور الخبيث الذي تمارسه قرن الشيطآن السعودية بحق الشعب المسلم في اليمن .
- المصدر ابلغ نايا بأن النجباء قد يصدر منها موقف ميداني بالتشاور مع باقي فصائل المقاومة بالمنطقة حول الأحداث باليمن .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/89568" target="_blank">📅 18:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
لا تزال جهود انتشال الضحايا مستمرة من تحت أنقاض الإصلاحية المستهدفة في الحزم بغارات العدو السعودي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/89567" target="_blank">📅 18:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/89566" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/89566" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇾🇪
المتحدث باسم القوات المسلحة اليمنية يحيى سريع:
بموازاة حصاره المستمر على اليمن أقدم العدو السعودي على خطوات تصعيدية بشن غارات جوية وارتكاب مجازر والتي كان آخرها مجزرة الجوف وتحليق بطيران التجسس وإمداد مرتزقته بمختلف أنواع الأسلحة.
إن العدوان السعودي المستمر على اليمن لن يبقى دون رد وعقاب، وعلى العدو السعودي أن يتحمل عواقب إجرامه بحق الشعب اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/89565" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇮🇷
القضاء الإيراني:
صدور الأوامر القضائية من المدعي العام لمركز المحافظة بحق شخصين من المتورطين بالاعتداء على الطلبة العراقيين واستدعاؤهما إلى الجهة الأمنية المختصة، فيما تتواصل التحريات لتحديد باقي الأشخاص المؤثرين في وقوع الاشتباك.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/89564" target="_blank">📅 18:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
معارك واسعة بين القوات المسلحة اليمنية ومرتزقة السعودية في محافظة الجوف.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/naya_foriraq/89563" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvPYsXm-FeudJxbZAfE4pm-_9k1t4h_OWkPZ9RFkdiG1soHWNN0bzCy2uBUFBfyWqseYqQmLwltAh_NWSD1S4eHSsYiFDQZZN9WdXG5hG50HHYjHs-oQnGLg9HdGpsQrbZioKJSPepU131BzM7TlaCZhUmWov4FYTSXLM7qEJOumsvVcrWNTBz-U7hyQfYcuIZsAKP8Z8t5NzkhUvKMFS1MwNsQzplK-exH_3-FDt-h5RP7YEUoU9EcjW8xCXSGcs-3-WwGp80ELkkCQ35r2A1BUYTmAilAb7xmtSBncSMun6KEab82PlKoLea_245wxBrEc4c67z7fbR0Im0y-x_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0L4gTJm5sJqkhdW86XypqiZVVjoCSaqNarMFs_iTrORFaTW34GhyFonySqkTKZK--eJKuMOFiapa3Ez_uhnP_x5Rzd4fXJVxGqr34KTcFIBI0HXK51KdAE4iysaBgrz4zRnb91-bdoQr-Zbi9_49-6RYAsqVQAiiV_cpCTaGJwrax53dsVKNOwVONMmTQdIQij_602VXJT-_09qKhFkmklpLRA2bsGGUA2YpFHMLKRc-wUBao5iR0UuXSokqvGlUHE3NvV6c4GHGQ3t5FJ2HgnKpiiCk7y1DFjBV-dfrStGEgsUY_4xxeqIe15hPjergNslz06FymSmk2niN-9nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t24vfYufjOcuZfo9dN1chQROScR29W_3pJQ6m0x39UIdTD_gkheHgFoicDPfU-LRzZvUecI7sXorrv_9A_259GAG1pNBQT-XppzcR23kNuo1C90CWndjEDVXY6iUWVyHtAJyklzliFkeOuT2zUH8OPqLmv5BQyKG9NKLf2_idm9w-KaKo8JtqWQDtIij_GbGRHRukEZ9yUeBM-pvBQyPmxXAER0jWQzyzSlxnF6PIAw34-g2P5hSRZyCenRbi8bZF4T_j2UyXMq4g-KfQY43tLPJbxQ__0qzZJAzuu0QGcUJGAYMP9Qf2XYWfKGJnxyJS7OoqPUPl2BYbQYDnLCYSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان سعودي يطال سجن الجوف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/89560" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj2bchhFjOlJlO1boM1DSd7RnPVoF7BTb-X3EPvmoVGjgGDFaN4Tx9GoHn4qRr0jKxcBMmY_LFzUFVXhvFa6wKYYiCSM3Dh8ON5vz04N3ERxcD4UtfM2bx-iTIG2PR2zNz5Scm36l8nR06qn7_gX8ydYJK6jd8r9dzx1csF0C0b9d32AooBYO5p74ERHX4MLVxFCFKU477sCUFPJv5UWk-ffcYZIBFzvF75qf4HUrj9SVSR9IQXdEy5qYAPcAwFvxAVKUFcEHYLvVtiLS3CPyKLrhBpyMNfIM8ikBkW3NYLKSdDu41v7IfcYeBmnJsAwr2br0_TjKRQFsEY3l_q3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/89559" target="_blank">📅 17:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انباء اولية عن استهداف العدو السعودي لسجن الجوف وسقوط عدة وفيات من السجناء
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/89558" target="_blank">📅 17:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇸🇦
🇾🇪
قصف مدفعي سعودي يستهدف منطقة آل الشيخ في مديرية منبه اليمنية الحدودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/89557" target="_blank">📅 17:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇰🇵
‏
وزير دفاع كوريا الشمالية:
إذا سعت الولايات المتحدة وحلفاؤها إلى مواجهة عسكرية جديدة، فسنتخذ إجراءات مضادة قوية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/89556" target="_blank">📅 17:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇷🇺
وزارة الخارجية الروسية تغلق القنصلية الألمانية في سانت بطرسبرغ.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/89555" target="_blank">📅 17:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b352d15928.mp4?token=svZg_i4RokcpcHbUCmR8ESyTFkibX-lgog9XRwyYXgCc9w9ROtZobjZBOKc1QOydPRICCGXErBoLzKjr40eRMcRcWW0WBYdEHbFABb1T3NtQsIaO4gNNW6FKlrZTcQwak_QjuL5DBkMcpHKOnWIHr94U2jrzeXVgUcdxMJRuFajXIWKYm8JKus6d1rQSr0XZbFbRBtMsX_gbLDEMlQ-yAjwXD2seQnSkZNfNk0UKaFh5kSekWz8zfBW9lwpQ62FJsoe3R4lQky44oj28mlipVipd-xw59MYz8fYzCyZpbQHGrH7EmQEUJz-RGKpCmU39uyjQ1DHv7LfWaGXfNVeafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء يطال النساء أمام وزارة المالية العراقية</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/89553" target="_blank">📅 17:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من استهداف القوات المسلحة اليمنية لشاحنات محملة بالعتاد العسكري قادمة من الأراضي السعودية
في معسكر
الوديعة بصواريخ باليستية مناسبة محلية الصنع.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/89552" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇸🇦
العدو السعودي يستهدف بغارة محيط مدرسة عثمان بالروض الربيعي في مديرية التعزية اليمنية أثناء تشييع بالمنطقة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/89551" target="_blank">📅 16:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
بلومبرغ:
العراق يواجه صعوبات في بيع النفط من البصرة بعد رفع أسعاره.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/89550" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPiZdQ5wVzeRStT18N5P9DF-HzBf9meQ6bVkdRyfkcczWwR9UOSKlopqR9NDmvJW6Q-RYTxO6K7naNYH0Mb-a3Hob4LtoM9pXy6dnmPw347pPI9wdhEqoHplT0Fs245W52iwboWrkltfw4SMuleQ5xWf0NQ0R88_Z_-ZqlYh1sNH-jOH8idY9y2Y4VCf0XlJR6WslC2cCB0XBUstpK4ghAs6bKw--NL-3ygyzvxbw-nvJx2NFUhrwQWCDEjHL-D4ST5UyTtCPJpIUH8j6x_dtuCLwyF9yNSzMQIyXWqik1iK1M5s5AyJb4vTcOLWOvCs9XLfjAlbVjKS-4sgo5L1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتال مرتزقة السعودية في الوازعية بتعز</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/89549" target="_blank">📅 16:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgGDoTS6CErLdmmv8MZnJf5W9ke3qrTC427rvivp66txNjQP1W_w6uMZjfQO4kGMwGHvdjdrju3ea29kZCxXEPF-Z7-DeoJP4wCVSEgp4VeBBSIx4Yuj40LjW5-oixCK67qIClR_op5daxCGaKj4doqHNjCXjloXb5ujO-WE2E1UhsCVkcTIAV1qSvf4VQ_seKgpkcoBXjP4YmSVSQF5tAbGdDzYjgJj65isw7D-w1vURykgovnhUxLmUQXFcsot7bC7Jqi_tk3g2q3-D5gdvA0cmyvGBSqUVMeC2uCrBu58U0IixHrVHrsGiINf9yNvBEHz_eQDQx-RTos3rNc1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابادة رتل لمرتزقة السعودية في الوازعية بتعز على يد بواسل انصار الله.</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/89548" target="_blank">📅 16:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/89547" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/89546" target="_blank">📅 16:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
وزارة الخارجية العراقية تثمن الإجراءات التي اتخذتها السلطات الإيرانية لتوفير الحماية للطلبة العراقيين في محافظة سمنان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/89545" target="_blank">📅 16:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
‏
بلومبيرغ:
أميركا تعتزم تحويل الملف النووي الإيراني لمجلس الأمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89544" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89543" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصدر عسكري يمني ينفي لنايا سقوط معسكر اللبنات في محافظة الجوف بيد قوات مرتزقة السعودية المدعومين أمريكيا ...</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/89542" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205a87d0b.mp4?token=YG0gaIplCc8Esr4plRgMXxtaMI2v4VJlO83VDu2zhF5MxNFWa8SCtW1uR0eDLy1PJLxhu_0DGdhFdkDLdNTVqfRgurkn8IrUkt6ymijKO0PIrhgZBnnYNkS9qvwWCsKPp0bA0Sp_flS1C_tauEDO2XHxIF9I0BL0sSNjnbHiFBXLi1PSU0zXrp7zP2Hc6Z8Qtp7gergvfvRH7Ifqh_2A1-vTDDO_uFACOfB705IqqItkOX9CzumJQXYs7LNKC8B0pipfBsKO8RSjvIJaHAcRHakHgLnUx6uB8NpmU0FIVrzVmdTtnAiQGBB9xmtCmEzgTyrsHhxngU3Usfk_zoZAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205a87d0b.mp4?token=YG0gaIplCc8Esr4plRgMXxtaMI2v4VJlO83VDu2zhF5MxNFWa8SCtW1uR0eDLy1PJLxhu_0DGdhFdkDLdNTVqfRgurkn8IrUkt6ymijKO0PIrhgZBnnYNkS9qvwWCsKPp0bA0Sp_flS1C_tauEDO2XHxIF9I0BL0sSNjnbHiFBXLi1PSU0zXrp7zP2Hc6Z8Qtp7gergvfvRH7Ifqh_2A1-vTDDO_uFACOfB705IqqItkOX9CzumJQXYs7LNKC8B0pipfBsKO8RSjvIJaHAcRHakHgLnUx6uB8NpmU0FIVrzVmdTtnAiQGBB9xmtCmEzgTyrsHhxngU3Usfk_zoZAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
🇾🇪
مواطن يمني يرد على عصابات الجولاني التي تنشر قريبا ستتعانق دمشق وصنعاء: "اخرجوا نتنياهو من ريف دمشق ودرعا، اقل شيء اخرجوا نتنياهو لنتعانق على انفراد".
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89541" target="_blank">📅 15:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الرابعة والنصف عصرا مشاهد نوعية توثق لحظة استهداف واحتراق شاحنات أسلحة قادمة من السعودية في معسكر الوديعة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/89540" target="_blank">📅 15:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
العدو السعودي يجدد استهداف محافظات الجوف والبيضاء ومأرب وتعز بعدد من الغارات الجوية وصواريخ الكروز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/89538" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اعتداء يطال الخريجين القدامى أمام وزارة المالية العراقية في العاصمة بغداد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/89537" target="_blank">📅 15:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e737d33906.mp4?token=T4Wh-1wsd-_0q8PcbvAPkss-Hbmu9EP7UKk_ZTj9jbF2F2dpQEhNMQZd3RRKHeiaJyWh6LvZsIkl5ZQkEgwVQwhxCwWhrD4iscDqGg6ImBq2bbEueH8JW5MnVDlv6V3ObCXlNkIGyev_LsAgkM4u3DHt9kSOkS4WybIzBMoQ31hWkDxNnwQTlGIUc3sZR42PWgtVbNDChnIY6ktuVHbf8l_SKfZHiFb0h9jz7lIB0r7yZhTTnP162-VEg5oL7h5XAFLGq5YzwBs5_udEc6f55w-TPH7OfsugoPCUJwIpZXjPJNkHQN21FqsDqi2t6r52c3voQxjUN_6qRqdIJlUcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e737d33906.mp4?token=T4Wh-1wsd-_0q8PcbvAPkss-Hbmu9EP7UKk_ZTj9jbF2F2dpQEhNMQZd3RRKHeiaJyWh6LvZsIkl5ZQkEgwVQwhxCwWhrD4iscDqGg6ImBq2bbEueH8JW5MnVDlv6V3ObCXlNkIGyev_LsAgkM4u3DHt9kSOkS4WybIzBMoQ31hWkDxNnwQTlGIUc3sZR42PWgtVbNDChnIY6ktuVHbf8l_SKfZHiFb0h9jz7lIB0r7yZhTTnP162-VEg5oL7h5XAFLGq5YzwBs5_udEc6f55w-TPH7OfsugoPCUJwIpZXjPJNkHQN21FqsDqi2t6r52c3voQxjUN_6qRqdIJlUcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء يطال الخريجين القدامى أمام وزارة المالية العراقية في العاصمة بغداد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/89536" target="_blank">📅 15:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/89535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/89535" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف التحشيدات التابعة للعدو السعودي وتدمر مدرعاته وآلياته وتكبده خسائر فادحة شرق محافظة الجوف
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/89534" target="_blank">📅 14:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز ارامكو السعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89533" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89532" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89531" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان: إجراءات الحكومة لتنفيذ برنامج حصر السلاح بيد الدولة يتم بموجب خطة مدروسة تبناها الإطار التنسيقي عبر لجنة منبثقة عنه تتولى اعدادها وسيتم الإعلان عنها حال اكتمالها وفي توقيتها المناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89530" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
من المبكر جدا الحديث عن استئناف الحوار مع أوكرانيا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89529" target="_blank">📅 13:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس: أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89528" target="_blank">📅 13:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جيش العدو يعلن استشهاد المنفذ  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89527" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم اعتقال المنفذ بعد العثور على سيارته بالقرب منها حيث جرى إطلاق النار عليه بعد محاولته طعن قائد القوة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89526" target="_blank">📅 12:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني
كاتس:
أصدرت ونتنياهو توجيهات للجيش الإسرائيلي بالاستعداد لحرب شاملة في الضفة ردًا على عملية الطعن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/89525" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني   أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89524" target="_blank">📅 12:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇦
🇾🇪
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء محافظة البيضاء، وقد تم استهدافها بسلاح مناسب.
وتعد هذه الطائرة هي الثالثة التي تم إسقاطها خلال ال24 ساعة الماضية بفضل الله وتأييده.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89522" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aef4dfe9d.mp4?token=VrSBtC4I4Boc2YOCMD9Vb28-GZjRtnRZsqQGrBwkffp4cGsaqNTiYRQcFoGlOS6mzjiATVMlwijdZnEbcx2lM2EA3N6T9Nyd3uNi1VQfkOGpMZvfcUB29RzHZTLzxv9r6BLlS09oGg0FASXrvM-Iw7AzxFAyh6Q1Jg68cz_DuTItsXV8Q1UrwbDmw3yzkN2Kxvb5Yjn8teFyPNIUYagxw-6-ua6L3sHLZVzfu_q1Nyp92xIe_a6PWYpzOMHUMfBPzOFi6gbxXbkK0D5KpFrN6GHMNpRPvhkHDB9YKBrIyc7burbZ7R4ma0hqGwJk7L8AtywD0aTxWNlO8ShkTpm8eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/89521" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a0805be6.mp4?token=BViMWzFk7T8VBnjQsCgwh0P1Bu51KcxvRYT68yh8H0qriU_6Fo_SobhXgOCidBs9pUG1P4-rNOCy1g41bTdIHnRL-aPUlBeCOsYcEeR7yEWKoO8TilKJHqCWamoKAynX1wDoQSBxDyICXUKKPwybAjHXfA36OwTaBOIkpy9kk89Eas6P-oP7Hx08Sez7AZvZo_V7gALHzlUNJY-5IYrx7IA2BfLkl9WbqcnIYv1wpFqwQdHIvljL9JSlPa_3uVkuo1c9ly6fplq05MeN-th8qBU8e4Uh_0lkmbo0r_lLCD-xmE7lqLqQS9EAO3WQaNa-UweDqn507MC7RgedmBrTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حدث امني داخل الكيان الصهيوني
أولي: قبل قليل، وصل فلسطيني بسيارة نقل إلى مزرعة "معوز" في الضفة الغربية وطعن مستوطن ؛ المستوطن بحالة خطرة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89520" target="_blank">📅 11:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur9T2dcgmrKlFZM7DNskt5DiNpNf7uazUVXz6mNlHnDNKMCeeCgt_05jcHeckbF6mtVggQxSdqNPu2xQF8wMj0JesJtVBerwwGem9-5DgcelsiuYOmQ2eKFHV67ahZOeMmZifR59i5DhFfcjfk6ttIOL2JygT19csbpXoRqPDclSDWXmfxzkcFgn-DUarYqMqaQRR7p3wdx02rOZmdalELI2MdVM_baGq4meQdu1i6v8tVB_f4-XMqDdC3cXQEaYoCEDxwvfG1ct_P8Tqky-nJDznVMn47uzX1OM7wNKZn164EZOMGnknKXKACOEEDKUaW2jGCkkiZzONy_XqnDi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوربا تنهار ببطىء   ‏يتصدر حزب البديل من أجل ألمانيا اليميني النتائج الأولية في انتخابات ولاية ساكسونيا-أنهالت ؛ الحزب يعتبر نازي وعنصري متطرف ويرفض الحرب ضد روسيا وحرب امريكا في ايران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89519" target="_blank">📅 11:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89518">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🇮🇷
🔻
المستشار الرئاسي الإماراتي قرقاش : التعامل مع إيران لا يزال قضية محورية بالنسبة للإمارات العربية المتحدة ودول الخليج الأخرى.
- من غير المقبول أن تتعرض ناقلات النفط والسفن للتهديد المستمر في مضيق هرمز
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89518" target="_blank">📅 10:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89517">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89517" target="_blank">📅 10:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
إعلام العدو
: بعد أسبوع من إعادة فتح الشواطئ في حيفا: وزارة الصحة تحذر الجمهور من السباحة في شاطئ كريات حاييم حتى إشعار آخر، وذلك بعد تلقي نتائج ميكروبيولوجية غير طبيعية في فحوصات جودة مياه البحر، والظروف التي أدت إلى ذلك غير معروفة في الوقت الحالي.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89516" target="_blank">📅 10:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89515" target="_blank">📅 10:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b2e12ce.mp4?token=dq9KVtGJ5P4PcUtH1J6BeJgnAxqkGZwg0qzjQH-EsE5PknSmKmOWS2-uLGVBZdp-WinpQ1p6ulln8vLBk0YYfruSzgcQOkf5n0uRNbkxis36E6YYUWu7ksl3ENqy9kHeocOx-XC4bgDMl1H-KzPnO7ZKZ7HRgGBpX_TjiO32fjTQsmbH0JxSgUwFe3hwv_mkd6-YQB8Iz2e9nwkSwbYjMDDh7P53I02YEOKuBLonhfqJvnXYnvbXOo32dTRVtyJ11xdMtMOXylL-pDyUJ-FugZE2CdNZb94VlwT7r3_JgMP7K_nBt5CgisBSnLPDxrW4XoQ0s3CtAI8d51qIabunEwFKiUkCLItyg0wqu9hKDh_5YJa4IXD0VahNDq2ADq5dTYw1c8P5uO9YTONjB4cIC2lx1Q4Ieydj6-pbzyNVtDmZUMfgMrGBN-Mab6cGa_pp2KQp3lwXKfVxLwOUX8ofQiw-g0BmaBCW150R8oB66fsz8keW4p3kqpuUQyuMKi7HNx3RWsV3s6H-2sbbU_u0Sxk268RiDRrHrMOS3VSdjifDXAUQ6_qguUtsyis5ia-fxlIz5_k9Q7pIQpUgd7g0PokRKcrLLiwF2WN-GnObMqnlGsrggQUcwm7uWaNOPZId_JDOHO7aWWnL5WfeQ228YOGx_fEQ1GinAjuOxlP6Fjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تصاعد أعمدة الدخان من مقرات الإنفصاليين في محافظة السليمانية شمالي العراق، نتيجة هجوم بطائرات مسيرة انتحارية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89514" target="_blank">📅 09:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏وقع انفجار للألعاب النارية بالقرب من كنيسة مكسيكية خلال احتفال ديني، مما أسفر عن مقتل ما لا يقل عن 10 أشخاص وإصابة 64 آخرين
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89513" target="_blank">📅 09:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لاول مرة   النفط يلامس ٩٨ دولار للبرميل الواحد  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89512" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruZE49Zv0u3jAyktXWIl_iXgM3uTXGhMe8q4gv5_coXtDBx8gXvgsroC3SPpsf8o63uJmDTXQowBjrMxYY_4xoiQZ6dACz4xXAZ28WGcOoyZdv78LvWg1F1KLWO2314mzWLkefFs0M3Bc26Tsq5ha1SQExm0xUKyxfpfLrxilzjMKhwCfDhwAfNutq4aLSV6jEro6oMr3l_CfHMxSaCzMy3ol28yfe2d6jNPIrCOXW2xKWjFvsR8MxBU2fEW3vfDJNdpfWQ8zCaSlrfqEDsAZcykXXjmjLpn491hoVGZ4URRb1BHNkpZwS03QjsRwbBSDeWC9twM_H2sJzoIRmYbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة
النفط يلامس ٩٨ دولار للبرميل الواحد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89511" target="_blank">📅 08:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc56be204.mp4?token=I6-v3tg4kybhbYqCXg5YDPB8GJDdP-K7ztsUIqByAzUqjUfJ_V0efxokMSKXrMId9I--o4M4HleqhOJTLNpdY30gCRwNiEE5vdt7QANETXRQTVSThuPHGdgLZZgXxVZ-1LC-l0eMxtvsxkHtQQe1ACwT7yWns_gLRWFWnLwBdCJXMwKucomO_A2Hn_Hclf5r2ZxEcU9j9y0oTHhes8k5WCVtmLWBAfMTRryP0mtwXCPH9Rb9HfgwIVdBHosL1fkvyi23wuT0KmyIMmhPansQFXt11r-FsauClnn4OYTfW7F8rzAIqA8lFIUAWabnqkv43rwaRSL6XJ6evYNVJ44KGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كبير للقوات الأمنية خلال إنطلاق تظاهرة إحتجاجية لخريجي معاهد النفط أمام مبنى وزارة النفط في العاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89510" target="_blank">📅 08:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa43e52504.mp4?token=shNAwmR9aZ0ZSpVjedA8NRpxmd1xBf2PubCodpYsGqgeHKFKNGNbztp683I69OQ1qJ2uUslcVgH0msbm6wPkslKL2jMqyowUzbemvOBemXxPg1l8Pdow4bkKvPj96yVPtkRDz1vDJ0CvY_MhpJ7Bh_-qv8Cikt0DGztFcmxwBKAjtBgoY7hSHk1Q2sBJhvf2RtHQofEDwf2w8RxWi13pEflTHg1gsRVemWORbgLZ_vLDYzzCEE3yDmgUxKB_fRnAn5wwKxRKeZAqG9Le5Hc43n4GnzsUN3xfKAFQsZLwDWpZH80G5Y5wDjmyhE_cjbSzG7R4-K1q06XSRi5N28RNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89509" target="_blank">📅 08:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
طيران مسير إنتحاري يستهدف محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89508" target="_blank">📅 07:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
القوات اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح تابعة للعدو السعودي من طراز CH4 أثناء قيامِها بأعمال عدائية في أجواء مديرية خب والشعف بمحافظة الجوف، وذلك بسلاح مناسب بفضل الله.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89507" target="_blank">📅 06:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf13f32be7.mp4?token=BpN-S04C_zi3O4qxCsRc6fgiSvqZxiv856B5CA5SblFJ9gRnG8XBRacE2E8mwttw4luVoKfjaufA7oFMASqwkYvTuXqA78cf9HyRnZdoUs03uLwapEcyWyfkQqnVwvH8noILxO6rrXygLL0hqmN41ARaFN4OolocvAlvK6Yzcd2j4pW3nXcnVM8z0YjyJSqhT9pPBegsRXZG1p03AKzGSGYQL2LFuI8dRM1iBVcnkC-RhXL_-wuNEfcfrhOVi3i9_3YpJPwhJ5dvy8gTi_wwfI_t39YenwsMm-fHqfvWJJWlNmwjOAttED_XoQUKEx69IPxv3w9Jg1fOZX5NezcQvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf13f32be7.mp4?token=BpN-S04C_zi3O4qxCsRc6fgiSvqZxiv856B5CA5SblFJ9gRnG8XBRacE2E8mwttw4luVoKfjaufA7oFMASqwkYvTuXqA78cf9HyRnZdoUs03uLwapEcyWyfkQqnVwvH8noILxO6rrXygLL0hqmN41ARaFN4OolocvAlvK6Yzcd2j4pW3nXcnVM8z0YjyJSqhT9pPBegsRXZG1p03AKzGSGYQL2LFuI8dRM1iBVcnkC-RhXL_-wuNEfcfrhOVi3i9_3YpJPwhJ5dvy8gTi_wwfI_t39YenwsMm-fHqfvWJJWlNmwjOAttED_XoQUKEx69IPxv3w9Jg1fOZX5NezcQvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إستشهاد طفل بعمر الشهرين في بلدة كفررمان بجنوب لبنان جراء العدوان الصهيوني الغاشم.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89506" target="_blank">📅 04:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1633213891.mp4?token=DW4ymDJuN11_gXQu1JnToKz_8h55rPPxNEIfBA3PnQfE0b7bxSxQ_WPefHxr6iGcY-OA-CZAAoB0e18Gk2kOm8oJPsesagTq4OWZBoYw0zMD6VuN4u1YuhJuCO4lxJXPYcOfWjNElONYEYTAj3FkWEjAokpfn-aSfZpXv71iC8Ir8bdyLNyEazhsT3Zd-QZbboAMKMWH5UHSZ7gkp2JBb18ycATt9Pdk_gkfHlVmd8GyOh7ftQRaGEVLPI72t-101uylQ9qcw75f9LvJ1pa7fiqUUWX1fodYRfaBJkjqpq8SKrnySN1LpMTw7h25fJzqWKSnCH6f9frbQFUVVozpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1633213891.mp4?token=DW4ymDJuN11_gXQu1JnToKz_8h55rPPxNEIfBA3PnQfE0b7bxSxQ_WPefHxr6iGcY-OA-CZAAoB0e18Gk2kOm8oJPsesagTq4OWZBoYw0zMD6VuN4u1YuhJuCO4lxJXPYcOfWjNElONYEYTAj3FkWEjAokpfn-aSfZpXv71iC8Ir8bdyLNyEazhsT3Zd-QZbboAMKMWH5UHSZ7gkp2JBb18ycATt9Pdk_gkfHlVmd8GyOh7ftQRaGEVLPI72t-101uylQ9qcw75f9LvJ1pa7fiqUUWX1fodYRfaBJkjqpq8SKrnySN1LpMTw7h25fJzqWKSnCH6f9frbQFUVVozpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار إخلاء في دير الزهراني بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89505" target="_blank">📅 03:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG7-I-9Fe1KTD-QTuWtpYus6QPuMZQNrSFTB0Xa01D8FF7x--gyeRMYXUHWNO1B1y1z3HnixFzB7qpF4efLHUlxga5NA4sNucuviCbyOuWR-fVnUHOvw4Uw0O9JrY0A99KSsTWE79kkyAc2OFnXqPOwiaISoN5jGOGUBI6diDp11daruildBXx9VyjuSlVf9Gi5yg-d8C3c7WjjVJIAXD7Ce2-PRYBDc7Oupim1yJtqYs1gqkosQ7PBNlscrVYIcyMfdsmOJghg2F2RIu5OIA7B1yxI92Cut0HthGbxRtEs4foSomLY2FDOY_RezMFwDRbrQq7aCtekJT1jEd28aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار إخلاء في دير الزهراني بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/89504" target="_blank">📅 02:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVz7QPyhbzoxn-FncCeBdIwfkSV2jaQikdYN-s5cov9sCLH1SMD1w5EAgxuJs10pCu7w26TJ35NDb_JWXan9DpD3qIEPwKyWJukouYq0_Q7pCKQXDmwK9fAt6iqjBiz-f4yJdsjFEIumNdA4mzQSDN7rAe9Xs_BExWi_I1OH8XjmcsQo7xRJToMfC-Ny0WfVbRxkrK9KVTxl9IsMxxDxhcGcN4xN-VQGW7pmlr1Ta5kvsBUcfapOYSMpDUeXo2Hvs9fVf7NXgMAm9XMmyOfuLIa-eiWe6cExuL1awQ6DkvX73cS_e4OMdI7UAPOvuqISgkRsLeC_GoYF55Sk7q_eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تبدأ بالإرتفاع وتلامس 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89503" target="_blank">📅 02:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🇺🇸
المتحدث باسم وزارة الخارجية الأمريكية:
"
لقد انطلق العراق في مسار جديد تحت قيادة رئيس الوزراء الزيدي، وذلك في شراكة كاملة مع الولايات المتحدة. وكما أوضح الرئيس ترامب خلال استضافته الزيارة التاريخية لرئيس الوزراء الزيدي في 14 يوليو، فإن الولايات المتحدة تدعم بقوة رؤيته لضمان مستقبل أفضل لجميع العراقيين خالين من الإرهاب، ومنع الهجمات داخل الأراضي العراقية ومنها، وتحقيق شراكة أمريكية عراقية قوية ومثمرة للطرفين".</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89502" target="_blank">📅 01:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217b61cb81.mp4?token=i1EtJqeKpTa5s5X25m_ad3b16m0-Q1XfnogU3jGg8p0QbS71b6SZ_XMa9ujiBVGY5f09sIK5_ySm6jLr2wmqpLQQVdXMMVU1MVLsHKxPfBnOPxBTPcQhpEZnxTnxzRTvgAngTesbVLI1Rk4G62HTaYbNE9jjOLNlIYgRLJwRTWhrUwiPon_Ru7Tm_QAFf-bit1dRWOpjBlmHuOqjlOqv809lcopUrO0CTWdI3yyszccV70-aOwlwVi-v1H7_U4aSrV40OSK5w9VnlVPmB857pLYfxSCYBRAR4k8yf6LAC-GUJ2HrP7jtZECGOrau5RX355O2cPQu4fwX8BpoLZ5Iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217b61cb81.mp4?token=i1EtJqeKpTa5s5X25m_ad3b16m0-Q1XfnogU3jGg8p0QbS71b6SZ_XMa9ujiBVGY5f09sIK5_ySm6jLr2wmqpLQQVdXMMVU1MVLsHKxPfBnOPxBTPcQhpEZnxTnxzRTvgAngTesbVLI1Rk4G62HTaYbNE9jjOLNlIYgRLJwRTWhrUwiPon_Ru7Tm_QAFf-bit1dRWOpjBlmHuOqjlOqv809lcopUrO0CTWdI3yyszccV70-aOwlwVi-v1H7_U4aSrV40OSK5w9VnlVPmB857pLYfxSCYBRAR4k8yf6LAC-GUJ2HrP7jtZECGOrau5RX355O2cPQu4fwX8BpoLZ5Iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
الجيش اليمني: "
ابتعدوا .. المعركة أكبر منكم"
فلاش 1448هـ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89501" target="_blank">📅 01:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
انفجارات في محافظة تعز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89500" target="_blank">📅 00:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
بقائي
:
كان مضيق ‌ هرمز  مفتوحًا على مصراعيه حتى 28 فبراير، عندما هاجم ‌ اسرائيل إيران. شنت واشنطن حربًا غير شرعية ووحشية على المنطقة، وعطلت حركة الملاحة التجارية الطبيعية؛ فتوقفت ناقلات النفط، وتعطلت التجارة، وارتفعت أسعار الطاقة.
‏تحاول الولايات المتحدة الآن تحميل العالم تكلفة اضطرابٍ من صنعها، ولصق التهمة بإيران. ففي رواية واشنطن، يجب إعادة صياغة حربٍ أشعلتها الولايات المتحدة بطريقةٍ ما على أنها "ثمن سلوك إيران على العالم".
‏بدأت أمريكا الحرب لكنها تتوقع من العالم بأسره أن يدفع الثمن، بينما تصور إيران على أنها المتسببة في هذه الفوضى.
‏هذا أمر سخيف للغاية!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89499" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة زاهدان جنوب شرق إيران؛ إستشهاد 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/89498" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBacNFtAflWLYQIjUrzQiBK_VLWLL5einUndvn78OQdWaIex6R5j3Yllaqxx2QkbCGx99KXDsuxpXxExvKGa68rJMo78F1VKlBu4Zad3WJmE19Szue-KkqJvdxRYSjiLxQwwpnAQ6pRYrxJVLUn1DP9i_3n3Hen5GxDNqSw-BFpiSbiCrjP-wF4yQY2bHU6zgnpMBh_XQyQXCUxuj2xO_YA_irQa4_IsHJvTRRMDcfcRSjw7mKzgFYB5oAelq-LwNVSOubFGwrMNbPoBySfP-WPtqee8nmBLlcEj3bVArU9nZdFBK3FYp_2Flwpw70g_aMMno0phQlCVl7_f9fJl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أنا التاريخ الأصلي روحوا گولوله
انه بالبعث لاعب ميت الف جوله
٩ بدر بالميدان
🔻</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89497" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoDWBzNHr3IveTrbnnSU-vNmlvk-oPsKKYLjjpQOdWii9W-Ot7si93SYpzLt9cO_WttmEmSsymV_1uXzHwrDHPebj8MVo5qeHaOOdfOqJ2YcsD41ZvBt1PF2yBoNfAxm8EXwzzj9Uo3ckC4hoOe2BnpxNWxVZ3iw94upGwUJoVLiN-BRwdSDVzrJempK9yHpG1XIufVIVCKWnJJLqvqJZbGABc-Bh5i92NsFd977AiYLjDvWO-exSEfoGc125DXCtEtFg3_873A3I4ISRalEfb30BAmO5IHq0DFjV-C_UoXxSllc0JhfLJfiPONgQyYZ_-6NN16b-ihdo4grFRQq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بدأت فعالية ترامب الاسبوعية بنشر صور مولدة بالذكاء الصطناعي لا تمت بصلة في الواقع.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89496" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
‏
ترمب
: كميات النفط التي تعبر مضيق هرمز عادت لمستوياتها السابقة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89495" target="_blank">📅 22:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb8764d1.mp4?token=rLc5Rypu6BpTAegLBVZpALKQwz1cg96QPgqoKEPv7b_Qy4mQsv5lK2EtAl8NURo_yyluxzDZu3WpKennsi_KuIr5LEp4suMmpeLOLb1yJ3_Lu9UXb2bv1JirPHxgZ_JqJzP2cYpxKl6Umnkwf6eIjyM2lTXIfua7F7JKA320yPz-UHxM5u1SmbEHnRUB6GN41hTSGd0A9z1DjPnip2vhRoVutQ8lA60QLOLZSJbPglkfiQXFL_51K4XWR6n_zs7oPo9170f1hkGwp5IQtrbE1QhyPdhSIjrG0gknOczsLhceTGiLKvv8zSVBT01Hv0aJggOV8DZkrfxlDK2wSN5zZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb8764d1.mp4?token=rLc5Rypu6BpTAegLBVZpALKQwz1cg96QPgqoKEPv7b_Qy4mQsv5lK2EtAl8NURo_yyluxzDZu3WpKennsi_KuIr5LEp4suMmpeLOLb1yJ3_Lu9UXb2bv1JirPHxgZ_JqJzP2cYpxKl6Umnkwf6eIjyM2lTXIfua7F7JKA320yPz-UHxM5u1SmbEHnRUB6GN41hTSGd0A9z1DjPnip2vhRoVutQ8lA60QLOLZSJbPglkfiQXFL_51K4XWR6n_zs7oPo9170f1hkGwp5IQtrbE1QhyPdhSIjrG0gknOczsLhceTGiLKvv8zSVBT01Hv0aJggOV8DZkrfxlDK2wSN5zZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رضائي
:
قبل 48 ساعة، ولأول مرة، اختبرنا صاروخاً إيرانياً مضاداً للسفن فوق سفينة حربية أمريكية.
‏لقد خلق هذا الصاروخ الخاص "جحيماً" للأمريكيين، ففروا هاربين.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89494" target="_blank">📅 22:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
امرأة تخالف طابور الوقود وتتسبب باعتقال مدير محطة في كركوك
🇮🇶
امرأة تخالف طابور الانتظار وتحاول الحصول على حصتها من الوقود بالحيلة فيما امتنع مدير محطة البنزين في محافظة كركوك شمالي العراق عن تزويدها بالوقود إلا بعد التزامها بالطابور لتجري بعدها مكالمة هاتفية  قبل وصول قوة مجهولة قامت باعتقال مدير المحطة ويقال انه قد انشمر ورة الشمس</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89493" target="_blank">📅 22:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qImOWKHHo3CoucN21tOYkVyWQh8Ux5fSDClcchFmClDyJ-N6MLv3QZjKoiM0v-XVGcdZngfUzY0aiG-as6iKqwoPtQDlLuQG44b7DRJIX8Sor8C6H2UIEpyT7hlEAah-WyfkOHeohGpKS4Xbn8gWfa5KWrhporiJjlQZ7tSaD_gxnLwAtQcZRy-7aGe6bO7X5ex-mqG9wuQlFSYqqgBRyZ4FA5wIdgE7kKtsjTd9H_a1Zo6Xhg39KzWooHMuFPyxkGUgofIbTwre-y8DQhe407tgX2IUCInPEvWnv-S7cvs8YnejUHc_JgwsOZHjTP2oK8lhnFRLKFV9sNwbnmJCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تحطم طائرة في مدينة ميامي بولاية فلوريدا الاميركية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89492" target="_blank">📅 21:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCLt7SQnod7n8fxJ7nhpS_pYaHwmekurOXAw9xVdB4Hi88wxN8ApKR8yZyStMQTvuL6HNSgRAxXEbRcKQ7paQBO8_iPc4JbgrrnEsSlGGZacYZ5cP089KSeTXd46T9Iq5Tpp3Du9SLOw6GpOcyZCPCgGPE6382gl_jUvKuuXBWs-7lKQSy0sPGlFbonf3g-hVkQC1DTWzycDTCFqmADSsPDp8hdVBO5ovT5T_YfPZW7FsRLlGy66vHScLhCIVM_XxQV6NgltjBHcejBi_VTDnjobDvQjoruboA1tlNEAmJ6hFpNYy1EMBaBIHmPM7S6XjWn-6fhc8JJZdJJ8y69yXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🌟
ترامب: الرئيس واشنطن يزور الرئيس ترامب.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89491" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhDmpMMWY7-H4UWTQ2z_f9yGekZF1lh-Ybfh59ywb2wwR5bAKBefWb5NvejOo-WjOyhcC34BhuuQFicIObLbVVzCRyIGtHIrgL4dcDyHgfzV-Cam_qsKvhl3efWQWaB2OFTSQdV7fnVeo-WnkwXD82pXw1HYD6IwkCwBryiNB7PhvbRVWCyW8Ra9-5aRnyJPYyagL7PsIRlw_wiHN18iu1fWNjHtTFFWuYwvCHKPoUckyzZYG0KlqxJz8F_HPdPrL679fxPr17KZbYDANC_STjxFcEkGoH809hj4qkpZh2ol7ZqDqOMXBI6L4P5Unez1CewK5dOVrhzo4aQv_3QoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🌟
ترامب:
الرئيس واشنطن يزور الرئيس ترامب.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89490" target="_blank">📅 21:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQc1b42enEHyc0jIqDyAADtjeV3mj0JWzu7evRX4TXOViNOiiV6AFcl2nXcMLuOWDFMS6Hs-CXXDOnDvBrhDY0jE8RYiqf4kSZ543a-HZS5je7kF87Hxt2YVD_y6XQ9KY1mS07QpumIFVtizUP-3pDeeR5VSNdgKZm_n9Ma-OIu5Qj2eQMj6m92epI-RXSgzc63wevnW2mnM5KHLExt8EQawsN_g1d-Dp08hEG1Mevu8A4PLvVf2bzQXbb6rYtq3FhPXyk_cEBNka0Zy6eKYEpy9qm8IIJN5FoiQKSM04uixuq1IyRr1uEveyo1USJbR3sTgt6aqOQFelrx8TrxQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن إصابة الصحفي علي شبيب والمصور في قناة المنار بغارات إسرائيلية وسط مدينة النبطية جنوبي لبنان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89489" target="_blank">📅 20:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9affbbc7.mp4?token=deLp2CoA5S1pC7GlCEUzoY5k__PcxQ_w-ent1vNWWLjw0nf9uOyq7EDQQBbK2GBKTEJP2TErdvhXVQ-9JYEqOKM5rHTGL5BnMMaVulaVE1cmxZqQNko-_WkCfDDHAfuimn3RkzSlVlkYCRam4mHPia66DL-TAeWldlEEB2gUksAQPbhejECVtopp2WeiUML5NT5LLbU92zvArU1HBX7xOaQTY6subHv0EeSftGK_RMSbewMnLRMv6r_zumO5oQPK0uP66ESa1m7Q6UnRPuzfIPbrtGPdnvYyuujaSc_2XSsAhYWZdNn7--iDhiug2l5y1VGX8ML70qaSjudvtCdOzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9affbbc7.mp4?token=deLp2CoA5S1pC7GlCEUzoY5k__PcxQ_w-ent1vNWWLjw0nf9uOyq7EDQQBbK2GBKTEJP2TErdvhXVQ-9JYEqOKM5rHTGL5BnMMaVulaVE1cmxZqQNko-_WkCfDDHAfuimn3RkzSlVlkYCRam4mHPia66DL-TAeWldlEEB2gUksAQPbhejECVtopp2WeiUML5NT5LLbU92zvArU1HBX7xOaQTY6subHv0EeSftGK_RMSbewMnLRMv6r_zumO5oQPK0uP66ESa1m7Q6UnRPuzfIPbrtGPdnvYyuujaSc_2XSsAhYWZdNn7--iDhiug2l5y1VGX8ML70qaSjudvtCdOzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية Sentinel-2L تظهر منطقة محروقة جديدة حول خزان لتخزين النفط الخام داخل مصفاة ينبع التابعة لشركة أرامكو السعودية، وهي مركز تصدير رئيسي للنفط على البحر الأحمر.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89488" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2yvHQe2ucXP5vW6SVKnK0kleGa-dnU5aCYYv4iK3i1Vv5txy0LqKLopUZdByfDhExj1Ta_G3bhiyl1dK9fFs0-_DkC22cVj6cYuswVaZWHguPgEhYe9-JqafVHqbMeciDJHLkV56kXDsVDpfHeld9L374wcxYKj9pjX5Dll7QDs34oirQJ2HibeGjfjyoMGIWCI51rGiw6QJBLJXgNkanf5L1Hb42UEvcKeIF15b5JG52y7zGioSg8WKB-8LP4jtxIYEYlVK1NRB0NPVOO4oAn6zK_v4VwIzcxc7t8_Bq6lNLT-o-1IkNTSzFN7aT5KzhdQlUwGS7lzFTRD32ZsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر لنايا:
العثور على مقبرة جماعية في مدينة الرمادي مركز محافظة الانبار غربي العراق عن طريق الصدفة خلال اعمال بناء تضم رفات عشرات الشهداء من منتسبي الحشد الشعبي والجيش العراقي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89487" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قراصنة تابعين لمرتزقة السعودية يسيطرون على ناقلة النفط "نيريدا" (NEREIDA) التي ترفع علم ‌جزر القمر⁩ بعد مغادرتها ميناء رأس عيسى</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89486" target="_blank">📅 19:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اوربا تنهار ببطىء
‏يتصدر حزب البديل من أجل ألمانيا اليميني النتائج الأولية في انتخابات ولاية ساكسونيا-أنهالت ؛ الحزب يعتبر نازي وعنصري متطرف ويرفض الحرب ضد روسيا وحرب امريكا في ايران</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89485" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🇺🇦
نيويورك تايمز:
نظام المشتريات العسكرية الأوكراني عانى من عمليات احتيال وهدر وسوء إدارة جسيمة خلال الحرب. وتُظهر عمليات تدقيق سرية أن حوالي 1.2 مليار دولار قد ضاعت في عام 2024 وحده نتيجةً للمدفوعات الزائدة، وفشل العقود، وضعف الرقابة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89484" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">القوات المسلحة اليمنية تعلن إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء شمالي غرب مقبنة بمحافظة تعز</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89483" target="_blank">📅 18:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsxg-0KTlLbBURCxz0QonLE3r5fQhUwyG4aqGuvP3Jby1eDCvJdu87vuSR6jxnk-_-bxwKcRENX8XAF0wsS8vHdqiQvpYu-ZxzNZou7c1fpgoY4Uk1OangQNRsOnm7HwwcxdBHSsseft1d9UUPdnXBLEz6qUvKt1QlBNl5NO22vhz7sSnx9gUXiUQ_B-NDDAXT0gw-0p0bVYUgCM_rwGh7c30dqHzGmjnXrTGTCpXNFrv7Kw2Vt0_GukQmLn2zn74P6necsGgFyI63CFvRh53WsWPFJImw-t1kAMvj7WggTGV_9DwfPFKUkVPZE4CHX6i5I6i93FLGr2AqOWrtXUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف ساخرا:
استعدوا للإقلاع. الاستعدادات قبل الانطلاق:
ارتفاع أسعار الديزل إلى أعلى مستوى لها: بيعها على المكشوف
أكبر دائنيك يتخلى عنك: حظاً موفقاً مع تدخل ين++
النرويج تخفض 80 مليار دولار: فلنغير اسم النرويج إلى أمريكاواي
انخفاض التوظيف: نسبة الدين إلى الخدمة مع الحرب الإسرائيلية، حسب توجيهات من يحركونك
أوه. مخطط النقاط الخاص بالاحتياطي الفيدرالي يومض باللون الأحمر
😁</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89482" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📰
رويترز:
تعتزم الولايات المتحدة سحب أنظمة الدفاع الجوي من كردستان العراق بحلول نهاية سبتمبر، وقد تنقلها إلى الأردن والمملكة المتحدة وقبرص.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89481" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
البنتاغون يرفض صرف تعويضات للجنود الذين لقوا حتفهم في الصراع مع ايران ويزعم انها عملية وليس حرب لأن الكونغرس لم يعلن الحرب رسميًا.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89480" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2l2EODBwb1yyOsZDDP2owNo5JBRCmXpVc0CzLI9iZYtMjyMnZ8Xhs67rYxDiEVf_Dc5THW-8nFtP7gYx3tzPs_oiiZWNCDFHPw7RVFsSake1bwO73DN3gHWzjFeh_-qpY10_ArG2Xtjzd8jxKXEQUs_ZcOnfFl97yMZ3dSKlWa967a9VNii-dAcxwELT5Oot8_KoOWBRADa4SOeEn88nqP2BH3mS3kWnp6HxOxVj5unx8e-ZJUHb4D-V6IJ1v9hZG8TGFSfwwoXJAO0NOskHdmOtEkZI1FIxibbFs0lzmctncK52qx8WJa1p_fYuhe4MhC1e0Ac90483gjA68EVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
حريق مجهول يندلع في محطة رأس لفان القطرية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89479" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#متداول
🇮🇶
بعد فضيحة تسريب أسئلة الرياضيات من وزارة التربية العراقية التي تعاقب على إدارتها وزراء من حزب تقدم.. تصاعد موجة الغضب الشعبي بين الطلبة وذويهم وسط مطالبات باتخاذ إجراءات حازمة وسريعة وفتح تحقيق شامل لكشف المتورطين ومحاسبتهم بما يضمن العدالة ويحفظ نزاهة الامتحانات وحقوق الطلبة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89478" target="_blank">📅 17:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmQbP4cJkK22Moc55a2MlXCDaofh0WarUL0Y-pmeVD_6Dc4QHJ9bnBrkzxhIAxANZl1OWWC9ajm9iyA-YgTrUgKNiXRGRolq3SMzjyR6JXdacACCq5j6Yd8zpzXpfq5DH64U1-q-m6_FC_UmZz1XDmyLZXrUQgXQwcns5SDWFzgZaca2SWOHVhsI_PkLLGFqPwrU7lbnElg8MEdPScOprQp93laR-vAABiLhQTMn-doP92Pkqpg94TESd21On_2Xo44H1n6dJpIO51Q-qldnf4kn6yb1peYyTDI5qNTg-QDg6vqSkZ-_0PKt_tEG17RibT4Z2hX_NFsWzbQw71_FPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXfZI7k4jFrYTiTUSddkSczwoGRyEHR4ywz9F0TdcXYkWnO9yLHt_e2AJZnXjPUFxLVxjsKwdlkuofB6yiODOpNzH-nVRz6Fb-s6cKhQY1T33887KDH-KofaiksHR4ZL14mpfrEE1DBMy4g8X26JVw4F0vDiJ0xvVsCj5yH5XfEBhmmasKUTwWmSsodKz-tBH1o0_pZEB-7hoL9svcuYMnua6vwvH35iA13przm0CGe04EvLlXqP1gzDGdafdxLep2cJZRId_9rhyCrlZroeTb6EDHwHy5uG15HbC7WWhNUORkGBh1pU9_W4SMkaL1jWxNENyqcY4VR_zfR4PYSMIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
محافظة بابل وعدد من المحافظات العراقية تبدأ مراسم تشييع عدد من شهداء الفتوى المباركة بعد مرور 12 عاماً على استشهادهم إثر العثور على رفاتهم قبل أيام في محافظة الأنبار.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89476" target="_blank">📅 17:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العدو السعودي يستهدف بقذائف المدفعية مديرية شدا الحدودية في اليمن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89475" target="_blank">📅 17:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ضربة صاروخية دقيقة استهدفت اجتماع عدد من قيادات التحشيدات السعودية بصاروخ باليستي محلي الصنع.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89474" target="_blank">📅 16:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محافظ البنك المركزي العراقي:
لا عقوبات من جهات دولية على القطاع المصرفي بعد اليوم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89469" target="_blank">📅 15:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs6ujJTJmt_ruuBWX9wzJ4rEWjk2dSM566iaUyyPupAo1V1t1d6ZN9eKc3jZmqBljz1Ao9RVTqB_vnC6fikuN1HnJV5lEeqHnWKvocpovUCFq8VyDIRceUas6KP5-VYmuVQamuIyxPMccvL-SaW6KVVpJrhls9HeRu7ornTRiNUVoSRI7iT5e3JZ8pnVOFwQcmICoPmz1Sunn4KkBqUWKBNcNS_Vrdi1r5li3vuB-51mTA0ypvF_GzKZR_FgkdA_GWa1alHQ8B2znCkBHTR7EXgqNENo3biFzNPiUOO_8q1mRzf_iM4lDBYT33YCxq8MjjfQOOaqxgHikLcdQQU_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو الاء الولائي مغردا حول تنظيم السلاح: ‏تنظيم السلاح مقابل السيادة الكاملة والشاملة</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89468" target="_blank">📅 15:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89467">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اندلاع حريق في منزل وزير التربية العراقي بمنطقة السيدية غرب بغداد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89467" target="_blank">📅 15:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89466">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcLBujY866Oe58iPB4yUnj7Icyzlgf2fvxKCYeHw9jBYBuaq2LMMGrBYgjcz7eSlRh1BmRGpaoqGZ3bpnpAJPv4qXxgj4o7WHqbzXRRzV3V_keqFoYq0to41WOQReygIE6l6yCwnfli2CBzfdSBCoSqwiPev_ZMoqw79RBTUs021M6lAqrO1AQ9F91L2FzOPLqqjsDtOGNFcS5Ew-a2RKMOgT_cJOJtkJn0cFfeTWpPy0cJA5mYJyRoMJmIjXhOHoJLrR4ypYJ_3SYUyHFkdUZqWXg0IJYGx_1PmkEhtoq21VFz26BWyJm4D-bPBjLwdY2VOQnxu4CTJ_j-5Pmsghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
🇮🇶
هل اصبح معرض بغداد الدولي اداة لترويج كتب تنظيم القاعدة الارهابي ؟
جانب من كتب هادي العبد الله عضو مؤسسة سحاب الإعلامية التابعة للقاعدة وكتب الجولاني وكتب ثورة سوريا التي تضم الإيغور والشيشان وتنظيم النصرة تباع في قلب معرض بغداد الدولي للكتاب !!!
المطرب سيف نبيل تم منعه من دخول سوريا بسبب مقطع مادح الحشد !</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89466" target="_blank">📅 15:01 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
