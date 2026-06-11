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
<img src="https://cdn4.telesco.pe/file/SsG_OQltecCAEmvZDhhlhhQWvM4D5lOciii9HaNkJHZ0jAUShxM6At604Kt5C8ezAocvFjWxFu8DnKpyOIs7uLLKaZ0Hd6_zVqfIcmQLOnNPokQ2UgFV3Es7HVkUd7D1_h9nH1shIpSi-BvqFmgzlsraJFlzomxVgKgUhcle7vNJ5w_biAEcVxJY9nSuaT9g2zoUbqhoJ_TCBD4CShgy-nICgh-x7-LSkl1tisu4womUOb55-pB3UIHAakY0R50z9CXp5hknr3YYCQ_yD6PZrrfhejbuoQ4-wty0lUByEBV3tdTPC7OpKQuVkNZu9jB7I5aVq5ExNLFjOXUJFsbXvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 06:16:46</div>
<hr>

<div class="tg-post" id="msg-77597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU6WqQgnd8NoiKqCeiwmeLRhYAa9fVckHxlS_ExsvvF77mc_wTADDRa1LhdsCfazKHlD7QySt82nu-uf1QhyOQS51dYLR5n6G2hRQtTuNLK5oe2qY30Es9Xd_vV37EyY5t_WMTLakLStuRFwAVL53mJgjSXrq4KRn3Iw4ZsCerqeER1x1UxCNfj0gsFpKrOrgtiP3jykglsOVxykAtgEdmP8RpTocBMDGhHGwo5Cg0yFtVYgd_5yz8w0CzNAk4GTfIy7pjyp1Y34IUrpNKQ0Dt1YUnNtiqAmQIWUo4-Nmct0xsTxmGouwC1UN9SvR-pBMkPIUtOqjr1jaoC56YwXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل نگارش کپشن
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/funhiphop/77597" target="_blank">📅 05:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77596">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/77596" target="_blank">📅 04:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=mY9bONupRNNbMzDxRwWdMgsJhh1h7a3OPkfFQlaFoDL45uI8qzD8TEFqOTjZK_vdUI8pFfNJYeGtsob8-64fj9vS9Qm4MjVLP3UddWkJOiSc1ECPLHKyVQFQrJI6C0rHRM5Uo6uXmUSOftKG4mZA8nnfdc6MXdEXbvXcPzDfFF2i3AdeZpGnhhhAg1K4RHHfUeTpjLM_uO9z1775Dax5NPxnZ5C0OsUD6EGkO24T9oQ8Pqv4FuTHjggCdtU1Tr-8WSNECrDzfNLXDEkOUrKuJKgqc1whUQY4fZ8Txgrb6Kx8eZYciq6xI0uJztRgf40LY0TiTVdIr0hxqDsS_8tPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=mY9bONupRNNbMzDxRwWdMgsJhh1h7a3OPkfFQlaFoDL45uI8qzD8TEFqOTjZK_vdUI8pFfNJYeGtsob8-64fj9vS9Qm4MjVLP3UddWkJOiSc1ECPLHKyVQFQrJI6C0rHRM5Uo6uXmUSOftKG4mZA8nnfdc6MXdEXbvXcPzDfFF2i3AdeZpGnhhhAg1K4RHHfUeTpjLM_uO9z1775Dax5NPxnZ5C0OsUD6EGkO24T9oQ8Pqv4FuTHjggCdtU1Tr-8WSNECrDzfNLXDEkOUrKuJKgqc1whUQY4fZ8Txgrb6Kx8eZYciq6xI0uJztRgf40LY0TiTVdIr0hxqDsS_8tPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام الان با انتشار این فیلم مثل دیشب اعلام کرد که فعلا حملات «دفاعیش» تکمیل و تموم شده تا ببینیم چه پیش خواهد آمد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/77594" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">احتمالا الان آمریکا داره خود زنی می‌کنه که حملات سپاه به کرج فراموش شه ولی نه ما نمی‌ذاریم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/77592" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قزوین و مناطق مختلف جنوب کشور باز صدای توقف حملات اومده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/funhiphop/77591" target="_blank">📅 04:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF9M0465eBOa_3Ei9bCbi6UBjMOH2E3CFP7V5ldZwfwWr0G-_5VoatU9dOsobtTceZgMk1-VDzJtagSX2NIHLcdHB0tStb5rVYB5Lm6c6pJSFsuVRTZHm3aTMbtAAkkgoMmep4x0E61kyg-89rc5RCGfrYKUPDPkGIIt9M6_7zm2AXQqAnpQ5CZ4OMmE2VxIX-id-qKLknX6lDOUE-Vrz90uZG-iwt6xUEjubeK2uT92Jp8XkbB51koKbYbs8jfXh5P7Cwn84eqrS1apm4aE1nY_sOFTX7-FxlD6zsZ096kX8UgwoGkkfFEU5Y8pKLd--LutQFYnAPcablFBhaPFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید بالاخره بیدار شد:
تنگه مقدس هرمز را ناامن می‌کنید؟ از سراسر ایران منطقه را برای شما جهنم خواهیم کرد.
این پاسخ به جسارت آمریکایی‌ها در منطقه است، ان‌شاءالله.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/77590" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/77589" target="_blank">📅 04:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/77588" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اوه اوه  هشدارها و درگیری پدافند در بحرین.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/77586" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اوه اوه
هشدارها و درگیری پدافند در بحرین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/77585" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/77584" target="_blank">📅 03:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/77583" target="_blank">📅 03:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا سیما به نقل از سپاه پاسداران انقلاب اسلامی: مهر نیوز راست می‌گه، سپاه پایگاه آمریکا تو بحرین رو با پهپاد زده ولی بازی رسانه‌ای دشمن کاری کرد شما نفهمیدید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/77582" target="_blank">📅 03:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946d468c47.mp4?token=m8H0u2pEqkggsKe3O0WPVOW8_Bb7K9MDva0Oxxkm7mg6glDgDt928AqDBJ2wh7KFBlbYX09XD0QxISDLVE-CfJaKv0TDkqOKa3NuHXmAdJHrK-R-1FoVckY-RtltJ013Y2uSWTp9K2eI1YrkIgxeBvAWwIVCuHb8AC3293GCcaUqxxxFrF5OHwj5h1vao0KQMPek9rBqEgE4xHpTuqL6kJJaAhF9RBxjEkOxSVxYAFmxLbi8mWU1fxaxMd0pKQq4dQOlihHZyM8m9OkPvxYgc9mk7AR09VaT1fv2a9QG1ugozo2roc6kWbnEn6H7GWj6-jLZ2V4qTWYDEM-rKITg6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946d468c47.mp4?token=m8H0u2pEqkggsKe3O0WPVOW8_Bb7K9MDva0Oxxkm7mg6glDgDt928AqDBJ2wh7KFBlbYX09XD0QxISDLVE-CfJaKv0TDkqOKa3NuHXmAdJHrK-R-1FoVckY-RtltJ013Y2uSWTp9K2eI1YrkIgxeBvAWwIVCuHb8AC3293GCcaUqxxxFrF5OHwj5h1vao0KQMPek9rBqEgE4xHpTuqL6kJJaAhF9RBxjEkOxSVxYAFmxLbi8mWU1fxaxMd0pKQq4dQOlihHZyM8m9OkPvxYgc9mk7AR09VaT1fv2a9QG1ugozo2roc6kWbnEn6H7GWj6-jLZ2V4qTWYDEM-rKITg6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر: سپاه امشب هم اون وسط مسطا پاسخ‌هاش رو داده موشک‌هاش رو زده باز شما عقب مونده‌ها داغ بودید نفهمیدید: مرحله اول عملیات های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد.  پراکندگی مبدا شلیک ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/77581" target="_blank">📅 03:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/77580" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/77579" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کرج زدن؟</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/77578" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/77577" target="_blank">📅 03:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: اگر ایران توافق نکند، فردا شب دوباره آنها را به شدت بمباران خواهیم کرد
(I will bomb the shit out of Iran)
.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/77576" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zlftju7s01rh-30dWZ6FJKk0XqwU7mtJBIsaF2_PXzLS3dSZ_LfpOWMdYKZ6L4K5pU0a9yptPEVhXwE9RafxYlKw0tAjDtICPjS5whazo5EQsLwX_EWwdlcBmKw3_4hh0xHLwPZvd6z80hxDPc3WgE3nawKPfTjfLXVnirb1bodsGL8lpf0kpUnNiG0qwxfZUj5A2EImh6BD6kIuaNqKCxNbo00rGCeS7hSlDUeEuld7JZUnpni3rU6FDr_eQ01QFLz4RAdjHgzTKjfUgC7Za49Mb-mPPuPD-lm6U02eVWzs2kilr0_sGP5ewrbv-PzSHY2_Q1dITidsXdqwb_b4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/77575" target="_blank">📅 03:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به فاکس نیوز:
این بزرگترین نقض آتش‌بس در تاریخ جهان بود.
(ولی هنوز آتش‌بس سر جاشه حرومز؟)
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/77574" target="_blank">📅 03:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/77573" target="_blank">📅 03:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: اسرائیلی‌ها در این بمباران مشارکت ندارند. من درها را برای بمباران بیشتر باز می‌گذارم اگر ایرانی‌ها درست رفتار نکنند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/77572" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: من مستقیما با مقامات ایرانی صحبت کردم و آنها از من خواستند که بمباران را متوقف کنم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/77571" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/77570" target="_blank">📅 02:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
بمباران به زودی متوقف می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/77569" target="_blank">📅 02:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یدیعوت آحارونوت: احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.  گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/77568" target="_blank">📅 02:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز:
حملات نظامی آمریکا به ایران همچنان ادامه دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/77567" target="_blank">📅 02:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پاکستان: به آمریکا اعلام کردیم که دست از میانجی‌گری برمیداریم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/77566" target="_blank">📅 02:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/77565" target="_blank">📅 02:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/77564" target="_blank">📅 02:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا اعلام کرد از الان به بعد تنگه رو کامل می‌بنده و به هر کشتی‌ای که با هر ملیتی بخواد رد شه شلیک می‌کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/77563" target="_blank">📅 02:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روابط عمومی سپاه: درپی تجاوز جنگنده f16 به حریم هوایی خلیج فارس و شلیک موشک سامانه پدافند هوایی سپاه به سمت آن، جنگنده متجاوز متواری گشت.
🔥
🔥
🔥
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/77562" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/77560" target="_blank">📅 02:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز: ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/77559" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77558">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینو منبعم زیاد معتبر نیست بذارید کامل تایید بشه که فاکس نیوز اینو گفته.
فاکس نیوز:
ترامپ گفته است موج بعدی حملات بر روی پل‌ها و نیروگاه‌های برق متمرکز خواهد بود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/77558" target="_blank">📅 01:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77557">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">موج جدید حمله‌ی آمریکا و فعالیت پدافند در بندر عباس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/77557" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77556">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
اسرائیل در این مرحله در حملات به ایران دخالتی ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/77556" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77555">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نیویورک تایمز:
امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/77555" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77554">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یدیعوت آحارونوت:
احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.
گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/77554" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77553">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: امشب چند موج حمله دیگر نیز وجود دارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/77553" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77552" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77551">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایرنا: فرودگاه بندر عباس ایز دد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/77551" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77550">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77550" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77549">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک سری گزارش تایید نشده از ترور علی لاریجانی داره منتشر میشه!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77549" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رشد شدید سهام فلافل پس از حملات آمریکا به جنوب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77547" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77546">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس:
تمام اهدافی که مورد حمله قرار گرفته‌اند در جنوب ایران واقع شده‌اند.
این اهداف شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77546" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شلیک موشک های سپاه به سمت بیکینی باتم!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77545" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزیره: اسرائیل هم امشب به ایران حمله کرده و تو عملیات حضور داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77544" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77543" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مقامات آمریکایی به کانال ۱۲:
ما انتظار داریم پاسخ ایرانی ها مثل شب گذشته باشه و پاسخ خاص یا بزرگی رو شاهد نباشیم تا آتش‌بس فرو نپاشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77542" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/77541" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77540" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بعد نیم ساعت صداسیما انفجار های جنوب کشور رو تایید کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/77539" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش‌های تایید نشده از وقوع انفجار در کارخانه پتروشیمی عسلویه
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77538" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77537" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAVKer6IkSq1YKo-7tLVycvn89ifJBX4GG3roci9-FlV1tbnbZZDgdujnl3LUyhDq567hVyzWmNl5iWsG_0CSMwXpud7mpuzwVRitQ-j2lFma2XqOhLtQTF9CcvsDXN15qBOF8kVZnpkN1-jGsrDxbqlTngCnzHWtC2S24vEnQ72djRC8UOFKEImDq-or306hy9OkKY9dN3jLS0EbR8io_rB8xmi2VppVybblwOCEeC1gKpZ0lgLCaa4eSY4i_CKl8abmayhlMoqcpIQr0TBwGGSIsrK7XmhY0w7YPumIdl-o1017Is3piecMNFyXu6I9GjTJvIq8-Arx93y4nV_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
حملات به ایران را از ۲۰ دقیقه پیش آغاز کردیم.
این حملات در پاسخ به تجاوزات بی‌دلیل و مداوم ایران است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77536" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سه انفجار در قشم گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/77535" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دو انفجار در بندر عباس چند لحظه پیش.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/77534" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">باراک راوید:
ایالات متحده حملات خود را به ایران آغاز کرده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77533" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فعال شدن پدافند ها در عسلویه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/77532" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تایید نشده:
لانچ موشک از سمت تبریز
احتمالا به سمت اسرائیل
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77531" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجار در میناب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77530" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۲ اسرائیل رسماً شروع حملات آمریکا رو اعلام کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77528" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل سطح آماده‌باش خود را افزایش داده است تا برای احتمال ازسرگیری درگیری با ایران آماده باشد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77527" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرید جان سیریک صدای انفجار بد اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77526" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تهران صدا انفجار شنیدید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77525" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری مهر: فعال شدن پدافند در غرب تهران.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77524" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77523">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حدود ۱۵ سوخترسان آمریکایی در آسمان منطقه درحال پروازن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77523" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77522">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فعالیت پدافند تو قشم گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77522" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای انفجار تو کیش گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77521" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سری قبلی قرار بود ساعت ۲ بامداد حمله به زیرساخت هارو شروع کنن و آتش بس شد
پس این سری جنگ از ساعت ۲ شروع میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77520" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: یه ساعت دیگه بالا باشید خیر نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77518" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77517">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر جنگ آمریکا در ادامه:  سنتکام امشب شدیدا مشغول خواهد بود. ایالات متحده تأسیسات کلیدی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد قوی و صریح خواهند بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77517" target="_blank">📅 00:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:  همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77516" target="_blank">📅 00:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:
همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77515" target="_blank">📅 23:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=tZczUASVq4KCEfB5Ys6wZ2IgS4B3Hc9o8F4sb05OhSciVnXf_Ckc9qVpYRjNpo1dMqlJMnI8gPTpFLxU1BwY7ocNBjRy9FrKvxbtKGnouNGveYYLecTEwik6BumpojSijhKxJmzv9bXSZEEGds83ECaQdvgIl7XfNEKPM8hW-s9we704VHNrd7RPSA1ObDUBqwXVCClv8N-3pPKUu_w4GdgY27Dej1cXW8udgQsqL59rkHXAxkiUaoQhGEDwSpTJXYLzV0blkGrvd1jZm9vFR2WwGXvhoTd4hi7I6YwmK_k0XQ6se9CRGmzoEa95oete-xoKw4ndkO6udifn9zbRMw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=tZczUASVq4KCEfB5Ys6wZ2IgS4B3Hc9o8F4sb05OhSciVnXf_Ckc9qVpYRjNpo1dMqlJMnI8gPTpFLxU1BwY7ocNBjRy9FrKvxbtKGnouNGveYYLecTEwik6BumpojSijhKxJmzv9bXSZEEGds83ECaQdvgIl7XfNEKPM8hW-s9we704VHNrd7RPSA1ObDUBqwXVCClv8N-3pPKUu_w4GdgY27Dej1cXW8udgQsqL59rkHXAxkiUaoQhGEDwSpTJXYLzV0blkGrvd1jZm9vFR2WwGXvhoTd4hi7I6YwmK_k0XQ6se9CRGmzoEa95oete-xoKw4ndkO6udifn9zbRMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام تصویر لو رفته از عاصم منیر همین الان:
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77512" target="_blank">📅 23:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77511" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">معاون سیاسی امنیتی استاندار قم:در ساعات گذشته هیچ‌گونه فعالیت مرتبط با پدافند در استان قم انجام نشده و اخبار منتشرشده در این زمینه صحت ندارد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77510" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷  فقط ۲۹۹  هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77509" target="_blank">📅 23:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq1dX86aZFU-VvpWiSl6TNt_WNXBO0O3SuU_QhmFvcYPZ8Sr8XtS8DxE7mk98dykosBofeUXhdyJ7m_tjkkjU1qUvpL7zU9a9TFS8N70IzDP_2YP3OGiGFNYevAUAhlLLqfkuu7sCy30h6i8DlEZ53sI_SrDqvrEv0KPhZo4u8R4-O7u6n35JtQikJzChwSZkx6kdFDzzTQXlZni0gXGt_RAJJnqCCVnF_Lkw6iTSXEggBZTDW2NscMAI7AfQVvAS8TwsN1EB57hTkIUu_jlzYpvxoQHD-R-Cn1tfT9bih58CP3tBM9prKFFDqyLvxyJbVtXkzf65Of2lE9YN6k_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷
فقط ۲۹۹
هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77507" target="_blank">📅 22:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0anW3yOjSTlewdn0VOOF-gU-yTnNZO7myPxBMh-H5YRGuA5rVj4OostxEU2nwKB-c77t4A9TFviGPzBaWkklbxJUmEJTzunIrGIVyUUvlDukxTITUA-96BNdXcRfg_x3e_cCtani6bV3uU8rSFwMU2ErUtH1363MsMkXe3lRTFmqclb9TGAwCz7Z3qi_12ykshpRWLIc8zPOUGbF47cWhGYhiOmOs_J2qqGVXCmnGaC9l5pHmuxGX2If74O3oEVARb4eYo33ACHe3Yte5AdbwYck5n9j6ERl_5XZ_7YhqPBgPF8dTaCmt-OCfhO5wznf6RNFQRJUeylHcnjv1ZWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس رو نجات بده خواهشا:
در جنگ ۴۰ روزه، وسعت آب‌های سرزمینی ایران افزایش یافت؛ در جنگ بعدی، شاید وسعت خاک ایران افزایش یابد...
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77506" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آکسیوس: مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77505" target="_blank">📅 22:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آکسیوس:
مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77504" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_PKJuqK773vp6Nnj1kFe4ZYAuNG8AZRXCD4JSYE4fS7qI_RLREZ20v01r3gy9YjdEyfynJF5ck2ImrtcZTLcBr3IO73Buyh8IjUfscvydre5nHeNBqIK6NrN807vVeRROhew2qJwlBUrWSQRxIzBo3h3gpMKftaQASjNloIr5aLpWRLZQKDJDD5-i7v9QcTnptvxO9qJPw4AQTE9284hgA-rh_swLYU-iisQWB_E9TggqKjmvIjTxdZWO0HUlhmjnaOhsTGozN_S3AmKt3JRTRR7W08vBodmbNQCTnjN982HAlsRUVes7QQj7EEryaDRODySEqill5jzM5bvOjc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام وحید جان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77501" target="_blank">📅 22:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جواد خیابانی بالاخره ول کرد و بازنشسته شد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77500" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77499" target="_blank">📅 21:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtBxyuDkClOZqgaB8tGwC6VXKTwfrt3grzTSIFxIm6fXmGYBP9r02eXm5RGs0b0aBs8MRctctOkDzVK1xvas0ShulYlDT0S4mzMak4R9IWam6XSEFC8gjtrIhY_nPK3OutIKQ_zxDkKa9c9T1el5oBghp9Rb6CSzyClZl8LukU90VBicSjMO2T4a3dA0YRuu_O9mlmR2ThApl6Om8eqAsIvZHJPxB5LW_N9obGVyd1R6PPXV0QPt61Sgjnz8-rtvUmfxBqRAMYI_Ovcczrpwnb4cstqZYVM4G0ZgbeiebXlwckiRjzE3KM_oHKYut_XVLRuF7oGkHCgojCwjBZcR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77498" target="_blank">📅 21:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlgcqvNcuf1FwVNJAxWJJDPuQNCk2AA0zMoHDZTTniu0kNXzlva2QVmlhTXWfsQSUL66DQZ1qkraWtoNp7iitaJOn9eOU1_4gfEarVPDH-XwfjroXVx20SvaZjmr4Pf0J1QDrdxnhYLLT_IX2IcCHcfWPcfOUSC6p6IiPPQZ8YaCjaz_ORdDEvPRhZBPM-J4SYja8zxD5nR3wvo8tOqhJF6xGEsDFony9jgN16PUnytY5daihRetEnhHOEFDrPaUBUAhxjYsAzy8MgT5fA7KPZsfGfoGtLbuLSwyJcGZ_re-8TaEWvbCWRe4xEP9P3K94U5NEjYxIseyatPXOcqwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تو این یه ماه گذشته که گفتم پروژه آزادی تنگه هرمز متوقف شده دروغ گفتم.
☺️
ما داشتیم مخفیانه اون پروژه رو پیش می‌بردیم و ۱۰۰ تا کشتی تجاری و ۲۰۰ میلیون بشکه نفت از تنگه رد کردیم.
ایران نه کنترل تنگه هرمز رو داره و نه اقتصاد و نه نیروی نظامی.
کار ایران تمام است!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77497" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300a3fc2c7.mp4?token=SK3jmNWM1Ed8sEY0zECpl4Cqyw_7i3NcwKr1iHGBR32qbu9zx9E78ZgqxA4AoE9qhvFokqptVgZ-Ny4h5vSw1oF0T6zVWNZhhjuB2huTreMNtACfWFDkL0I28cO9O_D49R4V7mNhZp_Cs5eWKIEPHcUInNd2UoCI4m6-lRWS8b6YFAe3xA-bcep-_ha1dgaI0OvKX3w7OAICNtbBWm3M6hQrGz7erUqGQ-4SNw6lZsxoc_9KY1BNTaPXLh1lbbeVnOuPtBjU8dovIuNBoVfOz_Dgs5rBRNciJUf89dow55kHUQjhFsiCu_Ifw6vut0ybqhqh-8yNzfkjdj1kDFlOoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300a3fc2c7.mp4?token=SK3jmNWM1Ed8sEY0zECpl4Cqyw_7i3NcwKr1iHGBR32qbu9zx9E78ZgqxA4AoE9qhvFokqptVgZ-Ny4h5vSw1oF0T6zVWNZhhjuB2huTreMNtACfWFDkL0I28cO9O_D49R4V7mNhZp_Cs5eWKIEPHcUInNd2UoCI4m6-lRWS8b6YFAe3xA-bcep-_ha1dgaI0OvKX3w7OAICNtbBWm3M6hQrGz7erUqGQ-4SNw6lZsxoc_9KY1BNTaPXLh1lbbeVnOuPtBjU8dovIuNBoVfOz_Dgs5rBRNciJUf89dow55kHUQjhFsiCu_Ifw6vut0ybqhqh-8yNzfkjdj1kDFlOoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست هم اکنون
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77496" target="_blank">📅 21:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b65b168.mp4?token=Wqd1byqL7oa0tax7glIF7KXsIvU06bG5d2PizFgQh8DBm65_dX0G3ACrhZCwTDBnP7ZnqzQFtcAHdZtIA42f5gGyb4Ekk9FbcQK3FDQjn5kamXhGA2fh_loC_Y4U2x43QzyQZIepb4NBh3JdMMDBHgxopqoL6W__-_dzQYjrIsDIvBai_ZnOwgMeYKHvWzK2EtiQUlP-8QM9Q51Age_gx10RaZJFSCaxi6CLrtV1JWCXzWWtSi8bzZlbP90Io8S6Cdk6iQZXau1-0uc2TjPQMcMNoNFo03etlcpf6OImE_sDi-toNdyVh6-srA7MuRQlHan3YxakOgs0LysCNpDD53pT5YnkeVTW7fBHuUwiuGbU06TVDillMLnFDGxciggxLlAJ7rBUmvfFQ26S0STZQ6jsZ4T80TsVtG5IziOTCmvX9--a6BITfx-MAgDIijFH_546mru5UnK_tw9PBHUTjKDvZ63wxvLnOZQD4P0g9xp1W7mVTMvMAkXuZNE8qXoAsAgn4O7mh6DkUkRxNKom0IcssHoC9vEzfWAIZ-l1Sq6UiOiGHvbudz3IAqlYpW-jKd3vzAXb9onEajfXVGZwa4QSlUhn6gdTOuANoS2tMcwyTE4QVxo0s181rTl4u1G6-sCwICmGBY06aHbR35oPTvCIJRcJVixGB7uAOG87v9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b65b168.mp4?token=Wqd1byqL7oa0tax7glIF7KXsIvU06bG5d2PizFgQh8DBm65_dX0G3ACrhZCwTDBnP7ZnqzQFtcAHdZtIA42f5gGyb4Ekk9FbcQK3FDQjn5kamXhGA2fh_loC_Y4U2x43QzyQZIepb4NBh3JdMMDBHgxopqoL6W__-_dzQYjrIsDIvBai_ZnOwgMeYKHvWzK2EtiQUlP-8QM9Q51Age_gx10RaZJFSCaxi6CLrtV1JWCXzWWtSi8bzZlbP90Io8S6Cdk6iQZXau1-0uc2TjPQMcMNoNFo03etlcpf6OImE_sDi-toNdyVh6-srA7MuRQlHan3YxakOgs0LysCNpDD53pT5YnkeVTW7fBHuUwiuGbU06TVDillMLnFDGxciggxLlAJ7rBUmvfFQ26S0STZQ6jsZ4T80TsVtG5IziOTCmvX9--a6BITfx-MAgDIijFH_546mru5UnK_tw9PBHUTjKDvZ63wxvLnOZQD4P0g9xp1W7mVTMvMAkXuZNE8qXoAsAgn4O7mh6DkUkRxNKom0IcssHoC9vEzfWAIZ-l1Sq6UiOiGHvbudz3IAqlYpW-jKd3vzAXb9onEajfXVGZwa4QSlUhn6gdTOuANoS2tMcwyTE4QVxo0s181rTl4u1G6-sCwICmGBY06aHbR35oPTvCIJRcJVixGB7uAOG87v9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">I24NEWS:
آمریکا در حال آماده‌سازی موج گسترده‌تری از حملات علیه اهداف ایرانی در ساعات آینده است که فراتر از محدوده حملات قبلی خواهد بود.
حملات پیش رو با هدف فشار بر تهران برای پاسخ به توافق هسته‌ای که در حال مذاکره است، انجام می‌شود و نه به عنوان نشانه‌ای از بازگشت به درگیری تمام‌عیار.
تصمیم رئیس‌جمهور ترامپ تحت تأثیر حادثه اخیر هلیکوپتر، افزایش ناامیدی از عدم واکنش از سوی رهبر معظم، مجتبی خامنه‌ای و حلقه اطرافش، و فشار از سوی مقامات طرفدار رویکرد سختگیرانه‌تر بود، هرچند مشاورانی مانند جرد کوشنر و استیو ویتکاف از ادامه دیپلماسی حمایت می‌کردند.
این حملات با هدف شکستن بن‌بست دیپلماتیک انجام می‌شود، اگرچه دیپلمات‌های عرب هشدار داده‌اند که واکنش ایران غیرقابل پیش‌بینی است و ممکن است خطر تشدید درگیری به جنگی گسترده‌تر را به همراه داشته باشد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77495" target="_blank">📅 20:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">میدونید چرا آمریکا همش شب حمله میکنه؟ چون خلباناشون سیاهن تو شب معلوم نمیشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77494" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرنگار: برای تولدت چه آرزویی میکنی؟
ترامپ: صلح در تمام دنیا.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77493" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است.
حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار
﻿
پ.ن: پوتین یه چیزو هیچوقت اشتباه نگفت، که این کصکش نابغه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77492" target="_blank">📅 20:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
در صورت حمله آمریکا، تنگه باب المندب را خواهم بست!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77491" target="_blank">📅 19:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دخترا لطفا نترسین، میدان با ما آشپزخونه با شما
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77487" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDpRa6PbrQ17WEBEXp7n327K5fgq5QhnyiFCduz0sDQt1PBLDUh7xdj2kccdz45iJyTNVpR8KgdNNXoagxy0kdD51_5CUCB8MCFD2g57IXMtwBdl2sWSHZ_ph9HpLDNfwXCCCzJxWKEZSxf1FGgWY_PqmOb371vu8HjHjW0xnE_QomUntqNw3JFKh9BhY00i8qvoBVhdxiLTh36NmXpZ4JOTnVMOVWvOdS6MD3A9uJ-acdMAPpOE2rD62-YT3kg4ISc_pMrKnwvZHNiFOQD7Nzv71UMpmL42fbcJ99QoJZOy62cakgQM-CWiDiVR--Pq75Y17q4bIaGYtD94nKcN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد از تهدید جمهوری اسلامی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77486" target="_blank">📅 19:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ خیلی واضح گفت کصو کونو جمع کنین میخواییم کیر خایه پهن کنیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77485" target="_blank">📅 19:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سردار سلامی هم اکنون در اتاق جنگ!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77484" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:
امشب میزنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77483" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
