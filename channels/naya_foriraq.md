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
<img src="https://cdn4.telesco.pe/file/s_eoxiJp--qJNHzDngtVVa_VYLSaiLtqTANDTTZTaIf269bt4pxV7aGtUkGLbYu0TOZwtcQ1yuSCvJewufIp9GogdzjABTC1QYUKbdhmSVWkvJbfcddKl5NDzhpK-NeVZBsvxwqnKASvCS1jLeXLuuxoddxiolPwd-090JhKQLm6-l64OvsqqOwQlGfyG0GguuPP_muoHf-xeVVMXnaNjY2Mq8zqrdNkrJHiYBPHKQmGut3qkFXsw6vKHNh7mNGMjcfJwZBRHiZyxBaFRFJsueYYo4kt1c6cSIu14QONwkU8BQizeszEmXeD-NyxyAXGV5S6WS5Uf-22TbdCmXiF4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 21:22:25</div>
<hr>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/naya_foriraq/79421" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQEXLpy9XoynKDncRG4c3qTXIOXUUieUTD22KhqurR5hEg2GqmIZXInJC7LA3y9Knwy_OMMHsilbmKilBl8_tn8RIvzyBkNUFt40ZubSFARbKBDSeKbPbn4CCrwDF-0UIK0ZqrDABaYlUIraZzTzcJ3RGo07vDRMKUL4Lhc3u8EvAwsRwoygh93_Z0AuciVmkMCCeydcKw1nwUpiLIso_gEDMk-3_v3VpvhBsVcIulgSqIrKxwDt5s7IoVtvFti5rU51awJ4L79-RxlijY5G0yVeGnWVHm-7Fx4ZNhMYc9OleBvQ5jWc0M5VH5LTVB5xzc1iPWbjiq1drSaX3av97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله..
جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/naya_foriraq/79420" target="_blank">📅 21:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كربلاء المقدسة تعلن تعطيل الدوام الرسمي يوم الخميس المقبل الموافق التاسع من محرم الحرام.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/naya_foriraq/79419" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
جرافة (D9) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة
#أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/79418" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
بلومبرغ:
‏قال الرئيس دونالد ترامب إن احتمال انهيار الاقتصاد العالمي كان سبباً رئيسياً لتوقيعه اتفاق سلام مؤقت مع إيران. ويكشف هذا الاعتراف عن نقطة ضعف رئيسية للولايات المتحدة قبيل الجولة المقبلة من المحادثات مع طهران.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/79417" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هيهات منا الذلة..
أبناء البحرين يخرجون بمسيرات حسينية تحدياً لعصابات آل خليفة المتصهينة ويرفعون فيها الشعارات الكربلائية بذكرى أيام إستشهاد الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/79416" target="_blank">📅 20:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emy3mwmPnrNBLSfpWGkr8wrnxb8ut1YUrq_mqjQbadEpSKFfMwOwsHWyE6_uJ9wzJyn2JaJoE21PCk2CLobamqK38tVxQ-qZuDOdH_c02Oc37Rxw_A7CnMmtDeQHM5QKQ2aT6oKZV1f-pDjQo_GEhkHsCfbff3DvxZzA4g1YRa7RvI51UnlrcyXuDiV5zhJEfzLPapFzzAUpjFbunykjP0njBBUhMzMMvgX3hpBj5wsCQqD9KxKdILOZ9gj37i0srG8RH-8tkfptvdU6ftRoBvelgbm-pA__dOCpyS_Yle2GAh0CgQ38XayYRMAKPE9QnSiMGOqTZTSjjRICAq4W9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الجيش الأمريكي: تبقى القوات الأمريكية حاضرة ويقظة لضمان الالتزام التام بجميع بنود الاتفاق مع إيران، وتطبيقها بكامل قوتها ونفاذها.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/79414" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcO94VNWx1-rMXOBxMwCuhSnrHBZZXOUmaJoVU8hKo9XFh0qop2OwNXgL0u_RFpAybq69krGhpa83iVqg_wZnvv5Q6TPtANFn3ixayjqk1Xt2iuDy6iM8BOqSzDresWats-Bo38Y0uUc6koltPMdMRZ2JuhnuBgHL3nSUxFIIepp5-eS0PuxO9rTu0e1sCl_1ft3p43vU1VgluNUAYnVb7RA1V1ZccQqyDbegcHbA48HSQ2sxgvd-NMSXluC0J9XjhhRPMkeWsQDA_ktDHGtPd2AjC8eqfjj0OiNzcOsSr3cKKALKP8FhipdZQDRyYwu676QW303Z-zajzuwQrS7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79413" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTtwEUvPEeVSqANcVcbR2XAIwIzENn8dvkDcac9qx-cnKWRnwAEtas9TmsaEzRhekhgSsBLFjYXaYCJHTFuNUnJQiVUgN2QUNpe8dZPIVomlQvDP8we07TPH2H9uK4QgT25ixu26cus_8JBcsHVJPpygHFlyEpny-tz4dPlukXRyMcYE9aoP-VC_XE4R71uL4TtRIbTreI7i1QKdavq8uLrAzCUFRlmwqRR8aFDUJ8LnramMOAY91VLAvdz_Jl4kXocf4jI7_dktdXSD5RVxW7YXGOoYbT3qN--M4VzHBRu8AYxdmmjKhbn4rxyFgKgxcYz8jU-jNW2otiWVrZ_PsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:  مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!  ‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/79412" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هزة ارضية في مصر بقوة ٥.١ على مقياس ريختر</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/79411" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf9pBzmCu8aUmJPr-oY44BEZ1o77RRp16Q1FC1v0GmFyOWTa4NO2E4zkwEiilmVgSCUxiIxpAMzVvYLMKs4ph7LF5-4LAZLrLaJBznt5tMXi0Gc9s-9wiJuYY91XjoLGuwBCB6Q6dbmIdHE89p02wZzS0o_CPe86QVW0R3ok1AaSUUdZmVoe5h5gsnP3EwX463enTcf0eAELPizgkkiS1ZXbgjK1HjV9r9YJ5tIvTeJJ5dcmcagLeZypET-cL4Hkr4kU73x8BmgL3GpY0u6_kkEiTFpRUagoJnfDu36nXrF09dC8ljce1JRQxzmPBENfwxxJU0_W_a0Ni1QafUGqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
لاول مرة
تنشر منصة كاف التابعة لكتائب حزب الله في العراق صورة تظهر نوع من المسيرات تشبه لحد كبير لمسيرة صماد ٣ اليمنية بجانب العلم العراقي ؛ لم تكشف الكتائب عن طبيعة المسيرة او مواصفاتها التي ظهرت بجانب مقاتل يرتدي ملابس عسكرية تشبه لحد كبير ملابس متطوعي سرايا الدفاع الشعبي التي تعتبر اقدم مجموعة عراقية مسلحة ظهرت إبان مواجهة عصابات داعش في العراق .</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/79410" target="_blank">📅 19:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">أنباء اولية عن مهاجمة قصر الحلبوسي</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79409" target="_blank">📅 18:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79408" target="_blank">📅 18:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79407" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuFdUAl-eyWoh8d6wWFLWLQ8tEJhxTjwuPbUU_S4huRiL__G8KKvcK_IwoLLorYFw9LiinPzt8Ms7sxZaD6ZIgbI1mHHYkIn2QSZiS2BNij9RCWCa86JC9PwPj63ob4MsExRVLoT8JFSvHCEuBRrhsOyY6ZmVxZRZG6SrpTS1kvfCSrglXgFuYxtnQpvw7Mfgc2wG_5R2SuI7XZAjHU5c3UePRE7s4S6M0bzSHwgzNFeoD6G0f7uIDKWKIvJrciCb-jkZwaZsaovMWuugDsKpjhc8gVOrEPEZlHx6ISHNmveU9ucy5mReS86gH1CCsAs1pS680nWC30wjZcPOuPQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل   زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/79406" target="_blank">📅 18:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.  يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79405" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79404" target="_blank">📅 18:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
بيان صادر عن العلاقات الإعلامية في حزب الله:
في ظلّ الادعاءات والأكاذيب التي يواصل العدو الإسرائيلي ترويجها بشأن مزاعم خرق حزب الله لاتفاق وقف إطلاق النار، في محاولة لتبرير اعتداءاته المتواصلة على لبنان والمجازر التي يرتكبها بحق المدنيين، تؤكد العلاقات الإعلامية في حزب الله أن هذه المزاعم عارية تمامًا عن الصحة، وتندرج في إطار محاولات العدو المستمرة لتضليل الرأي العام، وفي سياق محاولته الواضحة والمفضوحة لتخريب الاتفاق بين الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية.
فقد تجاوزت حصيلة انتهاكات وخروقات العدو الإسرائيلي منذ فجر يوم الجمعة 300 خرقٍ واعتداءٍ موثّقٍ، تنوعت بين  الغارات الجوية من الطائرات الحربية والمسيرات، والقصف المدفعي من مختلف العيارات، وإطلاق القذائف الفوسفورية، على أكثر من 25 بلدة وقرية، من بينها مدينة النبطية، وقد أدت هذه الاعتداءات إلى سقوط أكثر من 111 شهيدًا و176 جريحًا. فيما تشير المعلومات الأولية إلى استخدام العدو للقنابل العنقودية المحرمة دوليًا.
وقد بلغت حصيلة الانتهاكات والاعتداءات منذ صباح هذا اليوم إلى الآن ما لا يقل عن 180 اعتداءً، وأسفرت عن سقوط أكثر من 28 شهيدًا بينهم ثلاثة شهداء من الجيش اللبناني و35 جريحًا.
ومن الثابت أن هذا العدو الكاذب والغادر لم يلتزم يومًا بمندرجات اتفاقات وقف إطلاق النار، لا في 27-11-2024 و 08-04-2026، ولا بعد إعلان التوصل إلى مذكرة التفاهم بين إيران وأميركا بتاريخ 14-06-2026، ولا حتى يوم أمس الجمعة 19-06-2026، بل واصل انتهاكاته وخروقاته للسيادة اللبنانية عبر الاعتداءات الجوية والقصف وتدمير البيوت وترويع المواطنين وقتل المدنيين.
إن هذه الوقائع الجلية أمام العيان تُبيّن بصورة لا لبس فيها الجهة التي تنتهك اتفاق وقف إطلاق النار وتقوّض التفاهمات القائمة، بل إنا ما يرتكبه العدو الإسرائيلي من اعتداءات ومجازر لم يعد مجرّد خرقٍ لاتفاق وقف إطلاق النار، بل يشكّل عدوانًا موصوفًا واستكمالًا للحرب بكل ما للكلمة من معنى. وعليه، فإن المسؤولية الكاملة تقع على عاتق الاحتلال الإسرائيلي الذي يصرّح مسؤولوه علنًا وبصورة متكررة رفضهم للاتفاقات القائمة ورفضهم الانسحاب من الأراضي اللبنانية المحتلة، وعلى جميع الدول والمسؤولين وفي مقدمتهم الولايات المتحدة الأمريكية ممارسة الضغط على الكيان المحتل لإلزامه بتنفيذ الاتفاقات ووقف الإعتداءات، بدل رمي الاتهامات يمينًا وشمالًا.
ويؤكد حزب الله أن من حقّ لبنان وشعبه ومقاومته الدفاع عن أرضهم وسيادتهم في مواجهة الاعتداءات والخروقات الإسرائيلية المستمرة، ولا يحق لأي أحد أن يسلبه هذا الحق الذي تكفله كل الشرائع والقوانين الدولية، وأن ما يسعى العدو لتثبيته من حرية الحركة للاستمرار باعتداءاته أمر مرفوض ولن يمر دون ردّ، وأن طرد الاحتلال من أرضنا هي مسألة وقت.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79403" target="_blank">📅 18:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز..
إعلام العدو:
نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79402" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.
يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية في أمانة مجلس الأمن القومي الأعلى، وعبد الناصر همتي، محافظ البنك المركزي، وحميد بورده، نائب وزير النفط ورئيس مجلس إدارة شركة النفط الوطنية الإيرانية، وكاظم غريب آبادي وإسماعيل بقائي، نائبي وزير الخارجية، و... أعضاء الوفد الإيراني.
ووفقًا لتصريح بقائي، المتحدث باسم الوفد الإيراني المشارك في مفاوضات "ميناب 168"، فإن هذه الزيارة تهدف إلى متابعة تنفيذ التزامات الطرف الآخر، حيث يتم اختبار كل اتفاق وتفاهم عند حلول وقت تنفيذه.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79401" target="_blank">📅 18:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:   نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79400" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79399" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzGIwb2YbvNX2T70srj126iV5_6AEScONWQAttomx2AIB9kl0GofX3JDPm-6CRPf41Ae8V_-Jx7vT1NLwnPZMKa2r1yzlBRIWg0BBvz3c5FgwJWth9seFWNt_P_66ZS-J2chn3MBjgfpjgSajr_eDVKB8XRVzG8kvgJF3rY40kHhQq0YwzscF9gE-bcwcnplLGHwdtnuTLDxqsXMf_FkKUV5dOmaLG-ws67xnEfyzbDIS2oyxshXxCN9JV7pfIuql4I8VYo5uhyfnyFZZpDNgiuCX3sY7P96KeUdikXf0P_zLdVz-Uqi5vKF0jWcGef_G2kSCStrPhXfZZQCzO4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79398" target="_blank">📅 17:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
الخارجية الباكستانية:
محادثات تقنية أمريكية إيرانية ستعقد غدا في بورغنشتوك بسويسرا.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79397" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7S3Vyar_gXRnljuLn7VHbIMIODzsWnTVkNlbkKqo7xrub99O3oRpEuCaGvfVLoqREVzRG_HrPZAsd5a5qmLlgN6WFBVVyWlOzVB3UsIgy9WD-XL0-0dzsLiO4D2Du2Cjwoofqgccqg-mhUf94JeXkB8RMv0g6wD8-KMLSAcbNuSWnIIV2nhpnpuMd3SC2aT0mfsv2e4sqPslOVnSLV_Rsyyh4P_xSaW-hW-6GGOGa29cE0PVTF5qixg-W3-OGNAkk6xGcRJ3DNnQHy8Wzu9KAwvcT-3enSzgLWPrvbLn2e5VctKagH048asiISPoZODuHFe5bSiTeB_h5kJMEwf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:  طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا،…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79396" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79395" target="_blank">📅 17:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:
نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها سيكون مهددًا بالخطر.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79394" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxQt47jkRA-9HqIU6g-2aulrB501KrhxqpGa7AwxoGjFeiHyXYdQ8NzkIOrQ9yL27Vi4vP-sPFMwha5-JmEiJkYgbz_8hcc0WpDWjyuPTXN5gQFqoBpMI0DpHPjgt171sT9uDzOftvNwlpyjEzvvrkN53zFXvDKFq04oy4tvJ4D9yHqgLOkwQzPNq9FeL-9wQ95rrBYASg5fo4HN0ZC0pFHOlYLrAifZFIwKwwlzGwWscdjlZeWQZZxelWN1TglvbC7-VVgAbPmLHmPwzHswF-WoQO5Z1gsna1sdoG1_wH-vJdl9lasTjGip_O90eNoFraJCRTsdd4Ou60jXePJsEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79393" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرار الخارجية والتصريحات جاءات قبل بيان الحرس الثوري مما يعني عودة عراقجي في الساعات القادمة إلى ايران بناءا على التطورات في لبنان   ايران من اجل تلة يقاتل بها حليف تنسحب امام مفاوضات دولة كبرى  يخشها بعض سياسي العراق بسبب تغريدة</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79392" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فانس: الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79391" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فانس:
الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79390" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعلام العدو:
ما تحاول القيام به إيران هو رفض أنصاف الحلول والأمر الواقع في لبنان وفرض حل جذري لمسألة التواجد الإسرائيلي في الجنوب. قد تكون هذه مغامرة ولكنها قد تكون ناجحة أيضا بالنظر إلى رغبة الإدارة الأمريكية بإتمام الاتفاق، وفي ظل توتر العلاقات بين ترامب ونتنياهو.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79389" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79388" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79387" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وسائل اعلام تزعم:
عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79386" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">في محاولة لمطأنة الاسواق العالمية..
فانس: لا يوجد دليل على أن إيران تغلق مضيق هرمز.
جرب وادخل
😄</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79385" target="_blank">📅 16:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:  ﴿وَإِن نَّكَثُوا أَيْمَانَهُم مِّن بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِي دِينِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَيْمَانَ لَهُمْ لَعَلَّهُمْ يَنْتَهُونَ﴾ (سورة التوبة، الآية 12)  نظرًا لنكث الولايات المتحدة العهود…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79384" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5lHGwrbBrHF7FtJ2EfjjZfkfc7XRQ6oehpgLihFGRZo60GSPpxRYA7fl6oP3Q0aqqH_kdF3ir2b0D6S0LbYUiguza5Ym3V8_SfsBolHMbvhWSaHwHphiA2MUT6cEdDypdDLeHMc_gGMmAXmhQnmAffWtcbBHju8BdlAjoPgEx7eCQsztruqVIjUdSbjDBr7Hf-uGPMQYn3JO9oVmA9F9UdhnYoefTS5GWnPetvhIeF0m-BhBaKhAoeMNA1tHJfQVSe_7l69NtJxewFh2dClw5Wc_zjnngZxuUrnhBX3yzzUdYMNmNYYAVcx0fHaHV-wVxGPNhTbbPwDUBnHsd3yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من الإغلاق
ارتفاع اسعار النفط بالسوق المجازي الى اكثر من 80 دولار بعد اعلان ايران اغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79383" target="_blank">📅 16:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79382" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مجددا.. النائب عن حزب تقدم (مهيمن الحمداني) يطلق النار على عمال بناء كانوا يقومون بترميم جامع الخنساء في الحارثية ضمن العاصمة بغداد مما ادى الى اصابة عدد منهم بجروح خطيرة  متى يتم حصر مهيمن الحمداني بيد الدولة</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79381" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79380" target="_blank">📅 16:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مصدر امني لنايا : اصابة المواطنة (سناء محمود خلف) والدة زوجة النائب (مهيمن الحمداني) بطلق ناري في منطقة الفخذ ضمن منطقة الحارثية نقلت على اثره الى مستشفى الاميرات الاهلي لتلقي العلاج وبعد التوجه الى المستشفى والبحث والتحري تبين وجود خلاف بين النائب و زوجته…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79379" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
بحرية الحرس الثوري حددت مسارا من جنوب جزيرة لارك لدخول وخروج السفن من مضيق هرمز وإذا لم تلتزم السفن بالمسار البحري جنوب لارك فإن مسؤولية أي حادث تقع عليها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79378" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79377" target="_blank">📅 15:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🫡
وزارة الداخلية العراقية توجه بتشكيل لجنة تحقيقية عليا للتحقيق في حادثة وفاة شخص يحمل الجنسية اللبنانية كان قد أُودع التوقيف في العاصمة بغداد إثر مشاجرة مع أحد أقربائه.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79376" target="_blank">📅 15:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 11-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة طير حرفا جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79375" target="_blank">📅 15:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrOlyOv4VQwb5s7OCxjwqg45HepwC3Swt-G9_kDzs837JE-o3Y0c3ncPd1M3Oi_ak-PwbPEYmbuQHX1CXYAcRytBweAt078_H_bx2kY96nDeRldwxb8Yxuex-X3Lw-_gZ5rEze7W3ww5aEBDm9MNDPNe7-Mo1ReA0lf-bvRh8j00RBSKOFh_3TOFTQTENvdOrRx0If1-mPBOBCC96OwYTTyfwzPN-IC7kG6TE9G7bC-RzihEZzfZUzQScKaipfXVB04opZZtDuHBQKtCoqcB9ir7BIkOu_FhF7Dn_GSBlOVKQqIzG4Fy_w-nfhO1acbF9BMq0SPbijgyBEOB8_TR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
عائلات شهداء مدرسة ميناب ترفع دعوى قضائية رسمية ضد الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79374" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inh8EctQUZXu77Y1gkLHVa_RWaumdsfEmVpmfcgRyjH72vZzEbYry_C1crQnCApVfUrGf5sH3Zoi9JXO0gcVBxydgKD2s2uZqXzPTdXvHP6oiubPZGQ7U1pF3urZ190ID5bSBNxTNUq1OWp4GZ6z4vQUndnUm5Jlp_IyZeybzaxc4jEaY6s7HFu56mNiLXu9J5juEjwO_Mq1ChvdskIEofAW_VP3hQMI8e-0O6Vco1v95VcRUW7Jb4aEnZgXGNx7NMQxsBxVULXxTcIJNX65oSvpJ0TX9l_hxt0yb9MsNTnbE4dGDo4TTEN0WvWn5od4eLiK555HfWsKe-MLi2GUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:
طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا، عندما يتعلق الأمر بمنع إيران من الحصول على سلاح نووي أو تطويره (لكن الناتو فعل ذلك أيضًا!). حتى أنها لم تسمح لنا باستخدام مدارج الطائرات الإيطالية، وهو ما يمثل عائقًا لوجستيًا كبيرًا، وذلك على الرغم من حقيقة أن الولايات المتحدة تساهم بمئات المليارات من الدولارات سنويًا لحماية إيطاليا، وغيرها من حلفاء الناتو "المزعومين".
الآن، بعد أن هزمت الولايات المتحدة إيران عسكريًا، تريد أن تكون صديقة مرة أخرى من أجل رفع "أعدادها". لا شكرًا!!!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79373" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇨🇭
اعلام سويسري:
وفود تحضيرية لإيران والولايات المتحدة وباكستان وقطر تعمل منذ أمس بمنتجع "برغنشتوك" تحضيرا للمحادثات ولا أثر بعد لرؤساء وفدي طهران وواشنطن.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79372" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fea425d27.mp4?token=DK_vjedG2yxGln2dUKusK1jH6laC2ZtYKjgqzZeEIu5l4LmnUA6puIMyONvfZcZ960BrepW-Vs0QRycFOFbAbxl3KLMBh1DDFVqqSCZGuWJ3LVTfHuxptSsBhJzwkLlKnM0sskP-4z2cVnWFSHxoNQlVm12tW60jmyP0kaxgJZgmrA84wRmM62iswtvaOJQpgeN1O1hdzbAfxYTX-W_EKfIWQ2vJEfYLiXNiWb4tRT9ZESNNUWS2hrqOl1t9dStW1m0Nt2yIbtgAEYn5HexwIqVxH82V0hE3OHKd9LKhZLizchh6Ll87vlxM1bX-NAkx03F2qjEh4QGQ_wMHpI3Ybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
زعيم ما يسمى بـ"المعارضة الاسرائيلية" يائير لابيد:
دفع نتنياهو بالخطة الكردية دون مراعاة رد الفعل التركي المتوقع وتأثير أردوغان في واشنطن. أردوغان أعطاه درسا</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79371" target="_blank">📅 15:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGaq20Z8PH8RBtiv88bgsNHMHhFAcU_nlQ9f-mRTsPeNRNROOy6uSxRPTSfMWDEshFjFFrvfAvTN1AmusHc1rmFIYpVNkmL7K7BG6bn9MZiTsBsbBFz0fc9fG2VijacNI6yVbWJpGTisaQ3u3DZxvDast-Nax1mhXNBOl3Uj9gdfUcRyC6OxRu2VNjOV_OKvhCeNuBys7TNYMr1FJTLIaq-LwJXmxaYAOJMOEPAT3UjzsWpWkmre_3jSYTaO8W2DEcuEZgLKYqAd0ZHyCu6oj86168Bi1Tf2kwNI970Jwza6ajGINiJsESkWBry7lROgjSF1IvUV56OSMazL3A5TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
المنشور الأخير لمدير عام كهرباء الوسط علاء الجبوري قبل اعتقاله بتهم فساد والذي سارع أدمنية الصفحة إلى حذفه بعد الاعتقال</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79370" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e875b0f6c7.mp4?token=ZH2MbOs29kRFf0YcPm5tbDaWLrs45YC5GedKZh3F-E1EoMTm1EH58oWBAA84TYPE3JVY5WzjGO7m3tv1rznWSV1UBZlEiE7afvhEE1twaX1lf7UybCex5O-JvaSzR2aDUzcrDTfA6Mjkz8k4kUwbfERRHQe54t2DsoFU9kNDL52I0DBRg3sv0aPIv8tmAJrYcB9GKxoDw6g0h0n9sjZLelb0ykj6hq4cMPuYDxl8-OicD5R5jDVpcSbk2HaWCJXbLbMq8n2U29ns8Hh49RUhxeegY2h56faXwRpqRy4RCB0cfwN_PYbJa-CPRUAjelgtJWXoIaDODtgtTOpj1cKrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79369" target="_blank">📅 15:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
🇺🇸
السفير الامريكي في تل أبيب مايك هاكابي مجددا:
لو لم تكن اليهودية موجودة لما كانت المسيحية موجودة، ولما كانت الحضارة الغربية موجودة ولما كانت أمريكا موجودة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79368" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
جيش العدو الصهيوني:
في عدة حوادث مختلفة خلال الليلة الماضية أطلق حزب الله أكثر من 50 عملية إطلاق باتجاه قوات الجيش في جنوب لبنان. سنرد بقوة على أي اعتداء</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79367" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ويتكوف وكوشنر يصلان إلى سويسرا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79366" target="_blank">📅 14:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptWYRFsenMRZ0snD_PBdlhwBjS16LUuzdFcmWv3-lR3nfuVaGhpILvyF-6A4ASQ0BXxDA8pOp-6NcJQCWCp9pYm6aOeHQnL1dPoFTBLqPYHzB6EyENp9QYAfDZZCGVJ0fukRJUbujg-xyhgogvgTS3ba0usS8BD-ageY_JS46ySvNQ1zZ6p5VYGWkv225z0_v_uDgmjnYuYSI6OIxnpFlwRSBRMtd1j01pQA2_0OuiCwA5lMa3qLmV3W2uRFE0lTZ84AdZ5-Ykwth_4114nuvAS2LpURBHr7HRVktkxm_4jrowjSQXXs6-nXnyO0tIofQmCndS45e0djljpIOXHJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله:
ملتزمين بوقف إطلاق النّار، لكن لن نتهاون في التّصدي لأيّ محاولة يُقدم عليها العدوّ لقضم الأراضي وتوسيع احتلاله، وسيكون مجاهدينا بالمرصاد، وبكامل جهوزيّتهم، للدّفاع الكربلائيّ عن أرضهم وشعبهم ووطنهم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79365" target="_blank">📅 14:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otIdVlCGdcDC4Kb3TqwS1pzgEm6X9apA0s05qd4VvZZeoEVzZvvnavgRRIFG1BsowY4aUElwzdcAZr0aBRcLjbBXjUR60Pp5zUpKpNqGc72zQa2X1SzWch8YW5M01u9n6bJmLwKblz-NtV18AC0GW_S2J7PssvzbdANvRcQFhZlfyGQAdy-XEdCQPnx_wiCk_oPf4wODNq8FhczgYaXMNoEbyiF9aJHoavD9v0w0tyDMmNi6oQEKnQOutoktvHMl-pLfRekmYmEfzFbkOsI7Jw-4CRNsDh1iq2X5HGOgmziQQ2ZA_ffpWwTGjLf6UT3l9vnwn7b77B37aWunrwBTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب
يدرك الحمقى اليساريون المتطرفون والديمقراطيون مدى نجاحنا في حربنا ضد إيران، حيث هُزمت بلادهم عسكريًا بشكل كامل. استمر أوباما في منحهم مليارات الدولارات نقدًا، ولم يستخدم جيشنا المنهك آنذاك لما كان ينبغي فعله لكبح جماح إيران، الراعي الأول للإرهاب في العالم. لم يكن لديهم أي احترام له. اعتقدوا أنه، مثل جو بايدن النعسان، زعيم ضعيف وغير فعال، وكانوا محقين تمامًا في ذلك. أفلتت إيران من "القتل" لمدة 47 عامًا، حتى جئت. ثم تغير كل شيء. أمريكا عادت!!!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79364" target="_blank">📅 14:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK0gcdY4T4oBoDPtS6LsrWluCT_yBWL8BDId4uGRrUZvBrfvwSlxdXVjs5Q09J60t-rf5NtXaejZDb6IoZnJs-3GnCcxZWbKjsi1JFG-0T1_UJ-ArEGxuqxpCMMU3a60fhIJIvqxgLgE3tjd5oIN7qVUzig2ngmMY0hwdp6ZRDfsiVxWeFLbbLV5B2bSRNs0BMjO238B8x-a1ot6P87w-Dp4Ypt3m90Gc5vlJRsuSLy4HPxBhbZtZNWrUJlM5LMh0qF5Cdu6yk-9JnSqfASYXTl9ASejASQ-VB4fnYEx_6XbqNWSCzXlvsN86VgRVJIQ1ri8dyyXR6tx-i_qSemokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
المتحدث باسم وزارة الخارجية الايرانية يشارك تصريحات لسفير النظام الصهيوني في الامم المتحدة ويعلق:
هذا الاستعراض المخزي للتحدي المتغطرس - ضد العقل والقانون والأخلاق والعدالة - هو نتيجة حتمية أخرى للإفلات المطلق من العقاب الذي منحه عوامل التمكين لنظام إرهابي الفصل العنصري. يواصل هذا النظام حملته للإبادة الجماعية ضد الشعب الفلسطيني وفي جميع أنحاء المنطقة بتجاهل تام لجميع المعايير المتحضرة. لقد حان الوقت منذ فترة طويلة لكي ينهض العالم ويواجه هذا التهديد الخطير وغير المسبوق للسلام والإنسانية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79363" target="_blank">📅 14:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">من بغداد، من أمام السفارة الإيرانية، اجتمعت جماهير المقاومة الإسلامية احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في مواجهة قوى الاستكبار.
آلاف المشاركين لبّوا دعوة المقاومة الإسلامية كتائب سيد الشهداء، مؤكدين أن خيار المقاومة ما زال حيًّا في وجدان الأمة.
في رسالة واضحة بأن نهج المقاومة باقٍ ومتجذّر، وأن إرادة الشعوب لا تُهزم أمام التحديات.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79361" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇨🇭
‏سويسرا تقرر تمديد التدابير الأمنية في البلاد حتى 22 يونيو في انتظار موافقة الجانب الايراني على استئناف المفاوضات.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79360" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📰
نيويورك تايمز عن مصادر:
مسؤولون غربيون طالبوا نتنياهو بوقف مهاجمة لبنان كي لا تبرر إيران انسحابها من التفاوض.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79359" target="_blank">📅 13:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79358">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79358" target="_blank">📅 13:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
مقتل جندي إسرائيلي وإصابة 11 آخرين بنيران حزب الله في منطقة علي الطاهر خلال الليل.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79357" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79356">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
🇮🇷
وزير الداخلية الباكستاني يصل إلى مشهد تمهيدا للقاء مسؤولين إيرانيين</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79356" target="_blank">📅 12:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=GJOo8P6r2mZaotwu6CQMOgeQZeE4SeRNMMClRuvsPhPNWvj9EkgOlcn0Z-z-IQO1UoeT96iAsKQhFsjef0nTPUkEdWTuEgaZxkFMy1YoRFbQEGn3UYsG9qtENhFNR7iLQYBxrdRTBlJ_L3phi__R0j19S8dqU0hGwk5P3dtOBhF88LEOH0R81FE4OeT3kS0ncy7D9MJ16ih38Gqy6C9wzWbUBygIRK6yW7njKw1_Yrd68LQjr864iKzPo61Zu707sq10Z2zezCtuVkiC-AovJ7uPA9jUgRUTwxzJmUGniukRTZUYg40I8v_fxRaFCRRE_uSF1GtmNxFFAPjhbPYQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdcf3568f.mp4?token=GJOo8P6r2mZaotwu6CQMOgeQZeE4SeRNMMClRuvsPhPNWvj9EkgOlcn0Z-z-IQO1UoeT96iAsKQhFsjef0nTPUkEdWTuEgaZxkFMy1YoRFbQEGn3UYsG9qtENhFNR7iLQYBxrdRTBlJ_L3phi__R0j19S8dqU0hGwk5P3dtOBhF88LEOH0R81FE4OeT3kS0ncy7D9MJ16ih38Gqy6C9wzWbUBygIRK6yW7njKw1_Yrd68LQjr864iKzPo61Zu707sq10Z2zezCtuVkiC-AovJ7uPA9jUgRUTwxzJmUGniukRTZUYg40I8v_fxRaFCRRE_uSF1GtmNxFFAPjhbPYQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مستشفى رمبام في حيفا تستقبل جنود قتلى ومصابين إثر المعارك الجارية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79355" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fY4AdoZT9mL1YFnp0K3MLPO_w9qAyNN1sVCTu5zx71yAhYDZt463VoiTS2x-3Vin-YBqGoG7r-dqRRo6D6fuJAn_RGUCdQ41kQUtPBeF31QUbBBW1ztiA_5R4GfXTA15E0am3GPj3GEzn7rV7RzRfy9jl-jMd74jEHZkQsghDX8ejZbXGtZZLt7FaJaXZxT7kGkcpg6RhODzrgJMnD1dxJe5-4-VhARQJuvOAtE7lXcHOEpn8IL_hezPnkRM8F4M4pfhYr4OoMsgIsh8RDz6Ub3c3IUx4oAfpCLJH9YauQxFhUkrBC0A-RqiSBx-4qIJAvaVSdJ4cs8En2O59vnTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tsne-rs3XA4RQ2ir9aZ5j2iHswhS29piLaXOKDWqMduI09i0t-Smi3D1-mM299l6o6moy-KwEvdyS1soRbRaqflmZ3rBJQCnKQCiOKDevo9e_844VkwJIpDb0kFrVI3N4L8iXwQBkH4p5-4t5H3nRKnhbptOadbX4KhKNZzjDdVT0_C5WtEecAx-tOygEraMLD1pd0Jue8n5DPjOR3KXkdGnif3xv85Tzh6grxS4XfJCcuFsySPXBJOTFm-b3fHKf20E918Lpy8RFQITvD55kVqmzynuzC5oGVFI9AjqxuHyuZieaPJciB_EIaeZUTZVqfkKgZOUnzYJ_uM-pTtrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQmmiuwHg9xl4knJfLQOCbkjFeHQaK7m0HaTphAWpgJnsQtxhuLMKlRyV2dEbm7vOf3UV-XMifKlZU_Uxpa7VFs-K5mwY7FaIEzmA6F4Ww_P_L7py0SSfUGHVSplX0Pxsh4CpaTLLhntFqLb7DoUpuazN_95N4Xr6aJMboIrd9OgtFBT-qYLKYuHKcodCZZaJDjVEgGzCBFS3N_BQ10Zv8AStsQCoFViUe-3L5q8K2a4NYQQpf2DRibeGtF-QlYDUSV63z_bbrRabnlNXvz5gSClXx1BLvZcFLGRDETMcl5t8p_zxXMMXWsWwoG14HSyJEAxFnKYXOSRPtLTaK64Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
ضمن حملة التصفيات بين حكومة الجولاني وعصاباته.. مقتل عدد من إرهابي الجولاني إثر كمين على طريق منبج حلب.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79352" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=DiG1R9fMwfW-YcF_SJdEidaiQf2J2FLB665Cw8ZVAglu2M9_-Ht5u4-iP9flGOmt8QLnn1dO8S06XctK2H2p0A8o4xJjNprabW03_jaVRf1kOuX5q7Fx_c8qrr5NaIMnhc78O40oUwIuf0DlHq79qhZnCGQwQj9x_-KGncUtHPrKO5OW1vofw4D8Ivf6UwUElLwDXu_sctlKtvK-fy5AYWageZgxXZQHDivAR399NIqmZiqPb3T4RGuyT-Ec_IjpB7bLhULqDQBFo16EgWgAf_x719_jQq1Kp7GIYZ2xuNVSXn2w8o168vit_1XlYflPnZ5jdHJPTw1_clg50qDTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9366af54.mp4?token=DiG1R9fMwfW-YcF_SJdEidaiQf2J2FLB665Cw8ZVAglu2M9_-Ht5u4-iP9flGOmt8QLnn1dO8S06XctK2H2p0A8o4xJjNprabW03_jaVRf1kOuX5q7Fx_c8qrr5NaIMnhc78O40oUwIuf0DlHq79qhZnCGQwQj9x_-KGncUtHPrKO5OW1vofw4D8Ivf6UwUElLwDXu_sctlKtvK-fy5AYWageZgxXZQHDivAR399NIqmZiqPb3T4RGuyT-Ec_IjpB7bLhULqDQBFo16EgWgAf_x719_jQq1Kp7GIYZ2xuNVSXn2w8o168vit_1XlYflPnZ5jdHJPTw1_clg50qDTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
من منفذ مهران الحدودي مع إيران.. بدء توافد الزوار الإيرانيين لإحياء ذكرى عاشوراء في العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79351" target="_blank">📅 11:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmtsFUukdGpWxNDZEVQy_z5-rN5W6BOSPAF5sJwZ0c2QzLcxuR6qvojYQN_Us9zH10p1P6CZ_b0GWTsYQg8u496ebg5SWlXGsy4D85H_hkax2-SOkzCXPRWQ4Xt__jO14jiz-p8fpFCDi0IAzOnfo95ci3QKYC0B8C2HqtBo757GP0vUaKq7nBqjvQhAqgJYfkYTSVU-XycKeFdbyzLVx5eQylnsuGmM4XGt1H0MrPzt7Ci_SN_B8jzmPzi44MTqaqPzu82nc0Nhd-lgEpYFiRC4XcwdUl8j2KG-V1uMuCoI0Py1f0Rq92fDeCigl3aEgiYjSIrEtlwxtn_EVTsWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
هيئة البث: مفاوضات ‌لبنان⁩ وإسرائيل القادمة ستحدد مناطق تجريبية جنوبي ‌لبنان⁩ سيتسلمها الجيش اللبناني
من منجزات الجيش اللبناني إغلاق قرى وبلدات الجنوب ومنع وصول سكانها إليها ؛ الصورة أعلاه من إقفال بلدة العامرية في هذه اللحظات.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79349" target="_blank">📅 10:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇷🇺
ميدفيديف من روسيا: أصبح مضيق هرمز "سلاحًا نوويًا فارسيًا" وسيتم استخدامه على هذا النحو.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79348" target="_blank">📅 10:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=Es4wMPQevZdH8PwZoXM6QTWR6KOFgK6EvvTWI1g5oNDJTKcltMpuX4itZHJ-VOE2LCEowLfI8Z0cNF14hUA1XSJwt87MPD3AsbUBUeRGNZEteQ-yyh-ae7K8UCOQ4nr91FJFMOoAm8JZbO20PNsaBjPDqloKf4DU0Nthpu4-I-BD9zoxK3EY4Xla2JWmrPbc2MYc1LlKgcO5IUnqGzQEcXvQnSo9YqGaaIf8jruO13IpX-H80u-2ilJnfKCKW5UTOoGo-QPpNqNyO3RKQUCPm0F_Zf2z6gRyuaWEqhMf-zjv7UA9QmzoQGp5brVn_IlKluZFc_bWKsanNqm8lfRfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896e6400c7.mp4?token=Es4wMPQevZdH8PwZoXM6QTWR6KOFgK6EvvTWI1g5oNDJTKcltMpuX4itZHJ-VOE2LCEowLfI8Z0cNF14hUA1XSJwt87MPD3AsbUBUeRGNZEteQ-yyh-ae7K8UCOQ4nr91FJFMOoAm8JZbO20PNsaBjPDqloKf4DU0Nthpu4-I-BD9zoxK3EY4Xla2JWmrPbc2MYc1LlKgcO5IUnqGzQEcXvQnSo9YqGaaIf8jruO13IpX-H80u-2ilJnfKCKW5UTOoGo-QPpNqNyO3RKQUCPm0F_Zf2z6gRyuaWEqhMf-zjv7UA9QmzoQGp5brVn_IlKluZFc_bWKsanNqm8lfRfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79347" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=IZbgfNW5MHrlsCrJUfbuJEKMGyQ-Mb0UQYylW27JUAANIIvrHDz-kTYh3_TEcu1rNvuRldB05nYStxTFv5pudq3eNu39StvPQxc2M2KfU2QBHTLIHqC2_j3scyAx07Cy8B7_QrL0aYMgrUBWYQ5vqhkWUYw8GnrqxMGI-AjZC3yq25jdHG7zk4q45jGX1n1iYOySFl023kvhXcpSilLUm6CPipGY6v6rImTyK7ig4ZlMPzZ7Wxvhzb9CQhS-6ZNFC9aTPdXaGHs33tBtXMKuFxaLxJaHrzNzmOpriWkjJAUin_yrIMsDQdfPocPCjdmKV8axFRprlDqSQerbvCv3Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ed7f3d48.mp4?token=IZbgfNW5MHrlsCrJUfbuJEKMGyQ-Mb0UQYylW27JUAANIIvrHDz-kTYh3_TEcu1rNvuRldB05nYStxTFv5pudq3eNu39StvPQxc2M2KfU2QBHTLIHqC2_j3scyAx07Cy8B7_QrL0aYMgrUBWYQ5vqhkWUYw8GnrqxMGI-AjZC3yq25jdHG7zk4q45jGX1n1iYOySFl023kvhXcpSilLUm6CPipGY6v6rImTyK7ig4ZlMPzZ7Wxvhzb9CQhS-6ZNFC9aTPdXaGHs33tBtXMKuFxaLxJaHrzNzmOpriWkjJAUin_yrIMsDQdfPocPCjdmKV8axFRprlDqSQerbvCv3Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.   جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79346" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=sW7I3_QHrA1Ie6W566d83pyAHE5eWA77e5Ge91lih11kpVcqjD7SqkdkbPfAt2mJZdbTbPogpWPj1EXCwFHYfHf5peieiViB_uhiuIBf_8NCB-ag6CTpIefcYUGz3XVhuFuCAf0Wo32vlpFUsLZ3Q7ZxM7upxKxv8haEEJJ6bXOWiu-fVCu8jMdT_b6aOEqZDADmb1ct7VJ-bs4LxLYB1PTpSUcvcf9McEjPcCcgNfyhTGprWztj1Pk1bzAqkRyQ4IBUeI7YiMfdwYG_3cYwRxOZvmGjiR8DpR-ORoGkIwHznY3GC7dn3U-OuMD3198sCp3GF4g7R8fIifrxkK3eCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bd28a2f5.mp4?token=sW7I3_QHrA1Ie6W566d83pyAHE5eWA77e5Ge91lih11kpVcqjD7SqkdkbPfAt2mJZdbTbPogpWPj1EXCwFHYfHf5peieiViB_uhiuIBf_8NCB-ag6CTpIefcYUGz3XVhuFuCAf0Wo32vlpFUsLZ3Q7ZxM7upxKxv8haEEJJ6bXOWiu-fVCu8jMdT_b6aOEqZDADmb1ct7VJ-bs4LxLYB1PTpSUcvcf9McEjPcCcgNfyhTGprWztj1Pk1bzAqkRyQ4IBUeI7YiMfdwYG_3cYwRxOZvmGjiR8DpR-ORoGkIwHznY3GC7dn3U-OuMD3198sCp3GF4g7R8fIifrxkK3eCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب متحدثاً عن قاسم سليماني: عندما ترى جنودًا يتجولون بدون أرجل، بدون أذرع، مع وجه دمر تمامًا، فإن 96.2٪ منهم جاءوا من إيران.
جاءوا من سليماني. كان هذا سلاحه المفضل.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79345" target="_blank">📅 10:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=c5rphsJp4PfbV4Lea0LLq3FJtk8fQGBiJp64czpKezjCpk8byo8FHpsdSd1Lz4cgSC0q23Zgl9UI91Yy7vbXCaEPYTfRGPK68WKaafyEuVQ9baFnWK0TUZHITJZP90H0DHHPDQ_R-L_y0OOr8sAw2owuqAWLyplCtIBJFXFZpbUQGbjhliwLvoSFxyAerdpD5oJA7zB5IgHOxPrRDeBaiYxPvv7RnTs795QLo-8H_wQsOP78deOdjO0LoZ37ntQi3jHpylVnW9heqOlrbMgOwMCRt_AdQQPo1gXLyCOfYNTQ8Zh-C7hSKj2LWp6MG9r-MRXwqH17tyUsH42Po2xVRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd20de2869.mp4?token=c5rphsJp4PfbV4Lea0LLq3FJtk8fQGBiJp64czpKezjCpk8byo8FHpsdSd1Lz4cgSC0q23Zgl9UI91Yy7vbXCaEPYTfRGPK68WKaafyEuVQ9baFnWK0TUZHITJZP90H0DHHPDQ_R-L_y0OOr8sAw2owuqAWLyplCtIBJFXFZpbUQGbjhliwLvoSFxyAerdpD5oJA7zB5IgHOxPrRDeBaiYxPvv7RnTs795QLo-8H_wQsOP78deOdjO0LoZ37ntQi3jHpylVnW9heqOlrbMgOwMCRt_AdQQPo1gXLyCOfYNTQ8Zh-C7hSKj2LWp6MG9r-MRXwqH17tyUsH42Po2xVRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79344" target="_blank">📅 09:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=LvCHADY_buJ7zi9DNcTu-f2-NfMHF3GQsqdVq_cU2RtqjD6F2gwC8daE-UzGT7iElyfmNFk0lZJwC-qYDNXUK9vUnxgQ7jdD-eLIpyOeUl7IPhX2pxlj56dMMFw1LXNejmWDCcAbGsd-JCwrbAMvypA2RMi_awr9ko5a2_KQ5Ig8uQhWR90atsWJ0AnuOe_KVp6ttIR6FVlsM_assvoGiBvbVgDdwFwT9Meo9MSDDc5QChGYD-oDWZW4emDXgAnFIzc5NLQZyu9yjOzC6xzylv-G_rtnuSRJBxjO_F3ypOYT6vddwqH6mR6AODYLmamTOrR_qDfVDHMY300k0ZVb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
لليوم الثاني على التوالي لا يزال الكيان الصهيوني يستهدف الجنوب اللبناني بغارات مكثفة وسط اشتباكات عنيفة في مناطق توغل جيش الاحتلال.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79343" target="_blank">📅 08:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIadepxijtF_dopx5NydMMbtwT5ipYRfHBuKjkwSFRNnY5DI8PvvoezFU6LDG7cDd4cJ-bJBBPvyazg8LvmusefkeLa7vwA3TjeHvYWHVAcxEFZBYM3anNgu8rl76a7vwWDrsG7Dt6ZMha5myaCrjRvQYz-I3v6QCMeHpzKXyIe2ynj5T9C-rPxPm1MpC7Lsi9hr0Neis2XMYP4IDpqDHtkdp0KfDimgNnraK3T6GStqKAhbcIrFTBLnTewxUcLkM9sghVsnoKtaJvEdeHWytD4xe22UPgBBsI2V9wW0UiSxpykL8z4NrnEMMRYT_ugvFf-kC6PTf0AXDwap7KSNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
انتشر قبل يومين خبر عن وقوع انفجارات في قضاء داقوق التابع لمحافظة كركوك شمالي العراق
وبعد البحث والتدقيق، تبيّن أن الانفجار ناتج عن عملية تفجير مسيطر عليها نفذتها القوات الأمنية العراقية لجسم حربي عُثر عليه في قرية جمبور التابعة للقضاء.
وحصلت نايا على صور حصرية
للجسم قبل تفجيره، ويبدو من المعاينة الأولية أنه من صاروخ كروز، طراز BGM-109 Tomahawk الأمريكي .وتعيد الحادثة طرح تساؤلات بشأن السيادة العراقية وقدرات الدفاع الجوي في مواجهة الاختراقات الجوية المتكررة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79342" target="_blank">📅 08:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
🔻
🏴‍☠️
إعلام العدو معاريف :
لسنوات طويلة، كانت إسرائيل القوة التي سعت جميع دول المنطقة إلى استمالتها،واستغلت تقنياتنا ومعارفنا، وسعت إلى التقرب منا، حتى وإن لم يكن ذلك علنًا. لكن مذكرة التفاهم هذه تُحوّل دول المنطقة بعيدًا عنا ونحو الشرق، نحو الجمهورية الإسلامية، باعتبارها القوة المهيمنة في المنطقة، والتي يجب الآن احترامها واسترضاؤها.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79341" target="_blank">📅 08:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puDWwjGRBo7CvHW74anni5xx7MLhJ_nm_k31pf7XmuVlUMYaOeto5OpsW1LscCiBAIvO-B1FwiWb02uJRr5ogvT649ZPLkhI9bkjZp9DytBfOh4gQrB-ieTCeUwf28Tmmtc0WL58f-n4-J2gjapJoep2jYuB4js1Hd7UP27y1o0cDMsZlUqCVt7bkr5o-EqzlAAMN87594N3NE4oOY1qTzno5CleoldCtMShP22bbQAwC1FUpwNK0voBpo7QuUaHw7GDZqHlZsyJm4Xp0QuLCMG2M6vJJKI6_gzq1pwuuFKADebFEpzcQY7V2tr97B_iQsXEm8g4jaH9Wsy4VBJd9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
ترامب متأثرا بتجربة حيدر الاكرع
تم تنظيف ٤٥ نصب تذكاري و ٢٢ نافورة ؛ مراسل ABC حاول تخريب النافورة من خلال وضع يده على مطاطة داخل النافورة فتحنا تحقيق بذلك !</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79340" target="_blank">📅 07:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7567afa506.mp4?token=OzZxpwH92O6KvrA6YgfNY3EwRUsb2i2n22J1LE7tJj-MrYgBfUCF53FZfjx_rgTxhkuWxg3WPO8rtQBZLa1p2tilkqDio3V-5VaXBGycsyRRUyvlYU3IKCRHWez2ZMa7MwPMdzcaoVgG4-ZDYGUk7qyIiQqHgRJ4_xIlk8p6z2efp7Qg7TiUvaUDpFv3q8p2FTdDUAaWl6deokcvDmcjNQuKpc_Bzkk-RdzYkWGuEZH0rcmbyDo45ZsZpglecSKg1HejDHIokjj99eihbgWbV007shqp7KiOPtLadE00D64OHSeS0lpkhytujdQzInWEKHIwL8OjVpuZ-3glGvJyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7567afa506.mp4?token=OzZxpwH92O6KvrA6YgfNY3EwRUsb2i2n22J1LE7tJj-MrYgBfUCF53FZfjx_rgTxhkuWxg3WPO8rtQBZLa1p2tilkqDio3V-5VaXBGycsyRRUyvlYU3IKCRHWez2ZMa7MwPMdzcaoVgG4-ZDYGUk7qyIiQqHgRJ4_xIlk8p6z2efp7Qg7TiUvaUDpFv3q8p2FTdDUAaWl6deokcvDmcjNQuKpc_Bzkk-RdzYkWGuEZH0rcmbyDo45ZsZpglecSKg1HejDHIokjj99eihbgWbV007shqp7KiOPtLadE00D64OHSeS0lpkhytujdQzInWEKHIwL8OjVpuZ-3glGvJyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/79339" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🌟
اشتباكات ضارية تدور بين مقاتلي حزب الله وقوات الاحتلال الإسرائيلي التي تحاول التقدم واحتلال تلة علي الطاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/79338" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmeAPWJtxELTC6lS0l3ceGA4VFUetx8Wff0bpe3Ex-_UHYQbLykQS8zPKljXKSDu4gb22UerSXoZWp0_Ceh7nChxE6U0jeaSuJ4ORxe57rUiU6yKohHEUhpBPjnmNHLYENoVcXUn1XWdKBBpp7ZJTBEMoOY-4EdStzxmOyxHMx3WQJjcd7cdvcwkwlZEbjz3Tzj1qHKhibevFQCnLBB5naxw_P7D8SYeI3RBRnvQahfTdzvNN5CJmt-VM2IknKKOPcv5268P_bObrtfkjbIE2Po8U2eGIUvJTeH4z1K56tXin_63kLYZWRoPiTc1lWhl1monVfaknmkHQkV7Ps327A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2tY94VB7GTXQCqgSd6d7ZUQbquXNrM7RS3ZYKLgVyyZKm5TIK1NUs1Yk-IecjaVclls2mjX8i4D_dBQg98rrNYxGtSP0zKCuKaIkpPiM_XO2W40FMysTfxWQIbX2Y6ygNVlS1h3I5ahYaPmDrFZrNAEVNUvgspDbCXuDW3q-ZosQM9C_8T_1ioZjNQeYxHuwkErqH9-CQMKHE6J98Whb0XYxwZ559xvF6Y06ip9jMfDaxndf4L3-MmAwoKLq-jU6oTfP1HLnVuL1I5l7FhHrj_v2V4OOuDd20_sEFBzPick09Mz4fHf52xLGAOTeO7hI3KohyYe8qwJBFYhc6aEbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">التحالف الدولي ينفذ عدة ضربات على بلدة دارة عزة في محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/79335" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=TBjawBME5-d7enY7lppcyPpfjp0UzUJXlvCdzIRxotAngDlQ7KZ37HQnTrXbuuOhXWOxJz9qMG8OxVTR4SQ7yNUTTqNPJrdqSCtPKMDvV-44DzpWyEnoWx4x8G_eQi_zXLXOlbt145iN0EH3V3_S_VDcr6u05hnAIUXunRd9wPczlucD9mJf3drq_sBl07zD6PumQwlrNkLoYhNV45_WYmIxOewkMYgmR8aORlmDIi3yG6mGsOuNnam9kRYatTgM-GDuUZwsHN5z9lPmpakZ6rL8VMWTfU0t5dybK5q5u-JynzmyZUt4byQjhnmatAJb13ZFPRKsDeEUWdBP9jOkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa1b4e7b2.mp4?token=TBjawBME5-d7enY7lppcyPpfjp0UzUJXlvCdzIRxotAngDlQ7KZ37HQnTrXbuuOhXWOxJz9qMG8OxVTR4SQ7yNUTTqNPJrdqSCtPKMDvV-44DzpWyEnoWx4x8G_eQi_zXLXOlbt145iN0EH3V3_S_VDcr6u05hnAIUXunRd9wPczlucD9mJf3drq_sBl07zD6PumQwlrNkLoYhNV45_WYmIxOewkMYgmR8aORlmDIi3yG6mGsOuNnam9kRYatTgM-GDuUZwsHN5z9lPmpakZ6rL8VMWTfU0t5dybK5q5u-JynzmyZUt4byQjhnmatAJb13ZFPRKsDeEUWdBP9jOkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79334" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=FKDwRChpgUA5byYLU2yUuogJpf2hyy_rPJll6LiiVUmylmxoxKIs8SZv9qrXH2t3TfmTb-yJQf8FlZVBqq0F3aESuza6Zk1BZp-b_ExlOd8UppmsNaYQkvTIOvmApxZON_3PGAdHQvPuLl8_MqyBvOlUtKOIOPQXEbergXmZqGH1FEiOfkkUllqmxauf6piyptdC45jxDWIq3jercH0_oDowU_2OjhZR6u2b1W7GL4CIAyBqRfUPjUSEHX6oHonEF4hGndNhw79kpkRc6p9IMESW_VbRnVtn3dMMVc6kyEIK2221JymodmIJQo5IuhfVVQC-y3UpNX_qcmM9EaA0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d41c5588.mp4?token=FKDwRChpgUA5byYLU2yUuogJpf2hyy_rPJll6LiiVUmylmxoxKIs8SZv9qrXH2t3TfmTb-yJQf8FlZVBqq0F3aESuza6Zk1BZp-b_ExlOd8UppmsNaYQkvTIOvmApxZON_3PGAdHQvPuLl8_MqyBvOlUtKOIOPQXEbergXmZqGH1FEiOfkkUllqmxauf6piyptdC45jxDWIq3jercH0_oDowU_2OjhZR6u2b1W7GL4CIAyBqRfUPjUSEHX6oHonEF4hGndNhw79kpkRc6p9IMESW_VbRnVtn3dMMVc6kyEIK2221JymodmIJQo5IuhfVVQC-y3UpNX_qcmM9EaA0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الطائرة F-47 قيد الإنشاء الآن. لديهم خط التجميع يعمل بالفعل.  يقولون إنها أعظم آلة قتال تم تطويرها على الإطلاق. سنكتشف ذلك.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79333" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHonH4Bh6v-gWVr3CwUJ377g2A-YlaBzMH78j1WYt58Q-ZHCRe0U5ilI0jmCIVuPbPT8WDmMzKzhdojhKGZgzVzlX_bIbobZ-E9unjJoPcbsuLWUO3541y_dVx0K3g_w9wJDLFqwxzv0DER-No8fiTJc47y9KxFWTLSzSXxpyosk1FFVva7vm4D4vkd8pMgxpn626DJqXgDIxn48CwXSI2r5jA650HN7dQk8Jm8csCV8pTP7tQr470Oh6Pmf6wGg59p9ynPFHrKUwE76pyZTAYxODoKu6sCwOzuWlClWyMcKaHnQPDM4exUoof8FKeuJPTFn9GGsNWUGHh2KkYSi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي عدة انفجارات في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79332" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642865aff3.mp4?token=uyzW-9KkLXsITSPeiagyLtcHGljwvFtrfL8-jfgw534SDiKKShRz3eO-niCkcjBR-4WTOlJTzj77qAB9PXKER01P_JnJZA-g6hcXoQeBJwpV4hq_CgIg8N0lYhj4vRQa0ITIw1TwnrDpKiyA68cmf4dNWp-I7GvZ5r3HQ_5kcQKR-yBNNH2vX3hBWLl4x4mngC2TUUs07i-UuYj6TbXnkkwoU9-tHBsDN3aCkqbAI8gmkRR9chuBDBhNwd5qZIUMLrskNuZIUDzbBojn1S5DVjJYh8S5w6BPQN7gu3VixETErGts4wm0SlIV0RQAf1lB9jVr2mOwPajcyrr6XmOkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642865aff3.mp4?token=uyzW-9KkLXsITSPeiagyLtcHGljwvFtrfL8-jfgw534SDiKKShRz3eO-niCkcjBR-4WTOlJTzj77qAB9PXKER01P_JnJZA-g6hcXoQeBJwpV4hq_CgIg8N0lYhj4vRQa0ITIw1TwnrDpKiyA68cmf4dNWp-I7GvZ5r3HQ_5kcQKR-yBNNH2vX3hBWLl4x4mngC2TUUs07i-UuYj6TbXnkkwoU9-tHBsDN3aCkqbAI8gmkRR9chuBDBhNwd5qZIUMLrskNuZIUDzbBojn1S5DVjJYh8S5w6BPQN7gu3VixETErGts4wm0SlIV0RQAf1lB9jVr2mOwPajcyrr6XmOkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: إذا كنت سأضربهم الآن، إذا لم نكن سنضع قوات على الأرض، وأنت لا تريد وضع قوات على الأرض، أليس كذلك؟  إذا لم نكن سنضع قوات على الأرض، فمن المحتمل أن نفس الأشخاص سيذهبون إلى أعماق الكهوف. يطلق عليهم اسم "الكهوف الجرانيتية". إنها قوية للغاية.  إنهم يدخلون…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79331" target="_blank">📅 23:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سماع دوي عدة انفجارات في محافظة ادلب السورية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79330" target="_blank">📅 23:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🌟
حزب الله يفجر عبوة ناسفة استهدف قوات العدو الإسرائيلي المتوغلة في منطقة علي الطاهر، ما أسفر عن وقوع إصابات في صفوفها، واشتعال النيران بالياتهم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79329" target="_blank">📅 23:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCBb1zOt09YGU1YYzNs3b_EiT0taRMk0ClOgOauAtbldc2qBz1otwPAh4QqP9Soe_in1rxlUDqZntTiLoFUz8ILKd_Zd6FmDe0Xzl-MfWBdod7G-lggAISIwUK7E9ViOf3YQY64aHUQLKJJhv2sW88pD4bNUwx_ft6pa7dTGck2xIlYZewo3hwr0F782DuRRL9KnuQ-ybgvR9qbZMkTX4BrzlOiW0IsYPemVW4WSffrFhmmpDvQTgnsbKH3rK805lREf_s44XeLtYY2sJ0eR8qbHCmFDujJF5682XrMbMFyfek4w-KzlTPchgdSJ1ZzavzBW7uajPB8KuUZLeUo_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف بالقنابل الفسفورية يستهدف بلدة النبطية جنوبي لبنان من قبل الاحتلال الاسرائيلي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79328" target="_blank">📅 22:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ8ZVwu3FD37v7V3Td-sDtbqiXwMFsxoS1wcMhqWK4JS7FFlQv7y9qOjltmpA3pVtoC82lTLyLt61_ZrhNTi45HyXzfpU8Ogibr1uKY8A4InSQVvxe4vY9QNPoR7QaKB_qMLhnamsZN_Xk0SUAbAz2Ifa-n4LbpOwNBPnsS2PJXm1WWVcQjzgpM-L2U73RtlYmqV9HR-_PTLAT5f8rKBPYPmkyG4g_AXow4l3_S_F4cdQKIpEAUXX4C2LmAr-_9xCkOPn9ucgbnLzx0tkFADrbBoqFRMz8q7ieFtLRZdeH2DLJoYZWfhfHlMvu-axWqzy_z0XWhnBIrqt1_P-luASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصف بالقنابل الفسفورية يستهدف بلدة النبطية جنوبي لبنان من قبل الاحتلال الاسرائيلي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79327" target="_blank">📅 22:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945fd8656b.mp4?token=G1sqgLW9lR41l1lktLAZJ9sbXum2AoVGDB9ZFIFVoBN4akIMdjKM2uOyXjgT3wlo6KVqdJsNV4SluUmN1TimRV-f11c-p2z2tET2bbuMak4p6tqI4L12OOdrQ42PHkY9DRoRYqxTGD2-Vt9k_5zHo9A2Qs1K84okMrjfHr6rB_JYrEwHOvR5_OIHoIQ-O-eg-zu8c0tP_3qb9E5Ip3DclFTcN7nSqAq70xFDZPclTBnL4KIAMMV3-6jvvJ-HIAQkRYigJBv7azyaFaI3A20oB9LqURscUIvUcBrvAJgjS377tH1_tjHkFFuohvYNvP1af_JkrIDdi8z0ePmpZp-5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945fd8656b.mp4?token=G1sqgLW9lR41l1lktLAZJ9sbXum2AoVGDB9ZFIFVoBN4akIMdjKM2uOyXjgT3wlo6KVqdJsNV4SluUmN1TimRV-f11c-p2z2tET2bbuMak4p6tqI4L12OOdrQ42PHkY9DRoRYqxTGD2-Vt9k_5zHo9A2Qs1K84okMrjfHr6rB_JYrEwHOvR5_OIHoIQ-O-eg-zu8c0tP_3qb9E5Ip3DclFTcN7nSqAq70xFDZPclTBnL4KIAMMV3-6jvvJ-HIAQkRYigJBv7azyaFaI3A20oB9LqURscUIvUcBrvAJgjS377tH1_tjHkFFuohvYNvP1af_JkrIDdi8z0ePmpZp-5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: لو لم نضربهم، لكان سيحصلون على سلاح نووي. كانوا سيستخدمونه ضد إسرائيل. كنت ستستخدمه أيضًا في المملكة العربية السعودية.كانت الصواريخ تطير على الفور تقريبًا إلى هذه الدول الخمس الأخرى [قطر، الإمارات العربية المتحدة، الكويت، البحرين].  قلت، لماذا يفعل…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79326" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
ترامب: الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79325" target="_blank">📅 21:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
ترامب:
الإيرانيون أشخاص أذكياء جدًا. إنهم نوعًا ما من عبقريين بدائيين، لكنهم أذكياء. كانوا سيفجرون إسرائيل. لولاي، لم تكن إسرائيل ستوجد اليوم.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79324" target="_blank">📅 21:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران: كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.  هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.  لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79323" target="_blank">📅 21:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juaPOwDIKXwQQO9p0jJ5VLhkA8y4xlFKHGd6v5HFVa58orMJnfNNrzkHiN6b2hTHf32i0DsZS6gLfT1zNdWc5G4CaDOobjcBW3wQ-F7pB8wYECklXaNEQQci4V_C1n_H69x7jUhHH5WB06uPa0IDLFeFkD1YhKQqFL1NrlpVMob7lV1IvKajwYKzjLd_uxpqcLcTdqDTIHz_CUROuoy4p_g0j1E3YOcrqKjdiDdIQt2o20ibY41W8mobcgkm5Nt1jvAASF57eav8gXc-JSMataPISRytxHBZAl8kdUVr4hCesAnLr2RIILcUe1qsABwKcq5vMsg-86Kc7RZ7CBKDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني اللواء قاآني:
بسم الله الرحمن الرحيم
عندما قلنا إن حزب الله يمتلك المرصاد، لم تُصغوا، فوقعتم في الفخ؛ من سيُحاسب على المئة قتيل؟  غزة أيضًا لديها طوفان. إذا تحركتم وفقًا لرغبات سياسيكم، فستقعون في العاصفة. كونوا حذرين.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79322" target="_blank">📅 21:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🇮🇷
أوباما حول اتفاق ترامب مع إيران:
كان هناك اتفاق توافق فيه إيران على عدم تطوير أسلحة نووية.
هذه الإدارة - أو نسخة سابقة من هذه الإدارة - انسحبت منه، مما أدى إلى قيام إيران بتطوير المزيد من القدرات النووية.
لقد خضنا حربًا الآن، وأنفقنا مليارات ومليارات من الدولارات، وفرضنا ضغطًا هائلاً على جيشنا، ومات الكثير من الناس، ويبدو أننا عدنا إلى المكان الذي كنا فيه قبل بدء الحرب، بل ربما في حالة أسوأ قليلاً.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79321" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79320" target="_blank">📅 21:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
🏴‍☠️
جي دي فانس حول الكيان الصهيوني:
إسرائيل
شريك جيد بنفس الطريقة التي تكون بها المملكة المتحدة أو فرنسا شريكين جيدين.  هذا لا يعني أنه سيكون لدينا دائمًا مصالح متوافقة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79319" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0534464594.mp4?token=sfPCwSb2GpqkXW9XF8ixkfOchJUyAPs3OkjmXzuJx7-nAK9SCgIzVnP9ZjXunNJUUaIYDJztg1BTgUSQtFLqsc3bIvmFP6vOAN3nfmwfnpFZxKzWX2vdZ5A2uvpoxmg5AL4WzEyV5EossJpAOeFvlKsVPuH2EoRG7lF0m0tVjU_nUGNXDJOGY4SWsAQDO1KSxxfdAI_jF_6hElMMeCiDK-F3isfu7ll_v1Fe8tEV8LKRpcJmE--x7xjtqA__ztYFx-VKrc7ljzhrKBlhBIhzAfEWbtWJL6-7zDEeOATvZFhsGJGhWMPWqv2YqtwLBb52yp6XzVaW7ngFzZgy6yCuzGE8xyJd7ZXbguQWLDKQgIIYc3RfPtz6IDeQqnEVjuvGg8Ocy1b2X4sR_WdWoBjRD6DiBbE25reP6Z_vobYt2OsmmCJLlH_iZw_4dtdnTR5UWy6Vyez5_uoSmrOoK66sn3HBTgsxjhdAZan7LSjHmygjOanikUaHowyJQLPiFcaht4VJzVQoxPMhVkF2wuNFZGMZ8K-3FPTahCSbl10otoli5alpcF95bnxazqRPWBZSDGjv01DYBgXMtrhwvX54yfA35Rh5q6dRzk3Fb8OEMIkVpTSZtPQTKQJdOdTu6IzUmZVuEiQMxczTMUYjuMrGNVeCum-cVMysYLkFBiW-aqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0534464594.mp4?token=sfPCwSb2GpqkXW9XF8ixkfOchJUyAPs3OkjmXzuJx7-nAK9SCgIzVnP9ZjXunNJUUaIYDJztg1BTgUSQtFLqsc3bIvmFP6vOAN3nfmwfnpFZxKzWX2vdZ5A2uvpoxmg5AL4WzEyV5EossJpAOeFvlKsVPuH2EoRG7lF0m0tVjU_nUGNXDJOGY4SWsAQDO1KSxxfdAI_jF_6hElMMeCiDK-F3isfu7ll_v1Fe8tEV8LKRpcJmE--x7xjtqA__ztYFx-VKrc7ljzhrKBlhBIhzAfEWbtWJL6-7zDEeOATvZFhsGJGhWMPWqv2YqtwLBb52yp6XzVaW7ngFzZgy6yCuzGE8xyJd7ZXbguQWLDKQgIIYc3RfPtz6IDeQqnEVjuvGg8Ocy1b2X4sR_WdWoBjRD6DiBbE25reP6Z_vobYt2OsmmCJLlH_iZw_4dtdnTR5UWy6Vyez5_uoSmrOoK66sn3HBTgsxjhdAZan7LSjHmygjOanikUaHowyJQLPiFcaht4VJzVQoxPMhVkF2wuNFZGMZ8K-3FPTahCSbl10otoli5alpcF95bnxazqRPWBZSDGjv01DYBgXMtrhwvX54yfA35Rh5q6dRzk3Fb8OEMIkVpTSZtPQTKQJdOdTu6IzUmZVuEiQMxczTMUYjuMrGNVeCum-cVMysYLkFBiW-aqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79318" target="_blank">📅 20:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي: ‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب: لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79317" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
🏴‍☠️
إن بي سي:
‏تحدث ترامب مع نتنياهو في وقت سابق من يوم الجمعة وطلب منهم الموافقة على وقف إطلاق النار مع حزب الله.
🇺🇸
ترامب:
لطالما عاملت نتنياهو بشكل جيد ويتوجب عليه فقط الهدوء أحيانا وإعمال العقل.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79316" target="_blank">📅 20:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">أضافت فرقة العمل المعنية بالإجراءات المالية البوسنة والهرسك والعراق إلى "قائمتها الرمادية" للولايات القضائية التي تتطلب مراقبة متزايدة بسبب أوجه القصور الاستراتيجية في أنظمة مكافحة غسل الأموال وتمويل الإرهاب.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79315" target="_blank">📅 20:22 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
