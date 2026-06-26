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
<img src="https://cdn4.telesco.pe/file/uTaIMdr-YgfQFrpbEsWQClbZ-9T7MzWhbMPkrZ21uNNbmEsn5zwmaCM_Ezgv24m6qICRXvAhAa7nxXR1f3ypexwniP4w3h33b7q7FgpsVbKBpPlyJp_J8EWpNWmbodwKsEECjj68v8jEg7NuSxTPZXu1FF4_7UnGmwpsRX3YY0s1UP8yQkTWq_jvX4FndsgB_nyTKu5hxqjQlY-OQSNNJx2BvrwQx6_NqzvlorHJUl1VztGjNNMjJWbf5dV1DkuiN4VCfZC9m8etrI9bl1ygNdil9iAgbNJoZSfQnvF8oxwBvqs_LkFEtTau8a1ytZJSlxzyvuCw0407_w7BVGlxKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
حزب الله:
تنفي المقاومة الإسلاميّة نفيًا قاطعًا ما نشرته جهات رسميّة تتبع لجيش العدو الإسرائيلي حول سيطرته على تلّة علي الطاهر عند الأطراف الشرقيّة لمدينة النبطية.</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/naya_foriraq/79969" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
‏الإعلام السعودي: إعلان عن اتفاقٍ إطاري بين لبنان والكيان الصهيوني بعد قليل.</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/naya_foriraq/79968" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvelegl8DLp-9z0ECZ_njRY5sIpgCyxpjpemfnzEWRJ0QwgCWsgUqgCr28buz65BEEaCt5aTVUX0HulnsbpFTswmbbCy6vhoenCJdhQEdHxvMZjvF2d_mLsG6ZQ9S9SliYaAb3rmpEJI_ODopKs1rVzTQ9n-3LXBNP-QWmFkGs23q5l_-hWeGFIH4UdA2EOoNT-zKV_-hRMnh7C6uJ6CD56di3Dj6a2HbpyzddFgrIbK_023r8zgh81IRlR9StjsDR8Pm0MmGPenKmY0aychHAtLuHxPdVGE2BsptYAlweblj16lsyDjWPP7t8_rHS7U1Yirsdyk-Y2hiVjuzc9Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.   ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.   وقد أسقطنا الثلاثة الأخرى.   من الواضح أن هذا انتهاك غبيًا لاتفاق وقف…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/naya_foriraq/79967" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvBp5kdY1-Yn0aVph24_1UjkZyGvbHXJ-469oLiZrJKtVLnh2eSvYSD4B66bbwM8631vvQ3jL-TijNhEtcSa7ixcP363QnGpvDZSr81NxmAHUcsylmodgOW47RTrhazOhGCSls0R3AyzgvHCEMAIHGR5cSjdAK9H_glzJA3GsDiTzDQ0zFIsQ9EiMv6t19xWJ0ouVhPcqCZljaj9vLejce7Buc8aRrEie_2xP16q7PjKkhyFjdaI49_ypr-o27HDRl0c7SIMXeBuPE8zQzNV3yqFEBlW-pQFpNRaRbhwLSnt8WfVF2vTyd-ZIgQgaDoKBozUKs2dJlMuQU9G2J537g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.
ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.
وقد أسقطنا الثلاثة الأخرى.
من الواضح أن هذا انتهاك غبيًا لاتفاق وقف إطلاق النار بيننا.</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/79966" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇶
🔻
Dear brothers and sisters, in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79965" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
🔻
Dear brothers and sisters,
in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join via the link below.
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/79964" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭐️
مدير عام الوكالة الدولية للطاقة الذرية، حول ما إذا سيُسمح للمفتشين بدخول إيران:
من أجل الإشراف، نحن بحاجة إلى التفتيش. لا توجد طريقة أخرى.
هناك اتفاق، وللامتثال لهذا الاتفاق، سيتعين على الوكالة الدولية للطاقة الذرية أن تتمكن من الوصول والتفتيش.
أنا مستعد لمواصلة العمل الفني وأن أكون هناك في أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/79963" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-4-JJnSGNh8Tur3cRz0Qt5ylxjksqfoyrROSMMfUeoRV-LkgXM4h7XnVjVXERBtsqGFFBJgefNkyqWQpNHUucufYl5agHVlJQzSVy2HFhn5FlZDOtw_pTDoCXzU6bDshojm5sG_OzIG7-0Pu7MQfLxLzzi3pjpyitgkQhUblCXNr_NG6l_oDapWfGIOCnPbbkgCRlYEhFovdvXZLfLILgVTL6t_9vvhxqmONfY9UuTjQpEo79xZf6cttqv2I1N9Fyo1_xzmHNsHuCchtC69BZzB6kggPYbOy1E0gUXnfGxofdH9ufFcU7JMX2GWYz4bDluRw6EoUCCafrpuKqVe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هناك شخصيات لا تختصرها الكلمات، ولا تكفي السطور لوصف أثرها. ومع اقتراب يوم التشييع، يستعيد الجميع ما تركته من حضور في وجدان الأمة..
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/79962" target="_blank">📅 19:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
مصدر لنايا:
توجيه بخفض إنتاج حقل الرميلة في محافظة البصرة جنوبي العراق، بسبب استمرار الظروف القاهرة وتذبذب وصول الناقلات.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/79961" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية تنشر مشاهد لإستهداف محطة توليد الطاقة الحرارية في سلافيانسك الأوكرانية.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/79960" target="_blank">📅 18:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
بلومبرج:
أخبرت عُمان حلفاءها الأوروبيين أن السفن التي تعبر مضيق هرمز قد تضطر إلى دفع رسوم مقابل خدمات مثل المساعدة في الملاحة ومكافحة التلوث.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/naya_foriraq/79959" target="_blank">📅 18:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
14 بحارا قتلوا منذ بداية الأزمة الحالية في مضيق هرمز.
نحقق في استهداف سفينة أمس بعد عبورها مضيق هرمز من المسار الجنوبي.
أغلب السفن تستخدم المسار الشمالي الذي تسيطر عليه إيران بمضيق هرمز.</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/79958" target="_blank">📅 18:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">إعلام اماراتي : انتهاء حالة الخطر !</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/79957" target="_blank">📅 17:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية.. هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79956" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79955" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79954" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVuZkTOOyOq_qe2gfubXohjlVGhQzC4ZSvk260D11NEWIf_VKlXtJr91QVZlBwn234x64kGXwLMNaxBFfppmR7giRZeJ3Wtx6T605tbbm8bRvo53JMk1rUr63qvzwTBqJb-7TgHDiP2lvPV1gfdesrXt_1EhFZMBjQvX3OYBm483Tc49UP5v5Ac9_Z3ZJBieVnQcO2CZbnVwORckNf-FJ0gG39USmxjhp6Bi1Nanudm8ympihYbKNbNY_5wRMafEiNPmLVl8SQLL2bfq9ff6tlXjTVXuxLpo2PUJburAZFSqZtpi9T9LaqPmZRylktudmiYE34YO5h3Z00jRJH62GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79953" target="_blank">📅 16:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79952" target="_blank">📅 16:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79951" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇷🇺
🇮🇷
‏
رئيس شركة روساتوم الروسية:
روساتوم ستعيد موظفيها إلى محطة بوشهر النووية الإيرانية في الأسابيع المقبلة إذا بقي الوضع مستقراً.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79950" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني ينشر مشاهد يزعم أنها لغارة إستهدفت النبطية الفوقا بجنوب لبنان صباح اليوم.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79949" target="_blank">📅 16:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
قائد قوة القدس الإيرانية قاآني يكثر مؤخرًا من إرسال التهديدات تجاه إسرائيل.
إذا هاجمت إيران إسرائيل فستكون هذه أكبر خطأ ارتكبته حتى الآن.
هنا لن تساعدها أي هرمز أو إطلاق نار على السكان. لا شيء سيوقفنا.
قواتنا مستعدة لإكمال المهمة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79948" target="_blank">📅 16:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
🇮🇷
وسائل إعلام خليجية:
أميركا تسلّم باكستان 22 إيرانياً من طاقم ناقلة نفط احتجزتها خلال عملية قرصنة في وقت سابق.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79947" target="_blank">📅 15:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKZUABDCXiTGkxJoNkmdiMR-XBwqw9Yy6sch9RGofw5sfq9m9L0x1evs2c-czo0N89ej3mKa3n_fEsYRQnw7-8SIvoweTzjkZ-OLUpN2Kewk18L8lgVVNYSbz_DYVaXbd6a7tMiesUAq4QfgdXboNznEXKofx9p7b6TIBj7pSeOwDHZuM14j_Gmakz187uPP2qp5WM32Es0xc_iwYbgE_eR2_H1VmwXFaxQENxOZpZ3ofsV_JkeAItKdCKpExtx9QdELkV6k_TM4Zw45z8ZcixePENnke_JVQoQwg5yijZEXPXo645LB0VTuTwcOeJcviNGtdOzJ0Tw4YIRPEz2VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين   مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79946" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين
مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79945" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية..
هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/79944" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_ixa7o7fo_OsDrwbXf3VP4P_8khOrKh2goxFef_mTh0EHbc9ZOLzeQ9MGLMRvFHoxE7xS__HWp6IjlHeXlm85fUOw9XnkognSGd0vbWzdAfY3GLNpPK4dRGGXCD4gfDBZ48oesyULPZgdG4Ehpv8wFt8xbZMGcpBX-QOrHt_4QdHvPbP4hBTbvx8uxVsQQbLVtbUim2x2DVG2dm7n4qCyTYY4_mBSsWDmjXkk4bnop7bnJjCIVefQLycwu1BaoB6bBtJpxcHskSi1JLKkdnC7De3Snid1lUu4mHkKNBnVIJLFptUZRoF5uzewtro7-nD2Y-G5YGET8olBguVCz6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4tqdv4v6kveyt6IPA3QRO9bWnEKW1wjSKspFmbfU5psyy15-Sw6vBrkOkWrZtE-H3oqbPqc7Yc7Cvgn4gkxEJ5FMmn6z0pXHB4qeKxnxKs0uquejnx5LNZK3Dq-VPHj9kTUny9V_EPNFgaBafFrF4-yTjHZJ-u5JeLeuwTEKdC_ygplUyYuRCLQzduh40h7xSgqca0aumEYomPI7QFZ0Buzl90QtAioUMLBuf5NoivvNS3UayykA8I8Xx0rgSGEiR0z0q5gKZA_Ldr69WlD7zspaqadGWM4FdO-YAFN9pGaryHt5_MgdYPYGP4nN_D1x4b6Lr2HxTVgnON_i419ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnccruw24B75b-VZcaoetXqJrYHJl11z3ArhRqIA_8HQpFKGjRSHiNw7J01PLeqvf66S6RH0WrQRzjUZJxrecL7qBw7SKRNzHd5Zan7xb1wLfDpJMa7mztRinPVuT6YcCx6VruLS39m2NPYJZXAqVoKgPrpgEmriUCxHZPcu2sbwff9byO1zrOi9s0ShjrYzVNl4KbzV6iOcpigpoI1uJuxQ4qjWcz47maarvdAomZ_sd_apz01Zc4Suv0q0lC7J3IdMDa0L_p2JTpY97GB3nVBZxs3JRQ1yNe83rXMrlQviul1MSKXBvpU250dIKausNZp1NsCwjmHO4liGv9Z3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCCtSmdkpb_s7axGNv49wpZKNRmnyt5C3j4kvXcjFWmxu_qsi-cWlOAHBwalPusyI3pUFF6mH7WS63EQUTqbCfCrQQXlZjx804X_Qmcj3VATY56tmLR8Ap4BhwwQ-Sl1MgJZNGBNolaAC_ZlB78o9ZbF_wthjE1bE2k68iXN7c4S4ZBib4MGYBqntjTVtfMUB8NRb2q22GGDw770d8mURclwylSdnOdWSrvYYvH4hUClIkoRPQinoysHHWopxOndoYEHzJ9dhHdfMAtYseMQvhPh9ItFvzk3rVr1ws4i62616ot9sZLigbZatWYpBNHlnsxxIiF6GEDX6B0M8jRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWFgqtudkJmhjH7Lotl0MiXrvQLUcUeKPXV4AfSKeL9PJadhYiDv_PbGcAVS9v5wpjlHSVriE4AoNf7F6QCaSgh1EHepOOaPSyDNKR9V2nyieuej-TUAVfyqGUX53WdPd1Hb5xvqv3FEd3MrI0VEJ2KSDZN-0zL2lhfAgriEowKE3XtENeLwQxyRc3gv8rJfXFbTya0SjJkFV_dJV3uPD3fOJ3PZ5hZ2dQmbam9asDVBEk5CR-WuvRH_TAySqv0DhRf8DCxYG9O-Goevt21-KgGunPq4lSQSH58WBLLg9YJhOQMVacwI2vptlszBuxyBWvC6XaMS8QikBDYFUsD4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxVdw5DBLaFQuAaB33LdB64UbvYO3cmPUDbsLGHU75I7YEem4MtwB2-lqjCG3oY7Enc4Eo-t1ia3Rdu3XOHWaHF9gF-3chcEE6YGZXyJ5lGh0N5vQyEVwiMI9lCIN29xLx27hpCUCjwkMS3J7lHg7dcBRhjehK9aED2E-MsKOl2f8iDqkbdsDGXh3JYa3fw7KcHCV_AU0D771b4sQNiSkSnnVQNSiPITM5HpIHJmmuB4FxE6li8V68Ylo9FZbSifXEMgnTCsSYjahJiH79QX7BmI7rICVFXfLB42xuf9WfeoMidvQmGwTD5j7O9A4j4vC1cTNHVXRHYtf1qw6LveeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
تصاویر رهبر شهید امت در مراسم طویریج در بین الحرمین
#قوموا_لله</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/79938" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/79937" target="_blank">📅 15:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🔻
تشارك سفارات الدول الأجنبية في العراق بتوزيع الطعام مجاناً ضمن نشاطات موكب خيمة الانصار في منطقة الجادرية بالعاصمة بغداد ؛ العراق هو الدولة الوحيدة بالعالم الذي يشارك مواطنون من مختلف الطبقات ؛ الطعام مجانا منذ بداية شهر محرم إلى يوم ١٠ من شهر صفر اي بمعدل ٤٠ يوم كصورة للبذل والعطاء وتضامنا مع الإمام الحسين الذي أعطى دمه من اجل القيم الإنسانية والاجتماعية ..</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/79936" target="_blank">📅 15:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
🇮🇷
مردم عزیز ایران، ای مایه افتخار جهان اسلام..  محرم امسال با سال‌های گذشته بسیار متفاوت است؛ زیرا بسیاری از هیئت‌های حسینی در عراق، یاد و خاطره شهادت امام حسین بن علی (ع) را با یاد و خاطره شهادت رهبر، سید علی خامنه‌ای، پیوند می‌زنند؛ در حالی که روزه بود…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/79935" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
ثلاث ناقلات نفط أجنبية حاولت عبور مضيق هرمز "بصورة غير مصرح بها" قد أُجبرت على العودة بعد تحذير من البحرية التابعة للحرس الثوري الإيراني.
يمكن عبور مضيق هرمز فقط من خلال المسارات التي أعلنتها طهران.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/79934" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2Ohb_ss40YxciPUcqhRkFcVu4mUYdT_JUL5XoZRwWnE-G-yqkccu-UtsgSsSrmL58un6OopFw3Sm1FQONJDSIp4efpjrUmMUDC-cf6JhU3o9dvP4C31_cBkJDgyad3vfy-8KbBCQSwGEtJL5DkFA6ZjXnLT8wWeEfrfOCPhuVrkBtoQzc-Flc30PLMfF9CkvLWm-q3rhh6tpHyeLtTn-2PvXPx3r3ZD_3y2180PCQecKnfc2HbOs5FY9h0HCchZ65kkS0bIGNG7pH0vTXKfjSzPjZKs9aaMVJgV29EzpFxIr-WJUPwbCYIZF2yZQrmRGrhIh2Syi3zZRtJ30byK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين عام المقاومة الإسلامية كتائب سيد الشهداء "الحاج أبو ألاء الولائي" مغرداً
: ما العدوان على الجمهورية الإسلامية في إيران ومحور المقاومة، إلا امتداد لذلك الصراع التاريخي، وإن اختلفت الوسائل وتبدلت العناوين.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/79933" target="_blank">📅 14:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إنفجار عبوة ناسفة في جزيرة راوة غربي محافظة الأنبار العراقية؛ إرتقاء 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/79932" target="_blank">📅 14:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هاليوم هاليوم نعزي فاطمة.. جانب أخر من شعيرة "ركضة طويريج" في منطقة بين الحرمين بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79931" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من شعيرة "ركضة طويريج" الحسينية في حرم الإمام الحسين عليه السلام بكربلاء المقدسة، الرمز لنصرة الحق وعدم الحياد عند مواجهة الباطل ويزيد العصر.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/79930" target="_blank">📅 13:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايةُ الحشد الشعبي تتصدّر حشودَ المعزّين خلال مراسم ركضة طويريج، في مشهدٍ مهيبٍ احتضنته كربلاء المقدسة .</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/79929" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/79928" target="_blank">📅 13:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/79927" target="_blank">📅 13:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79925">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
حشود من الاف المعزين تشارك في إحياء شعائر سید الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/79925" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق شعيرة ركضة طويريج من كربلاء المقدسة بمشاركة جموع المعزين.</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/79924" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79923">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/79923" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM3VAFkJ0PCkQfoh6nh-S05mMKB3ZuhyJpO0iwS_Pj0d6v3ayMLtSj0L7jWqrprImu4kSrJcIPs-XvUI7I3TgmnZuY_SnSiisuYApfhqf3Qzk2kXkuSTr5MpAL6ZepDBaI0LZDHtMuOGyxB_kKjUpBxqWfTU3_7NnaeQxB-hQ3lar6UKWFsapT5w_FpxrbvAwiJyuSY5IZ_30BL-11P6UuzNAyOXKSoQ4RYOpxZ21d97glTVXnetCtg3_StKu54QjKr7qdayNwP078FhEzdX_SWLv_lWaiz-GDYUFW0WOaa-_oZ9PLeiQ7H1zArBk8tkAX9_i25TuaSidce5-apbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/79922" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79921" target="_blank">📅 12:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEe-wqUY7fN4NflqM7CIreZdh43ju413muvemM4oR5CkD5bNbsIOwG86Cl5ohUPC4jH7FCBGjbrzCL4hketlmqMFdQQSG2uMccDOwSVj9dJPCq6jvQt92znU-C-CUEzULtMlx9nczrifkKFj9rhFvOZ6qwma-gsoz4eFhxdA5e4R7vawnRSuL2BCHJqUvSSdWDZaa6QCXm5kDhDoAQBUd3o8cPIQfEQ3Kqf0H9cukdHk62SHQF19YSGLIX523wc7wvYyPh8kVzQ5yWk0zeJzKXfH1xtX0HxAq-pl_LAqb391hWoOBbZlcl0Mt1fsqp7l8ZnXdMCx0OD5H5zR2TQ-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم ، كن انت المراسل وانضم الى فريقنا
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/79920" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0-mDi-UN3NIhOwMpw1OLcYhNEQOwOGujvac_HH0uPFptFMdDazKQzqu-tTch4MLPzs8VWfNU7javYXFy47bD7ddCElYdYOwZvF5r0E4iA9kLVo1Pu79_a9Q6RGCstzArMqbuInMQHZS2Mtb2mlBXSwkZeV86TbmDawgM7p1ke3JPVQ9-hmCZuQy3yMP3HQRAOJjmtoXUhLrvIeEZfJVr0AhUmTS7H5ZSnulRJY88_a7x5lYyrn6Jj-WaOS-B78rKXtkFk86V-1Bn1r5SWD6hs3gFaRt_ZWAWypz79S-lSKLTRfpQN3AvcGuFmL7qs8Wm7RRwCutRkoJs4_VH93krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQJTEOrvQydf3th1DmyaksAtwDbmNL21hL7Vj7YTtr9Mchu73P6e3gqkSqRuoVt17nXNzoWnCqRe4cZHS4rmryELaGS2FFVH8jTGGIrn_nW9QqpKRNYdTa-JjwYpDc9eG_TT99L6z08jC3zZfDhjanBY2jRZH7h6pCNncwcPFC5XmG3h4FknZBR9ScYtGl2oBM90WZOBmTH278avCmTZy1NJuxSKtmlYZ5HJT7WWVxhWU-ONzvdHl6IwvHdDcJhSNsYWq0Tq0QY6x_AovnVczXTlx_TKIg6b8B8f72y5IvQ4fKL_RrNJbCp-EiqRD02nOapVZLZ-DD80fIWaC8RjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeNBT9A27YmCSETZt30k-_sA8hnU70-19YEOdYCIjB4g3hltrOKTiCcXGP1JzOxBWrPsXq7lGl76tInTaoP_eqjqTl3IZpzC8aurIL481IGrAH8kNzbjnhvRIT8vP4GbJwS7_E88fVyFTr2gEi5LtYiTZVrk8eX8BSytP3wZHWv7kQGCtLCMjt9OU0EckSI1ICcrP_W6qvLdNtHjMFxz7a0_qMKguiMIRiEAocbVpRUpS_NzZeIejsAhLmfvp7m_-7AXC-yENHJs2XX9rVnasCsW8kz5YrBRkDz4_TU61DQlsnKGxatOYq-L8RlMKMwp2pkIIyWPMlCCWEKY0olRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zq36gUR1ELdDV2ptKab9id6JgiqOroTMPehqBlIT7BhQfF3A_T6DX4PQ5jImKakkS3V2FL9PRZ_m6AlL67xdR8QYsqMNxm6hLVyEMtMyaTdyhYMI7BrXjooOV6YQbEdpq77Zpro0EeAosMvCIQ7-bmyI9OQSZAkpooTWi7VtLId325HMzKa1DLpC_j68rq8lCVFufL8qg685xVtBZlQ2832nyqlVNz4UJXMAk4ChfEqZYr5N3rQcALDeyaNkCCfOpA7Bwb2QcqC4-_OKp7HrrIrx_Hler9vx_zHIZIbp7rrAo-81oWACmRs_zIwY8qWQwcXFI1xhkZ5r_yWcGFinbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد إيمانية من داخل العتبتين المقدستين، تزامنا مع اقتراب انطلاق شعيرة ركضة طويريج.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/79916" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=ifx03FVjSTnjoy-MQ5NrSu7AVzK8ZCHglapfuLT3Rq04D41Gkgpf5pq2TESmCkHZbtSJ5SA287FcikjDKivjLi7JQKde7BmxJmAZPS36uQws1Jgm0oHPsx1nKl1XmUHlHYEqsXTZ3P1WOECiZXAYt6NtdZpZJAe4yBIiMGEArIGkSgmnvHHpdZEbkfANqr9rfth7E_e_qmIdMfjAJt1fgKWOqAWhzOrTqLDN_tt6LcyDoieh7lJtJA9q__P2euq6IE-5su7MIa8Omboe4lLtBnV7P7J6NBUEWYvE3DOousTWmBizsy8WxGDUIC7EOfCwCxerPIdMzMQ_M9QzwpG9koghEg2loDojv7wQdpxvdrDMY9I1qRWT5GnhNjbWY397fZSTHnHe_5y3B4ibSO7TkTVtEMUbbxTAMfQJ3vYEsfXiNrIqe5uWj9ikxav8AsVfE0JyhSV-7LwT2vIixhR5BDNzcGKELr51Pqk4FK7mMuwRNy77qqg-L4XMvJo0BZnd-qODlDYm3HyT71HQ-eKuWv2mN28pQP6iI-swgeqsZn2-FpKqdfotPan8PScPTEuULOFuPKSmxmoxeRC-LjeE4CK4MsS59L5IkrAaacvIo9mq0kPt80F6-ugNAzeIjWy19CU8LikBZZJoJnk_ciQBdR1OKZcBOKZUvYu2cIPf9z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=ifx03FVjSTnjoy-MQ5NrSu7AVzK8ZCHglapfuLT3Rq04D41Gkgpf5pq2TESmCkHZbtSJ5SA287FcikjDKivjLi7JQKde7BmxJmAZPS36uQws1Jgm0oHPsx1nKl1XmUHlHYEqsXTZ3P1WOECiZXAYt6NtdZpZJAe4yBIiMGEArIGkSgmnvHHpdZEbkfANqr9rfth7E_e_qmIdMfjAJt1fgKWOqAWhzOrTqLDN_tt6LcyDoieh7lJtJA9q__P2euq6IE-5su7MIa8Omboe4lLtBnV7P7J6NBUEWYvE3DOousTWmBizsy8WxGDUIC7EOfCwCxerPIdMzMQ_M9QzwpG9koghEg2loDojv7wQdpxvdrDMY9I1qRWT5GnhNjbWY397fZSTHnHe_5y3B4ibSO7TkTVtEMUbbxTAMfQJ3vYEsfXiNrIqe5uWj9ikxav8AsVfE0JyhSV-7LwT2vIixhR5BDNzcGKELr51Pqk4FK7mMuwRNy77qqg-L4XMvJo0BZnd-qODlDYm3HyT71HQ-eKuWv2mN28pQP6iI-swgeqsZn2-FpKqdfotPan8PScPTEuULOFuPKSmxmoxeRC-LjeE4CK4MsS59L5IkrAaacvIo9mq0kPt80F6-ugNAzeIjWy19CU8LikBZZJoJnk_ciQBdR1OKZcBOKZUvYu2cIPf9z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/79915" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/79914" target="_blank">📅 11:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk3xP6sfAScrCOCZRmk-IHHe6urRVdvK1-SOLDYqNL8Fzw3HgHeO-ZCq3lktU1ZNyD398hUOnw-Nt-qk5LgnavNpOPxbNA0HYUjPCGzhrz-vpufYUwD8wEv9G7fp4-6p9vOBujA8JnXaazVJHFAEFikpD25_nQ7zbPmJTJ-0ehjVPV58zz3rh_B-3qgpOfR2kWaDphu4oT6UzizXmbmnbQswYFoJq1kXwqfXBi6raMYIVFus7l1t7lDhR1WqGgTdSOg2XYUgJlh7p_sDwp-UCDEcsgkrz3bwCox_VFf3k0_-or5gd_waR2WFnoGjFe698GfNTZ-tOS-7pRLms0JAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية بشأن البيان التدخلي لروبيو ومجلس التعاون الخليجي
تعتبر وزارة الخارجية لجمهورية إيران الإسلامية المواقف الواردة في البيان المشترك لوزير الخارجية الأمريكي ووزراء خارجية مجلس التعاون الخليجي - بتاريخ 25 يونيو 2026 - تدخلاً غير مسؤول واستفزازياً، وتحذر من استمرار السلوكيات العدائية والتدخلية في المنطقة.
إن الادعاء بـ «الالتزام الدائم لأمريكا بأمن دول مجلس التعاون الخليجي» ليس سوى كلام فارغ وتحريف للواقع. لقد أصبح واضحاً للجميع الآن أكثر من أي وقت مضى أن الوجود العسكري الأمريكي في دول المنطقة هو عبء على شعوب المنطقة وعامل لعدم الأمن والتفرقة في المنطقة.
إن استخدام أمريكا للقواعد والمرافق العسكرية الموجودة في دول المنطقة لارتكاب جريمة عدوان ضد جمهورية إيران الإسلامية خلال الفترة من 9 اسفند 1405 إلى 19 فروردين 1406 أظهر بوضوح أن أمريكا لا تعير أي قيمة لأمن دول المنطقة وللعلاقات فيما بينها.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/79913" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم: - تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.  - عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.  - سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/naya_foriraq/79912" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم
:
- تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.
- عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.
- سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين في الميدان تساعد في إيجاد التوازن المناسب لكسر "اسرائيل" وطردها من أرضنا.
- لا خيار أمام "اسرائيل" إلّا الانسحاب الكامل من كلّ شبر وأرض لبنانية وإيقاف العدوان الذي فشل في تحقيق الأهداف التوسعية.
- أيّ التزام ضدّ سيادة لبنان لن يمرّ.
- سقف السيادة يمكن تحقيقه بأن نبقى في إطار اتفاق 27/11/2024، على قاعدة جنوب نهر الليطاني حصرًا.
- المقاومة مستمرة بوجودها، وحضورها، وقرارها.
- المقاومة هي عماد استقلال لبنان وتحريره.
- لا تستطيع السلطة أن تعادي أكثر من نصف الشعب اللبناني.
- على السلطة السياسية أن تعيد النظر في مسارها، وأن تعمل على جمع الكلمة، ووحدة الصف والموقف في مواجهة العدو الإسرائيلي، وأن تتوقف عن تنفيذ إملاءاته.
- نحن جاهزون ونمدّ اليد، فانتهزوا الفرصة، فالمقاومة قوية.
- هناك ضرورة لشحذ الهمم، وسدّ الفجوة الاجتماعية، وإعادة الإعمار.
- لضرورة الاستفادة من مسار التفاهم بين ايران وأميركا كداعم أساسي للسيادة اللبنانية أرسلها الله كهبة.
- لقد ثبت أن إيران طريق الخلاص.
- كفّوا أيدي الدول العربية والأجنبية التي تضغط عليكم للفتنة ولمصالح "اسرائيل"</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/79911" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=INKZ47Bh3JuSSifDva62QgeJrjtZYLkgFvYqTqxictNi4X4REJGMdteYh9tlyJW-iTvdzTyIzYKeIU49o3JKk7fZJC2E1Lvaqfmuijzjb6wlmu0kYIv2ZUKQeY3Id9E4W5YZF6duT53MKOSva3EwZY-eWP6WkmmOq-gF759KRDsfcwzjCSQjyprRdBtAKARKaL2p-ZhLw0hjwX6JvQNsk_vt3RF-eMqsuzyAke68WttA87K57VFmoLj9Dg04huEOZQGVlnHlMcFE1AychIsbnErvyiG7ULI4L8uTaAcflQrfs1a-J5eRnRWY9ZCjhpzVu4QDWxWvska3p6haVj8ymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=INKZ47Bh3JuSSifDva62QgeJrjtZYLkgFvYqTqxictNi4X4REJGMdteYh9tlyJW-iTvdzTyIzYKeIU49o3JKk7fZJC2E1Lvaqfmuijzjb6wlmu0kYIv2ZUKQeY3Id9E4W5YZF6duT53MKOSva3EwZY-eWP6WkmmOq-gF759KRDsfcwzjCSQjyprRdBtAKARKaL2p-ZhLw0hjwX6JvQNsk_vt3RF-eMqsuzyAke68WttA87K57VFmoLj9Dg04huEOZQGVlnHlMcFE1AychIsbnErvyiG7ULI4L8uTaAcflQrfs1a-J5eRnRWY9ZCjhpzVu4QDWxWvska3p6haVj8ymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ازدواجية المعايير في ابهى صورة لها:
في الوقت الذي تُنبش فيه قبور الدروز والعلويين في سوريا تسارع جهات سورية تابعة للجولاني إلى ترميم قبور اليهود خشيةً من رد فعل نتنياهو.</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/naya_foriraq/79910" target="_blank">📅 10:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء:
نعتبر تحركات ووجود الطائرات العسكرية التابعة للكيان الصهيوني الإرهابي في سماء بعض الدول المجاورة باتجاه إيران عملاً خطيراً وتهديداً للجمهورية الإسلامية الإيرانية.
نعلن أنه إذا عجزت الولايات المتحدة عن احتواء الكيان الصهيوني والسيطرة عليه، فإن الجمهورية الإسلامية الإيرانية لن تتسامح مع أي تهديد يطالها، وتعتبر من حقها الرد على هذه الأعمال الخطيرة.</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/79909" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
مرقد السيد حسن نصر الله قرب مطار بيروت يعج بالمعزين في يوم استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/79908" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwi2RNAmTBdik5ebi0qgla4tubMuSCZffKNiAqCf9qQbqKYoL-GWv7sFKvI5EITrpWoXofBpolqlX5JbE-F3bMl1y9vxMnc5EGM6lGdL0eQ4pOxprUnoiB_dI7CshwKHZhAHCRv3csGgtERtsjVHrXVWIU3mvWpBiXTy1Cejhkns0T7xNTiKKpa40i7QBuxW8TBFzZI7cBEk2c3_RKM5XcGD5JDSN1CVVZkfcnT8_jmP9gUma3CIjQvURzTVhQxAsU__41BZ2YKMiihiY_jhzvQJigl8h95R2Fi806xxUI5JBwoVjBDp_p5ob9fhTGXJwLJ0x3Vrq6u4XI40P2JBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RggLVAT_WkWuwYQ3GnjGSOy0Yx4L2u8sZBQAvXhRpbEujY9yagjbLdnAZb_rRsm3kfxQe1VL44-qzYaT50Up47ySOnoQ7ozJMt4PBWnxubgKafD62sRRcE3zCm9v0R-1kMFS9UvgmqJ8b7dwRik6cznCQkT0EosuXdTaTgubbiMC-cC15lIFifeZS07wtyPIECrtppsjL7onY0apVtq0tjFI2tpIWSKsEUujle2rugyJAgJk92tz566eBo7pUv2LLjgoyZTw7InVZoAkJlo2bXJ7J4fTOmx8gKWTBRwmVxN3dnQ7EmlxSEgETaqbHOSH0SQUn-hZukrecH2aAW9KRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ma8WVfMa8JNWch4UjTiE8PScXcer3vlAujSC1y7FYg85oXuYEhTG39JAl_mtYC5fCBmn0yJkGGqVWYQcAEfsWsRGRLFfyPlDjuvWwvmWOQT6EKW3qnBBvFN19o3JuVPlPPtSE1TzrL3Ov0PSVaxyEkoRSHyVOt-RxgSG8mfPwi5jTo7zamHiYAK_DnQ_127F0fmG01SgDszWNc5ey-6K-7lsCQ9Lv2hkMra6r2DykNbLSXeE-Bne2U5tgb1JQe8REV2DUD2efDQaR3wTZswuQvurJSOoHRgCpcNI_J7NWwUjbt8wI-NezwNRhDyd1aSVKw1nK8BkxnywEVa_1dq5KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جموع المعزين في الصحن الحسيني الشريف بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79905" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAjeLDH72jqtR25q75utPw1umYuH22tmCTHBhJ1rO_YJfZ6NuftjXa2jFZoAA4S82dv3eOV2XbBIymeBWMldOH6dhc5iitj6OHVm8mWW-lSClrnNzDaa_Va4Mym9zAfm1NPkVaXpgXhQ8U14hHKKj-jjkKp91INNrHHeTCzqj_wIh839HBiSy94ODoCBZScDGaY9-ZgGUh4xPB22t_748-mpxAEBrhIX85pOyitJwZDN_XklK2DEq6_NvSIDo9Xju1kc2tK3q7pYL0hPun31ideabg3DCRgycUWfBV5CaXWAKQu3oknwZDRU5Yp5PwvttmP-UoqtjWB733Q3OWlxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
أربع هزات أرضية تضرب الحدود العراقية الإيرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/79904" target="_blank">📅 09:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79903">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=HrQ6zSd9_VWLSbJyOeQRbJbIYWrpSZNo2S9QguM4T0FFhmv17fduulizGA1tnmNFShWyGcGkI-7d_m_wSm6B3Xqlw8lXgMbQarkZ1WqKlVjKtInNfKPTMgsyZhWBNtVCD0txdpPCk2VZDyBCgJSA-qtthdnhsICq4_oGpyFgzaQh5ZOOszwDr4yMxnzD1tbFyQDpnJ4kSkjwOwt7E3csxUxdQbMJw99v323ligefy-knDIBun-k0NAZN2C_iIfXgr_ftuCJgPDXw0xu6ixPu1elb17k3xLC0uAoUFloGQsaiMIqYZrq8D1MEhfh4GD6OaZaGl2bfRQ91bF6zy5-29CkbaXHFb-1RLc1OphC8nuUKZKDn8t2VWGeCPL3RqlXrK2OUc1TUxSrgje-5lcf6a_1VQVpPyAAQCjBPpOOkaKiC9XUqIunOXtTa_M1K6ZNqYJqJ_M7Z24whoPD-XND12ZvTGnwG42mcWanUpQsK3YpOReRKiVFpuVSwKWpBvpTuA89ESddC4f8KMCmgpdpjYhwhDXjLYZzasG2yOGgZhe2nJIDQFhO3XHr99Uz_WSmCYXbFCa7xPwoFBzBXKXwhWYO9YDxXOqHsDIxvNW-NzNN4-U2ab3JotmxYXXiGEGrtjKKuhb9ISiFunpVlPHZNGuCGHcty4m1qWNhDlxnhyvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=HrQ6zSd9_VWLSbJyOeQRbJbIYWrpSZNo2S9QguM4T0FFhmv17fduulizGA1tnmNFShWyGcGkI-7d_m_wSm6B3Xqlw8lXgMbQarkZ1WqKlVjKtInNfKPTMgsyZhWBNtVCD0txdpPCk2VZDyBCgJSA-qtthdnhsICq4_oGpyFgzaQh5ZOOszwDr4yMxnzD1tbFyQDpnJ4kSkjwOwt7E3csxUxdQbMJw99v323ligefy-knDIBun-k0NAZN2C_iIfXgr_ftuCJgPDXw0xu6ixPu1elb17k3xLC0uAoUFloGQsaiMIqYZrq8D1MEhfh4GD6OaZaGl2bfRQ91bF6zy5-29CkbaXHFb-1RLc1OphC8nuUKZKDn8t2VWGeCPL3RqlXrK2OUc1TUxSrgje-5lcf6a_1VQVpPyAAQCjBPpOOkaKiC9XUqIunOXtTa_M1K6ZNqYJqJ_M7Z24whoPD-XND12ZvTGnwG42mcWanUpQsK3YpOReRKiVFpuVSwKWpBvpTuA89ESddC4f8KMCmgpdpjYhwhDXjLYZzasG2yOGgZhe2nJIDQFhO3XHr99Uz_WSmCYXbFCa7xPwoFBzBXKXwhWYO9YDxXOqHsDIxvNW-NzNN4-U2ab3JotmxYXXiGEGrtjKKuhb9ISiFunpVlPHZNGuCGHcty4m1qWNhDlxnhyvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً  إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79903" target="_blank">📅 09:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3pM-euAlILZjlcnZyPr3xD9aQWvhrCaCkKipKdQb7uK6VYsa55vo6gyMRtiqa8t-QHyrOyArMVkPrF9_tA1EZOAGcZW7OtR9-ZDRsyJFeoi1D_yVFbI3JYrm_xLSpJDBI63jJSD-RWg-LzPhfDsdsozyCNogEdRu8fW9MQypLCuYlA0UrRWmeBlQP6XKD3qrNQBPsGb39uzNA9fNnZC8eF4zoESAPdCh9ssmZI5J170ln9VZQozvPAMic-6sYLtJCMzPkpn4olagR55aYGKKfHa-bbohgVXraivemB_iAs0KMjiOa9p4YRTAnM3Q9tj8tchYIUzdVGPA5tZYvjj6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدة نييورك من احد المواكب الحسينية يستذكر الإمام الحسين بن علي</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79902" target="_blank">📅 08:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLYO4DQcxODKHj4CgDZ_Ty7k-tp9nAJHmxwDfz6CnqMAUMqGutVOs9Gil0S5v8batib_Fj_qkEulUE_M16Q0ZvgSJCnzBt14F7vVMFFrqmdn0PR6K_cNMCldrC_WLlAojthy6oMqpqZKpZFrBdoPa2xxOa-66Zgr2nU9gfHzmLOYRTtaa1Unj9hWbaf3wvVgWh0yPr8sre67n_q0VXHJauqe1dlGuPUxHfmDZxLOS_SuupqPOJ8MXGsNjuaq6UgZlJkXA9VB34sB4lRWXHbryyrsZaitdxOYeJmgFTA8LeJinjP5KN9vQBsvR2EwlgNtBoc5IsYdCBNVG5lWdua4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM8i3aFAoJXu8nP8BYOyLOFGHTHiZ3Tr7Y5DWPIv5j2mIvdXLJuFKfKElwl0PuYFWzJkbPJuZltEMYKSdmzHZmhNgsAMMPiFC0d_sA0uFo3ddKAC72ZBs5kjIJOormL9gv0ewSEjHsx5GpQskuAZHSJr0L-9240F-4rwltRiQdPnkmRKwAvzLYfZ7J0VBLuiALanzIe6Wx7l3AHaQdS0AXGl6DwR4WDEyuRvJG9DAE-GIqR9nE65B4Cp1aeLRDk1PEuZxdgdsPm70As8KilZgS5TXoY81gu2b_QEuLSYvXpJkAF7TYSVO9mzFaPq6Rjb2lXt3q-g0AFP5XYpXAe8AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
🌟
رغم إعلان وقف إطلاق النار وأثناء إحياء العاشر من محرم الحرام.. غارات صهيونية مكثفة تستهدف النبطية الفوقا.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79900" target="_blank">📅 08:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgL81fizKe4YED0HH-x3BArg1yN2Mkz-L1rKaqU9qu5Qo1bV8yZrKQpEoKqzjDkBSKA6b_-P5C8zs_puch7ef_tIY16yNUm1_TK21ecMyk1q-c9y3dF-r0JsAMY_nm4AHDsNVz9s9FKhX5yYLpdLscDUMG20SxB7ix8TrHNtFFF0lQwZ5NrG3fROG9CMghlmcj3wvBhP7f3wHJGmi8OczGAZXDWT7XsrK5frdZyKCphQ-O7bBJlxnoDMoliS8Iu6wb9s2Q2yDWfNFQO2L5JH9KcyrfmSrTUER2elp3DjqPcgORbv30H2zfWEZxTh7I4i9l20wEUnGP3bRXeqAYWbnha8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgL81fizKe4YED0HH-x3BArg1yN2Mkz-L1rKaqU9qu5Qo1bV8yZrKQpEoKqzjDkBSKA6b_-P5C8zs_puch7ef_tIY16yNUm1_TK21ecMyk1q-c9y3dF-r0JsAMY_nm4AHDsNVz9s9FKhX5yYLpdLscDUMG20SxB7ix8TrHNtFFF0lQwZ5NrG3fROG9CMghlmcj3wvBhP7f3wHJGmi8OczGAZXDWT7XsrK5frdZyKCphQ-O7bBJlxnoDMoliS8Iu6wb9s2Q2yDWfNFQO2L5JH9KcyrfmSrTUER2elp3DjqPcgORbv30H2zfWEZxTh7I4i9l20wEUnGP3bRXeqAYWbnha8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً
إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79899" target="_blank">📅 08:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=UcukNfatmA6RFTE5TCkHbFeNE_peouJv8ldo2FHUvLixOBtXiqPukZCJYmU7_ecAVVb7vhnUCXDMx5kVYgtD7XSTHneyUglw204bUpFVuRhw36X1i-ACEUSd5laX-2c7_-Pt5lOphQOxhI0O6x7GhCMXsyzeyIB_SzXgL-UXILqUsP0H85UIEDsbS8LEb06u3YKmsQ7eEGhG3b7ZalBPKCP_kr8LW58U8NITpsPpZklqz5WUOhhzYmgCOlzjJUVz-4xGk62d6Gg1KUY6-h8jSpTYd9KOzxBMAYLEQNKIGWOrZlDUyobas6RhogVOm8uRQxKAFUS_CJh_6mWC3QXooq5hxRQL2lm4CSJpjHIbsKko8t7Q36fPVwgHklPwUFumaTTGgizj0e_EwR8YzxAZz04YqwAYN3FyyKAn5hLWaI8x8p_Xdrj-3Kwmh5NJx4xo6AljrS8o4hBXJBB8QYrkUA8NwpXYWel51cItKpVrTJKPKX-z3dzWq1n1I8o5919O_Uvyk-4JxIiXOngZcGKkFeXaDsGtrccC5yYY5kycnplrT0Z9EwmszAF3sANsfAcJcGp76HF5zjIwTs_09AGyhMvtR_urBkDRvFcPxetRo3h4CgQyV8jKsuqVy1E9g5q3gSe5IL4UmeTw3oO4K-IyC_gmV7M8FzoY-J0YRGEl8ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=UcukNfatmA6RFTE5TCkHbFeNE_peouJv8ldo2FHUvLixOBtXiqPukZCJYmU7_ecAVVb7vhnUCXDMx5kVYgtD7XSTHneyUglw204bUpFVuRhw36X1i-ACEUSd5laX-2c7_-Pt5lOphQOxhI0O6x7GhCMXsyzeyIB_SzXgL-UXILqUsP0H85UIEDsbS8LEb06u3YKmsQ7eEGhG3b7ZalBPKCP_kr8LW58U8NITpsPpZklqz5WUOhhzYmgCOlzjJUVz-4xGk62d6Gg1KUY6-h8jSpTYd9KOzxBMAYLEQNKIGWOrZlDUyobas6RhogVOm8uRQxKAFUS_CJh_6mWC3QXooq5hxRQL2lm4CSJpjHIbsKko8t7Q36fPVwgHklPwUFumaTTGgizj0e_EwR8YzxAZz04YqwAYN3FyyKAn5hLWaI8x8p_Xdrj-3Kwmh5NJx4xo6AljrS8o4hBXJBB8QYrkUA8NwpXYWel51cItKpVrTJKPKX-z3dzWq1n1I8o5919O_Uvyk-4JxIiXOngZcGKkFeXaDsGtrccC5yYY5kycnplrT0Z9EwmszAF3sANsfAcJcGp76HF5zjIwTs_09AGyhMvtR_urBkDRvFcPxetRo3h4CgQyV8jKsuqVy1E9g5q3gSe5IL4UmeTw3oO4K-IyC_gmV7M8FzoY-J0YRGEl8ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من إحياء العاشر من محرم الحرام استذكاراً لفاجعة الطف واستشهاد الإمام الحسين عليه السلام في محافظة البصرة جنوب العراق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79898" target="_blank">📅 07:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=Plx-_yQyCdGMkeoxKjCR-1tcVuccail8wAcvxq3CoDe_p6SqO43atiDD9CgpGPhR1hB2CVDK1rnD2IydwIuAmVsKOVAP51RQZ0b5NRbOo_uvE66Xc__NcLyglBG5HXkc1usX7kA-BYrXmUe4kyxJxNOsxKUHwjs5UhA484BAIspOQjuCINj33MCee_nQJ4c0EqPrHLI-O_BPn7pNkGJcqbWw34tz-cIwmHY3GvjNF0fwRoGAoVEdImjjXwRqp_d4wsL5XyGKYHyhK7v--bua5S2GG5yy7FWNrCyZzi9sHZaicL8sxpBmk0wx6kvzMW4h06qlWS5TCkMW58aKP42aUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=Plx-_yQyCdGMkeoxKjCR-1tcVuccail8wAcvxq3CoDe_p6SqO43atiDD9CgpGPhR1hB2CVDK1rnD2IydwIuAmVsKOVAP51RQZ0b5NRbOo_uvE66Xc__NcLyglBG5HXkc1usX7kA-BYrXmUe4kyxJxNOsxKUHwjs5UhA484BAIspOQjuCINj33MCee_nQJ4c0EqPrHLI-O_BPn7pNkGJcqbWw34tz-cIwmHY3GvjNF0fwRoGAoVEdImjjXwRqp_d4wsL5XyGKYHyhK7v--bua5S2GG5yy7FWNrCyZzi9sHZaicL8sxpBmk0wx6kvzMW4h06qlWS5TCkMW58aKP42aUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79897" target="_blank">📅 07:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=rh7qYnf3NIyNV2oS6EaGqULirvc2DRFUaGDZN0uyWThlHDhLGMyqJaerrCbGdRHgOn69TKjq0CLZBU82o1wEsN49cO9HeAKrb-MhBtkrMHRUsRMGDiZPrb_Ue2wE9lrkCh10QMiwDv-hwJnpS7ELy6a24_mH3El5gEaijWgLYkjIJu42dXNlI3fGtncEqGNZAbTxWZncBi2Xv2tqhtYFkH0awZYh8ICtOaXIVRgkg7GBRupJWW-XOaruJsf-9mOOJ6SNgcMtXCAMWMYxw_ZuDuho7KZnySU99QQCn_ULNjJwmq_jtFxJsnHkdk5ZCpF-JQphRQUxmZbluDezAAlbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=rh7qYnf3NIyNV2oS6EaGqULirvc2DRFUaGDZN0uyWThlHDhLGMyqJaerrCbGdRHgOn69TKjq0CLZBU82o1wEsN49cO9HeAKrb-MhBtkrMHRUsRMGDiZPrb_Ue2wE9lrkCh10QMiwDv-hwJnpS7ELy6a24_mH3El5gEaijWgLYkjIJu42dXNlI3fGtncEqGNZAbTxWZncBi2Xv2tqhtYFkH0awZYh8ICtOaXIVRgkg7GBRupJWW-XOaruJsf-9mOOJ6SNgcMtXCAMWMYxw_ZuDuho7KZnySU99QQCn_ULNjJwmq_jtFxJsnHkdk5ZCpF-JQphRQUxmZbluDezAAlbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الزوار إلى مقام الامام زين العابدين عليه السلام لإحياء يوم العاشر من محرم في سهل نينوى شمال العراق.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79896" target="_blank">📅 06:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-text">تمزقت راية الحسين في طفّ كربلاء ولكنها لم تنكس، وتمزقت أشلاؤه ولم يركع،
وذبح اولاده واخوانه واصحابه ولم يهن
انها عزة الايمان في اعظم تجلياتها
السلام عليك يا سيدي ويا مولاي يا ابا عبدالله الحسين.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79895" target="_blank">📅 04:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
كعبة الأحرار كربلاء المقدسة حيث ينطلق معنى الحق ومذهب المقاومة ومنها تُستلهم قيم التضحية والكرامة والإباء لتبقى منارةً للأحرار في كل زمان ومكان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79894" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=oqAV17L_hsrpr5DVECa0-Dqf8V3u6drMpDlpfG7Gm0pmFBxW2PDtFDOcyEnfYmwlCy83m5AZvEpCze-hOlK95hRss29TsQhElKv_6qCnHUYLSSLpGesZQ-E-0UQz5bNR6GYO_LQ6j1xldde4JTDCiTinyFKDZf3TvyEWLx22s-nGiH3iRd7NDXcEenKNJzrHWpfyM5-lrQaplh_gpPlAafmJ-gbgR8Tf7tu-3kuD4TGxDfAkdeKcnH2l9MWnqU3U3PINoJmrSp2ec2mS-YovtUWCjQSdXFzR__98j0KuOLvzpcu6leLgLUEC2Er89E4mKKGOpOz9tAwstsxW79Cnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79893" target="_blank">📅 00:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=PE91l6_bmeMtFSLYRknyTPQPhJ5veb1azVKNerNtgcdJT-qsKcPl7YuO0BKgZEA8joH-eAHKo42OYXOgcMRMPYrhC3pCBIMi3Bq3jsRCvDoD8c9w68bSzXs4iVNmomnPOcxTRX7BMO_lmgqNnpfjeuG042GM8ycLrWxRB-am9euEE0rC3Re94GLu6Rd-bXxVBSxzJd3NaBCiGqiy34JDRI_sb3lEkNr4d0B4ApCzS9gmxFXr7g5dBZTUH_B-0yIQPxQnrS9I3D0QrM9FFLGTRhG9ei4yCENohA3x3m3ceiQ124AHk0LOEc6rJ-CRo7WFPzHcqtU5rIxtukEgryhGZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79892" target="_blank">📅 00:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔥
خيارنا بالعراق هو خيار حسيني،،  المواجهة مع أعداء العراق والإسلام وشعار هيهات منا الذلة مثلته ثلة عراقية شريفة رفضت الذلة والخنوع والخضوع امام مغريات يزيد هذا العصر
السلام على فصائل المقاومة العراقية الشريفة</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79891" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9-UJyXzVY5HeHsTlROalP89boAjKIdUTxy9_Kvzd0yTJQ1shiMsof6JwUn93wE1hC76sJ7C5AREUvVoAC4DpA9_Hpb1nBKoXacjwJ_0A_1ZaTJPwxuc-ea7CjYmaouy-tpI1UABUNm3ZoEH7SBtJS1qJwPx6Mnqq9ZWAJYYZf4w0D9oqNgT-MChUT5aCydtO6GG9y0gm-_r_aVony1MgCiWKnIHJIdBHp_p1ioYVk4lrXhqXOvKEbxp4j0D1-R5IHP3Di2zB7-G4mY9doXBzgX_h0JqHDRG3egVU7deIYzkTpn3KLLniwTY4f404R94PfKh5wO1o3EX5jNyM4tFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة إدارة الممر المائي للخليج الفارسي:
🔹
تقع المسؤولية الكاملة عن أي تبعات ناجمة عن الإبحار عبر المسارات غير المصرح بها على عاتق مالك السفينة ومشغّلها وقائدها.
🔹
إن أي حركة ملاحة خارج المسارات المحددة من قبل هيئة إدارة الخليج الفارسي (PGSA) لا تشملها ضمانات العبور الآمن، كما أنها لا تتمتع بأي تغطية تأمينية أو التزامات قانونية مرتبطة بذلك.
🔹
وتبقى جميع النتائج والتبعات المترتبة على استخدام المسارات غير المصرح بها مسؤولية مباشرة لمالك السفينة ومشغّلها وقائدها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79890" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR7Icv65bF0nYoNE-2azeFhgEFTq4HRu_scjxTSFx2Piu40GH3dwZ1QkB2IWqSkoAOKV7WoL1R0UnWnvvWnsidTVdwt0ou81uYKVnOrsPLAtcDOWyTyeBbc7dpFUAYfU38P2CVQp2Iyf6MKGke8TKBJRDKJHZLJQFrVcZbLU3l49o595zMSoUJz4shQ5Ei3FRGZ24R92YIpSKhw8tJ5iQK2ghENRYdvJt6LnW5YJop9gxgqzToJ3qHHwTjST1aFwBgpyxaZ5nlPIxfdy8IOYgoxxkBmX4czyEg1A3h0KGXLcR8dNwSMtvrYm2jki5ufRfQ1LRvglthNJabnIyT3Jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79889" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79888" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOGSWfdatCzPCYe6MnycVDWXxm8p-tE7N-5yGzrTQo0h1KVOt_TAPyyKcOW9wYY_qZ0iKzS_5JE19smM_X8JoC1ckncf4UCejjlNe97FadHeMlIXlChXnCdF4VM_lT3lZ9J0uT6YUqnMZr_BHkI-vWA80CyVkllLQCj8IK91ixnTg7UKx8XotW6ug4VQ-ZDbyxxjwJ4wPw4_E9CAFQZAeO0LExLrRNBNgm_OEUzePOAI1tpmJzUwM0WcOtY2w47FLT7fIVgRBl5y_5BC4BrF-X4yKgP3F8SzjvBh2zgJAzbtLead8Ozghf7-z4FMBG5VqsJWs8vKw6noO4N-sa-D1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
مسؤولين أمريكيين: الحرس الثوري الإيراني هاجم اليوم بمضيق هرمز سفينة شحن ترفع علم سنغافورة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79887" target="_blank">📅 22:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79886" target="_blank">📅 21:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79885" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79884" target="_blank">📅 21:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇹
🇮🇷
‏
رئيسة الوزراء الإيطالية ميلوني:
لم نشارك مطلقًا في حرب إيران ؛قدمنا دعمًا تقنيًّا ولوجستيًّا فقط.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79883" target="_blank">📅 20:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
🇮🇷
وزير الطاقة الأمريكي:
رفع العقوبات عن نفط إيران يتيح لها بيعه في أسواق أخرى وتقاضي الثمن بالدولار.
أموال إيران التي سيرفع عنها التجميد ستخضع لرقابة صارمة بشأن كيفية إنفاقها.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79882" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-06-2026
تجمعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79881" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
هبوط اضطراري لطائرة هليكوبتر الرئيس هرتسوغ في قاعدة بلمحيم.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79880" target="_blank">📅 20:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭐️
‏
بيان خليجي أميركي:
إدانة هجمات الفصائل المدعومة من إيران في العراق ضد دول الخليج.
السلام بالمنطقة يتطلب التصدي لتهديدات إيران بما فيها صواريخها ومسيراتها ودعمها لوكلائها.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79879" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79878" target="_blank">📅 20:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
مصدر مقرب من الفريق الإيراني المفاوض:
انسحاب الكيان الإسرائيلي من الأراضي اللبنانية المحتلة يُعد أحد شروط الاتفاق النهائي، كما يعتبره الفريق الإيراني "خطاً أحمر" مهماً.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79877" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=R3EJ83jGmVfkz5VYGTId6_W-Q79o4Kh1wsGZ_gmvwQMeVumA3eoCDQQZyTm3DDErJeHEW0nzXAA5OS2QkoGc_u2eqoYzmZ7EG_8lRBnkjYCh7y_AWH8xEZAgCyhiBaG2nNl4lCdv596OT0fDMEHtcKeS4Dsm7Fyq5Tke50aVidaN-M11xLrhhnCv3WG_fdBVa3BIhOfX3ZkqP7op39V6tL99_tHTkxPK6S9dpe7DuEoT1v315htgdnhQhV27UQSjlSS2hb9K1OKL-q9vmlhBSZXo4Nd2yGEcXiEX4JDUqVsjOCQKPWHKf8kXi_810c4WKd_1WmfYNg6vXOtCGsrcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c6d9daee.mp4?token=R3EJ83jGmVfkz5VYGTId6_W-Q79o4Kh1wsGZ_gmvwQMeVumA3eoCDQQZyTm3DDErJeHEW0nzXAA5OS2QkoGc_u2eqoYzmZ7EG_8lRBnkjYCh7y_AWH8xEZAgCyhiBaG2nNl4lCdv596OT0fDMEHtcKeS4Dsm7Fyq5Tke50aVidaN-M11xLrhhnCv3WG_fdBVa3BIhOfX3ZkqP7op39V6tL99_tHTkxPK6S9dpe7DuEoT1v315htgdnhQhV27UQSjlSS2hb9K1OKL-q9vmlhBSZXo4Nd2yGEcXiEX4JDUqVsjOCQKPWHKf8kXi_810c4WKd_1WmfYNg6vXOtCGsrcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مواكب المقاومة العراقية البطلة تجوب شوارع ميسان.. إنهم رجال الفارس الكربلائي أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79876" target="_blank">📅 19:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🌟
قوات الأمن السعودية تختطف مواطن عراقي من محافظة البصرة أثناء أداء "مناسك العمرة" وتقتاده إلى مكان مجهول عقب نشره صورة "لقبور أئمة البقيع المهدمة" على إحدى برامج التواصل الإجتماعي!!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79875" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYXo3lBzZ1BvnU_CazE-bnTOevVZHZHrqjSq5lacVgT56NuKElf4CHDKTjZ-en9qKN5go-SG0S_FTlSSlhS7TUDdBUgg0Lb0EwTNqThooRMC0qiogWLqmP183aAef3O1FRnJB6MqkGs_TMdJAXRnLUzAbwTpUDBR3RjyLMyhdKmH_JAm3xsDduhpKhaKCQXqGlQ7LjVD7u2y6xhV3FyX_MIIJrwckd4aUT6O5CuvOdpLkV-A_Rl9DaG7CvBCusnrdTJUSpfyLw52uI6xlC1x2iuK5CH2H_XRXvjDeJwhQq_JL14Xf2V8VdPtjy1pVxMPCKjzrmqVoP3dwwkEBi3D8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأمين العام للمقاومة الإسلامية حركة النجباء "الشيخ أكرم الكعبي":
سيف يزيد المعاصر سينكسر أمام القبضات الحسينية، وراية الحق ستبقى ترفرف فوق قمم الانتصار.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79874" target="_blank">📅 19:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79873" target="_blank">📅 19:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
المعارضة الكردية الإيرانية الإرهابية، ماتسمى"وحدات كردستان الشرقية" تزعم تعرض مقراتها بالقرب من الحدود العراقية الإيرانية إلى هجمات بطائرات مسيرة صباح اليوم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79872" target="_blank">📅 19:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=IukHlxb-LZl6dmgm7mZHyu9Kjk99az00MrSyJgQm37C2ZqgD5WtDcz3Lma-Aj1nKz5Of0ZvsSK-AsHdKgt7cgcdItmKBvM4znsfKHV8yfG7AMVGF_9mwOLTW59HYTzXCzLfaNr3MpSeyqu5wRtTYxx6s-58iHzYPTyEAvzNM7CS-3N7w7UDFfQWy9pi0yMx7_1cZDADwIgO4veD_-OjKB317Z4fJe0PQzBmEC-0eoldMrV-NI_ybsdKGY-SI_mLKDJ5O_ukTbtMUC5wEdbrkdKbPSYjJEfIF4gliq4D-YjhaFNHjQGDuOxAR7Xzvc5VKe9CANFGjLj5F9VzGUrvJCRDutoRzldHzvy1zp0YK4HsCWa1HlAeY2_n5K3uoLaxK1hz0UzCgc-e7irblOJCjHEeEYzLXBK49g5V9v73HnLq4RNJQPXKIB2Vsi8WkGv_HTL4d4GBHovOlVqru9tsaVGyLKOeUzG7iUm2jc2G5355MymtUu86dYkl8fSQ-Ld7B0rirkQf46-PBBVW6WsSJ5_hzxwdx6bBkWa8LbbNlGYbwGlbAVodCjml0Zj0-Oe_hC_JX7jBKYSrgDsFwuWzjoI3vcnNabKHyBzgBt4JRssPVm0tdzez0ILTRXe_DGKkeZle5G_zHtDvg_D-1H4QtYNtZYtc6SpnmA2MUXysUgkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130c1ea3f8.mp4?token=IukHlxb-LZl6dmgm7mZHyu9Kjk99az00MrSyJgQm37C2ZqgD5WtDcz3Lma-Aj1nKz5Of0ZvsSK-AsHdKgt7cgcdItmKBvM4znsfKHV8yfG7AMVGF_9mwOLTW59HYTzXCzLfaNr3MpSeyqu5wRtTYxx6s-58iHzYPTyEAvzNM7CS-3N7w7UDFfQWy9pi0yMx7_1cZDADwIgO4veD_-OjKB317Z4fJe0PQzBmEC-0eoldMrV-NI_ybsdKGY-SI_mLKDJ5O_ukTbtMUC5wEdbrkdKbPSYjJEfIF4gliq4D-YjhaFNHjQGDuOxAR7Xzvc5VKe9CANFGjLj5F9VzGUrvJCRDutoRzldHzvy1zp0YK4HsCWa1HlAeY2_n5K3uoLaxK1hz0UzCgc-e7irblOJCjHEeEYzLXBK49g5V9v73HnLq4RNJQPXKIB2Vsi8WkGv_HTL4d4GBHovOlVqru9tsaVGyLKOeUzG7iUm2jc2G5355MymtUu86dYkl8fSQ-Ld7B0rirkQf46-PBBVW6WsSJ5_hzxwdx6bBkWa8LbbNlGYbwGlbAVodCjml0Zj0-Oe_hC_JX7jBKYSrgDsFwuWzjoI3vcnNabKHyBzgBt4JRssPVm0tdzez0ILTRXe_DGKkeZle5G_zHtDvg_D-1H4QtYNtZYtc6SpnmA2MUXysUgkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
لن ننسحب من لبنان ‏وأمرنا الجيش بالقيام بكل ما يلزم لحماية سكان الشمال.
نحن في ذروة حرب إقليمية متواصلة لا تقل عن حرب الاستقلال.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79871" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭐️
حادث وقع على بعد 7.5 ميل بحري جنوب شرق داهيت، عمان. أصيبت سفينة شحن على جانبها الأيمن بمقذوف مجهول، مما تسبب في أضرار لجسر القيادة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79870" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
​
ضغوطات لحركة طالبان ضد أكبر مدرسة دينية شيعية وقناة التمدن الفضائية في العاصمة الأفغانية كابل..
وفقاً للتقارير الواردة من العاصمة الأفغانية، تواجه "حوزة خاتم النبيين (ص) العلمية" و"شبكة التمدن التلفزيونية" ضغوطاً ومساعي من قبل حركة طالبان للسيطرة عليهما أو تعليق أنشطتهما، واللتين تُعدّان من أبرز الميراثين العلمي والثقافي  آية الله الشيخ محمد آصف محسني (رحمه الله).
​نبذة عن المؤسسات المستهدفة
​مدرسة خاتم النبيين (ص) العلمية: يُعرف هذا المركز بأنه أكبر مدرسة للعلوم الدينية الشيعية وأكثرها تجهيزاً في أفغانستان. ولم يقتصر دورها على تعليم طلاب العلوم الدينية فحسب، بل لعبت دوراً محورياً في التقريب بين المذاهب الإسلامية والحفاظ على الانسجام والتماسك الاجتماعي في البلاد.
​شبكة التمدن التلفزيونية: تأسست هذه الوسيلة الإعلامية المرئية بهدف نشر معارف أهل البيت (عليهم السلام)، وترويج الأخلاق الإسلامية، ورفع الوعي الديني والثقافي. وقد نشطت لسنوات طويلة كواحدة من وسائل الإعلام الرصينة والمستقلة في أفغانستان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79869" target="_blank">📅 18:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b657424a.mp4?token=WgNC6ZXkBilYa3qRvaUB9le2E3JZqxglCPu4MlXiPPWbg6DawRMp1VxD4l9CMt5Rf2WIa4VDNUsqkj8bZkA0BHymN9X9eOARHc1r1cIi3kEvGHNyZiP9DJ2tOO_OI7S4h5dpfY2O0teCHVqPIKv0oSMTd8hjROiv-srR-M-nHPoeY982-dTPwX1RyaYGa5ZfKQa-dE4Takfc772J8nlKmO4HieysOFL75iAfMWmOx4EXTIzVxbhlZhdktqLiBFZ8PWQ3ydn9GIztEyYt-zSDEaL0DN8iYN8s-C7BDSpQ5NT2R2MXvaS-HgjlqOAAwhWDzaHCuJx_snwgrKvw7nW0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b657424a.mp4?token=WgNC6ZXkBilYa3qRvaUB9le2E3JZqxglCPu4MlXiPPWbg6DawRMp1VxD4l9CMt5Rf2WIa4VDNUsqkj8bZkA0BHymN9X9eOARHc1r1cIi3kEvGHNyZiP9DJ2tOO_OI7S4h5dpfY2O0teCHVqPIKv0oSMTd8hjROiv-srR-M-nHPoeY982-dTPwX1RyaYGa5ZfKQa-dE4Takfc772J8nlKmO4HieysOFL75iAfMWmOx4EXTIzVxbhlZhdktqLiBFZ8PWQ3ydn9GIztEyYt-zSDEaL0DN8iYN8s-C7BDSpQ5NT2R2MXvaS-HgjlqOAAwhWDzaHCuJx_snwgrKvw7nW0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحين تابعين لعصابات الجولاني الإرهابية، ترفض عودة الأكراد إلى مدينة رأس العين ضمن محافظة الحسكة السورية وتتوعد من يعود إلى المدينة بالقتل.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79868" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79867" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79866" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
تسعى إيران إلى كسب مليارات من الدولارات عن طريق فرض رسوم على السفن لخدمات الأمن والسلامة والبيئة في مضيق هرمز بعد الحرب.
تقول طهران إن الخطة يمكن أن تدر ما يصل إلى 40 مليار دولار أمريكي سنويًا، وتريد من الدول الخليجية المجاورة أن تشارك في الإيرادات.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79865" target="_blank">📅 18:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSxEQe-BcyZ_sf76GwNn5-81urWfQallU91T44qbEEiIhA32iwspzq_mHqRxZ1C8fBhtB5qYKa6WvYS7W3QSro7jTtSA3ZqOw50IWxMIiuAC2cUema1IiN6dnO_zrk71K3RXpLfIw3mdEDpBx9HIA2xMMdqIvW7VrApyri1o0YnMhxhUq2WTPrb5jKFCaqKq4Lmg2LDP2PZlaQuvUp43PsaP9WHUCQXUqgoUfJ4oihlhlUnh_ydTYohfvH8gxxhX7o8DjXRZD3LGvESxQAbCWvnvUS4YvEblGUtqDBcGmeFJ0BWaXSmGtKlR_59cbruWikP9nEJpzoerHz0thvE0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brnl3zucnVpJQBK4iaLhvFyLJFlCpZUCOCnTw6b5ePWJ96UPg77dQDLd8sLaEUvn9O3P9fVHm0CQ2SVrs0oHNzaSs-HFwKnLkh-oW3br26hE3A_8o8zvtAkB_YW-117QXyq3JQZCAuU4bZhy7iRq0UsKBlcN1VEmvWMXOt6oWf53u0_F5Op8r3nxsx0MVki9UdHEmwTCIHmA3wWtVCkXzG6QT6POpgU_BXnLUU8doqxrP7VO-7CV6yyd7wBX9i_MfwhikyckjyreRy8yMLRkRhvqg6f96MU8UDq6V21_MsBx3OAM_paJ0KIpHhW-VIKpJBZx2HMKn8HpV9g0wFHk6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء "عبدالقادر الكربلائي":
إننا بعون الله لن نحيد عن درب المقاومة، ولن ننساق وراء تخرصات الأعداء وأوهامهم، فسلاحنا سيبقى مرفوعاً بوجههم وراياتنا خفاقة ما دام فينا عرق ينبض وسنبقى مقاومين حسينيين لن نتراجع أو نساوم إن شاء الله.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79863" target="_blank">📅 18:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79862" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=dxTIhFBCO_EbTm3t_PoIdlDdhmn3hvwqDekUGt2HlLtZyr9JlmpCr-dUMpCjXax8U2Re3HUL1wuHfDTOoGFyYitDlKkr64TEsitz9B8Pp3YMSSGwyqCfHqiroByTkGO27DE7_JvA3Fzd7hrlNnESFg7yBe8BXzktSj7rbM6Adsa3YhY8wA5VTlY0eTczn0FieKoqB95ibK5ZYTbwpkXwaCRPrfGfA4gz7gXNZWxmAWcTZMz7hN12RDglqAEQhU3uWxkx-DEIGmfTFaNYDrzMfg7iIf9l443Kx4_IDzWDrpco1p_SqpSa69rG9NWjthDYv8ZLQEDh9_Rhtv0nwUSZcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=dxTIhFBCO_EbTm3t_PoIdlDdhmn3hvwqDekUGt2HlLtZyr9JlmpCr-dUMpCjXax8U2Re3HUL1wuHfDTOoGFyYitDlKkr64TEsitz9B8Pp3YMSSGwyqCfHqiroByTkGO27DE7_JvA3Fzd7hrlNnESFg7yBe8BXzktSj7rbM6Adsa3YhY8wA5VTlY0eTczn0FieKoqB95ibK5ZYTbwpkXwaCRPrfGfA4gz7gXNZWxmAWcTZMz7hN12RDglqAEQhU3uWxkx-DEIGmfTFaNYDrzMfg7iIf9l443Kx4_IDzWDrpco1p_SqpSa69rG9NWjthDYv8ZLQEDh9_Rhtv0nwUSZcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79861" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=ucDwPGDuvsNBz0p_-hL3UP5FguJ1valuh1ySHdFhwSFyU7hhMAQc7Yc52HmQuM6_X3gpEjQL072CMAAQD1PuBJLdpEIqSjZSZyJpJWxYFwMpmJZmeAE7QEfjcV-oWRnbDaTevNax7G4D9awruchHLoCxGGoN3tMPjR1jAHRsPXJ_iv52LcNm3xrpv6BgdZdbKQv_zwnWzB3_-nS1rQCmPnIe7eYqi9PcyNcvbkVvxmXjhgzU5vDMzv2bFPvgP-4e6zuWPPMgPwDr1Iznn7Gj5PfDHn_dwfNBTuh2Wk_M6F7W_BjDbPevnCfGucgxEXJmARUvZ4lR8wmnaCNdNeAvaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=ucDwPGDuvsNBz0p_-hL3UP5FguJ1valuh1ySHdFhwSFyU7hhMAQc7Yc52HmQuM6_X3gpEjQL072CMAAQD1PuBJLdpEIqSjZSZyJpJWxYFwMpmJZmeAE7QEfjcV-oWRnbDaTevNax7G4D9awruchHLoCxGGoN3tMPjR1jAHRsPXJ_iv52LcNm3xrpv6BgdZdbKQv_zwnWzB3_-nS1rQCmPnIe7eYqi9PcyNcvbkVvxmXjhgzU5vDMzv2bFPvgP-4e6zuWPPMgPwDr1Iznn7Gj5PfDHn_dwfNBTuh2Wk_M6F7W_BjDbPevnCfGucgxEXJmARUvZ4lR8wmnaCNdNeAvaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79860" target="_blank">📅 17:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
نرصد بكل اهتمام مجريات الوضع في أرض الصومال وما يقوم به العدو الإسرائيلي بهدف السيطرة على خليج عدن وباب المندب والتحكم في البحر الأحمر، نحث الدول المطلة على البحر الأحمر لموقف مشترك إزاء نشاط العدو الإسرائيلي، ولن نقف مكتوفي الأيدي أمام أي تمركز في الصومال وسنبادر في أي وقت لاستهداف أي نشاط للعدو الإسرائيلي في أرض الصومال.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79859" target="_blank">📅 17:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مقتل ضابط بجهاز المخابرات العراقي برتبة مقدم في العاصمة بغداد بعد اندلاع اشتباكات مسلحة في منطقة المعالف</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79858" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
✊
العراق يعلن تسجيل تحفظه على بعض فقرات “إعلان باكو” الصادر عن الدورة العشرين لمؤتمر اتحاد مجالس الدول الأعضاء في منظمة التعاون الإسلامي المنعقد في العاصمة الأذربيجانية باكو
العراق يؤكد تمسكه بمواقفه الثابتة والداعمة للقضية الفلسطينية وحقوق الشعب الفلسطيني المشروعة، معرباً عن تحفظه على الإشارة إلى “حل الدولتين” بصيغته الواردة في الإعلان، انسجاماً مع التشريعات والقرارات الصادرة عن مجلس النواب العراقي الداعمة لإقامة الدولة الفلسطينية وعاصمتها القدس الشريف، وضمان حق العودة والتعويض للشعب الفلسطيني.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79857" target="_blank">📅 16:45 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
