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
<img src="https://cdn4.telesco.pe/file/PMYKx_PMRVBJ85fo9my9YT1Ak0wRDTGbr5C3lvsK8B4j1bJyHBBl1xosYM6RCVRim5FFWgenk8cRAiOS8lxGkG13c-Ry6bS6ByAO95Zu5kcsIaVxNzgGYG9v0JI9VRYwrfXhehPqcdLtwiqkll1_yjGdIJRMeILrn5lZ9PY3GBQjKWNFNLGb71xZojwpfFVz1mllhgeyH9nEbwiXaPhjUCtDenh_pFUfjAwAgHyT7uViIkVVCloqUPOx3n5emPwzejo_zXx_nkpIVTEtWr5SK0Uw2iLnlo4NnlMM4i0hVGnid9qOVqKzESs6RQyTvyYqqSstlZdWId7RTcYt3hq_4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
<hr>

<div class="tg-post" id="msg-90941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
الدب الروسي يداعب اوروبا
أوقفت مطار لوكسمبورغ الرحلات الجوية في وقت متأخر من يوم الجمعة بعد ورود تقارير عن نشاط طائرات بدون طيار غير معروفة بالقرب من المطار، مما اضطر الطائرات القادمة إلى التوقف أو تغيير مسارها.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90941" target="_blank">📅 01:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0kAfYB4DLIF1avv0NqXy_svRATkMRm9t_a2y_KZiC3_E8sU9-RERpFSRlzxUe2_u9R2rlux--kU1Bf2vzIweUwGmDvmKsdrVWmUrEyNOT_jOM25FibZfhJVg2JrK0ncumwWozGGY7s48cCFwxXSS8-KT5KXBONriuMQ7emKg9G4v0mWeGL1RKaPudsTRdhBEe5v8bxoTdMBFSLDNLCdMVZV5Wqpe35wwnBTyZU0HXYOOXoQcoFZheft52_TJM5reI0xrCilISHFs8GnHLz_2iINBrJnS-bjW4tlnd0vWU9TwKmvHkbCywokY1URhFoQmDgMy1ZUxlQbmbQNWjrvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محافظة فرسان تحت القصف</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90940" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90939" target="_blank">📅 01:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90938" target="_blank">📅 01:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب يوقع قانون العقوبات على روسيا.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90937" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKLC2M4nRk_OX4Du6tlskU_JaYn_s8yeXKdls0RXtDoUumaYkMunP-g2fnGqf9OERWaHYF1kWPPd7ZDJPIltwcGxt5MhPmOtuQEtEkNNV0w8XMulfLaGJTZ27N1Nue8m0bQq7qrLaPao9aplm_1Gr7AE8zUj9Onk9uxJ537pRrK8W9DJGM1mvgMVWyOpyH9XsgWvOXL10w-E-85Ri4NKvO8a1A7qHKouJyFk9bzZjvIW5zMR04e4oDo-pR5srAWn37fE00tB6Phb0yQx6roMEPrHn088cHGXhdmn2PcQZwV_AzAsDQ9LdDU44hu4ncdPyFGDrz99yWn5MRzAabwJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
يسعدني أن أعلن أن الولايات المتحدة الأمريكية قد أبرمت اتفاقية مع مملكة الدنمارك وغرينلاند، تمنح الولايات المتحدة سيطرة دائمة على الأمن وجميع الاحتياجات الأخرى في غرينلاند، مما يعالج بشكل كامل جميع مخاوفنا العديدة في الولايات المتحدة.
لن تكون هناك أي تكلفة للولايات المتحدة. بناءً على توجيهاتي، عملنا مع ممثلين عن الدنمارك وغرينلاند لضمان أن الولايات المتحدة ستحظى إلى الأبد بالقدرة الكاملة على فعل ما هو ضروري في غرينلاند من أجل تأمين وحماية أمن غرينلاند والولايات المتحدة الأمريكية.
بالإضافة إلى ذلك، اعتبارًا من الآن فصاعدًا، لا يمكن لأي خصم للولايات المتحدة أن يمتلك أبدًا قاعدة في غرينلاند، أو أن يكون له وجود عسكري في غرينلاند، أو أن يقوم باستثمارات حساسة في غرينلاند، دون موافقتنا الكتابية الصريحة.
هذه "اتفاقية مدى الحياة"، ولا يوجد لها نهاية. نحن فخورون ومسرورون بما حدث للتو، وكل ما تم الاتفاق عليه اليوم سيحظى بتقدير الشعب الأمريكي. سنبدأ على الفور عملية تطوير وجود عسكري كبير في الجزء المناسب من غرينلاند، وهناك العديد من هذه الأجزاء.
سنعمل مع شعب غرينلاند في تطويرها وبنائها. هذا الحل هو حل رائع للولايات المتحدة الأمريكية والدنمارك وغرينلاند وجميع حلفائنا. نتطلع إلى العمل مع الشعب الرائع في الدنمارك وغرينلاند نحو مستقبل عظيم فيما يتعلق بهذه المنطقة الكبيرة والاستراتيجية للغاية.
سنحرص عليها بشدة. هذا حلم يتحقق للولايات المتحدة الأمريكية، وهو حلم مهم وتاريخي وخصوصي. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90936" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:  ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.  ‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90935" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5qGg3F3HGFSmO-EEnjZk1l0I25ubGWITRu0E-rtNRjSKKBpn3Lf6GSiBX6jDxzGMIhe_TESL58ShbswvgmSIsxKiUWopjTdCWseLkKIq-b_Nws_MtFygigLkY8_iZgGuTR60ocpRk6uOv1NLnh_llz8tm7gqni9655NgwAURxbDxLryWbJvgce0Y2P9IM8G1Be6PZA-wkWcuf1fFJjHVrCaFveGDbpLhxMAmgfevg695gn6JlGBQ19MYK2E_6MvZOaCOcvm7s12y9hfrWwhSTZxcZCdCAjg04JSfeQLpGQXr7pGvGiqyNA7QgIX5-gsw2G0RDKbCnAgnMKm5fF2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Scp9totiYqBGov_SmUwYcKIRJ1XvuFOmHWc9nv8KclM5QFs0YJdRSDcoZe4Ypi7NEyKeyUEp1xmAixNBjwNgYDxRcR2A1aGoP7i7L8l5pv1fTt6O9lNKvYaD63nVXpQfO2Ky1uhVe6uQVKJownO-qDPmExL7Kh0w2RdyDwjqlj9QK9b5te10NaOCVToFytY4B16-meJVvkaTM01OB9RMNHcxJwrKiBuH26bfcxeor8AdOYtU8OLVbmayacy0TMIKyB1u2VjB0fHG3TAnZI31d7xyjkF1mc0A5u1yDiBRixiDSN-HVOxGn-gQoS8QRygSNxpVZ2EOlYpO0lNaKN-eqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzU0fJrufKwcSNq3ZISr8HdrmXiHN_9-1sD5vmNAvbE3Lb9ODO1EiXPJ7qAn4s-lGP1G4bYQJX6MdIrj604lA_ZW0cs69akqhzxU465rlaW9Oep8COqcp2svz71n6XVaFZJDuaxZsg36j0rD6Vdq1hUtb_4t7SzVJTkSA2vgdcDIj9VN_hc1KHBoxzYAS4lw_tQsoNQCXyyJrCxazJ3qZ_SzpXoQ7o1ZO2NaoBzBiSGzZzxLJA7d7LvTBR1zDZddceqXxrWn-E6PsAtHkeOm5pxjH2T57kNW7YJHEhqtXhr0TgbRJtBej5JjB7lnaDSLwOo2oMOezaqXIDUmnN05OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz1nSnDN6OqGOkDnPfkyJiLgJKqzL7m2uIQ9isf5OaUbmsqN1WX-57yQiRrooCe34dcSbilr3nThA9Fkd01PCynULlikwQ-sjEJRgUXimIujRqOlGTL9HQ8doGe4NuSuJ3jeee-c4GuMrfQxFzRi5LGwPgEWl7B4Oufb5JAV_xALXhymJjjojLBoLiSzJvDxJUmiDU8_qWOZElMR_OnB7YO_n52smJHmC8zQqVzqB70saURP2dJa0V8F01IH69fBiiZsqfCPK9gxRxhra_gJWJ8Pdny3a7efy2q6jOBETdKKcdpEt-VKMfgNcU6X3snxTH8GQ02neKx-Qpu7XFnAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhjo9-crzIZdsh41ZKIS-ns_BxZRyrXT_Pj6iO_OzVGE7GrbGHgDKj4gEdhrMnxRt2Kd8PYFCrlIkb4YpElo0DZHu7WCFnpy3flGuaBrB3O7T-3mP-OPDW6QjWIO9rV761EJ2b1-GXCpnXEI5AqOhFa9OLH-HVxEePTkaoz5_st3h0MfJDEdkkJExxnOudRoOuuWRn49F6dPKEbsOgqdR9PIm-aqIZzFxfeMYzopgWLm91q8UYCqOetyxqEWBlL8lBQ4jE443q_msZGCveYQVubqsW-aRAJAQk0NIL1gj2q29JN_quR1rVYKw73ivRmbOlBZmqkw4L9dINfyvFD_lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مشاهد جديدة تظهر الدمار الكبير في إحدى القواعد الأمريكية بالكويت جراء الهجمات الصاروخية والطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90930" target="_blank">📅 00:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">السعودية تفعل منظومة لا تصور " تكفة ، امسح الفديو بسرعة " بعد فشل منظومات الباترويت التي تديرها اليونان و إيطاليا داخل السعودية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90929" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام أمريكي:
ستة مسؤولين أمريكيين مطلعين على بيانات الخسائر الداخلية، فإن عدد أفراد الخدمة الأمريكية الذين لقوا حتفهم خلال الحرب الإيرانية يفوق ما كشف عنه البنتاغون علنًا.
‏أفاد خمسة من المسؤولين بمقتل ما لا يقل عن 22 عسكريًا أمريكيًا منذ بدء النزاع في 28 فبراير/شباط، أي بزيادة أربعة قتلى عن العدد المسجل حاليًا في قاعدة بيانات الخسائر العامة التابعة لوزارة الدفاع الأمريكية (البنتاغون). وقال مسؤول آخر إن العدد الفعلي قد يصل إلى 23 قتيلاً. كما لقي ثلاثة متعاقدين عسكريين أمريكيين في المنطقة حتفهم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90928" target="_blank">📅 00:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مصدر من الحكومة اليمنية لنايا
رصدنا عمليات هروب جماعي لمرتزقة العدوان السعودي في جبل حبشي بمدينة تعز .</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90927" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خميس مشيط قاعدة الملك خالد تحت رحمة أنصار الله</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90926" target="_blank">📅 23:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90925" target="_blank">📅 23:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات في العلا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90924" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">أنصار الله تضرب ب ٦ مواقع مختلفة في وقت واحد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90923" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الهجوم هو الأكبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90922" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90921" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90920" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90919" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سيدفع اخوة نوره الثمن غالياً</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90918" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صنعاء بعيدة الرياض اقرب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90917" target="_blank">📅 23:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90916" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/naya_foriraq/90916" target="_blank">📅 23:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90915" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز ينبع</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90914" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90913" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90912" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90911" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">العزة لأهل الإيمان والذلة لمن طغى وتجبّر وظلم.
عزت برای اهل ایمان، و ذلت برای کسی که طغیان و سرکشی کرده و ظلم ورزیده است.
Honor and dignity belong to the people of faith, and humiliation to those who transgress, oppress, and act with tyranny.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90910" target="_blank">📅 23:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامب: سنرى ما إذا كان سيتم تدمير إيران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/90909" target="_blank">📅 23:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامب: أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90908" target="_blank">📅 23:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
حذرت الولايات المتحدة حلفاءها من تأخير في تسليم الصواريخ قد يصل إلى خمس سنوات، وذلك في إطار جهودها لإعادة بناء مخزونها من الأسلحة الذي استنزف بسبب الاستخدام المكثف خلال الحرب في إيران.
ألمانيا والدول الأوروبية الشرقية تواجه تأخيرًا في استلام الأسلحة، في حين أن طلبات أوكرانيا للحصول على أنظمة "باتريوت" تتأثر بجهود الولايات المتحدة لإعادة بناء مخزونها الخاص.
أفاد البنتاغون أن الصراع كشف عن "نقص استراتيجي في المخزون" وعن "عقبات في الإنتاج".</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90907" target="_blank">📅 23:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
الاعلام الاوربي:
يتزايد قلق القادة الأوروبيين من احتمال قيام روسيا بشن هجمات بطائرات مسيرة أو صواريخ ضد دول حلف الناتو، في ظل تصعيد موسكو لحملتها الهجينة في أنحاء القارة. مع ذلك، يؤكد حلف الناتو أنه لا يرى أي خطر لهجوم وشيك.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90906" target="_blank">📅 23:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
استهداف برجي طاقة كهربائية على طريق بيجي_حديثة شمال غرب العراق.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90905" target="_blank">📅 23:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJ3tPyzU_uZfEfRgisiMUWwACbzCLyMTQ6enuXFOh14dx7_aJEQwtSXJCcP_s4qe5g6mthuqBp3-ScVQ2h6Ptykmd5bzkYARdFxPczXz4ib3b-Ga4CHyooPlcLJ3PhD0byorW8ODMur3N_gYFIqkm4T_2kOfh6guptpet0k73RuhIHV4sof-ax8VyZlMYzqX2C-oQApgNT-kkMA-qk7U6-OkqaOJmryGUmG5TR4KGv5Bl9lf7tG7T91ISN44a4lOGq-6mvi6yumCvggU1W9gU79bLMc5VGnLHA-QDhYNP0CJf8zcIVvXMAYoCJgXMKbUPsZ1Czl8acrCGzfIfSETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة بقيمة 8 ملايين دولار، وهو رقم قياسي، مباشرة من حكومة الولايات المتحدة، في عهد جو بايدن، وذلك للحفاظ على استمرارها. يبدو لي هذا فسادًا!).  أحظر على هذه المؤسسات العمل من البيت الأبيض نتيجة لـ "تقاريرها" المستمرة التي تتضمن أخبارًا كاذبة.
يجب ألا تتمكن وسائل الإعلام من كتابة أو نشر أكاذيب وخيال بشكل مستمر عندما تغطي أخبار الرئيس الأمريكي، أو إدارة ترامب، أو الولايات المتحدة الأمريكية.
سيتبع ذلك حظر على المزيد من وسائل الإعلام التي تنشر أخبارًا كاذبة. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90904" target="_blank">📅 22:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
عصابات داعsh الإرهابي تتبنى استهداف قوة من الجيش العراقي في محافظة كركوك بتفجير عجلة، ما أسفر عن إصابة ضابط وعدد من الجنود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90903" target="_blank">📅 22:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي يكذب النسب الرسمية:
تُشير قاعدة بيانات الخسائر العامة التابعة لوزارة الدفاع الأمريكية (البنتاغون) إلى مقتل 18 جنديًا أمريكيًا منذ بدء الحرب مع إيران، لكن مسؤولين صرّحوا لصحيفة واشنطن بوست بأن الحصيلة الفعلية لا تقل عن 22، وربما تصل إلى 23. كما أُصيب أكثر من 820 جنديًا أمريكيًا. وامتنع البنتاغون عن توضيح هذا التباين، فيما قدّرت (سنتكوم) أن الحرب مع إيران كلّفت نحو 43.6 مليار دولار حتى أوائل سبتمبر، بما في ذلك 28 مليار دولار على الذخائر. ولا يشمل هذا الرقم الأضرار التي لحقت بالقواعد الأمريكية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90902" target="_blank">📅 22:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
🇸🇾
الاحتلال الاسرائيلي يستهدف غرب دمشق بقذائف صاروخية.
صرنا نحكي عل مكشوف
😆</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90901" target="_blank">📅 21:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 26 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظة تعز.
بلغ إجمالي الغارات التي شنها العدو السعودي خلال هذا الأسبوع 300 غارة جوية بطائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف واستهدفت محافظات تعز وحجة ومأرب والجوف والبيضاء وعمران لحج الحديدة صعدة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90900" target="_blank">📅 21:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbeW4Wq0r-ye30qulnDWul0vf4zoA2Pk1wb0ZxxLFYtxIW40h0lSagogUPyMrw0LO3ikyXdXs6Y-oxiEtAYIyE0WLXDHwGJEgOk4cv-GQ0A7_qZ7jKRGrZThL4JKfj-OdonIGWEg-tSQmaHr-DsJ7L0IFHCnDMwltJimyrD5RSX4pQ2EBAu_n4Kt3Ar0J9R0mq3_dslyHoloMM8A4YSFGdnlY5PIiDcY8DF3QVmVRDymqpbXBB-LZZSAEpqiIviXLWlz6b9KQ4Ey7QTs2uCtfveTMT7_dMAhIpUJ1mL7oQWrtvfbHeE69h-lmfdsM6KpLHzYKY75jeapU9A_ti1LDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: لقد بدأ بالفعل العصر الذي يتم فيه مطاردة طائراتك من طراز F-35 و F-15 ويتعين عليك الإبلاغ عن تعرضها لأضرار
🤏
.
ما كان في السابق كابوساً مرعباً أصبح الآن واقعاً يومياً. تعايش معه.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90899" target="_blank">📅 20:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
🇨🇳
الاعلام الاميركي:
كادت القوات الأمريكية أن تشن عملية ضد سفينة صينية بعد أن زعمت تقرير استخباراتي مدعوم بالذكاء الاصطناعي بشكل خاطئ أنها كانت تحمل مكونات أسلحة نووية.
اكتشف المسؤولون، قبل وقت قصير من الإجراء المخطط له، أن التقرير تم إنشاؤه باستخدام الذكاء الاصطناعي وأنه تضمن معلومات غير دقيقة.
أثار هذا الحادث مخاوف بشأن مخاطر الاعتماد على الذكاء الاصطناعي في مجال الاستخبارات العسكرية وقرارات تحديد الأهداف.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90898" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7e415de1.mp4?token=cWgQVyEw13kngJRPB43uDo-wIgJW1it1HKx-ZSkEpybYpntA_S0o9wzJ1ToSl8MClSD4xjSy5yo0U2deshuv5Gg2hFIFV6wh0QkJXtCZXW4KwsnlULHSW7Bgh4gN5p3v0rjnwRVNzVLV2wAu-i5s2sNt7EluLcPcklxFB5Qx5fGTeaBXf4UdRkX_Dhhp62AEnHNasALdN85MVzUatx2fTh-lFNMBo5ZT2WTaSs_J8ZwFawJed1ibWWJ7tfZD5LMzmLuIwrCfnOkUKEZUl7NmeOPNFj7U_EqJJY3M8d4gkP4AO547q_hBtv_2AuRGMf1gZFLAQlme9mSikXoHO79s3XIdyCM8wkeGqRZix6j8U_DSZzH97VlDq247D_fqCKpaNINidm3gVuxHmrc8sCmrxy0q7R-KUxhxmc8kCo4A1E-VQlL97oMV6lrj-LyioaiZDvzdLaIS1N2ZVKCwjZlYcRzEcjhMiyqkNI8W6jlhwK2nKbJj4MU9H_kfrENtdXn2nmieVQCFRYEg7B2iHF3JfD1ZAbUEF-vzu1t_uoIpfSMISh0cd09rCvVQdeDM3RBXFMusxsZk381wdnl1sKfWVWnS6VeOZyWDTaOUBDgT9eUOjNljOxm6uBmZmSbbYLO0P0M6vmZnvHNp8sj-E8hAQqrDUK_7LRnt5myjwe1t4Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7e415de1.mp4?token=cWgQVyEw13kngJRPB43uDo-wIgJW1it1HKx-ZSkEpybYpntA_S0o9wzJ1ToSl8MClSD4xjSy5yo0U2deshuv5Gg2hFIFV6wh0QkJXtCZXW4KwsnlULHSW7Bgh4gN5p3v0rjnwRVNzVLV2wAu-i5s2sNt7EluLcPcklxFB5Qx5fGTeaBXf4UdRkX_Dhhp62AEnHNasALdN85MVzUatx2fTh-lFNMBo5ZT2WTaSs_J8ZwFawJed1ibWWJ7tfZD5LMzmLuIwrCfnOkUKEZUl7NmeOPNFj7U_EqJJY3M8d4gkP4AO547q_hBtv_2AuRGMf1gZFLAQlme9mSikXoHO79s3XIdyCM8wkeGqRZix6j8U_DSZzH97VlDq247D_fqCKpaNINidm3gVuxHmrc8sCmrxy0q7R-KUxhxmc8kCo4A1E-VQlL97oMV6lrj-LyioaiZDvzdLaIS1N2ZVKCwjZlYcRzEcjhMiyqkNI8W6jlhwK2nKbJj4MU9H_kfrENtdXn2nmieVQCFRYEg7B2iHF3JfD1ZAbUEF-vzu1t_uoIpfSMISh0cd09rCvVQdeDM3RBXFMusxsZk381wdnl1sKfWVWnS6VeOZyWDTaOUBDgT9eUOjNljOxm6uBmZmSbbYLO0P0M6vmZnvHNp8sj-E8hAQqrDUK_7LRnt5myjwe1t4Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان تقدم ميداني كبير لانصار الله في اليمن على جبهة راس العارة بعد تقهقر مرتزقة العدوان في جبهة الأغبرة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90897" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
ترامب: سنرى ما إذا كان سيتم تدمير إيران.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90896" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامب: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90895" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
ترامب
: الولايات المتحدة تتحدث مع الحوثيين، الحوثيون أيضًا يرغبون في إبرام صفقة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90894" target="_blank">📅 19:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇷🇺
روسيا تستدعي المبعوث البريطاني على خلفية تزايد شحنات الأسلحة إلى أوكرانيا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90893" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90892" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90891" target="_blank">📅 19:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
إفشال محاولات إجرامية في العاصمة صنعاء قام بها العدو السعودي مصبوغةً بالصبغة الداعشية ولن تمر دون رد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90890" target="_blank">📅 19:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
احتجاجات وقطع احد الطرق امام مولدة اهلية بسبب امتناع صاحبها من التشغيل في محافظة كركوك.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90889" target="_blank">📅 18:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يستمر في استهدافه لمواقع المدنيين في تعز.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90888" target="_blank">📅 18:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
اعلام العبري:
قضية تجسس خطيرة تتعلق بالتجسس لصالح إيران من داخل الجيش الإسرائيلي قيد التحقيق حاليًا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90887" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇷🇺
‏
الوكالة الدولية للطاقة الذرية:
برج التبريد التابع لوحدة مفاعل في محطة كورسك للطاقة النووية في روسيا تعرض لهجوم بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90886" target="_blank">📅 18:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇷🇺
🔻
رئيس وزراء سلفوكيا:
أشعر بقلق بالغ من أن كل ما يتم السعي إليه الآن هو ذريعة لنشوب صراع كبير بين الناتو وروسيا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90885" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
رغم انبطاح الدولة اللبنانية..
جيش العدو: إقامة الجيش اللبناني لحواجز بالمنطقة الأمنية بالجنوب "يخالف التفاهمات".</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90884" target="_blank">📅 17:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90883" target="_blank">📅 17:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90882" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90881" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90880" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab46f5034b.mp4?token=qO_WaerHNoY7j7ZABOXUmWW4dZsL5Y2Z1ZvIKZSpA0RnWR1BVbu1hqNRIm6Gh7gaHm6ksREbn1v90F32OwpZUqfyHvlf61BuTR8q1kJ5tMSh0Ek1GYwKT86QI6iclURzhCihDU5Shy7uxJ4kgEtf2_EdtMqutFiTw8uaSjlGaACz5514Uh4YW_5WONb6eTg_39gdfUm5kqlD_09BcbR2AzfDiEEnsNdT8tkKpbX8KOUs9YYlj2IQI7onUOj5uJPmwLJPs-KsxFEyAtVZPHHOY3OCgCPSFzyLyp_OfdGdJxRtmVUl8tD8lYvENZEMo-MzvgU4STL8tglSz4uVC3rRGaCoZgVTyqHwPx3lrDn_W2fE9HcDBQSxN4MXMcg-gAwx-m4IU05x2SXYc7BK0l2QPjxzdOX0zy68jaAtY0M8iGkvI6BXX7xem8vQcO7q9OSAK1VNl_d7flULjpyXuA9foeRX5X4fc9iwM-leqToxKqTjW99c0aW_DmfiguBuq9as0eEJpKhXH2ruJpcQdhBTGlQDvELn9JwGeCCNWU634lVWNTBY37nSWotYxoygk2Q8knitBJlWIR_LTqAmd7ZI6vm0A-YMG4I3RZp3TkwNr64hGGDfMRLuoEqDliJ5kQIrsQoju-Jx7vhuk7Pl-fBjD5bKqyfG6fGO31ptBq418SU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظام ال سعود يستخدم منابر المقدسات الاسلامية في مكة المكرمة والمدينة المنورة لمهاجمة انصار الله والتحريض عليهم دينيا وبث الاكاذيب لتعويض خسائره الميدانية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90879" target="_blank">📅 16:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90878" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbODQkIAUCL0ruBKjw7JMrKtquJYvA3BuuFpfVm0YVCAZW5KqElazamOXNQdZKi3CCI4EsgTiuO8h9CR0ZQAlF7pIEu0mpkTh51XZyiL5U0x16L91N48HeyWYK2Y1h4hCPkOOIJBok0v59epeZ-pWxYJQD83KTYeWMWvxW4qWqVchhN_22hhP9NyO9d7ZMVlVOSTg9eh4N5FICNWeIXTVYwIXfi-Jfx5paoCIg_OxPn1-ex2gYGTtsKrLxPuE0ssWSo92bKOKN1_O7TCxRqMCcU9Az-lCSEpUHJn7HcDjlEiw7Z6RWptsTg2unNMnERPOInuL1rH3fmZMmJGPh_EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
مشاهد من العاصمة اليمنية صنعاء لخروج اليمنيين استجابة لنداء السيد عبدالملك الحوثي لادانة البهتان السعودي باستهداف مكة المكرمة واسناد القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90877" target="_blank">📅 16:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me8mHQMZc8RmvHLMwcpoB-TZO2tQMkYo8GS94HXgJOhgNySd_SqDYILrh0dV_tcF34TIejeQb98M7aEaROMZtoWCEj4HISHG5LY3lFeASM7pd1CHwij3Z83lk70zzzsT3aGPCzaBy7_tBUxkaVhxNOXFjf0elJVJvXjuUCmtMKCYAxIhJ08jmR2oVeb2Dw_nw9jFG8eMCA2qixbJdUg59tiGbC3hDn7rvxIJLsJsK2lJ5QoiVYCjupTNa-c2ij1SZPSddi4kZQBZhL0P_jz7W5fyzE1lw26OEnlWzTr9RRx73apZZjRugbSsFpaV7m-3p1UcSQ5yyKaaK31Pl8bhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEw3RKMjecDdLmcsGYDxFVkGk44BvNgwlXmpYj2-U8sK-ia6MUVe7zQ2iNehecfIunTyUWT7MFD99SzBqzJdq64QWQ976L-HHa31DdtzYhN-PGU9Eoakyd7GuDFASXRZ-bmY5UN6siY-2_J0moGIvQ8dNIBqyMb1I1qlY6Sgbjm8yKTwA8b6LufWgIyuTJ1L6vpNFXyHqZHUdtxb4h8p_kI7F7nPqMOFXaX4T44uYlv49lWSRUyPbPpy4W01tPYEDgxHB7zg1OqtmZ6RV_wYuXxAwgREPEpTqvnmbstfhUN2nGyci5PANP4cX4perKiLRMURbMLzgtkidyANrPusiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULmyM8P-2QYxvjANxzg0Se2nacnP0H2qGj_kqSk-mvM6dBqEboCFFhOiF4NxMWs1OIXvYh1AoaqRRQcTE5oAXQj7LUoHkHRrxatJlsgsS0I1K5jcCdvsLrqZVnMQ0QS4VEKe197avVmBWqXKezySujynQ7tF0ItQDTLLt7get2-9mCFcn5BkRJRz2L4dX7T9hxpIlrCjL7zsWiXyPKKwBaeXj_J6sste8ObBUZvc3x68ouSR7i97--QkOHWSmTSpW_YKbo90q2cmYgTuQxlB9KSzaxtcALd1bTAJchB0uPVdqdo0Wy_MwZqg7vavuhb340Ub2rIArOTHEip0AJUzXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇷🇺
من محافظة واسط العراقية
منتسبي الشركات الروسية يشاركون بانتخابات مجلس الدوما الروسي ؛ الانتخابات تجري تحت إشراف السفارة الروسية في بغداد ولأول مرة يشارك العراق عبر المفوضية العليا للانتخابات بصفة مشرف دولي على الانتخابات داخل روسيا ..</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90874" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏الاتحاد الاوروبي: هجمات انصار الله على السعودية غير مقبولة وتعرقل الاقتصاد العالمي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90873" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
الـ100 دولار امريكي في الاسواق العراقية الان تسجل 159،250 الف دينار.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90872" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الرئيس الفرنسي:
نعمل لإنشاء خط أنابيب لنقل الغاز والنفط من العراق إلى السوق الأوروبي.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90871" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دير الزور السورية بانفجار هز بلدة عياش</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90870" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebNvvxhIxohgLt6NBDqMjD3SJCiv6CgA0uLBacVUloI9YzWb4sYgG1_cVSW4qnSBa4YWrdlyhO5W6hy2gjvHv3w7wu6d-OYfj6T8htMxvOpcnRgCku0uo8D5KWVsD3SaQWYnoJ3dXs42jjfixR9FPH16aRWEI4tEWTrNs9BaeLaqc-q3z1SyX0WN6k4KpJLBgKgc4bnF4Jh48C1n0YUpwyaaGYBH_vHaAMrApC8sZVHTD93t4ZcMqYmOtEs70baPhlM89eO2XGLPCppNEjwy8fZxT10TwDEPBGZQS2gAXjnoNvZ6RR5VYxtYTE_SJGONlXiC8sH-gmiYckaxeWh_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
‏السفير التركي في سوريا الجولاني يفتتح "مدرسة رجب طيب أردوغان التركية الدولية" في العاصمة السورية دمشق.
ورجعت أصالة عالشام
😂</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90869" target="_blank">📅 15:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
🇷🇺
🔵
ماكرون: استُهدفت فرنسا بهجمات روسية هجينة في الأسابيع القليلة الماضية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90868" target="_blank">📅 15:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي.. حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90867" target="_blank">📅 15:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شركة أرامكو السعودية تبلغ مصافي النفط الأوروبية بأنها لن تتلقى أي شحنات من النفط الخام الشهر المقبل بعد تعرض خط أنابيب الشرق والغرب السعودي لأضرار</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90866" target="_blank">📅 14:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxQSPuM3cH70RY98qJLT4HxDJwDo0nZyTLbg95kbyJePlMIAnvdFp0vys9jryb8ndGciXe_Cw1b04mq4K7b15GFi4E5Xs7XS_JKi9LZ3lwrQaIU40ut6obbww83BRfFXtROFqlMM6xZWifQUL3sGrVxULQmH7dqZtkdsTXMXWydKffLl-RwICj_gaNhsxR_GGh69ITE0gOWznyAlMUcODr-GJjBvSDpnf-jv7unHULSnRjOTucNRaaAJATYe7w0o_TZ8_IRs-z5J_42FnI8TqMr04w9njn6j_u6Bf9-uieg0CDWCmFgb2FYcInU8VmiFG1kp-XpnsbmNKFvaCILAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان فدا
شبه لهم يا حسين
ما طحت انت من ميمونك</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90865" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🇷🇺
وزارة الخارجية الروسية: روسيا تطالب اليابان بسحب صواريخ "تايفون" الأميركية من أراضيها</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90864" target="_blank">📅 14:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
إنفجار داخل مسجد في باكستان؛ 17 قتيلا وعشرات المصابين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90863" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
سي إن إن:
‏الجيش الأمريكي ينقل طائرات بدون طيار إلى أمريكا الجنوبية استعدادًا لعمليات مكافحة التمرد المتوقعة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90862" target="_blank">📅 12:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
هجوم بالرمانات اليدوية على منزل في العاصمة العراقية بغداد منطقة السيدية ..</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90861" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي..
حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90860" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
وزير الدفاع الإيطالي:
إصابة طائرة تابعة للجيش الإيطالي خلال هجمات على قاعدة جوية في مدينة الطائف السعودية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90859" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROYwEqtnQC_tMBdRPRqBbslkZ8T8dbf2BnYvEOFN5jnV0VdGYv2iSiVmvaxwm9nldCCaa2cVlzUoYTy5-Xvo7GPeaHm_Ib_0QXaOCXcHyCBT9enwrihYsLhb0sf5tMpb42Qem70gLmgPVu3KELgmGotFSq9NWDucji1xh_jbJIBhBaI2rW14swhULoD4AsUCc0dS4LvSDz5ImQQf2VQiJfk_flG5YCqRTZU2v6GzuS21UGsy6rwBsIxnaOYiaiBXfpZALYjPD86TnvwifNDCT1o7t8s4rC-Mx-3-x88j46jcQTMX7nA24t1IoNgc-yTIERUfW6byA0qtA0P9sbNauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستهداف ناقلة نفط بمقذوف حربي في مضيق هرمز، أدى إلى اندلاع حريق كبير فيها.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90858" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvJ7lEUy5aPTx4GcFEW4LSssWKV9S-vKbB5oDXdsgVMkCScNKBbLmgldWqmiJb8nhe0Rqt7-I5zRlcZXl2RtO46Y2rfNF4rNOKXrvJ7J8E5Xwcig97nFEc2S4OFGBDk9-Jla571mGbtiFG4m6SXrVAfCRlbezfmlwx7TZAdPiaPtIQrbpdYIgy6_AiIZjJNEeCCzLl_vToPfeymi6B4E6xsPfESzNaXpLjodnu9i40J9FMS2_fM5vyIHzdnKUHVCiD1Ol1JshFJ_d-awPVNPvxOwuJvLNjjCeJGQFp2-5fN5sgoNkk26h5jFTMKFunW0n6ilBKklkX5cAAc_SCJZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90857" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90856" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇱
إعلام العدو:
الشاباك والشرطة أوقفا مواطنًا عربيًا إسرائيليًا من سكان مجد الكروم للاشتباه بارتكابه مخالفات أمنية تتعلق بالتواصل مع عميل أجنبي من لبنان.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90855" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد تظهر إقتحام وزير الأمن القومي الصهيوني "بن غفير" لحائط البراق غربي المسجد الأقصى الليلة الماضية، حيث أدى طقوساً تلمودية برفقة عشرات المستوطنين الصهاينة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90854" target="_blank">📅 10:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حضور الرئيس الإيراني مسعود بزشكيان في مناورات "فدائيون إيران" العسكرية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90853" target="_blank">📅 10:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تقيم الجمهورية الإسلامية الإيرانية مناورات "فدائيين إيران" وبحضور 313 ألف عنصر في العاصمة طهران وبشعار "لبیک یا خامنئي".</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90850" target="_blank">📅 09:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90849" target="_blank">📅 08:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=t72E5cNLXvdDmp7fYIy6R95engUCUJxxzhdh9ck8DHXEn6SjIC5qgOCE9HQr05S2dDSVgxvut2sGS8niMsZMzO5VYBOAOsmDLmlw5pc1nRckiIDbo85nQWsQ6SpLn6970cKgBmWm1mAhm2m1w_AKK-7Y77Ry8VE8uuwgoWVC9GhTivLJyiQ6HqJZzFWkGsGTCH9PmRhZHqznRRVnJpjEC6ZDBYEbeotLCYLN3Slhk8SpdppcRK8n5_T7xcMm42hk0D5_DlRgg2EzICoIAn5zI5O6dbbL6gY9qiOfGvW22spYKK2NFdop4OH83BRnO4meKdneEISwvw1VPJtQz-E0Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=t72E5cNLXvdDmp7fYIy6R95engUCUJxxzhdh9ck8DHXEn6SjIC5qgOCE9HQr05S2dDSVgxvut2sGS8niMsZMzO5VYBOAOsmDLmlw5pc1nRckiIDbo85nQWsQ6SpLn6970cKgBmWm1mAhm2m1w_AKK-7Y77Ry8VE8uuwgoWVC9GhTivLJyiQ6HqJZzFWkGsGTCH9PmRhZHqznRRVnJpjEC6ZDBYEbeotLCYLN3Slhk8SpdppcRK8n5_T7xcMm42hk0D5_DlRgg2EzICoIAn5zI5O6dbbL6gY9qiOfGvW22spYKK2NFdop4OH83BRnO4meKdneEISwvw1VPJtQz-E0Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تريد عقد صفقة؛ لكنها ليست مستعدة، في رأيي. إما أن نعقد صفقة جيدة، أو لن نعقد صفقة على الإطلاق."</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90848" target="_blank">📅 02:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نايا - NAYA
pinned «
إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90847" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90846" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة جدة السعودية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90845" target="_blank">📅 01:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4RPLDX2IuvOW0gtgbjMVFjdOSCMhoDLyjWaYRS_8Jt_wGooffRO3Qr2R4feR5Dn4FGs75tQ-A2E2LbMLi_2b4lT21_puMIEbO6JViiqxFNrQFla8CoWSAqx7wapx5XpzEOeyjXYVPiqoJyEOt3t_nRb62bPZAXPHROlOFYNjcJDIKnp0U3rFqR-wlELgVXmOWWMjjhE1nqapkLTRZtJ7B_9fpJYVDL0z5PFS6FOstiXxV2By4c0nVmdoKduTU2BYvoa-UuBMK2B0lRc0t9LNX-wyWCYig-safYQ1kyF3CDEE1exTSqC8rnw5ddPTipOVNw_sc9kux5d3VKL3iMSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
الانسحاب المذل للقوات الأمريكية من محافظات اقليم كوردستان العراق مروراً بمدينة البغدادي بأتجاه سريع الأنبار الأردن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90844" target="_blank">📅 01:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=vjJe8VCTrDu4C1AM7r8fZP1tINKSTXwhfLd8PNPN1rEAeSY_A6m6M3I2A6gB1K539JD7-fmRvyBn0pPjBH2GfautklWo28YcVAUVYUXutraYL5bVRTHPW9Nf9HKIH9EN8eQv2VjWFO3yQR51fhKFdqnlKbDit-Pt2oxs9O9ef_XUd1BCisBDD-hGJVVG5ExZ4I3NjAWF4hq6MbYzuofrsnv3RR33b_PA7ra4Fx_30qCHtOUXVDlbry-BRLreSyAiaSO3corBl2DXEmuQqlW38BUfy5hnMXPNnbSZ0HKe-6hoinLymaCZu7QYMBH2018HBsQ7WIWEb0LaUa5Jxy-tsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=vjJe8VCTrDu4C1AM7r8fZP1tINKSTXwhfLd8PNPN1rEAeSY_A6m6M3I2A6gB1K539JD7-fmRvyBn0pPjBH2GfautklWo28YcVAUVYUXutraYL5bVRTHPW9Nf9HKIH9EN8eQv2VjWFO3yQR51fhKFdqnlKbDit-Pt2oxs9O9ef_XUd1BCisBDD-hGJVVG5ExZ4I3NjAWF4hq6MbYzuofrsnv3RR33b_PA7ra4Fx_30qCHtOUXVDlbry-BRLreSyAiaSO3corBl2DXEmuQqlW38BUfy5hnMXPNnbSZ0HKe-6hoinLymaCZu7QYMBH2018HBsQ7WIWEb0LaUa5Jxy-tsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بين ياسر المالكي وقاسم عطا المكصوصي من سيختار تيار الحكمة الوطني وزيرا للداخلية العراقية ؟</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90843" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارة الدفاع الأمريكية : خلال فترة ترامب، تدرس خططًا لسحب الطائرات والسفن والأسلحة وأكثر من 25 ألف جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90842" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4nPGddMkalfw-uNLsbeacXHXDv-4P1n4wCAmFOUhfI3wDfFxH7TA2ca7_RPSN3ZnH5RLC50IPGxD_NOhn2hIYNO4JQsp9Vv5XYFViYxVAL7V2VE2ureSgX_PxXba7jVYknOP9bAStwUrvRvFHZE8UlixJmUuq2TA4sSCYXoYyy57kHs2rGPw4mnctVrDjnYn3mfwwbNdmiCeTCjV4hYDjc4U3IJ2VMZODa_cH5VjVU1NBE2fWXlcDZbyXPj23B9AVoXWjJUf6ty0fAHBPdHH-cbZ_7d-VKDeZeVd3Bics1fdBPTXbrcKxaGCJeie22v94yc6-ECDU-BBlM80QtyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية لاندسات 8-9 الملتقطة اليوم أضرارًا إضافية محتملة في محطة أبها لتخزين النفط الخام جنوب غرب المملكة العربية السعودية، وذلك في أعقاب هجمات الحوثيين هذا الأسبوع. ويبدو أن ما تبقى من خزانات تخزين النفط في المحطة قد تعرض للهجوم والتدمير.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/90841" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewQoQIBJMMKAUVeDE5AMA2qMw-R-VUtTPx9mjcj3PR8ksUINDh-FaDDH_kuwQhes6aQ6AaOlloxsORLmIZGLoi0iSzSI3EHLXdJBMjZyLEyPa97R_fx-rquFgKKpltr9fnGhweV80aIy-QE5Z40wR0Gw1JwjrDGWvEvgElOtASzIDI1UzY1lTDs7xglqskD-ZPA8vDx2VkesRAMU3Ui_FWO0rhfkPXVsSwqrpn-sEoSifI2G14mzS1U5IEIlUNWDLCAbG_TyYNQB14ctVJUHPJ1vIVgVFf61Ph6YYgiCdQEzZYmP1ackYvUXKjKg_b6gHGmO8le2AD606KGpzreBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/90840" target="_blank">📅 23:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZgTuzUCmKXeIEmiy77FUsg-5Q9Pnew6VgmIP3pBzj71VQPXhXZ_CKKBtrrFv7X13U7Jd8LWbcNyzGcLdpd4m7b7CHrPUSd-e6ft3BlwWw73OBbjYc3BQumZCIWENz72cD6qIhcwJmoHQhEfqN6hHCv0FgZunNH5FpfhjTaI4mzGQM-em0rqg0EXeG4dNdwZkfbYxC1wIYbdmVjt3veF_WmQ4dTk8cahdvIgPobqIoQtluxXGRk3WXkZjblW0bEozfpcRcxkx0CxQ9Da1MlxGp3KbV-QtDcr9j9j1m3XmNbaN21MInYAhV_I-N363bpJNud30wMI5EDLxBiaAMlvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: ‏انتهى النظام الأحادي القطب الذي ينتزع فيه طرف واحد التنازلات بالقوة والإكراه. وقد رفضت الصين وروسيا، باستخدام حق النقض (الفيتو)، الاستغلال السياسي لمجلس الأمن، وأكدتا سيادة القانون. يجب علينا الدفاع عن التعددية؛ فالأحادية لا تخدم مصالح أحد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90839" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90838" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/90837" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_WzFvvA-QFoiNNJPAwQjjTwd_55R8rsrjSTOCFOeJcr3KnJ233rx2-PMpAaaIluae4YiOoVs8Er361WXwaILEYwiQex-58S2C3jis6hsNFlSkKveO11Op92UZo8QephsVAG3yvJp29iQVgyRlgWN1AGtapJiiBZcOvCyZ28JR3IFkCoxXT_9rsztKlmsCA1Op8Nd_3k6wbEvInq22-dYbYyIvqnLpPl1ezZxUDvk_-QOuRkQ_KUJTdDselX4V70vkwZtGWzdD7p-0kOd5rFMkLPAKaxsszo9ipS7-ZayERiVlr-oJ7eIP05Rvqo0q6H76DJxIRzTLOb-lXPiIkggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وردت أنباء أولية الآن عن تحطم طائرة من طراز إف-16 في مقاطعة بلير بولاية ميشيغان.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90836" target="_blank">📅 22:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
🇮🇷
الخارجية الاميركية:
واشنطن تمنح تأشيرات دخول لإيران لحضور اجتماعات الأمم المتحدة .</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90835" target="_blank">📅 22:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 37 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظات تعز وحجة وخلفت شهداء وجرحى من المدنيين.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90834" target="_blank">📅 22:04 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
