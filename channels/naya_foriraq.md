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
<img src="https://cdn4.telesco.pe/file/gbUD0iI6xr6h5WGaLTO2PVloCDW-k1ydik_W-nh5EGr4VIwBBMv_NH0hJV_77Yn-984Ahk752mnvu4RkhwW2M5pnCCwKlzOFQNdCRZYnHxlURmBiiOMe4ByJ6npeDQc8gy1j0RTOXLaWnI6t976HZZ56JEyaZjmkTSoUZbjvsj6v1u7Ei5_8SIB94mehEjJfOVohRCe6xF9jm4-AU5_Xt7wGPjjF5eCoNCcTmj9juCRhBBc0O8mipg7t2qKkeoCOg4hvSoUY7xJXN-uzBkTXkVltQXA5RK-7qumi6r96iw-VsADWyVuSDzJdWNak4LOSWgLJM5ZqZzsTDE-z5_Vp3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 14:19:15</div>
<hr>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGvrKqesoW4tQuQcpvIGlT06hfWq9_njiaxWVuHE5yEfTET2iWppNIOsHEDqcSoBFtbL_iCf2jFCF5cROzo6YeMYkGLXcoMjdTCvHDgshOuuzHMH1cKIJ7s1Z6sJlh2a2zoJ5j-shx8OKBmNPc-Wyq_wHE-hxCs5IJ3UWrweRIXTUK7f8kKmQhDrl0v2V4i6TZVkI_97ILlVVy6s86hHPT-qXqjLKJkp5_kjlEBP4Yz2s04cz6osj9VZBu9avWqXBUZHE8LyW9nO97wPZWFhQeIFwpkfkcTUBpUAsuIzY5QLxbrVGbfauWV09Yen362P_Q7_ZznnSdnzzJUzcB4OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مجاميع مسلحة تابعة لليكتي و الكادحين المعارض لايران(كومله) تفرض طوقاً عسكرياً حول جبال سورين في السليمانية شمالي العراق، تتحدث الانباء عن محاولة لاعتقال محمد حاجي محمود.</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/naya_foriraq/75928" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sc0ARIsplBhjELPyHvzf7V9JBlUhpbm43NVzsBZswTAyKsc-fWP5MZsNwVbMuZiW94Eo8CAEAcOnYs_J_Or7f8EkUyNavHh27Nhm01wvJ66XN4CI5Dr0E6Pf11ZVpGuFx8zPyDw760CDp4KGYR2rQ1b2f9WakN9lTZBmwQQRf0OdjGw7GF3ZKZh1DucLiQ0pjAEPrKA7fNyC38wEV011NFqTTh0B2XXH9FDpmm4jbbwF9D06kKtuaXTqwVPxj4ezMEOU9oLX3AKY3VXU6gCzzOhH3a8lHtIvrFG0-Gx8ZIZiiRBNM18WnhOJlw9Hkg9DU_8CDe8M5D40DdTlV3lgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/naya_foriraq/75927" target="_blank">📅 13:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 موقع هضبة العجل وثكنات أفيفيم، راميم (هونين)، راموت نفتالي ومعاليه غولاني بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/naya_foriraq/75926" target="_blank">📅 13:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV4Gn7gdADDrntpMQ24GBAd7p0pzyn1Lyqxh-8Y5T8i4GHpJ1kvWQGsViLqlRyT5wcQ8mf-yqtVy5jaIv7Aa0s_FqfMOvbC2IhUEKn7HZhji_TCJwj2DdOOv7JLPOZzhGiseiMcUVg13NxpFrBrTnN4vKv_uMFWx-IobkMzwy3itAmG9J_i8czhgE4tdiamRCNRg_I1hLbyMcZLX0LZZL_tEdNcHP19rhTACRhsqayhxfANcZQxhKvxsa0l28IqhXB5F2ghbFRu9hp1vq6r8JU_KfOKD9A003zekWjEUgCe7ypIjwJMMqVJRUnCJQtyxWJk9yQzQULeTR0scqIquoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
البحرية البريطانية:
وردت تقارير متعددة عن اقتراب زوارق صغيرة من سفن، كما شوهد زورق صغير كبير مزود بمحركين خارجيين يحمل سلالم وأسلحة.</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/naya_foriraq/75925" target="_blank">📅 13:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
‏
تايوان:
الصين نشرت أكثر من 100 سفينة حربية بالمياه الإقليمية.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/75924" target="_blank">📅 12:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم مستوطنات الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/75923" target="_blank">📅 12:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ed39e6b3.mp4?token=giMT83BJ1-IYUDyf_EN3szGurf657ZESAzSFE7zAXci2-jol8vCLkD2B7F04oZjt50nhdETT7X6NqbV3qyCOTIwMHzxND3UY9DkU7VtRzaAAN6dz7nuX3p88PtiQco3ju2RzeClpZysnCygeSnJAKWQ5wlJAYTsaO3umV-XdRzvr7vFz6bTH-xdRThWwtuGNzjwo_Ds4dEIFYi0kZn7vQkIwfMCaN4SYnKHeqv3Xp2TCB77oTOLpyUxE2W3wPYAWJYZdKe1Wh4usha_PC4_7dqmYAXvXZRDptUfeo-yhbqlpQCu20SLqoqOX11-pebJ6REd1LzFZDXg-sJGknJo8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ed39e6b3.mp4?token=giMT83BJ1-IYUDyf_EN3szGurf657ZESAzSFE7zAXci2-jol8vCLkD2B7F04oZjt50nhdETT7X6NqbV3qyCOTIwMHzxND3UY9DkU7VtRzaAAN6dz7nuX3p88PtiQco3ju2RzeClpZysnCygeSnJAKWQ5wlJAYTsaO3umV-XdRzvr7vFz6bTH-xdRThWwtuGNzjwo_Ds4dEIFYi0kZn7vQkIwfMCaN4SYnKHeqv3Xp2TCB77oTOLpyUxE2W3wPYAWJYZdKe1Wh4usha_PC4_7dqmYAXvXZRDptUfeo-yhbqlpQCu20SLqoqOX11-pebJ6REd1LzFZDXg-sJGknJo8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
ضمن الممارسات الوحشية الصهيونية..
قوات جيش الإحتلال الإسرائيلي تقدم على إعتقال عدد من الأطفال الفلسطينيين في رام الله.</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/75922" target="_blank">📅 12:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
المتحدث باسم هيئة الطيران المدني الإيراني:
لم تصدر هيئة الطيران المدني أي إشعار جديد (NOTAM). ننفي ماجاء في الإشعار الذي نُشر مؤخرًا على وسائل التواصل الإجتماعي. لازال وضع الطيران في البلاد كما هو، وتُسيّر الرحلات الجوية وفقًا للخطة الموضوعة.</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/75921" target="_blank">📅 11:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
رويترز:
بعد ثلاثة أشهر من حرب كان من المفترض أن تنتهي في ستة أسابيع بانتصار حاسم، أصبح ترامب عالقًا في المستنقع الإيراني، غير قادر على إيجاد مخرج يحفظ ماء وجهه أو توسيع نطاق الضربات.
على الرغم من الضربات العسكرية الأمريكية، لم تنهار إيران؛ ولا يزال سيطرتها المستمرة على مضيق هرمز - الذي يمر عبره خمس إمدادات النفط في العالم - تشكل أهم أداة ضغط لديها.
يقول المحللون إن الرئيس الذي يتباهى بالانتصارات يواجه الآن تحديًا قد يقوض مكانة أمريكا العالمية أكثر من أي صراع في العقود الأخيرة.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/75920" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIThtt07oLH2s3bSixpm4F0RIes5_0o_ClugmFij9o7D1wmhq0qraBNliQgQI5awr-fZu5BG8f85ss2yfJtDK3OM0h42QQZJrNs3HmSHJJiZeRi4PrE4dm4SwgPCUgGPoWqSsVIfSve67L5Wlp9zdVOfl6zA128_vbmhkERRcnNivdbm42-li60Lv_vfr37Jts80DTNVw6U6bZpO5qHiDObLdG-0vdZ4aeoBKSCkx4OwaJT7pM6yfXPfekzKhhIrHBfAgjza4pUsu-ao9ncLv8mK4LaYpaCu14C60Z8kqMGPDsBILOW2RW6QFoFyHYSf_ccGtMTHf4G5zfmqxYi8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   مسرور وارين بارزاني وسومو والزيدي في بغداد ..</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/75919" target="_blank">📅 11:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iC8BuEgfYrES0hh_UwnGB2KgukgO-PlO6Gj-jfAtO2Z4e4GWfDfgKSXBhYXFcbbvn1HsoFWK33GREdoycMRAEp5o9BW8dayw9qncvUfhnNMyI-56R11BgL7RqUH1ef78tw7iIgWB6V6jS0e-4_671HHejKE87SRC7-UiwUhjdOchVovYb968sLS1HRVqBIfk7AEDOZ4MMKN_QH5qtW2BvuRTKf0e9q94UFoGPHvRUTzgIPk42FJ6m8epxiDeCIQoQgsYxI_izDI_CdKfmDIJrD-kz8dRqrrPPGmZ9dSly6luV-A5m2Y7tY8whiAUu1j7yU-c1-LOKmJeyfFbJ8jG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YO6wNdXkUBU0XnZw-rv2Z4S3Igvn0LJQP_FQgB2SQFIWUPu56iP1jooH1Gc8zrRIr1ZUYvYdk2FqwaRZ8EFmB22sWTEI1-NTN00cBtgZb_G9F8XT4jJwDv7_JIqz8XMc0QkaCudIUnT_Waw2U9mi-lVgZElJgyx5rJjdQ7oaYc9vUnrMMPx9uSyWzUxLyDjcRT1fLjoC6QJ-f_PyOOrzKuMZaL0F1gxbEAYAoizr9L7BxTLnsmkUwzSJsT5Xs3FuEVeOq_LGBdh5WqwVCIrouc11Gpq-6yVpifv6qEVs58P3egXU2_WTrQMWRT_pkbkCw1G5gvzT1PQl-9GbVQEpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCQhGFq2cab7-xXxHrmTrO85J27R-o4JV_KwRn0mW7UHRQ_eod02BHs1EJm_hhnl3jifwKw60YEWDF7clZQvVe_t3fr4dYggkuzPHyfMJsfRdCurXBNc-mHm4N4NPblNUSoE9QxlUsAuDIjjcJwmJ8YH2uydDQGfbkizN0BuIADzRBSGgbBhn_7lKHC40yJwrlmktyH63F-Ki-okOnbhLXrqAHEeYm0MInIpvt4t8fQYjXabi1WaoLrItp9S7-zlZtr9cIEZBxtgoEpz6AYZpfMvR3QBUs-VkBnZBWp-Yuvis7kQlD3gCXSdcE6oDDIIOHE5ilUmARMNgniocNqhlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
تم رصد طائرة هليكوبتر من طراز MH-60S تابعة للبحرية الأمريكية تحمل نداء RESCU11 فوق خليج عمان. ‏قد تكون مهمة إنقاذ. (هذه المروحية تابعة لإحدى السفن الحربية المنتشرة في بحر العرب).</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75916" target="_blank">📅 09:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHFSp5UzkxhwCJ_P171BjxMRjEyj11UdiPlg-NzpYG9GO0sVyesVTlHp_DMqkoLUUnZdML0rjakfrzw91fdR2WdGccsbR_BREktxL3v8kcKkMX_gpZ_m5mtYo1TcYAUVNrflIpPUEkk-94iS3iVVfsYWokg_jNkTErLg-rSbvP5kRTC9DfwJgMW9XlHYUGjZeKtPlwKtBv0cAZ1jpypcvZPGPxEgzmA6R4e7vr1sNWjbKPczM6aHGM2vfyeADFCeHYEoPKD-FiMiP2yirFPldZ-QK4sPA6x_1Z8TFi2yHSWyX6-bJyan1zsTNb_gXGqQ-vlt64eteYSoUMyYn-GMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإحتلال الصهيوني يزعم إحباط محاولة إدخال سلاح وذخيرة إلى الأراضي الفلسطينية المحتلة من الحدود الشرقية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75915" target="_blank">📅 09:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
نيويورك بوست:
يُزعم أن محمد باقر السعدي، وهو مشتبه به عراقي مرتبط بـ "الحرس الثوري الإيراني"، خطط لاغتيال إيفانكا ترامب انتقامًا لمقتل قاسم سليماني في عام 2020. وتقول السلطات إنه كان لديه خرائط لمنزلها في فلوريدا وهدد عائلة ترامب عبر الإنترنت.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75914" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يهاجم كريات شمونة في الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75913" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الدفاع الإيرانية:
عدم احترام حقوق إيران سيؤدي إلى مزيد من الهزائم لترامب. ليس أمام ترامب خيار سوى قبول مطالب الشعب الإيراني واحترام حقوق بلادنا.في ساحة المعركة والدبلوماسية على حد سواء، يُعدّ تلبية مطالب الشعب الإيراني السبيل الوحيد للخروج من الحرب الثالثة المفروضة على العدو الأمريكي الصهيوني. كما يجب على ترامب، مع قبوله للمقترح الإيراني، أن يحرص على منع المزيد من الخسائر والتكاليف المترتبة على استمرار الحرب، سواء للشعب الأمريكي أو للمجتمع الدولي.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75912" target="_blank">📅 09:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWAXtc6-_fntkVRr5d_odux4j89-ypP8A_CY8UtpS_gne8GWB15eDqW90oDFo9vQ8oHHB6bdHoyX6F0q28dnrY2ZKET6wvi8OqxdOPQJ1Mwbq9gNUA_ScrV2Yvymbiy0xTYkaCqPZ7QEnRychx0sjGvRcwOBfAFGNWFGAa2-c_ftk-lVmzgvdjEZLHLMSUNAKgAZdbX02aIHet4IyF4VLr-GHOIPqY1NXFbkzVpnNFGXf7kWKVhNFOc2eU9kZSHqbLPRX5uVF4ejG-XkOxNu7iRIndENreuIOytT1wRTj9G0D1ANNJrT30pmQAwvHhr_uLdFnfIZ24tXTFCpwDI5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75911" target="_blank">📅 02:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لم يغادر الوفد الباكستاني ايران كما يبث إعلام العدو ؛ حاليا تنشر كمية هائلة من الأشاعات لجس نبض حركة الدفاع الجوي الإيراني و القوة الصاروخية .. حركة شبه طبيعية للطيران المدني في سماء العراق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/75910" target="_blank">📅 02:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q63k9Kt9UU3GGz_xGhFGnJhPMBQslVoBv7vDfJssppPZEnuuJH5sEo8c7bULV57cThoNKpkBbrK4QnngciyoqiPLCnEj1XEqSJcHC36HsZ5BCbQ93g5r8WHFLevhgf1G-_NPhEi7Md-B3CUc8vKzJxVxf4zR-crnBzcF5Wub-1Aa4smtKasBnJqNGeDDNthSWv-5KMwNyZDvTyT4NJV_Y6vtq9MkWMghlbt0gL6nyhtTlsGJTAUazreWhsdDca-Ol9rfoPHyq1Lr6TsHsCsbk9x9tsg6eSG-04LzUUsW7lpoNyb0NDnUCSFxDMnzFhVI55zsTXZ6XhCH0VZCYok56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنشط القوات الأميركية في سماء بادية السماوة جنوبي العراق بنشر طائرات إرضاع جوي الأمر الذي يشير الى وجود طيران حربي آخر في سماء العراق ..</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75909" target="_blank">📅 02:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نقابة البحريين العراقيين تطالب بتحرك حكومي عاجل لكشف مصير البحارة العراقيين المفقودين قرب المياه الكويتية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75908" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📰
وول ستريت جورنال:
أوقفت الولايات المتحدة مؤخرًا إصدار تأشيرات الدخول للمسافرين من جنوب السودان أو الكونغو أو أوغندا بعد تفشي فيروس إيبولا بسرعة كبيرة في وسط أفريقيا.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75907" target="_blank">📅 00:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1153e5630a.mp4?token=QL49tf47CGuSmAtFTuiLFicmiHnPQyEvE9TCcPfG9DuW8AMHr5q2SmLP8Vys-yYlfo9Jz1nLgi4OUEtJLf_t3zw95LztbRCI6izPW7nK1ZTY4YhMI0V8w9u0O6z98adkI2XbbNqaNu5_gNUDCZbeTcFeAphtHCw1UFc0fnmVviADXRorcHYPLYVwsdAEBH6cHIpkFagHZLTSRcPlV5TgXXBSGUe65yr4tSt94B1XM3o8GylnLvVDJ7DW_cKHPtbMywRdqU6qKjUeEgmT73tc6i1ekLS_MiPoErC11SlmKrMP9IGZCryH-_4uopfsrQXftoXQDpV2nnwyvennTOFkpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1153e5630a.mp4?token=QL49tf47CGuSmAtFTuiLFicmiHnPQyEvE9TCcPfG9DuW8AMHr5q2SmLP8Vys-yYlfo9Jz1nLgi4OUEtJLf_t3zw95LztbRCI6izPW7nK1ZTY4YhMI0V8w9u0O6z98adkI2XbbNqaNu5_gNUDCZbeTcFeAphtHCw1UFc0fnmVviADXRorcHYPLYVwsdAEBH6cHIpkFagHZLTSRcPlV5TgXXBSGUe65yr4tSt94B1XM3o8GylnLvVDJ7DW_cKHPtbMywRdqU6qKjUeEgmT73tc6i1ekLS_MiPoErC11SlmKrMP9IGZCryH-_4uopfsrQXftoXQDpV2nnwyvennTOFkpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب
: "قال ملك السعودية إننا الدولة الأكثر حرارة"،ولقد استخرجنا الكثير من النفط من فنزويلا، وقد دفعنا تكلفة الحرب أكثر من 25 مرة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75906" target="_blank">📅 23:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇮🇷
وول ستريت جورنال:
يسعى الوسطاء جاهدين للتوصل إلى اتفاق مؤقت بين إيران والولايات المتحدة لمنع شن ضربات أمريكية-إسرائيلية جديدة، يحذر المسؤولون من أنها قد تحدث في غضون أيام.
تحاول باكستان وقطر وغيرهما من اللاعبين الإقليميين سد الثغرات بشأن البرنامج النووي الإيراني، وتخفيف العقوبات، والأمن الإقليمي.
الهدف ليس اتفاقًا كاملًا، بل إطارًا مؤقتًا يمدد وقف إطلاق النار ويسمح باستمرار مفاوضات أوسع.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75905" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f688b7274.mp4?token=BVj5XXb49zcKfiAzYs2qO_BxrRb4vdDbxK3wdhORtPpD5hfGaD13KD9U7OHCKIMZbyfR30wqZchplJ925CPZAdH9ovnShGP9_OiLfgtyZ84dthRnKvh-KMHrvjNW4Y6v84fcQfk965tjmpqEiSBkngWxDks2cOmcj1nQ8tT9KH0zuMgGcBXB95NSnHKHgSv0bvHnnsrefbxvIxvcAvtOAlDEEs9mVEgsMoDwI_97USHEPb5btmK-bLcNFxwe7xhDu-5QlP7KHbpSjjGzBPOhN75Vhm96H4Fk2jQ04cMjKwQ0YuTkM4Fr6OGVzzjRz4ywByfNt4mOzDJj0EZZ1t5lGiep5b9ZsPIhDUKBQzBzWfHBcd_GApuV_CMWXm63TXAK2Q_i7KakS6KCslz_sdK3muSJ9LcwNm4X24hACloid84gvAHFSnEswrscVPBg1Be55VtTyXfwcopiCbDNkmHhFmWIWscKdUA-Wz1khQZRutN3fbkDrrtbRHrTzxAxynlCLRnIrCgHkPK5uGGfse9No3ezIErFvbXrdiPeoyIP8NygwY0yQ92Y5UXRU2qmaGdVXX8t67r0iDnjjtcDJRh8FaOaG-EsQYZcbVSh9fYzPKXWXW8by2Ok7eUwW2XdhYnfX_6GVe7WCLh4U1JJb6qXSKA12yUocFfWKfPJ1QaoTw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f688b7274.mp4?token=BVj5XXb49zcKfiAzYs2qO_BxrRb4vdDbxK3wdhORtPpD5hfGaD13KD9U7OHCKIMZbyfR30wqZchplJ925CPZAdH9ovnShGP9_OiLfgtyZ84dthRnKvh-KMHrvjNW4Y6v84fcQfk965tjmpqEiSBkngWxDks2cOmcj1nQ8tT9KH0zuMgGcBXB95NSnHKHgSv0bvHnnsrefbxvIxvcAvtOAlDEEs9mVEgsMoDwI_97USHEPb5btmK-bLcNFxwe7xhDu-5QlP7KHbpSjjGzBPOhN75Vhm96H4Fk2jQ04cMjKwQ0YuTkM4Fr6OGVzzjRz4ywByfNt4mOzDJj0EZZ1t5lGiep5b9ZsPIhDUKBQzBzWfHBcd_GApuV_CMWXm63TXAK2Q_i7KakS6KCslz_sdK3muSJ9LcwNm4X24hACloid84gvAHFSnEswrscVPBg1Be55VtTyXfwcopiCbDNkmHhFmWIWscKdUA-Wz1khQZRutN3fbkDrrtbRHrTzxAxynlCLRnIrCgHkPK5uGGfse9No3ezIErFvbXrdiPeoyIP8NygwY0yQ92Y5UXRU2qmaGdVXX8t67r0iDnjjtcDJRh8FaOaG-EsQYZcbVSh9fYzPKXWXW8by2Ok7eUwW2XdhYnfX_6GVe7WCLh4U1JJb6qXSKA12yUocFfWKfPJ1QaoTw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-05-2026
دبابة ميركافا تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75903" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي حول إيران: المفاوضات مرهقة للغاية والمسودات تنتقل ذهابا وإيابا يوميا دون إحراز تقدم كبير.  الرئيس الأمريكي شعر بإحباط متزايد خلال الأيام القليلة الماضية.  الرئيس طرح احتمال تنفيذ عملية عسكرية كبرى أخيرة وإعلان النصر وإنهاء الحرب.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/75902" target="_blank">📅 22:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🏴‍☠️
حدث أمني جديد يتعرض له جيش الإحتلال الصهيوني في بلدة الناقورة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75901" target="_blank">📅 22:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75900">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي حول إيران:
المفاوضات مرهقة للغاية والمسودات تنتقل ذهابا وإيابا يوميا دون إحراز تقدم كبير.
الرئيس الأمريكي شعر بإحباط متزايد خلال الأيام القليلة الماضية.
الرئيس طرح احتمال تنفيذ عملية عسكرية كبرى أخيرة وإعلان النصر وإنهاء الحرب.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75900" target="_blank">📅 22:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
حدث أمني في قاعدة بينساكولا الجوية البحرية بولاية فلوريدا الأمريكية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75899" target="_blank">📅 21:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2bT0hduIUFqbZRmeDQjE9vkW7fYmGujdW3f-6DVBWpfoXU3aUqPdpHrJU2B4Ic6VPeqZq332bI52xm4wzkE1-srrCiJECCLNOzGkdiVG-9t-e-PfTqpncqjNjW5fKcqTF9O-lwnVO3BhVJUzzR-qOXcRVa7D2jqeD4HxXMuGFXzTFxwtNay6QIyBvjkFvUkLTsH1dzL2Pz7ibPdbt6aUmdDN9DPYoGvNewaJTHONJWpoNiAj6PivFdLSLHHq-2C1NuXGEWyUUiIgEveImKAXQWnDAnYlYeXwrDweLptTP1ras3BnBvpFqm39G2Od0kZUkGEhQMS6vANk7tBirNyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMXAyoqcy96es39ps1XjbkjMTttAGNz4b9Tbdq44GzoNBSs0E1uRBL1Or75XxGvZFLURnYIKaYEtHiZxqMOwnLV32Dvl6WBpomOmzS-Re9d1CTwoDSIG6kEdXMY6pgl7hCDi75KpFmBEb6uEW1hlbpdzkl7UIYm_ffP2-nnE3Es62eBZbg3vTJ6UzwWCnwEbUzfMfXxHEJ2DiGAB8yakoJhsQhEYcmhlizsAWv66WypCxES-EeAhmbc_vnEt6pCzNwmZSsjrDiyCrUPAbfPL10b6ygT3_KIXSfD7twyR5dFlZ8jCL9m-YCRgtxe7cKyBNzFHXOEaokMwyeZMlZgIOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
سيتم اغتيال ترامب يوم الأحد المقبل، بالتزامن مع عيد الأضحى المبارك. وقد تم اختيار ثور يُدعى دونالد ترامب في بنغلاديش للاحتفال بهذا العيد الإسلامي. واشتهر هذا الجاموس الأبيض الأمهق بشبهه الكبير بالرئيس الأمريكي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/75896" target="_blank">📅 20:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
🏴‍☠️
أبناء نصرالله يتمكنون من إحراق دبابة ميركافا تابعة للجيش الصهيوني في بلدة مركبا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75895" target="_blank">📅 20:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
أمريكا تنهار من الداخل..
استقالة تولسي غابارد مديرة الاستخبارات الوطنية الأمريكية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75894" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: سقوط 6 إصابات في صفوف الجيش الإسرائيلي جراء استهدافهم بمسيرة انقضاضية في مرتفعات راميم بالقرب من الحدود مع لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75893" target="_blank">📅 19:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية الإغارة النارية التي نفذتها المقاومة الإسلامية بتاريخ
17-05-2026
على تموضعات جنود وآليات جيش العدو الإسرائيلي في بلدات الخيام، الطيبة، العديسة، دير سريان ودير ميماس جنوبيّ لبنان بالأسلحة الصاروخية وقذائف المدفعية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75892" target="_blank">📅 19:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لقد ضربنا إيران بشدة وهم يريدون بشدة التوصل لاتفاق.
لدينا أعظم جيش في العالم ونريد الحصول على ميزانية دفاع تصل إلى 1.5 تريليون دولار.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75891" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
نقل عدد من جنود الاحتلال المصابين بانفجار مسيرات حزب الله في المواقع العسكرية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75890" target="_blank">📅 19:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إصابة جندي إسرائيلي بجروح في البطن جراء انفجار مُحلّقة مفخخة استهدفت مستوطنة مسكافعام ضمن إصبع الجليل.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75889" target="_blank">📅 19:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
حزب الله: استهدف مجاهدو المقاومة الإسلاميّة ناقلة جند تابعة لجيش العدو الإسرائيلي في موقع الرّاهب بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75888" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇷🇺
بوتين: أوكرانيا قصفت سكنًا طلابيًا و15 شخصاً في عداد المفقودين ومقتل ستة أشخاص وإصابة 39 آخرين</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75887" target="_blank">📅 17:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات عنيفة تهز مستوطنة مرجليوت شمال الكيان جراء هجوم حزب الله</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75886" target="_blank">📅 17:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c738e132a0.mp4?token=hpWIHbHwq3NoZN0ibgCEsZUaU_o5bR2p2QBGivHD48RyxzR5Nfl48C-Zu11CEVLfgR_CjLAWF3u1-SD3qz7I-PdkpD60Iy5T4cqSNhTcnWu0RXZPrd4xIU0-VDPx1I6qfvUboEktDKDrsg_-TEIoy28oWBvTY8njJ4mCnwWttMcTkeZJfaUfkadw4J2tGUGGtiyM7-UMenp_aCYI4buRcU0Lo7zrMG7sTrjaUO5L_FEahGuL8WZqWiBsnJmeriABqguXWfE0-kC4qaKiuu626pX0sTqnt9O89QPmX7NqxkLI3EDK4IAxXTAwaGLWfDbLmiSCvD1RhdG2lx2rVuUh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c738e132a0.mp4?token=hpWIHbHwq3NoZN0ibgCEsZUaU_o5bR2p2QBGivHD48RyxzR5Nfl48C-Zu11CEVLfgR_CjLAWF3u1-SD3qz7I-PdkpD60Iy5T4cqSNhTcnWu0RXZPrd4xIU0-VDPx1I6qfvUboEktDKDrsg_-TEIoy28oWBvTY8njJ4mCnwWttMcTkeZJfaUfkadw4J2tGUGGtiyM7-UMenp_aCYI4buRcU0Lo7zrMG7sTrjaUO5L_FEahGuL8WZqWiBsnJmeriABqguXWfE0-kC4qaKiuu626pX0sTqnt9O89QPmX7NqxkLI3EDK4IAxXTAwaGLWfDbLmiSCvD1RhdG2lx2rVuUh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">البيت الأبيض ينشر: من المرجح أن يكون "تشكيل 4 أجسام طائرة مجهولة، إيران، 26 أغسطس 2022 فوق الماء [رمز النداء]" مستمدًا من مستشعر الأشعة تحت الحمراء على متن منصة عسكرية أمريكية تعمل ضمن منطقة مسؤولية القيادة المركزية الأمريكية في عام 2022.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75885" target="_blank">📅 17:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5999a11d7.mp4?token=kCrLgcCsSSi1s1pwFEWGCoQOZLdMX_JvzsSq-yghDpB1e2fB1AXR1eWyTg9USOBakKsuWgIDZq_BStygMKbFVZunmDQ0OH8QSwR5LzgFWm7HUs5whmgvxEFisiIV9V-eP70fMU-GV2uZwpCap0ILnbvNUoBeT5cqdhj5CDL89vFsX3qSyeARYBa9cbkNXAUZ-WU3NWZKIjib071Kb95GUMp2p2OFb-iIWJKgcdzo_eO1TBj9CZTZc0RckxlcwNQAveT-fZXW1FQodJwNpdo9_q8jm1AqQSTJIikwKHjsp9vens5BhvDYdSPAdBQPU9NMt6I2Y1Et-1P8OWeJNmdX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5999a11d7.mp4?token=kCrLgcCsSSi1s1pwFEWGCoQOZLdMX_JvzsSq-yghDpB1e2fB1AXR1eWyTg9USOBakKsuWgIDZq_BStygMKbFVZunmDQ0OH8QSwR5LzgFWm7HUs5whmgvxEFisiIV9V-eP70fMU-GV2uZwpCap0ILnbvNUoBeT5cqdhj5CDL89vFsX3qSyeARYBa9cbkNXAUZ-WU3NWZKIjib071Kb95GUMp2p2OFb-iIWJKgcdzo_eO1TBj9CZTZc0RckxlcwNQAveT-fZXW1FQodJwNpdo9_q8jm1AqQSTJIikwKHjsp9vens5BhvDYdSPAdBQPU9NMt6I2Y1Et-1P8OWeJNmdX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اندلاع اشتباكات عنيفة بين عصابات الجولاني وقبيلة شمر في اليعربية/تل كوجر - بمحافظة االحسكة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75884" target="_blank">📅 17:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB3hKlAIkHPNRyl9vKkvsTuYGLb2X8IbsXI2svhsPHDrBFXbozhVOQztV5jk_1sbaD3kQgsXt8WD0IZIqnnzVXKCsoJ06xf6g_W1MMTN91wO1iythLgOQP94t1-GrMeaiqJfv4ao3jSBIgbqcaGQr5LGDk_GbrGaM9oVzjzD0tFgcLXs_GZhExDp9ctsxcpAydb49EV-rNf0zgN7mLyq_ge8jMSODjUeOEtOYzj_QSivlqAPoyAMfOj2N1J7tS1AVEmezFGRjgp2H-4LCZaC5oLoDl_GBoYehu35JDD40Q_F-9hnGmwq2YW1nN_JMfPAXpUqI4Cnqb6H_JGnBnptgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
الناس أن توم تيليس، السيناتور الضعيف وغير الفعال من ولاية كارولاينا الشمالية العظيمة، وهي ولاية فزت بها، بما في ذلك الانتخابات التمهيدية، 6 مرات متتالية، لم تكن لديه الشجاعة لخوض غمار المنافسة في مجلس الشيوخ، والبقاء في منصبه، والترشح مرة أخرى، وهو أمر كان يرغب بشدة في القيام به. لقد وصفته بأنه "مُنتقد للتفاصيل"، دائمًا ما يُحارب الحزب الجمهوري، وأنا، في الغالب على أشياء لا تهم. عندما أخبرته أنني لن أدعمه، تحت أي ظرف من الظروف، لترشحه مرة أخرى، فالأمر يتطلب الكثير من العمل والدراما (لم يكن ليفوز على أي حال!)، انسحب على الفور من السباق وأعلن علنًا أنه سيتقاعد. قلت: "يا له من خبر رائع، كان ذلك سهلاً!" قالت وسائل الإعلام كم كان شجاعًا لمواجهتي، لكنه لم يكن شجاعًا، بل كان عكس ذلك تمامًا - لقد كان مُستسلمًا! الآن بإمكانه الاستمتاع كما يشاء لبضعة أشهر، برفقة بعض أصدقائه الجمهوريين المعتدلين، مُلحقين الضرر بالحزب الجمهوري. في النهاية، سيزداد الأمر قوةً وعظمةً وعظمةً أكثر من أي وقت مضى!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75883" target="_blank">📅 16:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📰
رويترز: ‏أفادت مصادر مطلعة بأن قطر أرسلت فريقاً تفاوضياً إلى طهران، بالتنسيق مع الولايات المتحدة، للمساعدة في التوصل إلى اتفاق لإنهاء الحرب مع إيران.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75882" target="_blank">📅 16:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37fac2bec7.mp4?token=TcZjy81O9MfwDlEgvFclaZ592oMIs8R-2hbQJXv89PQ59hng7wiFIiq1C4qzG8cCBuy1MjLRiGwibadoyZ7CEUg6TN_8ygLF_HPbtMxDGBu_SzdnzoFkob5U45HuBI0CkiEw4-L7gtBhDknWT5hoJBgZ5zTDF37qoYiEY5jpWOq0f29yXHm_DtijHz8T4ESdGo_E9rGRAlbQjvdlgbC9GOcGmhJ7rxvWH2PV_VpUPjGg-c7XlmiYNnOshPfMnW_FvQLhXUUkzty0ZtldpIIXPU1lznlVDgKxH--gMXwprKoyRFTQ7qDKRJUJnc-sKVVYNjxpRatoeWk4pKPbvniDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37fac2bec7.mp4?token=TcZjy81O9MfwDlEgvFclaZ592oMIs8R-2hbQJXv89PQ59hng7wiFIiq1C4qzG8cCBuy1MjLRiGwibadoyZ7CEUg6TN_8ygLF_HPbtMxDGBu_SzdnzoFkob5U45HuBI0CkiEw4-L7gtBhDknWT5hoJBgZ5zTDF37qoYiEY5jpWOq0f29yXHm_DtijHz8T4ESdGo_E9rGRAlbQjvdlgbC9GOcGmhJ7rxvWH2PV_VpUPjGg-c7XlmiYNnOshPfMnW_FvQLhXUUkzty0ZtldpIIXPU1lznlVDgKxH--gMXwprKoyRFTQ7qDKRJUJnc-sKVVYNjxpRatoeWk4pKPbvniDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
⚔️
جيش الاحتلال يعلن تعرض بعض مواقعه العسكرية لقصف بطائرات حزب الله المسيرة شمال الكيان ويصفه بالحدث الصعب جداً.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75881" target="_blank">📅 16:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1b6d1af0.mp4?token=W2OfUv4Pm_27vCo26hJ1lY3v9oYXs5sSZMH8tOqQALSrClWNrEFGZdzZl7NwzX4a4NZHXfhbSLoy77HUCHOKfRn7hb4i-HmqlXqQqmlV12ybv9cETygpCWllPsNaoU2Gkdv_qHAoCETF19oz2VG4rWVVXEuzMtW5RNIdLyfzZn3xFkKAMI-Cu3SI63gc113MFZQYjXxVpr9QuVzzw8PcrNT-K5dvK9zyHIGus-0CrsLT5joZuDI6zGYOztVBzAq5fXKjiDtSyIWlupkuOzEByNY8L_wyFpS28D75G0GO6ttCbV-sPFgVlK4vQHkzE1EKnls7kPdc84h1mupNLVt0BwzqkMA497rx8KRfbBFvcZj72RVkLsOsprBsAvL_oODxkqb9Ovqb1VWYa8WVDFSHlmGMS4sY6egsqDlqhvDBbqK-HL54M5xinI19hhK4PBIw9y4lNnZC9JlspMKJTOyG0Q2TRtTNapNcwoxfAb-3T6hR02NPf_fNtPJiENbzI6ZgOgI5ACxPKWyRcpV5se5EgY-cfURgnLX5ur2zLauYKpI8IMPpC4nFbkNbARjZigtFy3FZQ_4xkfBeG_Q-9vvpAf1dJbtPViTgU4OnxGgGtEs7JugONHVaR112yRtMs1wkMo8RwuJeUJBwJGJCrRJF52U2TVu85fmnE9CUYt_spTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1b6d1af0.mp4?token=W2OfUv4Pm_27vCo26hJ1lY3v9oYXs5sSZMH8tOqQALSrClWNrEFGZdzZl7NwzX4a4NZHXfhbSLoy77HUCHOKfRn7hb4i-HmqlXqQqmlV12ybv9cETygpCWllPsNaoU2Gkdv_qHAoCETF19oz2VG4rWVVXEuzMtW5RNIdLyfzZn3xFkKAMI-Cu3SI63gc113MFZQYjXxVpr9QuVzzw8PcrNT-K5dvK9zyHIGus-0CrsLT5joZuDI6zGYOztVBzAq5fXKjiDtSyIWlupkuOzEByNY8L_wyFpS28D75G0GO6ttCbV-sPFgVlK4vQHkzE1EKnls7kPdc84h1mupNLVt0BwzqkMA497rx8KRfbBFvcZj72RVkLsOsprBsAvL_oODxkqb9Ovqb1VWYa8WVDFSHlmGMS4sY6egsqDlqhvDBbqK-HL54M5xinI19hhK4PBIw9y4lNnZC9JlspMKJTOyG0Q2TRtTNapNcwoxfAb-3T6hR02NPf_fNtPJiENbzI6ZgOgI5ACxPKWyRcpV5se5EgY-cfURgnLX5ur2zLauYKpI8IMPpC4nFbkNbARjZigtFy3FZQ_4xkfBeG_Q-9vvpAf1dJbtPViTgU4OnxGgGtEs7JugONHVaR112yRtMs1wkMo8RwuJeUJBwJGJCrRJF52U2TVu85fmnE9CUYt_spTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 12-05-2026 آلية "نميرا" تابعة لجيش العدو الإسرائيلي في بلدة حولا جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75880" target="_blank">📅 16:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
⚔️
جيش الاحتلال يعلن تعرض بعض مواقعه العسكرية لقصف بطائرات حزب الله المسيرة شمال الكيان ويصفه بالحدث الصعب جداً.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75879" target="_blank">📅 16:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
🇮🇷
رئيس الوفد الإيراني المفاوض محمد باقر قاليباف يصدر قراراً بتعيين اسماعيل بقائي متحدثاً باسم الوفد المفاوض</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75877" target="_blank">📅 15:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🐻
روسيا تعارض تكرار أي عدوان مسلح ولا يوجد أي مبرر قانوني لاستخدام القوة ضد المنشآت المدنية في إيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75876" target="_blank">📅 15:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇩🇪
🇺🇦
وزير خارجية ألمانيا: يجب ضمان استمرار دعم أوكرانيا بغض النظر عن أميركا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75875" target="_blank">📅 15:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
الحشد الشعبي: وفاءً للعهد وتقديراً لتضحياتهم، وزّعت محافظة المثنى، وبالتنسيق مع هيئة الحشد الشعبي، الوجبة الأولى من قطع الأراضي السكنية لمنتسبي الحشد الشعبي</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75874" target="_blank">📅 14:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7066cdb1d3.mp4?token=MMuJAK8pnxjX_WRzZx8_XjC6dLilypNTNuen8zQ_go-eYOv5h1MgV_Q0yVpkpWF6dRHvduhRzKG9x6wj3XPo1xBaPZYAVKA1jPs2dSUnbk7ItSIbdi6_IvZU0UNRhntMqCZHy6UZJxxGBwc25Othio17uRDTzGHSJZMPsqvZ-7MqQh5w0sX05KDO7_SeqXe2Y_jg1SqB2phaOk3z9A-wpuI7FNRSM5xzos_DE_gTwzyvjcvtNo7W6MChISOFjEz6Uc6_yRoncxt1koSffGM5OYRSzBPM44Z3ydsb1PjI4Xne7jwVtavxymWbaovlr9dX-65TB16VEi9K1TE0uZptew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7066cdb1d3.mp4?token=MMuJAK8pnxjX_WRzZx8_XjC6dLilypNTNuen8zQ_go-eYOv5h1MgV_Q0yVpkpWF6dRHvduhRzKG9x6wj3XPo1xBaPZYAVKA1jPs2dSUnbk7ItSIbdi6_IvZU0UNRhntMqCZHy6UZJxxGBwc25Othio17uRDTzGHSJZMPsqvZ-7MqQh5w0sX05KDO7_SeqXe2Y_jg1SqB2phaOk3z9A-wpuI7FNRSM5xzos_DE_gTwzyvjcvtNo7W6MChISOFjEz6Uc6_yRoncxt1koSffGM5OYRSzBPM44Z3ydsb1PjI4Xne7jwVtavxymWbaovlr9dX-65TB16VEi9K1TE0uZptew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
‏لحظة استهداف جيش الاحتلال الصهيوني للمسعفين في بلدة دير قانون النهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75873" target="_blank">📅 14:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke2i61nE1OEj4dFUCW9LVlA_yUwFYzSjUmNuH8hLl8rpx3H2wqrkiF_zCCl8AW_kgE7n-Wu72RzWVLOy2ZnFfeqK1T2IBcDyVp4kDlWhe_rPEFSnrzMshFx8r8tScdSi3lqRf47txRqUiGyGq85w0Mo9sBDt_CQ6ziZBE2AtlebNyeeEopMnupKavGeg-bRgF_eLiYSps0WyfKf96nMtYFhf_IC-KGRuFcCOnx3_IdR1BU4UT2wtalnGiG99F5KsS-zMzRG-2BM08RKDXmXbXtNeycgMZ73TMlO6gNyMRy_mqsjeB6ZwVvkoaf1KuzLu2-bIYQZ-Nihkau1_R8y4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي رداً على تصريحات الرئيس الألماني الأخيرة:
سيدي الرئيس، صحيح أن الأزمة الحالية التي تواجه منطقتنا والعالم هي نتيجة مباشرة لانسحاب الولايات المتحدة غير القانوني والتعسفي من الاتفاق النووي في مايو 2018؛
صحيح أيضاً أنه كان من الممكن بل من الواجب تجنب هذه الحرب المفروضة؛
ومع ذلك، فإن ميثاق الأمم المتحدة لا يعترف بمفهوم "الحرب الضرورية" الذي يمنح الدول الحق في استخدام القوة ضد دولة ذات سيادة أخرى بناءً على قرارات تعسفية من جانب المعتدين.
لا يمكن التقليل من شأن الهجوم الأمريكي الإسرائيلي على إيران أو إعادة تفسيره على أنه مجرد "حرب غير ضرورية". لقد كان انتهاكًا واضحًا وصريحًا للمادة 2، الفقرة 4 من ميثاق الأمم المتحدة - عمل عدواني واضح ضد دولة ذات سيادة.
أي دولة تحترم سيادة القانون وميثاق الأمم المتحدة يجب أن تدين بشكل قاطع هذا العمل العدواني وأن تحاسب المسؤولين عنه.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75872" target="_blank">📅 14:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">إعلام سعودي:المجلس الأوروبي يوسع عقوباته على إيران لتضم أفرادا وكيانات متهمة بتهديد الملاحة في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75871" target="_blank">📅 13:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇱🇧
كتلة حزب الله في البرلمان اللبناني:
المطلوب موقف واضح من السلطة اللبنانية لحماية مؤسساتها من التدخل الأمريكي
ندين فرض عقوبات على نواب بالكتلة ومسؤولين من حركة أمل وحزب الله وضباط في الجيش
ندين فرض أميركا عقوبات على ضباط بالجيش والأمن العام وعلى السفير الإيراني في لبنان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75870" target="_blank">📅 13:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بمسيّراتٍ انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75869" target="_blank">📅 13:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇬🇧
وزيرة الخارجية البريطانية:
من المخزي أن إيران تحاول اختطاف الاقتصاد العالمي بأكمله عبر منع حركة الشحن الدولي</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75867" target="_blank">📅 12:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزير الخارجية الأمريكي: هناك بعض التقدم على صعيد المفاوضات مع إيران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75866" target="_blank">📅 11:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزير الخارجية الأمريكي: هناك بعض التقدم على صعيد المفاوضات مع إيران</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75865" target="_blank">📅 11:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اعلام خليجي:
- مسودة الاتفاق المحتمل بين ايران والولايات المتحدة تنص على وقف فوري وشامل وغير مشروط للنار على جميع الجبهات
- المسودة تشمل الالتزام بعدم استهداف البنية العسكرية والمدنية والاقتصادية
- مسودة الاتفاق بين واشنطن وطهران تتضمن وقف العمليات العسكرية ووقف الحرب الإعلامية
- بدء المفاوضات بشأن القضايا العالقة خلال 7 أيام
- المسودة تتضمن رفع تدريجي للعقوبات الأمريكية مقابل التزام إيران ببنود الاتفاق
- احترام السيادة والسلامة الإقليمية وعدم التدخل بالشؤون الداخلية
- ضمان حرية الملاحة في الخليج ومضيق هرمز وبحر عُمان
- إنشاء آلية مشتركة للمراقبة وحل النزاعات</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75864" target="_blank">📅 11:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh57sbd0FmRD9gxYH3r4ljjaTJqJAjArea_eFCizUkQjbrHmqWMXA1-pyuMHE_RSI-NMCpN82DL2NcbORzAk0-gZ1CW9My8Y02Cjh5MLpaJR5xQoRG_6r52dJElGvgDdK2qxLhKtKmIp3dumxRf-QjLLigAMu-C-PDpIm8LjBRW1VHOfISEv0Y_ifSyK1MSKTYXNi7xFsg5dzLEY0NJUyr7KaCO6lQR1YsjtkFsxybbZVYG3gZZ2tqvhAy2OrmOaOyvmqROEBoA4ypzFufVt0VrGpSZlcU2vOBPhBZHmOt96fXGPYH35LdAw664o5Fhpz6oG2IdxtxvGvKTJjyHoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
وزيرة الخارجية الكندية:
لقد تلقيت للتو معلومات من مسؤوليي تتضمن تفاصيل عن الانتهاكات المروعة التي تعرض لها الكنديون الذين تم احتجازهم في إسرائيل.
‏وصل هؤلاء الكنديون الآن إلى تركيا. ويعمل مسؤولو الشؤون القنصلية التابعون لوزارة الخارجية على أرض تركيا على ضمان حصولهم على الرعاية الطبية العاجلة اللازمة لكي يتمكنوا من العودة إلى ديارهم في أسرع وقت ممكن.
‏تدين كندا بشدة سوء المعاملة الجسيمة التي يتعرض لها الكنديون في إسرائيل. يجب محاسبة المسؤولين عن هذا الانتهاك الفادح. وسنواصل تقديم المزيد من المعلومات حال توفرها.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75863" target="_blank">📅 11:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بلاغ عن واقعة على بعد 98 ميلا بحريا شمالي سقطرى باليمن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75862" target="_blank">📅 10:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بلاغ عن واقعة على بعد 98 ميلا بحريا شمالي سقطرى باليمن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75861" target="_blank">📅 10:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
🇨🇳
وزارة خارجية باكستان:
الصين قدمت بالتعاون معنا مبادرة من 5 بنود. رئيس الوزراء سيبحث في زيارته للصين غدا مبادرة مشتركة لإنهاء الحرب.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75860" target="_blank">📅 10:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات تهز ابو ظبي ..</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75859" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صحيفة وول ستريت جورنال : وزارة العدل الأمريكية قد بدأت تحقيقاً في استخدام إيران لمنصة باينانس للتحايل المحتمل على العقوبات.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75858" target="_blank">📅 09:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6kbnWe7Htam3YTW7zBuol4xZN5ghd_uxMWhejQuy7djzYnI5oxkFlsUTPOGu7LUK0AqsVPK3IsNO4ZMy8xQOKnzzjZDY1TAeYkszzYFC2HzRycKalfXR1KQFtmaTEjN-6cjS5iPOLkTD1sYPvz0iCt0EaZvolS56aA9d5rtvaevWo5zoM4WTpSUI_ed_Ktm0l-GRaOI3JWqDhQsCxnSO1qVUa_7yANWGaj7NANemQF3_46VAtRCOI5eA892i1abQAtPuiED5DEL41qGH_zvnEVHAevDuuqkdfAI7vEvTwQNeNGlkVM9tY1J6piQFH42Lv2Eb5o1AOd35s9nRS_wRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارة الحج والعمرة السعودية تحذف منشورًا أثار جدلًا واسعًا بعد تضمنه عبارات وُصفت بالرومانسية وغير المناسبة لطبيعة الحساب ومتابعين يطالبون بازالة ادمن حساب موسم الرياض من حساب وزارة الحج والعمرة لكي لا تحدث اخطاء هكذا مستقبلا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75857" target="_blank">📅 09:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسؤول امريكي للقناة 13 العبرية:
لقد تجاوز الإيرانيون جميع الجداول الزمنية التي وضعتها أجهزة الاستخبارات في سرعة التعافي من الضربات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75856" target="_blank">📅 09:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بلومبرغ عن شركة رابيدان إينرجي:
استمرار إغلاق هرمز حتى أغسطس يزيد من خطر ركود اقتصادي يقترب من حجم ركود 2008.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75855" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
الشركة العامة لموانئ العراق:
تعلن الشركة العامة لموانئ العراق استنفار جميع كوادرها في قسم السيطرة البحرية ومركز البحث والإنقاذ ضمن حدود المياه الإقليمية العراقية، وذلك عقب ورود معلومات بشأن فقدان سفينتين، مؤكدة أن أقسامها البحرية لم تتلق أي نداء استغاثة من السفينتين (Bridge 1) و(Bridge 2) اللتين ترفعان العلم البوليفي.
وأوضحت الشركة أنها تلقت رسائل إلكترونية من الجهات الامنية في عدد من موانئ حوض الخليج العربي، ومن مالكي السفينتين، تضمنت طلب تزويدها بأية معلومات تتعلق بالسفينتين المذكورتين، وذلك بسبب فقدان الاتصال مع طاقميهما وصعوبة التواصل معهما خلال الفترة الماضية.
وبينت الشركة العامة لموانئ العراق أن السفينتين لم تدخلا المياه العراقية، كما أن الأقسام البحرية المختصة، بما فيها السيطرة البحرية  ومركز البحث والانقاذ ، لم تتلق أي اتصال أو نداء استغاثة من طاقمي السفينتين، ولا تتوفر لديها أية معلومات عن موقعهما الحالي.
وأكدت الشركة العامة لموانئ العراق أن عمليات المتابعة مستمرة عبر أنظمة التتبع الإلكتروني بالأقمار الاصطناعية، وبالتنسيق مع إدارات البحث والإنقاذ في دول المنطقة، وسيتم الإعلان عن أي معلومات أو مستجدات فور ورودها.
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75854" target="_blank">📅 00:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekIQa7aV9CukW8dNyW6DaxPT2IEDcZwtidcX5ZbQolzG1ZJg3n_Jk0tURg5dDoN61Wwrc_y-ftCx-cEzbUSPBwXG2A5JgAKFi15ub4ifSd_dtqHNj3uOefiqc7TWHjsLxzIjFtg-uumDG8L7iE0I2OEks4lXm6Rk2P-VZQeKTiHZLWSVUSxAGZmG3U9xycLAjb2D9CH7jPnVPCstdvG6PvKOXVi3REawecdskfvGEbVfV7bjzyB9Jdo0LdIA5hUHCqtJBPUPzwoP_4AIPoUr_eJ2U-Y1zAxKZqkPhxjWMgMPJSyMeb2DQrOlrTDrftH32aVPamrhoP-NqODdnTF5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b338d82e3.mp4?token=eXyY9duMHxi9PWniX3lzyzHXaD6BQrwmsi2ZBKG6nu7L06wIpLOrNrqomMQ4XK2XMidXOEeCMYHlQW96lBfN28JvkG8uQJKZMLGAm2DcabfQuv3XnQ28U-bHoyT6hz9jpeu_0Q-Q-FGqrMgmw9PFPhA1zeumeXzCnl6f-SE_G0H9ppd0MA2Jutw3JjvU4HFyTMniP-QllhtKOO8i80Qfve6_ulInhNtuI4cO2Ke-g7nQgD9F2yEdY5i8v0AmgzJWF3UDj_M5pS9G3AylVMbN5A_BBf8kPYee3dr_Jr6iQCWahZqEE1_FBHCbmXWCMadpREEA8dlLXd3NL6piJ8D3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b338d82e3.mp4?token=eXyY9duMHxi9PWniX3lzyzHXaD6BQrwmsi2ZBKG6nu7L06wIpLOrNrqomMQ4XK2XMidXOEeCMYHlQW96lBfN28JvkG8uQJKZMLGAm2DcabfQuv3XnQ28U-bHoyT6hz9jpeu_0Q-Q-FGqrMgmw9PFPhA1zeumeXzCnl6f-SE_G0H9ppd0MA2Jutw3JjvU4HFyTMniP-QllhtKOO8i80Qfve6_ulInhNtuI4cO2Ke-g7nQgD9F2yEdY5i8v0AmgzJWF3UDj_M5pS9G3AylVMbN5A_BBf8kPYee3dr_Jr6iQCWahZqEE1_FBHCbmXWCMadpREEA8dlLXd3NL6piJ8D3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مواطنة جرينلاندية تهتف ضد مبعوث ترامب إلى جرينلاند "جيف لاندري" وتدعوه إلى ترك بلدها والعودة إلى منزله.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75852" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9Zmdjz2rtdWH6HfXQudTTbibqGdi8w3DnG24KSTVyDXyN94mgmR_Zwr0Svf_FZ6YPeq23R06j4olaPOdIrfAOFxvoRLQrs6gXM_8-yMbGxsdfambLENeslsJNd-mvGcrT39_BdP_pnAMl-yJHVgoP08zlGQW2ZpPHyF3jYdIRbcTnVx6ndn5AE4z4eQbnlS6C-huMq4S42ADeU1QUcQFv5zZPaQhuHi2Td0z019XszjZPeQ8h9shVgHnnLk63yLSnv87rraVpJl4kOGFx3lJ7m97lIE1kZVhp72-boQZLSanQXAvixgwSEpsY5w8umfs-YclZyAvc4PqRruupF6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
"بناءً على فوز الرئيس الحالي لبولندا، كارول ناووركي، الذي تشرفتُ بتأييده، وعلاقتنا به، يسرني أن أعلن أن الولايات المتحدة سترسل 5000 جندي إضافي إلى بولندا. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75851" target="_blank">📅 23:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
حكومة آل خليفة المتصهينة تأمر بحبس أكثر من 40 عالماً ورجل دين شيعي بارز في البحرين لمدة 60 يوماً على ذمة التحقيق، بالتزامن مع تجميد حساباتهم المصرفية، في خطوة تُعد استهدافاً لأسرهم وتصعيداً جديداً في سياسة التضييق والمعاقبة الجماعية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75850" target="_blank">📅 23:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75849">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭐️
دوي إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75849" target="_blank">📅 22:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75848">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "إسماعيل كوثري":
إذا استخدمت الإمارات العربية المتحدة المواقع التي وفرتها الولايات المتحدة ضدنا، فسوف نطلق عليها صواريخنا بكل تأكيد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75848" target="_blank">📅 22:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75847">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🇺🇸
بيان صادر عن حزب الله ردًا على العقوبات الأميركية:
إنّ ما صدر عن وزارتَي الخارجيّة والخزانة الأميركيتين من عقوبات طالت نوّابًا لبنانيّين منتخبين من الشعب، وضبّاطًا في الجيش والأمن العام، ومسؤولين في حزب الله وحركة أمل، هو محاولة ترهيب أميركيّة للشعب اللبناني الحر من أجل تدعيم العدوان الصهيوني على بلدنا، وإعطائه جرعة سياسيّة وهميّة بعد فشل جرائمه في ثني اللبنانيّين عن ممارسة حقّهم المشروع في المقاومة دفاعًا عن وطنهم.
إنّ التهمة التي ساقتها الإدارة الأميركيّة ضد نوّابنا ومسؤولينا هي رفض نزع سلاح المقاومة والتصدّي لمشاريع الاستسلام التي تحاول الإدارة الأميركيّة جرّ بلدنا إليها لمصلحة الكيان الصهيوني، وهذه التهمة تطال غالبيّة الشعب المتمسّك بالمقاومة والرافض للاستسلام. وهذه العقوبات هي وسام شرف على صدر المشمولين بها، وتأكيد إضافي على صوابيّة خيارنا، وهي في مفاعيلها لا تساوي الحبر الذي كُتبت به، ولن يكون لها أي تأثير عملي على خياراتنا وعلى مواصلة عمل الإخوة والمسؤولين في إطار خدمة شعبهم والدفاع عن مصالحه وسيادته.
أمّا استهداف القرار الضبّاط اللبنانيّين عشيّة اللقاءات في البنتاغون، فهي محاولة مكشوفة لترهيب مؤسساتنا الأمنيّة الرسميّة وإخضاع الدولة لشروط الوصاية الأميركيّة، وهذا القرار برسم من يدّعون صداقتهم للولايات المتحدة التي تسعى لتقويض المؤسّسات الوطنيّة. وعلى السلطة اللبنانية أن تدافع عن مؤسساتها الدستورية والأمنية والعسكرية، حفاظاً على السيادة الوطنية وكرامة لبنان واللبنانيين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75847" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سوالف الگهوة
مسرور وارين بارزاني وسومو والزيدي في بغداد ..</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75846" target="_blank">📅 22:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75845">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن على استعداد للتضحية بكل ما أوتينا من أجل شرف إيران وعزتها، ولا نخشى الشهادة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75845" target="_blank">📅 22:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75844">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭐️
يديعوت أحرونوت:
🇮🇷
🏴‍☠️
صور الأقمار الاصطناعية تظهر تضرر قاعدة "رمات دافيد" وإصابات محتملة في قاعدة "نيفاتيم" وأخرى تابعة للوحدة 82000 وقواعد إضافية جراء القصف الإيراني.
🌟
🏴‍☠️
تُظهر صور الأقمار الصناعية حريقًا هائلًا نشب في معسكر "شمشون" قرب طبريا بدءًا من 10 مارس/آذار، وهو اليوم الذي أعلن فيه حزب الله عن هجومه على الموقع باستخدام سرب من الطائرات المسيّرة. بحسب تحليل الصور، استمر الحريق لعدة أيام، وامتد على مساحة تقارب 200 متر داخل القاعدة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75844" target="_blank">📅 22:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_GkSCRXxcmaeyB36xtgITLE1dKcHFz0VG4eyvBzltwgJMoFNZvet0H6F9Siz2Wsp0L0IeIv4udSCKGPNEo1nxTBsDRT_FPdUDCykViv-E-tSHU4-XTXVDKbsS5VHqcZapai2_3sppPChFjDO2RkJXAmFSLsf2ZVcQyf754F2-GWAycc0TlyX2Uf8a4Imgt1l2AqiCsgjjGWVyE-UGAim5sj1ktsj-IU6HiS2CpBhP-AHgu6ukBNvK6-Gp7oTgdmDwlojGfIoYkdEuowFfG4b0BBgf9MSyd6vmb1hTXDoRXMq8S9Q7Ba7eYU5FedwoKi6Oia9oaWgZ_QVF6Cz7ZDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
شكرا لتروي نيلز العظيم على القتال من أجل مواطني شرق فلسطين، وسلامة السكك الحديدية، وجدول أعمالي. أدعو الجمهوريين في لجنة النقل إلى دعم تعديل قانون سلامة السكك الحديدية، الذي سيتم التصويت عليه قريبا جدا. لقد أيدت مشروع القانون منذ عام 2023، ونحن بحاجة إلى إنجازه! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75843" target="_blank">📅 22:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
🌟
بلومبرغ:
‏دمرت إيران أكثر من عشرين طائرة بدون طيار من طراز MQ-9 Reaper التي تشغلها القوات الأمريكية منذ بداية الحرب، وهي خسارة كبيرة بقيمة تقارب مليار دولار تمثل 20% من مخزون البنتاغون قبل الحرب لهذا النظام غير المأهول الذي يصعب استبداله.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75842" target="_blank">📅 22:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCUl426-WvaWucEs8qdLN9pf0BnMkrU50yoKNyx1DZrNjPfs0a72Y7lpWp1TaPb0nhv1ELLy5quNiAcKPt1c_Kf7QMv9vPLcqVOzhifxp86mF3RpKMkeWuL2PP1PMjK9tC3MctDW0S37nqbROt5vu0Wnky9bkvPkW_i82AStJdWwykSG59kdPA2Mn0O_KEw84yibaKFt-Sh1HAt3OOhYaj4UeRBLT30Xfp0e_KxPRUikPmC-fK4ZAsu49vG18nbBXXTFhnVb9FpuobrOmVa9LmDfDHWIm4KHE7zO0vBtcq8_MxxUlwt4jzZDgO1tD7mRRO8i79bhJUxM5rzYsEPRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
برعاية وزير النقل السيد وهب الحسني..
وزارة النقل توقع إتفاق تعاون ونقل رسمي بين الخطوط الجوية العراقية والإتحاد العراقي لكرة القدم لدعم المنتخبات الوطنية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75841" target="_blank">📅 21:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
رئيس المجلس السياسي الأعلى اليمني "مهدي المشاط":
أثبتت أحداث السنوات الماضية والراهنة في غزة واليمن ولبنان والعراق وإيران أن العدو الصهيوني رغم جبروته العسكري ليس بقوة لا تقهر.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75840" target="_blank">📅 21:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭐️
وسائل إعلام كردية:
محاولة إغتيال تطال "خورشيد هركي" في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75839" target="_blank">📅 21:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
ترامب: لا يمكن لإيران أن تحتفظ بيورانيومها المخصب للغاية. بمجرد أن نحصل عليه، سنقوم على الأرجح بتدميره. نحن لا نريده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75838" target="_blank">📅 20:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75837">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴‍☠️
طيران مسير من لبنان يهاجم كريات شمونة ومحيطها وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75837" target="_blank">📅 20:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
ترامب: لا يمكن لإيران أن تحتفظ بيورانيومها المخصب للغاية. بمجرد أن نحصل عليه، سنقوم على الأرجح بتدميره. نحن لا نريده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75836" target="_blank">📅 19:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75835">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc2cb4582.mp4?token=T_mUPNWKRKPh14N1XMFJ0rNrsBpkckS9nCnertFVU4seXXIyY5oJpBPppgbimEvgQi-U5FPDEU3n0ketpIWo7lwCHB65APEWTvghG9A56roV7poDj-7Jhtrmv0JkGGaGgRfJ8zNgqq6dBPyKSxMSDziaywRihLs6ijelzNhzxGgWRdFroS_tgO_WAatiGkWsmfTjBD9Hpw6dIuW7BeRk68APpRe8EdeRoFvkdAEjcgC1SR8bT4_OYE03payksV4Oo6phXQ11EtbfABOKKbU2VMIjwfs87BH9b_Pc6pz3Bzf2Nmb5ONr8SovadyIVAm3l5ss3fEqDhqfQ3sVzlcjxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc2cb4582.mp4?token=T_mUPNWKRKPh14N1XMFJ0rNrsBpkckS9nCnertFVU4seXXIyY5oJpBPppgbimEvgQi-U5FPDEU3n0ketpIWo7lwCHB65APEWTvghG9A56roV7poDj-7Jhtrmv0JkGGaGgRfJ8zNgqq6dBPyKSxMSDziaywRihLs6ijelzNhzxGgWRdFroS_tgO_WAatiGkWsmfTjBD9Hpw6dIuW7BeRk68APpRe8EdeRoFvkdAEjcgC1SR8bT4_OYE03payksV4Oo6phXQ11EtbfABOKKbU2VMIjwfs87BH9b_Pc6pz3Bzf2Nmb5ONr8SovadyIVAm3l5ss3fEqDhqfQ3sVzlcjxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
ترامب: نحن نتفاوض بشأن إيران وسنحقق هدفنا مهما كانت الطرق.  نحن ندرس رسوم العبور في هرمز، ولدينا السيطرة التامة على المضيق.  أريد مضيق هرمز مفتوحًا ومجانيًا دون رسوم.  نملك تكنولوجيا طائرات مسيرة متطورة لضرب إيران.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75835" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7053f45077.mp4?token=NJzw4NEh5fH3lczGTU_RN6DyCd50Zlb4c1pxjCx2KHwuRqNevI32cJQlvdCdfGUwCyo2m-JhYyDhA0ymlNbBaViL63RCla2L9NH_3M4VdZo_0EExYHI9uX9g8YNDqRLn16iOmtcwv6tR10C7otxuQqQJTWZAgF_wIpVej8ss7KnheVE691vIOxqD12uZ32QToXYGFktBXvRz9WSydAFq29xu1rtY2L9sEyy4tdu1ZAUQZJQjFLL7HcJovINVdgC_E_zDDSFRJg-3ndE7BEwcQNrf1N-CA3f-rnTNQhwrGPdbbFsMbt8ZiAA-MszndCAubvOG0mtsQwES7A5ZMEahBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7053f45077.mp4?token=NJzw4NEh5fH3lczGTU_RN6DyCd50Zlb4c1pxjCx2KHwuRqNevI32cJQlvdCdfGUwCyo2m-JhYyDhA0ymlNbBaViL63RCla2L9NH_3M4VdZo_0EExYHI9uX9g8YNDqRLn16iOmtcwv6tR10C7otxuQqQJTWZAgF_wIpVej8ss7KnheVE691vIOxqD12uZ32QToXYGFktBXvRz9WSydAFq29xu1rtY2L9sEyy4tdu1ZAUQZJQjFLL7HcJovINVdgC_E_zDDSFRJg-3ndE7BEwcQNrf1N-CA3f-rnTNQhwrGPdbbFsMbt8ZiAA-MszndCAubvOG0mtsQwES7A5ZMEahBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
ترامب:
نحن نتفاوض بشأن إيران وسنحقق هدفنا مهما كانت الطرق.
نحن ندرس رسوم العبور في هرمز، ولدينا السيطرة التامة على المضيق.
أريد مضيق هرمز مفتوحًا ومجانيًا دون رسوم.
نملك تكنولوجيا طائرات مسيرة متطورة لضرب إيران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75834" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرايا اولياء الدم</strong></div>
<div class="tg-text">قصيدة
نحن اولياء الدم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75833" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي: نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.  ‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.  ‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.  ‏الباكستانيون سيتوجهون إلى إيران…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75832" target="_blank">📅 18:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي: نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.  ‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.  ‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.  ‏الباكستانيون سيتوجهون إلى إيران…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75831" target="_blank">📅 18:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي:
نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.
‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.
‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.
‏الباكستانيون سيتوجهون إلى إيران اليوم.
دعونا نرى إمكانية التوصل إلى اتفاق مع إيران، حيث توجد بعض المؤشرات الإيجابية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75830" target="_blank">📅 18:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇷🇺
وكالة
إنترفاكس الروسية:
بوتين عرض على الرئيس الصيني فكرة نقل وتخزين اليورانيوم الإيراني المخصب في روسيا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75829" target="_blank">📅 18:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇹🇷
النيابة العامة التركية تنقل عدد من ناشطي الصمود إلى وزارة العدل التركية لأخذ إفاداتهم تمهيدًا لإعداد مذكرات اعتقال بحق مسؤولين إسرائيليين متهمين بالاعتداء على الناشطين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75828" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
السيد عبدالملك الحوثي:
النفط العراقي تنهبه الشركات الأمريكية وتستفيد منه قبل الشعب العراقي، حتى على مستوى الشركات المنتجة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75827" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📰
بلومبرغ:
‏تجري إيران مناقشات مع سلطنة عمان حول كيفية إنشاء شكل من أشكال نظام الرسوم الدائمة الذي من شأنه أن يضفي الطابع الرسمي على سيطرتها على حركة الملاحة البحرية عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75826" target="_blank">📅 17:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🤺
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ
18-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في مستوطنة شوميرا بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75825" target="_blank">📅 17:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
مدير مركز العمليات المعلوماتية المشتركة العراقية:
رصد أكثر من 3200 صفحة مرتبطة بـ (إسرائيل) ودول مجاورة تعمل على إثارة النعرات الطائفية، حيث وصل المركز إلى مراحل متقدمة في مواجهة هذه الحملات.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75824" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=PtUM5XBlBk1PMZJcFVX1TZ-AJO9-Mif_q76rzhaDrWscVpJnfx6QwPBLPnHyojfUsbwA2bxkKBDrjxnnkh5SSvXDt4__VAQ70Pd4dI6Nkbnr20x0WuUmquodY4ETK_ERKI10srDQWraWOHejbbgTcDaEeiPIIcZwzy-p2xO7qoZtuOk_AHGiRStPe89vHUzI5YpR5i3vOl6lT69JmoHAMXzujNGJVc0Q_rY9QEgv0dS1aTXUhvRfeHfThunmG_V7A9yegldKtOspUWsAOFg17YPHvrtbMZVaT0RBgB4tIqKO0JoQGiasjiv3t3LE9H7EhCSpCnKFI8wAd5NchFT3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=PtUM5XBlBk1PMZJcFVX1TZ-AJO9-Mif_q76rzhaDrWscVpJnfx6QwPBLPnHyojfUsbwA2bxkKBDrjxnnkh5SSvXDt4__VAQ70Pd4dI6Nkbnr20x0WuUmquodY4ETK_ERKI10srDQWraWOHejbbgTcDaEeiPIIcZwzy-p2xO7qoZtuOk_AHGiRStPe89vHUzI5YpR5i3vOl6lT69JmoHAMXzujNGJVc0Q_rY9QEgv0dS1aTXUhvRfeHfThunmG_V7A9yegldKtOspUWsAOFg17YPHvrtbMZVaT0RBgB4tIqKO0JoQGiasjiv3t3LE9H7EhCSpCnKFI8wAd5NchFT3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75823" target="_blank">📅 16:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75822" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤩
استطلاع رأي لفوكس نيوز:
ارتفاع نسبة المعارضين من الأمريكيين للعمل العسكري ضد ايران إلى 60%</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75821" target="_blank">📅 16:42 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
