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
<img src="https://cdn4.telesco.pe/file/lALVgBpkwCEtDDIZx9z1z4K7WSrlVQZ_qMHlJveep48HFiUOv3Ox8cib4arAlGnnjD1_6Zt1Ij7Cs_E-MfDyx2r031wpGxaVeAqz5TZzFmVcSUSX061_0VrU1Rarh3diDYmkFkmBwy9W6Ljd_Virk0OTRz0cY5x4KE9pIdBK_L9VZYn8bEOk99N6KuWmc_y-9g_bH6Atwz4l7jn1pZYb0H--D1SyAhqv5J62qN_MueAPJxFy5AidT4f7zoPH8rQK3k7X13Zua9PoMhrHGCfFIbvH6EbgViZ4t-itpYhttwWvh1Nx2eOFhjLpi-pZuLTZIAoebo2nlMftSzC2ripsYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-93604">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
🇸🇦
الرياض تتلقى الجزء الأكبر من الرد اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/naya_foriraq/93604" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93603">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e039ec716.mp4?token=jiicq4PMbl74nuv2ynBI3WEMnYKj5G3P-2mhQnUIK-LGE5ax4hBC2fAiZ5sTsKwBFI1Q9M8gK95_Iz6_HTXV0eITvSEVW8zcEt-FfL4fsLo1KoW8MwMDSE5rx7vkEwq4Gg7FCySAZFGHv_VIC2POVN_8vagaAhBj8j62PjxYs3MaHQ5RWMX91Fx2LnvsryVVNfjo7pWcV11wx7773ISYUhK-_-razZE3lqx0Ho5qp3RrRicms-puMJBqrQUFPfMUcz5iIDAS618eLwil_WNzvUB68ZTdGJ9sLP_29r5mWDQZddvwnmZS3CVsXrnoZFOb35kHuaPm18Qt1c2LE84l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e039ec716.mp4?token=jiicq4PMbl74nuv2ynBI3WEMnYKj5G3P-2mhQnUIK-LGE5ax4hBC2fAiZ5sTsKwBFI1Q9M8gK95_Iz6_HTXV0eITvSEVW8zcEt-FfL4fsLo1KoW8MwMDSE5rx7vkEwq4Gg7FCySAZFGHv_VIC2POVN_8vagaAhBj8j62PjxYs3MaHQ5RWMX91Fx2LnvsryVVNfjo7pWcV11wx7773ISYUhK-_-razZE3lqx0Ho5qp3RrRicms-puMJBqrQUFPfMUcz5iIDAS618eLwil_WNzvUB68ZTdGJ9sLP_29r5mWDQZddvwnmZS3CVsXrnoZFOb35kHuaPm18Qt1c2LE84l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
الرياض تتلقى الجزء الأكبر من الرد اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/naya_foriraq/93603" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93602">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOryk7ehNGinoVTwPzj9IFCyy3tkIpDRkvHg_XfS9VS13lYcqIquPES3BK-oKYNN8y7598f4SnoiiIewi6CeOfJFKtHoBKuM0M1_RccR2uDilENLj1E1Fulj9wc7pltcEBxmZap6LxrkWUmYpWAeLW3dzemzcqHIQaF_mDSgMhHkr_JESfJZv-OCB2ONZ9F30DcS13aZllwD-pTtkivxd1QLeswi4SMlvay4kUgPwquMAIDtdIA0BBlzcfaFDlN27dY_CIQM0pAXEise-zMbU9Bat0YWwD2XX7eC2C_OgNDQ_FzDkMULOx_dQxwXlJihXrZcJsu1mXpcIoIqx6uR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينتي شحن في مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/naya_foriraq/93602" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93601">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e74ad2dea.mp4?token=VP45G29sJVKRF_PVKOZ0U-FyaaH_W9jUAN3qtBOhezVLocJ3wJelit4VVR7px9NS-JkwLyR74xQh5C1_9UEAfmTbWjRe2jN8_erhI9qeztMsLXvCkffiDO3CBaq80chkZN7eXKlSvjzw7tfAkYXCWpZM1TriQdmieVHtyTX5ldlseDzSIo-aUG5ymZiSro5T4RTkGZDaOoV5_iSt-QnJnXNc8Y25OytoftFHopC3mMcSFX8od2petKDXZ02pqMl0IU4wRM_W7VA7gzYuwqw5hlmh8MC9qnNWieEpwvSDEVbxvoMJQZ6dFCQRv11DP032if9uA5oTRTMNkhKp6qpsnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e74ad2dea.mp4?token=VP45G29sJVKRF_PVKOZ0U-FyaaH_W9jUAN3qtBOhezVLocJ3wJelit4VVR7px9NS-JkwLyR74xQh5C1_9UEAfmTbWjRe2jN8_erhI9qeztMsLXvCkffiDO3CBaq80chkZN7eXKlSvjzw7tfAkYXCWpZM1TriQdmieVHtyTX5ldlseDzSIo-aUG5ymZiSro5T4RTkGZDaOoV5_iSt-QnJnXNc8Y25OytoftFHopC3mMcSFX8od2petKDXZ02pqMl0IU4wRM_W7VA7gzYuwqw5hlmh8MC9qnNWieEpwvSDEVbxvoMJQZ6dFCQRv11DP032if9uA5oTRTMNkhKp6qpsnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تجدد في الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/naya_foriraq/93601" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93600">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7zVT27MGEJcjVNtBh7ekzm3p0cQ3MTIJ4gcgzDPyZehGMv2l3a-LgILEhqpfV0KA50YaleYItltJ5VZ9yQ-ekxeVmY5_oGJUYWxFUvdfStJ_2HDky_GDbwgSRyF2_1CAAcEFoTlAvpPDlkpAU84Yrl4XWyHAh_RS3KRCmoF3rFmtPCOaZQjBAAMW9vASXyX3Kh7ux4DbqTx2dei_NvVJZEYogjzy3bPRFBJQAbmWnfi_n9vjarX83CmDUjaevNQdSukwdc08B5YTm2onboyyCZ91yoz0TpxJ_4P6QT1c3uZzodA-DHw-gydnlpsNmpjP7gOMivBUiHeLbQ8nv58UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد تركيا وباكستان وبريطانيا واوروبا ومصر وكمبوديا وبوركينا فاسو واوغندا.. وزير الدفاع السعودي يطلب الحماية من بولندا !</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/93600" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93599">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇦
🇾🇪
توقف العمليات الجوية في مطار فهد الدولي بالدمام</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/93599" target="_blank">📅 22:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93598">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e6ef21d.mp4?token=PNmyMjPkQ-KGEQ3tSV0E9VXev1uyRi1gjH-a4CrpAIqeVA8GqmHdJpCdSWh8vNSAhBskaqOKWFEJ2hisJU5YGJW05BDjEPEdmkVwouuFR0RZHsP6p83XSZwVYGarRi0dyIp166maQM4WeMuJKC6GA18MihAGWdteo_HfXaZeFA35gyrq7LFbPGq7tJuq2Z2XXqFy4PQm6pnOvjQHaCEWaGcI6LdZl-95z2bz2r3HaYrkIZdmx0flh3jsY7gu92gRhERQxWpSw1mqnz2fWIvRRJAImBgyYzMiNU4yOEm6_AzJooDlD8DcO6I3j7gutuedYms6mOgNUwyCQ9mHRJPT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e6ef21d.mp4?token=PNmyMjPkQ-KGEQ3tSV0E9VXev1uyRi1gjH-a4CrpAIqeVA8GqmHdJpCdSWh8vNSAhBskaqOKWFEJ2hisJU5YGJW05BDjEPEdmkVwouuFR0RZHsP6p83XSZwVYGarRi0dyIp166maQM4WeMuJKC6GA18MihAGWdteo_HfXaZeFA35gyrq7LFbPGq7tJuq2Z2XXqFy4PQm6pnOvjQHaCEWaGcI6LdZl-95z2bz2r3HaYrkIZdmx0flh3jsY7gu92gRhERQxWpSw1mqnz2fWIvRRJAImBgyYzMiNU4yOEm6_AzJooDlD8DcO6I3j7gutuedYms6mOgNUwyCQ9mHRJPT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام السعودي يهدد من يقوم بتصوير مواقع سقوط الصواريخ بالاجراءات القانونية
طبعا الاجراءات على طريقة خاشقجي</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/93598" target="_blank">📅 22:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇸🇦
🇾🇪
توقف العمليات الجوية في مطار فهد الدولي بالدمام</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/93597" target="_blank">📅 22:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/93596" target="_blank">📅 22:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقرات شركة ارامكو في الظهران تتعرض للقصف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/93595" target="_blank">📅 22:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سماع دوي انفجارات في مطار الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/93594" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">استهداف مصفاة الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/93593" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">استهداف مصفاة الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/93592" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الرياض وما بعد الرياض
لبيك يا ابو جبريل</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/naya_foriraq/93591" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93590" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/93590" target="_blank">📅 22:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات تهز الخبر المنطقة الشرقية من السعودية المحتلة .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/93589" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/93587" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صاروخ باليستي يستهدف حرض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/93586" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الرد اليمني بدأ
المحطات بالمحطات
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/93585" target="_blank">📅 22:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/93584" target="_blank">📅 22:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/93583" target="_blank">📅 22:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">منشأت ارامكو في المنطقة الشرقية السعودية تحت رحمة صواريخ القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/93582" target="_blank">📅 22:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93581">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇬🇧
استدعت الخارجية الإيرانية السفير البريطاني في طهران، ردًا على اتهامات بريطانية نسبت حادثة مزعومة في قاعدة «فيرفورد» العسكرية إلى إيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/93581" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93580">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBzO08Mv4AdAMVpBk9Npfmt13siKjc0tqQH2I2-1pv4YHxc9kT2MSmOwwGttsz2w-ZeoRGKhQeDnjsvnt-M78jKTwxqZ4UTY5GB43XigPnd_CPF9N4vKcVzL9wQKaA8Py29Mv6EOxEDkKpROq-c78m_yb05yluugfAUT59xaczRkK4KUZfZ_4yCig8xEp12AH-w8rWylkOR8XZ5GPYrWnalV0mlcTp4sIIfGdWtPyLa99mknoGgiFmF74fFAExdbaX5HBISMxqprNyt3OQsCV4sYUg16zXUOODfrpFw8qRDe9pJmcjydixthuZaSEjX4TBS3_2jRpgTVV9_c0db6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن والاراضي المحتلة.
- طائرة (KC-135) عدد 1.
- طائرة (MQ9) عدد 1.
- طائرة (E-11) عدد 2.
- طائرة (MQ1) عدد 1.
🔻
يوم الاثنين 12-10-2026
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/93580" target="_blank">📅 21:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93579">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">منشأت ارامكو في المنطقة الشرقية السعودية تحت رحمة صواريخ القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93579" target="_blank">📅 21:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93578">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93578" target="_blank">📅 21:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93577">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93577" target="_blank">📅 21:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93576">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تناشد المعنيين داخل انصار الله:
يجب على الحوثيين الوقف الفوري لكافة العمليات الإرهابية والتي تستهدف المدنيين والأعيان المدنية بما فيها المطارات والموانيء والمنشآت النفطية والبنية التحتية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93576" target="_blank">📅 21:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93575">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سوالف الگهوة
بنكين خارج منصب نائب رئيس الوزراء ؛ الحجي العامري زعلان بسبب الدفاع و مشارب الجاي في اجتماع الاطار ..</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93575" target="_blank">📅 21:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93574" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 104 غارات جوية وصواريخ، استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات ذمار وتعز وعمران ولحج والجوف ومأرب وصعدة والحديدة من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران، وخلفت شهداء وجرحى من المدنيين.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2281 غارة جوية وصاروخاً.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93573" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93572">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4CWLagTG7ve5KSigUPJMmYiRtKOYXauwCI37In5KCCvjoasCnH43YU_AHGivgvQDBnTJTtPzL-9CjMFgXlFpvWlI3nxv4WteQJM7RZ_9OKcKqATmJp9fM958aaZcg1ISc4L5Z10qFMvHW6eJcQhATsQ8cu9XFcO4dzn4_x31QFaWSw6t0lEEIS1zf5U-AVIIL2guvD7LVMVfVJdvm8GfBMoJro4h7ObsHKxyjlwTmpyjtGszg-hgTILdDmTQMT8WcfNtNUdsIU87Jy1Mk4qPvbjpi5bS4Yr-OdcnEWK1GU_V8x-fMq-tHGeKg4qb0eK7Q48K6xetOq9zMad2A0xsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93572" target="_blank">📅 19:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845c9be631.mp4?token=R-FEB0M9OBiRDVFmenaRMxIDT1_eJxDaE4vVB9EM_UvoqKT2nusaVeeWZ6hh2xP2qOzHgn6Xbii6-SQHxNzwRE3ZliVW5ZBhn-mVWzXNwCqlU-oon7a_PNOFIOYvVmRitozO2EUPSihTU35hNoXL2F8oN8jDGsWkOM9aq6D4SRoM0TSW-hpE5NLMRqEM9MwuTY1JxDSpdYdNV9gT7AxVnRBXirTXfjtxIoBGEuf74-ssd9MQo1zI4AGTYSbkph6q6bsy6jgZ3Ow8WmYQJLXTA8aGGw7bSDL6d-DulmVeavs1s8CZUBpsZTs7iaxs0K-hEokwpiRs9MDHuINePODmGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845c9be631.mp4?token=R-FEB0M9OBiRDVFmenaRMxIDT1_eJxDaE4vVB9EM_UvoqKT2nusaVeeWZ6hh2xP2qOzHgn6Xbii6-SQHxNzwRE3ZliVW5ZBhn-mVWzXNwCqlU-oon7a_PNOFIOYvVmRitozO2EUPSihTU35hNoXL2F8oN8jDGsWkOM9aq6D4SRoM0TSW-hpE5NLMRqEM9MwuTY1JxDSpdYdNV9gT7AxVnRBXirTXfjtxIoBGEuf74-ssd9MQo1zI4AGTYSbkph6q6bsy6jgZ3Ow8WmYQJLXTA8aGGw7bSDL6d-DulmVeavs1s8CZUBpsZTs7iaxs0K-hEokwpiRs9MDHuINePODmGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93571" target="_blank">📅 19:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b1cdcb24.mp4?token=aTKjmAVPcS5QRWh-Y0t3JkzYukG8mTMn9_HRSsoqNHNsXWFUTHFdFYRWYrdNP6kdTcYwI0S1jrQ35lXp1UWWp0QEfwxw3ttNNuNZa4mGoYNU3Ga2o7gvt8SoKKM4Ld3T_DlvRTdlS2KYA7N0YAnDFVTU6gNvScv5s4e5a6X1-nNVEVQ0yJ78_gctkvuQ6laHWAEAFaVukddwacUWOFJkLnrbZvty9LPDXcNIjbgOrAXfu3qq4rUWWQRU6VjUgof2enQ0UzagN5gG1htyn5TzAyFkjVbz6h73hQh_e2ngn_IbgCDlvGaXdGd9CYlTrbGdRpJvcSrkn7Avih_Mv_QQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b1cdcb24.mp4?token=aTKjmAVPcS5QRWh-Y0t3JkzYukG8mTMn9_HRSsoqNHNsXWFUTHFdFYRWYrdNP6kdTcYwI0S1jrQ35lXp1UWWp0QEfwxw3ttNNuNZa4mGoYNU3Ga2o7gvt8SoKKM4Ld3T_DlvRTdlS2KYA7N0YAnDFVTU6gNvScv5s4e5a6X1-nNVEVQ0yJ78_gctkvuQ6laHWAEAFaVukddwacUWOFJkLnrbZvty9LPDXcNIjbgOrAXfu3qq4rUWWQRU6VjUgof2enQ0UzagN5gG1htyn5TzAyFkjVbz6h73hQh_e2ngn_IbgCDlvGaXdGd9CYlTrbGdRpJvcSrkn7Avih_Mv_QQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93570" target="_blank">📅 19:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
العراق يوجه برفع مستوى الجاهزية القتالية لقواته المسلحة إلى أعلى المستويات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93569" target="_blank">📅 18:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e752ab5a3.mp4?token=FjCQuf39IWuVgn9BotVm7iyhdnurmxhWBY-dTTIFH3TGoKPrcFjdXrmeI_vXSE-LSTfnotNLtiq4SguHGMB_0yNQOUqlYzbJgcaHPW9r8qzKcFNb9Fg7vzCJYEyeRQRheswH0yBGlJ6bmsPiBnNC08aiGQyqPY-vJM4uLJKDjH4HKMpr5E8IKt9OaCaqV1v60lbX5t3KEKt_PqbSS0tWRiyO6zX5CfsSWTVunSnjCP3B1Mwe5MJ5LLIJRSE8HZ36NJXEpmDH7-N0nhlRDD6gY8BEZJ7cmGMEFEtNX2MilcgCb90nj34XYPHTkIpqNNXc8X_Rp4tmcZt8uNrUVSVYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e752ab5a3.mp4?token=FjCQuf39IWuVgn9BotVm7iyhdnurmxhWBY-dTTIFH3TGoKPrcFjdXrmeI_vXSE-LSTfnotNLtiq4SguHGMB_0yNQOUqlYzbJgcaHPW9r8qzKcFNb9Fg7vzCJYEyeRQRheswH0yBGlJ6bmsPiBnNC08aiGQyqPY-vJM4uLJKDjH4HKMpr5E8IKt9OaCaqV1v60lbX5t3KEKt_PqbSS0tWRiyO6zX5CfsSWTVunSnjCP3B1Mwe5MJ5LLIJRSE8HZ36NJXEpmDH7-N0nhlRDD6gY8BEZJ7cmGMEFEtNX2MilcgCb90nj34XYPHTkIpqNNXc8X_Rp4tmcZt8uNrUVSVYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من مداخل مدينة تعز والتقدم مستمر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93568" target="_blank">📅 18:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93566">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اعلام العدو: المشتبك مصاب</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93566" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انباء اولية عن استشهاد المقتحم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93565" target="_blank">📅 18:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اصابة صهيوني بجروح خطيرة كحصيلة اولية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93564" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انباء اولية عن استشهاد المقتحم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93563" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اشتباكات مسلحة في مطار رامون</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93562" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مسلح يقتحم مطار رامون الاسرائيلي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93561" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93560">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسلح يقتحم مطار رامون الاسرائيلي</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93560" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رويترز عن مصدر دبلوماسي تركي:
اتصال بين وزيري خارجية تركيا وإيران لبحث الجهود الجارية لحل النزاعات الإقليمية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93559" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f5f511f2.mp4?token=su3mil2WhKCLALyGKMOpf9pbk6qMO8Wz2ediSpT7hfrI116l4C-SawORYbgmhFQQ8HH1tO0Lrofb5C5LLCqkvu5irzXl6i5c0Z4WSLaj_bvfM9GCSl_qkm6vAOO2fMUXTWN3MuKuZMcLWLV-1ShT8K0_ipdpVQ41LJlAnnz-kR_Rk8TE09fBNgTQ8LRODIxJPqv09jt_2P-NTW_G0yyYBIQ4rpjzvuMz0DzBg0aXR6HocHx3QmcPGPgdkI8misovkBuYta1d87WhQNIqK1HbdwuDSnqK75cbiv_SkkQ-eX_suM-e19expzaRio8caqUDB-WD8f-kX1B34WWJXxhu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f5f511f2.mp4?token=su3mil2WhKCLALyGKMOpf9pbk6qMO8Wz2ediSpT7hfrI116l4C-SawORYbgmhFQQ8HH1tO0Lrofb5C5LLCqkvu5irzXl6i5c0Z4WSLaj_bvfM9GCSl_qkm6vAOO2fMUXTWN3MuKuZMcLWLV-1ShT8K0_ipdpVQ41LJlAnnz-kR_Rk8TE09fBNgTQ8LRODIxJPqv09jt_2P-NTW_G0yyYBIQ4rpjzvuMz0DzBg0aXR6HocHx3QmcPGPgdkI8misovkBuYta1d87WhQNIqK1HbdwuDSnqK75cbiv_SkkQ-eX_suM-e19expzaRio8caqUDB-WD8f-kX1B34WWJXxhu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتعال سفينة نفطية مخالفة في شرق مضيق هرمز</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93558" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/So9kde9fE32s-AFFgTH6nwM7CHvLjBd_bs6Wa65yJMT2GwfVvGhxSqIM1O6G5PFP_v204hG0rwHiBf4cOo0it2Sxw2oq2hHYN0r03gJLwDhurxvDQZ9vw-EQ9BM6jkA-PiVmILgU89vMohVTX45xRZIlDGMxfh39EUAuMPJQbG_Yn2MrLfsmPR8J2RrQah1xzCHBt5oaNw_M_Jy0dTVMkc54WoMG1_-Fj1v8aLA20MM26DYEl5S03O-uEoXzkGgnX1f4MHeLClWp6xXbP3ctriPlEl2q3Plk6_UVK8WXWB3A2s_S4qV0-jnEg3i6Z2jSBUmWP7HOqriNgSNVQiIHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiT7oM6BKocePqFA9WGOO8vFgtQjV5SzHYuVFRnTdpJFKqwLrNwSVqSviNlO3IIyCqTS68x_vtokCwYqnCHwjgZCQ5iV4iGNKS5UcQM07SgjoW1ecZSNUzyFn7XAY0dO_ew2qzvjRAGuYTeS8aQwl3B_H3IxupjU7OdV6TUT7YLs7FJXkQJUuwzxR74CFJD_22h2nGQ5yY7qIIgMF0Xl3AhJotf1zzzSANFXoFidWE92D-sd7FYLOX3cdqaxSMiLV9o-iaxzd-6-H6ERRfXOH4unUlLDsz_kZcKjsfCaprqRWVq02iGpsQU5qeBXjIKGjifQwUOQVDB42qZeoHqAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGRuU_hWG3YN5WKd_DvnGRW_PpcR_7Zj7bFw-0kyaxs9MHj7wciF-3UyP5eEo_Xe1dIHXUYFMwrpVCVAKp0W7b7H8-q19dK-UauEhlH4NIrHYxrl9Gt5mvU6OIUI9wFPLrMtqQXYozIwKVIsjgWRQlqKgjS2VjJ0chcKpNrmVeTRhQhsIkKrkju7ME4TkwVh6UtyFtwTqlnbXg6hKCUUa_VEgy0HIi3xu-SveKm5zchiuRtWfWVKj_Oercx-G8rFrky4X32Nz8gXLL-UbXATvjJ9if77ZIzyAjueznjL1bftcn5EFIIpe-NfC4RgbzD4hNAO5SzeNECnpUEnmzDdcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدعو لاخلاء عدد من الاهداف في السعودية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93555" target="_blank">📅 17:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93554" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93553" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Rau3-lvhTaHshg7vXpOmCDBUsJLX5PF2ONIz7qJY3qxtjjTLQUrOsNLQ0w6_4suJGMTFy2vxi9cEjWKRMWM1Sh1QGUAHI1b8JI1GiIwvf_hiC_JQd-xRqj6lNhemdT8TC2mYd0B_yYLrbO_WP8jcfqjlbgOHgiXtuePFp59y5tpPiGn6j51k9p8rSlPenmkyigmERyux1Fsn4eLnQZQRqVGZIVMjb6z9_MwZauUQeEu7LlFdS-WH66jfPe2lBCANnUJ1agHplgF8jHZZSd1qan4ZxWGNI43tL6UUGBlyDYm3JZmiJdtDkTlLS5CQwCDQIevpeOOhJwoV01mFKyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية في مداخل تعز</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93552" target="_blank">📅 17:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇾🇪
العميد يحيى سريع:
قواتنا المسلحة تتصدى في هذه الأثناء لتشكيلات العدو السعودي القتالية التى تستهدف العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93551" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
🇾🇪
شركة النفط اليمنية:
تؤكد شركة النفط اليمنية أنها اتخذت مسبقاً كافة الإجراءات والتدابير الاحترازية اللازمة لمواجهة أي طارئ، بما يضمن استقرار الوضع التمويني في المناطق الحرة واستمرار تلبية احتياجات المواطنين بصورة طبيعية.
وتوضح الشركة أن منشآت الصباحة لا تحتوي على أي مخزون من المشتقات النفطية في الوقت الراهن، وبالتالي فإن استهدافها لا يؤثر على المخزون النفطي أو الإمدادات التموينية، حيث تتوافر احتياجات المواطنين من المشتقات النفطية في منشآت ومواقع آمنة، وبكميات كافية لتغطية الاحتياجات لفترات طويلة.
وتطمئن الشركة المواطنين بأن الوضع التمويني مستقر تماماً، وأنها مستمرة في اتخاذ التدابير اللازمة لضمان استمرار توفر المشتقات النفطية وعدم تأثر احتياجات المواطنين.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93550" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجار في صنعاء</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93549" target="_blank">📅 17:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجار في صنعاء</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93548" target="_blank">📅 17:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R95S-2zGdV4AqWSXe47sk5M-bnv7F0D3p9bPy26nDi4R1YNyIb8hU1pl45UCtwGADEMQQ2MwsAVj_a_4GjDUGZmuGsgkcPXzoY2wr3ASoKcKYM_HMnY6ouWuQLTuUZ16jQI5wyUDoH2Ar5JYUJgQh7sKaGWeNiMBOAul21yGmTR7iYTskDGDOalUwx4zpTahyWqzAUP4ECIs-LdZm0m1tSAOfFrHM8klQ_C6e_kMAYh03ak1azcpFa7igJiN_rVewZqK7f5SzAwm56d-egRiX7T3K9-1d9h-SxyxKLFWkJgQTTgTCOg8x2Cwp0zRQwVSJJOb9pvQFzGpjqltT5rVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYjeiTvtWbc3Tt30Wkn7ixdGKAf_MpubFTasTdGs6BJCft3OZysz3SeQsKXnvfELMQmp1-WHXBfRH9_0UCGk8oJEHBlupxtFfQi7c4QRsf199sWwEQAFrZGmRPQToG1aRVsooyrEkfRQEnTayHJG9NwrjvtPI_DqNQdO3W9kn3zP_YYMJmJqp45Xyrs1x0Z3FJiBThxZgKyiK5OKycVf6V7JBd9hhBJXGUrA6u-8Zpt7e7QWSO3ONdVNdUwMltXTesP2saAca9fLDclgp0Tj9LDB39chNZwjL7ai-Nd4DS-Ffoq0fCsuZUSiRFJQFwCVbYZkFfRwfE-ZKeRDkusahw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تجدد اضطرابات الرحلات الجوية فوق الإمارات لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93546" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6a89816f.mp4?token=cMnVNak-ntWXgp_tUDJGnd1oNrCqt9fvBwLoqSyEoVFIa5yRt5_G0dfKl8OBT_SmarkyydPBziR3xDEzLXFzVwcLKMIgXm6oTLL7zYOwpiYM1z08RbpyNTsseyRFfPV-xwv3mxRHCbBHOKFC04PCmDKe-VfNWyl1k-g6lFoX0IKV15x5W0IfSxGzREkGHku6l9gBKw7nibwZZvVFixL9UhZgITjBW46quD_Qnt8JcVDsoWGYMAui3HgbDW4G7fs-CpI2oBsQTroC6gz7ZDjF5S-SaJ_fsJ5dQurOV1crAuPyNiG-7uIrFdHaUHMLmMFzb49os1e2J3kNlHI3LCPcf4JLNgurTci4Ps_Zu0Z5zUat27oUd_2Y4RPy4xuiBstfRKhD49bvE2mQjbE4wQ9ktrIvPh8QnBAOf9LGRDU8goO5VEkQqVHpAHla-Z0vsQXhddQlIoZjPiCQA9SMA5FobcnLqfN5L7Lg5407rtHY9EiBUFII7QkWZX7tFOXt5yfrv-5U_SGM-awrnRipysOQdJqPNRPqvu2kYjvjPubq6mx68oHIr_LVLyfnJXgBoAXYJsye8ucgQ6AWGkMZCi8bSrVWns7OxFrelEwSbgThS_FUNh895r2zX75ZPotTg00aJAaH-mpN7VcKziT3X0hiqodJJK-GBeFxK-8T7Wngb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6a89816f.mp4?token=cMnVNak-ntWXgp_tUDJGnd1oNrCqt9fvBwLoqSyEoVFIa5yRt5_G0dfKl8OBT_SmarkyydPBziR3xDEzLXFzVwcLKMIgXm6oTLL7zYOwpiYM1z08RbpyNTsseyRFfPV-xwv3mxRHCbBHOKFC04PCmDKe-VfNWyl1k-g6lFoX0IKV15x5W0IfSxGzREkGHku6l9gBKw7nibwZZvVFixL9UhZgITjBW46quD_Qnt8JcVDsoWGYMAui3HgbDW4G7fs-CpI2oBsQTroC6gz7ZDjF5S-SaJ_fsJ5dQurOV1crAuPyNiG-7uIrFdHaUHMLmMFzb49os1e2J3kNlHI3LCPcf4JLNgurTci4Ps_Zu0Z5zUat27oUd_2Y4RPy4xuiBstfRKhD49bvE2mQjbE4wQ9ktrIvPh8QnBAOf9LGRDU8goO5VEkQqVHpAHla-Z0vsQXhddQlIoZjPiCQA9SMA5FobcnLqfN5L7Lg5407rtHY9EiBUFII7QkWZX7tFOXt5yfrv-5U_SGM-awrnRipysOQdJqPNRPqvu2kYjvjPubq6mx68oHIr_LVLyfnJXgBoAXYJsye8ucgQ6AWGkMZCi8bSrVWns7OxFrelEwSbgThS_FUNh895r2zX75ZPotTg00aJAaH-mpN7VcKziT3X0hiqodJJK-GBeFxK-8T7Wngb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمير دولة قطر
: انخفضت الإيرادات الإجمالية بنسبة 42٪ في النصف الأول من العام.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93545" target="_blank">📅 17:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93544">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b06ae644.mp4?token=PTwt1RHggurQvoXs2tn2DMQ38KjN63B8sRg4qyffNeG_6vkqg34Nt66YmiSbrMypwX9ewBIUD0pZCm_1hl2bGyUdrxOSrh9P5r2_04P5gtSWFIgi0R3ANUYPjPB6sbcZdl41nVvSRqOhKeYvOMuvio5pqKfDRXRurSqv7z8mZj7Dw-D3h4Zmxjlx0OBWh8w-W3x8jmsxqUgPe-kQfF1HJqizoX3ykCbkQkrZVdp_Z28uya8Jhe4mQKdqDQMmEMAtfsAOYA-EwMUtJxecnQacnV1LBTi2RABd9vpPCpQelDKVEvio2InaXIuhlP_KaCRV1wgubOBLa94KW_zWamSb0WE2Wr-l8xlX0oMhz4ac4bDT9ZGEN5OTLwgR818MVRF1XBKKode8J_LHYDamc1DjKta9NBFrbQTfyv_wUQeIEWq0iWQqNKaBbM7BrmCewQu-DPQpZwYC3XLv4_Qr2iym6YY821jE25oES1EPLumFTcwDmEV5KOMmnyfD3xJziqthsZcuuOuoDfPPZ8h275cNAlbvcNyXX3Ifq7L7Ps6kdE1FqeRA5noIsJPx2K-fwMorsETOHevE_bDVhcsycXFJZyFzEw-8z_TeZU2PtpgRGcqEhuW1DWVDswj8mof7gCmHrBUTsiR74aa8BsTyh_ehDeAzp4NRDgHv0VgrReBlGyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b06ae644.mp4?token=PTwt1RHggurQvoXs2tn2DMQ38KjN63B8sRg4qyffNeG_6vkqg34Nt66YmiSbrMypwX9ewBIUD0pZCm_1hl2bGyUdrxOSrh9P5r2_04P5gtSWFIgi0R3ANUYPjPB6sbcZdl41nVvSRqOhKeYvOMuvio5pqKfDRXRurSqv7z8mZj7Dw-D3h4Zmxjlx0OBWh8w-W3x8jmsxqUgPe-kQfF1HJqizoX3ykCbkQkrZVdp_Z28uya8Jhe4mQKdqDQMmEMAtfsAOYA-EwMUtJxecnQacnV1LBTi2RABd9vpPCpQelDKVEvio2InaXIuhlP_KaCRV1wgubOBLa94KW_zWamSb0WE2Wr-l8xlX0oMhz4ac4bDT9ZGEN5OTLwgR818MVRF1XBKKode8J_LHYDamc1DjKta9NBFrbQTfyv_wUQeIEWq0iWQqNKaBbM7BrmCewQu-DPQpZwYC3XLv4_Qr2iym6YY821jE25oES1EPLumFTcwDmEV5KOMmnyfD3xJziqthsZcuuOuoDfPPZ8h275cNAlbvcNyXX3Ifq7L7Ps6kdE1FqeRA5noIsJPx2K-fwMorsETOHevE_bDVhcsycXFJZyFzEw-8z_TeZU2PtpgRGcqEhuW1DWVDswj8mof7gCmHrBUTsiR74aa8BsTyh_ehDeAzp4NRDgHv0VgrReBlGyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في مداخل تعز</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93544" target="_blank">📅 17:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93543">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be32e104c.mp4?token=PQNEgCUz5sEEUcZewi7AdiTor2J7vj6OF5dr_-eK5viy_3Q18UkflN3-wBsAPuA5Wot9Tc3_RRmEsbxbDJcigqEDoI81H0SRBbPeyLJ3lmMkvLFNnDjUt7iQ8KXADK00Gi7fDt-ezIlVNByhAvCfWWp34l_JP5Aau3-qgyf7aADJRdpE4hLOFCfmSP8Y0MLhP4MGh1n6_orxJSEn5J9YJsJM6BmqlkaVnstcYYLO25gAvJhzHMw1yHufTLZXJVjbJbJBYOiCnHvjY8NPYVNuolC03xGRKTE8q8zcD7EK73y1O-npYw2UFEVeiDWxcnBkDSm7AoKq1QxyzUhmq1eN_lwJDST9NuB1lVBYKODADYTH3Yj9eOSyBq4YsYFYiyHslciBb_TRAww4C1iiG1fXA3xt-WRKyMdyiTncRR2dUq5ESVPjUJZh1K5gf99xnDjX_elOZcCK32iCXFCTgnWx2RuPCDq4V0xif8qrzVGjiIbLmPqBZNxoJHRYujZ58FDcWfOjWkbo3i2J5XNkEbAcf2hEwOpqOPapHoEnWPGnoskIrBWVc3iN2sGew0Nxjn0iiQI5h9y4_B6vW9LWu2FCIt_YHTKAXCAnR6UGc6Iy5UY9Uh2jhn9p_RlWT9LnXhHAMzbqcpyCAvlDn4IdmvzG4bK1ZvOdqMCxDgTkRdiWF68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be32e104c.mp4?token=PQNEgCUz5sEEUcZewi7AdiTor2J7vj6OF5dr_-eK5viy_3Q18UkflN3-wBsAPuA5Wot9Tc3_RRmEsbxbDJcigqEDoI81H0SRBbPeyLJ3lmMkvLFNnDjUt7iQ8KXADK00Gi7fDt-ezIlVNByhAvCfWWp34l_JP5Aau3-qgyf7aADJRdpE4hLOFCfmSP8Y0MLhP4MGh1n6_orxJSEn5J9YJsJM6BmqlkaVnstcYYLO25gAvJhzHMw1yHufTLZXJVjbJbJBYOiCnHvjY8NPYVNuolC03xGRKTE8q8zcD7EK73y1O-npYw2UFEVeiDWxcnBkDSm7AoKq1QxyzUhmq1eN_lwJDST9NuB1lVBYKODADYTH3Yj9eOSyBq4YsYFYiyHslciBb_TRAww4C1iiG1fXA3xt-WRKyMdyiTncRR2dUq5ESVPjUJZh1K5gf99xnDjX_elOZcCK32iCXFCTgnWx2RuPCDq4V0xif8qrzVGjiIbLmPqBZNxoJHRYujZ58FDcWfOjWkbo3i2J5XNkEbAcf2hEwOpqOPapHoEnWPGnoskIrBWVc3iN2sGew0Nxjn0iiQI5h9y4_B6vW9LWu2FCIt_YHTKAXCAnR6UGc6Iy5UY9Uh2jhn9p_RlWT9LnXhHAMzbqcpyCAvlDn4IdmvzG4bK1ZvOdqMCxDgTkRdiWF68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل نقطة الهنجر في المدخل الغربي لمدينة تعز</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93543" target="_blank">📅 17:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93540">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNW5SR9Z6nh7K2r-N36ezJN57HueWfpotub-hLSczGINeRNh1u3EP8EWFvgejJ4kXRsY5CZHGJ9xqETui-YjGWCXDiFzjNWVX-xW-sM24eIYpOYMjVzQZKKHSBcXtTMxrdLC_47ZFQMeATKrwxuROL_OR17RBA_-f3snI-GoXlWw9mTG24Jhg46NrfDoS2czHwyylLZ7gBA82NnIf9bvloXhmUKbfLV0vDbbG_QTL_LzjjXYbKd1utoufNsz44LoSnvjNAnYXYjGJ24AvVHvfPWmh8leV5rQKArM02di66AmSOp81-NiZLEv4HjRuC_fuFPc5YM32LID2dGsioEYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk1Dz2UYHIUySHFw5eIwjQoYJAj8tIL2doyCVoCxhyM5bsjB9yA4cPUL6sYmHN8fBL4xrWOUQqyk1w6JxtrILEO7lCPNCG6qZ49n0RRxy8kBbXjX3IAdraE6ET_z2evdq1mslchPqPR-C0bi8Ns4acgQTTl7gEVx_lnRDycFhqVZoQJpqI5seGdKVFhOYVcDK_LcnybPU3GRo7Zl71ibmHjsscGSQy3bxBun4QCSWXxIo0nyKGlM9lVj8eK_Yt2Z0F-gC1ro2HdAHVg0pybRY2b5fuFzSzkE4NITLlN8zxnR2qLJkZ6IJSRJufp6HJiEmCgIhY922yQiqs6gSV1NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS4kbZD9u6K-pXqYHfqLPH3CVpwB6swSPqkRIIrkA6HLAwkXF0Gu8bW3di-P8XRpWpjRaHPbl92_YoNHI8eepmbQN_da0G7nH4UMZC_TnewbMNDhmoTD27jSEOeGjpLd5rjxVaCIDP1rOQSjDSLTTzmdJ3LXOLFkSQrVow7G4msCD6Zb2JWIRzBvTOUir8y93DHRvA6FMEpokoet7y5ai9ILTytFD4l80b-M_HgYZydYiEV2cw8yNsa6V0OaBq2_bvXbhg6r-Cj3WTF_SNgOzsv8pSX8Rr91UNgFM42p6ltT4zbOpPoZD2ASa2-nRvC989Mjd-nBJpDdexkkIkKXgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل نقطة الهنجر في المدخل الغربي لمدينة تعز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93540" target="_blank">📅 16:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93539">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
نايا تدعو جميع المصابين بأمراض تنفسية في السعودية والدول المجاورة إلى اتخاذ أقصى درجات الاحتياط خلال الليلة مع توقعات بتصاعد كثيف للدخان ما قد يؤدي إلى تفاقم الأعراض التنفسية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93539" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تهيب القوات المسلحة اليمنية بجميع المواطنين بالإخلاء الفوري والابتعاد عن الأهداف التى ستقوم قواتنا المسلحة باستهدافها في حال أقدم العدو السعودي على استهداف ما أعلن عنه في العاصمة صنعاء
مقر شركة أرامكو في الدمام
مطار خالد في الرياض
مصفاة الرياض التابعة لشركة أرامكو</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93538" target="_blank">📅 16:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد من استهداف تحشيدات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93537" target="_blank">📅 16:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
🇾🇪
العميد يحيى سريع:
القوات المسلحة اليمنية تجدد تحذيرها لجميع الموظفين من الخبراء والمهندسين والعمال في جميع المنشآت النفطية السعودية من التواجد في الأماكن التي تمثل أهدافا لقواتنا حتى لا يعرضوا حياتهم للخطر سواء التي تم استهدافُها من قبل أو غيرها كما تجدد تحذيرها لشركات الملاحة الجوية في المجالات والمطارات والمسافرين والعاملين فيها التي تم الإعلان عنها سابقا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93536" target="_blank">📅 16:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
اعتقال وكيل وزارة الصناعة والمعادن العراقية ناصر كاظم جبر متلبسا بالرشوة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93535" target="_blank">📅 16:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93534" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93534" target="_blank">📅 16:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع: القوات المسلحة اليمنية تحذر جميع الموظفين والمواطنين المتواجدين قرب أي منشئة تابعة لأرامكو النفطية بإخلائها والابتعاد عنها كونها هدفاً مشروعا لقواتنا.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93533" target="_blank">📅 16:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع:
القوات المسلحة اليمنية تحذر جميع الموظفين والمواطنين المتواجدين قرب أي منشئة تابعة لأرامكو النفطية بإخلائها والابتعاد عنها كونها هدفاً مشروعا لقواتنا.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93532" target="_blank">📅 16:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هل يستطيع السعودي الذي تمثل الطاقة عصب اقتصاده تحمّل كلفة هذه المغامرة؟</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93531" target="_blank">📅 16:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">المحطات بالمحطات</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93530" target="_blank">📅 16:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">النظام السعودي: ‏نطلب إخلاء موقع شركة النفط اليمنية / محطة الصباحة المركزية بصنعاء بحسب الخارطة التوضيحية للموقع.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93529" target="_blank">📅 15:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHFAU71JTH_1Q8UBNdmU0ooz6nYSNRZlOuAjj6IL6YKvqa9N9w96Prs559oDHDMPvkOqh7fi2RPHKyskDbIGbPKpXPY-TBWtDXa8bZNYh59pqZPp2cPn3ZaMgiSstAAhPJzSshFPYHwuIkjD74eieganJqpmeH7DaJZIdq_1_yg5Qml7lbwta1LclYkvTUlieEgWwZiVks4HhfHCikVrOvW-trdvctUacGy_nJXvPAJtlP2KUyyhKdY2r7DIUS3Hgdk3jkb__Jio_OHOdNUdJCRiq3gC1ix8xUBBu3Gyb27Ca1DBwWJGGtNtnyo5_sWDt6X3HqyMJZ3Oa1BC8a8EEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي: ‏نطلب إخلاء موقع شركة النفط اليمنية / محطة الصباحة المركزية بصنعاء بحسب الخارطة التوضيحية للموقع.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93528" target="_blank">📅 15:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني: سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93527" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏مدير جهاز الاستخبارات الداخلية البريطاني: إيران تسعى لاستهداف مواقع كالمنشآت العسكرية ببريطانيا وخارجها</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93526" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني:
سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93525" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي الانفجارات بوضوح في شمال الرياض</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93524" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">في خبر غير مهم
🇪🇬
وزير الخارجية المصري بدر عبدالعاطي: كل ما ستطلبه السعودية سنلبيه.. ومستعدون لتقديم كل أشكال الدعم للمملكة بما في ذلك الدعم العسكري</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93523" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">في خبر غير مهم
🇪🇬
وزير الخارجية المصري بدر عبدالعاطي: كل ما ستطلبه السعودية سنلبيه.. ومستعدون لتقديم كل أشكال الدعم للمملكة بما في ذلك الدعم العسكري</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93522" target="_blank">📅 15:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هجوم بالمسيرات يستهدف الرياض</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93521" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93520" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93519" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مستشار الامن القومي العراقي:
400 سوري نُقلوا مع المعتقلين إلى العراق لم تَثبُت إدانتهم، وسلّمنا 50 منهم إلى بلادهم. البقية سيتم تسليمهم إلى سوريا على وجبات</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93518" target="_blank">📅 14:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9852db7c9.mp4?token=sXM3SiWdPP1hhcNXPUX3PxqJbh3GXZ304vUW95zyKvADtqsiX17zNsC2TrKTCeVcX2N52JacI0hqMH2NiC3gDI9BtbC1Svzkj3Wa3yna5lOb4CD1zdSraJMIpfADJOncGMigvVZMI0dUvfCrxbkznqzCQ4rzt_1uB7cDT79QxO5V3l-7Z3QM1oOeShqGI9fbS5zTfAynz8jnfhQzTVa25D4k5Jp74-N113iQvx2lDOSY7ZrTxn9Uh-XxBlNFS7V5SEV5cwxewQW9kzi0ntQp5Cbol6lqT0ZtGFUAlnm51wShRYhgRKSyXdmnocJHizYA6lP4ORH4oDuPT4aLnECYhCtgD4ydR82CUtcirBVgs7_Ci_yjJwdJ1MtCn59HBFrCUMMy0gX9h4Vv-g6DvDPtGRhHe6CdDGbHsZgRorhSd7nfTU4jBOKdHeov-mmKZnCxKx9NxEJCaRikZ5jyOJ_QnGLYVFtvFyaI6WydvnMRemk_i4s5byverHcOpWV1Zqe0kpFuwOSA9mnj7tdacHOZiFkDxnfDXTv1wdRYh6Qfhe-gpQQwHb_sK2-bS7ez4q32J7D8H8yXWCKQVLoT5D3CY1miYdyX5Ucj6Pk4Bqu5SXTQEJjTE_ggkS29XsEHp8UBpyNpSQJ-FKSr5uUS5g7IhhiKBraxxLJR5c5VAYNjRiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9852db7c9.mp4?token=sXM3SiWdPP1hhcNXPUX3PxqJbh3GXZ304vUW95zyKvADtqsiX17zNsC2TrKTCeVcX2N52JacI0hqMH2NiC3gDI9BtbC1Svzkj3Wa3yna5lOb4CD1zdSraJMIpfADJOncGMigvVZMI0dUvfCrxbkznqzCQ4rzt_1uB7cDT79QxO5V3l-7Z3QM1oOeShqGI9fbS5zTfAynz8jnfhQzTVa25D4k5Jp74-N113iQvx2lDOSY7ZrTxn9Uh-XxBlNFS7V5SEV5cwxewQW9kzi0ntQp5Cbol6lqT0ZtGFUAlnm51wShRYhgRKSyXdmnocJHizYA6lP4ORH4oDuPT4aLnECYhCtgD4ydR82CUtcirBVgs7_Ci_yjJwdJ1MtCn59HBFrCUMMy0gX9h4Vv-g6DvDPtGRhHe6CdDGbHsZgRorhSd7nfTU4jBOKdHeov-mmKZnCxKx9NxEJCaRikZ5jyOJ_QnGLYVFtvFyaI6WydvnMRemk_i4s5byverHcOpWV1Zqe0kpFuwOSA9mnj7tdacHOZiFkDxnfDXTv1wdRYh6Qfhe-gpQQwHb_sK2-bS7ez4q32J7D8H8yXWCKQVLoT5D3CY1miYdyX5Ucj6Pk4Bqu5SXTQEJjTE_ggkS29XsEHp8UBpyNpSQJ-FKSr5uUS5g7IhhiKBraxxLJR5c5VAYNjRiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تطل على مسقط رأس القيادي المرتزق حمدي شكري ومحمود الصبيحي ومسافات قصيرة تفصلها من البحر العربي وراس العارة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93517" target="_blank">📅 14:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93513">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLUoVA-gRAHus67GcJV9WzPI3xpHsucczFwncPM1unxU2RAZQ5CDvR6uytBeJ7scC8LYagziHepD6r3GLA20jfDvTnG5mzwiR5g-YRAobzyROmtFtS4_AmLLOC5eoWQTUWCccNgsr9rGmI42YKww8mn_onyKVwwK7Khg9_wJdpoBDzBr2QKJel40OuahkdKaclW_JK8D91j9VXrhhggC7sf7oGHy5gTBEX6teNyOEm_wlAvLygeynhorHRt1ZWrWWEMfAQQz-mOao6mY7MjN7bl1T9PcRoNkLWI2U0vFmgKZmsRWARHJS2qHRqN5l3Uq8qMkCUVaY-avPpkjG2NyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM1dpo1hbgt7C8Jpui0Slz6oFkCCErPx0bzQ2cUNWF776JxQ2-n0DvwWfhB9uFMfSQ8aCzTkmjOI9FYC3KrLBvQyHHEN4sAnN35I_k8qi6ThKmV7clDx0gKuxvaLfLtynjmkWnPNO65RXfKF-NSCYU4c2Z05k22UleAq2ema87V1zvb18QBN8yQ2U-7NBWZe1AoOryZzn2wMW5Hrm8jGVzu4tkG2FjDW1yjdxygI3nrccUMGuAOIcdzHJx8A_543XxtYBGDzAI_o8StZ5esUGdnsbwHCuP3iTw7sVhASX011Rfsuhf4Toxgc3DYBbxTWrc-ZkxadopFOKmaE5h5exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dP_naNevYK18jLwSTF5n43okPHg-qV04cHKaAjqHXvgVb6u2OKkvaUPjsgEi-2-sJkIRyjXkNtt9VjxiR5pK7TbGIY7LZiu1MarOUzbZzgS5y850hvDkJ0ZrB0GoOQ1RfSu73XhGZkDEnmQBdNi6odjoaG4rE14OpxzfeoY4whFJLImOn87GfI20y5qPYwsE0Vdw6XgQmqber6OONcS_EY6ptKHM-WHwN4ELlxKtWu3Z7PnbgghvWb3ORKMvfIlPG616iLr87Norh0WQlyWEhexQvo13UseBBjOkDT9lYfHiaFto2SIJhT2yyZCLRvjhDPK3z6QAEuCVQcBBhHJy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o94CSXejfxaO23ccqG7RjXg-PMsFCHvDZiAvSYa3sDnRFigmUZI9SIdeVQ5ztq_1ByjV5dPWS0yH-m-XgHTSOYQRApf96NkZQCdpJD3tSVQPA4aUg2wt9ifl32Z5IlGfBvEe7Ju_EOOiJ0KCjWEdoPUk9p-MvvfPT65oKPgFJcBMeeQtqvott9nAjlQakMPdA4YAEgv_OSu1tNqGu791ANotTGiO1ri_1wXEnZeykf0Ilp0eGMzRoqZcuEdrSNTMFkmy6TlqCl1AxhcbPvv3fXw19Dg_KUaGIXWvajBQ_s4Fbwvx4Ak7weiPRclCKecveVbAElKmDabk6ltMMJfCDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النظام السعودي يغير صوت الانذار ويطلب من المواطنين تحديث هواتفهم
اريد الرنة مال مراد ترن ترن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93513" target="_blank">📅 13:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93512">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d12152172.mp4?token=Av3dapeq7iUlKKVj04HeSaeJVxfm75Xq3rxO9ckSXyWKsxnWyzcB3xKtfMwaQFNMY3zI16M81dCyPAX7mCWMXVn61EeCyxRWNmZCF9kVwvMsTpzB2KAIOMVTvPaHSxfH8Wart-JdtYST6krWsrPDebFvRTaU1JG4O8YtbN9yvrcrav1Tv_rhlrucF76TQdWYvwUKTvLGXsEAceAUp0nGg7dWK24TwAnG2rFugjkqle3tyxU_iosv3VAG5ibQ_Ymm8YkVaLK0ANo5-i5SAjHwGJsRETBj2muZ9KM1ncaUpv9duUWXd73Kci4G5J2AyEOQ3Hu6tAIe5HvyKwqXov3qVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d12152172.mp4?token=Av3dapeq7iUlKKVj04HeSaeJVxfm75Xq3rxO9ckSXyWKsxnWyzcB3xKtfMwaQFNMY3zI16M81dCyPAX7mCWMXVn61EeCyxRWNmZCF9kVwvMsTpzB2KAIOMVTvPaHSxfH8Wart-JdtYST6krWsrPDebFvRTaU1JG4O8YtbN9yvrcrav1Tv_rhlrucF76TQdWYvwUKTvLGXsEAceAUp0nGg7dWK24TwAnG2rFugjkqle3tyxU_iosv3VAG5ibQ_Ymm8YkVaLK0ANo5-i5SAjHwGJsRETBj2muZ9KM1ncaUpv9duUWXd73Kci4G5J2AyEOQ3Hu6tAIe5HvyKwqXov3qVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
یا علي مدد ..
@Naya_Press</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93512" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لحظة الهجوم الصاروخي اليمني يوم امس على العاصمة السعودية الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/93511" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGgtgnFafiwsF-owbJ3tIwjtUSv2Q7a8E5iXQCzm20akiMETtQmigY6ESeP4LkrUaRLV0ZT9Ur17UiOduC2uVnbhMFm-jm93wO7FBf9GHp3NjgfOZfx54QwK3K6Hiuu6VdXOhExI-kC_9t61k9qY8AhFJYDNOiLXpUl0-zhGgQNE5nhfFvQgusti-Ka0VwPBq9BBde8kEGgeWVC5czQuYgheU8h1hUz_9zGfU-u9qVwY-qfBA7MDxfNf_-XnY6nmdyEnNUHOAjaWDB_8JHP0AhLAKloNWVq3B9A4wOA31FDF4_HoAMGMoRLcTZMBzCui01OEUQRzAcq1b6HanVOQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtVbbiE3Ve9_QdgCbIckJY3GA5uckjwlsOp9Cvl3UPBaDKcs0oPiIa47Q3D2oQ1yHEbB7oUuizYsL5_ouSroXAjPPmxx8o6FdyoPZQkgawWyg4YsxW01Pq1ENBIpgm-mu9b-V8tJnadil5h3vseZksWEWMVSO4j3f6kwSE_N7p5Bdb-o55TOfkN5SRYvL6L9am7fLCfWLv1meqBqGRVLbDJn5yTZqXqWzdYqcZaUJsr73XmdzqLxvn67RKfrc5hzUdRklBeUos3v2RB7p87SGSjLg0LLJ8Cc6Ts4sO4Ph2n5npdZm9xqCohZN_rEopLrdKz1QrpNSA3VlUVj8AO6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اضطرابات في الرحلات الجوية فوق دبي  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93509" target="_blank">📅 13:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اضطرابات في الرحلات الجوية فوق دبي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93508" target="_blank">📅 13:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bf372211.mp4?token=FW4eJRc-h-hgfvuJoCgee9-SDt5MCtw5pbItIatb7pD6f7KtHoTRdi3sl6aUNl_zJVJAJL_oZ1Y2jpaF9ohuCUmRnmcjAbslTR9FrRMhOIYRCx2uvkjoJtRgCOZaIZQ3GQC1mnYz3RFzeOGNOMNKap-iIEIEMTPoqDD9dTlLZneAxsRMoUxqU9HpGSli-zdUDj4upUdqOL0P6FObPT69PEmU3h1t155lgpu6bC-D_oGFelsasps9MgmGR5fKwSfBR0xCeL-CB0o7lfUWOBzqDOEl1KoisV4LmBS6PZDS_v0PaDWTx53gVgdHrAO9OlRRnXGTz_BwdCEMKWBfyLvXC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bf372211.mp4?token=FW4eJRc-h-hgfvuJoCgee9-SDt5MCtw5pbItIatb7pD6f7KtHoTRdi3sl6aUNl_zJVJAJL_oZ1Y2jpaF9ohuCUmRnmcjAbslTR9FrRMhOIYRCx2uvkjoJtRgCOZaIZQ3GQC1mnYz3RFzeOGNOMNKap-iIEIEMTPoqDD9dTlLZneAxsRMoUxqU9HpGSli-zdUDj4upUdqOL0P6FObPT69PEmU3h1t155lgpu6bC-D_oGFelsasps9MgmGR5fKwSfBR0xCeL-CB0o7lfUWOBzqDOEl1KoisV4LmBS6PZDS_v0PaDWTx53gVgdHrAO9OlRRnXGTz_BwdCEMKWBfyLvXC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعطل الرحلات الجوية في مطار جدة السعودي بسبب ضربات القوات المسلحة اليمنية وضمن معادلة المطار بالمطار لحين فك الحصار
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93507" target="_blank">📅 13:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
إيران وعمان توصلتا لتفاهم بشأن تحديد مسار مؤقت للملاحة والتفاصيل التنفيذية قيد المتابعة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93506" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
الكرملين:
العقوبات الأوروبية الجديدة على موارد الطاقة الروسية قد تعرقل التوصل إلى اتفاق بين موسكو وواشنطن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93505" target="_blank">📅 13:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a154d4b9e6.mp4?token=D9KJ9OBcY_QCE-H3QzEWCnFEyQtCUwPP1tlBeQqFyfNNBqnRU0SKQUrn8_L1F-78Y7UZN6a01wh3izqiBLebTfsK2PaCFoxMYrY2CmRH40xdTSzY4050CfhVrmjLbQdHPirNCoku0YFn-t2_Pgk49tV_J9PeUR4HvDX_CgynMnT5vEhEitDsxZO-F74MkGvLOzU3W0naRi5wN73zB_LdOmiIVSnuWFQL1pzXiZfJz5DmrvVK4HZyXYUteafad1zXVgM5E6LQaNyt2vnjfdHbD2PLmn_pXNAFsHv94dBc0ij5jaAdmU2ukpp21BrUwbpH4h0dh_tw-SFdD4uobkQk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a154d4b9e6.mp4?token=D9KJ9OBcY_QCE-H3QzEWCnFEyQtCUwPP1tlBeQqFyfNNBqnRU0SKQUrn8_L1F-78Y7UZN6a01wh3izqiBLebTfsK2PaCFoxMYrY2CmRH40xdTSzY4050CfhVrmjLbQdHPirNCoku0YFn-t2_Pgk49tV_J9PeUR4HvDX_CgynMnT5vEhEitDsxZO-F74MkGvLOzU3W0naRi5wN73zB_LdOmiIVSnuWFQL1pzXiZfJz5DmrvVK4HZyXYUteafad1zXVgM5E6LQaNyt2vnjfdHbD2PLmn_pXNAFsHv94dBc0ij5jaAdmU2ukpp21BrUwbpH4h0dh_tw-SFdD4uobkQk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
القوات الجوية نفذت ضربة استهدفت بقايا عصابات داعsh الإرهابية في قاطع عمليات ديالى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93504" target="_blank">📅 13:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-iWKOBkxtTZEaRedwUUbvIgYsz7RZqIeUxuitaIpIHEELJdCvAGkTtYCNvirFGXgGes4-wkuhuc_MS4Y4GPIpzcAJtZygI1TksTtYMwZJ4EbzDtuSlgOMG3WUkbUd4U1VT6-TmhpHVUgZ_Gufp5_uvI3qsNuh5vaQrB7xx3m_QClshFDZ6jhALWhxvlmoT5GznpPYDX2xHf1Fi5XoebYHAVLF9TImD8Vnf3SGdVupRMEvVgDDT_ZO4Sc3GGAQ2tFSy-k1aqdO10jxCMCTYrppZyZ6qFcK9KwqS8d3DL8SO1pG_H0cdcdpr4mPvQqPtqQ3q8jfplE4fWh8ovdoeQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا
بعد أن أطلقت وزارة التربية العراقية التقديم الإلكتروني للإنتساب وأعلنت عن مبالغ أجور الإشتراك السنوي في المدرسة الإلكترونية، الطلبة يطالبون بأن يكون الإنتساب مجاني بظل الظروف الإقتصادية والمعيشية الصعبة للعوائل العراقية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93503" target="_blank">📅 12:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olW9nFY3aJdycpyjRtFGoOuIl5VXPq_VE6g3qVq61OIZgNKpFMHU6ug_4DHEevk8cq8A3jM8Qk8XqC5uO6YUAXNL-ckEWuMFaTlGbWLJOwZz7nIt4GzTZozJASLtys7igZ4TUhbQdSsuFO8ZZEOhfcL5CV_ZV3T65g38D1OByUbfpOPpKedf14bmIKEQEvNvOIBUTZB9W6AHtuIgw21QVMzs0bRZZ20G4SR9H-PdNiN7Xa6Mb5X_NMPnW9PW9qVZi61S8bY6FNOZUnoJbnOEdPRl2SAb7gHWW_S6zQ8y8nvvT__jZjdS_hGuVxvj02ec9RICIcgtI8oo_QH4KhWu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا سيادة ومعتقلينا بالسجون
الحرية لابطال المقاومة ؛ ابناء الشهيد ابو مهدي المهندس
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93502" target="_blank">📅 12:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15614c3890.mp4?token=GW22stDJpTALnxTlqwPGdJ9a05QhL4Mno8ySfFfk11e33J07crFHYRzWttUeEoNwk2ZKgEnWeqH8gXaDpHGaCf9NWsgvwitKrYiwPhwiHcEB34dTFUvjIfSRCnauIx3TStNugI4ilE_IopcR8p4XaJiyEoRTg87P8ZMCb4y-60ZXJgMVarUrQN6gh_KgyK9DstQ6yNXGsLnDq_6o2asZSU7RBt84z9LrYL6S7ei2HBQ_I18p2zTJSqUXwCB9Up3HSjutjlBXue8_lm_egEWqrtcdtUWhtnFfzsIyA1Y14DcJqbLVXgfVPBP_wJXttbB4Mqwy90IB1BNTTwUKjweSkFb2wsKArcw1KECA9L9cIqXqn2NaXtQdb7pLi72nGoXUEOJanzWsJrZurX3yfbh9DU1SGEYfxZA-qKc2YPg24LKkhd_JHZFSt81Te_RfV0UbKMg5v_WnHm2OZtQL56UrPRs-c4f-uHuSMwCKqMZK0ZBW7Qgnm6f7zTk2XHcd55jSFwqfDvGZPUbyaTwQcyBCoavenw4hP4cZWIApZyqod84rf_2LYV7TMsVosMitocasq2zRlCvl7jtTifPyNMQaZkfhK-XpXbIwncih4pWUoQBPiymoAJznPQ8dfOWTYrsCd-bNsE8PPfEEZ3llhxtbTfKyGctCwF_V_4ojaiA8a4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15614c3890.mp4?token=GW22stDJpTALnxTlqwPGdJ9a05QhL4Mno8ySfFfk11e33J07crFHYRzWttUeEoNwk2ZKgEnWeqH8gXaDpHGaCf9NWsgvwitKrYiwPhwiHcEB34dTFUvjIfSRCnauIx3TStNugI4ilE_IopcR8p4XaJiyEoRTg87P8ZMCb4y-60ZXJgMVarUrQN6gh_KgyK9DstQ6yNXGsLnDq_6o2asZSU7RBt84z9LrYL6S7ei2HBQ_I18p2zTJSqUXwCB9Up3HSjutjlBXue8_lm_egEWqrtcdtUWhtnFfzsIyA1Y14DcJqbLVXgfVPBP_wJXttbB4Mqwy90IB1BNTTwUKjweSkFb2wsKArcw1KECA9L9cIqXqn2NaXtQdb7pLi72nGoXUEOJanzWsJrZurX3yfbh9DU1SGEYfxZA-qKc2YPg24LKkhd_JHZFSt81Te_RfV0UbKMg5v_WnHm2OZtQL56UrPRs-c4f-uHuSMwCKqMZK0ZBW7Qgnm6f7zTk2XHcd55jSFwqfDvGZPUbyaTwQcyBCoavenw4hP4cZWIApZyqod84rf_2LYV7TMsVosMitocasq2zRlCvl7jtTifPyNMQaZkfhK-XpXbIwncih4pWUoQBPiymoAJznPQ8dfOWTYrsCd-bNsE8PPfEEZ3llhxtbTfKyGctCwF_V_4ojaiA8a4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف مباشر من قبل القوات المسلحة اليمنية للمرتزقة في مديرية الوازعية بمحافظة تعز أثناء تواجد الإعلام السعودي، ماأدى الى فرارهم من المكان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93501" target="_blank">📅 11:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711d7fd6a7.mp4?token=oDiITNpmhCEQp939ncNygRZlgrNrE5xl_rkQ71Q85QknOGCTq2tv1Enc_BmjQynN1hoZrvVNwC0LAC2JCe7BexuGtPYrY1Eg9CHQeGh5IvbNKRX56W44eZpK5eXjaeHj71ZwTGnxo3VlfuStiOOJCzYU83C6dVFF7FLA65Z0csodgpx-2ucpCvm8LGXnhWf9QHn5jqjZ8E6GO4Fzj-iDB6qqnlreGroqMswlgYX3KDsIzmEAZqpvyBInanLwBV9SKuo62DFkkjbBaKBldY7YOc70gARf_GNhWM4lqXV75DnrULM1rRvBVPau2YXojj4dqHUCFdIvz2NRmyx1i-g51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711d7fd6a7.mp4?token=oDiITNpmhCEQp939ncNygRZlgrNrE5xl_rkQ71Q85QknOGCTq2tv1Enc_BmjQynN1hoZrvVNwC0LAC2JCe7BexuGtPYrY1Eg9CHQeGh5IvbNKRX56W44eZpK5eXjaeHj71ZwTGnxo3VlfuStiOOJCzYU83C6dVFF7FLA65Z0csodgpx-2ucpCvm8LGXnhWf9QHn5jqjZ8E6GO4Fzj-iDB6qqnlreGroqMswlgYX3KDsIzmEAZqpvyBInanLwBV9SKuo62DFkkjbBaKBldY7YOc70gARf_GNhWM4lqXV75DnrULM1rRvBVPau2YXojj4dqHUCFdIvz2NRmyx1i-g51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الأمنية تستخدم خراطيم المياه لتفريق المتظاهرين من جرحى الحشد الشعبي المطالبين بحقوقهم وسط العاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93500" target="_blank">📅 11:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8ebaf541.mp4?token=sJaZ4TjI12ndUnzYbsJVxDdRJjmyIMbS6M4I8MAfpa3XwCYqitGkhW54fqKktxy7w99JBizz6CKmBYq2ekJbuKrEhH6LW-cxCXFOOVJB_sbxSzVNrSmYoOZuHzjhR6GgV9VaN4yx8S117bHrihw_axtWzuMJSj9qiFIk9xGmidnrUR71gn6jrmeclILBpqJZ_iMZiSl9ai8AJ4eX8M1xuRmCUhC4OWZ2H4SPAwAee18Ru9jqCbVcy2_G6EHndjALZnE5KmrPNFF9VgC1DDnLDwZwrb4t5C3B04xqAMODQAplo2G5h4GIAGKISunon_PKXZLBOFEI6UMCoEKW-vI6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8ebaf541.mp4?token=sJaZ4TjI12ndUnzYbsJVxDdRJjmyIMbS6M4I8MAfpa3XwCYqitGkhW54fqKktxy7w99JBizz6CKmBYq2ekJbuKrEhH6LW-cxCXFOOVJB_sbxSzVNrSmYoOZuHzjhR6GgV9VaN4yx8S117bHrihw_axtWzuMJSj9qiFIk9xGmidnrUR71gn6jrmeclILBpqJZ_iMZiSl9ai8AJ4eX8M1xuRmCUhC4OWZ2H4SPAwAee18Ru9jqCbVcy2_G6EHndjALZnE5KmrPNFF9VgC1DDnLDwZwrb4t5C3B04xqAMODQAplo2G5h4GIAGKISunon_PKXZLBOFEI6UMCoEKW-vI6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لليوم الثالث على التوالي..
استمرار المناورات الصاروخية الإيرانية في عدة مدن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93499" target="_blank">📅 11:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
مصدر امني عراقي لنايا
تغير بحركة القطعات العسكرية بالعاصمة بغداد حيث سوف يتم نقل الفرقة 17 جيش عراقي إلى كركوك و توجه قيادة وألوية الشرطة الاتحادية من كركوك إلى بغداد ، قاطع عمليات الفرقة ١٧ هو حاليا جنوب العاصمة بغداد يشمل المحمودية واليوسفية و مقتربات الـ دورة .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93498" target="_blank">📅 11:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93496">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDbmmKmg066Qr8CTE41q0d7IjZjW4rsP-YHTyaaLDRwcane-CPhPN1wsIFLzI-v-Drq4P3znomlzygHjPZentV9AJgAlhXe9oFTqgAtwNwqghmw5nbI13vZGPYoVNmT6c2zCMFXQ3V6V1BmRHiecbLitlpzPrZ5v8NA1sNE8itPRLbA0DkJfsXqIXo1NXN2OZRZLCusYw5ISMuRmlPoI-8C7E9sLQjEZv862fZBxxYbgrqRpVJTD9Uf6kiriCgOQniG5FEey5kNep5mRnaGwrOFlQWYfbyr_MLirBi6P1DtgSAmgMfEQg6so599Jog50pJKFKZfLtW10wKytYZ4kIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
السيد مقتدى الصدر مغرداً بخصوص منع إرتداء الحجاب والمظاهر الإسلامية في دولة أذربيجان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93496" target="_blank">📅 11:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93495">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
🇮🇷
🇷🇺
🇰🇼
On July 20, Naya’s Telegram
channel published a warning about an existential threat posed by a potential Iranian military ground invasion of Kuwait. At the time, a pathetic and failed Russian English-language channel came out to respond to Naya, gclaiming that such a scenario was impossible because there is no land border between Iran and Kuwait.
Today, the American newspaper
The Wall Street Journal
published an article mentioning Iran’s threat to invade Gulf countries if aggression against Iran resumes.
Here at Naya, we do not write without reason. I am Naya, and I know all the secrets behind the scenes.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/93495" target="_blank">📅 10:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الامنية الإيرانية وعناصر إرهابية في منطقة تفتان بمحافظة بلوشستان جنوب شرق إيران؛ مقتل عدد من الإرهابيين كحصيلة أولية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93494" target="_blank">📅 10:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93493">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a00c4573.mp4?token=c9fOR23pskatBZae10r0XOCM6_AQWGnVrWPx5XKFud0QLXX-j9E2EKtPdRMqkWZBGZsTFhxXS8hLTJPoe9DJqm8KX8EkUIFHVEq-yGod9DWbj0aKVPn0-0oEvEQqGX2Bd3_6L5VTosL0kaZN8crLcELAmhtNk9v2mbKcHbq7CZfxIv4yNgH0JcAdlA1lUuOMHPWA5fo1sALQmqUmKmxVUi6Pg4J3kZuKfVaOAcf9glEYjXqMkN_sQtc_pG5i0Gue9Zdxs9CFQN5waMUeIL0IpJeZ8jaPk4ZNEWbvTTJtbOhP7Tz8GzVdisMe6xR2RBgmZz9vn8deq7bg0bsPLNRFUmhyyKSKiYiIPRMa306BZeVoRtIuMzpodRudsWgqwPTRLvWrecKEzytNGJWAl5ReSC2lw0YCPPZ6TT4O3gbXq7u7wU6khQPeDnUYoLX2C7JxGvpX-nmJPRVqhO5Vsi92ESzS8d8hgAUsbl1txYP8rtYlSB4h8F2ed0L3zm3gO4HtQ9-jWD3kfUN2k8v7odsFWxIID04fljTmTiFGj5a8-nGYs1aiCLyKZVBIVarVeJ5JaVWq0yeIiXQDlPFzTrLPQocBe18H7nOPzlJQlWWM3qRfM4KBe18g87GMLbnYzrqbGn62FANwz5N0Eg7qzTDnJFsp0zlMtT1HFLu03b-KJPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a00c4573.mp4?token=c9fOR23pskatBZae10r0XOCM6_AQWGnVrWPx5XKFud0QLXX-j9E2EKtPdRMqkWZBGZsTFhxXS8hLTJPoe9DJqm8KX8EkUIFHVEq-yGod9DWbj0aKVPn0-0oEvEQqGX2Bd3_6L5VTosL0kaZN8crLcELAmhtNk9v2mbKcHbq7CZfxIv4yNgH0JcAdlA1lUuOMHPWA5fo1sALQmqUmKmxVUi6Pg4J3kZuKfVaOAcf9glEYjXqMkN_sQtc_pG5i0Gue9Zdxs9CFQN5waMUeIL0IpJeZ8jaPk4ZNEWbvTTJtbOhP7Tz8GzVdisMe6xR2RBgmZz9vn8deq7bg0bsPLNRFUmhyyKSKiYiIPRMa306BZeVoRtIuMzpodRudsWgqwPTRLvWrecKEzytNGJWAl5ReSC2lw0YCPPZ6TT4O3gbXq7u7wU6khQPeDnUYoLX2C7JxGvpX-nmJPRVqhO5Vsi92ESzS8d8hgAUsbl1txYP8rtYlSB4h8F2ed0L3zm3gO4HtQ9-jWD3kfUN2k8v7odsFWxIID04fljTmTiFGj5a8-nGYs1aiCLyKZVBIVarVeJ5JaVWq0yeIiXQDlPFzTrLPQocBe18H7nOPzlJQlWWM3qRfM4KBe18g87GMLbnYzrqbGn62FANwz5N0Eg7qzTDnJFsp0zlMtT1HFLu03b-KJPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
أمير دولة قطر:
إغلاق مضيق هرمز والأضرار في راس لفان أديا إلى تعطل مهم من صادرات الدولة.
تؤمن قطر نحو خمس تجارة الغاز الطبيعي المسال في العالم وما يمسها ينعكس على الأسواق والمستهلكين.
قطر تعرضت لاعتداء على أراضيها من جانب إيران في انتهاك صارخ لسيادتها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93493" target="_blank">📅 09:46 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
