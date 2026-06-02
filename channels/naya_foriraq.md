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
<img src="https://cdn4.telesco.pe/file/DttAYQKfVWPjagU2q5aNNSZCupPBEG2xkyfDLqAcS3yM7qvX69FtYml7LryfnBz_ufzoVCd3XcymPk0vj-DT6ZVxpcDdBcNOn-2N81sA-a6QqbdU2Oj28wiESjNs_poO8B-AAEevsbInmlONAsJovemL0DkwOBzVFM0YmN8WPljWCf8O4SRXJIJqcSC-SihgrbQ4N27gBsaDJvLMYhXTZOhUEaEC2dpG96F_qpATDyGsqRD8e4c88xidx5hW7qfTzvGtmW0DH7fiLDSV8f5APE9uiEK6-hZwIQCFT6aJ4cJkCofjx9HGcXOti4vgs0aFvKNETpQTdESj4R12wUKCQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 250K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">توقف حركة الطيران في سماء البحرين</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/76810" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=dRw5EzuiLysTJYqy0GCZktQWqipGO8Oe2nUGvSVgIeOJnqwAtgXZZr0KMKsnNUPZMItaFcMaS3uhk6mSCYw2IDxGstRlBQDmSn8ZBoDLCFv7twW2ULJPL0OSfOwgXJ2HfyczMDRGfVkdUztEZBAktkIcE6nH6_0KJDAlv6bnaytdojRCQaBlvmFDoWSHHQLmKXVGmPcoUACDdBWBrvjrPQsnIJRB9U5h6bSiWLTUtV7NG_wQRc5fZDq07ktLQmYraxPfIjyDJI1pDH7npcm9Q4hjqAvjAzwZiXOXMWtAS53owsqkW_xm1wiaZ7W5rqJLBLfKEprBrUiuPJvgApyCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe9d3c1f.mp4?token=dRw5EzuiLysTJYqy0GCZktQWqipGO8Oe2nUGvSVgIeOJnqwAtgXZZr0KMKsnNUPZMItaFcMaS3uhk6mSCYw2IDxGstRlBQDmSn8ZBoDLCFv7twW2ULJPL0OSfOwgXJ2HfyczMDRGfVkdUztEZBAktkIcE6nH6_0KJDAlv6bnaytdojRCQaBlvmFDoWSHHQLmKXVGmPcoUACDdBWBrvjrPQsnIJRB9U5h6bSiWLTUtV7NG_wQRc5fZDq07ktLQmYraxPfIjyDJI1pDH7npcm9Q4hjqAvjAzwZiXOXMWtAS53owsqkW_xm1wiaZ7W5rqJLBLfKEprBrUiuPJvgApyCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/76809" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769c96fdc.mp4?token=lftdAgw_bMnKB68DMZ4pmFyvhWcB2E7zNt6eCVRvde1s1f7_o8kjc1Q9NTwc2kAfSmjqVCq4qgmbL8JloxfvudZOkjO8vPQqUbz-PAkRWN_ePDnd9sh7jOtH7sThPJp9v7JsW0M0nmeF9Pu4NQMAm2Ic_l4-NGI4wTdrZfkeD9Y7QT4p7BbHnoX_3njBZqsVUW3cRStbsI3HMp8GVdhdgVr2af3sSTveUR8pZRX0Tv3jD521HAT45vtrdMiPC0yAv788fQpGLEW0fqazyLda6U2SVtKKqhPYY1kMB3_HUtLhyePJraQeA0U6J84cRjX03rVSqzQKZRr-icuwFYiUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769c96fdc.mp4?token=lftdAgw_bMnKB68DMZ4pmFyvhWcB2E7zNt6eCVRvde1s1f7_o8kjc1Q9NTwc2kAfSmjqVCq4qgmbL8JloxfvudZOkjO8vPQqUbz-PAkRWN_ePDnd9sh7jOtH7sThPJp9v7JsW0M0nmeF9Pu4NQMAm2Ic_l4-NGI4wTdrZfkeD9Y7QT4p7BbHnoX_3njBZqsVUW3cRStbsI3HMp8GVdhdgVr2af3sSTveUR8pZRX0Tv3jD521HAT45vtrdMiPC0yAv788fQpGLEW0fqazyLda6U2SVtKKqhPYY1kMB3_HUtLhyePJraQeA0U6J84cRjX03rVSqzQKZRr-icuwFYiUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القواعد الامريكية في الكويت تدك بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 343 · <a href="https://t.me/naya_foriraq/76808" target="_blank">📅 02:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">استهداف سفن عسكرية قبالة سواحل الإمارات</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/naya_foriraq/76807" target="_blank">📅 02:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5327aa8b74.mp4?token=hCTdYxEdXZrOuDO0c4oTgnlz0fVo5mSuNKmAnbtntG9fsF5OHCYTiKU-mDCj4UBj-s2d39XmpXrAK-7ZvT8y0SpNXOpyhnTV2NwpaDYvdeP2AqiT8PGj8GOuHgOVB2pB_xfjqTqyNLsQ7fYW8HOYGdTBG4Z_IMX9p8D1n1Mqoklw3YPLKLnV692Yah8g2Kt_MEDAVCvknlFRvrO0oA3OzlT092TXujukrXdHfVxsRQN-So7XJx9Ly2qHBQHImEVXKDswfea7FWcOnB7xKyFKGc6FMCZq9EQP_3k34iAsVs5wugNjN_dTC5o2Lpcs_AJID6rr1xOopFnfE_Yx5uXTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف قاعدة الجفري الأمريكية ومقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/naya_foriraq/76806" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز أربيل شمال العراق الان مجددا</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/naya_foriraq/76805" target="_blank">📅 02:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74abf9487.mp4?token=TvjORGow1udcXsGYVX8c0TRgfc62gMna82y508IN_Dv7689ValgWWMBW9Al7UWUQ1Bc-XA-DJVGmpZOgqlFerEu1XmVrL9TqiaSY69_uMFjNh-PkF6et32p1jugpvDyNyZXrfcN91Mfz0NOTZh3GN7lv1lw5nFx164TK1XcqGBmKzNIK1QAMhjMAEtma4x0nFzB1Awqb69zNOYwGFZiHU-ksTm3ipd-pPpO5g72EFcKxHV7ymb9cF0rPkbsMvttS7khZwt-wFyLQQyXpItQj5vDUbwgLlO_Fdqmzl9-qBR3PQFLk4iw5md-YIfZzsB0VYNgz0mB0koZtpszt0CPVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/76804" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cefcea39.mp4?token=Gq3ZwxtELhROqQ1iKsFS8NHaEU57bDyIFgP68ix9VhwDQf3rKa5F4YKnBUQqNAPeLiOLmj6Sf6jXhNfB1CO_-AaWOwQwO77x2Ph5cbk19QV1EgFOQkMOcJNISY8LPP8UVxEpoV3_rv4dCuLKWUPQeVkbaTHhkn38kQeJuwoCtVCC6-iIws6WzYyTQk8d_oSufBQxwcdZqmIF4EZMyAAIq1O-UZLczcsqxITJtS-VUyp56Ty8BNLkumobBswP8OjhrAWEv8BazG6npy1moRLRDdDzoZQ8bgdWhmQ1nHiNcSwqPx3uIaePrdU6kJS9bJrpbeSxsIAkzaqU1v3ze1IMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/naya_foriraq/76803" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هجوم صاروخي على الكويت الان مجددا</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/76802" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/76801" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/76800" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صافرات الانذار تدوي مجددا في البحرين</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/76799" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c006192776.mp4?token=aGXitVGlzWpDUwZN3lRjT0fTazyTTGy4KqDVgSdiUHX-ZNI0KQKgSROTPXRCzfu9vXA-xDdWXH_3YXCjtHXRSRgB7qFe0t3fTcdATfxUIaUp5qBMi6aHfSTn_-gvvcL6PlewNnhZDMR-DMJaIX3KAimYOCtdFEswwTsZevH__p137di6AWNmvMQW8LMoOyyIS9yHmXhBhiqQB_I2EgSjznHntHSsHmjV8rVoIihXmnc3CxcASDhijsTg1_qEBs-s-Ztu-yL1JUL9gVmtZTfnIu1WgiH2_qVJKNoLRpF3vw3z5H5haD4Kw2_dD4tnjXdyVxBcv-diMBmqkyMqt-POrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجدد دوي صافرات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/76798" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuxkaRvvA6IffZfUMjxDxUqB_McZCenyswS3lEUwTVYxREm89X4aWeIHdl221jV4qURMFfYIEHTNny4ueQWUQfTTu3klOXF4uLSeOyvN21uWyObApsBmcbMoqInlVQcdgOXI7aSKiS9L3c4gR3vuiX1PebhJZKkaqH2I2YiMFuQ5Cq-kqK-Vro_ZEG7Wo9nYhzTXifXdTwQFU7qFNahODrr5GTjEOjd0mSYf4Ip1YXF17Sbq_QkHzXC3AJzfsV9x15zE4UM8a1kMPs6zQASLFx08mxeIKpiWykqPOOg1zPYDukbN8dcd2S_BOO5-y42Zgbvd0h-0g0U0DAKNMMrWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/76797" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bbb3482d.mp4?token=PTcQBL06NzJk7t_u4yB-8xJ24G7tnYLP5e-Otj39e_jKz9mj_W0n0G0h7lerxk5tLAxinZfQIgD5nblHNWAxDmIa2EFl-i1gr1y-5DVMjGztC3WQLJnT44VV7MEWTCCaDO0Yiod0DIWelcONIkUYoJGE27serGs4JveiMrUaquaVLF52dn6ezjfm07eBR1cIs2aohkSjvHIizNAJrqkeC0Qbk0fv7KWKFO1leGABzvd81ZwUFROFNyY9iEoUvvFhr-K1Mdc0kahIby04tEal0QMVWRVjGpTLIgc9TyfLnTkxdOTV4HW9U2-mSUqLIDcuvxZCsYuN18ueyugZ-FMo8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الكويت</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/76795" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/76794" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=YfOI0nPOMR-Wf044sl5pGFJNHrfnKPvO4fUdDU85MswQtKjTpunjN1NN-wr8yFAZ4nkQoilh1jlpiP9uhN_97rPsWOcpAkYQc6JBWbapBZD_JRyl0aghOeZyb9bX8bM-c91quryM8DePNE1AcXLVUP3RLoPsMfMkmlGKzFcdnIYxzem-DKObTdQhwolLsUVmDTr5MmboYfhmBLcF7nKN_hVSACX1W3INtzONxZVTKfGl26A95jMKKHAwfyCw3ZuhBKK0VQKu5rk0_THz8szAJRje1vCIx2LHNHax7xebr3zps41aFJtNT9llnSKd5xPhKEu3Gs9IkbNSx7C-paO03Hj9Y4xBNIQ0d5SAks96sNqHb4gLHrsEYzE0ujEW1ZLku1LUwbP0dEpkbcuwhdBPtmrxoJxtZXueRBV90oTnxPKTYvMjuOvaOr3AhIgVexzJRgpBa71t51PjpwelNob60ObfS-bmIhQV8qkUyNTa1e2iOHbi7b3HgOeApxTVY23UD2sggAYhDIy16LNG8EnwJZalgOXd-UiIdk_xv0_fuzEkLO6v74W98lMMyt8mgbHmpek6c482jzck2tA4-ff1RWnvWsRmgsKrn4A4gOYE5J5uqWf_2vUKdI-3HjSs9XMzJn8XCDF6DWmALUDK6AOvMdTQd-ukTgO0kmwuL797O1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cc4a4ac1.mp4?token=YfOI0nPOMR-Wf044sl5pGFJNHrfnKPvO4fUdDU85MswQtKjTpunjN1NN-wr8yFAZ4nkQoilh1jlpiP9uhN_97rPsWOcpAkYQc6JBWbapBZD_JRyl0aghOeZyb9bX8bM-c91quryM8DePNE1AcXLVUP3RLoPsMfMkmlGKzFcdnIYxzem-DKObTdQhwolLsUVmDTr5MmboYfhmBLcF7nKN_hVSACX1W3INtzONxZVTKfGl26A95jMKKHAwfyCw3ZuhBKK0VQKu5rk0_THz8szAJRje1vCIx2LHNHax7xebr3zps41aFJtNT9llnSKd5xPhKEu3Gs9IkbNSx7C-paO03Hj9Y4xBNIQ0d5SAks96sNqHb4gLHrsEYzE0ujEW1ZLku1LUwbP0dEpkbcuwhdBPtmrxoJxtZXueRBV90oTnxPKTYvMjuOvaOr3AhIgVexzJRgpBa71t51PjpwelNob60ObfS-bmIhQV8qkUyNTa1e2iOHbi7b3HgOeApxTVY23UD2sggAYhDIy16LNG8EnwJZalgOXd-UiIdk_xv0_fuzEkLO6v74W98lMMyt8mgbHmpek6c482jzck2tA4-ff1RWnvWsRmgsKrn4A4gOYE5J5uqWf_2vUKdI-3HjSs9XMzJn8XCDF6DWmALUDK6AOvMdTQd-ukTgO0kmwuL797O1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق اخر من الهجوم الصاروخي على القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/76793" target="_blank">📅 02:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e1fda2c0.mp4?token=nZeIUAHnMijbCOE_ZIp96vCQpzoI7Lxjlh7nFJu43vjjcrCW9dMbgF31vlUTyD1vPgCD7_gzGT0ug6JjxgnCzzLz02PVloXHpaju9d9a5r90c9Jj4s0auNX5XAGrmc7Iflcp8ZE3K3TX2LMHMiOiOWZAYl-eqVcNEgL24TS9dQKrd4Ol6Mjp84HwOWrCt-F_PSMNjivgV-YOt0Wqz7eCK8bwplEbbyru0LUUCVBA0gyKPQpLXsrkYEx9LsZaaqYyhf684SE8PVwORaEBHpDZWXWltb0Rg03NdAMvop6v0lFNJpa4uaaCE6qMN_ginat4l7keHBIHHs7MqnTCCvryW0oKJYYcwF1acnE-bl1Fz8PJCASpr7NIMbx3K1Y6H0UMQ0OBSKeAc9ho9lj8C8R-OvqUSYefDCwY2TArIYcfaJVNd0TkjZnyClGhYZj7v-uIEcErLprC9HRTEg0MyQNg_r1RXRTLG8VCn4MZNuzQZSwhvcfElWkFTFrFNXAN4bGBhtNLJHO5phz0cOBBzNSDxCNALXl4PKoCsRRFcWkZQtkbQpyBFJ351t1YezxAgVBBAnFBd4cuz1Gupz9FJL9HVflRwjZMUYXR-kSHRF_Fj_kAhXaiozsiHxI4t4Nfwyn7dkcCWz1QGVC2NF1F9dH-D4tufo9BsjjWW_m8A9oXtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء البحرين تشهد هجوم صاروخي</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/76792" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4c6cfc93.mp4?token=lCwjFhGcaH_aqZEOBB25bcoaBK7efHfvlwudz6v16QSQ2UMgJNnumCAd-1kkYUaVkQIZlU9Mib3W0zi0yrVzJ1mewgyxygrWOD-P6z0bip7oTpxaXAZ7izlI5JpsNthErokuYbhlrx-JZND_uCkDROyYGEpBORqfTDi9Wo6xUy093rIqH1cESOOHFdXL3PVvmmq95sA4aTxxV1UCwMAaG072bkCfMukFu4kodGAPy4xxqeIJPKj7jrAJV5XC3p_UK9STbHBWoN_IPngSsr4jmGSQ3QgmJbYjWy-k7FJqD_YMHWScB0o4_IVYlf9mS28-ZXFQPWEY9L3MDsS0NWtcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/76791" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc_3smLtDUiWO4-BmUF_PfPNl54ghRvBpC1T9-ST8QhzBj0xZ9IZL-tuoflEIe_dVYTMbYW1H6buZ0WPVMxJ6n4vqpIDrnRz-JD7KRo3m3PYU6BPM8-7fHgeqxnnRJzKYf9bb-znoehiW17RhMGfZ_agt8XIo-HGeJIRXbOUCldOIECIlB278ClhlZo9R7zvYtAySVQ0Zirh5Ak5iviHrLDzsQYT98i95MhbYEjBbCR4fPTK7EztyIpUtpbbc-dJdghn2u2hG8DGoDLIghiSdTzTBXz_QLbHiJlQZexhZwFj1McMVF6UG9OyJtRB5iTagNQO6AeDqhFzoObkAbwEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ تنطلق من ايران</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/76790" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e488c11.mp4?token=LnC4gbDU20YtA9DuSacck-vDDbXwBwjgAbajPVaB0ZcpD4blemV-8XiKoZ7dap5se1empPZOJXPe4S16yoJhhQ4ePHUocOwOikTLF38BNu1PgzQ--e2iuMJfo0U_sl3Do462J0RTJvOsZ2Qxew_r4-B-hLbtORA6vYyeDW5IYHAyIbyHKTtQRCKpGZ8B9H54nUp0ZEupHNoA3L0z_Ux_7h39ks3jWCECbgChe9JAWYidLpILlpxGsVsuF-YZ0AFGkUg31MfmC-xsAxYI51caIqDJ3eyZ6_GRv2uYoYd38oYgrN9Nui4zh01a22_sdqww4W0FXd-jpr_mxtFfl2t4bix4u0HCJAX-u6TNGl9kJUHExFCif7JCC0arAF280mt3JfykAYyhzLKmUQhmZjXeKH3K4aAQOPQ9zmO92KegvGbqxtQ1iV6c4hZDsnq1Z460I4MJbg6aBN3JpVTOdXQsRzo6m7tPJsJojIXYjCbjl5k9cAOLGxitb3I4Oy9gks_1EK472-IAnBmHM2mnzKsivDYpoYH5efLnJ_Vo_O496hROHyLdFXB3nX6HB5-C-byho9a_9luceMr5HDykzKLz0k1HZqAe0cQsaQBOYDyG_2610BnsIWg1nMo841oz0JhrUTJlJFVic4lrynzaWdajTbp4Lweao8dR3EQG80cXMxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/76789" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ab10aec0.mp4?token=ORRoFEFQ8zENUaybyOW9HvWKrg8uD65EggTc_Rx8IOyc18CbDIidgoyIEp_D2uy9DE3fobxd8Et9zu3S8mfznjc8KprgW94Tbx_7mq61jUY-aOxO7Xq2tGX5BzuHqIyNzd6L6H-OFpduh2Qq8gZI0Y4a42hi6YTh4szO1H9Lk7B-4T0kqD5gVFNomVcXICzTmnLmbixz4EmR8wguszO7WlTweW49haqpy5o-8DgqdjGEBPRvNR3QX0dkUc0w2k05pCdOKjEA2vZIjrB0xA1CytpWVh5qT3tCffMy9bMJUrehni7Tese1sb5savHqZxt937lZ8XPUjA35BjqhEkNfCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إيرانية تشعل سماء الكويت</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/76787" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky21UBlxaf1RU-o84V84CYUNrp4sEjwO1-3TsfEunyaJRUkxF20jJv8FiMmgD-eh5lQG_Ll2Ns86iyLsR77luHrWWW2S1pDSMaauTs9wJNJ7yi2A4EOAHR957CgPORtfu8T8-uy-USy6_hKOxp4twhPCY2Ow9jFjKMj2MC3avylF8T0c9RpWbqzPQR9GJ0CM9ttcd__oNHaS_Iisc2bxYivh2DITMII5SLUttk7JSuXOg4EioyN33j4mJHKTECTsbSbdWGtdaqNUXY0yR0l10BSnSo-Y8CBPZs2Y7RflbeO4LD0jchhhIGYqBaos-X3_OzTPF5-rwqWcJPD_ElP5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة اركان الجيش الكويتي: الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/76786" target="_blank">📅 02:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/76785" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/76784" target="_blank">📅 02:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئاسة اركان الجيش الكويتي:
الدفاعات الجوية الكويتية تتصدى حاليًا لهجمات صاروخية وطائرات مسيرة معادية، ندعو الجميع إلى التقيد بتعليمات الأمن والسلامة الصادرة عن الجهات المختصة.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/76783" target="_blank">📅 02:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صواريخ دفاع امريكية تتساقط على سكان الكويت بعد فشلها بالتصدي للهجوم المركب</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/76782" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a837cee.mp4?token=Wbj3xJlv9JM53xB9crRrYgmSHy7hmX7vC1AN2ySt-8-DoUgVnBrSFktmh0oAI6oI-RWJ3kb1wlGa4yKxCEHycfrXnBq6m8BPMhfjFSobGTXN_L9LxPTfUrck33DTE6Ptuoc6ErSznks8zZ5OcdcgBLXZJq1-SALQlAJ-091IOLQNgQ0wlFLP9mhMV41MlgAPUNPMQOKmT6ObBwCGTwBlSAdz0-qsDBcQifbJd27VyXQkM3ptRYNzyJxXZJQrVc1BIigIyPudngdmuKizN53CiNZNwW7IvAWcqCsVY0-kJRfzLWc0ZSjDpOpTXPDLRTNyFxock0NqtnxeFWbN3rGFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الامريكية في الكويت تحاول التصدي للهجوم الصاروخي والمسير</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76781" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4649ab83e9.mp4?token=iC6Z406rEQO9XdGgNXKusvUipjRA2Dij0XidZHBKgsEQmaC7HQ6kesv_32zn5uU-YpI_veteJRuvSfn678ZS1CmcRTxuMJM38xsk8BV8_vIm8le4qUW0ACpCA2kP8X2nD_6GGNhMahxdTRlGiTxsTsmmMs6z7qVa2XZ3nLfADGHQ9iEKBWIphjg_0PYk2pdFnAqXYOcnNDEBRQEd0YoXqN1rOI7Uc9mJtBUhO2G6kMJD8gX6tHGsCFMhNUwPjwy0VGj-MH33hDsRERDhj6Et1-VtUf726hMG4VIQHgZwBF_7s5vJmdR_mhTk5NYwjWeYMT-xFwPhg62K0a5Y1Eu_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من سماء الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76780" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3nizMuk33qBlbkh1Epf-lXjtc0IVhKJ4DqNlm1s8b4zz7OCNQA6zmBPZpciqnoFtrV8Zno3VkShF2saEmDu4O0lZ6SE6y25ggc_GSXmIaHKaKoyp43OBg9ZEsEzFmzVtMe3uCdmE7poCX7yQGH-38g1ifeCGIN-a41z-zGADMCgAsSnno8FSsaYzifTKDNh7s0MbX1kjg89P4FICz5_TkNi_J-f287h64KvD_8r5h5PeYdvGNAf7IyTiSSAHM-fgfzVg1UKz3Qr_ITNJeNYbed37j0kJ23N6oHeRBmStH1nwKSEp_p61nUIZ5hXlKdwJiRqhjf7nX5jsNRqvzqsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهود عيان: انفجارات تهز منطقة جنوب السرة في الكويت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76779" target="_blank">📅 01:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزارة الدفاع الكويتية: نتعرض لهجمات صاروخية وطائرات مسيرة معادية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76778" target="_blank">📅 01:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76777" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b49a37c30.mp4?token=deXtTyY4_M6ZLbcd_KcyInlIHsqD58tis46VfGcVsDXjXDXm_X2c5H8k1Pw__bruai5VAd8l6ix-jrCErxJsyEE4JKuNW6uYELMPArJnxkSOLf6jhCYKOeL3O-diRGDnXuyKtwrRnqiIoXm5KH7mCe88yj4PA2JkVkNjytTOk4_eqUe0CaAWQxBvtEz6xJeOWYpcWTan8AALYJdjVnDq4cDCnxdruae2-bXLlnziSyx27v5bScb6ndHf3jbiBjgaKTO_CK323EcVzeLnjbgSmxg0X8e5FJoKax-q3NyvwtitG3UhOfgN6gOyWs7U5UlvGfJ2Um87vXkgcFTI_zv_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76776" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم الايرانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76775" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce627a765e.mp4?token=o4Ogln7xBpxtOJB9FjKAFg4Cvyi70xvqMAUmykn5x8TN0ROdgTq1pG-yfvPE_XpWHgFQGJB4FE8hNcLezxJrHC9yCBOyrQvVMWLsBr2XbKFq5lng13JfMkxYVc5uoZL_r9wDwMoKDo5lfhckO1jcBz4M3xJSuNNessPldcGTP-NsfrJG0vgT2uAi5jr_ENNlGhp-ph2z23RJx0YP0LnvnARvVuZKpYx6VCmgz2oQKraLAQErxPgCaF9oYOjuTFsZ_B2aeo_CHlAV2O-s7bDbH1QoN86cukMVKiE9VBbJNN_PZxHqlmp4QUnqbGo0GbX961U78iHCNooKJmUtI202IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce627a765e.mp4?token=o4Ogln7xBpxtOJB9FjKAFg4Cvyi70xvqMAUmykn5x8TN0ROdgTq1pG-yfvPE_XpWHgFQGJB4FE8hNcLezxJrHC9yCBOyrQvVMWLsBr2XbKFq5lng13JfMkxYVc5uoZL_r9wDwMoKDo5lfhckO1jcBz4M3xJSuNNessPldcGTP-NsfrJG0vgT2uAi5jr_ENNlGhp-ph2z23RJx0YP0LnvnARvVuZKpYx6VCmgz2oQKraLAQErxPgCaF9oYOjuTFsZ_B2aeo_CHlAV2O-s7bDbH1QoN86cukMVKiE9VBbJNN_PZxHqlmp4QUnqbGo0GbX961U78iHCNooKJmUtI202IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل عدد من عناصر تنظيم داعش في صحراء البعاج بعملية نوعية للحشد الشعبي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76774" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
أفضل العقول في
شعب إسرائيل
، في
إسرائيل
وأيضًا خارجها، مجندة حاليًا لمشروع ايجاد حل لمشكلة مسيرات حزب الله. سنحل هذه المشكلة. سنُعيد الأمن والازدهار للشمال.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76773" target="_blank">📅 00:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6fd55fe69.mp4?token=Sk--sqEWjH66Gp8npY1WSbbkVX6aOT03I4OhHVPgwkEEs_rIoxyWqHrvjIMq7F2_PwWPFYlWh6Fbey1x1s1bNA7j3W4-t88DysdMbxxVF9k8tjMnPEXlMd2bSMYwOn3Gvjs9PF1SfOYMDm2jo_LX2IkAJmbv76QQ4SeuGNp1s3xQe_lVOhyrh2zDeOBaWuYjSZ-GkFSfnJAotVgjT69ETmpLtsfrMuC75oUFmfa4ZpQ5Yu_xAaDJUlHCsnYGz2pKYG3TEs4fdocslr1zEImGeWXJvECG4QTzwXsuU25l2rg-6e65vmC080ycFksOqtxLwzS9Zp_2vMMJ978MBHEvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6fd55fe69.mp4?token=Sk--sqEWjH66Gp8npY1WSbbkVX6aOT03I4OhHVPgwkEEs_rIoxyWqHrvjIMq7F2_PwWPFYlWh6Fbey1x1s1bNA7j3W4-t88DysdMbxxVF9k8tjMnPEXlMd2bSMYwOn3Gvjs9PF1SfOYMDm2jo_LX2IkAJmbv76QQ4SeuGNp1s3xQe_lVOhyrh2zDeOBaWuYjSZ-GkFSfnJAotVgjT69ETmpLtsfrMuC75oUFmfa4ZpQ5Yu_xAaDJUlHCsnYGz2pKYG3TEs4fdocslr1zEImGeWXJvECG4QTzwXsuU25l2rg-6e65vmC080ycFksOqtxLwzS9Zp_2vMMJ978MBHEvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحشد الشعبي العراقي يقتل 3 دواعش في صحراء البعاج ضمن محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76772" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc9160db4.mp4?token=F7B7g9iZyE1Q2I7nU6gttRCKpBISHSGkuvlujo9qMLIMx3SwmQEAv77MO8wB4963JiIAsN4tecGohSkUPj1zNjvk9wtGoAmpXNgzayh9mUAMdAD2h-hoRhL5FP4QlkiSdROt4TOxRHFq7DelLBt1luVN2_dRg-lA8_rHdRYxrj13qEn1q2tfS8IGwxpzv1sQT_dI3Pn1eUExKkwrt_RQsdjpF7MB2ShTEU5bqQfkJEc73QlhZQfK2rLkUcWSH_a_1XG1qJl_gBvARnHeBHEzfdtZJnsDnRnx_S78gw9KVd4lNDGJ0cGsiLR-ZR8GF2yk3LigifpFwYXTzULoL9wfpYX4G-C-pB9ZJWFFgIp7r9ag23EPfM_NMewNGZd1pk-pubFVP0m7NZ5hRS7Ee89kC9artfIgSw-JKTcorbCcLUO3UeNhuQ4ie0WrJO4Xs1D33lFHg25B469YfjLqsfgVVXKoLOxiPB5HoiKgbQrczD9E4VkLYOFFNaA6moCGAltEaf3WLzsoMUTExkmPfI10rgt38Yg7ZDN-ELRAi11-WTOD7URKzh4VxUb1JAf63n3A2eoLU4__UgLoauo_J4WXt5lpDO4Yswj8g0vh_NfhHJ8BanKFlXxrtSeJn6ARDpKApyPbRWun4nmvOupHBT7A-I-ZbAXUKvQ3MPzRespOcx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc9160db4.mp4?token=F7B7g9iZyE1Q2I7nU6gttRCKpBISHSGkuvlujo9qMLIMx3SwmQEAv77MO8wB4963JiIAsN4tecGohSkUPj1zNjvk9wtGoAmpXNgzayh9mUAMdAD2h-hoRhL5FP4QlkiSdROt4TOxRHFq7DelLBt1luVN2_dRg-lA8_rHdRYxrj13qEn1q2tfS8IGwxpzv1sQT_dI3Pn1eUExKkwrt_RQsdjpF7MB2ShTEU5bqQfkJEc73QlhZQfK2rLkUcWSH_a_1XG1qJl_gBvARnHeBHEzfdtZJnsDnRnx_S78gw9KVd4lNDGJ0cGsiLR-ZR8GF2yk3LigifpFwYXTzULoL9wfpYX4G-C-pB9ZJWFFgIp7r9ag23EPfM_NMewNGZd1pk-pubFVP0m7NZ5hRS7Ee89kC9artfIgSw-JKTcorbCcLUO3UeNhuQ4ie0WrJO4Xs1D33lFHg25B469YfjLqsfgVVXKoLOxiPB5HoiKgbQrczD9E4VkLYOFFNaA6moCGAltEaf3WLzsoMUTExkmPfI10rgt38Yg7ZDN-ELRAi11-WTOD7URKzh4VxUb1JAf63n3A2eoLU4__UgLoauo_J4WXt5lpDO4Yswj8g0vh_NfhHJ8BanKFlXxrtSeJn6ARDpKApyPbRWun4nmvOupHBT7A-I-ZbAXUKvQ3MPzRespOcx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحشد الشعبي العراقي يقتل 3 دواعش في صحراء البعاج ضمن محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76771" target="_blank">📅 00:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76770" target="_blank">📅 23:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76769" target="_blank">📅 23:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a991e7184.mp4?token=JysW3BxH6iM9SJAvcK4Fiqb1itfmnGBk2RHp_LUx025pJQSpIK5BoqcYXMV20Cc9ZaQ53UywbihG2iNhGbRgJMdM9FqMyvsrVCoKeVHpjWD5U2g8_YBiWow4pO88Ma6BjLDOWvCRHZ3_EKEFc2yvpuhGC3nT0tgk2oCQgMflmN7DMNO3FeMgRFT95lnin5kedIF5LDQYLgmAQCNRj7U_QvtGcYjcY9YeGq9qAE-2nEVzP5obLKOfSkTCsMrMcsbcvv2CAkTZzxgRvHyxgz0cIEZ6Z16MHFuQSYIzTHtgMkPtzs0t7voMwB4xO5xXnlMkD2XIJ8viSfwlROIaF1875w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a991e7184.mp4?token=JysW3BxH6iM9SJAvcK4Fiqb1itfmnGBk2RHp_LUx025pJQSpIK5BoqcYXMV20Cc9ZaQ53UywbihG2iNhGbRgJMdM9FqMyvsrVCoKeVHpjWD5U2g8_YBiWow4pO88Ma6BjLDOWvCRHZ3_EKEFc2yvpuhGC3nT0tgk2oCQgMflmN7DMNO3FeMgRFT95lnin5kedIF5LDQYLgmAQCNRj7U_QvtGcYjcY9YeGq9qAE-2nEVzP5obLKOfSkTCsMrMcsbcvv2CAkTZzxgRvHyxgz0cIEZ6Z16MHFuQSYIzTHtgMkPtzs0t7voMwB4xO5xXnlMkD2XIJ8viSfwlROIaF1875w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل 4 أشخاص واصابة 12 آخرين كحصيلة أولية جراء اشتباكات بين عصابات الجولاني في بلدة زاكية بريف دمشق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76767" target="_blank">📅 23:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو:
نريد من رئيس وزراء العراق الجديد معالجة مصادر قلقنا، نريد منح رئيس وزراء العراق فرصة للنجاح</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76766" target="_blank">📅 23:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
أصيب مقاتل في الاحتياط بجروح متوسطة وأصيب ثلاثة مقاتلين آخرين بجروح طفيفة اليوم نتيجة انفجار محلّقة مفخخة لحزب الله في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76765" target="_blank">📅 23:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2zr3c_UYFEbCQfAZHswNrx8BzQJi3w_ARPhwnOyw3Tyl1WEyrSZrcaBthauV19djXdAdY2LS1rXzmVFwvR5yK9pUMHOEXfWonfamyQvJMB3IiP-k2e023IIZPR4cNWEnofbkyiLnLzaUy3u2EVJjP9V_xje82_lgzGmrbtlvrRsYi_j_5HIULWuxihhFw88HDw-8MlWGIrrp7Yf5w1nx80YXcN5GUV-ZUndyDdCtkhReWy0cujLaaPj1glyyvoE9IQ8tl8lMTq2-Ddl3yPD3ui8pog8ik9oO_7-er_9LOtP2FZyJ_RBF1SU6V1Ga56Hh56HoH8mHQMLlUQaQc1F_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
توم باراك يشيد بالفصائل التي نزعت سلاحها
:
نتقدم بأحر التهاني إلى رئيس الوزراء العراقي  على هذه الخطوة الهامة، التي تُمثل حجر الأساس لحكم ذاتي عراقي مُتجدد، قائم على استعادة السيادة، والاستقرار الدائم، ووعد النهضة الوطنية. كما نُشيد بالجماعات التي سيُسهم قرارها المبدئي بإعادة جميع الأسلحة إلى الدولة العراقية في بناء النظام. إن ثقة رئيس الوزراء الزيدي في محلها، فهذه ليست سوى البداية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76764" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ‏روبيو:
نظام إيران لم يتوقف عن دعم الميليشيات رغم العقوبات ومتاعبه الاقتصادية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76763" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abYL8QVO6wVHou1lJJyK5-VskCxRLNBcd6VvYt-rgxVBWLgkrXmwlXTV3V_NbjxW3Pp_FhA9gTU1lzfZ3-XWxymRgA6PvyIsnVhesyEvoKdV3iZM2OlrRxTUUz1Qy-aD23G8uPuC8coKNMILeP5_uSkSMxRAfCO-_6epr70Rzco1vjaeH4d0Kmks-t8n57j65qddJMZmTjAA3KkQGOZEC_X7i5VYWroCvP1_JP2FZUPuyPHn_v4mWuFWXx4XkdnD5E2W1KSO6ycYM-ZVbTO3xWLL90eYhqYQMHF_Cxp6RRe5sJykwh15Fh-TqG3AkulUm8L3UspH3MVpVNI7__d0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يسرق المهاجرون غير الشرعيين والمحتالين الأجانب المليارات كل عام من دافعي الضرائب الأمريكيين. كجزء من الجهود التاريخية التي تبذلها إدارتي لإنهاء الاحتيال وعكس الهجرة غير الشرعية الجماعية، وقعت مؤخرا أمرا تنفيذيا جديدا قويا، ستقوده وزارة الخزانة، لمنع استخدام البنوك وبطاقات الائتمان والمؤسسات المالية لتسهيل تهريب البشر والاتجار بالمخدرات والهجرة غير الشرعية والكارتلات الإجرامية التي تنظم هذه الأنشطة. يجب أن يقتصر الوصول إلى الأنظمة المالية لأمتنا على أولئك الذين لديهم الحق القانوني في التواجد هنا، والذين يشاركون في التجارة القانونية والمشروعة. سيتم إغلاق الحسابات المصرفية المستخدمة لتمكين الهجرة غير الشرعية، أو لتخزين الرعاية التي يتلقاها الأجانب غير الشرعيين، وستواجه الأموال في نهاية المطاف الحجز والمصادرة حتى يمكن إعادتها إلى دافعي الضرائب. ليس من السخرية، ولكنه خطير للغاية، أن أي أجنبي غير قانوني يمكنه ببساطة تقديم رخصة قيادة الولاية الزرقاء، أو وثيقة بايدن الحدودية، والوصول غير المقيد إلى الولايات المتحدة. النظام المالي.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76762" target="_blank">📅 22:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e781b52e.mp4?token=q74q9I55EG4LYRVOsdvhze1Yky0WfftHwId9IwO1wbF2PSuSsN3-yRarnIsQYR1NjFpP9GDLeUOs5HPoiTkmW7F9WE3f1rft4ryyNllCHhVKMvw1mU5gagiMJomy5LdXZLoOuo1xY01JGND3T83z66v_-5GDf3V4B3ppxWCmz8V2JAoxjVBh59jh1RETwMOjAzsPiwF1HZjeqotCd2YFS0o8wnQps_Sj4_MrIP4tccGspQ0_0Q2W03byPBQQLphuNy_SRnj8Z6V4YcnsutYG1vc0TgB6EAcOy-Se-ZqKUAVeQLfNrMGe0QQRbbNQ_bOMf4P1chHyZcGQdExNbLbdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e781b52e.mp4?token=q74q9I55EG4LYRVOsdvhze1Yky0WfftHwId9IwO1wbF2PSuSsN3-yRarnIsQYR1NjFpP9GDLeUOs5HPoiTkmW7F9WE3f1rft4ryyNllCHhVKMvw1mU5gagiMJomy5LdXZLoOuo1xY01JGND3T83z66v_-5GDf3V4B3ppxWCmz8V2JAoxjVBh59jh1RETwMOjAzsPiwF1HZjeqotCd2YFS0o8wnQps_Sj4_MrIP4tccGspQ0_0Q2W03byPBQQLphuNy_SRnj8Z6V4YcnsutYG1vc0TgB6EAcOy-Se-ZqKUAVeQLfNrMGe0QQRbbNQ_bOMf4P1chHyZcGQdExNbLbdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
توتر أمني واستنفار كبير لأبناء قبيلة الفواعرة بسبب توقيف أحد وجهاء القبيلة من قبل مايسمى بأمن العام في محافظة حمص السورية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76760" target="_blank">📅 21:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUUkn5p6BlU7APyzcR5b5twmy1A7N31bHxgy5Rv41K7xppdHJpDcBCjfdkCT_Tuz5UilSvrREyXZZa-leEjOIwZdUYMMJFW_ymv-sHAB6Dqtg5toR_9V9pqb6xK0ABP4DSzgiCRM6qLvhPLm9WdT9P8lctSmkxYu30QkA-JmSp8RtAHug_tfctwIQC1ax5HG5Q0s5QutfjXexPF6DfuLECRjWxiZO_6IG-WBK0A1m7ePgqS-6-_0KF2KJx0HUR8EMmKHIyaifIKZwhWNSCFsUA8y47coINpKpKcFg3_-muzcZ75S_gAzcgRzgZRJzDltY-ZNtn2qu7v4k0hw2d-tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في إشارة إلى القوة والصمود، تم الإعلان للتو أن عشاء مراسلي البيت الأبيض، الذي انتهى بشكل عنيف ومفاجئ في 25 أبريل، سُجل موعدًا جديدًا في 24 يوليو. هذا الإعلان أمر جيد للغاية لأننا لا يمكننا أن نسمح للأشخاص المجانين بتغيير طريقة حياتنا، أو حتى جدولة مواعيدنا. لقد طُلب مني أن أكون هناك، وأن أتحدث، من قبل وييجيا جيانج، رئيس جمعية مراسلي البيت الأبيض، وقد قبلت. لا أعرف ما إذا كنت سأدلي بنفس التصريحات السيئة أم لا، على الأقل فيما يتعلق ببعض الأشخاص، لكننا سنكتشف ذلك قريبًا. على أي حال، ستكون تذكرة "ساخنة"! ومن المثير للاهتمام، أن المكان سيكون ولدورف أستوريا، في شارع بنسلفانيا، وهو مبنى وقاعة حفلات قمت ببنائها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76759" target="_blank">📅 21:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في حكومة الجولاني مساجد مدينة حلب السورية تتحول من دور عبادة إلى ساحات رقص.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76758" target="_blank">📅 21:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭐️
مشاهد جديدة من "حرب رمضان" تظهر دمار واسع في مناطق سكنية بالعاصمة الإيرانية طهران بعد تعرضها لقصف صهيوأمريكي غاشم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76757" target="_blank">📅 21:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭐️
‏
وكالة الطاقة الذرية:
لا نتصور التوصل لاتفاق مع إيران بدون مراقبة برنامجها النووي بصرامة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76756" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇦
ليلا عبد اللطيف فرع أوكرانيا "زيلينسكي":
قد يكون هناك هجوم واسع النطاق هذه الليلة على أوكرانيا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76755" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
توقفت وكالة المخابرات المركزية الأمريكية عن المساهمة في بعض التقييمات الاستخباراتية لمكتب مدير الاستخبارات الوطنية، بما في ذلك تلك المتعلقة بالحرب الإيرانية، نتيجة لخلاف دام عامًا بين الوكالتين حول نطاق العمل والمهام.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76754" target="_blank">📅 20:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKbxo7I7g68qKk2j_gec9NmtmbysmeK5otk3qI2IJ2YwCMPlLWBJQvlTDkexfqVjXGjqCMsazeA_HGDLRssGu2ks9qeo_dcqGeKJwG_mbBzm9rZ6Jco7ieoarswualLfkAsoClQ0gVDDIQwzC4Py4SZ8v-aVz5e70uYHS1OAzjq8MTzjtj4x-1na2BzagWveSH51crYkkpvKwkm30pEqc19dDghWcloM9VHvr6bqltAKj-ty9P6sIeXfGJS4rN3rvfxgscRGrpV62JDUd2IpMa09V9kMC-Rm-8SZ74-rTnRKvuDnvJSHy7Xi_BqkEzL8sggCVAS1_q6SH_HHZSbjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تقارير الأخبار المزيفة التي تفيد بأن جمهورية إيران الإسلامية والولايات المتحدة الأمريكية توقفتا عن الكلام قبل بضعة أيام خاطئة وخاطئة. كانت المحادثات بيننا مستمرة، بما في ذلك قبل أربعة أيام، وقبل ثلاثة أيام، وقبل يومين، وقبل يوم واحد، واليوم. حيث يقودون، لا يعرف المرء أبدا، ولكن كما أخبرت إيران، "لقد حان الوقت، بطريقة أو بأخرى، لكي تبرم صفقة. لقد كنت تفعل هذا لمدة 47 عاما، ولا يمكن السماح له بالاستمرار لفترة أطول!"</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76753" target="_blank">📅 20:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
رئيس المؤتمر اليهودي العالمي (WJC)، رونالد لاودر:
منذ 7 أكتوبر، أنفقت جميع المنظمات اليهودية في الولايات المتحدة معًا أكثر من 600 مليون دولار أمريكي لمكافحة هذا الفيضان من معاداة السامية.
هل ساعد ذلك؟ هل منع كل هذا المال - أو حتى أبطأ - الكراهية ضدنا؟
الجواب هو لا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76752" target="_blank">📅 20:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD-6buzosN2ycYa2I4KlDOhWvbh9vI9Pr8OyTwNQm7v3f-hu1qLztEs4vslHnZMx9Uzik3Mr0BY7GDE5FvY_BdT6fTCH68hozc9ioZ6nl6n--mcNJ1T894HafFgR_y-xJST3zpANTm6HVJR_L9EyFsB-1fEJ1s9UeD5hH3MGFJzH0z-aWAuRxa0DfrOEAuCNc3PbekuxUi1RQhDpKdOVOmCkkcR1r5KgrUy-78_8tklY9pMp_qeN8yGCpS7uhdL-uMT2mD_i2efOQp9yGyF-YshsSsVbqJBcNa1CoAyQwvjy3DdZ0yuZg2XA_-ka1O0-7enQn2W2FzUBw7gC7sHTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
‏
جيش الإحتلال الإسرائيلي:
سنصدر إنذارا بإخلاء الحي المسيحي في صور إذا لم يتم إخراج عناصر حزب الله.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76751" target="_blank">📅 20:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اندلاع اشتباكات مسلحة في السيدية بالعاصمة العراقية بغداد ؛ حصيلة اولية مقتل شخص وإصابة اثنين ..</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76750" target="_blank">📅 20:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25b0f6837.mp4?token=B1vBliOa9dbed24KqRQQuESxNd2-9owzNjzqf7nJ2OeUaw0dL9v-jPaGU4Xtxgc7UQBBtUNat8fK6YIR0y6jbfKTIEYXVUTz0tW9h3aMLU-Mxf6HMMOrrfdOodE52Ql4-u2yyLbRtosdzNByrHYsmTgdM-N2DRR7vympueiizSHzZXXf7f-8FXir6MnvUi8u7fX-IItXDORZicJpOfqUTqX4i1Nr9eXv-RFnjuroJcOOaN_SS0AEsA8HUfzf3iO-TzJMOcv6y87YjfmZF12q9BK0d0LICIsSn5ZVpuKFIjtWXfs1_Q8G00mmYi_svhAqJA2PlgINcMLBBSvoZGfXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25b0f6837.mp4?token=B1vBliOa9dbed24KqRQQuESxNd2-9owzNjzqf7nJ2OeUaw0dL9v-jPaGU4Xtxgc7UQBBtUNat8fK6YIR0y6jbfKTIEYXVUTz0tW9h3aMLU-Mxf6HMMOrrfdOodE52Ql4-u2yyLbRtosdzNByrHYsmTgdM-N2DRR7vympueiizSHzZXXf7f-8FXir6MnvUi8u7fX-IItXDORZicJpOfqUTqX4i1Nr9eXv-RFnjuroJcOOaN_SS0AEsA8HUfzf3iO-TzJMOcv6y87YjfmZF12q9BK0d0LICIsSn5ZVpuKFIjtWXfs1_Q8G00mmYi_svhAqJA2PlgINcMLBBSvoZGfXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي: لقد توددت عُمان إلى إيران للسيطرة على مضيق هرمز.  ‏لن نخفف العقوبات المفروضة على إيران مقابل إعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76749" target="_blank">📅 19:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0336d45622.mp4?token=AIwNbNseOihNF_7MznJwV1K0fYEC8gXw0egpr5evuSoKCIxp4UqODfOMEmikM-GZ33HCrVPCnvNwzn2HIeNxolppHDSqbljCD6UrpxlpLtmmHLX067cIn_oreQPkFqyZBY1z_q0ZPByJzVNL8cLhNSsSeuBLJsCy16lX0uL-vQqYhkzXtoR4WDVa5wsTfL7LfXI4gFm7TlK10edEf7Ak5cMgi4y_ZIElyeyc889A2YLp1jVwXFBhACszV5jFgqDGLu_I0WY7MLaLe4bHRdkENHSyzRia4p1Jj8kIHpxJrnufKmEdbg9kDyGDaOqZZ0eArNIM8wj1cTWxxA4CSSTpuRJkeHxX0LB5aFVPc-sAKwbc9XGRfIcWXRoTWH-QvzR50P_NcYNcdxD3oQj2Z_S-EsV3hLANEtXBa2ZbD_nYJRvDwBoN3tqaNWjr3Qf3CxFwsfCraHHEXAIfE8l5_wGM5WbV67PT98bCX35CCSE49YK49ZEpt8fezZxzJd1BkyvPcfaw-g7zIDSPWmR9c4gtuuoQK09GHu6qYAVXZvmNVG-yO64dDbBMW8tpjtXyDGPkXcsCHuPLoYPibzw9yeQBMf4ATOBQes3Jn1EkYuFXQNdVp8mRN6GQE-XM14goSOtDgAWtXT_MSMHY1NXy7SPBBT-adnps7hXHRw5ylk1yY-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0336d45622.mp4?token=AIwNbNseOihNF_7MznJwV1K0fYEC8gXw0egpr5evuSoKCIxp4UqODfOMEmikM-GZ33HCrVPCnvNwzn2HIeNxolppHDSqbljCD6UrpxlpLtmmHLX067cIn_oreQPkFqyZBY1z_q0ZPByJzVNL8cLhNSsSeuBLJsCy16lX0uL-vQqYhkzXtoR4WDVa5wsTfL7LfXI4gFm7TlK10edEf7Ak5cMgi4y_ZIElyeyc889A2YLp1jVwXFBhACszV5jFgqDGLu_I0WY7MLaLe4bHRdkENHSyzRia4p1Jj8kIHpxJrnufKmEdbg9kDyGDaOqZZ0eArNIM8wj1cTWxxA4CSSTpuRJkeHxX0LB5aFVPc-sAKwbc9XGRfIcWXRoTWH-QvzR50P_NcYNcdxD3oQj2Z_S-EsV3hLANEtXBa2ZbD_nYJRvDwBoN3tqaNWjr3Qf3CxFwsfCraHHEXAIfE8l5_wGM5WbV67PT98bCX35CCSE49YK49ZEpt8fezZxzJd1BkyvPcfaw-g7zIDSPWmR9c4gtuuoQK09GHu6qYAVXZvmNVG-yO64dDbBMW8tpjtXyDGPkXcsCHuPLoYPibzw9yeQBMf4ATOBQes3Jn1EkYuFXQNdVp8mRN6GQE-XM14goSOtDgAWtXT_MSMHY1NXy7SPBBT-adnps7hXHRw5ylk1yY-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
28-05-2026
آلية لانشر قبة حديديّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76748" target="_blank">📅 19:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbfO3Ug9zLx_PY7Q3tnrmuDltxWTyR4KBT4coGJ4Sf2y7io8dOZJAceO2LTilKSnyI7HSy_b-P3btx5nfIVqYHJF7lC2b1MxXNHAaqdUtYCei4qWiJQwCsrCpvBrY5UILTI1bRt3cqXJ4l1Mx0Dx_UIVCVQOw6-3ZcZ58f9U6GTHCuPC6ai40-x2FeZ_75lpe6f8vHjmK9U5OH4MQimtMqJFLvyWO1G6f3zbtnNuo9jwW_f_7dypQquEqIqpKDfObBIAsdrdB_HbZbGMjaiuDbVxw55m12NtyTc_ja5MmWXFbsj1sR-09B6UyWcEvu9Axlo2v25xAUc7HZYn6Ht0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبرا يا آل صفي الدين فأن موعدكم الجنة</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76747" target="_blank">📅 19:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🟢
الناطق باسم كتائب القسام "أبوعبيدة":
نحن في مواجهة عدو خسيس لا يقر بحرمات الاتفاقات وأساء قراءة المشهد وأخطأ التقدير.
فاتورة الحساب ستبقى مفتوحة حتى يدفعها عدونا.
قوى المقاومة جرعت العدو الويلات وأبناء لبنان سطروا الملاحم.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76746" target="_blank">📅 19:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNBL-4HRj7f70u0kCw91mJTC_DGyCH49mSE9OjXJYUNVyY-m2uxGGrd8_Vyse20BO65ICnZT8OnkHOufG3C7TSp-hiHzezlY87vteR694ozXvGEOi5VNSAKFkatxob2VctDHHkTxGyJydmO_0WE-pZKf5ruHoOTFCZJDgiZeSR0IIVvCsRIpEsNGdW6qi07WR5MKMfJUDafGsRujqhvGQgn6dU8Hfq-4dQqxxhj8tGbT2BjKgJkKRSoPS8qKfKzAPCZx5MWIMRkF6cPexIURZM2qXtV6FB5MgAeks8YbCoCg7EnUl2GkOtaUUSGBsBV-nXvK3hqXxUbepRIqwiky_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدثين أمنيين صعبين في جنوب لبنان ؛ 8 إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76744" target="_blank">📅 18:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
مصدر خاص لنايا   تم العثور على مبلغ يتجاوز ال ٣ مليون دولار في منزل عدنان الجميلي بصلاح الدين …
😆
واكيد مصدر الأموال مال سلفة ويه نسوان المنطقة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76743" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og6Hjo1hW6I9zEnompAQeg4FK6zmh_yjxRkLE1dnDcqLEr-lux1cs8h0GDNxGP6A8qe1Yhb17zdiFyK0dqx5U6qI1Ii4bJtwRmudARjSVQNkv6Kezet3ny-AYRsJ9H424IkkzrcMw5O3JBYtX_Bn97QVi42AakrP2dJ5ti6it6I5rXOkevetiOOM7gaY4P1ru0lQxzWgGv0zwPbIYFWIRSAhMpFeezUfkNBK1fY1JNqhzYu0LRupZG85zX84htFtx1vLXFrtLjvFORvPv2AP2gZ-KFMlRHfIPPJuV2TgllPkmg2i-B4i7matJGXqPy0Ia34RH0LWPOk6No-gSrXxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
كتائب الإمام علي (ع) تقرر فك الارتباط بتشكيلات الحشد الشعبي والمباشرة بإجراءات حصر السلاح بيد الدولة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76742" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:  لا تزال إيران تمتلك الكثير من الطائرات بدون طيار.  ‏ نحن نجري محادثات مع إيران.  ‏وافقت إيران على التفاوض بشأن جوانب برنامجها النووي.  ‏ آمل أن يُعاد فتح المضيق وأن ننتقل إلى حوار حول مواضيع أخرى.  يمكن إبرام اتفاق مع إيران اليوم…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76741" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدثين أمنيين صعبين في جنوب لبنان ؛ 8 إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76740" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d84411262.mp4?token=by8qkj_JOuZi2M05OPS4eJ4aldT5jIJ4Z5eQIDj9VTYsxau6wn1YRMYXbFQj8qXh6EnCkRUKuPYbRYMz88mM8kV8gd8By06ILZ_0BeaItHMjFYN2zpec1X57-0_Vwiqv00Xgaj3v4Tonou6D9dwncJYdNEHte9gsQgUEKDAdslHKPAA0jPPZ3FQXg4URpUxF5fMoqLrIcP6y7EEDJv0F_iLnQ24F35e0766hY9neB80-2XGwD2ntAsl31INTMb3vWjIPj3WCBC-A9A4GOifYE7d0Ngq1xoRIp0UNXgrXkUlMhUJB2wBC2y_U6vz5D7EJGnFb0W-gJx3r9bjDkxfZZTeudtgggdoxGdtWr6Q3SW8in3z3yPNSV0-3CwvCpMJzNJKTkNuGNzv6qYPyJ0whVCiBxcwCiFyiwWSzS9z-cJFsD-3qOWmnnNziURJ8a1l74QCQQ1z6SyrI-sL4ONF6cYjjF6cSGgPnfp38EDHbJ6XOIUA9RxNINqwxZwskSXUAkiIXhtqAXdKJ1l49neqcK_VFzY52OKBWS-0aHxihTfaPgxFxFutWX9syp7R02ijiSeP6BUdai6GVWMMXwf74j2rVdAbHE929kxJY14zVsdsYoXbdbJcjpmV-d8JRsMQA4gGHySAw-pLtovozPXdoVsLIDMOjLbQZKNM8ncJDlXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d84411262.mp4?token=by8qkj_JOuZi2M05OPS4eJ4aldT5jIJ4Z5eQIDj9VTYsxau6wn1YRMYXbFQj8qXh6EnCkRUKuPYbRYMz88mM8kV8gd8By06ILZ_0BeaItHMjFYN2zpec1X57-0_Vwiqv00Xgaj3v4Tonou6D9dwncJYdNEHte9gsQgUEKDAdslHKPAA0jPPZ3FQXg4URpUxF5fMoqLrIcP6y7EEDJv0F_iLnQ24F35e0766hY9neB80-2XGwD2ntAsl31INTMb3vWjIPj3WCBC-A9A4GOifYE7d0Ngq1xoRIp0UNXgrXkUlMhUJB2wBC2y_U6vz5D7EJGnFb0W-gJx3r9bjDkxfZZTeudtgggdoxGdtWr6Q3SW8in3z3yPNSV0-3CwvCpMJzNJKTkNuGNzv6qYPyJ0whVCiBxcwCiFyiwWSzS9z-cJFsD-3qOWmnnNziURJ8a1l74QCQQ1z6SyrI-sL4ONF6cYjjF6cSGgPnfp38EDHbJ6XOIUA9RxNINqwxZwskSXUAkiIXhtqAXdKJ1l49neqcK_VFzY52OKBWS-0aHxihTfaPgxFxFutWX9syp7R02ijiSeP6BUdai6GVWMMXwf74j2rVdAbHE929kxJY14zVsdsYoXbdbJcjpmV-d8JRsMQA4gGHySAw-pLtovozPXdoVsLIDMOjLbQZKNM8ncJDlXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
لا تزال إيران تمتلك الكثير من الطائرات بدون طيار.
‏ نحن نجري محادثات مع إيران.
‏وافقت إيران على التفاوض بشأن جوانب برنامجها النووي.
‏ آمل أن يُعاد فتح المضيق وأن ننتقل إلى حوار حول مواضيع أخرى.
يمكن إبرام اتفاق مع إيران اليوم أو غداً أو الأسبوع المقبل.‏
إذا أرادت إيران بيع نفطها عبر مضيق هرمز فعليها إعادة فتحه.‏
أي تخفيف للعقوبات المفروضة على إيران مشروط بشروط.
في المرحلة الثانية على إيران التخلص من اليورانيوم عالي التخصيب.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76739" target="_blank">📅 17:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
31-05-2026
آلية نميرا وناقلة جند تابعتين لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76738" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
الاعلام العبري: رسميا رئيس الموساد رومان جوبمان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76737" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
مكتب المرجع الاعلى السيد علي السيستاني يتوقع 17 حزيران الجاري أول أيام شهر محرم الحرام للعام الهجري الجديد 1448.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76736" target="_blank">📅 17:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76735" target="_blank">📅 17:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzaCzl56fd2eirmmFIxMuC2CBgv290DkGQX2JsIXMHBdAtz4Gnn76T76gssoiwB1XTyEbNeuLvueZLLy_Cw9bx41vBhrFglObPOAam_hNCl7n52g9IsMyvEmHYfJttgzEytYhe3MMAVHdGsMY91XRmPsiBeU1aaFslmtJt_HDNu84Q2n6kMVs1Fsauzc3oMn_ndeXuv5unIL_tieBLMNA51Y_raoNf509Jt6HRDIz48pXVtt3GXpDkoUns7EV0H7uO5F8NHrqQG3quAhVieCH7oH8TL-GbegSvCfDEVKJfgfeA3rq6rmfk92uc6brsS42GgDUaSqig8NVT9Mgk7pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاعلام العبري:
رسميا رئيس الموساد رومان جوبمان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76734" target="_blank">📅 17:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeItg-oytYQ89LITVPZCCNOj0uItBzeNYid2dyvWVzVD350H-LY0vOzRSZkgpEwbczjKlNGnkZWDcNYzbxY8HTRY5_p28EbOucIsOGtFifyaBn0GHCcjheLq87tMI1Uq79Q3SGiV4HfCyt-jWGYCcQx9rvQvhA_LlStaVKnoYNkiEOMgBbdrIY9bZ2iUZOTzFRWohNVOCqQX6VxVRRpY7JQPKYD-AY79wzCq2jZiYmR_I3TQzP62xFQnT99IYhYO_5FANDz7ya5ymyC-fUwlma70_020au0iG42CEHJ3763KWa4FF_X1jKAw2o6ziBshRE9npz1Z3Qeao4UE30rZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب:
بولت سيتولى منصب مدير المخابرات الوطنية بالنيابة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76733" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt9jKi2ZtCKAZZ0nA11H4I6HhEQmstf2UsbW0a1U78WJr7ZqPqYhilh7_oi3MVOp5EEaVdsAhK4N6IxypNqkJ-Y_prVFgjrFPkW6wBQfhsRV_GifqyLsb6MNnguevp2wQoegySdTMMzCtr3XUzRHcDqwDaISzkFyJJvvwBBHX1_nj2wrRNY-nayEoNi4kf_VqlM9IZX_Z2qbZ_6-cahAH9xRe6SbV6NmCYZV1LC24zFlR9N7CggCMfHtVAlczli6G0xRkaPF-4r52HhRDrlrrI7iWXdH_y4T8vLOQtJO_dPp9uTK1WQcK_PppWBAMI9Bts2Zn6om5PuHSNrkRfTN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بداية جولة المحادثات بين إسرائيل والحكومة اللبنانية في وزارة الخارجية الأمريكية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76732" target="_blank">📅 16:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇦
‏"أ ف ب"
: أوكرانيا تعلن عمليات إجلاء إجباري لآلاف الأشخاص من عدة قرى في منطقة "خاركيف"</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76731" target="_blank">📅 16:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtcB3QHXfm-BmlpgjZhzQVUKJYH1VO_3aC92TlfqQWJI6xL01RuNpShYs1coAbTlfUKqnKCwjue03toHMPmIpynxt-IzKN0SWvmFcq7B3E8vKQZ9XQmWvwksna9g0vX4hyraBvhgOd6oXmC8-zGyLiWxtl1pwXYkXtV2Kn2q3KHCeeULYzGVUXtnajPrFpu3rtC8MIkmvT3jgzm5J0SAShWHy1lNyrVB7Xe6Q1FoSldrI8Fa6TywlTImxdhak0v1HuSOvd_yvJVkVDXlKuWH4AiIIGQOklARv1q2tW6BTCGh4Veacdc6usjNnRT-eY7DEsvf-rMmLR6TMQ5PwCDUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المدير الذي ظن ان لا احد يستطيع المساس به
وهب الحسني يعيد شكل وزارة النقل العراقية ..</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76730" target="_blank">📅 16:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e25b4b3d3.mp4?token=vylNxzT9CHD6Z_doqDisUkqyoUEVAX41zGmgR92W7ShyVju1UFtnETIW0qud-QfOsuRwvIJuZCxwJvFd2uC6ilRsyKho934HyJxyVTylu0y6m2aXykIar7wvuKZgvkTfoTwWzxo0khd7ytWho-lsrKPI3lGZX4YRgqluUvGiyv0Nli0_sqDcAHc2z7bCDeJvOeb_zksuq2BVGEaZuoir5vfuDxsiPDMAo4FUlUl7Pa51yiB_Vpr-RJKG3HEg1AnTrjbZEeWgQBzl2yu29Wu7hsZEAIPc88NoXFx57IRKRww26QxECXVTDGdEebQNRAB6fBB1xWOe5Jw12mBVKp07gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e25b4b3d3.mp4?token=vylNxzT9CHD6Z_doqDisUkqyoUEVAX41zGmgR92W7ShyVju1UFtnETIW0qud-QfOsuRwvIJuZCxwJvFd2uC6ilRsyKho934HyJxyVTylu0y6m2aXykIar7wvuKZgvkTfoTwWzxo0khd7ytWho-lsrKPI3lGZX4YRgqluUvGiyv0Nli0_sqDcAHc2z7bCDeJvOeb_zksuq2BVGEaZuoir5vfuDxsiPDMAo4FUlUl7Pa51yiB_Vpr-RJKG3HEg1AnTrjbZEeWgQBzl2yu29Wu7hsZEAIPc88NoXFx57IRKRww26QxECXVTDGdEebQNRAB6fBB1xWOe5Jw12mBVKp07gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بريطاني من أصول عراقية يقتل ثلاثة من ذويه، والقضاء العراقي يصدر مذكرة إلقاء قبض بحقه.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76729" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026 مستوطنات نهاريا، كرمِئيل، صفد وكريات شمونة شمالي فلسطين المحتلة بصلياتٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76728" target="_blank">📅 15:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76727" target="_blank">📅 14:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c179fc637b.mp4?token=atbKa86QfGohXYCb7slog5sKiJLlzpNKiv69Lv1EfyHNDYFLBlmQhEB6TnQGkAXZFqqLFLO1hlLSxPLXLqtn1VWnPbuX-B5ECQIWHytQUBIwRZgoapoDkk0KPq2FgYb3MheY6Nj4X2Dxfp-ODbcxfIPFxLZ5iy4sMVUyHReRuRglylU4DMnZJh4E8ctmNhdxsxQpJBTtnft5eEQkCvlf6MCCpagOmg1tlY0uTpLjr4IsXOG7cj7RcQM_Rb2PUz8HUFMUPIknFn6fBKpqgdi1drdIhvaUfwkGj8EbJ5yqqAzs2UooqMyjwMFHvRhsRQj5Oz6Lmr4CoOA3vnzEDHLifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c179fc637b.mp4?token=atbKa86QfGohXYCb7slog5sKiJLlzpNKiv69Lv1EfyHNDYFLBlmQhEB6TnQGkAXZFqqLFLO1hlLSxPLXLqtn1VWnPbuX-B5ECQIWHytQUBIwRZgoapoDkk0KPq2FgYb3MheY6Nj4X2Dxfp-ODbcxfIPFxLZ5iy4sMVUyHReRuRglylU4DMnZJh4E8ctmNhdxsxQpJBTtnft5eEQkCvlf6MCCpagOmg1tlY0uTpLjr4IsXOG7cj7RcQM_Rb2PUz8HUFMUPIknFn6fBKpqgdi1drdIhvaUfwkGj8EbJ5yqqAzs2UooqMyjwMFHvRhsRQj5Oz6Lmr4CoOA3vnzEDHLifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
السؤال هو: من اين جاء الحلبوسي بـ500 الف دولار ليقدمها كهدية وما هي ثروته الكاملة اذن وما هو منصبه في الدولة ليكون هذه الثروة الطائلة وحتى لو كان لديه منصب هل راتبه يكفي لمنح فقط هدية بنصف مليون دولار وهل مهنة التجارة في الدهن الحر تجارة رابحة الى هذه الدرجة؟!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76726" target="_blank">📅 14:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الإسرائيلي:
إصابة جنديين بجروح إثر استهداف قوة إسرائيلية بمسيرة في جنوب لبنان من قبل حزب الله صباح اليوم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76725" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76724" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
وزارة الداخلية البحرينية:
نظرا لاستمرار توتر الأوضاع الأمنية الراهنة منع سفر المواطنين إلى ايران والعراق.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76723" target="_blank">📅 13:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
مشاهد من عمليات اطفاء النيران المشتعلة في سفينة MSC الأمريكية في المياه الاقليمية العراقية بعد تعرضها لاستهداف صاروخي من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76721" target="_blank">📅 12:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76720" target="_blank">📅 12:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني: عبرت 24 سفينة مضيق هرمز خلال الـ 24 ساعة الماضية بعد الحصول على تصريح بالتنسيق مع الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76719" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏴‍☠️
بعد فشله الذريع ؛ نتنياهو:
لقد تصدعت أركان نظام الإرهاب في إيران. ولن يعود إلى ما كان عليه، وسيسقط في نهاية المطاف
أي متآمر شرير ضد إسرائيل يعلم أن مؤامراته ستفشل. والثمن الذي سيدفعه سيكون باهظًا للغاية. والثمن الذي دفعته إيران بالفعل باهظ جدا
لا يوجد جهاز استخباراتي أو جهاز إحباط أفضل من الموساد. الموساد منارة للقوة البشرية، والتقدم التكنولوجي، والجرأة العملياتية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76718" target="_blank">📅 11:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a980d64c8.mp4?token=XdXJZ1Z5B2KhTkVVXDKYE6wvNy-AU_m5WqFhS91KYz3HAmRQ69XqJ0hr5tBBZHuY66I8SRY1SRopZYmMKUbqcCKxpL3_v7wSs-2ZCKJZVLktGR3EaRComE5uQf1-gHNgF_GeyG_WYA-SQ-OMtnf-gXS1wofehTyJFOHFhVsyOi7jdwW-EpxK679LqnOmsN4bM0biKYcCCT886LERRg_8T7yant7iguAN3VQw3TNBUT1inI21YyWTT6o44MSXsxtwxDSRmBY-OxCNE3oW9QHQ8J6HY6UWUArQ8W2sDTbghZkpWzH9j6N4sqgConv8m-IBr5XNzOiFvPDOJzQhWizv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a980d64c8.mp4?token=XdXJZ1Z5B2KhTkVVXDKYE6wvNy-AU_m5WqFhS91KYz3HAmRQ69XqJ0hr5tBBZHuY66I8SRY1SRopZYmMKUbqcCKxpL3_v7wSs-2ZCKJZVLktGR3EaRComE5uQf1-gHNgF_GeyG_WYA-SQ-OMtnf-gXS1wofehTyJFOHFhVsyOi7jdwW-EpxK679LqnOmsN4bM0biKYcCCT886LERRg_8T7yant7iguAN3VQw3TNBUT1inI21YyWTT6o44MSXsxtwxDSRmBY-OxCNE3oW9QHQ8J6HY6UWUArQ8W2sDTbghZkpWzH9j6N4sqgConv8m-IBr5XNzOiFvPDOJzQhWizv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني ينشر مشاهد من مضيق هرمز الخاضع لسيطرة الحرس الثوري الإيراني وانتظار طوابير السفن للحصول على إذن العبور.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76717" target="_blank">📅 11:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
🔥
⚔️
Another Vision , game of thrones . Hezbollah against IDF ..</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76715" target="_blank">📅 10:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇱🇧
هزة أرضية تضرب قضاء بعلبك في لبنان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76714" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
انفجار يهز جانب الرصافة من العاصمة العراقية بغداد، وأنباء اولية تتحدث عن مهاجمة منزل بواسطة قنبلة يدوية في الراشدية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76713" target="_blank">📅 10:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
تقوم إيفانكا ابنة ترامب وجاريد كوشنر بتطوير جزيرة خاصة ضخمة خارج الشبكة في البحر الأبيض المتوسط.
إيبتسن جديدة
⁉️
😱</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76712" target="_blank">📅 09:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: "الجبهة اللبنانية تُداس فوق رؤوسنا. الإيرانيون يُقيدون أيدي الأمريكيين، الذين بدورهم يُقيدون أيدينا".</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76711" target="_blank">📅 09:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📰
فايننشال تايمز:
تدرس الولايات المتحدة نشر أصول قادرة على استخدام الأسلحة النووية في دول إضافية تابعة لحلف شمال الأطلسي في أوروبا.
على الرغم من أنه لا يُتوقع التوصل إلى اتفاق قريبًا، إلا أن بولندا وبعض دول البلطيق مهتمة، حسبما ذكرت التقارير، باستضافة قواعد للطائرات ذات القدرة المزدوجة القادرة على حمل الأسلحة النووية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76710" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: "الجبهة اللبنانية تُداس فوق رؤوسنا. الإيرانيون يُقيدون أيدي الأمريكيين، الذين بدورهم يُقيدون أيدينا".</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76709" target="_blank">📅 08:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa6457510.mp4?token=bwvU56vcQKNwyf1FGk7Yfsao4UpIZuXsktnMpqC3zLaOGNeA7su-3gUfCWXfg0W3Y_hzIeQYREOryLBt3mC6SaS8wuhRl_cCRDQGy6PZPmO-Tw17pJXus7w-XzjO4rWb976HKKPYf5cRDDevV2phR2QNZNjJ12JUluNa2S13hVpeWzoLyTXSSHlhHsGlbUlY63dRQ54w_-g34Uk3BI5YrNWv7cr4fYC_1SIsyhD3CeFMcJrusBchl8Q4ACRtYa7V1Omc-5W1Icp7XiT1ICVDFNlh6AY2xaX0ZzFd5WXXv2cDTZNpO-a0WKV-dIBy4eEv8k7TNoyOnoCQt_lRsjZDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa6457510.mp4?token=bwvU56vcQKNwyf1FGk7Yfsao4UpIZuXsktnMpqC3zLaOGNeA7su-3gUfCWXfg0W3Y_hzIeQYREOryLBt3mC6SaS8wuhRl_cCRDQGy6PZPmO-Tw17pJXus7w-XzjO4rWb976HKKPYf5cRDDevV2phR2QNZNjJ12JUluNa2S13hVpeWzoLyTXSSHlhHsGlbUlY63dRQ54w_-g34Uk3BI5YrNWv7cr4fYC_1SIsyhD3CeFMcJrusBchl8Q4ACRtYa7V1Omc-5W1Icp7XiT1ICVDFNlh6AY2xaX0ZzFd5WXXv2cDTZNpO-a0WKV-dIBy4eEv8k7TNoyOnoCQt_lRsjZDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇷🇺
انفجارات واندلاع حريق كبير في مصنع أوكروبورونبروم للدفاع في كييف بعد قصف روسي كثيف.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76708" target="_blank">📅 08:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDrCsbYazcM90vB3TlbUsAL24LOizw7s4wVOA-WJD4PMvR-tEJMYDYrWg52F6X1pRVuIatIvr1YlOgLJ-vE2WBuMyD3v0wpxE938am-gHceWXl1KUiAgqW5JJHQrlDcyRN7unc3MLSD8HgcAHJkd11T9F8ti7Z25nbojEqL8BH-SwLVCIlSpXhAwtHzG4w-y85_klZcQurIZsF391GDGWeEd53InaHgMpdwWijjR7l3gTbf0hPBs7EOSQ9lJ57o1BDkIpA6N2CN2zjokbOawjX_zJbYmGH7SUytAZG9jJxobJmBkmnjS-Xs7i4anr9ewEEbO5UXu5FvFKB1Fw0a7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
إذا استسلمت إيران، واعترفت بأن بحريتها قد ذهبت وتستقر في قاع البحر، وأن قواتها الجوية لم تعد معنا، وإذا خرج جيشها بأكمله من طهران، وألقى أسلحته ورفع يديه عاليًا، وصرخ كل منهم "أستسلم، أستسلم" بينما يلوح بشدة بالعلم الأبيض التمثيلي، وإذا وقع قادتها المتبقون جميعًا "وثائق الاستسلام" الضرورية، واعترفوا بهزيمتهم أمام القوة العظيمة والقوة للولايات المتحدة الرائعة، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة شينجزي ستريت جورنال (WSJ!)، وشبكة CNN الفاسدة وغير ذات أهمية الآن، وجميع أعضاء وسائل الإعلام الإخبارية المزيفة الأخرى، ستقوم بتغطية عناوين الأخبار بأن إيران حققت انتصارًا رائعًا وذكيًا على الولايات المتحدة الأمريكية، ولم يكن الأمر قريبًا حتى. لقد ضل الديمقراطيون ووسائل الإعلام طريقهم تمامًا. لقد أصبحوا جنونًا تمامًا!!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/76707" target="_blank">📅 05:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1AwSPgLL48CVbIjaCQBxBDQWsuoOXEEvpwKfvCbOqscSb3AzaAnDrLe0cfy2OSL1u_q-iJsnmTBvzejF_-N_jnXUm9LwTtdJLVMMCGjAgx5Kdax6GUTldb0xtSQ9W79r73Zx_xoPs7EZ6D0ZKGkLQ6glS_Qkn6fxfp7IGOoXnjfRyobih6D9Y54g6mhxM2bdZ8JD9jAlIW2cC0ryI_1R-S7SSqVfwK6vvrE7jCFh5r1ByIxv15cyXgIYpt__90s3iDKUDGl1yIJLJ5vxYpe4mWMff52Lj1EY1kN5QfRlFzzEayyI-kZegZUM1bXrZq03-_wCWJ-bpEyrMVVbqLyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابات مباشرة لصواريخ حزب الله في مستوطنة شلومي شمالي فلسطين المحتلة ؛جرحى بحالات حرجة في صفوف الصهاينة وإندلاع حريق كبير بالمكان.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76706" target="_blank">📅 03:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✌
👌
👍
ضربة جوية دقيقة للدفاع الروسي
عمود ضخم من الدخان يتصاعد فوق كييف بعد إصدار السلطات المحلية إنذاراً بهجوم جوي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76705" target="_blank">📅 02:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770d1e923f.mp4?token=e5F-j07o1SpQUsrcSmKFvKWjvmZbA00xbWhTa9gJkWdvJ8uEGi8yFU60yNy6IwRKmFrf2Bbwy48_niWSNGWmK7TybJEONgGaDVHAyuE5xWjO48vCxdCm9KoQKrM2OGCxGWkRYYuAjesbsat0wgFj66yuX_UhDc4nCL5wj_MS9EyCzsJJz7mNk2SZjs3ppCAWAPFIGJ8Pi_HlyCRBzXiAfuuwBD1b2AjYGdtglT9BnkHzr5Q0vS1qw7cLBdy-PozG5oD-fGOg3EHeJiPW8zAC0w327qPxRfAcWWV7of-sJi_8FMUxamAQ1fNMUmO4pqJvZkZVbQ3wE7nwHlrGj-VLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770d1e923f.mp4?token=e5F-j07o1SpQUsrcSmKFvKWjvmZbA00xbWhTa9gJkWdvJ8uEGi8yFU60yNy6IwRKmFrf2Bbwy48_niWSNGWmK7TybJEONgGaDVHAyuE5xWjO48vCxdCm9KoQKrM2OGCxGWkRYYuAjesbsat0wgFj66yuX_UhDc4nCL5wj_MS9EyCzsJJz7mNk2SZjs3ppCAWAPFIGJ8Pi_HlyCRBzXiAfuuwBD1b2AjYGdtglT9BnkHzr5Q0vS1qw7cLBdy-PozG5oD-fGOg3EHeJiPW8zAC0w327qPxRfAcWWV7of-sJi_8FMUxamAQ1fNMUmO4pqJvZkZVbQ3wE7nwHlrGj-VLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقة صاروخية من لبنان نحو عمق الجليل المحتل وصولاً إلى محيط بحيرة طبريا.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/76704" target="_blank">📅 02:06 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
