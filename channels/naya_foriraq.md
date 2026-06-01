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
<img src="https://cdn4.telesco.pe/file/QPkPXIsZ4QVzlvpQO4s65V8EfCzzvPDWO6XRA89EGHII_WT_VwkNNGBTNsgJPE8I4uLRE4a-n2iVS_zUoYXUkd--Zd-qDdVDUp6Sih7CBuMc-AKqOR9v0Rf39PlYC8N3ZYq6dV0aMkYTa7ZIkTWc8IirUB8iRgpmDtCoZUjpNCOPlVJk_d_KKRWjfJE1JvIc0O3V2jDWqLogkYDv-_Jgbqc-nAMoQBL8mNrOwXleNDP-jE1JyXRq77uahguMno8QXX5JEwgyCKjNw9O9UX4tcwk6dO6dXCpz93Z30GojrSf0JU0pAgwpKv5nQcHkzSfl9XmW6Zp4fbxv361U5PLgXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 250K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/naya_foriraq/76592" target="_blank">📅 12:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
مصادر إعلامية تتحدث عن تغيرات
تسمية عبد الزهرة الهنداوي مدير اعلام مكتب رئيس الوزراء بدلا من ربيع نادر .
‏ تسمية حيدر العبودي، المتحدث الرسمي بأسم الحكومة بدلا من باسم العوادي</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/76591" target="_blank">📅 12:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106ccc92d9.mp4?token=jjUy5fc1z18D54-Ik60MloUseGg6gVyxUxmsjrXHMj9i0sfEw5UpZunRUWqJXfZwlXdd-bEPtXrjci3k7F-bEhPZolBDO9QwnfHG5S9nyANzI0uAG9D9ksiriBZ6sX5w92Bv-LDhdOBF0VnXtp35A20vkJA4pbMINTicBsLzB2Xk-ApR6kuVGty77JgMYkzn3WjSGFAamORnQwnxGV7KLjqbFMdopngwt9ov2SumKb0qHBfv6p9bFUO2J4HOxATCAoky4SxopwvogyVOXkh_bd3OSwpU7ljVDUX2TPUpJ719P7_G-Kx64RZabh3QLtBeID2QTLze4iagxTchItHEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106ccc92d9.mp4?token=jjUy5fc1z18D54-Ik60MloUseGg6gVyxUxmsjrXHMj9i0sfEw5UpZunRUWqJXfZwlXdd-bEPtXrjci3k7F-bEhPZolBDO9QwnfHG5S9nyANzI0uAG9D9ksiriBZ6sX5w92Bv-LDhdOBF0VnXtp35A20vkJA4pbMINTicBsLzB2Xk-ApR6kuVGty77JgMYkzn3WjSGFAamORnQwnxGV7KLjqbFMdopngwt9ov2SumKb0qHBfv6p9bFUO2J4HOxATCAoky4SxopwvogyVOXkh_bd3OSwpU7ljVDUX2TPUpJ719P7_G-Kx64RZabh3QLtBeID2QTLze4iagxTchItHEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة غارات صهيونية تستهدف الحوش في مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/naya_foriraq/76590" target="_blank">📅 12:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjdeZlco5FlZgo1oyDByZfslXJEwUasjmXEl2q0Mc6I7h68esrGkBzWrKt70JlN_JuJ7TTK2AsKf8mdlKtu6g70SGq7P_C_vXj5o5N37UHEecu7rMkgQu18PVMBQ6qGEhXYipNmKzu9FpyjuzBNLVEt2q5mLa_LZ-Zrda5-q_msQWtUMq1NlaStKtiMhIGUNqA7f6EZxKN1VuWPRuWJxmr7ko-0cNwc_hu9eiR2wSoTdKmgWx9RYDNPqLFbP8A9kqIY-XLE_FpwXuGQcnUdHwolupyD8APFZ2r73P5Ff0X5FY7aGUJNBTFmEkPmuHnd9kuvIOBZTSS8Kmq0n56AdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إن الحصار البحري وتصعيد جرائم الحرب في لبنان من قبل النظام الصهيوني الإبادي دليل واضح على عدم امتثال الولايات المتحدة لوقف إطلاق النار.
لكل خيار ثمن، ويجب دفع الفاتورة. كل شيء سيستقر في مكانه</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/76589" target="_blank">📅 12:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في ألون شابوت جنوب غرب مدينة القدس</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/76588" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ffdbce01.mp4?token=HTxUJ23SMG5kn2eJ1b3yejgJV0cXzTwVVCkPM56CuMnKFOfhjco5jpgJDiw9EcZtS7DV5BOzsMxW-F3i0KBBd1pOJsae5S7c7sA5QhcwDUbc33NCl3hHEZZ0ZXaWv5aEzmeVkTqp4E0NoRumKYQVEBVW3RiQDj_fuvmoYOe3Y25yjou7vjUHDtEUR9PiUjhBC0ileORUghJTbuyFqBlcyDzMIfZMXtucZAGmGQpDxl1vA2-5O3WFrYZ2Ld12dnAanSFM6JAi8L3Hr_TrP4BfETF2pnIV5lvdMeJjY4HmgR20gki0CPO1-3EmJ56MqSIruD_iIBYeJo8QZMJ-UfBivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ffdbce01.mp4?token=HTxUJ23SMG5kn2eJ1b3yejgJV0cXzTwVVCkPM56CuMnKFOfhjco5jpgJDiw9EcZtS7DV5BOzsMxW-F3i0KBBd1pOJsae5S7c7sA5QhcwDUbc33NCl3hHEZZ0ZXaWv5aEzmeVkTqp4E0NoRumKYQVEBVW3RiQDj_fuvmoYOe3Y25yjou7vjUHDtEUR9PiUjhBC0ileORUghJTbuyFqBlcyDzMIfZMXtucZAGmGQpDxl1vA2-5O3WFrYZ2Ld12dnAanSFM6JAi8L3Hr_TrP4BfETF2pnIV5lvdMeJjY4HmgR20gki0CPO1-3EmJ56MqSIruD_iIBYeJo8QZMJ-UfBivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صور من إحدى عمليات الدورية والمراقبة التي نفذتها زوارق البحرية التابعة للحرس الثوري الإيراني في مضيق هرمز.
أفادت إدارة العلاقات العامة في البحرية التابعة للحرس الثوري الإيراني بأن هذه العمليات تُنفذ ليلاً ونهاراً وبشكل دوري.
من مهام هذه الزوارق السريعة توجيه السفن في حركة الملاحة، وفي حال مخالفة أي سفينة للتحذيرات أو تجاهلها، سيتم إيقافها.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/76587" target="_blank">📅 12:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSZTKxdMUedd_3fDsCtiijg9GI89s5AsgKZyRJRc0u-uJfe6v2_Mo_1jh54ww9RgbYUS5hxenHtFHa5s3r_BltH3z74Yedk0pY3yFS39xg4H_4gM5eibgtagoh8Q7MRkXAwUukPZbkNxcDvkBqwCiB041GesW6gHdWCcC0aHcwwXevS7pPsTe9jIZOLW_C3C-fd68rToFwQb2sI7geeQPYx2kJ_BTVBwBI0y0k4HX0PxIWuZXlRWxBYPcxttP7_PyivN4q79N2wwdlS3O40GpkSPsuYbOuL8cJZBa9pjgKQIWtm_WHQBlMlAUhhl-iFPKeMdw_fm6z4WYUtC2_3qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الاصطناعية في 29 مايو سفينة بطول 252 مترًا مشتعلة عند مدخل مضيق هرمز، مع اقتراب أربعة زوارق سريعة كبيرة مشتبه بها تابعة للحرس الثوري الإيراني من الاتجاه الإيراني، ومغادرة خامسة من الاتجاه الجنوبي الشرقي.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/76586" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWTmlnSjrh6z2fVxvqtipZHZd8mQDRyPM7s29BggSdwbLk4ZGJ9EtdGj-_uK1_upzGskHK7A5TEG2fwgak9Cx_GnGhy1f2sNfCvKw5INXozIa2I5T_SUQfxSmBGjuGP5h9OPU3chuQrAHK59GZGr6SbVnLWKdcjnu7YCgVud88UdV-Gf6RpAOh7Y8kBPMuqEAVKXHpiwKUqz2WXdk7yxed-2LxgCXC35ks5lm7dG8PlQnmSM-1xVc-nfJu7u1bana8KOwY9nfW5slKY4AUBWxUaRHGLkSs8jWN1QVmgMA8rfsOE5vjXUbVTycV21dVNPgzV5Adm_4s9t2Guoax2-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رؤية اخرى !</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/76585" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
حزب الله: تصدّى مجاهدو المُقاومة الإسلاميّة عند السّاعة 15:30 أمس الأحد 31-05-2026‏ لمسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء البقاع بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/76584" target="_blank">📅 11:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇰🇼
دويلة الكويت تدين الهجمات الإيرانية على قاعدة علي السالم في أراضيها.</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/76583" target="_blank">📅 11:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=vkB8aDTgaoX5azsf2TD0H6IHNgYfF5e_AMyMcsQWwjhLzhjB4DFckY7ktT_ShcZAzLS-dIwCt3R3WflXmi09uFNl8uHq-Hzpc_BIy6EjSCgk_RNkd3vOzXQ66FhTLeDEbjfti8W_D9HMWU7l4UwFmkdiyGFvE6uTcZX1zNG_iqKGzsxIeAjtugqOdxjs3tiADKeiKrLENBjr_KM2Sd1jAXqe_wjIIT11J0E_Qw3wbkmW2pRjxs7FJ-y6KoHeOOtlV2mOciXb19hSmTvFhtx51qdiYu7_ez5nQ7lQ7fFjHDe5u9-FX6xbXTSczLk-rvjDncL68pRUrjPWs4EPWbcbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=vkB8aDTgaoX5azsf2TD0H6IHNgYfF5e_AMyMcsQWwjhLzhjB4DFckY7ktT_ShcZAzLS-dIwCt3R3WflXmi09uFNl8uHq-Hzpc_BIy6EjSCgk_RNkd3vOzXQ66FhTLeDEbjfti8W_D9HMWU7l4UwFmkdiyGFvE6uTcZX1zNG_iqKGzsxIeAjtugqOdxjs3tiADKeiKrLENBjr_KM2Sd1jAXqe_wjIIT11J0E_Qw3wbkmW2pRjxs7FJ-y6KoHeOOtlV2mOciXb19hSmTvFhtx51qdiYu7_ez5nQ7lQ7fFjHDe5u9-FX6xbXTSczLk-rvjDncL68pRUrjPWs4EPWbcbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حركة نزوح تشهدها الضاحية الجنوبية بعد توجه نتنياهو وكاتس بقصفها إلى جانب تعطيل جميع المدارس.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/76582" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان وإخلاء مروحي ل 4 جنود مصابين.</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/76581" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76580">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
إسماعيل بقائي: تبادل الرسائل يجري في أجواء انعدام الثقة والشكوك الشديدة والدبلوماسية ليست بديلاً عن عناصر القوة</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/76580" target="_blank">📅 11:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76579">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b911e1c9.mp4?token=u68VxHrv4CXkfCXHwktmWZBto21ajW6qxuS0eqtArZqZBLcIL9PY5WPWJthKyRFh10rk8c52rDmAVfmKkbSfJZlsfKrg4sthCSYz3H5NrbtC9BuysSsq3kuG6GRTmR1Isqs1RK74m5UXyRgtEThbQNCHvB0F1aYH4kM9adFm9qce1uSU3nadkGdGkQxzZhd4wtBlOabK9l-xyGfdcru9S5CMuep3j3WkJQK8fkKrOtC6qI5iI2QWIp6Qz5madtP2AKE8ARDutcLj438fQf7i8QSaZObUeqDjyKARH-wAXU0iQv4r_UI6YRqGJTNbzIxkaZPgRSVghCzGmbOxR5deag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b911e1c9.mp4?token=u68VxHrv4CXkfCXHwktmWZBto21ajW6qxuS0eqtArZqZBLcIL9PY5WPWJthKyRFh10rk8c52rDmAVfmKkbSfJZlsfKrg4sthCSYz3H5NrbtC9BuysSsq3kuG6GRTmR1Isqs1RK74m5UXyRgtEThbQNCHvB0F1aYH4kM9adFm9qce1uSU3nadkGdGkQxzZhd4wtBlOabK9l-xyGfdcru9S5CMuep3j3WkJQK8fkKrOtC6qI5iI2QWIp6Qz5madtP2AKE8ARDutcLj438fQf7i8QSaZObUeqDjyKARH-wAXU0iQv4r_UI6YRqGJTNbzIxkaZPgRSVghCzGmbOxR5deag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/76579" target="_blank">📅 10:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76578">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/naya_foriraq/76578" target="_blank">📅 10:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76577">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/naya_foriraq/76577" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
استقبلت الشركة العامة لموانئ العراق اليوم الاثنين 1 حزيران/ يونيو 2026، سفينة الشحن (MV KSL XINYANG) القادمة من الصين بشكل مباشر عبر مضيق هرمز، لتكون أول سفينة تصل إلى ميناء أم قصر الشمالي بعد استئناف حركة الملاحة البحرية عبر المضيق.</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/76576" target="_blank">📅 10:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76573">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIUxYxWIrdI4fwWs2ockUQjJ6Ff32grG4FPZ0lFcuN63e_xb86AZf3krOFeyHHTJBzxrSj_uKt7E-974i3iYiqOJ8gtStHCvv0N__YhW07sxQnDSrCIqT4BYTCLjFhfpEH-B5frLYEFuJ84MDh7RUDVT7xs1Mkqikiy-8KEpQlKXztQncdT3-AHNKKZC05krpywLFb8g2yOui9woZhZlBIuw_-UcvOVIHCzmJM5R6EK0OYUukPEHjzUqUl1mQPCKPGaccYzKjkW0lUUXXz2SynHR14bYdUEYp9QusBBojL_l3_zsi3f4pI_r-T5bJcrcjJpR1JEqYUomEummpxbpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtPz__SXyhPKTypW1XbPErgOUMSFVw-Vs4k8RbSWiNUZ2gSWuWAlFq0ay-ohxkgLhGiFHGXpFtqQAyzbHyK2po-_2u20t0u-XDTsHY4F2UmwgUi9iLxlCnbhae0dUohqpu-husH3cH_pta4UYuG-mpSs7ErRZjKuIxG-aINQA9FTR8nrtrMVM5TJtUhbYnQLkwcCjRcRCAtR1D58k9dTVDo3Dqg76q28wwBNSaXwkZFjel_2G-BCtqTGKIiP4oPiFRFAs6AwRS_aYWRdWDY5FI26Mt--PzRj9QLPUYGqfB_nTGF6xHdmN7WvpyTWDUYMQE6QFl5LW64pAkj2KOsaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0sQ5X4CGyjRUK-lZfEuaGwZT-aSsgpdq7HnLlNHIqIo-k6WhE5Rd3swU5jZm-A9rJ_TPeqikgfjyUss5h9NnTlnGmMohmymrZljwN2vyhfOdPowM5CKcz8kgn-E62lPgUq6IZYQtuqW5RUSuJIxRTNY5vCaRXFYAhZCRfEehYQjaBVQzm6B3vTBgAZWoLwR9ETRZSIEN0-gb8-h1yiTLCbWeQcvlmjsKBVYgQZRNsoRIwYHclwYax3x7XB1ovI6qsnxExuEuBh85iD88kbSzGCxdkbKB7lh7XZM04nG16-zKQarQGSr8ppIghkc-i0_BSlyGbe9izSTjIGZejj4Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
قناة BBC:
تشير صور الأقمار الاصطناعية التي حللتها BBC Verify إلى أن الضربات الإيرانية ألحقت أضرارًا بما لا يقل عن 20 موقعًا عسكريًا أمريكيًا في ثماني دول في الشرق الأوسط منذ بدء الحرب.
استهدفت الهجمات أنظمة الدفاع الجوي وطائرات المراقبة ومستودعات الوقود والبنية التحتية للاتصالات، مما تسبب في أضرار تقدر بمليارات الدولارات.
يقول المحللون إن الضربات تبدو أكثر دقة وشمولًا مما اعترف به المسؤولون الأمريكيون علنًا.</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/76573" target="_blank">📅 10:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdnS3p1YeJpI_EJjS5PIECZsVCpE7128AGrP3dPku0XlmQdXbx4o-c-T-IP5ZzT781l_7ufArMYQYwV-rd1ffcmSqhU9xOSUdoTClfF6_MXsCo8FcMlT-LLDwN0Ip5WjFbsl1-CZ7fkLV1rZBQw3vReXO6RvkKYMmcKvbiQ_W2lU2GU3bvnRDHZvJHo5U6lfKuSX4vCeK6LJ1hKXSTH7xclrn-HWBfOP2V2bPMoETIvSRLTxaz7ptJb9i8euTGQfSH_zx2fFtp4oL-ddd-btJxBt40IyFEbUV7dbvzArpy3a7-kABfUTwUMlldKSOv8wrlJQrf20niZtfBuwxfuaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي:
إن بيان الاتحاد الأوروبي الذي يُلقي باللوم على إيران لممارستها حقها في الدفاع عن النفس ضد العدوان الأمريكي الذي شُنّ من قواعد في الدول المجاورة هو درسٌ نموذجي في الغضب الأخلاقي الانتقائي؛ إنه نفاقٌ وتهور.
يجب على الاتحاد الأوروبي (
@eu_eeas
) أن يظل وفيًا لسيادة القانون ومبادئ ميثاق الأمم المتحدة التي طالما ادعى أنه يدعمها. يجب عليه التوقف عن استرضاء المعتدين مع إلقاء اللوم على أولئك الذين يردون على الهجمات غير المشروعة.
إن ضربات إيران ضد تلك القواعد والأصول التي تُستخدم لشن هجمات غير مشروعة ضد إيران هي ممارسة مشروعة للدفاع عن النفس.
تقع على عاتق الدول التزامات قانونية راسخة بعدم السماح باستخدام أراضيها أو أصولها لغزو دول أخرى</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/76572" target="_blank">📅 09:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📰
إكسيوس: تعثرت أحدث جهود الولايات المتحدة لتأمين وقف إطلاق النار في لبنان حيث توسع إسرائيل هجومها البري وتسعى للحصول على موافقة الولايات المتحدة لشن ضربات كبيرة في بيروت.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/76571" target="_blank">📅 09:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/76570" target="_blank">📅 09:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/76569" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال:
وقع الحادث قرابة الساعة الواحدة صباحاً، حيث استُهدفت قوة ماجلان التابعة لقيادة العمليات الخاصة بطائرة مسيّرة مُحمّلة بالمتفجرات. وإلى جانب القتيل، أُصيب ثلاثة آخرون - أحدهم بإصابات خطيرة واثنان بإصابات طفيفة. وتمّ إجلاء المصابين بواسطة مروحية إلى مستشفى زيف في صفد
حيث أصيب 137 ضابطا وجنديا في معارك جنوب لبنان خلال الأسبوعين الماضيين</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/76568" target="_blank">📅 09:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6982bec225.mp4?token=sJOQ1jfyg1cTk9-GDXJGBaXYeep_IumgFmKow357r3GYegUk0ew5a87X9QrCkGvOkA9A9SeRd4_Z0xFqz3rRJEKzVUK88oQFoqMsEhji8hWXm1W4lDkaUU1YJKsy67wRJz_Q8C9qlOqP7Eh2pnwMEmtz6_FiLGCOXmru1oOXHysySsjEe2ZFZ15-qnmC7eDXe3o_pBOGY6zLWXySfEagxFo5k7ga86e8p_E7QiXmCuX2dv4L2VSKdyZoLL3NkZXX1fiD68RJES2nguLAdR7OR7eQxkzQmIyhBnAaOpG6iWK7qdFA9x9ZEa6GJLw1WJ1JfS_U5XhIG28OmHzhNYv8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6982bec225.mp4?token=sJOQ1jfyg1cTk9-GDXJGBaXYeep_IumgFmKow357r3GYegUk0ew5a87X9QrCkGvOkA9A9SeRd4_Z0xFqz3rRJEKzVUK88oQFoqMsEhji8hWXm1W4lDkaUU1YJKsy67wRJz_Q8C9qlOqP7Eh2pnwMEmtz6_FiLGCOXmru1oOXHysySsjEe2ZFZ15-qnmC7eDXe3o_pBOGY6zLWXySfEagxFo5k7ga86e8p_E7QiXmCuX2dv4L2VSKdyZoLL3NkZXX1fiD68RJES2nguLAdR7OR7eQxkzQmIyhBnAaOpG6iWK7qdFA9x9ZEa6GJLw1WJ1JfS_U5XhIG28OmHzhNYv8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
محاولة اعتراض صواريخ حزب الله في كريات شمونة شمال الكيان</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76567" target="_blank">📅 08:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igq-pZLvwrWOiTYmfIupPDK-NXUmZReApb4t-leZxb0sh1Mqavy9uO9qL9Kn55VoqwdQp4EGZHgGjJuvvWaaJ0TaizybCb1q5zeUwPV5KEP2vHhQgd-oMw4RXrAUqP2-sQHkiP5sgUAtpLOdissbGcKC1NlWLir5CWODgomUJ6gADUCzn2iLwP5qVqQvjOgujvkdzM6xfdwGy4u8tOSDd2mUOEawVM3-1vQRLdZ7awReUcLR6z9up2DPk3e88PwERfI7q1xYaZQSN-y2VO60WnvCmK1-lE-9EkLXwnxscdFA4GamEbb8C-P0zIIQk97GdMsWTtKeO0AZcL13ppIZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إيران تريد حقًا عقد صفقة، وستكون صفقة جيدة للولايات المتحدة الأمريكية ولأولئك الذين يؤيدوننا. لكن ألا يفهم الديمقراطيون، والجمهوريون الذين يبدون غير وطنيين في كثير من الأحيان، أنه من الصعب جدًا بالنسبة لي أن أقوم بعملي بشكل صحيح والتفاوض، عندما يستمر السياسيون المخادعون في "التغريد" بشكل سلبي، على مستويات لم يسبق لها مثيل، مرارًا وتكرارًا، بأنه يجب أن أتحرك بشكل أسرع، أو أن أتحرك بشكل أبطأ، أو أن أذهب إلى الحرب، أو ألا أذهب إلى الحرب، أو أيًا كان. فقط اجلسوا واسترخوا، كل شيء سيكون على ما يرام في النهاية - سيكون كذلك دائمًا!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76566" target="_blank">📅 08:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc05a6034.mp4?token=Qa7L7B-qgT7hZQPhNWZk3_H9bStwTBBYnSfWCVLXDSiG3RAeXKn-5GdhO7fSaMXF1RTO18zx69TAPpCEG9gWvGSLU3831pGJr20_PhQeDfkfETaTRGa2el-1jnjYeJziKpMJ908p0Xg7rUhOF4kWYMSe_y3HKhUw79UGZ9KYofd4Mw2Jtt5K5C3wS2Gg9wuA6QqPlS1e60bVlNNhFhcyzBqSRRyFHVauMqDmY8eG1bvoPAvblft9XRpji2nYJSe7rdcR6pbKM5aClnWFvgYyLoucyxayvKtPUoDhUXFmQPZpmEurotfh504o2HyAPmlw6zoW74wR-wpeGkYTEnstFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc05a6034.mp4?token=Qa7L7B-qgT7hZQPhNWZk3_H9bStwTBBYnSfWCVLXDSiG3RAeXKn-5GdhO7fSaMXF1RTO18zx69TAPpCEG9gWvGSLU3831pGJr20_PhQeDfkfETaTRGa2el-1jnjYeJziKpMJ908p0Xg7rUhOF4kWYMSe_y3HKhUw79UGZ9KYofd4Mw2Jtt5K5C3wS2Gg9wuA6QqPlS1e60bVlNNhFhcyzBqSRRyFHVauMqDmY8eG1bvoPAvblft9XRpji2nYJSe7rdcR6pbKM5aClnWFvgYyLoucyxayvKtPUoDhUXFmQPZpmEurotfh504o2HyAPmlw6zoW74wR-wpeGkYTEnstFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني: استهدف مقاتلو قوة الجو الفضائية للحرس قاعدة جوية منشأ الاعتداء وتم تدمير الأهداف المتوقعة رداً على الاعتداء برج اتصالات في سيريك</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76565" target="_blank">📅 08:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
على الرغم من أن الأمريكيين والإيرانيين لم يوقعوا بعد اتفاقاً لوقف إطلاق النار طويل الأمد أو اتفاقاً لإنهاء الحرب، فقد بدأت "إسرائيل" تدرك أن الحملة في إيران لم تحقق النتائج المرجوة. فقد زعمت مصادر في المؤسسة الأمنية الإسرائيلية، أمس (الأحد)، أن الرئيس الأمريكي دونالد ترامب لم يمنح صلاحيات كاملة للعمل ضد إيران، وعرقل أجزاءً من الخطط العسكرية وخطط الموساد، بما في ذلك مهاجمة خزانات النفط والغاز ومحطات توليد الطاقة ومحطات تحلية المياه في إيران. يُزعم أيضاً أن ترامب، تحت ضغط من الرئيس التركي رجب طيب أردوغان وكبار المسؤولين الأمريكيين، وعلى رأسهم نائب الرئيس جيه دي فانس ومستشاره المقرب ستيف ويتكوف ، عرقل عمليات جيش الميليشيات الكردية في إيران . وقد بُني هذا الجيش على مدى سنوات من قبل الولايات المتحدة والموساد الإسرائيلي، وكان من المفترض أن يقود القتال ضد الحرس الثوري الإيراني ويؤدي إلى انهيار النظام. لكن بدأت الانتقادات تتعالى داخل المؤسسة الأمنية الإسرائيلية بشأن تحقيق أهداف الحرب. قال مصدر عسكري: "على مدى أربعين يومًا، زُوّد الموساد بكل القوة النارية التي طلبها. وتلقّى استجابة عملياتية لكل ما حلم به وتخيّله. عندما طلب فتح نقاط تفتيش الباسيج، تمّ ذلك. لم تكن هناك نقطة تفتيش أو مقرّ قيادة يشيرون إليه، ولم يتم تدميرها. ولكن ماذا؟ أين النتيجة الموعودة؟ أين تفكيك النظام؟" في غضون ذلك، تحاول النخبة السياسية الإسرائيلية تصوير النصر في لبنان بصورة ما. ومع دخول الجيش الإسرائيلي شهره الرابع من حرب "زئيرالأسد" وحرب "وقف إطلاق النار" ، فإن الاستيلاء على قلعة الشقيف ليس إلا حدثًا تكتيكيًا. كما قال ضابط كبير في الجيش الإسرائيلي: "دعونا نضع الأمور في نصابها. في النهاية، تغلبنا على عقبة أخرى. الآن لا نستطيع القيام بالخطوات التي نرغب بها. هناك خطط، لكن لا يوجد تفويض للعمل. نحن نحاول السير على حافة الهاوية بين ما يوافق عليه الأمريكيون ضمنيًا وما يمنعونه ويقيدونن</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76564" target="_blank">📅 08:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c11731b4b.mp4?token=lQgG0SfHWVFEtewf5dFSw7GwpzyW1bljlLSvmUdVqkcNxo9LsmHrSYyKUxeJMWLrDJnpIHLgcP_2KemDZNg1SUBdczeR7sMuwVKMcTmyjUbnR7XI7rmCTUTt7qPXA9Z4S7gStoiTlizoOZzz-STwbE_5KyVxsaGEeqrTcq7JX_kw5p8heKKcl0JjI2aW_Ld5W7iwZdM9iAINBZvqPkKzvUClAj2Z-xi1MD0mgLnGLeJLNCOCQeaHLblJmylwxxgp9fRKhJ6v9DAEBYVWxwdqqR55YAChMuXz3_OUetEqUbbaLhuseHJ6HAJnOaVtKYYjVPS16Qju3sMX_x1wLesQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c11731b4b.mp4?token=lQgG0SfHWVFEtewf5dFSw7GwpzyW1bljlLSvmUdVqkcNxo9LsmHrSYyKUxeJMWLrDJnpIHLgcP_2KemDZNg1SUBdczeR7sMuwVKMcTmyjUbnR7XI7rmCTUTt7qPXA9Z4S7gStoiTlizoOZzz-STwbE_5KyVxsaGEeqrTcq7JX_kw5p8heKKcl0JjI2aW_Ld5W7iwZdM9iAINBZvqPkKzvUClAj2Z-xi1MD0mgLnGLeJLNCOCQeaHLblJmylwxxgp9fRKhJ6v9DAEBYVWxwdqqR55YAChMuXz3_OUetEqUbbaLhuseHJ6HAJnOaVtKYYjVPS16Qju3sMX_x1wLesQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇬🇧
🇫🇷
فرنسا تعترض ناقلة ذات صلة بروسيا تدعى Tagor في المحيط الأطلسي في المياه الدولية بمساندة بريطانيا وذلك بادعائها بمحاولة تجاوز القيود المرتبطة بجهود الحرب الروسية في أوكرانيا.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76563" target="_blank">📅 08:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP8hqaxXfTvpdpnZnY9XnkRusS18fJ_J7GZVNB2Z0EpM93JCWs2tGfVw8ZEchWhGxjIwqq4pQKdxFfjVAtJlC0YtrjZ-ByPelWv6ghKhH7ASNBtjiy_Ge0Rb4BuYrLmk6vt1AuZJfW2y6iMZUP43k8pnDegrrkXSYoYNUkIekct3YI21-LWK588a1KCZeiR0I9nn7CICo5fEttsHR4TlDOCgAiNxVSsB-FKAUqw32V_l1KlQhQvLw_IefOFuqcZoeq2sBrw9XFYjJSlAXizcvm-TdRebsA5SpGpWcOezK_6OATKBh-f-wAk7KuYpoxfd0SnWveaG4RxTSJ_Km3ishw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emwrKKmMz3OXyzx8kyQI5pARfiRzwFBKoeSIzKbijbrgDxv87EZIzt0xBkVmXzCHGkPkqbEAiaUW-8oTAjgfg17WdDlTwrsOyuPhxenVnyYj1zeEkiTGCpOzudQD0dIpB52s86P4ln9lylXhHFEv3-D4jg2FCv5Ov8WRAltHsxlY_UUa75Zgj7yDMsHMHE2wia2qurSPgX7mjcpvP7cJypwTtMR518oUZz6WvaeSgwjkVOiDi9-h9KfAjLCZVLvF-nw_bVb98G7VAlFpI454em9A-CA0O9JCuBzA2Pe5SzjpgDuC7p80-Di81UDyu3d277h8f06bhdaOpojZnonV5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76561" target="_blank">📅 01:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76560" target="_blank">📅 01:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76559" target="_blank">📅 01:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76558" target="_blank">📅 01:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76557" target="_blank">📅 01:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عملية امنية كبرى في محافظة كربلاء المقدسة واعتقالات بالجملة لمجموعة الصرخي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76556" target="_blank">📅 01:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdNreu04rZW1JhYucK6Md6J-Tyva3PVb9_vqbzbSRACiFv_yDX11KylN_MYqq_ugDjMbE4behp0YP6ltln1_wKIhObaC5KW-iB_RuseOnlSzlGYbqeilxKzgFPiFg7xLhGFNaOLanxzX_TOtyauWDZEYczvXpANqO7GcprjkWIqIDkvN9Mi0z2nWfiuk5_c1gJF_d3AMiAhZSRsw8G6OkmXMppMYQTY1L_e-srTNb87WwheiyujuFWqEzyYWbjcVmPBNP8Ne2O5sI77eeFbHe7EDeEqc7s1xw6RfEtPKJGAUcvKkfOVt8L1YXDsXt0V5UKXLCkmm6sqthoXNbI3xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76555" target="_blank">📅 00:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انباء اولية عن حدث امني في قاعدة الكوت الجوية شرقي العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76554" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انباء اولية عن حدث امني في قاعدة الكوت الجوية شرقي العراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76553" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز وادي الانه بمحافظة اربيل في اقليم كردستان العراق بعد استهداف مقرات المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76552" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو الإسرائيلي:
في متابعة للتوجيه المسبق الذي تم توزيعه قبل وقت قصير عقب رصد إطلاق صواريخ من لبنان، تم رصد إطلاق صاروخ سقط في المنطقة التي تعمل بها قوات الجيش الإسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76551" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
لجنة الأمن القومي في البرلمان الايراني:
ليس لدينا أي التزام في الملف النووي تجاه الطرف الاميركي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76550" target="_blank">📅 23:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHHe4dZvBonUXr9WnlyGm1Gqb89oD5b0E6geIfipbhs0pfxRg6EBs7aI56qvqM5_Z9rZ2ZsQ6Rcl6rVrkUlu8oIpF_jl6ADRnZTd4eNSbX5Hiuu8XnbwTY_quHkgO7QpxHe6Hu5tEeey-_9A2GQ6jzcBq7wRZXD-qrQWcUB3Nl9_9Pzhkp38Q08MHRUiltI8AzAm3MA312AFGoV89CQ8Cjbfm578mygln7Swyt_jL02psLL14mngt9-gWMVccbRzXV9TRILlw7EYRKEuS6tTS8T1TTcLeNRQdlVPTT3bBl7quJ8-SbTjt6YOYVOD5F7p82MPp8K41cwdodWHHBek3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5AjmQuhlnYm0aqSgmFmfk5B0_hr0ogUaRV5cDAAeEX_bMy5C5MpKEa6g0lNIQ8qQcBpFOzbx7umXTM0bIb7Lvh8cUvSXc0hymZKysxepscGSQyQ3tgXP5Au4Ah3ihq_g7tvXMIQAbrvWj-ipF57ZBwFAmzSMYzKew31tWdCdgtiJ7mtoSu1lspx091kI_xChFzbT8n-CuqN11E0iDsNAJT_UkbcMaC4F7io-apLZfoxibihS7ytYdxvNzlk3P1oXP8gxQJC7JDF0G4jDcVQLwmyhqp_HeoR8p8Hgc37bzOkzS2Ql0AvxmHlDg8txfdnlqWvH5_Keg00UVpgPtqE8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✌
👌
👍
🇮🇶
🔵
مقتل احد المرتزقة الإيطاليين يدعى أليكس بينشي في جمهورية الدونباس الروسية اثناء معارك مع الجيش الروسي ، الأخير كان يعمل كمدرب لقوات الناتو في اقليم كوردستان العراق وتربطه علاقة خاصة مع بيت البارزاني ، حيث تظهر الصورة تواجده في أربيل بجانب بياران بارزاني</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76548" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1d-Fc13rH-xjb5UE-5oYacckSrFKOxzh7gBoR2XHeLExsrXaYHos32QurHKb-3hkji3WU774_BLqBPZ7O4kJacrPhRTeoNwsmhpt2EDjKoUacDfMtlD8UX0yERIFk7lUB6cdW2Is1npbMeuGYEoysP5Jh1STFFYGtmYwAPOwfLKVssXPJee2xLAIYupw2V8Rc7wVr3XwnfKl1goAuYHvviskRTCd18_zw-4rl1AT8-PzzAgPeDjzNIVxCGj1K4eVGukaQTuKz_j8sb2mMsgwxCg1z9ZENMMxTFOHRvf9RKlxHctSFiOwlDcofoTzCjLcA_H3tjxuvaWcNkcZ-2zMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9vsQqrfmdRSPYPg7M92Q6A7sjLUuP5dcVUFGa_dT9d349QulxNKXkZGqvLlyuG4syGTAsTMPGk8k--2M67ps6hzbkBpkaFMPlMy8aiZKolAcJ0eTKj7-XDjt5S5k8jkUBWkBeum7klXN4Qe6bIQcjmHQ5TuQbM3aFyEX-kOO54ZkEqgmc2K5sxjCeNv8JLRguDnTEkSFmjbQs_BKs334MqNnfcm2kh6uleUgphkyKpDmUfJh-88KJJEBtwxUSzredJJ8N2fMPHVWqEXQuvewf_xM9WewwWHzdrQKQ2Q2pgrXvPDcLTCoJ7egvN7EHdZEmKBtcTbi1ipnWlY44Cpfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
غضب في صفوف الايزيديين في العراق بعد قيام قيادي في حزب البرزاني ومسؤول في الاقليم ورئيس منظمة انسانية بالمطالبة بوضع شخص مسلم اميرا للايزيديين!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76546" target="_blank">📅 21:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmF0tfDVSbzUCuEgS2YTLf7RUFsBufd4B1KsqnTYXGvUXCj5DzFee67IUvuT4Q0W2HoWh8ODEIJ0JX05g4Htz5O35moAtsbgN8PooSIny7MrAYcX-j31KQK0yyCAa-iMDGhoD3XUVyLe4wisTZUNtQqZkn7g_xLVi4ItE0ME6kIfEXY7msYqdM_ciCOZaK19rb_PKT6evziLEMiZ_kw-u7VWSa2ETxcrE4xkkaZyum1FVL6v2UfJIA7kVVV8GYcQ37X_8EeiPuuZM_pDII0dp_XgHpsooVs5Uvyof5pxjyWLSoNUMuZQ3VaRE5EkS93A-Nmzjh4YBvlhVGxz_STQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✌
👌
👍
🇮🇶
🔵
مقتل احد المرتزقة الإيطاليين يدعى أليكس بينشي في جمهورية الدونباس الروسية اثناء معارك مع الجيش الروسي ، الأخير كان يعمل كمدرب لقوات الناتو في اقليم كوردستان العراق وتربطه علاقة خاصة مع بيت البارزاني ، حيث تظهر الصورة تواجده في أربيل بجانب بياران بارزاني</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76545" target="_blank">📅 21:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKMvkjigKeUDRWsEqLOV8RlH1Db_xMhIxjoO0eSl3DszIBJbGy1rtqA_aGJioMURhgeO6-O-fut1aT3hZKqx_7fT4GhrpmGfEqLEdEbbJ0xPQtYJydwByX4GpoX8wxl_lPVekDTZ31H48PJaHHQE6d1UzLqRQa0O-p2yfq4f8ZA1cHTMZISE-8mM4u-gWJt4GcNXSfB1UG69TNlOghi0P_P6XnKrvV6BQEn2ExrimRlExfBENVbG0BA6KPzCyDlTzNZ_7W_Al_9UeZXynOJ3yQ_GmCwQNNtMVM_oXw2_dPNtX7LxzYnSnP44eX1Vs_7yfJzDhFZeLxHufUJvHfhpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMriB32LlzDtF9OZDv85h3r5mM_BBSd0_OBltXbPm7f7rHb5rYzMBEkwmK5d7abVnZKTwtuciI-f735bD2sFtNPHPssZVU15kBQGdsLQAxJSVvwdDG9XrI5XZROwy7L0qi6Fnz8S2KOxC063cctyo8JgTyFTmX76IDBtCoWcXFowxHqYQddvh2Yzb4GA9PIBr2gxf25J6WlTCXEkDVZZj9ygi8FMQGCJl-soi959K2cSeEkX9eWWnjcrvQ9p_IuSJo0MbqvrG1VCfkpS1UFKCQEHOhars-ccyOVLgIeSKKwf-LjHyKNdkbYr2e5a1jd_TTIZ3bW_zGJtiOt5I8XdPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✌
👌
👍
🇮🇶
🔵
مقتل احد المرتزقة الإيطاليين يدعى أليكس بينشي في جمهورية الدونباس الروسية اثناء معارك مع الجيش الروسي ، الأخير كان يعمل كمدرب لقوات الناتو في اقليم كوردستان العراق وتربطه علاقة خاصة مع بيت البارزاني ، حيث تظهر الصورة تواجده في أربيل بجانب بياران بارزاني</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76543" target="_blank">📅 21:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭐️
إبن شاه إيران الهارب، العميل "رضا بهلوي":
على عكس هذا النظام الذي يريد محو إسرائيل من خريطة العالم، فإننا نعتبرهم شركاء استراتيجيين حقيقيين. نرحب بأصدقائنا الإسرائيليين لمساعدتنا في العديد من التحديات التي تواجهها إيران. ليس لدينا أي خلاف مع إسرائيل.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76542" target="_blank">📅 21:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
26-05-2026
منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في ثكنة بيرانيت على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76541" target="_blank">📅 21:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf6c39776.mp4?token=cHh1P-WrJQ0ExeO_ttw9XUz1svnwhxfcE3slPhOUUvPkQAqXwTixfKoa_qcp13jSXFAmF7EC7DLAsNH-ZkCdf4OhZS03jBVxkLYhCnkqwOSI9BfDZ4JaE4rViLOqcNTKiiBLStCfzmRpG2GYo1-4TNSccMPLIValI4vHAFE2kyqbqyfmUFPeO-IIfDBcQ8-d9DHN5S612HfveMdfojy-lgtDlEODBA8sB1gXaFJrKZul5whnOHL4dKRUTw9CRYYEpRvG1tKepcIztJ4BfJf5Axoiqoo_wfFyjRFWhr7DKIcWGTb_yC0CCfykjynH2_L5cz9bGB18R4sJvxrxxhXgpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf6c39776.mp4?token=cHh1P-WrJQ0ExeO_ttw9XUz1svnwhxfcE3slPhOUUvPkQAqXwTixfKoa_qcp13jSXFAmF7EC7DLAsNH-ZkCdf4OhZS03jBVxkLYhCnkqwOSI9BfDZ4JaE4rViLOqcNTKiiBLStCfzmRpG2GYo1-4TNSccMPLIValI4vHAFE2kyqbqyfmUFPeO-IIfDBcQ8-d9DHN5S612HfveMdfojy-lgtDlEODBA8sB1gXaFJrKZul5whnOHL4dKRUTw9CRYYEpRvG1tKepcIztJ4BfJf5Axoiqoo_wfFyjRFWhr7DKIcWGTb_yC0CCfykjynH2_L5cz9bGB18R4sJvxrxxhXgpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد تظهر الدمار في القاعدة الإسرائيلية في بيت هلل نتيجة دكها بمسيرة إنقضاضية اطلقها حزب الله.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76540" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de658edb85.mp4?token=hS1NWJOZOsOImlwKR8XkbM-0e_MW9A90OybP5JeeTuLNS6nCKHub3EbOzHstTYRgN2HOqRpt7bDFfOiBZW3A_o8yu2CQm8DbkpbCATAxNYpwFx3BKyJ50kERe0uGrtQhn5AZH_8Eg_s-RGUKuJUcIAAe7_8cyBSYFXLWO_jxHCu64ElmonA5oNmbCVdzL7jJAa31G4jKC0ROetoa3SMMOjeujZac2avTx-gLEGCi7akyXp7WO2LZSK7muw59jKFGaTzQ6FmdZVz7kKlGVU6E725uqRx-pOpdtctSo9qdBq8mhXLZjDTBr7Wdd6RR8Ue6GFPw3pu85R5VOCFRSKNldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de658edb85.mp4?token=hS1NWJOZOsOImlwKR8XkbM-0e_MW9A90OybP5JeeTuLNS6nCKHub3EbOzHstTYRgN2HOqRpt7bDFfOiBZW3A_o8yu2CQm8DbkpbCATAxNYpwFx3BKyJ50kERe0uGrtQhn5AZH_8Eg_s-RGUKuJUcIAAe7_8cyBSYFXLWO_jxHCu64ElmonA5oNmbCVdzL7jJAa31G4jKC0ROetoa3SMMOjeujZac2avTx-gLEGCi7akyXp7WO2LZSK7muw59jKFGaTzQ6FmdZVz7kKlGVU6E725uqRx-pOpdtctSo9qdBq8mhXLZjDTBr7Wdd6RR8Ue6GFPw3pu85R5VOCFRSKNldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إسعافات نجمة داوود تنقل عدة إصابات 2 منها بحالة خطيرة جراء عملية دهس قرب غوش عتصيون في الخليل.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76539" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99a02cad4.mp4?token=QqAmLNWMn_Hc2xmF7wmnzf0jW-uvH3WEwFtJz5I_kLC6ic7D2dGA25VfIanesu6hi9l5Sl3k_NZUXVeeRVbPHgt7ylmdewK3Xcdnbq03gPoDBJw1QuN5HnXpb2hMJlFrCYxChFRuN0moD9j0QQu1886dI2KidHHos4MeN4dkM_9cSUXJ8mxoqC1chYZqnU8K3WjjbnRpxkf7Hu4K1imKrFGuySR_tsY9EnKv5lQiOxHPBWsMyNa3nRlle4Hi-NKIuOhzIQWYesuG6ST0cWd_tO7V1A43_BzqBIvUlJlvCwfYc0xnHnA6OnWVNl4EKINPYmsuZxj69OXncpvh-2lLNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99a02cad4.mp4?token=QqAmLNWMn_Hc2xmF7wmnzf0jW-uvH3WEwFtJz5I_kLC6ic7D2dGA25VfIanesu6hi9l5Sl3k_NZUXVeeRVbPHgt7ylmdewK3Xcdnbq03gPoDBJw1QuN5HnXpb2hMJlFrCYxChFRuN0moD9j0QQu1886dI2KidHHos4MeN4dkM_9cSUXJ8mxoqC1chYZqnU8K3WjjbnRpxkf7Hu4K1imKrFGuySR_tsY9EnKv5lQiOxHPBWsMyNa3nRlle4Hi-NKIuOhzIQWYesuG6ST0cWd_tO7V1A43_BzqBIvUlJlvCwfYc0xnHnA6OnWVNl4EKINPYmsuZxj69OXncpvh-2lLNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقجي:
المحادثات وتبادل الرسائل لا يزال مستمراً، وحتى يتم التوصل إلى نتيجة واضحة، يستحيل الحكم، وكل ما يُقال الآن مجرد تكهنات ولا ينبغي أخذه على محمل الجد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76538" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce9d77b27.mp4?token=BPndnHxLMJpv2NDW1H53s-zwvfVEc8QCrZ-2_JlzbNSrk7GaaRStY5yImN-6y7yL7XeG4T2kPjx8UQzT-s8bS705HbXm6xeJQd34X9fCvaFR24bplmWiURK3s14mngVCntt-8rNtNbYAMouGuDXdvVLSCCeA8Juk7J8m4fpIZw4a0KHXAbW6rCDuFz6_dfcIoDP2HEUHdfzI_jaXT6CDXiausT6e9vor6gD0Bu25QiT7RdsH6NgsbJ19ahNDWwTjuycegQh48DzVY9K6xmx_HYpIqioODDP7FYo0szxBaVVvzPae8Eb-iuE5VUKPwCDjENkfJHre12ncRBKICOKlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce9d77b27.mp4?token=BPndnHxLMJpv2NDW1H53s-zwvfVEc8QCrZ-2_JlzbNSrk7GaaRStY5yImN-6y7yL7XeG4T2kPjx8UQzT-s8bS705HbXm6xeJQd34X9fCvaFR24bplmWiURK3s14mngVCntt-8rNtNbYAMouGuDXdvVLSCCeA8Juk7J8m4fpIZw4a0KHXAbW6rCDuFz6_dfcIoDP2HEUHdfzI_jaXT6CDXiausT6e9vor6gD0Bu25QiT7RdsH6NgsbJ19ahNDWwTjuycegQh48DzVY9K6xmx_HYpIqioODDP7FYo0szxBaVVvzPae8Eb-iuE5VUKPwCDjENkfJHre12ncRBKICOKlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رداً على أكاذيب إنترناشونال..
مصدر مطلع في الحكومة الإيرانية:
الرئيس بزشكيان لم يستقيل، وأنه منشغلٌ بأعماله، وأن خططه المستقبلية ستُنفذ كالمعتاد.
الهدف من هذا الأكاذيب بث الفتنة وتقويض النسيج الاجتماعي المقدس في إيران.
الشائعات التي يتم تداولها، عادةً ما تكون من نسج خيال القائمين على هذه الشبكات، ولا أساس لها من الصحة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76537" target="_blank">📅 20:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYME2iIfvf6R1-mSfXkwmH8KwyxwpY55sewAzPHFd74a7B2Q9RatsR_dt4_xrZniS4FMKSQj0V5qS8W5DJWookv_KqVYb1wGNxfdAz1_Q-9telgPIdoDpv5ZTCyQTqcBKjIDwjCgsi92zCzUiIPHXv6o-gWtBKkiYXE503vri1hzC1_2E1_HZ3inb6064CXDYFUN8C3txiORxMapVnJlozLf5SQbra5Og-G1uiKBLpcXY3KozqQxdQB6n1W9zMualq8EPRtK20FTFv9XJU4t7fyxgOe5kJyA1AvttntV4YxrRDeKjnY_jQZ-Qk6r9_WZbCxP9fruJbMPQVrnV_9Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سيكون ميناء الطائرات بدون طيار في قاعة البيت الأبيض، ربما، الأكثر تطوراً في أي مكان في العالم! سيحمي منطقة العاصمة في واشنطن دي سي لفترة طويلة في المستقبل.
مع ظهور أسلحة حديثة متطورة وقوية للغاية، لم يعد بإمكاننا حماية واشنطن دي سي باستخدام البنادق والمسدسات وحدها.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76536" target="_blank">📅 20:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
مساعد قائد القوات البحرية للحرس الثوري الإيراني:
سنقاتل ضد أي تجاوزات للعدو، بكل قوة، حتى اللحظة الأخيرة، وليطمئن الشعب الإيراني الكريم أن أبناءه في صفوف القوات المسلحة، بأسلحتهم جاهزة، يدافعون عن أمن وشرف هذه الحدود والوطن.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76535" target="_blank">📅 20:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية ضخمة من لبنان نحو مستوطنات الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76534" target="_blank">📅 19:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da394b0bcc.mp4?token=sqjUSZ5BXjPN9MxdN-CPya__O6HGNv7kHapw8LWnO2nDDq9hvwbAdEvy1tEfBK43x4CYoLCVkzVlAVoKqfpCrZ03bXrSmw4ZbOg2Y7ybS_IPzs6VkcED815UE00BRCYm_N2EwG6ktEyukLLm6pOZ7RRVp3c-P8jtfc3sUxEAixe7oRzCSQARzrwrB9VKankH-uBd_d3YdYmn-4eGC2ZynWgi5M7WBuxaMoZrLkni0YwndHvsVbj0-2L3ENIHjDEK_CTZ37dhJgzvP1hq2v9FDnjXNSMvo0kyooRaTsaG3Sbu_EsbnipB8QOs9mpHHFnXJnOU5k2pvBsD5Sgi_8LCJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da394b0bcc.mp4?token=sqjUSZ5BXjPN9MxdN-CPya__O6HGNv7kHapw8LWnO2nDDq9hvwbAdEvy1tEfBK43x4CYoLCVkzVlAVoKqfpCrZ03bXrSmw4ZbOg2Y7ybS_IPzs6VkcED815UE00BRCYm_N2EwG6ktEyukLLm6pOZ7RRVp3c-P8jtfc3sUxEAixe7oRzCSQARzrwrB9VKankH-uBd_d3YdYmn-4eGC2ZynWgi5M7WBuxaMoZrLkni0YwndHvsVbj0-2L3ENIHjDEK_CTZ37dhJgzvP1hq2v9FDnjXNSMvo0kyooRaTsaG3Sbu_EsbnipB8QOs9mpHHFnXJnOU5k2pvBsD5Sgi_8LCJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية ضخمة من لبنان نحو مستوطنات الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76533" target="_blank">📅 19:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP6AEtRBl0gumLVcu4Ed00UEWWH9ys-80tFfTjfq9PjAdrLysaBezXVvxStgqj7a6tdPmZe8ZaVSzxVPnCN3kQadIwxt5rvZV-w9Ig_CMHwYv1bOhzgQRSIgjLOZNeqyUXGbuLadwgfWJ1k5KgbsgwS6tCpp_pboYeYKBO6uZAsTuYIBQwXx8jM0Gff348SH0rE3IkD8nykOuIJD4VoW76_QfyCAJXGruv7Kiy1oII3HIjLfD54TEnjx8SCdSviFBfqMrqbuMmsCDkiThjsr6FeOuw6QryXJqxzpBr-Un7QWZv29c-PzJ1HWOOhlolPM0jBkJO23-ybsuJgK5NErPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9086b036.mp4?token=sEPrPAYvODQFIEmPtgOOZwB4QLDDtEXhprv1nv2QbttdxCLqIJnhAWTHOdB3UwHLtfKvV_pts9hlfCv3GJ6DdIXfHGRcb4hKyvcwclPu3xORKIEB9mtFKERNLSSjX44KxT7tu398lY93gHg1KR5JKpnZ-KNOvaC4ef3bF6tEVN1uhGqvJtolLz8Hx3qAAJYS4gGtXKP-wJxlKIfH-8EJmRiCMiVTfUQflzKC8ttwaM-_fBz9Fnu_g9Psgz0yaQ_FGxunc2BZMTqulTw0c5prA5AdddxQIalk_7QjALfx2NoKRvQ7svLh2br5U_Nmtue7SJ8Eogb4b4jcs7BkKNspxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9086b036.mp4?token=sEPrPAYvODQFIEmPtgOOZwB4QLDDtEXhprv1nv2QbttdxCLqIJnhAWTHOdB3UwHLtfKvV_pts9hlfCv3GJ6DdIXfHGRcb4hKyvcwclPu3xORKIEB9mtFKERNLSSjX44KxT7tu398lY93gHg1KR5JKpnZ-KNOvaC4ef3bF6tEVN1uhGqvJtolLz8Hx3qAAJYS4gGtXKP-wJxlKIfH-8EJmRiCMiVTfUQflzKC8ttwaM-_fBz9Fnu_g9Psgz0yaQ_FGxunc2BZMTqulTw0c5prA5AdddxQIalk_7QjALfx2NoKRvQ7svLh2br5U_Nmtue7SJ8Eogb4b4jcs7BkKNspxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لحظة انفجار طائرة بدون طيار تابعة لحزب الله داخل قاعدة عسكرية للجيش الإسرائيلي قرب بيت هلل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76531" target="_blank">📅 19:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=ungxADZzGNPOcnloGDp_KDdlVJQxTJAWAT32z2g813EA-gHPWR8P2MOiUQQpB-cE-82kuq8c625K5O1DwXqlJa0IN6G6KgPrM1Z9RiAPvmaNhHcM3l-6Zur3VbhpD__gvhM4SzyFDbbhIJMLj577EXaO0ah5zYs6UV0MI8hbnM1viH69ln1xftdghm_PRBkc2SR2NfDJgAjiR8YSaVqwfAStTjM8Zd_I7RaO_ZKT97qQGX7ywOLt-B6r14rMAAyEuPRFlVth1uwlyv2soSRmMG0XZAtn6UK6IkoZAmH6OrA0nRTtywXgPFEt0hrRrnteDw_7e1TzHJreLLzym71CAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=ungxADZzGNPOcnloGDp_KDdlVJQxTJAWAT32z2g813EA-gHPWR8P2MOiUQQpB-cE-82kuq8c625K5O1DwXqlJa0IN6G6KgPrM1Z9RiAPvmaNhHcM3l-6Zur3VbhpD__gvhM4SzyFDbbhIJMLj577EXaO0ah5zYs6UV0MI8hbnM1viH69ln1xftdghm_PRBkc2SR2NfDJgAjiR8YSaVqwfAStTjM8Zd_I7RaO_ZKT97qQGX7ywOLt-B6r14rMAAyEuPRFlVth1uwlyv2soSRmMG0XZAtn6UK6IkoZAmH6OrA0nRTtywXgPFEt0hrRrnteDw_7e1TzHJreLLzym71CAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  6 اصابات في صفوف الصهاينة 3 منهم بحالة خطيرة جراء استهداف بطائرة مسيرة انقضاضية ؛ ومروحيات جيش الإحتلال تجري عمليات إخلاء.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76530" target="_blank">📅 18:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYc_ZWvpnnb6E9SUVpGdS7wf5qMfRjwNkMKdXDuNWitmkaV4o9xWb2hQEa_B3UdJirXBotxIiCxlnJmnAc_MPLk7apUuUHEDX1XGp1BfGIBTnnq43a29Zx4WIkg-S25fq8YacqM9wT226SExePmFeLKgycUS7Nd7y9kZQxR3L_EaObTtss7H3dMwjv3tgmUgPRuRsdXv4D4cGkCApzmf3oDpv7KHL4Y_Wl6oSCB7xTkDUd1TJiQWz_-FUTD_zndRLzHguCxKtbD4Z6P8jeqPNUPC_0DhZkX4zUARddrrgSvqJuiRSXi7c_2I07jxRJnqJmrlEMokDJX9yEpUiOMuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
تشير تقديرات الاستخبارات الأمريكية إلى أن تنظيم داعش من المرجح أن يستغل هروب وإطلاق سراح آلاف المعتقلين والمنتسبين إليه من السجون والمخيمات في سوريا لإعادة بناء صفوفه، وتوسيع شبكات الدعم، وجمع الأموال. كما يشير تقرير أمريكي مُقدّم إلى الكونغرس إلى تقييم مفاده أن داعش في سوريا من بين الفروع الأكثر ترجيحًا للتخطيط لهجمات إرهابية خارجية. وتُقدّر الأمم المتحدة أن نحو 3000 مقاتل من داعش ما زالوا نشطين في سوريا والعراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76529" target="_blank">📅 18:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoMfDlxxBx8jJTKdqs_bMXOzaghVm-m2o8LodIzsBZp6egtWDA0_ulk2EY2WDS-2oJRMJCylsc_5-_t0yccxQIQAOYi-h4ZQcfEnZk9oOk07o5MnmOezu1sfmlOzPSAtd9TCxpLfjCfrr-IUvEM9Yo8-97mwUw08enX8H1gNcuKqJFmKSJIFiQjiTg3uePQLGUDTwht5qPH3G_bI5dgeP6CS3JoUZ315clu38Cq0BbHVW-2oMeCmZFAYwbqJLqDQAcxXqkl2uzYTcKgTF-doJg2B6pf5_3EWrrqcoUGhgrrKYY8K338inmxEbegdM9Qr79HOlBKF2i6iv-oPpCYChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: سقوط إصابات في بيت هلل عقب انفجار طائرة بدون طيار.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76528" target="_blank">📅 18:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
سقوط إصابات في بيت هلل عقب انفجار طائرة بدون طيار.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76527" target="_blank">📅 18:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية من قبل حزب الله نحو صفد المحتلة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76526" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
🇮🇷
مسؤولين أمريكيين:
ترمب أعرب عن قلقه بشأن حجم المكاسب المالية التي قد تحصل عليها إيران في إطار الاتفاق.
‏إيران لم ترد بعد على تعديلات طلبها ترمب في مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76525" target="_blank">📅 18:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKCTTX3B6Q7E94moHG-PMtmZTq2efyHkqNrJZfN4d1Td4qmIKbpGreQwCveXK8cHRAPtiC8wbfnLNKvth4imKMKa-PtP8XcBRWAbDijo8aKGAwS8_WVX5mgQVUvJAxREYyf-_1PLiRt19nXZ2QDyOPGj6sZe4vuBwQL9kqNi6h1bjPcuofsPtzcj6gDSmv1EAbsPWmtr4UtLRj2EqVqzduam0uPbq_m-Cum0GrRqd-CBZkoTHFgQHQrqjIkWyH64jYg7I9KoIXS06xYZM3BTTUmYMgV6RUFFdWjF5ef5cO6vYp_pbz6pqeaDXaDWey2U1mHwAOPx4n5eh5cL1IBWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
ترامب يعلن تعيين توم باراك مبعوث خاص الى العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76523" target="_blank">📅 17:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AafCLSiAEdZ1vvnzF5Qb_YfCTOi02Q26E46n3hxMmCcx_bsvYxL32Sxj2pe_w5K562sdS95kilJlps8heE0Ly8BerljiZGGsAwWYstlDRa6gBVy7nEnYHre5E4f2_6HGq_XBBqUI16ubuoyF7Gxy7J9VVbopcViHLCHgItjT3RzH-wA55o7BhYqjJdgI2AOBk6F0kqxVPaJJUrWOPNHDmVbvnrOhWx9pb9mJV-LPnvI_iNZgrJ_NEmB2UP6CW53UpFhjN1pUKhk2bCUn9yE0_o2kZicOGMDfNHuqtR77wyYudzLwTyFJhtWw8TZgyBPq81gqmm9VMLKVEuh3xqljiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ حزب الله في الشمال الفلسطيني المحتل وتصاعد أعمدة الدخان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76522" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449c4c4755.mp4?token=sTXGe9eqyYUG5Fb_PzQ9oKphlvST8l7dmtHllgFvQ1Lnl1PcD6zE6pQJWAps7d4GAs4PpUsEDZ-5LCmk8DwjxY1mWklQOHpRrHeMsxZ8m9KILGadDzZ5O2qCqo9Qn6Kak7JG9pXpwHsQ3EFRo0UsicdPCLAkR99fbzZw3ldHbR0EIFy5ayEFAnqzdGfbAz_0571CdUVIMatkYs1Pmqx6S7vBO4sVcu3_lVzK5Oq5wvwAuTTAfFV8KQ8vSQtARYJ_rJjqnoPq8yqNUoa_KUaUki6ci87KAIEecz2gy98HUWNm6CZyU4F97NAavZQTXyJg8vAaDRd9qufc0lX6VItSnKrah_WLUGse-3-HGGDk-F7MpoJ5NQe2eyuSsdnQ4a3y0EGiClP47r01426ZFlGRjjH_QLiLHDOEskjJZ5f9ntCcoV-hTzlLjVMvb6v06oO0RXWgc6gS6bJr8NZ9QhoW39VpHFEIA2an262sLihzRHiTXCKWTpiG9qf6gkNmn4SO50Y1NnqKHrroEsWq-lX5yfhsKMARKe_tKT2ULQ-uPBI2Ljylwa71odWCTrNc_nDymZSsgrPw-Kq3WGyc-WF4RET6FkT4TbCc63NkgtUAbI8TZoIagKTigRr0l5lmk_3choVN42GDw78xHAf1rR1xOufx_ijAYaCXl5Ne4e7LKUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449c4c4755.mp4?token=sTXGe9eqyYUG5Fb_PzQ9oKphlvST8l7dmtHllgFvQ1Lnl1PcD6zE6pQJWAps7d4GAs4PpUsEDZ-5LCmk8DwjxY1mWklQOHpRrHeMsxZ8m9KILGadDzZ5O2qCqo9Qn6Kak7JG9pXpwHsQ3EFRo0UsicdPCLAkR99fbzZw3ldHbR0EIFy5ayEFAnqzdGfbAz_0571CdUVIMatkYs1Pmqx6S7vBO4sVcu3_lVzK5Oq5wvwAuTTAfFV8KQ8vSQtARYJ_rJjqnoPq8yqNUoa_KUaUki6ci87KAIEecz2gy98HUWNm6CZyU4F97NAavZQTXyJg8vAaDRd9qufc0lX6VItSnKrah_WLUGse-3-HGGDk-F7MpoJ5NQe2eyuSsdnQ4a3y0EGiClP47r01426ZFlGRjjH_QLiLHDOEskjJZ5f9ntCcoV-hTzlLjVMvb6v06oO0RXWgc6gS6bJr8NZ9QhoW39VpHFEIA2an262sLihzRHiTXCKWTpiG9qf6gkNmn4SO50Y1NnqKHrroEsWq-lX5yfhsKMARKe_tKT2ULQ-uPBI2Ljylwa71odWCTrNc_nDymZSsgrPw-Kq3WGyc-WF4RET6FkT4TbCc63NkgtUAbI8TZoIagKTigRr0l5lmk_3choVN42GDw78xHAf1rR1xOufx_ijAYaCXl5Ne4e7LKUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
آلية تابعة لجيش العدو الإسرائيلي في معسكر غابات الجليل شمال فلسطين المحتلّة بمحلّقة أبابيل الانقضاضية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76521" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوالف الگهوة
🇮🇶
السيد محمد عبد الهادي الحكيم مستشار رئيس الوزراء منذ حكومة سيد عادل عبد المهدي استقال قبل ايام من العمل على الرغم من إلحاح رئيس الوزراء على بقائه بالمنصب .</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76520" target="_blank">📅 17:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76519">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVAZikyW7MLapDumiq2XP494DsZJzk1RGXnMeAi2Aw7ziQF9A90i-14tnpces2P7lpQPi8H_pm4V1MZ9nHJlk62RaBtFjwjQ6PGgHnsLo_NxocY5rgWlr_oFaqxO3cwbJDC6q0BtI89u75uf5vIxEzUP9QZ6QdCvetDnwI9NcoVrhVrSdVFp6mUrrWA7g0sFboNHju2JYsw6iEVdJoo-IsCXutBtAGkCuZPNsnw8c1QG5bMNJ8xtIDiCOBzdrBp1OvUjibJ5lwbWIPG6PMYY0Cc-e6DPeKB95tLropVaeUYs8XlkUpCt6ptF7UcM83zWiG84AHaMuEuAJn_ihUmzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اعتقال شخص انتحل صفة رئيس جهاز المخابرات السابق و مدير مكتب الكاظمي القاضي رائد جوحي علما ان المنتحل كان يستلم رواتب منتحل الشخصية !</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76519" target="_blank">📅 17:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBWGF1hsrnCEsv6HmRMjAwnXhD5a0ieSD0d2jypjoeF09hOGTvjGew8-tMMpy8SQnZ_gDkeh2UOys9cH3JuAcwfl1-x2CIxDDubn5rAEfzjKL730ofewbEuXUFFUqNxwjUKXR94ul2jMNCaHcKFaWhFpL94iNKFVeLKFFeeMbYrrxZlIAXeX_kg4ST374fGx-36dHpEnq-V-EIshkFdiAOxE8NLJYV8SYD7o_JaowvoXinYAtA8QmaYQjwah5I4FkkH4yLZ9TozhaK79bapV2VStKbM27Qhd8KVD-gQyMtJupz1xv47rZpkMP9A6EqVGlRtJN03NnnTLVBQCKChg5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مديرية كمرك الشحن الجوي في مطار بغداد الدولي تضبط أجهزة ستار لنك ( إنترنيت فضائي ) بعدد ٢٤ قطعة مخالفة للشروط والضوابط الاستيرادية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76518" target="_blank">📅 17:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
وزارة التعليم الاسرائيلية:
تم إلغاء امتحان شهادة الثانوية العامة في التاريخ في المناطق المحظورة في الشمال،نتيجة هجمات حزب الله المتكررة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76517" target="_blank">📅 16:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrRSE1K0DmpKt8SZK-f3dINAQkDpI9PmG_KZzHbqXh1paIhAhfWGxLL-eKp8e0RDWoOVVNhViGCYJMvMflsk91QGdUp3csJtj7iC3rSUY8i30CiEbHH6wsXLIeug42vrK7gUOnaXd3gc-P1qDEWqerXVzLgHZ61JRPcBHT7aFSGaSVSSMbL9O6r9xZ9fNWXrBAvUI2if3j9w7lB9tnEP6pzS5bVbDTRH0yXsXkHz4xKIBaIY4g1ba5dH-L5wHdx-cUc1vCzWarD6u70UC8FZEgOJPRm-2DTsQV_zVG3w7-CiYZUVMAgwq_grjL_usV9fFdGmCxX9TVYp5NdUbWoH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
عشرات الغارات الصهيونية على عدة بلدات في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76516" target="_blank">📅 15:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 26-05-2026 تجمّع آليات وجنود جيش العدو
الإسرائيلي عند خلّة الرّاج في بلدة دير سريان جنوبيّ لبنان بالصواريخ والقذائف المدفعيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76515" target="_blank">📅 15:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288c09ebfb.mp4?token=TPGY_TpRO_KnMvSXEPzCl-AvpID8KgXl2kAmg_iQHtPAY-y01YoDegI-88OcNr0OaZjlMwXj3Ac4p0pcySNSreFKhNRNM6KB7Yr5altME_ZJA66vW-_6XEtKHUOzWjYwngDi1tZ14A0OUWWOyOlbYuacHU-oWD-dIe_DrAOMxkhbAsJJWJeRviq0MPMS4AMwEufS8urtuOaGa9BMIaog7aRq_fRKJs3b_9GheLveE2P38oKJzmY7UjVFFebYpARUuBzfQgj2vbfbNiNWKREeycssdcKbQTvZY4nBHuRoUiCXmnYgO5YNKqyAx42-r1IWRbuAQ7fezgmUnaWn1e5aVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288c09ebfb.mp4?token=TPGY_TpRO_KnMvSXEPzCl-AvpID8KgXl2kAmg_iQHtPAY-y01YoDegI-88OcNr0OaZjlMwXj3Ac4p0pcySNSreFKhNRNM6KB7Yr5altME_ZJA66vW-_6XEtKHUOzWjYwngDi1tZ14A0OUWWOyOlbYuacHU-oWD-dIe_DrAOMxkhbAsJJWJeRviq0MPMS4AMwEufS8urtuOaGa9BMIaog7aRq_fRKJs3b_9GheLveE2P38oKJzmY7UjVFFebYpARUuBzfQgj2vbfbNiNWKREeycssdcKbQTvZY4nBHuRoUiCXmnYgO5YNKqyAx42-r1IWRbuAQ7fezgmUnaWn1e5aVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي يستهدف مقرات حزب الحرية المعارض في مدينة تشامشار بمحافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76514" target="_blank">📅 14:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم الايرانية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76513" target="_blank">📅 14:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم الايرانية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76512" target="_blank">📅 14:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW7Pukqvp0NrCIzhwMoViRpktniNZkDK2I6YKSQ-eSC_-mUzjNWSFGXgEPhe5XwJWxSbOcYAc50RvcGlccKHzDCFiWYQ0KmU9mOjI8BYDMR5cpKmgEC2TmFxMGZhre2KUDCxtD0WPA9nMaZzwhMfsv2s6tcYtd_0YMvFdWmZW6hmA4qG0JRXsQ7afLRFUJYrNUY-42yh1U1_73mfWCT0TSlKrS_9kTVxsi43z5EQT5SW6uF4Kb9VWIHJEBhO97jlLczLB_nEhORWpxRt-aFY1B9rS6iu6pPtJjti41ouoxGdAIzrHoC9fbzw_fK-aIDDSC6rBVsOLwB_lnQNXZOkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">{فَيُرْسِلَ عَلَيْكُمْ قَاصِفًا مِّنَ الرِّيحِ} - [الإسراء 69]</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76511" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76510">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
رويترز
: 3 منصات بحرية تستأنف الإنتاج بحقل بارس الجنوبي للغاز في إيران.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76510" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🌟
حزب الله يطلق صواريخ دفاع جوي نحو مروحيات الاجلاء بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76509" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
‏رئيس بيلاروسيا
: على أرمينيا الحذر الشديد حتى لا يتكرر المشهد الأوكراني هناك.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76508" target="_blank">📅 13:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76507">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282721e690.mp4?token=FPkU-S0YydxpMwZ-UmPToi0g280VlFs-VQsw-ew8QsdjPUQnA3oUEB-8LNnit29fJ7kJ4Urf83hATt4NpfGYbaue03KK7SjVIl4TzIIbRv4MuuTgCBV3ozbV10yiZeUGodxtbXRYyhBumvelb-MOvMMZYxa49iqV7VP2Xylw4ANJPza9YEh5-VIRrb6M9yL3jQ6glz1PY_6Obt9m0oQuzKsdUeb53YffUeiJE2_AnWS4SW1pA38DmKCsu5cr48SaAdY73TLwqOnp1BL0XTMXM4G3aR9wkALCjRzaNtbJnEtP_Gwum3dS6W-Ef9B4K6W1X9Bs_BnHwsM9cF5_vhfVW7RrkKLmXwmuKjHZLPQU7w1B_hNlwdIpOaTG0zLrJdVSEP05MDOCeqq0fRY63CqDJjrNjoN-BwDX2B8vl2lhNMGcgRIe8ZeBiCTUz-jTsUcqEQYM7EzrubMD-q3qE1osVMspIS57NZcURx6DrGNUif2NW86nEkpX7GjJ7aDM7towZ6DlD1bM5P8gvp-5s7puFp5GnB8zYSstyChPak1vHxyWyMmqsGeqgZpRlgTbYaOPSuEQnsjnMFj5ulJ8tfw8JyrrCGL7Du1OrZaWEPQLTrcINgzYcq8ln-N6gmrE0N6r1pvig9hgBzZ4820qn5GBUpHhX6uIQUarRG3hHMtVZ3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282721e690.mp4?token=FPkU-S0YydxpMwZ-UmPToi0g280VlFs-VQsw-ew8QsdjPUQnA3oUEB-8LNnit29fJ7kJ4Urf83hATt4NpfGYbaue03KK7SjVIl4TzIIbRv4MuuTgCBV3ozbV10yiZeUGodxtbXRYyhBumvelb-MOvMMZYxa49iqV7VP2Xylw4ANJPza9YEh5-VIRrb6M9yL3jQ6glz1PY_6Obt9m0oQuzKsdUeb53YffUeiJE2_AnWS4SW1pA38DmKCsu5cr48SaAdY73TLwqOnp1BL0XTMXM4G3aR9wkALCjRzaNtbJnEtP_Gwum3dS6W-Ef9B4K6W1X9Bs_BnHwsM9cF5_vhfVW7RrkKLmXwmuKjHZLPQU7w1B_hNlwdIpOaTG0zLrJdVSEP05MDOCeqq0fRY63CqDJjrNjoN-BwDX2B8vl2lhNMGcgRIe8ZeBiCTUz-jTsUcqEQYM7EzrubMD-q3qE1osVMspIS57NZcURx6DrGNUif2NW86nEkpX7GjJ7aDM7towZ6DlD1bM5P8gvp-5s7puFp5GnB8zYSstyChPak1vHxyWyMmqsGeqgZpRlgTbYaOPSuEQnsjnMFj5ulJ8tfw8JyrrCGL7Du1OrZaWEPQLTrcINgzYcq8ln-N6gmrE0N6r1pvig9hgBzZ4820qn5GBUpHhX6uIQUarRG3hHMtVZ3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صانعة الأفلام الوثائقية الأسترالية جولييت لامونت، التي تم احتجازها بعد أن اعترضت إسرائيل أسطول المساعدات إلى غزة في شهر مايو، في مقابلة جديدة أنها تعرضت للاغتصاب من قبل جندي إسرائيلي داخل حاوية شحن غامضة، بينما كانت مقيدة بالأصفاد والأغلال.
كما تصف أيضًا تعذيب الماء، والضرب، ومشاهدة الجنود يستخدمون أسلحة الصعق الكهربي (التيزر) في وجوه النشطاء.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76507" target="_blank">📅 13:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🌟
🌟
حدث أمني صعب يتعرض له جيش الاحتلال ومروحيات إجلاء دخلت أجواء جنوب لبنان القطاع الشرقي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76506" target="_blank">📅 13:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لا تزال صواريخ الاحتلال تحاول اعتراض هجمات حزب الله</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76505" target="_blank">📅 13:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc349f8e1.mp4?token=LdjwkcGm-Ue_kxhKYmUvFsY18dX21SgOi0JLbtCFeTySTwpx_jEH2mL4Cgw4Sx7IZ5B2DDjA0knD7MOr_W_fEAB6dF1REzUHgLu6tz9JdUg1Nk-3qRQtei5ihO9GLL5ERQwpxQeKERi7pOXk9nM4RItr8QpUJChJe1hMiePusYp2RA2r2RbWotv5E8xp9trGPld97skJ_9zjxyKsA4jfLnYNQlU82z7iTsGgzBUSOEJ4vB0_rkIgaTM-ZJAEY-v-1s4HGC3mxMLuNZmbK4VD9Mdth4plWI1cMBiHoHFenpv_n7BN5GMt5gYuYKH1SHcoIecEwPrivL4ClSzaxp6-eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc349f8e1.mp4?token=LdjwkcGm-Ue_kxhKYmUvFsY18dX21SgOi0JLbtCFeTySTwpx_jEH2mL4Cgw4Sx7IZ5B2DDjA0knD7MOr_W_fEAB6dF1REzUHgLu6tz9JdUg1Nk-3qRQtei5ihO9GLL5ERQwpxQeKERi7pOXk9nM4RItr8QpUJChJe1hMiePusYp2RA2r2RbWotv5E8xp9trGPld97skJ_9zjxyKsA4jfLnYNQlU82z7iTsGgzBUSOEJ4vB0_rkIgaTM-ZJAEY-v-1s4HGC3mxMLuNZmbK4VD9Mdth4plWI1cMBiHoHFenpv_n7BN5GMt5gYuYKH1SHcoIecEwPrivL4ClSzaxp6-eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا تزال صواريخ الاحتلال تحاول اعتراض هجمات حزب الله</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76504" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51230d4a55.mp4?token=g8n-SE0bRTHcYqImas4lHS72U2c16l09c3Ld4AsMohGsZnqaYAYD0UlJe-crQJtHWoJdFv7QsJyVMBZOYrpID0cHnkjtx3chjL9FesgVmbb8Wkt5Cu4hIXF5uZjdxPn3hNE65nD95LzFWKU2Y40VM9IuLjjwKcs7lwUpARFoPzVtglMJumimP5Y-f7iAIK8PBVuEQvzhIhOMceHS2YiihPpDG2ntt-uMYhLiF0hcZS8pcIIDLPLhazUIX6uegEfoPuvjzeuF5Q2fxNdAiQgY2Is4sKPfXKn5TlxUGmEX0NO3MUKyKK9e03nmAbf4gWbupJq8cnwH_ki0mHYNDbkIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51230d4a55.mp4?token=g8n-SE0bRTHcYqImas4lHS72U2c16l09c3Ld4AsMohGsZnqaYAYD0UlJe-crQJtHWoJdFv7QsJyVMBZOYrpID0cHnkjtx3chjL9FesgVmbb8Wkt5Cu4hIXF5uZjdxPn3hNE65nD95LzFWKU2Y40VM9IuLjjwKcs7lwUpARFoPzVtglMJumimP5Y-f7iAIK8PBVuEQvzhIhOMceHS2YiihPpDG2ntt-uMYhLiF0hcZS8pcIIDLPLhazUIX6uegEfoPuvjzeuF5Q2fxNdAiQgY2Is4sKPfXKn5TlxUGmEX0NO3MUKyKK9e03nmAbf4gWbupJq8cnwH_ki0mHYNDbkIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76503" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هجوم صاروخي يستهدف مقرات حزب الحرية المعارض في مدينة تشامشار بمحافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76502" target="_blank">📅 12:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جيش الاحتلال يصدر تحذيراً نتيجة إطلاق صواريخ من لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76501" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWNaT65GhoxEXgE2IguzM1ClXcuSVBZqiv5-OrvhBN1RO-1Qa-v4qrI_UazZ--I53JzSI83uuVwBl5moAQCOcw2E_2ZhXODSU5qRZxRokWzZ4ynm7PZkGPCTke7GxO3ZGBBeKpLTbr-goHyCzHGeZb-s7WGbxySFxPMiq_YJuk08f_BWx3aW9CVEyj6OrMv1HvaERGw670ZPYA0JaDiHqredToMt6gDgGyNWC9cLE_K6kp-HaEGidReh5xYROMi85O45gBHGPTGM6hb37_Tn_1fFyNuEHYkz8bHwnpoVpCVPcVCdGAUebuofR5jc2hPy0KlcKM3LXnj_1m3gpMoZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15e46c68c3.mp4?token=rkod94XPwH9upRb256dJiPMDd5c-hnFvmGW5RAWiqck1_B46c4SnnUZNGticnD6Gc8IuTJHQkVm1J1VEh7Bj5gF1NYQ4XISVc-Q4_YB34sAXd5NHbjbw5q7PbV3UhT0pVSJgyMkQRg2wniYhgUF6Acd4KQRsY8tcp-9Pk6IsE5pZrsS2YACnFkVZ3wsZygVflRMfeaG964zRt5_ss29zLG3lip_oyjlsgYhZcya3Tyfmdxi6sRJy5p2wYzEUSU9z6MI6L3fUIHs5Y5pu_FYLV7abpeiO5VjkiMtnpW9SENQ62C1u7OF2Tw5RXltipmVN4cwFKzbKRFQRhHXAiKmH3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15e46c68c3.mp4?token=rkod94XPwH9upRb256dJiPMDd5c-hnFvmGW5RAWiqck1_B46c4SnnUZNGticnD6Gc8IuTJHQkVm1J1VEh7Bj5gF1NYQ4XISVc-Q4_YB34sAXd5NHbjbw5q7PbV3UhT0pVSJgyMkQRg2wniYhgUF6Acd4KQRsY8tcp-9Pk6IsE5pZrsS2YACnFkVZ3wsZygVflRMfeaG964zRt5_ss29zLG3lip_oyjlsgYhZcya3Tyfmdxi6sRJy5p2wYzEUSU9z6MI6L3fUIHs5Y5pu_FYLV7abpeiO5VjkiMtnpW9SENQ62C1u7OF2Tw5RXltipmVN4cwFKzbKRFQRhHXAiKmH3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات شديدة تهز نهاريا ومحيطها.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76499" target="_blank">📅 12:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76498" target="_blank">📅 12:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liDB6BOdBPdjPzxwQXKC8NuVJmvwJAkxhDejKM6uDBbVZSCATzT_HnSpiS2N_5uWKWs37m6Erg9fRht7dev6HeAYYTKdqgumPaQFMJYIeDbjJjrtMvY_xCUAFt050qTsbiSG-LdNA21pkgAhqcw71ziAn-bHzBK4PNpYcdeo26HxUHnJdoNs9d0zYWRiJOG3zr-Qt0MashVxWR8mqoLlM7elr_rQGRlQK5zO68ZATYXOAwQKowMO_dTsPX7sOGP8kbcrGmSotKyM3XDSCB1EDoQoX1Yq1aoNdjPl2nQdtkHEm9QuO3fUJLLw_2O3phOz_5LeJkaGHFyD2pYZoQO3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76497" target="_blank">📅 12:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
⚔️
ماذا يعني ذلك ؟   يبدو أن " إسرائيل " قررت وتستعد فعليًا لتوسيع المواجهة، خصوصًا في العمق اللبناني، وهي تتقدم نحو النبطية لفرض كماشة عسكرية مستغلة الآلة التدميرية وسياسة الأرض المحروقة. فيما يكتفي حزب الله بتطبيق “نظرية الكلب والبرغوث”: تقدم أكثر، كمائن،…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76496" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
🏴‍☠️
نهاريا تحت قصف حزب الله</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76495" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c192cff683.mp4?token=R7OQzx0EdtMlNSCRwpv3Mt1Q41fi4B7hG6f-prd3pARTaLObHY31HZVlZvpXbBwioAa3aERi0l7qOzw8FkQXfot486xHGww4eVigvH4od8AG61VDLR6SBSDcIXSTre-102YvRGveNV-hCTxfjFT0hx3SFGI0v0BVZy9b-LKXNuHKejF2i0NleCQhohpz9qAjASClytXnSefmK3eALp5nmgthXsfihs9ScESMPyW1RdhbxzCcHxlz7TCBH8RSq1KxNi9dtIFVqkV28YL_0b_Uz3RqYwXw05T1cAYQc90WgvtrSlUeOvu30eG2t53fyft7r-lDQvONF9mmMnpKfWs4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c192cff683.mp4?token=R7OQzx0EdtMlNSCRwpv3Mt1Q41fi4B7hG6f-prd3pARTaLObHY31HZVlZvpXbBwioAa3aERi0l7qOzw8FkQXfot486xHGww4eVigvH4od8AG61VDLR6SBSDcIXSTre-102YvRGveNV-hCTxfjFT0hx3SFGI0v0BVZy9b-LKXNuHKejF2i0NleCQhohpz9qAjASClytXnSefmK3eALp5nmgthXsfihs9ScESMPyW1RdhbxzCcHxlz7TCBH8RSq1KxNi9dtIFVqkV28YL_0b_Uz3RqYwXw05T1cAYQc90WgvtrSlUeOvu30eG2t53fyft7r-lDQvONF9mmMnpKfWs4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
غارات صهيونية على مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76494" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmzmq996L9_wjF_MKmp_YV-ZRYPw-981C9JPnbUHlRNRXPGplrnx2Y2tQUy2JNzjIXn0j-QtUIuLiMcoH2xe8lofA59OWeHbOo2W0ddgCiATQ0rY_-_kblALp1oBmdi7Gp3C0u3biEuXOP9Z8KZwqIb_HJfvS6aqhRl02cC_UMny9DxqcMxLm1dTryQflyj2uQsjdPKy8RWVPRfvBYswKZg2gNu7Y6XR-bcsYooukU2-cVlbm2mCvJfQxqnmI3g72Xn3AG4FfNjo3vCnU6AZas103ZdzpiNWaWuNNqC9pDsZxycPlKQc499udngXHhfUp6e1zYsWTWljGb39VoQTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
تحليل أجرته Ynet العبرية:
يظهر أن إسرائيل قد وقعت في فخ من صنعها في لبنان، حيث يوفر عبور نهر الليطاني عنوانًا رئيسيًا مثيرًا، لكن دون استراتيجية خروج واضحة، مما يترك جيش الدفاع الإسرائيلي متورطًا بينما يوسع حزب الله مدى صواريخه وتهدد المحادثات الأمريكية الإيرانية بسحب البساطة من تحت العملية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76493" target="_blank">📅 11:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM7b12bf_8OHnSPeUWbSSpC3VQC8kWxRugvFZZSvdm-YO2A61eVWPRMWxwUWOFpEmsjorPL_fKkxjlDdGoDr2asGZDb7L7ee1yarbz45h8Ef49PHpdN03gcAG_NAy9xNyTjKqTmAtH0UfAnhRxgboWymDLSOZUKSKRUw47MLZVBFctiIVJfAS5yt3BW0k3NsvDgJ79Aho8Kui1ikQ81Qz2vlgyGKrj-P6RtEnAIfvh5iXrEt1DrpouG-X2UiOjGofkwP5_70PY7L8IMawP-klFao_aJbeJfr05FEDS-7zid5WlimwKr_lMTahNo8upFzpNZTGOE8lolAe0uHPB3gGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
انفجارات ضخمة تهز الجليل الأعلى في الشمال المحتل.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76492" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e1090629.mp4?token=vZNH7GtAX1lNMxyl1zq9RK5ahHd-ogTZvz4EZVUQ1pux8bien9VIySr3d5ZLUd90y18YmWNnFzD27RmTc2Cw0ZBpiHMzJqhFQVDcPO1Ys4uKGUF0T8xU7nZoDw43ei8ekFkBFjs7BtfalXCn2h8FHQzPD_E_2VvmR9Q86dpil5BG_zYJg58NmNhTusWfudQ6gU5znTT39Z5MXH7eYtE0bbpd_wuEjXckkmma71K-dwtqXIcqeUg3rml-8_hJ7PESP6ONJuDklDdY8hXcz6WvmoSRAsYRm71veOo9NoL0minM_7XMZaPqSrg9kiynpw-RQHEWQEQ7dWxZXNVYDrRTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e1090629.mp4?token=vZNH7GtAX1lNMxyl1zq9RK5ahHd-ogTZvz4EZVUQ1pux8bien9VIySr3d5ZLUd90y18YmWNnFzD27RmTc2Cw0ZBpiHMzJqhFQVDcPO1Ys4uKGUF0T8xU7nZoDw43ei8ekFkBFjs7BtfalXCn2h8FHQzPD_E_2VvmR9Q86dpil5BG_zYJg58NmNhTusWfudQ6gU5znTT39Z5MXH7eYtE0bbpd_wuEjXckkmma71K-dwtqXIcqeUg3rml-8_hJ7PESP6ONJuDklDdY8hXcz6WvmoSRAsYRm71veOo9NoL0minM_7XMZaPqSrg9kiynpw-RQHEWQEQ7dWxZXNVYDrRTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
صحيفة تايمز أوف إسرائيل: جيش الاحتلال الإسرائيلي يسيطرعلى قلعة بوفور (الشقيف) الاستراتيجية في جنوب لبنان كجزء من الحملة المستمرة ضد حزب الله.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76491" target="_blank">📅 11:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af04a6e44.mp4?token=E-iOIvny7qzoXHBYpY93lHo2ebX0nfJYaZBDrYcBxECTSWr3UV3ilFFL0PvGHfUTVkrXADajTIRxhAOW7uFFIeuNIpLJZ7VfcDW3_LYas3buYBne7srNhWvtFctCVigiaIrWYYtqL3BEqL5eo2TM_dCXdHFUQyoji0WxgmLKwGK1Sfr_w6Mm5OE079YG1UAHosPpeSkoqJDeH00pEjbgaiLMeuRiFnhvKMpLuJq9dTpci4IIxcmrJCjVqj9Em63fEcJvmqIkZgJ52UqCJ_Nq7SbWNn7Gn-2pEVAhJFH3rIVoLVC6gHkCHhvqBxiXO-MRjTzhrPgI6fTExGaJ7wQF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af04a6e44.mp4?token=E-iOIvny7qzoXHBYpY93lHo2ebX0nfJYaZBDrYcBxECTSWr3UV3ilFFL0PvGHfUTVkrXADajTIRxhAOW7uFFIeuNIpLJZ7VfcDW3_LYas3buYBne7srNhWvtFctCVigiaIrWYYtqL3BEqL5eo2TM_dCXdHFUQyoji0WxgmLKwGK1Sfr_w6Mm5OE079YG1UAHosPpeSkoqJDeH00pEjbgaiLMeuRiFnhvKMpLuJq9dTpci4IIxcmrJCjVqj9Em63fEcJvmqIkZgJ52UqCJ_Nq7SbWNn7Gn-2pEVAhJFH3rIVoLVC6gHkCHhvqBxiXO-MRjTzhrPgI6fTExGaJ7wQF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
قوات اليونيفيل تنسحب من الجنوب اللبناني بعد اشتداد المعارك بين حزب الله وجيش الاحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76490" target="_blank">📅 10:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6piE78mDi4teCiDgeICiu6RAkzefnkI3umWoD6ZLBZ9Ln_-8W6X8QvmRjCD2ASl6TRXo-eKy5pkhtagVU2k7454CKQ5VdV6ewk4LNuyoLAxYcWG4z0Yu0jOeV9xLZUBcoypyTczxPiQNz9aIqBIl5dkVrZ7S8SPMVaEF96gErq1HNnFw98cEWcRICfn7Qt-gLODsAxEszj64j6RHA_xjINwtCMMhqRzpps-CYQAlOrcJJLwVoFtnkcSwL4VMerOs-ip80Jhw7K8NjH_KRmJngXrQdCH5v2OkSRiuDePb8THxL-UJQQzS6fOFpb8_pdTWK6b1M9GyrxklDtssMd_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
رصد هدف مشبوه لنظام التعرف الآلي (AIS) يدّعي أنه ناقلة نفط ترفع العلم الأمريكي بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76489" target="_blank">📅 10:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCyoCe9AvF6p__hiGu5H3butWtY6O26euaTRMwv9wPo8zDKh3yaUSPSPUvlMfFX840aW8sjU1e9-YKLskerl83q-WDojLH0yo-LZa-_Fm_Q2ID8lvFPmUX8Q_vGMQWYyDu1hxgxhz8Tt6nlgQvfXPaUxFffzdjOws_FN2riPdtIiBUy9g82Ue-jN9XxfUbUhy2TMdEuCTIpRGKGc7KNepdExTP7fCjY-K6pU62-8jnZbJHZwEtX8jlYhsk4m2_Z719kk9MiyMOKXvogMexz2FYg0voizuvRcdJkt1YJ6bBKvjvdyzq429FsFpw6dqosX_C3UAtSVwQvTY-1C8wws2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
نيويورك تايمز: يحاول ترامب تصوير حرب إيران على أنها على وشك الانتهاء ونجاح كامل، لكن روايته لا تتوافق مع الواقع، وبعد سنوات من فرض روايته للأحداث، يواجه الآن أزمة تتعارض مع قصته.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76488" target="_blank">📅 10:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVr4P42xa8PAqZYjfXXjddj6Ol-dRjOmVugQx0OrLQlJublNWkQARmdCFAU4abjUFBjfuBJ22VFsRhcgLYQYg3fJoC3Ysfr5JIblTwxB0m2ZkKyPsI29eR_T0E-UuBOp7T5Gq7xKDWGJygzFObOd3wB6W102MxHlJVqxqapqSBcxe4mh9YPZlKynAJI2Ww40yht3Zg5ivt36kbNMvl9mv-Y6ck2fIjTs0idLRhmAbNISalcGMCyN55hLCSiSSNzVJ5Hi7-Pd_Xui4-i6Ga-exP1i0iKnACACbzgjUfTk9WI67SXg-OnbCei_6379xDEAvovtklM1UYtKRDy0yjLQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
صحيفة تايمز أوف إسرائيل: جيش الاحتلال الإسرائيلي يسيطرعلى قلعة بوفور (الشقيف) الاستراتيجية في جنوب لبنان كجزء من الحملة المستمرة ضد حزب الله.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76487" target="_blank">📅 08:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ترامب:  ستكون قاعة الاحتفالات هنا.  يُطلع د ترامب زوجته لارا ترامب على كواليس بناء قاعة الاحتفالات في البيت الأبيض، والتي وصفها بأنها هدية منه ومن "الوطنيين العظماء" لأمريكا.  "ستكون هذه القاعة الأروع من نوعها على الإطلاق".</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76486" target="_blank">📅 08:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
ترامب: تنتهي كلمة "Dumb" بحرف B، لكن معظم الناس لا يعرفون ذلك.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76485" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvK24LSSUq0IcUUlymqA_rIm6lNahk1rO52xf4SsRCRnsyyLGIvDTn6U0SjVoV7YsDqjdwmoJ72SiT1a3oVvIqvXEA1PjcqxjA5il5E6tWxRoxI_8eXERc8Lj3rZrz0bN8T6dBnoaKCb_Y5nwWQf_qLhrSqZziNUXRWGJ4CMj8-8DFttB57NYlxAqb7G41mRLuoukZfOZYFWjwyaoLJ5_67QyGRGm-M0hTO28OypT8wbddTQmwN4bZzA8gZLdqpFKocFJm5bcedlqZ84pykt6rxuspLkx_uzmYinuOoE30Q4z5xBUZttIo6T_l7-iwIXqveHflaOdLfQYZ5tsG9ABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
كانت نتائج الفحص البدني الخاص بي، الذي أُجري في مركز والتر ريد الطبي العسكري، والتي تم إصدارها للتو، جيدة للغاية.
على عكس الرؤساء الأمريكيين الآخرين، الذين لم يخض أي منهم اختبارًا معرفيًا معتمدًا عالي الصعوبة، سجلت 30 نقطة مثالية من أصل 30، والتي تعتبر "ذكاءً استثنائيًا".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76484" target="_blank">📅 08:33 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
