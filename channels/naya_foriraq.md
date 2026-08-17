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
<img src="https://cdn4.telesco.pe/file/Y38AWV0lHxkOy8cxoXqtnyRvgYH1WFC7pZoZp10lJdTwUiuZUJaXw52Jh2LgX1SlrF44qUhnj2ue8NizJ7qGr8qRAO-lw8XOYi66Wsc17u8fM2zPlLO-i2AzPfWcfvu3EeV9W3J4CvLN3nGShgbW22le5gr2thgK232NPTQehDuzPLEkQ1ZqUhO3CBoNQmZPP9zJ78bQx4DMS0eXpfANxsABaKrGjUvsOXAPL-wEm0hoiM7qmxqPNL5unqIl2F7lMhPWehdI9txWzFbWvJdsQPKSkfl-h6jzIjBw80BavGl0O4PIg3Hi2S1ZOlmacyut5DyhNDNfkM6dWPebXsXCdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 08:34:47</div>
<hr>

<div class="tg-post" id="msg-87926">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-XyTTx8eBivu745KGGhit6Tl6uoI8rAvzL3Fco26UNLDUxsDBOM6L4U8vrv5lp1Ut_4Ft_09XI6Z_znoVXNLxEZ_Ab1Tc4JU2IVh3VmKuejtU2kDEVsdOWWKrJ1n2d0by_HFhkDuYL4_k7lqNK1U_CFfM3MXu8GK1eu7xOWmlYFLUQVvmn5yr1oNivvJX483lXJMPfPlwiqVhf3UO3S2rCpzop2tRnZ9Hsjuuu6DsEA0hGm6REq7rkeb2Y9GagleEuYbn9q5JfWxUi3Vejds3Xhl-LY96L8dpvNoVd6yTFyTjuB0vipnlE4Je2VL4sEuCY6LqSDHhpyaTI2J07GrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
اسعار النفط تشتعل مجددا وسط التوترات بمنطقة الشرق الأوسط وقرب انتهاء الهدنة بين ايران وأمريكا .</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87926" target="_blank">📅 02:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87925">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2bd5f6ffe.mp4?token=EYvU0pZLBIyzjk0nA9smJ2orBGrKQhPmziJMsGWB-AcMxoXoHYKexoThE6INiVqqFj895_ecqZRRWyMlPfxSjXykFwIKtJ6BKUBWpRlc0uB7b7mx3I9LQXbJRc4k1P7T_b86T69Libr9XnSz3FzQXTobf3wVOE3Le3V5YVn-3WbRMXCVdnqU42CpMoQAPXZLA2R6c48fPQARSPgd-UdfXiSLbK4eCcwXVuLmBHmVyxdEYqP6SPowdO1A8_TceCp-UZFBhQyf8z5x60UJM7zJ9oQo7rkyreeh9qf8sU1kloUju3hWVmCToCoQPqLSU7OZOR4LzmiJDImOuaZdNtFLXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2bd5f6ffe.mp4?token=EYvU0pZLBIyzjk0nA9smJ2orBGrKQhPmziJMsGWB-AcMxoXoHYKexoThE6INiVqqFj895_ecqZRRWyMlPfxSjXykFwIKtJ6BKUBWpRlc0uB7b7mx3I9LQXbJRc4k1P7T_b86T69Libr9XnSz3FzQXTobf3wVOE3Le3V5YVn-3WbRMXCVdnqU42CpMoQAPXZLA2R6c48fPQARSPgd-UdfXiSLbK4eCcwXVuLmBHmVyxdEYqP6SPowdO1A8_TceCp-UZFBhQyf8z5x60UJM7zJ9oQo7rkyreeh9qf8sU1kloUju3hWVmCToCoQPqLSU7OZOR4LzmiJDImOuaZdNtFLXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نائب قائد القيادة الشمالية الأمريكية:
الولايات المتحدة "غير مستعدة" للدفاع ضد هجوم باستخدام أسراب الطائرات بدون طيار على الأراضي الأمريكية؛ "ليس لدينا أجهزة الاستشعار [أو] الأدوات اللازمة لمواجهة هذه المشكلة."</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87925" target="_blank">📅 01:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1jGRDzNCXb6Eai0A0bQl0niGZDk-DnMxwSxzJ44JGwDNKKPBcdwYOFt__tpMgxbN5FBtbRZLMxYR-ZfICBtcoLBGP6CmsTzy29gV--38nBi0S8xOKE5HbQG1my8IKieBLFlc1JbkOkHEj7Wk7YD6M4T3-s6FLtsREpN6xTTK1MAGkiOEDJCVdC_Oqf2HPW8ezdc6X6IVpW9XhxuVYHuNx6qblWbg0yjfROBraiCwf53cHjP81DPrDC8yMQdbPIecOh2UhMlfCvdg6UPHIrWaVfzpAW5Vm4OmyvGEDACKl6KnQzAoM3H5RWjH8MXolQRrOhYj2EcjNSPbea4Qq_-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
انطلاقًا من علاقتي الممتازة مع كيم جونغ أون، زعيم كوريا الشمالية، لا يسرني أن الولايات المتحدة وافقت منذ زمن طويل على المشاركة في مناورات عسكرية مشتركة مع كوريا الجنوبية. هذه المناورات ليست مكلفة فحسب، حيث تتحمل الولايات المتحدة الأمريكية معظم تكاليفها (كالعادة!)، بل إنها تبعث برسالة غير لائقة وعدائية تجاه دولة لطالما كانت، طوال فترة رئاسة دونالد جيه. ترامب، غير مُهددة ومُحترمة. لذلك، ونظرًا لتأخر إلغاء هذه المناورات، فقد أصدرتُ تعليماتي لوزير الحرب، بيت هيغسيث، بتقليصها بشكل كبير! وفي سياق منفصل نوعًا ما (?) ، سألتُ مؤخرًا رئيس كوريا الجنوبية عما إذا كانوا يرغبون في الانضمام إلينا في نزع السلاح النووي من الجمهورية الإسلامية الإيرانية، فكان ردهم: "لا، شكرًا!". شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87924" target="_blank">📅 00:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTEb1SGPDHmbKiwC0NLmdEhsNx6Dl6W398TnYVz2XOcG1_nrjCE9KMqjNQWf-EdLwUuPjjBFPoVeRhhJfKSLnxqHf4T6czK3askNNN4EkHEGLS3g1eeXlN-Dd4NM8CHMv_vgK8Y0FvlzJvu8hqMSSUGBN7Dc9SO9crnFj8dyDIFbZ1mxg2_1cq36FIUh-lZyx04h9tHhOSZ66EgwsgoXtxluCxk6l1JYyl5fW7Ej_R02A69QDsvrUghYIPsV0WfjW2y7DGtkxNldy-1s8ls02tmmRy5gfpMuAOcVXBuMgChrQE-fKoGpVaQ61IZxwOjwzLlbRTnww69pqNLCv36gEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
يسعدني جدًا أن أرى أن المملكة العربية السعودية وتركيا وباكستان قد وقعت مؤخرًا، وأخيرًا، على اتفاقية الدفاع المشترك في مكة.
هذا يدل على تكاتف منطقة الشرق الأوسط، وكيف ستتمكن الدول أخيرًا من الدفاع عن نفسها بطريقة أكثر فعالية.
تهانينا للقادة العظماء في الدول الثلاث المذكورة. هذه خطوة أولى كبيرة وجريئة ومهمة - يا له من إنجاز!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87923" target="_blank">📅 00:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية على جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87922" target="_blank">📅 00:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx8bofuAMmv_CNHnL0kfEY0hKDNypvMWxgqOw2UG-IWkO7tKUYKOkMOwmm3ilOo742mB8KxIKbfjG6WgYHojx65h6gber6mwH-Wz1BnXHNCOBHoR3b0OF0PLzr3xWsTNws-ROpxaAdiOTurkPX1BDc69D5PQDbTvMWQWsNihB88qaw4A0msLX3lbGbcvW_uTGpySKs0CxwE3YfDMObN-kY-78iS-DwW5I-h1aAquy5qU7WgSbFBd-z_-EyPTe2oHaUUf6Ou-fmZWgqN8ZNK5zUR_6lqirOrLIRBkqge_DgRP7glKaJOK7lnH8T8xVdxbBg_R2u44KHB02Vn1tV6bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID    تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87920" target="_blank">📅 00:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lirQxLXixPlV8nPDKi-5n5J97d_YYSSyL3BjYCLHPXebUdbuV0-Jjq3VGDvvqQNV2rJsYJjnRsRCAyCUqQSylaTHvSRTh9FPJ-9ADTceYPAYKM8Mh2BhcjQVDcDfdRAr2sTqeUcqcOn-4wft-7sFB2KTym024_3FLrY6Tjw9QTNyMePhWbnmAMg6woyQVCvryBe6Uql-ncdpupkZoDbQ7cXJwOJ07sWyGwa86CXPex6YGgBzRPBvPEAf7wzRQ4YPLIpXEru7ie3Ss9OAErNeB_6vbFwzF5bd64hRVwt4aHNIZQl69feYwmvaOvdgUX4xN_AiN9T7eSHGaiLouRuKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب مقداد الخفاجي لمنى سامي: «أني آخذج لجرف النصر وأنصوّر حلقة هناك».</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87919" target="_blank">📅 00:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc75c7dd8.mp4?token=vn7hKqL-NBGVX1vlI6U6Ciou5hhFkJEWC8O2W3sj7OAi4ctPxeg3QpeEfk1lgvTu6IZowE429g5BER5hXkH8dhzGCdHZj65aTpYMk2kszYOP_xqk6r6QhUBbNwS9ZKxrd19rqys5Myk-6AXJ69apaWzV9gRasEnGQZJ2Wknc9ZXdAZUZgKKZ5TkwAl8TBt5Vrj6Fi7HoBIbwR3gAiZBats-QNLxaSSiTT8z-dL1tOD_Bw-uXoZm8SQXkWZpefr6r2V9-ycfJdzyu8F4PBze5imf36yyecAuFMbgHoRD0pY_shyFIoVDAS-QlTsMvro-8JMtO1RMctu92qJ8UjeH5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc75c7dd8.mp4?token=vn7hKqL-NBGVX1vlI6U6Ciou5hhFkJEWC8O2W3sj7OAi4ctPxeg3QpeEfk1lgvTu6IZowE429g5BER5hXkH8dhzGCdHZj65aTpYMk2kszYOP_xqk6r6QhUBbNwS9ZKxrd19rqys5Myk-6AXJ69apaWzV9gRasEnGQZJ2Wknc9ZXdAZUZgKKZ5TkwAl8TBt5Vrj6Fi7HoBIbwR3gAiZBats-QNLxaSSiTT8z-dL1tOD_Bw-uXoZm8SQXkWZpefr6r2V9-ycfJdzyu8F4PBze5imf36yyecAuFMbgHoRD0pY_shyFIoVDAS-QlTsMvro-8JMtO1RMctu92qJ8UjeH5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
النائب مقداد الخفاجي لمنى سامي:
«أني آخذج لجرف النصر وأنصوّر حلقة هناك».</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87918" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279f369819.mp4?token=pxpyJ5z1BtBxRmReqlHA9BAuide6b6KMIHz8b6Ae820ou7Us4E2rsF8rFvLJu24-fZp4BkxY6nFjB7fDyZR5a5slVS9vc1KB38t31NZhAogQeldO4NqYoxjwkWP2kkFndYmOlnTrZKmd8JvLD9xe8-HV1qVsFSRVk6rQwkKUP7srpfFgnoKpDDl7wgXVQuSalXnwSG_FzKbrYt9e2PkE75lw42tjBmU2xectq01ryj5D4fbBWYbM-GLlaGLa3subTxpv4OkcBIsz3RQKqlYBtTEZxUzF_3slKvzDX74q8y5AbKWYqzmMd0B1IHlT7mVhjjdbT-wySzUER9JCLctU44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279f369819.mp4?token=pxpyJ5z1BtBxRmReqlHA9BAuide6b6KMIHz8b6Ae820ou7Us4E2rsF8rFvLJu24-fZp4BkxY6nFjB7fDyZR5a5slVS9vc1KB38t31NZhAogQeldO4NqYoxjwkWP2kkFndYmOlnTrZKmd8JvLD9xe8-HV1qVsFSRVk6rQwkKUP7srpfFgnoKpDDl7wgXVQuSalXnwSG_FzKbrYt9e2PkE75lw42tjBmU2xectq01ryj5D4fbBWYbM-GLlaGLa3subTxpv4OkcBIsz3RQKqlYBtTEZxUzF_3slKvzDX74q8y5AbKWYqzmMd0B1IHlT7mVhjjdbT-wySzUER9JCLctU44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اردوغان يعلق بخصوص اتفاق مكة:
في حال حدوث أي مشكلة أو هجوم، ستكون هذه الدول الثلاث قادرة على اتخاذ الخطوات اللازمة معًا.
‏قد يكون ذلك ضد تركيا، أو ضد المملكة العربية السعودية، أو ضد باكستان.
‏أياً كانت الدولة المستهدفة، إذا وقع هجوم ضد أي من هذه الدول الثلاث، فبما أن هناك اتفاقية دفاع مشترك، ستكون الدول الثلاث قادرة على الدفاع عن بعضها البعض ضد أي نوع من الهجمات.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87917" target="_blank">📅 23:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-3v-Akf27rH0hYmJTeb97583DwkQHu1nMuiNzrwcM2MDRiFwWqNG75AUc9aUap1x2Q8BN4yKRHyHob2EZv3Gl-9AtVX6qjZqL9V4Z2wz1uQuEXRyEVtVG5WVtCoNMBN7_XfGxvSfBA4_37KXccruYT7o6YhLuVYWziFGiPC2VT3OJc6n0Jq4wl3TZzkBCtlWFawywuCw0lP9g34jo-t93vuU1dB5SwL3Lw8ak6dwfE90qxiXzZNQsMRqw_URVIBZVxSuGnGyqfytWLn5qpBjvv1f0cSYNvfdLC4yIgfstqColovW1a15q_hZKk3co2rv6pHnzMOUOfDCVSreFPpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يختلف على قناة فوكس نيوز التي تعتبر اكبر واجهة إعلامية مقربة من حزبه الجمهوري …</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87916" target="_blank">📅 23:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_l-mjjjpWJZvbXIVmvk17W5e6j0dBrbLJKaqf9xaTHj4r3zLsIfw4jc3pGgc_JhlZc0PcPlNCQBhIZRY31hJAgXS8IA9LgZgTwZJJYbki1ebe6AIG6rj09z9pJp08CTLfomtsHZLla2GewAwgeLzRttnz7009pNbPzxeOrARhIV_i9KB7eq6JQFhL4M61LLriJ_8SfA3EJAiBcCm81aM9OUrq-ETE_BW4b5iySJMuvapNcYp3q2cotbV3W_YyZfKhQzDhQhjrNcY83wBK9j98AMziWO0rvlCqEPXg_5Vl6g-WqXsr2oHy2JoJC7_4YALYNWhA8U6ZdJ9k0k29guEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إصابة 3 من عناصر الشرطة المحلية كحصيلة أولية، إثر اشتباكات بالحجارة في محافظة ميسان بعد قيام مجموعة من المتظاهرين بإحراق الإطارات احتجاجًا على واقع الخدمات في المحافظة جنوبي العراق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87915" target="_blank">📅 23:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🔻
نشرت مواقع مقربة من قوات الحشد الشعبي العراقية مقطع فديو دعائي جديد يتضمن ظهور عدد من المقاتلين وهم يحملون بنادق روسية من طراز كلاشينكوف 104 AK والتي يعتقد انها هندسة عكسية من هيئة التصنيع الحربي العراقي مع راس مرتبط بكابح الفوهة او ما يعرف بالإنكليزية Muzzle brake ؛ المقاتلين ظهروا بجانب معدات رؤية ليلية متطورة و عجلة مدرعة تبدو انها الأبهر العراقية الصنع و المقاومة للعتاد الخفيف والمتوسط والإلغام الأرضية التي لا تتجاوز زنة ٤ كغم ..</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87914" target="_blank">📅 23:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363e3b5820.mp4?token=dMOoD123aZFw9AlFXymmA0XvF6JnoLlGubv9wCYc0327LLVkwWi7hdgwkyEGWdUXtlpiQuY1rWV9plRTSQxa8i9-i_4TsBK94C44Cp9AVk_0WIadoU1A0sOpaAoS0gq6UXwyMhVQDiMRxDfxoEhJ3snQOvqdP-PKpM8gUqpQzDDx5HRDX8VzXPfohdQTz-IylfyuN9rrHBLMErbthAdFKc_AEWvHsYa-af4Fdy75zsCSTt88K3pdVjPZC_FcaN_gVROyxs-N9rGECE6P9YwYUMIXMCmPyg4t63iWukSQlACkFy65mzEYX0IJdufrqNQo0Q9IKEBf6x9hYkh9qrG7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363e3b5820.mp4?token=dMOoD123aZFw9AlFXymmA0XvF6JnoLlGubv9wCYc0327LLVkwWi7hdgwkyEGWdUXtlpiQuY1rWV9plRTSQxa8i9-i_4TsBK94C44Cp9AVk_0WIadoU1A0sOpaAoS0gq6UXwyMhVQDiMRxDfxoEhJ3snQOvqdP-PKpM8gUqpQzDDx5HRDX8VzXPfohdQTz-IylfyuN9rrHBLMErbthAdFKc_AEWvHsYa-af4Fdy75zsCSTt88K3pdVjPZC_FcaN_gVROyxs-N9rGECE6P9YwYUMIXMCmPyg4t63iWukSQlACkFy65mzEYX0IJdufrqNQo0Q9IKEBf6x9hYkh9qrG7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إصابة 3 من عناصر الشرطة المحلية كحصيلة أولية،
إثر اشتباكات بالحجارة في محافظة ميسان بعد قيام مجموعة من المتظاهرين بإحراق الإطارات احتجاجًا على واقع الخدمات في المحافظة جنوبي العراق.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87913" target="_blank">📅 23:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇹🇷
الاعلام التركي:
تستعد إسرائيل لسيناريوهات قد تدفعها إلى اتخاذ إجراء عسكري ضد إيران بشكل منفرد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87912" target="_blank">📅 23:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec13b8e67.mp4?token=jo85PzERHTY9D2ae3-g0lkEHzvKtYBzudyN-49o0mmKaafBY48DgkgcibCZbNt9HCB6e47-mgsKYgKLvNUd-2GXwVZOgR-p7SHFAmzx8mRueCIRDFq6iN41Jnatmaix39YEdRJ2Qd0SPbPpxxvI0hD0LLvJhFfRQcx5zQ6bsBOHHJYCTsUHk74ubbRhtVnQBfkX__pojzWXfWWbEVNWF03AkfS5FS96g-15bU4slzSZmzdum5PoftmnvOqBBHcdGO3wKvvA_FSbuLqh6xS77r-UwRpVTXKGuy-odeJG3pblbyQ4lK5nDVIp7Y-IKlLs95hbMbv1raXWCsn_Vj5l4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec13b8e67.mp4?token=jo85PzERHTY9D2ae3-g0lkEHzvKtYBzudyN-49o0mmKaafBY48DgkgcibCZbNt9HCB6e47-mgsKYgKLvNUd-2GXwVZOgR-p7SHFAmzx8mRueCIRDFq6iN41Jnatmaix39YEdRJ2Qd0SPbPpxxvI0hD0LLvJhFfRQcx5zQ6bsBOHHJYCTsUHk74ubbRhtVnQBfkX__pojzWXfWWbEVNWF03AkfS5FS96g-15bU4slzSZmzdum5PoftmnvOqBBHcdGO3wKvvA_FSbuLqh6xS77r-UwRpVTXKGuy-odeJG3pblbyQ4lK5nDVIp7Y-IKlLs95hbMbv1raXWCsn_Vj5l4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر لنايا || بالفيديو
🇮🇶
بعد استحداث قيادة عمليات البادية،
جرى استقدام قيادة عمليات شرق صلاح الدين إلى محافظة المثنى ويُذكر أن محافظة صلاح الدين كانت إحدى معاقل عصابات داعش الإرهابية ولا تزال هناك جيوب للتنظيم في صحراء العيث ومنطقة الزرقاء!!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87911" target="_blank">📅 21:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPvqTcBn_5Z65M970kDVkD9WPC2U90Z_EIn8Gve7lRcVFpaeCrqdGi5n9j28d0reF2vD935Yg7eL6JuaH1Wn31yzvMTaUM_xvlzKheNTGKsZBfdHscgCXNBK-1Fw0WhRoGwkAk9EJkjOImU42QHiBOqOu0sE0Lh5g7T4hYyh_FZy4GZP4jQxyOo1bFKQC92atoH3-Rw_JWOh67Qp2UvZJxZpsLcnBH1dZtWfXUACybXXy7NVzgXkqNreatTQxMo-zKR5ZQlnvob14TSAfS6Gd-ickMjmf2V7ccf3SRwX_T06VBeDgUtIe5IkR1GukiqCBeO7SjquUtJNnixPnlO-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
حزب الليكود الحزب الذي يقوده نتنياهو يطلق حملته الاعلانية
(يريدون ان يخسر نتنياهو).</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87910" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uu03PY8UkgKI0TnQLa0yKevAgDmVUHI2fm9kfQEw5k2-Mftcj3GlHgMSW8lsCH_SQMpzYTaXfSe8qmkDpZRIwuJSALkkrr-BMyCe4PkvUDHxkRBQz4OsKdy8cYfWQKjdhwMHMVAwULMnX9utO7U5s_tj4YfL22C16YBWPVPs-4ahXxRqjWGegGnaezp8sotWRQEnp_-s-B7i3-Gl7jypX8XIiMq2Ktmp-d4PPni2YCAUbrx0wP_kThLKIzGqVpuK0UwdMUxjDyAmZi47lQE_kWVHyEsOBXDjO1JOsERL5XAkKDMuy2ayCDAx5ZXRF5kVRtxB035sbQnPzOor7bVfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
‏
تُطلق واشنطن على كندا لقب ولايتها الحادية والخمسين؛
‏تفرض واشنطن تعريفات جمركية على البضائع الكندية؛
‏واشنطن تهين كندا وتهدد بمعاقبتها بسبب دخان حرائق الغابات؛
‏........
‏رد أوتاوا: مفهوم يا سيدي!
‏وفي الوقت نفسه، تشارك أوتاوا في الحرب غير الشرعية التي تقودها الولايات المتحدة ضد إيران، وذلك لاسترضاء واشنطن!
‏ما هي المكافأة؟
‏هذه ليست ليلة الهوكي في كندا؛
‏إنه فريق واشنطن الرديف.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87909" target="_blank">📅 20:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
اعلام العدو:
بعد 32 عامًا من إصابة والده في منطقة سُجد جنوبي لبنان، أُصيب الجندي (أ) بجروح خطيرة جراء انفجار مُسيّرة مفخخة تابعة لحزب الله في منطقة علي الطاهر، صباح أمس السبت.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87908" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
وزير المالية العراقي:
نتجه نحو إقرار أول موازنة للبرامج والأداء في تاريخه تربط تخصيص الموارد بالنتائج، إغلاق مضيق هرمز ترك آثاراً مباشرة على الاقتصاد العراقي وماضون في تجاوز الظروف الراهنة من خلال تعزيز الإيرادات غير النفطية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87907" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=gncQAUTV7fR13jfBSBhjlezXbl5NuCw1ac6Vujlmpm7tLF4Z6cA0bAKLwQB0NmfN2qnire5T6JiuGt8JMPDezaGG_DnxqRZLE86mJxck9HjFvathqxWfg5DOiVvLxcFbzPSl3i070NVkMfCeTp3fxyQkoQu1XwX7UXvOjIkUNLGA0YG0rI3RLIkDGMTLhZeAfxI8iRhlGo8Neaiuvh1DrmP6p62u4tunS9eikluu7zb1OD7_1fDm2nlQchTzz7OMegtM3_OZulgATUjMdm7rYAzdlA0shluczhuj22D3z82RFniP-8k0fyMIer3uBpoAY06nWQpMJq986-cP5YGb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0bac8e80.mp4?token=gncQAUTV7fR13jfBSBhjlezXbl5NuCw1ac6Vujlmpm7tLF4Z6cA0bAKLwQB0NmfN2qnire5T6JiuGt8JMPDezaGG_DnxqRZLE86mJxck9HjFvathqxWfg5DOiVvLxcFbzPSl3i070NVkMfCeTp3fxyQkoQu1XwX7UXvOjIkUNLGA0YG0rI3RLIkDGMTLhZeAfxI8iRhlGo8Neaiuvh1DrmP6p62u4tunS9eikluu7zb1OD7_1fDm2nlQchTzz7OMegtM3_OZulgATUjMdm7rYAzdlA0shluczhuj22D3z82RFniP-8k0fyMIer3uBpoAY06nWQpMJq986-cP5YGb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ثلاث طائرات فقط تابعة لسلاح الجو الأمريكي للتزود بالوقود جواً منتشرة في قاعدة العديد الجوية في قطر، موزعة عبر المدرج بدلاً من أن تكون متوقفة معاً</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87906" target="_blank">📅 17:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
النزاهة العراقية:
الحكم بالسجن لمُدَّة سبع سنواتٍ بحق محافظ صلاح الدين سابقاً عمار جبر عن جريمة تضخم الأموال والكسب غير المشروع.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87905" target="_blank">📅 17:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASXoJWG6dDdBMWaNHS4FmTCWEMsVCdfKAFIqmVGzcmvertXcLPyunFWs9gbBs_6PDzLky8oC-_hoamFoc7mrn2MQP6hDHeKgT3h9JMSYR2EjKcTj77WkQzq4nTRirikiAzt98GBTz9qW452VVduNdaeHg_hWewovogerHwvgCHdG93Epyi_qBBhptc41_EYlohZzDeE9DGC2tcwlTIbJknBC-AWCUMyuzlzrRN60lbSwlaMzNqTQBznhFgGI03RYHqYCaZ1mlYWo7nfFTUzoJZ8dGtMVwe4tlu8wPsrI9zMfZxqSs3--Xf2tXGOE67WlvbRgpvu98TUcRd-KUHYM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87904" target="_blank">📅 16:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز ابو عريش بالعمق السعودي في جازان   ال سعود ظلمة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87903" target="_blank">📅 16:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87902" target="_blank">📅 16:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87901" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87900">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجرات تهز السعودية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87900" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87899" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87898" target="_blank">📅 16:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
قائد الجيش الايراني:
- مضيق هرمز المقدس هبة إلهية للأمة الإيرانية، ولن يعود هذا المضيق إلى سابق عهده.
- من بين إنجازات الرئيس الأمريكي تفعيل مضيق هرمز.
- كنا نعلم بهذا المضيق، ولكن لولا هذه المعركة لما تم تفعيله؛ أي ثمن نتكبده في سبيل ذلك يستحق العناء، وسنحميه بكل قوتنا، امتثالاً لأوامر القائد الأعلى للقوات المسلحة.
- هذا المضيق أحد الشروط الأساسية لإنهاء الحرب بشكل يزيل شبحها عن إيران.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87897" target="_blank">📅 16:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
🇺🇸
‏طائرة تابعة لعصابات الجيش الأمريكي من طراز P-8 تحلق بالقرب من جزر المالديف على مقربة من ناقلات النفط الإيرانية قبالة سواحل سريلانكا ومن المحتمل أن تقوم العصابات الأمريكية بعملية اقتحام.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87896" target="_blank">📅 14:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGaP-m6NoZCA9irhTiEfp_TGz9Ps2NVKtlL7oH7UJTFGG3GXSpY4qS-XodUYeC7_3EshY_UDnzuOm_OdHJymRsbNf8lO5ZFzBJgirpYh4hJTAisHrhFd4gOIoGe3J2LheAtvRwTQMaOB4tJ-Y7WxxDL_cZBLPR2NrTHSLpZ9Du_X-pJh5UtS409O73CgSOGJGa_5uljxzori2WJ553BQAd-KDu21FxUcLbMnNcAjNcJGkmg5CyVnVEX9D8YdSDsnn8A-arXMmBw2dGt5ytv53IITxeln7lBeh-s29j5kflf3ej5YRYYjT5TEY10CrfBLgJLQJlzcM88U9WESCsoflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMLsLer2SWhJsjD_lMXeVXwyQh4nCB2qaXfnjwzYNev7bLQFNz98KhtzxWpXMpXpp-9zPfchvVShW_pdtD4iZSxdiyQF-TzM3elruxjG0sQRVWIOY7CCOT4RWpmiD_xd4_KeOc1Hu6HWYbT6KSro2q1PZeQoLPPYOtfqBnquZCyu8SA9gHzDqiVDYnHd7gFFKKTcDI4d7ti4eJz9DyKqG0z0px2ILCFqiDmeE12kfzNGlCERElw-eMC8yUlbI-0JBnfG8HYK9JTgILMm5cwzij3Gl09oMWQjdswjSOYvY3sFDlX79cW7E2Fm2wF7BO8beuT_HnQH2FxiHGIH6UxNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNQCFf5kH0mJHYh1vMZsU6PVEPk_DiqP6IV6jCFeG3cGSTZ4O27B3Gq1gKQH5efac3fs4lajnkNmwrpTjTapaZbVDuUM_43CfU2wx-KCEALQADLcFfGTCKtUA6N1u8iDZybH4yCgV-gm7uVJwFbij0N8qH4ku_YDO-SLfes0mBolO6VsfedZUG_k36MQ0thPSpBhVmsqRWGX5zY05bwWOep7JJ7QIQL1ISmTrrHYh2cU6qb38pRy7ZRI61CIPQvMnv4LOrm1rXdAhaiG5MpXJ-vQzr6yodhEdy92Eyo_FdXVbJWL0PHagJTf0rGclWut3eVi_rnZGMXdk_x1fAIHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q42xbcgp2_5z2g2BNhEsDwc2JXc0pVFFyb44I8b49N7bQErPyfKI1jTx5lMsi6BEz7j0RQWOtCuEGtcXtLUOm0JX1GBegXdZwExe7L5Cpkf5P3ffP2NRwPcqTmLGb521rn9vhUer2NN44lC1v-R9Hg6AZ838Iy5fkdw7tyq_JBY53qSwJvAXuXk3owWyEbvGboQNOaufRyk4PlCGqyNvh5I5PtRRK1n8_BTFIMUWv4jbNtFWzJEPIiwZE5pI9vUbfdUuCU2EnX7ib-nDiRqSoj8F__FSmt6b8UfH2aUhOBIeVSJuX5TMOWe-dnZD4nird96Fa3tUDszAOD3SA8n7mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
حريق كبير يلتهم مخيم شاريا للنازحين الايزيديين في محافظة دهوك شمالي العراق</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87892" target="_blank">📅 14:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=SQgq7aFjiHW23NJL0XEKEIunO0k44LV9NTCRdaHvhOiKBoi4asCXK6jdIDlnlnRbtOeSAoaq_iaqWKv1a-_UK3Cv9jvVeKlUH00xwsQ33DIWGxjZv-8h1A4Du1ofqCpe5WI-pRd9Q2q8FyS0TK52AVgUtQmO9wHBid-l55ikIJGJRt-jjPY-s8A-HQxjnMyRZ4dvKY-kfr2XvQ5CHz7lx_gSn_bkDmcmOAfE7vSlRbUwGRQOMbBIm5cmgA-1j-p17_JBkAIKiFus-8bdAnbtIzcKKxrfWieRYPiZQ0-zsJZzE__S4yXWF6e25ui0VhOV2VWlfxde9RL0bEpbnlc1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d572bf9031.mp4?token=SQgq7aFjiHW23NJL0XEKEIunO0k44LV9NTCRdaHvhOiKBoi4asCXK6jdIDlnlnRbtOeSAoaq_iaqWKv1a-_UK3Cv9jvVeKlUH00xwsQ33DIWGxjZv-8h1A4Du1ofqCpe5WI-pRd9Q2q8FyS0TK52AVgUtQmO9wHBid-l55ikIJGJRt-jjPY-s8A-HQxjnMyRZ4dvKY-kfr2XvQ5CHz7lx_gSn_bkDmcmOAfE7vSlRbUwGRQOMbBIm5cmgA-1j-p17_JBkAIKiFus-8bdAnbtIzcKKxrfWieRYPiZQ0-zsJZzE__S4yXWF6e25ui0VhOV2VWlfxde9RL0bEpbnlc1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جماهير نادي زاخو تنزل العلم العراقي من ملعب مباراتهم أمام نادي غاز الشمال ضمن منافسات الدوري العراقي ومراقبون يتساءلون: أين الذين أخذتهم الغيرة على العلم العراقي خلال زيارة الأربعين مما يتعرض له العلم العراقي داخل إقليم كردستان؟!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87891" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
صوت الانفجار الذي سمع قبل قليل في مهران ناتج عن عمليات تدمير الذخائر المتبقية من الحرب في الأراضي العراقية، ولا يوجد أي حدث أمني.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87890" target="_blank">📅 12:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
القائد العام للجيش الإيراني:
بمشاركة الشعب، إذا تمكن أي جندي إيراني من القبض على أو قتل جندي أمريكي متجاوز، فسوف يحصل على جائزة قدرها 30 ألف دولار من الشعب الإيراني.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87889" target="_blank">📅 12:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NReLswzqkJl8Nk2iKH8q0b7jpATWROTaXyAqs5A_plAi3S9d2kUeljw9gvzfo585NMJyPyfYd9V2ZOSrRTCftsdMHTh9U3KHgBDbJbdNCznzQCp-M-j7J-axM4M_dB5c4C591gkm04m6jpBeskrjqUK0s4HimhhJtYA6MMPNWftQ_vWIT29AMqCIbuDIit_oitK54kWKwzLB__2ZU1pbvpCqTM8cp1O3j9JxSJKmIMVwKTbPmBtFQ-YfVKJIRtOnxfEdQ3Il4yqvZa4M2tlvYAp3knmnBIxVUOCreLbc-xw1aXXDXh7WDxUVZETnGeFxafs4tVu60R2WXQZ8gJRv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c305e2b0ee.mp4?token=IicCBFZ0vJIpW7sSAVEWYs5x5NHSN6ymz5RPs2FtD-AG3xchR9NwLsBTmzDhq2B2tmufNbwOrQOUPivJOIl4l_H3B4--pH5Yum_vUAsp-rwLi2nv2Onmeez6P56SLm33kXl8M8Y4AjRtdkMKk9u3OmuL2Stl49FcXnUa55ItjU9bHeeIbvDoCAJkHFqU_km1GDoDLnktnrBp3llfQOOVSqkY54aRrRIu-Le5djKj_DSc2WrjnPlEgK-mjGtb-gXRDr61qIJgAjbml_ixd8Hf6Std-Ibfj9CDOxA83v_GTfa4yok-VdecctItI-dsrg5IhwWH9nKvj9Tj7fEQtj4IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابات في صفوف المتظاهرين من خريجي المجموعة الطبية جراء إطلاق قنابل صوتية ومسيلة للدوع من قبل القوات الحكومية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87887" target="_blank">📅 12:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇷🇺
🇬🇧
ذا صن دي تايمز:
استُخدمت طائرات بدون طيار بريطانية لأول مرة لشن هجمات داخل روسيا.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87886" target="_blank">📅 12:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
نتائج الحرب مع إيران.. وزارة الطاقة الأمريكية:
تراجع مخزون الاحتياطي النفطي الاستراتيجي إلى أقل من 300 مليون برميل.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87885" target="_blank">📅 11:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇦
زيلينسكي:
13 منطقة أوكرانية تعرضت للهجوم هذا الأسبوع وأطلق الروس أكثر من 1550 طائرة مسيّرة هجومية ونحو 1560 قنبلة جوية موجهة و62 صاروخًا على مدننا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87884" target="_blank">📅 11:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴
مَرَّ أربعينَ يومًا…
چهل روز گذشت…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87883" target="_blank">📅 10:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
هيئة أركان القوات المسلحة الإيرانية:
نؤكد أننا لن نتراجع حتى تحقيق الهزيمة الكاملة للأعداء الأمريكيين والصهاينة في المنطقة، وتحقيق الحقوق للشعب الإيراني البطل، وخضوع العدو. ولن نتنازل عن المطالب المشروعة للشعب وتطلعات قائدنا العزيز، في وجه أمريكا المعتدية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87882" target="_blank">📅 10:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
‏
الحرس الثوري:
على قطر السماح بتواجد فريق من خبرائنا بدلاء من إنكار قضية احتجاز الطيارين.
‏خبراؤنا ينتظرون دخول قطر منذ عدة أشهر لإجراء تحقيق ميداني بشأن مصير الطيارين.‏
قطر ترفض إدخال لجنة خبراء وتقصي حقائق إيرانية للتحقيق بمصير طيارين إيرانيين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87881" target="_blank">📅 10:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة في مدينة المخا اليمنية جراء هجوم لأنصار الله على مواقع مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87880" target="_blank">📅 10:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0696943056.mp4?token=JCT-mfRO86mJCpHxe1a53MPN5lro10QtMJ_9O4RH51szH8OdlyJkl-FEMpsoO3eN4G5ENMLN6HDmdzd-v_8mz8zGKl74FB7-5yrqYzG3NiX5ftJVA8-cs3uT6L9pdkoJsNfhrHy9d7IXiCTJN8y0xsgzj3xJPIolv6dkgm9lexLd8AdsJkEBOAWUIQ8Ub5P9BHU2pfXvk4lPK2AkpGT53ABOxKaXkWvn-YA7mHDnN0HWRFmypqU2lmAnfAN1JhTdpT_8f6AzEYDIhM126pWTWo_ZV5GfQjy82x_-hw9Wy-VJeEVt24U_zrA-fxm-boxP_RbjCbpjcXGbsdrjlakG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني   اصوات الانفجارات ناجمة عن استخدام قنابل صوتية من قوات مكافحة الشغب تجاه المتظاهرين السلميين من خريجي المجموعة الطبية المطالبين بالتعين .</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87879" target="_blank">📅 09:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87878" target="_blank">📅 09:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87877" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجار يهز العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87876" target="_blank">📅 09:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87875">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
🏴‍☠️
🇷🇺
بلدية موسكو:
تعرض المدينة لهجوم بـ 600 طائرة مسيرة ليلا وإصابة ثلاثة أشخاص</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87875" target="_blank">📅 07:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=Q1pP11JD8xyA0txGiJcI-9rxWF6ee3-xvfkjCIJrtwmN_4xHNGnsxvnfqvyQJXE7oBYhx_4AvJXgzosBi9V57ykDsHkqwqsNm7hb5SzBRX7MwoXSnduunmWII8UK_Scc3W301Lwl4KKV6tfs8bwt4tKnfHXvReHHf66z4cBT90vktN5QOV6BbPDrDhScs8iRXbHpd-5ohYTC3UDxWKpMeHsKPhIYgFETVVhVmKWOt6fMeK4sQemgdLVm3kyMzsdqz6UChE3IiIXU5SxM9xGhRNPzglP8ZgmEC3SSe5Virffo0j1EcTA-iTrqHS4_wv7BoV9FhCSc5X8D_suvY4wDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29dd6be136.mp4?token=Q1pP11JD8xyA0txGiJcI-9rxWF6ee3-xvfkjCIJrtwmN_4xHNGnsxvnfqvyQJXE7oBYhx_4AvJXgzosBi9V57ykDsHkqwqsNm7hb5SzBRX7MwoXSnduunmWII8UK_Scc3W301Lwl4KKV6tfs8bwt4tKnfHXvReHHf66z4cBT90vktN5QOV6BbPDrDhScs8iRXbHpd-5ohYTC3UDxWKpMeHsKPhIYgFETVVhVmKWOt6fMeK4sQemgdLVm3kyMzsdqz6UChE3IiIXU5SxM9xGhRNPzglP8ZgmEC3SSe5Virffo0j1EcTA-iTrqHS4_wv7BoV9FhCSc5X8D_suvY4wDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
🇺🇸
فضيحة عنوانها منظمات المجتمع المدني المدعومة من السفارة الأمريكية في بغداد USAID
تداول ناشطون على مواقع التواصل الاجتماعي مقاطع فديو لناشطة معارضة لقانون الزواج الجعفري المقر موخراً بمظاهرة قرب المنطقة الخضراء وسط العاصمة بغداد ادعت انها شيعية وان القانون جعل الشيعة مضحكة امام العالم لتكشف صفحتها على الفيس بوك و مقاطع فديو سابقة تتحدث بها على انها مصرية ومن السليمانية فمن نصدق الفديو الأول ام الفديو الثاني ؟ فيما تسأل ناشطون عن الدور الحقيقي لجهاز الامن الوطني وجهاز المخابرات العراقي وتفعيل دورهم المطلوب والرادع عن طبيعة هكذا تجمعات وشخصيات ذات هويات متعددة !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87873" target="_blank">📅 06:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9h-uFnJ_N5kitMR0DaqK67uNvB3cGFA239Lg2iU7scRnnUMd_3Ss-F_d61tCEUPA8jJ4jt7x99HcjEZAn8Qmpsw70VpsJbuYfG-D-zqZAcgNy_PTcBg1YjczUURh5ChjgJ45jc2FtgfRiJ2CHy7F_AreqL99lhf_ehpzaGrL8FaJVIR8IAB9nPVMZN3u-7bybJqCnFj8CCv8HDXeyiZCBl79mDH11UGY72WbuyK_CwMWmprS3MssQ6D1rIlcoFVspe_-ABJdxDLytnIu1nsyM46ZdU0zRxYBCvOEI2juH4ilo7mwSJJEuvk3mooAA5lxaju2URj7jRflpdKrombuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنّ من أوضح أوجه السيادة المنقوصة للعراق هو هيمنة امريكا عليه اقتصاديًا واحتلالها وسيطرتها على امواله حرفيًا وتحكمها بثرواته كُليًّا.
فهل يرتضي الأحرار للعراق العزيز أن يتعامل مع ثروته وكأنها منحةٌ تُسلَّم له، لا حقٌّ سياديٌّ أصيلٌ لشعبه؟
وهل نطلب كثيرًا إذا أردنا التحرر من الهيمنة المالية والاقتصادية الأمريكية، وتنويع أسواق التصدير وشبكة العلاقات المصرفية، وبناء اقتصادٍ يملك قراره وثروته ومسارات تجارته؟
فالسيادة لا تكتمل بالسيطرة على الأرض وحدها، بل بامتلاك القرار السياسي والاقتصادي والمالي بعيدًا عن هيمنة ايِّ قوةٍ خارجية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87872" target="_blank">📅 01:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq8j2QnGg05plNSeD-hDptIWF2OA9nqdxH2Xh63YBZZoxT8DtqgOpgJE1oepGTwCU66kJXAwtNVR99oWVnUERC7QYUYaaW9fza7qrEq4_aRWm-q0fXahgeKU5aMH2qnQhtUl68DyS9jrdblbkNoXjiXYTH-XiGemuF2Fp31WIWfyee7nVZgi95NP_ZDUOv-FLt6EJ6_QOwOqAWM4XiALGyeVd2dm5MB3ud-gynMZEUYCLJushdpJhsHZAEdrPbUZKg2doecde_QAV7kPnwSdvhgxqtZFgq2C_sT0fQe4T5M_DOAecJoyUS3ulgwtJmXDJFC_E95bRhogknCGtyVb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
سنتنصر.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/87871" target="_blank">📅 00:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=WZ1DvULYx_3v4FPAq41bFBvY4qcm6kNZTkTgMpsqP0IIscYhs0TFN4-vAzU9Ft_M8uGwsmBUR82pHqAmCjKTkitwVt8W2TFfWJQhqN8CrAWQ1ptlgS5-KJLjxqJ6cUPY2FHEGL22VSDDXuKnuofRfFibpRJ6-w_zjrikMbOH3Mhj1ZhJCGnlgEkTt0KTc1Nme8pzLDcnfT9i8i0ejbbhgcJRBLMw9odfPVBiBOicRewGKhQ3ktMa-86dYRjz3BuoLG6G25avU-gTBK1HuiQQ9uBxDtWFhVO0oLMeokni7R02u_h2hfqDMHHbllFDw4aI-3t4TJ26-2T6H3XtuHT_6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb4c61f98.mp4?token=WZ1DvULYx_3v4FPAq41bFBvY4qcm6kNZTkTgMpsqP0IIscYhs0TFN4-vAzU9Ft_M8uGwsmBUR82pHqAmCjKTkitwVt8W2TFfWJQhqN8CrAWQ1ptlgS5-KJLjxqJ6cUPY2FHEGL22VSDDXuKnuofRfFibpRJ6-w_zjrikMbOH3Mhj1ZhJCGnlgEkTt0KTc1Nme8pzLDcnfT9i8i0ejbbhgcJRBLMw9odfPVBiBOicRewGKhQ3ktMa-86dYRjz3BuoLG6G25avU-gTBK1HuiQQ9uBxDtWFhVO0oLMeokni7R02u_h2hfqDMHHbllFDw4aI-3t4TJ26-2T6H3XtuHT_6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
انفجار في محطة كهرباء الحرشة في الزاوية بليبيا اثر استهدافه بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87870" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=d-vtBQ5QQC-k_V65X7P3HqiK--GplgAlXBQAbfafPO18ZLDg2GKFCuyU4JDtRWhHll3GjiyURXIygFMPNA_5K4ZAlNxMgcNSOx-rjJzGjR5CFynZu9xqgiYV7h9ad_rEIshqIbAcJ5c6tXk6sXr2dJvj_2_D1SZzvjfa6oR2Zz3Fbgglo9PB7HFIgamQDgZ6xYeavneXuA5ChqUPXmxkmfJfAxA3H65YRqhwmwLAlv6vGSiqBSe8rf7EqiPYIlSB8W_olkPKyBOA2MYnJOuciG6Kd0iTSsjX8mQe73qr-krPyww7ecPEC3h7OlqLrrYV8qi2j_jFFxrvaYs66Zr4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd380ae70b.mp4?token=d-vtBQ5QQC-k_V65X7P3HqiK--GplgAlXBQAbfafPO18ZLDg2GKFCuyU4JDtRWhHll3GjiyURXIygFMPNA_5K4ZAlNxMgcNSOx-rjJzGjR5CFynZu9xqgiYV7h9ad_rEIshqIbAcJ5c6tXk6sXr2dJvj_2_D1SZzvjfa6oR2Zz3Fbgglo9PB7HFIgamQDgZ6xYeavneXuA5ChqUPXmxkmfJfAxA3H65YRqhwmwLAlv6vGSiqBSe8rf7EqiPYIlSB8W_olkPKyBOA2MYnJOuciG6Kd0iTSsjX8mQe73qr-krPyww7ecPEC3h7OlqLrrYV8qi2j_jFFxrvaYs66Zr4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
اكثر من اربع انفجارات سمعت في مدينة مأرب</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87869" target="_blank">📅 22:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇶🇦
‏
الخارجية القطرية:
ننفي ادعاءات احتجاز طيارين إيرانيين، فرق البحث بحثت عن رفات الطيارين الإيرانيين وتواصلنا مع إيران للتنسيق.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87868" target="_blank">📅 22:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني العراقية :
موعد 30-9 ليس بعبع وهناك مفاوضات تجري عبر هيئة الحشد الشعبي كونها المؤسسة الدستورية والقانونية لهذا الملف .</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87867" target="_blank">📅 21:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/87866" target="_blank">📅 21:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
انفجارات متتالية تسمع في صنعاء ناتجة عن اطلاقات صاروخية.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87865" target="_blank">📅 21:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3kxGNeQxXIKiOQr8WNWxyE0isNZwIP88m1uvzAYoJhttsqtg28K_255s7H66MiHR9YCObRZGZxGnAGbrzSKt85AhltwgU0Uyyl4efXvZBMurQHa7muGyeN4JuV6do4vOun7ybsW3a8VgeSbIRk5rHDI_ei75YR67DHf71inbXU4qXwND172FanUbSYRVTFgD303zdkCod_HU-K7Qu8K7LmOA-pJ_nL3JcLMuXzncnPv0KI0ndYLP-pvm_nECYR7tsP0zzp2_o7d2zVUeXorpjGv4MiJWx8gVCwHdy2AqlutGtonD_rBwkbplwRap5t4jTHSbfu1AnrcxZu0myI5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
ثلاثة انفجارات قوية تهز مدينة مأرب.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87864" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر اصابات مباشرة تطال المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87863" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87862" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb5TiSeu59ja6sqPuz7b_LCUd6bAhUWYKNKYRrVFBaPFGcTrvFwpFEGQ57CiaOnr3rEuMwJ7OchD2QdjIJKLMaC-ZTfg26jMpMkWNrMLJO24ZPZxQoW1kMl3U9BFouicy_XCN13vfkdy3xGp8ntYoXrgGyowbE7D7xPLt9WFHhIoSFYz79Zmm_aYrqQzqtKG94_yd5LR3fcMF_nP9csZ5GZmp6FPnG94KBL_wqW3Cqp641ZiwwpBNGlQfH6t3seSCwlpg2qbUXpT-LuvnZTO_oe1ItH2Ot8P_il9cBuCG2NTaxPXQlxsOIA9O9oBfEzFxGAonqsMD1Et6OgpD6s0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مشاهد متداولة لمدينة مأرب يعتقد انها ناتجة عن قصف لانصار الله.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87861" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA60C0fAMRKQ9ojvK_k8jW6D0RjcBPs_hUpkY-bKCljN8RSb6Y-ADq29Uyd_kfvJToA6yuzYRhZt2oBQzi4Gy5Fcipv29wEbEhTU95A7U5fRFjtvnOF7vSB_9YmpJNdQnVVTwA20NZ8Xf4C5B_byBfXam0pg6fzjOorxxhQFIzwSxb4N1TKQhvURAO-YRGCb291JeWKOChtLPHqSPCGxkkswlYS6FXa65_qinKmDsTGRRZ2NUO5ipb9unK7vMakwNDcgqbtDaSIKpAPUBB24OQYmXKjgRAJq05-1zQfDAFSFJaRhPd3Y4PP4ZE7uuWE7tSK96VVkw8B39efcblUyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!  هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !   هل لا…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87860" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تعرض دبابة لهجوم في قطاع غزة نتيجة لغم تابع لحماس.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87859" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هل العالم بوضعه الحالي قادر على فقدان أربع مليون برميل من العراق في حال اندلاع الفوضى ؟!
هل يعلم الإطار التنسيقي ان حجم ضربة لوبيات الطاقة العالمية للعراق الأخيرة الهجوم الأكبر" ضربة السعودية للعراق " كان بسبب فقدانهم نصف مليون برميل فقط من بقيق !
هل لا يرى ساسة العراق افول امريكا بهرمز و وضع قواعدها بدويلات خليج فارس ؟! وبروز نظام الدفع المسبق للسفن المارة بخليج فارس  ؟!
هل ستقطع علينا امريكا الدولار الذي هو منقطع أصلا على العراق منذ ثلاثة اشهر ؟! وتمنع علينا بيع السندات ؟!
ام ستقطع الكهرباء التي هي أصلا مقطوعة منذ ٢٠٠٣ ؟! ويومية هزي تمر يا نخلة اجه جنرال الكترك راحت سيمنز ؟!
متى يعرف قادة الإطار التنسيقي ان مصلحتهم لا ترتبط بامريكا ولا البرتقالي وان مصالحهم الاقتصادية مع احزابهم وخوفهم من المجهول لا يجب ان يكون على حساب سيادة وتاريخ شعب العراق …
كل مشاكل العراق وبروز نظام بشكله الحالي القريب من امريكا وتحت سيطرة الحاكم في العراق والشام " توم باراك " بصورة مذلة يتحملها قادة الإطار التنسيقي ال 11 …. وعليهم اما ان يتولى مسؤوليتهم التاريخية او ينكفوا عن إدارة البلد …</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87858" target="_blank">📅 20:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obh5fJDY78Qd0HwAns8ZiEyL21Apq4rZgMmKhlhYTyWuZqMLnp9KTCXPQ2nLRjyV-NSazYqI2myqxtQ3QBs81zhgB3Cz_H3RSJ7tOUC0mXRUQ6ZvPR8WCV7mORCoM5id8n1JGOcLoxggPA4JbOF61Pl1DSfNcm2SYpPBCpN8WZekbQ7otKFHYG2tLe1yrJJAq9i5n6aKEW-XtgC8eQTe-tHRg3v3Sw7CAzksThyEDNryL6uz5nBhXaxmPQUsAn6Ppi4IRj54e5TUGYj4WTq_8w6DgtG185pvfmqLsldNK91O1x4a_sIpISjDGgaWKrocsgDbG5A7T9zObIavUtckdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اول تعليق للبرلمان العراقي
زحمة قناة رسمية تثير الفتنة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87857" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FACLFewM06dP0kF44vBQ0i9RsBs7BUgB9YgG_lBEjGyycRdP96K6mfO-6fWJQSPzfn4cJWqiieE9HC3VQzZmZeBy0-MhVEj1m8HzsPsfUulxuVUaafPuxe34iZ8w-as0dwH1RaaZOTTltLafFKQ4m9xR-ap-YNldo08uK_p0j8w4JnbL_qXjN2XRoFy956byZ0vvL0TiOaoGXt6pYF1I04bkQ8Tnt16yTu5WDWzQxs7Q7pWQhBnCe2fQ-czOW2M0IAXBQJcfGqqTB-EQW1tCpPbq_SiI8W_nklH9HAYKSvxXFn9gkOS9U64PK6skkJDT96PAJd0N5WYT9tnfJHOzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: على الرغم من المظهر غير الودود في هذه الصورة بالتحديد، إلا أن هناك العديد من الصور التي نبتسم فيها، وأنا و Kim Jong Un نتفق تمامًا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87856" target="_blank">📅 19:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
أعلن المتحدث باسم كتائب سيد الشهداء،
أن الفصائل المسلحة لم تكن وراء الهجوم بالطائرات المسيرة الذي استهدف مدينة أربيل فجر الجمعة.  كما يوجد "شبه اتفاق" لوقف العمليات وتأجيل الرد على الهجمات السعودية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87855" target="_blank">📅 18:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇾🇪
مدير ميناء المخا اليمني يوقف العمليات بعد هجمات الحوثيين.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87853" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي: تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87852" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو:
هجوم لحزب الله في "منطقة الأمن" اللبنانية يؤدي إلى إصابة ثلاثة جنود والجيش رد بقصف مقر أصدر أوامر الهجوم ولم نعلم الا لاحقا ان بداخله مدنيين.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87851" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7OzoOmLmAmiYKf_OBkUXXr3Sx8qqMEtAW_EtKjS0YwauBf5WtbAjlZcOVL_72ZyXmIsAIswiY4B-PsQFdn3eqfdxUpi4uHKhE0v0VsNw6NZR_Goznc2cp6NdTksH_PPk_NC9WtMSVun86LoHQwWTzcC7bUraFT-1dq1Ud3H2knto0XIZq0KfF2Q4VEtN-TzHaZIKSgK1J1-q7c92NJu35S2u_1w4Maa0fIqsRIJZyU2VL_Oref944dQ3KpHpAXhpEpQNKYEm7wz8-bzwhjZhFQOffinuvSLeD_omUnbeAxyViouQhhjn2MwB9DHkMkIG4dt-wSWmIcs2chiFa6KGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس مجلس امناء شبكة الاعلام العراقي:
تقرر ان تخضع جميع الفواصل الاعلانية اياً كان مصدرها للفحص والمراجعة من قبل الادارة العليا للشبكة ولجان الفحص المختصة فيها.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87850" target="_blank">📅 18:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق   المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87849" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
مصادر خاصة بنايا   حراك برلماني لاستجواب رئيس شبكة الإعلام العراقي تمهيدا لاقالته وذلك لدفعه وترويجه الاقتتالات والحروب الداخلية في العراق .</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87848" target="_blank">📅 17:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=X2C0r4xzzyxBARYfKkzgZqGyaCukGTSp92UOqehMcOmnbV48z1LfpyYd5sx2u7TM6lZQBMyLy1YwGlh1UXKqWRnFCCAc6OA-ZF1DlLjcQKFu2zq_grWn3gnAIt6w2zfmo_TOJ4J5KsCbnpXXCRFAhs6iGDYXOmUjbDqiMVAs4TM6Xe76xUZKO7ii1rNoQnXGpPgwUFkW3Rhi5O8Gb2m9K-v-OHEXoZLZl3H1hKuwlWVFbTQFAlccOKPEVoRX8kYyc-BajCjMxbipFCBJTPCoJ59354RlwegEdU6Bz3Jt_wV7iTzTGJjlKEWVz6J8VmT1x3X84YI_oggtIoUEa_NGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b7ffa1c5.mp4?token=X2C0r4xzzyxBARYfKkzgZqGyaCukGTSp92UOqehMcOmnbV48z1LfpyYd5sx2u7TM6lZQBMyLy1YwGlh1UXKqWRnFCCAc6OA-ZF1DlLjcQKFu2zq_grWn3gnAIt6w2zfmo_TOJ4J5KsCbnpXXCRFAhs6iGDYXOmUjbDqiMVAs4TM6Xe76xUZKO7ii1rNoQnXGpPgwUFkW3Rhi5O8Gb2m9K-v-OHEXoZLZl3H1hKuwlWVFbTQFAlccOKPEVoRX8kYyc-BajCjMxbipFCBJTPCoJ59354RlwegEdU6Bz3Jt_wV7iTzTGJjlKEWVz6J8VmT1x3X84YI_oggtIoUEa_NGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🔻
الموضوع هو اكبر من المقاومة وسلاحها ، الهدف هو الشيعة وعقيدتهم التي تقف اما المخطط الصهيوني الابستيني ومشاهد ملايين الزوار من الشيعة حول العالم في الأربعينية هي مشاهد مرعبة لأمريكا وإسرائيل ودول الخليج والهدف القضاء على هذه المظاهر لأنها شعلة الحق الوحيدة المتبقية في العالم ..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87847" target="_blank">📅 17:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الرئيس التركي: استمرار الهجمات الإسرائيلية على لبنان يشكل مصدر قلق كبير لنا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87846" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلاح ما نسلم   مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87845" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=C8C_mB0hhUKIxOAq9IEL-ly3ygo0tsC8qqyfjAhkL86GKNuNrad-23H7AsuGydqIIFFvaBiH4MGqJq2okPP7V4o_c4JTAbY7F6YQxsoR4iIGinfIVjtzkqsvxV6KdSqRv1uLKr3UDpe196Ig8BdCIkWJH1cPJLk4bL1RBHHluWz5f9zyvb-s3IcA9YBDvWDLN5eDB9p7dmmTM0lGOOyKxohA0SdKjFpnbSakg4wD-2M6GVEk6wqge_vmUr34PM3GxeEJMliSK4ERl6jGEVl5QifZTcaMjsvsY9KzXpVia3Y25jUw70jiA9i0hc_DEKJoQnbW2zgr9f2iAjRGm8gKxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c189e3c62.mp4?token=C8C_mB0hhUKIxOAq9IEL-ly3ygo0tsC8qqyfjAhkL86GKNuNrad-23H7AsuGydqIIFFvaBiH4MGqJq2okPP7V4o_c4JTAbY7F6YQxsoR4iIGinfIVjtzkqsvxV6KdSqRv1uLKr3UDpe196Ig8BdCIkWJH1cPJLk4bL1RBHHluWz5f9zyvb-s3IcA9YBDvWDLN5eDB9p7dmmTM0lGOOyKxohA0SdKjFpnbSakg4wD-2M6GVEk6wqge_vmUr34PM3GxeEJMliSK4ERl6jGEVl5QifZTcaMjsvsY9KzXpVia3Y25jUw70jiA9i0hc_DEKJoQnbW2zgr9f2iAjRGm8gKxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات الآلاف يقررون التظاهر ليوم غد ايضا احتجاجاً على الدعوات الطائفية في محافظة بابل وسط العراق
المواطنون يطالبون بمحاكمة عدنان الجنابي و شيوخ الفتنة والتحريض .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87844" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIWNDkQVySm9uRf8SHQOCJIQOPFVTaZ_KAgmbRELN-bKC9O8wlnfbOFqxyHXsbXzyeI4D640LXi8fq_Yb81bcMI_uvg3RIbMAgil7cvGehbM3v92oLdQwxB0YE7QEoqBYCThg1IzD1K7jcUL5D2iVQOb8rKfrh1QdKkmQ0_DVEvYDjmG9PdIYE92pGoQHxipejXNAuK0MlGOF-HKMYhDzlAyriRZeyoORoVyai4eRdB95nq20kc8aNng06kbpFA9f8l4ogjlaHu0RbY5Shu_GOa1McSPIGuOvOdYz0T202hcNSTwmB6C2MiBEy2ffGcA3kTKy1xwnuR7HyghLNlVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
منصات التتبع:
تواصل أكثر من خمس ناقلات نفط عملاقة عمليات نقل النفط من سفينة إلى أخرى قبالة سواحل الفجيرة، مما يشير إلى أن صادرات النفط الخام من العراق والإمارات والكويت لا تزال تعبر مضيق هرمز. وتدفع بعض السفن رسوم العبور الإيرانية، بينما لا تدفعها الأغلبية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87843" target="_blank">📅 17:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=ERJY0hQ_7Dbl196DTzbmbASR7paOTYFY4kCNXtL9l9i9dw_zNI0Ax-6Hx9tEsGF1Y--rgjPGAR5nox9W5eeuuuhU-wEUF5jRsgjTr2xWn0bzXNxTanG6quUX-cNMItIXjxvocCIToGI0xD4Sa7os9Qn9WqhNPmbKxIrXr7zvW4xICHgR3j2-rJepEtMJYR2P3xXydWwPpRZMfgI9cn93Z70jVWwJcHYMMviEZQuBQUQUh3RQzQ8qCxvq8tT5ga8KzNfcKbHR-X3cUIMyJIsjd3FYcRUUifCYR4d3yPaChqDlHM6xAjzKl_JOy8k7eTgrFMw3MJgIzz--3wjAkLTq4FRphzT6ueRgqFhtCb1VAFS4WvgUL__RW1iXCxtHrMb8aJwFq0va9VvHrBkUD7wMjAjasg9GePB6KzxxVUFj9zjMq_yyyyZecPTkdD5LRvVc5-dXXzpUbiNagRP39ZV8WWNk0VQA8XMLdZTlIEZpY-oBv9KJRtPFmQOh27NMIvfcOiZMZXR-9MovMsTrEpfjggOJhNcyQX4dG9B9Rc53IMv4ijjS3Df1JW9TPxHJsTe43vXBzkBOMZ4FiYr2uATLZFQ4_QasxjMN9gdXCJCZnErMJ12VSPz8CDeiXf0Q4AChmwNoS56Ti7916V7jv8x-QYQWlZqjPBi606s21QtOteU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7dc434c.mp4?token=ERJY0hQ_7Dbl196DTzbmbASR7paOTYFY4kCNXtL9l9i9dw_zNI0Ax-6Hx9tEsGF1Y--rgjPGAR5nox9W5eeuuuhU-wEUF5jRsgjTr2xWn0bzXNxTanG6quUX-cNMItIXjxvocCIToGI0xD4Sa7os9Qn9WqhNPmbKxIrXr7zvW4xICHgR3j2-rJepEtMJYR2P3xXydWwPpRZMfgI9cn93Z70jVWwJcHYMMviEZQuBQUQUh3RQzQ8qCxvq8tT5ga8KzNfcKbHR-X3cUIMyJIsjd3FYcRUUifCYR4d3yPaChqDlHM6xAjzKl_JOy8k7eTgrFMw3MJgIzz--3wjAkLTq4FRphzT6ueRgqFhtCb1VAFS4WvgUL__RW1iXCxtHrMb8aJwFq0va9VvHrBkUD7wMjAjasg9GePB6KzxxVUFj9zjMq_yyyyZecPTkdD5LRvVc5-dXXzpUbiNagRP39ZV8WWNk0VQA8XMLdZTlIEZpY-oBv9KJRtPFmQOh27NMIvfcOiZMZXR-9MovMsTrEpfjggOJhNcyQX4dG9B9Rc53IMv4ijjS3Df1JW9TPxHJsTe43vXBzkBOMZ4FiYr2uATLZFQ4_QasxjMN9gdXCJCZnErMJ12VSPz8CDeiXf0Q4AChmwNoS56Ti7916V7jv8x-QYQWlZqjPBi606s21QtOteU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافد حاشد لموقع التظاهرة في محافظة بابل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87842" target="_blank">📅 17:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">المتحدث باسم الخارجية الايرانية بقائي: لقد تم التوصل إلى اتفاق بشأن خريطة حركة الملاحة بين ايران وسلطنة عمان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87841" target="_blank">📅 16:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da068288c4.mp4?token=ZsjtDnJ-NkjODtgQaQl2SBK8TIsfSW_e65YKQhy-KUsFi9PIqGsOxI2iGq7hSxYJ0pI16AW8cZzjtJ45TxVsakP2VXVp4kWDDxJ_6xSu6r25bOjW_tw711EWVh6iM3ZVKcJw4Mou3TZ9Iupq1eSpGLayDJkF6M2wCFxZMA4TUIk_z4toiGhUZYrc-APge_To-wsPNqjR4FAZaLofqfgUzokMGAacCoMQSHJ4p08fer-5f-6VLTomipkwcoFhDCz7ags-b9WThamTW4adfmo26l-EI2gdY3JjzYweIRu1pAaLnTPyC_GfwgTL-Hq88xtcuofB3epzu0GsUOYc3q-Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da068288c4.mp4?token=ZsjtDnJ-NkjODtgQaQl2SBK8TIsfSW_e65YKQhy-KUsFi9PIqGsOxI2iGq7hSxYJ0pI16AW8cZzjtJ45TxVsakP2VXVp4kWDDxJ_6xSu6r25bOjW_tw711EWVh6iM3ZVKcJw4Mou3TZ9Iupq1eSpGLayDJkF6M2wCFxZMA4TUIk_z4toiGhUZYrc-APge_To-wsPNqjR4FAZaLofqfgUzokMGAacCoMQSHJ4p08fer-5f-6VLTomipkwcoFhDCz7ags-b9WThamTW4adfmo26l-EI2gdY3JjzYweIRu1pAaLnTPyC_GfwgTL-Hq88xtcuofB3epzu0GsUOYc3q-Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاح ما نسلم
مثل ابو حميد ما نصير</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87840" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=rkdYJ6SSyBRa0Tnjxl0S6XyR5gtT-NHqx3uzrLLPBlenlSQ_E-XaHjOqqyse51UsXq30ZBTnFZu5V34O6IJ0H4_e5mXeXI47ZIxlvkP06yd4AvYpIHEordf7pP3HK-7Mo2gdrrW26ztpOnYJZq0AnM3tnynV5mJCwhzZ5a6ggR4OGeWyiExFTY1kkPBOPIOwoMbhRUzWLNV2PsPUxBYqW4kWG1WEwZfAzQT2T00jBRnts8DptW7JKXjMuZZ-2rpn7_OW1bFwETvNbg37sx6dIv6Vjk42Np60hdfQtutr2kHcIhkN6hfG51dj0TUUItFFCZAhibhDCO_xEEY3pqx6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d027dce5.mp4?token=rkdYJ6SSyBRa0Tnjxl0S6XyR5gtT-NHqx3uzrLLPBlenlSQ_E-XaHjOqqyse51UsXq30ZBTnFZu5V34O6IJ0H4_e5mXeXI47ZIxlvkP06yd4AvYpIHEordf7pP3HK-7Mo2gdrrW26ztpOnYJZq0AnM3tnynV5mJCwhzZ5a6ggR4OGeWyiExFTY1kkPBOPIOwoMbhRUzWLNV2PsPUxBYqW4kWG1WEwZfAzQT2T00jBRnts8DptW7JKXjMuZZ-2rpn7_OW1bFwETvNbg37sx6dIv6Vjk42Np60hdfQtutr2kHcIhkN6hfG51dj0TUUItFFCZAhibhDCO_xEEY3pqx6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يتوافدون الى موقع الوقفة الجماهيرية في محافظة بابل لادانة عودة الارهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87839" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏وزارة الخارجية الروسية: شحنات الأسلحة الأمريكية التركية المحتملة إلى كييف ستضر بعلاقات موسكو مع واشنطن وأنقرة، طلبنا من واشنطن وأنقرة توضيحات بشأن مزاعم وجود خطط لتزويد كييف بالأسلحة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87838" target="_blank">📅 16:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87837" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
اللواء 52 بالحشد الشعبي يتسلم قاطع بسطاملي في آمرلي من الجيش ضمن تنظيم توزيع القطاعات والمسؤوليات الأمنية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87836" target="_blank">📅 16:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=ElQXU1jFdjuJ3SoRhSvDmnp043qZ1iworqwtKPQo9GV1jVgrHZ9Is4ZXfO9T8IDCHuf4tPbJp77CQ6MjJenRd4XLhCJOovKmWngd2AYvYMLFk7zu3tEmaJsyB23JOdUzq0OjOqZKcvtNHImfIqfiXAfHNkT9rQx7LaS5MtmzwXNJY0db4CTZfRKLdb0nqstyFtfnYw2gX9vY9_cn8iYgxoF5tVjm9cGdNQdJ6iisMFoJ_R0Mih_msheHLlBfDqzBmM0bAY0r0gM9UGkO2wf1QBygKSpRTpF8PxYbISItVGS6vQbgq5Ahb52LDUiKe7DW3UEbf45CP4NnmDKGb2K3zgMwS1VODm3JZeqdx1N50lxEvBU3RuGznV8ei6e8Y6XYhinA4caahL_vtHfC5cAhuTbOv9xqITATaSwcRWDWI6RjMCoI2yUjTs5jK-bQbAv6qp5IE6L0eKlXeXY4D7YxqcHTBDg934ZuFa36GOcvFgwFiVsERMXqOC0Iuop2eZkvPqdbsokdFGBU--XXF3FanB9GtHNikZousKkMFx9nwoS102x8y38EuVoqF8f8bAvgJJ1OoH4Rf8RmW7zPF8fef8DtMl22aA1PxJzhqw6aeM1_5rX8W9zsbPOY_IjljByVZ7-P_t7NGX6orGePnXD5ki-g5sqAYG4JLD6mQSq1VvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa80e2a4e.mp4?token=ElQXU1jFdjuJ3SoRhSvDmnp043qZ1iworqwtKPQo9GV1jVgrHZ9Is4ZXfO9T8IDCHuf4tPbJp77CQ6MjJenRd4XLhCJOovKmWngd2AYvYMLFk7zu3tEmaJsyB23JOdUzq0OjOqZKcvtNHImfIqfiXAfHNkT9rQx7LaS5MtmzwXNJY0db4CTZfRKLdb0nqstyFtfnYw2gX9vY9_cn8iYgxoF5tVjm9cGdNQdJ6iisMFoJ_R0Mih_msheHLlBfDqzBmM0bAY0r0gM9UGkO2wf1QBygKSpRTpF8PxYbISItVGS6vQbgq5Ahb52LDUiKe7DW3UEbf45CP4NnmDKGb2K3zgMwS1VODm3JZeqdx1N50lxEvBU3RuGznV8ei6e8Y6XYhinA4caahL_vtHfC5cAhuTbOv9xqITATaSwcRWDWI6RjMCoI2yUjTs5jK-bQbAv6qp5IE6L0eKlXeXY4D7YxqcHTBDg934ZuFa36GOcvFgwFiVsERMXqOC0Iuop2eZkvPqdbsokdFGBU--XXF3FanB9GtHNikZousKkMFx9nwoS102x8y38EuVoqF8f8bAvgJJ1OoH4Rf8RmW7zPF8fef8DtMl22aA1PxJzhqw6aeM1_5rX8W9zsbPOY_IjljByVZ7-P_t7NGX6orGePnXD5ki-g5sqAYG4JLD6mQSq1VvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام امريكي: المنفذ ليس واحد بل عدة مسلحين</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87835" target="_blank">📅 16:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUUnC0dVKcHTbb0ygW6V-waaQCuAS2X9HN-2A_bzO-RhmLh2a4fpZSbPxaIDqMPpimLHhrS-HnBG0_zLPoMqnaj4UZkyKcLfy6B8M8Haw0hNBX-4M0MB3j61L6OMrd8JEM_eY07unp_r8Y9s57pBVDuiZtNXZ-9QcqRnr8XX3l3BbY2MUdJ6d7Xmb-zW-0f7HNNn20pQlVOga3Pqsly5rbxHdzKk73OSMJfFmqZORsGZIS2n8DRsiz_BteALwqu9YbavyS5hIHJuViQAsHYASHxuCdazuIzCZIMSp48fXjZbuK2G0vrJd1hfzUZijeJZm4aYWEzA44x7Oyy7WtWZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصادر لنايا
شبكة الإعلام العراقي بصدد انتاج الجزء الثاني عن تسليم السلاح لكن شخصية حميد ستصبح كاكا حمه في اشارة لسلاح مليشيات البيشمرگة ..</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87834" target="_blank">📅 16:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اغلاق جامعة ولاية فرجينيا بعد الهجوم المسلح</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87833" target="_blank">📅 16:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اطلاق نار داخل جامعة فرجينيا ومقتل واصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87832" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87831" target="_blank">📅 16:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حدث امني في ولاية فرجينيا الأميركية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87830" target="_blank">📅 16:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله:
استيقظ اللبنانيون فجر اليوم على وقع تصعيد عدواني ومجزرة وحشية ارتكبها العدو الصهيوني المجرم بحق المدنيين الآمنين في الجنوب، من خلال استهداف منزل في أطراف بلدة أنصار الجنوبية ومبنى في دير الزهراني، ما أدى إلى ارتقاء إحدى عشر شهيدًا من بينهم أطفال ونساء وسقوط اثني عشر جريحًا، في جريمة موصوفة تضاف إلى سجل العدو الحافل بالمجازر والجرائم وسفك دماء اللبنانيين وتفجير منازلهم وجرف حقولهم ومحو معالم قراهم.
إن هذا التصعيد الإسرائيلي، باستهداف المدنيين وتوسيع دائرة المناطق المستهدفة، يعبر عن رغبة وإرادة رئيس وزراء العدو المجرم نتنياهو  بتصعيد الحرب تعزيزاً لواقعه السياسي الداخلي، وخدمة لأهدافه الانتخابية وإرضاءً لليمين المتطرف. وإن هذا التمادي في العدوان وانتهاك سيادة لبنان تتحمل مسؤوليته حكومة العدو  والولايات المتحدة التي تؤمن الدعم والغطاء لها، فيما يجب على  السلطة اللبنانية أن تبحث عن السبل المتاحة لوقف هذا العدوان وأن لا تصر على الاستمرار في مسار المفاوضات المباشرة المذلة وتقديم الهدايا المجانية للعدو، رغم كل ما يرتكبه من جرائم واعتداءات، وما يعلنه من نوايا عدوانية وتوسعية تجاه لبنان.
لقد آن للسلطة أن تراجع حساباتها مراجعة شاملة بما يحفظ سيادة لبنان وحقوقه، بدل الاستمرار في سياسات تأكّد عجزها عن حماية لبنان وشعبه، وأن تقف موقفًا وطنيًا وشجاعًا ومسؤولًا، وأن تتوقف عن اللهاث خلف المفاوضات التي يجرّها إليها الأميركي، وأن تدرك أن الرهان على الضمانة والوساطة الأميركية هو رهان خائب، فالأميركي شريك للعدو الإسرائيلي في جرائمه ومجازره بحق لبنان. وما التصريح الأخير والوقح والابتزازي للسفير الأميركي في لبنان الذي دعا فيه إلى تسليم سلاح المقاومة، فيما المطلوب منه أن يضغط على العدو الإسرائيلي للانسحاب من المناطق التي يحتلها، إلا تأكيد على أن ما يبحث عنه الأميركي هو مصلحة العدو الإسرائيلي وأمنه على حساب سيادة لبنان وشعبه.
إن على اللبنانيين جميعًا، بكل مكوناتهم، أن يدركوا خطورة النهج الذي تنتهجه هذه السلطة على لبنان ووحدته وأمنه واستقلاله. وإن على العدو الإسرائيلي أن يفهم جيدًا أن اعتداءاته وتجاوزاته ومحاولاته فرض أمر واقع لا يمكن أن تستمر، وستقابل بما يناسبها، دفاعًا عن لبنان وشعبه وسيادته وكرامته الوطنية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87829" target="_blank">📅 16:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXS_rxtaZAn1akPNQ-Khcbi9jNi-KBUIbBp-_g9Rc7Z0guqRz9327ZZBHho3lqXNaNFZ6yPcZr6GzBlXolP_A_IZdCGcoyepgQEQsXr2Gj_IFLkg5zKLWrUB5t2q9wT38hakLDpgpXxwYEylsUBHi994FrMIQuaYvRE8ncfuw4rjxAgs6XUCD2wDGEQ1M_-v9ip7sYn6P69MX8CMxeYmZ_gT7_GTEH8GuZF4YqAxFa7PtT9E5l7ET32R44qgtyXXBH09jAhCK-9i0BPLNc9j1JD2VQoxlAfNNEKLhkW8Aqv9Kmyuz7Oz9zzhKPrz-jq7J-2_L0ckW-E8q7iOqbRL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشوراء الفرقة الخاصة
نار على أعداء العراق</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87828" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87827" target="_blank">📅 15:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNgPu9DC-GeeEh3JeXpo2vQMdWzEZThopiKtqqXKA-5VVdVQnSssdDOP0ftzx0wJfHDTlq7U1uqQ6TKkJXrNt1hd_4mXbZu8okxsn58QiFNNNx8e6nuHQg-Pli-d7_Yjrs3rE9T41GGe-0TKhs1MVV3SfMaxKghM-AZnKdTkenvt38sjMTMcj1FmrOIENGWPG-XLJ2TBe8Y1ZzDK0Iw2suks0IJw64-hh8604C_-uXqnkcLT2MxoGe3nFbuCB7k9jKxPKrT_SInIzOMfBY4rcr7ZMKOypwWAI_9rUMoSlT2rwZwa0E0gPiJJqCR0cGUlYveYCBGXf6fxEt6YOfeT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي
لكانت الجرف الان ولاية ارهابية داعشية سلفية ..
شكرا حميد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87826" target="_blank">📅 15:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏قصف مدفعي متبادل بين مرتزقة السعودية وانصار الله على جبهة كرش شمالي لحج</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87825" target="_blank">📅 15:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زلزال بقوة 6.9 درجة يضرب إندونيسيا، وهو الثاني في يوم واحد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87824" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
الامريكيين ينتجون فيديوهات دعائية بعد ساعات من تداول اخبار عن تعطل مراحيض حاملة الطائرات الأمريكية "لينكولن" واضطرار البحارة للسير في مياه الصرف الصحي على متنها وكيف كانوا يحصلون على طعام رديء. كل هذا دفع البعض إلى القفز من السفينة.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87823" target="_blank">📅 14:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">السفير التركي في سوريا: اردوغان مغرم بدمشق وسيزور سوريا نهاية العام ومتشوق للصلاة في الجامع الأموي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87822" target="_blank">📅 14:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
الحشد الشعبي جزء من القوات المسلحة وحصر السلاح يشمل الجهات غير المرتبطة بالمؤسسات الأمنية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87821" target="_blank">📅 14:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تمكنت القوات المسلحة _بفضل الله_ من استهداف تحشيدات وأسلحة تابعة  للعدو السعودي وزوارق حربية تابعة لأدواته ومرتزقته في منطقة المخا، وذلك بعدد كبير من الصواريخ  البالستية وكانت الإصابة دقيقة بفضل الله وقد أدت العملية إلى تدمير الزوارق…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87820" target="_blank">📅 13:39 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
