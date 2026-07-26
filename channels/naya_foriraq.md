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
<img src="https://cdn4.telesco.pe/file/T7pE4HvipQpgUUgAIDiCQPp3G3h86igjHkXD9E3muDfCYGMt_k9RNHYXPMGNazlT8FcG41s0TJQWicuvo0e3PmUS6RR9Kv0JCJOXQ7muYpsPDJNdYkeDeX9Pu0xTdPzbc5cMQ3Z8-OrNKKdVcaM9M9LJIPu_g_OwO0K3XcT0gZONsHkqqlg-MeD-skHBpn8KyOBj1iZWtHkmlsKygKiggx4L8Orf6AyPydTqmTAHfqty-zWo_Jzxq1ZVOSj3c22Yjyng_D71E8rVgpH_q43CXhkAq3nPvpvxrDTsYocIfMvHdeeYYBUpJxrS6R5RyCYm5qI4U2JlNdelcYSBmiODbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-85658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتن ياهو: زوجة زهران مامداني وعائلته احتفلوا بمذبحة السابع من أكتوبر.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/85658" target="_blank">📅 18:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1821e338b.mp4?token=vf-TH9XZA72ktalsBrO-E5Cx0u_OebGByqI6KbcVQj-RvwdmiRZcJwhAKUUzR-fgN6TKBDJ36XPPNmL3iFDjIRtE0Rsj1eYlDdw-_Fq53j4EjMG9dFvWENy403nrfFUnpJepIzpjml0qXrqcsUcvlUrXpOLfNXB3bFvB27GGF6Vf1_w9fvOZyTh9fVCZbNcHBsxlO30h-cNu88bTSoDctS86-RbGsFfJ1RNJd6ckL6AGADiTYi8PVJR1uxplZT24Rlzv05obP8_HrVmZ05vg0-T7TJenQAEA1LOwAUUdy57tXSmYS6RBDotCXBcDviWzo2k5YR87EL2yqo5DIjD0e68ZHCWgtVOKMVQxthg0BEYvJvmdJNAh5NKJf8CsrTBdmhYZ78FtNsb37wmyin-vFFy-9jXOJTtMoGgSDZ1Yeq454VjRP_0dl27zollnCNT_BiubtWijEKoPc6kXDiHfMNxjrD0AYIyBLSwq3I5qlgBy85gcWaL4DGhxRORi9Lt8SXXbOSmJ1qeo6DUBysmO3EHo-KLOucm2Vws62q_fJgHS6vk11P-Kt9TGeD7R1r2SiI312d7Eh_nZryKKxbNFLnaEhSJMPDfuoJ2VEnhUJI_34gwZjT5ljyJUWQ0LItD0B6bBEg9hwD3jPcf825W9pjpSeZxuYZtSrU28jeve_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1821e338b.mp4?token=vf-TH9XZA72ktalsBrO-E5Cx0u_OebGByqI6KbcVQj-RvwdmiRZcJwhAKUUzR-fgN6TKBDJ36XPPNmL3iFDjIRtE0Rsj1eYlDdw-_Fq53j4EjMG9dFvWENy403nrfFUnpJepIzpjml0qXrqcsUcvlUrXpOLfNXB3bFvB27GGF6Vf1_w9fvOZyTh9fVCZbNcHBsxlO30h-cNu88bTSoDctS86-RbGsFfJ1RNJd6ckL6AGADiTYi8PVJR1uxplZT24Rlzv05obP8_HrVmZ05vg0-T7TJenQAEA1LOwAUUdy57tXSmYS6RBDotCXBcDviWzo2k5YR87EL2yqo5DIjD0e68ZHCWgtVOKMVQxthg0BEYvJvmdJNAh5NKJf8CsrTBdmhYZ78FtNsb37wmyin-vFFy-9jXOJTtMoGgSDZ1Yeq454VjRP_0dl27zollnCNT_BiubtWijEKoPc6kXDiHfMNxjrD0AYIyBLSwq3I5qlgBy85gcWaL4DGhxRORi9Lt8SXXbOSmJ1qeo6DUBysmO3EHo-KLOucm2Vws62q_fJgHS6vk11P-Kt9TGeD7R1r2SiI312d7Eh_nZryKKxbNFLnaEhSJMPDfuoJ2VEnhUJI_34gwZjT5ljyJUWQ0LItD0B6bBEg9hwD3jPcf825W9pjpSeZxuYZtSrU28jeve_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: زهران مامداني يثير الكراهية. من المفترض أن يكون عمدةً لجميع سكان نيويورك - اليهود والمسلمين والمسيحيين. إنه يحاول أن يثير الفتنة بين مجموعة وأخرى. اليهود الأمريكيون في نيويورك يشعرون بالخوف.</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/85657" target="_blank">📅 18:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نتن ياهو: سآتي إلى نيويورك من أجل الجمعية العامة للأمم المتحدة، ولست قلقا بشأن أي شيء.</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/85656" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96e9c0943.mp4?token=h_w3_fq6abeJIwvPGmZE_NEVrEd0Ob34_Zx4H5HTkcxCC01_reaAHr7IXFX7rnSSL3j52jaBFqSVXgEbVMYY2KYHqRMC34fgjxoKNgkZDMAHrA4PYH73pk4GY-uRpKZzsb7t967wHdO3giA1K-TOXq4zmHR8izERuPoWKGVZ-65JvtSGVZVT46bGKZdgF8so8J6W45jSGBbJNG3E8ouQ37po60uJVddkJTaf2VZJhynNV0yd6rtUL5UX_Ie_f6OBDVh8hy79vJ3u8bWIa6OkunR4i9KBzarOC1vr8XiYY2VJAyuke9PGq5XS_FYqMof0EJeriAhIFhHs0YPwyyeRlC83Vih5vIPvq_p7gYT_kJ57-rccEmw2EUF1IYcUqJUjhzRknksyoChrrvX21RZZomWWBlcQX_zDDtEUnTQ86ZaEKLX6_CzgwmJ091F5i9LZG9wvumW54iY9vK6yYT7AytkvXMU4-HqnzhqkYknVPozOo1B57vTsAEsY0ym4_jbIpsSgOZHPAF_V-vUFp84vEPQsXDTxIK1LBYcVWQON6Sxe2anJPnfONdjzYbzfYS1sdo85b918jiMm7JE5kTCFmbXn3fAe4OpGTuIV3PjIm33rGyJ2OwjNEUpzGmHmkFE9FGJI2Jyn9sSPO-deJmifci-98MmVYIc93iK152QKXk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96e9c0943.mp4?token=h_w3_fq6abeJIwvPGmZE_NEVrEd0Ob34_Zx4H5HTkcxCC01_reaAHr7IXFX7rnSSL3j52jaBFqSVXgEbVMYY2KYHqRMC34fgjxoKNgkZDMAHrA4PYH73pk4GY-uRpKZzsb7t967wHdO3giA1K-TOXq4zmHR8izERuPoWKGVZ-65JvtSGVZVT46bGKZdgF8so8J6W45jSGBbJNG3E8ouQ37po60uJVddkJTaf2VZJhynNV0yd6rtUL5UX_Ie_f6OBDVh8hy79vJ3u8bWIa6OkunR4i9KBzarOC1vr8XiYY2VJAyuke9PGq5XS_FYqMof0EJeriAhIFhHs0YPwyyeRlC83Vih5vIPvq_p7gYT_kJ57-rccEmw2EUF1IYcUqJUjhzRknksyoChrrvX21RZZomWWBlcQX_zDDtEUnTQ86ZaEKLX6_CzgwmJ091F5i9LZG9wvumW54iY9vK6yYT7AytkvXMU4-HqnzhqkYknVPozOo1B57vTsAEsY0ym4_jbIpsSgOZHPAF_V-vUFp84vEPQsXDTxIK1LBYcVWQON6Sxe2anJPnfONdjzYbzfYS1sdo85b918jiMm7JE5kTCFmbXn3fAe4OpGTuIV3PjIm33rGyJ2OwjNEUpzGmHmkFE9FGJI2Jyn9sSPO-deJmifci-98MmVYIc93iK152QKXk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو:
سآتي إلى نيويورك من أجل الجمعية العامة للأمم المتحدة، ولست قلقا بشأن أي شيء.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/85655" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7w4mhbgJaWuFrKzE1ADmpU0DNAdcF3k4jMHEBUhq_XwiwWfue5rhdXW_N3f-_p-DQpugElikuIOfTeT9aj3Ea0qqs-KRBZx0HGjjirLfb2a-9IfrgHX0b-HinbP1Um0oxgkffdHUk5XKJ2hpJ7hlQmgh1XPsJGkSE8xmYA1NW6JRIHlA_tPSWOIDx5Xy5KvXB8IiXlcCvSYDDH6i8211xRyXn8sVoaL5rgBYIvXUnew_xdffTljAoCb7frJrd83pMqFNApyhYKIgYC3nnZL8J7gPvkssC8f8FbSNgGps6Ff0k3M1tYTpZBMzmTxJegOPzPpw1eQPTVr9BMcIbPeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇧🇭
اعلام العدو:
للمرة الأولى منذ السابع من أكتوبر.. المديس ملك البحرين يعلن أنه أجرى اتصالا هاتفيا بالرئيس الإسرائيلي.</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/85654" target="_blank">📅 17:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📰
‏3 مسؤولين لـ CBS:
محادثات إيران وعُمان بشأن مضيق هرمز أحرزت تقدما ملحوظا.</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/85653" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
اعلام العدو:
الكابينت يوافق على إدخال ما يسمى بـ"مجلس السلام" إلى قطاع غزة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85652" target="_blank">📅 17:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مصدر إيراني لرويترز:
نعتقد أن وقف أميركا لهجماتها تكتيكي وليس حقيقيا.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85651" target="_blank">📅 17:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
اعلام خليجي:
إيران أبلغت باكستان رفضها إنشاء ممر جديد في مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85650" target="_blank">📅 16:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
اعلام العدو:
بحسب تقديرات وزارة الحرب الأمريكية، استخدمت الولايات المتحدة أكثر من 1200 صاروخ باتريوت خلال الحرب تبلغ تكلفة كل صاروخ منها أكثر من أربعة ملايين دولار. وحذّر رئيس هيئة الأركان المشتركة، في مناقشات مغلقة، من أن الجيش قادر على استئناف قتال واسع النطاق ضد إيران، لكن مثل هذه الخطوة قد تُقلّص بشكل خطير عدد الصواريخ الاعتراضية المتاحة للقيادة المركزية الأمريكية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85649" target="_blank">📅 16:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">كتبوا بدمائهم آية الخلود، وترجّلوا عن أجيادهم كالفوارس، ليبقى الوطن عزيزاً والراية مرفوعة.
#كتائب_سيد_الشهداء</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85648" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
🤡
رؤية قريبة من نايا   سنشهد توسعًا في الصراع الرمادي، ولا سيما مع دخول أوكرانيا إلى هذا الميدان. ولتفهم ما يجري، لا ينبغي النظر إلى أوكرانيا بمعزل عن غيرها، بل باعتبارها جزءًا من مشروع يهدف إلى تمكين أطراف ثالثة وفتح جبهات جديدة، مع وجود بصمات واضحة للكيان…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85647" target="_blank">📅 15:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏خمس شركات طيران تعلق رحلاتها إلى مطارات إقليم كردستان العراق " بيغاسوس ، تركش اير لاين ، القطرية ، اي جت ، يورو ونغ "</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85646" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npj3hE_fWRJRDO5DGNGRIFpDuBM_WCu2eJ72a4rveNMVKfQyOZQDUu-cPleIQ9tfPRglT21qEtAKbjkA5gsQeTGBt6EIC4O_synRJlPGcMrjJExHBALKi1jyd3aWftECVtDzFZP35pBbm8NEBNZI28aHzP7spVYwgZJeWhpEa5DBMKFfiJE4cS0KscKAvwZK0STSZ_YVGO6wdybXeFB9wsX0CvZ9Q7m7eJH-7jlXse-VIvTS5ysVHFOJ1MbLIfP9o-tzJ9omvFHq8X_v3LM0QMqaAQGjIxMlKhrxBGofl9bUiht2l9pbhJvTeFY14448SdLNClWAq049NUTO4uuwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صورة نشرها مواطن هندي من مدينة جيزان السعودية تظهر تواصل تصاعد اعمدة الدخان من شركة ارامكو
شكرا لاخوننا الهنود الذين يعانون من ظلم واضطهاد النظام السعودي منذ فلم حياة الماعز</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85645" target="_blank">📅 15:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">غدا تفتح بورصة النفط العالمية
نتحدث عن استهداف ثلاثة سفن تجارية ونفطية اثنان باب المندب واحدة في هرمز ؛ ايران تلاعب اعصاب ترامب ؛ النفط قد يلامس ١١٠ عند الافتتاحية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85644" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">التلفزيون الايراني: تم استهداف ناقلة نفط انحرفت عن المسار المحدد من قبل الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85643" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار لغم بسفينة مخالفة</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85642" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85641" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات عنيفة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85640" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85639" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnB5OgmW1-xqsTkldOjH5qCHmCSxvaXvAQOW4f-y-x_jI8EZyHgrg-5LvMRu1XtoTQjzhHlAe3nGSJ59kE8ZMzGtKWBKutB3DuHaM97PW7BgXOK6VV-S3-8sT2vPXpSXmHxLsR52sV_7QEVMmdU2WdgliyDqZTnljKrGYEP5ErBiabXSMjTAWbMB7xb0j_pjg3gXkqgKWVese_ZN61vZ6osQifpqfwK58f_ft0cV-IEE2ywoQ3wbY8LeYhh1EduUejMYW5Fgpc5THVe1M2jC7mkVNLU7ttZsOdL2eg5lBxenMN8IOqyXv30lVShEo_DJevrei4VnpKKr1p51t4n_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا تزال أعمدة كبيرة من الدخان الأسود تتصاعد جنوب مصفاة أرامكو جازان في المملكة العربية السعودية، حيث لا تزال الحرائق مشتعلة بعد هجمات الحوثيين ليلة الجمعة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85638" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📰
فايننشال تايمز:
أبلغت كبرى شركات التأمين البحري الحربي في لويدز لندن الوسطاء أنها ستتوقف عن بيع تغطية الحرب للشحنات المرتبطة بالسعودية في البحر الأحمر بعد هجمات الحوثيين على ناقلتين سعوديتين، ويستعد البعض لإلغاء وثائق التأمين الحالية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85637" target="_blank">📅 14:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85636" target="_blank">📅 14:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85635" target="_blank">📅 14:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85634" target="_blank">📅 14:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇾
زعيم تنظيم جبهة النصرة ابو محمد الجولاني: لا نعتزم القيام بأي تدخل عسكري في لبنان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85633" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇷🇴
‏رومانيا تتهم روسيا مجددا بانتهاك مجالها الجوي وتزعم انها اسقطت مسيرات: من غير المقبول أن تستمر روسيا بانتهاك مجالنا الجوي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85632" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇴
‏رومانيا تتهم روسيا مجددا بانتهاك مجالها الجوي وتزعم انها اسقطت مسيرات: من غير المقبول أن تستمر روسيا بانتهاك مجالنا الجوي</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85631" target="_blank">📅 13:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇾
زعيم تنظيم جبهة النصرة ابو محمد الجولاني: لا نعتزم القيام بأي تدخل عسكري في لبنان.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85630" target="_blank">📅 13:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استهداف سفينة في البحر الاحمر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85629" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeFsVaoZUjOgK0Lj5oSipGrei4UaIMW5c70lx6-L9Y1sYgrdoAscMsQIyuc-Oi_k7Ytzan3PLpFUtDpoJXAFSf1Z13dHIhTgixc3q6mYQ0iVN1m4EUzf3gUR1IRxTaocSl3vKW7sNsncstADKC9aezB67-NEdjdIau5iN32ttqOtwI-Usq5GvJIhfpkOaWuEkCH9Al8BQEBeToNOJ7To8-xJDeF2U6ytvXVV65juoob6AU6MWNoJqpf8RqLnuD3BChlecsUx69NUQF5YgWCCrUq0qTLnxxlx_gnv-8D3WNlgOgxTBB9ONjzaIchq-8QLcWyeuGJdRetS3nE_5Kb-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85628" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85627" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: غالبية الشركات الأجنبية العاملة في المحافظات العراقية (باستثناء إقليم كوردستان) لم تنسحب بالكامل عند بدء الحرب، بل اكتفت بتقليص عدد موظفيها.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85625" target="_blank">📅 10:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c4330a279.mp4?token=GWMsBUdRMn2d-H35tHVDga4nEaYKkN2N_cCsTaih2xgBdC7fKGlu-LwBA3Hb2ohavXMWSY4ozvDuyA9J4MG22ZSpZoc-FTVYWOtPFeaeTBYx7Wig6JsUGlenC-VmXOIr7cdX-MLiIU5Zhsix25L52RbNXw7oIFlqS6yRKW8kjg1-zP4EiGyhVUJeYOIrqXRlmw-8HhoFHLaRsng4Os88xt_0UR9eMA6jXR8MFMiwfMDiF-u8MjrbMQXunuz0nqwsl9uoBhyCwpEu_KCPpLS8slqxE9_kufUmy7yvJ6l01Qj5U-ti3gLy2ftY0O3s10MRiKyqbG3-GLukYDPARzkpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c4330a279.mp4?token=GWMsBUdRMn2d-H35tHVDga4nEaYKkN2N_cCsTaih2xgBdC7fKGlu-LwBA3Hb2ohavXMWSY4ozvDuyA9J4MG22ZSpZoc-FTVYWOtPFeaeTBYx7Wig6JsUGlenC-VmXOIr7cdX-MLiIU5Zhsix25L52RbNXw7oIFlqS6yRKW8kjg1-zP4EiGyhVUJeYOIrqXRlmw-8HhoFHLaRsng4Os88xt_0UR9eMA6jXR8MFMiwfMDiF-u8MjrbMQXunuz0nqwsl9uoBhyCwpEu_KCPpLS8slqxE9_kufUmy7yvJ6l01Qj5U-ti3gLy2ftY0O3s10MRiKyqbG3-GLukYDPARzkpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
قوات الاحتلال الصهيوني تجري مسحاً هندسياً تمهيداً لتفجير منزل أحد الشهداء المقاومين في بلدة تل بنابلس حيث تم قبلها حرق عدة مساجد ومنازل في البلدة نفسها رداً على مقتل ضابط في جيش الاحتلال خلال عملية إطلاق النار قبل يومين.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/85624" target="_blank">📅 09:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: تبادلنا وجهات النظر مع عمان في آليات إدارة مرور السفن بالمضيق بمراعاة حقوق الدولتين الساحليتين</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85623" target="_blank">📅 08:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
يديعوت احرونوت: لم يهاجم الجيش الأمريكي إيران الليلة، للمرة الثانية على التوالي.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/85622" target="_blank">📅 07:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
زلزال بقوة 4.6 درجة ريختر هزّ محافظة كرمان.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/85621" target="_blank">📅 04:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">استنفار امني واسع في جميع احياء العاصمة برلين</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/85620" target="_blank">📅 04:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
الفايننشال تايمز :
شنت السعودية غارات على الحوثيين، بعدما استهدف المتمردون المدعومون من إيران منشآت للطاقة .</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/85619" target="_blank">📅 03:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
نييورك تايمز :
‏في أواخر أبريل،  البنتاغون استخدم أكثر من 1200 صاروخ باتريوت اعتراضي في الحرب، بتكلفة تزيد عن 4 ملايين دولار للصاروخ الواحد، مما أدى إلى انخفاض المخزونات بشكل مثير للقلق، وفقًا لتقديرات داخلية لوزارة الدفاع ومسؤولين في الكونغرس. وقد ازداد الوضع سوءًا منذ ذلك الحين، حسبما أفاد مسؤولون عسكريون هذا الأسبوع.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/85618" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvxp7a7BsCYNmAoC0NVjpeCRLPdEo2WzZI-4hmtjG0I0J_opSvqpOJGVO_2IGiru226P_q-ESUYMFCgEPBNDnK2BFwjG7J2jxRiwPt2Xy_ON7dSyywmk_j4CaopwyDQwCETZil-wU5Crlr1L8lJW5Camy58FCkWN95y3MPZFt7qf1h4SABGGr5lAgNJooIEKi1n9ccaXAoTzxksaJcpkp4qTntHTya1nz7uUSRSZDBr6gBrxBIhx9M_VL1qzlHkHtrgIM7GMUZ6qljldlNyS_JhUyBJkWI5mz30tjZMmu7yOS7-NA_F38_Xkkg6Zj9NR-iqqUhGQDcH8VkYoB3zg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر امني لنايا : لا يوجد اي انفجارات في أربيل شمالي العراق .</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/85617" target="_blank">📅 03:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مصدر امني لنايا : لا يوجد اي انفجارات في أربيل شمالي العراق .</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/85616" target="_blank">📅 02:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc65291a8.mp4?token=NKbW69EiakoaEA7tD0XOPb2YCT6azAlNz_ko07-Aza9lQEkQkw8fuFabcQ2jp8-R6ir1gDc0ngUvUYLpIcTNuY3kszlsEujjLp_Vw-np21YNaQ4L5pzqzffNEFw02SMzsELYuHs_MoYdGFotOrtun4bDqdFTxrsFbqu8UhxFAvEdwXsRFGby9xj7lPkuQxBNIL8T9hYJy7577i5zyeY8-KTQdK5qqVtTkK9RqoZGZL_4aGxx5O5Z16kHIDUYpJiOJHiLuwRloZYGwjSUDzYF-YQkjRZ3d6NVSOk1TSDzxH7gvI8cbn7CF29j_GkxKLVqDGUzdPsq7mOePMMuznEttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc65291a8.mp4?token=NKbW69EiakoaEA7tD0XOPb2YCT6azAlNz_ko07-Aza9lQEkQkw8fuFabcQ2jp8-R6ir1gDc0ngUvUYLpIcTNuY3kszlsEujjLp_Vw-np21YNaQ4L5pzqzffNEFw02SMzsELYuHs_MoYdGFotOrtun4bDqdFTxrsFbqu8UhxFAvEdwXsRFGby9xj7lPkuQxBNIL8T9hYJy7577i5zyeY8-KTQdK5qqVtTkK9RqoZGZL_4aGxx5O5Z16kHIDUYpJiOJHiLuwRloZYGwjSUDzYF-YQkjRZ3d6NVSOk1TSDzxH7gvI8cbn7CF29j_GkxKLVqDGUzdPsq7mOePMMuznEttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إندلاع حريق في شارع المتنبي بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/85615" target="_blank">📅 02:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/85614" target="_blank">📅 02:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLDNVqUwPB_tfN-FTNagtXb0nlfGfbGIp9qqdz8ooB_Znrd2eJf9HnhWOs_JUBemXaiNg3hL4wi-qfIvQnzm2un6jSHnKDRbRGLhSyYHmy65Xt4GjbushRLopg7ge636aChYDMeZ0dSvF55PtszOb9jSI9_YtDWWSzo0Lzux4eNiJblgGhXlxT_WSbtrCTt_rfzYMScBanEYEZBnQ7L2veTjyrONAH1WIfzTmE4cyhbaqz4nm7N-7ZopkBZY9pAom7poD9d_F16bAqJujLVy0Jq0GFH5_E2fKxi-mW_vchqPhBQDZ2SVtF-o-YprwBtiJULofx2hQO2FPeOw7FGnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/85613" target="_blank">📅 02:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نيويورك تايمز: ترامب قد ألغى خطط تصعيد الحرب مع إيران بسبب مخاوف من أن الهجمات الإيرانية قد تؤدي إلى تقليص مخزونات صواريخ الدفاع الجوي بشكل خطير.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85612" target="_blank">📅 02:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حدث امني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85611" target="_blank">📅 02:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85610">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حدث امني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85610" target="_blank">📅 02:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85609">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نيويورك تايمز:
ترامب قد ألغى خطط تصعيد الحرب مع إيران بسبب مخاوف من أن الهجمات الإيرانية قد تؤدي إلى تقليص مخزونات صواريخ الدفاع الجوي بشكل خطير.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/85609" target="_blank">📅 01:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇱
إعلام العدو:
بلاغ أولي عن عملية طعن على حاجز قلنديا.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85608" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تقول إنها ترحب بإعلان فنزويلا عن انسحابها من المحكمة الجنائية الدولية، وتدعو إلى "تفكيك" المحكمة لأنها "ليست موثوقة أو مستقلة أو شرعية"، وتطلب من جميع أعضاء المحكمة "الانسحاب من النظام الأساسي الروماني".</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/85607" target="_blank">📅 01:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصدر امني لنايا
توجيه من قبل الزيدي ؛  أعفاء كافة القادة والامرين والمدراء العاميين في وزارتي الداخلية والدفاع الذي باشروا بمهام مناصبهم من تاريخ 2023/1/1 والذي تجاوز المدة القانونية للمنصب ثلاث سنوات. .</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/85606" target="_blank">📅 01:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🔻
🇦🇪
شاهد عيان جندي كويتي يتحدث عن عواقب الصواريخ الإيرانية ويؤكد ان الصواريخ الإيرانية تسقط دون وجود اي دور للدفاعات الجوية الأمريكية في صدها</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/85605" target="_blank">📅 01:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afbbaafca9.mp4?token=eJVXpmfwvUNdafXat4tW9GZH4LifqOmF29fCh74sKoz_7SCGtn78szN2QhAYG-tSprTmCcJapPEK_brshf-8KKDaaaWie3AMdUIFmgykeVXlhelPev5t3_0IjppbsZCHX-UanYPCK0gheEky6wFI2Z5Ygdup8He1SEZHonWSQC2KcJk72Y6uo-fJnk5dTsV9c-c4aqBBN5WHy1u-5Ym4DRTPUgWWu_bv1ZBJ0-RoWOZgP5GHzHkN5b_4AyYyEcrqqzXQjBkRV4UATeV56LOKAC6jH-WJ9AksUCgIUPhiJ5ZiuTWL62Lu-c0BfZMfnyinkjJeUx3DHKZXXNotwKjUNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afbbaafca9.mp4?token=eJVXpmfwvUNdafXat4tW9GZH4LifqOmF29fCh74sKoz_7SCGtn78szN2QhAYG-tSprTmCcJapPEK_brshf-8KKDaaaWie3AMdUIFmgykeVXlhelPev5t3_0IjppbsZCHX-UanYPCK0gheEky6wFI2Z5Ygdup8He1SEZHonWSQC2KcJk72Y6uo-fJnk5dTsV9c-c4aqBBN5WHy1u-5Ym4DRTPUgWWu_bv1ZBJ0-RoWOZgP5GHzHkN5b_4AyYyEcrqqzXQjBkRV4UATeV56LOKAC6jH-WJ9AksUCgIUPhiJ5ZiuTWL62Lu-c0BfZMfnyinkjJeUx3DHKZXXNotwKjUNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تصدح حناجر زوار أمير المؤمنين علي بن أبي طالب (عليه السلام) في محافظة النجف الأشرف العراقية بصيحات
الموت لأمريكا والموت لإسرائيل
.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85604" target="_blank">📅 01:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85601">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515003979a.mp4?token=tdmOf662zndaKCWU8Cng0bqKkhnUMCRJmismZxh-TR-0BHqJ7rNmYbIUwHUDWqfhXLXnqVs6Qk8lXVn2Bds-yXovdmLygOB_sLJWTQHrCKbTAOLsK1D__tBhQCW-mXMcsi2YR-5uCwiqRBjDUCTZOyJppGJiAUewqnp1Jgb_JeqaXK79OnXQbc0cTNYOpK9zcezaJxg51VojHNgxYJ4hSiLurVNaObp_3cgueW2YvO5LVFnM6lwd2MBeGp65vkcZsUBhA6rXnEj0PjbhS3B2Mto5sT-nmYFoBu0_YXfBDK2VQZtL8HQmD1AZIpOEY26QQCjIH0nSuyfHpap-IdvTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515003979a.mp4?token=tdmOf662zndaKCWU8Cng0bqKkhnUMCRJmismZxh-TR-0BHqJ7rNmYbIUwHUDWqfhXLXnqVs6Qk8lXVn2Bds-yXovdmLygOB_sLJWTQHrCKbTAOLsK1D__tBhQCW-mXMcsi2YR-5uCwiqRBjDUCTZOyJppGJiAUewqnp1Jgb_JeqaXK79OnXQbc0cTNYOpK9zcezaJxg51VojHNgxYJ4hSiLurVNaObp_3cgueW2YvO5LVFnM6lwd2MBeGp65vkcZsUBhA6rXnEj0PjbhS3B2Mto5sT-nmYFoBu0_YXfBDK2VQZtL8HQmD1AZIpOEY26QQCjIH0nSuyfHpap-IdvTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع معارك بين القوات اليمنية والعصابات التابعة للسعودية في محافظة الجوف شمالي اليمن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85601" target="_blank">📅 01:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85600">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
🇺🇸
🇮🇷
ترامب: سنستأنف الحرب بشكل واسع النطاق على إيران اذا لم نحصل على 100% مما نريد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85600" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85599">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0521e55d96.mp4?token=ufagNs5sUSbHk86PA8rg0zQBtsODesim4qNzrlqm6IlufLCJPtCypErWiMmHNrusfPngepLaHbxqmlY9y6Lvc-3Z84hjNaiQxoSNu1iWY_4jV8K6k-VYdW6LdtE0TlLOmjVzNrIbt9NIibh6M9k-1-U_Hhad5GM61BxswXzcB-tJmVlV4bl2IiMt8TIC4fzOLiTwBYUPM-sX7ywHkt1Yb6YEue73s9TtAV3c_RkOI_duoRgHLrGmWcpJd8LSqG3RtuQXwIos26E9DhYXsmGZf-6HGkqly2Yv59Oyl0dyZbsECr-hktNo0a7V7D2cMK7Fm6cmfqAEoDK4C911ykZYXZIw6WJtWjj5zt3uq4jRIKWoxhazHT_8ZLdHJ7CYORI2a0erKDeU7Oxm9FEf1sXiBshkFPpMwzwNhrCiIZF3SjxZyRW9ivOkNuxd6mjIjZvkJzAH8ac0BZPfCS2vZXE-DnSrmSpwJf0Q4yNLJBbaX7ebqm5VLtgbPf3lZnz7lK8uNuX9o-nEuPrO4EOlFp4oudgjYC0QJbRQ1HO3bOIKfo6riOgZBBdnmemb65IbeSLMkr9x7EiORBFEWmmdtATSJlYi8zFJ9aYHztLkzurmXhcSby_vs5hLsfBEkvM5H2sVPA0D8b44Zglamz65MnoiDKculUCKQd9BiB4p2she6zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0521e55d96.mp4?token=ufagNs5sUSbHk86PA8rg0zQBtsODesim4qNzrlqm6IlufLCJPtCypErWiMmHNrusfPngepLaHbxqmlY9y6Lvc-3Z84hjNaiQxoSNu1iWY_4jV8K6k-VYdW6LdtE0TlLOmjVzNrIbt9NIibh6M9k-1-U_Hhad5GM61BxswXzcB-tJmVlV4bl2IiMt8TIC4fzOLiTwBYUPM-sX7ywHkt1Yb6YEue73s9TtAV3c_RkOI_duoRgHLrGmWcpJd8LSqG3RtuQXwIos26E9DhYXsmGZf-6HGkqly2Yv59Oyl0dyZbsECr-hktNo0a7V7D2cMK7Fm6cmfqAEoDK4C911ykZYXZIw6WJtWjj5zt3uq4jRIKWoxhazHT_8ZLdHJ7CYORI2a0erKDeU7Oxm9FEf1sXiBshkFPpMwzwNhrCiIZF3SjxZyRW9ivOkNuxd6mjIjZvkJzAH8ac0BZPfCS2vZXE-DnSrmSpwJf0Q4yNLJBbaX7ebqm5VLtgbPf3lZnz7lK8uNuX9o-nEuPrO4EOlFp4oudgjYC0QJbRQ1HO3bOIKfo6riOgZBBdnmemb65IbeSLMkr9x7EiORBFEWmmdtATSJlYi8zFJ9aYHztLkzurmXhcSby_vs5hLsfBEkvM5H2sVPA0D8b44Zglamz65MnoiDKculUCKQd9BiB4p2she6zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
قيادة العمليات الوسطى الأمريكية :
لا يزال الحصار البحري الأمريكي المفروض على إيران ساري المفعول بالكامل. وحتى 25 يوليو/تموز، قامت القيادة المركزية الأمريكية (CENTCOM) بتحويل مسار 12 سفينة تجارية حاولت اختراق الحصار، وتعطيل سفينتين لم تمتثلا، وتفتيش سفينتين أخريين لضمان الامتثال التام.
‏في وقت سابق من اليوم، أكملت القوات الأمريكية عملية التحقق والتفتيش على متن ناقلة النفط "شارمينار" التي ترفع علم جزر القمر في بحر العرب، وتواصل الناقلة الآن رحلتها.
‏قامت قوات القيادة المركزية الأمريكية بتعطيل ناقلة النفط "لافين" التي ترفع علم موزمبيق في خليج عُمان، في 24 يوليو/تموز، بعد أن حاول طاقمها انتهاك الحصار عدة مرات وتجاهل التحذيرات المتكررة. ولم تعد السفينة متجهة إلى إيران.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/85599" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85598">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9643bf0188.mp4?token=cMdlyeNcO6470d0jYOktfhUqRg-hIoGK2Yy5eOdUd5_dhV_MHU9zD1kU9DW5NRmIl-S8xom_EdSKk6fxDJ0vsB52ilxaa4R2u_2NUdOqfjHx5dTsRbpv2x-jB1HjTwM6Y-3xt_2rNJJoZv1-2Wz_7JASQqtt90IzyPmub7dLL4tc-vqmj8dyWUGAquKJMhdYTU4uqjUEm2PBzppwk-1HGQWDIQVKgSd_M-ReoqLs45S-FbyYzrfQU8T-qtUcnNYD622tQfqBFZAQ2Z4s5fIaYCJCqbAsHwlqHXLLdIFUgABoF_SOvGA6TkIHbafQLdnGKzhTsV1Ihf0XVU6y5MbnOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9643bf0188.mp4?token=cMdlyeNcO6470d0jYOktfhUqRg-hIoGK2Yy5eOdUd5_dhV_MHU9zD1kU9DW5NRmIl-S8xom_EdSKk6fxDJ0vsB52ilxaa4R2u_2NUdOqfjHx5dTsRbpv2x-jB1HjTwM6Y-3xt_2rNJJoZv1-2Wz_7JASQqtt90IzyPmub7dLL4tc-vqmj8dyWUGAquKJMhdYTU4uqjUEm2PBzppwk-1HGQWDIQVKgSd_M-ReoqLs45S-FbyYzrfQU8T-qtUcnNYD622tQfqBFZAQ2Z4s5fIaYCJCqbAsHwlqHXLLdIFUgABoF_SOvGA6TkIHbafQLdnGKzhTsV1Ihf0XVU6y5MbnOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استنفار واسع لعجلات الاطفاء في محاولة لاخماد الحرائق في الحقل النفطي.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/85598" target="_blank">📅 00:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عملية دهس داخل الكيان الصهيوني</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/85597" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عملية دهس داخل الكيان الصهيوني</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/85596" target="_blank">📅 00:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44111e1596.mp4?token=irluB_uE-N61K8hFCtEaewXHP351aiADZvhj78uqbGdWkEZ2f4LwQvJDSFVSq9QRc_W-PB0HcoUD_dLOFrrjoHEhm3EpxKHDIeyr6lkznBsoeL-o0dr4icaZbPhix3LO4H7CYdNZfFjahfDfyJkDjr0srrkOknlpIZS-fkZd6XggSUNPP9x_VS7Dd7Qm93-OGXlTNaHNK_O3XEQXE80oxu2PXksIIr6u4-J8BYpyJvZgs9V6TMdYgP-ZylOi3dYTNCRWXNN5_msxU43Z8ZgjrmQd8JG7gxDYNjyl82c298YO0UWm203G3Uh76DOmeqTdMf-e6QssqLARAmkbbalBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44111e1596.mp4?token=irluB_uE-N61K8hFCtEaewXHP351aiADZvhj78uqbGdWkEZ2f4LwQvJDSFVSq9QRc_W-PB0HcoUD_dLOFrrjoHEhm3EpxKHDIeyr6lkznBsoeL-o0dr4icaZbPhix3LO4H7CYdNZfFjahfDfyJkDjr0srrkOknlpIZS-fkZd6XggSUNPP9x_VS7Dd7Qm93-OGXlTNaHNK_O3XEQXE80oxu2PXksIIr6u4-J8BYpyJvZgs9V6TMdYgP-ZylOi3dYTNCRWXNN5_msxU43Z8ZgjrmQd8JG7gxDYNjyl82c298YO0UWm203G3Uh76DOmeqTdMf-e6QssqLARAmkbbalBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلان حالة الطوارى في المانيا برلين نتيجة عملية دهس وجرحى بالعشرات كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/85595" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اشتباكات عنيفة في العاصمة الألمانية برلين , سقوط عدد من الجرحى كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/85594" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568a7d842.mp4?token=jPDGBdI7venzNEuwajzDQJJ0XSTKBRbbaFieTodmeeV2tRXYeKMudM8eKCE7EcS_SV-XoFYGCsw_w4y48Esy5P-c1FGQBG3u63RakygZed-sh-sRaK8ZoLOy4c3geI2CQMjW0OW0f59UC4pw3YUI5mR62s0yGr93cT1URXC49JtatR8cfkrz5adHDVcJJTQPKkWYCWobZ0Mr2psfOZjHdyVaxeQ_U1LmGQqhjQLlCuBqjaUfahaz_aXO_pnZI-xGBU9IyEA4x8tzagUIgLe_L8RxupwaxC8ZDdeuC2EopeNPTj0qUSK16D5uJQvRj6UZZ7u0mURTrkhYbaXMKPZJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568a7d842.mp4?token=jPDGBdI7venzNEuwajzDQJJ0XSTKBRbbaFieTodmeeV2tRXYeKMudM8eKCE7EcS_SV-XoFYGCsw_w4y48Esy5P-c1FGQBG3u63RakygZed-sh-sRaK8ZoLOy4c3geI2CQMjW0OW0f59UC4pw3YUI5mR62s0yGr93cT1URXC49JtatR8cfkrz5adHDVcJJTQPKkWYCWobZ0Mr2psfOZjHdyVaxeQ_U1LmGQqhjQLlCuBqjaUfahaz_aXO_pnZI-xGBU9IyEA4x8tzagUIgLe_L8RxupwaxC8ZDdeuC2EopeNPTj0qUSK16D5uJQvRj6UZZ7u0mURTrkhYbaXMKPZJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حرائق هائلة تطال حقل جمبور وسط انفجارات عنيفة مستمرة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/85593" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اشتباكات عنيفة في العاصمة الألمانية برلين , سقوط عدد من الجرحى كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/85592" target="_blank">📅 00:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cffa98cdf.mp4?token=D4_0QV_8YUTwztunuMTUIg5Nedaj7fx-PgwbcFrPm3hEb9U0gZheXshY-ODk1EGw6pyKFsl-UVWlAZq26f_GrGbhsvSgAoK-YGdM2IY0bbyHw0_WclMnQHDR37lMmLjoOTsD6kMiz-yySVT01FMAOh9KgoVeI8DPO4_w-mZPDpHYQDOAiFNKQtKaTNsUT1dmeLndfr_Gh7dx9xp9rnqT3r5B2akjocq_qHrQbdWdPRgAvQjqasLwFiJWNiV1_m_2-KKGpbvksPsesbC93lujaFXzkw6DB4xSFeMHHyp64SUobtqB13EAy_3gYTQewXgMvjnkm1j7j8elGhZKlsw5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cffa98cdf.mp4?token=D4_0QV_8YUTwztunuMTUIg5Nedaj7fx-PgwbcFrPm3hEb9U0gZheXshY-ODk1EGw6pyKFsl-UVWlAZq26f_GrGbhsvSgAoK-YGdM2IY0bbyHw0_WclMnQHDR37lMmLjoOTsD6kMiz-yySVT01FMAOh9KgoVeI8DPO4_w-mZPDpHYQDOAiFNKQtKaTNsUT1dmeLndfr_Gh7dx9xp9rnqT3r5B2akjocq_qHrQbdWdPRgAvQjqasLwFiJWNiV1_m_2-KKGpbvksPsesbC93lujaFXzkw6DB4xSFeMHHyp64SUobtqB13EAy_3gYTQewXgMvjnkm1j7j8elGhZKlsw5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في تقاطع قادر كرم</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85591" target="_blank">📅 00:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85590">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
انفجار كبير قي حقل جمبور بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85590" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85589">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
انفجار كبير قي حقل جمبور بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/85589" target="_blank">📅 00:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85588">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
انفجار كبير قي حقل جمبور بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85588" target="_blank">📅 00:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85587">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
للمرة الما نعرف شكد
...
🇮🇶
🇺🇸
سفارة الاحتلال الاميركي في محافظة اربيل شمالي العراق تصدر تحذير امني شديد نتيجة الضربات الايرانية الاخيرة.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/85587" target="_blank">📅 23:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85586">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr0xA9AIufyL8ZM8gDLOHYgNXU8wpvjJ3Gb91xIIhQapquWc2gVKMrS7R9Yu3jBYAkxmtpA4ZhUPugxHy5Dy7W2fD88HRqQzCZ9LvArhUnQzG392mkyDGTS86pOmkUtQzJmN-J8W6V62252gvx1VYL9xeuYCN0DtLevE1CfIDog9igI8qAPwi7iB3OC-22mfsKZnZaljLzaM8k4ZIhvd0OGTtDrL0jqhAjhKtdnYIxU5golaHu_oYYJ9s6Mz5sBZVm3556cu72uE5_6Jw8IeghDPpd2dcnXk7OyhJN8_uslQ8Dd2tGEOK9bOhuoh_am3_kqNScrlkeCBEir7qotR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراكرز
:
‏بناءً على طلب المخاوف الأمنية الأمريكية، فرضت وكالة الفضاء الأوروبية تأخيرًا لمدة 24 ساعة في نشر صور الأقمار الصناعية كوبرنيكوس سينتينل (1 و2) التي تغطي خط الحصار البحري الأمريكي الذي يعبر الحافة الشرقية لخليج عمان.
‏في الوقت نفسه، يتمتع الإيرانيون بإمكانية الوصول إلى صور عالية الدقة حديثة التقطها الروس.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/85586" target="_blank">📅 23:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85585">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
المتحدث باسم الحرس الثوري الإيراني:    أي دولة، سواء كانت إنجلترا أو دول الخليج أو غيرها، إذا دعمت أمريكا في الحرب، ستكون هدفنا المشروع.  استخدمت طائرات B1 الأمريكية مؤخراً مطارات بريطانية. إذا حذت حذوها، فستكون هدفنا النهائي والمشروع.  لدينا سيناريو خاص…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/85585" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85584">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
المتحدث باسم الحرس الثوري الإيراني:
أي دولة، سواء كانت إنجلترا أو دول الخليج أو غيرها، إذا دعمت أمريكا في الحرب، ستكون هدفنا المشروع.
استخدمت طائرات B1 الأمريكية مؤخراً مطارات بريطانية. إذا حذت حذوها، فستكون هدفنا النهائي والمشروع.
لدينا سيناريو خاص بنا لكل مشكلة.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/85584" target="_blank">📅 23:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85583">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يقرر تعطيل الدوام الرسمي يومي الاثنين والثلاثاء الموافقين 3-4 آب 2026 بمناسبة إحياء أربعينية الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/85583" target="_blank">📅 23:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85582">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094db86814.mp4?token=m8rqw_iPRufgRqtWfceWdlSXLW8S-iF1lb9ZSlmX5HqStlePRRhJwSJucJo88dhWl69L-bayOgQSfgSeITmLZM1eABf4kKm5twiRAsTCaVzSaapD_umX9c04wWbs3j1WJkX0UdgR0FQtIGsl5b-Nd6OTI2pGEseXS_d-KFVcg0j8gPT5SiL5LUMyJYV6Rk-TS_fJLJZror_xhXbh_woGXl5wktTjNkS4b-oSls11V0ti8GcA1utjPgA9LwDfhbxpMAZPykVpNVRxJcRqXlaiZQ4hgNcCkiyYyaySEBdREOWI_gdZiOYjbO4KklksB6KNWg2eoV4SgzxElqJWBhnqQSANuh0HLVoTMaAP97ppZwCOMJZy29Oks9x1a0KuGv9IMaN84I_4ap0k1T9SJIMQnMcQtRG5MxZoeOdP7P6q5oYUNVjv1Fs5EyZpPLyhGCOBQxzvJL9oUR-_udIrVvgW9EpAypzISWMkeJ_fYC76FqS4UtWGl6uJ_nlbCoG-oiUrZLpz0rnQJLXURYFHV31MF29WhiciQTfZkKC7jMCr1dcSHbKQBL02vmZjIDx5Ro9qEYlHihVYfYfqmOAV12M_Y2uOemvaRg6bxBOXGXySZjbYIapy4FPbm1Bu-uwY-XgN_rNocHLzzZihVgMYZx_AjYvXrkDSZ_ZIab4glhXqvNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094db86814.mp4?token=m8rqw_iPRufgRqtWfceWdlSXLW8S-iF1lb9ZSlmX5HqStlePRRhJwSJucJo88dhWl69L-bayOgQSfgSeITmLZM1eABf4kKm5twiRAsTCaVzSaapD_umX9c04wWbs3j1WJkX0UdgR0FQtIGsl5b-Nd6OTI2pGEseXS_d-KFVcg0j8gPT5SiL5LUMyJYV6Rk-TS_fJLJZror_xhXbh_woGXl5wktTjNkS4b-oSls11V0ti8GcA1utjPgA9LwDfhbxpMAZPykVpNVRxJcRqXlaiZQ4hgNcCkiyYyaySEBdREOWI_gdZiOYjbO4KklksB6KNWg2eoV4SgzxElqJWBhnqQSANuh0HLVoTMaAP97ppZwCOMJZy29Oks9x1a0KuGv9IMaN84I_4ap0k1T9SJIMQnMcQtRG5MxZoeOdP7P6q5oYUNVjv1Fs5EyZpPLyhGCOBQxzvJL9oUR-_udIrVvgW9EpAypzISWMkeJ_fYC76FqS4UtWGl6uJ_nlbCoG-oiUrZLpz0rnQJLXURYFHV31MF29WhiciQTfZkKC7jMCr1dcSHbKQBL02vmZjIDx5Ro9qEYlHihVYfYfqmOAV12M_Y2uOemvaRg6bxBOXGXySZjbYIapy4FPbm1Bu-uwY-XgN_rNocHLzzZihVgMYZx_AjYvXrkDSZ_ZIab4glhXqvNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
طائرة “
شاهد
” المسيّرة إلى جانب صاروخ “
ذو الفقار
” في ساحة آزادي بطهران.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/85582" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85581">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFt89NFi6CcSYI-bsawqXXf9ecZbz9ktsf950efFD9s_5qfAriE7RPETS4cJ0d_TPxi2DKVACSNMqfq91KT6tueVE5-dYEd3X2fn8gxKH1h-qvAtrXUFii41cJxMEOSCiVbbJ4RjRi2ykkQOmO8jz2XUOhmB1B403Kmfbn_Ll6N0B0vgh4GjnfLBWbQYMuvCQGybtKD8Fvqoj6ZMHUmJVm0HfeDtKsHYRNTSYblVCzq2YDdcHIlB8_8m85s-77ga_JQBfnU8vgBFHQOGUfzdo4BOoeeEN9rdmrS_zhJCXdBXnwZfLJfm9eZoUSac9QoOuxc9_ys5LGWSKn8DyjMl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🔻
🇨🇳
توقف الشحن البحري بين الصين والسعودية نتيجة ضربات أنصار الله في اليمن على باب المندب</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/85581" target="_blank">📅 23:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85580">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔥
آق مجید نقطه زن
یه موشک اوکراین بزن
بزن که خوب می‌زنی
🚀</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85580" target="_blank">📅 22:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690a9e602a.mp4?token=eKqyV8oFWw6mNRX283abTM8gGLDIZ96WRV18jddnJXo2wxHGD02WF2l9573IF4UBnCXj505ar1jc-FugshpX-SPrzF3lSeLTbfq9r7LhVwD6YwHAJIdqwZXavJH9kVtakFjIGDsB8NkJ-s8WZpRlwszE3bD4tW1-sn8ad0rNydshmXxUzhksTCfTAvVRp-63t-tqdfDPQEyCCbVKjQo-zaUykgSLc7u2RBhYwzLVyMkienP6o_cUS2vyam9eFo2yzRslMEbPsLqT-ZIkJt7dwhDvts76s-hsbRXmr0nFcJHmENRQeFdCWXEMxO2jlIxmpdp04vgFnsgQwp6G-aOZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690a9e602a.mp4?token=eKqyV8oFWw6mNRX283abTM8gGLDIZ96WRV18jddnJXo2wxHGD02WF2l9573IF4UBnCXj505ar1jc-FugshpX-SPrzF3lSeLTbfq9r7LhVwD6YwHAJIdqwZXavJH9kVtakFjIGDsB8NkJ-s8WZpRlwszE3bD4tW1-sn8ad0rNydshmXxUzhksTCfTAvVRp-63t-tqdfDPQEyCCbVKjQo-zaUykgSLc7u2RBhYwzLVyMkienP6o_cUS2vyam9eFo2yzRslMEbPsLqT-ZIkJt7dwhDvts76s-hsbRXmr0nFcJHmENRQeFdCWXEMxO2jlIxmpdp04vgFnsgQwp6G-aOZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوف يتم تعليق صور الشهداء بأمر من العتبات المقدسة .. في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/85578" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJe6bDdUuaIwDu1igvJz7fIOtjLS95XktZ2a5YX9C-W-QRhiEOwf5KGDb3NvHvml3g8RJRmOKSh-e5J2LIFZUg6xgkex5FvrfWxvPltl9QvpYopcJpF996eSmY4JO8awHgI8XYUPm-UlWtjXBzTcGCFy5o7LrPx4moLjK_fDPwPyULIeaNFJqLnGE9ylHmECV9AgfPc3ZcAs5rIPrK1swiJ9Twu3_3jNuNQrp9gZnceF4JjCl0yAhSJN8zCRnFrTHFd3jfg6L6Vhd9Y4wZeQf0FCmYSCRo4AHx2rorTM7rE893UVKD8Hos6KUGBzIOEcRZx8qbxHuWT5D5PAtUOCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/85577" target="_blank">📅 22:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOdBoCGLJYxL1UFUQxHA4BO0TDXZMth__51YMPoovazHoLlnOHVhpVg5UQZ5QCzW7X1qnGLGn5n5JyMjya-WHW4skzTjH_fdr0RGyh02LqQfLSFtfhddQmwP-Qg85_Wy5tRGlxgGIFc9KO2Yivn0lyRoULmCx8GEIe3u4R-ZJ9sxXlZbkrBRB_d-ptRonpVwxe3D4CYvpVPpqH4siIENOwMsXPbNCFuBeP-aLN5ibveDUMQWxnBW6EYLQ22FZy_k2Mkt23hr-l_fHt4a-yUKFNtys2Nz0jJUAPb4_RcmLsCtdCBS2Z5LzsW8sy9iXukGdjB7RuvdL5eG69eWPj4tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇱🇧
🇸🇾
🇾🇪
🔻
نحن أمة الإمام الحسين
ما ملت امام حسينيم</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/85576" target="_blank">📅 22:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Ggg17taxM5iLYB9y6ZqEXcSD2dKqVvZEjrYiazUysmL7WGLs8Mb6ToB5FPNZ1KbmoRn95GPapMV5GRuuys-bUs81zMirWbgvyXdBMM1fUqxEG5ebCwwfXXBzE2-u7RM0EbVqPgZkCoiBkrL4GMEDQ0m2i3XY8CBsvSJq9xX55Rv5cFiZZNyC-UwJypLXi8sjF2U2SHqRkZeX82ekQMv4T3LDkYz4X-OkFBl7BKQK3-1FuU60JYcWQooE_cpeHQ0iibx_TbW4ERDa6CeHUsq3EG5x1LJTbuXHPKJ-FZYo3Wq9-RNlImKtt60ByV0JJw7VPBImyPDipzqcIiWkERtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوف يتم تعليق صور الشهداء بأمر من العتبات المقدسة .. في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/85575" target="_blank">📅 22:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/85574" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cc3dbd29.mp4?token=lhDWCtgISJU8mF7U-PAGXhS14-MqKUxVAf80iN6g7REJbRW7LmAjXawzb_P_6A4num_rZAyimMnHXNCJ_l5S8iqZ_bme8VLk8_n-Tud-TcIioiGCinzS7ViHKPsjAyoA3iNqPdF37SrzyMhhxnpSe39kEi4l1nHURSOvnxfsK4xdxVLAg3qqpZREd-yWauu4KAOzqVjKcNj6s_47CYGAIQULkoviKgcX0ylI_fNQ_FObukiHlLEVo1Z1L_s8obMDFffrf1o3cE0avVcdteUxWNYVPPhld9E6oRFtzI0jQ9GftIWfJx14kY6ct54w6Gm_Yz73eMOtSN0Be37SA8nvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cc3dbd29.mp4?token=lhDWCtgISJU8mF7U-PAGXhS14-MqKUxVAf80iN6g7REJbRW7LmAjXawzb_P_6A4num_rZAyimMnHXNCJ_l5S8iqZ_bme8VLk8_n-Tud-TcIioiGCinzS7ViHKPsjAyoA3iNqPdF37SrzyMhhxnpSe39kEi4l1nHURSOvnxfsK4xdxVLAg3qqpZREd-yWauu4KAOzqVjKcNj6s_47CYGAIQULkoviKgcX0ylI_fNQ_FObukiHlLEVo1Z1L_s8obMDFffrf1o3cE0avVcdteUxWNYVPPhld9E6oRFtzI0jQ9GftIWfJx14kY6ct54w6Gm_Yz73eMOtSN0Be37SA8nvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد خاصة لنايا توثق لحظة اطلاق الكويت رشقة صاروخية نحو اراضي الايرانية</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/85573" target="_blank">📅 21:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
‏
سفيرة الكويت في واشنطن
: ادعاءات WSJ بشأن مشاركة الكويت في العمليات ضد إيران باطلة.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85572" target="_blank">📅 21:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012b1c9a7c.mp4?token=K4tCuIOICdwG7ohC7XqOo_PiAVFSmFtIT4qImeT4mSf-6xrbNkZhkCK0kqZfFdgb7ntLyViAIzpHsnFraNudEJQLc-b7xjgmzokYzZteCkowUwRhOPT2O-y9LkyLHbaqlAQTnp3IoGw2JE-XX7eBUBMzG7qzdI-hMbpV7P1bBGLxT1p0SB5DwHxx1gfVtcPwLwQFbNqYXr31E-Bj-eLO0SrS1nXsH_kw5r4qyOOtD5JQ08PxOG9gMR3QpCVzMAz-eAqXIHbukCiPjMjwrtf06PltUljXwD1jn55UTrK57_uDg56D3Yq_c2uv8lIzRVvhERoXQEu97cNkHpks8wsTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012b1c9a7c.mp4?token=K4tCuIOICdwG7ohC7XqOo_PiAVFSmFtIT4qImeT4mSf-6xrbNkZhkCK0kqZfFdgb7ntLyViAIzpHsnFraNudEJQLc-b7xjgmzokYzZteCkowUwRhOPT2O-y9LkyLHbaqlAQTnp3IoGw2JE-XX7eBUBMzG7qzdI-hMbpV7P1bBGLxT1p0SB5DwHxx1gfVtcPwLwQFbNqYXr31E-Bj-eLO0SrS1nXsH_kw5r4qyOOtD5JQ08PxOG9gMR3QpCVzMAz-eAqXIHbukCiPjMjwrtf06PltUljXwD1jn55UTrK57_uDg56D3Yq_c2uv8lIzRVvhERoXQEu97cNkHpks8wsTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
رتل عسكري كبير يجوب شوارع العاصمة العراقية بغداد.تحديدا مدينة الصدر مناطق جميلة الطالبية المدينة تتحول لثكنة عسكرية</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/85571" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d9b8fa0a.mp4?token=eKRgEgFvRL-8qS1J1PVUu21xoCH-VFGR7tv1P-HDeD3VOTp8Joegdf8eC4QqVJ4V783FitKn-zkjkIVMdSscqAFvA-sYLcM4WWNRK9k9bzFj4GTZTPwvalqeV__Euz6aZjFiCukV4UQZzzT82Eby3mJBqrzqIPEkjmL4chE7uZ3tZzta8haP10fLx7g4F0cb-O1R7tW1cpr4mssib1Gi2xVpOlRA7YDWd0rQ8n5u2XO-mcxxFiZJA-hB8hNzJP_4yFcr6yQqmicaVGWgmtWAX40WtydFN49lRlog8ZdYkFoLV16TO5EPk-8r2YH4-xOH2YmMQ2oMoJaSe4-ZRdI7VSNapJkWGSpELMHUs9vh3-gnshZK5By9NDSEXLBQbV9QaXx93LEXnPKCQ9qsKYzMLUykLpsRmP_oZE-qiCAlVq2vrGkgcxhgFxgzVbZzKZMi1bWSB3fWHW_2xclBLShHdK5eGhEF9z7yi6WYWK1pWGKIZP1w_9YTDRToFgr8pHLLQhgeaI_ksSDLGe1llfMwtE85tOcfbBiH0foAcRzGxaLTg6RSsjzDWv9hJw29L-_9lWlFut9eqjDhVAibkDk0W6KEp3m0ya9u85htW0jkNqOEDbzAYB9YlQCSFmqGF_MymoEzNeB_trE-FzyVp9Xh9_dnDTCfeyWZfbIYj4oGacY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d9b8fa0a.mp4?token=eKRgEgFvRL-8qS1J1PVUu21xoCH-VFGR7tv1P-HDeD3VOTp8Joegdf8eC4QqVJ4V783FitKn-zkjkIVMdSscqAFvA-sYLcM4WWNRK9k9bzFj4GTZTPwvalqeV__Euz6aZjFiCukV4UQZzzT82Eby3mJBqrzqIPEkjmL4chE7uZ3tZzta8haP10fLx7g4F0cb-O1R7tW1cpr4mssib1Gi2xVpOlRA7YDWd0rQ8n5u2XO-mcxxFiZJA-hB8hNzJP_4yFcr6yQqmicaVGWgmtWAX40WtydFN49lRlog8ZdYkFoLV16TO5EPk-8r2YH4-xOH2YmMQ2oMoJaSe4-ZRdI7VSNapJkWGSpELMHUs9vh3-gnshZK5By9NDSEXLBQbV9QaXx93LEXnPKCQ9qsKYzMLUykLpsRmP_oZE-qiCAlVq2vrGkgcxhgFxgzVbZzKZMi1bWSB3fWHW_2xclBLShHdK5eGhEF9z7yi6WYWK1pWGKIZP1w_9YTDRToFgr8pHLLQhgeaI_ksSDLGe1llfMwtE85tOcfbBiH0foAcRzGxaLTg6RSsjzDWv9hJw29L-_9lWlFut9eqjDhVAibkDk0W6KEp3m0ya9u85htW0jkNqOEDbzAYB9YlQCSFmqGF_MymoEzNeB_trE-FzyVp9Xh9_dnDTCfeyWZfbIYj4oGacY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🔻
بعد فشل منظومة الباترويت اليونانية بحماية شركة أرامكو في جيزان السعودية
السعودية تخترع سلاح هام و نوعي جدا يدعى صابون نيكوت ؛ مراقبون اكدوا لنايا بعد هذا الاختراع سوف تتعاقد كل من روسيا والصين وباقي الدول العظمى مع هذا الاختراع السعودي لحماية منشأتها ؛ شركة لوك مارتن هود الأمريكية قالت ان هذه الصابونة يعمل ضمن المزلق او اشبه بالفازلين ..</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85570" target="_blank">📅 20:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي‏: من المحتمل أن تتوصل مسقط وطهران لاتفاق إما الليلة أو غدا حول هرمز.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/85569" target="_blank">📅 20:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي‏: من المحتمل أن تتوصل مسقط وطهران لاتفاق إما الليلة أو غدا حول هرمز.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85568" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: إحراز تقدم في المحادثات ويمكن التوصل لاتفاق بين إيران وسلطنة عمان خلال عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/85567" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ترامب يوجه بعدم مهاجمة ايران يوم الجمعة، القرار يمنح الدبلوماسية مساحة، مع بقاء خطط العودة للعمليات العسكرية جاهزة إذا صدرت أوامر جديدة.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/85566" target="_blank">📅 20:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🇺🇸
لاول مرة منذ 13 ليلة   لم تهاجم قيادة العمليات الأمريكية الوسطى ايران ولم تنشر اي بيان !</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85565" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو يتحدث عن اطلاق صاروخ من جنوب لبنان نحو مناطق التوغل</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85564" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881aa0985d.mp4?token=golYZL-eOQarmQI917hdHiHh6uTXVMj2iLPwJa0q8dFNfX5yRS8eWn0ZH7uwLOwi-eK4nSFtDV06IIK7845aGSdzR8senWMJm-_eDZ7N_ByrQRy2s-ySnPBXpa2h5Ed-Bg_joijmwF4EPuM40MoytNSU3OYcLvyEY_sB3XXB-eDqL4OSehcgCjuIfN_bTlKn9mY2kKPGV3vFedPkkFhqTF9v1_JJex9oIi9gdUh3FCAZOMRN2Epb6ZP3HJK4VEPBLoa6e_l-O-AzZBIP55j8EiL9JSI1yyXGRD-0sLFblCyrfjKsPgjxF8RlTzhPog-LKhcLSQNLaSsX8WLq-GmUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881aa0985d.mp4?token=golYZL-eOQarmQI917hdHiHh6uTXVMj2iLPwJa0q8dFNfX5yRS8eWn0ZH7uwLOwi-eK4nSFtDV06IIK7845aGSdzR8senWMJm-_eDZ7N_ByrQRy2s-ySnPBXpa2h5Ed-Bg_joijmwF4EPuM40MoytNSU3OYcLvyEY_sB3XXB-eDqL4OSehcgCjuIfN_bTlKn9mY2kKPGV3vFedPkkFhqTF9v1_JJex9oIi9gdUh3FCAZOMRN2Epb6ZP3HJK4VEPBLoa6e_l-O-AzZBIP55j8EiL9JSI1yyXGRD-0sLFblCyrfjKsPgjxF8RlTzhPog-LKhcLSQNLaSsX8WLq-GmUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
من مطار العقبة في الاردن حيث تتوالى طائرات النقل العسكري الاميركي بالهبوط.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/85563" target="_blank">📅 20:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو يتحدث عن اطلاق صاروخ من جنوب لبنان نحو مناطق التوغل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/85562" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00bbbd525.mp4?token=T5DZc-Hod6ZRPbykXvVAkQaKHndQUNq3BLov_RS2ZKlAqZbOYdyIMrfeyU3QHKOsJOBBKNNTMQv53dd3vpAR2rWsJr7U3eOSFr8TzBPyqdxXLmlAiE0yAp3nPau-EosaM8BLU8qEJ0nrcOov4yhm4N1fcs6GeuBj7yZGfMWfqfOQIu9de4A7niDdw8hEhuTmlTrL92J69IkR5j_zLr7INpL7H_GMu8pJh4g_3jIbW_9SXZxLwENBWZjIN72g37pz8F6WfOPbk38kYdgm42O7-YSWHVnuP6hZH1vyxFFpLNdfUu5GSGDq7QrWQt-A1zRo3z12LIJMFx6QcxBRJzEMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00bbbd525.mp4?token=T5DZc-Hod6ZRPbykXvVAkQaKHndQUNq3BLov_RS2ZKlAqZbOYdyIMrfeyU3QHKOsJOBBKNNTMQv53dd3vpAR2rWsJr7U3eOSFr8TzBPyqdxXLmlAiE0yAp3nPau-EosaM8BLU8qEJ0nrcOov4yhm4N1fcs6GeuBj7yZGfMWfqfOQIu9de4A7niDdw8hEhuTmlTrL92J69IkR5j_zLr7INpL7H_GMu8pJh4g_3jIbW_9SXZxLwENBWZjIN72g37pz8F6WfOPbk38kYdgm42O7-YSWHVnuP6hZH1vyxFFpLNdfUu5GSGDq7QrWQt-A1zRo3z12LIJMFx6QcxBRJzEMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اعلام العدو يتحدث عن حدث امني جنوب ضفة الغربية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85561" target="_blank">📅 19:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
اعلام العدو يتحدث عن حدث امني جنوب ضفة الغربية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85560" target="_blank">📅 19:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">غضب واسع يجتاح الشارع العراقي إثر قيام مديرية حماية الحرمين بأمر من اللواء المدعو أنور النصراوي بإزالة صور القادة الشهداء ومنع رفعها في مدينة كربلاء المقدسة بدعوى أنها تعد من المظاهر ذات الطابع السياسي كما تم اعتقال عدد من الشباب ومنع إقامة أحد المواكب الحسينية…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85559" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFVg331JRwytNaDdBQAT0DElNt9bI4DMZ_X2OYwFd9f1pwqdZK0fTgUqNJtNCg7niqCXcehYQb7vcyYoFCFdWGMQM65Dv6aX-_WMynv50YqlldzxmRll3vZ-wONJ4NGMQnVZsftVDy_MCEq_zhmB3ZONb79_htOelWCk5XiTi1G_nGbHdqlzEgnT1B6-hTPuhDCzxfAlVjdK8YIdorxJmFC4ukbwale6Vvyq44ZsN1REXsM3aq2WbdYv2PKCwgBRWtOELJ6S5K5LEnRpbc6MULRxLGBKCXF0xURcaRdGwQlEmkpR3b7Zgw9WHNo_9u28G2PHMEMNXwOp6VZTSQ_NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان وسط محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/85558" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85556">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kbwi6SCIaK8stVSqso5IDUSRPiPcm0eVZy_eZ0yiWGh71UYj3FuZne34GWyuqfH1dyBDnZ1aHlMYcBHy7IwJlxsfr2dROq3BeCbH099Sez6FNzM6BAl2iP67jQG6YWbHdB6iFD5VGJeIpatK-6qBaAY_aWB8bLWu9ynDEs-PlAaTDQVoX8NB-IpXlf-V5mKxgKc-xmWjsLli0CsLr2S7oHzmZ02dJd8o1Qoxzbi8zLKZs9eFD8xt7yDrldySrcqbKoGJpnVrU3SfEfenbrrEXu4TbFWl54R5TGPddMeyfaSxFkP44KvY3fVG2aRdi-g8I3lEp2lTEKtvIv7Gij7bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfQ_etqJ7gX_5JQnP0_19JRA7rKrYRa-Ugri3SgOMHrGflgTcvO5zHhdlCiSCD86C6Yt55EVaShXLRuawdd2IMUKEz-QwH8m83l2rFQ9LJv_3TxDXaH-Y46-Qy9LTZtdMx6J9dmhPbkXlaKPqUazJv3zONzzCBrjhXCHFXgvrVnfLNA04la98sUVom_bB3U-aN2SWL4muDjKD7REJ9rz71IBuQ8IaxafdfrZpUyFB08UoBhzAxEY62RUbSprir_PqxgwSjeCKx4QEEyZT_iqiMbem7NbF1ZmxfK22mOqBHuJE4ZL4EFdP1lDc7Rahk47424YCqwbpIfriOd3tDeqog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مشاهد من مطار أربيل الدولي شمالي العراق، حيث تواصل عشرات طائرات النقل العسكري الأمريكية عمليات الهبوط والإقلاع في ظل أسباب لا تزال مجهولة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/85556" target="_blank">📅 18:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇱
اعلام العدو:
الهجوم الذي كان مخططًا له أمس تم تأجيله إلى موعد غير محدد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85555" target="_blank">📅 18:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85551">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6aqQTfwlUu-CGgn6C0dwKrXwcUC_xKooVxZ1yCqT40d2JRviGzJzdMZYw9QDZbJ1ILYEBT6FAqo_akiwNLTTIUgZTo1FhMeU7B6rdNMkWcgydCWOg2RViQyKOr48D56Cnyw5QpOtUkNC8K8s81NvNojFbrnbox46AG3q1d8AykfzUZJhUj_--Vw-WOMYxIhiRWhqDxWGMvuXmXysMJRpuoR0fxmMUEBMr1v8l4BxZQt0NRB4BoXIi3l7ud8chELfQGuKnONRz7Urzo_TliH2xP52hIuUd_Vfrl0RoT8jNLJ9rAgBDFxbm3soAABf434QMRGuZVvlWYMUdC5lIb_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IthlWLd8TV87cRU9pj09Rgtb9m8DsfndKG4a7rtiXtZKaztzcDIX0yjsKirXIwo3hylicaM034fTyYwqamw3snmceNIyR9IvS_9ZG5g9rBlrIZDSbmN-VHzpYoPjyh-pYiz__gIp-HzqNytufi8B86syZsCl2dOqy6D8PhvHTnoOQU3XIPska16ENCIKCz5A3oaETsfyVCCcuosr0nM7UiYnOBecAv5xQSS-1VnDqK-wGC57Q2DP_zhCFZ8sh1Nwxo2nwtMTpl0EsGgXVnhnf36RcOxHlSGIfBpCCrXp26oH2vcU2auzVxgNa_o-bG6CLhZhi9guo8jyRkJ5mVPQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeneTpoZPA321ucsVS8Wq1JUekRxke3zex2FSvENTJCkOWs07S1Neksp3ua2ToMVPD1k-54CHFrYfTahmjjqRdB2j4ebV5jhbrvod4u_bpJo6sCd_qYWHwwukk3h2JEtzBt5v8JhoZ1UC2bfe7lImQC0qs6aQBx0wotkxHX3H3PUTam-L0JjtyVKl7jML5uNKk9yXWS3zLinGZ8STkdyb5KbeOsxvMmC_uIilNT-OGzqNhMklM7eEAUfyvSG7iXJjHC7bBaKMni9F0jYzhSIefnrXMvDjV56UKrjeHij6zrV_rDZolXYBSkT1XyESKKIAdRXEz7952T2G6dcuQQ3-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5a389e95.mp4?token=QHnRz2Yx8WzGGQ0hIsfmtk2V4Lyy70JIlYlaKuciFilzPolRIhYBY0-_CBooMA5AXpjeSmvlmMwEtMQhZDidA7IcoVvftnElQEbhlgM7QFifVdfbnJRhpLS-Fp7jYovuAFi_wvnhlERCSHueaEU8zepyYihJfNBcvgnrX5pVPvlTS44o9KXqDsltZKqnE7iTUzUdcxstg7LxdSa8VYaX5lGcHS-20t2p8vwmGMVj1qCyutHPgf51kVHNl3bw-66uIirGhLaNudzOScetG4rAqJifqC0yTpv-M-_KLhn_7wD21_TXEoWaTgPSELNZ8XCcGajChhDlacYRjeq5ojGWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5a389e95.mp4?token=QHnRz2Yx8WzGGQ0hIsfmtk2V4Lyy70JIlYlaKuciFilzPolRIhYBY0-_CBooMA5AXpjeSmvlmMwEtMQhZDidA7IcoVvftnElQEbhlgM7QFifVdfbnJRhpLS-Fp7jYovuAFi_wvnhlERCSHueaEU8zepyYihJfNBcvgnrX5pVPvlTS44o9KXqDsltZKqnE7iTUzUdcxstg7LxdSa8VYaX5lGcHS-20t2p8vwmGMVj1qCyutHPgf51kVHNl3bw-66uIirGhLaNudzOScetG4rAqJifqC0yTpv-M-_KLhn_7wD21_TXEoWaTgPSELNZ8XCcGajChhDlacYRjeq5ojGWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غضب واسع يجتاح الشارع العراقي إثر قيام مديرية حماية الحرمين بأمر من اللواء المدعو أنور النصراوي بإزالة صور القادة الشهداء ومنع رفعها في مدينة كربلاء المقدسة بدعوى أنها تعد من المظاهر ذات الطابع السياسي كما تم اعتقال عدد من الشباب ومنع إقامة أحد المواكب الحسينية الأمر الذي أثار موجة من الاستياء وسط مطالبات بمحاسبته واتخاذ الإجراءات القانونية بحقه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/85551" target="_blank">📅 17:33 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
