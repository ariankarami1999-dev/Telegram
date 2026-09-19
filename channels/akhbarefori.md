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
<img src="https://cdn4.telesco.pe/file/QVXn3d0oSKEdI4e-U-s8biouUjj9p-uqeX4bnbJeDT3t_d-sOkfNgihB2j2qSg6cTe0z7jnqlHGvtB1u1lW2wKJrJxPRplcHoxTVMIjypRJG062sOsFHKOTk4S-nwHMJ9yv22l4anleSmjKf0rg5UwUu_0G8fAtmWyzn533B6kLukAyEENSdx7UAZrdLO4fREmCvPB8AHGk2JXDxEhpzWlINwTiWGyiPsAAczVxupWCBgltZAVUEjeSPrjG3P4JBkJURzOBIA1KvAwb6YqD7A7qCipizHf1Ozg5VFOLBqJlYkSr2amwqijFnrMAZsUayqCLjifnJg4Z1H6a-5CwupQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-691292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNp6xotAIJ5fvAwJYBCAKov2Gt8pCUaeIa4S5pKYEVCGQEcdnSkTa9Q00QgVh_PXG2wuTxgiV_ibxmGqE1uRoIh4YQrYUi5G5k4KmjhpMIQAKb4MsUEZ0pngdpYx2MxtH70LkKV08kczoEy9QqGt1t1fyxbNhBUqkNVM-LmFMrJIvJg5LjPI6HV0R03SFjKCONhboY5ixFtbGTSKgBg8zPwbFj2Y-VQqz6L6l2rBHmDZbrAQczaccB8C6eznKwjAc2zxblUyjNGTWjGbA6Pj2qfaHrAZjD3ek8nLXoso9GYUmIxRtycVoTwGZE0GhBfxSNx8-dvYJWSjLlo2gnOf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: آمریکا به متحدانش هشدار داده تحویل برخی سلاح‌های مهمی که قبلاً خریداری کرده‌اند ممکن است تا ۵ سال عقب بیفتد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/akhbarefori/691292" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f37a29cd.mp4?token=JnybuYvhSr8JktlBW7Xt98pKxGjjOmpsmL8X3f5hiCxYDgQ6OdMTaZOzlMAGp2YmNFPZkWuf5fAwM_ox-XuIE2k_L8vSWOu3jVOSW4a04DninhK0HLigCavqUNnmJOsGZXVgvrFnwmE3BIj02ntQTUc_LgDWhZodyeSpETzANx1Dc9A1mPehq-LD-gRlgjIuV2GGcNAVqsS_gUuOuwTbg_Euj1bt6IkR1Xs5M25omm7T82q_KtAkevyTfADjPAvl16u2OPKnMEARpqV-6cXJ-Bhm-v6EiE1hROZO5vci6xffIbs4EEXrwQgknYVqwAmtH06cdPW5aQ-eOrhQYm1M8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f37a29cd.mp4?token=JnybuYvhSr8JktlBW7Xt98pKxGjjOmpsmL8X3f5hiCxYDgQ6OdMTaZOzlMAGp2YmNFPZkWuf5fAwM_ox-XuIE2k_L8vSWOu3jVOSW4a04DninhK0HLigCavqUNnmJOsGZXVgvrFnwmE3BIj02ntQTUc_LgDWhZodyeSpETzANx1Dc9A1mPehq-LD-gRlgjIuV2GGcNAVqsS_gUuOuwTbg_Euj1bt6IkR1Xs5M25omm7T82q_KtAkevyTfADjPAvl16u2OPKnMEARpqV-6cXJ-Bhm-v6EiE1hROZO5vci6xffIbs4EEXrwQgknYVqwAmtH06cdPW5aQ-eOrhQYm1M8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ سوژه تمسخر خرد و کلان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/691291" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
نتانیاهو از ترس، به فرودگاه نظامی پناه می‌برد
🔹
بنیامین نتانیاهو، به‌جای فرودگاه غیرنظامی نیویورک، در یک فرودگاه نظامی در خارج از این شهر فرود خواهد آمد. او سپس برای ایراد سخنرانی خود در مقر سازمان ملل متحد، به منهتن سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/691290" target="_blank">📅 21:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYfBsWGheoSVq5K59BnbFqamNwcijiEuy2HnN8o7kKE0WYR5aAjJjWjmc3X3N5HYlvYeqR43fwi0iDS3Q7gcl33s4a9fsI2pXsthxaYHay4gTk4hCyxqnHnEj_yBEHDiY7JEK9oC3A8E2iRe6N-AMywy-28YVLkOjVdMyIxoh-0Idl720VBVXJnLvvi9CfwJkxBVdRSb2XPi617dGM6DxaK3wyLA6WeXpU8I2G9QlIm_brbYWYPWPJ1r2K9vGWgB78Wwwo1YJ76-OEL-xXUbB3k6CmShp0bR0LmWZIMFZoIJMFWyeP37rHAag63Woqst9NeLPImBMpH2JWXEpZCyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیاید رایگان با این هوش‌مصنوعی پادکست بسازیم #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/691289" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/388a43995c.mp4?token=O12lW5xZ92YhAueUaaWSdHHuV5z7_lHT6LmSYMdC70HW2_-yC7ZSMyRDoPv5vt4inAxZDZ0OSUz6iuZOOicS4wd6V4YgQ7fooq4DcXoMN3dxXRlMc9R0esZk_UwgOIDC-wu_S0rITGSOZ7Dniu_nuvv1-YWItPJu-9F-NG7vBI9QRRPquZwl3GDLIdAXyjHTmqPysdz9AYX4BYACrhp1e6HykK__sgoH6MaiHT6BvWFEARM7YrZhxR9l4wXjWPPHx2Jny7NwfOzTIb2OvQYGuGA_caedAv9YzGc9g1gK4V5xvf6nx8qfNqjquqYJcJE3eDG8Q_JmgIi2gVMl0yi5fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/388a43995c.mp4?token=O12lW5xZ92YhAueUaaWSdHHuV5z7_lHT6LmSYMdC70HW2_-yC7ZSMyRDoPv5vt4inAxZDZ0OSUz6iuZOOicS4wd6V4YgQ7fooq4DcXoMN3dxXRlMc9R0esZk_UwgOIDC-wu_S0rITGSOZ7Dniu_nuvv1-YWItPJu-9F-NG7vBI9QRRPquZwl3GDLIdAXyjHTmqPysdz9AYX4BYACrhp1e6HykK__sgoH6MaiHT6BvWFEARM7YrZhxR9l4wXjWPPHx2Jny7NwfOzTIb2OvQYGuGA_caedAv9YzGc9g1gK4V5xvf6nx8qfNqjquqYJcJE3eDG8Q_JmgIi2gVMl0yi5fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تازه لگویی/ هر رأی به ترامپ به‌معنای قیمت بالاتر بنزین است. هرگز دو بار همان اشتباه را مرتکب نشوید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/691288" target="_blank">📅 21:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691287">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برخی از رشته‌های مهندسی و صنعت از انتخاب رشته کنکور امسال حذف شدند
رمضان رحیمی دبیر کمیسیون آموزش مجلس در
#گفتگو
باخبرفوری:
🔹
براساس برنامه هفتم پیشرفت، برخی رشته‌های غیرضروری دانشگاه‌ها باید حذف و با رشته‌های مورد نیاز جامعه جایگزین شود و در دفترچه انتخاب رشته کنکور سراسری امسال بعضی رشته‌های جدید اضافه شده‌اند.
🔹
در انتخاب رشته امسال بعضی از رشته‌های مهندسی و صنعتی حذف شده و برخی رشته‌های مرتبط با هوش مصنوعی به انتخاب رشته اضافه شده‎اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/691287" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691286">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1ntwNdVKnLaAwNIqHL6TlWL5xRc26g2bHl_3ZAOHZWlK4121J1rttYE2UAdANHOa_4D3-Gxf7_sdfbEmWcwMJC8XIHSXRURQ4-uhvNh6kj5Ldveknd3iUGyoOAeuVPSsdU5AcJbcTQoG4o6ufAw_wFXb_rFvGKlA6WmuIEZepuu6LdtctMWtLc-BmY1_IAKdZicXlD6cItV2Nr1vbt3hAMJM4Uuo2dzEYVSAWqDPPvV3E80gBHpq4OClfqf8hJD6bR5MscPPB8-nibo_jEbqmuU50hzQQiQnGZ_tLtqyUPvsCkThXxXzemXof8Ztliw0IhHPxc4qMZL5cXfw-rGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: تجمع گسترده در تهران در اعلام آمادگی برای دفاع از ایران
🔹
الجزیره با اشاره به ثبت نام ۳۰ میلیونی پویش جانفدا برای ایران نوشت: صدها هزار نفر برای دفاع از ایران در این پویش اعلام آمادگی کردند.
🔹
الجزیره گزارش داد صدها هزار نفر روز جمعه در تجمعی سازماندهی شده در تهران برگزار شد، به خیابان آمدند و آمادگی خود را برای دفاع از ایران و در صورت نیاز به‌دست گرفتن سلاح اعلام کردند.
🔹
الجزیره با اشاره به اعلام حضور ۳۱۳ هزار نفر نوشت این تجمع با هدف مخالفت با آمریکا و تأکید بر آمادگی برای فداکاری در راه ایران برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/691286" target="_blank">📅 21:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691285">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b4317f40.mp4?token=b1zbQFrNzFuHzVVXARS-NZB8YqXkZMb_1nDCe7K7DAXTRe53E50C_VEFBWYNGKI4McsZRw_B02vsYx4zlg4ynIHggHX796LUrPFiiA3r73m5NWmdU91QC2SPEU5pW8jpji2MxEJa36xgKXB5SlrkPGUcwaipAqz0RUvUlElabVfa5QC_-MdRVJEqZoZ1ImkMmUG2Ny4TWzsw6kAOaqO5mlLFT6y1sTugObVBBDFpZmKO045w1jvzoOoSQgZ4H26uketBmURsKWn1fb-3kXRxvY0oqC6EgP6xLmw3BHCXdOC-c8TEaCV1S7-euLaY40OOhX9jnvHxZFOZfpBTpHWI8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b4317f40.mp4?token=b1zbQFrNzFuHzVVXARS-NZB8YqXkZMb_1nDCe7K7DAXTRe53E50C_VEFBWYNGKI4McsZRw_B02vsYx4zlg4ynIHggHX796LUrPFiiA3r73m5NWmdU91QC2SPEU5pW8jpji2MxEJa36xgKXB5SlrkPGUcwaipAqz0RUvUlElabVfa5QC_-MdRVJEqZoZ1ImkMmUG2Ny4TWzsw6kAOaqO5mlLFT6y1sTugObVBBDFpZmKO045w1jvzoOoSQgZ4H26uketBmURsKWn1fb-3kXRxvY0oqC6EgP6xLmw3BHCXdOC-c8TEaCV1S7-euLaY40OOhX9jnvHxZFOZfpBTpHWI8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/691285" target="_blank">📅 21:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691284">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ4LhmGje30hUm3UNlgr0Y7FJE5t8XV0TUWzIbzScCu5NbuVlHn56JiXzwP7fqyQJ8Z2w3_HsqU8wo7jDgTG6UMhMcu-knYOaxTi2XNZx_lIGcIj8V3XliRVrTZGpiZ-S-CC6OiVfx4UG_L9FVkmlL3EyBQSwYCnhEVEaiWQJIcTo-OhwK3GcRHsq-3tk_xo00EgUnVhHcRMZgz7hziIJT0JI6KKMQOzMyOmd-taClcHfl21RwVtJgYuD6sG458cLAKNocagF3UZ9yXxIw7fHS6VenD845cWh0gGm7mY2e7IuDJJtqcw0jLGjv8eZJ2FafxM_J3UmKZ4I40jj1OKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشریه لو پاریزین: میانگین قیمت گازوییل در فرانسه به بالاترین حد تاریخی خود رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/691284" target="_blank">📅 21:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691283">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8aea9937.mp4?token=EROWk9lZbd45r52ZWsXRy3SJGdrhSaHEUksvlSJ4hrGiL6B3bPMhS5qvWAzzegfEa0Cx-2GonSZnj21K_9tq6-MkrsaD2zEN-q1EES5K8nCFD5DtaI_0KGyZEF7mDeCW8yV3s08T5ou6wdsgWlvIFhej6BGGpfCdcoS5UMs2kUZmbFTNhMAM_SvUelwGj3SpiFzwgpZtsOE71APCYBy1TcQoo6IP61gh38swT2_BveIDDRtettgdVc5RFUunj-5weRx1hBndbOuzgFqRwnCg6X_ITv7WOFzbAhODLuhXXqTQOVjMlJqlpxx5cDzd-eT7JAS9qul4jxM_4FORzF1Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8aea9937.mp4?token=EROWk9lZbd45r52ZWsXRy3SJGdrhSaHEUksvlSJ4hrGiL6B3bPMhS5qvWAzzegfEa0Cx-2GonSZnj21K_9tq6-MkrsaD2zEN-q1EES5K8nCFD5DtaI_0KGyZEF7mDeCW8yV3s08T5ou6wdsgWlvIFhej6BGGpfCdcoS5UMs2kUZmbFTNhMAM_SvUelwGj3SpiFzwgpZtsOE71APCYBy1TcQoo6IP61gh38swT2_BveIDDRtettgdVc5RFUunj-5weRx1hBndbOuzgFqRwnCg6X_ITv7WOFzbAhODLuhXXqTQOVjMlJqlpxx5cDzd-eT7JAS9qul4jxM_4FORzF1Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکن سابق استقلال: بخاطر تصمیم علیرضا منصوریان با گریه تمرین می‌کردم اما هیچکس حتی همسرم خبر نداشت!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691283" target="_blank">📅 21:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691282">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3588f464f6.mp4?token=nsNLxJjvPM_Eu0ISKIh_afR95LMoZPi8TccONiO_NNSyr7DfPhneI-owyCKzy_iZd8FYH_aX1q55pHnOT6Bzd4nQ_ITykDhoLrH6a3X48XYvhjA12hg2NUdePSty2RDbp_l-Vaf0mPlGT9jpHZzZDUMVpr6wvG-t0GxF5snVqW2A6dbp1LBBaeSjCbtZoAmYNallNaz4qDnNOogqJB4begtalbtvgD9GcXXs-x91HFQ9ixP5-t2ysr9SiQhIDhvjdDuxmXAWZQv8iNxhFYqSpYBsIvekjR346qcCBZ4sONbl6VVCw6p_8Hh-mEubQ843T_MaFpmBjqIIoGuw9xDRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3588f464f6.mp4?token=nsNLxJjvPM_Eu0ISKIh_afR95LMoZPi8TccONiO_NNSyr7DfPhneI-owyCKzy_iZd8FYH_aX1q55pHnOT6Bzd4nQ_ITykDhoLrH6a3X48XYvhjA12hg2NUdePSty2RDbp_l-Vaf0mPlGT9jpHZzZDUMVpr6wvG-t0GxF5snVqW2A6dbp1LBBaeSjCbtZoAmYNallNaz4qDnNOogqJB4begtalbtvgD9GcXXs-x91HFQ9ixP5-t2ysr9SiQhIDhvjdDuxmXAWZQv8iNxhFYqSpYBsIvekjR346qcCBZ4sONbl6VVCw6p_8Hh-mEubQ843T_MaFpmBjqIIoGuw9xDRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصف‌شب دندون‌درد گرفتین و خوابتون نمی‌بره؟ این کارها رو انجام بدین!
🦷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/691282" target="_blank">📅 21:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاباما تور</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5tEmcrsGxpmGhnnTT5tRJxhjDlXDKzd0kG9XLfoE8McqJmMip6myVvaTVQedzD5XfnKL_cIMyPkJZInkvlZZbfHpah8sySJCOgJaYvZFb1QdfYs04a4YlcW3znGseyYMVAojG4RJgfJYBcCI_Rdn2rJj43lyeM0JT3-_TkjLg-CvtyarpF-5-HsW0CSecSfZ_JTU9dTDvIxWyERRpabQxPLN1ZW5Zu44RkXwyxJ0xWRyiVso_gXQJGERVddqOREzjo3UXmnOq9zkOFkVFjYE6dKRLTwQrO_AEupp21IdzaSYSntaI3RskE3GlXKiBzNgwcozXypqfRoZmhpe9foLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vV01VDGHcUKPjwgvRLvfdgsNb1ztMBDSI2mdPC-9grgrQEjlTXsahMRM1Lnld4X167mmUubsoAPsBL462ue3xZ1DUlJIFGNTavSYu2A2i8wLfAHmM1WJ2VWnadTMqcEI0BOdBFYdD7JlYWnK0vhiEAG-WmmcgnVbzCWEnHRch58w2Jam1njqZ_lF8R--J0WFxUyArvPtAlzjYcl8ovuO9Y18NjYD3GwZ5XDj0P0Ar4lpQtflQuCNbYR9OvJP4YIaKjX_6jMbU2SLtko3TYXiNI_94OhY8-cHOwxFYyR3-2IEoYPF6mw0fyDOQEs99q2b5AIc1EOwbdYgdmol9H0hxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehwMZcu0v0RkftLG5YxdWs20ja7pxMPV4DL28f4bJ3wJMyTNByheq5MNzljT-yXtG6uFm5apgQ4eQIPJ7bOgvoJ6Q17THLCH8n8HI7_CbT2_Z8PPSf2BTLMR_hpTkykrbzBxyV6Re40wufWrRxYnX3b44dHGvTvW7KeI24r_QKb6gxTS_-NSdmGWdpayr0ZFVH1nTEQ6Rs5x_JnSOBDh3UCtXddaKEeHvFgCc7-ho9M8o281KyIbamz5ImpNedyWaxYtTkZ5610Ealzfg-Cc7QQlztHd0WuLIkvrn6OXRCORVnstUBFlLO9nrIfC3lX4HDvWOhJUA7ytKo2CAMCSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNuLsT701nmGYOTWxXBu1M1N3Rz3HSTT5MyM8TtRRYwA_KnnpSfAJq8kE9Nh9lxM1OadBMXh7RkjCekZFTpBWqPHxrdnMAorL1i1fTGrvRYty-e3LvVMW46uVx0df9Gg9xoihSaVjfn6UEkI_gHCSMlmFc1Oalel67yq0uB_YPQswaRR1HG7hAdBhvPfitQSFYerBfuMmzqZ9Hd0MiHy7k1RoJZzjKjT-lHmig5wGli4NWhXgp0nQm2N0hCVPqkRkKmMFi5hl7pc88ym6sxpfTo_yoxrAEBkfBUl1oJuHuadpA0NSI3sUV1vY5M6iBdVBEbJWA5Uq8vZiJpIFVtExw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای اولین بار در ایران می‌تونید تورهای کمپ هتلی لوکس رو از جاباماتور به صورت ۴ قسطه رزرو کنین
😎
برای اطلاع از تخفیف‌های لحظه آخری و مشاهده تور‌های بیشتر کانال جاباماتور رو دنبال کنید
👇
@jabama_tours</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/691278" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXwbig0Y9Bmos-FE8nS5SNcmVvCffGB6bcH2dTqgP_AYhehjTCQo6I6fhmvpr418uToYDuznCN3YNT1hQFNpDXorCqOtJGazTbDh7Xvw33Fk8mO_ADF8yuNsUL7wsg-ixX05032bxLyEsNVQ62e3xJCpoEXoYDiPitB6w_NAH8rIsWFl4umOTD41Qu9eOXN3_Aecro74ERVcbI-NWXSESdPODcV_JDIWrTlj29yGOoy7uUevQ0QvCD8ZRl-idy-ZKRNte2oKM0TXK1jesz4yrBugO8I92MnyZKqlDY2QU2WdcDfCrHnRMeKq6znK3gNmKK3bM4ZlWl8a9-zwOkkyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدیدترین پست رسانه رهبر انقلاب با بازنشر سخنان ایشان:«بنده قاطعانه اعلام میکنم که ارتکاب هر آنچه به‌ضرر انسجام اجتماعی باشد، ممنوع است»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/691277" target="_blank">📅 20:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای ترامپ: من در حال ایجاد نیروی هوش مصنوعی هستم، درست مثل نیروی فضایی
رئیس جمهور آمریکا:
🔹
من در حال ایجاد نیروی «هوش مصنوعی» هستم، درست مانند کاری که برای «نیروی فضایی» انجام دادم، که در دوره اول ریاست جمهوری من، موفقیت فوق‌العاده‌ای به دست آورد.
🔹
به همین منظور، من در آینده نزدیک، رهبر یا مسئول ارشد هوش مصنوعی را معرفی خواهم کرد. فقط افرادی که ضریب هوش بالایی دارند، می‌توانند برای این سمت درخواست دهند!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/691276" target="_blank">📅 20:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teY3xvM7D9I-eirByb-Ae0tYFtrdlxWlceEXYN5ucmeOfBZmmYlVBj7-4HzWP0XZPJs1AhEg2JOZvarkOfa7YDynQNrb2noQ3nyPOsgqmKvdFLCxoAXrYy9mcCjqtweIsuDAbisxlvNDH113CLp7ldF1m78WBlr0JSTIdH41vEikrgWIxt9Dv0vBDODDn0vegAnAEMENWu06vVjPiTN4AtyVGChDrkJ2aiGckiF9mhhV6EJMUeaBhdC6j8u6NINsKY6jIylmEcisC74NjCGMbHdaMuV-_dlWiw6iZV6c0LW7FZgGfjVdpPgsFj4RuCjQibCj1GD_VFDDb98FOfPx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هرمز تا باب‌المندب؛ درگیری‌ها در خاورمیانه به کدام سو می‌رود؟
نیروهای حوثی عملیات نظامی خود را در یمن تشدید کرده و جزایر راهبردی نزدیک به تنگه باب‌المندب و در داخل آن را که یکی از گلوگاه‌های حیاتی دریای سرخ محسوب می‌شود، به کنترل خود درآورده‌اند. پایان این درگیری‌ها کجاست؟
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3246392</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691275" target="_blank">📅 20:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcFOoRjOSKUmfZszxernfW4H1UXydczlHNJHM0osUVlMXE8m5z5WA96jWJHMpounc4pms5rRBUY0YePlwuCEc4ocJjRfdxk2fD6XV8KyweuTqCwx-ydEWmuA7bSDliJ5nYw2gULVrXKQoboJsKOtseXjbcugZr8eHhwLGKbNcdD7kaVZc3AY78vrx41bPsyDD2isbrQONHNit2wvsdYu59XPWc8-8miHtuR8EYr4KmTvu_hAmmtVizkFrrG465HiQzjy6C_3ZLx8nV9wPTnMa5Wxf8LhPLNEko6lDfkJdEy-xdUBcrh8ozFPvuGZgdiFAkcEbOUyhdrLmhNwooWQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یورونیوز نتوانست قدرت نمایی جانفدایان تهران را انکار کند
🔹
یورونیوز از برگزاری بزرگ‌ترین نمایش قدرت حامیان جمهوری اسلامی در تهران از زمان آغاز جنگ خبر داد.
🔹
در این گزارش به حضور صدها هزار نفر در خیابان‌های پایتخت، مشارکت نیروهای بسیج و نمایش تجهیزات و پهپادهای نظامی در جریان رزمایش «جان‌فدای ایران» اشاره شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/691274" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
یمن: با موشک‌های بالستیک و کروز و پهپاد به اهداف حساسی در ریاض و شرکت آرامکو در ینبع حمله کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691273" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503821f386.mp4?token=liOnqAW6-X2uvZVqXx5a6SD9nvZuEYYYsk2NRRyJCbUNRgTbFgTp-Q7HIR4tF02n8W7cQ83oHv1LNavdAPGsC66rtI8j-8rWtB5Qh0cNsAaIjGOD68Il2gyG9setaROQyCmi-3nMqKsljcRHfDiLJcdv5wO-rOtuU3rU1m1qERi_hM4_CvOzCBZmYszi06HH9RJQ41LaAPnPZut64YX4o5RiUUnVE-iQkzeODZYwc-JHrOBQbdjAb_xqTeKeC-3Vg1RP-ANXRksxo92R7wxt0Vi5yNinXmNhKG6MZ8N5EaV2RnLAlhssvBt6Y64_HSKGgB_ydaa8ZAf6dABz2qXlPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503821f386.mp4?token=liOnqAW6-X2uvZVqXx5a6SD9nvZuEYYYsk2NRRyJCbUNRgTbFgTp-Q7HIR4tF02n8W7cQ83oHv1LNavdAPGsC66rtI8j-8rWtB5Qh0cNsAaIjGOD68Il2gyG9setaROQyCmi-3nMqKsljcRHfDiLJcdv5wO-rOtuU3rU1m1qERi_hM4_CvOzCBZmYszi06HH9RJQ41LaAPnPZut64YX4o5RiUUnVE-iQkzeODZYwc-JHrOBQbdjAb_xqTeKeC-3Vg1RP-ANXRksxo92R7wxt0Vi5yNinXmNhKG6MZ8N5EaV2RnLAlhssvBt6Y64_HSKGgB_ydaa8ZAf6dABz2qXlPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اصابت گلوله به خودروی یک رهگذر در جریان درگیری افراد مسلح و نیروهای امنیتی در زاهدان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/691272" target="_blank">📅 20:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقائی: حرف‌هایی زده می‌شود مبنی بر اینکه هیات ایرانی به دنبال خرید از فروشگاه‌ها در نیویورک است؛ الحمدلله در تهران شیک ترین فروشگاه‌ها را داریم و نیازی به خرید در آنجا نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/691271" target="_blank">📅 20:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در این شرایط نمی‌شود از پایان جنگ صحبت کرد/ ایران و عمان درخصوص تعیین مسیر در تنگه هرمز به تفاهم رسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/691270" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها سال ۲۰۱۸ از برجام خارج شدند و مدعی بودند آن توافق برای رئیس‌جمهور قبلی است. واما این تفاهم نامه که برای همین رئیس‌جمهور بود و ۲۰ روز هم دوام نیاورد  سخنگوی وزارت خارجه:
🔹
سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبه ایران و پاکستان…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691269" target="_blank">📅 20:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بقائی: آمریکایی‌ها سال ۲۰۱۸ از برجام خارج شدند و مدعی بودند آن توافق برای رئیس‌جمهور قبلی است. واما این تفاهم نامه که برای همین رئیس‌جمهور بود و ۲۰ روز هم دوام نیاورد
سخنگوی وزارت خارجه:
🔹
سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبه ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/691268" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3982e96.mp4?token=kc8XtVd6MCfNPsgRNV5MyBUTHmom6AMzgJofV-YkOGmZzC1-9T36OC5MwnuQSIv5lTpUDqjKHnmpTQ-oE2duDLV1owjH2s2HGifHBkXrwRwX5kIJWZ6kET079HyT0UskeSvhLczb56mkHZ-KLchllO7Q4atQncxV-2t7Q90HIpPNvSrBWXtDWEIf5MuWnHM0rO3B6xJ29VJhvgbKPovKMW9BJtShjxmnIubGuasRA0n_38MqMYQclwRMB6C6TgRJiXUzhMIDIBXFFoLeUFynPYI-DuPoL-_eqqiCM-VjxYIGZREorbz3s-NlSUcC1Te-UHhTzfjCbzcL9KqCSP6X3V8PvwQl2ghMVLFSHua0ltuniJrm-qimOPKEuone0_JzzoxM6WyDzFHS4RIkzV_RPgDNJ90IY9cJRiOmzalyjsoSC2ch2AxPdESogcL23709OwZo-WURKBAKxnc-BE-sTljm2h9n_TxjqtpcAMGqbyVUugXicpaDHGxTU-WcwMcdcRCh0nb4iwQH0KLC1BDXcC7qF6tp5vX8E1q4gx6tTSB0kYhwTpbyy01nFLDJe50wTxgB3KmmbyhD6GtsvlZSQimThSLKJSrFuvww6iq6R-Xs1EWjy7KYmdSRk7sLfbyHusOmEG35EhIOAyPon4Ms11mW_XUvmGfRLDTlIMQx5Ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3982e96.mp4?token=kc8XtVd6MCfNPsgRNV5MyBUTHmom6AMzgJofV-YkOGmZzC1-9T36OC5MwnuQSIv5lTpUDqjKHnmpTQ-oE2duDLV1owjH2s2HGifHBkXrwRwX5kIJWZ6kET079HyT0UskeSvhLczb56mkHZ-KLchllO7Q4atQncxV-2t7Q90HIpPNvSrBWXtDWEIf5MuWnHM0rO3B6xJ29VJhvgbKPovKMW9BJtShjxmnIubGuasRA0n_38MqMYQclwRMB6C6TgRJiXUzhMIDIBXFFoLeUFynPYI-DuPoL-_eqqiCM-VjxYIGZREorbz3s-NlSUcC1Te-UHhTzfjCbzcL9KqCSP6X3V8PvwQl2ghMVLFSHua0ltuniJrm-qimOPKEuone0_JzzoxM6WyDzFHS4RIkzV_RPgDNJ90IY9cJRiOmzalyjsoSC2ch2AxPdESogcL23709OwZo-WURKBAKxnc-BE-sTljm2h9n_TxjqtpcAMGqbyVUugXicpaDHGxTU-WcwMcdcRCh0nb4iwQH0KLC1BDXcC7qF6tp5vX8E1q4gx6tTSB0kYhwTpbyy01nFLDJe50wTxgB3KmmbyhD6GtsvlZSQimThSLKJSrFuvww6iq6R-Xs1EWjy7KYmdSRk7sLfbyHusOmEG35EhIOAyPon4Ms11mW_XUvmGfRLDTlIMQx5Ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«جان‌فدایان» در قاب رسانه‌های انگلیسی‌زبان / مشارکتی که حتی از منظر تاریخی نیز قابل توجه است
رسانه انگلیسی‌زبان فرست‌پست:
🔹
این میزان مشارکت حتی از منظر تاریخی نیز قابل توجه است؛ زیرا در جریان جنگ ایران و عراق در دهه ۱۹۸۰، حدود دو میلیون داوطلب ایرانی به خطوط مقدم جبهه پیوستند که در آن زمان تقریباً ۵ تا ۶ درصد جمعیت کشور را تشکیل می‌دادند.
🔹
رسانه انگلیسی‌زبان الجزیره: این اقدام فقط به آمریکا و اسرائیل نشان نمی‌دهد که ایران نیروی نظامی برای مقابله دارد، بلکه نشان می‌دهد صدها هزار غیرنظامی نیز آماده‌اند در صورت ضرورت، به جنگ علیه آنها بپیوندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/691267" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
بقائی، سخنگوی وزارت‌خارجه: من فکر می‌کنم خود مقصربینی یکی از نشانه‌های جنگ شناختی دشمن است. بعضی‌چیزها به قدری عیان است که حاجتی به بیان ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/691265" target="_blank">📅 20:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU8Kl5x3CqPx_pOfpm8y7aA0ofafEuJZ4XdsKwh6r_lNDX_d4fAZDxso4KeeZIO_CUWuMdITgdCkAFbUhc56g8SnRc5B75r9Fq6F5vUtNljouSlvMzKOfsr89m8Lfaim_xgAVDvT1yPjUVEex5Gn41KYiESyiRCo7zamW-EShgIoRYblRDncukm7Q04UZna_ZhNf_jvABi36Hg_Fp2bEg4ECwllPoe10aTXGpghBnLAuU3dGGPrjDFDAXfBi6Zyy8ylsIWFagMptxOd8Iob00A1TxdX17IRFLUe7RrLHb2eKKB_appXD32Wgr-m2WU9PFN51BhQdSou7bOBnqflCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه میامی: اسرائیل و آمریکا غول‌خفته (ایران) را که در هزار سال گذشته خوابیده بود، تحریک و بیدار کردند. حالا تمام دنیا با یک مشکل بزرگ روبه‌رو است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691264" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c148f5e986.mp4?token=WMPKYwL-pBUyEeDFGKXaUQMQgwT40pVnjOG1EcjoS7ybsEkiaxcklV2l9dNhYV985Ory3sA7gsdiBNY2BmV9Vp5LZJRuQGsTdHAIdlZu1TeKDIG2IASBE4VNQVrt_H0e5Bxh6KAjGPGAqp32hMJuEmKA3rOvgiKmOalLnW3n4ceEibOxsrAC7NAtT7v_q_bvux-z2trGzq_0_vdhg87saiH9zP3zkTHhAfT8nlRsF0DvtkjcYfVS5hfJ5VUVu83j_lj9jevZiXgIJVVZhApf_PMIojx4aY-ylBEXoZUIEI4XPPuT950zo8rDkUZkzoAxHac1l_4CQzsJir2egm26Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c148f5e986.mp4?token=WMPKYwL-pBUyEeDFGKXaUQMQgwT40pVnjOG1EcjoS7ybsEkiaxcklV2l9dNhYV985Ory3sA7gsdiBNY2BmV9Vp5LZJRuQGsTdHAIdlZu1TeKDIG2IASBE4VNQVrt_H0e5Bxh6KAjGPGAqp32hMJuEmKA3rOvgiKmOalLnW3n4ceEibOxsrAC7NAtT7v_q_bvux-z2trGzq_0_vdhg87saiH9zP3zkTHhAfT8nlRsF0DvtkjcYfVS5hfJ5VUVu83j_lj9jevZiXgIJVVZhApf_PMIojx4aY-ylBEXoZUIEI4XPPuT950zo8rDkUZkzoAxHac1l_4CQzsJir2egm26Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دونه‌های ذرت هم می‌تونن تبدیل به یک اثر هنری بشن!
🌽
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/691263" target="_blank">📅 20:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شوک قیمت‌ها در ویترین مدرسه؛ آیا لوازم‌التحریر به لیست کالاهای غیرضروری خانوار اضافه شد؟
🔹
شمارش معکوس برای مهرماه شروع شده، اما لبخندها در بازار لوازم‌التحریر کمرنگ‌تر از همیشه است.
🔹
گزارش میدانی ما از قلب بازار نشان می‌دهد که رشد سرسام‌آور قیمت‌ها، خانواده‌ها را در «مهرماه» غافلگیر کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/691262" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jama0AKUTkCyz2MRhyeyvfh1IceVtNlra69THZp4RlIZ80xxtTed9Dhk8Z_GzTEYXGFfXFGXHTP7Eyxxs_kts2Ei6apdAKvGdKPqhgHvmgfYadwjhLZDyu9ixIvatJiD5Y8qqEj9Mwapnb_ydGj3ast3caZZxIDTsmoovmT6r4e_XLU27xJjSEuGAewSLuxsN9BYG2VLgoPGLsBXOzwqiTADqSPmitwQ1MsAmI50BE5Z6CTFPJaFCTMN4hG44otG3MiO08V2GVN6DzWnjGwflaYzhn6GDzPG-ShD6SdCA6SQKVb9n6_Fm6HlEVzDyY1iWcvJZTXZVoY1_fa2zkfyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد
🔹
نهاد تنظیم‌گر بانک‌های ترکیه اعلام کرد این تصمیم بر اساس قانون بانکداری این کشور و به دلیل احتمال خطر برای سپرده‌گذاران یا ثبات نظام مالی گرفته شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/691261" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bis16vOUDqnFmAnKEImpzr9q0zLgMSglsy256z2fwf0gpCxijAQKONSJUE3TYa0TjGV0n6ATKvVEwi5-iMEPARlcTGQjWuLsfc5ThR--Tl-ThsIhZ0Uvf2GchvMs1eMsubkN9v_Jz3oyNUv_y9NBJbD-frygtCRYOg7dfo21syg1lg-tp2Pi200QAJDBcyFuECjXJ-BH9yh_NYEXBc3tm69DfOHv2hXkKwwtu14IDvINO_wpJvNFDUR0S3wb8b-43tyxhg-CnIYG6E1nMC5e2TygdyBt2PkHcg7I4mGaIDQxT3URCCqAhmiQvr2oPPUBh-H9rh5EUhL8DQzRhZ2Rew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به صدا درآمدن آژیرهای خطر در شهرک‌های صهیونیستی اطراف کرانه باختری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/691260" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">16-1 Ane Manaee (1404-02-01)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه شانزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
قید اِحترازی در تفسیر واژه “ایمان” و تفکیک مرتبه خاص ایمان از مراتب عام [01:04]
🔹
نگاه مرگ و زندگی به قرآن! حقیقت گرانبهایی که بی‌توجهی به آن، گم‌ کردن دنیا و آخرت است [05:40]
🔹
قرآن و عترت، امانت ثقلین پیامبر اکرم(ص) برای پیوند فرش به عرش! [09:16]
🔹
قرآن، معیار حقانیت و سنجش حق از باطل در عصر غیبت [16:04]
🔹
در دوران غیبتِ امام، قرآن حجتِ الهی و حقیقتی‌ست بی‌نقص و مصون از نفوذ هر باطل [22:46]
🔹
حکمت‌های عمیق و شگفت‌‌انگیز قرآن و روایات معصومین در عرصه‌های مختلف زندگی از پزشکی تا اقتصاد! [26:44]
🔹
قرآن نسخه‌ای تبیینی از عالم تکوین و مرجع راهگشای مشکلات جسمی، اجتماعی و اعتقادی بشر [35:03]
🔹
معرفی دوگانه حق‌گرایی و حس‌گرایی در قرآن؛ و تفاوت ابزار سنجشِ مؤمنانِ حق‌گرا و کافرانِ حس‌گرا [41:54]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/691259" target="_blank">📅 20:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
متروباس‌های ۲۶ متری برقی در راه ایران
معاون شهردار تهران:
🔹
با ورود اتوبوس‌های جدید به گمرک بندرعباس و تحویل ۹ اتوبوس داخلی، شمار اتوبوس‌های نوسازی شده طی ۵ سال اخیر به ۲۵۰۰ دستگاه رسیده است.
🔹
همچنین ۷۳۸ اتوبوس فرسوده در این دوره بازسازی شده است.
🔹
شهرداری تهران در پی ورود مد جدید حمل و نقلی به شهر است که با ورود متروباس‌های ۲۶ متری محقق خواهد شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/691258" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromستاره یک / #1*</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32dd295af.mp4?token=djNxTI7uNv_DNklo0BmghN4xyau1TyD1uFQR_TeryveTFyCOZ7Ywi2YZGJYZ6nEP8LKt-Gr_giShMugNK2g437mAgVhnk756X78sKhq32h9VVwql9zckamPEMvLbiV3dR7Pv2Y0XOtLTTH2luOctjkDTUiWZY14MRtU3xR89krGTt2FJtyPL4PaprkBOS6BadJ8BB-oS9vHWGbXOKvvmm-ECudX98y6hTizJ1glpicWiVIgyip2pvPkm7IzVvIs4d0hwYvraWtpk4rf0aRryOs2TQYERnvT-WIzlW9q9S44ietMOT80aaPQsTVs9CZBU5yH2Y94Z52EC7bvXEjOz0jFpSR0K4cQKHrt4R2pcN7cCvgJKpkaARKxToHunIM34TB8Pas6k9Gkz2WLPlbmYGOvKW8KiuFAZafQc_1a4vPOqUsClMrXsenTqGm95tXXCGY68HqXB3FDiHe2dMGhmzTj_avdTaHDpWQRAtuymot-LC3cZZYnDli7h4uXkyZ1HoVgw-YaingT7jQiLEqpZXm5M-1Dgseeqsooilm3o9Np76ZbS3KjFF4Y1Beta9nbHj_giOSwKlg6MzSvEiITxWJh2znhMo6BpChwHxY2YjJwzus_IYfrA5O4NPW1Cg6jajFLO1wBnT5Jcbwf_Q8qUF4SC922qrEDc9S_ne3QSeDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32dd295af.mp4?token=djNxTI7uNv_DNklo0BmghN4xyau1TyD1uFQR_TeryveTFyCOZ7Ywi2YZGJYZ6nEP8LKt-Gr_giShMugNK2g437mAgVhnk756X78sKhq32h9VVwql9zckamPEMvLbiV3dR7Pv2Y0XOtLTTH2luOctjkDTUiWZY14MRtU3xR89krGTt2FJtyPL4PaprkBOS6BadJ8BB-oS9vHWGbXOKvvmm-ECudX98y6hTizJ1glpicWiVIgyip2pvPkm7IzVvIs4d0hwYvraWtpk4rf0aRryOs2TQYERnvT-WIzlW9q9S44ietMOT80aaPQsTVs9CZBU5yH2Y94Z52EC7bvXEjOz0jFpSR0K4cQKHrt4R2pcN7cCvgJKpkaARKxToHunIM34TB8Pas6k9Gkz2WLPlbmYGOvKW8KiuFAZafQc_1a4vPOqUsClMrXsenTqGm95tXXCGY68HqXB3FDiHe2dMGhmzTj_avdTaHDpWQRAtuymot-LC3cZZYnDli7h4uXkyZ1HoVgw-YaingT7jQiLEqpZXm5M-1Dgseeqsooilm3o9Np76ZbS3KjFF4Y1Beta9nbHj_giOSwKlg6MzSvEiITxWJh2znhMo6BpChwHxY2YjJwzus_IYfrA5O4NPW1Cg6jajFLO1wBnT5Jcbwf_Q8qUF4SC922qrEDc9S_ne3QSeDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏳
چند روز بیشتر نمونده!
🚗
شاید این ۲۰۷ مال تو باشه
🗓️
قرعه کشی آخر شهریور
⭐️
افزایش شانس با خرید شارژ، بسته اینترنت و سایر خدمات
✅
از اپلیکیشن ستاره‌یک یا #۱*
⭐️
Setareyek.ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/691257" target="_blank">📅 20:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDTul7LZ_8F2_XMJss48rMg2BFma7GAHDYCk0sF1iE180AqEj_01-xvo1AYn2zM7dPizB-jk5emBLnoKkBgPGZw7Q_N0f2iEkPz-NlktQCUBFSUqqG2qkfFFS1qg_pa7wmg-R7w3iyVOCjFYl4pjq-cZ7InKDUq3fmc0K5kmxFYObOHRqNmPHnpDGSGOxl2gU-1QOa3z4OCGYrugMDA1nxzHupmwhqm4oGWJjnlTFYAWMULQs6fv6b9FOCirGBFLgZso3DAIVWKYSfFFusXIaLwhRPGnOxGWzFsco_-U3yXltKhASAf3xyadcDL4Gi-OygUVt5n7wecHLsnoh_kPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوشیت دیر شارژ می‌شه؟
🔋
⚡
با چند ترفند ساده، سرعت شارژ رو بیشتر کن و کمتر منتظر بمون! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/691256" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn5oMCj39PmjByNGsx8_9EDC-mbxZms3cSl5hDDK18ygL7tGZ7OhSI0BlmUOIQzKLl6Fo7DiImIVi_3-UfnpSHBYn2qKGuPalL0SUToa9i0UERSDEFKYQvItPFQGJqxkFg8pFJMseCr84k4n94kXmMT6lb6ejxmPheJfKMj_LKj6Z9sp0oqGu3-Hqh53fIZUdrSP9IfpLZJ-LbO4d3gxxADLHlYkzTtXgGdxQi26w04w0OtKy4xoiWP8o_OHNiJeNScj3i8QwdhfYBXccajvYe-W41FH1jAFyGZi2TbFtVMyZ-CUrAMq8yCaHz9hzoJRZUL6c_Ub7VAyR2lOwrfQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان سعودی: یمن به مکه حمله کرد.
مکه‌شون:
به توییتر خبرفوری بپیوندید
👇
https://x.com/Akhbare_Fori/status/2101314072545480794</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/691255" target="_blank">📅 19:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqeiP6AdjV5ct-J8Nipdh0EedUEn5V3nyo2SQ93su3abT1wRmW4nlTTlMABUk1h3TIL77Q2ks968Y8xJoSoRHdXIAIuh8AyQHGTBGEJ950CCzsakPRG7EC5ioJ9dEPAkFU3hl1BKKcT64AIPywdv6kqRN0mKDu2zICnuLqztHg24vYIkN1FFH8CldlG9rJLB8hLNsaaXvEbwj9mL3KL31BkIZc8xHrSUVhkQey1dafsuAHKptZ22C-ZpdFqyUKYdANuo6CY_xoGA5VJdDCDRW-ntK1UfY4TaQzskb70vwuR5uy-i9kucHA309g2KlWs5F1yWoRaflpNNF0Iq6qJ9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اروپایی: پیت هگست میگوید اروپا بیشتر از ما به تنگه هرمز نیاز دارد. سوار یک قایق شوید. این جنگ آن‌هاست، نه ما
🔹
این احمقانه‌ترین و شرم‌آورترین دولت آمریکا در تاریخ آمریکاست. خودشان جنگ را شروع کردند و حالا می‌گویند: این مشکل شماست بروید خرابکاری را جمع کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691254" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZuGjcVJAAol9qkaWSJJ2PL1ZiPv2isG8uWHJkXpxGa5CvOnHuhaFMl8d6i2gbpCoFaPQ1DmK4mgyq6ndcnVovq2nSuckxl10hfJ8xpF6MNe1I9NecrVtkSIz1M_nRH2FuNtzPMwt0Zrf0O1dUBch_z6yzmVtPUAINI-WYNqdx1MlnPF_BkCHy8-OKGZZs4D8ultSXoBITXeGVALg-OacnbEq8A8d9skn1X0X37aX9NMa36JBMusDMr8h1ri9dZtQ9QGlLWC_GEe9Sj_x19qGcqPMxOZJzSJLb3j2hRcX64NK4Qey6CeFz8iweM3GRhFyG_jA8nc0Cj8Xua716MIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لس‌آنجلس‌تایمز نسبت به حضور صدها هزار جانفدای ایران واکنش نشان داد
🔹
لس‌آنجلس تایمز گزارش داد که صدها هزار ایرانی روز جمعه در مرکز تهران تجمع کردند و در جریان این راهپیمایی، بر آمادگی خود برای به‌دست گرفتن سلاح در ادامه جنگ با آمریکا و رژیم صهیونیستی تأکید کردند.
🔹
این رسانه، تجمع روز جمعه را بزرگ‌ترین نمایش مخالفت و مقاومت از زمان آغاز جنگ توصیف کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/691253" target="_blank">📅 19:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سفارت چین در عربستان از شهروندان و شرکت‌های چینی خواست با دریافت هشدارهای امنیتی، فوراً به پناهگاه بروند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/691252" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdef470d2f.mp4?token=YSLAaVphT-vzSp8JMQRfCJtGDQrGSctS5_ube9EywN7GH7Nr4FXuyheGBgc7dmSjmhH3Pa6PzJB09gQy50I4muk36eYMnf8tH3qpm3_ngCEUoxzrGYpO3DuFJZEn1RdQvkQtlxC_YYc8jkzbD_phqN1Oc0_Io-dx_Kl0SlSwVUSDqaL3Jx67uq2jy-WVp2w3l-yfFKg_YYlGfXXvmo4z6JgKpJH06TeRgh_6VKjukvG8nfrmOjAy7aiUA6-tu8SWI0TrMwybUhZbpYKebKH14sYNeTHvSxkzythgmexoT_ylIqzc8fVtg6Af-uMVQIx7ifk1sPE-TUcB0ptNdsY0tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdef470d2f.mp4?token=YSLAaVphT-vzSp8JMQRfCJtGDQrGSctS5_ube9EywN7GH7Nr4FXuyheGBgc7dmSjmhH3Pa6PzJB09gQy50I4muk36eYMnf8tH3qpm3_ngCEUoxzrGYpO3DuFJZEn1RdQvkQtlxC_YYc8jkzbD_phqN1Oc0_Io-dx_Kl0SlSwVUSDqaL3Jx67uq2jy-WVp2w3l-yfFKg_YYlGfXXvmo4z6JgKpJH06TeRgh_6VKjukvG8nfrmOjAy7aiUA6-tu8SWI0TrMwybUhZbpYKebKH14sYNeTHvSxkzythgmexoT_ylIqzc8fVtg6Af-uMVQIx7ifk1sPE-TUcB0ptNdsY0tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگوها مهمان دریاچه مهارلو
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/691251" target="_blank">📅 19:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPut7QTpcZODlrPegMxCDoCmkQHr4zXHqpgOhot9Hig5DdlsmvjzOC9fHR-HS_6K44FhZWTwP84_NEFNoDF8O6B8z5ZtoutKIwi4zIr4cIMN1hfWdmcvMSnrSJ8-Wp6-3vgMIpDa4oGVGeNGPCqZFBbS4PViz4fP8_BekF-AqH7NN4nYJfqq9Dt8g6R4mipSWsgfoI7yQn-SVIm7oj8Bz67YbXIkhnWXIbG2aN7y0cc5XoiNJhlouYeX7jI2nwGSGO70kxl5z54zymploJskKGTH14ev9eiNjkRTICmruGBdm9FvxVPqgT0QtY2XVQNZCVyiUIEDai7PtBXrosHtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانی‌متواری
🔹
آمریکا در حالی از شورای حقوق بشر سازمان ملل خارج شده که تنها یک روز پیش از آن، هیأت حقیقت‌یاب مستقل سازمان ملل اعلام کرده بود «دلایل معقولی» برای مسئول دانستن نیروهای آمریکایی در حملات به مدرسه شجره طیبه میناب و یک مجموعه ورزشی در لامرد وجود دارد؛ حملاتی که می‌تواند مصداق جنایت جنگی باشد. خروج آمریکا از این نهاد، در چنین شرایطی، بار دیگر بحث درباره سابقه اقدامات این کشور، مسئله پاسخگویی در قبال نقض حقوق بشر و استفاده سیاسی از سازوکارهای حقوق بشری علیه ایران را مطرح کرده است؛ مسئله‌ای که می‌تواند نگرانی‌ها درباره تضعیف سازوکارهای بین‌المللی پاسخگویی و تکرار حوادثی مشابه میناب و لامرد را در سطح جهان افزایش دهد.
🔹
هشتصدوشصت‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/691250" target="_blank">📅 19:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs1ABfzblGDwlwrREubC0O9TSanLwtH_c-twws0IlCBl0LehP4Itp1Yyh_6VZMGE8f7-PWYDxYkF3dqNZiMzRRo96MSvsljt_jvG2PVf7jMEHGCSpYMQ8I5YLlLKM11OATv8YV4MqQT_4CBLaa-AKHkss7flcmXjOvRx87Hk5DRENqO-N8AS2JV0Llk5oYMpUY8YwGAACRUOeQtu9vpWwiffiSHtXNK8JchlRYlYRBQR1JnSs0uoUAVtX-BNL2IS1klqv13c345HKmOW-fBWXF8utIZyIxv46rW51zYZtU--XLVMnO23HCY-Lw9hmI74EzHydcqY7JTg0zHLVbSVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعت کاری ادارات از اول مهر تغییر می‌کند
🔹
طبق بخشنامه سازمان اداری و استخدامی، ساعات کاری دستگاه‌های اجرایی از اول مهر تا پایان سال، ۸ تا ۱۳ تعیین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/691249" target="_blank">📅 19:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgJmqp3n5HWjhwE7qGvhfGndzqNqRh2opJtf3IgdBL0BeA-Fqk5ygjf0W8x2R-_QTYD3VcpZz1ETd9tT5LeQ202ytQUKaeyE3ZVFjnaI3oE4hl2IpR7oqe7CpJRmyLaym6GV6wy8tY_pvgg6puvWRuV0rrjTSRDkJg8tdmfgfP5xp47TMRkRPzGMkBWK9T9HRUaXE-ES6JWJtO15jWHT_TGka_VhNXBT43sQs2O99cBujTvgDDfriebDpFXAnhIb542ib2Rdmff3ToONbmV6qlzjhtb68QmFnlH0VvDxExLt5a0uR46qiZaTX5cftXE5WGIIwrJnCbAsJ1fOeMNC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZxS2gtUiUKp0maa2EscYR7QvdSEQRycqvs_h3qPRqgAiNtOPJbgF0fCwn2OKKSq4CSC5tSuwT9_kX_aCp3cfMcibigbaT0aM3mTr13mm4SVea3veU2smKp77vzJq2zIIPW0354PkgTEt56KKKX-ZCsbXtQB0wE05VsSvTvpuNadxrf3N2AguxcVOFPjXwUKxGyfI8CvVPC6OmzUhHAfkGhwNI2yMCvmj9lGPnt9qebj7Is4iYH6cfjBbSnfQTmD0KeZJJsPqpPkLR8Rip5eg1aB8M_LhkhCDyr5pw-VpEtUHngIStfUnKSv1A28veMVslaEAN2XGbLONgeK-8QkcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوشش رسانه‌های عربی زبان و انگلیسی زبان الوفاق و تهران تایمز از رژه عظیم جانفدایان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/691247" target="_blank">📅 19:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نایب‌رئیس کمیسیون امنیت ملی: عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/691246" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
محسن رضایی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ  ترامپ هستیم   رضایی:
🔹
شرایط ما عبارت‌اند از: پایان‌دادن به جنگ در تمام جبهه‌ها، آزادکردن دارایی‌های توقیف‌شدهٔ ما و پایان‌دادن به محاصرهٔ دریایی.…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/691245" target="_blank">📅 19:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
محسن رضایی: اقدامات آمریکا و اسرائیل این اجازه را به ما می‌دهد که از معاهدهٔ منع گسترش سلاح‌های هسته‌ای (NPT) خارج شویم. هنوز تصمیمی برای خروج از NPT نگرفته‌ایم و این موضوع به رفتار واشنگتن بستگی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/691243" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoO4pIMmAkzlwzCSSVX_h5WoOK-Ip6FAr-Uzk-6c4C5Of0_gL1YWJa4lAq48Dh9p0Un-qHdLGsDFNjxgzsP0e_Z1wjytjGmdQB3SMfmRgnU8ToK7T0519HQNNm7DIoVcMuzPH_LwlnhS5NE4d0vMGgVihIWaQTFvueTUu_WO5oi8ZVMQJvSZBiEufgE52pXj8TzhARU5mgkJe8NJpyCJnhvGIpuiko5PALIfky8fS_b_LZIM0Tr6cS3r4FRsN6AMwyf2UIyTlH2NPR6DXMq05FPm4-atCmvTcw2owDmE39K_KIh3SjowO8gJtiAHZrMaa3VqC10P_KjfjvV1GJBqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از اینکه یک حادثه هزینه سنگینی روی دستتان بگذارد، خانه‌تان را با «جام آسیا» بیمه کنید
آتش‌سوزی، زلزله، انفجار، سرقت، ترکیدگی لوله آب از خطراتی هستند که می‌توانند به خانه و اثاثیه شما خسارت وارد کنند.
🛡
طرح جام آسیا؛ بیمه جان و مال
با پوشش‌های متنوع و
۵ بسته بیمه‌ای
، متناسب با نیاز و شرایط شما.
از سرمایه‌ای که برایش سال‌ها زحمت کشیده‌اید، امروز محافظت کنید
📲
برای مشاوره، استعلام و خرید بیمه جام آسیا کلیک کنید
👇
👇
https://online-li.bimehasia.ir/issue/jaam
https://online-li.bimehasia.ir/issue/jaam</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/691242" target="_blank">📅 19:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
محسن رضایی: اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم. به نفع واشنگتن است که برای خروج از جنگ، شروط ایران را بپذیرد  دبیر شورای‌عالی امنیت ملی:
🔹
ما همچنان به فتوای رهبر شهید انقلاب پایبندیم و دکترین هسته‌ای خود را تغییر نداده‌ایم،…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691240" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713eda6e84.mp4?token=VsGWJeDNHKXCBiMVw-kF2OCnlO7Xxb8UT4G4qbUHbLUZtcmX1NcCYhkftrskr-WQGrMQKNwORbGkvjJZKsa3tJBKHM6BWal5pKHok76CVQGMjYjIzvLPgl7Emjq73LYGxZM-ALPENrUNhx8Ss9FPMogpxDmg8w6aa9oItv-r5HLLIQTeYVVSP_COvQ-FeDC8P1kkDg6ckK12UpQNgPhkNpiOiEZkeS9pOsr-PNWve8_vHtxhzF2S04tZm6b3wxTTBoBquYT2eDREH8d_H7tU1MgYqkEsvdqTInuHwNHvtdf6TKZjg1lLiWNwcXn1dYEy8AvQ11tem6NotgiS5mu5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
مسیر موفق کارآفرینی؛ داستان کسب‌وکارهای نوپا و موفقی که با پشتکار رشد کردند.
🔸
روایت شما از آغاز کسب‌وکارتان می‌تواند انگیزه‌بخش دیگران باشد. در یک ویس ۳۰ ثانیه‌ای، داستان شروع کار خود را همراه با تصویر محصول یا خدماتتان برای ما ارسال کنید تا در خبرفوری منتشر شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/691239" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد  محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/691238" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: به نفع واشنگتن است که شرایط ما را برای پایان جنگ بپذیرد
محسن رضایی:
🔹
ما برای یک جنگ سرنوشت‌ساز آماده‌ایم. ما نقاط ضعف ارتش آمریکا را می‌دانیم و بیش از هر زمان دیگری برای مقابله با حملات هوایی آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691237" target="_blank">📅 18:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: سخنگوی کاخ سفید فهرستی طولانی از اتهامات علیه ایران مطرح کرده، اتهاماتی که بخش عمده آنها، با دقتی شگفت‌انگیز، همان اقداماتی را توصیف می‌کنند که خود آمریکا آغاز کرده، مرتکب شده یا از آنها حمایت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/691236" target="_blank">📅 18:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd708c6b05.mp4?token=LtgXpHxBVuL7OpMyZcmpeaEM2wTQsgLx05ZB1ukqIhkNR_tKbQqYDmzAwKrUoSM704mSRZGd8LxSBRcsjtTWHCBP26UZSZYSzpo37XZ4mooH7SMzgs-eAd5bTxy8M4sJ91x9JAbU-pn0CDWTka8hLw1Q2tX4sNEqESwkYpjCt_Nd_nrYLh90gDIXugBqe0jw45diIRdzEECLtS-guoSC5-5J2syuCweGmKGFjoTIyFdalT6s4d9PbdpGG8f_kYb9UJa4F9WVGqZtT4JE1k4CtvTfgTkl1El2SqjIdHXKHWWsVSh_dM5r4TfgVfCGbJsoqhngfZQhhXWBy1_94PaSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش نوشتن پیام‌های طولانی با گوشی سامسونگ؛ بدون دردسر و محدودیت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/691235" target="_blank">📅 18:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aobj1cjjyKPg6KWO4u54HrQVEQIG59OKjKA_fntJA3VbpHZH3mdzlH2En-SR3zBa3qXkdpfRk2q6MkH962TxnjHWdRSlMzfnpYMBL1k8oGdqoT8N-Rt6d-QXxymSTz8lNhy___F0xTqecGDuyzvJnHWaBR5Pk7kTVKPrBds2XUvztHz5TlM2c1V7udDxJV2kJB6xUYal2aanaegLlul_5_rpbPzgs4Ha51ClazuZLwj46B58Tn4U7j0CJ2WlQhd2ssLx0GnQ788JMykXnLnViud-lQwAD-7zjjBjZFNuuyjsrp8RxVR_vPInzMXSKgeLPdHRjNvyDNuTRONgUU-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8Ls33LCJew7q5iU1IE3PvH2WTGnsA1t1ds9AtDqDlrghFvjeLKsAGf74b6C7CEzf5XUsj4PgmFHXL-Yxq1COB5kair-2EENtQM8lltcgIbutpOMWr3bIk5Ghfs6ygfYGdVI6Os2Selp5HgNZlD9R4JEJACxt8A8UpZZzTpPTczvV0agfTHmrFF8eU32ZJyhdCKG6eXziZsVQ6NwXIYkQYE6hgt0aB8-bn6gcAEMtAKZ8vyUcg6z0v7-QukIDxE87_FXqBFC9xWJOi6JsbMTXjEUVuQdzN3edowe2V03XjTfqKQPQsjudqHYThK9li4qdDtSWuRhlBqFiWe736WsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCU_r-5K5cwS92K72HJL5RJldcE_aXjUcE7MZBEw4iV5eUbHGRdEZ_v15CcGMEFDe4OmJsWPTjIpIXOMREznXdXZYzzZhURDGCp9Bc2GCROlAOek5D0j9UVihJVHTPoL3aMBYQqGzD6UKWBKm--omRZ_u-0bdu_kCDUCG6FOKE2MCsJLTuiHB9d4SdXdgNKZnn3GSioqOnE6pe7BH4TzGKzwnqgygkORbG4XUY1-S-O_lBBUzrvk9QbF32YyNA27RudBdhN-zDTHi1bK3G9I08jHxYW7wf9BUyO1BuLk7cj-efpiFprN4oQZhDVm8lp-hULT0PrG3mCX_TpBUUkxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lucoR2zLlRCRl9iZI56nJVIp9oE67mVbo3ZNeQUbeF9tPwjSCvjD-q7Oh15nsfOUmDhYSDDBm1GhK4t5JTyJFSIb_vcKewlJ4bRNsma5itVdwKP2YjfWgznbu6OonoJLpmGcjavMHj34psRNRVFoD6MsTJEdv42oHD9c5Ui_-lY1urNPam0DiuLFsgyIHVaZBBoW0FuT7YwS_ZnfeMNBuhhu8kVFUCRPAxxuMvUo28EO_6ffY-7MtnA3zRRMV82A2TbNn7Qj4EUmxlGDurxL6I_Zf13dKnwnMMFqsP7Urgtu9MoL07kXaoGYNh6spRwf9K8MjQwcEn87IRuxOHWtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnecApdm_8xhj_Pta1pbx9FXquQbLgdS_PEHg-YLh6K7wr6joSx2TJ26HUpKNxdTHSXpiemjCkwWDJd5SncXid3fvGxaHi2vAJxHbXmnxu3mvrwnFnLifIjNiLufk6D4PbQ1Td1lhdQLyQs1i4s2wTdoFjo5jj1T5cPxmDwBU0fX-Kc_COjOZbIIDcE6nFi2wnHumIBi5fbrjGYO6Fh9DfslFAuCpvzrQIUVhutKP2WcXTzx-9UZp_Cff-qVX0wcJEZVZcv_jdWll783EbKwybvh-8V-LMjTUIJCEeUiq4_WValTkCZo4LvkWSAEaT3iAuVPoBR0sA7n-Ozi-Xt3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5To3_Mxv_sqY9lQX3Tdo9fI-GO47_8Xve__1zY41TIkO1SdbAX4ong5yUu6S_VaS-RT4GBcY5aeADnwmjDTwyJh5TVFT_Frle7AmrgAW0iwTaLa0D56eIV1j7sqT0P43NcOVh3_XmexlidpXwn_dQcNzgD_D9w0-72KZ6FPdkeWXAwJ5eYmmC1LRUxp-UWxhsMHz6a2j8RaUtiGrBYkgLaEJ64ybOBRTWtvT7IUB0EAg81dfRo9u3nEd3u2OY2Y9706ZZ_xyVGbJhUDrq5hnKcY52AKrcVM8qlIhLQG1cqrlKn4UZxeay6rBHbGAq6EUEqq7ELqcIuuyEWdWox7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4I19XYfQ2iZoDZH0nJumtWhjptpC2_V7Pn9Lk8ufPnTNrXHi0k1aXa2tOMhqRt_0lCW38tlqYv0Vjsb0Qvn1fKrZaSOr51rD_AE0mctYxjzf8Vn2hZNpA7T7SESuzHIhj0yQ3e91FhxWNX3osUVGs-5HzxCCoCmWiYKZtvdzvgwYSfjYBjAxWVRcXrSKTNv7Qo5SzVVBDfNp3tNbH0xFNMnEAsrE12u-e0TMgs31UHpi29K94I8Wni62hX_KGvMSgd_B0ITmoGZ_NRtJ2ZxbSA6nemsYEpvDSWU0lUb1C7Ocdillj8BCYLOx9_1rev4MRUk8JzUWzBGJAh4CItxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyiTRsjbVfyrrKpk7Kjt6nYIClY-QBP5h8edM2aAF1zLFFoUF2TsPXk1d8KYT44yJKbmRxXwNKMi21GvnrjYmjVJ_KKkp990ZVh5I2Da30ZVnA2PgsEJjC_artMjQBTefhFAPSMs5-f3XCo1aq6ao7rQhcTt_1PovwSswp-STmESiyeFUm7yA_MehXSkm_A3Rrp_QqPWgk0bX0QnSBjGk5UqlMYFm_KuZw11pvHDcBnyMgFY5z7PBA93WPLhxZgUWwko5m8hXQ9NV9_o2SRAB9Q62YsraoWAa-w48kl9P0DRPYJn2puTyKZiL9n7sf-bIkEEPouhcrboyvza4nwfAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوشش مطبوعات داخلی کشور از رژه جانفدایان ایران (۲)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/691227" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uROMedK3W0n4fLDQqXfRK3nZ2hJDeT7dP7f0KBEI1PcDdc9tRk0v064QvXZiIs6rdVQL0BNb4kFNkFgJRgsn8_RBZ-JsUXBhC3049m-uMIcByrG-8nUBWN9Zkj9ifZXWiKJ7OEiuR1p7xsJ3Sfk8IsjEblDwQcUHPGrYM1fFbxJWeO385fiYjSE3Z-WrGysd3U0pfDYZ8bGljKIVwS22YNf3cx2Qz_iep8ABjK4aBHZK2PVVNlYC4cVyQbQTYoOzRi8EuoEIAcKpEp-4UNnb49xmqejVRwoeut27UdkYlmq2g0hZE5Hs11YwsZxfBYB60JJkJz_vR7iArXCi2daqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام
انصارالله به عربستان: حملات بزرگتر در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/691226" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691224">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtyDqyGdF80OYMzZ6hfxNo1Jbi5OF745YfBUQLmp3IuxMniWFi3qoqiKpIfuVA0Q3q8QX4XtSpbTEG3_73cq1tazSRShaOVf6SAmpXydhthXcTl6M56FfhOWePd6aPmuCrzaGC0anCdKyTiZlBCZ36YiDBbH23miCOEX1ERE3lyCVCnyCy9zl4OfJjN5HS2saYCAb1aM8jLswts9nQzE2rBBpNavLxZktiagRwvBeuz_RzYLPdp0ROnwWllMDpuDAq81npYBpzzgtWQiboyvsjdJ1A4kEcQ79I90LL4US4ShtrQNVNaflODX2KDP19TJvmVoW0txZC0Bm3BuaQ5jDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wkjg2G66nq2c_FRNVopWoAmD-oE7KWGfYR1BVF4e4--uCEvs1K97DCFFdRDVtPf7mGwMzW5PsQuSaIRmdqyQQi1PcXZNK_ZOolTUZWNey3zBSTocFJjXQouPKr5GuHMFtq8keoVfwm8PO-23o0zIjK1oz6K0ly0aTILTSVjhoAB3-l8CfLk_rjYriIPwjjKllpp536ZLLROK9YjIqrhhBgOEdSA-EybrKzFI-AgAPEHQ0R_L_md6ejUje91OOXLN9umsk_HgOFZ34FZDSDZ_Oy-v0ouUA3nOrJaDgho39JY-qx65l7r7D9WejczmiwNfvoUCK0VXvJUg-Z5ApN8U0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جایگاه دانشگاه‌های کشورهای اسلامی
🔹
بر اساس رتبه‌بندی تایمز، ترکیه با داشتن ۹۱ دانشگاه در رتبه نخست کشورهای اسلامی از نظر تعداد دانشگاه‌های برتر قرار دارد.
🔹
ایران نیز با ۸۱ دانشگاه در جایگاه دوم جای گرفته و کشورهای پاکستان با ۴۷ و مصر با ۳۵ دانشگاه در رتبه‌های بعدی قرار دارند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/691224" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f01df87d.mp4?token=DHpQ5A6LdEt7KBGQZaTOpLbKo8D7U85l-6xllKQqe18LNBqSsoJ8IYnAUWZ7922qajgpafs8y3JQkNlZ4YsLEyd0UbPi3A2uJvY1u4UuEL0lNp_nZkCTRuDeH7jJBIqqQSKeOPRSzck5wU57XZwN5i_RDDPllOadgMjMnqsyzTci31xc-X4U4tvrTuH0YUZspA1uwgWfRxDkyeuDihmiTSRHQKGpIfH659nemyi6bqypO7sbq9s1rcWCUvwPITvm-5l7XN-cpDenYyZ7axDVQQHQ-EEsBYPASxcc23go_Sojp0QkIk9jxFnGNRx688bp2CHNIorfFksufsTjNVaZ9TU4rsDfg4T4xfvpCo-pEbCN36Y_XwMjdYv3VAxXCSZTKkW-Z6iRUrlP1-KuZymRjAtH-iHPM2PJaVkgjMZbLvyNUHGrmUPnKTq6b_0WS0UmDweeaXrtqZ5VNzVsfnnQCLaKGnzT40o5OQ9Aofg2ErlBI4VRsT1_GvvJZ7qemPaA6uvoGTY2ubiZKlkpo6BGEG2JygwnFLd4rwN0_zOWJecDCpdW74VSNa7J7KO8P-TsmzGiBp98oaSa5jWpEoYMthDypcP6JXKFJLz6k3MUW9EggpAZyeFiXxJvFJNXvHJO7jkRoKcHUz0OKquTAaYv9s6LBakkKxRT089IrBldE1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کافیه این ۱۵ ساختار زبان رو هر روز تمرین کنی تا خیلی سریع انگلیسی یاد بگیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/691222" target="_blank">📅 18:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c94427c5.mp4?token=aNjewiKspeyecyG9Dtt7qzXNP8IEztwo54BZZZk2R3KMGGKnkhudIId-LDMXHBEidqvp-iFkk1HQVnFh-vHtA4xdWBd527DgOX5FtujdLrWpPx8QA6fm5Q4bECo-jhskiOOgbyfgfaiJ6DCPWVFzRFMWc-y7lytut8W2Je5WUX-elIY7vUBTG7zWHecB47KbNf0b0WUY2ODvrRFtzLn0X6RvPB3gz3o3X57E1t3AXUJfXslHEab5BXySPLzDMiPvP62NyXn4jRga9CmKSSqk8myfcHJb4ydA1-G3XD76qQTysbw5MRm1VhDzj1k3oKSjtHWqFXyHg1Cy-ScZ9ZQsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک قبیله بومی منزوی در آمازون که از هوا عکاسی شده. آن‌ها نمی‌دانند ما وجود داریم؛ و ما نمی‌دانیم در ذهن آن‌ها جهان دقیقاً چه معنایی دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/691221" target="_blank">📅 18:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caugzHpFW6s2DYbzwaVOKXFAfRKNnOF04FgPLISBCS4VaFaJ2kZ_3ETA5nGrKWwL2O7lvNxHemWMfoGc-WEpB9mxc3q3MHNiBW2lBW7tzl90ps-2JWAIt1MaY8rszayfmFrQ7dSmgcPVhcTYNt_09L9wNtBowAFt9me28ciyD9ihhJY0u6Uz9Nx7Xi-I-HfrA8n3j2AfY99dFTHdyk_gTcOMvrWM30TwsSQO8i8wZ-a_UthYzwf4DKKJGGXksOrPpSOImFJKCXEkWavFGrhoaowI5jv3PRg6E5EH2riMk1EMX6P4N5qYIbvj3YiU_y5YKhFBFjT7eiWRudh2V6r4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخبه و مخترع باشرف، خانم لیلا کشاورز در بیست و پنجمین دوره مسابقات علمی و فناوری جوانان و نوجوانان آسیا در مالزی با کیف مدرسه نمادین به یاد کودکان میناب ظاهر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/691219" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcP3JuqO4dCpK0xS4U2VkfG7Ew7dodngbMzXKq6cOtGaJWNd97SfnnzyZXPq_cgGKkJua-6n-8CNTmeSuGqsBKfc6MIN9TQkmcEnKihV4qWpnoWFRLFoKjvumFXK8I6hCZh305ybaOm8gy5EiC8DT9JpQ-yueXzT3gratpNYnIaN6ak9E23ajfx-rn1qS5A7p2CA82QUzLAUNf39OO7t2JKa5Q0D9Gkh2vJKi53XwGMjjUzLXfC3m3Jq3QTqNIDg4QKN_FTRs9Ds4dWk5Pfe-b-f9IgZDBUlG-IAGFa6blbvfpI1kXVsXJi-gG-Cg_yUho9mNcbcnCg_eKERWIi4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه سفارت ایران در مجارستان به بلاتکلیفی ترامپ: راه خروج از جنگ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691218" target="_blank">📅 17:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691217">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40dcd9622e.mp4?token=FHWcjkTRV-6xOOBB7fh_HMVHD2ziqmSIEzBln9IxE0YmWJZlVEE-SsFYPWAYwEbHGbQPZT3AYqdfe7XJ-hMOQA1fhjzNn3AOjhjBWoRoVCNop8uyYeZ0PEc4-60X3glxaQdsGa7EJFw8_rF8LniPv1Ed9W9TedH82Ylceb7UM2xcsolY8zjRLvRC9q2UZP3wHRepzcstaAMgD49rgf_GFkTLVUFcoqe99iCDeLbgorzljLclleq_jC5PVdfjN2Thz0EIUyR9aZ30-dkstmg6plcyiR3E_Fd3N4FD49dsDIAmZU04EP8Ce-PdCG3oLJPJeEPRooU3Dqj0gKzXyG4IZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند حامد مدرس، مجری کودک‌ و نوجوان به لاله مرزبان!
🔹
چطور تونستی چشمت رو روی ۱۶۸ کودک معصوم ببندی؟
🔹
اون جایزه ای که گرفتی چند؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691217" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691216">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اوضاع نابسامان درآمد پرستاران، ۲۴ ساعت مراقبت از بیمار فقط ۶۰۰ هزار تومان!
محمد شریفی مقدم، دبیرکل خانه پرستار در
#گفتگو
با خبرفوری:
🔹
تعرفه خدمات پرستاری برای ۲۴ ساعت مراقبت از یک بیمار حدود ۶۰۰ هزار تومان محاسبه می‌شود و پس از کسر کسورات حدود ۵۰۰ هزار تومان باقی می‌ماند.
🔹
این مبلغ برای مجموعه خدماتی که طی ۲۴ ساعت توسط پرستار، کمک‌پرستار، مدیریت پرستاری و سوپروایزر به بیمار ارائه می‌شود، است.
🔹
در مقابل ویزیت یک پزشک حدود ۵۰۰ هزار تومان محاسبه می‌شود و این اختلاف یکی از عوامل نارضایتی و کاهش انگیزه پرستاران است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691216" target="_blank">📅 17:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهای حامی اوکراین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691215" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66205bdc1.mp4?token=ShDwsbOitQ9s6f8oaKpph83wRGzhEW8euOLGe9zyWbeBwrIO8Gx6Briqu8Q0mg1pavXOp9HZc88GvNtZUblI_zEgOBMy-XWGggYlyIHgq9jhISqpSv5ITHtIeEXYi-_wv4-ZKstVX1SnFtY1GUnv2pxgyJrxGJ5v_ZKbpUj4cw3tRz0RBa2cSTPB3PzAwR-U7R7lduqHIcCLZ5EaiSThkKNlN1ZxwG23KxzWXxlPYtkPJOLFKrvChjidMX6OqxCMllhDP7vDarNH4O0snw2IakO1HX2kboDmOaFsGjRIXCtV2y7asswU40rUQMri6xhyaHLuguXT37TNgotFU4ojgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال‌شده از تهیه و جمع‌آوری تخمه آفتابگردان با لاستیک ماشین در ضعیف‌ترین وضعیت بهداشتی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691214" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTahagasht(Tahagasht Social)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs835RAb9d4R8TUcsja6G9pJUvdEeUa4fFs1SsIrBDFJKYO4jmDvlbABJ6tLIALfo5VZkxGqPujfJyAb8cjsAAoOsoVG1VadDFz9dJdhTOuIvbnMTRemQ4lnO2aArhKWHF7R8irkeB2a3i1eG6VYQqS0UezUo_bkbw6tT9XVTpCLTxi4WEJoqJqtFTpWFV91XSSpJXJGUu4s99LkUpEFCgP492i-dLEuAnvhiJ2FnqIG-GIHMeoXnvRzpcVXIZuhfvr2Xkx5BjhwjXLKEiuUBnsfK1O3SvBy8IP0bTXcr-yJedkhM0bbaDAzYVWc-y0Mlk4x2smZBr_EHIztr3Se1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
تورهای تکراری ممنوع!
✈️
سفرت رو خلق کن!
سفر رویایی‌ت از همین‌جا شروع می‌شه!
✨
🔹
بهترین نرخ پرواز و هتل
🔹
تنوع گسترده هتل‌ها برای هر سبک سفر
🔹
انتخاب مقصد، تاریخ و مدت اقامت
🔹
طراحی سفر متناسب با سلیقه و بودجه شما
🌍
همین حالا سفر دلخواهت رو بساز و رزرو کن!
📲
تلگرام:
https://t.me/+2wRXAjoDIG44M2I0
🌐
www.tahagasht.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691213" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای مضحک سنتکام: ایران به‌لطف محاصره شدید ما حتی یک بشکه نفت صادر نکرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/691212" target="_blank">📅 17:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEU1ecrEKoMCpl_ftYt-6pvpK6m_4Z4F5mkJ0HE5DMP2th286mMJv0WrrrtrNuUN9uM6ZU58hjjHjnXqb4tnerImaJXiaaZ40hOc1lTOG08Ihw1sB47AL3FTMaiPztH2Sg75k6difw72r_dUqSwo7bjSKaN4rfmuO1biTYffZv13KmaB_Ev2dtvEPmvyNJVcIvVnhWTyNBWEZVF0SMcHGjMvnA8RlS-mhSjlrxjToP1RcVVHs_emRSjqanV5HkJPB84pFtj0bKcbN9hNpwnxJmKWboUZZjNLcsimtDtf65kPjjKPK9tKi418H_A9YffA1CWJM8ux4MIMUthGnSgi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نان مناسب برای دیابت
🍞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691211" target="_blank">📅 17:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
فروش نفت ایران در شهریور امسال از ۳ میلیارد دلار فراتر رفت/ این رقم بیشتر‌ین میزان ماهانه در ۲ سال گذشته است
🔹
طبق آمار سازمان برنامه، درآمد نفتی کشور تاکنون بیش‌تر از سقف بودجه محقق شده./ فارس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691210" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLVBtI4CNETbRTUalq91VpTTgqU7SKl4tDbGJuuubMHd6GTxT_QwFNd7SwphoewbGCHn-irYjnOTm2b8vwOcO7pd7f42Jd3iB7GQmpMiZS0YNcSLGhtpcWcZFFifR9wSjfvPMm3hImNCkYDVdAMuWlF5g1qgmzs4YyDv_SjzfwZF9xZuPcUo75O-Z8STTxYVul50uLviMyx__dYed6UMAUwibTXUK4KQZL9WCZOocUZPppyMjnP0pbwIRASqF5x0C5tg1aRnghZzqH5LIddqh2vvrW4qEvOD_Cu8RNzGdBdnb3_RUTkdXo25qLZrYO0RMvEJpU6AHheHaehF4MsJlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN گزارش داد که در آمریکا میزان جستجوی "قیمت بنزین" در گوگل طی یک ماه اخیر ۳۵۷٪ افزایش داشته است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691209" target="_blank">📅 16:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فروش نفت ایران در شهریور امسال از ۳ میلیارد دلار فراتر رفت/ این رقم بیشتر‌ین میزان ماهانه در ۲ سال گذشته است
🔹
طبق آمار سازمان برنامه، درآمد نفتی کشور تاکنون بیش‌تر از سقف بودجه محقق شده./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691208" target="_blank">📅 16:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ba6c7af0.mp4?token=YN5Ml1Yj3Db50natfkzsI-Z2mGpWDsOkrXGtHZB0hedLCUCTZ1S0xG0m4s6EDKnOjKJFY2VYBsq3QU-Mj1rQWf8qOb0sLbT9472RUaBhx_Y6Bz_1wIZHTsGQ9s7ojJqtXgGl5IAAr31QT3DaSte5aAL5-0EAjmherdhjBRialpxvR42m5qND-Wxh8nh6tjy7ncG6lPhObgfbwkMNe2FVNWVTfl_5cMiz5UQUsEdLrhOKYbZu9BF_c-N0DTLg0z4OIk0K4uWDFz6ujoCHeKthhqGdONS2OqXADmq3M1Ddljqh88YTHI6e0q7EIr5gijIjWCHcEdTSlyA0dl9nsTsF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ba6c7af0.mp4?token=YN5Ml1Yj3Db50natfkzsI-Z2mGpWDsOkrXGtHZB0hedLCUCTZ1S0xG0m4s6EDKnOjKJFY2VYBsq3QU-Mj1rQWf8qOb0sLbT9472RUaBhx_Y6Bz_1wIZHTsGQ9s7ojJqtXgGl5IAAr31QT3DaSte5aAL5-0EAjmherdhjBRialpxvR42m5qND-Wxh8nh6tjy7ncG6lPhObgfbwkMNe2FVNWVTfl_5cMiz5UQUsEdLrhOKYbZu9BF_c-N0DTLg0z4OIk0K4uWDFz6ujoCHeKthhqGdONS2OqXADmq3M1Ddljqh88YTHI6e0q7EIr5gijIjWCHcEdTSlyA0dl9nsTsF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پزشک در لیبریا با روشی ساده و به گفته خودش مؤثر در هر شرایطی، نوزاد گریان را در چند ثانیه آرام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/691207" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
قصه‌ «پل بیات»، قصه‌ یک سازه نیست؛
‌
قصه‌ آدم‌هایی‌ست که نگذاشتند یک شریان حیاتی از نفس بیفتد.
‌
این‌بار، تصاویر حرف می‌زنند…
‌
🔹
پل بیات؛ روایت یک بازگشت
‌
#سازمان_راهداری_و_حمل_ونقل_جاده‌ای
#آزادراه_زنجان_تبریز
#پل_بیات
‌
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691206" target="_blank">📅 16:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عوارض رفت‌وبرگشت آزادراه تهران–شمال در روزهای تعطیل به ۷۲۰ هزار تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691205" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccb9c545ee.mp4?token=LEwvs9m0U8ypLqOr4PvTgjevJDlmHRUauS-QeK4SBWS1XxvnZHPUdOE2E_o3MVtBN0fJMmEuAlmfinsbryX-LU0QZb0Xu8tYAeCPH0niSgi6g2g4J2DMtH2xFu_A12M42cLLcRClj6aH4Pp66Ez4-6hGjvfcNUllWNYAHk8DNX0czto9SHbMIj712MbiY1FExpTyi_gRaTAc7qtUdiYx_27ENNT3QYFsfFsFAykRrzD-f_wCQGKZjbrRlz6JmOdDOg6BejPmRRM0ztj1xHqH9zLYV096ZgC890nNr-mXKIrdkK6Bp2CEzNffYBnGWI5uJRsy-QLeEy0z5Q3pRmjWM0EjLPCtXdKzNiZeYSqjxftHIW1hgTJzzInu1mpt9AKS5Q0zgvf1b5ab-KDfApLwLLKx5EO9rDPXa_btPPS9J4mrmBVKjOy_aPRMj0mdALZDmQxaayqAflgEvB4VjESR3BSLjAEhcpnaUeakZzzbF7SZRCeqHI-36f44Qv0hHW2nnzVgr8zfrn2fiJn5dg-M4g3_YSn2SWOEunsvf01rCoenrEz7mtDjJdf1ZhguJ7kq3k4cWRFOeyUm-vcPPqgQE1GlOGwUxJPNqvMbdEaeF5B6FvcnxmxsWQ5sRb9ctaGQj0IXR8_jfLVzcGUKCfCkX1RI3nCyMbShd04uw08aw04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccb9c545ee.mp4?token=LEwvs9m0U8ypLqOr4PvTgjevJDlmHRUauS-QeK4SBWS1XxvnZHPUdOE2E_o3MVtBN0fJMmEuAlmfinsbryX-LU0QZb0Xu8tYAeCPH0niSgi6g2g4J2DMtH2xFu_A12M42cLLcRClj6aH4Pp66Ez4-6hGjvfcNUllWNYAHk8DNX0czto9SHbMIj712MbiY1FExpTyi_gRaTAc7qtUdiYx_27ENNT3QYFsfFsFAykRrzD-f_wCQGKZjbrRlz6JmOdDOg6BejPmRRM0ztj1xHqH9zLYV096ZgC890nNr-mXKIrdkK6Bp2CEzNffYBnGWI5uJRsy-QLeEy0z5Q3pRmjWM0EjLPCtXdKzNiZeYSqjxftHIW1hgTJzzInu1mpt9AKS5Q0zgvf1b5ab-KDfApLwLLKx5EO9rDPXa_btPPS9J4mrmBVKjOy_aPRMj0mdALZDmQxaayqAflgEvB4VjESR3BSLjAEhcpnaUeakZzzbF7SZRCeqHI-36f44Qv0hHW2nnzVgr8zfrn2fiJn5dg-M4g3_YSn2SWOEunsvf01rCoenrEz7mtDjJdf1ZhguJ7kq3k4cWRFOeyUm-vcPPqgQE1GlOGwUxJPNqvMbdEaeF5B6FvcnxmxsWQ5sRb9ctaGQj0IXR8_jfLVzcGUKCfCkX1RI3nCyMbShd04uw08aw04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا انسانِ معمولی هم می‌تواند با فرشتگان ارتباط بگیرد؟
🔹
پاسخی عمیق به یکی از رازآلودترین پرسش‌ها درباره مرزهای غیب و شهود در زندگی روزمره./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/691204" target="_blank">📅 16:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a90b8817.mp4?token=ofeiGLNpMQVJJU5bdQeAkoxegg7s1_CRDMpK58Iql2A7RFzM6_bOKjFWxSRPeouIr0TQPpfn2EWO1KJn__ffQrhNKUUUXU9TYBqrMMoG2HmeUU22V-YNxsPSbLxeDEU4Hafvry-VdM1r8bdEHLh0dJRew-PcTHA3ujV09lTrFwCI0tFeakCNHczx1TAXbBVBhPBvPNRuEMtmTsYO07n2k_aQrcMK6nGRgPUGyENw_d0VR9_qkSm-z4xIonWWqOEmDHBG_QY-AMksaTmSsKHPN0xBj4cBzGiJJhRudBLhQnTLuNYFkhRTekOYLW4hLhvX44EmK1TqN051dtM0EJdInYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a90b8817.mp4?token=ofeiGLNpMQVJJU5bdQeAkoxegg7s1_CRDMpK58Iql2A7RFzM6_bOKjFWxSRPeouIr0TQPpfn2EWO1KJn__ffQrhNKUUUXU9TYBqrMMoG2HmeUU22V-YNxsPSbLxeDEU4Hafvry-VdM1r8bdEHLh0dJRew-PcTHA3ujV09lTrFwCI0tFeakCNHczx1TAXbBVBhPBvPNRuEMtmTsYO07n2k_aQrcMK6nGRgPUGyENw_d0VR9_qkSm-z4xIonWWqOEmDHBG_QY-AMksaTmSsKHPN0xBj4cBzGiJJhRudBLhQnTLuNYFkhRTekOYLW4hLhvX44EmK1TqN051dtM0EJdInYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر نوری در پی یک حادثه رانندگی و تصادف شدید، باید جراحی شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/691203" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGx5Je1YNTP_1DuEnnzmfLfsZeVLhaBWooi4BOhnLugHJfTx5-7oPnwPDSwF3QsoWdaQD0DcMEc78QP7Xv3Wh0QeAK6A3BXMKnqvFzGElkbxO8rWMs_NpQUzSCcELf53rr8FiDY7wa6dFqBtW64iazZMoA7X87HhMaMwURGVEukNjP5i-TR9Ugfh0uGStYQGYuzqUx4iThgHdbuntPwNReIZp2Q3PYSVnGgYjFZqebqNYKRUuS_1uGHpef8sbFGSifYjtCoR0V-LWBXreku1OrPqZ4VS-Vle8hOp6bAzNcNP89MgWtvFziGZwCvDd2xxTz_JNGuzD499imcHBKidjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش فاکس‌نیوز
:
قیمت گازوئیل به دلیل تشدید تنش‌ها در خاورمیانه، به رکورد میانگین ملی ۶٫۴۴ دلار به ازای هر گالن رسید
🔹
فاکس‌نیوز، رسانه طرفدار ترامپ، چند روزه داره مخالف ترامپ پیام می‌زاره؛ شاید جمهوری‌خواه‌ها میخوان راه‌شون رو کمی از ترامپ جدا کنن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/691202" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047145406b.mp4?token=AVVTmQSrYLrl28ic42WM6XB8_A5o8jah5rLWYxlEDsMi89usMxcZyXeYCRaBqUq3cU5ck61VjiWb8kFuSUp3vZSAZc_bxcYyhQbTPR4ACdrP7EgeWOzIjcMIcDAnqRUIwEJvIK2vBmdItcmghzKBI6zhLdxJ1epGBoXrnvzEmqoMMsnJ-tBpEMOHA-qU8sxmCOGmu6Gd-WQKFt-dvD5CAx6psaH2wL-W6bdlVIxpGBlKJJ21-6hVAtzknUvT5lLL7hZWvQ3We_-WU-6TCSRXP8NLkxZqibhZAlKkL2EtViEB1ufSZU0i61mMBrxY7SjArAaoOAOQo9XJ_TZuzKYbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047145406b.mp4?token=AVVTmQSrYLrl28ic42WM6XB8_A5o8jah5rLWYxlEDsMi89usMxcZyXeYCRaBqUq3cU5ck61VjiWb8kFuSUp3vZSAZc_bxcYyhQbTPR4ACdrP7EgeWOzIjcMIcDAnqRUIwEJvIK2vBmdItcmghzKBI6zhLdxJ1epGBoXrnvzEmqoMMsnJ-tBpEMOHA-qU8sxmCOGmu6Gd-WQKFt-dvD5CAx6psaH2wL-W6bdlVIxpGBlKJJ21-6hVAtzknUvT5lLL7hZWvQ3We_-WU-6TCSRXP8NLkxZqibhZAlKkL2EtViEB1ufSZU0i61mMBrxY7SjArAaoOAOQo9XJ_TZuzKYbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: آتش‌سوزی در تأسیسات نفتی آرامکو عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/691201" target="_blank">📅 16:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4mCW2gWIP9q7m_VGC7dU18JVF0dnIoUoBcLs094rQgh_G82FsiPze4d9mAUNqJIGuV4O6aedTFEMJvDXc5b4SX2PY9dVVTb87o2L62MCVsjaPohLNBRcb55WJkM-PUG5o7yV_PfPM2snbpkgmJJxh60SPOX_5FiuHKAwBhcRDRLLPPKLk66XywKE5eNglmy5rklEL3Dcdz4R9SthmD6GvoZrD563lP1A5b3Cugp7CQM_RlpsT6RpmSLxSzOygc7HxTwmomiZRYBaNRv5o93azlpYvmsDBVDyp-pbK8Rl9FbyjWEXo3dXCewf7Fgcy60mcrxBc8JhzeNeiFx3ksM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
واشنگتن‌پست: جهش بزرگ قیمت بنزین آمریکا هنوز در راه است. بدترین بخش شوک اقتصادی ناشی از اختلال در بازار انرژی هنوز از راه نرسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691200" target="_blank">📅 16:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک مقام ارشد نظامی آمریکا به شبکه ABC News: ترمیم خسارات وارد شده به پایگاه‌های آمریکا در خاورمیانه در پی حملات ایران ممکن است «دهه‌ها» زمان ببرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/691199" target="_blank">📅 16:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745d49995a.mp4?token=Ur0wsf1okGIrvqVLpF5dlbxpohc1Q4-VadL_tymsTkekO9p3vMOOT4xqHn9leJ-7HUdWtNWVRT1H2F3ow0A6fVhl-8f85ZrLmjuFyTqN4pFvzQkL6YJ-ufYi8aEwEUST4Ty-pwl4LxeAkBoOd5t-BPt7DOYpmZkvf5mFyES3LaoeWse2HcE6HAH3uFNPzsAx-rz33Nhd_ShXELpgjSwAGICPva2NjDtRa9Zd_W3odpYZNdqUWjNyq7pvePxdLu_9XASvNyhfbuZr7XRlqMsyIlK8PSegKqSnU0FPkg5t2El2O9MvHPyf8m-oVGLc0q_7U6wIPMElRdaqIExIQEPX_3jUmL2kjuClNpQHa891mJiWidtSy9XP_NEVW829mJtzjnE8ZYCi2kZLBQNVl186MEQPFJAqltR5syHT4xhKJltrTryeYZBUmpEXcbytSRN-ISCe00rcAOGSz26gOE3_zUupaHxJhxSOripXemat7aGRNfY-EWOtZfaD7KamgnTzv06NsYFt9y8twLukgAdbR5WM6KKa98V_lEVV_KrPXZrkYq7kUFXDdQmAifEzZexsiux9xlg5x40k6HwOXZjW_6t5t1zAoGJxu9Zq-D-S-jC-n7J6s7jbpe6Xn2cAaGpGp8Bz2QjIUWdhtj3Oyks6YAvALFONS0dU4VRq9fo3jh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745d49995a.mp4?token=Ur0wsf1okGIrvqVLpF5dlbxpohc1Q4-VadL_tymsTkekO9p3vMOOT4xqHn9leJ-7HUdWtNWVRT1H2F3ow0A6fVhl-8f85ZrLmjuFyTqN4pFvzQkL6YJ-ufYi8aEwEUST4Ty-pwl4LxeAkBoOd5t-BPt7DOYpmZkvf5mFyES3LaoeWse2HcE6HAH3uFNPzsAx-rz33Nhd_ShXELpgjSwAGICPva2NjDtRa9Zd_W3odpYZNdqUWjNyq7pvePxdLu_9XASvNyhfbuZr7XRlqMsyIlK8PSegKqSnU0FPkg5t2El2O9MvHPyf8m-oVGLc0q_7U6wIPMElRdaqIExIQEPX_3jUmL2kjuClNpQHa891mJiWidtSy9XP_NEVW829mJtzjnE8ZYCi2kZLBQNVl186MEQPFJAqltR5syHT4xhKJltrTryeYZBUmpEXcbytSRN-ISCe00rcAOGSz26gOE3_zUupaHxJhxSOripXemat7aGRNfY-EWOtZfaD7KamgnTzv06NsYFt9y8twLukgAdbR5WM6KKa98V_lEVV_KrPXZrkYq7kUFXDdQmAifEzZexsiux9xlg5x40k6HwOXZjW_6t5t1zAoGJxu9Zq-D-S-jC-n7J6s7jbpe6Xn2cAaGpGp8Bz2QjIUWdhtj3Oyks6YAvALFONS0dU4VRq9fo3jh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تأثیر جنگ بر هزینه انرژی اروپا؛ بنزین در برلین ۵۰ درصد افزایش یافت
/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/691198" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
فرماندار جاسک: انفجارهای کنترل‌شده در جاسک هرمزگان/ این عملیات تا ساعت ۱۸ ادامه خواهد داشت
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/691197" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qREtlmnhf2IUKpTa7lpdf8AsLOBniVJmLgl1idDbroyHYHXMIhk88LgPyihRrAWaiQJnSlsg2qhnD-K-JVzqJKrHMWGzPK9oXu0PQMeODj6JnB1dXlJ0wdlcieQYAwb19CtZsu_Hy4wLGVffIRibNKB55JGqHlsg8AulE-BdKb8LisJ_9U8nzcLl9rlcj4us5dUvFU268fKuFzwQ5x0030SNbHXqy-sNpeqyPC68pA73CJJ07FQcgxXf1PgOOpu9v0UwiASUeLBjK8ccoNTiKmo0WIeaoaTYUiALobvyLl-KdF3tOdQoBBFxwOHdvYfo1ORxYun6uoaW6rsdvyNY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت جشن ولادت باسعادت حضرت امام حسن عسکری(ع)، اجتماع بزرگ «امام زمانی‌ها» برگزار می‌شود.
این آیین باشکوه با حضور عاشقان و منتظران حضرت ولی‌عصر(عج)، یکشنبه ۲۹ شهریورماه، ساعت ۱۹:۳۰ در میدان راه‌آهن تهران برگزار خواهد شد.
از عموم ارادتمندان و علاقه‌مندان دعوت می‌شود با حضور در این اجتماع، در گرامیداشت این میلاد فرخنده همراه و همدل باشند.
شهرداری منطقه ۱۱ تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/691196" target="_blank">📅 16:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBF6xsCJRKIPgpGZghDb8orfcsNl_Wt9HhVmGhVAwPSz49aVlkIhwI2T5F3GPPs9kjrhaOexDIFURf7mUTWKEsIdCVjNV2Lr5CzLpMkCScE-sGiiMnAzAKm67oQdMxjYyYY-hPe6u5QKjM81dJ7hzFtxeu4bDPvnGST-vpHTfrwg35kUTN7UbI-_ZWbiFows_VTui_vln2RH7ZL7Pvy2oLcqYkBrE9b6NHPQ0nEVMiL7hW4lTzd0MuNZERD4clp-7YlEsdt55U0MEsNAtSFrngWF0_kbrVBMCgAz6E9fs1bEQsDrOugVujomVvoWyf3pdBzgemdOH6W3Zs5KwjT3gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: عربستان دهه‌ها برای حمایت نظامی آمریکا سرمایه‌گذاری کرد؛ حالا واشنگتن پا پیش نمی‌گذارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/691195" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تکذیب تعلیق فدراسیون بدنسازی/ ملکی: هیچ ایمیلی دریافت نکرده‌ایم
مجتبی ملکی، رئیس فدراسیون بدنسازی:
🔹
هیچ ایمیلی از سوی فدراسیون جهانی IFBB درباره تعلیق فدراسیون بدنسازی ایران دریافت نکرده‌ایم.
🔹
برخلاف اخبار منتشرشده، چنین ایمیلی نه برای فدراسیون بدنسازی و نه برای دیگر نهادهای ورزشی ایران ارسال نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/691194" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjiR_yCtsUtoQoGf4LqraRZ-w-8UB75siyXXLOovA1mRTSpofZS8pgEqKVzFzolwNwc9q__hiYwCYFRB5CNIoYpI_4SOP4MjGhCfPOQfqefSmIDZ9qfVSlSj4w7rhkG9bdvS7Z41CKMpJS0Bmv501k78sE-QLHdNeqOdMFv5CQkWatIkWDQU7Sv8RRwG3xZoeIjqQN2f5WhjqICh9g6XGWjIGR2lMGhOFAZAqUPvbdZNWkbwAIvXm5PUOGSYU2wE3WKRh5U7nnFxwrWgXOgv02Cbjf3byuJsJJiSNVDOp6tKiDU65cRvIUZMtZaPKPXxiMAUu9HdT7PAm5UN-HGJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آندرانیک تیموریان از تیم ملی جدا شد
🔹
آندرانیک تیموریان که در سال‌های اخیر در کادر فنی تیم ملی فعالیت کرده و حتی در جام جهانی هم روی نیمکت حضور داشت، از تیم ملی جدا شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/691193" target="_blank">📅 15:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbadb7e5.mp4?token=CwUU9ng-I45O-NYUCs6CD0LUJIxKgX8RbsJGVdv8VFLMU5BhNd0w48u35bK5D6NuXqboUvt4EoDK5e-HZv7K7YzmDnh55aadsaXd8aaYZ0vPiuypLqGExJ3vExEde-1cIiXCuTRvj34FRee8Q_VnMWBZmED3xs8Vww83ybYEe8ByAQYW3LcveOiBGa8SUR3TyAKau3LFXMhSixe_NuMY8GAk6-GRDXREAnNUBFB6-wqYphUW4C0UxbDvdckkBWyDtyRmraOJBEPTYHZBw95J9IIM8Av0rVrBZRs6JiYssiiX-GoZHRpR-UdYjGeD_HIJb2yHMnsOMQ-ZFfAS8j85TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbadb7e5.mp4?token=CwUU9ng-I45O-NYUCs6CD0LUJIxKgX8RbsJGVdv8VFLMU5BhNd0w48u35bK5D6NuXqboUvt4EoDK5e-HZv7K7YzmDnh55aadsaXd8aaYZ0vPiuypLqGExJ3vExEde-1cIiXCuTRvj34FRee8Q_VnMWBZmED3xs8Vww83ybYEe8ByAQYW3LcveOiBGa8SUR3TyAKau3LFXMhSixe_NuMY8GAk6-GRDXREAnNUBFB6-wqYphUW4C0UxbDvdckkBWyDtyRmraOJBEPTYHZBw95J9IIM8Av0rVrBZRs6JiYssiiX-GoZHRpR-UdYjGeD_HIJb2yHMnsOMQ-ZFfAS8j85TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فینگر لایم (لیمو خاویاری)، عجیب‌ترین لیموترش دنیا
!
🍋‍🟩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691192" target="_blank">📅 15:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANdCmk4FWhk1bQA3owdXL_M3pxDu-il0ua58gvgcjm9zNek4mPFQFJNZUTOzwe5wcZYBr-ZiokFGMFfLYPbci_dTDAsHu377rktwmTmE8uUiqTNdHCyYqfvUR1pxndPXEceLtuWOf-9rYDfihwZt4VNomofVtQvRLkAXL-jrJ7HyXIQppxcnpspzx_iUpN740iCgWwcv6NaYNxqTFSYGzXbX39CIeALB7llc_SAxGoxhn9iB34wi-o-kkEMMx53gv4UfQkasu8EgVe96xR_42yRWPqV6vHjw3AaTbFHeGS8qD04glvbUZ33K5vLbnWGyQ6wshFX50mn3DdZiJypn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کامبیز مهدی‌زاده (داماد حسن روحانی ) به شعارهای تجمعات شبانه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691191" target="_blank">📅 15:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26362f645a.mp4?token=o5dh-mlLcHQI7EljOnFurt9vcMDtRIvAhtzT7Vt6lC7JTO9-eSO6uhqX8ZMwD91jnGUVmp74AOLOTWOMLstUfKx0MHcfSc2U26CyS4qNxPFWKvjz6jVJPVnaFEloc_pQzzGnU-DEG8SiURB3Vd570BgYKxdIasUa2pwnoRmIKXieE3Ms_Onbu7ghjiioh4_-7lfUdALHVOjzkxijy2G8cgeQkztyHM9WVhdhyTT4peEaHq30Jb32dfNHmtuYriplnQbWNsRsOpjzj5GgQUVnvpeqweu0Dx9Qu3nRL-SE4D7E6ObB_9k2eaUaLPpEcPmmg45akZOpaRA2NJ48DTavUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26362f645a.mp4?token=o5dh-mlLcHQI7EljOnFurt9vcMDtRIvAhtzT7Vt6lC7JTO9-eSO6uhqX8ZMwD91jnGUVmp74AOLOTWOMLstUfKx0MHcfSc2U26CyS4qNxPFWKvjz6jVJPVnaFEloc_pQzzGnU-DEG8SiURB3Vd570BgYKxdIasUa2pwnoRmIKXieE3Ms_Onbu7ghjiioh4_-7lfUdALHVOjzkxijy2G8cgeQkztyHM9WVhdhyTT4peEaHq30Jb32dfNHmtuYriplnQbWNsRsOpjzj5GgQUVnvpeqweu0Dx9Qu3nRL-SE4D7E6ObB_9k2eaUaLPpEcPmmg45akZOpaRA2NJ48DTavUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جالب از دیافراگم دوربین در چند گوشی پرچمدار پیش از عرضه‌ آیفون ۱۸ پرو اپل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691190" target="_blank">📅 15:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naLYxHDPH9Cs4SIOAarUxLS_lDCd3HoTw3rFK2rP4gs8bbHHmvd_iNJaN1dyyiBXJwcOe_Ich3maFDtki4QR5COYR_936909mdwgHaldU4z1gm8zZHy4PIKrb5BlbcfbO72SnieXMXm4YYYy8RxEGLyhYSjCjhy4KqeY-iSwqnBvJaF1BdHKpSQp1gCfgTuOoWHzDoGzwQRwyEFFGDKr-lfRDIMlZDOcRdEaKSAX-3LEWZ5fqiSStTFMoAow65Ioe3O3niDPR07Pr9fIVpy46yMdzsBHwECgNRcGkDst9Hi-vb9xq0EkRm0eazrpLXYTgTCzCbHC_d2oAxGIM3PisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از افزایش قیمت‌ها تا جهش ثروت میلیاردرها؛ اعداد جنجالی درباره اقتصاد آمریکا در دوره ترامپ
🔹
بنزین +۳۹٪
🔹
دیزل +۶۹٪
🔹
خدمات عمومی +۱۵٪
🔹
سوخت جت +۱۰۰٪
🔹
مراقبت‌های بهداشتی +۱۳٪
🔹
گوشت گاو چرخ‌کرده +۲۵٪
🔹
ثروت ایلان: +۱۲۲٪
🔹
سود وال استریت +۲۲٪
🔹
حقوق مدیران عامل: +۱۴٪
🔹
حقوق واقعی: +۰.۵٪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/691189" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52586b2c2f.mp4?token=c9P35NFXL_B6P1hO1F2uyngxt_mFa6lfPYojkQLzOh42XOzPFjfUDcP6j8HXbxeY7ovKXEry_XQ4Jtv9puPRAUIy5BEqYg6LFOQ_ccCMyvy22DOrol63gs_dCqRPz4P01XU94JNqqarGdBOwe5jfo22A7CHJ4h3lbpq-vpnx3zNv0vVzjL-FVdz6zi7P0AIDdAJn4LnvDXEhe1PXo3o0Wxb_nbmdvLuH4xv9xOj47ZJAXrzSiD6Xc-HqUZvpH5ePKOr06RUrnukK5VlGI-ghFAdgX2mvewnu8hxss4i5kLdJ-qHmt-_5wkfaCVab5-_HepsKFc4jGUvNiGPjmW5FI4xKE2QxoYrFgyMYdwZddWo81TECqj64KxK5MnU5-KqANu1FucbqWREVM05Vl5zDnQdmYmdeXnks-V7w_9WprMdi0ZH-HgbIoQ7bKLSP4ECDsIKBIB90kH19WxGQcPIdPGqW78C1DN9nBc_HPllcQMOm42h6DI3AbWbPwRiOptrm_LJVpFNcGeZJu8NAeSzYBL9TXOwexzC6k49czieuTspyNDHE1hxt4QqtwkuJOSYsEJcaSuxLNnW8nNsFJvXrjBDSdHV1GLJ3l5qij0ei3hMgz8J77Wiv7S8t_-0ALL3f3vSvWDrWZ41oq8QMRO-l67dSRpeFl38b7J5KQQCKNRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت ۲۳ میلیارد دلاری آلودگی هوا
محمد درویش، پژوهشگر و کنشگر حوزه محیط‌زیست:
🔹
سرانه فضای سبز هر ایرانی به ۰.۱۶ هکتار رسیده که کمتر از یک‌چهارم میانگین جهانی است؛ همچنین مدیریت پسماند و شیرابه‌ها کیفیت و کمیت منابع آب را به‌ شدت تنزل داده است.
🔹
وضعیت در تمام حوزه‌ها بحرانی است؛ به‌طوری که فرسایش خاک در ایران تا ۸ برابر میانگین جهانی رسیده و آلودگی هوا هزینه‌های سنگین درمانی بر کشور تحمیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/691188" target="_blank">📅 15:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxevddRvwomw1rtsZ4_bXA7FIRuXew-jMCbdAQtZmi96Al0ZuVihQndRu_BAAUF6tikkUB8snY8Z3CyTzgJmdOk9eRcZcLdwt_LkVRyFNEO675f-kV5Eb62Psr1VBR_ufZc-T-MBAz2ZHNmrBU3gqzFHvlb0v3XWDvx02a24sXkswAv5UrLHR3btZDbZnj0hbpq3XBpdtZrd9f1asOrw2mj5BAdCHrr2592pzCsGTlnoH-l0vH1IHQd1c877Ygigimk5P_CLsnJQH683rjJxWz1hxSJXZTSp9_1mRNSZW1xJ5rzupn5MV0jGTFf-djLyCdjuRBqe2_ICLUivNhpqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش المیرا شریفی‌مقدم به افتتاح بزرگ‌ترین پروژه کشور به همت شهرداری اصفهان
🔹
بزرگ‌ترین پروژه کشور که به همت شهرداری اصفهان در هفته دولت سال ١۴٠۵ افتتاح شد؛ به سال‌ها حوادث تلخ، ناامنی روانی و عذاب تردد مردم پایان داد.
🔹
زیرگذر شهید رئیسی دروازه ورودی شهر اصفهان از سمت شرق این شهر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691187" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قیمت برخی موبایل‌های اقتصادی با ورود محموله‌های جدید تا ۳۰ درصد کاهش داشته است
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/691186" target="_blank">📅 15:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af8fe0907.mp4?token=ja0scrUisnKmMM_VGXDTZewYknRA1GBlFtDOuajArVQh7Gc7ylmHFXGuxPJZ9XOz2M-Xm8kfk1l60kQ1nPNYrJpW-_baxEEkFp-AZVk6BzUigI5Ud9KiCn4N8A6YuNl82pFl34uVAZSsRM5BhWiS48DSd_M49pyemRANemKJBRCqDszCXiQnAu1PvVWzdFDEuOnoy6SWhyv336Ds41AqwCbqj1TNcFqFEhZ_gCxlsPEYNJaRyTt2C3w3KOZXy292QVmg9CZ0rFR4OJtyOEMxPZQkdPW1OqE2ZCtc8MiXSU7mc2sAMjEmOvhSJxMRSMhWcXxSbOf30qd3APg6hp0VxmWRsRS27qEK_nATbVu3iZDVgSQJeN4ZGlyNdOqbqwjS6kWCn8wW-UOvK52oh0LqiUyGSKgnZlBuS6VjGd_sOxDDMqUBVoJ8goV1eIHwmCilWZ9e6tuurbcsofnKGc2VAh4DPsN6mu7hp-bJ8_vbKjJbvK10THrQ_jQN_u0UW88DjrSQcQADOnklNdHUKPh8WXih66f7nQzLD35CEZhWRulD9YuVQ9N879dp8A_voFkWyXTudIdJA4iNOnc6GhIastu1FxdOANH4Y0hb5bTm0WINCbXI4OvkngCaZye0Rj7o4jemwYXoLw5-v_lkDI12R2qKLHzxMXu7G1f6W9KB8R0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگرد جدید کلاهبرداران برای خالی کردن حساب
🔹
پیامک‌های جعلی با وعده واریز معیشتی، کالابرگ، حقوق یا ابلاغیه، یکی از شگردهای کلاهبرداران برای کشاندن مردم به لینک‌های آلوده است.
🔹
اما حالا با ترفندهای جدید، روش‌های دیگری برای کلاهبرداری به کار گرفته می‌شود.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/691185" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383bde4a6.mp4?token=d7ihF5eViFkSx-2lBt7F34s2aYEJ11d1n2hhDvhLCBld0DISAcGfTEmcgfjdEYLQJFvTdFMWg_nO1CZ8c0YvuGhJKRX2q-Yp4acbgspE-rSZhS9t1fa2ty5Oq_jXRY0W9U2qz_6vJOJhDTrrRpX8s7FfDSAyyVtIUWE4BZ4XtoLVAfEv_mb1BsfH_NKdUyIhDsnp2ngodT_CEavexp1y1aMB-zgM-2cZw0zNUkymijjZTa-ApeKHroN3FmKKom-y_CpblK46V-e6h603D1faMxUDvewN36MKyjQknfLBPvZ2zyVkPsoRlBtcaezYPDNfo3K-sQxlTaucf7MV5e7TDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز پاک کردن لکه وایتکس یا دامستوس از روی لباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691184" target="_blank">📅 15:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
معاون پژوهشی وزیر علوم: سال تحصیلی جدید در مقطع کارشناسی ارشد و دکترا کاملا حضوری خواهد بود
🔹
آزمایشگاه‌های تحقیقاتی فعال خواهند بود.
🔹
در مقطع کارشناسی ظرفیتی وجود دارد که ۲۵ درصد آموزش میتواند غیرحضوری باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/691183" target="_blank">📅 15:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyEe6SuBm09t1UrvPTotaY4SgTDapyUXq49ZNkBUfdXIdGUFVFUqOzagiFLVCXGyod0UYLrrSaBbdlnGIsQhsfVuPTcBafm_ee3hBmhmiQDHBO8WhGqRKp4OCfA9TuHXFFqMLxO0dEUh_oO0lAKbf3eDQal-6IoXsNj6L5Lht7mN_uk6N-ddq2C7QuDoZe1S7TDCWsDFCJVka1HLaQofcQwkkSegxz4M5ab-Z-4TyQjddRUAeQ1-hYowlF1RbPJwEG9QaecGdiu-UFpDbfnRdyUYYXEd9xWfdlw8gF0o08T4T6FmKLI9f22J60apC_dSosGHOZFEJDRVPH6Jb8hVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیان‌‌های هزار میلیاردی در شرکت‌‌های دولتی!
/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691182" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38d91cf74.mp4?token=X8IFs9yBopIbUleCm4Cyd67xvJrOkIDCbLNoFVtuY7XPWGD3eemiMHrv9GPoHcAd7ZAIl-5n2NibqMJIF7xOHPNQhaX3KlIfnup846eiErujvWxf-6S4oTyIiTD3RS0QrtDHmGGqfTKtnkNvx7qFekFKIlTVxrDP_FTtoloss3sMmO_gn4HCtjqHPXpeJfpVoh0j01r8TWcTEW_qGs8hmxwfQCf_cbQl5qI0I7wSgvEGNya4HtocRysnz7hklS9JMsB-UjAxBz_A6K4YeclDkd7a2W89E1pUSofnQwFrdnp8VtstZ-7tMcRVIsZRb-_IS7ejY7o7VnIck8dQ7pSTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهندس
اتابک
وزیر
صمت
:
بانک
صنعت
و
معدن
در
ارائه
خدمات
به
واحد‌های
تولیدی
آسیب
دیده
در
شهرک‌های
صنعتی
خدمات
خوبی
ارایه
کرده
است
▫️
این بانک در زمینه راه‌اندازی پروژه‌ها و تأمین تسهیلات سرمایه در گردش مورد نیاز واحدها نیز عملکرد مفیدی داشته است.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/691181" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691179">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1HD6tK470Z9CELReeybUrN2-lY_Bp4d-uGZsZD4TB_Cjfu26QCYYtDuCKCFVUjt3ZQac4u9WRopdWKHe-N1DHmznoClYi6KUMIGL2Z4ZfOIwcVYsj3EDSqVTWbjUwlni683TZRfY1G1CHAnWzYdrH-Cwge4B7rbKriAUi2Id_2keq2pSvFD_Y1VVLO6Li9ZgThjTPKDYTTV2h9ig2c6lnO0wRjoSODXcsJ9mhEVP8F-eDioMYa8vBSIMGFqHRC4T5BmRq5XWwHxnYOxLXg2T15pYMmCunHw2ofqt9fGSPQad1-WoKv1DuLCS8UNAz9lUxCovRKVhKVCKwIfFlKPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXUs5VqRJgnIifvfQsab3FAQwca0MW3QgRG_KU4vSbzKRkS4V_Ft0dBxxMNTlbrnPcDEY9rQTSTq4kNEC6wEmi5YUEF0k18eR0G-GvOvF7v_qmUVhjhOkv6BFFzath4NFwGWDEMndLc7Z4-ju8EejJJmcHNgBhMQo__cfi_9zyKJ739z7zmgV9OtGArzXwrd0F13tN2q-_e1AadegUd-z7bJWYsda38XjFZa5s17JKVX0Cd3g1i7wJ3oPIFREUY1N0wj1i5a7S2m6wWLNcerVMmUUHyGnb8xqrixOfP3SstnwLbdEK2MTqqeAX4c2YdYSPuo7NNB5cRhszO_Al8LHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691179" target="_blank">📅 14:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691178">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af90ba159.mp4?token=rja-nkJIdgv1jpUc393sMVyEy9JbBPHhffGWYodyqEbzXmjhNmNnCZ8PtMcOxssc-UoKWaCHma9Nc3J8zIqgInIRtKJBtetkGD7GbQfOOsghiN85rmJx_SwUQZ9PIkFfDRELzfbMqp52J39aqkH7CVnymGf7WQqUCXGbawb-FmPbC72eg6sFn6FU5ZcQfCguaprjQ6_kAyPjOBZuszxKWJHb9CyNMdB4f8HC1E35M5KXiQAT7sOJNA6K3KHLlHvuKVIFoR5fi1ia33JTmbwPLoTrkVHk5HlP9BF3maNGjS21PFA4iDOn7ugWmZd6-2Nm404M8LnckkZ2oCuolBG6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجه سابق آمریکا، ادعای ترامپ در مورد «التماس ایران» را مسخره کرد: اگر منظور از التماس شلیک پرتابه‌های بیشتر است، پس روش جالبی برای التماس دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691178" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691177">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
فرودگاه ریاض هم‌اکنون/ ستون‌های دود از فاصله چند کیلومتری دیده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691177" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691176">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8d853409.mp4?token=bcIjlzrexFwf1wa-9AUyt1WJzUZeKdzrNIo9Oqgr36s9Zrk_MnKwEB1dnPLlxS9eXYK2nfONcg7yois9iGjgYBPY40sIydXGfratNufM94Mx83QzUoNffPoyM9bwIeJ6Wr-DlcNxg7n3CPgW9nT9uHKWq2O8hlr80jBesanQA87GCGJhcOLpiGgnm_8I7wPvH0_SBwqFfekHZH2AbgpIDCz9PKzTwSx1nffQYSk0G4wjONJw8dWGkHxoJf-gZp9YJiIecuh_3kcjoVt3w2JGP0my1qZbD3IF83-9L9ACidKt-y8CgkW2JNKp0e8xCaWuJW_YjPUwvakvHhzCf5LGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فؤاد ایزدی: انتظار بازگشت آمریکا به تفاهم‌نامه یک خسارت بزرگ است!
کارشناس مسائل آمریکا:
🔹
توافق یا تفاهم با دولت فعلی آمریکا امکان‌پذیر نیست. انتظار برای بازگشت آمریکا به تفاهم‌نامه‌های قبلی یک خسارت بزرگ است و تنها احتمال حملات گسترده‌تر را افزایش می‌دهد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/yRIXrUwC5Xc
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691176" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bd5beb93.mp4?token=NC5Z7b0rcRtDL6awOIf-X7naBty-UUwoqTUivJ5aOQKa93LD1WUhTnB722cW_UaAdSZWuHyhLNvEf0tlcVkCg-SPaq5lB819tYVKfp0j57kLFoGMLeLn4a0VfKCuVp_XPmlgFAvWgAlFMVQNrY6x-fMndoDlH4izCbyFiHsZugY7KaZ_40kxg3-fdrkzr0edBvYNbbedNY1Bjp7HstZWEDcn_ElESV598roN4YJs6ke4i5s2LOcamt5_1IYwVIyma7z6_Sun2lQpX8WjcvRwC8DArtqsi92Fufz16ngTCEO-VuTXqdUa8sizqbveJ243hvRNoWCO3CkIZMnO_6_qkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاطم شدید در پرواز
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که یک هواپیمای مسافربری را هنگام عبور از تلاطم شدید نشان می‌دهد. در تصاویر، هواپیما به‌شدت تکان می‌خورد و بال آن نیز از داخل پنجره در حال خم‌شدن و نوسان دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/691175" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
