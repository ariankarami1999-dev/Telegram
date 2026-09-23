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
<img src="https://cdn4.telesco.pe/file/lsya6yL8n8co6Az2uGlWP48M9GVxSIr7rgeAB56H-qdUfWeRAsYOjZirgNEwULNqc731Lb0goyscV-_zBxx5IKqXYxIUluEqbum08o_9ZlKnpMxiFxuA_3Mh0lPe3YnwajZedLteIGVVV-pLxYnVIPWQd1PRHsNCw2zSS4tH9WHflKztVKLDbwIkEjTWDga7nwEIGzvx0vM8_Gj4tdNn0Hazrx7AFeAQPHItnxui_SmIBq8LltxFJZAFvHpNXEx8_BmdiM7sXhuXAcPeJC9X8Px3i2RZLG66I3pug5nM9XfIqpGVg4sapqnM7CgzmYzHmnkBgLc-oeCHjnuIH7RyMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 01:53:59</div>
<hr>

<div class="tg-post" id="msg-91409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/503e190498.mp4?token=BzQZbHBLN4qjIfhT42tp6YdtqVGBtlgvF2d5BOoy4fYSXEqWGc2mFqSk4J6ohI2GW-Yi_ePfNbIa9nRhZDMYKkdG549MIv3es3hULXa2cqGv8WPU8BDvzlG5YIHlLImKitZOQ5y_gOu_d8eUtmB0fU7M0BNMFxUOdMMRii5v2QiA8S7fCC3fjrGs6xsphEkj30tw8hwHoh9w7LV1RC4TLHC_MG3Uc32r63KwDe6wq9a_MCDzPNFD-Jdp4vkOnNN0faVUA7vE9xntAic-nSALj3umPfvY0LK7odc4_fmVgehNdb9NdJ9DAl6S8bY9-QRog6cY7XIocU-6RMdvTrnHc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/503e190498.mp4?token=BzQZbHBLN4qjIfhT42tp6YdtqVGBtlgvF2d5BOoy4fYSXEqWGc2mFqSk4J6ohI2GW-Yi_ePfNbIa9nRhZDMYKkdG549MIv3es3hULXa2cqGv8WPU8BDvzlG5YIHlLImKitZOQ5y_gOu_d8eUtmB0fU7M0BNMFxUOdMMRii5v2QiA8S7fCC3fjrGs6xsphEkj30tw8hwHoh9w7LV1RC4TLHC_MG3Uc32r63KwDe6wq9a_MCDzPNFD-Jdp4vkOnNN0faVUA7vE9xntAic-nSALj3umPfvY0LK7odc4_fmVgehNdb9NdJ9DAl6S8bY9-QRog6cY7XIocU-6RMdvTrnHc4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
السفينة التي تم استهدافها صباح اليوم من قبل الحرس الثوري بسبب مخالفتها قوانين العبور في المضيق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/naya_foriraq/91409" target="_blank">📅 01:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇨🇳
‏
ترامب يستقبل الرئيس الصيني بمراسم رسمية في قاعدة أندروز الجوية.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/naya_foriraq/91408" target="_blank">📅 01:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a40a23d1.mp4?token=jP3feDfByDf1GlwkeO7Yu_jalL7xAJP-FRqjEwX7_6s0jsaUKpbZ7slWkLj8DodGCWXUgYF2oCwfo5COELxd1lav46Zc_LhubVefBtILT-ktOnJXE9KdRRSSG8EuAGsQUjnPqXlLLI0DAe8fuLmqCLq1CLJ3D2qaCBaFr6oOHr_OyjEEWUWoTxNaRYm17c658L5kaoTY7l28CMgpZrXYtYGBW2MAfCVNW5mMb_gcNCz4gwNXWu83-DMX_UKKulqWA2iL3CQ76OU8megNSexSNCEf3V4H4reSCurO1eX4-XCbh60RBfQ7g5pcBTcGzRr2I6WqFVhjT7PKi7b_nR8X4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a40a23d1.mp4?token=jP3feDfByDf1GlwkeO7Yu_jalL7xAJP-FRqjEwX7_6s0jsaUKpbZ7slWkLj8DodGCWXUgYF2oCwfo5COELxd1lav46Zc_LhubVefBtILT-ktOnJXE9KdRRSSG8EuAGsQUjnPqXlLLI0DAe8fuLmqCLq1CLJ3D2qaCBaFr6oOHr_OyjEEWUWoTxNaRYm17c658L5kaoTY7l28CMgpZrXYtYGBW2MAfCVNW5mMb_gcNCz4gwNXWu83-DMX_UKKulqWA2iL3CQ76OU8megNSexSNCEf3V4H4reSCurO1eX4-XCbh60RBfQ7g5pcBTcGzRr2I6WqFVhjT7PKi7b_nR8X4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ظهور جسم مجهول انفجر قبل لحظات فوق سماء وسط وجنوب العراق.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/91407" target="_blank">📅 01:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الصين تحتجز قطعًا حساسة من طائرات الـ F-35 تم تحويلها إلى هونغ كونغ.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91406" target="_blank">📅 23:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91405" target="_blank">📅 23:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91404">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxv9EDY7vwNbgm8ZU7TideMBNsma-_xn1IxOu1QjEoZYzHsBqIVhlUaoBM7VdSrQdGKgTg7xXjKoRLa835oMm3tbcGeT6eOzLeomOrZTwkiAxkslzJNn4EsUJfLdM69_msu606ZMzkEg07-sZByDHpq1mL4OnemLzAVjh4k0rq4R4eUqQOisBaja8uXsS3FYj7yOw5e8pdleZuwlvU0dv1rciiuTM7s7TDxffPnmPxvLk1anGTsdCdxrzmO-dbEeIJcuWwnYDtHwDW_N0yYqyGx5PMGP2Qvpbuz6n5NK_HH0XJt0AnP3vQjDEDb2qQvRgDHE9kv9GpBCAQ5VoWIKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇮🇷
اطلاق صاروخي من باكستان شوهدت من ايران وباكستان وانباء تتحدث عن نجاح عملية الاطلاق.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91404" target="_blank">📅 23:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91403">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
انسحاب النائب العراقي ياسر وتوت من تحالف الاعمار والتنمية وانضمامه لكتلة ثابتون.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91403" target="_blank">📅 23:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91402">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDWSn0gRAcjJaw1QYP3sWXu2FYFkXr_fIk-j7nb8ltxv4ZReSElWsr_25RBdSvvR7qhLj88_mpzf0-eMOrm8hJIqgq-yomHO4MhGmXtwnWco3tugc9AYj0B7comQZi0MZF4_VS2AgTP2mgK2bbuk6Iwyhz9gUFnqmAt5qJ3QraRKNu0C-BIHrbZjga3ZQhnLXDe0zdDZwxgIFXDqJXxeQuEU4u9r_8w6L818ZttJu2N61z8uI86BmaBfb9Zy2Yl-zN5Okz9jL5Za9u1Z5scIXzn4UiaFzPF4z-goHlXgLPuipxs5MAfwnJ5PZLA1P--I3kWG0kRSYbnEGEdP8ul9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري الإسلامي
اليوم، في قلب النظام المتعجرف، أعاد رئيسنا إنتاج رسالة القوة والفخر والكرامة والأمل لأمة صورت على مدى سبعة أشهر جبلاً من السلطة في ذروة القمع أمام أعين شعوب العالم.
بالاعتماد على هذه الوحدة، بدءًا من أعلى سلطة تنفيذية في البلاد وصولًا إلى المحاربين الشجعان في الميدان والناس في الشوارع، سنحبط العدو ونجعل مستقبلنا أفضل من الماضي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91402" target="_blank">📅 23:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91401">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
عكس خطاب ترامب في الأمم المتحدة الموقف السياسي غير المستقر الذي هو عليه.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91401" target="_blank">📅 22:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91400">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇹🇷
‏
بيان عراقي تركي:
تركيا ستسلم "تدريجياً " للحكومة العراقية معسكر بعشيقة - زليكان، و الاتفاق على إنهاء وجود العناصر الأجنبية المسلحة المحظورة في سنجار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91400" target="_blank">📅 22:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdBOkgg8MFrN7uz28a2kCfzmpsJJFfyZCoJshQoUJgH_kSAduszj19573VKY9PEPsn2FhzyRvptTyP-eSrqJE6HEcNvAfgKyTPzOsbp0hE2Myi00AgkXXxUmHJWRryrjWLqHtz8XvLMFKFv7v3Tezs0sPE0JqO5gkrBJCxU18NWbOFxdhgbyVgV0tJRWCK5RsW4Dbba2t2binlCZl1rHUBZT5LuGAiD3i8Lh9EH-Nz2RmQ7iEXLC_1Tnnru5A4BICA82Ef0Xye0yxcUcwT5dd4RNDQyLUV2YkmaKieb9LXbxTpFnlTl_JQOYz7r2dc432H360B1nJEW35JwkIHaeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط ترتفع لتصل الى 103 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91399" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91398">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87ad81d2a.mp4?token=EOF62F-JfrSbqRey5Qi-fuNyau-1b4BfQs86ePDE2QXlNWRig-_uzWpheMhJv1gwc_-Tke635Lm5O3PnAlSfYXWq37Tp2B0u2HkehAjZbZlPYC2Tm18I1I2OBQlpdIUVa4swHM3CzGbi5kK0d1jAXWyksWNEsNhWdhmFWF5Cyus08mSMxgVS309a7fEL9TUX29FIGNSarMjMlbGjrfC7GZeiNPw6YLHko5vuma-D1LESePzbes5nMrUouL5jzZTgmMsek1KZBJnRf2TrshtjGB_AgklAbdH83IEFZol8MUp93htmqZw31OcD8TyWH_C9iPuEiROejDQpiC_oWAd7Lb42851tScYbU1A1S_vL-n3l9XTJt6qSut_DzWqvs-RH6hE-uFY-n4Ey_hFD6uBo_M6UhzjflscwLd3q07w-H4U7YME07zUlvFTqHeRivfIk_nb3ZwfhPBZR9Iml7Rm1u4a3RMfLDnFgrYT07_VG07VFAY1XjaAStlou2xXs6zhQ5TZbLBgFN-W4L7cHyJ70kDKTFY0kYYTGDNlyBFXvYDgFG-azh4ZLji9ckf_-vHMmpgM719Kn_vGBEEeHsrXpoXi_t77NUXC62v2Vsd9P8Xr7jvY6BXh2YZFTnIKVKiDAdaFnAEVITmB10fEiulDpZpDvJRwfPc7zQ3fCgFLYsg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87ad81d2a.mp4?token=EOF62F-JfrSbqRey5Qi-fuNyau-1b4BfQs86ePDE2QXlNWRig-_uzWpheMhJv1gwc_-Tke635Lm5O3PnAlSfYXWq37Tp2B0u2HkehAjZbZlPYC2Tm18I1I2OBQlpdIUVa4swHM3CzGbi5kK0d1jAXWyksWNEsNhWdhmFWF5Cyus08mSMxgVS309a7fEL9TUX29FIGNSarMjMlbGjrfC7GZeiNPw6YLHko5vuma-D1LESePzbes5nMrUouL5jzZTgmMsek1KZBJnRf2TrshtjGB_AgklAbdH83IEFZol8MUp93htmqZw31OcD8TyWH_C9iPuEiROejDQpiC_oWAd7Lb42851tScYbU1A1S_vL-n3l9XTJt6qSut_DzWqvs-RH6hE-uFY-n4Ey_hFD6uBo_M6UhzjflscwLd3q07w-H4U7YME07zUlvFTqHeRivfIk_nb3ZwfhPBZR9Iml7Rm1u4a3RMfLDnFgrYT07_VG07VFAY1XjaAStlou2xXs6zhQ5TZbLBgFN-W4L7cHyJ70kDKTFY0kYYTGDNlyBFXvYDgFG-azh4ZLji9ckf_-vHMmpgM719Kn_vGBEEeHsrXpoXi_t77NUXC62v2Vsd9P8Xr7jvY6BXh2YZFTnIKVKiDAdaFnAEVITmB10fEiulDpZpDvJRwfPc7zQ3fCgFLYsg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي
: بعملية نوعية كبرى، إلقاء القبض على تاجر دولي بارز للمخدرات على الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91398" target="_blank">📅 21:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91397">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
البيت الأبيض يضع خطة لحظر تصدير الديزل لمدة 90 يومًا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91397" target="_blank">📅 20:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91396">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10fa15f285.mp4?token=KXS-scJfUKHfBOIjrtEUoTqO-wMSgUUv0g4sgAg3vVyoYKgIm2jp6gOObsM9qcjbVjz-ViyNKYLZ4MZXqdLg4IVgPkEQ5YbFlB3jmcCw75tS5VdCY8U1VKRakZc5x7YhwmdHYyMmjISR5lvALOXAf3f0aIjThWewiyzsz5cDKsZMiJes4fhvo9UaIew8fbh1BmsTalhQgL15X5pWcPzHGgjCVcz3SX021dB8do4FEQRajkBAkZLI2_E5X857o4UUYWK6ii2oPVGv0dV_cLUOfymPut_qgNdyjoRfX6zmzxCoSI4ul5ZtxefYHnJTT_lnqc5bx8sLd_mxrsnN_lO7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10fa15f285.mp4?token=KXS-scJfUKHfBOIjrtEUoTqO-wMSgUUv0g4sgAg3vVyoYKgIm2jp6gOObsM9qcjbVjz-ViyNKYLZ4MZXqdLg4IVgPkEQ5YbFlB3jmcCw75tS5VdCY8U1VKRakZc5x7YhwmdHYyMmjISR5lvALOXAf3f0aIjThWewiyzsz5cDKsZMiJes4fhvo9UaIew8fbh1BmsTalhQgL15X5pWcPzHGgjCVcz3SX021dB8do4FEQRajkBAkZLI2_E5X857o4UUYWK6ii2oPVGv0dV_cLUOfymPut_qgNdyjoRfX6zmzxCoSI4ul5ZtxefYHnJTT_lnqc5bx8sLd_mxrsnN_lO7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
في وقت يعاني فيه العراق من أزمة تصحّر وتُقام عشرات حملات التشجير
... شاحنات تركية تدخل إلى عمق الأراضي العراقية في محافظة دهوك، وتقوم بقطع الأشجار وتحميلها حطبًا ثم تعود أدراجها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91396" target="_blank">📅 20:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91395">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 52 غارةً جويةً وصاروخاً من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي انطلق من جيزان، استهدفت محافظات الحديدة وتعز والبيضاء ومأرب وصعدة وخلفت شهداء وجرحى بينهم نساء وأطفال ودماراً في المنشآت المدنية من شبكات اتصالات ومدارس وجسور وطرقات وغيرها.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا العزيز 988 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91395" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91394">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه: الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.  والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟ https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91394" target="_blank">📅 19:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91393">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
السفينة التي تم استهدافها صباح اليوم من قبل الحرس الثوري بسبب مخالفتها قوانين العبور في المضيق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91393" target="_blank">📅 19:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91392">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
القوات الامنية العراقية تبطل مفعول عبوة ناسفة في ناحية الرشاد بمحافظة كركوك شمالي العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91392" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f03f1569.mp4?token=S2y-Y_ZqbjpJ0QFpd_a6dv0OkaeYHy0hKzqIJKB5i7Xn6TrTRFlQoptTV5Voga3obDN4guNIMwB9393z11atuT9axd6o0nvH69GkA4yhCJm3Nd4pmJqCFccJ15IA0Y8mQ4Jgs27M3qMr3yGyQrqLi1yMxZSQBYdAxOAR-E-ugvXUba4wqDcOQE3LRkT8GyN7OsaMnYWQhJEB3ydGNt_f7UeMv_VAnXFsEf-M4Y2LY9ClcV6_i4chIzKhYLsmxT1_4PReoMgWuGsT0rDo6dJrjY8QnchJ0dj_CluyGdYmqo-NCu-aDfq1kpaIP3V7rsN-MCDBP8LdlGpAmHTT9Vey_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f03f1569.mp4?token=S2y-Y_ZqbjpJ0QFpd_a6dv0OkaeYHy0hKzqIJKB5i7Xn6TrTRFlQoptTV5Voga3obDN4guNIMwB9393z11atuT9axd6o0nvH69GkA4yhCJm3Nd4pmJqCFccJ15IA0Y8mQ4Jgs27M3qMr3yGyQrqLi1yMxZSQBYdAxOAR-E-ugvXUba4wqDcOQE3LRkT8GyN7OsaMnYWQhJEB3ydGNt_f7UeMv_VAnXFsEf-M4Y2LY9ClcV6_i4chIzKhYLsmxT1_4PReoMgWuGsT0rDo6dJrjY8QnchJ0dj_CluyGdYmqo-NCu-aDfq1kpaIP3V7rsN-MCDBP8LdlGpAmHTT9Vey_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
المتحدث باسم الوكالة الذرية في ايران يرد على ترامب:
الوكالة لديها إمكانية الوصول إلى جميع منشآتنا
"إسلامي"، رئيس منظمة الطاقة الذرية:
على الرغم من عمليات التفتيش المتعددة التي أجرتها الوكالة، لم يتم تسجيل أي تقرير عدم امتثال. الوكالة لديها إمكانية الوصول إلى جميع المنشآت. إنهم لا يصدقون هذه الحقيقة لأن هدفهم هو إيقاف تقدمنا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91390" target="_blank">📅 19:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ievuvl_QhVkBEktMgNvniaqi3Y6-GD1-bo3MEhOGtZ6IK05P-0ACYWzU3DtIrLpydJLwHinvMhrsUGgFSHHloewr5531Dujt8bVRac-cWXIKE4V7QKoVOGOtlheCXOnZ9erriANTX4NQ3gqvMyT3q8_3vnauUiecDWiH6uVvoZhLVWzeFMNpnvygwMkXcxuKWUQ5LQCAiiUWz63kUdcWJiNuGeOT1Q7PMBDstodrdeDd2lttzqAiJgt-OiR6h6pzaiLQmgzlqoahZOH9t5ZzKB8ijkbobnLZhyffZkH3YB2Fm4MiizK_3xQsX05X9jszQg3dewEXu6PqYJxnKKuRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDF4P4Wp0ub4I6FNG0NBoPFovooOa6dtdWsGBnbtxTCrpV9bmz864771JGTt_GIEa58vwwY99L36fFDjoYczFBgrYkyaf8_0i17gjgWRYAqqKHYQSr0dxM5vd9xvD8w23MDa6nXWYLz2UTOjr00pF9GyHjUN_exxx82sWMBAcOoI9knZ7HQIbQ9C3LYkq6RoEOaI5kp4ZTA9oZG89NFvjRMf4QLa_-73f2wbUs2Bg_Wf_Cwf8WVtO_EfSPLxVkxr_W2G-aWmZ-yPPSVIM8x2I_8ckp75cJEx5KqoOtT8hoxnUDBmzvwtLwx1DimDeeyJUKutLHxjiCcqeeqO1PMSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmlYA__I9TxHrpe-IsCuomeHuDohwXBBV9npjLxcvYXH4l0kmK8euL6wi2E6xNlcx2OXkFbPBbek4qlre5EMEfrR5fvvhJCDkGFC6zjWV1HMLGDGHTVEPB55qghBUpcv1AGnQ-DcvNj7Y8q-EQNE6aH5BUJHKbE7vb7fHqIgjNCbv1wHYdOcosdiOJUIbCpLlfGGva-8_BAHFBoVsfaXGSeA6bkQodw7m1GRn6Z8rbaVzr8e4EzBT4fu50sGGgRFcnRPCmbyg1QJ-3hvjdHD1aEiRM-HjRuNNauwNrNAOxG4F96my7NetBL0WAxaiUVbFu-spH5UlLT56FN66Vt8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9Fx40vXANmxG__ali5uhHDMc26L6p9sRo9iwcSjefGByBB6p-PnV7rb_TzQCi1iB0QEDK1YgUuIh_eLIEDLGgfKmPRbeK_Vw-JOrqXYIATjszUXcoOIKCSkOLi4m8BO8eEL9eQuU-lrXP_b62xA9AaS80gsGPNB2dgZGgVdpupzvyx_-u78Cs8_eQ9ytP5aKUZk76OVTyzRcVKLJ__eMT3yClWhm2HRHPUdeCIPZRpMkSIKYkJitBP1hcXDacWsalIVSljcU3OFc2U0G4sVXSDZOxp6rG_5U9UKGvaV8p_eCcqBGWh4WtEgQk7BtorUAErl77n0OQO1QZkJ6CT0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الاسرائيلي
يعثر على اسلحة في عمق الاراضي السورية.
قلت له اعطي نيوجيرسي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91386" target="_blank">📅 19:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636d677358.mp4?token=nA2JNQqpx_T8O8ob0avXoa9lI397fWlye6iCVjrjEzRKDQR-IlrW-5ovAfjSG-XTaAgYxwv6NWWQpt6zaI6xlDA7mK5BfRe5nAxFtifqqicv2MqFmL3NmyXmE9CjhxIcQnKyOyMnJt3E5zg1YCKzhRUeIXIQUiY3i_dUj7ZG9gf0nn3vdUt0H5hafV1d7Q47EMy6SEBHckOxqP40XWG16_S4XTJrFaW8WvdXcYdEHle_oY7Tfb4SDVo27pjaG5gCEfMzKxcODcvRkRvx9Buoajt4by1mAqCtzmWk4V2TTfN5vT7VUpxhRqOXE6KPX9iB-zuWwenE-_Q1uZ8snsJlMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636d677358.mp4?token=nA2JNQqpx_T8O8ob0avXoa9lI397fWlye6iCVjrjEzRKDQR-IlrW-5ovAfjSG-XTaAgYxwv6NWWQpt6zaI6xlDA7mK5BfRe5nAxFtifqqicv2MqFmL3NmyXmE9CjhxIcQnKyOyMnJt3E5zg1YCKzhRUeIXIQUiY3i_dUj7ZG9gf0nn3vdUt0H5hafV1d7Q47EMy6SEBHckOxqP40XWG16_S4XTJrFaW8WvdXcYdEHle_oY7Tfb4SDVo27pjaG5gCEfMzKxcODcvRkRvx9Buoajt4by1mAqCtzmWk4V2TTfN5vT7VUpxhRqOXE6KPX9iB-zuWwenE-_Q1uZ8snsJlMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هيئة عمليات التجارة البريطانية: مسؤول أمن إحدى الشركات التابعة لسفينة شحن افاد بتعرضها لإطلاق قذيفة مجهولة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91385" target="_blank">📅 18:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزير الخارجية الامريكي روبيو:
اجتماعنا مع الايرانيين كان إيجابيًا، ولكنه لم يحقق اختراقًا.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91384" target="_blank">📅 18:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
مسؤول إيراني رفيع المستوى: طهران تدرس رد الولايات المتحدة على اقتراحها لإنهاء العداء.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91383" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ‏روبيو:
يجب نزع سلاح الميليشيات العراقية لتفادي "بلقنة" العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91382" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏روبيو: الحوثيون هاجموا مقرات دبلوماسية.. إنهم قوة شريرة بالمنطقة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91381" target="_blank">📅 18:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
مسؤول إيراني رفيع المستوى:
طهران تدرس رد الولايات المتحدة على اقتراحها لإنهاء العداء.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91380" target="_blank">📅 18:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي: سنفي بالتزاماتنا الواردة في اتفاقية الدفاع مع السعودية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91379" target="_blank">📅 18:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
سنفي بالتزاماتنا الواردة في اتفاقية الدفاع مع السعودية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91378" target="_blank">📅 18:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🔻
هدف عراقي اول في مرمى سلطنة عمان ضمن منافسات خليجي 27</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91377" target="_blank">📅 18:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c54bff4fb.mp4?token=XVvpQfVyCs9R3xgojs2YWn4s4O2TkYehoPan6tDK3NrIq7ugeZ9FXiY91jpKEAEnDoMCl6jDgSHch08n6hKwrl5kKUYmwnW6gvhsvIJXefRIWKDm76UEKaUZqrYHTMxCf0pddJHJhKThT0OVw5VrFYaFLVPRygmDIaDsSg5Xn4_EKYnCghCjgXS-P0Za3HdZm5CBD4PMvR_zTOqSqdtsZ2Vt2MP9pT7GQU27zBOwkZWB80fCMxBBFPlBF4mg_1C6iOmROoQrz9R_ccymXuQ6YqGuzjAgJfO-OHb31eO6QSMJXB2xAanNSTHeH37W1C8oZ8FRC_oggm0Ky667wRieckMvsQtF4NHPYEszEZpbaogFOjT4Um4Ddvnn52Yj2h8W49kdd6eK0R0Eq8RUnFlGx3XyQL9qpUK7-dwI5GjGd5kd2iKEvrASE-OlCy3KxB9tBTW5EOsO6KAIGb_8SqVmFYyR8hRWqX8y1h6Y3QzT55OlHXyVarobrEGCMpADHNDkef1bnpRKqOJX_SbkcPJCJBtzfu-QHuLO436yQy5UWbMPVOyGcn-FudSSyMm3_9nOmcJCQv9Y7848c3P0evS5C-e1CDKzDF98gQqqSLEKHy5VFBlzqloyfemuGHfpOkcVNRbRa7F3PNtypst3maJgxHtE3fbRRdjJQtvG5mQppkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c54bff4fb.mp4?token=XVvpQfVyCs9R3xgojs2YWn4s4O2TkYehoPan6tDK3NrIq7ugeZ9FXiY91jpKEAEnDoMCl6jDgSHch08n6hKwrl5kKUYmwnW6gvhsvIJXefRIWKDm76UEKaUZqrYHTMxCf0pddJHJhKThT0OVw5VrFYaFLVPRygmDIaDsSg5Xn4_EKYnCghCjgXS-P0Za3HdZm5CBD4PMvR_zTOqSqdtsZ2Vt2MP9pT7GQU27zBOwkZWB80fCMxBBFPlBF4mg_1C6iOmROoQrz9R_ccymXuQ6YqGuzjAgJfO-OHb31eO6QSMJXB2xAanNSTHeH37W1C8oZ8FRC_oggm0Ky667wRieckMvsQtF4NHPYEszEZpbaogFOjT4Um4Ddvnn52Yj2h8W49kdd6eK0R0Eq8RUnFlGx3XyQL9qpUK7-dwI5GjGd5kd2iKEvrASE-OlCy3KxB9tBTW5EOsO6KAIGb_8SqVmFYyR8hRWqX8y1h6Y3QzT55OlHXyVarobrEGCMpADHNDkef1bnpRKqOJX_SbkcPJCJBtzfu-QHuLO436yQy5UWbMPVOyGcn-FudSSyMm3_9nOmcJCQv9Y7848c3P0evS5C-e1CDKzDF98gQqqSLEKHy5VFBlzqloyfemuGHfpOkcVNRbRa7F3PNtypst3maJgxHtE3fbRRdjJQtvG5mQppkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بزشكيان:  الأسلحة الذرية والصواريخ النووية موجودة في يد النظام الإسرائيلي، ولكن يُطلب من المفتشين الحضور إلى إيران. إسرائيل قتلت بوحشية أكثر من 70 ألف مدني في غزة، بينما إيران، على الرغم من وجودها في طاولة المفاوضات، تعرضت للقصف. إسرائيل تمتلك القنابل،…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91376" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يرفع صورة قائد الثورة الشهيد في مبنى الامم المتحدة بنيويورك خلال كلمته</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91375" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي روبيو:
إيران أطلقت النار على سفن تجارية هذا الصباح.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91374" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe-2IqAppC7nMeIwraa0wzFymQDTsW4r2R9bpfCNzl5BpLJOoOmb7pR2coNAOWxa_uTh-W-LBTUd0k5N9oB1qwhHA9pMpD4OqFykRG--d0Ni9tKveOyTpghRcDxbcn7MEdOCbu3Y_0CirkmEd7RcCWlVOuK-0_owNb1GCymsm-BsCHkpJjAQIqRtnRgqor_d9W9J26Nk_ydEh9SF504luuPUy61X3Dn5jGW0bWvxlLs4ocFaiC25sgRgJGQvnUjDIYbD-rNZWW74FJ9mDlg3SV0ChfvQwcV54rj7N9JdWWVeg-k6GF66LtITZO4R06AIGzTLGjglO_XPl0csQxQm8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزشكيان: إسرائيل تستهدف أي حي في أي مدينة وفي أي محافظة، وتقوم بعمليات اغتيال مثل الإرهابيين الحقيقيين. وفي غزة، تم قتل أكثر من 80 ألف مدني بريء بوحشية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91373" target="_blank">📅 17:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf567a415.mp4?token=BS9hLCkPChcrhf0sDTjGo4P8xArLUnvv-j_HiLKIRrO5DZOYEdHrDDFih9zQnSV5pIQNpJk2M55iNPdaqhUv-XhDPJQWY3pIiJJvXW8RnlsGC3ZPphGXFiwmhZuho9G5D8VDFzhIpxjfWzEnmNvT0lA7kpdWvbB3IHLkuNalcoXnM4ypxBWnahQvc_DROUvelyHSNpk6PQa3X3g2z6xW2XJ3a-ntcMz-1_YzbfKpuqMFVXTlHNtjfgWsCxjsKzi_DkjspIwd3WZ_mF2RWnsmKUzYOPH60pji4aAHbpTyZmkISu47b9e6XZOw8dNPytVsdWrm1YqjmQ63NvnB3QQicIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf567a415.mp4?token=BS9hLCkPChcrhf0sDTjGo4P8xArLUnvv-j_HiLKIRrO5DZOYEdHrDDFih9zQnSV5pIQNpJk2M55iNPdaqhUv-XhDPJQWY3pIiJJvXW8RnlsGC3ZPphGXFiwmhZuho9G5D8VDFzhIpxjfWzEnmNvT0lA7kpdWvbB3IHLkuNalcoXnM4ypxBWnahQvc_DROUvelyHSNpk6PQa3X3g2z6xW2XJ3a-ntcMz-1_YzbfKpuqMFVXTlHNtjfgWsCxjsKzi_DkjspIwd3WZ_mF2RWnsmKUzYOPH60pji4aAHbpTyZmkISu47b9e6XZOw8dNPytVsdWrm1YqjmQ63NvnB3QQicIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بيزشكيان: شعبنا الأبرياء كانوا هدفًا لهجمات جبانة فرضت على بلدنا. دافعنا عن أنفسنا بكل قوة. هاجمتنا أمريكا وإسرائيل بأحدث التقنيات. لقد أصابونا، لكننا لم ننحن.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91372" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260ef30b47.mp4?token=XcLobKfD8qZI9Qd_peyjJWUKiNVhtdDFSJpaYpndk8vcc5zVgX3PWwLLmSewbrBneGHtA72GkLIFMRzwTcxYjaztRjD-s_uh83npYsKrFAT2NYE1iZDMS-0zHJ-28h64cvApcWZ8km6KrjfJ-MYy496n0GyrjvGvcqU60vYCioLmKXP_j-K6L2AEZJ26iHDGKVVQOk7DzB5VBbYnJe8YVjKw_Ff4ZGKblUwKNNuNXrI0hdHvCvhvWfBmEPLMNRoWQjHwCtHPBGnS-nMVs9ZT2grUfN3Xt3w0JEpAJe93yIxhBrszKTcJdTmsbg4cLnTbTbbHBjg5ym4cTbQP3zfiOCjv7DdnAZHno4x0qJiarZhaGACH-WYcEnXzY3wTEtoVpLtrhwKSApW--1BzE0e_8Dw-gEeMnO-EAWDiZrMXtk6OwQ0r72NyZ5Lzi6S1cqeu7nLtL7uWMwOItPKJMPvVKeHDejlQD6LQmhGjA6jHRlZwLdrIKEYHjiFUyP02VttdmYm_NJNJz2gEvFDd9Zl8rm0xKOs5EAwSOYFB_vt64MBg4XY2PFMjb84RMXvsWPosMCNgKvSaJ3xsU0LKsrt4VE-GfWCEkLm0jqZwRRjFqH0-fLi8pxKTb-OWBtrSsJf3AwgnyVOsciNrmEluzeicKfEEFxWt2Dq6LceION9RNX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260ef30b47.mp4?token=XcLobKfD8qZI9Qd_peyjJWUKiNVhtdDFSJpaYpndk8vcc5zVgX3PWwLLmSewbrBneGHtA72GkLIFMRzwTcxYjaztRjD-s_uh83npYsKrFAT2NYE1iZDMS-0zHJ-28h64cvApcWZ8km6KrjfJ-MYy496n0GyrjvGvcqU60vYCioLmKXP_j-K6L2AEZJ26iHDGKVVQOk7DzB5VBbYnJe8YVjKw_Ff4ZGKblUwKNNuNXrI0hdHvCvhvWfBmEPLMNRoWQjHwCtHPBGnS-nMVs9ZT2grUfN3Xt3w0JEpAJe93yIxhBrszKTcJdTmsbg4cLnTbTbbHBjg5ym4cTbQP3zfiOCjv7DdnAZHno4x0qJiarZhaGACH-WYcEnXzY3wTEtoVpLtrhwKSApW--1BzE0e_8Dw-gEeMnO-EAWDiZrMXtk6OwQ0r72NyZ5Lzi6S1cqeu7nLtL7uWMwOItPKJMPvVKeHDejlQD6LQmhGjA6jHRlZwLdrIKEYHjiFUyP02VttdmYm_NJNJz2gEvFDd9Zl8rm0xKOs5EAwSOYFB_vt64MBg4XY2PFMjb84RMXvsWPosMCNgKvSaJ3xsU0LKsrt4VE-GfWCEkLm0jqZwRRjFqH0-fLi8pxKTb-OWBtrSsJf3AwgnyVOsciNrmEluzeicKfEEFxWt2Dq6LceION9RNX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة هروب الوفد الامريكي بعد استعراض الرئيس الايراني للجرائم الامريكية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91371" target="_blank">📅 17:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=ht_g-0qCh7QB0Y5wPJ3JfY3uJkOvXf3p_ITQxxvotZK9Rb42yo_K46ZkJ6nkRf0lGFs6fLN4AOjPqDN_RMkmBTrLxy9BePAdj93ps48-jTQNZBKOyva3iHBjqNtoz8krS71iqhurQXMciTYHkrfY85s6hL_8IKScow_3iZu5EVtq2wCflKKMFZ5PtxwM9m8d-LnO_js7UEO_tY8_gM-5RzydAu2R3LNOS_gXtLQvibiCtnIHKfY9-NpKdn4Khd-313XFVJa9DYgwLT-EgotKjV9gSK4j8MMhoZrO6xqcX4uNAopE_YU2ZHPs5qS0rzOfytxWUQuXUTcIbSyI58pmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1f06c6df.mp4?token=ht_g-0qCh7QB0Y5wPJ3JfY3uJkOvXf3p_ITQxxvotZK9Rb42yo_K46ZkJ6nkRf0lGFs6fLN4AOjPqDN_RMkmBTrLxy9BePAdj93ps48-jTQNZBKOyva3iHBjqNtoz8krS71iqhurQXMciTYHkrfY85s6hL_8IKScow_3iZu5EVtq2wCflKKMFZ5PtxwM9m8d-LnO_js7UEO_tY8_gM-5RzydAu2R3LNOS_gXtLQvibiCtnIHKfY9-NpKdn4Khd-313XFVJa9DYgwLT-EgotKjV9gSK4j8MMhoZrO6xqcX4uNAopE_YU2ZHPs5qS0rzOfytxWUQuXUTcIbSyI58pmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الامريكي يهرب من القاعة خلال كلمة بزشكيان</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91370" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بزشكيان: أنا قادم من إيران حيث تم اغتيال قائدنا الأعلى الموقر دون أي إطار قانوني أو سبب. أنا قادم من إيران حيث، في الحقيقة، تم قصف مدرسة. هل ترون هؤلاء الأطفال؟ هؤلاء الأطفال لقوا حتفهم تحت القصف باستخدام أسلحة استخدمتها الولايات المتحدة وإسرائيل. لقد كانوا…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91369" target="_blank">📅 17:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پزشکیان: أولئك الذين هم إرهابيون والذين يربون الإرهابيين يقولون لنا إننا إرهابيون!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91368" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
پزشکیان يبدأ بعد قليل بإلقاء كلمة الجمهورية الاسلامية الايرانية في الجمعية العامة للأمم المتحدة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91367" target="_blank">📅 17:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز نجران</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91366" target="_blank">📅 17:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91365">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91365" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91364">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91364" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91363">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91363" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91362">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC2QdeMGy0ooz5mCp_og-hb6csFbA9x5RCMkDKDO-NW3phOOOBpEJ-nr-5ilmP1UcYLx2ff4I22KMpgMfsirICcKW-0-lud-9QsFklxjH_r9IUDIeh67_2ToGJCWkbeQHnpdLPok9udluhTtXMfM3e5EOOrBtTJT_1RzJSfpZheIhKTDGDb6oZ3H_bQ87vJ5sXw422QQ7s8zFsw08Wc0DR6Hfw-UlvRe2eX4Aons8GGYI3H2binIxEjuynCoitVk72tFh8XA15XJD9pkEusHcfSTt0ZTsVo602QoEA5XeeGimuzlFfEC10KcSgTYzX91h76jwHgTZGmBxhiD-R36Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان يصل مبنى الامم المتحدة في نيويورك لالقاء كلمته.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91362" target="_blank">📅 17:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91361">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حادث دهس على الطريق 443 بالقرب من بيت حورون واصابة جندي صهيوني كحصيلة اولية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91361" target="_blank">📅 17:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91360">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3627ab6983.mp4?token=SfLWx2iS_4v8mpO5HxIqDmS5EM8FFNJQSUIqQgcaXH36CI_vD1eKN6veUFlWK63uR0S7KesH29bLEsx-BEM0EhfjNEuzQTXc2iRC0dIJmOeB2f7cOcA7af8e_PwFDVJ127aVyxDPc0xKBhG_59K7w2MTZCUU6DdFRo2diQrryXK72wdFlD_sgbgL24uNsk7gj7cYtYrD0ZmxBBj9JF372hVcAga8Yl20ewaQvwkpUr1tv4yGDer5mdiVKELDJhdB5CVZnffZNmI_VHf2ka4R3RMw0dB5ArvTek2a9wI-GIOcRldkbsSepV6TaWaPLF2Z90YPk8tUnraMD2GZ0cWwCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3627ab6983.mp4?token=SfLWx2iS_4v8mpO5HxIqDmS5EM8FFNJQSUIqQgcaXH36CI_vD1eKN6veUFlWK63uR0S7KesH29bLEsx-BEM0EhfjNEuzQTXc2iRC0dIJmOeB2f7cOcA7af8e_PwFDVJ127aVyxDPc0xKBhG_59K7w2MTZCUU6DdFRo2diQrryXK72wdFlD_sgbgL24uNsk7gj7cYtYrD0ZmxBBj9JF372hVcAga8Yl20ewaQvwkpUr1tv4yGDer5mdiVKELDJhdB5CVZnffZNmI_VHf2ka4R3RMw0dB5ArvTek2a9wI-GIOcRldkbsSepV6TaWaPLF2Z90YPk8tUnraMD2GZ0cWwCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث دهس على الطريق 443 بالقرب من بيت حورون واصابة جندي صهيوني كحصيلة اولية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91360" target="_blank">📅 17:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91359">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smOvzPBWVFv2gA_uigNsyKBfv_pdzY9J1o34i8jYFFO0GvBkrbhFCCYLEHDhN07uGrtJ84gUVPaW3K6kESva6E5lvl-WWr8rWFG9-I3iGvvl23GQXUz0KyEQpFp82Z7K7rAgw6NPQQTEJp8RYPdS9BwPl-lHnHV257noC_kLbAA3S6jXfv02X2WCxt7Wib_j8CfLFAC-a1DHkME0o1D50SHxxgrfktBH7carsG2l_E-bssp0doYNXEznuJlvZKBKod4-0uK7HR4L5-MRVd9EMlugAcP67ZzrtXZiXj4CP6hCW3y0zV_MoyrgfBgrzUiYmbcEytutdCmYbPmsFwL73A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الشيخ ناظم السعيدي رئيس المجلس التنفيذي لحركة النجباء:
نعلن رفضنا القاطع لانخراط العراق في قرار المجرم ترمب الجائرة بحصار شيعة علي بن أبي طالب (عليه السلام)</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/91359" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91358">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان يصل مبنى الامم المتحدة في نيويورك لالقاء كلمته.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91358" target="_blank">📅 17:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91357">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">محسن رضائي: يجب على الدول المجاورة ألا تتدخل في مسألة تحليق الطائرات الإيرانية، ولا أن تشارك في المغامرات الأمريكية. إذا حدث ذلك، فسوف نمنع تحليق طائرات الدول المجاورة التي تتعاون مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/91357" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91356">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7feb0d61e.mp4?token=YaPQG3FdBrH7HnwwaMzZlJSpWI-wK-w8DLvO1zdbTT_t4Lq7nrdGl6wxoHDxQiYO698VJ8xGeAJjXVQwMlVICnbBb57moISeXXpl8KMbeWf4WyNOjmBMTYJrtNhv-dCBZOPFmtnla4KHDdSg3PqriGnSMl1v9rVy51V_atWVjy54xxHE326MFcE4-cCSR79As0Iwn8CpZlmwahL8hAIxMxOuqKzRaS05pIHGASf-fxcOGjAQwQe6ukKRzYeAaTQyrqdxD4bFWGp6hQFetsyhmt51qKmKg2HdERHh_yiNsjG83AKMA9SjQu6IUePoVCu4wQVwF5sa6hVAuy7ZZBd_Rl-uWAYguRowIiwqxE6HPEDJ0DEbAApvSoMe4VXi1VLvpFuM3sLQWtYUkEwdcl8_eMEaKIYAkXc7PqqdSMMk0_9Erwi7IixjlTRgiQhX0YhGCAbBvU_acsbari19kqvNfI_TMjtYBeUlw7X0GbFXojQiedOXZVtAZtwdMWkk5RYV4RNsm4XdFcZGeA19xNaCWWhH1xKQuIAe6Se0hYJC1Toj_nrYZ2tA_3lsBeh4IcVbDlQ7As-u9bibO6SN1Lt57-xRWhVKs96ElQcHFOrsTNmUhNQgSnpCyTmaJBRIgY8gEPGRyc_FhDQiySrdwQxqu4peszKakKKypAAfMR9jv9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7feb0d61e.mp4?token=YaPQG3FdBrH7HnwwaMzZlJSpWI-wK-w8DLvO1zdbTT_t4Lq7nrdGl6wxoHDxQiYO698VJ8xGeAJjXVQwMlVICnbBb57moISeXXpl8KMbeWf4WyNOjmBMTYJrtNhv-dCBZOPFmtnla4KHDdSg3PqriGnSMl1v9rVy51V_atWVjy54xxHE326MFcE4-cCSR79As0Iwn8CpZlmwahL8hAIxMxOuqKzRaS05pIHGASf-fxcOGjAQwQe6ukKRzYeAaTQyrqdxD4bFWGp6hQFetsyhmt51qKmKg2HdERHh_yiNsjG83AKMA9SjQu6IUePoVCu4wQVwF5sa6hVAuy7ZZBd_Rl-uWAYguRowIiwqxE6HPEDJ0DEbAApvSoMe4VXi1VLvpFuM3sLQWtYUkEwdcl8_eMEaKIYAkXc7PqqdSMMk0_9Erwi7IixjlTRgiQhX0YhGCAbBvU_acsbari19kqvNfI_TMjtYBeUlw7X0GbFXojQiedOXZVtAZtwdMWkk5RYV4RNsm4XdFcZGeA19xNaCWWhH1xKQuIAe6Se0hYJC1Toj_nrYZ2tA_3lsBeh4IcVbDlQ7As-u9bibO6SN1Lt57-xRWhVKs96ElQcHFOrsTNmUhNQgSnpCyTmaJBRIgY8gEPGRyc_FhDQiySrdwQxqu4peszKakKKypAAfMR9jv9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضائي: إذا وافقت الدول المجاورة على منع الرحلات الجوية الإيرانية، فلن تتمكن مطاراتها من العمل.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91356" target="_blank">📅 17:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
محسن رضائي: نحن نقوم بتحليل هندسي للغواصة الامريكية. هذه الغواصة ذات قيمة كبيرة. ربما اقول لنا بعض الدول في المستقبل: أعطونا هذه التكنولوجيا، وسندفع لكم مقابلها مليارات الدولارات.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91355" target="_blank">📅 17:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvgZWg7LQ-N37geEAY0AOaEB5FRkjWK1RevQfVmDFHSx4REgxW5uC6J7VKomPKd71U39jQLiS3PiuayPs2IN81EpHVD5sZdD8DJF6SBjOw_tbOK6aMszNt9Q7ppjM2wbnk1YnT6cHamJqaXAjfyMNvJiaf-vsR2Sud6neWgX9Ym4QOrC96LbYYLeM52dNS-hpI_btiQAfTjDnEArX0teHEu3X62RbOmlYik9WOmHiTHZfjhTu4W5jW_LAsLkRqkSU74GC29yA627fVu7SE-s7nEWcgV1nNI4mqGQbazY4CwDvHU0P6oMmTz0NINXpDdu_yIhdzaWPXcKikXgdr-RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي للناتو:
خلال الاجتماعات مع الاتحاد الاوروبي حذرت من العواقب الوخيمة لتسهيل ودعم جرائم الحرب الإسرائيلية الأمريكية سواء في غزة أو إيران. بغض النظر عن هذه الحماقة الكبيرة، يجب أن يعلم الناتو الآن أن التذلل لا يرضي المتنمر أبدًا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91354" target="_blank">📅 17:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da478de12.mp4?token=q0c-E01ZdfpZDw3ty-GY1L2vhDDU6hq2__OsoYu0mIDzeUEYuL38Fweo9JjE-LXYt7mvgvWiYZQtWqDokpngmT1wEK1Ny7KBV_DN9vXchquyMKA7N4vle4rV5qpDCQqr04u-9lL8qIrmvwI-ZTyO5sJnKBxwO2i7gj7b2WOZakD4wJtv1ZQorwrX2H3c-mtMTjQWfrCDnbwPvgh9VU728iv0c3XjlNhurBkehRzJWQ0REai-MqD5bIpBMRBUOlrvK8B3OjGigw3ZORp6__SgRbdrqsbH11YFQtc12EMi_sXq_CLCxGbg_ps4xOB6rMg4LWvOd7Bc1kZy1s2v-YGA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da478de12.mp4?token=q0c-E01ZdfpZDw3ty-GY1L2vhDDU6hq2__OsoYu0mIDzeUEYuL38Fweo9JjE-LXYt7mvgvWiYZQtWqDokpngmT1wEK1Ny7KBV_DN9vXchquyMKA7N4vle4rV5qpDCQqr04u-9lL8qIrmvwI-ZTyO5sJnKBxwO2i7gj7b2WOZakD4wJtv1ZQorwrX2H3c-mtMTjQWfrCDnbwPvgh9VU728iv0c3XjlNhurBkehRzJWQ0REai-MqD5bIpBMRBUOlrvK8B3OjGigw3ZORp6__SgRbdrqsbH11YFQtc12EMi_sXq_CLCxGbg_ps4xOB6rMg4LWvOd7Bc1kZy1s2v-YGA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمين المجلس الأعلى للأمن القومي الإيراني اللواء محسن رضائي: طالما لم يتم تلبية شروط إيران، فلن يتم إعادة فتح مضيق هرمز ولن تكون هناك أي مفاوضات.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/91353" target="_blank">📅 17:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91352">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e236baf83d.mp4?token=OlKfMEC1ziZuomAC7ilZkrxXccXNzzdqwvmyQxpwfq2hPVNlHUQIrlAUEh6mSRFKTNWMW4v5ZxK6p2vCLntKUN48hHeEfwqU1PEt3YQXlRyxtdfpjCJ9-iTZ5PcaG6V3Cpf-e3cRKsp2qRWsZuRbk1lEq-bePGJCXnxobwnIoNQJ274YmgohObMnBdM1ee50WaW-zePoxxV6lwGl2Bcgh5GuwPSNRdeluEehws5ZDc5x5jF-vq92jLL_5mHIwEi9S-u25UfwQetOEpUviucnP8vMn3SaM2QoNPJwL36g8qOQ1SPloA6WhbdhyDEELAjuqm2duLL5SV3gmMIukUMLX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e236baf83d.mp4?token=OlKfMEC1ziZuomAC7ilZkrxXccXNzzdqwvmyQxpwfq2hPVNlHUQIrlAUEh6mSRFKTNWMW4v5ZxK6p2vCLntKUN48hHeEfwqU1PEt3YQXlRyxtdfpjCJ9-iTZ5PcaG6V3Cpf-e3cRKsp2qRWsZuRbk1lEq-bePGJCXnxobwnIoNQJ274YmgohObMnBdM1ee50WaW-zePoxxV6lwGl2Bcgh5GuwPSNRdeluEehws5ZDc5x5jF-vq92jLL_5mHIwEi9S-u25UfwQetOEpUviucnP8vMn3SaM2QoNPJwL36g8qOQ1SPloA6WhbdhyDEELAjuqm2duLL5SV3gmMIukUMLX4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمين المجلس الأعلى للأمن القومي الإيراني اللواء محسن رضائي: طالما لم يتم تلبية شروط إيران، فلن يتم إعادة فتح مضيق هرمز ولن تكون هناك أي مفاوضات.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/91352" target="_blank">📅 17:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
🇦🇪
‏مصرف الإمارات المركزي يعلن اتخاذ إجراءات إنفاذ صارمة بحق فروع بنك ملي إيران العاملة في دويلة الإمارات.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91350" target="_blank">📅 17:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
النائب عن منظمة بدر مهدي تقي الامرلي يعلن عن استقالته من مجلس النواب العراقي ومنظمة بدر .  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91349" target="_blank">📅 16:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇸🇾
🇮🇱
ابو محمد الجولاني:
500 غارة جوية ومدفعية إسرائيلية على سوريا. نرفض محاولات إسرائيل فرض سياسة الأمر الواقع</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91348" target="_blank">📅 16:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
النائب عن منظمة بدر مهدي تقي الامرلي يعلن عن استقالته من مجلس النواب العراقي ومنظمة بدر .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91347" target="_blank">📅 15:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
مصدر امني خاص عراقي لنايا
قوة امنية تحاصر فندق ركسوس وسط المنطقة الخضراء بالعاصمة بغداد وتدقق في هويات العمال السوريين والأتراك البالغ عددهم حوالي ٣٠٠٠ آلاف موظف منتهية إقامتهم في العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91346" target="_blank">📅 15:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇷🇺
🔻
الدفاع البولندية : دخلت مروحية روسية من طراز Mi-8 لفترة وجيزة المجال الجوي البولندي شمال برانيفو، قادمة من مقاطعة كالينينغراد. اخترقت المروحية المجال الجوي البولندي لمسافة 300 متر، وبقيت هناك لمدة 42 ثانية إجمالاً.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91345" target="_blank">📅 15:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91344" target="_blank">📅 15:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91343" target="_blank">📅 15:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
صدور حكم قضائي عراقي ثاني بحق كل من عالية نصيف واشواق الجبوري بالسجن لمدة ثلاث سنوات عن جريمة إخفاء معلومات في استمارة الذمة المالية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91342" target="_blank">📅 15:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نايا - NAYA
pinned «
🔻
🔻
Dear followers, we are making a fresh start with exclusive news and updates on our X account. Please join us and follow along!
🔻
🔹
جمهورنا العزيز سنكون بانطلاق جديدة واخبار حصرية على حسابنا في منصة اكس يرجى الانضمام معنا .    https://x.com/nayaixa3?s=11
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91341" target="_blank">📅 15:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
🔻
Dear followers, we are making a fresh start with exclusive news and updates on our X account. Please join us and follow along!
🔻
🔹
جمهورنا العزيز سنكون بانطلاق جديدة واخبار حصرية على حسابنا في منصة اكس يرجى الانضمام معنا .
https://x.com/nayaixa3?s=11</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91340" target="_blank">📅 15:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم:
خلية كانت تخطط لاغتيال وزير الأمن القومي إيتمار بن غفير باستخدام طائرة مسيرة متفجرة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91339" target="_blank">📅 14:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
الجيش الإمريكي يعلن مقتل مجندة أمريكية في السعودية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91338" target="_blank">📅 14:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇪🇹
مستشار رئيس وزراء إثيوبيا: قوات تيغراي هاجمت مواقع للحكومة في عفر وأمهرة وسيطرت على مطارات في تيغراي</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91337" target="_blank">📅 14:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a602906952.mp4?token=HUSxLxMBtSGNNDR7iRpTWYiPb1sxFkJ4D-zuCkczV9jxfbpC167ovxbKiBiEOMZE_eoC4QOzs5raHq3Qqd0mSbgUC9i68IKH1aMLEiERbyFR4w8k1NRcICj3viM0ql1F5nWGWCDdQfS8Nf3PopU8QJKHcLAlDFPwHsoowe0p1puNnPA4EfjypzzUcVJEcxizBG4Oh2xjwn-nRQ9mwCFS8Y5P5n30aA5_PA8wwJRKnYRs8UtMChq-MJROze4SlxTn7vg_S4fabPtfacnGsHYtT6N29D_eL-YMhLkYx46jzXkgTCxhlaoBqCReZzc1iw6pRZTwREMNvx7yafsyOpjVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a602906952.mp4?token=HUSxLxMBtSGNNDR7iRpTWYiPb1sxFkJ4D-zuCkczV9jxfbpC167ovxbKiBiEOMZE_eoC4QOzs5raHq3Qqd0mSbgUC9i68IKH1aMLEiERbyFR4w8k1NRcICj3viM0ql1F5nWGWCDdQfS8Nf3PopU8QJKHcLAlDFPwHsoowe0p1puNnPA4EfjypzzUcVJEcxizBG4Oh2xjwn-nRQ9mwCFS8Y5P5n30aA5_PA8wwJRKnYRs8UtMChq-MJROze4SlxTn7vg_S4fabPtfacnGsHYtT6N29D_eL-YMhLkYx46jzXkgTCxhlaoBqCReZzc1iw6pRZTwREMNvx7yafsyOpjVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
باكستان تزعم اسقاط 8 طائرات مسيرة افغانية حاولت مهاجمتها.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91336" target="_blank">📅 14:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇪🇹
مستشار رئيس وزراء إثيوبيا:
قوات تيغراي هاجمت مواقع للحكومة في عفر وأمهرة وسيطرت على مطارات في تيغراي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91335" target="_blank">📅 14:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
التلفزيون العراقي الرسمي يزعم:
- عدم استقبال الطائرات الإيرانية متعلق بشركات المناولة والخدمات الأرضية وهي شركات خاصة غير حكومية متعاقدة مع شركات الطيران الإيرانية وهي من اعتذرت عن تقديم خدمات خشية التعرض لعقوبات
- المطارات العراقية توفر بيئة مكانية للشركات الخاصة التي تقدم الخدمات مقابل أجور ولا تتدخل بطبيعة تعاقد هذه الشركات مع شركات الطيران بأي تفصيل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91334" target="_blank">📅 14:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5VOXbgRgxahkqnsrfRG8aopw75elvM_4Llf9WupIzL1WbvKAbDggyhNDejUu06eg9aOqEDTMjzwQOfMkpLgUzmSa0iYS_XF4ASqJd8Dt23b8AMqPoQufHkpZZdHN5BkeTfipCV0DoZh-hWm53W7eQ0QKpyr9eyTXWN62iy2Pq4ysbXiBXz7ekbFEIJY0cvjuVltkMh2QXbj5u4NQVOwMtXKZcMpgp7RO3SwF51811jBZyiELkDRgeVngeMPZhLsU6nX06NZQ58l04VdH-KAMwSJfEpZhHKo8l6jRF23dWJ9ATDd38YRIvzw5HyLuJr7nemKinQfZ4btpn5gf_Olmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحكم على النائبة (هند العباسي) بالسجن 7 سنوات بتهم تتعلق بالفساد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91333" target="_blank">📅 14:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇾🇪
مسؤول في انصار الله لوكالة فرانس برس:
إما تسليم مدينة مأرب وإما ويلات الحرب والدمار وسنستهدف كل مصالح الولايات المتحدة في المنطقة إذا ساندت السعودية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91332" target="_blank">📅 14:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV6gxaaDuW3NnjiTG7ya3FT6A7u-dlj_dyDws0I9tYw5x8Ryp_gDq-nfYLvK3LKS0uh58rMUlsGBp3IO7aDNCohU2EVlziBudN1Ml4dz6qaubo58i1O3rruLP2qT0iM6njfWps2eNpPj7gSR3M6xFdYOQs_6ADxCJZEbWoWW8woiQ1snx-vD1WESudzyu7hpvOWmq72doBEtAsJq5fE6CvxAk_eEVFiFE1FGUsVKDhYTY3QCSp_MTZMeIMKhLGBc95RzCultLJxz4yZoyBIZPJXwkUzfBbe3T_DP0y0TuCPWIrD0euEeYJolSbGtkvYgEGEuhwMzhiJAn9FIQP01IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء العراقي:
السجن 7 سنوات بحق النائبة أشواق الجبوري على خلفية قضية الكسب غير المشروع.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91331" target="_blank">📅 14:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91329">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
‏طائرة تابعة لـ"إيران إير" تهبط في اسطنبول رغم سريان الحظر الأميركي.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91329" target="_blank">📅 13:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91328">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggbYH0s-pBslmJXdRF_8RHkEZis8IoBFMYQYiOutQiR5-a7yekrt8pNCslaGj3iB-ejrkWkewsgZvLZriLeU1cJg2wVdjW2nrufKSk46FDA6KaGWFsJXTVxwXtmC4DpidnVhQsmdVt8NrCWw8Q4sijw3DfeH4UXMVZOzbOthGrEqhoYpRGhIgP-PIUGmefhjB7XMR4aJL53jUSZhKOcgTgI3kcdmQHNPGCyLkhJwd3SYqlymImCu9OQiXzTtPMrD40z_cYKPVckAnFNbJzG9zaYida5yaIFMx4SQZFOyZoqiqeU_mWiIQTWlMiS4-F83RVPib1HUXjINW4qbzIavow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء العراقي:
السجن 7 سنوات بحق النائبة عالية نصيف بعد ادانتها بتهم فساد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91328" target="_blank">📅 13:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91327">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
اكسيوس:
ما يسمى بلجنة السلام تكشف عن خطة إعادة إعمار غزة بقيمة 2.45 مليار دولار وسيتم عرضها على الاعضاء يوم الاربعاء
علما ان غزة تحتاج مئات مليارات الدولارات لاعادة الاعمار ان لم تكن تحتاج اكثر من تريليون دولار!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91327" target="_blank">📅 12:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91326">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇾🇪
🇸🇦
عدوان سعودي يستهدف محافظة الحديدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91326" target="_blank">📅 12:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91325">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
🇮🇷
🇨🇳
الاعلام الاوربي:
هبوط طائرة تجارية إيرانية في الصين رغم العقوبات الأميركية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91325" target="_blank">📅 12:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91324">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇷🇺
جهاز الأمن الفيدرالي الروسي (FSB) :
تم اعتقال أحد سكان موسكو بتهمة التخطيط لتفجير سيارة في موكب مسؤول روسي رفيع المستوى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91324" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91323">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c2099f8c.mp4?token=tgJSlatgbza-RDaeTEYotp02oBfxidumVhq5_9KZO6d5mgSN_z-JbuGhBw2ZVHwM8eqsXqH78nj-w9eWEBpk2Oh3UKIxAyJXXW8j0csgTYyghw8V_YnDMUlO4sjbjKCeFxKP_3eBjdlsU4nIlzFjZtM9rjzDlAR6TzzvyaIMH3UTdVRwGkEWQFUoKowfZHf0TAgnEzuzNAfDOuI322sxZQH7mlqsKOwXzx8AuYgfnHY0FeEuKdhOvFJTBEJMyZx62ddWS8Kanl_OSB83WlFMI_rfTdLesi4N-B5mzGR7itpbo176CSLBzcsyyZa74VrzbeWh5w16e5SC7jQQbzl1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c2099f8c.mp4?token=tgJSlatgbza-RDaeTEYotp02oBfxidumVhq5_9KZO6d5mgSN_z-JbuGhBw2ZVHwM8eqsXqH78nj-w9eWEBpk2Oh3UKIxAyJXXW8j0csgTYyghw8V_YnDMUlO4sjbjKCeFxKP_3eBjdlsU4nIlzFjZtM9rjzDlAR6TzzvyaIMH3UTdVRwGkEWQFUoKowfZHf0TAgnEzuzNAfDOuI322sxZQH7mlqsKOwXzx8AuYgfnHY0FeEuKdhOvFJTBEJMyZx62ddWS8Kanl_OSB83WlFMI_rfTdLesi4N-B5mzGR7itpbo176CSLBzcsyyZa74VrzbeWh5w16e5SC7jQQbzl1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇷
الأمين العام لحلف الناتو، حول إيران:
لماذا كان من الضروري تدخل الولايات المتحدة لإزالة القدرات النووية الإيرانية؟ ولماذا ينظر الجميع الآن مرة أخرى إلى الولايات المتحدة فيما يتعلق بحركة أنصار الله في البحر الأحمر؟
لأن الأوروبيين بطريقة ما لم يمتلكوا القدرات الكافية للقيام بذلك بأنفسهم. هذا هو "الفناء الخلفي" لأوروبا، وليس "الفناء الخلفي" للولايات المتحدة.
في المستقبل، فإن ما ستحصلون عليه من حلف شمال الأطلسي (الناتو) الأقوى هو أن الأوروبيين يمكنهم الاعتناء بـ "فنائهم الخلفية" بأنفسهم.
فناء الخلفي يقصد به ان هذه المنطقة هي منطقة نفوذ حيوي لاؤروبا وليس لامريكا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91323" target="_blank">📅 11:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91322">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
🔻
تم صرف رواتب الحشد الشعبي.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91322" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صحافة غربية
📰
‏
🔻
فايننشال تايمز: بحسب تحليل، يدفع سائقو السيارات الأوروبيون 40% أكثر مقابل الديزل مقارنةً ببداية عام 2026. ويعادل ذلك حوالي 30 € إضافياً لخزان وقود سعة 50 لتراً
💶
.
🇺🇸
مجموعة جرائم إلكترونية تُعرف باسم شايني هانتر سرقت أكثر من 2 تيرابايت من البيانات من أنظمة مكتب التحقيقات الفيدرالي، بما في ذلك المعلومات الشخصية لآلاف العملاء والمتقدمين للوظائف.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91321" target="_blank">📅 11:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91320">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
مصدر عراقي لنايا
محكمة جنايات الكرخ تصدر حكماً بالإعدام بحق المدان محمد عبد المجيد خلف الطائي، قاتل العميد هشام محمد طلاع والمفوض خالد عباس لفتة، عن جريمة استهدافهما أثناء أداء الواجب في منطقة الدورة جنوبي بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91320" target="_blank">📅 10:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91319">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7c3165ca.mp4?token=i9UgrKtp0S4F5dvYtZ27pBpxeD9m_f9OkvzMOBfhcNFmvexcUuN9udy2RfXeO1S3C82lo16ISe8gupb_Iq9ZDOP3vypOkr6rul6QEMR760GadLm3a0EUarxymecGC6tQrIJ2RILMAqtND3ViJHlblOv5opYeM2yrriFmj07Cpp860BDoZc2pyezoegqg598mq7yZlWILm8v5j0nTit7WPRCVEU7TTSxoQ39vffqkw79wEI2BUIjtoPu6m9EfqPa8zTDq5zvH74OCYSIp2pqVB79_tN0uwseTpq0UsM5Ps9kkCY7w91lMRbNevYrypjA1S60Bbrh0m4c_qd-zTgNihpyJd-ckHNk0b77yhg5nvU1Nf50f1b_FzAqlRdryFVy6RS9rteK7vD3r7UhNzQP-2svzOjhgXuV3mCULcwqbqMkwP_pZnjOloZP7Z2Xm4YxNSfaX7IdhKf_TrK-BUNLH3Vpe52ixs6bnj0hM5lQEqpniPXBJVDMo2fJYBzgx5QFBN8kyY8-gkrVYWGIUMZRrs5SbxEkd8VNu8CA8xduAyC9ltb4EZTddW_re0300nxDZeNPQZE6BxMrBco4VvK5KdbWG7SiHkxl016Z--Ohoponp2dI03dUE4spWa1J_FvjmRoppZbr57-GkHLSboIDNBHy0FCeRFRDaKRHLtW0qVlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7c3165ca.mp4?token=i9UgrKtp0S4F5dvYtZ27pBpxeD9m_f9OkvzMOBfhcNFmvexcUuN9udy2RfXeO1S3C82lo16ISe8gupb_Iq9ZDOP3vypOkr6rul6QEMR760GadLm3a0EUarxymecGC6tQrIJ2RILMAqtND3ViJHlblOv5opYeM2yrriFmj07Cpp860BDoZc2pyezoegqg598mq7yZlWILm8v5j0nTit7WPRCVEU7TTSxoQ39vffqkw79wEI2BUIjtoPu6m9EfqPa8zTDq5zvH74OCYSIp2pqVB79_tN0uwseTpq0UsM5Ps9kkCY7w91lMRbNevYrypjA1S60Bbrh0m4c_qd-zTgNihpyJd-ckHNk0b77yhg5nvU1Nf50f1b_FzAqlRdryFVy6RS9rteK7vD3r7UhNzQP-2svzOjhgXuV3mCULcwqbqMkwP_pZnjOloZP7Z2Xm4YxNSfaX7IdhKf_TrK-BUNLH3Vpe52ixs6bnj0hM5lQEqpniPXBJVDMo2fJYBzgx5QFBN8kyY8-gkrVYWGIUMZRrs5SbxEkd8VNu8CA8xduAyC9ltb4EZTddW_re0300nxDZeNPQZE6BxMrBco4VvK5KdbWG7SiHkxl016Z--Ohoponp2dI03dUE4spWa1J_FvjmRoppZbr57-GkHLSboIDNBHy0FCeRFRDaKRHLtW0qVlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇺🇸
🇮🇶
🇾🇪
وزير الخارجية الأمريكي
ماركو روبيو يزعم
:
"
كتائب حزب الله" العراقية هي المسؤولة عن الهجمات بالطائرات بدون طيار التي استهدفت خط الأنابيب الذي يربط بين الشرق والغرب في السعودية في وقت سابق من هذا الشهر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91319" target="_blank">📅 10:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91318">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6Nknfbh7QcWxD7NfMr1YQ_eQ9j4m_eeo1njT8Mju3V4-aft4nlb7ut4QfuwzhVLDAHlfSQ3TRdQu-KAQ96ASHxRsDt-5Bn-jILTmgDG2JesRBe6o8swhyBUx2F_SoU3suKjcvLYgrPNtCW0b4vQ77N89zXfEtU5ZvNo68xLgTFVWJWagsP1-C6G1kR3dmf_bMwwHbnLffiyTzMwDmRHnoKwyxDCskys0N0KtlohAxkbHVB3q5vzhMSSw7r5KvH3-Bqk7-xQUEMyTAa97bi2oj8j0ETb-8axZ7kMl2tL_C8Sf9zjFXahT18fpusaUFccudk5QtYepZGS9zm2QBC5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع فلايت رادر : يوكد ما انفردت به نايا   توقف الملاحة بمطار الرياض الدولي</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91318" target="_blank">📅 06:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91317">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ستيف ويتكوف:  خضنا محادثات مطولة مع الوفد الإيراني عبر وسطاء.  ‏الوسطاء أتموا بنجاح جولة مناقشات بين أميركا والوفد الإيراني نأمل أن تكون بناءة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/91317" target="_blank">📅 06:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت القوات المسلحة اليمنية بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية في أجواء  المخا بمحافظة تعز، وقد تم استهدافها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91316" target="_blank">📅 05:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇦
🇺🇸
زيلنسكي:
الولايات المتحدة ستسعى للتوصل إلى اتفاق لوقف الهجمات على البنية التحتية للطاقة. حياتنا أهم من أسعار الطاقة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91315" target="_blank">📅 04:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91314">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات عنيفة تهز العاصمة الأوكرانية كييف نتيجة هجمات روسية بالطائرات المسيرة الإنقضاضية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/91314" target="_blank">📅 04:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91313">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9064f0220.mp4?token=aN2wepKPJevhNzMWouDexZSfMUzBkhJ7EN_3btFMgQHdyjpNXNwrZD_T7xxp6wWqVX82gKEigQIQXVetnJwarfmIYEth1UZjQ2tEMZkPUe0psTvoG8mgZOxZSAsC2K-lir5MaXz_28RHmElZ7vCu58M5P-n_itztARKQS7Oc1iZv3HQNXQT6jPJVjh6ofB5UrN-S8Jb1_aFigNI0ReROE7lQltkGP5-NCmAuNk3Er1mvxCxS7S6WM1fcffMQ-wavuTx2cE8OHaaIO92eAHFtwO-pjUB0YVxBkiGvcB9fMr5yUzm8Ej1wlVWJ1KD2XU7FQ4T6RI3vxeF6hRPN2z63ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9064f0220.mp4?token=aN2wepKPJevhNzMWouDexZSfMUzBkhJ7EN_3btFMgQHdyjpNXNwrZD_T7xxp6wWqVX82gKEigQIQXVetnJwarfmIYEth1UZjQ2tEMZkPUe0psTvoG8mgZOxZSAsC2K-lir5MaXz_28RHmElZ7vCu58M5P-n_itztARKQS7Oc1iZv3HQNXQT6jPJVjh6ofB5UrN-S8Jb1_aFigNI0ReROE7lQltkGP5-NCmAuNk3Er1mvxCxS7S6WM1fcffMQ-wavuTx2cE8OHaaIO92eAHFtwO-pjUB0YVxBkiGvcB9fMr5yUzm8Ej1wlVWJ1KD2XU7FQ4T6RI3vxeF6hRPN2z63ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏
رئيس الوزراء البريطاني:
نحن نقف إلى جانب إسرائيل في مواجهة التهديدات المستمرة، بما في ذلك التهديدات القادمة من إيران، التي تستهدف إسرائيل والشعب اليهودي في جميع أنحاء العالم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/91313" target="_blank">📅 03:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91312">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/747a67a438.mp4?token=cpUy9Sf-924T98I4GhhOJbQWGLVipf8da4OMWEFwhKoB0C_1csRLSspTdnMnXEp3XD7P6uQBxDnNtZtUIiaUvemyzuWlWwmzI6HgqM3oh9hZgvEiZ524a3GaqxxAgXV_XrObnncvg3zHxxdg_l84M-r4NyDf7Iw0pbcnbXkgJxz-bZj8vqOTgPZCGSvARRtouLNszLc2w4hBbubQ3Za450ubLrKJiCY9KrbGS7xytw-yhz3QzyK-nLJwSxIEKxvZIEni_KieZy0myLkLTqQG2scWl1nirvT7IoHXE0BPLBwZNa7nzOZG-CdDpQ64bZcJTx2Ju0hDQWf14Rs_eC-LEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/747a67a438.mp4?token=cpUy9Sf-924T98I4GhhOJbQWGLVipf8da4OMWEFwhKoB0C_1csRLSspTdnMnXEp3XD7P6uQBxDnNtZtUIiaUvemyzuWlWwmzI6HgqM3oh9hZgvEiZ524a3GaqxxAgXV_XrObnncvg3zHxxdg_l84M-r4NyDf7Iw0pbcnbXkgJxz-bZj8vqOTgPZCGSvARRtouLNszLc2w4hBbubQ3Za450ubLrKJiCY9KrbGS7xytw-yhz3QzyK-nLJwSxIEKxvZIEni_KieZy0myLkLTqQG2scWl1nirvT7IoHXE0BPLBwZNa7nzOZG-CdDpQ64bZcJTx2Ju0hDQWf14Rs_eC-LEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية عن انسحاب انصار الله من المخا وباب المندب واخلائهم العاصمة صنعاء والاتجاه الى صعدة بعد هذا الفيديو</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91312" target="_blank">📅 03:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91311">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
ستيف
ويتكوف:
خضنا محادثات مطولة مع الوفد الإيراني عبر وسطاء.
‏الوسطاء أتموا بنجاح جولة مناقشات بين أميركا والوفد الإيراني نأمل أن تكون بناءة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91311" target="_blank">📅 03:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91310">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇱
🇸🇾
الجولاني يكشر انيابه: الجولان هي أراضٍ سورية تقع تحت اعتراف الأمم المتحدة. لا يوجد أي نقاش حول هذه الأراضي ومن هي الجهة التي تملكها.  والقنيطرة ودرعا وريف دمشق والسويداء؟؟؟ https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91310" target="_blank">📅 02:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91309">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توقف العمل بمطار الرياض الدولي نتيجة هجمات اصحاب الأقدام الثقيلة أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91309" target="_blank">📅 02:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91308">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صنعاء بعيدة الرياض اقرب
اخوة نورة معكم ومعنا بحر من الدم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91308" target="_blank">📅 02:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91307">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91307" target="_blank">📅 02:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91306" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91306" target="_blank">📅 02:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91305" target="_blank">📅 02:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91304" target="_blank">📅 02:00 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
