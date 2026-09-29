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
<img src="https://cdn4.telesco.pe/file/Zenb6Eb0VBztIazZqnLDZ1QSG5LB-1D52vuhQDXwucEUMqsxPu70BIuLtadcttHNNhwrOrFJ1jYKEbU-eDSUb0fvkSEQIfTnh6N07IoU3IeYyPSsWy5foUkKUt_1IIhP_jOKq4qWzYj6C4ZzKa_npRY9cT_l_UWPfq3REe9e2dLfSOap51NeL-dqhocdtdGWI2vphnU0N_U0ul31W2S4QpUDmWCuwpzdVMYekjqY6HGf9t8w4ItNtZTbbWb258SGIrzjwnfIedKQo7HdBFdlQPl2pYaKmXZC1e_mn5fN3C9raZBlD2fYLQA0SBla2RdJDhC9ffw9vTrwyui6uLE4Mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-91981">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af18a9ad1b.mp4?token=eh6tZBiuefr9C5YnUVNBFfVaD_RzPZhQhDAL0YMxdPn_jGatScsqkYpSKQrVcocaMfaG5vQclf8tq82rVHH6W7lTqiWz-3sqjfITPa0Rp7DQGBq17Vb0600ePPII8WtRtLONp6PAOoCFFa4hp5ubWYZeMM13vYq5UBD8DCI6lOjlAJJdkrGq3XeBT64nlyxyqBytwhwpJOOADSQUb5IfPcLuIl0n2V9M_9-gLFElK1oDovJDXAky8p0bZaDPX5i7cKBaJTLsJUSf43bOWOkmH3MZ1tKRyzCxvxuVxtBwN20zNamfHNmwv5XZkZ597h-FyZKZk2BvYmSmK6dNoSevgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af18a9ad1b.mp4?token=eh6tZBiuefr9C5YnUVNBFfVaD_RzPZhQhDAL0YMxdPn_jGatScsqkYpSKQrVcocaMfaG5vQclf8tq82rVHH6W7lTqiWz-3sqjfITPa0Rp7DQGBq17Vb0600ePPII8WtRtLONp6PAOoCFFa4hp5ubWYZeMM13vYq5UBD8DCI6lOjlAJJdkrGq3XeBT64nlyxyqBytwhwpJOOADSQUb5IfPcLuIl0n2V9M_9-gLFElK1oDovJDXAky8p0bZaDPX5i7cKBaJTLsJUSf43bOWOkmH3MZ1tKRyzCxvxuVxtBwN20zNamfHNmwv5XZkZ597h-FyZKZk2BvYmSmK6dNoSevgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهدت محافظة ميسان، اليوم، وقفة احتجاجية واسعة نظمها أهالي ووجهاء العشائر، استنكاراً للقرار الحكومي القاضي بتعليق الرحلات الجوية بين العراق والجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/91981" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91980">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
‏
فانس
: الأدلة المتاحة تشير إلى أن سيد مجتبى خامنئي على قيد الحياة.</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/naya_foriraq/91980" target="_blank">📅 18:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91979">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇨🇳
🔻
الصين تتعهد بالرد إذا ما اتخذت الاتحاد الأوروبي إجراءات تمييزية بخصوص قيود اوروبية على البضائع الصينية.</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/naya_foriraq/91979" target="_blank">📅 18:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91978">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇶🇦
شركة قطر للبترول تبدأ مفاوضات لدخول قطاع النفط والغاز في فنزويلا.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/91978" target="_blank">📅 18:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91977">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbSl_nWbgri8O8drlb58MzVGweVL85irAuo_5iA4aVK8rLfjZYDPVtPPN4cDEwzeGTA1QkXdb5-BJkw4nru-nF18y_dFqNzyjylBlr2UjNZUc-LshfTf_WWNVvoXSbYvy5f7T2qpT-Bse_FduQyjK9vDyxVyV8MWhjYM7SjqhY3diwIHHoHLfwjbgNF-M2Y3Tnct-HAgYlyxzWHVpkPfzqb7J4s6ky_7VpL09fEMU1aK2-IERPWKvjhzOqNotQfF6ZFmcRGVOt1v-BWHtf39XrfLj8dLAQlFm-LbvomfumgFNJXamiKZtf6KGl0tSNyW5nvJc6q_9jaWxIccGuvvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
جيش العدو الامريكي يبدأ باعادة طائرات التزود بالوقود ووضعها في مطارات بن غوريون ومطار رامون</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/naya_foriraq/91977" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91976">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
اعلام العدو:
نتن ياهو سيعقد بعد قليل اجتماع أمني في مكتبه مع كبار المسؤولين في المنظومة الأمنية ودعى زعيم المعارضة لابيد الليلة من اجل احاطة امنية.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/naya_foriraq/91976" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
الكيان الصهيوني يهدد باستهداف قيادات حركة حماس في قطر وتركيا.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/naya_foriraq/91975" target="_blank">📅 18:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91974">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c46a987c.mp4?token=jkDcsLpK39LvCC-1yUXYtsmjiCthuMoHfpRJ2O9a389y3kmOfp5WR_UeIxKq2zWTYXa2lHRqpxXwo2YHShrKs5ETKrIMUp2aPULhoIjFlVuzG5tK6B9kYfNd-2mmKoWUJEDVAEbP3G1PSaRKpsxhLgVSxWnh9Q3CxBA4jPnIHiWCMOXm9PwxF4SOpIf7tTs9Ji-0612QbfJfrJKE5DNvsyVFZ7WW0_VSnQm9a-GhZw2jbYuwdcigHyr0-5nFOY01-10QvoY4HTwODXOi2CBpZUT6oKr8Mlh7MsM3kd_T-T54oMHZ26HCxAgjxG-TdXDnqQz8ssBsExaY1-f6uTuzjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c46a987c.mp4?token=jkDcsLpK39LvCC-1yUXYtsmjiCthuMoHfpRJ2O9a389y3kmOfp5WR_UeIxKq2zWTYXa2lHRqpxXwo2YHShrKs5ETKrIMUp2aPULhoIjFlVuzG5tK6B9kYfNd-2mmKoWUJEDVAEbP3G1PSaRKpsxhLgVSxWnh9Q3CxBA4jPnIHiWCMOXm9PwxF4SOpIf7tTs9Ji-0612QbfJfrJKE5DNvsyVFZ7WW0_VSnQm9a-GhZw2jbYuwdcigHyr0-5nFOY01-10QvoY4HTwODXOi2CBpZUT6oKr8Mlh7MsM3kd_T-T54oMHZ26HCxAgjxG-TdXDnqQz8ssBsExaY1-f6uTuzjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جماهير محافظة البصرة جنوبي العراق يرفضون الحصار الذي يشارك فيه العراق ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/naya_foriraq/91974" target="_blank">📅 17:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91973">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/91973" target="_blank">📅 17:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91972">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/naya_foriraq/91972" target="_blank">📅 17:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
العراق ينفذ حكم الإعدام بحق 10 مدانين بجرائم إرهاب.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/91971" target="_blank">📅 17:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91970">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مصرع عدة عناصر تابعين لجيش النظام السعودي على يد انصار الله</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/naya_foriraq/91970" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AW-dKDdAq78cLZcvsipcDDZyRi-kT9cfyYGQ37lXhGIQCnwLMSsyy-5AcBW4IrMwshLXOa0ZrFc5gNxhE6iL1VXFYGPSs8RrxIDuWOW3w37kcHH_EWCJDq_JFTqpSCgYmi84bj3fj7VC7QkUSnPWbbPIJvUXEcax8ZKpRofY7keuD7lq_sMlIH_B2GLcc2VjDmDz1eX81tKHZlFoaYp7k_dX2N18TqzTdR8GFWI3XTQMmCSAkJn6T18Sei0zmWDed6YaN85wY9SnA_HzJweaH0cABdbvejq-kkMXxNsms37LuAm1-hQcfNqsL3ctFNVUpeFfaD9sa7SOQQVlreN23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leAtTk6X3XfqEKmOyCkIQMTIo2Oj3Y_tzQzzOehyuABFF1ra2Glfd6JaBspiEKhDUTWhzYbN4QDcBsOEPhDQ9bRe66swsloK6eW5-3pZwf4M6erqrIAqFErQOn5GPGcI_3caR5nP4BSckXAdU9TCfskO-4M-d6Z2sSmPZRDFo8KhSwhG6p3Jq-qBI95fTNFR-hrdg4xK1oUMTruXEa2CbKC2vpIYXflh1U5jaIupFX2WWwu00hrOUfJ9UDTdG3mcqtpLeN7NidFGruRdFhqBIE42HCSYcBW5JIaVD7HalIfCEEJVIcrC8F3KZvHBd7cfr2PYYhl3XW8pbKCsYu6iGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصرع عدة عناصر تابعين لجيش النظام السعودي على يد انصار الله</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/91968" target="_blank">📅 17:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91967">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ce5ba33d.mp4?token=vICHvwIEFBGjfcxpSO8V9jaj8GkX36fhhOpESNzYTW4_9D_JQ6X6CjwWgjWlZZ1oVHuTZtG6O6bEl9hxC1W2uHgvLeDwhWtO47np4-XFq-hfSoQEqMe_Q-3AXGlA09X3QIPP_Mo1ZCP0DK5oUsioqCWoXt487KVTk6dKcJ1Afn8T-PSCN0pQun4LambL-d39rb136Gtfu-tcYHgDLZXiRxYgQSgw5XeoGuHo7n88zt5-AW7czwQPUtwnna2ukMcnt9FUG2KBxhJrN512lBaZTvKGjXmYt7Vpc1StiH3Mq5EpJl_MWA3mMJmCIum3bBdLyGELY5-JEHUpRGRerc29G4qAEL9rrD6mEggdz-_enwaVBQ3Bm_Ykw-9HqO7Fbu79fKlXsm4EOAdVLyujynuqxjrb9o1EFAridgiHHiw_-kMWK9z0zvVKWJsTW4nEB75t5psjBgtwLUX4VWjXNaymPsZctkYwDKEP3Qft6GDxj8jug72jem7-kMbC15d0tGlTJMzzlimseAvOdsUe083vDXLswEPungpYqZLlSoucx-nsOsNgihWgr8r8eOY9JY7-HaxshC0XQkocKJdKm1DSiUNE3HTlFeHeWic17g4iQYx-w9g0YOtZeYK-e18zkaKSLvfNLUmjhmtpbtGOg7QtaVDiZAv18WV1eEUb6kJcjsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ce5ba33d.mp4?token=vICHvwIEFBGjfcxpSO8V9jaj8GkX36fhhOpESNzYTW4_9D_JQ6X6CjwWgjWlZZ1oVHuTZtG6O6bEl9hxC1W2uHgvLeDwhWtO47np4-XFq-hfSoQEqMe_Q-3AXGlA09X3QIPP_Mo1ZCP0DK5oUsioqCWoXt487KVTk6dKcJ1Afn8T-PSCN0pQun4LambL-d39rb136Gtfu-tcYHgDLZXiRxYgQSgw5XeoGuHo7n88zt5-AW7czwQPUtwnna2ukMcnt9FUG2KBxhJrN512lBaZTvKGjXmYt7Vpc1StiH3Mq5EpJl_MWA3mMJmCIum3bBdLyGELY5-JEHUpRGRerc29G4qAEL9rrD6mEggdz-_enwaVBQ3Bm_Ykw-9HqO7Fbu79fKlXsm4EOAdVLyujynuqxjrb9o1EFAridgiHHiw_-kMWK9z0zvVKWJsTW4nEB75t5psjBgtwLUX4VWjXNaymPsZctkYwDKEP3Qft6GDxj8jug72jem7-kMbC15d0tGlTJMzzlimseAvOdsUe083vDXLswEPungpYqZLlSoucx-nsOsNgihWgr8r8eOY9JY7-HaxshC0XQkocKJdKm1DSiUNE3HTlFeHeWic17g4iQYx-w9g0YOtZeYK-e18zkaKSLvfNLUmjhmtpbtGOg7QtaVDiZAv18WV1eEUb6kJcjsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جماهير محافظة البصرة جنوبي العراق يرفضون الحصار الذي يشارك فيه العراق ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/91967" target="_blank">📅 17:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
🇺🇸
بعد الترخيص الامريكي لمدة شهر مع الزامها بارسال بيانات الملابس الداخلية للمسافرين الى واشنطن.. الخطوط الجوية العراقية: تهيئة المتطلبات المتعلقة بتنظيم الرحلات تمهيداً لإطلاقها من وإلى إيران خلال شهر تشرين الأول المقبل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91966" target="_blank">📅 15:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
في مخالفة قانونية..
مجلس محافظة واسط العراقية يصوت على استحداث محافظة الصويرة.
محافظة تستحدث محافظة!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91965" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏قامت السلطات التركية باحتجاز طائرة ركاب ايرانية بسبب مزاعم ديون غير مسددة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91963" target="_blank">📅 14:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:  السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران  ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91962" target="_blank">📅 14:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:  السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران  ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91961" target="_blank">📅 14:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارة الخزانة الأميركية تصدر ترخيص يحمل رقم (IA-2026-1516078-1) ينص على:
السماح للخطوط الجوية العراقية ومقدمي خدماتها والأشخاص الأميركيين العاملين نيابة عنها تنفيذ المعاملات اللازمة لتشغيل الرحلات بين العراق وايران
ينتهي الترخيص بتاريخ 28 أكتوبر 2026 مع احتفاظ الولايات المتحدة بحق إلغائه أو تعديله في أي وقت
الرحلات المسموح بها يجب ان تغادر من مطار النجف الدولي فقط وأن تعود إليه، وأن تقتصر على نقل ركاب إيرانيين لأغراض الزيارة الدينية
يحظر نقل الأموال النقدية بالجملة، والشحنات المخصصة للاستخبارات أو الجيش أو أجهزة إنفاذ القانون الإيرانية، وأي أشخاص محظورين، بما في ذلك الأشخاص التابعون للحكومة الإيرانية، أو الأشخاص التابعون لجماعات الميليشيات المتحالفة مع إيران
ما يمكن نقله من البضائع يقتصر على الأمتعة الشخصية والأشياء اللازمة لسلامة الطيران، ومنع تصدير أو إعادة تصدير البضائع أو التكنولوجيا أو البرمجيات إلى إيران، باستثناء ما تسمح به الأحكام المحددة في الترخيص
للولايات المتحدة صلاحية إلغاء أو تعديل الترخيص في حال عدم وفاء جمهورية العراق بالتزامها بتقييد الرحلات الجوية الإيرانية من دخول المجال الجوي العراقي أو عبوره
الزام الخطوط الجوية العراقية بالاحتفاظ بسجلات المعاملات المشمولة به لمدة 10 سنوات وتقديم تقرير إلى الولايات المتحدة خلال 10 أيام عمل من انتهاء الترخيص ويجب أن يتضمن التقرير إجمالي عدد الركاب الذين نقلتهم الرحلات المصرح بها وأسماء الركاب وأرقام جوازات سفرهم، إضافة إلى الأموال التي أنفقتها الخطوط العراقية في إيران على الوقود والصيانة والخدمات الأخرى المرتبطة بالمطارات</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91960" target="_blank">📅 14:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات تهز الجنوب السعودي</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91959" target="_blank">📅 14:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhthFEUxNz74JcbfFThnBmZrgZh6MsqQcaRcv-nVVyIUaJPF4-RHxRyUDeUGS7FfyN3pSLLyOLgS7KVUp3XB8riHjBpSmRGMIkRUevMi15c5Jdqq3ZIizfWJTnlUla6rXnVvllmHrXGuAB5uWXnBUGwL935x1sLLspomeO4MRKqYjgExoVF8TcdpoDA7XpNCBK8orKoQvVTuPIfLqXNwCKsj4NyjUgiOXRV519OpAww2FyPp57mtMyYfACHmL0cLbO3vryoac3_-Y2pfCsdKWWyKinoZ2BA6jqsODpQtE2Dtkv4vc_2Yx7GH-Llmnz2k7Ti7lNj8uSdmuwu62XejdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91957" target="_blank">📅 14:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91956" target="_blank">📅 14:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🔻
رسالة من حرس الثورة الاسلامية إلى الشعب الأمريكي
:
افصلوا أنفسكم عن المحتلين لفلسطين، الذين سيضطرون عاجلاً أم آجلاً إلى مغادرتها والعودة إلى بلدانهم! يمكننا أن نتعايش معاً بسلام.
تخلّصوا من الحكومة المارقة، قاتلة الأطفال، الشهوانية وعديمة العقل، وأسندوا إدارة شؤونكم إلى المفكرين بدلاً من الأوباش، وذكّروهم بأن العالم قد تغيّر.
لقد استيقظت شعوب العالم، وانتهى عصر نهب ثروات الشعوب بقوة الحراب؛ فهذا القرن هو قرن انتصار إرادة الشعوب. إن مواصلة هذا النهج اللاإنساني ستحدد مصيراً مؤلماً لأمريكا؛ لأن يوم المظلوم في مواجهة الظالم سيكون أشد بكثير من يوم الظالم في مواجهة المظلوم.
قبل 7 أشهر، بدأ الجيش الأمريكي المعتدي حرباً ضد إيران، عبر انتهاك القوانين الدولية وارتكاب جريمة حرب، وذلك من خلال مهاجمة مدرسة ميناب الابتدائية وقتل 168 طفلاً من التلاميذ، وبالتزامن مع مهاجمة مكتب عمل الإمام السيد علي خامنئي، قائد الثورة الإسلامية، واستشهاده مع أفراد عائلته، بمن فيهم حفيده البالغ من العمر 14 شهراً
وقد أسفرت هذه الحرب، حتى الآن، عن استشهاد أكثر من 3600 شخص، معظمهم من المدنيين، بينهم 400 طفل، كما تعرضت 8 جامعات و3 مستشفيات و8 مدارس للقصف.
إذا ساوركم الشك في صدقنا، فيمكنكم القيام برحلة قصيرة إلى أي مكان تختارونه في إيران، حتى إلى مضيق هرمز، والتحقق بأنفسكم من صحة تصريحاتنا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91955" target="_blank">📅 13:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇶🇦
المتحدث باسم الجيش الإيراني:
الحكومة القطرية لا تزال تعلن أنها غير مطلعة على وضع الطيارين الإيرانيين الثلاثة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91954" target="_blank">📅 13:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
إنفجار لغم في بادية محافظة المثنى جنوبي العراق؛ إرتقاء شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91953" target="_blank">📅 12:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
🇷🇺
‏
الناتو:
روسيا تواصل حملتها العدائية ضد أعضاء الحلف.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91952" target="_blank">📅 12:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A25sbkDaQUovrtxpqxz-_SvVPBJAJq8ejUoLo6ctup_Gvqfg_WzrhADY5lMBM4GWwapJ0fh4pEmt-Oke8sMhv_7d7yMcJY5Lzd-Jwfq0RU8FQx7cPX4ncSBqALqibrNFufYP7LuOAPbzdDam0BhKf-89bkKfj8CosQrWV4Coqi-m6XBFu_1YHaNms79ap3zXw8ZvGUrik0CrdQvdLWWumWZ4DYq2M5_s43gfGcFmWeDP8OnKqxuQBjNG7zcWhBcMDea-o1MXX0-lmNvj07H5hnIvq855dvhsLkc-QmwMJlzfDCe4tBiyihvqkhsiwse5ZYLuO3vhGJzo2zk_ueGJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سلطة الطيران تفرض شروط تعجيزية على المواطنين الراغبين في السفر إلى تونس عبر الطيران العراقي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91951" target="_blank">📅 12:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي يستهدف شبكة الإتصالات في محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91950" target="_blank">📅 12:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=DZt9nK2NnlIaCVcWInCyfO4py59qmz8WKSSzQua4hgrN63ct0UxpRfRzcW1vSTnhrhsnmHs2AYXuTrWirla2opr7sPyJ-hWyvO_hcwWiOaA4myvZ20raDsRy03VflYsHOTCF_m6GFQtvOJbttiv8j-uvkK7yk7W8vofPy8YtfntDGKu0dwe9_m1wuqArzxL1zU1htt0FGnFro3nv7gBrtck900x0npTD8dwLCpJ6sCfUSfGJOqhpJ97v_8NadulgSQEvET9zYNe8vUkZeG27lBUBT45-B-vo0OnbAmzTSy9tZE6exF1r2dzhLLGXClbvHgtTfYqcN0_jDrUmi_dqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=DZt9nK2NnlIaCVcWInCyfO4py59qmz8WKSSzQua4hgrN63ct0UxpRfRzcW1vSTnhrhsnmHs2AYXuTrWirla2opr7sPyJ-hWyvO_hcwWiOaA4myvZ20raDsRy03VflYsHOTCF_m6GFQtvOJbttiv8j-uvkK7yk7W8vofPy8YtfntDGKu0dwe9_m1wuqArzxL1zU1htt0FGnFro3nv7gBrtck900x0npTD8dwLCpJ6sCfUSfGJOqhpJ97v_8NadulgSQEvET9zYNe8vUkZeG27lBUBT45-B-vo0OnbAmzTSy9tZE6exF1r2dzhLLGXClbvHgtTfYqcN0_jDrUmi_dqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أعمدة الدخان المتصاعدة في سماء العاصمة الإيرانية طهران ناتجة عن حريق طال أحد المباني ولاوجود لحدث أمني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91949" target="_blank">📅 11:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBqPXmKiYgHXvvHI6CdqSIAV_F7qLkvTcmHiRwc2Fxi6kPXeCagiGezDBf6zDUoKP4_gIg42Xi_yQVpovfcOSxYqC4SfSkzEPsm1EtsekE7nUz-JntFIv8JEcX8iE8w1MFfxL8nintckTzZ8qs2x5hgxJwtv1X_Yb7ZTgKPPdhMzt9jEXxEK6wmmFvcnjt_UcbAUlVJIBegYZhgXGHiHFIARin8oBQmKb0yDW5ncjpOUVv6Ov6J6yKeCo3eVPqNvylOLhPILl0jliITm05apqQm9z8fS9SgNwnrVDG3o8zXgEGwoSmQifLpWI4l1jeBNYprLVqO7ztOaRARNpVnMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏توقف العمليات الجوية في مطار أبها الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91948" target="_blank">📅 11:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
المتحدث باسم الحكومة الإيرانية:
نشكر الشعب العراقي الذي يسعى إلى إلغاء قرار الحظر الجوي الاستبدادي على إيران.
منع الرحلات الجوية من وإلى إيران هو تجسيد للغطرسة الأمريكية.
نحن نؤمن أساسًا بأنه يجب حل القضايا دبلوماسيًا قدر الإمكان. لذلك، تجري مفاوضاتنا، ونعتقد أنه يجب حل القضايا المحلية والإقليمية داخل المنطقة نفسها.
قمنا برفع شكوى إلى المنظمات الدولية المعنية لرفع الحظر الجوي عن إيران ونتابع هذا الملف عبر المحادثات.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91947" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
أ.ف.ب:
قاليباف يتوعد باستهداف البنى التحتية في الشرق الأوسط إذا لم يُضمن أمن إيران.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91946" target="_blank">📅 10:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي يستهدف شبكة الإتصالات في محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91945" target="_blank">📅 09:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله اكبر
🇺🇸
اصابة اكثر من ثمانية جنود من المارينز في مضيق هرمز اثر تعرض سفينة لهم بصاروخ كروز بحري اطلق من قبل بحرية الحرس الثوري التي اعلن ترامب انها دمرت.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91944" target="_blank">📅 06:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
اختراق قاعدة بيانات ضخمة وشاملة لموظفي البنتاغون تحوي معلومات حساسة طال 2.76 مليون شخص على قيد الحياة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91943" target="_blank">📅 05:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91942" target="_blank">📅 05:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp829R8QDrgrZGr36NOS4BJUYPfaHMNLRVXQ2iv-Ris4wf7ifigYiDVJFf3oxRyCRh7FIuCPsGoUAWSYtKYBk5_kRhgNnHE-PgtgekyzIuoo_LWqq4a1bGQHSel3XejxhBlrqx6IioQzFFG1zfnvfdXl2vk8bwZ5TD_fJ3Mjhv0ouPFzjXex56KNe7GFU4PhvZBOCra6g3l8nbCFmNO3g6e7_JEyw1Fa-n8wdyjD_ZH3RVEMdxAry3waUvaOsOIindMtWFTrW1P-G5I2q7XV8JfKPuS6e8qOzDHJFBWTdRrlYI1ZpK8QRX54R_y1Iwo3dn8eGdxaUL79s3c2g_dcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
مراسلنا من مطار الملك خالد في الرياض يؤكد تأجيل جميع رحلات الإقلاع والهبوط فيما لم تُفعّل صفارات الإنذار لتجنّب توثيق عمليات السقوط.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91941" target="_blank">📅 05:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">روبيو: لو امتلكت إيران سلاحاً نووياً يمكنها به تهديد جيرانها والعالم، فلن يتمكن أحد من فعل أي شيء حيال المضائق؛ إذ سيكون بوسعها السيطرة عليها، وفرض رسوم عبور، وتحديد من يحصل على الطاقة ومن لا يحصل عليها</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91940" target="_blank">📅 04:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d8a438ff.mp4?token=t8XKt__tZF-xuidwp2SEWYKNV8gWIw-zA61nECmKMfVh4RDOv_bkOjY0rDKpK9MKiXowbgb9VpwxmPZOAuMVbz40J5CrLfH2zMR8579FvVSER-6w9ngPLEJj0XC4GM6KyRtltd-PZgWki9imQkZOKTxdCqB6nzO-oSFndmZu8JtvMVtAQwweG_5g5Re1kxgPBpygpSCH5hnCMrM40aLYJ6ZSzEYn8ccPNLR0EUParJDI92jxQuVw3-irY5l2fe9dfosrHWVPgSBH31VlUfgSCRUdjBITWPyqOzolYT71F8PilGUud7HZmDA4kBeTTPWuEvMYEQh4n6Su85P72SsF9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d8a438ff.mp4?token=t8XKt__tZF-xuidwp2SEWYKNV8gWIw-zA61nECmKMfVh4RDOv_bkOjY0rDKpK9MKiXowbgb9VpwxmPZOAuMVbz40J5CrLfH2zMR8579FvVSER-6w9ngPLEJj0XC4GM6KyRtltd-PZgWki9imQkZOKTxdCqB6nzO-oSFndmZu8JtvMVtAQwweG_5g5Re1kxgPBpygpSCH5hnCMrM40aLYJ6ZSzEYn8ccPNLR0EUParJDI92jxQuVw3-irY5l2fe9dfosrHWVPgSBH31VlUfgSCRUdjBITWPyqOzolYT71F8PilGUud7HZmDA4kBeTTPWuEvMYEQh4n6Su85P72SsF9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
روبيو: ستكون هناك تداعيات إذا تعرضت المصالح الأمريكية لأي هجوم، وإيران كانت تسعى لامتلاك أعداد ضخمة من المسيرات والصواريخ والأسلحة التقليدية،وكنا على وشك أن نرى كوريا شمالية في الشرق الأوسط والرئيس ترمب منع حدوث ذلك.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91939" target="_blank">📅 04:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70770abcc.mp4?token=OPqjVTLHv45TUKYfVUrHjzOmYPcxI4seqRsd149cf92vpmqx06Q_AisKSHC_dnOZD0MQqZg2Hi1f01KJjjpI1IyMe2fUyKnRuVqH6NXNmBzV6-mXUI5gdsVQdomvwXUHXmGA6T9GNZ_Jq689ZA2aXkzyNkcvysc7wQE20ktgNuhi47VfbIzqGp4zep_MBYNlgtel8hs9D2eg9ZbDwLEIcCN7dyFUax6F0jNOZ4K2w5fuyJsst7SDN5fXkYfZ-5LpuTEhFTeVQrh2wyln5q_UR2hXoERqRqYDz6V0hhFoBcd0AKGnJ7aSrWpcZlIsq85ueUDlOn2bzjmwBoYEvCQxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70770abcc.mp4?token=OPqjVTLHv45TUKYfVUrHjzOmYPcxI4seqRsd149cf92vpmqx06Q_AisKSHC_dnOZD0MQqZg2Hi1f01KJjjpI1IyMe2fUyKnRuVqH6NXNmBzV6-mXUI5gdsVQdomvwXUHXmGA6T9GNZ_Jq689ZA2aXkzyNkcvysc7wQE20ktgNuhi47VfbIzqGp4zep_MBYNlgtel8hs9D2eg9ZbDwLEIcCN7dyFUax6F0jNOZ4K2w5fuyJsst7SDN5fXkYfZ-5LpuTEhFTeVQrh2wyln5q_UR2hXoERqRqYDz6V0hhFoBcd0AKGnJ7aSrWpcZlIsq85ueUDlOn2bzjmwBoYEvCQxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
روبيو
: ستكون هناك تداعيات إذا تعرضت المصالح الأمريكية لأي هجوم، وإيران كانت تسعى لامتلاك أعداد ضخمة من المسيرات والصواريخ والأسلحة التقليدية،وكنا على وشك أن نرى كوريا شمالية في الشرق الأوسط والرئيس ترمب منع حدوث ذلك.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91938" target="_blank">📅 04:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=DkJQ6BEq4jWiE9ml5etTp8475G0ND-5ZAzkdeZi2MyxGrkkPpgYdk8j3BgfIGFpWjSGEJdMerYvbvq2ntM5N-F2c2lTb5OfJHWbXRGZVJszKaxfklyxfiO5a5VsNMkluXQdlHj4_5ikrjKG2cszFDursX0UyZA4PUKtsTc4WqQ8dZ4nWGrpyiyfUcc54norkyYdohXvaxVqaqVEy5uaYLToT7MzA4TTyT3Yloza-w-nREoC-enP-aQKmDB2LAvDy0sBHBYmSATKwAzTikCg6KuYjyJw7rqTQ2dd_mwkoSXlqIknw2p_SSnNUSxXsoXc2t9xnOchujMQPp6vn6UV5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=DkJQ6BEq4jWiE9ml5etTp8475G0ND-5ZAzkdeZi2MyxGrkkPpgYdk8j3BgfIGFpWjSGEJdMerYvbvq2ntM5N-F2c2lTb5OfJHWbXRGZVJszKaxfklyxfiO5a5VsNMkluXQdlHj4_5ikrjKG2cszFDursX0UyZA4PUKtsTc4WqQ8dZ4nWGrpyiyfUcc54norkyYdohXvaxVqaqVEy5uaYLToT7MzA4TTyT3Yloza-w-nREoC-enP-aQKmDB2LAvDy0sBHBYmSATKwAzTikCg6KuYjyJw7rqTQ2dd_mwkoSXlqIknw2p_SSnNUSxXsoXc2t9xnOchujMQPp6vn6UV5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مراسلنا من مطار الملك خالد في الرياض يؤكد تأجيل جميع رحلات الإقلاع والهبوط فيما لم تُفعّل صفارات الإنذار لتجنّب توثيق عمليات السقوط.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91937" target="_blank">📅 04:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d7be32d1.mp4?token=EEqKqzMLjJtErLyWQfXefCi2LeGiTPabHvC28_3gjGfhrtnkodDazxeqcN6D2Aayron-CmUaBwHw5a3h5vR-QuiNkZY_dZ5BMAQS0GbEuEXLL5VGjgMku1FGjZKG1zcI-TqeVEXTLY3B_xdqyOrTtbINdOt5ibjjtpT46SfTo9-3NoOYeGBz3-g8UEz_H5rTWFMUFJbqkStKCXp_qkYB6vQhYh120AqM2I7rlTilk2DP1J2fw86xe4zLuRmLEHi33OutInme8sJmkS-YYXcX4pk3HIGhZj1jJ4E8hLkumuw0rEMBXWDFXFFuvSEgpuj_g3XJPPh1LZCdsmzHsALJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d7be32d1.mp4?token=EEqKqzMLjJtErLyWQfXefCi2LeGiTPabHvC28_3gjGfhrtnkodDazxeqcN6D2Aayron-CmUaBwHw5a3h5vR-QuiNkZY_dZ5BMAQS0GbEuEXLL5VGjgMku1FGjZKG1zcI-TqeVEXTLY3B_xdqyOrTtbINdOt5ibjjtpT46SfTo9-3NoOYeGBz3-g8UEz_H5rTWFMUFJbqkStKCXp_qkYB6vQhYh120AqM2I7rlTilk2DP1J2fw86xe4zLuRmLEHi33OutInme8sJmkS-YYXcX4pk3HIGhZj1jJ4E8hLkumuw0rEMBXWDFXFFuvSEgpuj_g3XJPPh1LZCdsmzHsALJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91936" target="_blank">📅 04:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91935" target="_blank">📅 04:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91934" target="_blank">📅 04:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91933" target="_blank">📅 04:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91932" target="_blank">📅 04:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lop7sebUAvjFlEV0mItz9tOH9ryH_mJLuVI0MPkyhBBAyxUqgVj3LUIGOdMdMknYvlAVbJKKwqwmeiKjpC2m1GWk5ADGsyzxAZnqzKiY12egLbQh3psevQfZmu9T5HjXX_LeLCQnzlctc9TSsHZR81gjBxw4gRw_BYwm59uWc-K3V6NDTkxHWuNnZ55fgmlZeFsAYhal5Z-OhZgd7WIwLedstjz6XsRbirH8yxz5KU0wLGSIC4YuZLVdJyUcjMQ9kow82o3ehElzjGUf8ZIVr1GwF2Rrycd-MzOkvfcLFHveEOl1BF1Ub3o4zWzVC16uhtgo4NYzKdgqvmzGIVHZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
ايقاف حركة الطيران في مطار الملك خالد الدولي في الرياض نتيجة هجمات القوات المسلحة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91931" target="_blank">📅 04:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية تسلل مقاوميين.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91930" target="_blank">📅 04:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a57a9c44b.mp4?token=gTI4GWxMt8UUHdWGeIi5FqySUjJo0-wyWyQOic_7yIZwFQiVduuuyOY6AjTyj-NR8Z6dA_qVuAm_evi6eG8hCOnnWHA4bxIsf9aWuqFKN1TLhTLkP3odSi_Oscdau_ffWCc7pgwQ4kaydXDDnpSs33f25TRn2-XzHcN_8-vvhoHn9p18LjTQCYZ9Dt6CbWrpB7oDCFZKUUY9WiKKyZIQ8U3UyUUUEgm8m0hXRqWpS02gzUUlT9m3AUiIveeSvPimw_9PxeTHKRu2cj1mazxLiuSph3HepDd_M8dYVAshzd71PIVAS6WThSJb2zrqW582zDQql9nUqvatyN-fJF35Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a57a9c44b.mp4?token=gTI4GWxMt8UUHdWGeIi5FqySUjJo0-wyWyQOic_7yIZwFQiVduuuyOY6AjTyj-NR8Z6dA_qVuAm_evi6eG8hCOnnWHA4bxIsf9aWuqFKN1TLhTLkP3odSi_Oscdau_ffWCc7pgwQ4kaydXDDnpSs33f25TRn2-XzHcN_8-vvhoHn9p18LjTQCYZ9Dt6CbWrpB7oDCFZKUUY9WiKKyZIQ8U3UyUUUEgm8m0hXRqWpS02gzUUlT9m3AUiIveeSvPimw_9PxeTHKRu2cj1mazxLiuSph3HepDd_M8dYVAshzd71PIVAS6WThSJb2zrqW582zDQql9nUqvatyN-fJF35Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انسحابات مذلة مستمرة لقوات الاحتلال الامريكي من اربيل الى محافظة دهوك شمال العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91929" target="_blank">📅 02:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91928">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شركة أمبري البريطانية:استهداف سفينة تجارية بمقذوف أثناء عبورها في مضيق هرمز شمال مدينةخصب في عُمان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91928" target="_blank">📅 02:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91927">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
مصدر امني عراقي لنايا
ممارسة امنية تجريها القوات المسلحة العراقية بالساعة الثانية فجرا بالتزامن مع الانسحاب المذل الأمريكي من العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91927" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91926">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سطو مسلح على شقة مسؤول في منطقة المنصور " مجمع المنصور ستي " بالعاصمة بغداد .</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91926" target="_blank">📅 01:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91925">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اندلاع اشتباكات مسلحة شمال بغداد بمنطقة سبع البور</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91925" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91924">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85b26a8e1.mp4?token=lBI0rDU_Kc3fH7LEXDEkipeJK9EhSgDUmcZv_w2n--dms9kSBlfytV3CLUxsVgviSjFLWbb58fvIKfVbfFdluFpPnrcEo7RbISjb1bt1HVPnAKBF6iq-_e9UDYBlbZsX2NYcaXqorW0CVrpCVxrZ1W0_uFPHueCXty4gWwgcnKf9ZU93OcFN6fkT9Qjd9EsFT5xR1k_sWVQzKSs9wJPh6RLTR44K4d4w8NJlX5cNHYaHeCzA-F75O2wYtHRiBCqeFJWnEl9hQkwy0RaCJEjyhQ67HiB0ZlR2t20er_JDe7Wm3wGGnb93OED9aUCrc6E6gKFlAcvUKh1dvmEnTp5TTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85b26a8e1.mp4?token=lBI0rDU_Kc3fH7LEXDEkipeJK9EhSgDUmcZv_w2n--dms9kSBlfytV3CLUxsVgviSjFLWbb58fvIKfVbfFdluFpPnrcEo7RbISjb1bt1HVPnAKBF6iq-_e9UDYBlbZsX2NYcaXqorW0CVrpCVxrZ1W0_uFPHueCXty4gWwgcnKf9ZU93OcFN6fkT9Qjd9EsFT5xR1k_sWVQzKSs9wJPh6RLTR44K4d4w8NJlX5cNHYaHeCzA-F75O2wYtHRiBCqeFJWnEl9hQkwy0RaCJEjyhQ67HiB0ZlR2t20er_JDe7Wm3wGGnb93OED9aUCrc6E6gKFlAcvUKh1dvmEnTp5TTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتحاري يفجر نفسه في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91924" target="_blank">📅 01:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91923">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91923" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91922">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asmEKrwxekALS3yuOwrWdV51rM8DmwPCl4j3fZlpGtc4L22RXbWBe-WPk2dFU7qWyz_WG6sQlVhjOVwBo6yn5f7z0EKoPkuufUsbaTh1zwhago_1vPSWNetIuEcgdIc8_NE0BBRzlmZY_qn4YilY6yqu1GWXfS-xcKeLmjc2FYH1BmrvgoQpGnjtD0vUl4b0OcptdyMUvmHCvqFv4l48y5VTAUPUAunPvISh54stciR5JDLJG61fHXWfxfL4uv4UkziuMvUEXwOTesdc9W49asqxGGfJHhzPuf-fKhsNGscPJp9ImMck0wDyvxSvOpUPhojcgszgSBPJu9qecFe0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يختلف على صحيفة اكسوس اكبر الداعمين للجمهورين
‏ «نشر موقع أكسيوس للتوّ خبرًا مفاده أن "ترامب" عرض تخفيف العقوبات وإعادة الأموال المجمدة إلى إيران. هذا غير صحيح. لم أعرض عليهم شيئًا!» خبر أكسيوس، كغيره من الأخبار الكاذبة، مجرد خدعة، تُستخدم فقط لإشباع هوسهم بترامب. عليهم سحب هذا الخبر الملفق فورًا!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91922" target="_blank">📅 01:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ea1HYrJ76By3CwtOCKJhpen8Px8jFKXAJEv_0-cfFUTV_Ov-RDijvOdeOi3TuCx5mCsjCA3-6uV03UlWvRYbCoCp6wIphIr_5qk1isDa2rPm6m-r0o9IrVXXtbvvuSq5zY0sr2g1dABOa3-wrJglrsE3U88dxucRTlBhxIno-3m-lMFMYs6AEfHnKpm2Fkk_NQa4kT5UyyLCQr3hWWqpX60RlumI6XEZjoZms-VYdvh4yP6cHPsDAfoUYY_EhYoED9I4l0qNn2pxSa4RVMgMKgiwRosW40ULm8KWPEO56BVi_kY_05P9i1OTUfAbI9DxSX29h9ucQ6EmJRGYM-XnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqGtJxDCP4eSdXXnOXZ8j6_f92syo8F21QrviQxYeoEOkWBsRzr53gBVhRGAssYX9L-5ueH870waZueUhFWIY0b36Bi5itWy8OYVUTrwM7b4zk7qf7Xhqk1Je2OxRjcSVoJcgAVkYoSC6yTw2XMjjcWpXp05K-tcEsPXzrgIXlxYZFrk8_RQ89vnU8tfdhMKuxnXtMQf9KxqZAnTipTcSCyQUuCJhYiCykdf9WxUoZf0_AnQESxjltzkanFt4zgMYFd5sLFW4nGPEwwkcHUSXT6d1tXL-UgPNaD6cNpNPk03AmLcnZNA8z3xkMxYZJCvu4nDOEvwefRxpygHm_IFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5YAoWwH1gzSTD_JCXtAHbFTxMt55BySf9anXsiZ1ZOeLybHrAMUcSb2n6NXhDpbp_fIoXeWv2NMvDgSJKpaSMMKoj0Im_klJmArLUAvKeoOZzyztNY5bi-HVfnfgTkqApdxLE8zjachsj1wgM7toeRVUwdUxr43mAqva4Dfs08dHeweWlaovUQncv9lw2esTaJwLzqsdM_-0idXdDluNdJD1t6mGIIIE3dc4DJAKYV4sxS6-PP9a8Q9lCGngdnzfmxZruStj6GpCUv0C72lRVMU5HJhs-zpCxE8DI8JqRisuq8SQt5FsZAK-cRd78dc0wvb9Jxvojs3IvIE3hFpqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">البحرين: مسيرة لأهالي الهملة تُحيي الذكرى الثانية لاستشهاد سيّد شهداء الأمة وتضامنًا مع السادة العلماء وكافة  المغيبين ظلمًا في السجون.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91919" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91918">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاناشيد المقاومة</strong></div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91918" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91917">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromأثر</strong></div>
<div class="tg-text">ضليت راسم صورتك انسان
ذري، غفاري ومن جبل عامل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91917" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91916">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
🔻
وكالة أنباء الإمارات تعلن رسميا زيارة نتنياهو السرية: استقبل رئيس دولة الإمارات نتنياهو رئيس الوزراء الإسرائيلي يوم الأحد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91916" target="_blank">📅 23:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91914" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91913" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صافرات الانذار لا تتوقف في نجران</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91912" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات تهز سعودية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91911" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات تهز سعودية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91910" target="_blank">📅 23:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
القوات الامنية تعتقل المدعو  علي الهذال بمنطقة الجادرية وسط العاصمة بغداد ؛ الأخير يمتلك مقر وهمي باسم حزب الله في العراق ؛ مذكرة الاعتقال تمت على المادة ٤٢١ المختصة بالاختطاف والأخير يمتلك مقر ابتزاز وخطف مدعوم خارجيا لتشويه سمعة المقاومة .</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91909" target="_blank">📅 23:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">▫️
زلزال بقوة 4.9 درجة يضرب اليابان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91908" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4-tkZZXbpkgKXiJvVgaYu6v2xtk_oQ40KEf4pP9xO4Xn6lTZ_mMEj27zqWqdDuAfSrxDAAltSFGVxbKQ7QkSVhIh_n2LHd5j9Do7NtZhbCZEisVk9Ods6x6So4zXsjl8QCRvMqdPiTKc-LjUoOWHbo3GmgAHJedYDDh5isIvOKJnvcCBUmxIOy5dPjvmtiGIESvBByEGhALRXVPQn1ath244SUmbXYsM2D9Q2y2HCJkm06Aohg7IEvibTfrM4ATvxxmHJQmD2ZpwMhKMlFlIBCsP2tHfyG_bRCj4097bggysleJkPpTXtteut11upmQXwqd5cjALYQRDhLw5mmEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مسئول امنیتی «ابومجاهد العساف»:
در صورت ادامه محاصره هوایی ایران پس از اول اکتبر، مقاومت اسلامی عراق پرواز متخاصم را در آسمان عراق سرنگون خواهد کرد
روز سی‌ام این ماه با جشنی مردمی برای بزرگداشت اخراج نیروهای اشغالگر آمریکایی و ناتو از عراق برگزار خواهد شد و خروج کامل این نیروها را گام نخست برای تحقق حاکمیت کامل عراق دانست. او همچنین دولت فعلی را حاصل توافق سه‌جانبه‌ای خواند که برخی پشت پرده تصمیم می‌گیرند و به نخست‌وزیر هشدار داد دولتی که در خدمت مردم نباشد، ساقط خواهد شد.
او اعلام کرد اگر محاصره هوایی علیه ایران پس از اول اکتبر ادامه یابد، مقاومت اسلامی عراق آسمان کشور را زیر نظر خواهد داشت و در صورت نقض آن توسط پروازهای متخاصم، ابتدا هشدار داده و سپس اقدام به سرنگونی خواهد کرد.
@Naya_Press</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91906" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">.
♦️
اين ما حلِتْ امريكا حل الخراب
🎙
وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91905" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
🇮🇶
الحاج ابو مجاهد العساف: ستراقب المقاومة الإسلامية الظافرة الأجواء العراقية للتأكد من عدم انتهاكها من الطيران المعادي، وسننذر أولاً، وسنعمل على إسقاطها ثانياً.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91904" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV_mECnTZ_lJqWrHBsH8dAUPcPG0w2bDU4dWxzJRgwtzLiHBX6Av4PfB8FrS6axmi9mMzCrfSwtCdb3kQoJWJUC3OKY0wNSlzLrdb-pOyNSa989TBzaTkg5GCjkTgrFH9f2i9iqntcKJeoqTJ-5BB_RkBJF9X2kW9Qs644VHE42bXFDbmSpnTng17WvSaT-ARHUjw0LDEpPG-wer3UoWlB7dLloicwOhrcA3k1LjtLqz9Ujj8On7p3nvoiMYjyOaX85ISdXG0Cf4-Zf3FBNXCPwQQ4qIAbhvBSMr2TD8UU8wKIgQ9LjJNHTsfhWHKBobK2IiS8_Ce7DfPSyyC7m83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
تنويه: سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله ابو مجاهد العساف.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91903" target="_blank">📅 22:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
🇮🇶
تنويه:
سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله ابو مجاهد العساف.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91902" target="_blank">📅 22:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZYa_EcpyZ9W5e3ePpf1t6AQ9ZJwQYe3KRRZzuoY8mzLidEEdOA05BAwKXnlSXgTD2xMGRAa2mZ9pSLauYq8EN2j74eGkbXj8OkDbLT6UIYfxehyJNN7iZemK8FylBahm4pJQBmIXiTxIZ-AyGnpabKd5C43DLv8vZ6PocSeJ7NQZ8JVwIMGxRL5zw2_85FJCXqWUoYwvtGSb9Jv3z2-iReAm3siE0uZDZpuyQiym4Yt_sdIgFaFxge5pv-T5l5tJDl0s8jXAH177SQ6d0s26LxiFHauc75-vdsbHzDamyIHzA7DNgJDCfTMAEx7q-gzc9PfPx3JEj3mL0_nsxEk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🔻
‏خلال زيارة سرية إلى الإمارات طلب نتنياهو من محمد بن زايد نفي التحذيرات التي صدرت قبل 7 أكتوبر.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91901" target="_blank">📅 22:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74652b403.mp4?token=o6Ia3ldq5xdMCi2AqyeBdaAOenpbCN0UEN7hGzZQRfjm2psQP8dhuoUHi99Z__45PpNYoQruQyL1CLCIpvtgatCoIo05egJmdIaxwPmv_eGUmpme_ffWWLVNWISujyz_6Md8gzF0VmEYPTuP4_hN9iBLONX-bi1WXB4dn-8YrrEN5uBHmLpUWekuz46S4FupeOPJo1pePq_xClvp5FyK5BSz-olRiHzATgX7EL57VQOXJKA7uSBeT9nBi9A_DY9RvwqCXZ-FZ2M6F3cWjjnyaKDyO9iAG4mZLOWhUfXA3kD4dyjWTOpgrvdh_YA9fQArB51XLSyfynR4hoAS2hHEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74652b403.mp4?token=o6Ia3ldq5xdMCi2AqyeBdaAOenpbCN0UEN7hGzZQRfjm2psQP8dhuoUHi99Z__45PpNYoQruQyL1CLCIpvtgatCoIo05egJmdIaxwPmv_eGUmpme_ffWWLVNWISujyz_6Md8gzF0VmEYPTuP4_hN9iBLONX-bi1WXB4dn-8YrrEN5uBHmLpUWekuz46S4FupeOPJo1pePq_xClvp5FyK5BSz-olRiHzATgX7EL57VQOXJKA7uSBeT9nBi9A_DY9RvwqCXZ-FZ2M6F3cWjjnyaKDyO9iAG4mZLOWhUfXA3kD4dyjWTOpgrvdh_YA9fQArB51XLSyfynR4hoAS2hHEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إذا أردتم أن تروا الفوضى، فدعواهم يستخدمون سلاحًا نوويًا لتدمير مدينة. أنا لا أتحدث فقط عن إسرائيل وأجزاء كبيرة من الشرق الأوسط. دعواهم يهاجموننا بسلاح نووي، من أجل كل هؤلاء الأشخاص الحمقى الذين يعتقدون أن هذا الأمر مقبول.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91900" target="_blank">📅 22:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91899">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏المراسل: هل حادثة قاعدة سلاح الجو الملكي البريطاني في فيرفورد مرتبطة بإيران؟  ‏ترامب: ربما، لكنني أقول إنني متفاجئ من قيامهم بنشرها. لم أكن لأفعل ذلك.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91899" target="_blank">📅 22:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91898">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
‏ترامب: سننتصر في الحرب على إيران قريباً جداً، وستنتهي قريباً.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91898" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91897">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59404fbd6.mp4?token=uwI4ivKlzr_0DJU9u3xZ7VKWCpqHoMsd-cq5a_id7HRijGajgCzLJabFuMI7NBqHxS1JG8WMJpuZhiyJB8bgnM4WAbDWdvBJyBBIHNuyAyfMljfwTf0R6wNoJcSzAOLuGnKm_oH5xJRnW9kp_cGv51Osz1flnw6lbGOYTRYi_rMBzNAULope05K-nowhLHxC_3Ly0vZS9Vp4BazhWdCgVQ5eaUrpJ0uSdYreYsNnCJrcu0B0hiOMiEP7NzKHTzWNW-ZeixJ16xj6NrxfudxiT492szIIElCz-ayFn0ks3Y_KAiaeY0qOBBQHM8mTkPeLTdORBvO7LsZo7K-XE55zCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59404fbd6.mp4?token=uwI4ivKlzr_0DJU9u3xZ7VKWCpqHoMsd-cq5a_id7HRijGajgCzLJabFuMI7NBqHxS1JG8WMJpuZhiyJB8bgnM4WAbDWdvBJyBBIHNuyAyfMljfwTf0R6wNoJcSzAOLuGnKm_oH5xJRnW9kp_cGv51Osz1flnw6lbGOYTRYi_rMBzNAULope05K-nowhLHxC_3Ly0vZS9Vp4BazhWdCgVQ5eaUrpJ0uSdYreYsNnCJrcu0B0hiOMiEP7NzKHTzWNW-ZeixJ16xj6NrxfudxiT492szIIElCz-ayFn0ks3Y_KAiaeY0qOBBQHM8mTkPeLTdORBvO7LsZo7K-XE55zCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: سننتصر في الحرب على إيران قريباً جداً، وستنتهي قريباً.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91897" target="_blank">📅 22:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91896">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
محافظة البصرة:
بدأنا الاستعداد لاستضافة خليجي 28 على ملاعب البصرة وذي قار.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91896" target="_blank">📅 22:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91895">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
🇮🇷
الخطوط الجوية العراقية تستأنف رحلاتها إلى المطارات الإيرانية عبر مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91895" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91894">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=BA1rlUt4qszN1i7rGDajhC3W-x1_JNR2U9etFcwqztISkpW1fn9ZKVAMJqFgQzZENqtn9eqFYGEBxduh4nw5Un0PecPmVa9KoV1fXShk9Suw4SK5dBSxe0nCDWZ3HhWQrVHL8xjM7AtbaXKhYE96vwSbD-5V1-4SEWy77CgkQWrht8zwvtM9BTmLX4nr6UrkdLqspS6ijr-3xt3wfklptUlC6wiwJQeS6jfn_3g7kOwpEcnLNhRGEyTq9vL4ROsBeVm9StpRShfl1hS2C2H5ZnSR8AkasIpspiteEe9PBfWFPrlLCRHP44gpxFLuMsbQXb4040xYaShZkHYhZGn1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=BA1rlUt4qszN1i7rGDajhC3W-x1_JNR2U9etFcwqztISkpW1fn9ZKVAMJqFgQzZENqtn9eqFYGEBxduh4nw5Un0PecPmVa9KoV1fXShk9Suw4SK5dBSxe0nCDWZ3HhWQrVHL8xjM7AtbaXKhYE96vwSbD-5V1-4SEWy77CgkQWrht8zwvtM9BTmLX4nr6UrkdLqspS6ijr-3xt3wfklptUlC6wiwJQeS6jfn_3g7kOwpEcnLNhRGEyTq9vL4ROsBeVm9StpRShfl1hS2C2H5ZnSR8AkasIpspiteEe9PBfWFPrlLCRHP44gpxFLuMsbQXb4040xYaShZkHYhZGn1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91894" target="_blank">📅 21:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91893">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
الاعلام العبري: صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91893" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91892">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfx75oTDEjkAI99gHQ3mUuPkdrQmmuN9t9FTtMFy8PPUhZyNgGLvGKZpjJyzaU9tkY3-7IGqlmO-P-nIIN_zujuOeLPatuMGkppaMciAO44oTJgmzYpL72bwqt3qHbzDpbaf33wWBTuKPXxu1fbmdS_jV5NUEIC00Dv7Ftm6PcZFCSRdq_2xXdyGxoFOZTRReBxNNp5JNG1PofMBmNdx0c_9U2onEKeuIuyhXk2p7MHyHPuOgRFL2dXAb46RYB97Fc-XnDUeyU-UifFH05ZWpK3n0fSV29JX47W8M5SAtz4rietroXU68hzceA3CSFd9ZibS8Styknl8w9sAK4V-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سيادتنا_لاتفرض_بالحظر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91892" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91891">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏الولايات المتحدة تدرس إمكانية التنازل عن العقوبات، ‏رحلات جوية بين إيران ومدينة النجف الأشرف في العراق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91891" target="_blank">📅 20:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91890">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91890" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91889">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
نجري محادثات إيجابية وبناءة مع إيران عبر الوسطاء.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91889" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91888">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 38 غارةً جويةً وصاروخاً من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان استهدف العدو بها محافظات تعز وصعدة وحجة وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1123 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91888" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91887" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91886" target="_blank">📅 20:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91885">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇸🇦
السعودية تستأنف تصدير النفط عبر خط الأنابيب الشرقي الغربي بعد إجراء الإصلاحات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91885" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91884">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91884" target="_blank">📅 20:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91883">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ترامب منفتح على تخفيف العقوبات المفروضة على إيران مقابل "تقدم ملموس" في القضايا النووية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91883" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91882">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c474fe6c26.mp4?token=M95nUJq6YQG097Qv-vQ8nXc5OOMBrKNx9XDcZhVgzsXYAzB0aQVhjP3AQcvRG6355Ti25ytMAhzpTVfl6E_hQ17QqI1OM5rzhh9bj2sespMBAwlc9tJw61LTPSnvPPVI7g6WHQ_ZeM28SNUtTe5EPXf7DLnUM5aa2qDK1LGzuDFoPjN0sKL_2P2xViIbjPYJtBHGCHjB0L2TRswi_o0TgJ6_JawITNRTcEoUc27YDMfRKW7lriuihaHAXGGSnT-wm7POMWsqF_2IT_JmFFOyOejNr0Hpyw4km1Of_YJ7UamYnMdFrBfSKwFhFwjFJ0f7mFH4GYVvoc_dLB8rxvUSIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c474fe6c26.mp4?token=M95nUJq6YQG097Qv-vQ8nXc5OOMBrKNx9XDcZhVgzsXYAzB0aQVhjP3AQcvRG6355Ti25ytMAhzpTVfl6E_hQ17QqI1OM5rzhh9bj2sespMBAwlc9tJw61LTPSnvPPVI7g6WHQ_ZeM28SNUtTe5EPXf7DLnUM5aa2qDK1LGzuDFoPjN0sKL_2P2xViIbjPYJtBHGCHjB0L2TRswi_o0TgJ6_JawITNRTcEoUc27YDMfRKW7lriuihaHAXGGSnT-wm7POMWsqF_2IT_JmFFOyOejNr0Hpyw4km1Of_YJ7UamYnMdFrBfSKwFhFwjFJ0f7mFH4GYVvoc_dLB8rxvUSIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار عسكري في منطقة اليرموك بالعاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91882" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91881">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91881" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
انباء عن اطلاقات صاروخية من ايران.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91880" target="_blank">📅 19:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مقر خاتم الأنبياء المركزي:
العدو الصهيوني الأمريكي ظن أنه بإقصاء "سيد المقاومة" جسديًا، ستنهار دعائم المقاومة، ولكن حسابات العدو، مرة أخرى، باءت بالفشل.
جبهة المقاومة لم تضعف فحسب، بل بلغت مستوى من التكامل الاستراتيجي الظاهر والخفي، ومسيرة الشهيد السيد نصر الله مستمرة بقوة في لبنان وفلسطين واليمن والعراق، وفي أقصى مناطق الجغرافيا التي تمثل المقاومة والسعي نحو الحق.
القوات المسلحة الإيرانية، إلى جانب مجاهدي ومقاتلي المقاومة الإسلامية، مستعدة تمامًا للرد بشكل قاطع ومدمر على أي تهديد يواجه الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91879" target="_blank">📅 19:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91878">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJFJpciks4fT6vzuvgheZS7YvZLT78eOpyNnm1rH9f4Vtkbq9_RkaGJdjiELVvQDRoUCRImcVdFKWAKmJ2GDISSWUtcxMnoSoXrRQOmMTtpjklvME24QTW2FQWx_Odv-A--Nydp92zPw1WugxKepJyf48prD7XpXUcMfGE20tWQzS3_uBNnO-Qxka5_utyT7WwxhUsraWOBSJARFZob9lLHzTva8Y4TFHNe2rgjqitJZNtdNwTnDEyw_IBNc7CVYdYpO_b9ut6xeMBLGVXxUraO1u6rMwzOgtt5qENs7IX5IritjYP_TMggMNXRbN1OMMrfRZdZpndqLHqkENfIXAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية تعلن إعادة حجب لعبة «روبلوكس» اعتبارًا من مساء السبت المقبل.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91878" target="_blank">📅 19:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91877" target="_blank">📅 18:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
المشكلة الكبرى هي تفجير مصافي النفط في روسيا. هذه ليست مشكلة شرق أوسطية بالمعنى الحرفي، بل هي مشكلة روسية في المقام الأول، حيث تتصاعد حدة التوتر بين أوكرانيا وروسيا، وتقوم أوكرانيا بتفجير مصافي الديزل في روسيا. لقد تحدثت إلى الرئيس زيلينسكي وقلت له: "يجب أن تخفف من حدة قصف المصافي.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91876" target="_blank">📅 18:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇱
الاعلام العبري: سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91875" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
