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
<img src="https://cdn4.telesco.pe/file/KbteY4qQzX364hZpKecS82tCojVcWe9zjkVDtcoN_rC3Kjf9zpdqtfD7e1hssJiT2A6sCfQP3BlC_97u1PJTDq57O7SwDpqfc_BhNx0NfdkqMe1WPsRV7Bmr2clmJ4yDJQtOL18KArR-Pfxvb4Tl7kGWMBeKzk4JPKYz5dQmfLjK6mwOAU6qQlvsOYtcRGm_tCmu0jm4RdGf2aFz96lr4SUAgVuE3UhoOf5q2zDiJAIIaMdODAIhys2CZS51-2kpQDAI8YM1XqBtGHP2xAgemElLvHpVmpxD-ulylKqc9H-aQ4VRArDkP4j59vK7U2uW_Zjwp7yFu8lv51dGbIfJWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc22d2744.mp4?token=PJ_Wzd6glHuQeemMnJidjR8nYwIuIhtLc9m84RuoTE5JARArQqHHZN9s2lemCqLyxGpXVwpUEUtGziw4PHahk8VEw1TUZCfZ_8RQmwVonslWoifsa30IqcFPrsxsPX9jTJMIfnDRxAkMmFwRV6jwDRCD3rZWN2ANebtYgHuLCDahSSiVaWeXxcXAtD5IKwOm9Flj6oi-Kp5VBO23OC0CXqNQy7XpoR_P1lcMUxm5hD7X32Mbb16T5Mi5_iJN8C-boIlRmO28EpZLX_Xh38r-lpTlGLYhZgCXqK77XR2tANgWNkxlr8y3EYUM538tAmLhLSAAcKMdtOt5EwuWvUe66Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من إطلاق صواريخ اعتراضية من مستوطنة المطلة شمال الكيان المحتل لاعتراض صواريخ حزب الله.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/naya_foriraq/78975" target="_blank">📅 11:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7652e2bde8.mp4?token=L-sseXeiYOIYla0uX3kUs4aWr7H6_dTEBzn-t0233WDplbdAN3MsGdpHzPBQf6xOaTJL71D7hzGNAgpWjfseS9RP70uLBPBPNNeqkN2kEl9hpVRuuFuWojiddleEgj8fUYqNnfbeYuf2oOn0nUnqhtDMxLCSS5agzDPmPIWqu4ld7BdzVqi8-9gVipNs1bWix1RjcX5fX99l4b3m4CQ4pub8pJM3qiI0oK3gXoS4UnU6nE0ZQxHudM1BUVDNqkz1zPOiOBwhhkDQqe3zUnSCroQcpOXhI0tZOFeYjwgGcRAGlOOmeLl8cs8vc0ZVJ1c1wcZDH_QRNvb7giZBmivPL44tLYytmESWLQtTc_H3kvmX5wNfbITvAJUBjQIX4gIHz9G4oRUljH7XNXMzx1QzxzIdyH6woheVugrAPTMCDf59Zos4Fp3DozxloIWpGtDe4bqtVz2ird4fmQbOT-EzQ1dGc7DwOAxqewwO2VFNqGZnOqkfEtSsWZ2fwkCy0yszwCMrTCNPXzldA0QStHF0-5C2ULG_XohhKLIwRgrCwTvPP666sFM-IUlzxFLMcKcf5ZLVc9U_Ny_wg9MF3pTs1lVIoBvRayTnU7kRP0nVwO-mbjmXW6b9ex9uOtIVSQQpttOWLKJqrEyFL_y-KaYLwsJOwoIpZpUMZxgE1bLLEcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات  إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين  جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة  البدء الرسمي…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/78974" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
وزير الخارجية الإيراني: سنطرح الملف النووي وإلغاء الحظر في المرحلة النهائية من المفاوضات
إعلان نهاية الحرب أهم ما حدث في المرحلة الأولى من الاتفاق وتم إعلانه صباح الاثنين
جولة جديدة من المفاوضات بين أميركا وإيران ستبدأ في سويسرا يوم الجمعة
البدء الرسمي لتنفيذ مذكرة التفاهم سيكون يوم الجمعة
نهاية الحرب في لبنان موضوع ملزم لنهاية الحرب مع إيران
سنناقش الملف النووي والعقوبات خلال فترة المفاوضات التي تستمر 60 يوما مع واشنطن</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/78973" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=S5WZlpxBV5t00x_F57Z27elcDgLQ-AWzNzolIIwShr5WHPwyRcWyhCkBqlhdtmIzJdG6engfz0f04z58hWQ7LXXHkVIi7g8-b-iTq-4uoVjrt2YHNUCTIgiQVDO30h4afZiCpaDchCRIkc3Fxr84M-uVD4nluE3LIAlOjQa5Z1yiTXbRa8kgtPfICgD5ZoSh9lMqukWloJULi0narnfmX6cLAEjnljhCbUDrwPaE-_6KCM3z520ZZYBjyPF4TTUnngweV4YcHAr0DuAaZoaBYpiu_DmSFWX0Zck6_j9_5DHSkZ6w6DKSaAEVtzb8LOIZVaGLCquOb_l_sOFISsIADg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59974eb34.mp4?token=S5WZlpxBV5t00x_F57Z27elcDgLQ-AWzNzolIIwShr5WHPwyRcWyhCkBqlhdtmIzJdG6engfz0f04z58hWQ7LXXHkVIi7g8-b-iTq-4uoVjrt2YHNUCTIgiQVDO30h4afZiCpaDchCRIkc3Fxr84M-uVD4nluE3LIAlOjQa5Z1yiTXbRa8kgtPfICgD5ZoSh9lMqukWloJULi0narnfmX6cLAEjnljhCbUDrwPaE-_6KCM3z520ZZYBjyPF4TTUnngweV4YcHAr0DuAaZoaBYpiu_DmSFWX0Zck6_j9_5DHSkZ6w6DKSaAEVtzb8LOIZVaGLCquOb_l_sOFISsIADg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇱
الجيش الأمريكي يبدأ بإجلاء طائرات التزود بالوقود المتمركزة في مطار بن غوريون حيث تمثل حوالي 20% من الطائرات المتواجدة حالياً في الكيان.</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/naya_foriraq/78972" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📈
بورصة ICE في لندن: ارتفاع أسعار الغاز في أوروبا بنحو 1% لتستقر عند حوالي 512 دولارا لكل ألف متر مكعب</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/78971" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2de826483.mp4?token=rIaXc8QgioQugoBgl1upgAS9TWffEwDr-uPA23r0_LdHptvCRd2xpLW6zyxLbbKsoA92QP0ZWS0yw17r8cI8iFjGhrS1lwNiACUqSOskNTK9WiaC8l1RgWhTj39hpKuMIEGjsHuMuiYi_Vhmrh9gC82wUBpJVCwJCnpoTeNmOj9VKMPbFhWsKAhOgPDakDpPdo3a_MfWPUDC9H84M3GnOP-zNWT8R12Y7hfncXn58jGDec_2Y-K7WtSisQi8VktU4FmTQVt_42cwx65fLn25cNmQx0Sx1Ih5x9Dv8sW6j9VYsNKvXLTVWJ4O6r94fQSgbYfAoNddfotJgBb_-tahlG4fw55gwuo-3Ycjv0j465dJL3OuEBNzz-LCwuEln-LhAU--mDMApwxmbwfm9eZAxff_DHbe0VhUMePyoIF2MkrSPOdV0HWbVPHZmErfM9wlAVpZ8daFS2XN1c9ro1zWR1WFxoSj0YNebfzXZY46aePkPGjLas1scG3uvKfGPL44PeBvfKW8PdS2vK342J290PMl9JFlv9jxYCCqdLJ3nEfFMecYkkYm-ZaBPsBvDjh3aaSVMpuRB_8s3JnLeUHU7Hm1ztzBsxrhR-uUWbJBbsY01Vv8jUxhY_-oxDDK0ixgJ8VOQyg3d_A9nsA4hp7leySnDIXw6KrZULMtO7sYdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/78970" target="_blank">📅 09:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة المطلة قرب الحدود مع لبنان متحدثاً عن نتنياهو: إنه منفصل عن الواقع، أدعوه للمجيء إلى هنا لرؤية الدمار عن قرب.</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/naya_foriraq/78969" target="_blank">📅 09:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a58183f17.mp4?token=mEbdMLJpTVQ0aF8N4iJrjqxfVLpu_C5C2nPz5_kx3YHdr4EBPItImGMFevgsMA-m_-YQgS3st7cAtQ92Hlp3gvJ9u-ohW57s2HJSlp3Vhz0gSZxc8Z4OrIYcSaZev-1a3wbjxM1_YF80AqMpneWyvww-zNQHE4g-xAbQuylQ2Ic3P_0-j2KBpbO3xxVFn5Ko4lHiTn387TEJY13nRdCuJlgRGtMdnanWTk9aTwXwp6PL3VGuWVFaUYkJSU5fqYe0jWW4X2GExuvJdS5KmL4PhnTKlGpey8sGKF8AsaBRp-D1rU8SSe-xkj9AtMo_Ghw9lBP-LnjzBt8RiZx1_pIxc5HxtYWc72J_j8OprHJHA28R3owm0ON0DJ68eqT1ZG8mMOQNwMPjwUNMRbtTNaQ7qKITOU-H4E6X2NaL2UyjOoSgQH8e-w8Jcgntuo-9T12l18bbmcDKvaIjW6E2D8eCR6mJ8Y0y5S3PJaGLZFbn151CwgDfaYJx4e-TFEF1Sh44aotbVS3zU06VXn1QlwMLowVIrx1dmIX08-PmdKqMJwkMDJtJkiy7UPOSnyfcu1T02bcbv61D6Z4Z5ixZsTrBnKlRoEN_HJ_trPsv_ksqlluhDKf8YwcMlFaVHk9OxWFbUxAGSBTY0Ix2bkl0QKwKCVPSEy7kjnUYH_LdemeuEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الجماهير العراقية تشعل الأجواء في ولاية بوسطن الأمريكية قبل ساعات من بدء المباراة بين منتخبنا الوطني والنرويج.</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/78967" target="_blank">📅 09:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حدث أمني عند معبر حشمنوئيم في محيط رام الله الضفة الغربية بسبب إطلاق نار على مركبة</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/78966" target="_blank">📅 09:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=KtpWEg15_xxreh_Jr-AOJOZ6_Q6q9zDT3GU9ysZUV7oUX-96GSA3vuKFndVEif_d7dEeRW_1IgUrLx5Vt6T8xyEBYi_d3SYwzDgyikOujIhU3_EeNlkSjeH284MH39vIvHKiscqkwIZbBvDJsxlAp8Li9uhLMLAKl541jv0FMZNBrZcQd6wG9egWl0jG3fuFbWEo9DaQSv37xaET0I8KaqzIm7tgY5aWGanEjVFfY7FTHfNTNehjbRIgac-j7RBMEfwy_Z6kqa9lgdRZYkLzjAnUvBpZPsxC3LlRITJI1Qc8YKPVrrtaRT75gEBPvjM15S0NX7_edRKwrP09Lc5vnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4be2373.mp4?token=KtpWEg15_xxreh_Jr-AOJOZ6_Q6q9zDT3GU9ysZUV7oUX-96GSA3vuKFndVEif_d7dEeRW_1IgUrLx5Vt6T8xyEBYi_d3SYwzDgyikOujIhU3_EeNlkSjeH284MH39vIvHKiscqkwIZbBvDJsxlAp8Li9uhLMLAKl541jv0FMZNBrZcQd6wG9egWl0jG3fuFbWEo9DaQSv37xaET0I8KaqzIm7tgY5aWGanEjVFfY7FTHfNTNehjbRIgac-j7RBMEfwy_Z6kqa9lgdRZYkLzjAnUvBpZPsxC3LlRITJI1Qc8YKPVrrtaRT75gEBPvjM15S0NX7_edRKwrP09Lc5vnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فكرة رفع علم الأسد في بطولة كأس العالم كانت حلما لترامب ونتنياهو لكن الأحلام حين تتقاطع مع السياسة غالبا ما تستيقظ على واقع لا يشبهها وها هو علم الجمهورية الإسلامية الإيرانية علم (الله اكبر) يزين ملعب لوس أنجلوس.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78965" target="_blank">📅 05:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=jFiI9z3VmgGEJhbjm7BzrEsU-xG-rM7oFL_3xDso3x_rnfR3nLlH3yJ6u0Zd1RmONCTFkjq0RK_36s4y6-RrdDg3mdYzQS3TVeIh6xpiqp_OKlhwedGiRMlC8_8dgrgmiPCMMAGx8vOTU0N1bs9dfcY_koXvqf4bRwNR2MXyGQq0IRZ7z6sewnVP7ZQFsE7KpddwUPSHXMdHzAsHogL1TsYQkM1-wGg9GZto44DwTNeaHp8CQVHrVkQPGAoLLbUxg3bcoKd6DadkYXn80acS6f25EBNPTmWIWJtB4JbGWra4sUG2HuJU_NL6RbBHO5Q2cVnTmc97QX3E9iUI8vRqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29d91e814.mp4?token=jFiI9z3VmgGEJhbjm7BzrEsU-xG-rM7oFL_3xDso3x_rnfR3nLlH3yJ6u0Zd1RmONCTFkjq0RK_36s4y6-RrdDg3mdYzQS3TVeIh6xpiqp_OKlhwedGiRMlC8_8dgrgmiPCMMAGx8vOTU0N1bs9dfcY_koXvqf4bRwNR2MXyGQq0IRZ7z6sewnVP7ZQFsE7KpddwUPSHXMdHzAsHogL1TsYQkM1-wGg9GZto44DwTNeaHp8CQVHrVkQPGAoLLbUxg3bcoKd6DadkYXn80acS6f25EBNPTmWIWJtB4JbGWra4sUG2HuJU_NL6RbBHO5Q2cVnTmc97QX3E9iUI8vRqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بداية مباراة المنتخب الايراني و المنتخب النيوزلندي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78964" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrGSIz15SKFDdj1gJXwJBjig5cSZwKBlD4Obz1VYM2w8iAu6o_WHnODHr5TydCluxM4EeGf32qWbNLNkFfNBXZeU-lTDFzs0sv94vp6qH7Z3jEcK8gIftzgK7PRXfwYOXMfcJCOEtOMzLuZs4if1ZUuXmcjltrCf1HZvf0GoQe1GnPILlLY7p6nilNo0bf0C4Y7RHpDRKfP-EvbFtM-lC4f8n_eT2WPxu4TvgGuFtDMDoZa2m8TIsxwf1a5DbP9SWv7WtpL3qUA4udV4ED-zTurDKgxxSkZB4QqpPtTjs_g4W89VrSCBeodM9XjOV27RsamUjDi7DV4dLjBguxO7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:وافقت إيران على عدم امتلاك سلاح نووي أبدًا! كما أن قصة دفع الولايات المتحدة 300 مليون دولار لإيران هي أخبار كاذبة، نشرها الديمقراطيون!!!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78963" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئيس المرصد الوطني للإعلام "خالد السراي": أبو آلآء الولائي رجل شجاع ومقاوم والإطار التنسيقي أساء له ولم يدافع عنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78962" target="_blank">📅 01:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMphCccjRJEcUh1jzr71AkNuzhR__4VgeCsg8U2_QG5g48XrwVuuFeuPYoVbRq6ffttDNyu7BEiZAh3fANUC4j_HW1_6WCy_CcdiT0Bg97V7tCccSZG0ut_Akln4Q0ySb8mnmopt04bNpME_3jSqZNbI_oCEs3JpnhImznwFvmwi746WYpOErcDuFgn8JdeKiOppYvmh3Ba7716j9-TeyvpwDJpI0ipc0jTBeGH_N2ZpzsDwZ7jMjPCckKBAT2Cf0ujJ6VzkDCeBd4b0c0-YzX_p2YfBwC1pB7-48xYrqksOEzF-d110WtDqo8afFpEOWHNhaCl87uHnLF9eIJj-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/78961" target="_blank">📅 01:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مصدر امني لنايا
...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة من قبل القوات التركية إضافة إلى تنظيم شراء المواد الغذائية بكميات محددة لكل عائلة!!؟</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78960" target="_blank">📅 01:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=SnQOOjMNBAKrq0UnMV9WAxRtDdry1ADuA7tsW_unCwGdume3ASaXVEvJO6i66wfS6wh2O2pRHKqTBz6iZ5H91YXafEQ7cMGs_OJG_DuFngRYesPzyt2k4pXD_60iYHk-f0FqODvDJhHuX7jahVD6569echMMNJQ33DjunVFl93l0RKIElM3uztVFbZUtJZreXlfjVRVgwLlocsFhExcZGPXN1Zg3QWutX0m0-h39TLwo5DHhJTP-VoLOL135ezjNxovNTaNwNFZtWnGFKcKDQ70BS3dYKWQfHclvFmlaFqQQFr9T2Li8aEoyEf3HR1pOCq2wH_t2LaxS-4_0xNZq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22131f5c0.mp4?token=SnQOOjMNBAKrq0UnMV9WAxRtDdry1ADuA7tsW_unCwGdume3ASaXVEvJO6i66wfS6wh2O2pRHKqTBz6iZ5H91YXafEQ7cMGs_OJG_DuFngRYesPzyt2k4pXD_60iYHk-f0FqODvDJhHuX7jahVD6569echMMNJQ33DjunVFl93l0RKIElM3uztVFbZUtJZreXlfjVRVgwLlocsFhExcZGPXN1Zg3QWutX0m0-h39TLwo5DHhJTP-VoLOL135ezjNxovNTaNwNFZtWnGFKcKDQ70BS3dYKWQfHclvFmlaFqQQFr9T2Li8aEoyEf3HR1pOCq2wH_t2LaxS-4_0xNZq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هروبًا من المحسوبية وتدهور الأوضاع المعيشية في إقليم كوردستان العراق،
لجأ شاب كردي إلى ألمانيا لكن رحلته انتهت بالقبض عليه وترحيله إلى بغداد بعدما وقع في اشتباك مع الشرطة الألمانية أثناء اعتقاله</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78958" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
الاعلام الايراني:
تم البدء بتنفيذ رفع الحصار البحري الأمريكي المفروض على إيران، حيث عبرت ثلاث ناقلات نفط وسفينتان تحملان سلعاً إيرانية أساسية "مرتا" عبر الحصار البحري الأمريكي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78957" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7cdxKlKBohHESKxumFinUW7kxnm_jhD7yLrKNhkX3GdxdNHN-PYtzmga77TqGohTIHGDj_kWOloTWW0I1bsiqnjXkvzhgWot-8ZTzJ1EdYlIJHF8YI5sfK9VNvRZqJP_avMUBYHeJMYG_vwwgzZUJ2sLDxFKLRQZuoTdQr_CZK-DQ3GZfQuRSpX0jARzowkQl7kn8HDXfbPxuiH8DE74QRz-rqUA4P2KfInxUFI1Cpcl5ZixMaWgjQ33J97zV_Y0W-H6uwGPM15i-muLVgZPkzbi5f95Zo-7lrlU-Sm1q0-uXe1_wmfsu3PA0H-uR6fPTElC1sEsWsOQXYRAoh1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
في ظل تعثر السياسة الخارجية الاميركية واقتراب الانتخابات النصفية للكونغرس لجأ الإعلام الرسمي إلى استخدام البروباغندا لترويج لإنجازات استثنائية لإدارة ترامب رغم أن العديد منها يندرج ضمن المهام الاعتيادية للإدارات المحلية ورؤساء البلديات.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78956" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilZg1XrhX_MD3sGOiiSy2MVezbuhJNMfvkzJpnJ1LPGLz216mfOa99-pd0t-UiJfI9h0j8OjkGnAUXkCHpN0YF-X2dvDJQ59KCo_BIQP4Gd-lFK5DTx_1N3p9UNVGWSUw76aOY0cVReatGcr1WeKyDN8JXiDtQFS1COgCwB_FBOL3DAO7UCvDTGcHSHuyGcqntKBnOdpJojKgqQxUs3EbBBtVzJlhyTC1vbkrdmgPkYPZNFp8gTDcA3hruV_cmzi32apbs-I03-jR64jDlxwPkmhDZ0CW14NH8f1Yl4BQCvgbLmgLnPXqQpROJVc_OngLVDo7aNKOlcG-8i28rYHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الحاج ابو الاء الولائي:
وإنا على العهد باقون وعلى النهج ثابتون(لن نساوم).</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/78955" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الطائرة التي سقطت لها قدرة على حمل القنابل والرؤوس النووية   وشاركت بهجمات على المنشاءات النووية الإيرانية …</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78954" target="_blank">📅 23:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
‏عقب تحطم قاذفة B-52 لاسباب مجهولة، أعلنت قاعدة إدواردز الجوية إغلاق المطار وتحويل مسار جميع الطائرات القادمة، كما علّقت جميع تصاريح الزيارة غير التجارية حتى إشعار آخر، لتكريس موارد القاعدة بالكامل لعمليات الاستجابة للطوارئ والتعامل مع تداعيات الحادث.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/78953" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKq6O0wqfX1e3cnYk7p8VyeXseV-fcwQ1E02n8h-F6guM88_Kkig0AWoZ2ybz2yd6sLhJZqSXsa2EvyUYkYDhc6ZFBa41CXD93t6CWp8LzpsbeKU5P9RQywmuORHz1Bcu1BP6lu7QCfunGot5tAizncwjnqfngdftzOAxUIw0__WSMnlCNfUbf_zbSTCG6Y2TemmWo6DdkQQi4cL8Rg8a67u9-C6vUX9DXDTgTDUPKJWTyLgvpM9POfncuIopVWvM3MOqIsRMv-sldGIgnBs7ZrwBZ4lMVTM1eWuHQnj8jPV7yoM_mhCD1deCBUDmvfolp9Gg2ffiFm6ARy4ype63Aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb2aab1af.mp4?token=gsGnLol9x-I_9onKDFGeREu_DQxl82700CBn5O1Z0B89qQsyIrIiljrWM_om_RL_qv_2zn75_KR8HemyizPmOSXNdemkl9mms4lv8a0F4T5RIVm6RGRYvlhvt4wO5TF59QYQzzljPqlHusNEZbbbkhcbMMgJHs4xuEhAqLMQQVMEE2U_IPOE2kTTXQmxU2lDVIgnAyhjuF5NnVkA5WQRLzjOtphTh_aH_qn0LXNqBoImrSFk8xTkgxiB-6SIKdJFJAJSSKiMUDguVvUR_IM1nSCvnfFIAohBrt-i3-_ThxcKeCLxf9AgK5Nmx-HP73oQMf_Uyr4xaD60giR-xMLQKq6O0wqfX1e3cnYk7p8VyeXseV-fcwQ1E02n8h-F6guM88_Kkig0AWoZ2ybz2yd6sLhJZqSXsa2EvyUYkYDhc6ZFBa41CXD93t6CWp8LzpsbeKU5P9RQywmuORHz1Bcu1BP6lu7QCfunGot5tAizncwjnqfngdftzOAxUIw0__WSMnlCNfUbf_zbSTCG6Y2TemmWo6DdkQQi4cL8Rg8a67u9-C6vUX9DXDTgTDUPKJWTyLgvpM9POfncuIopVWvM3MOqIsRMv-sldGIgnBs7ZrwBZ4lMVTM1eWuHQnj8jPV7yoM_mhCD1deCBUDmvfolp9Gg2ffiFm6ARy4ype63Aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
العراقيون يطلقون وسم #الله_يستر  على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78952" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رويترز : تحطم طائرة بي-52 ستراتوفورتريس تابعة للقوات الجوية الأمريكية يوم الاثنين بعد فترة قصيرة من إقلاعها من قاعدة إدواردز الجوية في كاليفورنيا، حسبما أفادت القاعدة.  ‏"أرسلت فرق الطوارئ إلى موقع الحادث فوراً والوضع مستمر"، حسبما قالت القاعدة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78951" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=eAmu1Dbbx8q_8eptPF4TjXtpUYB8oJDAtLqefkTpKReRHr7LuYTVABZzttZyoR9s2Rmh5LhqzQ1Lef_Xst5qtYtGJ3zXiW_tm9SlkZDSH2ljxM0m29hvyjRbUQGUMlLl5-9I4tjkZddJ7xWr8uu-yy-FZMxCSJWqfYJPJ-H1FrNVB5WyDxpouvZM0feOkN-Rw1uFjl-PRJvj6iu3vBs2twRCJX2AsSm-dnkfWgL7Vn8dHM1EaowR06Ucd9kgnmpbiaVYJpdz-wY5aG3K6p7RuWtqZXdp8NsRmR1lnjzsPRq4l6nzUpQ82pN0BxirIKUpv5YgageA4I4tYtkFo6a92Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc8a91edc.mp4?token=eAmu1Dbbx8q_8eptPF4TjXtpUYB8oJDAtLqefkTpKReRHr7LuYTVABZzttZyoR9s2Rmh5LhqzQ1Lef_Xst5qtYtGJ3zXiW_tm9SlkZDSH2ljxM0m29hvyjRbUQGUMlLl5-9I4tjkZddJ7xWr8uu-yy-FZMxCSJWqfYJPJ-H1FrNVB5WyDxpouvZM0feOkN-Rw1uFjl-PRJvj6iu3vBs2twRCJX2AsSm-dnkfWgL7Vn8dHM1EaowR06Ucd9kgnmpbiaVYJpdz-wY5aG3K6p7RuWtqZXdp8NsRmR1lnjzsPRq4l6nzUpQ82pN0BxirIKUpv5YgageA4I4tYtkFo6a92Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تقتحم مدينة تدمر بريف حمص السورية وتقتل عدد من الشبان وتحرق ممتلكاتهم تحت عنوان الشبيحة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78949" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_zljPd5wjWgGv2s2EpkIMBh5DvYzd0shiixeY9F3gVy66ivcg4vKp1TpzmFeSQIEBc8PwTSq3NAy1vwDRYmQ4cwT2EEXL5zOLAHAHDAsaI0l02GrGBOj0sqyo6KPwiwq5yJsPWHsfIGz4Yckfmb7DxA_9vcAr35RWVxBCkhsbGcojMLKTov4Q4bhC7LF0uodRuGfouAB11VTrB5exnvuf9PJpTdUrKyVocAKViPKyPO7AuUi2dh8zCLFW5N6zSTEntVCatGEbt2ybJojc0ulehkOJlNozetx-31wP_Q6T8o7Ogx33oxfAegnjBNMqA2rXr6W6-JWufLY-4B6btVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
العراقيون يطلقون وسم
#الله_يستر
على مواقع التواصل الاجتماعي ؛ كون كاتب المنشور في موقع X قد كانت آخر نصائحه لمارك سافيا الذي يعتبر أقصر عمر مبعوث أمريكي في تاريخ امريكا ..</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78948" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=DptkWLYUADHe4F-IfPEdPnmliRBNR_aLm6JBhj8VYXSKzbhl7OLuj8qiUa5b4SCtcWCrE1SDthb6eKxQTNNkoqIKGqGlEdexB_mBYomjowgetBR1MZ_26GY0HWB-a4R7MBhyMA6ZCCZ181nA3wgZEvlwKFSPLbCl0xdwHIT_AeZH2cmUs-wgPPUvMdybbvunO0MEOXbfgBIemTfmiAjBamMgzT8oLO4K0GJFJK214Yo378WsO_S2barxV3RUfx4LQjbR-91WigOJg7jDYzO_GGHgy8dCyihgZLsbbVT4TFK1PmaO9j5HPNCqCBlNdFdc7Z4pCb_--EU8NOIjNO1qHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18ec03199.mp4?token=DptkWLYUADHe4F-IfPEdPnmliRBNR_aLm6JBhj8VYXSKzbhl7OLuj8qiUa5b4SCtcWCrE1SDthb6eKxQTNNkoqIKGqGlEdexB_mBYomjowgetBR1MZ_26GY0HWB-a4R7MBhyMA6ZCCZ181nA3wgZEvlwKFSPLbCl0xdwHIT_AeZH2cmUs-wgPPUvMdybbvunO0MEOXbfgBIemTfmiAjBamMgzT8oLO4K0GJFJK214Yo378WsO_S2barxV3RUfx4LQjbR-91WigOJg7jDYzO_GGHgy8dCyihgZLsbbVT4TFK1PmaO9j5HPNCqCBlNdFdc7Z4pCb_--EU8NOIjNO1qHTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78947" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41580de098.mp4?token=OPfUOv8efYpU9-iG6U1Uc4WXR8hSS_o0_qV6seENbQJYuTSFpUMAk_LYH0YynJlm-UlvqhN0lV5H09tVw-wZLZvd7kvyNdZpYrReURrCnZS3RynztedD8Um6sbb_gpnjTDsXoKVHv14N4A8rYWjyK8YdtvDxFiRV21sllF6gybq_M6RIHsqXzL1X7XwRDuacDQc4f979rFuSzsukp67JoTAvrGu1ceAOLt3t-xekLjUvFXM88IUdMTVor4x3SlfCcFgLEriWCkPEvLDuRMuYF31Jl2r10vsz4hA7l3303nUJLe2QS-lGjAQGN008R3nILcj9Reptnab2v5-lAfaoSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحطم إحدى أهم القاذفات الاستراتيجية في سلاح الجو الأمريكي، من طراز B-52 ستراتوفورتريس، بعد إقلاعها مباشرة، فيما لا يزال مصير أفراد الطاقم مجهولًا حتى الآن.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78946" target="_blank">📅 22:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTrZrLKdlJ_Wm3qqmrZdA5dmb6gPGyF4YRXu8oAA2SOTP3d8w2RTHFCyU9Ki4sqr1XeuXobyO76rbm6cOPBIpA_UG9sqk41ZAXkATZYirvbyKO2AoUg5XHC5y0nSEsXB0eY73_W6cSHKosC6CpvFri9qI5PHip2xpnWjr8i37KLOb6uecl2vJyhcpSmH-m_Hy_qAIzK8RckytmMTVlk9eEq7Se8zzbGULkYjDPwZXAyQouoATNIkxROEcXOHsDVGrdAKqXjeu_S2RkZ07AM9j-ubVlHsCGgllbkqPEJC6-Eeqmw2-eSiCUJy0_iiitkjGdD1dJfI6wIU_-zRRuv3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=m2XTGsFgHMsbh3jz_RCisP0WCKmqVxCP3qf2H3cDR6kMmj08zH2uc0Cr4qzEWypD9qTu_ut04pntWcpP19bpVMz2NUrvpF5cJamEcaaXbvnx06FFovGb3ayGM9l2j3xE3173yrBrnKy8Say1MHN97YhuG6aIx5YISyTdKKemp5kIZXoY1XAmI5j3mAAdGPRkrPsk3wkpVdwjyhQR63cFyrMJf-8oEhVLMezUYKVpvJGx1JxWy8nZL0sjfRV6DwpWqsQ3FQqxOI2KqfMGBYP0GbCL3-NwqFLlVUC_mgFLImWpaPhP5SrKHy_i5-MI1DUnpkKeoPmSZQdhbNDAGzDIXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0694a202.mp4?token=m2XTGsFgHMsbh3jz_RCisP0WCKmqVxCP3qf2H3cDR6kMmj08zH2uc0Cr4qzEWypD9qTu_ut04pntWcpP19bpVMz2NUrvpF5cJamEcaaXbvnx06FFovGb3ayGM9l2j3xE3173yrBrnKy8Say1MHN97YhuG6aIx5YISyTdKKemp5kIZXoY1XAmI5j3mAAdGPRkrPsk3wkpVdwjyhQR63cFyrMJf-8oEhVLMezUYKVpvJGx1JxWy8nZL0sjfRV6DwpWqsQ3FQqxOI2KqfMGBYP0GbCL3-NwqFLlVUC_mgFLImWpaPhP5SrKHy_i5-MI1DUnpkKeoPmSZQdhbNDAGzDIXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حطام طائرة B-52 في ولاية كاليفورنيا</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78944" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7_6L1ypO_-jMVvoAENXjyK68tOkGhBXQ5Vj5toR2aveOXix0ydvj9NtenZKMKr9BnIsfLDn_CVeUDHw0jpJj5J66manaMxA2F3bpO6O_rU1D57FEakcC9UZtgDMKHOqROLo7tZVvKbySc3oEvIHEzLW2rUkM_CtI87W20vfFe2U96lwQ3eC_ia5BFCZSaOMuXhb-N_2WiqXFqX_iHcD9ZjAS3NUnBMuXy93encTdsdVN2FnDaYkjS_eAF3SANPms7vgRwWoRbhUEBCbfUjs_ABHubzdlLqw_Uw1KTjDyMrI3l50_dfRfo9e06cl4Pb-tGr_gJvQizTvMdWQH00paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
طائرة قاصفة شاركت بقصف ايران من طراز B52 تسقط في امريكا !!!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78943" target="_blank">📅 22:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcsIdV7cmINoIstVx7ua2L1zAdY2gOGmR29zmahxq-N7fSooG6y82wqrYLeFDTIRnV77YXjw-njhHjhRPTZxJQ9tqUhxwaVf1eiEj7lF7bzokfmSRs5DywZlVZhYVPfgGaQ-EJGJ10toe5td9QTxSku2k2TQ5BsC5lyQatuI3PKlI9UG4hoaporam965bq_mXosKZAEUb37SSroD8XUGs6E9hIbG-OQHQUbFqo1O0B4p1WFdl4sZcQE03_bTP5z8d99-sUiuMXcrfY056FKDng5zPJXmc5h5YFtVpMHXoP7zj0O0yVFlWmrmR74r7qOgIGt0pP6yeD1ABAttPOUPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78942" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🌟
أعلنت قاعدة إدواردز الجوية في مقاطعة كيرن بولاية كاليفورنيا عن تحطم قاذفة من طراز بوينغ بي-52 ستراتوفورتريس بعد إقلاعها مباشرة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78941" target="_blank">📅 22:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">إغلاق مدخل العتبة العسكرية في محافظة سامراء !</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78940" target="_blank">📅 22:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مالك تطبيق تلغرام :
تريد حكومة المملكة المتحدة حظر وسائل التواصل الاجتماعي للأطفال دون سن 16 عامًا. بموجب القانون الجديد، سيتعين على جميع مستخدمي وسائل التواصل الاجتماعي في المملكة المتحدة "إثبات" أنهم فوق سن 16 — باستخدام بطاقة هوية أو مسح للوجه أو بطاقة مصرفية. يتم اعتقال الآلاف في المملكة المتحدة بالفعل بسبب منشورات سياسية كل عام.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78939" target="_blank">📅 22:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78938" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !   السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !   ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78937" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الإخوة في سرايا السلام ما هكذا تورد الإبل !
السيد مقتدى الصدر اعزه الله دعا لنزع السلاح وحصر السلاح بيد الدولة وان السرايا مرتبطة بالقائد العام !
ثم ما علاقة خدم مقام الإمامين العسكرين من الجنسية الإيرانية يتم اعتقالهم ؟!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78936" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aeb08e28.mp4?token=OMqG4k7ABYkQ26QSnaHOZZzherT_1cqgGI124HALD0W2JcANYXl00eQZqSSW6myicIGBoos7JTbgsNxjgyvjhqGlfjROs90UwqaqoiHcpnKyjdNk4HuojCweLIopaMHQaLK-Vg5UHjZzC0TYNd85jO3lZf_Kz7cY_KdsMWjHOIrwXk4K2k-jwHHcLjh6130LJqJ47Tr07Fx7X53ToonXG1nY26rPl11CiHmHqE8VTPZXvgxo2HxxPGruGXvq0_tXzwJYwr5HLXKMDywj8y7OMO7ZhJhuCJbRrMoG3nNsJHdLQENNoLgc_ZQK54k36Xi4mKin4WmQThOGhLMbFFmm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وزارة الداخلية البحرينية التابعة لعصابات آل خليفة تصدر قرار منع مشاركة بحق عدد من الرواديد الحسينيين في مراسيم العزاء بشهر محرم الحرام: الرادود عيس الغبص الرادود حسين الأسدي الرادود يوسف القصاب الرادود محمود الشهابي الرادود سيدجلال البلادي الرادود سيد حسين…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78935" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78934">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe6cd6ef1.mp4?token=Yz7kU630qZKnYVDwQlZqajB2SpGwaHjTG_DVvzFxlm_o4BItNjns58MRTcfHuTG7DN7UeHPg-fu3bgCk56_6u46Ii1nqX6cNTFQr3C4otLwZDk3iusLxFM_WED5PC4q2rEAJx_jkeECxi_b1hynSW1LGSnWVJeIMa9OKM5sQtsS2JrxgFgEnOEJ7O9bshrBEOrD-Pj5c48yv4ehX0APDbTGJk-cf_zbln9g4OmU1JiYdxHejU0EM1JDkFWj_lGDGdJA-ifQBwEPLeqj4z8-AVFGWjp43Xkx1Z26H2aKV71uujId45oe7tzXXGrcBFb6XsBB1QIAZ3BnbfuxQsqpJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: ترامب رئيس الولايات المتحدة، أنا رئيس وزراء إسرائيل - أنا أدافع عن مصالحنا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78934" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتن ياهو: لست متأكدا من تفاصيل الاتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78933" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو: ‏هناك خلافات بيني وبين ترامب.. العلاقة مع ترامب شراكة وليست محل تنافس أو فرض قرارات</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78932" target="_blank">📅 21:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏نتن ياهو: أنا سأنتصر في الانتخابات المقبلة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78931" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتن ياهو: لم أقل إن أحد أهداف العملية هو إسقاط النظام الإيراني. قلت إن الهدف هو "تهيئة الظروف للشعب الإيراني".  لا تحلف مصدكيك وداعة حايط المبكى
😄</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78930" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏نتن ياهو: أحيانا لا أتفق مع ترامب في الرأي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78929" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
الخطوط الجوية العراقية تعلن تفعيل خدمة الصعود الإلكتروني وإختيار المقاعد قبل موعد الرحلة عن طريق التطبيق الالكتروني.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78928" target="_blank">📅 21:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتن ياهو: هناك من يريد تقزيم الإنجازات التي حققناها</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78927" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتن ياهو: دمرنا أسلحة نظام الأسد وسنظل في المناطق الأمنية مهما تطلب الأمر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78926" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏نتن ياهو: سنبقى في المناطق العازلة في لبنان وغزة وسوريا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78925" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتن ياهو: قتلنا نصر الله ومنعنا اجتياح الجليل</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78924" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتن ياهو: الأمر لن ينته مع إيران بعد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78923" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتن ياهو في محاولة لترضية الداخل الغاضب: ألحقنا ضررًا اقتصاديًّا هائلاً بإيران سيستغرقها سنوات للتعافي منه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78922" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#ترفيهي  ‏نتنياهو: لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/78921" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبية لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78920" target="_blank">📅 21:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#ترفيهي
‏
نتنياهو:
لقد حققنا الكثير وأبعدنا مع أصدقائنا الأميركيين خطر التهديد النووي لإيران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78919" target="_blank">📅 21:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇱🇧
حزب الله في اول بيان له اليوم:
ردا على خرق العدوّ الإسرائيليّ لوقف إطلاق النار، وبعد رصد قوّة تابعة لجيش العدوّ الإسرائيلي مؤلّفة من جرّافة ودبّابتَي ميركافا تتقدّم من حمى أرنون - الكمّاشة باتّجاه منطقة المعبر في أطراف بلدة كفرتبنيت عند الساعة 18:15 الإثنين 15-06-2026، تصدّى لها مجاهدو المقاومة الإسلاميّة بالصواريخ الموجّهة ومحلّقات أبابيل الانقضاضيّة ما أجبرها على التراجع.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/78918" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
إن الشروط التي قبلت بها الولايات المتحدة في مذكرة التفاهم الخاصة بالمفاوضات مع إيران، وفي حال التزام الطرف الآخر بتعهداته، يمكن أن تُرسّخ مكانة إيران بوصفها أحد الضامنين لمستقبل لبنان في المحافل الدولية. كما أن إنهاء الحرب، وإلزام الكيان الصهيوني باحترام سيادة لبنان ووحدة أراضيه والعودة إلى الحدود الدولية، يُعدّ إنجازًا مهمًا لإيران ومحور المقاومة.
وإذا تمكنت الولايات المتحدة من إجبار إسرائيل على تنفيذ هذه الالتزامات، فسيشكّل ذلك نقطة استراتيجية بالغة الأهمية، إذ سيُضطر هذا الكيان للمرة الأولى إلى قبول قيود يفرضها عليه حليفه وداعمه الرئيسي. أما إذا رفض تنفيذ هذه الالتزامات، فقد يكون ذلك بداية شرخٍ ذي دلالة بين الركنين الأساسيين لمنظومة الهيمنة.
وكما أشار القرآن الكريم:
﴿بَأْسُهُمْ بَيْنَهُمْ شَدِيدٌ ۚ تَحْسَبُهُمْ جَمِيعًا وَقُلُوبُهُمْ شَتَّىٰ﴾
سورة الحشر، الآية 14</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78916" target="_blank">📅 21:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
🇺🇸
نتن ياهو:
يمكننا شد الحبل مع الأمريكيين، لكن لا يجب أن نمزقه.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78915" target="_blank">📅 21:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8wzFKkPU00w6B0-mOkiImOC8YgiieYQvp6DT41YQVcKo_W1Sntgi8X44zrkAH4yszTOocrCGj72Wj2wGykxrkbz7DZzTNLKQ9JhHAy6kum1JPVLhTBikL2nLQd9YfFKH9JEG7i7Ajn_bT-KkAAa3PcVGntTUlNxsj-AWNDl82aRKMdBFyQ-e48L_1EqVRoWs6Sx-Wy88qvgNQySl7EadQfHKKoRUUylW55MD_F70q_JI0HeRfafgMNGyLgBhWl1uk4KzLXqucMSHsLNQAXSipD3xBGSw2ZfBeR2loz5BY1EDTgsAo-Zf0hiYS52YOYQzO70ovemz3SioV14myikZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان: ‏إن مذكرة التفاهم التي تم تطويرها هي نتيجة أشهر من الحوار والمتابعة المستمرة في هذا المجال، وإذا تم تنفيذ جميع أحكامها بشكل صحيح، فيمكن اعتبارها وثيقة فخر للبلاد. ‏أرى أنه من الضروري أن أشكر إخوتي، الدكتور قاليباف، وعراقجي،…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78914" target="_blank">📅 21:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofWnvbEmeCYj50pbN_rltgX2tcwpl9-5hohvGTAzXBCWqOXkhHvYBJePgXQPY12nNLc2t6mVw4XbIdCbsZKmbpV1e9B8DRrQKL4Z0BJ5Eh395FVVzeJaC304C7oqKHknPJNKdWPQh2jP44Tp-pLY8vPlGa50lT6UzrDjARvAYFx3mrW9-OdKx3IdopcnRkbVVFxjkwY24aHabvXEqnto3l8NGhEFvAyHu4cHJWgaaOFjeRkt7HSR8wUNDSuGI_jrG-UVtY3MzFZYH28mAl_DOKBTVsopiWqwJb7UAT6xZefygQmwLzoc3fFDGuWj9HHDzoYKe8iRJlWQfcqv4cZXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏ بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78913" target="_blank">📅 21:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBWS9Jzpz4QfWPF2TRzx8S_KD4hB7xMQPdWvKod5pH6mtO7XDeN0tfv_Rj7LbMXK155sNjd97C10n-WNLpzyqadH5bFecnprttvaMzHXNVojYo3_fS_gSLvYyVQUmXEybO8lYdm8Su-zIMx_PQ8nzoIZumcFRdK28zZl7dGtWGj70RCtPfTASGWGbQ0s0L25L73impVDKV1FwAiy1SGAslu7ZrUkCHWIvfFSTofc5aaC1-kzh9Tbwnpr9ZqmdPgNHiuXXaua1jB96mwbdcxgTNX_XLKajP2BM4_Nn1Kim_lnHUyU8fuxe_cTX1X2DVCxiGSkm_nceQjEU4WRyVmP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:‏
بعد مناقشات مكثفة، أيدت أغلبية أعضاء الحرس الثوري الإسلامي نص مذكرة التفاهم لاختبار مدى جدية الولايات المتحدة في احترام حقوق الشعب الإيراني على أرض الواقع. وكان لتوجيهات المرشد الأعلى الدور الأكبر في إدراج بنود تحمي المصالح الوطنية الإيرانية، ونحن ممتنون لذلك.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/78912" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
لدينا تاريخ من نقض الوعود، وعدم الوفاء بالالتزامات، وإلغاء الاتفاقيات، وكل هذا حاضر في أذهاننا، لذا فإننا نبني خطة التفاوض وننفذ التفاهم الذي تم التوصل إليه على أساس انعدام الثقة والتجارب السابقة. وفي الوقت نفسه، نسعى جاهدين لخلق أكبر قدر ممكن من الانفتاح الاقتصادي للبلاد في هذا المسار. من الطبيعي ألا نفوّت أي فرصة في السياسة الخارجية، لكننا في الوقت نفسه لا نعتبر أي فرصة أمراً مفروغاً منه.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78911" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏴‍☠️
🇺🇸
بن غفير يلغي زيارته إلى الولايات المتحدة بعد مماطلة السفارة الأميركية في منحه تأشيرة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/78910" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PptYk_xOM6E5cwZAgb_yHWmF07xuWrqaCjhGgEFmKMbmNezgxJZky3wgdZisBq7RW8cjI7hHB8J2eYeyzbvi9db1LV7Vj3-o9ERT6NQa8j8bute7jtN8Hkb8m_q2H21m1bmm16dU2Tu63WHVUVikRbK1LbgMte-zxTkej4svNwl9KbgDApo3_crT9CmqFgJL6WdU5qC8YT2R6fsyfZIuxopSTj0LXwXJWpxFwkmT22tpVXsMFgoz8Y3vddijiSPk5Q01iARx1n6X6_bIZzFFUCBwlXTP3vB6VmRWvOAsiXPkMVeDkmzjeX6H0YOo5dG1Nm5BbWLR7FxkgXruzH52qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفع الرايات العاشورائية في مدينة النبطية جنوبي لبنان تزامنا مع عودة اهل الجنوب</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78909" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اعلام العدو:
محادثة متوترة بين نتنياهو ونائب الرئيس الأميركي حول لبنان، فانس طلب من نتنياهو انسحابا تدريجيا من لبنان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78908" target="_blank">📅 20:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبية لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78907" target="_blank">📅 20:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
- الجيش الإسرائيلي سيقلص نشاطه بمنطقة الخط الأصفر في لبنان
- المؤسسة الأمنية وجهت رسالة إلى المستوى السياسي بانه من الصواب التوصل إلى اتفاق الآن مع الحكومة اللبنانية</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78906" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اعلام امريكي:
احتياطي النفط الأمريكي يصل إلى أدنى مستوى له منذ 43 عامًا.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78905" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🛐
مكتبُ السيد السيستاني يعلن أن يوم غدٍ الثلاثاء هو المكمّل لشهر ذي الحجة ويوم الأربعاء هو الأول من شهر المحرم الحرام لعام 1448 للهجرة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78904" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a751e7c4.mp4?token=S0faOBaqM8kDvIuH4Kief-vhqwguECqIuqEvqsZGPuyBCzMx8AlvgJQ1JSkylkjpqC5fA_qNtSHhPOJUnWsBErvP2O1jYgUm1YlI9qsPi2qkL4KijBqyBKig7XjVf5oXaOYziSbg3811OTigOwwJMZ0BcFz4WMofElz5nV3PGqw4YYkAbpw_otiIVJ7SniyTNPIv1s1AsFh4LiZhEN5RHGg0cxLUt7eZkoMW4x_hyxS-qTb4U3OKV4qCvq_D0f5fyY6h1-WNb27rEM6l2XwPXY-tZQeibVzSLP_Y6BPfkl_tPM-pwzT4MlmrkaV6Od7-s24A2tW9bud4eM6A6IirhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a751e7c4.mp4?token=S0faOBaqM8kDvIuH4Kief-vhqwguECqIuqEvqsZGPuyBCzMx8AlvgJQ1JSkylkjpqC5fA_qNtSHhPOJUnWsBErvP2O1jYgUm1YlI9qsPi2qkL4KijBqyBKig7XjVf5oXaOYziSbg3811OTigOwwJMZ0BcFz4WMofElz5nV3PGqw4YYkAbpw_otiIVJ7SniyTNPIv1s1AsFh4LiZhEN5RHGg0cxLUt7eZkoMW4x_hyxS-qTb4U3OKV4qCvq_D0f5fyY6h1-WNb27rEM6l2XwPXY-tZQeibVzSLP_Y6BPfkl_tPM-pwzT4MlmrkaV6Od7-s24A2tW9bud4eM6A6IirhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
الرئيس التركي اردوغان:
لم تتحقق خطط تحريض الأخ على أخيه هدفها. ‏لقد فشلت محاولات إشعال نيران جديدة من الخلاف بين الأتراك والعرب والأكراد والفرس. ‏بالطبع، لن ننسى أبداً الدمار المروع الذي حلّ بمنطقتنا، ومأساة الأطفال الأبرياء الذين قُتلوا في ساحات مدارسهم، والاستهتار الصارخ بالقانون الدولي. ‏لكننا نعتقد أن هذه الحرب العبثية، التي أودت بحياة آلاف المدنيين، بمن فيهم أطفال أبرياء، قد وصلت الآن إلى نهايتها.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78903" target="_blank">📅 20:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏المراسل: هل ستحاول حضور حفل التوقيع يوم الجمعة؟  ‏ترامب: حسناً، الأمر يعتمد. جيه دي سيتولى الأمر - كان من المفترض أن يتولى هو ذلك في الأصل. ربما سأكون قد رحلت بحلول ذلك الوقت. ‏سنبقى حتى وقت متأخر، لذا قد أشارك، وقد لا أشارك.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78902" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b513c34ac.mp4?token=DvtjaDvV3OTBBY8xYl9uSeoyI7CACY5XuGS4Y_RymRgMX-mbRrR6lyJcWww_rLx0zF3x4sZ-xIg11Py1EDUBgBVuGD2OhpGyQeFALL5ScoWbkRKvMPmoxXJKVbAXTDW-75deJOYLLgHTqcf13PaYtsiCUOfWrC2AzC80KRmKtApJytHJ_fjFW8ZD7B265wnGSv11Bl4K3-WvB9Ojq6954yS_8FQymHxfgVM13yOhhRvcixto-qR5dFmfeZVRQSRnJxL5-kQTUMcQFtGyKJ15uVhR_Kt3eMDNUwiA8Ltmq8iMHNE8TdgL633irsrOclBU5tIq1oSRo8PYnh6lS1jt706lExUnpbTK6Y6AF9kp7_jQbCsGr-HBshLj9zv6JR_aJ4KD8qgaEOhEJFOPen9H2-QCEi0UGGLtcaAXtCP5E7sgHOfcyRZiZURkE5M0XAZzyMkjIeWcKqXRHnxKt0MS5jC9gQVe0rCWgw3mK04IegLUB9XWQt0EFa6Sv9Ei9iBE0fSEgRJ0B6V6Bly3Trn6Hllr4ANwH4MJd3YwX21Q0-dPSb-jP3TPVTKivVrdvXgimyb8GBChzfWMjg-P8wyOmTwngZy2jdvT0zWJR_ZgkpK7Y99tcpYhgM2I5-F5T0r6Okzo23IgA3jqFf5Szql5iQyWdj_WtbFe_SPHKyGLh00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b513c34ac.mp4?token=DvtjaDvV3OTBBY8xYl9uSeoyI7CACY5XuGS4Y_RymRgMX-mbRrR6lyJcWww_rLx0zF3x4sZ-xIg11Py1EDUBgBVuGD2OhpGyQeFALL5ScoWbkRKvMPmoxXJKVbAXTDW-75deJOYLLgHTqcf13PaYtsiCUOfWrC2AzC80KRmKtApJytHJ_fjFW8ZD7B265wnGSv11Bl4K3-WvB9Ojq6954yS_8FQymHxfgVM13yOhhRvcixto-qR5dFmfeZVRQSRnJxL5-kQTUMcQFtGyKJ15uVhR_Kt3eMDNUwiA8Ltmq8iMHNE8TdgL633irsrOclBU5tIq1oSRo8PYnh6lS1jt706lExUnpbTK6Y6AF9kp7_jQbCsGr-HBshLj9zv6JR_aJ4KD8qgaEOhEJFOPen9H2-QCEi0UGGLtcaAXtCP5E7sgHOfcyRZiZURkE5M0XAZzyMkjIeWcKqXRHnxKt0MS5jC9gQVe0rCWgw3mK04IegLUB9XWQt0EFa6Sv9Ei9iBE0fSEgRJ0B6V6Bly3Trn6Hllr4ANwH4MJd3YwX21Q0-dPSb-jP3TPVTKivVrdvXgimyb8GBChzfWMjg-P8wyOmTwngZy2jdvT0zWJR_ZgkpK7Y99tcpYhgM2I5-F5T0r6Okzo23IgA3jqFf5Szql5iQyWdj_WtbFe_SPHKyGLh00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ‏رفع العقوبات عن إيران يرتبط بسلوكها</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78901" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 29-05-2026 جندي من جيش العدو الإسرائيلي في موقع مسغاف عام شماليّ فلسطين المحتلّة بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/78900" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395c3841b8.mp4?token=vRoARWXpAdSYc3F_BhwyRLp1QSO7V4r9S78q3WnZIams6AETVjlO7dM8iUizWadwY436CqjrGAetx2zMPe_CDtDluSUGWcrNB28IQI5grZ1EQSdzQQlKTeWJ7yrqeDWq5U6QQ-MdC4x_iqOGJsvA1dvhLks6UPQBNISGQEF5eeAvFACmBo7maxLELnQAZJbTUYKjoMh13kWSyUNFIARwTfYBsaueY1qlCL1b39pBWefgNBgGWDBYBTeMIVo_Ja4bGn9bq1gb2Ndu2qFwZu2cuIE0J6ph5_SYBumTABR3izhDPZTmKBSBm47ZxfTGgSOBGxbMCN7XUd_9T3Cuf-WR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395c3841b8.mp4?token=vRoARWXpAdSYc3F_BhwyRLp1QSO7V4r9S78q3WnZIams6AETVjlO7dM8iUizWadwY436CqjrGAetx2zMPe_CDtDluSUGWcrNB28IQI5grZ1EQSdzQQlKTeWJ7yrqeDWq5U6QQ-MdC4x_iqOGJsvA1dvhLks6UPQBNISGQEF5eeAvFACmBo7maxLELnQAZJbTUYKjoMh13kWSyUNFIARwTfYBsaueY1qlCL1b39pBWefgNBgGWDBYBTeMIVo_Ja4bGn9bq1gb2Ndu2qFwZu2cuIE0J6ph5_SYBumTABR3izhDPZTmKBSBm47ZxfTGgSOBGxbMCN7XUd_9T3Cuf-WR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سننشر بنود الاتفاق قريبًا جدًا، بعد يوم الجمعة بفترة قصيرة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/78899" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب: سوف يحضر جي دي فانس حفل توقيع الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78898" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامب: أعتقد أن نص اتفاق إيران سيُعلن قريبًا جدًا.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78897" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامب: نريد علاقات طيبة مع إيران وإذا لم يتحقق ذلك فسنعود للحرب وآمل ألا يحدث ذلك</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/78896" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامب: سيتم فتح مضيق هرمز بشكل كامل يوم الجمعة</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78895" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامب: وقعنا مذكرة التفاهم مع إيران وتم فتح مضيق هرمز جزئيا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/78894" target="_blank">📅 19:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامب: وقعنا مذكرة التفاهم مع إيران وتم فتح مضيق هرمز جزئيا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/78893" target="_blank">📅 19:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي لرويترز: قواتنا ستحافظ حاليا على تموضعها بالشرق الأوسط وأي خفض لها سيتم عند توقيع اتفاق نهائي.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/78892" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حزب الله يطلق رشقة صاروخية باتجاه عدد من الآليات الإسرائيلية حاولت التقدم باتجاه بلدة كفرتبنيت</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78891" target="_blank">📅 19:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
رئيس الوزراء الباكستاني:
سنستضيف حفل توقيع الاتفاق بين ايران والولايات المتحدة في جنيف يوم الجمعة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/78890" target="_blank">📅 19:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏مسؤول امريكي لرويترز: مستعدون للنظر في خطوات مع إيران لم نكن لنوافق عليها في الماضي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78889" target="_blank">📅 19:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حزب الله يطلق رشقة صاروخية باتجاه عدد من الآليات الإسرائيلية حاولت التقدم باتجاه بلدة كفرتبنيت</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78888" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مسؤول أمريكي رفيع المستوى: تسمح الاتفاقية بإعادة فتح مضيق هرمز على الفور ورفع الحصار الأمريكي على إيران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/78887" target="_blank">📅 19:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📰
مسؤول أمريكي رفيع المستوى لرويترز: وقع ترامب وفانس مذكرة التفاهم، وقام رئيس البرلمان الإيراني بالمثل.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/78886" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
مسؤول أمريكي رفيع المستوى لرويترز:
وقع ترامب وفانس مذكرة التفاهم، وقام رئيس البرلمان الإيراني بالمثل.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78885" target="_blank">📅 19:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA3MaWt89_DrKq5hevL_xtkmEtNg0qHweqSIyl8mWZZq6Pc0vyJLNbZpuxWBV6MnEkG3ykpEte7HZaQ-hC3V-qpRTQEX-eFNkEWHoS4cxca9tO350wfeUhcqE8QWXlhlmQ1EiaUEuyUldJRhTby-ozdtipC9hkDjPn0YVHNNY4oDI0f1rS8u9CCtP9K2Uvdq-qfHIAE66fdb_Kcc57Kdx4JWcoZgOOTmgCOBluf2Zhu-ZVETu6t-NVcZRRHh77qp-o6ChsY_IWzBUgQtXDZd7X5OnErphsQH91QikowjKlAde1XxeMu3UhIsIi7yj9X_brXk40a30c89nBbCA6v2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
كانوا ينوون قتل هذه الأمة وتدمير هذا البلد والاستسلام، خطت إيران خطوة طويلة نحو النصر النهائي. أرادوا ذلك لكنهم لم يستطيعوا. سنقف، وفي النهاية، ستنتصر إيران، بفضل الله.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78884" target="_blank">📅 19:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اعلام العدو:
وصلنا إلى وضع غير مقبول على الإطلاق أصبح فيه لإيران "حق نقض" على حرية العمل في لبنان وهذا واقع عبثي وغير مقبول.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/78883" target="_blank">📅 19:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الجيش الإسرائيلي يعلن مقتل وإصابة 45 ضابطاً وجندياً على جبهة لبنان، خلال الـ3 أيام الماضية فقط.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78882" target="_blank">📅 18:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مصدر أمني:
الجيش يقلص عملياته في لبنان وينتظر قرار المستوى السياسي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78881" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هجوم بقاذفة ار بي جي على سفينة نفط</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78880" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78879" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78878" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOiYfd_d0Qgd2Bj6BlhyBtfEVcN62qEl8Tiy_MXyp1mc2Csd7m6np_gK7DG53Pn_ToyJl6jvgbNmmAlEJhcKxNXJMbA-azYcxHUFP3PNt-JUkO8E5CGqsk8CPKWEm5byQPevWQIGW8xh-D95LJgXzhY0C13hJqpHv6g14My7om_f95WnAd40dUrxbNNwscZtQAHGrDgtSofIKAm6U22FoZr_YZYxhgVlaoS3AB7Z549yuodh6cX_tF7ztw9skzZpE5_s18NdrVGJ-JXHSbOkpikHbiKdE7-GYjIZQ9yTsC-he8zmhOtIHypHYXfDZ_e1upuiVBSH7ULl2PSrteExcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
متابعة جوية |
أظهرت بيانات موقع Flightradar24 تحليق طائرة الاستطلاع الأمريكية MQ-4C Triton التابعة للبحرية الأمريكية (OVRLD02) في أجواء الخليج الفارسي ، وتُعد الطائرة من أبرز منصات الاستطلاع والمراقبة بعيدة المدى المستخدمة في جمع المعلومات ومراقبة التحركات البحرية والجوية علما ان الطائرة انطلقت من قاعدة موفق السلطي في مملكة البندورة المعروفة بالأردن …</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78877" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لَن نَغِيب عَن المَيدان ...</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78876" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
الجيش الأميركي:
حصار موانئ إيران ما زال ساريا في انتظار استكمال الاتفاق وعلى السفن المتضررة من الحصار عدم السعي للعبور.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78875" target="_blank">📅 17:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
حتى هذه اللحظة، بالمناسبة، لم يكلف رئيس الوزراء نتنياهو نفسه عناء التعليق على الاتفاق أو التحدث إلى مواطني "إسرائيل" في يوم مهم كهذا. لم يصدر حتى بيانًا مكتوبًا قصيرًا. مرت 17 ساعة منذ إعلان ترامب عن التوصل إلى الاتفاق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78874" target="_blank">📅 17:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇾
إشتباكات مسلحة عقبها انفجار في منطقة الإنتفاضة بمحافظة الرقة السورية ؛ وأنباء عن تفجير انتحاري لعنصر من عصابات داعsh الإرهابية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/78873" target="_blank">📅 17:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78872" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78871" target="_blank">📅 17:24 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
