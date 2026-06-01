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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">الخطوط الجوية العراقية: رحلاتنا إلى بيروت متوقفة حالياً بسبب الظروف الأمنية والأوضاع السائدة في المنطقة</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/naya_foriraq/76628" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
🏴‍☠️
القيادة المركزية لمقر خاتم الأنبياء تحذر سكان الأراضي المحتلة:
نتنياهو، الذي يواصل أعماله الشريرة في المنطقة، هدد بقصف الضاحية وبيروت، وأصدر تحذيراً بالإخلاء لسكانها. نظراً لانتهاكات النظام المتكررة لوقف إطلاق النار، فإننا نحذر سكان المناطق الشمالية والمستوطنات العسكرية في الأراضي المحتلة، في حال تنفيذ هذا التهديد، بضرورة مغادرة المنطقة فوراً حفاظاً على سلامتهم.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/naya_foriraq/76627" target="_blank">📅 19:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">المتحدث باسم جيش العدو : مقتل جنديين في جنوب لبنان</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/76626" target="_blank">📅 18:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 31-05-2026
نقطة تموضع جنود وآلية هامفي تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقتي
ابابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/76625" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">إذاعة جيش العدو: انفجار محلّقة مفخخة داخل موقع عسكري في رأس الناقورة بالجليل الغربي.</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/naya_foriraq/76624" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/76623" target="_blank">📅 17:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/76622" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/76621" target="_blank">📅 17:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxVLOC3DC7-GXKs8HsuPmv6vaAv9c6Q0FT3fvqtTZxkjMupNXQe-_01Wc3YyqkZW7GCnfEwY-RRL6NEwBHQvcl70RJmjNMw5ieEtCeQho8zC4CqYg2oqGktR1NoQ6MnwtlFzzdC53YT6VEGNLUdsMd8PIDTLhvjkDaJkwfyn-8xs6MpKknJwK_Q1ekQqxu6oHd_FfVIx5jaQP6vP5XqeKpIMwBkAcdoP76sA0GsyXrXDUDlc-2xCmx_kGo-Hs-XIVMZ4zcunFjvWePTJnL-i0G9EXys8vY0mRXvRl7hh8sQaKaI22aaptfS8Xca2Uf0wmKxzY2IDqQi-H19q5oosQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تبدأ التحليق بعد إعلان إيران وقف المفاوضات والتهديد بإغلاق مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/76620" target="_blank">📅 17:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴‍☠️
إنذار إخلاء من جيش الاحتلال للضاحية الجنوبية ببيروت.</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/76619" target="_blank">📅 17:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f9941fa3.mp4?token=EP1NHEpdeVnzBjsS62ONX7Z1KC_70odZHNSQpnvpoFZ68nwSjZVcxuFat8p7c0Vulvms7c7MFVk9NlX3lCT5TssNe5CHzfXxr02jWRTa9ZPWFafxqsTiKBdYgLWzUzzxUkUmBuAafi9umAbEx3m3WzVX58Von-6l4S4QiBdRZ6PnD8z1_Q4xC9Ncwnkq-Vb-9Xf_J-rSNkXkMd9dKPjVb_ypPgstYRkuWBBse1oNUNv-7YkjlgjggQqxF68RiMYJXqZURoNxdDk9oyYhL0g8kBXthef_mQczbe9I9eu5tIeP1GwYTVA2bnocJw2VQl_KSa0eEgQu-1WAZKBOcBdImzpSk8OYLbBIXKG9p_rXsm1uwRKYpSj_shiwEZrUVA9fgMvYXmy3zZyuIAW6nsOKKafvZ_qrlSFyqdU6pXRSIE1g6wqJWzdzICQgc7XYhFsr4zG2VPCzitV7fdeWQuo8lgiAK5i9xPUYUXLB7H08Jk5glEIN8m1YWdH1gcDDVKutI1HTkZCgnnHQ7bI81nMWTg9_OMYeJs9ub6MGId0hkm8ynGbZGiekLa3OvSCBKDMP6NGVGIghAQQdbT8N7ZbakvsXWTmFgV-JF1hfH1lk4qHkiAJ4M1cnR2kUsaZ2SGPcX3L-nEnl3FBkq7vtaZq0j3zX3X2ZTs6x5IEMdkSuGf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f9941fa3.mp4?token=EP1NHEpdeVnzBjsS62ONX7Z1KC_70odZHNSQpnvpoFZ68nwSjZVcxuFat8p7c0Vulvms7c7MFVk9NlX3lCT5TssNe5CHzfXxr02jWRTa9ZPWFafxqsTiKBdYgLWzUzzxUkUmBuAafi9umAbEx3m3WzVX58Von-6l4S4QiBdRZ6PnD8z1_Q4xC9Ncwnkq-Vb-9Xf_J-rSNkXkMd9dKPjVb_ypPgstYRkuWBBse1oNUNv-7YkjlgjggQqxF68RiMYJXqZURoNxdDk9oyYhL0g8kBXthef_mQczbe9I9eu5tIeP1GwYTVA2bnocJw2VQl_KSa0eEgQu-1WAZKBOcBdImzpSk8OYLbBIXKG9p_rXsm1uwRKYpSj_shiwEZrUVA9fgMvYXmy3zZyuIAW6nsOKKafvZ_qrlSFyqdU6pXRSIE1g6wqJWzdzICQgc7XYhFsr4zG2VPCzitV7fdeWQuo8lgiAK5i9xPUYUXLB7H08Jk5glEIN8m1YWdH1gcDDVKutI1HTkZCgnnHQ7bI81nMWTg9_OMYeJs9ub6MGId0hkm8ynGbZGiekLa3OvSCBKDMP6NGVGIghAQQdbT8N7ZbakvsXWTmFgV-JF1hfH1lk4qHkiAJ4M1cnR2kUsaZ2SGPcX3L-nEnl3FBkq7vtaZq0j3zX3X2ZTs6x5IEMdkSuGf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
31-05-2026
تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76618" target="_blank">📅 17:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17494497c8.mp4?token=OV3dEUytzm4mJ3cw2S9GGh7M6NKu31YYe_3LTHM9tnXFaPoOk0oKZH7m-DQ-Di93Xzp12VJiOyCINwOm2pTmmHujKEthc5J-kIYjTs9jZyiRjtpvfM_IKvjgknZEp0qMAalZR4cMm7EqBhMN1aE_JnFstyBl8aZhPtut7TvBq3fkmI8hM9zu1L1g2KAJFNQ21L1pAk6XRuivOWkGCvH5GyWOXVHBER16-BebOSsM7DVvD4rdMxbdgnmIxzSvrK8yWP9-axKZNMdJTGlcg4v5DDAz31c-wnO87qi3KNw253NqNMLlLuqVZQCflix9m4MzOhKsVvBBi5jt72LrgmX_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17494497c8.mp4?token=OV3dEUytzm4mJ3cw2S9GGh7M6NKu31YYe_3LTHM9tnXFaPoOk0oKZH7m-DQ-Di93Xzp12VJiOyCINwOm2pTmmHujKEthc5J-kIYjTs9jZyiRjtpvfM_IKvjgknZEp0qMAalZR4cMm7EqBhMN1aE_JnFstyBl8aZhPtut7TvBq3fkmI8hM9zu1L1g2KAJFNQ21L1pAk6XRuivOWkGCvH5GyWOXVHBER16-BebOSsM7DVvD4rdMxbdgnmIxzSvrK8yWP9-axKZNMdJTGlcg4v5DDAz31c-wnO87qi3KNw253NqNMLlLuqVZQCflix9m4MzOhKsVvBBi5jt72LrgmX_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/76617" target="_blank">📅 17:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يعلن عن مقتل جندي صهيوني وإصابة أخرين بعد دكهم بطائرة انقضاضية على أيدي أبناء نصرالله بجنوب لبنان.</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/76616" target="_blank">📅 17:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfebVJ9SbaUmF8U-aJVpJXafsnmrO1mQGJxPoa0LjCsPabB2UsGkwBsJHXVqjTb9pDsOq0jepumwwntlg48WmkJlO_X7xfXnvjOd5qsFqdt6ye-fFe3WJqn6g7trAVhbEvHqXo3wvvrX_LwLf-0M7np0zbYzyzxI1SjSVDtuL1EZ57gW4g_I6ef1N0DRxYJriDKpd9l-rpEMmAs95biU6cXk49_cyzBvy0TaR8d2tzovQpX3YWPmyU1NlroL45gh7CFrkRRkC0He27sdSFWJ-h7dhlTiD6Jb8ORU__rVVQ0vcVhmxPhVvbooYpvgWCpvMQQtdJkZbFJIfyjEYax9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/76615" target="_blank">📅 17:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
تم احالة السيد عبد الكريم ابو ايمن الى التقاعد وتكليف السيد يوسف بدلا عنه برئاسة هيئة المستشارين كان يعمل رئيس جامعة الشعب
أيضا تكليف السيد حسنين الشيخ بدلا عن السيد علي شمران بادارة دائرة المراسم
تكليف السيدة ازهار بادارة المكتب الخاص بدلا عن علي الاميري ، السيدة ازهار متقاعدة سابقا كانت وكيل وزارة التخطيط …</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/76614" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76613" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رشقات صاروخية ضخمة تدك مركز الجليل المحتل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/76612" target="_blank">📅 16:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.
نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك الآن على جميع الجبهات، بما فيها لبنان، فإن فريق التفاوض الإيراني يوقف "الحوارات وتبادل النصوص عبر وسيط".
أكد المسؤولون والمفاوضون الإيرانيون على ضرورة الوقف الفوري للعمليات العدوانية والوحشية لجيش الكيان الصهيوني في غزة ولبنان، وضرورة انسحاب الكيان الكامل من الأراضي المحتلة في لبنان، ولن تُجرى أي مفاوضات حتى يتم تلبية موقف إيران والمقاومة في هذا الشأن. كما أعربت جبهة المقاومة وإيران عن عزمهما على إغلاق مضيق هرمز بالكامل وتفعيل جبهات أخرى، بما فيها مضيق باب المندب، لمعاقبة الصهاينة وأنصارهم.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76611" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db7ecbe9a.mp4?token=opudIoilYCx_Ce-LcweAonM-cCpPDCgwzq3wu-ebQ4MkDFqVMSI5N3DorzM2Zfoup4BSfjQC-dS3PDJtnVRkAmYPRzoEuuuRsGmHL3SGIiTQE15dgjlc-0bjHtFWGIOP5YMnO6ECXbjuM4LgAw5DXPT-t2tabZq8-rhsYqmwTNvVEig9JNUJ35Gs69oVNuM9OpPA2v_5I2sxtyWMvuLvu20Gp-giPxFYrTrEmL3AIMlxBx3ti9iy4WXLEVG6aI0xIh_Xh1kifsbn2FxWbDxdisBcHv9k-SxlqcJiqXn-68S5wHkM6X_Ed5UC5vs9dfz8oL1hynRPpf282PlNTg2aKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db7ecbe9a.mp4?token=opudIoilYCx_Ce-LcweAonM-cCpPDCgwzq3wu-ebQ4MkDFqVMSI5N3DorzM2Zfoup4BSfjQC-dS3PDJtnVRkAmYPRzoEuuuRsGmHL3SGIiTQE15dgjlc-0bjHtFWGIOP5YMnO6ECXbjuM4LgAw5DXPT-t2tabZq8-rhsYqmwTNvVEig9JNUJ35Gs69oVNuM9OpPA2v_5I2sxtyWMvuLvu20Gp-giPxFYrTrEmL3AIMlxBx3ti9iy4WXLEVG6aI0xIh_Xh1kifsbn2FxWbDxdisBcHv9k-SxlqcJiqXn-68S5wHkM6X_Ed5UC5vs9dfz8oL1hynRPpf282PlNTg2aKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76610" target="_blank">📅 16:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4e51e32f.mp4?token=V3mUIe7nlfpSr00SJq0OImDBK6LuCkeDbWaHkipciVF_TM8dX-zoT23XJTwPNlu0JB8i668CdvDC3Dgev_zxxJdYdA8NDWwg5njXlgEowvz3L8pewAqiklUZWhNZbxBIBS-AYjMtf7rDrjfuRKP-kMZF2S02-duz24qY9aMamjHxv0mBZ_yL_T8f0MsMtAd4hdyZHHBQdABXgbmyk5CPW3rc7XbvLFhnn6VqDceMDn3q6Lkh8mfLgLVzP05wb1_S4ofKqA6qWpT1VfAVN-hXvbBip2e_PvFzEl3jfPt_ANiSPV2goGoRznA3UnIX_BZ_sdKjujGY5vVNftX27d8_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4e51e32f.mp4?token=V3mUIe7nlfpSr00SJq0OImDBK6LuCkeDbWaHkipciVF_TM8dX-zoT23XJTwPNlu0JB8i668CdvDC3Dgev_zxxJdYdA8NDWwg5njXlgEowvz3L8pewAqiklUZWhNZbxBIBS-AYjMtf7rDrjfuRKP-kMZF2S02-duz24qY9aMamjHxv0mBZ_yL_T8f0MsMtAd4hdyZHHBQdABXgbmyk5CPW3rc7XbvLFhnn6VqDceMDn3q6Lkh8mfLgLVzP05wb1_S4ofKqA6qWpT1VfAVN-hXvbBip2e_PvFzEl3jfPt_ANiSPV2goGoRznA3UnIX_BZ_sdKjujGY5vVNftX27d8_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ المقاومة في مستوطنة المطلة بالشمال الفلسطيني المحتل وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/76609" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGC_t5OmKPPi7HcW-CBpz4DrrBjWESx92usEfdIC4-5SDVi2EDEq5kKqUEUoejy8RWpdRc0tQeSly2QvDfqJg_-xqx6wz9CtoDoYQ6LUkQd1sb2bz17YshKnTipjVLQsiekUKIEreCm77pNwaZpRerPK0uoVfGnASsdn4-mZJ1qvz_KLfsD0sgynbw7K2j8gD9cnXtR4kOUlsSdVdzGCpoWXLh6zCByq1f0GBIb5TZkBsSO7Y25qFEmN1-l4CIpBhZtBUEQG_rTntCqOC9Wp7EhL3h8ynAEcnDIZARxNsqyAodoPv71ZsD3YT9vuuTde_lbbON__1kLwD2CAd-vJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إندلاع حريق وإرتفاع أعمدة الدخان بالقرب من مطار بن غوريون الإسرائيلي.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76608" target="_blank">📅 16:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول تواجد العدو في قلعة الشّقيف التّاريخيّة:‏
بِسْمِ اللَّـهِ الرحمن الرَّحِيم
‏﴿أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ﴾‏
صَدَقَ اللهُ العَلِيّ العَظِيم
مع التّأثير السّلبي الكبير الّذي تسبّبت به المواد المصوّرة التي تبثّها المقاومة الإسلاميّة لعمليّاتها ضدّ قوات جيش العدوّ الإسرائيليّ في وعي المستوطنين داخل كيان الاحتلال، سعى جيش العدوّ جاهدًا للحصول على صورة يروّج لها على أنّها انتصار ساحق، علّه يسكّن من خلالها روع مستوطني الشّمال، فكان الهدف هو قلعة الشّقيف التّاريخية في جنوب لبنان والتي تبعد عن الحدود اللّبنانيّة الفلسطينيّة حوالي 4 كلم فقط.
على مدى أكثر من 5 أيام، شنّ العدوّ الإسرائيليّ سلسلة من الاعتداءات الجويّة العنيفة والقصف المدفعيّ الكثيف على بلدة يحمر الشّقيف والقرى المحيطة بهدف السّيطرة عليها واحتلال قلعة الشّقيف، وما إن تقدّم باتّجاه أطراف البلدة الجنوبية حتّى واجه مقاومة بطوليّة وشرسة ونيران كثيفة من مجاهدي المقاومة الإسلاميّة منعته من تحقيق هدفه، فاكتفى بالّلجوء إلى أطراف البلدة الشرقيّة ذات التّضاريس الوعرة. غروب يوم السّبت 30/05/2026 تسلّلت مجموعة مشاة إسرائيليّة تحت غطاء دخانيّ كثيف من الجهة الشرقيّة لقلعة الشّقيف حيث المسارات غير المرئيّة، ووصلت إلى القلعة والتقطت مجموعة من الصّور الفوتوغرافيّة الّتي سارع العدوّ إلى توزيعها صباح الأحد والتّرويج بأنّه احتلّ القلعة، علمًا أنّ القلعة كانت خالية من أيّ وجود عسكريّ للمقاومة.
يجد العدو منذ فجر أمس وحتى ساعة إصدار هذا البيان صعوبة كبيرة في تثبيت قوّاته في محيط القلعة، حيث تتواجد هذه القوّات قرب منطقة الاستراحة أسفل القلعة. تخوض المقاومة الإسلاميّة معركة استنزاف ضدّ قوّات جيش العدوّ الإسرائيليّ المتواجدة في المنطقة، والمشاهد المصوّرة القادمة ستثبت ذلك.
﴿وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيم﴾‏
الإثنين 01-06-2026‏
15 ذو الحجة 1447 هـ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/76607" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
طيران حربي منخفض في سماء نواحي مدينة آبادان (عبادان) بمحافظة خوزستان الإيرانية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76606" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
القيادة المركزية الامريكية:
في الليلة الماضية في الساعة 11 مساء بالتوقيت الشرقي، اعترضت القوات الأمريكية بنجاح صاروخين باليستيين إيرانيين يستهدفان القوات الأمريكية المتمركزة في الكويت. هزمت هذه الصواريخ على الفور ولم يصب أي من الأفراد الأمريكيين بأذى.
لا تزال القيادة المركزية الأمريكية يقظة وستواصل حماية قواتنا من العدوان الإيراني مع دعم وقف إطلاق النار المستمر.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76605" target="_blank">📅 15:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daec07043a.mp4?token=BIefHyf-2usSKCRHa4xZFIvylsmsJpCxVjFnTtXSJxaSHI04-zKdQROYmx-Hz847stPU_Optavk7N78YPfzbGOLQz-6z61FiY3C1jKDsrn_gofR3F4GlWZ2I_-NAh3syMCLbpCZ0Id-9dSAPTgw-IWRHXI2CQ5-6XHvTp8cEbhT-4XXZYxk1yW15ooYsdVM03T8SmiRgKq3-VDz7IP1aPeptgKRsyJxcTl44znHWi6lwqj6bsBcFOnHiZsvN640yh2D5wYa0VaNXpowNg9OoxVnA10YBzq3n_OAgDIRbRIYGiKQS3lZCtGCY9CmGZRT-cj1MzCdw03Pp7sSgbgpq0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daec07043a.mp4?token=BIefHyf-2usSKCRHa4xZFIvylsmsJpCxVjFnTtXSJxaSHI04-zKdQROYmx-Hz847stPU_Optavk7N78YPfzbGOLQz-6z61FiY3C1jKDsrn_gofR3F4GlWZ2I_-NAh3syMCLbpCZ0Id-9dSAPTgw-IWRHXI2CQ5-6XHvTp8cEbhT-4XXZYxk1yW15ooYsdVM03T8SmiRgKq3-VDz7IP1aPeptgKRsyJxcTl44znHWi6lwqj6bsBcFOnHiZsvN640yh2D5wYa0VaNXpowNg9OoxVnA10YBzq3n_OAgDIRbRIYGiKQS3lZCtGCY9CmGZRT-cj1MzCdw03Pp7sSgbgpq0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الإحتلال الصهيوني ينشر ملاجئ جديدة في الشمال الفلسطيني المحتل خشية تصعيد محتمل.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76604" target="_blank">📅 15:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487f60223a.mp4?token=B4qJAFMv0GL8T6KwmKfJOniEsg9VF2p9awxsRMKWvpc-atLlEo86hPAsMZ4pDMOacg9SWwKFRRIz2iM_s4SHYwjXaOmd-mIMszt1AHq4ap8KL_TXsMU6jaQhOXMD2vr42UZEj3QnRqONjenviDKTOQsQ6-u4l03Bi4P9nMHIoUDVhqZzhvIR4mN1F2qDoZ9fuENO41CGDvJw8js3iTzlqL_Bl_PQie8KEs8fc36kEHVk8OoGBURCzOxaPeYGoSQWKQ4rs6te_KHCK2BqcCZduZrHfTIYcYq-XyaJY2RNT_9QABCApzcZyYdU812afUm7cnM-DIlcnLn0kf6Trpn80VS809OTpqCKe4x5WxklXgPfV3e59ou6orcH-qxw2MS7wx3PsQaK_XLdutdhnlAETZ-TJU3E3U9e1N8EYOaiqnBAC000BOSevmToBDcV0jh83PPbqIA7Obg34etckwys83nsErp_Xm3Jn6LdxjETk_TW3J4pJT7dCFd7FlgqYAviemXpBttzX0zufokRC1Zb_IES3TGlwqaR0HJ-QkJ2kpGKwt20_hNrOq_ZB1jI7ADVDBjumHcHk5HnmRVvTWbr9GgiS0pCs-Sh5YfNvo-a7KTQtmiILiGwmfVwoyvbMOVZ0Z_pDJ-U5uasSXtQFL5okfZ1pjQ_kfDO3S0VDfjJUyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487f60223a.mp4?token=B4qJAFMv0GL8T6KwmKfJOniEsg9VF2p9awxsRMKWvpc-atLlEo86hPAsMZ4pDMOacg9SWwKFRRIz2iM_s4SHYwjXaOmd-mIMszt1AHq4ap8KL_TXsMU6jaQhOXMD2vr42UZEj3QnRqONjenviDKTOQsQ6-u4l03Bi4P9nMHIoUDVhqZzhvIR4mN1F2qDoZ9fuENO41CGDvJw8js3iTzlqL_Bl_PQie8KEs8fc36kEHVk8OoGBURCzOxaPeYGoSQWKQ4rs6te_KHCK2BqcCZduZrHfTIYcYq-XyaJY2RNT_9QABCApzcZyYdU812afUm7cnM-DIlcnLn0kf6Trpn80VS809OTpqCKe4x5WxklXgPfV3e59ou6orcH-qxw2MS7wx3PsQaK_XLdutdhnlAETZ-TJU3E3U9e1N8EYOaiqnBAC000BOSevmToBDcV0jh83PPbqIA7Obg34etckwys83nsErp_Xm3Jn6LdxjETk_TW3J4pJT7dCFd7FlgqYAviemXpBttzX0zufokRC1Zb_IES3TGlwqaR0HJ-QkJ2kpGKwt20_hNrOq_ZB1jI7ADVDBjumHcHk5HnmRVvTWbr9GgiS0pCs-Sh5YfNvo-a7KTQtmiILiGwmfVwoyvbMOVZ0Z_pDJ-U5uasSXtQFL5okfZ1pjQ_kfDO3S0VDfjJUyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لتدمير طائرة MQ1 المسيّرة الأمريكية بواسطة نظام الدفاع الجديد التابع للقوات الجوية للحرس الثوري الإيراني فجر يوم أمس.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76603" target="_blank">📅 15:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
سماع انفجارات في حيفا.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76602" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76601" target="_blank">📅 15:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZwZ5UN8CUNcu6eF7jLa9xQDudC3P0eETXVDG8y2O4qLfJSfelgMxY2O8DAWA5Ln4qMZjD5KdFZ9OdK-1qvqEEjhU48vfCXUValToSKJabRzDUSwgu-oxUgkl6EJhyN5Bn5XkHP56gToL2BQ5NrrK6G7jKTiB1J845zo5-MME3U6ie0rtXOF7zylowmWoPh3BbWCFeCn9VX5128MPW_jaZqLC0ZAHtVQR_uPkIB05W34lNu0p6sfy-PTwYVB3OZhiysjUvCa4fOoIwWNOehnJlfrIEOM_dpkbvOz8cElY8rVg01iEmmNa_v-ERnLQ6HmE1E_MTwMhEtggOrRFBLEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
للعلم الفوري:
وقف إطلاق النار بين إيران والولايات المتحدة هو وقف إطلاق نار لا لبس فيه على جميع الجبهات، بما في ذلك في لبنان.
إن انتهاكه على جبهة واحدة هو انتهاك لوقف إطلاق النار على جميع الجبهات.
الولايات المتحدة وإسرائيل مسؤولتان عن عواقب أي انتهاك</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76600" target="_blank">📅 14:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce25a3cd4e.mp4?token=dKh5TBwlnAhvf7KNaT3JAXic6uNY-c59PJvC09BB2ItqGcYGH0RBLK6QENqoahPf9IcQCaqfK_aHmDO1NQJGsC7FtsQlYefjI3UVj_NWWXUBAwc42YOgLvZX-xv-FvtW89ljpJrlATBCvdmcYr3NXzUY86gXn4aajWWBJhoVOPNnVyZm9sS07wN-V_oD99wTvHmVNtzFi07kXvcONV8dD53QTV2yzcUKgWYzYrdGdDqD7cEfYtXPA5hVYxPz262THe6SkqVZycLXK04wE_Pnrtt_sYAFZKpaMVK-Hk-q9OdHF6pjKUypu3WHPxaxPe5yJNHNOUiByogQ40FV1Qh9nkA7i5X6i1q6eXqG2fJ_uTqxkppj42rEcFytbsQrDrHBAqxb-wOvtaY8-vb-sPlelZuHnmIjTM8fPXfQ7IKnIVloVLhdf2gUFHDdMxDbAzo0__Xnl_AFLS7nKfaOe5EwIVOCK8O2JB3b6j94LXdZPxYTKJwj3ZQucJSPrJ1qFgHS8BWaycABPL-4d_VH7MU0XUrnwv-tqdoq4tKSONT-dQBbt5vpQM0ymuhhNLc3nsvR1tRNDj3dIcyWFAGACrLhOdoQsI8MAdHrEfk2W-WIJTn4z0LEQtX4c3A4D-x65Hl0c_x6RZ9j9RI7iG8IligjaGB77peK-ETVKSJ1R9OhGyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce25a3cd4e.mp4?token=dKh5TBwlnAhvf7KNaT3JAXic6uNY-c59PJvC09BB2ItqGcYGH0RBLK6QENqoahPf9IcQCaqfK_aHmDO1NQJGsC7FtsQlYefjI3UVj_NWWXUBAwc42YOgLvZX-xv-FvtW89ljpJrlATBCvdmcYr3NXzUY86gXn4aajWWBJhoVOPNnVyZm9sS07wN-V_oD99wTvHmVNtzFi07kXvcONV8dD53QTV2yzcUKgWYzYrdGdDqD7cEfYtXPA5hVYxPz262THe6SkqVZycLXK04wE_Pnrtt_sYAFZKpaMVK-Hk-q9OdHF6pjKUypu3WHPxaxPe5yJNHNOUiByogQ40FV1Qh9nkA7i5X6i1q6eXqG2fJ_uTqxkppj42rEcFytbsQrDrHBAqxb-wOvtaY8-vb-sPlelZuHnmIjTM8fPXfQ7IKnIVloVLhdf2gUFHDdMxDbAzo0__Xnl_AFLS7nKfaOe5EwIVOCK8O2JB3b6j94LXdZPxYTKJwj3ZQucJSPrJ1qFgHS8BWaycABPL-4d_VH7MU0XUrnwv-tqdoq4tKSONT-dQBbt5vpQM0ymuhhNLc3nsvR1tRNDj3dIcyWFAGACrLhOdoQsI8MAdHrEfk2W-WIJTn4z0LEQtX4c3A4D-x65Hl0c_x6RZ9j9RI7iG8IligjaGB77peK-ETVKSJ1R9OhGyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام شمال فلسطين المحتلّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76599" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تعرض طائرة مروحية من نوع Bell إلى هبوط اضطراري داخل القاعدة أثناء تنفيذها طلعة تدريبية مما ادى إلى ارتطام الطائرة بالأرض ما تسبب بأضرار مادية في هيكلها</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76598" target="_blank">📅 14:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
قاليباف:  إن الحصار البحري وتصعيد جرائم الحرب في لبنان من قبل النظام الصهيوني الإبادي دليل واضح على عدم امتثال الولايات المتحدة لوقف إطلاق النار.  لكل خيار ثمن، ويجب دفع الفاتورة. كل شيء سيستقر في مكانه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76597" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
مصادر إعلامية تتحدث عن تغيرات   تسمية عبد الزهرة الهنداوي مدير اعلام مكتب رئيس الوزراء بدلا من ربيع نادر .  ‏ تسمية حيدر العبودي، المتحدث الرسمي بأسم الحكومة بدلا من باسم العوادي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76596" target="_blank">📅 13:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الجمهورية الاسلامية:
"نقل" اليورانيوم و "التخلص منه" ليس في مسودة الاتفاقية الأمريكية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76595" target="_blank">📅 13:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noqh6SO1oixiS-sG3qH63LMRlQL-1rro4AjZUfHulPDyJ64FOlTupoRCzegplmzxEnLfuF3H0tedIXgKMtQAzJOAB6jq_KsmjYLgb9OsqfQhM_XxEVsWzRqXRUDywbIfkL40zmJ_1XkeNbVJov3iKLvsR0poGQt2rzHN72MmqxWJLUpQjYcPzaHOTYz8Trm-9KLsDNDwg7Y0IHFcO_oqxU0rBGHv-UH0JURaB3qZslYmrfczGsODE_2AnpZWK7T4cEieA-qX0Ps-hCqqB7UfqZiX2BubDhaKXFyjRbV1v_h-AOkOjQGEyUdoaekQPe1byDllW-jbmsxMFRalRxMdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
أوروبا، التي تغذي الغضب العالمي من كل ادعاء لم يتم التحقق منه حول النساء في إيران وتصف المهاجمين على الشرطة بأنهم "متظاهرون"، انتقدت امرأة حامل بعنف على الأرض وسحبتها من شعرها في هولندا - ولا تزال صامتة إلى حد كبير.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76594" target="_blank">📅 13:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d9c96244.mp4?token=Oy04EWUWAoISXq4f7ogGrnLuRe6oVTQM4-SG0uHWBWU530XhepXRomfzmsj8c4H2twulaFz14NKb87jC-NN6_pXSqOv75LBFppUbcKpj3qnY_PtRS_x_47sxJPqiQ-O-gMFomugQSNdzBcvX_FnC146mLoDkuTDvzJPHwHGQE2_JuM2cihNZipXtwuu3FCwlCafJWmHnegk6_an5zfBxauSfX3U8HzbsA05tLvdrB2NXI8xtL5fNcYbKoVfxx5fkoWe7K3BJgCGlmqb24LzxQKJwKlvUG-zG6K5lweTR-R5AZrhw5SqJ1X8L9qp8pmy6p3hv1DZDuWvbAJW8xfEEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d9c96244.mp4?token=Oy04EWUWAoISXq4f7ogGrnLuRe6oVTQM4-SG0uHWBWU530XhepXRomfzmsj8c4H2twulaFz14NKb87jC-NN6_pXSqOv75LBFppUbcKpj3qnY_PtRS_x_47sxJPqiQ-O-gMFomugQSNdzBcvX_FnC146mLoDkuTDvzJPHwHGQE2_JuM2cihNZipXtwuu3FCwlCafJWmHnegk6_an5zfBxauSfX3U8HzbsA05tLvdrB2NXI8xtL5fNcYbKoVfxx5fkoWe7K3BJgCGlmqb24LzxQKJwKlvUG-zG6K5lweTR-R5AZrhw5SqJ1X8L9qp8pmy6p3hv1DZDuWvbAJW8xfEEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء طبريا بعد هجوم صاروخي من قبل حزب الله</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76593" target="_blank">📅 13:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76592" target="_blank">📅 12:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
مصادر إعلامية تتحدث عن تغيرات
تسمية عبد الزهرة الهنداوي مدير اعلام مكتب رئيس الوزراء بدلا من ربيع نادر .
‏ تسمية حيدر العبودي، المتحدث الرسمي بأسم الحكومة بدلا من باسم العوادي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76591" target="_blank">📅 12:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76590" target="_blank">📅 12:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjdeZlco5FlZgo1oyDByZfslXJEwUasjmXEl2q0Mc6I7h68esrGkBzWrKt70JlN_JuJ7TTK2AsKf8mdlKtu6g70SGq7P_C_vXj5o5N37UHEecu7rMkgQu18PVMBQ6qGEhXYipNmKzu9FpyjuzBNLVEt2q5mLa_LZ-Zrda5-q_msQWtUMq1NlaStKtiMhIGUNqA7f6EZxKN1VuWPRuWJxmr7ko-0cNwc_hu9eiR2wSoTdKmgWx9RYDNPqLFbP8A9kqIY-XLE_FpwXuGQcnUdHwolupyD8APFZ2r73P5Ff0X5FY7aGUJNBTFmEkPmuHnd9kuvIOBZTSS8Kmq0n56AdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إن الحصار البحري وتصعيد جرائم الحرب في لبنان من قبل النظام الصهيوني الإبادي دليل واضح على عدم امتثال الولايات المتحدة لوقف إطلاق النار.
لكل خيار ثمن، ويجب دفع الفاتورة. كل شيء سيستقر في مكانه</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76589" target="_blank">📅 12:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في ألون شابوت جنوب غرب مدينة القدس</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76588" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76587" target="_blank">📅 12:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSZTKxdMUedd_3fDsCtiijg9GI89s5AsgKZyRJRc0u-uJfe6v2_Mo_1jh54ww9RgbYUS5hxenHtFHa5s3r_BltH3z74Yedk0pY3yFS39xg4H_4gM5eibgtagoh8Q7MRkXAwUukPZbkNxcDvkBqwCiB041GesW6gHdWCcC0aHcwwXevS7pPsTe9jIZOLW_C3C-fd68rToFwQb2sI7geeQPYx2kJ_BTVBwBI0y0k4HX0PxIWuZXlRWxBYPcxttP7_PyivN4q79N2wwdlS3O40GpkSPsuYbOuL8cJZBa9pjgKQIWtm_WHQBlMlAUhhl-iFPKeMdw_fm6z4WYUtC2_3qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الاصطناعية في 29 مايو سفينة بطول 252 مترًا مشتعلة عند مدخل مضيق هرمز، مع اقتراب أربعة زوارق سريعة كبيرة مشتبه بها تابعة للحرس الثوري الإيراني من الاتجاه الإيراني، ومغادرة خامسة من الاتجاه الجنوبي الشرقي.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76586" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWTmlnSjrh6z2fVxvqtipZHZd8mQDRyPM7s29BggSdwbLk4ZGJ9EtdGj-_uK1_upzGskHK7A5TEG2fwgak9Cx_GnGhy1f2sNfCvKw5INXozIa2I5T_SUQfxSmBGjuGP5h9OPU3chuQrAHK59GZGr6SbVnLWKdcjnu7YCgVud88UdV-Gf6RpAOh7Y8kBPMuqEAVKXHpiwKUqz2WXdk7yxed-2LxgCXC35ks5lm7dG8PlQnmSM-1xVc-nfJu7u1bana8KOwY9nfW5slKY4AUBWxUaRHGLkSs8jWN1QVmgMA8rfsOE5vjXUbVTycV21dVNPgzV5Adm_4s9t2Guoax2-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رؤية اخرى !</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76585" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
حزب الله: تصدّى مجاهدو المُقاومة الإسلاميّة عند السّاعة 15:30 أمس الأحد 31-05-2026‏ لمسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء البقاع بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/76584" target="_blank">📅 11:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇰🇼
دويلة الكويت تدين الهجمات الإيرانية على قاعدة علي السالم في أراضيها.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76583" target="_blank">📅 11:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=vkB8aDTgaoX5azsf2TD0H6IHNgYfF5e_AMyMcsQWwjhLzhjB4DFckY7ktT_ShcZAzLS-dIwCt3R3WflXmi09uFNl8uHq-Hzpc_BIy6EjSCgk_RNkd3vOzXQ66FhTLeDEbjfti8W_D9HMWU7l4UwFmkdiyGFvE6uTcZX1zNG_iqKGzsxIeAjtugqOdxjs3tiADKeiKrLENBjr_KM2Sd1jAXqe_wjIIT11J0E_Qw3wbkmW2pRjxs7FJ-y6KoHeOOtlV2mOciXb19hSmTvFhtx51qdiYu7_ez5nQ7lQ7fFjHDe5u9-FX6xbXTSczLk-rvjDncL68pRUrjPWs4EPWbcbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=vkB8aDTgaoX5azsf2TD0H6IHNgYfF5e_AMyMcsQWwjhLzhjB4DFckY7ktT_ShcZAzLS-dIwCt3R3WflXmi09uFNl8uHq-Hzpc_BIy6EjSCgk_RNkd3vOzXQ66FhTLeDEbjfti8W_D9HMWU7l4UwFmkdiyGFvE6uTcZX1zNG_iqKGzsxIeAjtugqOdxjs3tiADKeiKrLENBjr_KM2Sd1jAXqe_wjIIT11J0E_Qw3wbkmW2pRjxs7FJ-y6KoHeOOtlV2mOciXb19hSmTvFhtx51qdiYu7_ez5nQ7lQ7fFjHDe5u9-FX6xbXTSczLk-rvjDncL68pRUrjPWs4EPWbcbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حركة نزوح تشهدها الضاحية الجنوبية بعد توجه نتنياهو وكاتس بقصفها إلى جانب تعطيل جميع المدارس.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76582" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان وإخلاء مروحي ل 4 جنود مصابين.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76581" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
إسماعيل بقائي: تبادل الرسائل يجري في أجواء انعدام الثقة والشكوك الشديدة والدبلوماسية ليست بديلاً عن عناصر القوة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76580" target="_blank">📅 11:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b911e1c9.mp4?token=u68VxHrv4CXkfCXHwktmWZBto21ajW6qxuS0eqtArZqZBLcIL9PY5WPWJthKyRFh10rk8c52rDmAVfmKkbSfJZlsfKrg4sthCSYz3H5NrbtC9BuysSsq3kuG6GRTmR1Isqs1RK74m5UXyRgtEThbQNCHvB0F1aYH4kM9adFm9qce1uSU3nadkGdGkQxzZhd4wtBlOabK9l-xyGfdcru9S5CMuep3j3WkJQK8fkKrOtC6qI5iI2QWIp6Qz5madtP2AKE8ARDutcLj438fQf7i8QSaZObUeqDjyKARH-wAXU0iQv4r_UI6YRqGJTNbzIxkaZPgRSVghCzGmbOxR5deag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b911e1c9.mp4?token=u68VxHrv4CXkfCXHwktmWZBto21ajW6qxuS0eqtArZqZBLcIL9PY5WPWJthKyRFh10rk8c52rDmAVfmKkbSfJZlsfKrg4sthCSYz3H5NrbtC9BuysSsq3kuG6GRTmR1Isqs1RK74m5UXyRgtEThbQNCHvB0F1aYH4kM9adFm9qce1uSU3nadkGdGkQxzZhd4wtBlOabK9l-xyGfdcru9S5CMuep3j3WkJQK8fkKrOtC6qI5iI2QWIp6Qz5madtP2AKE8ARDutcLj438fQf7i8QSaZObUeqDjyKARH-wAXU0iQv4r_UI6YRqGJTNbzIxkaZPgRSVghCzGmbOxR5deag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76579" target="_blank">📅 10:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76578">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76578" target="_blank">📅 10:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76577" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76576">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
استقبلت الشركة العامة لموانئ العراق اليوم الاثنين 1 حزيران/ يونيو 2026، سفينة الشحن (MV KSL XINYANG) القادمة من الصين بشكل مباشر عبر مضيق هرمز، لتكون أول سفينة تصل إلى ميناء أم قصر الشمالي بعد استئناف حركة الملاحة البحرية عبر المضيق.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76576" target="_blank">📅 10:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76573">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76573" target="_blank">📅 10:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdnS3p1YeJpI_EJjS5PIECZsVCpE7128AGrP3dPku0XlmQdXbx4o-c-T-IP5ZzT781l_7ufArMYQYwV-rd1ffcmSqhU9xOSUdoTClfF6_MXsCo8FcMlT-LLDwN0Ip5WjFbsl1-CZ7fkLV1rZBQw3vReXO6RvkKYMmcKvbiQ_W2lU2GU3bvnRDHZvJHo5U6lfKuSX4vCeK6LJ1hKXSTH7xclrn-HWBfOP2V2bPMoETIvSRLTxaz7ptJb9i8euTGQfSH_zx2fFtp4oL-ddd-btJxBt40IyFEbUV7dbvzArpy3a7-kABfUTwUMlldKSOv8wrlJQrf20niZtfBuwxfuaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي:
إن بيان الاتحاد الأوروبي الذي يُلقي باللوم على إيران لممارستها حقها في الدفاع عن النفس ضد العدوان الأمريكي الذي شُنّ من قواعد في الدول المجاورة هو درسٌ نموذجي في الغضب الأخلاقي الانتقائي؛ إنه نفاقٌ وتهور.
يجب على الاتحاد الأوروبي (
@eu_eeas
) أن يظل وفيًا لسيادة القانون ومبادئ ميثاق الأمم المتحدة التي طالما ادعى أنه يدعمها. يجب عليه التوقف عن استرضاء المعتدين مع إلقاء اللوم على أولئك الذين يردون على الهجمات غير المشروعة.
إن ضربات إيران ضد تلك القواعد والأصول التي تُستخدم لشن هجمات غير مشروعة ضد إيران هي ممارسة مشروعة للدفاع عن النفس.
تقع على عاتق الدول التزامات قانونية راسخة بعدم السماح باستخدام أراضيها أو أصولها لغزو دول أخرى</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76572" target="_blank">📅 09:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📰
إكسيوس: تعثرت أحدث جهود الولايات المتحدة لتأمين وقف إطلاق النار في لبنان حيث توسع إسرائيل هجومها البري وتسعى للحصول على موافقة الولايات المتحدة لشن ضربات كبيرة في بيروت.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76571" target="_blank">📅 09:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76570" target="_blank">📅 09:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوي انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76569" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال:
وقع الحادث قرابة الساعة الواحدة صباحاً، حيث استُهدفت قوة ماجلان التابعة لقيادة العمليات الخاصة بطائرة مسيّرة مُحمّلة بالمتفجرات. وإلى جانب القتيل، أُصيب ثلاثة آخرون - أحدهم بإصابات خطيرة واثنان بإصابات طفيفة. وتمّ إجلاء المصابين بواسطة مروحية إلى مستشفى زيف في صفد
حيث أصيب 137 ضابطا وجنديا في معارك جنوب لبنان خلال الأسبوعين الماضيين</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76568" target="_blank">📅 09:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76567" target="_blank">📅 08:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igq-pZLvwrWOiTYmfIupPDK-NXUmZReApb4t-leZxb0sh1Mqavy9uO9qL9Kn55VoqwdQp4EGZHgGjJuvvWaaJ0TaizybCb1q5zeUwPV5KEP2vHhQgd-oMw4RXrAUqP2-sQHkiP5sgUAtpLOdissbGcKC1NlWLir5CWODgomUJ6gADUCzn2iLwP5qVqQvjOgujvkdzM6xfdwGy4u8tOSDd2mUOEawVM3-1vQRLdZ7awReUcLR6z9up2DPk3e88PwERfI7q1xYaZQSN-y2VO60WnvCmK1-lE-9EkLXwnxscdFA4GamEbb8C-P0zIIQk97GdMsWTtKeO0AZcL13ppIZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إيران تريد حقًا عقد صفقة، وستكون صفقة جيدة للولايات المتحدة الأمريكية ولأولئك الذين يؤيدوننا. لكن ألا يفهم الديمقراطيون، والجمهوريون الذين يبدون غير وطنيين في كثير من الأحيان، أنه من الصعب جدًا بالنسبة لي أن أقوم بعملي بشكل صحيح والتفاوض، عندما يستمر السياسيون المخادعون في "التغريد" بشكل سلبي، على مستويات لم يسبق لها مثيل، مرارًا وتكرارًا، بأنه يجب أن أتحرك بشكل أسرع، أو أن أتحرك بشكل أبطأ، أو أن أذهب إلى الحرب، أو ألا أذهب إلى الحرب، أو أيًا كان. فقط اجلسوا واسترخوا، كل شيء سيكون على ما يرام في النهاية - سيكون كذلك دائمًا!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76566" target="_blank">📅 08:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc05a6034.mp4?token=Qa7L7B-qgT7hZQPhNWZk3_H9bStwTBBYnSfWCVLXDSiG3RAeXKn-5GdhO7fSaMXF1RTO18zx69TAPpCEG9gWvGSLU3831pGJr20_PhQeDfkfETaTRGa2el-1jnjYeJziKpMJ908p0Xg7rUhOF4kWYMSe_y3HKhUw79UGZ9KYofd4Mw2Jtt5K5C3wS2Gg9wuA6QqPlS1e60bVlNNhFhcyzBqSRRyFHVauMqDmY8eG1bvoPAvblft9XRpji2nYJSe7rdcR6pbKM5aClnWFvgYyLoucyxayvKtPUoDhUXFmQPZpmEurotfh504o2HyAPmlw6zoW74wR-wpeGkYTEnstFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc05a6034.mp4?token=Qa7L7B-qgT7hZQPhNWZk3_H9bStwTBBYnSfWCVLXDSiG3RAeXKn-5GdhO7fSaMXF1RTO18zx69TAPpCEG9gWvGSLU3831pGJr20_PhQeDfkfETaTRGa2el-1jnjYeJziKpMJ908p0Xg7rUhOF4kWYMSe_y3HKhUw79UGZ9KYofd4Mw2Jtt5K5C3wS2Gg9wuA6QqPlS1e60bVlNNhFhcyzBqSRRyFHVauMqDmY8eG1bvoPAvblft9XRpji2nYJSe7rdcR6pbKM5aClnWFvgYyLoucyxayvKtPUoDhUXFmQPZpmEurotfh504o2HyAPmlw6zoW74wR-wpeGkYTEnstFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني: استهدف مقاتلو قوة الجو الفضائية للحرس قاعدة جوية منشأ الاعتداء وتم تدمير الأهداف المتوقعة رداً على الاعتداء برج اتصالات في سيريك</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76565" target="_blank">📅 08:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
على الرغم من أن الأمريكيين والإيرانيين لم يوقعوا بعد اتفاقاً لوقف إطلاق النار طويل الأمد أو اتفاقاً لإنهاء الحرب، فقد بدأت "إسرائيل" تدرك أن الحملة في إيران لم تحقق النتائج المرجوة. فقد زعمت مصادر في المؤسسة الأمنية الإسرائيلية، أمس (الأحد)، أن الرئيس الأمريكي دونالد ترامب لم يمنح صلاحيات كاملة للعمل ضد إيران، وعرقل أجزاءً من الخطط العسكرية وخطط الموساد، بما في ذلك مهاجمة خزانات النفط والغاز ومحطات توليد الطاقة ومحطات تحلية المياه في إيران. يُزعم أيضاً أن ترامب، تحت ضغط من الرئيس التركي رجب طيب أردوغان وكبار المسؤولين الأمريكيين، وعلى رأسهم نائب الرئيس جيه دي فانس ومستشاره المقرب ستيف ويتكوف ، عرقل عمليات جيش الميليشيات الكردية في إيران . وقد بُني هذا الجيش على مدى سنوات من قبل الولايات المتحدة والموساد الإسرائيلي، وكان من المفترض أن يقود القتال ضد الحرس الثوري الإيراني ويؤدي إلى انهيار النظام. لكن بدأت الانتقادات تتعالى داخل المؤسسة الأمنية الإسرائيلية بشأن تحقيق أهداف الحرب. قال مصدر عسكري: "على مدى أربعين يومًا، زُوّد الموساد بكل القوة النارية التي طلبها. وتلقّى استجابة عملياتية لكل ما حلم به وتخيّله. عندما طلب فتح نقاط تفتيش الباسيج، تمّ ذلك. لم تكن هناك نقطة تفتيش أو مقرّ قيادة يشيرون إليه، ولم يتم تدميرها. ولكن ماذا؟ أين النتيجة الموعودة؟ أين تفكيك النظام؟" في غضون ذلك، تحاول النخبة السياسية الإسرائيلية تصوير النصر في لبنان بصورة ما. ومع دخول الجيش الإسرائيلي شهره الرابع من حرب "زئيرالأسد" وحرب "وقف إطلاق النار" ، فإن الاستيلاء على قلعة الشقيف ليس إلا حدثًا تكتيكيًا. كما قال ضابط كبير في الجيش الإسرائيلي: "دعونا نضع الأمور في نصابها. في النهاية، تغلبنا على عقبة أخرى. الآن لا نستطيع القيام بالخطوات التي نرغب بها. هناك خطط، لكن لا يوجد تفويض للعمل. نحن نحاول السير على حافة الهاوية بين ما يوافق عليه الأمريكيون ضمنيًا وما يمنعونه ويقيدونن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76564" target="_blank">📅 08:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76563" target="_blank">📅 08:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP8hqaxXfTvpdpnZnY9XnkRusS18fJ_J7GZVNB2Z0EpM93JCWs2tGfVw8ZEchWhGxjIwqq4pQKdxFfjVAtJlC0YtrjZ-ByPelWv6ghKhH7ASNBtjiy_Ge0Rb4BuYrLmk6vt1AuZJfW2y6iMZUP43k8pnDegrrkXSYoYNUkIekct3YI21-LWK588a1KCZeiR0I9nn7CICo5fEttsHR4TlDOCgAiNxVSsB-FKAUqw32V_l1KlQhQvLw_IefOFuqcZoeq2sBrw9XFYjJSlAXizcvm-TdRebsA5SpGpWcOezK_6OATKBh-f-wAk7KuYpoxfd0SnWveaG4RxTSJ_Km3ishw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emwrKKmMz3OXyzx8kyQI5pARfiRzwFBKoeSIzKbijbrgDxv87EZIzt0xBkVmXzCHGkPkqbEAiaUW-8oTAjgfg17WdDlTwrsOyuPhxenVnyYj1zeEkiTGCpOzudQD0dIpB52s86P4ln9lylXhHFEv3-D4jg2FCv5Ov8WRAltHsxlY_UUa75Zgj7yDMsHMHE2wia2qurSPgX7mjcpvP7cJypwTtMR518oUZz6WvaeSgwjkVOiDi9-h9KfAjLCZVLvF-nw_bVb98G7VAlFpI454em9A-CA0O9JCuBzA2Pe5SzjpgDuC7p80-Di81UDyu3d277h8f06bhdaOpojZnonV5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/76561" target="_blank">📅 01:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76560" target="_blank">📅 01:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76559" target="_blank">📅 01:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76558" target="_blank">📅 01:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وكيل وزارة النفط العراقية عدنان الجميلي مع الاسلحة التي تم اخراجها من منزله اثناء اعتقاله</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76557" target="_blank">📅 01:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عملية امنية كبرى في محافظة كربلاء المقدسة واعتقالات بالجملة لمجموعة الصرخي</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76556" target="_blank">📅 01:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdNreu04rZW1JhYucK6Md6J-Tyva3PVb9_vqbzbSRACiFv_yDX11KylN_MYqq_ugDjMbE4behp0YP6ltln1_wKIhObaC5KW-iB_RuseOnlSzlGYbqeilxKzgFPiFg7xLhGFNaOLanxzX_TOtyauWDZEYczvXpANqO7GcprjkWIqIDkvN9Mi0z2nWfiuk5_c1gJF_d3AMiAhZSRsw8G6OkmXMppMYQTY1L_e-srTNb87WwheiyujuFWqEzyYWbjcVmPBNP8Ne2O5sI77eeFbHe7EDeEqc7s1xw6RfEtPKJGAUcvKkfOVt8L1YXDsXt0V5UKXLCkmm6sqthoXNbI3xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76555" target="_blank">📅 00:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انباء اولية عن حدث امني في قاعدة الكوت الجوية شرقي العراق</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76554" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انباء اولية عن حدث امني في قاعدة الكوت الجوية شرقي العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76553" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات تهز وادي الانه بمحافظة اربيل في اقليم كردستان العراق بعد استهداف مقرات المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76552" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو الإسرائيلي:
في متابعة للتوجيه المسبق الذي تم توزيعه قبل وقت قصير عقب رصد إطلاق صواريخ من لبنان، تم رصد إطلاق صاروخ سقط في المنطقة التي تعمل بها قوات الجيش الإسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76551" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
لجنة الأمن القومي في البرلمان الايراني:
ليس لدينا أي التزام في الملف النووي تجاه الطرف الاميركي.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76550" target="_blank">📅 23:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76548" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1d-Fc13rH-xjb5UE-5oYacckSrFKOxzh7gBoR2XHeLExsrXaYHos32QurHKb-3hkji3WU774_BLqBPZ7O4kJacrPhRTeoNwsmhpt2EDjKoUacDfMtlD8UX0yERIFk7lUB6cdW2Is1npbMeuGYEoysP5Jh1STFFYGtmYwAPOwfLKVssXPJee2xLAIYupw2V8Rc7wVr3XwnfKl1goAuYHvviskRTCd18_zw-4rl1AT8-PzzAgPeDjzNIVxCGj1K4eVGukaQTuKz_j8sb2mMsgwxCg1z9ZENMMxTFOHRvf9RKlxHctSFiOwlDcofoTzCjLcA_H3tjxuvaWcNkcZ-2zMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9vsQqrfmdRSPYPg7M92Q6A7sjLUuP5dcVUFGa_dT9d349QulxNKXkZGqvLlyuG4syGTAsTMPGk8k--2M67ps6hzbkBpkaFMPlMy8aiZKolAcJ0eTKj7-XDjt5S5k8jkUBWkBeum7klXN4Qe6bIQcjmHQ5TuQbM3aFyEX-kOO54ZkEqgmc2K5sxjCeNv8JLRguDnTEkSFmjbQs_BKs334MqNnfcm2kh6uleUgphkyKpDmUfJh-88KJJEBtwxUSzredJJ8N2fMPHVWqEXQuvewf_xM9WewwWHzdrQKQ2Q2pgrXvPDcLTCoJ7egvN7EHdZEmKBtcTbi1ipnWlY44Cpfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
غضب في صفوف الايزيديين في العراق بعد قيام قيادي في حزب البرزاني ومسؤول في الاقليم ورئيس منظمة انسانية بالمطالبة بوضع شخص مسلم اميرا للايزيديين!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76546" target="_blank">📅 21:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmF0tfDVSbzUCuEgS2YTLf7RUFsBufd4B1KsqnTYXGvUXCj5DzFee67IUvuT4Q0W2HoWh8ODEIJ0JX05g4Htz5O35moAtsbgN8PooSIny7MrAYcX-j31KQK0yyCAa-iMDGhoD3XUVyLe4wisTZUNtQqZkn7g_xLVi4ItE0ME6kIfEXY7msYqdM_ciCOZaK19rb_PKT6evziLEMiZ_kw-u7VWSa2ETxcrE4xkkaZyum1FVL6v2UfJIA7kVVV8GYcQ37X_8EeiPuuZM_pDII0dp_XgHpsooVs5Uvyof5pxjyWLSoNUMuZQ3VaRE5EkS93A-Nmzjh4YBvlhVGxz_STQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✌
👌
👍
🇮🇶
🔵
مقتل احد المرتزقة الإيطاليين يدعى أليكس بينشي في جمهورية الدونباس الروسية اثناء معارك مع الجيش الروسي ، الأخير كان يعمل كمدرب لقوات الناتو في اقليم كوردستان العراق وتربطه علاقة خاصة مع بيت البارزاني ، حيث تظهر الصورة تواجده في أربيل بجانب بياران بارزاني</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76545" target="_blank">📅 21:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76543" target="_blank">📅 21:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
إبن شاه إيران الهارب، العميل "رضا بهلوي":
على عكس هذا النظام الذي يريد محو إسرائيل من خريطة العالم، فإننا نعتبرهم شركاء استراتيجيين حقيقيين. نرحب بأصدقائنا الإسرائيليين لمساعدتنا في العديد من التحديات التي تواجهها إيران. ليس لدينا أي خلاف مع إسرائيل.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76542" target="_blank">📅 21:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
26-05-2026
منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في ثكنة بيرانيت على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76541" target="_blank">📅 21:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf6c39776.mp4?token=vRAA3Yw_aAjjkrfD-BRJVrLPReGTxLazXFUtpEbhQv4C9uGuJ26lny64DYuXSvbxQwFUJ_kzXa5TGCn7GUvGsUY3VExOj9R3Jox--g_-qC78aZ1e-YuIC9FanufLWTbVFZb_29-Qp_pcUK4PvYlpznFeekY7s_DjDhiiUkEJnws_pLra5fxl0yJeZ7nXzR1Eo1-N_WuIjHXNbL_1bxsYJLxKi6kQ8YuW_TH86zSKeAw82E6uSxLU4f_wpVX-pTDazBrCl-376xaqt2GkGrp6wgo9eSuONadHuzh3EQLYy4xwL_bfRUNfvvoMDYtrXPYvehf_w3sA3ZT5Jm_-3wukbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf6c39776.mp4?token=vRAA3Yw_aAjjkrfD-BRJVrLPReGTxLazXFUtpEbhQv4C9uGuJ26lny64DYuXSvbxQwFUJ_kzXa5TGCn7GUvGsUY3VExOj9R3Jox--g_-qC78aZ1e-YuIC9FanufLWTbVFZb_29-Qp_pcUK4PvYlpznFeekY7s_DjDhiiUkEJnws_pLra5fxl0yJeZ7nXzR1Eo1-N_WuIjHXNbL_1bxsYJLxKi6kQ8YuW_TH86zSKeAw82E6uSxLU4f_wpVX-pTDazBrCl-376xaqt2GkGrp6wgo9eSuONadHuzh3EQLYy4xwL_bfRUNfvvoMDYtrXPYvehf_w3sA3ZT5Jm_-3wukbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد تظهر الدمار في القاعدة الإسرائيلية في بيت هلل نتيجة دكها بمسيرة إنقضاضية اطلقها حزب الله.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76540" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de658edb85.mp4?token=kGLWQTWXqkF0ZE5qhCdRjD5RQE-kHEFKP5NmbLAKV1fa26pE3k6evzqxUa47vE_TaRuuAVeW-fjzg5Dl4ZhVpI_OOrmgfOaQEPsV-z4Bzfn3jeFHyzwDlHHxm-QJEBNdE1GKMXqL6U2iDmIcCqSmQ5ZEdr60UzXjJFElbfN3CLIQliWczeFlqXNwJFs0uSTfbbTO82keka-jzf9oFrnvdl6rWi8CZvML4ZQQBh004CERT3c-QmGkvJdWCpDpLJiRndHQadWr7Pcg_aY9I1Shh64RxbSK9Elnq21ITpvikJYdtEZjQPv7zjUckopc2BD9q7mY7MoA6ZCLcDqnRPVZGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de658edb85.mp4?token=kGLWQTWXqkF0ZE5qhCdRjD5RQE-kHEFKP5NmbLAKV1fa26pE3k6evzqxUa47vE_TaRuuAVeW-fjzg5Dl4ZhVpI_OOrmgfOaQEPsV-z4Bzfn3jeFHyzwDlHHxm-QJEBNdE1GKMXqL6U2iDmIcCqSmQ5ZEdr60UzXjJFElbfN3CLIQliWczeFlqXNwJFs0uSTfbbTO82keka-jzf9oFrnvdl6rWi8CZvML4ZQQBh004CERT3c-QmGkvJdWCpDpLJiRndHQadWr7Pcg_aY9I1Shh64RxbSK9Elnq21ITpvikJYdtEZjQPv7zjUckopc2BD9q7mY7MoA6ZCLcDqnRPVZGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إسعافات نجمة داوود تنقل عدة إصابات 2 منها بحالة خطيرة جراء عملية دهس قرب غوش عتصيون في الخليل.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76539" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99a02cad4.mp4?token=ehm8YvM6UhsgdihOvFvd23uDDId-ph9-88TaBTYJoVQ9xM3UB59sDTdJgVm67gRVFJHKKWS0nBZFBUJpUpOBmejuPZFENXQNhCi_IzW8yEnyRGTx1YrQGAsPKL0eKdTZm9yNLKUfVbLFe0O6oDsvDIchZ1v6fSDx5lMm2a3Egc6yKMTG3Lz0Htap9avonRWxwX7lOJUC8v94_1TeTzSgUlPbmppGZigVRwU2V3929UaizOuYPFFwR70bWgCid44Ygde_Aezl6PLGKEnrJ6T3KjGVvUN638g23rgmd2G_v5HyCQlJr2U6SmENgh0x4nZxqzM7noc94I5muNA0vfV9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99a02cad4.mp4?token=ehm8YvM6UhsgdihOvFvd23uDDId-ph9-88TaBTYJoVQ9xM3UB59sDTdJgVm67gRVFJHKKWS0nBZFBUJpUpOBmejuPZFENXQNhCi_IzW8yEnyRGTx1YrQGAsPKL0eKdTZm9yNLKUfVbLFe0O6oDsvDIchZ1v6fSDx5lMm2a3Egc6yKMTG3Lz0Htap9avonRWxwX7lOJUC8v94_1TeTzSgUlPbmppGZigVRwU2V3929UaizOuYPFFwR70bWgCid44Ygde_Aezl6PLGKEnrJ6T3KjGVvUN638g23rgmd2G_v5HyCQlJr2U6SmENgh0x4nZxqzM7noc94I5muNA0vfV9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقجي:
المحادثات وتبادل الرسائل لا يزال مستمراً، وحتى يتم التوصل إلى نتيجة واضحة، يستحيل الحكم، وكل ما يُقال الآن مجرد تكهنات ولا ينبغي أخذه على محمل الجد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76538" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce9d77b27.mp4?token=gmrqMa05EXZcqQXIcBgBnSjeLWOAE74o2iDLJpaHVtkfTb432x-PXlB6A1X10sywG9MawIelB7xOlwjM4eOWW7zm7yJXgDKIYMH9wYEsl6DO31-1GXXuGLP-KhDcddYDsVAwi3Tsw1DprFI7pAF7VOdJi6rZRLCoZ7bdyENtZ4L0SPK_CvElfVwc_9KRH9td7tDN-OWIbLi_p6L9p2sQVOJAosi9tR0bkAWjAjEeEe53L0gSI-C05Sju09Nqa4iUpnRYMZBuftZj4PiNEl_dVg4tl8t2qOYKPKVv_6U25KT1VzBDarH3jw8FuBN4Wem_n_NooO8i5uqjukCqGqBPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce9d77b27.mp4?token=gmrqMa05EXZcqQXIcBgBnSjeLWOAE74o2iDLJpaHVtkfTb432x-PXlB6A1X10sywG9MawIelB7xOlwjM4eOWW7zm7yJXgDKIYMH9wYEsl6DO31-1GXXuGLP-KhDcddYDsVAwi3Tsw1DprFI7pAF7VOdJi6rZRLCoZ7bdyENtZ4L0SPK_CvElfVwc_9KRH9td7tDN-OWIbLi_p6L9p2sQVOJAosi9tR0bkAWjAjEeEe53L0gSI-C05Sju09Nqa4iUpnRYMZBuftZj4PiNEl_dVg4tl8t2qOYKPKVv_6U25KT1VzBDarH3jw8FuBN4Wem_n_NooO8i5uqjukCqGqBPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رداً على أكاذيب إنترناشونال..
مصدر مطلع في الحكومة الإيرانية:
الرئيس بزشكيان لم يستقيل، وأنه منشغلٌ بأعماله، وأن خططه المستقبلية ستُنفذ كالمعتاد.
الهدف من هذا الأكاذيب بث الفتنة وتقويض النسيج الاجتماعي المقدس في إيران.
الشائعات التي يتم تداولها، عادةً ما تكون من نسج خيال القائمين على هذه الشبكات، ولا أساس لها من الصحة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76537" target="_blank">📅 20:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX67dydSd2TnDNQbyqjobqa3O481BqZndRB8KpTihck6NM2VXbfFMrij_kzJXOpYK7g02NydpMwFw6mv_szlq-XdYivpN0zSpUEOEiPBDYpiX3H-oNmtQ_UoBOMhikSUM0NrM6uR9H4vOwgJ-KOPkTVKFYMwwzh8FqByzUHHUgDuSDLfRoGEugq_0NVsmlwoK9_QpLYKPV2ClikUCvNYSiQPfcI3Zh1TSdSuXz1vW5kKpZTMmbnLXg_UDu-wGEwzDhaZPB36l6NFDkL1ZSGqpukJ90rvoDZ3CqhGv_F9gHjodbXe8pzOddqZUwf4qCX68ebjoGlKG1BVpRyyS-zi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سيكون ميناء الطائرات بدون طيار في قاعة البيت الأبيض، ربما، الأكثر تطوراً في أي مكان في العالم! سيحمي منطقة العاصمة في واشنطن دي سي لفترة طويلة في المستقبل.
مع ظهور أسلحة حديثة متطورة وقوية للغاية، لم يعد بإمكاننا حماية واشنطن دي سي باستخدام البنادق والمسدسات وحدها.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76536" target="_blank">📅 20:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
مساعد قائد القوات البحرية للحرس الثوري الإيراني:
سنقاتل ضد أي تجاوزات للعدو، بكل قوة، حتى اللحظة الأخيرة، وليطمئن الشعب الإيراني الكريم أن أبناءه في صفوف القوات المسلحة، بأسلحتهم جاهزة، يدافعون عن أمن وشرف هذه الحدود والوطن.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76535" target="_blank">📅 20:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية ضخمة من لبنان نحو مستوطنات الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76534" target="_blank">📅 19:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da394b0bcc.mp4?token=UXZ2mHXxclaRkMF-FO-G3J-cmeL1x8yGiJmzzX1AE3AZ-XrLEglJ2k3O1-alesIkhb6qC2P99IyBCPvx1tGUwP2CxTIxoB9-YDpsG18byKzpCcsBxIPiUmryUmT4KMZK5oDJG2ttaK35GfZV9eHEKyJBr-PZgQJflWpHpFnag8A_3q2QJOvSogroWmMerzLahdJPEN-YRtFf5TUxT6JpSURqfrD0_MRj77oSan2BGshUWcINyqWKRTTkLh30x7nkCSn2_V-lGPMzwBfqBkrhRTnKqFw2PHrmBfO5yt676f_Mt8aDgDaGC0OScqin1VaCdzQDHMOe3tF0Nop96bloyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da394b0bcc.mp4?token=UXZ2mHXxclaRkMF-FO-G3J-cmeL1x8yGiJmzzX1AE3AZ-XrLEglJ2k3O1-alesIkhb6qC2P99IyBCPvx1tGUwP2CxTIxoB9-YDpsG18byKzpCcsBxIPiUmryUmT4KMZK5oDJG2ttaK35GfZV9eHEKyJBr-PZgQJflWpHpFnag8A_3q2QJOvSogroWmMerzLahdJPEN-YRtFf5TUxT6JpSURqfrD0_MRj77oSan2BGshUWcINyqWKRTTkLh30x7nkCSn2_V-lGPMzwBfqBkrhRTnKqFw2PHrmBfO5yt676f_Mt8aDgDaGC0OScqin1VaCdzQDHMOe3tF0Nop96bloyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية ضخمة من لبنان نحو مستوطنات الشمال الفلسطيني المحتل والدفاعات الصهيونية تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76533" target="_blank">📅 19:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76531">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOu_GhKU_EVI9FzfyCtKZKKtQhWTlGVNPtqiLLepOi_d1KwnJyGTORfkFHMFvEbM4e-1wekToqU40ck97G9FvZ1gzR1lsuQ3VSvSYDfnv0M8K-K1tCQiSbVsjB4ekSZNR-Bo9cw2QmWvV7QuoHdzlRGmQGZrJtkzh7d8eGFcQHF78LGA_DMeLtkR_dzJ90p1dUM0uxZcZUi0BAxiR6GUNr77ZUFzWiChon2jVRpZjv-a_uXW0QtPUC9HfwDLFzjM1dyboeY5dFRUbGxPDBG_u98jSVBgkfY12bP7CtsT2l7ibA9bUqAjIVObYr2I2Z7SAXCMYBsbC__riyTlkwMXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9086b036.mp4?token=dL93C0WsNrHAqJZf3ORewKhl4m-blSltjfGohqz9h0EsWrdZvW_3SYLpqSx7LP82Yh6QCJksP-A6DzG-mgxyUPAio2IOmNvIPdh2AHuFnLGs0sKmqPPeuchrQbuQPC90tZFj_zrVriYaWVjfIHAPpH8uCUqqRRNSefN3jCWUoS0LiE-D2ECufq1pu6p2KqAepe-eTNmc8BRt3HABYLnIMjhQMdLLlbwkRJ0fgv3ge4HhccRXPZIBoYz_-X65qfoYO0DYKK5jxEemSMrmduQMHwdhLcdiawJB8kmCJ3qUv4lSsCb1mZ3WsaLmiMPXzCdNcocceiW22LRJkpy2AFtFxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9086b036.mp4?token=dL93C0WsNrHAqJZf3ORewKhl4m-blSltjfGohqz9h0EsWrdZvW_3SYLpqSx7LP82Yh6QCJksP-A6DzG-mgxyUPAio2IOmNvIPdh2AHuFnLGs0sKmqPPeuchrQbuQPC90tZFj_zrVriYaWVjfIHAPpH8uCUqqRRNSefN3jCWUoS0LiE-D2ECufq1pu6p2KqAepe-eTNmc8BRt3HABYLnIMjhQMdLLlbwkRJ0fgv3ge4HhccRXPZIBoYz_-X65qfoYO0DYKK5jxEemSMrmduQMHwdhLcdiawJB8kmCJ3qUv4lSsCb1mZ3WsaLmiMPXzCdNcocceiW22LRJkpy2AFtFxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لحظة انفجار طائرة بدون طيار تابعة لحزب الله داخل قاعدة عسكرية للجيش الإسرائيلي قرب بيت هلل.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76531" target="_blank">📅 19:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76530">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=TXvuF5BhBVdnKIVBFx4Qd5RVFIdEKX6dO4zdpJh34X-FlujQ7qXzi0y3rGBSNwXy26KoetiOck7BsE-PcmrdrMm7HnyAE1ncs9tgHM09WnNSjvA_8zW_XNGeYpRdGkcQwuzCNuFOGSAq9rOFp9feFTtfYbgi8fqUsSjCaCXH0dNEQDKiEoJ--LpfuG77qDSrCr7RhZQIk5T7OI7Fr51xMVYk4n-dgJOIW4aLNNj110Lxl5lK1NimpeqAU2xTpzgwy0eslMp-Y7ur2P3dD-d1YH-IgURCeR-AhRs4cmdc6HFtmY-EtSGu17O79W3_mLDaM5AJuK9KPNqq568wmmcZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70850c8c7e.mp4?token=TXvuF5BhBVdnKIVBFx4Qd5RVFIdEKX6dO4zdpJh34X-FlujQ7qXzi0y3rGBSNwXy26KoetiOck7BsE-PcmrdrMm7HnyAE1ncs9tgHM09WnNSjvA_8zW_XNGeYpRdGkcQwuzCNuFOGSAq9rOFp9feFTtfYbgi8fqUsSjCaCXH0dNEQDKiEoJ--LpfuG77qDSrCr7RhZQIk5T7OI7Fr51xMVYk4n-dgJOIW4aLNNj110Lxl5lK1NimpeqAU2xTpzgwy0eslMp-Y7ur2P3dD-d1YH-IgURCeR-AhRs4cmdc6HFtmY-EtSGu17O79W3_mLDaM5AJuK9KPNqq568wmmcZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  6 اصابات في صفوف الصهاينة 3 منهم بحالة خطيرة جراء استهداف بطائرة مسيرة انقضاضية ؛ ومروحيات جيش الإحتلال تجري عمليات إخلاء.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76530" target="_blank">📅 18:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76529">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McrVMv9ByI4qX0CHTASq6txP0lDVAsJonHJGhwBDxgHzE39BxfNNQLBzylR2cdL63jchpBmi8RL7W7lneKxVs3BHxhSzIYUXWvJuDnzfznhgETM758PXHw5Cizck_-gN91FrJeI6pKhZeL1-T8uuaXS6xH_KZfOS6OnNJdUrnuWYpmUUYDj00pCnlZFJm48PsCS22N-TyLmCc0XaDQKXXyU2bTtKLd27qs_YhxhWan4waIjD8yoPvOCdRx_OVzhKn2QLLyLEQ_bQx9Xho7dT0VsatyDDrAx2mTAsdANDmFixMrNq8Ra3s2D6MPWTgU3NN7vTRmm9xatPYBcizFY_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
تشير تقديرات الاستخبارات الأمريكية إلى أن تنظيم داعش من المرجح أن يستغل هروب وإطلاق سراح آلاف المعتقلين والمنتسبين إليه من السجون والمخيمات في سوريا لإعادة بناء صفوفه، وتوسيع شبكات الدعم، وجمع الأموال. كما يشير تقرير أمريكي مُقدّم إلى الكونغرس إلى تقييم مفاده أن داعش في سوريا من بين الفروع الأكثر ترجيحًا للتخطيط لهجمات إرهابية خارجية. وتُقدّر الأمم المتحدة أن نحو 3000 مقاتل من داعش ما زالوا نشطين في سوريا والعراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76529" target="_blank">📅 18:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76528">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFJnKzXne1tlWSAq6lReFBPY4mVJECsR6BnST316HRqu135mvhQQrJQRu_jg4INJewsG-H_JSZc2foBeurooAIuxnuAa-zIUtUaZb_ksuHC-X2s8jA0i8oDCm4ttGBdLSNet5VgxFVkhFgDZ1AmrL6EKXZGSiKLGxzjVBE04YbHtJTBrQTmWcGDTLakbri4xOUAZlr_RZhjVPDDLakr3O6DRpSqYoTf7KNpPu1jp6GGR7YwQHAgbNscpGvtHd00W6m9ryUoLZbM4F9b_AnEDJnMAlUVOonuKQmmzy3K2-K9SSia6QZCwDBbfYJUSqyFJwtaxZwBaZmfOl9ZKXkl10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: سقوط إصابات في بيت هلل عقب انفجار طائرة بدون طيار.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76528" target="_blank">📅 18:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76527">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
سقوط إصابات في بيت هلل عقب انفجار طائرة بدون طيار.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76527" target="_blank">📅 18:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76526">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية من قبل حزب الله نحو صفد المحتلة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76526" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
🇮🇷
مسؤولين أمريكيين:
ترمب أعرب عن قلقه بشأن حجم المكاسب المالية التي قد تحصل عليها إيران في إطار الاتفاق.
‏إيران لم ترد بعد على تعديلات طلبها ترمب في مذكرة التفاهم.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76525" target="_blank">📅 18:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnNA33FPT_uQXp-ucvAmZjAUW9DflCLZGzcHYQTBLMFe-b_vo-GjZHXhdPiZBq1UBCmaZCKzFa9pj0DZkYMnRTokvw-og8TUlAetGlNfkKx0y0uUgL0LA10QZnXtOEFR1bl5t-2xD2JToazImFurFVcBUMEQn4mJO76NoVZ_thZ60VjdZ-pRxleppajUPAAfLDiLTG7rMqX4vmiMlTB1z-LoZF6BxFsFIfi35d4bWekltH4nn-8FJgQgF3eIrs-GKBiM7RXGDeHCYfLdEn3eTQ6Ij50gCdvDt8PpINh7TlnIu7oMqhK_D-83iYJzFMW6HqBMKkJtTRjBunM4VxCv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
ترامب يعلن تعيين توم باراك مبعوث خاص الى العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76523" target="_blank">📅 17:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG0RtmpL77xuqrARFDD840eYWpJ8wdodsNJWpAqzfKxRdryC4OxwoQKbFqlhnVMjP011oMoNWpclwq5XIfn4SVbnf1OW-ECCjHzY7MEW1gsORnU2zhwcAyYIglrCfHjfJO4PupQ_hENeKnI7wbMyhS09tR628O3e_vEJmjc3GWHvHydnTPUX3q_EA4C3tVnzP8AuT_dTnjl1xGc2TqJNXwt0o6BWPBzwU4Tijp9uei4lm10Th7cBcnNxhqw4YdB7d5YpRv9UDfXqaWgrBhgKtFPfMBLvxLDA3ZxwmPBnywj5077P8XMKIaisuGYkzYk74VjL--cxiznevEANzKY1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ حزب الله في الشمال الفلسطيني المحتل وتصاعد أعمدة الدخان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76522" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449c4c4755.mp4?token=gLAxL25j553WN5HseIhN_9dcCo2kMHl0bxggeen17S_sKMj-JSs9sGjG2zmi9gdI572XpWHfEMrs5Fj8iFbT99P_Q0UfoPyDS0uOnxh-PW5n98ZyprfAE7rMyCNnv-OwI_M_OypVGpb50W4D6wfF13Tg5wv0jTVW_6Oaenrq13LuJvI6JJLK_II61jqaf3fi3SvHNDPYZfki3Rfqd-CBjF_nKQhtyBWNcuDLTJll-BAOkC0o-fw0bKxiDnEtSQzGTkaSEduHj1DSMYDcGa_VTIA5AqthjV9xtxzcLqxgG42LXCJFZb5OpHtWh7OZ-jvTUlg6gwqcPK7qprCd32noez5Vz_477GxOVe3zj48Sr5wJZOctvl2Hn1tcPxdiX1EMsf9XEKx2RaLdCK_Udwn8McPVYOtSQLz9oPpe2yd06XawTSBYJbrUgvSR6T__NadzpOAJNKofusCVDYDQ8yqqDOCzlCKOiYxA_4gJ5L-7ngkBRXNbX720CtyoslP-ynRoc4QBaZW86Yi3ScZ0MWhk6YstzFLSdxHbnw6LWCwJifX2_Dcnutkmr9i_0J-tHh9-NQG_6H6OPlEc50xJYT70Uh5WLuFYjw54GOddP4Rfi_cOWI36XHijpLGlMnInZoPOSkgFQfNDE3WQxtMGKiPEnN6ZQM-8jnemfQI3S5zb5pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449c4c4755.mp4?token=gLAxL25j553WN5HseIhN_9dcCo2kMHl0bxggeen17S_sKMj-JSs9sGjG2zmi9gdI572XpWHfEMrs5Fj8iFbT99P_Q0UfoPyDS0uOnxh-PW5n98ZyprfAE7rMyCNnv-OwI_M_OypVGpb50W4D6wfF13Tg5wv0jTVW_6Oaenrq13LuJvI6JJLK_II61jqaf3fi3SvHNDPYZfki3Rfqd-CBjF_nKQhtyBWNcuDLTJll-BAOkC0o-fw0bKxiDnEtSQzGTkaSEduHj1DSMYDcGa_VTIA5AqthjV9xtxzcLqxgG42LXCJFZb5OpHtWh7OZ-jvTUlg6gwqcPK7qprCd32noez5Vz_477GxOVe3zj48Sr5wJZOctvl2Hn1tcPxdiX1EMsf9XEKx2RaLdCK_Udwn8McPVYOtSQLz9oPpe2yd06XawTSBYJbrUgvSR6T__NadzpOAJNKofusCVDYDQ8yqqDOCzlCKOiYxA_4gJ5L-7ngkBRXNbX720CtyoslP-ynRoc4QBaZW86Yi3ScZ0MWhk6YstzFLSdxHbnw6LWCwJifX2_Dcnutkmr9i_0J-tHh9-NQG_6H6OPlEc50xJYT70Uh5WLuFYjw54GOddP4Rfi_cOWI36XHijpLGlMnInZoPOSkgFQfNDE3WQxtMGKiPEnN6ZQM-8jnemfQI3S5zb5pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
آلية تابعة لجيش العدو الإسرائيلي في معسكر غابات الجليل شمال فلسطين المحتلّة بمحلّقة أبابيل الانقضاضية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76521" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
