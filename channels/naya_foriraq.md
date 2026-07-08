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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعلام العدو: التقدير في إسرائيل هو أن الرد الإيراني سيكون موجهاً إلى دول الخليج وليس إسرائيل</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/naya_foriraq/81919" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=B52JsxxwEQBn7iOoL9cVXHjQuMaL_nTk5B26PF_wR6jzd1VtkE8WFt3lt8zLDx_xwvX4VNfDW84D7kz8hA-CmkCjFmJ5t69EZIaRNHROBh7LqqJvTd8-8ETyzU4CrTwfppGk_4VPm3g-mOfG31aENzOHZEkT2Fmn-XTUfZuWmd3c5EJDo5c2z7d0pAYZDNlYDlnbOjczJIeA9c-4yMB1ZweSu-86KfdNaIoI1OvwGF8rWETJVmu-cK6rMzYz76c17ax7t48NM3oTIDIZW3Mm1Vgu6pScpD2UA8DuuiuJA6t-R5IRuW6-tTokHjNLRYOw8YoXom0VBF-WErAHExPoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=B52JsxxwEQBn7iOoL9cVXHjQuMaL_nTk5B26PF_wR6jzd1VtkE8WFt3lt8zLDx_xwvX4VNfDW84D7kz8hA-CmkCjFmJ5t69EZIaRNHROBh7LqqJvTd8-8ETyzU4CrTwfppGk_4VPm3g-mOfG31aENzOHZEkT2Fmn-XTUfZuWmd3c5EJDo5c2z7d0pAYZDNlYDlnbOjczJIeA9c-4yMB1ZweSu-86KfdNaIoI1OvwGF8rWETJVmu-cK6rMzYz76c17ax7t48NM3oTIDIZW3Mm1Vgu6pScpD2UA8DuuiuJA6t-R5IRuW6-tTokHjNLRYOw8YoXom0VBF-WErAHExPoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان قرب محطة بوشهر</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/naya_foriraq/81918" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81917">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l21p0DFDFG3RACaN2GVsipYhD-8tHLJXYorVGEyhof2blsEWQnDZQkQSfMjAYSzXT3sXHIxN7ldjufDRJGqOl_wJAjkwr9FJYs5STuJJrdAYJ54r6qq5zectMq8R4vf_ojwY9z1VTA5t5x1mi2Uq1egMFVEPOC2wb5qiY4sHhyYzDV2zGzWgdXNpCpfb0U13Od2xtvwdKEeAaQEwmkP0EwUK3d5LoXP3PBxqn0VLqolU-1OQk5aLLYgstStg4DT0Z1qTCwzgmrxrTaJf5MzuxWpjONOTdxhr2ko45uwNyuP01z8Mw_2L8clioCqOUoXxGggwlV19zwRKDDoa6WMpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو يدعي بوجود قصف على محطة الطاقة النووية في بوشهر</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/naya_foriraq/81917" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81916">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">إعلام إيراني: انقطاع التيار الكهربائي في أجزاء من مدينة تشابهار الإيرانية بعد سماع دوي انفجارات</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/81916" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81915">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">القيادة الأمريكية المركزية الوسطى : ‏بتوجيه من القائد الأعلى للقوات المسلحة، بدأت قوات القيادة المركزية الأمريكية بشن ضربات إضافية ضد إيران لتقويض قدرتها على تهديد حرية الملاحة في مضيق هرمز. وتُحمّل الولايات المتحدة إيران مسؤولية العدوان غير المبرر الأخير…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/81915" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81914">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هيئة البث الإسرائيلية: الولايات المتحدة أبلغتنا مسبقا عزمها مهاجمة إيران الليلة</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/81914" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81913">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">إعلام العدو يدعي بوجود قصف على محطة الطاقة النووية في بوشهر</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/naya_foriraq/81913" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81912">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محافظة واسط تعطل الدوام الرسمي ليوم غد الخميس الموافق ٩/يوليو/٢٠٢٦ حرصًا على إتاحة الفرصة أمام أبناء محافظة واسط للمشاركة الفاعلة في مراسم تشييع شهيد الأمة آية الله العظمى السيد علي الحسيني الخامنئي، ونظرًا لتأخر موعد مراسم التشييع،.</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/naya_foriraq/81912" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81911">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات جديدة في بندر عباس</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/81911" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81910">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/81910" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81909">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوي انفجارات في جزيرة خارك</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/81909" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوي انفجارات في جزيرة خارك</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/81908" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81907">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81907" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81906">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81906" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81905">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGgLHmIr14aO1DKwJO1rnxfLypFDa1f4b2pZe2hPjArfQbUJPiwrEUTM3ulX4vp8i_vHyauK73lvBwcKe_UGA_wlQffsfUyEb2CMckLrrLlvCMb7t_w9Alj8G0bJxEUZC31aHuvJxbCuHPORpf1NIduE-lhXy0XhL7Pwib4Tj8NYWXsUea-bvl_Ktfx-t12s3Hhf6y_HN6ZrwhINjUYWFomSo7irP4pL6Wgg-v6nj_RZM_J4l4iDzGKCNpo3hPZWSyoj0hzsHguDnfJ_GoPZtSjxrYD7zP1y3emtE4HQ75Mhreh9SGIPNqBXRuwBxP_UDy2KBzg6xYuvowJ4MGKMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة الإنذار المبكر تتجه نحو الكويت...
قد يكون هناك رداً إيرانياً.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81905" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81904" target="_blank">📅 23:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لجنة استقبال وتشييع القائد الشهيد في مشهد:
نظرًا للاستقبال الشعبي النادر والمهيب الذي حظي به الجثمان الطاهر للإمام المجاهد الشهيد من قبل الشعب العراقي، فقد تأخر موعد وصول الجثامين الطاهرة إلى مشهد المقدسة، ولذلك ستُقام المراسم عند الساعة 14:00.
وستُقام مراسم استقبال وتشييع قائد الثورة الشهيد وعائلته الشهيدة يوم الخميس، من شارع الإمام الرضا باتجاه الحرم الرضوي المطهر.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81903" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a412ac0d.mp4?token=ZP7vGabq9cViahI4trOFQKY2EnVnYuQZFMGjSdyq7p1XL4gmvBkexiWVn6AaVLAZA16Um1M5DgG4QTozpbOY1zwDDXmbUO6vEoigEt0iYu7Rnp9ZcyCT0slDYi8r7YHzAwsKlggyQwG_VLijGAYY5Vp1p1Swgx8JwSmUGmFfvPrsWliaA3zQ6fTYx9WRxKl-2PlFEovcR_euHHHv3LRdV7SScWjdxK1xTECCCqOFPRxtblXKYpGceAudvhG-On8n7RRhdU6gg44ZBRHx2KOeviCyt2Z-4bm4O9irgZWrS9a4Sv_upLEtwaT4iH1d-9PlQwde7eVYMZxSzLEKsGYEbi8O7RPUh6ibPkUTEZxO0U1cnSyciDK_Kspe_zDDarRDLZYlmxkITAlVelRHBWGKEvTZ0mRUnyZ15bEXZcuA1CIsSJp9v9Vu1yxv7tvvMacMDsUb2vbSdbSl34XFoP77R1YypENOdp9aVyGxes6WHQR5KU3_EeFovP_5qpfA-8IO4MdK5CtDtlI6_b76Ck2qJ3Ke_EwSiqoSXtt-N12_8M2zHtmznWBkt6iqux1m7jJI_GhgnsNUVjci2KtNgdxNn7vdyoP0Iy_4x2pFR4z7IXX8be0AYCQx2x3yYgetnVhDEBZulMwwkjVapdjRquDdX9qTRINMtWItF2zZd2Vcl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a412ac0d.mp4?token=ZP7vGabq9cViahI4trOFQKY2EnVnYuQZFMGjSdyq7p1XL4gmvBkexiWVn6AaVLAZA16Um1M5DgG4QTozpbOY1zwDDXmbUO6vEoigEt0iYu7Rnp9ZcyCT0slDYi8r7YHzAwsKlggyQwG_VLijGAYY5Vp1p1Swgx8JwSmUGmFfvPrsWliaA3zQ6fTYx9WRxKl-2PlFEovcR_euHHHv3LRdV7SScWjdxK1xTECCCqOFPRxtblXKYpGceAudvhG-On8n7RRhdU6gg44ZBRHx2KOeviCyt2Z-4bm4O9irgZWrS9a4Sv_upLEtwaT4iH1d-9PlQwde7eVYMZxSzLEKsGYEbi8O7RPUh6ibPkUTEZxO0U1cnSyciDK_Kspe_zDDarRDLZYlmxkITAlVelRHBWGKEvTZ0mRUnyZ15bEXZcuA1CIsSJp9v9Vu1yxv7tvvMacMDsUb2vbSdbSl34XFoP77R1YypENOdp9aVyGxes6WHQR5KU3_EeFovP_5qpfA-8IO4MdK5CtDtlI6_b76Ck2qJ3Ke_EwSiqoSXtt-N12_8M2zHtmznWBkt6iqux1m7jJI_GhgnsNUVjci2KtNgdxNn7vdyoP0Iy_4x2pFR4z7IXX8be0AYCQx2x3yYgetnVhDEBZulMwwkjVapdjRquDdX9qTRINMtWItF2zZd2Vcl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء تتحول ليوم العاشر من محرم
الملايين تشارك الان في تشيع نعش السيد علي الخامنئي في َمحافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81902" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfASp5v-dAKOn2QUtwJKDKlSyh0N2oE5brCpdj-NyRHt_ybFxSOJo-Kw0Ka4Ud3sR2S5FMYM0B-nMpRRbsjx2NZ5LABtcJtrMdwF055XPXcermjBmvGEWeKdzdqtQNeSqTr8YzIbFDvPM7Ng5RG08vv7fIVPoej0bK55PjieqI_oy_Mv3pL4usSfWIXl6NjqZcx0tBc2qKcNOPwSTqFVNikAaUBgzsQHBo0vhY5OdnV0xlcQZWzq8tt4i79uLgroaXtOb3apZfiQ2exXDASM-a8T8oN3f_AYMz_dD0LhUc9iesAlbRM1U5WTby5RRmpSQ3cdLAB_efhjUcVsCWRm_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصلت طائرة تحمل الرقم 79-0001 من قاعدة الأمير سلطان في المملكة العربية السعودية.
في الوقت نفسه، أطلقت طائرة هوابيماها خزان وقود من قاعدة العديد في قطر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81901" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81900" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81899" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81898" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81897">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadf361ee4.mp4?token=hrwv1TC6yfue-3KnVka5jk4sbaYcMyKMcWA8EWnPy5JbCWAxLd3HKsqBYeXpExU2neHdjDlM0YCBtyE6zxKcpklIHdPfupecKNfX4iH8R2ZEOYvX-s_yUjZKZEx2u2nUTs1OiMme2ViiU9k25U30wybco9Qne-QvzIDpmDGIt-kaisWuxBC8KlsZLd0MpNmkHzFvMsR2GjjaMQCIQ-a6vcx8Tiw5cIlmeIPXUm0AbLeL6rGFsuSVmpHoQuaEpha7GOuWKut3Oc4_g1lolZ7qNIpD6lSMNicZhwNjeRHUEIqD-7eN_ebHw3Tfobe-BuDr3fX2YEowiTMKIx9ASOrk52S_5WuWJI2a4Dr9IAIy1tchhBW00dkI1R00FpUdISM6S7vAH2sdm6fKJOM_c4azRd0SeHopP4oOPkmk8vezqZI_0e1YO8OSdcbeXYap3Im1_W-GDn6VLgZlWhu-vaycxe32zeodjn9fd38N8XUiUMDKDrdoVr-CgwPfbAGMzBsAB6j2iLbzRJ4bjRtIe7GhHsxM6VfHYGc199JZWG1lK1Jqhfth77n0_MBmAs9fCk75eTib1IPIoH5wmdC83YGBa2mHWDZvbkIFQRPzP3MQDWog2lY249sXeovWnoWq2_Uv3eh9aljo4z9QKU3nb19hlS2TWkZ9T60IeosM-m7OJIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadf361ee4.mp4?token=hrwv1TC6yfue-3KnVka5jk4sbaYcMyKMcWA8EWnPy5JbCWAxLd3HKsqBYeXpExU2neHdjDlM0YCBtyE6zxKcpklIHdPfupecKNfX4iH8R2ZEOYvX-s_yUjZKZEx2u2nUTs1OiMme2ViiU9k25U30wybco9Qne-QvzIDpmDGIt-kaisWuxBC8KlsZLd0MpNmkHzFvMsR2GjjaMQCIQ-a6vcx8Tiw5cIlmeIPXUm0AbLeL6rGFsuSVmpHoQuaEpha7GOuWKut3Oc4_g1lolZ7qNIpD6lSMNicZhwNjeRHUEIqD-7eN_ebHw3Tfobe-BuDr3fX2YEowiTMKIx9ASOrk52S_5WuWJI2a4Dr9IAIy1tchhBW00dkI1R00FpUdISM6S7vAH2sdm6fKJOM_c4azRd0SeHopP4oOPkmk8vezqZI_0e1YO8OSdcbeXYap3Im1_W-GDn6VLgZlWhu-vaycxe32zeodjn9fd38N8XUiUMDKDrdoVr-CgwPfbAGMzBsAB6j2iLbzRJ4bjRtIe7GhHsxM6VfHYGc199JZWG1lK1Jqhfth77n0_MBmAs9fCk75eTib1IPIoH5wmdC83YGBa2mHWDZvbkIFQRPzP3MQDWog2lY249sXeovWnoWq2_Uv3eh9aljo4z9QKU3nb19hlS2TWkZ9T60IeosM-m7OJIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تدمي القلوب لتشييع السيد الولي بين محبيه على أرض كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81897" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مشاهد تدمي القلوب لتشييع السيد الولي بين محبيه على أرض كربلاء المقدسة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81896" target="_blank">📅 23:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسالة السيد الشهيد علي الخامنئي لنعيم قاسم وحزب الله: أنا معكم أدعمكم اطلبوا ما شئتم سأكون بكل قوتي إلى جانبكم لا تخشوا حتى لو وقف العالم ضدكم فأنا والمؤمنون والمجاهدون ومعكم الله والملائكة معكم أدعمكم</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81895" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وداعا يا امام المستضعفين</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81894" target="_blank">📅 22:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2da09f92f.mp4?token=V12PbyZ6jaTv0JYF0HPCCqsuWvF3k8m-LldzZV6okmSWT11gjM0NhBclSY8L4uk9p_I1WbU3ocSRHZbMvw2ok5iL7tiW4Ek8PcDWWaiX5Y-XV3yh5ZvAPogtEeQzH-_0-8ckq8gPiFqvFVmSi6SHTF9WECT8cfiOeR7ZPHuc_jci_Yl1kRxH-s1YvCkVtbpTThMFjxOoo9BW1dkm43mITmMtCIWuwHiDYv66nDLXF2nAnZwscZxqnovGmOfJlSDYD9OtyeVQ02pb06yBbQbn4xY2_GE5y1ejv7NU1HaTwSKaTstWBNdQQ3eQD7FuVdO-PB5vk54e9iC8wxjrMw-n4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2da09f92f.mp4?token=V12PbyZ6jaTv0JYF0HPCCqsuWvF3k8m-LldzZV6okmSWT11gjM0NhBclSY8L4uk9p_I1WbU3ocSRHZbMvw2ok5iL7tiW4Ek8PcDWWaiX5Y-XV3yh5ZvAPogtEeQzH-_0-8ckq8gPiFqvFVmSi6SHTF9WECT8cfiOeR7ZPHuc_jci_Yl1kRxH-s1YvCkVtbpTThMFjxOoo9BW1dkm43mITmMtCIWuwHiDYv66nDLXF2nAnZwscZxqnovGmOfJlSDYD9OtyeVQ02pb06yBbQbn4xY2_GE5y1ejv7NU1HaTwSKaTstWBNdQQ3eQD7FuVdO-PB5vk54e9iC8wxjrMw-n4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كربلاء المقدسة تعج بالملايين لتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81893" target="_blank">📅 22:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81892">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📰
‏وول ستريت جورنال: العراق يوافق على مطالب أميركية بوقف تدفقات الدولار إلى الميليشيات الإيرانية
ضوابط عراقية مقابل رفع إدارة ترمب تعليق شحنات الدولار لـ 4 أشهر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81892" target="_blank">📅 22:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8Q84kxdTzeABL1tfxBeRGemiidCncZmhqnWDEjeylALnqFWCa59BmAsruh6YD98dwzxvW_URQGHfQMul410uIuVDSTdbRTv6hId1kQIE4vvnf7xpnmxe6Wz6eRyZg0bHEpaXVdG8RllCC6fYcNkC_0jVzq18KllxCU1Sl7xuxnf2e0yMx0nP0zPVsWj3gOqjob0uRKkxA8bUu5g0p02zWijlH3X1FGVWDkEjci6Bz0sFQ0lgfZRKQS6_16ge-HTG9SJmvI8lKVco5Ch4NH3HfkqRGLikwPd4_90YzHO6hsK91b6tvuidMiykDvchmsx_wcOxj2Q8g74XZDoGHJXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
الخطّ العاشق لقائد الثورة الشهيد في وصف الإمام الحسين عليه السلام
▪️
بنفسي أنت، بروحي أنت، وبمهجة قلبي أنت…
🔹
بسم الله الرحمن الرحيم
من هذا الحسين الذي هام العالم كله بحبه؟
وما هذه الشمعة التي أصبحت الأرواح كلها فراشًا حولها؟
يا شعلةً متّقدة، يا نورًا ساطعًا، يا من تدفئ قلوب الخلائق!
من أنت بكل هذا الشموخ والجلال، وبهذا الجمال والعذوبة، وبهذه الهيبة والاقتدار، وبهذا الجمع الغفير من القلوب التي تسير في ركبك، وبملائكةٍ يتنافسون مع البشر على مرافقة موكبك؟ من أنت يا نور الله، ويا نداء الحق، ويا فرقان، ويا سفينة النجاة؟ ماذا صنعت في سبيل ربك حتى كان جزاء ذلك أن يكتسب كل ما يُنسب إليك صبغةً إلهية؟
بنفسي أنت، بروحي أنت، وبمهجة قلبي أنت، وسلام الله عليك يوم وُلدت، ويوم استُشهدت مظلومًا، ويوم تُبعث فخرًا ومفخرةً.
19/5/2014
📩
تقريظ قائد الثورة الشهيد على كتاب
«النوافذ العطشى»
، يوميات نقل ضريح الإمام الحسين عليه السلام من قم إلى كربلاء.
قائد الثورة الشهيد عاد الليلة زائرًا لكربلاء من جديد، بعد 69 عامًا.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81891" target="_blank">📅 22:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81890">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقجي: كل الشكر والامتنان للعراق الشقيق حكومةً وشعباً ومرجعيات دينية على حسن الاستضافة ومهابة الوداع في تشييع إمامنا الشهيد
شكراً لعراق الكرم والأصالة على هذا الوفاء</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/81890" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81889">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محافظة كربلاء المقدسة تعطل الدوام الرسمي في المحافظة ليوم غد الخميس الموافق التاسع من تموز الجاري نتيجة استمرار تواجد الحشود المليونية في المحافظة للمشاركة في استقبال وتشييع الشهيد المرشد الأعلى للجمهورية الإسلامية الإيرانية آية الله العظمى السيد علي الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81889" target="_blank">📅 22:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81888">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محافظة المثنى تعطل الدوام الرسمي ليوم غد الخميس الموافق 9 تموز، لإتاحة الفرصة أمام أبناء المحافظة لإكمال مراسم تشييع الجثمان الطاهر لقائد الثورة الإسلامية، سماحة آية الله العظمى الشهيد علي الخامنئي (رضوان الله عليه)، في محافظة كربلاء المقدسة، وعدم استعجالهم بالعودة منها، تجنبًا لمخاطر الطرق خلال ساعات الليل.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81888" target="_blank">📅 22:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81887">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d333d0597.mp4?token=celCRHyXm_pIt8JTZ4gEEP9nBbXAwTzcg2qet8f8e2oETmN6sytJV5E8xrnNexHpF1RxfwG27bQnPsPkDM8tfKx8_xqZBII24ZyxEy8sK_v4vU7T27deg5qnkavuFO-YOvNmAu3KIj0-WkJTFXkcJctFE7Moa9eW_adRSI16Jv9ZdWEOtLs4IqyNwBXiLsjy2HMEMFTetZ9TcY7D5jokyH3H8YJyTE4PV5G5AbaxkpaQm-VR8FWinCbecYkwxbc_e8AP9Hz-8aa0-n559Y43byDr7FfenNYCx1VrWr0BA6vihT8H65BtFVomN9oAK9imrzhwW9_dh_1oadciVl6EbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d333d0597.mp4?token=celCRHyXm_pIt8JTZ4gEEP9nBbXAwTzcg2qet8f8e2oETmN6sytJV5E8xrnNexHpF1RxfwG27bQnPsPkDM8tfKx8_xqZBII24ZyxEy8sK_v4vU7T27deg5qnkavuFO-YOvNmAu3KIj0-WkJTFXkcJctFE7Moa9eW_adRSI16Jv9ZdWEOtLs4IqyNwBXiLsjy2HMEMFTetZ9TcY7D5jokyH3H8YJyTE4PV5G5AbaxkpaQm-VR8FWinCbecYkwxbc_e8AP9Hz-8aa0-n559Y43byDr7FfenNYCx1VrWr0BA6vihT8H65BtFVomN9oAK9imrzhwW9_dh_1oadciVl6EbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرقة العباس القتالية تستقبل جثمان السيد الشهيد في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81887" target="_blank">📅 22:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnCd-jrsirZTWPthegCAZ1YztVZGM8m_TUzfzoh3d4vwbDVaTaksFifN6bGFyLa_kGTXrg1frUoqqARizI9a7mmkNOA8VBJ4JS2UPTfVVoBNEtYo-R5tnP68mEi0PvRF6yEDen98w1G6l0eoD1iBi0arVM77VAEcRHWnIc-vYw0rJ1lUMVNW-9KbzQ2j7AasRrgs-7gVmizP2w0DZNE_dewtvH61d9Dl8lsNKziva8D60o_owfFE5X5VBs0R-sRpGq2zikhLdYACAwKwr4KlazndGJEfaQ5uPbQ5mr7DnCYulBIYPPxAw6xQs0shtFrLrcdruYRXtFiTyBPsQK-Gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حشودٌ مليونية تُحيي مراسم تشييع السيد الشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81886" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81885">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حشودٌ مليونية تُحيي مراسم تشييع السيد الشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81885" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81884">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfca02e00.mp4?token=qhvD07Eufz6gR7xXFH6364MrYM01m2LfwKYghysfC5itT-uwqYgnH-j4e-bQg1YVbE9smGoQpw7Tw-csSMLSWhyghFIATpz5UVNE4EamehP_ASL9haZTF2sTxi-wWKiASEQGx7YzFNJygwSxjWPplhr5UUdt12ykIlXwn1NLU5Tw7GNX5ZW8z794lpM7ngj8mNkK1I-ZCW6jyX-_O6fUAyhOzuoO4XxW9jcQWoNDd_nqmMGRxRPR-D829Ko9cqmTmwpevr36bnEtzHC9jqaFJaIA7kE11Mdz6FgJcA4RRb9ZvAeq5Zl8TxpUvZ2solBxl9l0PJpGIX-zQwX6F-mxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfca02e00.mp4?token=qhvD07Eufz6gR7xXFH6364MrYM01m2LfwKYghysfC5itT-uwqYgnH-j4e-bQg1YVbE9smGoQpw7Tw-csSMLSWhyghFIATpz5UVNE4EamehP_ASL9haZTF2sTxi-wWKiASEQGx7YzFNJygwSxjWPplhr5UUdt12ykIlXwn1NLU5Tw7GNX5ZW8z794lpM7ngj8mNkK1I-ZCW6jyX-_O6fUAyhOzuoO4XxW9jcQWoNDd_nqmMGRxRPR-D829Ko9cqmTmwpevr36bnEtzHC9jqaFJaIA7kE11Mdz6FgJcA4RRb9ZvAeq5Zl8TxpUvZ2solBxl9l0PJpGIX-zQwX6F-mxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لتدمير طائرة بدون طيار من طراز MQ9 صباح يوم 8 يوليو 2026، بواسطة نظام الدفاع الحديث التابع للقوات الجوية للحرس الثوري الإيراني بالقرب من خورموج، محافظة بوشهر.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81884" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68213b66f.mp4?token=ncgW6KYbTMwZZn4fl1E6NrryhNTzii5wknDsOu7L2Hopg5dma6eTJSRuDGsLjNW1-NJskJhdOAvBszC9FZl1jHBhH_wvgfxpEHSs8oCilWo3lJvRGaHJ_ZqV4bpP4HWKNHbAJlq0VZlTIK-G2h0neo0I_kYL66cvKxEfcXVCpkT6MAVL7OmlLM7f80fzCiKhm3dNX1FIYDhJb2eXNqj3jIqOlH58vLyqdC9xygkApv405wcPe8wZ4N7qVc4x_-xD36HYNPsoaLUm-6taQJhyCEH2IBqsw-M5BA7XVY2DaAC19Vecifft9_soOvVeqmJwk8JjocvwMT7Om6NSd7ETIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68213b66f.mp4?token=ncgW6KYbTMwZZn4fl1E6NrryhNTzii5wknDsOu7L2Hopg5dma6eTJSRuDGsLjNW1-NJskJhdOAvBszC9FZl1jHBhH_wvgfxpEHSs8oCilWo3lJvRGaHJ_ZqV4bpP4HWKNHbAJlq0VZlTIK-G2h0neo0I_kYL66cvKxEfcXVCpkT6MAVL7OmlLM7f80fzCiKhm3dNX1FIYDhJb2eXNqj3jIqOlH58vLyqdC9xygkApv405wcPe8wZ4N7qVc4x_-xD36HYNPsoaLUm-6taQJhyCEH2IBqsw-M5BA7XVY2DaAC19Vecifft9_soOvVeqmJwk8JjocvwMT7Om6NSd7ETIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحبين العراقيين للسيد الولي الذين أتوا من جميع أنحاء العراق يفترشون الطرقات منذ ساعات الصباح الأولى بانتظار وصول الجثمان الطاهر للمشاركة بتشييعه</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81883" target="_blank">📅 22:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81882">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd77a340a5.mp4?token=g30LHKk3hqMz_X0Z58lkRxSgcUu9sPJwVzCsD-oeaDAWUsb8dmRm9vq0igeDiwKLlMY8Y64MHg9RDe2F_HzDApgn8ZMLxO0rgxdnUpEgSkcWC7ZvNU6XglAObBY5Kw8KOIUlA0ijNCp9dThQlC47Gdd9CXw8LuhPM4KUYE6Xf2lNGFif42MRhLy2gobjKnTxaBRLcPOkAop7ocg7wyC6Is1GAUXlqvNkx49QpkT319IencHpUd1LcoCUrwVHetfQI2wC7KUTmV7454MP0JnY79yQS6LWO00EyS8uQ4To1IG1cv4Ax_d9dS0SGwLpbhWRHfB-N1scQdKCPrLgTUB5e3SamE79hrqIsf0GCvqRXPsefT8OwOjDpvni4gdkLqOMFSITPBG5RgrCLEMtXXSuU51zx8PGM_mVBiHKhljcJsTKvl7pXIcmSrwJEZFIKxH0-jd4zNhomuWzQopYszq0xxQNtidCjq_A1Kmvwat4XTFloYEw-YicPPK_ond7IPaRB6qrVbDUq99348IB6lN7VxoIxdZ61-ITZb9HHrZ5aS79e2VM7pzZu94jdhIDTu7nnG_-48u3wKpiJlsqp1XfGxfCdyNo_9mGgAB5McctMY0Ld4XDAaxvtL6H3vTtkMAl-ZWRGfDVR2J2Cau29qV4nxAx3TEy02NEPlQS55CTeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd77a340a5.mp4?token=g30LHKk3hqMz_X0Z58lkRxSgcUu9sPJwVzCsD-oeaDAWUsb8dmRm9vq0igeDiwKLlMY8Y64MHg9RDe2F_HzDApgn8ZMLxO0rgxdnUpEgSkcWC7ZvNU6XglAObBY5Kw8KOIUlA0ijNCp9dThQlC47Gdd9CXw8LuhPM4KUYE6Xf2lNGFif42MRhLy2gobjKnTxaBRLcPOkAop7ocg7wyC6Is1GAUXlqvNkx49QpkT319IencHpUd1LcoCUrwVHetfQI2wC7KUTmV7454MP0JnY79yQS6LWO00EyS8uQ4To1IG1cv4Ax_d9dS0SGwLpbhWRHfB-N1scQdKCPrLgTUB5e3SamE79hrqIsf0GCvqRXPsefT8OwOjDpvni4gdkLqOMFSITPBG5RgrCLEMtXXSuU51zx8PGM_mVBiHKhljcJsTKvl7pXIcmSrwJEZFIKxH0-jd4zNhomuWzQopYszq0xxQNtidCjq_A1Kmvwat4XTFloYEw-YicPPK_ond7IPaRB6qrVbDUq99348IB6lN7VxoIxdZ61-ITZb9HHrZ5aS79e2VM7pzZu94jdhIDTu7nnG_-48u3wKpiJlsqp1XfGxfCdyNo_9mGgAB5McctMY0Ld4XDAaxvtL6H3vTtkMAl-ZWRGfDVR2J2Cau29qV4nxAx3TEy02NEPlQS55CTeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النعش يدخل المسار المخصص</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81882" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81881">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cf632ba4.mp4?token=Hz-UtKeRD4qyoGvyS0W0SOdh-IJiGCKTvUssM-QcTeZ4Y1UQpZI_CviSYEDx7u8fFR8dVa3WYly7GB4wahfwgB3iD7gPtNyB42oGmNP2kOddvvW2yv-Q1eHgZjzsWWm1y6w3aVSsDth88awQ43ijwnlxZqMR8BHz7Q-9PktnQgPiFBkJtYmLfrdk8sGA8TCuwKLVx7xFqp0dtsQPj7gASRgy6SI_njhXbBPAcu3vu5ZqAxm5gzDdVdZdRC6KyQebpuCcyMUNV5c5i_CeLcfFcfvC73Gq3QcFNTI3ZsSlH9ASQI7R5NoMwmyvtEP8o8ZRMPtzdQ1feYzQZVbD0t2cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cf632ba4.mp4?token=Hz-UtKeRD4qyoGvyS0W0SOdh-IJiGCKTvUssM-QcTeZ4Y1UQpZI_CviSYEDx7u8fFR8dVa3WYly7GB4wahfwgB3iD7gPtNyB42oGmNP2kOddvvW2yv-Q1eHgZjzsWWm1y6w3aVSsDth88awQ43ijwnlxZqMR8BHz7Q-9PktnQgPiFBkJtYmLfrdk8sGA8TCuwKLVx7xFqp0dtsQPj7gASRgy6SI_njhXbBPAcu3vu5ZqAxm5gzDdVdZdRC6KyQebpuCcyMUNV5c5i_CeLcfFcfvC73Gq3QcFNTI3ZsSlH9ASQI7R5NoMwmyvtEP8o8ZRMPtzdQ1feYzQZVbD0t2cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تقلّ الجثمان الطاهر للشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره) تدخل المسار المخصّص لمراسم التشييع في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81881" target="_blank">📅 22:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81880">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">العجلة التي تقلّ الجثمان الطاهر للشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره) تدخل المسار المخصّص لمراسم التشييع في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81880" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81879">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بدء مراسم التشييع الشعبي لجثمان السيد الشهيد علي الخامنئي في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81879" target="_blank">📅 21:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81878">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2076bbd163.mp4?token=RkDr7oWSjoCbWsUaIVbYH8LXV0G7O9bS-oT9-YDJjaZOiTJHjQkzIOrE1V-ju6pmYrghORL_6HALG6iQLqqzrxnx6JRd581fq3o9D43sa1ZCve39ZZ0ciqsiDdjmiYwLnpvbyoiTDjb5khl4f7zlAUcUehL3YuKT74BBhTQ3KICF_2kGXQzV9GyylmC454N8LHbM2ugo6OZfSR_tv3uOwp_18ZzEOfwkL5HZBFmXXMJZtKRI-DznQNP_sgC6aeBs-ZWzbbAAtFQs6BpknuN9IWY8UEQfbDTK9qkNPtD6YSBXf4zJn5O5817ilBsXLS3pZ1zsEVcnfaayBCPPmSlgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2076bbd163.mp4?token=RkDr7oWSjoCbWsUaIVbYH8LXV0G7O9bS-oT9-YDJjaZOiTJHjQkzIOrE1V-ju6pmYrghORL_6HALG6iQLqqzrxnx6JRd581fq3o9D43sa1ZCve39ZZ0ciqsiDdjmiYwLnpvbyoiTDjb5khl4f7zlAUcUehL3YuKT74BBhTQ3KICF_2kGXQzV9GyylmC454N8LHbM2ugo6OZfSR_tv3uOwp_18ZzEOfwkL5HZBFmXXMJZtKRI-DznQNP_sgC6aeBs-ZWzbbAAtFQs6BpknuN9IWY8UEQfbDTK9qkNPtD6YSBXf4zJn5O5817ilBsXLS3pZ1zsEVcnfaayBCPPmSlgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد الولي بين سيل من المعزين</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81878" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_rB20xRTZlBxz8bzh1MpW5xghpxqpuePe8InwttraF1ZLzOL7Omq9bALyHK1-taACKgn5kbicdkBOHq2ut8iEWaPNt2dEaQPCN9wPtrXbo87da3OG4ONx2WUDYD7X6XDNluXhLq2V-YPOmrVVG9p76J0CLDI0w1EEluPu2wi8PX3SqNC5fJWtUq0I9Z6jkSqfOSaVc6jPCTtiD3gZLHXI23_-ZFXvE1eshIquQz4Oy_oj_39d9LntyayVZwqVJmfBHQyH7qfY0i0zm6fyU2STx2nWA1Z1JxdtAqpb56Jd8ZG9nCtOiB5VoWFlxt30NvneB5vrzrVKEtgOi_Yanaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_1nwXI8kE5jGehprdzISqP1Dw4OWb_RdAZqE575lbX_BCs8Tc1SJv0Z4GksXpuYe9VUxecb9mIwywEHxfTe4qbm3_9XMAapoD0yH-wcs8nGyP4JgtbH3HCxjdR9fWAbgpO9MrdtlOpRmrhQLJsjufRaZ-ozWrlWu2ZkL4J4txCnRlVocSsRKoeRnXQ6DM30_qxzshFElYTMPOMJcNjQbt_o1Yt3tJeKsqm7wZox9yx3lyYy9FLprM35PkSdb1U-el0w4lhPgeKeaTY0wr37b0TGptgW906E7cJXM3LXkd__EG5zWgEyjk-c52BltVQ0o2qbJtAGSGKIYorNigYeoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الجنرال اسماعيل قاآني والحاج ابو الاء الولائي يستعدان لاستقبال النعش الطاهر في العتبة الحسينية المقدسة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81876" target="_blank">📅 21:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05d8d1fc.mp4?token=WWG43BkfdOsoZV9nF-89UlwnnM-0AkZ6ENxBydpOzv5Q-TUU3DNb78tS5e5dGADSrdNtTj52s-629ZTKRJKOTIRuwbEZvM0H9xq6o-rDJhxyYmLiR8ryvQ5n1oapxWpaVxSHohy-yu_FOvVdmo-6dnQnlBmAn9_Rxhn80EMENlnB7SK5aL5watpE_5lALgfevZSt29tTSOtC5Reohtr8A8Jd7Ot45tKn0r7sB-Ryf2-l6q0-tgwdS4eiAMGs69988vJPjXjVa1OMANuHDApVAKCK_IxHKuLEl_23sREhDGraiIP_R-KTrT3KdHeyWy92A0evdBEnNKt01bJd1883eFmGta9dJRbr1bzbnc53hYkWIwYgb7cD7m1YaaztOlk0RAsQ3To9fZM49Fu2ObLTEgJHND2dxlgjArUTkqx5g1sfTCcHoX1lCazYKlTh4wy0f_8-q0izfRdczoC4Dxnpi13E5NSkRLH2vZcojC5VdfhR2HJegd1EbKKZL-uziVrQw2w6lZlXlNgd9BUi7wJpIGepvGZUDDgiUgjjblydBS6-eCXUO9ytOzacLCrMmV_x2WMAKO1nLzcC_GynqPeggS3pPclQjiAIkWRuMWR-2pev6T1Y_lqebWpy1as0MDVH7FgoNEtlGwxwLc0pY510wInq9vJH5gGbPklfAYTLTBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05d8d1fc.mp4?token=WWG43BkfdOsoZV9nF-89UlwnnM-0AkZ6ENxBydpOzv5Q-TUU3DNb78tS5e5dGADSrdNtTj52s-629ZTKRJKOTIRuwbEZvM0H9xq6o-rDJhxyYmLiR8ryvQ5n1oapxWpaVxSHohy-yu_FOvVdmo-6dnQnlBmAn9_Rxhn80EMENlnB7SK5aL5watpE_5lALgfevZSt29tTSOtC5Reohtr8A8Jd7Ot45tKn0r7sB-Ryf2-l6q0-tgwdS4eiAMGs69988vJPjXjVa1OMANuHDApVAKCK_IxHKuLEl_23sREhDGraiIP_R-KTrT3KdHeyWy92A0evdBEnNKt01bJd1883eFmGta9dJRbr1bzbnc53hYkWIwYgb7cD7m1YaaztOlk0RAsQ3To9fZM49Fu2ObLTEgJHND2dxlgjArUTkqx5g1sfTCcHoX1lCazYKlTh4wy0f_8-q0izfRdczoC4Dxnpi13E5NSkRLH2vZcojC5VdfhR2HJegd1EbKKZL-uziVrQw2w6lZlXlNgd9BUi7wJpIGepvGZUDDgiUgjjblydBS6-eCXUO9ytOzacLCrMmV_x2WMAKO1nLzcC_GynqPeggS3pPclQjiAIkWRuMWR-2pev6T1Y_lqebWpy1as0MDVH7FgoNEtlGwxwLc0pY510wInq9vJH5gGbPklfAYTLTBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد الولي بين سيل من المعزين</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81875" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الجثمان الطاهر في شارع الشهيد ابو مهدي المهندس بطريقه إلى منطقة مابين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81874" target="_blank">📅 21:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc47e46f.mp4?token=AdNU7UklZGGPpeyaHgHOURmxxDzv_VjDJjAhAGcWktRZXiYwJNmRdQL68uVNLVgOiLoK7Bp9TS99eZJOZYvW8goJxVt2Ct16taPuwb0naUGKQAGXHWmMj9VZxpPxqSWPgxXwpNzDlwUDTVSPjXcG_sCgAzz4jqewtBqiT7P66v1ewD4N8bXrw7GUgeGYR-AIsaiWGYQNIh87zpuqqKXBmzwwANvzBOzLZ_MbE98ALdJ8lDGLDAVJPTh9_zas4AcRK3nM2sIErjTSlJQk0_D3yM37pm-0o1pDpwgp0Tb8KOxngk6MInWsrEQ7SJmXO5-Y11Riu6ygmK90K-5SgNLO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc47e46f.mp4?token=AdNU7UklZGGPpeyaHgHOURmxxDzv_VjDJjAhAGcWktRZXiYwJNmRdQL68uVNLVgOiLoK7Bp9TS99eZJOZYvW8goJxVt2Ct16taPuwb0naUGKQAGXHWmMj9VZxpPxqSWPgxXwpNzDlwUDTVSPjXcG_sCgAzz4jqewtBqiT7P66v1ewD4N8bXrw7GUgeGYR-AIsaiWGYQNIh87zpuqqKXBmzwwANvzBOzLZ_MbE98ALdJ8lDGLDAVJPTh9_zas4AcRK3nM2sIErjTSlJQk0_D3yM37pm-0o1pDpwgp0Tb8KOxngk6MInWsrEQ7SJmXO5-Y11Riu6ygmK90K-5SgNLO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثأرنا عظيم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81873" target="_blank">📅 21:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgj6RCQ9hl5jRsyJw0OOghgfoRvCYCDlapr-Krm4dIDrHq87y22X5xC5lukRNbyuc-UUS6zhRmLTqAMg1HLGpXbdNzBjyWRZCYquz76RX0RAQ-raM9d-FPmr6r_m3uHajP-yW-UlZQCyPxsDKUeK0Xi3ka3fTk1SywMqQLemC6nh0_tbAA6eAbAenP1HCagOVKvIZkmZM7qymWX_y3X0ohEqe7CASwkF-K7EKko2A5wcQIBqRXKNs8eaPrTfoqlpOmSLiliO1M2fnZIiPKwVIm4BKRCY34GIbLyopWqEIsuprLiFwXVIuZ5FrKgFtmWaegNyk2S9iIj3IPt0bQrfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81872" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9778d57aaf.mp4?token=vo9E2XuoJDGJmIcdCfgiXnBHkU3WCEfw2FhEDyk79kpXVF-3LJXMBVqAm3JjMLBLRdLK7AhPCqUFB2naaoSMU12THXIjcijjHe3mxPIiNEkhCF7qszRXbDQS7TNI62P9Q44ZyD1EcYVDtozmjfBXKmE_u5wuOzuVlpKK2zS82wFEZ5152VvAsRSqcqidZJGo9LBE7oLBv8v8zZKkZ8Izzb3eM2dRJO5R-MWVNLm-iXyfrOIpi5oXAJY70urniC9B3w-W6841ZcMbi3HE0Ag9zoDUPXkhwB_py4KB9Zm1jWTKrZ5cV7gUHANkEdFsEkW2e0dCaqGPar0aE9RNxRB3UoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9778d57aaf.mp4?token=vo9E2XuoJDGJmIcdCfgiXnBHkU3WCEfw2FhEDyk79kpXVF-3LJXMBVqAm3JjMLBLRdLK7AhPCqUFB2naaoSMU12THXIjcijjHe3mxPIiNEkhCF7qszRXbDQS7TNI62P9Q44ZyD1EcYVDtozmjfBXKmE_u5wuOzuVlpKK2zS82wFEZ5152VvAsRSqcqidZJGo9LBE7oLBv8v8zZKkZ8Izzb3eM2dRJO5R-MWVNLm-iXyfrOIpi5oXAJY70urniC9B3w-W6841ZcMbi3HE0Ag9zoDUPXkhwB_py4KB9Zm1jWTKrZ5cV7gUHANkEdFsEkW2e0dCaqGPar0aE9RNxRB3UoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا إله إلا الله
وصول جثمان الشهيد السيد علي الخامنئي إلى قلوب العراقيين المنتظرين في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81869" target="_blank">📅 21:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9890507f.mp4?token=krrNmZWV0QIurkhzrLE28CPQWnj5UQANHmaJETp18rfmXtJJWLTBjBgSv7k-AOaxgzuqm0myTa4hmLSTcpgBU2b7g_kJs-W-UFpOLTrsRuWUSCqJPSxVKnsj2TUoU7QDi3wvI24mJGnoA_05OqOEFLDiOCyjZDPa2hx6xQhfMhbWjq95OAe_B_F75_KwmjcP0D4iq6Vuo-2a7Bzq0hrXvBLH727i-Kcyt6AuCITWEhiWzR3iStv-mJOW6K4fwLFhevF8AMeYS0cjNBlBkS7zu3nWYiScuFz3oZbd2Rv9WUFfkSSNxi3g9ayDlRNCdrrMMimlxag5dT3EkVBpbmkzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9890507f.mp4?token=krrNmZWV0QIurkhzrLE28CPQWnj5UQANHmaJETp18rfmXtJJWLTBjBgSv7k-AOaxgzuqm0myTa4hmLSTcpgBU2b7g_kJs-W-UFpOLTrsRuWUSCqJPSxVKnsj2TUoU7QDi3wvI24mJGnoA_05OqOEFLDiOCyjZDPa2hx6xQhfMhbWjq95OAe_B_F75_KwmjcP0D4iq6Vuo-2a7Bzq0hrXvBLH727i-Kcyt6AuCITWEhiWzR3iStv-mJOW6K4fwLFhevF8AMeYS0cjNBlBkS7zu3nWYiScuFz3oZbd2Rv9WUFfkSSNxi3g9ayDlRNCdrrMMimlxag5dT3EkVBpbmkzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد القائد بين جموع المعزين العراقيين</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81868" target="_blank">📅 21:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25353e2c37.mp4?token=gudpkChZ3fDCpaABHdB2kpw-E5IUl4JRQPShzpD0oWyG8QFiFIWer0O0bOmqrs8j_m4V2yUNNOANA8UAuI3WtFFOSQHEJTX8hAynhXQip4g3sSd4A3yFFt-u8RjNJifsbKT9kVzDviFL2AXUonGjJANhyWb4yjI6YJcRwmemRh8erqMeDgKLWau9wPEpoGvFaPnvt05PjPP4BUjrsDMC-0nnK4YR9zoXGSb8f8j8XQceHDhWlRKG_N_y5xm5grjV1PzQG9GuvWxuwA7y_PQcO031maTeKLmp8ZJLRXcQVpbYOTkUi6z1w8WOsvoW6Q3h3pbvfGBxBihGT5viw7HuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25353e2c37.mp4?token=gudpkChZ3fDCpaABHdB2kpw-E5IUl4JRQPShzpD0oWyG8QFiFIWer0O0bOmqrs8j_m4V2yUNNOANA8UAuI3WtFFOSQHEJTX8hAynhXQip4g3sSd4A3yFFt-u8RjNJifsbKT9kVzDviFL2AXUonGjJANhyWb4yjI6YJcRwmemRh8erqMeDgKLWau9wPEpoGvFaPnvt05PjPP4BUjrsDMC-0nnK4YR9zoXGSb8f8j8XQceHDhWlRKG_N_y5xm5grjV1PzQG9GuvWxuwA7y_PQcO031maTeKLmp8ZJLRXcQVpbYOTkUi6z1w8WOsvoW6Q3h3pbvfGBxBihGT5viw7HuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلام علي حداد عادل، برفقة معاون وزير الخارجية الإيراني، يتواجدان في الصحن الحسيني الشريف، في انتظار وصول الجثمان الطاهر</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81867" target="_blank">📅 21:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0405b0ba29.mp4?token=jBaE4C58gS6TxROcPblREeo2EeLgC_9cEZbcAB0Oi1hFuYgANZJAEQGwmddUsQ7Xv5pGnIaqEpik0iyRwaWlTPpBn3FZHkqw5YdC1WFBENdjsrRVgq3cmLVUg_gXcxafvwbgfj6QzfNR0NTIYikzozcJm76bgFJl8IGipmOW4y7TmEQNQTMsgod6k5HWimPzCnlAH4l-ySIQ4IoK_n4pdqgt_q1gd8GYhvdWM-gFc6MBJPnpto-A6a7rlGJf1WoqSYO_95ZuxfQjst7iZapojx10EqdREQFbWehHmCMO8HSkK1pDmFx4fJ8xKh2yHlP3kaIpPOoLBe9ndL9-nQMG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0405b0ba29.mp4?token=jBaE4C58gS6TxROcPblREeo2EeLgC_9cEZbcAB0Oi1hFuYgANZJAEQGwmddUsQ7Xv5pGnIaqEpik0iyRwaWlTPpBn3FZHkqw5YdC1WFBENdjsrRVgq3cmLVUg_gXcxafvwbgfj6QzfNR0NTIYikzozcJm76bgFJl8IGipmOW4y7TmEQNQTMsgod6k5HWimPzCnlAH4l-ySIQ4IoK_n4pdqgt_q1gd8GYhvdWM-gFc6MBJPnpto-A6a7rlGJf1WoqSYO_95ZuxfQjst7iZapojx10EqdREQFbWehHmCMO8HSkK1pDmFx4fJ8xKh2yHlP3kaIpPOoLBe9ndL9-nQMG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد الولي بين المشيعين في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81866" target="_blank">📅 21:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7113041ff6.mp4?token=ThLg5uz2I8Diyw1bZjEZFgzvKgPW7Z24XTR3skF45PS6X4PSkbRLidpyi7W-bczmq4_YLdbpGmsfZiqQU6TDLSEcDfnW12TZB1OnuR-bbOsl7IdALcfzfR-yGAo_2x9SQOcGJzohTnsEoVsrZTCtOwV3tCXk99C-vPHbMAM6mRefKF5ljk48HDdZ7WpbjaiZdhgl3IaKxK7SsDqHhEDbYVbjJuRZAq3rcwL5fU3uw4py0GOPon8KRlvJ9BDMd0eC2kJ8PdQgviAoeKbS8q4cfTUd9833Yi6cZq6MEhHHieIssm56tCNbOROp96dVjdfWxMflPVXyrkO6XlfRRMNDUSMbMucKLlpT-O2gaDFB8VJGWf8jrGeYIu4juMY1GktFDoVvxYA1yP3NHt0uqN3wmJEq0Y88g6VhpkZU-I0uFcGPWRP0hUb4SU7NSMoWTYrzibi3rCDQbVaV1IZx1WKAyW5GjDpxPP_XC9COWon7NwHkfX9WoeeKJK1V5Om9coTaEZzq6cmHJVhs64EXsnZdJpcOvvb7WUFO7fcURnIGBdoM_IznU2A9Dkw3m6o4yUgl1I3qpVwbRiatAJabgk4G9xS0ZyfIA_Y-AZLv6-fhuWsn0cTnycMnWA3iOzAicsEaVgAnP5AFFbZUKCHUU5RCU7t0Cg03yxSiGaNKsAS0nGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7113041ff6.mp4?token=ThLg5uz2I8Diyw1bZjEZFgzvKgPW7Z24XTR3skF45PS6X4PSkbRLidpyi7W-bczmq4_YLdbpGmsfZiqQU6TDLSEcDfnW12TZB1OnuR-bbOsl7IdALcfzfR-yGAo_2x9SQOcGJzohTnsEoVsrZTCtOwV3tCXk99C-vPHbMAM6mRefKF5ljk48HDdZ7WpbjaiZdhgl3IaKxK7SsDqHhEDbYVbjJuRZAq3rcwL5fU3uw4py0GOPon8KRlvJ9BDMd0eC2kJ8PdQgviAoeKbS8q4cfTUd9833Yi6cZq6MEhHHieIssm56tCNbOROp96dVjdfWxMflPVXyrkO6XlfRRMNDUSMbMucKLlpT-O2gaDFB8VJGWf8jrGeYIu4juMY1GktFDoVvxYA1yP3NHt0uqN3wmJEq0Y88g6VhpkZU-I0uFcGPWRP0hUb4SU7NSMoWTYrzibi3rCDQbVaV1IZx1WKAyW5GjDpxPP_XC9COWon7NwHkfX9WoeeKJK1V5Om9coTaEZzq6cmHJVhs64EXsnZdJpcOvvb7WUFO7fcURnIGBdoM_IznU2A9Dkw3m6o4yUgl1I3qpVwbRiatAJabgk4G9xS0ZyfIA_Y-AZLv6-fhuWsn0cTnycMnWA3iOzAicsEaVgAnP5AFFbZUKCHUU5RCU7t0Cg03yxSiGaNKsAS0nGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة في هذه اللحظات</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81865" target="_blank">📅 21:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpjKJfgkS7bHqm0wp_-1w_Xc79t967Xnijrd3Plye_qBcQUKTmivE4KYogACNuJ4HtZ5LOd2DS3p5-pr9IXnK9mV2vT2TErKp9KC1i7T-RIuz0PWxpD2TnBf_CXSkWKnu6ZHuQu6K7wMExyZAhBgLZhcbCVws2nyI3BZUjQrQjyPggBZHmlp8ivgB9nfZ_Av3SckoNuTe9I3fw3MyrMLuyXrfhdMU_t-wCcBVSGqoPwIavLCENV0Ff6IPO_Oa147ugkxlQjrI47rgAkZutQ2zigCQUNP3aR398x71gycfB-tknNhg8J_83PrbFYBLMiYMhmQVE9SWXzumYzZBuOUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غلام علي حداد عادل، برفقة معاون وزير الخارجية الإيراني، يتواجدان في الصحن الحسيني الشريف، في انتظار وصول الجثمان الطاهر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81864" target="_blank">📅 21:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deaa646ea.mp4?token=a-m0gQAB6eWDrferO5LEIc9_udkFSiD4vGB777rvoNGVVD5K2gup-KpwgP1aDUR-5o6z_zxRowesZVlS0L3Bg5yefeVF8DMmX41hEype2WnBJ4A-cnO3eVuJoKx9IDZrN7h6bqSS9mFl8qDKHIhAH06RPH1uMwdzcrYO3EsibodUHYlEmXIOZfiUM0uRnDkDHNGTvqGrgyk2NBPvdGQB69EX6z6ATUvffZKN6cfEKq1Otaphgkod_0P9Pa61bkXpQXm6RoTSzf33o8Ur7sZXAWAU9--zjclep6A6Jg4ZTWh2xq6ZxaGYd9Bt40W6zL9m16LwA1xKU5TXZYbWJHh4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deaa646ea.mp4?token=a-m0gQAB6eWDrferO5LEIc9_udkFSiD4vGB777rvoNGVVD5K2gup-KpwgP1aDUR-5o6z_zxRowesZVlS0L3Bg5yefeVF8DMmX41hEype2WnBJ4A-cnO3eVuJoKx9IDZrN7h6bqSS9mFl8qDKHIhAH06RPH1uMwdzcrYO3EsibodUHYlEmXIOZfiUM0uRnDkDHNGTvqGrgyk2NBPvdGQB69EX6z6ATUvffZKN6cfEKq1Otaphgkod_0P9Pa61bkXpQXm6RoTSzf33o8Ur7sZXAWAU9--zjclep6A6Jg4ZTWh2xq6ZxaGYd9Bt40W6zL9m16LwA1xKU5TXZYbWJHh4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة في هذه اللحظات</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81863" target="_blank">📅 21:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a79e53333.mp4?token=sTQWrh5mGVXirQ0KWdeo1NL2sowtWNhWbauoTaIvl-CYlPxmr5VaYaxNzWTKjc1fw2sq2ABcCoVioX9DUTSzHcSg85tEZ-RBdoJDySj50AX355c3mF2E2Szgo5sHrMbxcP_sCzuj3_0FI4a7yTyMbQ4mmjlIWnDWRPG-Dq7y7HnS68KRypfFb_H7ILtkR-q9VPC1RizU12PDqF8ka4GIwuFDhj7gB2U45IbeQ1olI8FKFtevOZ2Mme0W_ShoXmT52mk2g-SJ7-isIUmxkXChl1mlDnXQpKqvMlyGk0Q-Gfh464iAcvdR-qZZlT8zwrboKmHpzP9h9-NGrrHcfTcQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a79e53333.mp4?token=sTQWrh5mGVXirQ0KWdeo1NL2sowtWNhWbauoTaIvl-CYlPxmr5VaYaxNzWTKjc1fw2sq2ABcCoVioX9DUTSzHcSg85tEZ-RBdoJDySj50AX355c3mF2E2Szgo5sHrMbxcP_sCzuj3_0FI4a7yTyMbQ4mmjlIWnDWRPG-Dq7y7HnS68KRypfFb_H7ILtkR-q9VPC1RizU12PDqF8ka4GIwuFDhj7gB2U45IbeQ1olI8FKFtevOZ2Mme0W_ShoXmT52mk2g-SJ7-isIUmxkXChl1mlDnXQpKqvMlyGk0Q-Gfh464iAcvdR-qZZlT8zwrboKmHpzP9h9-NGrrHcfTcQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موكب نقل جثمان الإمام الشهيد وصل إلى
بداية المسار المعلن في كربلاء.
ولا يزال يفصله عن الحرم الشريف ساعات، في ظل هذا الحشد الجماهيري الهائل.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81862" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جموع العراقيين في شارع ابو مهدي قرب مستشفى الكفيل بمحافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81861" target="_blank">📅 20:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded844eec8.mp4?token=l_9fFPspDtyP2rd79KRskgrxF3EpgtoIMOlof0MOk6NUha15_8LnedmLgt5_4ILZybdLCqu-hC02uRJpXp-3PT89BdJdk_qPXDI6Acnx2_wbUpj4uO2my_1wblLj3U2Q1klP83-ny9ALoZO8Yq8YZRNSiuoyJ1MVXFkUvRC9GaNBrF0uGu21b1QeC70vfP-lyiyk1Z7IfCw2Hpgm0EURA0qZOhx9xKAuQbp1D6uDEjHCnt8_reIFiexmEGn_X-o8Cnf6wadknDwBd12J_2Xz1c2r6N6Gn4wMqQ23UsFiE817jQLQUuwHopVn13JfzbsN2cDXkk1_QzqzMXslSlgOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded844eec8.mp4?token=l_9fFPspDtyP2rd79KRskgrxF3EpgtoIMOlof0MOk6NUha15_8LnedmLgt5_4ILZybdLCqu-hC02uRJpXp-3PT89BdJdk_qPXDI6Acnx2_wbUpj4uO2my_1wblLj3U2Q1klP83-ny9ALoZO8Yq8YZRNSiuoyJ1MVXFkUvRC9GaNBrF0uGu21b1QeC70vfP-lyiyk1Z7IfCw2Hpgm0EURA0qZOhx9xKAuQbp1D6uDEjHCnt8_reIFiexmEGn_X-o8Cnf6wadknDwBd12J_2Xz1c2r6N6Gn4wMqQ23UsFiE817jQLQUuwHopVn13JfzbsN2cDXkk1_QzqzMXslSlgOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صلاة قادة المقاومة في العتبة الحسينية المقدسة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81860" target="_blank">📅 20:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محافظ كربلاء المقدسة: تأخر وصول الجثمان كان بسبب استقبال الجماهير والقبائل والعشائر للشهيد على امتداد الطريق بين النجف وكربلاء.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81859" target="_blank">📅 20:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=CCHDvvhnx5rabRv9EqrfB0FViyY3r7ciPxcG81hEnZqkKJYNaTgUg7qSTWFKzO6RIap9xLO1fbn4BCtUwPqaTpIClWCxA8lJp6RLVHsog5JVO0MUHwrNlVikU6X3tMTJx9Mpv6Xc_sXc2nbYAPS-fi_n3QFO6y-uUSbE3fa-Hygq6k_MObBzsReJdGLyFMm0NQaaNkNyNrubrqsnVEMclyejs7UBw4P3M--SA_8UevrAkxdePxdAVsKOGzgIsfd9NVKnJ9hli1MbGkuYO1PrSYiysVBtMBjS_xWD2Cxgxj6TAYuNw2ib6--_vdgI47JR_lJ_y6BiyDmCGOyfYPgLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=CCHDvvhnx5rabRv9EqrfB0FViyY3r7ciPxcG81hEnZqkKJYNaTgUg7qSTWFKzO6RIap9xLO1fbn4BCtUwPqaTpIClWCxA8lJp6RLVHsog5JVO0MUHwrNlVikU6X3tMTJx9Mpv6Xc_sXc2nbYAPS-fi_n3QFO6y-uUSbE3fa-Hygq6k_MObBzsReJdGLyFMm0NQaaNkNyNrubrqsnVEMclyejs7UBw4P3M--SA_8UevrAkxdePxdAVsKOGzgIsfd9NVKnJ9hli1MbGkuYO1PrSYiysVBtMBjS_xWD2Cxgxj6TAYuNw2ib6--_vdgI47JR_lJ_y6BiyDmCGOyfYPgLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صلاة المغرب في منطقة مابين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81858" target="_blank">📅 20:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">من مشاركة هيئة الحشد الشعبي في مراسم تشييع آية الله العظمى السيد الشهيد علي الحسيني الخامنئي (قدس سره) في النجف الأشرف .</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81857" target="_blank">📅 20:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2eaa95f1.mp4?token=puYLDpLn5K8e4n8-ZOZMxATG2kyYPrY3ZUMPg5jMLUH4wvBhQBUTo80CC52bzDqcwhrNk9WdY6XntZ6_FJWEUheU_DDxVO8QWiCJvTtSdGmWQGJWsHwTuqjKbU06vYshj6gwVa_akXjgVLyaRmO2jgEOePd9cLA9nWzTZpA9Whcm_qvOg2n9Hh29fDCbFtv4ldshhAOet-6vwyYCWbWs-ppiCK2VSecxs5SQnZv5R2tBxiecpNQdBechTX7VUq6PenPFci-vQvjJpsKFg2MhqoQo-GOjBVb4dZhlJ1Zm77J07D3t5Nt7mbieQIdYne5zHQzSVbobrcAJodIjuTt3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2eaa95f1.mp4?token=puYLDpLn5K8e4n8-ZOZMxATG2kyYPrY3ZUMPg5jMLUH4wvBhQBUTo80CC52bzDqcwhrNk9WdY6XntZ6_FJWEUheU_DDxVO8QWiCJvTtSdGmWQGJWsHwTuqjKbU06vYshj6gwVa_akXjgVLyaRmO2jgEOePd9cLA9nWzTZpA9Whcm_qvOg2n9Hh29fDCbFtv4ldshhAOet-6vwyYCWbWs-ppiCK2VSecxs5SQnZv5R2tBxiecpNQdBechTX7VUq6PenPFci-vQvjJpsKFg2MhqoQo-GOjBVb4dZhlJ1Zm77J07D3t5Nt7mbieQIdYne5zHQzSVbobrcAJodIjuTt3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أردوغان ليس من أشد المعجبين بـ "بيبي" وإسرائيل. ولكنه لم يشارك في تلك الحرب.  كان بإمكانه المشاركة في تلك الحرب بسهولة، لكنه لم يشارك فيها بناءً على طلبي.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81856" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f210a6bdd1.mp4?token=ELi705cTD_93C6z5SE1n3V8xhv-pioBxBkuJ2UFLLPHGEZgy9nyB5NqsKJ1gcqxPMLR--sN3IADTNEyXE_pgegE_UmghjIEsm-BWrMn2SFLtrLdw_oeKJR2JxXWaoqxxDRVmtmsGL1dMEVohGCd53LZJBpaShnLA-lgrPPKqoyjBycrqoxe9evi3UMBNt2UptnMlvQDn7aE9IKFlKw4k29Ra3Ym2sTL87PhMCUjlx10eMEks4PkLqUKLcJ8lbPyvCeRhrYnqxOvJMG6D5nkeRKdrLkpaM5G__ycMjGumAVknw4NU4PpSbPL1D0MxWHWVHQVOvfoaiRYR0uG_O2QP5TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f210a6bdd1.mp4?token=ELi705cTD_93C6z5SE1n3V8xhv-pioBxBkuJ2UFLLPHGEZgy9nyB5NqsKJ1gcqxPMLR--sN3IADTNEyXE_pgegE_UmghjIEsm-BWrMn2SFLtrLdw_oeKJR2JxXWaoqxxDRVmtmsGL1dMEVohGCd53LZJBpaShnLA-lgrPPKqoyjBycrqoxe9evi3UMBNt2UptnMlvQDn7aE9IKFlKw4k29Ra3Ym2sTL87PhMCUjlx10eMEks4PkLqUKLcJ8lbPyvCeRhrYnqxOvJMG6D5nkeRKdrLkpaM5G__ycMjGumAVknw4NU4PpSbPL1D0MxWHWVHQVOvfoaiRYR0uG_O2QP5TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أنا الرقم واحد في قائمة القتل في إيران.  لا يهمني حقًا، أنا أقوم بعملي.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81855" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/775967f794.mp4?token=JZTM0HFmzIATbrhqqBludofdIt5gsI1TrILPlX_nHOKSeFmFRE4XWzDjHvvYu1_Gu9VxgV4Tjt77OBh8W1dQS44-BofiJcjMBM3Eb3o0DyscyRDFbfoOtogMG3396lHNIukyhs6bGeCo4POY1wr85sY3_DhGN0tsLItIReqYLhHM9nf2Y-YNtpCqo7NHpJqZfzh9OEhwfet2Bf690Iz8DEizo70lxMa6HXu9nPSsxmRiG_iy2fHbGKZMuLT-qFG1uKbVLX_DG3SmLgPkQi4gBRUfkqjvXaWbESQ1T4eLzhiCE_Mmp9n-LIHhxnghi_RhUpBno8KP_PC7rp9nmtpLxRCFpu_c17QZNuoTZHDJD6_BxotY58yLI-pvoWmFAwP9Fe4nmlPKaYL0XpVN0UW7iThsNCBOO8MBzd1fDKVratk26G9_zJ5xD6Ne2I2WSNwSdEjXxSh-rZPwbSqrkSt7O1oZEJh0o3rkMtJ8zF0AOJi1tgqvLOAeevjCfSgk534HwJVyXJb6q2PwFQutCosHCA1dCSBUGHjTx3evtFq5wS0YW0ANd88ezY_NN-IkBA6-lEdgA84kbfKhW0rAnVXmJDHY7N2oDm3SBkcCEffOTe3vTQIxkzZDTNQm11cvNO8I1aRwt-qChpNGvXnV0_p0mZEPCQMaepdNEnxgVwoHPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/775967f794.mp4?token=JZTM0HFmzIATbrhqqBludofdIt5gsI1TrILPlX_nHOKSeFmFRE4XWzDjHvvYu1_Gu9VxgV4Tjt77OBh8W1dQS44-BofiJcjMBM3Eb3o0DyscyRDFbfoOtogMG3396lHNIukyhs6bGeCo4POY1wr85sY3_DhGN0tsLItIReqYLhHM9nf2Y-YNtpCqo7NHpJqZfzh9OEhwfet2Bf690Iz8DEizo70lxMa6HXu9nPSsxmRiG_iy2fHbGKZMuLT-qFG1uKbVLX_DG3SmLgPkQi4gBRUfkqjvXaWbESQ1T4eLzhiCE_Mmp9n-LIHhxnghi_RhUpBno8KP_PC7rp9nmtpLxRCFpu_c17QZNuoTZHDJD6_BxotY58yLI-pvoWmFAwP9Fe4nmlPKaYL0XpVN0UW7iThsNCBOO8MBzd1fDKVratk26G9_zJ5xD6Ne2I2WSNwSdEjXxSh-rZPwbSqrkSt7O1oZEJh0o3rkMtJ8zF0AOJi1tgqvLOAeevjCfSgk534HwJVyXJb6q2PwFQutCosHCA1dCSBUGHjTx3evtFq5wS0YW0ANd88ezY_NN-IkBA6-lEdgA84kbfKhW0rAnVXmJDHY7N2oDm3SBkcCEffOTe3vTQIxkzZDTNQm11cvNO8I1aRwt-qChpNGvXnV0_p0mZEPCQMaepdNEnxgVwoHPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شارع الجمهورية في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81853" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4.5 تضرب الحدود العراقية الإيرانية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81852" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e1ba83b0.mp4?token=EQ2ZNY9Ddwdwpln30sxtmzAm93o7iVclSBU3wDSJvdQuxH0ydeOqkrTWIy4txFZIbsWuXBZ7w6WSKyXLczkEX-5c13zUwiXyXsGYKQ8CXumpqTtpmOLyJIll5OKTl1FiO-r7K-jvHtwzjtYfCTV-YkuCngqAH4l-92GNKePDMOnTiYVd0sYojpF_t2f6Kp5HLtXC9EBgieeROuc6hlefnQWklQhNPfErMXUw7oXQ64Ic_Q8ZmMYEKsLB04Ksvy5TmWn1YkZWVqUFvA1UAKDWPiu0f_U5xeyl2dj7mA11m2uEs6x_N0WSHOJvEpT6FEzn7Y7Ja9GO0-MRtN_FBoWRw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e1ba83b0.mp4?token=EQ2ZNY9Ddwdwpln30sxtmzAm93o7iVclSBU3wDSJvdQuxH0ydeOqkrTWIy4txFZIbsWuXBZ7w6WSKyXLczkEX-5c13zUwiXyXsGYKQ8CXumpqTtpmOLyJIll5OKTl1FiO-r7K-jvHtwzjtYfCTV-YkuCngqAH4l-92GNKePDMOnTiYVd0sYojpF_t2f6Kp5HLtXC9EBgieeROuc6hlefnQWklQhNPfErMXUw7oXQ64Ic_Q8ZmMYEKsLB04Ksvy5TmWn1YkZWVqUFvA1UAKDWPiu0f_U5xeyl2dj7mA11m2uEs6x_N0WSHOJvEpT6FEzn7Y7Ja9GO0-MRtN_FBoWRw4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بشأن إيران: أتعلم ماذا؟ قد أرحل أنا أيضًا.  أنا الهدف الأول لهم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81851" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81850">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab6ed2b31.mp4?token=COV-L9pTuCIuRuZk74S6uewbFegkkV5YkL-Y-6GO14NCFB5HBkcIygZzp9YGLm6ZpZmTNyn_kQE_QghHJinJMrI4XgEcnT8Udi_a2FNsuQd5jFZpGH2MU0wjZ-_IGMGRDloP8u2qjhx9rl-G0a15G-Aobuq-l710OF5K3oafo5vow0jNhACa7NczcxawR4Y99EmYBXo_pwMbczrx013IQw1SyYbSsbteIWCwbh-9NODlkE30zQBVU1KgZb-1kJzSE40EXxm50rpZOaksvsQZCvM7s2hSa2zmrL4plB4vQL4dZyDBCi-0bRjz5vD_BH-4b3aP7TUB4OYtg8VHIO86-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab6ed2b31.mp4?token=COV-L9pTuCIuRuZk74S6uewbFegkkV5YkL-Y-6GO14NCFB5HBkcIygZzp9YGLm6ZpZmTNyn_kQE_QghHJinJMrI4XgEcnT8Udi_a2FNsuQd5jFZpGH2MU0wjZ-_IGMGRDloP8u2qjhx9rl-G0a15G-Aobuq-l710OF5K3oafo5vow0jNhACa7NczcxawR4Y99EmYBXo_pwMbczrx013IQw1SyYbSsbteIWCwbh-9NODlkE30zQBVU1KgZb-1kJzSE40EXxm50rpZOaksvsQZCvM7s2hSa2zmrL4plB4vQL4dZyDBCi-0bRjz5vD_BH-4b3aP7TUB4OYtg8VHIO86-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران استطلاع مجهول في سماء محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81850" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68ac9182.mp4?token=VzeIZaadzy16kzBrR01lCQ0iop3C5gOsb6UujO1iWllmne2b5jW9Fd6y7ZSnBSHv7DMTqaYkKduJLI7VTaq311xyGOiycTH7dw-O9IloZeDnD0-rB0pmXSIJbLO5WNgdtqNGOONR6ZA3lIlrs_TgMG_1XYmbD7JkCRT5kdZr2078hvE0trnK5Zl4aZwpRVM5t9t2NkKIIjGZ0VmG1e_wMAks06v5RxeM1wg_ox__iYvkQePbOuHSZkJ1t_iZuAdADfieL9ze5PN4cwxOJ0zYF-RzWayJIQ4HxSjIjFmSnvYxfkZAOEWlBK0D7lMch69eWFQmQtMW8_V_slXlYFUy5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68ac9182.mp4?token=VzeIZaadzy16kzBrR01lCQ0iop3C5gOsb6UujO1iWllmne2b5jW9Fd6y7ZSnBSHv7DMTqaYkKduJLI7VTaq311xyGOiycTH7dw-O9IloZeDnD0-rB0pmXSIJbLO5WNgdtqNGOONR6ZA3lIlrs_TgMG_1XYmbD7JkCRT5kdZr2078hvE0trnK5Zl4aZwpRVM5t9t2NkKIIjGZ0VmG1e_wMAks06v5RxeM1wg_ox__iYvkQePbOuHSZkJ1t_iZuAdADfieL9ze5PN4cwxOJ0zYF-RzWayJIQ4HxSjIjFmSnvYxfkZAOEWlBK0D7lMch69eWFQmQtMW8_V_slXlYFUy5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للتجمع المليوني في كربلاء المقدسة بانتظار وصول جثمان الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81848" target="_blank">📅 20:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a261d865e4.mp4?token=jufr7ZmiWkKI6HTOEFR09NrY8hdrexvgNuxLty5-x2NWajaDYivelreiuE56fM0clvSRR5sogjq1UE_7EoYfxOQ0-9n3NXVBjK4kEeEUBDocU5mKzERq4Wff4LCx82qOGNh1MPd2_6ZaIckK1xx3gxsKeCjlDGAwUVQJDAX3fh0exgDi6JT4pRf0nCdcLXnfHF7axC9FcjhgNIk5KCbfuQXzCeNCKs9DJzXJk_joF7H5qvNgBELo0uyyiVu1I5u6noGrRka8zhGr7bf369x2SDwJ8dlIma8f0wyhugsOSlNH9Bkp7tfXVoyhSXckojSJz0qOCkQZXufDf1ts7QZhfnKyf4y7dp-MnuKBLtCOXVwCugr436jwPepbQqjYgt_XX6WwBAtSVTOaK3Na_OPuqXp2WjB9zjQyWs-3Ues_sNraQECbf4gyoKXhFYHR4fL6nE42DbLMYRIyNjfcJf4iNyBL0tOUvgV8Yj-C_UM0_eWwp2xtwyMV94k6V67pkAKf2D2onC6ENSbXZAm8pZMj5aeRW8wHoBXIb6Zw5w-0KsySmmbIv2QJzutWtQKNM24Afbaq9P4kDRWcLFZ2iQT2Go-zgX7KHr9zzIs0QQk0b62jw11xFAr4eTqDYIUgwWJ2sysG4zIGpKn95m0bpOyMsYjX6hoaimhznssUfUFHvRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a261d865e4.mp4?token=jufr7ZmiWkKI6HTOEFR09NrY8hdrexvgNuxLty5-x2NWajaDYivelreiuE56fM0clvSRR5sogjq1UE_7EoYfxOQ0-9n3NXVBjK4kEeEUBDocU5mKzERq4Wff4LCx82qOGNh1MPd2_6ZaIckK1xx3gxsKeCjlDGAwUVQJDAX3fh0exgDi6JT4pRf0nCdcLXnfHF7axC9FcjhgNIk5KCbfuQXzCeNCKs9DJzXJk_joF7H5qvNgBELo0uyyiVu1I5u6noGrRka8zhGr7bf369x2SDwJ8dlIma8f0wyhugsOSlNH9Bkp7tfXVoyhSXckojSJz0qOCkQZXufDf1ts7QZhfnKyf4y7dp-MnuKBLtCOXVwCugr436jwPepbQqjYgt_XX6WwBAtSVTOaK3Na_OPuqXp2WjB9zjQyWs-3Ues_sNraQECbf4gyoKXhFYHR4fL6nE42DbLMYRIyNjfcJf4iNyBL0tOUvgV8Yj-C_UM0_eWwp2xtwyMV94k6V67pkAKf2D2onC6ENSbXZAm8pZMj5aeRW8wHoBXIb6Zw5w-0KsySmmbIv2QJzutWtQKNM24Afbaq9P4kDRWcLFZ2iQT2Go-zgX7KHr9zzIs0QQk0b62jw11xFAr4eTqDYIUgwWJ2sysG4zIGpKn95m0bpOyMsYjX6hoaimhznssUfUFHvRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب: الإيرانيون كانوا يريدون صفقة ثم أطلقوا النار على السفن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81847" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترمب: الإيرانيون كانوا يريدون صفقة ثم أطلقوا النار على السفن</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81846" target="_blank">📅 19:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c91d39b.mp4?token=DDA3xn8UNrHNlMa4y7zPNDjlqD38xWUhJUK_xyzpJVfa5qtKLjYeEPXx-N45pM8T3742qeSSHCiK8gEWDO9u9sn-uPx4QvEK_CDE5OLuKg-29m2dt76jYLrKnETuuDdDW2z5MxUT10HmgeEFzlZxgCgaaffkv41SgbJMYLrPMdFvlcDvoVOq8ytCRRlJEUiAuPKZjx4McIY4Zo3XeB00eIiGJE8iED_zmzCvmNcT736Fy8ypAQaNk9nRCmIrbhCnOLP3fHkHsm05ro6DtzjdvTOeakpVYnooMNErzB4er2w6pYToyxqe35rUxQGrGNgd316v8YUn3Q7z9L8fzL_LOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c91d39b.mp4?token=DDA3xn8UNrHNlMa4y7zPNDjlqD38xWUhJUK_xyzpJVfa5qtKLjYeEPXx-N45pM8T3742qeSSHCiK8gEWDO9u9sn-uPx4QvEK_CDE5OLuKg-29m2dt76jYLrKnETuuDdDW2z5MxUT10HmgeEFzlZxgCgaaffkv41SgbJMYLrPMdFvlcDvoVOq8ytCRRlJEUiAuPKZjx4McIY4Zo3XeB00eIiGJE8iED_zmzCvmNcT736Fy8ypAQaNk9nRCmIrbhCnOLP3fHkHsm05ro6DtzjdvTOeakpVYnooMNErzB4er2w6pYToyxqe35rUxQGrGNgd316v8YUn3Q7z9L8fzL_LOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممثل المرجع الأعلى السيد السيستاني الشيخ عبد المهدي الكربلائي حاضراً في كربلاء المقدسة بين المشيعين المنتظرين جثمان السيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81845" target="_blank">📅 19:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtcprfHJV2pDPI7n48KqJ8Hd-YHezpe8bCpZFb-43r67mM-LVQLJUINFG-x2OiM-VIS4NO4wKeLi28Slw3jzXq6lF11dAk7dMbdaz7PPRTXZi7fpCIBJE7_pIw_lnUayggMjwdVkvVrqCjvt2OmVRhR5yAJ4-as0vsMhvrQQZ1cFSzt5hS-Wq4fVzJ1kZUoyznQMrO-SU60PNGZiT8YRmraobsV6gSkBzDjCMfu6iOb5QnWkETXERfAVTDUi-khUmJogAD7807Gyt_qdibOJ1ZvfDZOH8sm90aye7G_Wa7bIOamFCwH6vsyxaDtKsFPXEYuRJO9u1x1uUFhT6tpIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWXdXSRKsZvF3sHzgmBKGcVx2g97ZHokWagdpjzt9Dkvo1Bfm2Ni-1JSnpHpWGExhMcoF2Qrk8EELRuS7rm-xFV10q6-0AqOW0lJwnlZKcV_W6jfAAfNDHOt3Ngl9WKmj-JE6kI6ruxKn0xOsLSZsVwCvJUj0aRlO8DDOeGQVei8eJvDsK5p4HzSdyLYj9BOd___fULY-IR4t7pR_EUQhP9DYn03Pdj-W1U-Uv3MJV-aEvDEk3b7qG8r71_RVHr_-O_cjgfnSOLZlzzrEtKvmV0-b-uDDbgKk86LmIPIYS0J43DCgIrm79ysy2AwxU482oAuus8QdwtnePzfWtueQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من لقاء أبناء المرجع الأعلى في العراق السيد علي السيستاني دام ظله بابن السيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81843" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cd79c3b1.mp4?token=KY8BSsA5U6drkJiPm-Wy58BdUNNCaEZlGmi9kixyCYaVnfQk6uS3VuI-WtDGYptMQzI2E3I5zBGlHa-3gUNQrTxJnRQByhG4tRkNq_datk7dXIElq1tUODdy_r6rYwP1_TWIo8vFBlGgYXyxnNZCLw9DzbzugaaCiPUCwDQRSetIBlaYL1U87_2DcwTPIt56GAmZKD8UUS4aLgfV5orzDd5fkNMKWtEakxiAc58ZK-mvThdwOf7faJeuz3tQ7sCzvXPJLm3v4X9V4XuVAgP7F1vQd8RVFy-XSFAO_GCGrIVgVp5TSdoRLkbbrnSCs_oIBpI_i-9NAtIsUvWGDapS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cd79c3b1.mp4?token=KY8BSsA5U6drkJiPm-Wy58BdUNNCaEZlGmi9kixyCYaVnfQk6uS3VuI-WtDGYptMQzI2E3I5zBGlHa-3gUNQrTxJnRQByhG4tRkNq_datk7dXIElq1tUODdy_r6rYwP1_TWIo8vFBlGgYXyxnNZCLw9DzbzugaaCiPUCwDQRSetIBlaYL1U87_2DcwTPIt56GAmZKD8UUS4aLgfV5orzDd5fkNMKWtEakxiAc58ZK-mvThdwOf7faJeuz3tQ7sCzvXPJLm3v4X9V4XuVAgP7F1vQd8RVFy-XSFAO_GCGrIVgVp5TSdoRLkbbrnSCs_oIBpI_i-9NAtIsUvWGDapS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد مباشرة من صحن الامام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81842" target="_blank">📅 19:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANpATfyADxgAWDxtlaiRYQdnHBI2mu78ZN6cHhjyFp-QAnG14pBtO5eNbr7BiEznKEcD8Q6nKKvEo26IEoXrOWRqniH2nkJ0SPHBMyuanHg1s3xgBX2XFXiYCIyIrpauL03PlmHSY7GJcfT6COB3hmNwG9k4UmfczqXhG5Yd2ak9FgMv5TTHRypCo93GFxbcWSJPG-jeq4o1-adOYw64-4oijp6NXgbwaAEmdLtyiNAbYQMKInjdTWdicFspoMYafpBXhgxEENkNceRjuq_WkU3DDGMIXeg-KXwRMQ-hK4OAjh_X0qDef4ladAtW0Fbxl2iF5Bz97Vg6_nszd6Crew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسل نايا في كربلاء المقدسة: قطع شارع الشيخ عبد الزهرة الكعبي بانتظار وصول السيد الولي وسط انتشار واسع لقوات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81841" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114bd7b9a2.mp4?token=uTPiQMHAzsmYEYACeG7hjZl_Kz8mUGjG-rKJcUYECuxUj2UWSNf-B3XslHXlm9hr1_-3ARs5dwXMEFUJmC6Fdfa9ML9wIq_jE5ZCeSgbigVDXO-3pUjSmNwwxhx8SXpNsWcwwJK5a0Hh6NeQiAMnNk2iNQ6SODtPwgwJ1nbMPSf1s6UHE1erYR8IHccUIoJFvTFB9dIi-eE-Fu0VXdn8HkjYnHPzW4iKLckGRegGTIZjmgPU11J-lkFdxLVHLASz95nHP-DZtulrLDP0s-9bbl1LqBqcnxWyfraaRph6GuhwtYtYgQIVrSQiy9V5OGzkZLh68VZfi78LoDs4D9zcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114bd7b9a2.mp4?token=uTPiQMHAzsmYEYACeG7hjZl_Kz8mUGjG-rKJcUYECuxUj2UWSNf-B3XslHXlm9hr1_-3ARs5dwXMEFUJmC6Fdfa9ML9wIq_jE5ZCeSgbigVDXO-3pUjSmNwwxhx8SXpNsWcwwJK5a0Hh6NeQiAMnNk2iNQ6SODtPwgwJ1nbMPSf1s6UHE1erYR8IHccUIoJFvTFB9dIi-eE-Fu0VXdn8HkjYnHPzW4iKLckGRegGTIZjmgPU11J-lkFdxLVHLASz95nHP-DZtulrLDP0s-9bbl1LqBqcnxWyfraaRph6GuhwtYtYgQIVrSQiy9V5OGzkZLh68VZfi78LoDs4D9zcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامود 1096</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81840" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTKtewQIWM_kuuiPTLElhazicoSpXV2tPq4D7TrlpSYTYWbWZ7-JZyt1i-4ujhkBlx6OmkfYV2KC4dxDLWXYG2_pvcsnYQC2fl12weFx2lpkg9KMU5u2oyk1foxtiVhgs7qJ5Bs-q81u93DY9BtiPRiEEfzaLpAABa9hU0sAmzJ622NRIkGHygeLEntuKsEu3_gUdq5jtrxZ0McpgnbuyPGwhqqS3iIseJp0BCGhSsB0bRU15iRNd2UKMoXaLOrrEgJMwG9dbFELXxPLV8-uQ4lp1OQUzV7jGMzRttjFfRbnCuEPBq6_XQxr87UwwEUdlAD5LbBCE733PaP4quNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابناء المرجع الأعلى في العراق السيد محمد باقر السيستاني والسيد محمد رضا السيستاني حاضرون في كربلاء المقدسة للمشاركة بتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81839" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ca63dcb4.mp4?token=u5L1O0JxylbLcyEezgYJIMpTAbhIkHxdN7eJbx4bjNzZj0J0Ymmnu32C6l-iJxN1If840elXGgaC3P1OBgZ8qoDJVr2th5dM_JJYlwWfLGj6xyHKPLJWsS-dNopH4IPxGVAiSDDWK4XI5rxeFhXFjOvdNfuqRaZWzo92JWVBRJLxyPlR94zvbjDQPXchioqb8w9wlDTAyHrZDb3uOl76wJteLn9X4tSz2pz9at6o313bFbAFIzDHNIj1RrfmRdROzhzspuVisUKk2wSqXgbQ6D7krZob7AMcXMJT0V92goFyjErETIrbf4h3cGGr3NdzXbR7CgRyXrQwfBuFFtn-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ca63dcb4.mp4?token=u5L1O0JxylbLcyEezgYJIMpTAbhIkHxdN7eJbx4bjNzZj0J0Ymmnu32C6l-iJxN1If840elXGgaC3P1OBgZ8qoDJVr2th5dM_JJYlwWfLGj6xyHKPLJWsS-dNopH4IPxGVAiSDDWK4XI5rxeFhXFjOvdNfuqRaZWzo92JWVBRJLxyPlR94zvbjDQPXchioqb8w9wlDTAyHrZDb3uOl76wJteLn9X4tSz2pz9at6o313bFbAFIzDHNIj1RrfmRdROzhzspuVisUKk2wSqXgbQ6D7krZob7AMcXMJT0V92goFyjErETIrbf4h3cGGr3NdzXbR7CgRyXrQwfBuFFtn-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممثل السيد مقتدى الصدر وسط المعزين في كربلاء المقدسة بانتظار وصول جثمان السيد الشهيد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81838" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98467fd50.mp4?token=TzBwuLTVHqyb7F3Kn7GET_GdRW3jkkB1h4Yw_hDkbGAHJcU0BFsqooIVvaPjbrku0lM4GYwb3Ytl9lrLwuKQFtelxth1O7pjT-TioIDJ_7k7FVhWqQKbxnWS5-gUN8TPV5JDh2OmvZxCNvlViU3iVRl-g3FeLbN1ouUmlSelVrAUDOlBEUMfD2oRgAG_DfK72eu9E_68BhUB_hdarxLEMaFeNECfBTReVCPXSMbXhs3UpqT6yoMIQAKHzPUW0751xa0jNRgQdrK38pCiuUVaFYQdbup6XpL2bXnf6VLmGZISYyVQIakOjGYOT-T3lIyiLGxhacjnYzfUlO66i2usDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98467fd50.mp4?token=TzBwuLTVHqyb7F3Kn7GET_GdRW3jkkB1h4Yw_hDkbGAHJcU0BFsqooIVvaPjbrku0lM4GYwb3Ytl9lrLwuKQFtelxth1O7pjT-TioIDJ_7k7FVhWqQKbxnWS5-gUN8TPV5JDh2OmvZxCNvlViU3iVRl-g3FeLbN1ouUmlSelVrAUDOlBEUMfD2oRgAG_DfK72eu9E_68BhUB_hdarxLEMaFeNECfBTReVCPXSMbXhs3UpqT6yoMIQAKHzPUW0751xa0jNRgQdrK38pCiuUVaFYQdbup6XpL2bXnf6VLmGZISYyVQIakOjGYOT-T3lIyiLGxhacjnYzfUlO66i2usDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المكان المخصص لوضع النعش الطاهر في مرقد الامام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81837" target="_blank">📅 19:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3622436047.mp4?token=BoeiVxxXXELyiW3MjZFgHAWtX6oLVP6pVIU_qcavs7Is6rHMysBBHEXByo4nTbElr_-RJN2us1MONUVu3QDbW0Od4QWHB_CMx5iY7RM_iGkma-kOolTlem8zkwBWrF_N5WydJLngLw-xrG1xE2k_uZFfhJ3ZbSYhrRu0_ytPFAHA6eaRvzL6d9buH74QV-JFLwlD75UH9SmCnJ9Jg8LuK3FdoYyF1Shr-uBZmpMQ1Oai4itlOEZpcY1xZMIq3AsaATqqCyMUPcd14espxZggomEtUuSxoGb1nVWwerAzckxjJpbNhOP6r79_dOqTKbGlW-sps2Y2N1EPQU-GOPNm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3622436047.mp4?token=BoeiVxxXXELyiW3MjZFgHAWtX6oLVP6pVIU_qcavs7Is6rHMysBBHEXByo4nTbElr_-RJN2us1MONUVu3QDbW0Od4QWHB_CMx5iY7RM_iGkma-kOolTlem8zkwBWrF_N5WydJLngLw-xrG1xE2k_uZFfhJ3ZbSYhrRu0_ytPFAHA6eaRvzL6d9buH74QV-JFLwlD75UH9SmCnJ9Jg8LuK3FdoYyF1Shr-uBZmpMQ1Oai4itlOEZpcY1xZMIq3AsaATqqCyMUPcd14espxZggomEtUuSxoGb1nVWwerAzckxjJpbNhOP6r79_dOqTKbGlW-sps2Y2N1EPQU-GOPNm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد الشهيد يصل إلى عامود 1096</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81836" target="_blank">📅 19:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b49bf1997.mp4?token=YsU-xZHpivc3HeG2Q1rSAAfk_r5xkCI7C61x9OLLX0I6GOc9kS-E8LKSvBaAeACdh_ymh0Roc-QJ8TtEqhZafKUfYgHjt_Scax-bHHDW7aEYuVclWdLiO7yrVbfJ_l_jF_UMKIzXsgyemFrFghLqy1dC9i4GDCT1bH4wHNH8R14vZcAw_8jYluYaO059MY0VLEuorLCkbQlHc0v-RRjrqvW6yplJAze1CVlcNe5YuN26YIu6_tAP2k1a1U8CHdfU-9ZWAuRrHPqj6mmEMG1oZWqt4AUROLGFM_-C1XgsvRaexWMmN0PF3ARTAZaEBT-cUUhQFFAYfLysKR3v7Bq6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b49bf1997.mp4?token=YsU-xZHpivc3HeG2Q1rSAAfk_r5xkCI7C61x9OLLX0I6GOc9kS-E8LKSvBaAeACdh_ymh0Roc-QJ8TtEqhZafKUfYgHjt_Scax-bHHDW7aEYuVclWdLiO7yrVbfJ_l_jF_UMKIzXsgyemFrFghLqy1dC9i4GDCT1bH4wHNH8R14vZcAw_8jYluYaO059MY0VLEuorLCkbQlHc0v-RRjrqvW6yplJAze1CVlcNe5YuN26YIu6_tAP2k1a1U8CHdfU-9ZWAuRrHPqj6mmEMG1oZWqt4AUROLGFM_-C1XgsvRaexWMmN0PF3ARTAZaEBT-cUUhQFFAYfLysKR3v7Bq6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات هائلة من امام مرقد الامام العباس عليه السلام</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81835" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81832">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b41d2542f.mp4?token=tiQ5PFgdNVs7u9F4z0UkaDawN4qI0TC0psfFF-E_jv3Cj6I-NdHtRpxXnx4NX-C6lT9wmtjoMvTNwT1qgrY8QNG_-n0UT_A4rDbZqgYeKq8jpDVHI0dm2sbQ85VP6m7oBIrZ_2FzHaDtiKido9_cODTm8roEeQKcrIfRLGbbG4yRlWdgpQ7L109UijCoireJDgbLl36sQnegAa5Bugd1z6vxvM0kCIoStCDlqAt2bLd387BbRzT2lNfV82zmG15YrmIP_JD26KRUieucy-t6eJbe7KEZzqtYPSJK0UcP89VJjivspiVL9h-aGzMN9DT0JmrzodCOKJERTAbvD5_QJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b41d2542f.mp4?token=tiQ5PFgdNVs7u9F4z0UkaDawN4qI0TC0psfFF-E_jv3Cj6I-NdHtRpxXnx4NX-C6lT9wmtjoMvTNwT1qgrY8QNG_-n0UT_A4rDbZqgYeKq8jpDVHI0dm2sbQ85VP6m7oBIrZ_2FzHaDtiKido9_cODTm8roEeQKcrIfRLGbbG4yRlWdgpQ7L109UijCoireJDgbLl36sQnegAa5Bugd1z6vxvM0kCIoStCDlqAt2bLd387BbRzT2lNfV82zmG15YrmIP_JD26KRUieucy-t6eJbe7KEZzqtYPSJK0UcP89VJjivspiVL9h-aGzMN9DT0JmrzodCOKJERTAbvD5_QJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطقة مابين الحرمين الشريفين تشهد تجمعات هائلة لتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81832" target="_blank">📅 19:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جثمان السيد الشهيد يصل إلى عامود 1096</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81831" target="_blank">📅 19:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منطقة مابين الحرمين الشريفين تشهد تجمعات هائلة لتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81830" target="_blank">📅 19:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235484d88c.mp4?token=M_5gLCm7Z5bGJpBfC4sykxwrEAyfGM-pztpqlwJYqXK8hZXlmspETkNV2jqOew8ur6Xx2Zdl4PqxsBmomYh9yu2sSQj5r8b93dcoxdZieaPNyQ15akiXFGJpTfvCphA_8JaFZhoXACYVyF8ohK6jz5ucZc1j9PqIywjkfUngXL_SPffykyQkosDoBr8cE25lAQ_bEQSjzBCqhXGg8k19RbVh3l2QsPBNDIBRTq1azMLaZk_0YnV2cGPP6C7MkqeN3rH2eU8gJG8Tb7ms7b2kkPTpSEpUEfsLIIsGmPlVnxTqMtTkNI1Af7qsIfi5B3s0cZ-O7y8N3gkgqyR5A2aAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235484d88c.mp4?token=M_5gLCm7Z5bGJpBfC4sykxwrEAyfGM-pztpqlwJYqXK8hZXlmspETkNV2jqOew8ur6Xx2Zdl4PqxsBmomYh9yu2sSQj5r8b93dcoxdZieaPNyQ15akiXFGJpTfvCphA_8JaFZhoXACYVyF8ohK6jz5ucZc1j9PqIywjkfUngXL_SPffykyQkosDoBr8cE25lAQ_bEQSjzBCqhXGg8k19RbVh3l2QsPBNDIBRTq1azMLaZk_0YnV2cGPP6C7MkqeN3rH2eU8gJG8Tb7ms7b2kkPTpSEpUEfsLIIsGmPlVnxTqMtTkNI1Af7qsIfi5B3s0cZ-O7y8N3gkgqyR5A2aAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش السيد الولي يصل قرب تقاطع الدرة</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81829" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc00f4ecfd.mp4?token=an-ILfKsYnljGLzFhxdIPl4Wa_VDe4XBWP8HtLkOmDppdsHHYTy6GHVLMb-fkIDQ_8wda3oRnvurf-OxYJ07owXjmMmFrpMLDpg22cMEUwguDtUL9oPUAb35qzYjd3XraQRtAVMIX4WW6Q0PfhqMO_sumO8SgW4FtkwolHVEddmsHlXy03jflyfc6xqVnupG1373MGHT1rXfs0r-9dvwKmN_bjrfkpaZGEkkGFrE830EBPB09K33rN14_cz9FybIP3zG9it4-DGBaWL6fvqcV2O10rr2JqHBiMH8242eThJvXF68DlnwnMzYjTdzoOuDw-dcsirJPTC1kHHGixPW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc00f4ecfd.mp4?token=an-ILfKsYnljGLzFhxdIPl4Wa_VDe4XBWP8HtLkOmDppdsHHYTy6GHVLMb-fkIDQ_8wda3oRnvurf-OxYJ07owXjmMmFrpMLDpg22cMEUwguDtUL9oPUAb35qzYjd3XraQRtAVMIX4WW6Q0PfhqMO_sumO8SgW4FtkwolHVEddmsHlXy03jflyfc6xqVnupG1373MGHT1rXfs0r-9dvwKmN_bjrfkpaZGEkkGFrE830EBPB09K33rN14_cz9FybIP3zG9it4-DGBaWL6fvqcV2O10rr2JqHBiMH8242eThJvXF68DlnwnMzYjTdzoOuDw-dcsirJPTC1kHHGixPW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد القائد يصل إلى محافظة كربلاء</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81828" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1a1de273.mp4?token=lqEcwlP8SxcElBbmCmT-0jjELOGy91-JVRUP3xf5pGfjWvvEiQQocFGKq26q1FetomVMjbfKz0k2gQM1vrSS1mUlhNShRrvDyP43I06qTWQ6A6maQBHHGEQCB26CP9YN9hWeCZLzJW-0J3vUmSV3rMh1KXMd-mw-toYojkB-ddjFYEgGivaRK5OrTkejf8nk9lMSBHbuZ0vS8Oy5Mieptir11FQdJKC5BFZ2rX3AQJfiyUwRFKPELqIp-xd6YlbHKe7UJ6DrO1uj6yKQ8WI7daADok6ocbFUGoa2ILHsZS2IF2xanZqWkCGB23ro2PxYFJ8LMeqRcTpv4v9-xoW45AiB7_KARYBDGaWfJ03y1M2rlTAer2lcSBc7ytiA_qnunYFSD5JTesAgELzS3hDq9uc6vbT9phTN8H9Zk0WOczrbaq1ljnvm3cva8MIL8ffoSE0m1vi6_yPx55nUswL2RDjgjO91IoeBjj2mCH-M9Y_vQs7L_7Wgia3qHtXhQbfeflatL0gqfX19JLC52xRzitZGGNUEa00z3Ntp8q8xrapHzFKp0UAGkhgd5N2Qi8jz5gLSS2C2SPEIQjlIO7PLRYMY0NqpKPX1UHfMHmSqrxbZlrvxsscrUiaff9MNLnjK9rBkxRy5Q_FT2hr3Mqh00EtziBg6oA3kAQVgLpSSjCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1a1de273.mp4?token=lqEcwlP8SxcElBbmCmT-0jjELOGy91-JVRUP3xf5pGfjWvvEiQQocFGKq26q1FetomVMjbfKz0k2gQM1vrSS1mUlhNShRrvDyP43I06qTWQ6A6maQBHHGEQCB26CP9YN9hWeCZLzJW-0J3vUmSV3rMh1KXMd-mw-toYojkB-ddjFYEgGivaRK5OrTkejf8nk9lMSBHbuZ0vS8Oy5Mieptir11FQdJKC5BFZ2rX3AQJfiyUwRFKPELqIp-xd6YlbHKe7UJ6DrO1uj6yKQ8WI7daADok6ocbFUGoa2ILHsZS2IF2xanZqWkCGB23ro2PxYFJ8LMeqRcTpv4v9-xoW45AiB7_KARYBDGaWfJ03y1M2rlTAer2lcSBc7ytiA_qnunYFSD5JTesAgELzS3hDq9uc6vbT9phTN8H9Zk0WOczrbaq1ljnvm3cva8MIL8ffoSE0m1vi6_yPx55nUswL2RDjgjO91IoeBjj2mCH-M9Y_vQs7L_7Wgia3qHtXhQbfeflatL0gqfX19JLC52xRzitZGGNUEa00z3Ntp8q8xrapHzFKp0UAGkhgd5N2Qi8jz5gLSS2C2SPEIQjlIO7PLRYMY0NqpKPX1UHfMHmSqrxbZlrvxsscrUiaff9MNLnjK9rBkxRy5Q_FT2hr3Mqh00EtziBg6oA3kAQVgLpSSjCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عدسة نايا ترصد التجمع الهائل للمعزين بالسيد الولي داخل حرم الامام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81825" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec731f577.mp4?token=uuV78cvv9DEJzjI5YoMxqHHl--Mm_OLvsUceC04EKY6v9rzVduhWCBKTK-Uho2n1IBjibzLgifErO1djv8Eg8fi0dZmho3xpGf7R_X_A-dJTMY14hmf-BIvOJ3jeSdiY6dXdSjXWRqc-5HcL60dQ0wjpGiXBMUGChPRc2BdrRIbpqhGbKWxzhupsLzJ03jFsCvkwQhlwrr5Y4vuVvXCwgIfMZI-wevAQ2YO0dmoMJjpqhLuSNGr-lMGGjuuC0iXmmNzhR8-W7qPo1iehVnNobq147F65VuRFtS7GsCtx_7-815y3po-F5CaRp6X0vOFTsenVuewOBwyOmjsVprp-1C9WKCJZ9LheSrEsTBkGqKYux4X7Iagd-8ciD-Vr5Xd3cUwA_9KHuFMB1A0cgQgSR6Z11K3ZjCYQJfiUtED7vhp7IKkhqHFh8xG90bNkoqksT6RHAabKkLa-G5F8j9Gyf8XYcvVChayaxwhIGrtweYzzwHDCKXgU4QwW6fQUQ5ETgBmkayjhWTbx1ZRQDJhXIoJdDMS1FgvvC9qbpP-V948Y7LnBE_syJwadWTIXI0kDJ4ontnQDyQUzdxr1tDO9smaf9Yn8z05OpfB9geK3hmjb1KvI-L9_3vc_OYLtr9pifit8fSyzOTXxTpZ_i1G8AM-hmd_ko0ha6Xz0UoS8QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec731f577.mp4?token=uuV78cvv9DEJzjI5YoMxqHHl--Mm_OLvsUceC04EKY6v9rzVduhWCBKTK-Uho2n1IBjibzLgifErO1djv8Eg8fi0dZmho3xpGf7R_X_A-dJTMY14hmf-BIvOJ3jeSdiY6dXdSjXWRqc-5HcL60dQ0wjpGiXBMUGChPRc2BdrRIbpqhGbKWxzhupsLzJ03jFsCvkwQhlwrr5Y4vuVvXCwgIfMZI-wevAQ2YO0dmoMJjpqhLuSNGr-lMGGjuuC0iXmmNzhR8-W7qPo1iehVnNobq147F65VuRFtS7GsCtx_7-815y3po-F5CaRp6X0vOFTsenVuewOBwyOmjsVprp-1C9WKCJZ9LheSrEsTBkGqKYux4X7Iagd-8ciD-Vr5Xd3cUwA_9KHuFMB1A0cgQgSR6Z11K3ZjCYQJfiUtED7vhp7IKkhqHFh8xG90bNkoqksT6RHAabKkLa-G5F8j9Gyf8XYcvVChayaxwhIGrtweYzzwHDCKXgU4QwW6fQUQ5ETgBmkayjhWTbx1ZRQDJhXIoJdDMS1FgvvC9qbpP-V948Y7LnBE_syJwadWTIXI0kDJ4ontnQDyQUzdxr1tDO9smaf9Yn8z05OpfB9geK3hmjb1KvI-L9_3vc_OYLtr9pifit8fSyzOTXxTpZ_i1G8AM-hmd_ko0ha6Xz0UoS8QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة تكتظ بالملايين المشيعين لجثمان السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81824" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جثمان السيد القائد يصل إلى محافظة كربلاء</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81823" target="_blank">📅 18:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e4f47a54.mp4?token=MIG4qmWFAt7qhloYxJjF8vpZZ_LKob5BueGVV8p4ar-SPt32YJAeQf6YZd3hDEb46jaN4f8zHxfY5aoB1Rov9xzeLm9GOI3ZWTsJqNHoMO-MzCdn2CydD-JGiAWHzrG3dzm4cpbzP6N1EsFtwXGWXD1XaNJclL1Tfjw7WJWwqFNFd9XKLV3WE4YPfIPhbAMzNo5tDmfxIDw3PHvjCLPXAH34Y1WuxWGicYgt2cCMknChExYsfn4ZYzlQnrgRr60U8U9TliSujp62sz6V3WJnjmoouj7OvmijFkugGLpHrLWafxpZJHBFf_gCRLU5H1PSTsEXxJhkzPXBAkjJ2GN4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e4f47a54.mp4?token=MIG4qmWFAt7qhloYxJjF8vpZZ_LKob5BueGVV8p4ar-SPt32YJAeQf6YZd3hDEb46jaN4f8zHxfY5aoB1Rov9xzeLm9GOI3ZWTsJqNHoMO-MzCdn2CydD-JGiAWHzrG3dzm4cpbzP6N1EsFtwXGWXD1XaNJclL1Tfjw7WJWwqFNFd9XKLV3WE4YPfIPhbAMzNo5tDmfxIDw3PHvjCLPXAH34Y1WuxWGicYgt2cCMknChExYsfn4ZYzlQnrgRr60U8U9TliSujp62sz6V3WJnjmoouj7OvmijFkugGLpHrLWafxpZJHBFf_gCRLU5H1PSTsEXxJhkzPXBAkjJ2GN4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المعزين في فلكة جودة بانتظار تشييع جثمان السيد الشهيد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81822" target="_blank">📅 18:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بعد حوادث انفجار صهاريج النفط العراقية على الأراضي السورية.. حادث جديد يطال 3 شاحنات عراقية مما أدى إلى احتراقهن في منفذ اليعربية الحدودي بين العراق وسوريا.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81821" target="_blank">📅 18:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57c3e2f71.mp4?token=XqM1vgfgoTVz8H5YbEP5Y7yFudUjB6eMBezQ7MaiFE7sRui-rSaCDp4Y3em_PMz7jlRwkKDp6ETCMFzPtJcdT422QdAtZmdtbJifJww0a1OIlWz8bIcLC3IccrSeBFn_-aKhU3ECcZHX5Fh7muMrPchwyY7knut54Li-xFeRo2X1A6oDoSf5FAWNSCupxY7H746FZh7DHi-gHaB8aLYV1ziukvCVfk3hbtF2r1rxQCGBfya7fo35a7zQS9all4zrf7jsH4NsDFSi52TQDyd7wj_TwFQXkuWloJ4AU-44rNTCeAySzjxrABthPLjygRaCGMvFX8Tbv02Gef-2FURWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57c3e2f71.mp4?token=XqM1vgfgoTVz8H5YbEP5Y7yFudUjB6eMBezQ7MaiFE7sRui-rSaCDp4Y3em_PMz7jlRwkKDp6ETCMFzPtJcdT422QdAtZmdtbJifJww0a1OIlWz8bIcLC3IccrSeBFn_-aKhU3ECcZHX5Fh7muMrPchwyY7knut54Li-xFeRo2X1A6oDoSf5FAWNSCupxY7H746FZh7DHi-gHaB8aLYV1ziukvCVfk3hbtF2r1rxQCGBfya7fo35a7zQS9all4zrf7jsH4NsDFSi52TQDyd7wj_TwFQXkuWloJ4AU-44rNTCeAySzjxrABthPLjygRaCGMvFX8Tbv02Gef-2FURWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراقيين يفترشون الأرض في منطقة مابين الحرمين الشريفين بانتظار وصول السيد القائد لتشييعه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81820" target="_blank">📅 18:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f76af383.mp4?token=CvNJXnbKgIBt9A8hQvwMdv7hmwUG7uIkmjjwh8f84OTTq9wHFl649Ibx7xvrXhbWq8aqU3eF0wG4lSRJn4gzBtuQDjmj07-tTU_NoCSFhJnffXjlQIM7Sw65LiVZHBMRkCU00dNTgyK7jUfwO-A-uTH1ee_QP03L8ZjL96TtEhUI6NCktGReSWyWvhseUTi0ahJWbIIB0Mb8zMGLWoL3F_ymJbS4XC28qIsPTAl7CFh3zN0iNXf78PBM5o6dm2qlkJ3trNP7_XbNBPRF1j9cNbfiImrTrk20uco2YP8SGZnWEvIN27bQjfCgva-HoUlh9MoLLLGas6O6OJCOAMaTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f76af383.mp4?token=CvNJXnbKgIBt9A8hQvwMdv7hmwUG7uIkmjjwh8f84OTTq9wHFl649Ibx7xvrXhbWq8aqU3eF0wG4lSRJn4gzBtuQDjmj07-tTU_NoCSFhJnffXjlQIM7Sw65LiVZHBMRkCU00dNTgyK7jUfwO-A-uTH1ee_QP03L8ZjL96TtEhUI6NCktGReSWyWvhseUTi0ahJWbIIB0Mb8zMGLWoL3F_ymJbS4XC28qIsPTAl7CFh3zN0iNXf78PBM5o6dm2qlkJ3trNP7_XbNBPRF1j9cNbfiImrTrk20uco2YP8SGZnWEvIN27bQjfCgva-HoUlh9MoLLLGas6O6OJCOAMaTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مراسل نايا: ازدحام شديد وتوافد مليوني مستمر منذ الرابعة عصراً في شارع العباس (قطع المحكمة) بكربلاء، للمشاركة في تشييع جثمان السيد علي الخامنئي، وسط بدء المشيعين بافتراش الأرض انتظاراً لوصول النعش المطهر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81819" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">يأتوك رجالا وعلى كل ضامر يأتين من كل فج عميق
الحيد في الميدان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81818" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الحشد الشعبي: تشير التقديرات الأولية حتى الآن إلى أن عدد المشاركين في مراسم التشييع تجاوز أربعة ملايين مشيّع، فيما لم يدخل النعش المقدس بعد إلى الشارع المخصص لإقامة مراسم التشييع .</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81817" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الحشود العشائرية الهائلة تنتظر وصول الجثامين في سيطرة مدخل كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81816" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وصول النعش إلى عامود 888 في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81815" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fb0cff28.mp4?token=KEdkam7Wuj6LAk2jWID_hshtR191PDczYHP9ekyB1c1CTrqcbsaxJUGRtOOHPqwH2t9WEwQGD0Ylk1aRb4os_xNNQCHtAyI3wLjX8sos6eRLE_gFfzQOWWifAlROLyGqwciBISTETGrku-_5KJETV3pk5Kngwwtzqs33il2CbvcT52i3vCzuQsPnEQqi6UC3EONlv1dMJVW1-ytzo_tLpcwccL9B53FbYLvhKEI9d9CkXpdncF8djzXPtJAEKoZzA4A_NS1ukvjehZZfVt1TGm_JcZqYkPGM0RedHO0tO4wgTq9b5UQf554DRw8OFrNfCIRiR-uS0GJ1XmttW9qwgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fb0cff28.mp4?token=KEdkam7Wuj6LAk2jWID_hshtR191PDczYHP9ekyB1c1CTrqcbsaxJUGRtOOHPqwH2t9WEwQGD0Ylk1aRb4os_xNNQCHtAyI3wLjX8sos6eRLE_gFfzQOWWifAlROLyGqwciBISTETGrku-_5KJETV3pk5Kngwwtzqs33il2CbvcT52i3vCzuQsPnEQqi6UC3EONlv1dMJVW1-ytzo_tLpcwccL9B53FbYLvhKEI9d9CkXpdncF8djzXPtJAEKoZzA4A_NS1ukvjehZZfVt1TGm_JcZqYkPGM0RedHO0tO4wgTq9b5UQf554DRw8OFrNfCIRiR-uS0GJ1XmttW9qwgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شارع ابو مهدي المهندس</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81814" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4c42142.mp4?token=NbA-K_i6ZcNy1M70ElSbmGAj2DXO4bgCI2ZbNKI9btXQ46cyZqPzXCQYJCWW106Zd93L1yTEC0kn1C-qrFOuiYsqOtbMmXSOmBBzktq7pQRN32J2GTUtKxLlukoY8NB3tlaL0Kd8uy12DHwBHkYKe2k7ttwSANbhW1yeJ3WCGKhnRSbJGQk_bQu6JzT-SIHagMVUjhnEdLjjw44-4FSCWISG8H6nlVQs5mfRgGXckhv96jUFiZ5_IL9o79hN2uGn0n1Q_NrGdahtGIs3Bv7vqsrZAoGy1AKdzZtTOFr8OnIwlOujeFkeyLbIOFvDpgEurlhBm1UZkiLvRDLm7OQs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4c42142.mp4?token=NbA-K_i6ZcNy1M70ElSbmGAj2DXO4bgCI2ZbNKI9btXQ46cyZqPzXCQYJCWW106Zd93L1yTEC0kn1C-qrFOuiYsqOtbMmXSOmBBzktq7pQRN32J2GTUtKxLlukoY8NB3tlaL0Kd8uy12DHwBHkYKe2k7ttwSANbhW1yeJ3WCGKhnRSbJGQk_bQu6JzT-SIHagMVUjhnEdLjjw44-4FSCWISG8H6nlVQs5mfRgGXckhv96jUFiZ5_IL9o79hN2uGn0n1Q_NrGdahtGIs3Bv7vqsrZAoGy1AKdzZtTOFr8OnIwlOujeFkeyLbIOFvDpgEurlhBm1UZkiLvRDLm7OQs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باب القبله للإمام الحسين عليه السلام بانتظار الإمام القائد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81813" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdffb3ca0f.mp4?token=sWt0M3RTe-LXG1AXWm6NOIRJtqe4d0D2B2_KafhvxtMVpE5859KWYz5xpj7tvALPAAbBhJZoxbLMJcrXkxUCgCx7nO643OwmrNc7RcVcsQ8mD1Dv3unH61C5NlkWOcNSRES40OwcjSUCjNNVnnQ2KbB-ZO9UGckqFX2DI2-n_ssxRDcZwqMZ9kCLqlPgK2NLHVYehuOnlx8FKIyrs8_1E_1vCVYg_RVa8uXZsvlRZnYDCyB_UDjmCrWAlP5FjqEDmrX3b0Ps8FTvA9w6bJQ0qouAIMgpvVrZzraaij6FF2nzfa8X8d6u9XkCPZUu4S45p6u-KS_cFdueGQ5m2gfKIq1NYavSQZ8xC5GXpjptbWHOqiKUgjDB2hXcj_nd64bLHd7gVfUCthjYmxxaKLA6j_eY2GP7snvmZ9SlCWxQ6dk41aCrN8NGdNrgHhuNoC9Jqyhjy9cQ7CMttzdhYd8jNLJDQMDjueIuOeG2fkzPBBeSX6xKPtXXfiOHRVhKyVIMZb20CzM7KSO9U5xPdtwp9tkmW4f0IMR0h8GfMbz57Zvgqhgpc2JXALQNGkBZDYLwhYQl4yiutbgPODNvh6GT_WXQ5aE05is0L3wtLuBB2kSZSE83_BzfsAlewqaRmjyDb9Z4ztCLd4zrdvk56oQmvqFMTB3tGM8Xx7Z_Y5AgxnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdffb3ca0f.mp4?token=sWt0M3RTe-LXG1AXWm6NOIRJtqe4d0D2B2_KafhvxtMVpE5859KWYz5xpj7tvALPAAbBhJZoxbLMJcrXkxUCgCx7nO643OwmrNc7RcVcsQ8mD1Dv3unH61C5NlkWOcNSRES40OwcjSUCjNNVnnQ2KbB-ZO9UGckqFX2DI2-n_ssxRDcZwqMZ9kCLqlPgK2NLHVYehuOnlx8FKIyrs8_1E_1vCVYg_RVa8uXZsvlRZnYDCyB_UDjmCrWAlP5FjqEDmrX3b0Ps8FTvA9w6bJQ0qouAIMgpvVrZzraaij6FF2nzfa8X8d6u9XkCPZUu4S45p6u-KS_cFdueGQ5m2gfKIq1NYavSQZ8xC5GXpjptbWHOqiKUgjDB2hXcj_nd64bLHd7gVfUCthjYmxxaKLA6j_eY2GP7snvmZ9SlCWxQ6dk41aCrN8NGdNrgHhuNoC9Jqyhjy9cQ7CMttzdhYd8jNLJDQMDjueIuOeG2fkzPBBeSX6xKPtXXfiOHRVhKyVIMZb20CzM7KSO9U5xPdtwp9tkmW4f0IMR0h8GfMbz57Zvgqhgpc2JXALQNGkBZDYLwhYQl4yiutbgPODNvh6GT_WXQ5aE05is0L3wtLuBB2kSZSE83_BzfsAlewqaRmjyDb9Z4ztCLd4zrdvk56oQmvqFMTB3tGM8Xx7Z_Y5AgxnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ربما سنفعل بعض الأشياء التي سترفع أسعار النفط. عندما نهاجم إيران، يرتفع سعر النفط. لا بأس بذلك.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81812" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب: أعتقد أن إسرائيل ستنسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81811" target="_blank">📅 18:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b458bf5b.mp4?token=H871PzjGPwGU0nuzvRkBlHls11seqUGQ2jeoPvX66PyAWgltUqUrv_cqVDhGvuiwrMt5u2WyOtmLyLjY31s2IPs9VSLuc8uyOtewZirDDPW8q3IauKD8DK8XFG69xvAvm3ovxbS6TAM9fOH-P1xlFr4tf8gIvKo2JruFXWR5ElG1NrDFQVy6RkR9cs-Vz6j8pC-YWwAJKN7I08ycUp_OTxtv16uyvVEWCNJN1mHR5JoaTDXF9GLSO-Fv3DGMI3--n_dlmpoxRbmB8v7MoLKZ2ogE4PwA56nrcFGvVFumKjB9gZ8axUb0OJ9NUdM3TVpyGcmrRx19JiCswKpl9Btpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b458bf5b.mp4?token=H871PzjGPwGU0nuzvRkBlHls11seqUGQ2jeoPvX66PyAWgltUqUrv_cqVDhGvuiwrMt5u2WyOtmLyLjY31s2IPs9VSLuc8uyOtewZirDDPW8q3IauKD8DK8XFG69xvAvm3ovxbS6TAM9fOH-P1xlFr4tf8gIvKo2JruFXWR5ElG1NrDFQVy6RkR9cs-Vz6j8pC-YWwAJKN7I08ycUp_OTxtv16uyvVEWCNJN1mHR5JoaTDXF9GLSO-Fv3DGMI3--n_dlmpoxRbmB8v7MoLKZ2ogE4PwA56nrcFGvVFumKjB9gZ8axUb0OJ9NUdM3TVpyGcmrRx19JiCswKpl9Btpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أعتقد أن إسرائيل ستنسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81810" target="_blank">📅 18:05 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
