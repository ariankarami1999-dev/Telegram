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
<img src="https://cdn4.telesco.pe/file/c6bgWZKLl8jSUnsCo1oVwaH0It2mO_wYOtbpjQBQzZWTcvoZje5QbHoFDobzhJirjwNBITW5vtRkXF2_1ev7cZJ4CnUmx_Drx414jlRSr4tYVfB-3E6KhsrvmF-IFDNvx28wnWMy6XGipsTusLcSqI4aiV-Fqe4M3e6_fVVGDoJWy2dpNOPPNlWY2Jd_QfmlZpSpxVkua2YQj49SK8xHArCm0STzIdbqBc7cjRUBR9RByeh4N5RlMQmpYg3YF8FKCUO4hw6k5HLtGkLO1HWFUJX719xEd9Jxt0ovzlNujDdJroLjlaGUs4ho5XTjPibBEOzZA5qsurlD05_1N-Zr4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 03:19:38</div>
<hr>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
كعبة الأحرار كربلاء المقدسة حيث ينطلق معنى الحق ومذهب المقاومة ومنها تُستلهم قيم التضحية والكرامة والإباء لتبقى منارةً للأحرار في كل زمان ومكان.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/79894" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/79893" target="_blank">📅 00:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/79892" target="_blank">📅 00:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
خيارنا بالعراق هو خيار حسيني،،  المواجهة مع أعداء العراق والإسلام وشعار هيهات منا الذلة مثلته ثلة عراقية شريفة رفضت الذلة والخنوع والخضوع امام مغريات يزيد هذا العصر
السلام على فصائل المقاومة العراقية الشريفة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79891" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9-UJyXzVY5HeHsTlROalP89boAjKIdUTxy9_Kvzd0yTJQ1shiMsof6JwUn93wE1hC76sJ7C5AREUvVoAC4DpA9_Hpb1nBKoXacjwJ_0A_1ZaTJPwxuc-ea7CjYmaouy-tpI1UABUNm3ZoEH7SBtJS1qJwPx6Mnqq9ZWAJYYZf4w0D9oqNgT-MChUT5aCydtO6GG9y0gm-_r_aVony1MgCiWKnIHJIdBHp_p1ioYVk4lrXhqXOvKEbxp4j0D1-R5IHP3Di2zB7-G4mY9doXBzgX_h0JqHDRG3egVU7deIYzkTpn3KLLniwTY4f404R94PfKh5wO1o3EX5jNyM4tFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة إدارة الممر المائي للخليج الفارسي:
🔹
تقع المسؤولية الكاملة عن أي تبعات ناجمة عن الإبحار عبر المسارات غير المصرح بها على عاتق مالك السفينة ومشغّلها وقائدها.
🔹
إن أي حركة ملاحة خارج المسارات المحددة من قبل هيئة إدارة الخليج الفارسي (PGSA) لا تشملها ضمانات العبور الآمن، كما أنها لا تتمتع بأي تغطية تأمينية أو التزامات قانونية مرتبطة بذلك.
🔹
وتبقى جميع النتائج والتبعات المترتبة على استخدام المسارات غير المصرح بها مسؤولية مباشرة لمالك السفينة ومشغّلها وقائدها.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/79890" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR7Icv65bF0nYoNE-2azeFhgEFTq4HRu_scjxTSFx2Piu40GH3dwZ1QkB2IWqSkoAOKV7WoL1R0UnWnvvWnsidTVdwt0ou81uYKVnOrsPLAtcDOWyTyeBbc7dpFUAYfU38P2CVQp2Iyf6MKGke8TKBJRDKJHZLJQFrVcZbLU3l49o595zMSoUJz4shQ5Ei3FRGZ24R92YIpSKhw8tJ5iQK2ghENRYdvJt6LnW5YJop9gxgqzToJ3qHHwTjST1aFwBgpyxaZ5nlPIxfdy8IOYgoxxkBmX4czyEg1A3h0KGXLcR8dNwSMtvrYm2jki5ufRfQ1LRvglthNJabnIyT3Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/79889" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79888">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/79888" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReAWYI448nJfvGRf_zcZObCBtvAc4exsDdfVXJb_Gek2YUNxQiQ5xK7EWcNTyQRP9GN_nw8awmxx05HPxZaMmwCUUup_uQrP7JMMKHbLcnaJh-_0W4lBazFzcO4Wm3BatiRamC8c__X84Tv4GG91BbKw8Xs-bCoxs47VVGXMMaUVIwGgDtff8KOJDidvmvho4FHJda4KYQouBEZrQxnd0w14kjboHziv7wOothE_bwI8ZtZ8UOyU8Xv7KRUAIe6vV8VljTpLa2HxP4dO3OsWkEBztgHAzl91vq3ohzeE8IDitM6QGvFYIpCHkq_MlA-GgEUGTx2Ta2o8j3-PJ-oq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
مسؤولين أمريكيين: الحرس الثوري الإيراني هاجم اليوم بمضيق هرمز سفينة شحن ترفع علم سنغافورة.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/79887" target="_blank">📅 22:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79886" target="_blank">📅 21:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79885" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79884" target="_blank">📅 21:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇹
🇮🇷
‏
رئيسة الوزراء الإيطالية ميلوني:
لم نشارك مطلقًا في حرب إيران ؛قدمنا دعمًا تقنيًّا ولوجستيًّا فقط.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79883" target="_blank">📅 20:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
🇮🇷
وزير الطاقة الأمريكي:
رفع العقوبات عن نفط إيران يتيح لها بيعه في أسواق أخرى وتقاضي الثمن بالدولار.
أموال إيران التي سيرفع عنها التجميد ستخضع لرقابة صارمة بشأن كيفية إنفاقها.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79882" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-06-2026
تجمعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79881" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
هبوط اضطراري لطائرة هليكوبتر الرئيس هرتسوغ في قاعدة بلمحيم.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79880" target="_blank">📅 20:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭐️
‏
بيان خليجي أميركي:
إدانة هجمات الفصائل المدعومة من إيران في العراق ضد دول الخليج.
السلام بالمنطقة يتطلب التصدي لتهديدات إيران بما فيها صواريخها ومسيراتها ودعمها لوكلائها.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79879" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79878" target="_blank">📅 20:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
مصدر مقرب من الفريق الإيراني المفاوض:
انسحاب الكيان الإسرائيلي من الأراضي اللبنانية المحتلة يُعد أحد شروط الاتفاق النهائي، كما يعتبره الفريق الإيراني "خطاً أحمر" مهماً.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79877" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=cg7MspjH3PuAmUOL2pkWx3Tcfk_wrmGynlfN8yD3fUK5zY0O2XVuG8RttJaYvzKDXYfXu6wBHZ9lSfKfCotEVlpkj3eH1g-TcaC--dJgwx40dMd373Arf38Y4JWJLLbJAnR3IUA_8ccn1NbLusohTnxkVEGHhWekUJpeK9jxG4-fC7snP014HNCNe6BVNPwcXM3Rrk6jWyASfMP4h5JALpb5_qOyRxZS053poJ2XyYiCJww6bk5tAZzEDEl-CCzoxW5jF9YIs6cYOUFXtUK75JSTfm9Mu0RAk8EfrjCOckYt_LkIYoEZ7v3xjgCvDQV8brGtqGRzCzZRj7-KGiI_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=cg7MspjH3PuAmUOL2pkWx3Tcfk_wrmGynlfN8yD3fUK5zY0O2XVuG8RttJaYvzKDXYfXu6wBHZ9lSfKfCotEVlpkj3eH1g-TcaC--dJgwx40dMd373Arf38Y4JWJLLbJAnR3IUA_8ccn1NbLusohTnxkVEGHhWekUJpeK9jxG4-fC7snP014HNCNe6BVNPwcXM3Rrk6jWyASfMP4h5JALpb5_qOyRxZS053poJ2XyYiCJww6bk5tAZzEDEl-CCzoxW5jF9YIs6cYOUFXtUK75JSTfm9Mu0RAk8EfrjCOckYt_LkIYoEZ7v3xjgCvDQV8brGtqGRzCzZRj7-KGiI_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مواكب المقاومة العراقية البطلة تجوب شوارع ميسان.. إنهم رجال الفارس الكربلائي أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79876" target="_blank">📅 19:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌟
🌟
قوات الأمن السعودية تختطف مواطن عراقي من محافظة البصرة أثناء أداء "مناسك العمرة" وتقتاده إلى مكان مجهول عقب نشره صورة "لقبور أئمة البقيع المهدمة" على إحدى برامج التواصل الإجتماعي!!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79875" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAtsP6ilQZbSDzX6paEWwWh1chu5eqUcR59Fu03vWKX4lZg5yKb8g0UNJyNiN0zkn4lxTCuSYGzZQcC1Mha3vvsj45uMRX85SP6RL8zLfpqO66IZkiRq9EAfpiKv7-ESmW01OGkvZU5vk93u0rkrDlYOKk0cix_r3XwyOhk01Ivvwqn7Z6uWLbX307GIvE-Xuhg5vjAJH1YeF2xEv0tRPg4xFz_9iXtxs32UR3d6qBLB7HncN3JnNoUZ3p_v8y5xsoOeFPdCScEJZNDb7g4wpMJ8AA2k5DL7_GbpyP4yRw4hUXUERjtXbtPP0o3vKnkXDOo9gU1tqS1F7jF-FB2o5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأمين العام للمقاومة الإسلامية حركة النجباء "الشيخ أكرم الكعبي":
سيف يزيد المعاصر سينكسر أمام القبضات الحسينية، وراية الحق ستبقى ترفرف فوق قمم الانتصار.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79874" target="_blank">📅 19:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/79873" target="_blank">📅 19:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
المعارضة الكردية الإيرانية الإرهابية، ماتسمى"وحدات كردستان الشرقية" تزعم تعرض مقراتها بالقرب من الحدود العراقية الإيرانية إلى هجمات بطائرات مسيرة صباح اليوم.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79872" target="_blank">📅 19:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=l5rEXFeZdF25Yd_tO8kYbMP0VQ4jFg9-sJib3dO42fuR62DOZNu5X59yR-zJi2VBZKJ8qw5PKKpFPC2vz4q_YZOhcX326JxmPGPKx1XoPr6jTJkP_50A9eJXIIXFvrwiBMw703jcbdOiBu0_AHzt1Gmr-Mfxmcyh0F-nIU6GS8zCimX0SiqSsc_pY8Ij79N3Abb0WKFYlHp4MIlGYuQWn0bxJAwtc3SNUmPQvwkITguX7f75041vY8cvxAInfFO9jNY-oXu00ElmnRdCQClFj2cI11GJGUjkinOq5M9kOc-YiFmdeCXCslQRGPHVNWwk25AwpByPWAhgbo0aNauQNFnDn3V0SFqtZcb9T2xk65iWJM1EmtD0mAVEB2gvMf_2lS3JtGlka9ps6VDEPMKUq2mwMrN8zfKRszqwlbKwFadq6CTnrcH8iHNehZJrNfJWuRcphTCE1DPd-yM4-WvshDt41P-eV0s25Z3xK7rJRC88kY11O1kilGbrbMU9CsjGGPbBzr3hhPL2fL6I1_RNOd5RHElyZYdfy5ioFkFbaJyp9bpBt6njOxC1J0-2H5rhAK1YQ9tZ3ZrXE2Ic5t_B1dLlW1dm-e2hHmjqyHr4A0crp2oESo-188hcAMp2i20j7q_1EVtFUx4UkqbESJEDyP0tkYr60Gwz4TPM_bqsNvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=l5rEXFeZdF25Yd_tO8kYbMP0VQ4jFg9-sJib3dO42fuR62DOZNu5X59yR-zJi2VBZKJ8qw5PKKpFPC2vz4q_YZOhcX326JxmPGPKx1XoPr6jTJkP_50A9eJXIIXFvrwiBMw703jcbdOiBu0_AHzt1Gmr-Mfxmcyh0F-nIU6GS8zCimX0SiqSsc_pY8Ij79N3Abb0WKFYlHp4MIlGYuQWn0bxJAwtc3SNUmPQvwkITguX7f75041vY8cvxAInfFO9jNY-oXu00ElmnRdCQClFj2cI11GJGUjkinOq5M9kOc-YiFmdeCXCslQRGPHVNWwk25AwpByPWAhgbo0aNauQNFnDn3V0SFqtZcb9T2xk65iWJM1EmtD0mAVEB2gvMf_2lS3JtGlka9ps6VDEPMKUq2mwMrN8zfKRszqwlbKwFadq6CTnrcH8iHNehZJrNfJWuRcphTCE1DPd-yM4-WvshDt41P-eV0s25Z3xK7rJRC88kY11O1kilGbrbMU9CsjGGPbBzr3hhPL2fL6I1_RNOd5RHElyZYdfy5ioFkFbaJyp9bpBt6njOxC1J0-2H5rhAK1YQ9tZ3ZrXE2Ic5t_B1dLlW1dm-e2hHmjqyHr4A0crp2oESo-188hcAMp2i20j7q_1EVtFUx4UkqbESJEDyP0tkYr60Gwz4TPM_bqsNvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
لن ننسحب من لبنان ‏وأمرنا الجيش بالقيام بكل ما يلزم لحماية سكان الشمال.
نحن في ذروة حرب إقليمية متواصلة لا تقل عن حرب الاستقلال.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79871" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭐️
حادث وقع على بعد 7.5 ميل بحري جنوب شرق داهيت، عمان. أصيبت سفينة شحن على جانبها الأيمن بمقذوف مجهول، مما تسبب في أضرار لجسر القيادة.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/79870" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭐️
​
ضغوطات لحركة طالبان ضد أكبر مدرسة دينية شيعية وقناة التمدن الفضائية في العاصمة الأفغانية كابل..
وفقاً للتقارير الواردة من العاصمة الأفغانية، تواجه "حوزة خاتم النبيين (ص) العلمية" و"شبكة التمدن التلفزيونية" ضغوطاً ومساعي من قبل حركة طالبان للسيطرة عليهما أو تعليق أنشطتهما، واللتين تُعدّان من أبرز الميراثين العلمي والثقافي  آية الله الشيخ محمد آصف محسني (رحمه الله).
​نبذة عن المؤسسات المستهدفة
​مدرسة خاتم النبيين (ص) العلمية: يُعرف هذا المركز بأنه أكبر مدرسة للعلوم الدينية الشيعية وأكثرها تجهيزاً في أفغانستان. ولم يقتصر دورها على تعليم طلاب العلوم الدينية فحسب، بل لعبت دوراً محورياً في التقريب بين المذاهب الإسلامية والحفاظ على الانسجام والتماسك الاجتماعي في البلاد.
​شبكة التمدن التلفزيونية: تأسست هذه الوسيلة الإعلامية المرئية بهدف نشر معارف أهل البيت (عليهم السلام)، وترويج الأخلاق الإسلامية، ورفع الوعي الديني والثقافي. وقد نشطت لسنوات طويلة كواحدة من وسائل الإعلام الرصينة والمستقلة في أفغانستان.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79869" target="_blank">📅 18:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحين تابعين لعصابات الجولاني الإرهابية، ترفض عودة الأكراد إلى مدينة رأس العين ضمن محافظة الحسكة السورية وتتوعد من يعود إلى المدينة بالقتل.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79868" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79867" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79866" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
تسعى إيران إلى كسب مليارات من الدولارات عن طريق فرض رسوم على السفن لخدمات الأمن والسلامة والبيئة في مضيق هرمز بعد الحرب.
تقول طهران إن الخطة يمكن أن تدر ما يصل إلى 40 مليار دولار أمريكي سنويًا، وتريد من الدول الخليجية المجاورة أن تشارك في الإيرادات.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79865" target="_blank">📅 18:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQo20yPgUw0NvLg2u6AseV14lHMwcv-HnzOs123KXveFQYPrdX4GZcWZeF2B8xT4E3Za_FB3I4SoKEJ1LqOS7u6jmDgxopENsy0P8Chy2_PMeV9jERl28x3dbIlHM5CrjwAkhmAK7V5i_FUlFsN6fDVqp7SMwyxUvk2bJrdLEEQ_M5i1lGBLxKebw9MQKbn3iccZw8so3rVpaoFR6Cg3dWLtZcJUlL2xfKyhDRRJicx2baQCNRsUUQOuJzXuUNJrC52gS19VOVaeLp8rP5tu7T3_hoHDVUkwHwI_39DI4GRnxcJZfq-YDT5mBVgreRHy6bb91hYz8JQhw-cLezjGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUkkImm8Jkfk375WL7REgRV0pEH9cAfY4d8oxy9vXfnhcPxsQlAFtIHPbdKCo-9i9EyhXZ3w9SlTeXxgXDVfYofGi6TrRhdprDg3uWrvCwoEwMHvIKzwpZCV_-IIRURCj6ewJBMFxmmceOr0CyG0NoRrZYjCpeYqOYPxqwvFAtFjIlN_D7gC5KcvDvLJtENgnxCdqjkIUsgWErAlSW2OpGmoR9iEC8SQ_l5kJHqkfJZH6xMCHTNJxG-YjRkCM3lAycQ4mVthEsNPcQfoZpRzD5gUvkbO7770m6WEYje6s-nAmmXRne4p427SlcVWCmATNH_-t-X_F76Yo-_bREj-1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء "عبدالقادر الكربلائي":
إننا بعون الله لن نحيد عن درب المقاومة، ولن ننساق وراء تخرصات الأعداء وأوهامهم، فسلاحنا سيبقى مرفوعاً بوجههم وراياتنا خفاقة ما دام فينا عرق ينبض وسنبقى مقاومين حسينيين لن نتراجع أو نساوم إن شاء الله.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79863" target="_blank">📅 18:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79862" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79861" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79860" target="_blank">📅 17:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
نرصد بكل اهتمام مجريات الوضع في أرض الصومال وما يقوم به العدو الإسرائيلي بهدف السيطرة على خليج عدن وباب المندب والتحكم في البحر الأحمر، نحث الدول المطلة على البحر الأحمر لموقف مشترك إزاء نشاط العدو الإسرائيلي، ولن نقف مكتوفي الأيدي أمام أي تمركز في الصومال وسنبادر في أي وقت لاستهداف أي نشاط للعدو الإسرائيلي في أرض الصومال.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79859" target="_blank">📅 17:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79858">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقتل ضابط بجهاز المخابرات العراقي برتبة مقدم في العاصمة بغداد بعد اندلاع اشتباكات مسلحة في منطقة المعالف</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79858" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
✊
العراق يعلن تسجيل تحفظه على بعض فقرات “إعلان باكو” الصادر عن الدورة العشرين لمؤتمر اتحاد مجالس الدول الأعضاء في منظمة التعاون الإسلامي المنعقد في العاصمة الأذربيجانية باكو
العراق يؤكد تمسكه بمواقفه الثابتة والداعمة للقضية الفلسطينية وحقوق الشعب الفلسطيني المشروعة، معرباً عن تحفظه على الإشارة إلى “حل الدولتين” بصيغته الواردة في الإعلان، انسجاماً مع التشريعات والقرارات الصادرة عن مجلس النواب العراقي الداعمة لإقامة الدولة الفلسطينية وعاصمتها القدس الشريف، وضمان حق العودة والتعويض للشعب الفلسطيني.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79857" target="_blank">📅 16:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79856">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
السلطة القضائية الايرانية:
أن الادعاء بـ"حظر ترديد الشعارات المناهضة للنظام الأمريكي وحرق علم الحكومة الأمريكية الإرهابية في التجمعات" ادعاءٌ باطلٌ لا أساس له من الصحة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79856" target="_blank">📅 16:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79855">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇷🇺
‏وزارة الخارجية الروسية تستدعي سفير رومانيا وتعلن القنصل العام لرومانيا في سانت بطرسبرغ شخصًا غير مرغوب فيه وتعلن اغلاق المكتب القنصلي الروماني هناك ردًا على إلغاء بوخارست موافقتها على القنصلية العامة الروسية في كونستانتا وإعلان مديرها شخصًا غير مرغوب فيه.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79855" target="_blank">📅 16:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDuIm4lBl14uBYCiM0bg4NtUQRyJsJctjff4qRvhpWJv238_WRv7sEH5hapQPyC91BHhE57gIH5WiosWsfcshjrgFA3s_lF43qJD_mUdh8m9bNLxBjl6QPXhwuqiZuokOBSBWL3cxHmHmUYww6pyfGK8aOeFOK1aIBV6pP-hONQAy0P3SgGX1Jh_v_zmyW9IGer0Udd3LXGzBT2rhY_W-OzmhmbkIL2VdWS4pz-7KPXCwmb9_3gKuhuAoq-c72c3HS3mj9eSgW74uPfkDXn0KmNLkhSDaX6JXW5_UtQywwxDQQAB5sHBGIwZNpwx5Ke-VPqmgT61nlPk2pvOBZw9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
‏
تزعم أمريكا زوراً أن أصولنا المجمدة ستشتري منتجاتها الزراعية. أمرٌ مثيرٌ للاهتمام. المحصول الوحيد الذي نحصده هو ما زرعتموه أنتم: عقودٌ من انعدام الثقة. إنه عضوي، وفير، ومحلي الصنع. لكن يبدو أن الولايات المتحدة لا تصدّر سوى فول الصويا المعدل وراثياً، والوعود الكاذبة، والتصريحات الجوفاء.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79854" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCz_ig3AVy9NN48qbV6MnMru7XUWdycU_wrLtaAv2t3bZkhgwlq9LO-N7vbitHa9Tm5EAlWAnLE1Id9vgdNtKKYT_8Rz1fDj5UnArB4Wls_Q27xKFc-WRc2BNUV4sZll8bIs6NEW9UGfSee3sV5P21XmYoWeE-NDw-y2Kj6z9HRDDP-BE7TvfxRWpNsg4pK0ZiGbYOVjsnNPiRjrGr-DuMmBnmk43MaC-_-xxY6Lv2Td_7iuVZPOabTHgflPJ8VA9lL9nfUO7_w7fp49MBlDgvunx5O09-lPqKPTh3mo3DvTBkPBixK-fFzC-P_8GlLn1vRpI8P5wmYjjNdCdxywZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yjloqo8DoydSwP1vEtX8IZELKpp7Ml42VjlIYbfNaZJWNQZgP9l7oHh6Uj7rh6oVBxLznMuU6JkOaYzTO56PJWo45yocw8eVztShmaTq67hugLDv6ICITTDOrSgFTOKNbc4DthxdSgU1z4WzBpkOf1pA2eaAW5QcGYhaUKTdRjARSPXfvgNxYgyJm0hnSBdju4UbgKRoPyu0oFXvONXR_nJ59q8zoBSKA24gpgodA320141KKkPhrpnQNhCtdkxTeBGYA8w_q3uSS_60iKLHxs6nWkK1dl_Bzz0uprYl0MVCDkNjv7pqr0wAQpmlg4r6_oxQ4mAUGgm-ukkl8XsDVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
❤️
القيادات الايرانية تشارك في احياء يوم عاشوراء.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79852" target="_blank">📅 15:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏ زلزال بقوة 5.5 درجة يضرب تشيلي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79851" target="_blank">📅 15:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏روبيو: دول الناتو لم تسمح لنا باستخدام قواعدنا العسكرية رغم أن إيران تشكّل تهديداً أكبر لهم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79850" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">روبيو: إذا استخدمت إيران الأموال لتمويل وكلاء لها، فإن الاتفاق لن ينجح.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79849" target="_blank">📅 15:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روبيو: نحن قريبون من التوصل إلى اتفاق مبدئي بين إسرائيل ولبنان</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79848" target="_blank">📅 15:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏روبيو: سنشارك دول الخليج على خطوات تطبيق مذكرة التفاهم مع إيران  تحديدا فقرة دفع الـ300 مليار دولار
😄</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79847" target="_blank">📅 15:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
‏روبيو: لن يكون هناك سلام واستقرار في المنطقة مع وكلاء إيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79846" target="_blank">📅 15:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">السلطات المصرية تغلق مسجد الامام الحسين (عليه السلام) في القاهرة لمدة 3 ايام بحجة "اجراء صيانة"!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79845" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
‏
بيان صادر عن البحرية التابعة للحرس الثوري الإيراني:
لا يُسمح بالمرور في مضيق هرمز إلا عبر المسارات التي أعلنها مراسل إيران دراغون المتمركز في المياه الشمالية لمضيق هرمز. وقد أعلنت البحرية التابعة للحرس الثوري الإيراني حظر مرور السفن خارج هذه المسارات، واصفةً إياه بالخطير للغاية، وطلبت من جميع السفن الالتزام التام بالمسارات المعلنة. ويُشترط التنسيق مع البحرية التابعة للحرس الثوري الإيراني لعبور مضيق هرمز عبر القناة 16، وسيتم اتخاذ الإجراءات اللازمة بحق المخالفين. والرسالة العامة لهذا البيان هي أن الملاحة في مضيق هرمز لن تكون آمنة إلا في ظل الأوامر الإيرانية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79844" target="_blank">📅 14:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو: لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79843" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو:
لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79842" target="_blank">📅 14:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
قائد قوة القدس في حرس الثورة الإسلامية اللواء اسماعيل قاأني للصهاينة:
عليكم مغادرة لبنان بأكمله؛ لأن هذه الأرض ساحة مقاومة ونضال، وليست ملعبًا للمحتلين. إن لم تتراجعوا اليوم بإرادتكم الحرة، فستُجبرون غدًا على الفرار مُذلّين مهزومين. لا تنسوا عام 2000 والإرادة التاريخية للشهيد السيد الحسن نصر الله في بنت جبيل؛ ذلك الوعد لا يزال قائمًا، ولا شك أن المشهد نفسه سيتكرر.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79841" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس: كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79840" target="_blank">📅 14:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس:
كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79839" target="_blank">📅 14:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
مقتل ثلاث اشخاص واصابة اخرين كحصيلة اولية في اشتباكات مسلحة بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79838" target="_blank">📅 14:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
تتويج العراق في لقب بطولة العالم للمواي تاي في ماليزيا بعد فوز اللاعب العراقي مصطفى التكريتي على نظيره الروسي في النهائي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79837" target="_blank">📅 13:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
إن ما أُثير بشأن تلويح العراق بانهاء عضويته بمنظمة أوبك لا يعكس الموقف الرسمي للحكومة العراقية، إذ لم يطرح رئيس مجلس الوزراء أو الحكومة العراقية مسألة الانسحاب، بل أكد العراق باستمرار أهمية إعادة تقييم السقوف الإنتاجية بما يتوافق مع الطاقات الإنتاجية المستدامة للدول الأعضاء وفقا للاتفاق الذي أقرته كافة الدول المعنية والتفاهمات الخاصة بوضع العراق الأمني والاقتصادي.
وفي هذا السياق، استجابت دول منظمة أوبك والدول المؤتلفة معها لهذا التوجه من خلال إطلاق عملية إعادة تقييم الطاقة الإنتاجية القصوى المستدامة للدول الأعضاء، والتي تُنفَّذ حالياً بالتنسيق مع شركة استشارية دولية مستقلة، وبمشاركة فاعلة من العراق، وفقاً للجدول الزمني المعتمد.
كما باشرت دول منظمة أوبك والدول المؤتلفة معها بالفعل بإعادة الكميات المخفضة تدريجياً، ومن المقرر استكمال عودة جميع التخفيضات الطوعية خلال الأشهر القليلة المقبلة، بما يسهم في تعزيز السقف الإنتاجي للعراق. وعليه، فإن أي مطالب تتعلق بالسقوف الإنتاجية أو مستويات الطاقة الإنتاجية تُعالج من خلال الآليات الفنية والتوافقية المعتمدة ضمن إطار دول منظمة أوبك والدول المؤتلفة معها.
كما نود الإشارة هنا إلى وجود تفهم عالي المستوى من الدول الأعضاء في المنظمة لوضع العراق الخاص وما عانته الصناعة النفطية العراقية خلال اكثر من أربعين عام مضى من الحروب والحصار والتحديات وآخرها ما حصل من تدمير للعديد من جزئيات بنيته التحتية النفطية والساندة من خلال الهجمات الارهابية التخريبية وان هذا سيؤخذ بنظر الاهتمام ليكون الانتاج النفطي العراقي بالمستوى العادل الذي يمكنه من استعادة موقعه كثاني اكبر منتج ضمن دول المنظمة ويحقق النتائج المرجوة من مشاريع التطوير والتأهيل لكافة مفاصل الصناعة النفطية التي تشكل العصب الرئيسي للعائدات المالية العراقية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79836" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2psAmnlQB-WQIU39eye1_AvgJU9_MqW_-53Eg0jqK_7VdZ1BoIFyTHnKqApP4FOoy9nVw-ns5tzKMAQP_9J809p0ffHznQWauHBuCRZ9ASaFWXZ9JYdykNSKKShpAg2UnCaZzkmPZDrhmaTkgTkIOZOs4by55kFfxq3J4wWFp6Qn3NKkZM9-5GKTJpCxlmLY8WqWIHmvIbwRIphxazh9oVARxGKDq_E4LaN9piCncWtocMUOv_QiWWLQjDGjckSyJnrJCzTBqpFGbwSUILDNv21m3BjcgEjy2B8t55qt1psRF_KrqaYsjgaTWQc-4wdn_1zVXnm3WdUGoLZ6ml9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
قوات حرس الحدود العراقية تحبط محاولة تهريب 34 كغم من المخدرات بواسطة بالون هوائي على الحدود العراقية الاردنية السورية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79835" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
🔵
فرنسا تتدعي انها اعترضت ناقلة نفط خامسة تابعة لأسطول الظل الروسي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79834" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79832" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79831" target="_blank">📅 12:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
📰
رويترز عن مسؤول كبير بقطاع النفط: العراق يمر بأزمة مالية حادة ناجمة عن الانخفاض الكبير في صادرات النفط بسبب حرب إيران ويجب النظر في زيادة حصته في أوبك بمنتهى الجدية
🔻
العراق ناقش داخلياً احتمال خروجه من منظمة أوبك، لكنه يعتزم البقاء في المجموعة والضغط من أجل الحصول على حصة إنتاج أكبر.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79830" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2hzAhcmnkCwca0_2YNdboqUnHIz96cYNjScjyIsRlLwIeX9lGiMSnBiNjHCRSyUKLIYBJwG53qqq_t5aJVuPjxLQUlqTxYKmMNJ7Q1lHep0KEYs2k5fVw60tVeqw4cEQnFyzhOT8mVdQrbweGdOQdmUJQqF2IXubHLVmfOnZUXtd9G230gVr5LS-NxfY8bFzSsxZfyETRRlUUlzWaT_MM0CVJcIzkmA5niUa0gYXSqMFEATNTA2pHiSY8hNYAnPlCgq9-rpLOjPWQ1vIPqgesJoDqECIYDp7PxdFCESZc9xtnKkdu_X2L9tf-KNTxlAKM3RLiR2UgbPo31YZYRNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أفلس العراق رسميا ؟!
مجلس الوزراء العراقي يقرر إيقاف التعاقدات للمشروعات الجديدة الاستثمارية وما يخص العقود السابقة يبلغ الشركات " اصبروا ان الله مع الصابرين " يبدو انها آثار عواقب الحرب بين امريكا وايران على المنطقة ..</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79829" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تاكر كارلسون: كان ترامب مقتنعًا بأن قتل آية الله سيؤدي بطريقة ما إلى انهيار إيران. لكنه وقع في فخ الحرب مع إيران بعد وفاة آية الله علي خامنئي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79828" target="_blank">📅 09:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79827" target="_blank">📅 09:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79826" target="_blank">📅 09:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 تضرب خراسان شمال شرق إيران</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79825" target="_blank">📅 09:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAIsz0m6kZHStgGxxFTsCVpJCJNH7LNMGOrjNl0dzAY3wd2u_KmjDe5GDSfCxXNDL-B5RQJi0tqxY-WwK03t1tk3-ESBvzCR7TWPMzm28IzZfRm1bpVl-ppCmYGrap6u_1qvMu0Jp31tBO7usZgwBihAX_hQyxRCZby26TptMaUzNRPHkpTK1f8ksqyV_v_Ob2IY6-KDmSmNXF6L9XD4xMgO-Rfyv8U6MN1bHG_FCXsy3csxePYnpOivFssyeCcXNS_sU4ukdnzDNCLnWvrl_Z3i8Tv7CWvWRPiW346TNOR5Fk5jhjVcP4x_Ytn6ZBOwtlYyCGJrjSU8cCdomjKokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الزلزالان الكبيران اللذان ضربا فنزويلا مؤخراً كانا هائلين، وقد خلّفا عدداً هائلاً من الضحايا. الولايات المتحدة الأمريكية على أهبة الاستعداد لتقديم المساعدة!
‏لقد أصدرتُ تعليماتي لجميع أجهزة حكومتنا بالاستعداد للتحرك بسرعة. سنكون حاضرين لدعم أصدقائنا الجدد والرائعين. التقارير الأولية ليست مبشرة!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79824" target="_blank">📅 08:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXiNuHJIHIofRG-LFciMDNem_c1Dy_mP-E2r6ivuYv6-K3XBYGToEaMiCWvtIeAo-IMPXhmSUKVt98C8LnHknaSwGyHT0AtAxpUN4gw54dQjlu8GZHZJAfBxoCjdzou0rlLil4c1xqgEf_ADxUbypNcp3pm9UepZrXpHpANckdmhIudF7ICO1Ia5gmo0zc3oDyfh9A62a7MVvqBwPOjcHzs5_ks6foaHcrD4bwjGPbu7EfvXPUtCQ_Xj9qPIS-pcMO7TIaPSXW-kNYx3iXagDyO4oAs_13ko18u74lDMwQUQM8ZIbCKMh3DJq0m3ObpMYcSLe7t9xyRZ5eYK2N6pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي للصحافة العالمية :
سيتم تخصيص 500 ألف برميل يومياً من النفط العراقي لتجديد الاحتياطي النفطي الاستراتيجي الأمريكي ؛ سيدرس العراق "تعليق" عضويته في منظمة أوبك إذا مُنع من الإنتاج بما يتناسب مع قدراته
‏سيتم "خنق" الفساد
‏سيتم نزع سلاح الميليشيات بحلول 30 سبتمبر مع مغادرة آخر القوات الأمريكية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79823" target="_blank">📅 01:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران. ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79822" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=UJ2SdtQV-WxM172HqFTKFDjBZWciXD8mFHAfqpkKk7po0Fs5TsrkZ0ETDsu1Qhr-ZrC8styAscsHvxHtxRXMVDOppd_Tv-i8mSprUxsgBIfdN0BryRJwftcZTByNIuBEDUCAycke1Yqxy2gQQ4Sj5MDVuHqk-Rjgo7E9kFJ97BQyDUix_9yFeYqYq9KN14pfuvMAYYy4zcQAhivP5m4Buz8uhFL-V1n7OVBfN9jzxvzoyiQvqHV3t4AJ_h_qqmUmAZVL7JBTrH8YYWFtyFykkDsBwpRXTt9Yq2_nxe6LtTz6UQHh_rERdyzeP2l3se9qa_4IU5Ji-SWhdsO7jPcDIZdsnV31ck83U2CAV-Rhg4fB1jUkRRGifbCC6Kn-4eqw4m52Odz1eV5ac5zujgwsFFgXalj3Kx1mCgWPsW9OzHoRxEUl6B0hUMNuqF9W4myatVdq3LdR_rliuOfI0S-jyN2TRHWbt12zuwhi8y2c5AcZoMbJgEydUJ-SBeHKUL_OJT0RK4xnoc8FySP3RdpHv_efjJ2ButLhoiVh81C-ojFmNC2-SiWEiiPAIACIEFkE_T_5KaYlQ6NPkl0VDFEqqi6w9YKmq6txYfwSx0TO4GPQylvnFIaG1Zvt3B73kolrAwsjZ12WJRhX3YutoQh7eVn2dmYh_s2zVZtxphnum_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=UJ2SdtQV-WxM172HqFTKFDjBZWciXD8mFHAfqpkKk7po0Fs5TsrkZ0ETDsu1Qhr-ZrC8styAscsHvxHtxRXMVDOppd_Tv-i8mSprUxsgBIfdN0BryRJwftcZTByNIuBEDUCAycke1Yqxy2gQQ4Sj5MDVuHqk-Rjgo7E9kFJ97BQyDUix_9yFeYqYq9KN14pfuvMAYYy4zcQAhivP5m4Buz8uhFL-V1n7OVBfN9jzxvzoyiQvqHV3t4AJ_h_qqmUmAZVL7JBTrH8YYWFtyFykkDsBwpRXTt9Yq2_nxe6LtTz6UQHh_rERdyzeP2l3se9qa_4IU5Ji-SWhdsO7jPcDIZdsnV31ck83U2CAV-Rhg4fB1jUkRRGifbCC6Kn-4eqw4m52Odz1eV5ac5zujgwsFFgXalj3Kx1mCgWPsW9OzHoRxEUl6B0hUMNuqF9W4myatVdq3LdR_rliuOfI0S-jyN2TRHWbt12zuwhi8y2c5AcZoMbJgEydUJ-SBeHKUL_OJT0RK4xnoc8FySP3RdpHv_efjJ2ButLhoiVh81C-ojFmNC2-SiWEiiPAIACIEFkE_T_5KaYlQ6NPkl0VDFEqqi6w9YKmq6txYfwSx0TO4GPQylvnFIaG1Zvt3B73kolrAwsjZ12WJRhX3YutoQh7eVn2dmYh_s2zVZtxphnum_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران.
ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79821" target="_blank">📅 23:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
جيش الاحتلال الصهيوني:
أصيب مقاتل من جيش الإسرائيلي بجروح خطيرة نتيجة انفجار عبوة ناسفة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79820" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c6939043.mp4?token=pkU-8zi0LNAUZLbb5E8W2ABZ5nvZsN4O5OZRSKhH2b7GZA_y0uqhzlaW8Z2TwApOQNCs5lhuB0QzLVQ1IpxF9S8-ByQmqXDgiliqQ6l7WgdMoLoG8RSEJVvkOZ4BEp4dwFBaBt5qw7WVkiY06fWakeSMgjlzlxfYD22FrM3s8R7TaEKQ2v7SWsYMV8KJ-6NmQHahKsXxJmQ-3L744QTJUz9wVGSQG2ZNotbLVL6ekV6eHcVZ8dJsIun_spsiawfcDhMkXvpvwtkcpfF4Ol7Xaxq4ETOkOFC5qkKIX7vFR1RDGetTABJBUJfQUV50kSIAhdY-uaZj7lwlbaNh_G8HzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c6939043.mp4?token=pkU-8zi0LNAUZLbb5E8W2ABZ5nvZsN4O5OZRSKhH2b7GZA_y0uqhzlaW8Z2TwApOQNCs5lhuB0QzLVQ1IpxF9S8-ByQmqXDgiliqQ6l7WgdMoLoG8RSEJVvkOZ4BEp4dwFBaBt5qw7WVkiY06fWakeSMgjlzlxfYD22FrM3s8R7TaEKQ2v7SWsYMV8KJ-6NmQHahKsXxJmQ-3L744QTJUz9wVGSQG2ZNotbLVL6ekV6eHcVZ8dJsIun_spsiawfcDhMkXvpvwtkcpfF4Ol7Xaxq4ETOkOFC5qkKIX7vFR1RDGetTABJBUJfQUV50kSIAhdY-uaZj7lwlbaNh_G8HzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
رغم التضييق، يواصل أبناء البحرين إحياء الشعائر الحسينية، مؤكدين تمسكهم بممارسة الحريات الدينية التي تُعد من الحقوق الأساسية للمواطنة في الدولة الحديثة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79819" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09002baed0.mp4?token=cnBcifA8grHqTgyFTmeb-SXkzMO2_OAybT2eks01XOIyAtbWCaaCbzHFbfN-8Jr4U26-sTuiElR7x-vqLzUAIL0mZaYyXv7iCfvqb0jpWN4HkldtsY6Jwf504pgSsoUE67GPlqSQfv9EooJusKfdcd3sa-RQfHGgVdMpdXWA0QLo3XDZ3ZW-gr_ISEd5n9QbDsI4zBIa_aKF5DRjgl-GNmYAoFtSkJES0sztsm3SwGf7DNtXzNMfKz34WIEb6nmctRdtlNqfLi0RW-L1SuaxkwOO5BT9aHKIwwIp5fX_xqBP2kyp47h4Z3mryhIS8szY61oMO3p9_qDfbcbdpoTnvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09002baed0.mp4?token=cnBcifA8grHqTgyFTmeb-SXkzMO2_OAybT2eks01XOIyAtbWCaaCbzHFbfN-8Jr4U26-sTuiElR7x-vqLzUAIL0mZaYyXv7iCfvqb0jpWN4HkldtsY6Jwf504pgSsoUE67GPlqSQfv9EooJusKfdcd3sa-RQfHGgVdMpdXWA0QLo3XDZ3ZW-gr_ISEd5n9QbDsI4zBIa_aKF5DRjgl-GNmYAoFtSkJES0sztsm3SwGf7DNtXzNMfKz34WIEb6nmctRdtlNqfLi0RW-L1SuaxkwOO5BT9aHKIwwIp5fX_xqBP2kyp47h4Z3mryhIS8szY61oMO3p9_qDfbcbdpoTnvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب: الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79818" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
🇮🇷
استكمالاً للتنظيم الأمريكي الفاشل في كأس العالم..
أفاد الاتحاد الإيراني لكرة القدم أنه خلال الزيارة الثالثة للمنتخب الوطني إلى الولايات المتحدة، قام مسؤولون أمريكيون بمضايقة سعيد الهاوي ومهدي طارمي، مما أدى إلى تأخير مغادرة الموكب إلى سياتل لخوض المباراة ضد مصر. وينتظر أعضاء المنتخب انضمام اللاعبين إليهم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79817" target="_blank">📅 20:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=N2T3IMhAxIKQp2nOTaZJeAqTos8MHIgw4Yu5_Vbx4jj0un1q8Ra0s2ekVv4USFOR2VZdfWPR3lzi0nXjgv0HAynbY25W4j7w3RHgg4Ee3gRJzR6FN8BevSkWZ-VPj_Ngttr3AysAN5YGnSM_eksvZ6l58GpdiNI0EmlbWvoZ5FwjMwd7NMkPjpDylHWDTrab0OK8SPS_8YYPIEVVsRQsya72184ww7hnJ2cMS7Kip5CUXuXHCo3UDOwRfywnU63jFQHyJH6J_Xh05qkrHDVYoNuzDLzfynM3r4PpOd9eShPzOUr57vv1hlz87ABvMsgD0wCqe47II4FhX7qVGeBStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=N2T3IMhAxIKQp2nOTaZJeAqTos8MHIgw4Yu5_Vbx4jj0un1q8Ra0s2ekVv4USFOR2VZdfWPR3lzi0nXjgv0HAynbY25W4j7w3RHgg4Ee3gRJzR6FN8BevSkWZ-VPj_Ngttr3AysAN5YGnSM_eksvZ6l58GpdiNI0EmlbWvoZ5FwjMwd7NMkPjpDylHWDTrab0OK8SPS_8YYPIEVVsRQsya72184ww7hnJ2cMS7Kip5CUXuXHCo3UDOwRfywnU63jFQHyJH6J_Xh05qkrHDVYoNuzDLzfynM3r4PpOd9eShPzOUr57vv1hlz87ABvMsgD0wCqe47II4FhX7qVGeBStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
جيش الإحتلال الإسرائيلي يعلن عن خرقه لوقف إطلاق النار: شنّ الجيش الإسرائيلي هجومًا على شخصين مشتبه بهما عبرا المنطقة الأمنية في جنوب لبنان، وشكّلا تهديدًا لقواتنا.  قبل قليل، تم رصد مركبة تقلّ مشتبهين عبرا المنطقة الأمنية في منطقة مرتفعات علي طاهر، وشكّلا…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79816" target="_blank">📅 20:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=XkinSz68XHAHtniXgOAxLRKEH_7z-s8NEMhe9Pna1VRu-GJvk_6olNg4gZG-9NxFBykJjCbGWCs7qWMyU95N3OooRPvZC1xQHiTbp55QhIAe9lx4L2Ocwdgpks59BoHH9gAaKwqGVli6A10YWZJag5YErH9NqPe_dXFndtI4FxK-xu8Gri2_qPETAQjLfsJ72ikQpzyKUtc4FCKeoCJoVhjN1_I8lV0jU6TcCjQ-eAbgLUdh-roZUea6SKzPPx_zcq3i_6RPNaiYaDEviLgVsytVUxS6uULonrNIbJYR80vuETycLIgr0_c9UreW2q6do2fqM70eCKKO2YrRCetwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=XkinSz68XHAHtniXgOAxLRKEH_7z-s8NEMhe9Pna1VRu-GJvk_6olNg4gZG-9NxFBykJjCbGWCs7qWMyU95N3OooRPvZC1xQHiTbp55QhIAe9lx4L2Ocwdgpks59BoHH9gAaKwqGVli6A10YWZJag5YErH9NqPe_dXFndtI4FxK-xu8Gri2_qPETAQjLfsJ72ikQpzyKUtc4FCKeoCJoVhjN1_I8lV0jU6TcCjQ-eAbgLUdh-roZUea6SKzPPx_zcq3i_6RPNaiYaDEviLgVsytVUxS6uULonrNIbJYR80vuETycLIgr0_c9UreW2q6do2fqM70eCKKO2YrRCetwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترامب:
الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79815" target="_blank">📅 20:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
🇮🇷
‏
وزير الطاقة الأميركي:
إيران لن تكون قادرة على إغلاق مضيق هرمز بعد الآن.
‏الألغام الإيرانية أخرت عودة تدفقات النفط إلى طبيعتها  في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79814" target="_blank">📅 20:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار.. غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79813" target="_blank">📅 20:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opyA_IjH6Pm8_Lrdpu_PHOhtc6D8kq7eupiXYcMD9LKesvsjIWSoAltxiD7hUS0VduKkbHaT_Dl-FLeGnCNZxCfQsBiWoBHKOzP66H-qCbK6C5LeKaySXOMicwXWOYArcsmm-q0pYuY7D_Z6aJLlCqBKC0TIcljfA0sOLTNp0WCOLhr4r9L4nhuZn1y5G0Sge_frYbjCtSR2-agma6MvqyL7jZPLddVo9vUxdesmnpS9r04RN1cJeVUYwRoOgg8lbcOQln81DGNpO3hkPXU1S6Pfe-52vts7cOglXsthbC9tC4GMhHD9uc6IqT2J2FOhjkokSh2GELT-yrpCinTktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية:
لن ينخدع أحد؛ لا يمكننا أن ننعم بمنطقة مسالمة طالما استمرت النزعة العسكرية والتدخلية الأمريكية، واستمر وكيل الاحتلال التابع لها، مع الإفلات التام من العقاب، في شن حروب لا نهاية لها في جميع أنحاء المنطقة وارتكاب الإبادة الجماعية والعنف الإرهابي وكل أنواع الفظائع.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79812" target="_blank">📅 19:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79811">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBhcMEu71z0LhilY7EyW3JdVnYQ-hcPEkZD9Cbc_n6EH7op1b4DTLHZK40rhxe7IDX8WzvarVcxEEcPg6Ncf_aXLxC-dKZ5hYu0XuBbW8enrKLXYtetiW0hK0I6gdNJBWqNAPnoZ7D6XF-ceDiIIG1hnpnyu--b8zlgQydMt2jyku2rlBPK57djPnrqGMLztK3XjprKQDJtRpCF8L74RS4jlO4XZ0YVbw17kUrXz1nzn1f0xbeOYA2_cahVqnqsxqlbjc22BUmdpeHeTvDyrRAkjL-9HGy6bq3KgFb7DR0-zivgzcBEsuHN_vwhtps8E3ToD94hm3L2CSipJpkpdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79811" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
علي الزيدي:
العلاقة مع الولايات المتحدة ستتحوّل من عسكرية إلى شراكة اقتصادية.
معظم الفصائل بدأت بالفعل بتسليم سلاحها للدولة.
بعد انسحاب كل القوات الأميركية لن يكون هناك أي مبرر أو حاجة لأي مقاومة في العراق.
نريد من "أوبك" زيادة إنتاجنا النفطي بما يتناسب  وقدرات العراق النفطية وعدد سكانه.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79810" target="_blank">📅 19:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
روبيو:
الرئيس ترامب يريد أن تلتزم إيران بمذكرة التفاهم وإلا فلديه العديد من الخيارات بينها العودة لفرض عقوبات.
اللجنة الفنية ستعود إلى سويسرا يوم 29 الشهر الجاري لاستئناف المحادثات مع إيران.
المحادثات الفنية مع إيران تتعلق بالملف النووي والعقوبات.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79809" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwajwgbKDbL6Tca6TcS8RFKcfmmigK99drXDeyKLSCK9xif2sJKMhTAr6UODOgnwHMi4M8KXHZjoFdExB0KH0pf6MK6L4ocV25Gp8WAV6a2P9s_PC3ZCuPNNa2LQl2vjJbv7UxHPNYLLiRFqpeYhSzTwq2dcTd7lgaXxBDwKhBB1AtLOIQRyY3c8xbihTLrxbUdq21j4dXJdisP_3T_wqQKc3atR4hwJfiKAYcqJRdTvVB-lnWjCm9My5a_6CN8aaRcYAK2Jrp2d2VKgpXB0Mkb7Yg4WmfPh_S1fynBBWEp5dd8xR-iWiCM_rYiEO6TPvlko5HrsFYwubjzNF5sLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itNSDXH1MsXgP0Di5MekL6FDHyaFwsZ_L0oBm6IJ4_eJ9XlLz9BmCOZqdK6DkISafkSpN5KnpkOBdIDf7rSC7YOxKh4cN6EklYSsgtEnccIIBiGKyQdsdMW4GwDgM78yXJjzZLrlYCZappKE3NzQms9HT5hEBDVjlvWMpK1CKMdAwQwEU5Xr4f9PSMoDwDmCaAqipPno1RWyzelzfeIEFoWDIpRWu35pbN15ncXWPR2B1wdFhK9D_zJEtUhaRLOQZPcG2lXs8yz0xrEu0-QaCQx5JOeiAr3yiCiAKLH-CfCOihsvb1saGejNRL_wrL4-PY_SJn_z4nQAfadMSr10eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صورة خالدة لإرادة قوية..
طهران، تقاطع ولي العصر؛ رجل مسن منحني الظهر، وعلمٌ ظلّ مرفوعًا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79807" target="_blank">📅 19:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
🔳
🌟
سي بي إس نيوز حول هجوم إيراني على قاعدة أمريكية في الكويت:
يشكك عدد من الجنود الأمريكيين الذين أصيبوا في هجوم إيراني بطائرة مسيرة على موقع عسكري أمريكي في ميناء الشعيبة الكويتي في الأول من مارس/آذار، في مزاعم البنتاغون بأن معظم المصابين تعرضوا لإصابات طفيفة وعادوا سريعًا إلى الخدمة. في مارس/آذار، صرّح وزير الحرب بيت هيغسيث بأن "ما يقرب من 90%" من نحو 400 جندي أمريكي أصيبوا خلال الحرب الإيرانية، تعرضوا لإصابات طفيفة وعادوا إلى الخدمة. إلا أن بعض الجرحى وعائلاتهم أبلغوا أن الإصابات كانت أشد بكثير مما تشير إليه التصنيفات العسكرية الرسمية. من بين هؤلاء، رئيس ضباط الصف رودني بيرمان، الذي امتلأ جسده بشظايا عندما أصابت طائرة مسيرة إيرانية موقع عمله في هجوم الأول من مارس/آذار. تُظهر السجلات الطبية أنه عانى من ارتجاج في المخ، وفقدان للسمع والبصر، وتلف في الرئتين، وجروح متعددة بشظايا، ومع ذلك صنّفه الجيش على أنه "غير مصاب بجروح خطيرة". وصفت زوجته، إيمي بيرمان، هذا التصنيف بأنه "غير مقبول"، إذ أُبلغت في البداية بأنه سيعود إلى الخدمة. كما أصيب الرقيب أول كوري هيكس بجروح بالغة جراء الشظايا، وخضع لعدة عمليات جراحية طارئة في مستشفى كويتي، ويتعافى حاليًا من إصابة دماغية رضية. وقال إن عائلته أُبلغت في البداية بأن إصاباته طفيفة. أسفر الهجوم على ميناء الشعيبة الكويتي عن مقتل ستة عسكريين أمريكيين وإصابة أكثر من عشرين آخرين في الموقع العسكري الأمريكي. وأفاد ناجون وأقارب أنهم يعتقدون أن الجيش قلل من شأن خطورة الخسائر، بينما يرفض الجيش هذا الاتهام، مؤكدًا أن تصنيف "مصاب بجروح خطيرة" مخصص للأفراد المعرضين لخطر الموت خلال 72 ساعة، ولا يعكس بالضرورة العواقب الطبية طويلة الأمد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79806" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=CjpeYP2bWZmNBmD9QCPICqwEAcXRH0DI3f3VH3-eSl3bUzdO7yGuElM48Q_n5QkPjqJ2xdDTJkedg8cY2i1lsVnVPC6SpfO0obn-wKf6BLHffdgYq8XxWt1AKQ9T_n01xCbOIk_hjx655-d95QPz7w7odsgWVvTAwS5sz5mtsqZocm-8-1gpyZ6IqZ38D-NTNEqELJAywhunVxQ3Ml4l9PfjWDS1A0EvRtuV87Un5kRgZlrZ98xjxiqNwQkeVkGnKu04DuaAiRibr7T2IeOJqjw6WDwbO_l-yfyTgrG0pRbWbX8nt60EOW5Wd2ju3GErcNLXFb-TsKkY8eyUxirUUCV_eImF0695ACGOSKYpJZlW9NopcCG5grytanZ9R7VQ0wdC9Q1OLuz0mwuGOCMcwlXpIr5ptzarpfC314RfM155uDgF-uiPSVD2f1X0W3eOXRPfvm89fnQrhNI_UgFneZ2oGINhkg7biGW6aPOKuNoKdRvlcUUF-6xaqazxlknf-hvrygJMncRY9MgSBc4ZGljd6vJUXtyZC2sZoM-PBuW5iG4rInaPdeX7WCAIUzc_YP5S5KGQTKXsNfIsZt36tY3f6jBqZtvLKw_J_udOdba8s2mDUXTyripcqJhJk1ll_yizRrjZIn9LYNtBKkOckt63bPYLSj3mf3Hw_QZLG88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=CjpeYP2bWZmNBmD9QCPICqwEAcXRH0DI3f3VH3-eSl3bUzdO7yGuElM48Q_n5QkPjqJ2xdDTJkedg8cY2i1lsVnVPC6SpfO0obn-wKf6BLHffdgYq8XxWt1AKQ9T_n01xCbOIk_hjx655-d95QPz7w7odsgWVvTAwS5sz5mtsqZocm-8-1gpyZ6IqZ38D-NTNEqELJAywhunVxQ3Ml4l9PfjWDS1A0EvRtuV87Un5kRgZlrZ98xjxiqNwQkeVkGnKu04DuaAiRibr7T2IeOJqjw6WDwbO_l-yfyTgrG0pRbWbX8nt60EOW5Wd2ju3GErcNLXFb-TsKkY8eyUxirUUCV_eImF0695ACGOSKYpJZlW9NopcCG5grytanZ9R7VQ0wdC9Q1OLuz0mwuGOCMcwlXpIr5ptzarpfC314RfM155uDgF-uiPSVD2f1X0W3eOXRPfvm89fnQrhNI_UgFneZ2oGINhkg7biGW6aPOKuNoKdRvlcUUF-6xaqazxlknf-hvrygJMncRY9MgSBc4ZGljd6vJUXtyZC2sZoM-PBuW5iG4rInaPdeX7WCAIUzc_YP5S5KGQTKXsNfIsZt36tY3f6jBqZtvLKw_J_udOdba8s2mDUXTyripcqJhJk1ll_yizRrjZIn9LYNtBKkOckt63bPYLSj3mf3Hw_QZLG88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-06-2026
جنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79805" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1nyJzK3bFluOt8DDfsXbr5TKrfZVACCwL0jUuuNr2BhAchUB82vabOfyrJwW38gDWrKVgzooiSu9QGN0WjwHJSydzOmWLQ-Jybp_Ya3f1Tjza0Q-Qqap0JdzyhLkUv0jj_Azge7037wikKNoFyvbdMFBTiW0K3XH2RwewnhZLe9dxUEG1AHsgrosxMmnjfsAESQCf4mNL4Lnifq-EJA0HuMz8vxW8Trfn2AQn9SSMrnq3eGC2JOwZQTWwGX5UdsAE5Y0DM5EkWl_VtS9IvBoCUwBSjLkrwJjqIb_j9j_a3ixKThxOshkL54E9f5w3iOjWSb6cxAhUi0-C1AuCCSPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار..
غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79804" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRjDAfo2WNNwQPoTyusjMJCG55a0X9si-h7-RVWonzJamV543BJn_D_Cv9Y_RzJIAQgpjXAZfVxtwW4M803FcJol0s-Tlznv6T1m1DM0sKksOpO8_aISp8K9WbSv2ciD9U_-di8SGJfDn8kbMH2mjm3iyGvqK-7Bbj6-OmwAnDkAjSXq2oNTt-0vEGv-b76Kv7HOvPJyPqO2241H8T_OvfoMRf54m0X0bSD2HNOT8KjjSgXZT1E2Q8S3WpDV1eOULPTUBLzBZaVR0lCVKlOzEah4s_G_POoi7S_m5IWxU4S2OffMcct5qCAJQ4UiakUu8Jh4Z6v1uc4tAH-GAtY0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير: لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79803" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=eyHDDDNuavJjAN3rJyrFv-AR7Ka4_Pq1k8rGmhnUJY77Zr0Gi4ldejPwsLzwAa3EDc5KUuh4CBqQRetyPz6CExRiwBFhrvWFsurnAOwRTZ23XUUZjlNVYsgabR19rbFn1x9jmycuifQEvS9JNLsq1YH6K0g3pv2ckpjl4iZcM9U4nNC9mwVLVlB6arZU4D9vJs9K_i-6Wz2DEa2YzifaVwTsCwsj77QvltULwM5lLXKGBwm6KyDVsaZAL0X8y77URCsG7yJTpeokbNeTRbUXJ_anVBCxR0YcjHkcKnZJlCIIoc9qtS4eVP0Qv1xOyOaSmmLyqDsWfpKWItMh3gtxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=eyHDDDNuavJjAN3rJyrFv-AR7Ka4_Pq1k8rGmhnUJY77Zr0Gi4ldejPwsLzwAa3EDc5KUuh4CBqQRetyPz6CExRiwBFhrvWFsurnAOwRTZ23XUUZjlNVYsgabR19rbFn1x9jmycuifQEvS9JNLsq1YH6K0g3pv2ckpjl4iZcM9U4nNC9mwVLVlB6arZU4D9vJs9K_i-6Wz2DEa2YzifaVwTsCwsj77QvltULwM5lLXKGBwm6KyDVsaZAL0X8y77URCsG7yJTpeokbNeTRbUXJ_anVBCxR0YcjHkcKnZJlCIIoc9qtS4eVP0Qv1xOyOaSmmLyqDsWfpKWItMh3gtxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي تركي يجوب أجواء مدينة الباب بريف محافظة حلب السورية، وأنباء عن نقل جرحى إلى مشفى المدينة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79801" target="_blank">📅 18:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=oXU9cmdqqR7IDXd3u5ZF7ObhQvUOzQaaONnXmBAcalkXX3jg_10am1FGN2fvr4qxtSMOYSFobJGv11PcAzyS46IHdV1TVtF7ClbjeTCNzGfqWktz-E8lu636BBHNcksOjlE8emQfuScocittwlA4JJhpup6zqhWxJ6y5z9jmjCRseFOzVwwaW9ydQuj_YC6vpYMyEnCL3JaP2Ks_F8gkNNZjuphHCB6jmXpDdIad6I5hq6AGlmBwBZvvpD5lXXI-zflVNqjbBhwZNsiSORqO1gpQaUmhB9O3J5ex35Wr-QEBiaRh5XoWg71qVnnCEQZ9y1gVCfmJde7IEYAhfSVEsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=oXU9cmdqqR7IDXd3u5ZF7ObhQvUOzQaaONnXmBAcalkXX3jg_10am1FGN2fvr4qxtSMOYSFobJGv11PcAzyS46IHdV1TVtF7ClbjeTCNzGfqWktz-E8lu636BBHNcksOjlE8emQfuScocittwlA4JJhpup6zqhWxJ6y5z9jmjCRseFOzVwwaW9ydQuj_YC6vpYMyEnCL3JaP2Ks_F8gkNNZjuphHCB6jmXpDdIad6I5hq6AGlmBwBZvvpD5lXXI-zflVNqjbBhwZNsiSORqO1gpQaUmhB9O3J5ex35Wr-QEBiaRh5XoWg71qVnnCEQZ9y1gVCfmJde7IEYAhfSVEsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الكيان الصهيوني ينهار من الداخل..
استمرار المعارك الداخلية بين الحريديم والمستوطنين في عدة مناطق بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79800" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCPDDxUzCzR8olOmYFJIvpBSCPxxQpl4bgR2AyGlL_kKb2FGA0VPwoEfcTDDP9gVOY0JQnfDpFuFmxqS67GVymTovnGVuLQnufi5At0I6lFogA6_E0E5mTUeTeI3KnZg_3TYyzR6zb3nxBlqXIBjNfXv_bbM7PNkZe6oIW2ot0rZ_IOzk9zXB5ku4fabRpld769vdFeN6-C3Kak_eDMvf5jcKo_kdjIkp1tjQBO0ttKPMlR5qc89XB2q4VnNsp-d_JKS2ZIeB9BM6JuUmRazIJeEm0IGVgRtMwoPbQfOq2gcbyYrtuQD9_XUU6JHYN530sWMGNU0xZP0r_acfFeIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
يُلغى بموجب هذا المؤتمر الصحفي والتوقيع على قانون الإسكان المقرر عقده اليوم إلى حين إقرار قانون إنقاذ أمريكا الذي نحن في أمس الحاجة إليه.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79799" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
نتنياهو:
نقيم حزاما أمنيا عازلا في جنوب لبنان لمنع حزب الله من شن هجمات علينا.
لا يزال هناك ما يجب علينا فعله في لبنان.
سوف نحمي إخواننا الدروز.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79798" target="_blank">📅 17:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
إعلام العدو:
إصابة جندي إسرائيلي بجروح إثر انفجار وقع ليلاً في لبنان ويجري التحقيق في ظروف الحادث.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79797" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBzD8_UeIJp5HeedGelKdS0luDu2qnGS9j69U01INy3JSacuevnhsTz6LYr4cPuYrhS16-qaDtftQ7nfDt_Ak2zBfx35DKHo9gkPrI0wAd3YhnJ1V3jDL2MKA-afNdvvhy0gXc_KxG66gtd0_NqxrEDrIYFPvPst1vnEGUR11jcTDMKR88ub4jmq6F-YnVhRZwUHop2BSfn9dgGtsiVanziEQn-0TnqG6sGjEOth-psPjtW_ZhN5xEi_HPZLcp-ieOQzWYub7L_aN0YXRlfB8YmobFGZKpHUhLTfsFaid4AP6A958f-sdfmHQ0B6aLdDxr_V9UKz2VJK_z_Pmef3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سحب العمدة مامداني ثلاثة شيوعيين قويين، وتلقى تصفيقًا عاليًا وشاملًا من وسائل الإعلام الإخبارية المزيفة. تهانينا سيد العمدة!
حققت ليلة أمس رقمًا قياسيًا بلا خسائر، حيث ساعدت في انتخاب وطنيين أمريكيين رائعين، ووسائل الإعلام لا تقول كلمة واحدة.
على مدى العامين الماضيين، أدى دعمي إلى فوز 259 انتخابًا تكميليًا، ولم تكن هناك خسائر تقريبًا، مع عدم تلقي أي اهتمام من وسائل الإعلام؛ أخبار مزيفة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79796" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-2SpQekOoVTia-9rDf-bEa2oFacsYjy0ZBcS-8Yy9FrqTOnQrEJjUXurRCEksJ-JtqeCLy9DY7h-C6yUuAU2ztFsgM8RvhNVpKcxCPF7dHceJAfz2sMQNSTKAleNJdmiJ7xIizS3zDhwGR8hrhtpbwhpm0803QioSLNMzYy1HkRpb9Y9_nwQ_Qg773O8KSE-7lxAOg356wxUc3XUAZ3QuuMSoWMMLUEkBE4d9Ht3T7BPXpXWXErS1q5VtIjkghlJZ1dUUML9gN83-1OyqoJFTjMHMWqNRgTJ_tD4FIU26TzeeFf-kr7_u_dtA6iRfyUX7L8WPNs2RI8twuuoh--ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير:
لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79795" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
سلطة الطيران المدني العراقي:
منح ترخيص التشغيل لمطار النجف الأشرف.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79794" target="_blank">📅 16:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
‏إير فرانس تمدد تعليق الرحلات من
تل أبيب
وإليها حتى 30 يونيو.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79793" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الذهب يسجل خسائر غير مسبوقة منذ نوفمبر 2025 وسعر الأونصة يتراجع إلى أقل من 4000 دولار</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79792" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64062428bd.mp4?token=NNFgQA0x9QjmsJMMahaauLrAq1easVW44AL6lb54s33b8lmoSP3PKrTg7ryEHtiCONobWl_tyhzzh7E_p4nEqVsUIVLXO8zjMLi-3OqEnS_oE_XwEf4TCovu029yrL18Pf-34Ztklb9kSX4wsrs-1fuD2p9wtLa1r6LasdGYWjVOPNQimWgbnc_CrtmCQwlT0RvicLhx_AoNRk2XjrTsmHn2GZZGD82yVAxPsknYJHnFQaBsrUEPXSopqSoDGXdotb7VxGcXDIT7Db7UQPa7shbWWD-KYW8g58vWLICqiY3Rz3CgfzaYpln7uZE52fGbx_3yYroy05WE65WcriiXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64062428bd.mp4?token=NNFgQA0x9QjmsJMMahaauLrAq1easVW44AL6lb54s33b8lmoSP3PKrTg7ryEHtiCONobWl_tyhzzh7E_p4nEqVsUIVLXO8zjMLi-3OqEnS_oE_XwEf4TCovu029yrL18Pf-34Ztklb9kSX4wsrs-1fuD2p9wtLa1r6LasdGYWjVOPNQimWgbnc_CrtmCQwlT0RvicLhx_AoNRk2XjrTsmHn2GZZGD82yVAxPsknYJHnFQaBsrUEPXSopqSoDGXdotb7VxGcXDIT7Db7UQPa7shbWWD-KYW8g58vWLICqiY3Rz3CgfzaYpln7uZE52fGbx_3yYroy05WE65WcriiXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
مشاهد من احياء ليالي شهر محرم الحرام وذكرى استشهاد الامام الحسين (عليه السلام) في مدينة ديربينت الروسية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79791" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امريكا تزعم قتل قيادي من داعش في غرب سوريا</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79790" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
