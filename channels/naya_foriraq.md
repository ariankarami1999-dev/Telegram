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
<img src="https://cdn4.telesco.pe/file/Z_iIBA8Tzs3ynxtEJINwZHW3sR23xg6IbiNQDaQMzXb4QxYXHmm8wJVkEzvpC-pP4V4lu2Yb6BdAE3dK9oj-o4Ev9VqIIeT2Rar_nRGwNrZcY3wy_53c6ZcHOvi7OogE2mOboFTrcq6d0lm8DZcjPpFTchce3l0PFkbO-lUVH37zMTlKZwYoGXYifDipzX4cRnB8fRqc6_DIxakMcsMbFCyZd4DcqNtKyKK9RxoqtPSQJ6UJnS9AnS_CAmS0xI2rZmTon3alfwUnjNKT2wczm8I9iodMoSoTXRBm819UrVu6m07qjq6TCDQO5jVfw_QXX8Ug-jwSPJPv99PNRNongQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
ترامب: سنرى ما إذا كان سيتم تدمير إيران.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/90896" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
ترامب: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/naya_foriraq/90895" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
ترامب
: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/90894" target="_blank">📅 19:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇷🇺
روسيا تستدعي المبعوث البريطاني على خلفية تزايد شحنات الأسلحة إلى أوكرانيا</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/90893" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/90892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/90892" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/90891" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
إفشال محاولات إجرامية في العاصمة صنعاء قام بها العدو السعودي مصبوغةً بالصبغة الداعشية ولن تمر دون رد.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/90890" target="_blank">📅 19:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
احتجاجات وقطع احد الطرق امام مولدة اهلية بسبب امتناع صاحبها من التشغيل في محافظة كركوك.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/90889" target="_blank">📅 18:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يستمر في استهدافه لمواقع المدنيين في تعز.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90888" target="_blank">📅 18:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇱
اعلام العبري:
قضية تجسس خطيرة تتعلق بالتجسس لصالح إيران من داخل الجيش الإسرائيلي قيد التحقيق حاليًا.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90887" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇷🇺
‏
الوكالة الدولية للطاقة الذرية:
برج التبريد التابع لوحدة مفاعل في محطة كورسك للطاقة النووية في روسيا تعرض لهجوم بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90886" target="_blank">📅 18:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
🔻
رئيس وزراء سلفوكيا:
أشعر بقلق بالغ من أن كل ما يتم السعي إليه الآن هو ذريعة لنشوب صراع كبير بين الناتو وروسيا.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/90885" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
رغم انبطاح الدولة اللبنانية..
جيش العدو: إقامة الجيش اللبناني لحواجز بالمنطقة الأمنية بالجنوب "يخالف التفاهمات".</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90884" target="_blank">📅 17:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/90883" target="_blank">📅 17:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/90882" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90881" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f17d0c4a.mp4?token=PDSQX3mB_evyG-asBu3lEqVqVuJGgxhTC-hxjID1x1go0ovLsOG9BG895Svowm3AQB1OMt4FWZ6eE1TCZMwkEuxOgf82vmXEBMSqf7peCA35NeIwWreZzmxOGCP7VmYErgUzRmoo-jWcmAk-hLF62-uQGLwqn26EeyAg0GRjo21jtjbrjoMMEV-h8BjzAnjrpTvD1sPWw5q55F4hJ0Kj0Kodios9WPLyeACOojfWec2hz-2Ep6nQ-iUMCYDZFLIpe3RaUrpdGlQgm240OcXv7IlzqZLU6ljDPeLjtwQEs5VnHRvu4JFbzOHSlOPnOrGbGNaYDrSDp2g5qYKv4co1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f17d0c4a.mp4?token=PDSQX3mB_evyG-asBu3lEqVqVuJGgxhTC-hxjID1x1go0ovLsOG9BG895Svowm3AQB1OMt4FWZ6eE1TCZMwkEuxOgf82vmXEBMSqf7peCA35NeIwWreZzmxOGCP7VmYErgUzRmoo-jWcmAk-hLF62-uQGLwqn26EeyAg0GRjo21jtjbrjoMMEV-h8BjzAnjrpTvD1sPWw5q55F4hJ0Kj0Kodios9WPLyeACOojfWec2hz-2Ep6nQ-iUMCYDZFLIpe3RaUrpdGlQgm240OcXv7IlzqZLU6ljDPeLjtwQEs5VnHRvu4JFbzOHSlOPnOrGbGNaYDrSDp2g5qYKv4co1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ونقولها من عراق زيد ابن علي بوضوح
نحن جمهور فصائل المقاومة العراقية بندقية بيد السيد قائد المسيرة في اليمن سيدنا ابو جبريل …</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90880" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظام ال سعود يستخدم منابر المقدسات الاسلامية في مكة المكرمة والمدينة المنورة لمهاجمة انصار الله والتحريض عليهم دينيا وبث الاكاذيب لتعويض خسائره الميدانية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90879" target="_blank">📅 16:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90878" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbODQkIAUCL0ruBKjw7JMrKtquJYvA3BuuFpfVm0YVCAZW5KqElazamOXNQdZKi3CCI4EsgTiuO8h9CR0ZQAlF7pIEu0mpkTh51XZyiL5U0x16L91N48HeyWYK2Y1h4hCPkOOIJBok0v59epeZ-pWxYJQD83KTYeWMWvxW4qWqVchhN_22hhP9NyO9d7ZMVlVOSTg9eh4N5FICNWeIXTVYwIXfi-Jfx5paoCIg_OxPn1-ex2gYGTtsKrLxPuE0ssWSo92bKOKN1_O7TCxRqMCcU9Az-lCSEpUHJn7HcDjlEiw7Z6RWptsTg2unNMnERPOInuL1rH3fmZMmJGPh_EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/90877" target="_blank">📅 16:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me8mHQMZc8RmvHLMwcpoB-TZO2tQMkYo8GS94HXgJOhgNySd_SqDYILrh0dV_tcF34TIejeQb98M7aEaROMZtoWCEj4HISHG5LY3lFeASM7pd1CHwij3Z83lk70zzzsT3aGPCzaBy7_tBUxkaVhxNOXFjf0elJVJvXjuUCmtMKCYAxIhJ08jmR2oVeb2Dw_nw9jFG8eMCA2qixbJdUg59tiGbC3hDn7rvxIJLsJsK2lJ5QoiVYCjupTNa-c2ij1SZPSddi4kZQBZhL0P_jz7W5fyzE1lw26OEnlWzTr9RRx73apZZjRugbSsFpaV7m-3p1UcSQ5yyKaaK31Pl8bhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEw3RKMjecDdLmcsGYDxFVkGk44BvNgwlXmpYj2-U8sK-ia6MUVe7zQ2iNehecfIunTyUWT7MFD99SzBqzJdq64QWQ976L-HHa31DdtzYhN-PGU9Eoakyd7GuDFASXRZ-bmY5UN6siY-2_J0moGIvQ8dNIBqyMb1I1qlY6Sgbjm8yKTwA8b6LufWgIyuTJ1L6vpNFXyHqZHUdtxb4h8p_kI7F7nPqMOFXaX4T44uYlv49lWSRUyPbPpy4W01tPYEDgxHB7zg1OqtmZ6RV_wYuXxAwgREPEpTqvnmbstfhUN2nGyci5PANP4cX4perKiLRMURbMLzgtkidyANrPusiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULmyM8P-2QYxvjANxzg0Se2nacnP0H2qGj_kqSk-mvM6dBqEboCFFhOiF4NxMWs1OIXvYh1AoaqRRQcTE5oAXQj7LUoHkHRrxatJlsgsS0I1K5jcCdvsLrqZVnMQ0QS4VEKe197avVmBWqXKezySujynQ7tF0ItQDTLLt7get2-9mCFcn5BkRJRz2L4dX7T9hxpIlrCjL7zsWiXyPKKwBaeXj_J6sste8ObBUZvc3x68ouSR7i97--QkOHWSmTSpW_YKbo90q2cmYgTuQxlB9KSzaxtcALd1bTAJchB0uPVdqdo0Wy_MwZqg7vavuhb340Ub2rIArOTHEip0AJUzXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇷🇺
من محافظة واسط العراقية
منتسبي الشركات الروسية يشاركون بانتخابات مجلس الدوما الروسي ؛ الانتخابات تجري تحت إشراف السفارة الروسية في بغداد ولأول مرة يشارك العراق عبر المفوضية العليا للانتخابات بصفة مشرف دولي على الانتخابات داخل روسيا ..</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/90874" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏الاتحاد الاوروبي: هجمات انصار الله على السعودية غير مقبولة وتعرقل الاقتصاد العالمي</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90873" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
الـ100 دولار امريكي في الاسواق العراقية الان تسجل 159،250 الف دينار.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90872" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الرئيس الفرنسي:
نعمل لإنشاء خط أنابيب لنقل الغاز والنفط من العراق إلى السوق الأوروبي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/90871" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دير الزور السورية بانفجار هز بلدة عياش</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90870" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebNvvxhIxohgLt6NBDqMjD3SJCiv6CgA0uLBacVUloI9YzWb4sYgG1_cVSW4qnSBa4YWrdlyhO5W6hy2gjvHv3w7wu6d-OYfj6T8htMxvOpcnRgCku0uo8D5KWVsD3SaQWYnoJ3dXs42jjfixR9FPH16aRWEI4tEWTrNs9BaeLaqc-q3z1SyX0WN6k4KpJLBgKgc4bnF4Jh48C1n0YUpwyaaGYBH_vHaAMrApC8sZVHTD93t4ZcMqYmOtEs70baPhlM89eO2XGLPCppNEjwy8fZxT10TwDEPBGZQS2gAXjnoNvZ6RR5VYxtYTE_SJGONlXiC8sH-gmiYckaxeWh_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
‏السفير التركي في سوريا الجولاني يفتتح "مدرسة رجب طيب أردوغان التركية الدولية" في العاصمة السورية دمشق.
ورجعت أصالة عالشام
😂</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90869" target="_blank">📅 15:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
🇷🇺
🔵
ماكرون: استُهدفت فرنسا بهجمات روسية هجينة في الأسابيع القليلة الماضية</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/90868" target="_blank">📅 15:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي.. حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90867" target="_blank">📅 15:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شركة أرامكو السعودية تبلغ مصافي النفط الأوروبية بأنها لن تتلقى أي شحنات من النفط الخام الشهر المقبل بعد تعرض خط أنابيب الشرق والغرب السعودي لأضرار</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90866" target="_blank">📅 14:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxQSPuM3cH70RY98qJLT4HxDJwDo0nZyTLbg95kbyJePlMIAnvdFp0vys9jryb8ndGciXe_Cw1b04mq4K7b15GFi4E5Xs7XS_JKi9LZ3lwrQaIU40ut6obbww83BRfFXtROFqlMM6xZWifQUL3sGrVxULQmH7dqZtkdsTXMXWydKffLl-RwICj_gaNhsxR_GGh69ITE0gOWznyAlMUcODr-GJjBvSDpnf-jv7unHULSnRjOTucNRaaAJATYe7w0o_TZ8_IRs-z5J_42FnI8TqMr04w9njn6j_u6Bf9-uieg0CDWCmFgb2FYcInU8VmiFG1kp-XpnsbmNKFvaCILAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان فدا
شبه لهم يا حسين
ما طحت انت من ميمونك</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90865" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
🇷🇺
وزارة الخارجية الروسية: روسيا تطالب اليابان بسحب صواريخ "تايفون" الأميركية من أراضيها</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90864" target="_blank">📅 14:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
إنفجار داخل مسجد في باكستان؛ 17 قتيلا وعشرات المصابين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90863" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
سي إن إن:
‏الجيش الأمريكي ينقل طائرات بدون طيار إلى أمريكا الجنوبية استعدادًا لعمليات مكافحة التمرد المتوقعة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90862" target="_blank">📅 12:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
هجوم بالرمانات اليدوية على منزل في العاصمة العراقية بغداد منطقة السيدية ..</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90861" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي..
حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90860" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
وزير الدفاع الإيطالي:
إصابة طائرة تابعة للجيش الإيطالي خلال هجمات على قاعدة جوية في مدينة الطائف السعودية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90859" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROYwEqtnQC_tMBdRPRqBbslkZ8T8dbf2BnYvEOFN5jnV0VdGYv2iSiVmvaxwm9nldCCaa2cVlzUoYTy5-Xvo7GPeaHm_Ib_0QXaOCXcHyCBT9enwrihYsLhb0sf5tMpb42Qem70gLmgPVu3KELgmGotFSq9NWDucji1xh_jbJIBhBaI2rW14swhULoD4AsUCc0dS4LvSDz5ImQQf2VQiJfk_flG5YCqRTZU2v6GzuS21UGsy6rwBsIxnaOYiaiBXfpZALYjPD86TnvwifNDCT1o7t8s4rC-Mx-3-x88j46jcQTMX7nA24t1IoNgc-yTIERUfW6byA0qtA0P9sbNauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستهداف ناقلة نفط بمقذوف حربي في مضيق هرمز، أدى إلى اندلاع حريق كبير فيها.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90858" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvJ7lEUy5aPTx4GcFEW4LSssWKV9S-vKbB5oDXdsgVMkCScNKBbLmgldWqmiJb8nhe0Rqt7-I5zRlcZXl2RtO46Y2rfNF4rNOKXrvJ7J8E5Xwcig97nFEc2S4OFGBDk9-Jla571mGbtiFG4m6SXrVAfCRlbezfmlwx7TZAdPiaPtIQrbpdYIgy6_AiIZjJNEeCCzLl_vToPfeymi6B4E6xsPfESzNaXpLjodnu9i40J9FMS2_fM5vyIHzdnKUHVCiD1Ol1JshFJ_d-awPVNPvxOwuJvLNjjCeJGQFp2-5fN5sgoNkk26h5jFTMKFunW0n6ilBKklkX5cAAc_SCJZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90857" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90856" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇱
إعلام العدو:
الشاباك والشرطة أوقفا مواطنًا عربيًا إسرائيليًا من سكان مجد الكروم للاشتباه بارتكابه مخالفات أمنية تتعلق بالتواصل مع عميل أجنبي من لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90855" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد تظهر إقتحام وزير الأمن القومي الصهيوني "بن غفير" لحائط البراق غربي المسجد الأقصى الليلة الماضية، حيث أدى طقوساً تلمودية برفقة عشرات المستوطنين الصهاينة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90854" target="_blank">📅 10:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حضور الرئيس الإيراني مسعود بزشكيان في مناورات "فدائيون إيران" العسكرية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90853" target="_blank">📅 10:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تقيم الجمهورية الإسلامية الإيرانية مناورات "فدائيين إيران" وبحضور 313 ألف عنصر في العاصمة طهران وبشعار "لبیک یا خامنئي".</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90850" target="_blank">📅 09:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90849" target="_blank">📅 08:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تريد عقد صفقة؛ لكنها ليست مستعدة، في رأيي. إما أن نعقد صفقة جيدة، أو لن نعقد صفقة على الإطلاق."</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90848" target="_blank">📅 02:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نايا - NAYA
pinned «
إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90847" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90846" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة جدة السعودية</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90845" target="_blank">📅 01:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwcJ8ddnCn4fTkBEOR6Q_E_zY2hVqWBEFGxpGnUvte1sLAo7yYqlES8D1rdTKbQl1iM6OoB4Af7bzJfH8ftJlKbUgZjtsfaP30UiS4Ef1ZwPH5JeX6c5Kea3HuzAaL5T6071xwvqXvEJGct72RHL6_WyHO0LeLkEvTDGTfPMjIQzYCeOp1QdLxtKqsXFiJCaYXJnoOwd62SkUfaG3TIO2hV-FBE3WdLq_ngZ4OBVpm9D2boRoPTlJyixX6p1sb-oRn4OO93lkVcGiaXTiDyHt7ELWiHBIZ5LU4atabgshpG9L2BU4whWVWrPs-Jiyw4plAb6Wb38zyTHbz3ID7aLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
الانسحاب المذل للقوات الأمريكية من محافظات اقليم كوردستان العراق مروراً بمدينة البغدادي بأتجاه سريع الأنبار الأردن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90844" target="_blank">📅 01:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بين ياسر المالكي وقاسم عطا المكصوصي من سيختار تيار الحكمة الوطني وزيرا للداخلية العراقية ؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90843" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزارة الدفاع الأمريكية : خلال فترة ترامب، تدرس خططًا لسحب الطائرات والسفن والأسلحة وأكثر من 25 ألف جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90842" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4ADKrh1gy715XKacikjVf0vPNoV_JBhAin09fEb4ohCciwD_B_jc1tjQlrIkK6v6n7BE9YFIUTiEP0dfbVDTtBdU5TAmZO9GfnQr_idESQZBzdMjPSahpFVDVHzPv7Jx0myDoKkcfwQ2oZWxeoJ2_p4U2H3SSIkrmxcomK2d774p4uNqMEwAgHqmzBMZ2CuwAJWdKKy4y_2l2MwnOX9zBmt9LjQ6J7gfSlNUncdbZEvsfJ9saRemHA58hvvNm6MQ6rFQiU9QSlca0usYXqzc7-cddOoqyaWyAwy4Bhq3Dfl8t1MHILjQ-__mzOi7UrSwq2YYVbeBRckCqdmE-WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية لاندسات 8-9 الملتقطة اليوم أضرارًا إضافية محتملة في محطة أبها لتخزين النفط الخام جنوب غرب المملكة العربية السعودية، وذلك في أعقاب هجمات الحوثيين هذا الأسبوع. ويبدو أن ما تبقى من خزانات تخزين النفط في المحطة قد تعرض للهجوم والتدمير.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90841" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kByKmKegOk66liXDrcbXoMxKsIJjNmKtPzA6IdJmQ49kMVgEQxUz2Ripyf9-A0xNUBx-oDATYyavQfQOfev5ADsDmZE17OI-RlqgeL5ZceRS4rImmmEypOyqB8zpyac3DXano5qavXT0L_jUh9gaIhsE67_0AUHmk_kNWo8X37mnPHh_0_8MnYRXgz7S1vjCTaLStNLETGBL1aS0_wvBdy8GCr8ponjrW2une84e04VwbzPX0RsuvLHtICsgW1Y7H5N9MrcGcJPMXeikCPycD7WI4_aM0KHGg2uTGIMLt3PvA5y5mrExj2IZl3qbD8v5WnSP4FTaSgEOEDw5ldszEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90840" target="_blank">📅 23:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvnCW7WWFMX2D66MCLSNXIp-KoD5gFEDA9J2X_slYAp4ZCKT7p8Xo8Fats6lO7IAlCHJz8yPD-3aMHOgo8Lm8rkNGJ1ksvLygz0CSAAVYR2SgFJJzFvTxAU2eZSUO_NRGFwIB_ezBW_al_73Bh3EpvLFLECnX6FlmdYKEl_OIk-Pwynq6w28Nn8n-o2wkI2k5gb-R4wnBhb1ehe4LMBXhS9C7ad7bxgjnmodubHHpoDcfbQOoRmHcDBflUqVqNbajtzwrCt6Y41hsnVOMOcef2X4uuJn0LLfWwWWkOLnAU5oXAHIl_Gv3nbVhb3g5UaQG0PN3iBJbSqRF9qqPUQcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: ‏انتهى النظام الأحادي القطب الذي ينتزع فيه طرف واحد التنازلات بالقوة والإكراه. وقد رفضت الصين وروسيا، باستخدام حق النقض (الفيتو)، الاستغلال السياسي لمجلس الأمن، وأكدتا سيادة القانون. يجب علينا الدفاع عن التعددية؛ فالأحادية لا تخدم مصالح أحد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90839" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90838" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90837" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu6MtomqVP3RaLE7qKzugu1-UpA2LvxU87CT9InPNF7YwscGPCyR0EJS-VdCtC56B9GMD_6fQkaSGk2OlZv_wmF49jYZ9ocU3ek2BgsEtWhHiTmQOYPp1GRAsMb-zCOzLuaKEm8U8HNu57jivuEyWocW5OfBOIUiaJNfkhTsY0QK5MUjhUgjsgAPWKyL6Zc8zSVSbmA42ZhU-FxNebSyUCmVRb24vSmMy7aL4lvS2bIs5NnVSqx5MUJRi6BErvtj29xmEUYD2tS6BtaaEfTrf7on6l1hlXR2cfic-ih8621xsfAac2gRIoU32kByiBh_3pvKf3vafIRVO18dXXTlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وردت أنباء أولية الآن عن تحطم طائرة من طراز إف-16 في مقاطعة بلير بولاية ميشيغان.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90836" target="_blank">📅 22:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
🇮🇷
الخارجية الاميركية:
واشنطن تمنح تأشيرات دخول لإيران لحضور اجتماعات الأمم المتحدة .</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90835" target="_blank">📅 22:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 37 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظات تعز وحجة وخلفت شهداء وجرحى من المدنيين.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90834" target="_blank">📅 22:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
🇨🇳
حادث سير عنيف في محافظة ذي قار اصابة اكثر من ٨ افراد بينهم افراد من الجنسية الصينية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90833" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يغير على المدنيين في محافظة تعز.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90832" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇸🇦
المعارضة السعودية تنشر:
سَنْطِيح مَلْكُكُمْ وَكُلُّ حصونِكُمْ.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90831" target="_blank">📅 21:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امريكا تفرض عقوبات على منصة بتبانك للعملات الرقمية بتهمة العمل مع ايران
وعقوبات إضافية على كوبا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90830" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الأميركية: صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90829" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90828">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
إصابة سفينة الشحن التركية «ماريام إم» بمسيّرة روسية في قناة دلتا الدانوب داخل الأراضي الأوكرانية قرب الحدود الرومانية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90828" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90827">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QII8cjcyWw-0S4SueRWL-iauJLqQQin_1m85Ga38QVBiXEW58eGFrhmEplex_WeWa5bDagpjhbJPn93jfyDwaT1e8Y2BXKXETOhJ2qscWu7K0VlMopAEG3JFvj6pZvqJIGvXfJWokNogWRWuzurAChAkwl0thIhAr1r3OmH_AAOR5NSWNlLxhsYpajbpXCSivTgpusWt5Vb4XcmcbtzBgxxgIHvTGd9WhIYXBIfSlpeD8FJj1dJEJAI1cm1WXvwHVWBR4YpbYNIQoieGATSwi2F52iZQZKxGb-QMNUSe3eKg76Hkyn4vNJGA9zNDXBsTDYnDO41Re6UYxFO6AZ_MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أخبار رائعة! بفضل القيادة الجريئة لصديقي كارول ناوروكي، رئيس بولندا، يتم إحراز تقدم كبير نحو إنشاء الولايات المتحدة.
قاعدة الجيش في بولندا. إذا حدث هذا، فسيتم الإعلان عن الموقع قريبا جدا. ستكون هذه خطوة تاريخية للولايات المتحدة العظمى. /التحالف البولندي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90827" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇸🇦
‏
الخارجية الأميركية:
صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90826" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL1VHqpXEEWCRfJl8wzAROTZp40qAaTpLbqUs0HLN5k7eTVP0YAImNVjveWuP0zIEsyRxF7O433hJE7s9wU1k4cAKzqtkIhoxcxkFhEUbsVvbgry2cw8jToh4s-vpKrJFEBTXx0MBk5tXPw3z9TGIilpZb_zfU0ZydYUk4tlEH-b0j-dN791n3rXQ9-iwFWTgrzyhNQOcMvTJ8wb8kVHKGYA6yhUZT1kA40ohERYnISjTCpB7Ggq7azMqUJDDw3Cinb3TqcnlCAzBcqTXwnhw56mX8QRJqyZwdF-ZyVnKPkgt8z_SDUnZVNOdtzDYSXnirFHGJ3oUEx0IaWrUe4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
آیا ایمان لازم برای انجام این کار رو دارید؟
@Naya_Press</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90825" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
متحدث باسم الحكومة العراقية:
رئيس الوزراء سيذهب إلى الولايات المتحدة الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90824" target="_blank">📅 20:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران: لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90823" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90822" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=uAOIRUb94qqzHc1JZUCLBH2ZV4E87cEz-pyZ84GQo-wPtGwh9YNEHOhwzCo7bySZikpIWeL08Yddn7UCb2wQIXXxyvOy7-XEOhx_3LYzFexChBZHPK0WK76T3igsy2dpg4AvDLurH3L2tVeJ95ygy7lfaUwDLLov5uidc8LwFbyMfscCSWHh9eAD2Pg-BJhEEXqo2ubyOfWeVPiF36WGzLVTQG_-WwF4Ynx6QZ8qekbQR8KhOc0ig2e6ZhLP5qoNvWsyUXXfDDotUA05IAe2OUnmBaDbiU48RypOE5kQ5QRWPAn3_Y2r1xk8UulG1jTM32ZsvULyDbgd7VtuCtpDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=uAOIRUb94qqzHc1JZUCLBH2ZV4E87cEz-pyZ84GQo-wPtGwh9YNEHOhwzCo7bySZikpIWeL08Yddn7UCb2wQIXXxyvOy7-XEOhx_3LYzFexChBZHPK0WK76T3igsy2dpg4AvDLurH3L2tVeJ95ygy7lfaUwDLLov5uidc8LwFbyMfscCSWHh9eAD2Pg-BJhEEXqo2ubyOfWeVPiF36WGzLVTQG_-WwF4Ynx6QZ8qekbQR8KhOc0ig2e6ZhLP5qoNvWsyUXXfDDotUA05IAe2OUnmBaDbiU48RypOE5kQ5QRWPAn3_Y2r1xk8UulG1jTM32ZsvULyDbgd7VtuCtpDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المندوب السوري في مجلس الأمن: إسرائيل قابلت رغبتنا في السلام والدبلوماسية بالقصف والتوغلات
القدس تنتظرنا يا اخوان</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90821" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">إعلام صهيوني : إسقاط طائرة مسيرة تابعة لسلاح الجو الإسرائيلي في البحر قبالة شاطئ بالماتشيم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90820" target="_blank">📅 20:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اندلاع حريق داخل مبنى وزارة الداخلية العراقية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90819" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90818" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9f6n3Zew3v-edqOuSiWq-svKC9ZLjQNiNe1ie4dHoaAI2Voo4ibysEKfM5LjjyW_4MFnn5rF8qlSsDvSd4UipdMr-K96jfFoDBAhNUWeMMCsWLoHS8bO4VcVgCHeT2M-_5YvSZHrTgIhrWUnWlZ5mCO4i-ks35LAxaynYMq4LuTAM44YgVN1zkxdKTcKaFYqwGOn84fy3Qr6qLkO3BbsD_rzGSyoIt1wMFa2rv2FN46OcmTNmQNmOosor-hZXtiNC9BMQPbdJ0f5MWV6vvcen_Mbpw5h0LNW9hBpsmMxwYAo06uu9f41K5vfvw7ykTJgEiMpCc5MSPh2ZQDGsq_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة معتدية قرب عدن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90817" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90816" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇦
الاعلام الغربي:
تضررت ثلاث محطات ضخ على طول خط أنابيب النفط الذي يمتد من الشرق إلى الغرب في المملكة العربية السعودية، في هجوم وقع الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90815" target="_blank">📅 19:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZhPNz3xS6-M5kwQz18Vidu7WEetnbuTXw55tq3JzBnz5KiYGR4e0atmONiaOjsZyKRr9ik8f3lyGOlVLRP6swO4Pak_C7ksU6S1qxMxNessbM44grGZ4vKWdTx5bzmT7jxY5ALdeYatlq2Obiq5d-dfkWvKSkrviaFyc3PgFo_kIhe_YquiR0oZyVO02jXLvdVdonJ76sS-PKgUacrESvr1FW0P3Sv94fJguyqjcZzfxXxScGPb6jotCCbeh_LdlpSMij9Idn6CwZDmdxUfZEQUpS5oweG_e4d-tcX_xMnMQOi09lF8XGXI66Pb-17HnxpLKG-am1DB-4bZJYxHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
السفير الروسي يغادر العاصمة بغداد قريبا ..</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90814" target="_blank">📅 18:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">السيد الحوثي: لن نسكت على البهتان السعودي وادعو شعبنا للخروج يوم غد في صنعاء والمحافظات للدفاع عن شرفه الاسلامي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90813" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">السيد الحوثي: هناك تبعات شرعية وقانونية لهذا البهتان تجاه شعبنا ولذلك نحتفظ بحقنا في الرد على هذا الظلم والاساءة</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90812" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
استدعاء السفير الألماني في طهران على خلفية تصريحات مسؤولين ألمان ضد إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90811" target="_blank">📅 18:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">السيد الحوثي: الانظمة التي تلقفت البهتان السعودي يتحملون مع السعودي جنبا الى جنب كامل المسؤولية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90810" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">السيد الحوثي: كل من ادان البهتان السعودي باستهداف مكة المكرمة هو شريك في العار. انها اساءة لشعبنا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90809" target="_blank">📅 18:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">السيد الحوثي: نحن كشعب يمني أنفسنا وأرواحنا وحياتنا وأموالنا وما نملك فداءً لمكة المكرمة فداءً للمقدسات الإسلامية بكلها.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90807" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">السيد الحوثي: قارون العصر السعودي المفتري يحمل راية هذا البهتان ضد شعبنا وهو قرن الشيطان ومنبع الزلازل والفتن.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90806" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">السيد الحوثي يدعو الشعوب الاسلامية لرفض استخدام مكة المكرمة من قبل ال سعود لخدمة عدوانهم الظالم على الشعب اليمني.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90805" target="_blank">📅 17:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يسعى لحرب مباشرة تدخل فيها كل الاطراف الاقليمية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90804" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90803" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">السيد الحوثي: استهداف مكة المكرمة كذبة كبرى وقبيحة وشنيعة للغاية كررها العدو السعودي عسى ان تلقى بعض الرواج.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90802" target="_blank">📅 17:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">السيد الحوثي: المعتدي السعودي استهدف في بلدنا كل شيء ولم يرع أي حرمة على الإطلاق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90801" target="_blank">📅 17:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90800" target="_blank">📅 17:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90799" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">السيد الحوثي: شعبنا العزيز لم يقبل مصادرة حقوقه وتصدى للعدوان ولم يهاجم سوى القواعد العسكرية والثروة النفطية السعودية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90798" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يتصور ان قوته واستقراره وتحقيقه لطموحاته يكون بوضع شعبنا ضعيف ومستعبد ومقهورا تصادر حريته ويصادر استقراره ومشتت ومتفرقا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90797" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">السيد الحوثي: العدو السعودي ينفذ عدوانه على اليمن بدعم امريكي واشراف اسرائيلي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90796" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">السيد الحوثي يبارك للشعب اليمني انتصاراته</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90795" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بدأ كلمة المرگض ال سعود السيد الحوثي</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90794" target="_blank">📅 17:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الكلمة بعد دقائق عند الساعة 4:45م</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90793" target="_blank">📅 17:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90792" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
