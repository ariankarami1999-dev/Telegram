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
<img src="https://cdn4.telesco.pe/file/nrpSN10HLcftzlyOmHlW0YFm-bAsj5Htns0A75yny8FP5OhbCqbNZSrqvorwEMnqnK1ABsOOkBIewo9qdTmfcdvTKEJlQRblYQjfEPI46OlhmAgZuzyP4RwUVAIP-RRucVwmCWcD8Sqn-vNNdEsPFD4tjdek8C0_69446Qo9dB2Nd5KNY2bnGOqVhEumt25eMjLuj2Yv_eZxqwPYYG08s8r4l4GOs2KN8ZWk86rsfYR_23eySVFpfq8rvmYncICNr0EejpG4oRwwJ4L3a_18BoN5pfi1TKomtV_Z2pFh5dYR89vd2ZAqZFvJrQjoOVw2TdPmj0mg8e-TfDQtmfmCVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 08:43:31</div>
<hr>

<div class="tg-post" id="msg-85294">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
محافظة خوزستان: لم تقع أي عملية قصف صاروخي من قبل العدو الإرهابي الأمريكي على مدينة خرمشهر في الليلة الماضية.</div>
<div class="tg-footer">👁️ 131 · <a href="https://t.me/naya_foriraq/85294" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85293">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
هارتس العبرية: في "إسرائيل" يجدون صعوبة في فهم شخصية خامنئي الإبن (السيد مجتبى)</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/naya_foriraq/85293" target="_blank">📅 08:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85292">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">4 انفجارات تهز قاعدة عيسى الجوية في البحرين</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/naya_foriraq/85292" target="_blank">📅 08:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85291">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/naya_foriraq/85291" target="_blank">📅 08:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/naya_foriraq/85290" target="_blank">📅 08:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/naya_foriraq/85289" target="_blank">📅 08:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85288">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyYovb50YgxAYp0EocrubXYbk_FzfiSJlMa6CyI91xygiqvmSz4Dh466lCC4ypO9JbuAAgAexnyko9F3RDeUmWJnauOUn9nGQUoLUbw8r9R3Tk8Js8-KUUtd7aFzfPEfNRM_BlCMsXbCYGxG62K1YWGAsia0eE9fX9lRDy5hP8ph8g3g-1-RxUkYgJvfHVkfvprpoKwKd32ZLuboO-u1inrdZ94GGygEhRkXGxvbjkOba69Y0SMgjmQ9-qZTvFoEYKVqeH00V_n9ZqOg9h4b-A_SWFS8TeCpZGdk5_zKWxTHGFAicV3RIrcYpt1r8c80ugJQGMEt75tlFk3CyTU0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/85288" target="_blank">📅 08:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85287">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات في مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/naya_foriraq/85287" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/85286" target="_blank">📅 07:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX3Z_ZpVkzIPS4NEESdlbhsLBV0uXrwlFjXm5WbxX7p5T5n5ZDzsnsyiYDp_RDbUuJ8M3SJunMKR2znF0RWDHXjWJdJxid1igflo5eUv70P-fY_CJK-JhB9pra5rme3fyNIWT-tje3IwUkwoFhpM5uS3qPEIcbwdAVbCMnRxctoZ0AeFkRGvvMqUQqcHHfC5W-qS5DKCfhSWHHyElJOz8X5Mi624t7kaDj38EwF2nKjPfvozEve0gT4plbrgo2wk5PUlKUgU_EXTEL1uTjVMrGmCLCUZMGdxCa52D6aWn3p_jOF6a7SHBdR_svPilSp1A7t7e1BrfqeMypWqAFrXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفارات الإنذار تدوي في البحرين نتيجة هجوم صاروخي إيراني</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/85285" target="_blank">📅 07:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏وول ستريت عن مصادر:  استمرار الحرب مع إيران يترك آثارا شخصية على ترمب ودائرته المقربة</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/85284" target="_blank">📅 06:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6b49a5ef.mp4?token=gvUj784kXNuWr9FyhbvAj3jiuTAN7bHp3fmyxSIeC_JpaIWuSRC7Umkd5397XoQq1OwPQv1HwmcDCHfL7lP9af6W6cl-9prNv7FmSqazmngo32sD0dvGcObtAYJFsJcL4YyaSJJMqycgjGfuhcI8-qapn9eKX6lL1nVnPrd8m2rk7QO5j_34H65ZvP7e0WvVDHSQyezNgHtu6WvJ7QEa9AsdU4VrZewJredqvMAS01zq1wMBMMYXoCf7MdO2Kd4w9jXGuSs3t2yDGkCOb2OmmVDBllgBZBjJQaTnO6kDFUK2a3rPlLYzRnAGLlaER2B93_ECWB_Uj35aPqnc9HaBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6b49a5ef.mp4?token=gvUj784kXNuWr9FyhbvAj3jiuTAN7bHp3fmyxSIeC_JpaIWuSRC7Umkd5397XoQq1OwPQv1HwmcDCHfL7lP9af6W6cl-9prNv7FmSqazmngo32sD0dvGcObtAYJFsJcL4YyaSJJMqycgjGfuhcI8-qapn9eKX6lL1nVnPrd8m2rk7QO5j_34H65ZvP7e0WvVDHSQyezNgHtu6WvJ7QEa9AsdU4VrZewJredqvMAS01zq1wMBMMYXoCf7MdO2Kd4w9jXGuSs3t2yDGkCOb2OmmVDBllgBZBjJQaTnO6kDFUK2a3rPlLYzRnAGLlaER2B93_ECWB_Uj35aPqnc9HaBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاقات صاروخية جديدة من إيران</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/85283" target="_blank">📅 06:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd05236fdc.mp4?token=nsVM63AiVwyFnhB2fFFXU6jEN-BnQIo5QKiQXYpdqb3A1gm-Q_Io4k0leXGvy0Kto4u5Wyj4katajx3OBvnz8ewzFBidjcG51LLqQbIsT0dLJT8op2qe-2XCBuFI86-74bzXgujSW-1JIgsO5sOmKATsxiz3qc2j9m7Tm8r8KolcA02o6yQVKzb3Tuc9HAXespTt3kGAs_Cwj2YwtwMHYZd1_4b74_-F6Cj58XPBf94RoZxZVNWojZJaWkOZTB_8hobVynRWbbY_KLgQtTOxdAfRGye3NwHjRzQfvcR9OF2M2XGl_7cYHdKuqWg6Hn7DTkqzWG9JPSLHpZtzPSqnDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd05236fdc.mp4?token=nsVM63AiVwyFnhB2fFFXU6jEN-BnQIo5QKiQXYpdqb3A1gm-Q_Io4k0leXGvy0Kto4u5Wyj4katajx3OBvnz8ewzFBidjcG51LLqQbIsT0dLJT8op2qe-2XCBuFI86-74bzXgujSW-1JIgsO5sOmKATsxiz3qc2j9m7Tm8r8KolcA02o6yQVKzb3Tuc9HAXespTt3kGAs_Cwj2YwtwMHYZd1_4b74_-F6Cj58XPBf94RoZxZVNWojZJaWkOZTB_8hobVynRWbbY_KLgQtTOxdAfRGye3NwHjRzQfvcR9OF2M2XGl_7cYHdKuqWg6Hn7DTkqzWG9JPSLHpZtzPSqnDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاحتلال الأمريكي يحاول اعتراض الصواريخ الإيرانية فوق قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/85282" target="_blank">📅 06:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1pXWfmgtF_3xzejbvkfG9Z7Jt4adYGvYfPD7wGkkLMhuJBqyCBuynX7p8_A5JbQ7yxq9S54Jr7Nqi9MnPBEPeAB6SPNdAqBOp2pEKpDefCHNPmq-5wMnTWcuAtVK4ulrXkwJHSJgEfl-ZLhr57iK6mWqSz10-FqUraaUZ0OPRfYXWJKVsUmpSuXaQy-YoKzLykwrxeLTbY7CE0JjZaI1E-ZQM4DCLsGviEAyyt4kEnxi4yNKoo9pQ9rVReEgnfPABV577MrHeyDmlLrMXi7caqlF1YfZq9qdeRWqv-EjhQHueOcoTtIyO_lQkLkTQD6CczdDWiZWcBVO2RsGr2Yqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاقات صاروخية جديدة من إيران</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/85281" target="_blank">📅 06:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd26e288d3.mp4?token=ZwmBGn5qyw62D5PpialMJ3YB6wzoYhHm4NSUpSHwdUQKW4-2mi9DXtd_7ei7weeMeJcUhcNAGNSYboVSIT9lcH-Jmh2C6xriHv0RL59JvwimTqcXSe2k1s51rKOU7NkMbRdQw9PNNPUPRoFw9L5pf72269w6nx0CEogYNIC9YV5LuUljZ3IxVdUHlfHdQeaguBGGaXpC_B2holgx5mPA9T3p-E0VnJ3uerMypTxxQytxoFy0S7yg0xFdH0ED8PpWu5kJpOuZEk_e61q5KtjIv0WGg7rbDyhBHtLpEfJcfSFwoGLwOXSM7F97IoPLZJT9hJ1YH9CBU2vjpFNU0rz-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd26e288d3.mp4?token=ZwmBGn5qyw62D5PpialMJ3YB6wzoYhHm4NSUpSHwdUQKW4-2mi9DXtd_7ei7weeMeJcUhcNAGNSYboVSIT9lcH-Jmh2C6xriHv0RL59JvwimTqcXSe2k1s51rKOU7NkMbRdQw9PNNPUPRoFw9L5pf72269w6nx0CEogYNIC9YV5LuUljZ3IxVdUHlfHdQeaguBGGaXpC_B2holgx5mPA9T3p-E0VnJ3uerMypTxxQytxoFy0S7yg0xFdH0ED8PpWu5kJpOuZEk_e61q5KtjIv0WGg7rbDyhBHtLpEfJcfSFwoGLwOXSM7F97IoPLZJT9hJ1YH9CBU2vjpFNU0rz-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الأراضي الأردنية لحظة وصول الصواريخ الإيرانية إلى الأردن قبل سقوطها في مواقعها</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/85280" target="_blank">📅 06:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e5840a91.mp4?token=WTlLpsxc9bZ1x2R7CSRLiCB3QgZQRcitUowxyO1V5hKNV-7lqVM-nvFRTdxz2E_TQ5Kd8sHVHVyJ4FBAwIX77-Ot8w-iwtglXMOSWEubmVrIErYfGnwv-Mgs-rkwV6KdOHQBolboLvfcyYZu5PMSpPGEhYGuKoVXwlWoIKR-3nathhf-oUBeC9bPUftnKntX5cA5UMgrzkoSlTTDKs_CRAXQOO_t8lMI1HxvxqWfkl-e59qPgjzynAzOsvJehNeNs6u6UG-rUSps3OmPvzNVVOx3z7uyHrDIiI-kJBGxRYMLBhRm_lYe1J2RTalc1NmcJ_Vg7RH_Wl5-TnwmDTDDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e5840a91.mp4?token=WTlLpsxc9bZ1x2R7CSRLiCB3QgZQRcitUowxyO1V5hKNV-7lqVM-nvFRTdxz2E_TQ5Kd8sHVHVyJ4FBAwIX77-Ot8w-iwtglXMOSWEubmVrIErYfGnwv-Mgs-rkwV6KdOHQBolboLvfcyYZu5PMSpPGEhYGuKoVXwlWoIKR-3nathhf-oUBeC9bPUftnKntX5cA5UMgrzkoSlTTDKs_CRAXQOO_t8lMI1HxvxqWfkl-e59qPgjzynAzOsvJehNeNs6u6UG-rUSps3OmPvzNVVOx3z7uyHrDIiI-kJBGxRYMLBhRm_lYe1J2RTalc1NmcJ_Vg7RH_Wl5-TnwmDTDDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من انطلاق الصواريخ الإيرانية نحو أهدافها في الأردن</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/85279" target="_blank">📅 06:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dddaaef9.mp4?token=lzqojNzGbwggok2NLLrO8sZ-vSDmubG4dgSi0RTo8TSLCBOQ5iZwFn7t6cLNMSFCnz6m8onHxfw-v42-15IExYJcXbVheOJm8fkFYy0JV5uYjc_Z7wq3RzECISTPyWmqztPVNDNzMxOFVQglJfRgjXTAkluSgRCzkta3Y3qO5Th8jMcHQYtMym8Wy7EqlqEpkUPbBYzxjdgdazT8tmnT0igWyfBJrRAkDO9KCrVU5gM77SE6iH9YApMscByGuj0RxMBByvBB3SpzaaEdxm3EEdNZWTris1mMsN9SzHQHFtpbBpcpeHpJqFbzYCui3-l8mJvhCUYvNIolN-QRHzy4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dddaaef9.mp4?token=lzqojNzGbwggok2NLLrO8sZ-vSDmubG4dgSi0RTo8TSLCBOQ5iZwFn7t6cLNMSFCnz6m8onHxfw-v42-15IExYJcXbVheOJm8fkFYy0JV5uYjc_Z7wq3RzECISTPyWmqztPVNDNzMxOFVQglJfRgjXTAkluSgRCzkta3Y3qO5Th8jMcHQYtMym8Wy7EqlqEpkUPbBYzxjdgdazT8tmnT0igWyfBJrRAkDO9KCrVU5gM77SE6iH9YApMscByGuj0RxMBByvBB3SpzaaEdxm3EEdNZWTris1mMsN9SzHQHFtpbBpcpeHpJqFbzYCui3-l8mJvhCUYvNIolN-QRHzy4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تدك قاعدة الملك فيصل وموفق السلطي في الأردن حيث تتواجد فيهما القوات الأمريكية.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/85278" target="_blank">📅 06:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaxMC4mu47FKUJAes28PGVGmlfxMyQeswiL1FeX8qlyySTv-asd2ZFF3xtDdU7PZRnbUFDe1JXh3VYDuvuhLpArSKOZ2_IOG4sLdqILHK9eS2EBfn074802P8M0RagFSup1LHjzjAE5_xS4nR90q-aGXr9mFac9dSHKE41PiWYJ1edk3p-RcJOuNXXlCEX3LYPpjQdJhCShhWwqAgs16mB6VbP7IHehmfEVrzMgsYb3n525m7j4y6-2axHy9hPLGDJBd7IIL9umrxpPEf3PEMn8XNCUsMGneCfwX7VVHyjid7IIaJ4f55hqgUMnCQg7kqE55zHDqFLWlbIcCOci8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاحتلال الإسرائيلي يحاول التصدي للصواريخ الإيرانية المتجهة إلى الأردن في سماء محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/naya_foriraq/85277" target="_blank">📅 06:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4febbbbc29.mp4?token=mZeK6Vwh_2Z-Bl1c3L_HKJ7nHrjfi62tTCRYQ_IOtBtypQtw99jWA_iE8kGB86t7rYquf-588YVKdodloQCguqAMBetOyyPCzHOwOepXD9YrDH3LZiMUYqe_Paw-ARBdtap-YYQUmBR87w9UNpNOZj1B9DT1g7WdSLgopzIR1gxKIy3ckhoYCsSkfsm3P-iOCXSmijFLvG2Lqm3KhAYHwnlnibI7q4Osd570qzMGmdTc56ogv_uqK7jFPzGmx8P1xrGdlzqugMyd-mDC--z4Qu_AxruWoNZyqWDLswu8I93Y6mIDJvw3bLJWe88CTB1oDA5jhxa1cPqI4pVaqfd_Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4febbbbc29.mp4?token=mZeK6Vwh_2Z-Bl1c3L_HKJ7nHrjfi62tTCRYQ_IOtBtypQtw99jWA_iE8kGB86t7rYquf-588YVKdodloQCguqAMBetOyyPCzHOwOepXD9YrDH3LZiMUYqe_Paw-ARBdtap-YYQUmBR87w9UNpNOZj1B9DT1g7WdSLgopzIR1gxKIy3ckhoYCsSkfsm3P-iOCXSmijFLvG2Lqm3KhAYHwnlnibI7q4Osd570qzMGmdTc56ogv_uqK7jFPzGmx8P1xrGdlzqugMyd-mDC--z4Qu_AxruWoNZyqWDLswu8I93Y6mIDJvw3bLJWe88CTB1oDA5jhxa1cPqI4pVaqfd_Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن تشتعل بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/naya_foriraq/85276" target="_blank">📅 06:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85274">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d31a0f52.mp4?token=L10nSY5CFLXbxLVkAI-RkfnOMav-SgDSzS0DYvOxMyXOpE15P88C37TOXQl1C4Qopih4G58CBmPSgAsmkfA_cO3SZkhoVQ1XBByWJBcOe5eS5y2wQxgdRm101ctzU4QDnLA8j44RXZOTrJ6PPuvCQubVoolVuspSATBuT2Z0SgKY4S-cPexPOhIi6sAn9SxU-50DXmma7kg_DFA4hUy4Nzj-YMQUKrWX82d_6nZMoRy_biE8Wajwe2UM0tyYvLjHlbeWElWO0bsJJQ8YSdf1XFBGesz6MM-lSHXkEzeEClVZzp1L1IUj1UILxCqx1zPMt9Zs1I4Y7CsEguMlxGw5DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d31a0f52.mp4?token=L10nSY5CFLXbxLVkAI-RkfnOMav-SgDSzS0DYvOxMyXOpE15P88C37TOXQl1C4Qopih4G58CBmPSgAsmkfA_cO3SZkhoVQ1XBByWJBcOe5eS5y2wQxgdRm101ctzU4QDnLA8j44RXZOTrJ6PPuvCQubVoolVuspSATBuT2Z0SgKY4S-cPexPOhIi6sAn9SxU-50DXmma7kg_DFA4hUy4Nzj-YMQUKrWX82d_6nZMoRy_biE8Wajwe2UM0tyYvLjHlbeWElWO0bsJJQ8YSdf1XFBGesz6MM-lSHXkEzeEClVZzp1L1IUj1UILxCqx1zPMt9Zs1I4Y7CsEguMlxGw5DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في سماء الأردن عقب وصول الموجة الإيرانية إلى القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/naya_foriraq/85274" target="_blank">📅 06:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a1a7390.mp4?token=Gy0N4onlWS--_zNl9jc1LTKCAtDmFW0yep4q8fDIktivZs6WRaGcUvpp6J0P69Oy7nyikqelkMKpTzVxnupfT5DynNOE2l_6T0A7HVMSfdn2Sd1s_UGqW74Z529P9gMSuYLHAlL4GoJn-ya6jDxn804-6fPT7PdsDc7_l37hJYVaxbMpibJ4BEIU1UPbDqE7b5a4l9UFcAAz6KBO4vrXjfJevO7unJAP7AkHRPO62l8p6w5BolfRhzbM-VZk1espVlE72SxB-raoFfwB1Tu-7gmTrUMsgghoSOslKl-ZOpY9WAdD5T3lg4plW8boQia8XqpIlO7jYSj3iSZvUCUKXRSxRa7cbT5Tld9XolgMCmDNWB76LnSUux0E4zg2f4075bnen1g4GDrD4D7cl8b8xoZHU585Y7Zn2VhStN1pWgD2Xzp1CegSD6y2mz3isNv8qA_ElYUMDTceq9CUq6z0aeu4e0yQhsDCoYfusDJQOj2yTVfQyxb98wRCWgKMlQF3h7YU_J_CLfMUGNsTHiAj12yx-PSvNH6sLeCl8M28R6dgyNX39BKej0jDkfaRyenWMan4d8IwuTBljMjB8ht5TcInfM6rBkbog87u6-obyRi7P-N8AtJXovD81dLjMU3_uvShQaEuGGaFXPuB_umZZcJVXm316r9S7FfxAWz0vwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a1a7390.mp4?token=Gy0N4onlWS--_zNl9jc1LTKCAtDmFW0yep4q8fDIktivZs6WRaGcUvpp6J0P69Oy7nyikqelkMKpTzVxnupfT5DynNOE2l_6T0A7HVMSfdn2Sd1s_UGqW74Z529P9gMSuYLHAlL4GoJn-ya6jDxn804-6fPT7PdsDc7_l37hJYVaxbMpibJ4BEIU1UPbDqE7b5a4l9UFcAAz6KBO4vrXjfJevO7unJAP7AkHRPO62l8p6w5BolfRhzbM-VZk1espVlE72SxB-raoFfwB1Tu-7gmTrUMsgghoSOslKl-ZOpY9WAdD5T3lg4plW8boQia8XqpIlO7jYSj3iSZvUCUKXRSxRa7cbT5Tld9XolgMCmDNWB76LnSUux0E4zg2f4075bnen1g4GDrD4D7cl8b8xoZHU585Y7Zn2VhStN1pWgD2Xzp1CegSD6y2mz3isNv8qA_ElYUMDTceq9CUq6z0aeu4e0yQhsDCoYfusDJQOj2yTVfQyxb98wRCWgKMlQF3h7YU_J_CLfMUGNsTHiAj12yx-PSvNH6sLeCl8M28R6dgyNX39BKej0jDkfaRyenWMan4d8IwuTBljMjB8ht5TcInfM6rBkbog87u6-obyRi7P-N8AtJXovD81dLjMU3_uvShQaEuGGaFXPuB_umZZcJVXm316r9S7FfxAWz0vwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في سماء الأردن عقب وصول الموجة الإيرانية إلى القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/85273" target="_blank">📅 06:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b308e2eb6.mp4?token=NklyhlbBRr60rFvfWEUlEtZ5_ThI0PrAoiDk8Ivz2gJT7gSYuDDQiZFe1MwRkUFlVcZ7yPHoE2a7KwWRzTh7IuqHENN1YZys3kynopD3_MW5YfWFzOJVihGTOATEAsKsedyJ1-W0i02yuCS-ZgOfODISjjjCLxN8zSWbzGam2XMJAGxwyo3sX6ftuRTxwjXv_y50wIdni5oKl_kKU7VyaALbgoK2mKhK6NL9l81ACqabDF6KUdDIOgWIODk0-HoajBh3Bt1EmBQxUEFP_bvjBw4j1xBHEULklwWKxbmwZSiXEc_QwE_j_Ksyr4F4hmY-SHFlHweow6xm9DWKWxPVurOrP3PfHNVeY4_rdIlrl764I50CksCQi1ioxjKd27BVMmlEWGQzP-m-1uI25nUIgoS0uQr5xvEssFEKl8JJPU8uDYcpPHCLo_UC1GnmwzpjkJOaYCAzttmvG1f5WV4hSBgMTUM0KbIJGFxtIwXXzOTvPRGYQsRzZkMyfStaxMh8Dyk4YPwSabT_gaZrjR73BrIc2IFGSx5d6BQuphO-IjNZzLL0icmRYRIVkgZvEvDKajdjbH13_HkIoO4yJ8NzN3NJvYzT-7_NAia6mxTqxXro5PLXboYGfc_cEzBktMyGyiY88gZjlCmoJcjnETqErdruJg9Nkz59qndUSdIMlbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b308e2eb6.mp4?token=NklyhlbBRr60rFvfWEUlEtZ5_ThI0PrAoiDk8Ivz2gJT7gSYuDDQiZFe1MwRkUFlVcZ7yPHoE2a7KwWRzTh7IuqHENN1YZys3kynopD3_MW5YfWFzOJVihGTOATEAsKsedyJ1-W0i02yuCS-ZgOfODISjjjCLxN8zSWbzGam2XMJAGxwyo3sX6ftuRTxwjXv_y50wIdni5oKl_kKU7VyaALbgoK2mKhK6NL9l81ACqabDF6KUdDIOgWIODk0-HoajBh3Bt1EmBQxUEFP_bvjBw4j1xBHEULklwWKxbmwZSiXEc_QwE_j_Ksyr4F4hmY-SHFlHweow6xm9DWKWxPVurOrP3PfHNVeY4_rdIlrl764I50CksCQi1ioxjKd27BVMmlEWGQzP-m-1uI25nUIgoS0uQr5xvEssFEKl8JJPU8uDYcpPHCLo_UC1GnmwzpjkJOaYCAzttmvG1f5WV4hSBgMTUM0KbIJGFxtIwXXzOTvPRGYQsRzZkMyfStaxMh8Dyk4YPwSabT_gaZrjR73BrIc2IFGSx5d6BQuphO-IjNZzLL0icmRYRIVkgZvEvDKajdjbH13_HkIoO4yJ8NzN3NJvYzT-7_NAia6mxTqxXro5PLXboYGfc_cEzBktMyGyiY88gZjlCmoJcjnETqErdruJg9Nkz59qndUSdIMlbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة للصواريخ الإيرانية في القواعد الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/85272" target="_blank">📅 06:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR1Irr1I8VvB6gkkW_8O0zYBQcHhPhW6ToxOsW_T2IW2DQqim_7ixJDt_rnSVuqg-wTX3KGyOi_Otv_89j8ZOUqL-cAXYWQZJV7L1BS5UziVLEIcP5YtjwPpbIZIkmP1FieCe2pZHyVNCYEWfV4-zLRbY-6LFZlQuM1GBTqSLBLXmeek3wXx0AfEOBHMQQiYmDxOFOeHFvKzSfYYhBMH56CmpIQE--IzbXf7QseSDT3gUWrWZpp8bwA5NssVG_dKtvPyj5aUkix5khCRgT41vk2tb4Eoq2YTU8REx9SUx_v_jcWN4O0rpjEAaLieRTSSrvgK_W3PghNFoFvSqHldjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
إن الاستيلاء على أصول دولة أخرى لدفع مطالبات مستقبلية لا صلة لها بالموضوع يُعد سابقة خطيرة.
يجب على أولئك الذين يحتفلون بهذه الأموال أو يستفيدون منها أن يتذكروا: بمجرد أن تُطبع الحكومات المصادرة، لن تكون أصول أي شخص آمنة. ولن تكون الفوضى التي تلي ذلك جميلة أو سلمية</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/85271" target="_blank">📅 06:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b72a5b6ef8.mp4?token=aTxiIdvWy5_5TZMBakgeQ4grN8jEJCqfjghn6oLLdCcF0dwTbMNE4ngZs49L4K7EYz5WnvPjIK1aFej_rjq5umKhPwMAVLflLuhrrEFdC7-wPghFrAZId5qgdoNT2U-OD4LzUNYZbVkOTfiaUD40NQTLY6Ej3DbA5XrdAfeur4wTv3wTqENGjHtNsl9ZtISuWcjR5nH8H-zDMeauNB_gAa2GfVVh9Dd0epy_Em4d3-VqnlvIEc1uKh-bOe5vLhsD2Ojo5_ztmrsRNsPqvf51pTcTv4YFc5T1zuZDI6_T__VbaT9Tr3YJpQByfUMwDF9dw8ihQKaLMNXmtgBC4LYD4BmraZ9yGvCdMWD1XPKIOTmN6GX3Huu8cgIxyRxWEBi2XbZeagfxqL8GwKCDOynshl8JhRZki2yloGyATEt0N6rDIVJnLCTgV_lg7Rs15U4s7WXPFKlGkItu_jhAZU5fVh-2LA-AOB2qPGJofF3V7BCniYCYARu34WqlUT6qi3J1C_Vb6a5EJljNenNHG235Ke04T1PY_NKHDzKiuv7zrdAOGqOaAYm0bPt9aR_Wm1NaTOeMaqkHyjdblnaN3V_X32_Njqkpt0Bu2gJpRy3ULyhbCKcomUNjXVGhoqT6KOvzM--KhiJcy4iTId45ir4Hi2qG-K1nUjKsZeCebMCXZ2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b72a5b6ef8.mp4?token=aTxiIdvWy5_5TZMBakgeQ4grN8jEJCqfjghn6oLLdCcF0dwTbMNE4ngZs49L4K7EYz5WnvPjIK1aFej_rjq5umKhPwMAVLflLuhrrEFdC7-wPghFrAZId5qgdoNT2U-OD4LzUNYZbVkOTfiaUD40NQTLY6Ej3DbA5XrdAfeur4wTv3wTqENGjHtNsl9ZtISuWcjR5nH8H-zDMeauNB_gAa2GfVVh9Dd0epy_Em4d3-VqnlvIEc1uKh-bOe5vLhsD2Ojo5_ztmrsRNsPqvf51pTcTv4YFc5T1zuZDI6_T__VbaT9Tr3YJpQByfUMwDF9dw8ihQKaLMNXmtgBC4LYD4BmraZ9yGvCdMWD1XPKIOTmN6GX3Huu8cgIxyRxWEBi2XbZeagfxqL8GwKCDOynshl8JhRZki2yloGyATEt0N6rDIVJnLCTgV_lg7Rs15U4s7WXPFKlGkItu_jhAZU5fVh-2LA-AOB2qPGJofF3V7BCniYCYARu34WqlUT6qi3J1C_Vb6a5EJljNenNHG235Ke04T1PY_NKHDzKiuv7zrdAOGqOaAYm0bPt9aR_Wm1NaTOeMaqkHyjdblnaN3V_X32_Njqkpt0Bu2gJpRy3ULyhbCKcomUNjXVGhoqT6KOvzM--KhiJcy4iTId45ir4Hi2qG-K1nUjKsZeCebMCXZ2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/85270" target="_blank">📅 06:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726db6ae6d.mp4?token=jCzUyyrESRwaGN8rnB0Mk2X8x6nH0QS2u7DTx_1kxq3NNJz8aqswXZmiJoq2rtCiHl_AKZ_itRJra0t3aUeYsZDOEW5Lk4Gzket9P3aSXnfMXPT4ezEErFK3_eM04DUXwJE8OEHkfOtCPLIgcrLe4NN57BvICXzbQr5e0rcCWgS9919AK1oWrxrIWbkPkQSMUOIO_Pdbfvf2HNDC3RvvIuy4Pp9z_z6Yw_nH97uP1YORo5gC85QEBnlX4DjvRpq5MZsHjriKmXQzeywsn17BdvRAsmWekXjQmWChWlZFKtJ47hVHmTtBesVwHAY3CTlrmf98HsVjZy47BUBN4wq8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726db6ae6d.mp4?token=jCzUyyrESRwaGN8rnB0Mk2X8x6nH0QS2u7DTx_1kxq3NNJz8aqswXZmiJoq2rtCiHl_AKZ_itRJra0t3aUeYsZDOEW5Lk4Gzket9P3aSXnfMXPT4ezEErFK3_eM04DUXwJE8OEHkfOtCPLIgcrLe4NN57BvICXzbQr5e0rcCWgS9919AK1oWrxrIWbkPkQSMUOIO_Pdbfvf2HNDC3RvvIuy4Pp9z_z6Yw_nH97uP1YORo5gC85QEBnlX4DjvRpq5MZsHjriKmXQzeywsn17BdvRAsmWekXjQmWChWlZFKtJ47hVHmTtBesVwHAY3CTlrmf98HsVjZy47BUBN4wq8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک های ایران اسلامی در آسمان اردن</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/85269" target="_blank">📅 06:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0874f68421.mp4?token=LqMd5subwmAnpNWF6Q0I-GtvkRxjZTkMo6TlNLq0Hsn9xXE1rRnAVoAWV7hiVBUCRHAuO-EyvpOW7e2N3WVWzR_Rzs9UUvylGLfGUfz5t8NT9YRAJBtoseX9wsZ7we9vmetd19fRscQUjs2gergjm9JlJaqVnMiDlYnp75bIfkUXFBULfWMM0Wa0eR1s5jhegoSQwKTNU1V_R-KyXZcXsOINaich7Qwu-nLGawRdhF9sVq0VW6dfayViY7b5rfBqNv8us0sVKPuGJiJPp49Qlz3zQFjxDTnOgUizUE1Dd-l6DdVJnV7-IdkdSFx-3lt3tvMj6Y5mkzw6fsJrtaYp5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0874f68421.mp4?token=LqMd5subwmAnpNWF6Q0I-GtvkRxjZTkMo6TlNLq0Hsn9xXE1rRnAVoAWV7hiVBUCRHAuO-EyvpOW7e2N3WVWzR_Rzs9UUvylGLfGUfz5t8NT9YRAJBtoseX9wsZ7we9vmetd19fRscQUjs2gergjm9JlJaqVnMiDlYnp75bIfkUXFBULfWMM0Wa0eR1s5jhegoSQwKTNU1V_R-KyXZcXsOINaich7Qwu-nLGawRdhF9sVq0VW6dfayViY7b5rfBqNv8us0sVKPuGJiJPp49Qlz3zQFjxDTnOgUizUE1Dd-l6DdVJnV7-IdkdSFx-3lt3tvMj6Y5mkzw6fsJrtaYp5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباتريوت في سماء الأردن عقب الهجوم الصاروخي الواسع على قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/85268" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d84fda6e.mp4?token=XW6zT8pVobxkFTJyA2sr-AioqmoG5UYajAPKi4gUQWRgxMJe1hWT2AYH5WZ2F2A1Cnlmul14FkwwAzAyh2TXl4QGLafib_OhSyHnN7cStSOnD3ykhb55VRwgFp8Gv8TSlwsisGRkWI2TqpLNiCDE-TN-fc58XYfnpGrXUCvP9bqofJtrvntLS_GuTHu6UE3QqH-p-wE2GKbdv5_8r9Xe-tJUNlOvn3KcnXlt_E1vQIppx30COjNeCi0T3rXKndBOx-y0KTwbwvTag0KwARbkWBtUdOEAWH9urn74q-7pI2mM-vwzIGxjMeLPkkmTQEc1zTCZrQS_Bkcqnqje-u3iBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d84fda6e.mp4?token=XW6zT8pVobxkFTJyA2sr-AioqmoG5UYajAPKi4gUQWRgxMJe1hWT2AYH5WZ2F2A1Cnlmul14FkwwAzAyh2TXl4QGLafib_OhSyHnN7cStSOnD3ykhb55VRwgFp8Gv8TSlwsisGRkWI2TqpLNiCDE-TN-fc58XYfnpGrXUCvP9bqofJtrvntLS_GuTHu6UE3QqH-p-wE2GKbdv5_8r9Xe-tJUNlOvn3KcnXlt_E1vQIppx30COjNeCi0T3rXKndBOx-y0KTwbwvTag0KwARbkWBtUdOEAWH9urn74q-7pI2mM-vwzIGxjMeLPkkmTQEc1zTCZrQS_Bkcqnqje-u3iBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/85267" target="_blank">📅 06:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85266">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f6a2735.mp4?token=dw-mOlrq9emBHHqA2JuEzrYA8vsz6c-kqkq8Tk-jCKyvkQfuvdyIE_XqZe6FVG0mzRqDjjGd8GjtvMsyb5L1LWfEqMjhPFjHCO8jT5koYpfciGsmM40FIH5WClTbl04T2aFb2Vt4v4hXHje3XUCuj9n071eWb1OQPSS4e3dsgBeP5fPvCG9e5M-YA20wZ4UhgQClNcM_sX_zYD-UMVmBhYzAuQCG1n4p8RotfZbvD_zOBwopAGwRGeFTiq7sFoX68_d-7XbHE671pAttK2ZiT5GWVZ_7fnGR6MyRYZD-Bj0EZQj7PwmHPzZDFMH2Lcn0EvmXxEp9BIabC8pPlnXovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f6a2735.mp4?token=dw-mOlrq9emBHHqA2JuEzrYA8vsz6c-kqkq8Tk-jCKyvkQfuvdyIE_XqZe6FVG0mzRqDjjGd8GjtvMsyb5L1LWfEqMjhPFjHCO8jT5koYpfciGsmM40FIH5WClTbl04T2aFb2Vt4v4hXHje3XUCuj9n071eWb1OQPSS4e3dsgBeP5fPvCG9e5M-YA20wZ4UhgQClNcM_sX_zYD-UMVmBhYzAuQCG1n4p8RotfZbvD_zOBwopAGwRGeFTiq7sFoX68_d-7XbHE671pAttK2ZiT5GWVZ_7fnGR6MyRYZD-Bj0EZQj7PwmHPzZDFMH2Lcn0EvmXxEp9BIabC8pPlnXovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/85266" target="_blank">📅 06:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85265">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0c09dda6.mp4?token=rz27Fs5vgpqfqTgPNpKWiv5HYyw4-4F-PUKozmBVDRfEig55-oWd8lmwoZaKuzwmHfLU9HY8Ntt1EKiRs4Q4hj9ILtVOCSohR4lngFMjdrT3IcRRUAbtq-KPZhLcmcCFEcxc3ofzsaZ6Rbekx1Cf3SSGwImYA2jd_2BVNCiUuOpflR6gdu1EHfHSgUFgOR7EgZ0_Qbl_RUfUEopycQatUNBhk1-Eh3Sp3QLf77UE5qCLO5489_uuAL3FVq2MfDfzqcoGaVSIw1yvXrMiZB0BD5iRxJylQM7-uvTnBHysi-RODXCYvextz_iWA_9HMuwjfNg-W3IM4Cq-WMdPV2ng-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0c09dda6.mp4?token=rz27Fs5vgpqfqTgPNpKWiv5HYyw4-4F-PUKozmBVDRfEig55-oWd8lmwoZaKuzwmHfLU9HY8Ntt1EKiRs4Q4hj9ILtVOCSohR4lngFMjdrT3IcRRUAbtq-KPZhLcmcCFEcxc3ofzsaZ6Rbekx1Cf3SSGwImYA2jd_2BVNCiUuOpflR6gdu1EHfHSgUFgOR7EgZ0_Qbl_RUfUEopycQatUNBhk1-Eh3Sp3QLf77UE5qCLO5489_uuAL3FVq2MfDfzqcoGaVSIw1yvXrMiZB0BD5iRxJylQM7-uvTnBHysi-RODXCYvextz_iWA_9HMuwjfNg-W3IM4Cq-WMdPV2ng-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية واسعة تنطلق من إيران الإسلامية</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/naya_foriraq/85265" target="_blank">📅 06:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85264">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dc03c583.mp4?token=gxVxPpOhNcCpFafCepT9yKNVyWAq1renoUpccH1HR1Y7XsJ8uwdJeHCIcNwJ_ZqDvc_VAhcXlzkciHBpLwsV1LV1cisoH25WK2ZeEZ7dIN22QNekIcnGiPzEi7KCPMwEk5NqrtDJvLDtk0GyIW8O31bHcbqoz4JnwgSGxyuhwUMMVLXL7y3mxSrDC8vPTAWdi46M2pI1b1SAZYJOVb2XkdYFPAVbx-b9-vneHjUJ_uT3Vtd-iTkQou7HRFJ5gujhRH0DjQXEFXLpKBsGZbhMQOiUaiu9WP7QG06r8cifvNTdNIiWrT3ixQ0w10Q2qh6OeI5O7M4P-tmKe8cipzkAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dc03c583.mp4?token=gxVxPpOhNcCpFafCepT9yKNVyWAq1renoUpccH1HR1Y7XsJ8uwdJeHCIcNwJ_ZqDvc_VAhcXlzkciHBpLwsV1LV1cisoH25WK2ZeEZ7dIN22QNekIcnGiPzEi7KCPMwEk5NqrtDJvLDtk0GyIW8O31bHcbqoz4JnwgSGxyuhwUMMVLXL7y3mxSrDC8vPTAWdi46M2pI1b1SAZYJOVb2XkdYFPAVbx-b9-vneHjUJ_uT3Vtd-iTkQou7HRFJ5gujhRH0DjQXEFXLpKBsGZbhMQOiUaiu9WP7QG06r8cifvNTdNIiWrT3ixQ0w10Q2qh6OeI5O7M4P-tmKe8cipzkAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية واسعة تنطلق من إيران الإسلامية</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/85264" target="_blank">📅 06:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85263">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات في مدينة خرمشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/85263" target="_blank">📅 06:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bc05e0e7.mp4?token=hsBIPuTwScscP40TYRc0j5g5j9ODo0bMMe0jAXVo8GKCzPwUxCSHppaqGXgaluNSoN1VNg0w_4cERO5S8RDbGWIEkj-Ytg7F-1NNkgDiKsvEjehq9iAeIzIEhppTCaEnNDvdSRI3ndldOCkyXAE5jMYljdE9eUByz58zB8UuDesXxD-9_JBDZtWpe86W9wwzu6hj09q-QOcXm2ysvIqRiaKDcZrKvsK9pGfsjP7CaYCsjeHZTw0c3PVOJxLGHTHT-W0n1Ko4NsvPv5Fz-laBbKTQXhjdbUuOTSD7MQjCWYttGYZVi4EJRhlw6ne1mrnAf4rTKQ7CXeRopGllFXgqCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bc05e0e7.mp4?token=hsBIPuTwScscP40TYRc0j5g5j9ODo0bMMe0jAXVo8GKCzPwUxCSHppaqGXgaluNSoN1VNg0w_4cERO5S8RDbGWIEkj-Ytg7F-1NNkgDiKsvEjehq9iAeIzIEhppTCaEnNDvdSRI3ndldOCkyXAE5jMYljdE9eUByz58zB8UuDesXxD-9_JBDZtWpe86W9wwzu6hj09q-QOcXm2ysvIqRiaKDcZrKvsK9pGfsjP7CaYCsjeHZTw0c3PVOJxLGHTHT-W0n1Ko4NsvPv5Fz-laBbKTQXhjdbUuOTSD7MQjCWYttGYZVi4EJRhlw6ne1mrnAf4rTKQ7CXeRopGllFXgqCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صواريخ واسعة أطلقت من إيران</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/85261" target="_blank">📅 06:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85259">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZsZhs7tBc6eF5v7NunavOAPkwFlKKUw7UUaPTlJ3kaxWLoAhvLuK-5gqI8HTU95ZlrSGKbWWJEvumI_JRER_tOHlfYlfTP0xq7soE2YHuECRG9O-zQoFToZGJpQrNXx-JKIErJAMXNQ9-iys_Oeu-tNUqz7PvJa0mu5aQK0fZPvJbQNALEbtrqvu-C5UU5TaL9Ccy9B5NZcZveftd3IjlPJjh_GF9AO0I5FMq6hQQlpLfekHO2AZRKUe4xJPgQ7crBdOhYom0KgKrVdcBz7daHpFgQDoy6qIcfPVR0mX1GioXb-upBakwa7GDAkkyP6b_8UyU-LXnrnbqMGAe5MNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2638dcbb22.mp4?token=GMzWw962Pivq97RPgVaHIYk3fQVSe_23DPOWRfQxPa08NCPFUxmM78qvzGxpbjRXVuGcUSKNB2TeK0AxL3QmxqBjNjfRR8O3AEjEXEOUai9C7T3D1I4Hn_OwKw4qn9_sZ4NFqPIAg2fWzALAJdyJ8QnttU4-Im3bVSQcfNdAXUfUVC8i7KFJEB1lIIDu404lENCCjC26oKKsUn3doiC9DDQJF896DUGxyFfyqXcCGE7e2HbvcdEFVkK3yY6MFS16QCJJ4bNlxh4f_QzPPn8CtvnsH5NqEVNoUklKGmZO5ucZEqV5Z0MwMT-n1K1n5ZT_B7GJZpNdUvcxcMQOxj1hgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2638dcbb22.mp4?token=GMzWw962Pivq97RPgVaHIYk3fQVSe_23DPOWRfQxPa08NCPFUxmM78qvzGxpbjRXVuGcUSKNB2TeK0AxL3QmxqBjNjfRR8O3AEjEXEOUai9C7T3D1I4Hn_OwKw4qn9_sZ4NFqPIAg2fWzALAJdyJ8QnttU4-Im3bVSQcfNdAXUfUVC8i7KFJEB1lIIDu404lENCCjC26oKKsUn3doiC9DDQJF896DUGxyFfyqXcCGE7e2HbvcdEFVkK3yY6MFS16QCJJ4bNlxh4f_QzPPn8CtvnsH5NqEVNoUklKGmZO5ucZEqV5Z0MwMT-n1K1n5ZT_B7GJZpNdUvcxcMQOxj1hgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ أخر يحلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/85259" target="_blank">📅 06:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4217f405.mp4?token=WC3dZWDqhsvj0h9_iGz6_i9sCXPPKWkwywiDbX-F4axYJBmG5uNB-DTbqPGMows7JtaUdL6XOZfliTFoH-Y5GMfrWQAuaNCLFULrGHUyWHIbSuqj5HneODKmOBUeMIvvbBG0moT4Fdx4HfQxfy0IAZSBcLA6qutGM2GJrHs_8s3YrA9jJNHYJ6u4z6yRwIBRyl7R4xNapK-9NvZDzXhn85_X0wEqax0wL7OefYdI3uQoJr1qUYXr6XSIclccs-7UkWAWiCv8g8lI18z4LzUbEFT1RrR_-E_EceLZgwi5yufVrDR5XMYLd8SxubEObFVrkcYTEP1kFfNDSDN8KYFBPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4217f405.mp4?token=WC3dZWDqhsvj0h9_iGz6_i9sCXPPKWkwywiDbX-F4axYJBmG5uNB-DTbqPGMows7JtaUdL6XOZfliTFoH-Y5GMfrWQAuaNCLFULrGHUyWHIbSuqj5HneODKmOBUeMIvvbBG0moT4Fdx4HfQxfy0IAZSBcLA6qutGM2GJrHs_8s3YrA9jJNHYJ6u4z6yRwIBRyl7R4xNapK-9NvZDzXhn85_X0wEqax0wL7OefYdI3uQoJr1qUYXr6XSIclccs-7UkWAWiCv8g8lI18z4LzUbEFT1RrR_-E_EceLZgwi5yufVrDR5XMYLd8SxubEObFVrkcYTEP1kFfNDSDN8KYFBPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقات الصواريخ لاتتوقف من إيران الشجاعة نحو قواعد العدو الأمريكي</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/85258" target="_blank">📅 06:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">موجة أخرى تنطلق من إيران</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/85257" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ياعلي مدد</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/85256" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ياعلي مدد</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/85255" target="_blank">📅 06:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85253">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c6f8344d.mp4?token=AKgLOswgHbsdZ2w9Nk81YfHwgRZGbG7m8CEyxDFEWG-dVZXE3mu11U0oRndK2Al5nuhuwa1WnZY5oYHFFY_4NASVJ4v2IrfVcsb6nndwz0Xij45AI2LeHMO28Uc9zTD7CS8i3cWCK-kxQTkMeFXf0DhmsznN_fjDpy13l5hl7xiFkBZfJ1xogcLDCb66z48JI3ayM5NxHn55PS64OTtcGyOanO4vwSstngcN1uA2Qs5HOeMjAa6r3UFNSRsaKXDs6KQsduuMmXJGzEouxrghkLVAKkzZv3LfQQL9bQifcTmmud1JEzy_O0p5QAlSYcKeLVjrXcX6cpGK3ZmDIipw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c6f8344d.mp4?token=AKgLOswgHbsdZ2w9Nk81YfHwgRZGbG7m8CEyxDFEWG-dVZXE3mu11U0oRndK2Al5nuhuwa1WnZY5oYHFFY_4NASVJ4v2IrfVcsb6nndwz0Xij45AI2LeHMO28Uc9zTD7CS8i3cWCK-kxQTkMeFXf0DhmsznN_fjDpy13l5hl7xiFkBZfJ1xogcLDCb66z48JI3ayM5NxHn55PS64OTtcGyOanO4vwSstngcN1uA2Qs5HOeMjAa6r3UFNSRsaKXDs6KQsduuMmXJGzEouxrghkLVAKkzZv3LfQQL9bQifcTmmud1JEzy_O0p5QAlSYcKeLVjrXcX6cpGK3ZmDIipw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تتوجه نحو الاصول الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/85253" target="_blank">📅 06:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجاران عنيفة تهز الاردن</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/85252" target="_blank">📅 06:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجاران عنيفة تهز الاردن</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/85251" target="_blank">📅 05:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الصواريخ الإيرانية تتوجه نحو الاصول الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/85250" target="_blank">📅 05:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c59ae5186.mp4?token=KLO3XtQIJRuCeqdF7zQ_zJGG9xEiRXXw6XMdKlkMTKnk_cbKH2SH2xGm51R_h1tAWeoFDWyBkeY8syXY3sCjTlvoLuCVMqKu5ymU2X0urMIwjj2N1gjehUwutNHf_O5gxYPu7VVToubb8E4HIhI0SEbxT0rXFgJWzc0KCeOm6aL2ddd_swh7C6A8WizDvBohCN9IyNtTYzaBDOxbZCGjeIOHdKMLr2OidAtZ_n1_zmYJ7MxjK1_BlvOFH9yKHxq-RUlLQDEBjZKVLDbFV2pNtLwcRllpuZBUC4jff7bENIYO3aj9bETfoxW8rCOzIcwWIplqEA9kGzNbVUtsPohudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c59ae5186.mp4?token=KLO3XtQIJRuCeqdF7zQ_zJGG9xEiRXXw6XMdKlkMTKnk_cbKH2SH2xGm51R_h1tAWeoFDWyBkeY8syXY3sCjTlvoLuCVMqKu5ymU2X0urMIwjj2N1gjehUwutNHf_O5gxYPu7VVToubb8E4HIhI0SEbxT0rXFgJWzc0KCeOm6aL2ddd_swh7C6A8WizDvBohCN9IyNtTYzaBDOxbZCGjeIOHdKMLr2OidAtZ_n1_zmYJ7MxjK1_BlvOFH9yKHxq-RUlLQDEBjZKVLDbFV2pNtLwcRllpuZBUC4jff7bENIYO3aj9bETfoxW8rCOzIcwWIplqEA9kGzNbVUtsPohudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الأمريكية تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/85249" target="_blank">📅 05:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353c971c6d.mp4?token=smnwySeLvnCwpsCMDSTaUFa7gPZ-TAHPo8Bl_MCrfa3xgjMN86LlkSAfVff86nwdGQATeWEjkyXDCGikOcaAFmMNPdrJY3qkGBib-jZ43NkkpEyKAlrHioI8g5NFjSxH6IPmCo37AGkxbldZ-TN6cQmTGeh8VywQvg-u0yQHTKjOt1BiFoh1YOtERIW6-BtpbhQpoi7vkqDZ6Y3eKJghbNFkXjYTYvt9nfmf9oy7GRI_-vWPGwDYOXsY3qpbfyLzEEph9S9U-F54QTWCm6FNjWlrItCsnmIjXiT_k-1IxBpodAL32RQAPS75RHZyh74i5wEFIXtKCnfDGwMg-h1roA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353c971c6d.mp4?token=smnwySeLvnCwpsCMDSTaUFa7gPZ-TAHPo8Bl_MCrfa3xgjMN86LlkSAfVff86nwdGQATeWEjkyXDCGikOcaAFmMNPdrJY3qkGBib-jZ43NkkpEyKAlrHioI8g5NFjSxH6IPmCo37AGkxbldZ-TN6cQmTGeh8VywQvg-u0yQHTKjOt1BiFoh1YOtERIW6-BtpbhQpoi7vkqDZ6Y3eKJghbNFkXjYTYvt9nfmf9oy7GRI_-vWPGwDYOXsY3qpbfyLzEEph9S9U-F54QTWCm6FNjWlrItCsnmIjXiT_k-1IxBpodAL32RQAPS75RHZyh74i5wEFIXtKCnfDGwMg-h1roA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الأمريكية تحت مرمى الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/85248" target="_blank">📅 05:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTMeDzV_sLHwh3rqcxZO5zEfiqETfJghx3jlBjeYVphD_SM2E5yCuGCR6yvYbATJy9urnn2vqLUYA_EX0rqId--KehaxAW8q_izTflY9cpIVNdGcnk6J2HoZlWieU7QgyEoOYJLUXimF_1fmRaB3EpZBNOqumHFtvXQek3w0rs0ousMcB9t_Qke36JLvDFQvuMJ8LzGLbLp9Bq_D_-JikuF73VNJPUwKx2NZZ2gHi_2pkOlNbJzylcnBdeDsVwfnO7iA7LYod4eIMaQgpt1RzpjdBGRI_-FGhLHqb8kMT5F7OkeY6DqIoc5Iu4XQ7zfIQCC_autbrUcgGAVpFepM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjcpy-6d8v8m43BnkHoQM1WoSo-BTmxNyeYEPy4_13Ko3EEg19i6v0q0AjRSk7CES6eFdzSb0K2jqvZdFDlY9WyFmg_nVmJ1pivxEh_5doeVOuDbtX-eIH89P2DYIY8G-2Wg6e8nsZpZuTHmpKr2w4ExlL9TuCvuqsn13_2Yd4MD83umzvaBwwAEJL7C1okHDJPnc9FPTsl3iNU4TBoYtQiFRUzI38eNmUEWLy27pgml6K8c3bcja5zKzw-vWOM1vFLCVEUrE6-vJ1054lg-kIsMkqAaUsSYoqSJitP5setE0vaoaw93SI2Q-HO2IdVeCg_ZIYsIdI6lF5QRMG4Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvr94sJ6egAjwwI9dTZyMFEkx4yPo1ExVD16cff4gnjtE61KiAXhN8IZJQUfWiJbkoHXhLS0KWVv-SMpu8wI6HgAPIc9ynoplLISGwnT2ooUtlDj33LlFajQwU1wkGm3ZCwq0vlEstLex8wfjXDSvzB6Jy-_8YOuvZYHcC8mU1XkA6N81cDJhAWuaX3XBntbhbk8kMgTpNYFr9aU6H9ms8IRTkE77wqvrnR3bS_cHcWF8DyLuAAQvx02M2H5O6Us9dR_RHpKYWbcE_OrdTqOSqmFHX3EKONSqYO6p7lx82GA9SmymYLKHttOOwWs0Aj4my9wUcSVtilVPNaDXlugBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إطلاق موجة صواريخ من إيران الإسلامية نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/naya_foriraq/85245" target="_blank">📅 05:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ae9c6675.mp4?token=U6Sabtw7Tbf9xuEOJpf5AFf5VX-WGRnqYH4oFxXP5aSogTOfVE70Hw0f99VwTGGFS6_mQwpgrrej2PWG8Qej_-oMxzuwWfCL4TzunwV5fOCeqr8gGoLq0VD-Ei6mlZ9SySvJamzTPSRxfxQUIAWpeNaS8AmVBf8fyNJRZqWyLnNBIqrLMAzp3Vi6_Zlw_IxlUGpWnyrdvpoT3TvvLm2uVBmTWbVQMeEe3IMv0Kp1625HjZ1vaZ2qGLsjxJ-WS0tM8nyQdCKP2c6olLDMSKHVxLDPVFfne3jL298UVO989GZ2wBlc1MG4WjQFXzJu0dxm65Z69RfiqHzk_13jAp910A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ae9c6675.mp4?token=U6Sabtw7Tbf9xuEOJpf5AFf5VX-WGRnqYH4oFxXP5aSogTOfVE70Hw0f99VwTGGFS6_mQwpgrrej2PWG8Qej_-oMxzuwWfCL4TzunwV5fOCeqr8gGoLq0VD-Ei6mlZ9SySvJamzTPSRxfxQUIAWpeNaS8AmVBf8fyNJRZqWyLnNBIqrLMAzp3Vi6_Zlw_IxlUGpWnyrdvpoT3TvvLm2uVBmTWbVQMeEe3IMv0Kp1625HjZ1vaZ2qGLsjxJ-WS0tM8nyQdCKP2c6olLDMSKHVxLDPVFfne3jL298UVO989GZ2wBlc1MG4WjQFXzJu0dxm65Z69RfiqHzk_13jAp910A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/85244" target="_blank">📅 05:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMZ28naGClPOAVdn3Q3o4KX6nyKsLGSS4TPTZOHyiZqveN0kVnBedh2fK_y7j_1zYeSgFBroJV58tkTpuIjQKdk3vF72ovicdmPyB85jNeGHS2I2reLSnLDHUfSDGEOqpUqKgOV0dnNxKnA4z2-g7XDrr4isWtYMejPEbxi0dfA3Rn_ELPBwBUdXZHkIqSMuNArVKVCzW23mmlwioaNWjMaBKjx0hzXiO9C-gbsa6DGAzunGrFoUNJVh2WGz5PAjWyi5i19ejQF0Oyn1oyHFxcC407Cr6BrPhMwNXeonw2V8eBJN8355LhtjjDt2aNUUxvzrNWHDu2wq33sWwMzSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/85243" target="_blank">📅 05:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">استهداف مناطق سكنية في مدينة الاهواز جنوبي إيران من قبل العدو الأمريكي</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/85242" target="_blank">📅 05:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أمريكي:
ترامب لا يرى خيارات جيدة سوى مواصلة الضربات على إيران.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/85241" target="_blank">📅 05:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a00b3eb82.mp4?token=mrDei35rippTtapYdE7Ri2uxbCSlAFezqDgNYnLUnWismxjl0pP8c-nu639EI55v-sa6NKGY4jdl-LcjBMcHdrSKv8hdyI7UrRNcMON2qtDNX2oHFJolhG9Y99BwvhRMbBiz5iL9RIwCemOI_RlfGCXj-hATYRfWqUekmOhxf7ZGt7QVxJeFht_2ywIffWZIvYABylfdWXFSkUzOmDJtFRREpn7WkPIygrOWOFT8tz4_GY58BFda1qToUn9HS7i8lxrZxWZs1CXgYKpPJkTzme4L_gKPyNtV3KxrwW9c37Nyma4WIcrbwxiy57IHOYyoZdA0ZWejNfS6YMiRt5X9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
أكملت قوات القيادة المركزية الأمريكية (سنتكوم) بنجاح الليلة الثالثة عشرة على التوالي من الضربات الجوية ضد إيران، وذلك في 23 يوليو/تموز، الساعة التاسعة مساءً بتوقيت شرق الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/85240" target="_blank">📅 04:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات في مدينة خرمشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85239" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات في مدينة يزد الإيرانية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85238" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات في مدينة فيروزآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85237" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7cdfe133.mp4?token=HKlPzKOm8ofmI0-aF9hxoWxod_1rV33exLSz91Pqn2B38frsPxGhQG9ogCI95DgvWeZ9I6aCXTkg0Bz9UPcq-aXeeNtrm8K424uefBue6s__TGZbJcR45WRrFzGHRNqlMG2jfTwbG7xmonQCLWl_4R6MLckK9qBJPp_eY3M1um3Q_FhIi70nDSlqIhEUZdFXsDD7y6b78cOpR0krvKFFAJSdPR4OWf40LD4tRcrTVsBq0OaFqLhIdLKrqaVkPiCGNZaakDyfCcprOwDermab9cf5dzOpoUGb2zpwCIz3JGgwf3ku4_iZWdnE5sVvMdTTSFxo6eR68R67q9xkXmNrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85236" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تفعيل الدفاعات الجوية في شرق العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85235" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0d03f058.mp4?token=gDV2Ki1oHVVA1uCslwpWbydUb0ksqTt9P1JBcvHdrBkaO1u9nzvmvJfmL8IURROo6aya-byyjbYGegBvdxrHPEAYlejPeZljjUhlErKXY8z99DwGyR49oHcO3fJU7taWjeTtdlVeIBuYlGCTwPSMaSC9pb2QcdkH-hArnBXwKj4FvmD-mg8WpdW9_CreNNVU0rcGpjldQGt23EAFmpBdHX49FO5WEFSgFDT84oN1R2hn43hAxg9e3nxy_JpGWX8n8XiIGe0yzJp8n97fAhkI1XruknxYzVExFWfEyvEs_4kMdWwV5oPXw2BTM48cIGBFx8ALCNiopU9rx3R1YIL-wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85234" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">😆
Bahrain and Kuwait, now</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85233" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca971c5573.mp4?token=m4eTC1dXMyxQxsmvQ6vU1hmXpz8LTeg2vX04pMgR2jx79fDEr8oWBCdaSf5xOgqgMoUoxTlIqZ-Ou1EnZFAvQVyMFt1Kk35sPFeY-Rv5H6HkqY2jZxU0x7HIEYrQMU5GnsbxRDY6xIQn27MUgSsa4vhrfFGyxx8au3yDv8uw4rdNUQfeYmSYtQdJGy8W9SjrCjGnGVLjrHckYD2Q3IUxqsUtVb9Y7q8qMj9pvVr-Da9_9_WFtr_lzRYUrooueSZ25ok-XE-1Wkj-74dq1YQHCBBha4o5Cz6tEhB1tDV-DDVv5LXDPzdSxKOxhKSO9E9pKiuUMBD22qeR-_0lXnJ7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85232" target="_blank">📅 03:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e36721028.mp4?token=QF2q17oIfAcbvr5U75h19jAyxzebrNwccHwbAg2ta85s6nejRmSR6LA9vvtNvo0bU2b1zNk87yn4NVopegZ7aN8RvDYfgEE0ziM_FxuD6lS-InHfb_T18DNRrt6q3pJPRPo7g8dqqbQuIFub7PzKlKJJ0eYYi29OZYOSjoL0xU0O41cjOsAnk_ObNATeZzEA2QLVUDn2Y2oCnrBek827NN_BoP8JyyJ-o9IRXeREDpH_LZZ-Dblq5QjUHBI09QWEaD2XOjcLA0ry37ZDyBB7h85YGej7deVlWI_uv21zkEkzv4uRDwa7iQr6-MNKOv7utvjOkujEKd5W9K04t9YZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي يجوب سماء العاصمة بغداد ومدن عراقية أخرى.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85231" target="_blank">📅 03:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات في مدينة خنداب بمحافظة أراك ومدينة بروجرد الإيرانية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85230" target="_blank">📅 03:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات في ميناء كنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85229" target="_blank">📅 03:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85228">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصدر إيراني: لاوجود لعدوان على مدينة دزفول حتى اللحظة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85228" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85227">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USCVL5ZYfCezyxExQGExLu46Wl3SSHz0KjgngO77TcS5_0ZFGAsvzUAE2wKzRN9q55LUughYqHcTN5Ean7SMpTxq10nqN3iIh4iNjFzQYJ_8_i7TZR_KX3-RPs68zqyq2cZB7B2jJ8BkEpliX7PFPl-sJ-07InkcM8XfkO3k9rDy6pSGP1BrmT4fZNvYowHuagZYmVIYIVKOB9NuKmozkaj7sRuXTUPD2ZANuGZCg6mXDZi3CyMJvV3Bcq_7t4WiHITKukmB_2lK1pFOpk4-yoLleW6u9q1gcQyniqaZsASzEZpIUQAPY0X_RAtvMY3Za-ZRdTS7hKd6lMcLaX10Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
طائرة تطلق انذار الطوارئ 7700 بعد مغادرتها قاعدة الملك عبد العزيز الجوية في الدمام بالسعودية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85227" target="_blank">📅 03:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85226">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ba4c5527.mp4?token=ev4T1kPcDplzOu2WLrXG5RZi-9L_TA1t_f965lAgdieZTVrLsfMUTy1bcVHuPp0aHj6RfpIbqD7B50MTEYjwRz6ktzkQes4fcx2gKz6jXEm3Cd_z8AdpZXirL-N3BB3hoOIljVf-Tp0YESbRG3jAK_zcTdVv-0RTQ4pRHB-Lle51MzWRITnDqQbstkv8GNNZeUEhuNmYtWcPTp9vMStBLOob8yE3-cqMEMpVAjnqHYGOfNuZe8NWbs6P_nFLsF-vF7OoNiRnjovSay4MaI7HiM1rlaMjQuFqAP_boliKnCsQZhhWroUwWkMGUbRxOP72XYEMgCt852kATzEd7C4s5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ba4c5527.mp4?token=ev4T1kPcDplzOu2WLrXG5RZi-9L_TA1t_f965lAgdieZTVrLsfMUTy1bcVHuPp0aHj6RfpIbqD7B50MTEYjwRz6ktzkQes4fcx2gKz6jXEm3Cd_z8AdpZXirL-N3BB3hoOIljVf-Tp0YESbRG3jAK_zcTdVv-0RTQ4pRHB-Lle51MzWRITnDqQbstkv8GNNZeUEhuNmYtWcPTp9vMStBLOob8yE3-cqMEMpVAjnqHYGOfNuZe8NWbs6P_nFLsF-vF7OoNiRnjovSay4MaI7HiM1rlaMjQuFqAP_boliKnCsQZhhWroUwWkMGUbRxOP72XYEMgCt852kATzEd7C4s5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مناطق سكنية في مدينة الاهواز جنوبي إيران من قبل العدو الأمريكي</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85226" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85225">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجارات في مدينة خرم آباد غربي إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85225" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85224">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85224" target="_blank">📅 03:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85223">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
نييورك تايمز :
رفضت إيران مقترحًا لوقف إطلاق النار قدّمه ترامب، ونقله إلى طهران رئيس الوزراء العراقي علي الزيدي، وذلك وفقًا لمسؤولين .</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85223" target="_blank">📅 03:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85222">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ed624ca2.mp4?token=sc0QeZyg68C8T20T-1QNSVJzu23byjRNF3S5vEgHZRNJyB0IJpm8fZlqHJlPZ1NBMpE5D1wgc5McqG7pAduQgrSlxLJPXaUCYL9kbE-f6yVPtFjC3u4LapLpCcgzsZzZXwJXLoChsb02SYljC-J24Qynl3Z_dPsxwt3p-eJE7FaRvCBoeq3KnJ8Xscbz7V0dq1jFxAN8ZksTyBc4Hjhi5v9oFL1eEOYfZTm1Ifc39oix24aMyyr4c8r3XUPRyaMmy9bZwkFvBN-LV7nsFfNRH1gl2-u-SIQ6SK-1-pkvQWNw5JTqCR_XleIftoCe2YFBTVpwIWL7LTIEpD60nDhJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ed624ca2.mp4?token=sc0QeZyg68C8T20T-1QNSVJzu23byjRNF3S5vEgHZRNJyB0IJpm8fZlqHJlPZ1NBMpE5D1wgc5McqG7pAduQgrSlxLJPXaUCYL9kbE-f6yVPtFjC3u4LapLpCcgzsZzZXwJXLoChsb02SYljC-J24Qynl3Z_dPsxwt3p-eJE7FaRvCBoeq3KnJ8Xscbz7V0dq1jFxAN8ZksTyBc4Hjhi5v9oFL1eEOYfZTm1Ifc39oix24aMyyr4c8r3XUPRyaMmy9bZwkFvBN-LV7nsFfNRH1gl2-u-SIQ6SK-1-pkvQWNw5JTqCR_XleIftoCe2YFBTVpwIWL7LTIEpD60nDhJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من العدوان الأمريكي على الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85222" target="_blank">📅 03:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbeb67552.mp4?token=O1qhISV_XsoTUpuZWrnpBYV9-gvGPnq72bSzcAPHYBmbFy-KMao6hoZrUn--w2nCs0LnBDEbayCq4iOYaKvrcNBy3XvC1RpPsSeQygfYzxyG-a278bUJT0TiftgyspGvzfxVeBYHxLv4tnJFSOMvg2r8T2ZMb31_8q-yX1if9XridnEauzG-SGSChjBEinPy61b6XHpFdz_RDcCQXDL8RezDmyg-wJH6bBQccx4MMtcRx5dnEi45BksibW4G65A1X9CoywBKTekGuf7mxRLvvfOKAf1UO0ql07tMoPoAuSbiAWNVuA5U6YNXm9PSAjorINWhbr5kz9kX8rYqQLbGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbeb67552.mp4?token=O1qhISV_XsoTUpuZWrnpBYV9-gvGPnq72bSzcAPHYBmbFy-KMao6hoZrUn--w2nCs0LnBDEbayCq4iOYaKvrcNBy3XvC1RpPsSeQygfYzxyG-a278bUJT0TiftgyspGvzfxVeBYHxLv4tnJFSOMvg2r8T2ZMb31_8q-yX1if9XridnEauzG-SGSChjBEinPy61b6XHpFdz_RDcCQXDL8RezDmyg-wJH6bBQccx4MMtcRx5dnEi45BksibW4G65A1X9CoywBKTekGuf7mxRLvvfOKAf1UO0ql07tMoPoAuSbiAWNVuA5U6YNXm9PSAjorINWhbr5kz9kX8rYqQLbGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على مدينة الأهواز جنوب إيران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85220" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e893b05ea7.mp4?token=stUzvR618bhU7Pm9g3t-Yt8mt4Uy5SQTXvhEncRffJQahXUj44OZI-tnUdLFdWgOVDHxcvc2mWADO-_VqMh3px8RGqizpUGhne9Zklad5aEsiuLohQU7hb_hgeBTBUkQiAfAmNjOTDxU8dRBCEOgHbjszFu_04tiCKofQ-pwNEUTLIpCHJ8gw6ItosLTMwfyysgutWIkNeRJFw6TvUG-52yy8_Pc-P2kkwQLlzqKL175WF1NxpfHzPtClFPDCoHDfJovJVSWJNkdnLIGwMefeujS3zHvcRLcFoV8OdjMjgKz4Uz2LBopZImrZVV6EBbbYMSwP3eMyYOdWETy2eqn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e893b05ea7.mp4?token=stUzvR618bhU7Pm9g3t-Yt8mt4Uy5SQTXvhEncRffJQahXUj44OZI-tnUdLFdWgOVDHxcvc2mWADO-_VqMh3px8RGqizpUGhne9Zklad5aEsiuLohQU7hb_hgeBTBUkQiAfAmNjOTDxU8dRBCEOgHbjszFu_04tiCKofQ-pwNEUTLIpCHJ8gw6ItosLTMwfyysgutWIkNeRJFw6TvUG-52yy8_Pc-P2kkwQLlzqKL175WF1NxpfHzPtClFPDCoHDfJovJVSWJNkdnLIGwMefeujS3zHvcRLcFoV8OdjMjgKz4Uz2LBopZImrZVV6EBbbYMSwP3eMyYOdWETy2eqn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85219" target="_blank">📅 02:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات في جزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85218" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99c419e82.mp4?token=NXfQ9VHwV-3EExULqtLDzWIUEW7wqZM7qApC4KarqxwKkeu9oNxgbEHICjlvzf2hb4RzJheDQ1UsWcK0pPg42eyGXacFxjTXV8ac6f7zCDpXf7rEde4eT-iALLC8doYG0jvfJHK_VNXt_u1CFXAXfuJk5QD76SR2PdMu3C4FUKAPZWnfc9-0V4XGX7428XN8hGxZYTlDh31RfmIb4I3Mb8hcV66gvVPh4LeZmSwlLnjA82GrFkxWYMvHQMYVTzSbrcximiZpgPhtVI2LvKPDsx097-Ld6RjbYTmDa-1ptdgzlWq7vxO_GM2-kbwG-lsZ8cvCnI8cDGf1DK-AHHqh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99c419e82.mp4?token=NXfQ9VHwV-3EExULqtLDzWIUEW7wqZM7qApC4KarqxwKkeu9oNxgbEHICjlvzf2hb4RzJheDQ1UsWcK0pPg42eyGXacFxjTXV8ac6f7zCDpXf7rEde4eT-iALLC8doYG0jvfJHK_VNXt_u1CFXAXfuJk5QD76SR2PdMu3C4FUKAPZWnfc9-0V4XGX7428XN8hGxZYTlDh31RfmIb4I3Mb8hcV66gvVPh4LeZmSwlLnjA82GrFkxWYMvHQMYVTzSbrcximiZpgPhtVI2LvKPDsx097-Ld6RjbYTmDa-1ptdgzlWq7vxO_GM2-kbwG-lsZ8cvCnI8cDGf1DK-AHHqh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تكبيرات أطفال مدينة الأهواز وسط العدوان الأمريكي الغاشم</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85217" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=TyH19MPFGFFDQrZQD26ERbiqtu19W8LcYyxvWDxFPbLEaIjCkV0XqLzyPMwA0JgsCDP-RcpLqadTWC84hJF0B-xmxVf5SPwvGcbQXc8jx-Ap6_EzaSsON7upwj-JtvBGuZHHSo8dsc7Zf1KtdK1UyeaSt8xw8GZhxFPrzdOen17Fblo1jkeMO9Nn1qkOYSRurd-DofTMvhb3fNigUZCwbnbdimjRzjz2luxkp5oRmZDtbVRxedXPhtTikXljsGPF9Rn1V-0T1O0zKfP_2nofNlJn-84D3syofq6d_UXIkyPNwdcV-s3qeubE8UTDahJo_IGJJAvsL1dNGqjwBP4n1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=TyH19MPFGFFDQrZQD26ERbiqtu19W8LcYyxvWDxFPbLEaIjCkV0XqLzyPMwA0JgsCDP-RcpLqadTWC84hJF0B-xmxVf5SPwvGcbQXc8jx-Ap6_EzaSsON7upwj-JtvBGuZHHSo8dsc7Zf1KtdK1UyeaSt8xw8GZhxFPrzdOen17Fblo1jkeMO9Nn1qkOYSRurd-DofTMvhb3fNigUZCwbnbdimjRzjz2luxkp5oRmZDtbVRxedXPhtTikXljsGPF9Rn1V-0T1O0zKfP_2nofNlJn-84D3syofq6d_UXIkyPNwdcV-s3qeubE8UTDahJo_IGJJAvsL1dNGqjwBP4n1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری دیگر از تجاوز آمریکا به اطراف اهواز در استان خوزستان ایران.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85216" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=pc3HAe9XYdRLzXWrVdQBBf1kZ6ebdCeA8RXOH_oRRSXTvvbEUaSWyyeRQN-am-ocxx6T_6L1wEqv3mKhgo2uDe1RvFpsljlfZqUuyDqLq4EG8amYVfBu6J5nEvC9a3K3uOKRCaS5v5YKKzGo9JZGhun97EXKZyvg_BONNSIYuZUtVnYZxnWFeBxh3W0oTHjWuMgBmhgWN-wd-TwAmW1HiyVjJqWfdfHClCO6GLp1A4_H20eFCFkejaLrPHaHPMF-6bBoquneLyCYAuOOGHUlJV2gMVzCDHwp8d4qc8vOZ6_DY_oK9EXv6OuOLqLTxsZBvf31cYcimcGIVO8N_AUnAbkbhxOoFN5T-y6tIb38VTAPCTBmJu5WSMkVKyhlFq6cJP0vse3qlZn-3ORIrxhOHm87wVXzLTk8jcv-q20HTmJnPQbOrUUfm8echpqFJYwKyhDKSg2A8NZjcRCVj29j_tKMuDr_H6ml2md2nTVaTY4Ge3z35sQJrOEiJaEMrCjSe5BDADpqp2RaFFZVpU04b78y9tsa5GCYDZpHu7FWAr-wZkj-9mavLiYzTOEkZprVEiLUO81nqw6cXu5luMWdVDZIPDqvxXhlxphFwWJyGm3Cgo5kKf_HQ1R4QpikTHLm4iLbLHOsDxpj4qKV_k9pWKCHDOWqJwMBeI1HcGYFj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=pc3HAe9XYdRLzXWrVdQBBf1kZ6ebdCeA8RXOH_oRRSXTvvbEUaSWyyeRQN-am-ocxx6T_6L1wEqv3mKhgo2uDe1RvFpsljlfZqUuyDqLq4EG8amYVfBu6J5nEvC9a3K3uOKRCaS5v5YKKzGo9JZGhun97EXKZyvg_BONNSIYuZUtVnYZxnWFeBxh3W0oTHjWuMgBmhgWN-wd-TwAmW1HiyVjJqWfdfHClCO6GLp1A4_H20eFCFkejaLrPHaHPMF-6bBoquneLyCYAuOOGHUlJV2gMVzCDHwp8d4qc8vOZ6_DY_oK9EXv6OuOLqLTxsZBvf31cYcimcGIVO8N_AUnAbkbhxOoFN5T-y6tIb38VTAPCTBmJu5WSMkVKyhlFq6cJP0vse3qlZn-3ORIrxhOHm87wVXzLTk8jcv-q20HTmJnPQbOrUUfm8echpqFJYwKyhDKSg2A8NZjcRCVj29j_tKMuDr_H6ml2md2nTVaTY4Ge3z35sQJrOEiJaEMrCjSe5BDADpqp2RaFFZVpU04b78y9tsa5GCYDZpHu7FWAr-wZkj-9mavLiYzTOEkZprVEiLUO81nqw6cXu5luMWdVDZIPDqvxXhlxphFwWJyGm3Cgo5kKf_HQ1R4QpikTHLm4iLbLHOsDxpj4qKV_k9pWKCHDOWqJwMBeI1HcGYFj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينة الأهواز الإيرانية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85215" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85214" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=FEGbEZyg1exgRUwvKgZcH3tunlq6jdMYJqWBkNPBgAgR-90cOku9T59hVHcR3jK6F_3tGA4oUzvIB6GPRgzaqzA7mugTDORAlGrqk_0qw66q4pclNbLNsQcRWFRk94ZWBX-NIlWciTTyjRaLrAsK2lEoacIZZgul71hpl8J_Tl1floYpwbJ6dFGePy4Po74i7tP25kjUEFstRiNu2yXh1ot4c-o2Mg-sx4oZJ-oChP_85GUMXZWvxYZjlfkf-DzupcqsxnfPhpRY7pJSkA8C2O4IMr4Jlh6cBSzANoLe-J66LBTm8e06-GhLlzP3wAP7SVRFjNT7hBfg01JgWKJzDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=FEGbEZyg1exgRUwvKgZcH3tunlq6jdMYJqWBkNPBgAgR-90cOku9T59hVHcR3jK6F_3tGA4oUzvIB6GPRgzaqzA7mugTDORAlGrqk_0qw66q4pclNbLNsQcRWFRk94ZWBX-NIlWciTTyjRaLrAsK2lEoacIZZgul71hpl8J_Tl1floYpwbJ6dFGePy4Po74i7tP25kjUEFstRiNu2yXh1ot4c-o2Mg-sx4oZJ-oChP_85GUMXZWvxYZjlfkf-DzupcqsxnfPhpRY7pJSkA8C2O4IMr4Jlh6cBSzANoLe-J66LBTm8e06-GhLlzP3wAP7SVRFjNT7hBfg01JgWKJzDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
Bahrain and Kuwait, now</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85213" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=fhNOlA20WaBytcTmz4HYBSQxUB0irfXDUalLBFOI1_Y-6HB9N8zbVda4XvgG6y_ENEuSkdT5B5IqBqtkqlhwvimEQS4KpG3ATCzrrk8CQPwseq4V1jxOsfgene8fNgQP-ZSJHoaSXzXgPPGSZYeO2ovgC9uELBRgyAtNEN_bmBKkxcAH-Z_t2UJtjVzdTnJA4PkJ7n8oWTP3KAri_MfMPtzGyt5rtttC0jBb4qb9e1JFMImwvDpqODVDdYtr9BzmFCAwQJoCdnnY7B5P3K9fZj09Now5i70FgSUGTvujB2mCysUYVEPbn08UnZaWEjj2phrCaotWRviTsP8tVc9MgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=fhNOlA20WaBytcTmz4HYBSQxUB0irfXDUalLBFOI1_Y-6HB9N8zbVda4XvgG6y_ENEuSkdT5B5IqBqtkqlhwvimEQS4KpG3ATCzrrk8CQPwseq4V1jxOsfgene8fNgQP-ZSJHoaSXzXgPPGSZYeO2ovgC9uELBRgyAtNEN_bmBKkxcAH-Z_t2UJtjVzdTnJA4PkJ7n8oWTP3KAri_MfMPtzGyt5rtttC0jBb4qb9e1JFMImwvDpqODVDdYtr9BzmFCAwQJoCdnnY7B5P3K9fZj09Now5i70FgSUGTvujB2mCysUYVEPbn08UnZaWEjj2phrCaotWRviTsP8tVc9MgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبيعة الانفجارات توكد استخدام طائرات قاصفة ; على الأرجح B1</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85212" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بيان للجيش الامريكي:
بدأت القوات الأمريكية ليلة أخرى من الضربات ضد أهداف عسكرية إيرانية في الساعة 6:45 مساءً بتوقيت شرق الولايات المتحدة، وهي الليلة الثالثة عشرة على التوالي التي تهدف إلى محاسبة إيران والحد من تهديدات الحرس الثوري الإيراني للشحن التجاري.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85211" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=PxsZOhVUfDxBasLQH5L4ZY977wS4KS2IAzle0oChNWrbIsCDIe9P2MeAznyAetItm-gBTD58V7Tlt9bFih_-i3uOyHJR6U2nmuCJFoUVXw-PYdl1qv-dLx_ULpWlaD3OYHvgycFLL9KDylEn3kxKfBAHDEzL2HrHzvQ3xcdEe3uI2vyp6LK3SvIL3eBfBq42L6rg8FBTtHQMNK7O0jABZJeIBw2Qhb05ayWwMxtUtyXYouO8x6Yzzhhm52usntd3UCtS-NE20Az8bHvvjURr2siAkkVVISKMYA6ZfaIywVdXlBzt8UgarjarJQ6xn030Bet1qhb879ieYHx0_eVLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=PxsZOhVUfDxBasLQH5L4ZY977wS4KS2IAzle0oChNWrbIsCDIe9P2MeAznyAetItm-gBTD58V7Tlt9bFih_-i3uOyHJR6U2nmuCJFoUVXw-PYdl1qv-dLx_ULpWlaD3OYHvgycFLL9KDylEn3kxKfBAHDEzL2HrHzvQ3xcdEe3uI2vyp6LK3SvIL3eBfBq42L6rg8FBTtHQMNK7O0jABZJeIBw2Qhb05ayWwMxtUtyXYouO8x6Yzzhhm52usntd3UCtS-NE20Az8bHvvjURr2siAkkVVISKMYA6ZfaIywVdXlBzt8UgarjarJQ6xn030Bet1qhb879ieYHx0_eVLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85210" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات في بندرعباس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85209" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85208" target="_blank">📅 02:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4fc23b50a.mp4?token=tB8tTLmiamgqkgdTVfnG8H3QyytInlXAX4DJ0bw38TnEjl9QTMN817THxiNXTswzkOeRL8DoRXflcRoiyBM33eLldSOQ9J-Dkp7qphEmomvhKC3PzC_sfToIPfuy2Nf0lUbqAjcG6NPf9RmOab_35tXFlBu9THX-8LC8rO3itTXpHt7X_kGcQXzuGBxjDMiy254vogiAmmrc3PSbt6zAj6oXZWd2qF88y69IG_jG_K5A-hZvNDgDppingve0_C8BaX27SNN4wNtnLONxIyU3iNmkkUjqNIoBvMSIWhT9iRmHbjJbWNfZ3bM4mZxQhttSztJrUdZoDfLuHb6-m-PTlm91czWZy-y-3B5AntpxuVfOccPFAAhIdNgw-cNaLafUbOd2Futumyt_45xjqoXsrgHYFq7DbXJIgo39qXtkIMRft1jf68ZnFK5VdHIqYtbIyPE0HjpNSTRHkT_blvxbRxXcuocsq7NSJMxaT6RWMjeKtojoFBpWrbqOMJCWGjfLkpxxh5xqd67GNo6phTA1PYe8B9zVj3dhzntfU7AVDdc4TVWwzHTt6C97DMxMG_XkyXtJ-NFsap6eFVw6jHziT65INi6zrPTYaFIXThNBX52l-p9V_aixYbxOJVuyqsKzZGFMLYRCabl4C3S_b5GKscNa7bKgTn7iuuAOBkUR1Is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4fc23b50a.mp4?token=tB8tTLmiamgqkgdTVfnG8H3QyytInlXAX4DJ0bw38TnEjl9QTMN817THxiNXTswzkOeRL8DoRXflcRoiyBM33eLldSOQ9J-Dkp7qphEmomvhKC3PzC_sfToIPfuy2Nf0lUbqAjcG6NPf9RmOab_35tXFlBu9THX-8LC8rO3itTXpHt7X_kGcQXzuGBxjDMiy254vogiAmmrc3PSbt6zAj6oXZWd2qF88y69IG_jG_K5A-hZvNDgDppingve0_C8BaX27SNN4wNtnLONxIyU3iNmkkUjqNIoBvMSIWhT9iRmHbjJbWNfZ3bM4mZxQhttSztJrUdZoDfLuHb6-m-PTlm91czWZy-y-3B5AntpxuVfOccPFAAhIdNgw-cNaLafUbOd2Futumyt_45xjqoXsrgHYFq7DbXJIgo39qXtkIMRft1jf68ZnFK5VdHIqYtbIyPE0HjpNSTRHkT_blvxbRxXcuocsq7NSJMxaT6RWMjeKtojoFBpWrbqOMJCWGjfLkpxxh5xqd67GNo6phTA1PYe8B9zVj3dhzntfU7AVDdc4TVWwzHTt6C97DMxMG_XkyXtJ-NFsap6eFVw6jHziT65INi6zrPTYaFIXThNBX52l-p9V_aixYbxOJVuyqsKzZGFMLYRCabl4C3S_b5GKscNa7bKgTn7iuuAOBkUR1Is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/85207" target="_blank">📅 02:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7123743603.mp4?token=nvM1SLtHTlwRL1FzlJYiaAKYLIuweA_QpEXOzSfr5Km44IKhicaelEcdBO5ZmlHWzQ1O6p3UugXm7yYdpVfEaUiDdEwuWCBF98HTj6-7j0MC77lVDtMOOwNMIGxFLE1Pb9iKIHz_d5r6VtMqRrOAvoVll_pbWBOJ7E6211tZ9VjsJPdedTTzwO6gD_9y8e5QgX76giWXZOuCW9jmfp04eYk0DWgZEZ1XIIYkJh0PxpxYj3SVzJKvy0wFk257C1ePdyC6aHx9FH5MFXK2EFcyXsiqBKn2vftahfa6HIZijvevnxr2DPNzSxwDswqQlLH646lMIpUksB8nvs7zAMdKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7123743603.mp4?token=nvM1SLtHTlwRL1FzlJYiaAKYLIuweA_QpEXOzSfr5Km44IKhicaelEcdBO5ZmlHWzQ1O6p3UugXm7yYdpVfEaUiDdEwuWCBF98HTj6-7j0MC77lVDtMOOwNMIGxFLE1Pb9iKIHz_d5r6VtMqRrOAvoVll_pbWBOJ7E6211tZ9VjsJPdedTTzwO6gD_9y8e5QgX76giWXZOuCW9jmfp04eYk0DWgZEZ1XIIYkJh0PxpxYj3SVzJKvy0wFk257C1ePdyC6aHx9FH5MFXK2EFcyXsiqBKn2vftahfa6HIZijvevnxr2DPNzSxwDswqQlLH646lMIpUksB8nvs7zAMdKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي أمريكي في سماء محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85206" target="_blank">📅 02:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇺🇸
55 شهيدًا و 629 جريحًا في هجمات العدو الأمريكي على إيران حتى الأن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85205" target="_blank">📅 02:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇷🇺
🇺🇸
اكسوس
: مجلس الشيوخ يستعد للتصويت على العقوبات المفروضة على روسيا الأسبوع المقبل</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85204" target="_blank">📅 02:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/85203" target="_blank">📅 02:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/85202" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جسم غريب يسقط في سماء قشم بعد إطلاق النار عليه الان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/85201" target="_blank">📅 01:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fec637f4.mp4?token=oR-ryJVmPCPg2zutUAcOBkzFDJ2bwPhJuJj2G7z_WIYglvzRya2GZA7JyeSkA3DA8_qVXGPSDs0cOXrJDbzSUl73vHT0deveMVTAK_KMXXcrgPJz-v50ib1b_LUyNQ0X5PHnMor8BawdtqWezbk8qZ4_5QweQXuJtAlOSaDyyy4Qxqozrcwru_0KXTEGzXP40D-DIe4TTMimnQ2QC1eoKG8M4uYNLGQfmyCmLlVHL5BAv91bK5-9ckbTbofdZArNvntdPGRKy4q9jZLIkRUaX2wkEOYroslOVzEAn0oP2vJ5-k4geQ8WlDaO7_rgL7__As4VIRLlGJokO48l2oUuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fec637f4.mp4?token=oR-ryJVmPCPg2zutUAcOBkzFDJ2bwPhJuJj2G7z_WIYglvzRya2GZA7JyeSkA3DA8_qVXGPSDs0cOXrJDbzSUl73vHT0deveMVTAK_KMXXcrgPJz-v50ib1b_LUyNQ0X5PHnMor8BawdtqWezbk8qZ4_5QweQXuJtAlOSaDyyy4Qxqozrcwru_0KXTEGzXP40D-DIe4TTMimnQ2QC1eoKG8M4uYNLGQfmyCmLlVHL5BAv91bK5-9ckbTbofdZArNvntdPGRKy4q9jZLIkRUaX2wkEOYroslOVzEAn0oP2vJ5-k4geQ8WlDaO7_rgL7__As4VIRLlGJokO48l2oUuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنباء اولية عن إسقاط طائرة في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/85200" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">أنباء اولية عن إسقاط طائرة في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/85199" target="_blank">📅 01:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/85198" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7726b6f71.mp4?token=mVL9utd1gIl8QaOhpcXvuicPpaeEsGBgwyLuWnpuow0R67tShfJW3U3tv4K-66iNIopTlYyu1sx8DZzk666OxzP-CoDztw2Zya1J299UkjgkzrlkLCOmsU5uPWTOUVEnGJDx8ELwkcVlTuBxnniCG8WYUg95GtBVNtK5bSg6u3dtbQmnTmjkMUUxLXjNIUnjfzk34ZoY23cMyCy_gYfH0l6NhzmHqPEctd1SyzzOzWg_Z-gJIdgo96yDdy8QvwQiZ2rjD7R5yujtRtF_8uda3hXOMS6eKDYJJAwP79f0hTgwWwiRimJ4obv7rRyvCDQEb4SsmvS83TLa4vZf9kdxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7726b6f71.mp4?token=mVL9utd1gIl8QaOhpcXvuicPpaeEsGBgwyLuWnpuow0R67tShfJW3U3tv4K-66iNIopTlYyu1sx8DZzk666OxzP-CoDztw2Zya1J299UkjgkzrlkLCOmsU5uPWTOUVEnGJDx8ELwkcVlTuBxnniCG8WYUg95GtBVNtK5bSg6u3dtbQmnTmjkMUUxLXjNIUnjfzk34ZoY23cMyCy_gYfH0l6NhzmHqPEctd1SyzzOzWg_Z-gJIdgo96yDdy8QvwQiZ2rjD7R5yujtRtF_8uda3hXOMS6eKDYJJAwP79f0hTgwWwiRimJ4obv7rRyvCDQEb4SsmvS83TLa4vZf9kdxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: "يرجى اعتبار هذه التصريحات، حتى إشعار آخر، على أنها تعبر عن أن أي أضرار تلحق بالسفن أو البضائع أو أي شيء ذي صلة، سيتم تعويضها من الأموال الإيرانية التي تملكها الولايات المتحدة وتسيطر عليها. قد تكون هذه الأضرار كبيرة جدًا، ولكن على الرغم من ذلك، فإن…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/naya_foriraq/85197" target="_blank">📅 01:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏
‏
نيويورك تايمز:
"على مدى ثلاثة عقود تقريبًا، كانت الأردن قاعدة مهمة للعمليات العسكرية الأمريكية في جميع أنحاء الشرق الأوسط." ‏"والآن، الأردن يدفع الثمن...".</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/85196" target="_blank">📅 01:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snajLzPN_GuJq2RlmTnHzL_ICFI2hXaCD3l7pA3FfB5vEYuheevt4O3wb_N-rhPLFJqyy26zkEb8vxzlreyG4_LdBLJV8w6OEVByKGTqvu2P4zB63RaGLY6Le-TcWlL8X0RxK46V-oTc8U0G9pMswvAZMCfw1h4ybX3rniuzai4FqCjK6xQ2w1ecudQJ4JqNvE1mVtEbpmr-SoxX5UkPBP4Su1ZQjoTviriBEFl_HQFJ_qJIn7z3SUHwwItCGWrzwZg3mTjFEFLwiw_xT9HErkTWSbfNkQ-btJ6FS4zOjjO5yG3SqfQIBWVl3pZ4d-47I8BGSS918kgMoGTWyx4DZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
"يرجى اعتبار هذه التصريحات، حتى إشعار آخر، على أنها تعبر عن أن أي أضرار تلحق بالسفن أو البضائع أو أي شيء ذي صلة، سيتم تعويضها من الأموال الإيرانية التي تملكها الولايات المتحدة وتسيطر عليها. قد تكون هذه الأضرار كبيرة جدًا، ولكن على الرغم من ذلك، فإن هذا هو الإجراء العادل والمنصف. شكرًا لاهتمامكم بهذا الأمر."</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/85195" target="_blank">📅 01:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
سي بي إس:
‏
إن الوتيرة السريعة التي تنفق بها الولايات المتحدة بعضًا من أحدث طائراتها الاعتراضية للدفاع الجوي وأسلحتها الموجهة بدقة في الشرق الأوسط تُشكل نقطة توتر كبيرة داخل إدارة ترامب.
‏قال مسؤولون أمريكيون إن الولايات المتحدة لا تستطيع الاستمرار في استخدام الذخائر الدقيقة بنفس الوتيرة التي استخدمتها في بداية حملتها ضد إيران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85194" target="_blank">📅 01:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
وول ستريت جورنال:
صور أقمار صناعية تُظهر أن إيران تعيد بناء مواقعها العسكرية بوتيرة سريعة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/85192" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUE2KRAso_-00IUu2rg2zomBe8HLPeg8hcSPsU77E7usZzHOjmPfHronu6w3cbKtkql0q6BKW5EIKJ73o3EjrxJPNUPQvfS_dldysP5Az_6wPi3kX5sUdIO5354V2FMUuY2l5x4b3tAyYJJQPd2nj-V_kSE_8AIdLykNaSabCpFyekOXVk6NaBPsmpvPB4W9P5RnEl9roKeO_0XhYWx8XWmldCxu-bPtAQX4NkmmLyG6YcYGvUOTxPFszrNYD0dJnwG5xgjxV0nUhbLxH9sj_IA1sGKMOBmnzZjndgurf5hi4RBHfJW1sssk0tfS2T3p80bzST8k_3h2sIVcg_xYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
مواطنة كويتية تطالب بالغاء فقرة الأغاني في التلفزيون الكويتي والتوجه لنشر الدعاء بسبب الأوضاع الأمنية في البلاد نتيجة القصف الإيراني
🔻
اتركوا لها تعليق جميل
https://x.com/sarahalnomas/status/2080376158214877597?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/85191" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر
🇮🇷
🇺🇸
الدفاعات الجوية الإيرانية تتمكن من إعتراض وإسقاط صاروخ أمريكي في سماء مدينة كرمان جنوبي البلاد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85190" target="_blank">📅 00:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0f2cc539.mp4?token=LjZFqQRHKgtazvTLxfR9WXBDhtifaibwQXcavB4GilvY6QAqtTlxihw6oUjozFckfVgK-g381FYUBs4SsqmbztTYGIVEKZkHVf0j9JoC_3R2kVe2Gwlmjxu5GEjNrYnZhbOWt6zADoszHlhvIkpaaflSSA_RjTVPZmraoXebdspgD5euT4G7wtSQgI3Qm_vKO784lVtffbjx8P6uh_KIvBWWpsWgwo950iqnj2dwJiXbR8TPC0JNySTNTBpumZiLJhyA-tXsrYY_gEoz6-maDvwpeuytkHmBhrPzh7VWMs-nYQ2oiK7ivE_CVLg2A3XoR5UUtxnZa8LkiABMYzW_7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0f2cc539.mp4?token=LjZFqQRHKgtazvTLxfR9WXBDhtifaibwQXcavB4GilvY6QAqtTlxihw6oUjozFckfVgK-g381FYUBs4SsqmbztTYGIVEKZkHVf0j9JoC_3R2kVe2Gwlmjxu5GEjNrYnZhbOWt6zADoszHlhvIkpaaflSSA_RjTVPZmraoXebdspgD5euT4G7wtSQgI3Qm_vKO784lVtffbjx8P6uh_KIvBWWpsWgwo950iqnj2dwJiXbR8TPC0JNySTNTBpumZiLJhyA-tXsrYY_gEoz6-maDvwpeuytkHmBhrPzh7VWMs-nYQ2oiK7ivE_CVLg2A3XoR5UUtxnZa8LkiABMYzW_7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أبناء البحرين الغيارى يستمرون في مسيراتهم الداعمة لمحور المقاومة والرافضة لظلم عصابات آل خليفة المتصهينة.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/85189" target="_blank">📅 00:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8547a511bc.mp4?token=dDcFL9__rjAKDYTAkrbS2dzmt-puCQ-UPwL8vjwVjkfIOpd4zvpPmoAWHKOzZ0TLCKEKh5XKM-p7llujJuS87mXUvmrMyyYWMIyFiR6Qw4RYxnyYmIa7wGfTPo_ofCF4Qy8NePJ2qcgirITPyRqZEt0LPUnoq9H7-RnHQG5R_mHIal3i5BJ2g73NcXtMd6uiJCBBiGHX-6vaR0dLdi-a0NhAYbIHAbBusCtQQMiQXCExI49bWOJPxOyLdj90VxvjbRTZL6klgR34lOFLvwCOrod0cs9xs_GdrwKlLyOj0cHx5UhI8lddNhs5ZKLx1bHP0tTwLz1S-91z1zsMlekTZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8547a511bc.mp4?token=dDcFL9__rjAKDYTAkrbS2dzmt-puCQ-UPwL8vjwVjkfIOpd4zvpPmoAWHKOzZ0TLCKEKh5XKM-p7llujJuS87mXUvmrMyyYWMIyFiR6Qw4RYxnyYmIa7wGfTPo_ofCF4Qy8NePJ2qcgirITPyRqZEt0LPUnoq9H7-RnHQG5R_mHIal3i5BJ2g73NcXtMd6uiJCBBiGHX-6vaR0dLdi-a0NhAYbIHAbBusCtQQMiQXCExI49bWOJPxOyLdj90VxvjbRTZL6klgR34lOFLvwCOrod0cs9xs_GdrwKlLyOj0cHx5UhI8lddNhs5ZKLx1bHP0tTwLz1S-91z1zsMlekTZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
توثيق من جانب العراقي يضهر محاولات الكويت بالتصدي للصواريخ الايرانية عن طريق اطلاق عشرات صواريخ الباتريوت.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/85188" target="_blank">📅 00:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
عدوان اميركي يستهدف جزيرة قشم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/85186" target="_blank">📅 00:08 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
