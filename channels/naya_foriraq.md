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
<img src="https://cdn4.telesco.pe/file/GhITPEx3jOYXFDz8aeXaFlbZjXFAymrZpfMSIm0BnPG3WuJy__0_CK4dC8RSWXua1AhZOn6hpUIRp1_PDNJ3xLV4nayry0kfKIg56se8Txe1iB5JzwCZfoDNGz92ebJrcSfW3l96z_c3PJzWwoPR7DufsNikMP06a3krCzCg7VOFx6jzFk6a3vzsSUYlvQ_mE7WBcVZKIpRD1U2a-PyGzCSgWL28CthHqUulnW9FIXL--5khVlg0EW3ii1Ez4C6FCFZDHGxKYP5OcFqoArdyRP_X-BXWzAO3k2naCGL1rbLlGgoydv0ltEJZ7frJ1lZxU06oXQNpKyIFWQasCZ26Iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 21:55:33</div>
<hr>

<div class="tg-post" id="msg-88519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=I0QrhRl88ZSJu0NJ_1D-0rED6EIlFbLQG_yp3ukfi_rKjGL7b9NtbT_VFZ91wXT1hVTxBTiu9Ev5dTxn2pBU4TPY3AEUwrWW__gqI1gqiVmcYDwwo23I3vTt0c9nAKRBR7ynimcLtUU_zSiiGZOLzJFkQ5lsD-8H6ABP7WHcrIlEwSLXtf79AxT3shm1MlP5mLhoyyiaRMHVQ9fjZwBvjCVMmnYVLcTuSmlLkX5xQBsgNql_vHUhBSPo6r4mep3MFm0_32KwIWkhKOL0Id8PzF8prVkuTVbD7UYwZ0kQZCBtIaMvT6U6mu3qYzT2Mw7rJEjXVnWhlRmSr8KxahnZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99461fe9fa.mp4?token=I0QrhRl88ZSJu0NJ_1D-0rED6EIlFbLQG_yp3ukfi_rKjGL7b9NtbT_VFZ91wXT1hVTxBTiu9Ev5dTxn2pBU4TPY3AEUwrWW__gqI1gqiVmcYDwwo23I3vTt0c9nAKRBR7ynimcLtUU_zSiiGZOLzJFkQ5lsD-8H6ABP7WHcrIlEwSLXtf79AxT3shm1MlP5mLhoyyiaRMHVQ9fjZwBvjCVMmnYVLcTuSmlLkX5xQBsgNql_vHUhBSPo6r4mep3MFm0_32KwIWkhKOL0Id8PzF8prVkuTVbD7UYwZ0kQZCBtIaMvT6U6mu3qYzT2Mw7rJEjXVnWhlRmSr8KxahnZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مظلوم عبدي يعلن حل تنظيم قوات سوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/naya_foriraq/88519" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
ضبط 36 كغم من حبوب الكبتاجون وإلقاء القبض على المتاجرين بها، بعد تنفيذ كمين محكم أسفر عن الإطاحة به بالجرم المشهود.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/naya_foriraq/88518" target="_blank">📅 21:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=SVUrepZSUMxCDTvx5PFjiw6ehQnZeDUQ7ijFcLqd3_kUVsWstmq4kZlRCKgH092D7zxavxghf-adZ52zvD6QghsSCNego_DuzR3-ggoyzc7BrgI5vXc8xujCcu763maKDcTYihsCjmcPOI1jvNHayOJKQ2NJKBvWY_1nQsXaNX4rJ12JdVH3APq5BZTsJmMVLVWP4YFP3jBS0jU7PvjKJ9cRGd-0CUVF0cUo_qVyKrHByV7EYy0DwshBwfFO4UZKmTTkLOyJTJejU7psfSEj1fOwTLwb9Uw7l8oiD_fQdWuDB2iUUB5-a_VJSkJLBkYZZ-Le6MMEjdsd00gLkwaCHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c9cb6e3.mp4?token=SVUrepZSUMxCDTvx5PFjiw6ehQnZeDUQ7ijFcLqd3_kUVsWstmq4kZlRCKgH092D7zxavxghf-adZ52zvD6QghsSCNego_DuzR3-ggoyzc7BrgI5vXc8xujCcu763maKDcTYihsCjmcPOI1jvNHayOJKQ2NJKBvWY_1nQsXaNX4rJ12JdVH3APq5BZTsJmMVLVWP4YFP3jBS0jU7PvjKJ9cRGd-0CUVF0cUo_qVyKrHByV7EYy0DwshBwfFO4UZKmTTkLOyJTJejU7psfSEj1fOwTLwb9Uw7l8oiD_fQdWuDB2iUUB5-a_VJSkJLBkYZZ-Le6MMEjdsd00gLkwaCHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
رئيس تركيا أردوغان حول إسرائيل وسوريا: نحن لن نتوقف عن دعم جيراننا لمساعدتهم على النهوض، لمجرد أن الشبكات الإجرامية التي لديها دماء الأبرياء على أيديها مستاءة من ذلك.  السياسة الخارجية لهذا البلد يتم تحديدها حصريًا وبشكل كامل من قبل الشعب التركي.  لا يمكن…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/88517" target="_blank">📅 20:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=F4RRMDLSmCETyQGYZnl2fjt5P5hmA-LA1nvU9B52q-vBr_6r_RZSKCQYy1_IG-zJOrHJ2eKDeH5d0kPKZysjZH-BOmB9dWhl2zhH4mGl3fNDwPu6E54zJc17tjG9skbLDcZMiUw1M3jcDPsKByHfxG8XqzbwHctZLu9CaGf91xcpwJuuzrE2sQNFIohk4Ybm2qWVda0uiUtq3FCLurVr-FdPY7hfCWOGz4sLZYXWh2C3Dl-tkZpGp38eW44Xu0szKlhNkvfOc2sY0kzWyVLocLBRgF5CReV6D1vu4Y5sFXPrDW1F0LdebhpHIBPxO18JzE3fuAiMoyPhuj07L1xkxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c8b533d3.mp4?token=F4RRMDLSmCETyQGYZnl2fjt5P5hmA-LA1nvU9B52q-vBr_6r_RZSKCQYy1_IG-zJOrHJ2eKDeH5d0kPKZysjZH-BOmB9dWhl2zhH4mGl3fNDwPu6E54zJc17tjG9skbLDcZMiUw1M3jcDPsKByHfxG8XqzbwHctZLu9CaGf91xcpwJuuzrE2sQNFIohk4Ybm2qWVda0uiUtq3FCLurVr-FdPY7hfCWOGz4sLZYXWh2C3Dl-tkZpGp38eW44Xu0szKlhNkvfOc2sY0kzWyVLocLBRgF5CReV6D1vu4Y5sFXPrDW1F0LdebhpHIBPxO18JzE3fuAiMoyPhuj07L1xkxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/88516" target="_blank">📅 20:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owg_9G5esK2B1zjYqEr4R0Ybe4rij5ASbpuGiZ5q2a4FJLxcPU6AbAmMNONYQIxqlxNTKQu2sMG_56EqvkT7jq3d5OaGYuB4tBfnVccWL8Utf_zHeAjrC3Tqr6wLU3HM0qJoJGOIpj6uEFJwOIAME8NT_CD46CNyTc4J-wHggIV04BrcJMSdpK9kjmobqNO4hu2p-cxEx-1myCYZ5hvJAe4ITls-AxTu5uWGQigNWmJa3dWHMAtsnsjpw54DmhR60Wb_yFyzMTFPChopxrb0XTqZgz5Ddjsri0P_HspaQLc05Dy6Hr6J3KrLn5-u-Qp3GuEUG4Vu1bLyCDbn07k0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يعيد نشر تقرير
: أمريكا على وشك تحقيق ثروة طائلة في منطقة الشرق الأوسط والخليج.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/88515" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
وزير خارجية الكيان:
سنطرد ممثلي هولندا من مركز الدعم الدولي لغزة بسبب تحركات حكومتهم المعادية
لإسرائيل
.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88514" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQoMlXpGS6ojIguwek6kCMRqi_7DVriNWzlzSVjFR1CvONAYDVdzZ-TfztRQ2OcVPJcnchsG1kATArrgAxyD-BZpXQ2Gbwu7ZbxyutwPW5PozpTsdsE3G--ZsuwweyBBAwqgfs2J1XBA16anBPLY5aqT9kopDEMpJGIiv7pLElDq6RMqjjQQazuV-4qoXmWtGSjtGusq6v7fSlNgeiQAddQ4UkG9cTduQpoz0j1-L9p0-zdIL_DaU5zCMZTELlLmoqrI0y0nWiFG85WyK9YvBUV05s_cHzl8jtVEQ_A9gx3MxjLEGH3aK2mOymPa-9pNU8RgSh4i5u_JPuExhDMtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
بيان ايراني عماني مشترك
:
أجرى معالي السيد بدر بن حمد بن حمود البوسعيدي وزير خارجية سلطنة عمان مشاورات بناءة مع نظيره الإيراني الدكتور السيد عباس عراقجي خلال زيارة العمل التي يقوم بها إلى الجمهورية الإسلامية الإيرانية.
ركزت المشاورات على الأهمية التي يوليها البلدان لاستئناف الملاحة الآمنة عبر مضيق هرمز مع الحفاظ على سيادتهما وحقوقهما السيادية. وناقش الوزيران إطاراً مرحلياً من شأنه أن يوفر أساساً عملياً وقابلاً للتطبيق للمضي قدماً، في ضوء الوضع الراهن في المضيق، الناجم عن الحرب الأخيرة وتداعياتها الكارثية.
يتضمن الإطار المقترح إنشاء ممر ملاحي مشترك مؤقت عبر مضيق هرمز، واتفاقية لتنفيذ مشروع مشترك لتطهير المضيق من الألغام. وستستمر المفاوضات الفنية بين الجانبين بهدف الاتفاق على ممر ملاحي دائم، وإدارة المضيق مستقبلاً، بالإضافة إلى آلية لتبادل معلومات إدارة حركة الملاحة، وتوفير الخدمات البحرية والأمنية اللازمة.
وفي هذا الصدد، أكد الجانبان على أهمية إجراء محادثات مشتركة مع دول المنطقة المطلة على مياه خليج فارس. كما أكدا على ضرورة الالتزام بالقانون الدولي المعمول به واحترام الحقوق السيادية للدول الساحلية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/88513" target="_blank">📅 19:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUu8EfUpbbQjCYRncQPI_Y8rwwb-kgkKjBXpoFWgvwGTIo_LB0BlmVs6mirTqf8purfh3PhnfWq1aqo_HOq39IsdgXpwLy_ePclYgRUiXGBbTHSB7Lyfib2sNdDLebvrT9niCU_FChYSVFAxUyoFpQkW5s2XKuT_Fnen8ZBI4H5cudlgUPBdrh5K49ekXUcVfe8rF4utkDbh1laCgvUMfVqrTLeWCYm21EGS8KJGHrdU4GuWMiNtgQuDlXPkrQFTjW_FrPOrdlZHfrDZmt4w677oQ5qH_PDf87OkxtjFvYxxG1i7CG8LRa_dBAaFk2WCjDfrKNY6kGnCNkAsLFuxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
المتحدث باسم الخارجية الايرانية
:
‏
الولايات المتحدة: "يوم النصر الاقتصادي".
‏أولئك الذين يفضلون الظهور بمظهر "الخاضعين كالظلال" يقولون: "هذا جيد".
‏لكن انتظر on. هذا ليس جيداً على الإطلاق.
‏عندما يعلن أحد المتنمرين أن على كل بنك وشركة وميناء وحكومة أن تختار بين إطاعة أهواء واشنطن أو مواجهة الانتقام الأمريكي، فإن الأمر لم يعد يتعلق بإيران فقط.
‏يتعلق الأمر بتدمير أهم القواعد الأساسية للقانون الدولي وميثاق الأمم المتحدة - أي احترام المساواة السيادية وحق تقرير المصير لجميع الدول.
‏لن تقبل أي دولة محترمة تقدر سيادتها ومصالحها الوطنية بتطبيع مثل هذا الفوضى العارمة والتنمر الممنهج.
‏تُعد كندا من بين الدول التي بدأت بالفعل في استيعاب هذا الدرس...</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/88512" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=mq9hXplmQFOx1TbN_Y4lEuk-CFP4ahqMqZtUOOD3EE7DIBVtts3p-HopYLb479TTxbDO0PfuTnUmUZqULNra9-QgY-1gHx34XAtlXHlLJGa9tp5e82S1iGsQ56PSVyNWL5BmFC-bFqFYYkVHK_L7aOfOYmaQjBj3g2MDDOriD_FCdrqPc2l8fLgRctW4CLrZib8qkGHBTt0XBhZ9SADLx5I8Y1YGWIPXQvRjE7Ha51kdYU4nn7yGeKlbtAsa15sgYMJEavveC-iJIZDJDFoXuRXv8f5BTL8OXi0PzQtn41vRPIYpdXBD7AU2jWJ5eBAlXKfesEAKZY6yeedVhWA-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3771f51e.mp4?token=mq9hXplmQFOx1TbN_Y4lEuk-CFP4ahqMqZtUOOD3EE7DIBVtts3p-HopYLb479TTxbDO0PfuTnUmUZqULNra9-QgY-1gHx34XAtlXHlLJGa9tp5e82S1iGsQ56PSVyNWL5BmFC-bFqFYYkVHK_L7aOfOYmaQjBj3g2MDDOriD_FCdrqPc2l8fLgRctW4CLrZib8qkGHBTt0XBhZ9SADLx5I8Y1YGWIPXQvRjE7Ha51kdYU4nn7yGeKlbtAsa15sgYMJEavveC-iJIZDJDFoXuRXv8f5BTL8OXi0PzQtn41vRPIYpdXBD7AU2jWJ5eBAlXKfesEAKZY6yeedVhWA-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد كبيرة من ميليشيات البرزاني تدخل قضاء خبات ضمن محافظة اربيل لاقتحام منازل الهركية</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/88511" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلزال بقوة 4.9 ريختر يضرب افغانستان</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/88510" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا:  لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/88509" target="_blank">📅 18:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇨🇦
🇺🇸
‏
كندا تصعد الحرب التجارية مع امريكا
- كندا تفرض رسوماً جمركية تتراوح بين
15% و50%
على منتجات أميركية بقيمة تقارب
20 مليار دولار
.
- كندا تضاعف الرسوم على
منتجات الصلب الأميركية
من
25% إلى 50%
- الحكومة الكندية تعلن عن حزمة دعم بقيمة
7.5 مليار دولار كندي
لمساعدة الشركات والعمال المتضررين من الرسوم الأميركية الجديدة</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/88508" target="_blank">📅 18:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=mRwsF34AdaADUcQnU_de6Z2us9ZxOHBRhVuzca361nW_IAaLC-SlHeLDBM9qu00p9RBFr8LFg-Nk8RGOVOTphgFkRECgYYYdGj7v_sSm68yy_o2dsEsQvAJhJ2LxE_-eyPujCWKriDieuMm31dvePLeYoTsJO-ud52QJyToeBvQSsGPolz-7Wt4PxlCBS5gnu7nwnRM8hUDkNZTA7C3iz5dFx1vwheXU26MPFEYme7fuFa5HZ7RnooZ7WPQb0QIByPfUkeWBVeCOqdBG8DyXYtgoqsdV7YHZMxmkR7vLj34PeGqHJ2Sy0PSn7H7-uqxpQn71wf9cdQqP5wiWj_7e9i3NP3rbVY3JGRHBJlrhBGLd-IaPCinoMM9SOrkKLZaB4CCEJEdYcQaiK7Fl7XcMhPJrC-C69RxFFNAG7xkcR5AnQ-Q_SXLcTWa3H23WeZ-7HH0I-fsoxkO_ajLBm7MjfAeF6kDHmrMenA2sOWW5JV_Y3K6OtXa8jjnwCEG9-GGPk6aKs3VLswwQYBYOi__qfdokNbGk5oEjVdIrUtAcFkCuIaxztlbSRSQy_ELQEsy4tTVcjJnie-WWkCi42XNYTY-jqDgUyObEKBJbrQ-BR2ZgUwolSyypxFliURnmymb8p5PHwmMQg26zlJ5mmmGoE_eulp5jByKgocqSPW2-_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c487d787a0.mp4?token=mRwsF34AdaADUcQnU_de6Z2us9ZxOHBRhVuzca361nW_IAaLC-SlHeLDBM9qu00p9RBFr8LFg-Nk8RGOVOTphgFkRECgYYYdGj7v_sSm68yy_o2dsEsQvAJhJ2LxE_-eyPujCWKriDieuMm31dvePLeYoTsJO-ud52QJyToeBvQSsGPolz-7Wt4PxlCBS5gnu7nwnRM8hUDkNZTA7C3iz5dFx1vwheXU26MPFEYme7fuFa5HZ7RnooZ7WPQb0QIByPfUkeWBVeCOqdBG8DyXYtgoqsdV7YHZMxmkR7vLj34PeGqHJ2Sy0PSn7H7-uqxpQn71wf9cdQqP5wiWj_7e9i3NP3rbVY3JGRHBJlrhBGLd-IaPCinoMM9SOrkKLZaB4CCEJEdYcQaiK7Fl7XcMhPJrC-C69RxFFNAG7xkcR5AnQ-Q_SXLcTWa3H23WeZ-7HH0I-fsoxkO_ajLBm7MjfAeF6kDHmrMenA2sOWW5JV_Y3K6OtXa8jjnwCEG9-GGPk6aKs3VLswwQYBYOi__qfdokNbGk5oEjVdIrUtAcFkCuIaxztlbSRSQy_ELQEsy4tTVcjJnie-WWkCi42XNYTY-jqDgUyObEKBJbrQ-BR2ZgUwolSyypxFliURnmymb8p5PHwmMQg26zlJ5mmmGoE_eulp5jByKgocqSPW2-_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تواصل اقتحام منازل الهركية في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/88507" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه باعتماد البطاقة الوطنية الموحدة في الانتخابات المقبلة</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/88506" target="_blank">📅 18:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW0V-K8YN3Qo60i9wPVmUwXfhaqui2DbGDWAPA3tUwxjsSi5byoDf1QIyJYEkduNEXHfBl8gywjqVlOXXpdEL__Wh0Gx1u1JSgAA2HDlYyNDFF_G0lvV-cd8bsS4pmNbU5qHS11SIjjuBkeppRYlJkvg68UDBXyVfxlvZkXDWw2Nec730h80M0fsmEqwjID6vkG0zd8YaPQTQAyizTsJSqHdMCzZcj_ZMFkLcaBb9HgrDA8Sg-7X4xAVzMDNHH6exYtqO2CQn3QS9I4F0T0Nw1ICHEnA2-U0B0TuS1UCgVZ2w8n11Q7qEJ4hZRSpoGMvVewJhjx3V4nKCRGH15PAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
ترامب يزعم:
لقد أُبلغتُ للتو من قِبل البحرية الأمريكية بإزالة جميع الألغام و/أو تفجيرها في المياه الدولية لمضيق هرمز. وقد تم إخطار إيران بأن أي سفينة أو قارب يزرع ألغامًا جديدة سيتم تدميره فورًا وبشكل منهجي. ومن خلال قوة الفضاء، نراقب كل شبر من المضيق، كما نفعل أيضًا مع موقع بيك آكس ماونتن والمواقع النووية الثلاثة الأخرى التي تم تدميرها بالفعل. هناك سياسة عدم تسامح مطلق مع زرع الألغام سارية المفعول بالكامل.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88505" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي يطيح بمنتحل صفة تمكن من الوصول الى مسؤولين وشخصيات رفيعة من بينهم رئيس الوزراء العراقي والتواصل معهم وتحقيق مكاسب شخصية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/88504" target="_blank">📅 17:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtCIn55hBxVOyV0wnAQEzmHUC6pJ1c5UXHs0OmagIwFLFkpNNYyNurBmCQt5r5BkvYq7-K405tehtzkSyMDNpt8BxpmWjPf53vmqqWA6LQ8jx4C0N9SXYJABdPhk7n1rz1aGKfDK_eefSSRBmGo5tUqSZMt0KLkrH1VKwogUTIW4DGK2CyZsOIvzFWThvG525MKgIRKC9xw1kBtm380tq2hT8zLqiR8qi4_C9CqJ8DhVbVZ5EUnOlv_KcVLSIsw56AhyZWrb0ixGDZYBXWDiK1l0hxIEHGPFlI1vva1tCHjFI10BnPjrA2fPICsXhDq2Pg1RAFFIGTodcJKYQyOEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامب:
على مدى السنوات العشر الماضية، خسرت الولايات المتحدة، في المتوسط، 60 مليار دولار سنوياً مع كندا. كفى!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/88503" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb337cec2.mp4?token=dhNCMLCQONyTlhkPRY-Gog_Y1AwhmuizoxFHj-7qENkBgTuCE1oK_zP3Wfm3g3MxT-AWNFLb8dPWWTvn6KgKqnheKPz-KdpeIkcqZyov42ubGso-XEnE4Cvhm_Jy11X_DDyB_07fTGjxNB0gM10H4u7KXODeNb1gcoTgC6paInGHseH7dJZc7Xp5tnyhfwyEmlDB8dYK8laUqSrZqupyP_6e16o8smYPIb0Ho02ejhDzr10Nvd-DUNV3L1o_GouPveleb_tf3QRblTax0jtU2QOYDgR4gP9Ad9HASp3DYO5SPG7f1fAy554uCPTyxmfvJMhI9bWGjZQj_UxdSm5s_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb337cec2.mp4?token=dhNCMLCQONyTlhkPRY-Gog_Y1AwhmuizoxFHj-7qENkBgTuCE1oK_zP3Wfm3g3MxT-AWNFLb8dPWWTvn6KgKqnheKPz-KdpeIkcqZyov42ubGso-XEnE4Cvhm_Jy11X_DDyB_07fTGjxNB0gM10H4u7KXODeNb1gcoTgC6paInGHseH7dJZc7Xp5tnyhfwyEmlDB8dYK8laUqSrZqupyP_6e16o8smYPIb0Ho02ejhDzr10Nvd-DUNV3L1o_GouPveleb_tf3QRblTax0jtU2QOYDgR4gP9Ad9HASp3DYO5SPG7f1fAy554uCPTyxmfvJMhI9bWGjZQj_UxdSm5s_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تدفع باعداد كبيرة الى مناطق انتشار الهركية في محافظة لاربيل لتفتيش منازلهم بشكل اجباري وبدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/88502" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB0rT98IauvyxfHDu9zn9PZebVgDfHOnAWE6citk48Pehk5ltbZpwpJe564ROj2yQ30BAkWRAVd-S7vpSNTv2KzDr2CcnAFNgBK95ZZ-oSsiX7oiebT0EUegcxunNANBwd0Y5Z7JZMLcMAwmsyFReoNyaKbw2SZihOIL5Xw-m5_nt7PHsPfwuRlrWWn39ERNmvMVdrCNHB6a6s5MeI3p9-RsjOtNSOX7dhjSSltk5U_Md0R3H9Zl5Y9jT0rIeY0N66ppUE49CIhGWoYHupcyy3KrZhsUAlPYLoC9LDEY-SoeW6xGlIEr2ItpX_8i3Bi_IPQe98NEwS_w0NBJL3tA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88501" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSXTgXEIZgo-VkIPv9GEVRZpTtRCeSvG__Fy3ERgnPWLwhk88BeJSFNyalSaUlzqP6icSv6I80uu1yXP9UlS1hMmyE7rTOSBsD9ZJXy0khAbIi0Tgoyx5cLiqCd3Lrs5GXa9uXDfETFu-_44mS1CQXB5HzL9IT9fUQ2akA00HYbkIcloHlNRapweQ4Zh2gvCd3PljJMvE4B7L8FxpMPSoV_1alYklb54-jAljwHfEbyHHdp4g7IoQV0vI30sYjRmMGCakyzFB6oLTXg8g9zA1QIPb94TeOqYz-DFq8i8hS8rD_epogiXdGOMy_eaKt7UoFsgkA-tjRva744XweWBHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب للمرة الألف
لن أقوم بالمشاركة مع كوريا الجنوبية في اي تمارين عسكرية مجددا واستفز كوريا الشمالية ؛ كوريا الجنوبية رفضت المشاركة بالهجوم على ايران .</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/88500" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي:
- في الوقت الذي يَحرِم المعتدي السعودي شعبنا العزيز من ثروته الوطنية ويُغلق عليه المطارات، يفتح أجواء بلاد الحرمين وأجواء مكة والمدينة لليهود الصهاينة
- النظام السعودي المعتدي العميل للصهيونية يتحمل كامل المسؤولية لكل ما يترتب على استهدافه لشعبنا
- أدعو شعبنا العزيز إلى الاستعانة بالله والتوكل عليه وتكثيف جهوده حتى يستعيد حقوقه المشروعة ويدفع عن نفسه الظلم الذي تمارسه مملكة قرن الشيطان بدون حق ولا مبرر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/88499" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
🇸🇾
وزير الحرب الصهيوني في سوريا
:
لن نتحرك من جبل الشيخ ومن المنطقة الأمنية ما دامت هناك تهديدات جهادية على إسرائيل. الرسالة إلى الرئيس السوري واضحة - عندما تستيقظ صباحا في القصر بدمشق، وتنظر إلى الأعلى نحو جبل الشيخ وترى الجيش الإسرائيلي - فأنت تعرف أننا هنا لحماية بلداتنا وحدودنا. تحركنا ضد محاولة تركية للتمركز في سوريا، بما يعرض المصالح الأمنية لإسرائيل للخطر، وأوضحنا الأمور بصورة واضحة وسنتمسك بها في المستقبل أيضا.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/88498" target="_blank">📅 16:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f511c9c4.mp4?token=gDt0bjtCCrGq7dmduy9GKTjOy7bVFJuuev0gmqIemiyAgedh8T73a4t7fJAD4VM3d3AcoCIo45RGldfpM_DpyRH8UWZ_hjtuIilvGK1Fnr5AQl2eFsjLwBpkIVfr0MTAkl2O6YOL9Py537lT-nvVkoUlecr8fQAzY2dNN3qINPjrZV_m711U9_SYbBjiswzjbZom8fQ4asgrm4Ays9_oc-8Ww7ubtZBibY_Vux_JYb-g1s4zkiJc783uXQaJUdFApJpWJtLavbLdGbeSQsuf4o_4iTrl2QlQibsRSc75SU0Lg84KceYM1r1EOkNnH-nNcaqOM2L3cpIPGnjGoGhtmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f511c9c4.mp4?token=gDt0bjtCCrGq7dmduy9GKTjOy7bVFJuuev0gmqIemiyAgedh8T73a4t7fJAD4VM3d3AcoCIo45RGldfpM_DpyRH8UWZ_hjtuIilvGK1Fnr5AQl2eFsjLwBpkIVfr0MTAkl2O6YOL9Py537lT-nvVkoUlecr8fQAzY2dNN3qINPjrZV_m711U9_SYbBjiswzjbZom8fQ4asgrm4Ays9_oc-8Ww7ubtZBibY_Vux_JYb-g1s4zkiJc783uXQaJUdFApJpWJtLavbLdGbeSQsuf4o_4iTrl2QlQibsRSc75SU0Lg84KceYM1r1EOkNnH-nNcaqOM2L3cpIPGnjGoGhtmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تقتحم منازل الهركيين في محافظة اربيل بدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88497" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a53977ec45.mp4?token=b-Wnkcd8Dx7CaxCgLLWy-q9arg4gc7LacxNVLrk6bGU1sekUdMfSXPkTx5k2tOH1rhnW24othumGLJXW3W4pkoAQg4Fak3KgfNgRpvBln-vudcl7ZRIuQ8V-UILUSVblcUtollqHpTN6SWthxicL1VRFA-TKBMsb0Pb_ubyHb4_rL_M6ZLKOrT8AD_jxehSzwiimFCZDkJ0gJ86sQfUX23vgXchKkV7TLOVScjTouBRmPdN2h2i_rCYKnHadylT5ss-pa9ekD-aUxQV7wRTkCh7NO6QCYuVckQaFWIx4axLRoHhklBmzOF5AeYsDvdMEMSvSorEjxcaLqR0idHwPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a53977ec45.mp4?token=b-Wnkcd8Dx7CaxCgLLWy-q9arg4gc7LacxNVLrk6bGU1sekUdMfSXPkTx5k2tOH1rhnW24othumGLJXW3W4pkoAQg4Fak3KgfNgRpvBln-vudcl7ZRIuQ8V-UILUSVblcUtollqHpTN6SWthxicL1VRFA-TKBMsb0Pb_ubyHb4_rL_M6ZLKOrT8AD_jxehSzwiimFCZDkJ0gJ86sQfUX23vgXchKkV7TLOVScjTouBRmPdN2h2i_rCYKnHadylT5ss-pa9ekD-aUxQV7wRTkCh7NO6QCYuVckQaFWIx4axLRoHhklBmzOF5AeYsDvdMEMSvSorEjxcaLqR0idHwPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ميليشيات البرزاني تقتحم منازل الهركيين في محافظة اربيل بدون مذكرات قانونية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/88496" target="_blank">📅 16:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
شركة JGC اليابانية المنفذة لمشروع (FCC) في محافظة البصرة العراقية تبلغ العاملين وإدارة المشروع بأنها تستعد للعودة الى الموقع واستئناف أعمال المشروع تدريجيا اعتبارا من مطلع شهر أيلول المقبل.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88495" target="_blank">📅 15:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
🇾🇪
‏اندلاع اشتباكات ومواجهات عنيفة بين انصار الله ومرتزقة السعودية في جبهة كلابة شمال شرقي تعز.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88494" target="_blank">📅 15:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngIofFzEjUKceUqCc5jYvHTF7zfH4lkrn3cl1jGmEhfXcNypVHt5vnmZzxLgO03iaFNYes95bsLZ4pteawotyH9sPnBNbYeAcjbZJvW848UcoCM0bKw9XEjlPxwF2sQ8d_LIOljL3YYSh9udKeY_QgasDS53on4oTBgTiUDc99KBH0P-HSE0xNHzM2IBJCUrVM3zLj06h6KHM45jpH5Z_m9R8kO-xd7nkUJJwjlzT2jysyiY3dWVhNA0ucYiGBFKATGmAa7nsxgCF2a9VryW5kt4MlAeXZ549756RnOHZ6_uh6fhJE5k47oPy333n_eanb1txmNmZeaFBSh7y8nAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
ترامب مجددا:
الجمهورية الإسلامية الإيرانية الفاشلة لا تدفع رواتب قطاعات واسعة من جيشها، وفي الوقت نفسه تقتل المتظاهرين، حتى في غير أوقات الاحتجاج، بمستويات غير مسبوقة. إنها أزمة إنسانية ذات أبعاد كارثية، ويجب إيقافها فوراً.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88493" target="_blank">📅 14:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d51a41e3b.mp4?token=qJyCEiWg8PfA1_liWFMmdqYjgu09W2VphNNvHqMgcNpD756WCFXeBgvg-QYWKJu2mpI18yB13tlWqG3SCMXBWhzcRrsWZZHwAZVh76uJej_-i65ID64cZVFjrEL6E5SOBEwU5oV1kx8kxuD-bJskLX35_hE_nlO9GY43nql5Tr8zCFflfpWB8m6GmrdRwCdKqP2JtAV_-4VIY6gFBy9Ur6BnVP1Nv01QUxJNBvGgLdny3MUdeuyxX1tCLP9aJZHjt17w5Lbz34cheuojt9WqET2ZECvCRZhayVKow4oGImheP48OmzmIK4-dbkybqYIPlOENW4h80UtqRb8nETAy8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d51a41e3b.mp4?token=qJyCEiWg8PfA1_liWFMmdqYjgu09W2VphNNvHqMgcNpD756WCFXeBgvg-QYWKJu2mpI18yB13tlWqG3SCMXBWhzcRrsWZZHwAZVh76uJej_-i65ID64cZVFjrEL6E5SOBEwU5oV1kx8kxuD-bJskLX35_hE_nlO9GY43nql5Tr8zCFflfpWB8m6GmrdRwCdKqP2JtAV_-4VIY6gFBy9Ur6BnVP1Nv01QUxJNBvGgLdny3MUdeuyxX1tCLP9aJZHjt17w5Lbz34cheuojt9WqET2ZECvCRZhayVKow4oGImheP48OmzmIK4-dbkybqYIPlOENW4h80UtqRb8nETAy8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعدسة نايا |
حشود غفيرة تحتفل في العاصمة اليمنية صنعاء بمناسبة المولد النبوي الشريف</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88492" target="_blank">📅 14:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDAtuhwDIrjb0EHrzhBMBSaB_wKz2ZfZsif437qxCEqe3eXcTdMlZfacOSHxVDBbx-_Ctne5HYLwJkS1LzIEVI7HyhPuzYNJo1cj8gv2WAMgjCv23t_uPRyCrd-TQxIIm-DNPUyyYIC_ZuA0BC6cMmHQu_1BpBzp5JJ8TdbOGs5SqrNFlIz4bKEL3hLlKVBjoQ0OTAioqnuiiiToCRgbgoyVxVrcwFifEajR9CCuOOGckd2wp7_x9WcFGTdDPGKszWUfGjzQKkBPewQBXBR2QvLHUirC7_x3jg1f9W3LFpbU8827GKntDWAGwdl8ked36vgmaHXD215vxe4derqexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
تدرس الولايات المتحدة بجدية تغيير اسم بحيرة أونتاريو إلى بحيرة أمريكا، إذ لا نتوقع استمرار تعاملاتنا التجارية مع أونتاريو.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88491" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BktD-4bRTvSPTBXvjkYxIY4eae5oP6fD1Pzw4uB8gwHGZNeOwu792wCVpxznV0x1SF0kDq9aXr48SBlXKwhLNrsUGisTReSidFVZ8L2_TzjuX6UkBBVSLTeDxF7Z94jx1o62hULA9Ljk5E3MBnbwu1xqjdDSKi-H5p5VqrxanjaExGqRM9INCp-_dSexkAS_LHe_9CJMhDr8VtHn-azeu8JaI17Sykl224gCgKoA9DLZk0F4y2MnXvbh3h_x_YVe1h-rHanS9ELCpHC48R5Y_JNOHRLxbY1T-pyeYLJ1xTrmCYqMANeJFwHyf-cpj4yXMFPNdGi_Hs9_naYLxhmW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGP-zz65dWUi80a0VCLf6WfjqptB3x6uypljaRSk61DjwZAnDt0xIoi8J9txWUXz2BBPV0XqOv9b_OkGiNIK7PLlHHW7krGDCms_5PZssie00jIDWc5w2IJR8nS_GHzglqjGDXglL3rW-NgKJ7RTh5cvOz_3q5CMW5N3sfT93y68qPq-ND4so7_6zbrZl51anpAGVsIb5QKUVMagFbFRggIA2PVKNqw4kT5nxAxB5d6-BOqEYNNAjX7h2koMY-leOxqUKWlRXuyUED7JQtfsnEqeTuI4Q7pGJmx_2MaIAF3EzCkc62cDvhMWtH92hs01wnW1M8BVsMb1aUH4-vXGFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضبط (1004) هاتف من نوع آيفون 17 برو ماكس مخبأة داخل إحدى الشاحنات في سيطرة الشعب ضمن العاصمة بغداد في محاولة لإدخالها خلافًا للضوابط.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88489" target="_blank">📅 14:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEBz2l7b7XT-cgkdeLMG390Q7VMUVrT-AlfLEAZbYe96zqo0Nol-zc_9IR71Zseyi43aeetSPhJ4UtWPvO6E_8gqrcM_Jd85op6neqdK3P2apcsbAGcMk-6qtjhfAdUYnTwAEAFQSpb2G3kPP5UXR441yfXF8wmzoGOGDXhEfVqdidbz_84bBAyKN0Ihga1ngiqKn1SaZygDvYiccbRgP1GCRQCiePq8EycmAd0ev4OgcqZnvrX945fVufgwhteXdCJW-agjbX381rpn6991gAGEdbutgAd28PDl2Iz1KSF9wm1QRRNlrkRANbFDC29YQ5xhRQfeRyNID2gEwOqWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تحالف العزم:
مثنى السامرائي ليس أول زعيم يُعتقل قبله نيلسون مانديلا اعتُقل 20 عاماً.
غدروك يا شبل الاسد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/88488" target="_blank">📅 14:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇨🇳
🇺🇸
فايننشال تايمز:
‏حذرت الصين من أنها سترد على أي توسع كبير للعقوبات الثانوية الأمريكية التي تستهدف الشركات الصينية، وذلك بعد أن أعلنت واشنطن عن إجراءات جديدة ضد الشركات التي تتخذ من هونغ كونغ مقراً لها .</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88487" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
‏
نيويورك تايمز:
واشنطن تعيد دبلوماسييها إلى سفاراتها بالشرق الأوسط.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88486" target="_blank">📅 13:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
🇸🇾
إعلام العدو:
وزير الحرب كاتس زار سوريا هذا الصباح.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88485" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
🇵🇰
وصل قائد الجيش الباكستاني "عاصم منير" إلى العاصمة الإيرانية طهران، للقاء المسؤولين الإيرانيين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88484" target="_blank">📅 11:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee375b397.mp4?token=GOHRD5khrvmH5Y65-0cJlfVbPicfWKscpcLaoMNyZLD6qVNWdgka2RZ-0bNd_zTIvM50cgCZeK4eP4zrJ6seunRrPDtUk8zzJ3IovBLuKsbWRkCo86i_QsJoQm3NQF34PMYp9dUCV8bDJb0-ZBm7aYW1EjvotVqJODV2t2DAZ1kW-1qpLBihbJEM2rpecyLs8Hhl2Lrq9wwSt4XqR3OjyYy1ieN_BDx8GMYqfLSGw56mRnyCCVK3MieR3dQtcpLXkd12kd9GhzhRebWVGwUVMm2oFm-FZYnXXNvSg-CmJRoigQs_OBhC79LjG4xjqJJOk1r-GuhPeA3-cuHBE2mLwKQ5tlsHGT5Qhw9ZGbOH4_YpTscgbI3jnPsYhjkz0TScTfMLR9OCEqDzry--TT8RFaqk08YAL_6vyIaR1nmSNJPwghB9flvcLaRJPQ6jZMNfa6vjNsJyLpqbq7ELUgkOMKtDvQWyuTgFpiecCpJsRiogux8--w8O1pkHDMI-sZfoLx2QWFJojIoDpi7f7oRePB5e09b3ijPtslxsjYhun1PmpvQ5-xeYbo6uogfS5aFhU_tzvlSs3YCJShVb72It8th-7xqK1dnSJLqCRgN1fBMTAPcAnrwU4sII47df3thVuYDq7codYDoHbK4dF8SU0nE5oVZrLYY_8uDPfyp0fmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee375b397.mp4?token=GOHRD5khrvmH5Y65-0cJlfVbPicfWKscpcLaoMNyZLD6qVNWdgka2RZ-0bNd_zTIvM50cgCZeK4eP4zrJ6seunRrPDtUk8zzJ3IovBLuKsbWRkCo86i_QsJoQm3NQF34PMYp9dUCV8bDJb0-ZBm7aYW1EjvotVqJODV2t2DAZ1kW-1qpLBihbJEM2rpecyLs8Hhl2Lrq9wwSt4XqR3OjyYy1ieN_BDx8GMYqfLSGw56mRnyCCVK3MieR3dQtcpLXkd12kd9GhzhRebWVGwUVMm2oFm-FZYnXXNvSg-CmJRoigQs_OBhC79LjG4xjqJJOk1r-GuhPeA3-cuHBE2mLwKQ5tlsHGT5Qhw9ZGbOH4_YpTscgbI3jnPsYhjkz0TScTfMLR9OCEqDzry--TT8RFaqk08YAL_6vyIaR1nmSNJPwghB9flvcLaRJPQ6jZMNfa6vjNsJyLpqbq7ELUgkOMKtDvQWyuTgFpiecCpJsRiogux8--w8O1pkHDMI-sZfoLx2QWFJojIoDpi7f7oRePB5e09b3ijPtslxsjYhun1PmpvQ5-xeYbo6uogfS5aFhU_tzvlSs3YCJShVb72It8th-7xqK1dnSJLqCRgN1fBMTAPcAnrwU4sII47df3thVuYDq7codYDoHbK4dF8SU0nE5oVZrLYY_8uDPfyp0fmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هيلاري كلينتون:
لقد أهدرنا الكثير من ذخائرنا في إيران، وبالطبع، أرسلنا الكثير إلى حلفائنا في الخليج. وقد استخدموها للدفاع عن أنفسهم.
لذلك، نحن في وضع صعب لأننا لسنا قادرين بشكل كافٍ على مواجهة المخاطر غير المتوقعة.
إذا قررت الصين التحرك ضد تايوان، حتى لو كنا نرغب في ذلك - ولم يكن من الواضح ما الذي سيفعله ترامب - فسوف نكون في وضع صعب لمحاولة مساعدة تايوان في الدفاع عن نفسها.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88483" target="_blank">📅 11:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
🇷🇺
🏴‍☠️
تضررت مصفاة نوفوشاختينسك النفطية نتيجة لهجوم شنته القوات الأوكرانية المدعومة من حلف الناتو على منطقة روستوف، وقد أوقف المصنع عملياته .</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88482" target="_blank">📅 10:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwXGrLngC31IIOln2sJsmfIpPoZkazpLeLkB8Tv3K7v9iaiuRbhcddgjahYEzIxunDwzJy0O-PwxIsOVIJFOI0S2LZzLJfcPvpOWnLNthugJ3WgPu6I-JwMfqGS9VVsYTe2DgA8wtivGyH7CjjgLnFVXuDTj49lYg_aTNwm2TM1MU-RcLpnrQ5memmtsLeFkTWNosxZcu9AYymQlddCn9qs3wuHLt4ZaOlwfqzFVlQ57U_3mE9iiLUPsVKHqyV11bYclMqwPG2R-6EX3k4wonCsc24benj7sdnUW20isDrcEVlhPHwbjfMd9SKRcb69u8Y_c2JjtZ2hZNGqKeEXhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
نييورك تايمز :
تستعين الحكومة الإيرانية بمجرمين - من بينهم رجال عصابات روس، وأعضاء من عصابة "ملائكة الجحيم" للدراجات النارية، وحتى مراهقون سويديون - لمهاجمة معارضيها وترهيب الإيرانيين في المنفى ؛ إن استخدام مجرمين محليين، لا تربطهم أي صلة بإيران، يُجبر الحكومات الأوروبية على "زيادة استثماراتها في الأمن الداخلي"، ويُظهر أن "أي مجرم قادر على إحداث فوضى عارمة" في مجتمعات الشتات. كما تُصعّب هذه التكتيكات على المحققين ربط المؤامرات بالنظام الإيراني</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88481" target="_blank">📅 08:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🇺🇸
"
وول ستريت جورنال"
: قبل أيام قليلة من إصدار أوامر بشن هجوم على إيران، تلقى ترامب تحذيرات صريحة من أجهزة الاستخبارات حذّرته من أن اغتيال خامنئي لن يؤدي إلى إسقاط النظام، بل سيؤدي إلى صعود قيادة أكثر تطرفًا وصلابة، والتي ستعمل على تسريع تطوير الأسلحة النووية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88480" target="_blank">📅 08:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ_og4XyOkn2jqZAvflEzb16pou24SCg4yO3WcuNMYaQJ_VDNWgeaulTKY8Z2hoaqbuQ_z-DyyGxjsktzzf27rmGgucGNfHbi-NM63N8QTlUG5fBCpbdIWEH6I5jRlNvVU6w0t4Ey9jwYIx-XWAkN1Y3xuPlM9D1T5C8gfoO38R6hdSFUf1nzQ676pFoMiES193pPo-pMFU3RoNwCrKHtzhtXx2yAEC4Sb1eA4xqpGxV2yw2qD8dr0loxwOUFB50pkdtnZkpfQJSlWy3rpCsKltAPsKkUugszp1VTZkxLM-RLFtWCDaYpWOKJzM_rc1-B_NC7D-ADFGbWwqb6X5Wcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
‏إستهداف ناقلة نفط بمقذوف حربي على بعد 9 أميال بحرية شمال شرق سلطنة عمان.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/88479" target="_blank">📅 01:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq924WviweKsgpk5VU4AUllGjQFX7oLBZuAP_0YTbkUlyi1nBRNq65bt0jz-w2XgyRkKnCNLzOsb6SU7SFJxI3jVkLrtOIHGfLx5W4wmfbmOuWaRQrPV2Na2v_ygnBru1UKzLGnwCgINZQ0js4bfFEQbWt5FhXFcuG1gb40NDEfGqCcOKmcWLMFGnxko6ZNlIFrlrvIGubwNcEP55areBKdgPM9lYTiCqUltge9GnW8_f_yqcG95r8Y3hsG4eF1-XQ6m8SDhB4VmsFtgv0OpmRBW_BLzQTIKwIISnUbJvn-ugSS1DWqb8S8UnSPg1LI5vqz-QLaILzeQ5t45yVJJZ2rQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3dbea05a2.mp4?token=C3EKGXMNxmBXrEXHLFoDjqZBtRKX3q-PV6JO87k6xq39ed9NNq0CIG0f9BLthGsMr-YfVE9pc4lVREVLUwD8yuYjCnoBH9kAIFpNwwifOM7cEVeil2Ch9auF9AY1IYUfHg5CtODQWDb_KfXuEM57aWqRuHUu2b5Ov4TiVLP-bGKrtVu2HY2JS5zm1_h6l-hycV5n2NYhKHdqTXpS2e2UkwRuYFRDJLoROJuU10G5GYavcYLZ-xM4MESyTfqHUQ6D5fQ9eI8lDJoGXbdYjw6VmGCJFs9Vmf91KgcFbSHuEkBvCFofFKIS4QyLkNs6yuGWlcLquysb6NRVbnwtwaaq924WviweKsgpk5VU4AUllGjQFX7oLBZuAP_0YTbkUlyi1nBRNq65bt0jz-w2XgyRkKnCNLzOsb6SU7SFJxI3jVkLrtOIHGfLx5W4wmfbmOuWaRQrPV2Na2v_ygnBru1UKzLGnwCgINZQ0js4bfFEQbWt5FhXFcuG1gb40NDEfGqCcOKmcWLMFGnxko6ZNlIFrlrvIGubwNcEP55areBKdgPM9lYTiCqUltge9GnW8_f_yqcG95r8Y3hsG4eF1-XQ6m8SDhB4VmsFtgv0OpmRBW_BLzQTIKwIISnUbJvn-ugSS1DWqb8S8UnSPg1LI5vqz-QLaILzeQ5t45yVJJZ2rQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تنفرد نايا بنشر اللقطات الاولية لاعتقال الحاج ابو جعفر التميمي القيادي بالحشد الشعبي من العاصمة بغداد على يد عجلات تحتوي عبارة INSS في اشارة لجهاز الأمن الوطني العراقي</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88478" target="_blank">📅 01:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🇺🇸
رويترز :
أعلنت قوات مشاة البحرية الأمريكية في سيول، يوم الاثنين، إلغاء مناورة إنزال برمائي مشتركة مع كوريا الجنوبية كانت مقررة الشهر المقبل، وذلك بسبب القيود المفروضة على القوات الأمريكية جراء الحرب مع إيران. وأضاف متحدث باسم كوريا الجنوبية أن الحليفين ما زالا يجريان مشاورات بشأن استئناف مناورة "سانغ يونغ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88477" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=sQsSPmbuZVv8aOVpbS0xZkfKPkRS5sInt7MJcFJ-iormKEpIJ1BRKHG2jHqxktBSuFEknWa_d6lKCNAebdb4Sfdh1-zKvxviXaf6rF15MKJZnwm5o2gJnXzDLjW5EiET5CRsEjwTaTmXskRF3x0E672Idbxc_XWKk4iVSzEGddsMVnBu7j18kRVzTLCyTn3Ubl-C-sIbbYuKvHXjhA5WP_9LP-ZxXM36m7bzC5yMxsTi3c2SJQ0VAyvMadA74EFEIhG5zqVQcQXEm-7bHvMGOaLXqF6zl2w0fishXWZeUsU4xs35NXtp4CPK7xC-m1oV3sj3-ioTa5yxcDrXKScT4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8050a036ac.mp4?token=sQsSPmbuZVv8aOVpbS0xZkfKPkRS5sInt7MJcFJ-iormKEpIJ1BRKHG2jHqxktBSuFEknWa_d6lKCNAebdb4Sfdh1-zKvxviXaf6rF15MKJZnwm5o2gJnXzDLjW5EiET5CRsEjwTaTmXskRF3x0E672Idbxc_XWKk4iVSzEGddsMVnBu7j18kRVzTLCyTn3Ubl-C-sIbbYuKvHXjhA5WP_9LP-ZxXM36m7bzC5yMxsTi3c2SJQ0VAyvMadA74EFEIhG5zqVQcQXEm-7bHvMGOaLXqF6zl2w0fishXWZeUsU4xs35NXtp4CPK7xC-m1oV3sj3-ioTa5yxcDrXKScT4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي   لكانت الجرف الان ولاية ارهابية داعشية سلفية ..  شكرا حميد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88476" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5i3yjaM4twDEHAW62fB4ZFJ53ebOutzRXariC4DT9Z3URYHYOlkLymMW5i9hGJPLmpfwOePqJCoYoYRcLRgZ7Mh-mn5E9hfnsXCA9mUcH8_7hw1bnit8l2idOhtsDO2Vp0D4wS2TQnVtk3FA_tsjd84lyRuCLisa4IuiJeFuujvrfsHMGmwbNKdEoLeCiGH26K7Pfve4ReO_8uSQ42yPKRiiFXcOcHdnWA_9wvqc8DS75vETwBlK-ARNNw5NShXo5faBIOF1ClmCLzsxRuHquNnpXOb9mOAauhPU9rsE68EPhOyaPavShci1T6cLldOMd0Z5YNjVQS1S8obHMvdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
الخارجية الاميركية تعيد نشر:
مكافأة 10 ملايين دولار لمن يدلي بمعلومات عن قائد الحرس الثوري و4 قيادات أخرى.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/88475" target="_blank">📅 23:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي ‏هيغسيث:
لا يستبعد استخدام القوة العسكرية في مضيق هرمز أو أي مكان آخر، لا تزال إيران تمتلك بعض القدرات.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88474" target="_blank">📅 23:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=pFZBEHZK5X4Aoiiq1C-0gt3iCg5EnU0CS2fnNxa9pe52rWD_cCD3ACbuF2CiBtV0M6xU5VN2halWrkpYB8a88TkApr9FDm8s5FlTB4YrnWoiT4jM8QWe8rhKt2iYbpExVKXVxisSDmLcj00ex1xpyZ4nsXNBanDVlR_Z2ddk0RqDjpqqDUHE0LbySsaq21f9TXFYd-CxHed03u6yWI97aN04rCV3CUixqJ60zCj2HgsgDqiD_swZFltC84xgv6RYGVDi5i2VJH6FVPYTGIlAEa2A9IiGkugoM0iMlIjmSshhvobE1UW7VU-dfUVl3iFxo1QSIku1DIdKqKUHgY4_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845b8cd8b7.mp4?token=pFZBEHZK5X4Aoiiq1C-0gt3iCg5EnU0CS2fnNxa9pe52rWD_cCD3ACbuF2CiBtV0M6xU5VN2halWrkpYB8a88TkApr9FDm8s5FlTB4YrnWoiT4jM8QWe8rhKt2iYbpExVKXVxisSDmLcj00ex1xpyZ4nsXNBanDVlR_Z2ddk0RqDjpqqDUHE0LbySsaq21f9TXFYd-CxHed03u6yWI97aN04rCV3CUixqJ60zCj2HgsgDqiD_swZFltC84xgv6RYGVDi5i2VJH6FVPYTGIlAEa2A9IiGkugoM0iMlIjmSshhvobE1UW7VU-dfUVl3iFxo1QSIku1DIdKqKUHgY4_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88473" target="_blank">📅 21:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=ZFn9PqnzK7q_y0XfDT6jEhI3M9BdHlLA-5Gv17FAOseAng2SUVTl3vLxjxPYv14o5GfWZ8mVyrEpjN3wpeWZJUaoTKOv5ralAd3iwBiV_Br98uz2fcslqYpkr2jqbUHFINs6hIH_mBbqPuWAEImOcNnGkRwpMsdY6D7He-9py9mTf6qhIp9pOQ7YjwiQlUgBuyv6tXnsf1D2MTEEvfr3s_VtbqHqTBaOibZRdBjOmi9FqCFkXir-oTFtHMgBYdJ7IpFmyVemy2OeHKkGu68kpagyC0S7KIOhqQLV0SAwyc5qwXYrDURF-7SreRFeqkk0RC8JGzlQc2pntYpZtHmdbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9654cfd2.mp4?token=ZFn9PqnzK7q_y0XfDT6jEhI3M9BdHlLA-5Gv17FAOseAng2SUVTl3vLxjxPYv14o5GfWZ8mVyrEpjN3wpeWZJUaoTKOv5ralAd3iwBiV_Br98uz2fcslqYpkr2jqbUHFINs6hIH_mBbqPuWAEImOcNnGkRwpMsdY6D7He-9py9mTf6qhIp9pOQ7YjwiQlUgBuyv6tXnsf1D2MTEEvfr3s_VtbqHqTBaOibZRdBjOmi9FqCFkXir-oTFtHMgBYdJ7IpFmyVemy2OeHKkGu68kpagyC0S7KIOhqQLV0SAwyc5qwXYrDURF-7SreRFeqkk0RC8JGzlQc2pntYpZtHmdbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
العاصمة اليمنية صنعاء تحتفل بمناسبة مولد النبوي (صلى الله عليه وعلى آله وسلم).</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88472" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇦
🇮🇷
بيان سعودي فرنسي:
باريس والرياض تدعوان إيران إلى استئناف تعاونها الكامل مع الوكالة الدولية للطاقة الذرية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88471" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88470" target="_blank">📅 20:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=crtiuK82g-Lo4Ri601miqex92pta4pzlVLtHaD6gMH3BaO-HW9UMRzx-3j0__jImz1FNeniSRMF0bnPs6s5479YqF9KvJPQjdZOIGnTMsNHAY7vzZ1oECg-2Hc_mAUgrrdd7UoqRWv_QEkbOK89EiJ_lP4N98Lx55QmlRnLFVpmauyDIXLWd7Yx61W3vt7Ag21VL8bgl2fzBCmp3MOI6nYElBJerADz-IdHWOmYcsZQDNX7HxBHGjKRa5kZyfUciW-GcaHzYcdv_14NhBAZxAP-Oa6G8rjL7jdhVv47sG_7OdYXyDzb1mzZKpVAgkiSyLx3x-1TbKhkoF2A8Fdm9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c955d03b1b.mp4?token=crtiuK82g-Lo4Ri601miqex92pta4pzlVLtHaD6gMH3BaO-HW9UMRzx-3j0__jImz1FNeniSRMF0bnPs6s5479YqF9KvJPQjdZOIGnTMsNHAY7vzZ1oECg-2Hc_mAUgrrdd7UoqRWv_QEkbOK89EiJ_lP4N98Lx55QmlRnLFVpmauyDIXLWd7Yx61W3vt7Ag21VL8bgl2fzBCmp3MOI6nYElBJerADz-IdHWOmYcsZQDNX7HxBHGjKRa5kZyfUciW-GcaHzYcdv_14NhBAZxAP-Oa6G8rjL7jdhVv47sG_7OdYXyDzb1mzZKpVAgkiSyLx3x-1TbKhkoF2A8Fdm9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأميركي:
نطلق الهجوم الاقتصادي على إيران، توقف التراخيص العامة التي كانت تسمح ببعض التحويلات المالية إلى إيران - بيان وزارة الخزانة،أي عدو يسهل غسيل الأموال نيابة عن إيران، سيتم استبعاده من نظام الدولار الأمريكي،حان الوقت لقادة العالم للاختيار بين الرخاء والعزلة وبين السلام والإرهاب وبين أمريكا وإيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88469" target="_blank">📅 20:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHl8KywXt-c2tbJqdo-1xdj3MsGPROTi_wnKIuAoEXIvkmcUuREgaigUv4v9HQP-ilv7ivlSLJM49_CGJSfdl8slznkM3xlmn-k4BTwBAUyirUaGSoILrPv2HnXpLHb31O8YiyyM3xyoOLXyrB2U6YbPNqdNkWpYg-JfjrKfRjb5yrleeJ6HAnAGesz7fb6hP2oKEJK6GifLcJJocSll0hrJh-oWmpj87RVXPqaVAry6bsbfKfe5nPn4Xk2dNzLUdn1uTx1ZaZyiECNyAJqqhIbhotKWauNsaQxWk1nE4ulug2CxeYzu-9aF1vVasJDzd1K0HG2g53qZYhCPPMpLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_ZAl_26s_Elk9Jeo-94SaOKJgewgvzpCxtm_g1yh4EajSrq9fUXLXFiDqnoghk95_l3un5O0D2V6BMzbz4SGm0LaJXTLFY5XGp6fCECkrpXpz-xawwE5E1ikoOPsDsg7NYx9QyAx7cFfS2orfMg5-ZhxuhPLQcTgTmdCourm6NL53yHK4DdITfDIhQ5iBPgnjZQSeRDhynlDD9YZ35p5EPRp83B7s_2_2TqamRkfZAZvq1sRCxjEO_q-FJRy0opQZqzhDRO2uE1hOHJdBNUn_ii32SSy2xUuH74uDh-5r7LzdL4sx9yMQnZwruYVxXrsjjYDONb-HgIY9JYQZmulQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇰🇵
ترامب يعيد نشر صور قديمة تتعلق بلقائه مع رئيس جمهورية كوريا الديمقراطية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88467" target="_blank">📅 20:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6dnL65VuL86mo0KqwZcs3XaZM6DONeoo4gX6qKyMOi_mq6lpTDPowQiShVugVTXb1jFPRWKQg_Gd5Y_7YhwmOUQPgwXxIBko2jYYKVbzc3p7hEoMml4Ink3FG4nXMNZmF-Rsy3n_l3jM00lM4B6OTOXj2qGnA4650TTqi6VQxA9PnG1h5dlb3zmDUlFHQC7j3f8KmUqSBmao4rJDO2yBrHXaEY1tBv2u3UR_p3aAWynQVAYZBYUUN4p43l5_Wmjr31H_P_fcZtRGQsxW1zcsZ4mvcazQghe7q9GGFbt7DEHGo3siVgm8DgMgPZa1BJ25jjwes32PG97o5kJbQqA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف:
يدرك الأمريكيون أن لا أحد سيصدق هراءهم؛ فأمريكا ليست في وضع اقتصادي يسمح لها بتقييد علاقاتها مع الدول الأخرى أكثر من ذلك.
‏أعلن شركاء إيران التجاريون، سواء في وسائل الإعلام أو من خلال إرسال رسائل إلينا، أنهم لا يعترفون بهذه التصريحات في أي مكان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88466" target="_blank">📅 20:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMMpX_IEe1IaXfGzjYXdt7Beg4wCQesXhMv_h69Bi7eg0HxwXk4aKV25nv3O4i_3er7nLwxBCJSlO9jl_TIFwYcElA_bF_mSbHJe6SL_evI6JG23JJqch1HRi0cXzNSAv1I-FeYCK6y5vd_SRWzr8y2JxCxgQIam-SdrdcpdldepYv9_DXw_Im47pfSIpMZmVDWyTiMEMjTurR10kQ3z0XYZFS6cVwY9uti9yU8GrCGt5q62GP7oPpjgpRDh_7Ky6wuixDCEy2HYa2MPzfB24t3THEZ3WbdWARUTjMPYcAPdTCBH0egC657bDj02JCbc9vC8I8JLp8vZ2ECeVDV_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88465" target="_blank">📅 20:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو
: حاولت إيران اغتيال أحد أفراد عائلتي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88464" target="_blank">📅 19:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🇸🇾
الولايات المتحدة تستعد لرفع تصنيف سوريا كدولة راعية للإرهاب بعد 47 عاماً، سوف تقوم إدارة ترامب بإلغاء التصنيف يوم الاثنين.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88463" target="_blank">📅 19:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=OVOcmGTdXAu-2fHL4CclpaGoZ72z5oVwX7SrYeRgaVFq0dWYuDt6bgMLqdGEVQ1wvZWnWK5LodbDj9JVLFyOIpDkbTCiJUia7HJ0RMSiD84c0avBCR_2UuEhNq7t2NRWKm4coxPruNRxr8Z3e4ZPKWKRLagtSNOTkZWmkSPn5Y2Iu0PRaWXp6_bHSCCGW2_eVC8NQ3xX4kfd9v1fZgBbIemK72jJzQUCd3VaxtANXmsGI7Fl3doIzUqAsp5Jv67QgP7l51aEwv_SfOq274fzsL5oZwCrX9w0kpxrlna9fZQOA84lvjKw_iP_jG4ZaJ3vzLZoeh6qvrtYU7mWlQw-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b5c9408c.mp4?token=OVOcmGTdXAu-2fHL4CclpaGoZ72z5oVwX7SrYeRgaVFq0dWYuDt6bgMLqdGEVQ1wvZWnWK5LodbDj9JVLFyOIpDkbTCiJUia7HJ0RMSiD84c0avBCR_2UuEhNq7t2NRWKm4coxPruNRxr8Z3e4ZPKWKRLagtSNOTkZWmkSPn5Y2Iu0PRaWXp6_bHSCCGW2_eVC8NQ3xX4kfd9v1fZgBbIemK72jJzQUCd3VaxtANXmsGI7Fl3doIzUqAsp5Jv67QgP7l51aEwv_SfOq274fzsL5oZwCrX9w0kpxrlna9fZQOA84lvjKw_iP_jG4ZaJ3vzLZoeh6qvrtYU7mWlQw-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏صور الاقمار الصناعية تظهر قيام القوات الأمريكية بزيادة عدد طائرات التزود بالوقود المتمركزة في الإمارات تدريجيا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88462" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يوافق على منح فرصة امتحانية واحدة لطلبة الثالث المتوسط والسادس الإعدادي (بفروعه كافة) الراسبين بما لا يزيد عن (4) مواد للعام الدراسي (2025- 2026)، على ان يؤدوا الامتحان ضمن دور خاص تحدد اللجنة الدائمة للامتحانات العامة موعده لاحقاً.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88461" target="_blank">📅 19:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph0pCNc2xDSVI60MhRA5-85vMDYTHwU15c1KwJDlYijRw3W8-llCModus5p6cMUgtMtd-zjFAcZhPo_Pf_qiiCjlKdyRkhv1xYNwMAGCv1wJ53_WcEB7NRrGR3A_cqXzWWnb6CgDaTG4RAcTY-qLl3fH2rPbSN072PoSSZuLz6ObIwA3Fj841FZNBctTRSPwOfZYBy6T7habWgMmciPvSCF7ZYFsmPEsIEcfeu3ovDbnu09CgerBGyBUnHqVg81fPjcE9YnhxLwfr7TK5gnDbRw2EKyscwZvi3jxCCKVEP59XLCvfZj3DNqRhd7WMQ2JxgKeVoRxarCCQN0WqnicPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند:
بعملية نوعية وبالتعاون مع جهاز الأمن الوطني، فككنا الآن واحدةً من أكبر الشبكات التي تُهرّب الإنترنت (المدمج) والفضائي غير الرسمي، وتعيد بيعه للمواطنين والشركات، وتمت مصادرة الأجهزة واعتقال مدير الشبكة الواقع مقرها في العاصمة بغداد (الأعظمية)، كما تم رصد شبكات أخرى سيتم تفكيكها واعتقال افرادها تباعاً.
وتتجاوز المبالغ المهدورة للانترنت المدموج والفضائي غير الرسمي، اكثر من 100 مليار دينار بالسنة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88460" target="_blank">📅 18:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇫🇷
الرئيس التنفيذي لشركة توتال إنيرجيز عن ارتفاع تكلفة الشحن:
نشتري براميل النفط من الخليج بسعر يتراوح بين 50 و60 دولارًا، بينما تضيف تكلفة شحن البرميل عبر ناقلات النفط العملاقة عبر مضيق هرمز حوالي 10 دولارات. وهذا يعني أن تكلفة الشحنة الواحدة تصل إلى حوالي 20 مليون دولار.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88459" target="_blank">📅 18:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88458">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88458" target="_blank">📅 18:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88457">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88457" target="_blank">📅 18:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الامين العام للامم المتحدة ‏غوتيريش: توقفت حركة النقل تقريبًا في مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88456" target="_blank">📅 18:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88454">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88454" target="_blank">📅 17:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trBZ7ry_xZPPgFbahsiQGUowIhV2t6WmKGjUULKJmVqb5JVHPnTIc8kMW9TIcQfVxHZFUXUKtkbmGuhIdbCtRzbc0G8sSWkefn9rus5j9CGzsNzasfrYmDT_BveS5PTTxOKUYLEaoEFOUm6w8RN1TBNLReDa7l-n9qHygTQp2MW4V5Fg7E3iJWy-2DBiWx16R8mdwBClZqziM74vZcf-640eaTqU8cRXemaC1lgQFJONqe845b1-CuEOG5PQfAHLhiDKaReYOa0_Q1iidk8m3h821NaGEGPmyNbVEDtOQB3KLC2TWUig5JUr980P1ljWDCi5G3AbX6CqwzI9Avh3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPTGk6h-2Jpb45nF1g7P4WnGuvdwppUXmfzLIrfO3eP0zZ85QusniVvghWtxGy04S932tlOIYybYxAS7e26rH_DxaSuf400nBWM5fZxQSEk2hfxHXEjM99h6tVJNhZZHm8uPm4piVBp3iXJaK3aRRKA_iLA2ouWGYXeFxWeIsVFGyKte4_02woaxQxNaN8bCs2YDoRyvyuECs7EDaWkHz08kuEbJlSPyu1_yLgbuW8ZfpSNvccj3ImdXwGCG6Ma8QHmRzHERfhax6odB8RekY2TNeHStie-lRM5uHJRxOTfpvdPeFDBwK2mVKUPIdoi3x5Jcje72lsYx-WRYlC-tCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن   مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88452" target="_blank">📅 17:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=HGsFwI3-Pj95fhKOItAPhpOQLqeUIt3UQd-PdgZr3a_nxOZDYAzQmMMFj0VAPYbpJUXJ0-sPqabweQLcHvaFwvvIvv6rkvrZwCSAjAUngXbqgV5BYIAkIg0L7r6lCimYcqa_KJprfCeTNvlu7TWLwOhb0rVt15ddJ-1xF4jLRtth03a6SuOeI4HQz83koDKpH0qk4Nf4mTnph10KdsY3Wv5mrj5MXp2ZtA32ro7EMfBaZUMY2ddD8ZlWEe2W35YMvYzngb9HyGrD4q6yU-qxWwjPT4ieOZi8zStGSvdQOv0BAk43UZo_209V9l1xVOB1FxsRN60lfiUkIaT4zYArAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef5880eec.mp4?token=HGsFwI3-Pj95fhKOItAPhpOQLqeUIt3UQd-PdgZr3a_nxOZDYAzQmMMFj0VAPYbpJUXJ0-sPqabweQLcHvaFwvvIvv6rkvrZwCSAjAUngXbqgV5BYIAkIg0L7r6lCimYcqa_KJprfCeTNvlu7TWLwOhb0rVt15ddJ-1xF4jLRtth03a6SuOeI4HQz83koDKpH0qk4Nf4mTnph10KdsY3Wv5mrj5MXp2ZtA32ro7EMfBaZUMY2ddD8ZlWEe2W35YMvYzngb9HyGrD4q6yU-qxWwjPT4ieOZi8zStGSvdQOv0BAk43UZo_209V9l1xVOB1FxsRN60lfiUkIaT4zYArAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ضربات من أنصار الله في اليمن
مستودعات أسلحة العدو السعودي ومرتزقته تحترق في منفذ الوديعة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88451" target="_blank">📅 17:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmwJiRwvJw5wOaXQYAZt9KWbTkTwG1IWb6WZWp9QXBG0-a5ny4KjWmIxcXJxf-VmTX3_s0lAKDanhctoKmfwfUjoW7Fk7_pxbQ4ID-6LWJ-ftYhrYvPUNcsxKqagm0RK6wqv1GSIeKMv5EJR-WWVIF84YID7eTv3lJqb9O7itvFUU-AOTXLlMPyTdCAKHSTz70B4etWFZMOPk8V2bVEKej-bqHth6YXr709-n6q2yEKmJ6oUKB1kYGY41cZLdVgIyzTzq4oX7-SrMkEtwd2b97BXyecqy9AVa6AJR9TtmyvWe5V6kZ9Lx_etR9JeIHyF86mx95xJzsQB-g5tx1VxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الترجمة بتصرف " كندا ٥٦ لسنوات طويلة وجانت ناصبة علينا "</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88450" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=hlsugf0gYaDPOoVKyldhqu2nJp3W2fd2Caob_Stu3kxBYtCXo6I-e80IaRZDqWHgimZmX8XFTTttby8YzWkBNT4vkbxibyhm0ApGiGZeWn8y_ideEycXCB-H7i-JI7ac3RbjqPfMOjn3NfdUAYZQZB3XaMZrta2fx0OHpoKyWZiSlBhuvy20Wvha_-QhL819MlpCtQjnOKEFuQDRrIehuTUXYdE5zDfepoyh0KNzS_EtdNcri7nCiB3X7JEZ8qbTN8LVZU4sLZbtq86qJIh4MLYl420_UDwtZUwXPZwYtrD-NllhXwbkLaUFAndl1deww1r1tN57zkADLVNC5MhNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c68e0f99.mp4?token=hlsugf0gYaDPOoVKyldhqu2nJp3W2fd2Caob_Stu3kxBYtCXo6I-e80IaRZDqWHgimZmX8XFTTttby8YzWkBNT4vkbxibyhm0ApGiGZeWn8y_ideEycXCB-H7i-JI7ac3RbjqPfMOjn3NfdUAYZQZB3XaMZrta2fx0OHpoKyWZiSlBhuvy20Wvha_-QhL819MlpCtQjnOKEFuQDRrIehuTUXYdE5zDfepoyh0KNzS_EtdNcri7nCiB3X7JEZ8qbTN8LVZU4sLZbtq86qJIh4MLYl420_UDwtZUwXPZwYtrD-NllhXwbkLaUFAndl1deww1r1tN57zkADLVNC5MhNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوة من فوج مغاوير الرابع تتجه نحو الجسر المعلق</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88449" target="_blank">📅 16:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=Yize57tKseAk8tMxVHP6zSX2Pee3_oUw6WGq0KGnuMWhKsYYVqmOAkqq80PQP69nAY_eu72NYxCQYh1jquti7tH0CKRJ6uec26VB1qo70lNX-o65aIWRfvxHffbjOcBPJz5Mc-HLKMORUOxb0WuBB09UQ7o3fYEPt4XkBoLogEuNcPH98P5_6lYw72nv4fyn4I2TS2w4ZB64sJkXVCmZJIkD9F5Lg_NQU6kfSiRQfR-IVkCMFnAkJlcTNeSitbFFm_x65uB7aaQajORZ1aWcBu3nYHzDxOR4hfv9FuFEegRkMFGlEBkwWFvbG7-1NId5uhC75xjVYXsFzUIbY36zxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc052bc00.mp4?token=Yize57tKseAk8tMxVHP6zSX2Pee3_oUw6WGq0KGnuMWhKsYYVqmOAkqq80PQP69nAY_eu72NYxCQYh1jquti7tH0CKRJ6uec26VB1qo70lNX-o65aIWRfvxHffbjOcBPJz5Mc-HLKMORUOxb0WuBB09UQ7o3fYEPt4XkBoLogEuNcPH98P5_6lYw72nv4fyn4I2TS2w4ZB64sJkXVCmZJIkD9F5Lg_NQU6kfSiRQfR-IVkCMFnAkJlcTNeSitbFFm_x65uB7aaQajORZ1aWcBu3nYHzDxOR4hfv9FuFEegRkMFGlEBkwWFvbG7-1NId5uhC75xjVYXsFzUIbY36zxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88448" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
مصدر امني   انتشار قوات سوات الداخلية لاول مرة بالقرب من مداخل المنطقة الخضراء بالجادرية وطلب إسناد من الشرطة الاتحادية من جهة المسبح إلى فلكة الحسنين .</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88447" target="_blank">📅 16:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مصدر امني يوضح لنايا   قطّع طريق مطار بغداد الدولي على خلفية زيارة قائد الجيش الألماني للعراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88446" target="_blank">📅 16:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne6rumFq-S-yJBsUX_SMTzD1P_gJqjnWZBEHlcA9S7KwGmSPHQTV30hgfFt2eqalUf6aOdAHxs3kcvk5VStxMXDExhGHxVoaGDFyTi3I10xiKq3KjN2m07fRBtbTpL4L-EDm-Hemi-Gq7802SWonw3GSkdEEWlWfbtopIms8KC4D4eK4z-HGUuJyl0DR-vRHM9NaxMCaZpzYI5MpHUsvMFxXVs_XnNDSXeTrAHYYbj-gqmWyWvw-CJ13ZvfBR2GUhSXjmulcUchWx-ZJ1ULVBohkHc9ir6XGk4WJ_79VSo8yrZ4xlUTR9pD8KAzFdsTjymt2dJPYCxnCtevpgeFOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تضبط (428,794) قطعة من الأدوية البشرية المهربة وغير المفحوصة في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88445" target="_blank">📅 16:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
مناشدات عبر بوت نايا:
نناشد وزير التربية التفضل بالنظر بعين الأبوة والمسؤولية إلى ظروف طلبة السادس الإعدادي، والتوجيه نحو تأجيل امتحانات الدور الثاني، وأن يكون الامتحان موحدًا لطلبة الدور الثاني وطلبة الدخول الشامل.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88444" target="_blank">📅 16:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=qM_CnhgF3Bls__yorvd3tzsqzUeELkdKV6JU_d77-Zm5Bg0K-L4g6-4MEnThCqKdeAOfV5vy8ZVhfN3OqgFQ6KFlARt4twXNCydDAXNq7BJxKlGBLiQAT8LoQmqHQ4RmtqHX4y6aPKhfG-tRGbyAI6Z52T2n4bIJhHbX7hEqvZxRb1l229PItoBOEHX6Yy9KigzGCJrITdSJeG8LC9ze2QZj_x4NHoggaWVG-iII7V0R80ptP4UjMviiXyR-SfzZpR_bJtTyPN9KpaH0MSZX0rC7oS0fMuVf5h7AwSzlpXzUFLD2WyQWjM7nyEWSDAn8OQeatcjDrykF-j9gWRf9Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a39d0b36.mp4?token=qM_CnhgF3Bls__yorvd3tzsqzUeELkdKV6JU_d77-Zm5Bg0K-L4g6-4MEnThCqKdeAOfV5vy8ZVhfN3OqgFQ6KFlARt4twXNCydDAXNq7BJxKlGBLiQAT8LoQmqHQ4RmtqHX4y6aPKhfG-tRGbyAI6Z52T2n4bIJhHbX7hEqvZxRb1l229PItoBOEHX6Yy9KigzGCJrITdSJeG8LC9ze2QZj_x4NHoggaWVG-iII7V0R80ptP4UjMviiXyR-SfzZpR_bJtTyPN9KpaH0MSZX0rC7oS0fMuVf5h7AwSzlpXzUFLD2WyQWjM7nyEWSDAn8OQeatcjDrykF-j9gWRf9Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مراقبون
اعتقال ابو جعفر التميمي دون الرجوع للمؤسسة الدستورية التي ينتمي لها ضرب للقانون العسكري ويندرج ضمن خطة توم باراك لاشعال الفتنة بين القوى الامنية واشعال الحرب الاهلية التي يتربص بها أعداء العراق …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88443" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88442">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGZAS658rBKWb7vr9035yPcnDFlSLn6RBjmdV0_5_ooH2YeaE9vklR0niJ2zyCm4iO_-xsTyoV1KA1gPwlcfFsv1vVE5v8fGITZmWU7ezGNzYLeR5Nvm0DZsl8bI63FkWjyqJRuGMtfled5MljoMrH36hiC7gahcn2AA97nZQxrCswmuae4dtoz18YKuFz9L-ztK15PGl0H_SoPsCGr4SlVtpO1K6LQmklEOgnX3bNSVMUOU_wCIkFsnPEOYwXFXRSnTCmaoEb1KhuS_ee_9vY9XrSd8m18UoK2VwWBD1Jq9mki2pz2Dfn2i3UxZcWRCBkWJ1PL9UM3mPq-O-jo43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ايران تنهار</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88442" target="_blank">📅 16:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88441">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88441" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88440">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">إغلاق ساحة الحسنين بمنطقة الجادرية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88440" target="_blank">📅 15:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88439" target="_blank">📅 15:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88438">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88438" target="_blank">📅 15:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn6hBpXTrkbupSbWI8rTs2VkbuTIlIRmlvU9u6ZJK-i_yEw2ErU52e8MpJeT3EMEuOZlttF6TQDkSgkymonTmcILS8innx94Uo3aiOwtj_E9ngd5qHnr5qJobAKAgbroKedgsiKPh3-7_FXAUdPT4TJa_WVe_8RE1TZUNK667r7G7lXmtegGofRqMMLonR6IE9_-VxAXe20_0jcGRjedoCYTc8S-EX0HHur--P9CtCWgCviynZZq5agOIoEQTKvqjcYBaNJ88ukBdcdUlsy09B2zovxuvS6ghRP8do9DJz9N0JwZxH2osR5HRepaTbLyKpP54INpzeO78XjQBK7NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غلق المنطقة الخضراء وسط بغداد من جهة المعلق وانتشار قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88437" target="_blank">📅 15:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
رئيس وكالة الطاقة الدولية:
قلق بشأن وضع الغاز في أوروبا هذا الشتاء بسبب انخفاض المخزونات، وانقطاع الإمدادات من الشرق الأوسط، ونهاية إمدادات الغاز الطبيعي المسال الروسي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88436" target="_blank">📅 15:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انقطاع الكهرباء ‏عن منطقة مزارع العبدلي في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88435" target="_blank">📅 14:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLD5k-wnaIo6EOuF1jmi6Vuhu9SV5f29-9HgEHMa9Bw2gU8Ughc2SWmA69dG4uazWmrdKOV6sOM9u1hSTk61Ue_SiSlJfv-WZjk-jUhO7qpok_2WdF4U2zXwig_UTpDHSGG4d7G-cXjOqGGBBi0pLBYkb2TKPtQf1vGQeGOX5GWpXslEa9oIxihTAR37VIR6Ki5tSLbJ4zW6dgH5zv5AL-v6yHybu6wkt9JNhHkpc4EiRmpTQoCLp8dtpgfI-WVeRUiGOdBrINkpDmItLOINt2tINUUNOdcR9uLX-XJt_sNbcKMq6N7bhGDVUDqRW6ECJUJerySRw8rZjovykuQLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت ليست بخير</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88434" target="_blank">📅 14:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKiYixg_147kC-rBCvE77DmAHyQFGWjw-0yVDC7R8NGPL1KInW9X_yeWx492OUM44GW36EDLijthTQNPfYgMCjyJ-EqU8iKF3MUhPBC1kfecia5eksf_T9QBLJ1Aj1DqNsEMIDngFcIZteDaLo9dvkRHq6iGzn0lqOv9jP1YMRfPEE_ZZCyAVPCsVbKis9NsOrYgaF6fuBIHXujMgdvvg6jHgnR2D7c506inEcvutKO0TKhpWzEwCQuIYGObJYses4xySy1HPSRLxo8SIqz0-IyfEeUiSmVP2LHAj1CoKPsTBdMeujb1-X1ORzrW-8ZaZ-xuzMoqy6cKLebH9xPJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
‏لنجعل أمريكا جائعة مرة أخرى! ‏لا يمكنك التستر على الهزائم بادعاءات كاذبة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88433" target="_blank">📅 14:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pggTQnIL__N2Ad8UXhWzCOc4HUYKKDzLy0i53uTmlS-bCvP3d_KlpqQ0hHmKLBOPv03zO_xWWqtfrXwOsY3zg7_ucxy83GgWbFRrR-ougR99SiEKqo89P_Z1r6WOze63AP4J2lMhpyJULsIkVZnfFv_KrDfI-ViPMsu2kJKZXYGZikAvn1sXknuugLbqupZVsyAgJ_5_hRll1W2qFWc8BuG-MYhLeXcUsE3nZ--Og2Oa6LrbvIud36GXlsFg-MLMNDMR4diCa2UI3qHP0Eob8G5UsPjZ9CNckVquzaJ5w5GydMtDc3eltwbOIfTMuqeShATQJUz2Lzcvz44dHy2g9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدير مديرية الإعلام في هيئة الحشد الشعبي مهند العقابي:
جماهير الحشد الأحبة، تمت تسوية الالتباس الحاصل بشأن اعتقال الإخوة في الحشد، وتسليم الموقوفين إلى أبطال أمن الحشد الشعبي، لمتابعة ملفهم مع قضائنا العادل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88432" target="_blank">📅 14:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=ekmKRY1mU77pjxCD5YwCdHsXH9v8khj0uQX70mGDXt7HuBp7UFmBjhdTFK2TsCldZIdByh7a-zsY6g477d8DMgCBFmTjaT0Kyp3UYUpoWGW4M_gmew3eHh5KdHzAqGVV3T4oQ8VR4zcrNfp8cWW4VFGgVDkNwhmJWNf4brAkSypF8K_O3cKaNA6cZYjag8fkTFij_q0UpSX2QNSX2m_qdpUy-RVrIQQN5eLpcMflrV-Bbrnz3HtXic0fxz4H0Lj9LWpsnmXkbw6WoC80cU_7EU8N6CQe8C_ZNjPd1VrDMJqkae5BCBa8rUBeAPhC3Itw8NvDTRTntPebV4WT2hPkDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b09c0dce.mp4?token=ekmKRY1mU77pjxCD5YwCdHsXH9v8khj0uQX70mGDXt7HuBp7UFmBjhdTFK2TsCldZIdByh7a-zsY6g477d8DMgCBFmTjaT0Kyp3UYUpoWGW4M_gmew3eHh5KdHzAqGVV3T4oQ8VR4zcrNfp8cWW4VFGgVDkNwhmJWNf4brAkSypF8K_O3cKaNA6cZYjag8fkTFij_q0UpSX2QNSX2m_qdpUy-RVrIQQN5eLpcMflrV-Bbrnz3HtXic0fxz4H0Lj9LWpsnmXkbw6WoC80cU_7EU8N6CQe8C_ZNjPd1VrDMJqkae5BCBa8rUBeAPhC3Itw8NvDTRTntPebV4WT2hPkDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع طريق مطار بغداد الدولي لأسباب مجهولة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88431" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=JYOvrR8A2MQKBF-THdNBwVZYqEOGhS22PF9YhhZ9JVlZuVv-DBBo8wngz_aT9UMT86bjg5I_Vvd4lFnArhwuC5QFSESo8t3mf45vPuxHVs98iUhuIsvlEPx2T7Dyg6ljB8eIBBqQpIF2yBddqOyEp6KFFBDFEZd7X4pyFMdsS268sMsDQemkNmJ6OMO9PVXmFtJ5qA_rL-YQq7A2O-0ILe0F-bTpdrFVqEcTUsM7xN42T83TNBSSfRVYVdUJete2t0XcI-DcLjkWHvqyqQqh8FJBB4mswVtw-Hx6FoC7w1FbnAnc0ege5JzcSH1qD3k7anLg19JB3RBcib--ALoWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b122a3fb40.mp4?token=JYOvrR8A2MQKBF-THdNBwVZYqEOGhS22PF9YhhZ9JVlZuVv-DBBo8wngz_aT9UMT86bjg5I_Vvd4lFnArhwuC5QFSESo8t3mf45vPuxHVs98iUhuIsvlEPx2T7Dyg6ljB8eIBBqQpIF2yBddqOyEp6KFFBDFEZd7X4pyFMdsS268sMsDQemkNmJ6OMO9PVXmFtJ5qA_rL-YQq7A2O-0ILe0F-bTpdrFVqEcTUsM7xN42T83TNBSSfRVYVdUJete2t0XcI-DcLjkWHvqyqQqh8FJBB4mswVtw-Hx6FoC7w1FbnAnc0ege5JzcSH1qD3k7anLg19JB3RBcib--ALoWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88430" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سماع دوي انفجار في مدينة تدمر السورية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88429" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88428">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=SbHpBlBtfOsjnYqjYrEBKZeLBdanevawbdBbbQzoPkXLLbt1IcyWHQnsOpcEr0JS40fvSr46Tc2wQw29pANAtixJuM-BLaADD8Pz4H9AP8mOhp4A_TGAudAJ3f2fTBhBJzusAEEDEK4XW8vXHZaTIKdysdwKEcsqYGcUZlyISx_qlZ3NsAAvRCvqLj9pwBd0Ar2VCrfQyzP-HK33BGqeTfYdWbAhvs3pGt5E4PShH26_7-kkVT5M-dNPZedeSSUsex4mB23ACg29HwLP4rDw_BTq_lFkSDi4_vG_5OCo8mLs9wOscxfCaTtH1m5tXrFMe2i46--hN4m6jGXBrCiGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec4022a6a.mp4?token=SbHpBlBtfOsjnYqjYrEBKZeLBdanevawbdBbbQzoPkXLLbt1IcyWHQnsOpcEr0JS40fvSr46Tc2wQw29pANAtixJuM-BLaADD8Pz4H9AP8mOhp4A_TGAudAJ3f2fTBhBJzusAEEDEK4XW8vXHZaTIKdysdwKEcsqYGcUZlyISx_qlZ3NsAAvRCvqLj9pwBd0Ar2VCrfQyzP-HK33BGqeTfYdWbAhvs3pGt5E4PShH26_7-kkVT5M-dNPZedeSSUsex4mB23ACg29HwLP4rDw_BTq_lFkSDi4_vG_5OCo8mLs9wOscxfCaTtH1m5tXrFMe2i46--hN4m6jGXBrCiGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحشيدات امنية كبرى داخل المنطقة الخضراء من قبل قوات مكافحة الشغب</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88428" target="_blank">📅 13:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
إنفجار مجهول في قضاء كويا بمحافظة أربيل شمالي العراق ؛ إصابة 4 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88427" target="_blank">📅 12:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية في مدينة زاهدان جنوب شرق إيران؛ إستشهاد منتسب كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88426" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
🇵🇰
وصل قائد الجيش الباكستاني "عاصم منير" إلى العاصمة الإيرانية طهران، للقاء المسؤولين الإيرانيين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88425" target="_blank">📅 12:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=iKUniJtCYfCoI7V2fUsloJ9BvBRGZPThfbadwDl11WL2iLuG_6M6Ci9uPbDpv_Td9FKKJv7okxpWcQazdz0mon41ZuTPBVtL87JeN4CE--B1D3RwjrKw-aGP7vB3KiGCEHF7AGKq9_BLjs8v1FOXzLduCSdo5SwsK5LeAzjliT33vvwB4xxDBLwy7bBApv8-wUsgmd_njsRw-m33LAABN4STR6pVhFnJT-KSu1vKfPaDHrEFAmnVBALc3p-0FNllxMZYANTo6nV8-0MlPruaDqN4GDvC2SGbQhtmU54yv1UNxsNDvcYoGz2sTBqTC_pyAxVreIo-yQQZiS5EZGAxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1fc56eb9.mp4?token=iKUniJtCYfCoI7V2fUsloJ9BvBRGZPThfbadwDl11WL2iLuG_6M6Ci9uPbDpv_Td9FKKJv7okxpWcQazdz0mon41ZuTPBVtL87JeN4CE--B1D3RwjrKw-aGP7vB3KiGCEHF7AGKq9_BLjs8v1FOXzLduCSdo5SwsK5LeAzjliT33vvwB4xxDBLwy7bBApv8-wUsgmd_njsRw-m33LAABN4STR6pVhFnJT-KSu1vKfPaDHrEFAmnVBALc3p-0FNllxMZYANTo6nV8-0MlPruaDqN4GDvC2SGbQhtmU54yv1UNxsNDvcYoGz2sTBqTC_pyAxVreIo-yQQZiS5EZGAxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88424" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=nhrB4Sv_TxcVZQl_oIRDkP3Udeq6QUX7Aah0dNnxc0PhZTNrMcYHREo33BL6GqQszv0voRnJCOpUs0V4-yEuIxmMGlXAUDZr73-_mBN1pRpFEt2EzGXg6Y6BrnAR7MuS_CD1qIEC6KmysqrasbESh01Mb64ISUflVwL15u2OSTCtZEICd1qToZE3NGJPZbHruv9elSoPuY91fwEfJ8iCkdHNmuA31dKUGfumCcCUD6UvHWJMRy7YIDynZ0GRDTRjLtRTLybdS2yJASk4ELkeVO0IXxX6qYzjgnGc5gVgOWf_cg8md_xOfXTXUGW5qpQyHXBAkqsBUNe5ogRxFjAQ5pyiIByCNL6OmEcD_Aqgqj8KGa1DelUztR9J_iw0XDHkRkrI211TwazlnRR_kaYByqq2_yqC3gzSN-NQBRd0wQXDMjM7O2V4PcvM7vLb60z0NNTxcNl94iVB09Eo_KkkVbxbKEymCOqQEvPEDcNiFHLrs1Vi0cuMM-vy22cbtu6ESggEVgJjGYjNHKHY7TVcyn0SxL_Ny-cSi-cvyrS8uo9mrmn93H3zvz1vr637cnyrt3lhTCiFK8KKvfiZRIbaSpEAq5e2GLrTgLEHG4C5_66kwRxdY8l8pwO5WmV4rD3tBqzXg2sRb9FvgwFEiTET4IjS3V4Q8-cv3ucXEnIGgl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5ed1dfe3.mp4?token=nhrB4Sv_TxcVZQl_oIRDkP3Udeq6QUX7Aah0dNnxc0PhZTNrMcYHREo33BL6GqQszv0voRnJCOpUs0V4-yEuIxmMGlXAUDZr73-_mBN1pRpFEt2EzGXg6Y6BrnAR7MuS_CD1qIEC6KmysqrasbESh01Mb64ISUflVwL15u2OSTCtZEICd1qToZE3NGJPZbHruv9elSoPuY91fwEfJ8iCkdHNmuA31dKUGfumCcCUD6UvHWJMRy7YIDynZ0GRDTRjLtRTLybdS2yJASk4ELkeVO0IXxX6qYzjgnGc5gVgOWf_cg8md_xOfXTXUGW5qpQyHXBAkqsBUNe5ogRxFjAQ5pyiIByCNL6OmEcD_Aqgqj8KGa1DelUztR9J_iw0XDHkRkrI211TwazlnRR_kaYByqq2_yqC3gzSN-NQBRd0wQXDMjM7O2V4PcvM7vLb60z0NNTxcNl94iVB09Eo_KkkVbxbKEymCOqQEvPEDcNiFHLrs1Vi0cuMM-vy22cbtu6ESggEVgJjGYjNHKHY7TVcyn0SxL_Ny-cSi-cvyrS8uo9mrmn93H3zvz1vr637cnyrt3lhTCiFK8KKvfiZRIbaSpEAq5e2GLrTgLEHG4C5_66kwRxdY8l8pwO5WmV4rD3tBqzXg2sRb9FvgwFEiTET4IjS3V4Q8-cv3ucXEnIGgl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
محكمة الجنايات الرابعة بدمشق تحكم بالسجن المؤبد على مفتي الجمهورية السوري السابق الشيخ أحمد حسون.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88423" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">على الرغم من اتفاق الإطار التنسيقي   بأن مذكرات القبض تنفذها مديرية الامن والانضباط بالحشد الشعبي في حال كون المعتقل منتسب ؛ قوة مجهولة تداهم مناطق شرق القناة وتعتقل الحاج ابو جعفر  و قوة اخرى تعتقل ثلاثة أشخاص من منطقة البلديات</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88422" target="_blank">📅 11:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=g3NgnqhgjTRrPoes7mphqU8ICNu2ndpXoaogVYmn82xXDnMB_RamMzeDikXizo3fgHe8yqFt47kaRoGpT21TxAIXXpVAuoF6eXCuO54P5cy5OBrlzIMBlOYIdo0ActjpUy-Gvbo6gyedicatGrA_n5ZRUBnff9i_C4AoDJSy-lcOAn59as5Pu77vYsEKnorXVpdiQucKtdKXB9aPmA15fRo_ljH2XpWcd5DCxoOdCb9tAj425pB0K_49zpGLr44MYThHn7nipF8gz7ZczEttcmbt9eVSw9OntDlm5TLrNE_giwSb2CyNXZzQPoftNtR63NEeApqi2eZX8zaevG3pyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67556e45.mp4?token=g3NgnqhgjTRrPoes7mphqU8ICNu2ndpXoaogVYmn82xXDnMB_RamMzeDikXizo3fgHe8yqFt47kaRoGpT21TxAIXXpVAuoF6eXCuO54P5cy5OBrlzIMBlOYIdo0ActjpUy-Gvbo6gyedicatGrA_n5ZRUBnff9i_C4AoDJSy-lcOAn59as5Pu77vYsEKnorXVpdiQucKtdKXB9aPmA15fRo_ljH2XpWcd5DCxoOdCb9tAj425pB0K_49zpGLr44MYThHn7nipF8gz7ZczEttcmbt9eVSw9OntDlm5TLrNE_giwSb2CyNXZzQPoftNtR63NEeApqi2eZX8zaevG3pyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
الخارجية الإيرانية:
أمن إيران والعراق مرتبط ببعض، ويجب أن تكون حدود هذين البلدين آمنة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88421" target="_blank">📅 11:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0OiOuZo6fIHBBrrzBR564T4d_mY18kVCY-JRM6SMbuWkZQfFQNZ4hy68rtUXuT0Ex2bz_u9QnljzDMVz_5g5rPcxVeu08rgYicY52PGgYFzNrado0d6RaLjPBlI_vZ2t7aK4qtFdp_S4FKLs8pciuYwvLDsiuqzOmeTqyWeqkdOYImsjDIpdt1mlhfJhnoygbnqvl61-ZhGsBpfAoc0LN-sHGgCET8R-2XBk0EVXCBkIipnzWH9BlCHd4LTSPpKpCOqa0J5G80HHMmmotw0QXi0Hq2n67OmDHznEXqx-tPoHb1LrM8_zN3CKpeyc98O9_Fm3SuRl7bU5DpymxFu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88420" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88419" target="_blank">📅 11:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88418">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=a34HuGR9X40Jvwz2_02uqaIEt81tS7hjqAnPdy0WlCGEPqqJFf6YyFnGOFmJdxoPbzknX7qmAghRq76HN-MLVfMUXV7p-WonAs3kK6M3N5LhicPgXeMAG0oj7Kc7xEoNO65VIHACBJFv1ysvbUVfXTSlhnNsTHGTVfuyyNaCfB3ZMFRv4SCvuKFaMpClh7UIk5J8hRCdgVgT19KgW0dECUS_fjP49EkidL8KoG-HG6PA_PXRwBvV79NSLtEAuhb5CYOjRF8F06dHFiS2nAZ0zxFK0_zVk8YtuaPGRMtEq6nfFRrcW90xXn9wW7th253iuSV5KOxz9frNEhtLN-2VNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e1af33a.mp4?token=a34HuGR9X40Jvwz2_02uqaIEt81tS7hjqAnPdy0WlCGEPqqJFf6YyFnGOFmJdxoPbzknX7qmAghRq76HN-MLVfMUXV7p-WonAs3kK6M3N5LhicPgXeMAG0oj7Kc7xEoNO65VIHACBJFv1ysvbUVfXTSlhnNsTHGTVfuyyNaCfB3ZMFRv4SCvuKFaMpClh7UIk5J8hRCdgVgT19KgW0dECUS_fjP49EkidL8KoG-HG6PA_PXRwBvV79NSLtEAuhb5CYOjRF8F06dHFiS2nAZ0zxFK0_zVk8YtuaPGRMtEq6nfFRrcW90xXn9wW7th253iuSV5KOxz9frNEhtLN-2VNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط طائرة حربية تابعة للقوات الجوية الإندونيسية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88418" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88417">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1M1lvPCYgw_angM6hD-D0fwigM24m2B9hA9aceE6RtsqmpedwDDuMcBaFYbdNJKpRmlbJcBhZeghb_dNdsK5ka--aQUsLCa24kc2EHnornu5SSrFqSrDcCnR40dQDS8KBfaICwYmF2lhpTXJBrGhGtBT5mmgV-DcFYnzwBi2fG_j6Ei_nWbXzMr9xFgfWHlySn3uCQ1IkET96XkhTSPVlacXRAEYok2Fn8Z5Xfj4Lsoka1fn0FWIpEazj92HuaFYv2E4Rvi82oILFBzxg8qdO-84xS4KRnilFx3ZH3lJOzQZL5YFUx5L4qoMHEi5WwGn4896syIZjbntomz4FXmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسقط وصاية توم باراك على العراق والشام</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88417" target="_blank">📅 11:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88416">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=eRRK1KNe0Z3qftG8zIN-88dvW-sgsQGexX-_GwmEzOFhGLZ7fvUyP4ZF-9I00PXFy5TIqmCGyKxCfBA3kk0li-BYaHg9AvC_sxDkh1m9KJaO1Ms5oL0t-6_QwyFvTO0aw0GQCzUGC_6mwZJKn-3-sOG4F5baM6P5Rx3YSVuJ8aAJTn7nBcjYqKF41CTWzcjuZZl7PuQkeo_EOy2YVh-TAmtM9czShx4RgLRBXtnA174HXo-hteEt5842HoCuTf_znJuioG_r6t_fA_Lfm8P5Og7JI2soJ4rS25tVFXNdBpkWn_sB_XSduV3CeweWwxOGSE87ggZu2MYFT-4NoZgIEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba72a77c.mp4?token=eRRK1KNe0Z3qftG8zIN-88dvW-sgsQGexX-_GwmEzOFhGLZ7fvUyP4ZF-9I00PXFy5TIqmCGyKxCfBA3kk0li-BYaHg9AvC_sxDkh1m9KJaO1Ms5oL0t-6_QwyFvTO0aw0GQCzUGC_6mwZJKn-3-sOG4F5baM6P5Rx3YSVuJ8aAJTn7nBcjYqKF41CTWzcjuZZl7PuQkeo_EOy2YVh-TAmtM9czShx4RgLRBXtnA174HXo-hteEt5842HoCuTf_znJuioG_r6t_fA_Lfm8P5Og7JI2soJ4rS25tVFXNdBpkWn_sB_XSduV3CeweWwxOGSE87ggZu2MYFT-4NoZgIEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث بإسم عشيرة الهركي: لا نتائج إيجابية خلال الإجتماع مع وزارة الداخلية والأمور تتجه نحو التصعيد ضد قوات البيشمركة التي تستمر في إعتقال الزعيم خورشيد الهركي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88416" target="_blank">📅 10:21 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
