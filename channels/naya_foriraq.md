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
<img src="https://cdn4.telesco.pe/file/FKHlvjEDVU9q_fLGcjHvfUGNv90uwNr6RfMxM3Q46hT6ZoQq3ofAdA_kX23C_fGzPnIaxR57Ov-Kw-vaZnNQxtr5bd92n2QNUvx6E3kG6bkPhx1mMnlXLj1zUoXJiK9fPUjr_hdqVP4WYAGI7hUokHnDZzvQGzY2lai8gijiJlwIgsXIJBu7o0kMr3jaZh1XAj4TWrgBeOy8CBAGKnXpQKxRx0N850HO5YEcjktrpkwZ9yrZh4lWRDzj1L1nFE8xR3F2f9ZHQUjwplRMlS3PZV1hn-TfeHc2FzsKJBcDc4aVou2a26ct-y5iH0PE2fzyXlER9v5vnuEahbUdgPsvZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي:
بسم الله قاصم الجبارين
﴿وقاتلوهم حتى لا تكون فتنة﴾
استكمالًا لعملية الرد بالمثل التي نفذها الليلة الماضية مقاتلو القوة الجوفضائية التابعة لحرس الثورة الإسلامية، وفي الموجة الخامسة عشرة من عملية «نصر 2»، وبالرمز المبارك «يا أبا صالح المهدي أدركني»، وإهداءً إلى شهداء الجرائم الأمريكية الأخيرة المظلومين، وبهدف تأديب المعتدي ومعاقبة الجيش الأمريكي قاتل الأطفال، نُفِّذ هجومٌ عنيف ومباغت على القاعدة الجوية الأمريكية في العديد بقطر، جرى خلاله تدمير منظومة رادار بعيدة المدى وعدة طائرات أمريكية استراتيجية للتزوّد بالوقود بشكل كامل، كما تعرضت عدة طائرات أخرى لأضرار جسيمة.
ليعلم العدو الأمريكي ومستضيفو قواعده في المنطقة أن تجاوز الخطوط الحمراء والاعتداء على المدنيين والبنى التحتية غير المدنية ستكون له كلفة باهظة ومُفجعة، وفي حال استمرار هذا النهج من قبل العدو، فإن ردودًا أشد تدميرًا في الطريق؛ ردودًا ستبقى خالدة في تاريخ المعارك.
(وما النصر إلا من عند الله العزيز الحكيم)</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/83599" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في العراق :
ويُنصح المواطنون الأمريكيون بما يلي ، لا تسافروا إلى العراق بسبب الإرهاب، والاختطاف، والنزاع المسلح، والاضطرابات المدنية، ومحدودية قدرة الحكومة الأمريكية على تقديم الخدمات الطارئة لمواطنيها داخل العراق. ولا يُنصح بالسفر إلى العراق لأي سبب كان</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83598" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر   احتجاز السفينة من قبل أنصار الله</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83597" target="_blank">📅 12:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83596" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83595" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83594" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خون ریختن خون بریزید خون در برابر خون پل در برابر پل برق دربرابر برق برج در برابر برج</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83593" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇪
🇺🇸
🚀
صور الأقمار الصناعية تكذب وزارة الدفاع الاماراتية
صور جديدة تظهر احتراق ثلاثة مباني بقاعدة زايد العسكرية ، علما ان الدفاع الاماراتية قالت حريق خشب
😆</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83592" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEMn5baYAsrhiw8zPftexTB3jf7XGvBcdm3O9ayLVTCkWOt7vQat5t2htN0Qe7exDMtqreln7yw0BSwlK5mtgQwJvIAjun67OMXN8kaHJKtfuX5fGh1cM9QS14HGcrNWQsTQJW0QIZ6gASuHvyEVD__xXIiuiujLOTnWEZkfoH4oI4lt-YEAIWPIVQ7F0PTx14dpYyvKcuaVZXpAnFLSIONZdMC4-8N2kKLUMT1ssFKF1zyCCpqTUtCJDm1J56cswWgTuQ8vdz19VfR-x_yI7IJdYpORq8ALmv66Zw5nlDG_E6LmSMPRCx74Gmcur0ADq6rEpfoEx8NoCbakuXWS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🔻
مسؤول في حزب الكومله الإيراني الارهابي : تم إطلاق ستة صواريخ على مقرنا، أصاب ثلاثة منها مكاناً قُتل فيه ثمانية من البيشمركة، وسقطت الصواريخ الثلاثة الأخرى بالقرب من نفس المكان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83591" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
US ready for airborne operations inside Iran</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83590" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
في إطار استمرار عمليات "المعاملة بالمثل" وردًا على الجرائم الحربية التي ارتكبت الليلة الماضية، قام مقاتلو القوات البرية التابعة لحرس الثورة الإسلامية، في الموجة الخامسة عشرة من عملية "النصر 2"، تحت شعار "يا مهدي، أدركني"، بالإضافة إلى تدمير منصة صواريخ "هيمارس" في الكويت، بتدمير عدة مواقع لقوات أمريكية ومعارضة مرتزقة لأمريكا وإسرائيل، من خلال عملية جوية وصاروخية، وقاموا بقتل عدد كبير من المعارضين والقوات الخاصة الأمريكية. وتستمر عمليات "المعاملة بالمثل".</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83589" target="_blank">📅 11:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83588" target="_blank">📅 10:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83587" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkwsMZ_WqTaWQqPlZvFXnXoUHZH19Qs3hvGOwvbe375EYNvVXYUULba1F1UFAI4LFaEfm6itS1R5uwfzQcZzsJ2GNPZYykspCe9_s4MRVvWr0gad1DkaYJAM1sYdipS6DmMjTicA7R-LhtXuKztqW05UGFbx71dA1btLseTeHBZQ-J7xNh738uWC3PBuxqFlq7yBjiSNX_45dcJfDnntSVxzEQPklTsLiJLXXKn46TMgJKZ40kxjkfJy-K_JDNYsAm7830-5WgFt5kAoVV-RJ2ZmymsZaYnAn2iZ3MydZSVQNUvyFcjvMHxFEirX7flG-OqcJrcDxCikjbyw6A56Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83586" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دريغا كه ايران ويران شود
🇮🇷
🔻
🇺🇸
Trump , If you are man come in the ground</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83585" target="_blank">📅 10:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83584" target="_blank">📅 10:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83583" target="_blank">📅 10:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83582" target="_blank">📅 09:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بكين وباكستان تدعوان إلى وقف إطلاق النار واستئناف المحادثات بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83581" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">استهداف رادار أمريكي في سلطنة عمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83580" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83579" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URWjItrk5Ks5n7xyvrB7n-f5GooEkqlpQ0BzlLHGkGozY7Qk-0VBfJDz8mhXxJKnFl_ERW-KfVW_ahTKgqAm9pAt2yzXefnRB9tCwmtutxIOoSAyCmI4BnCgd9et0qtjgn4rJ7efd43xxcQD9hCG-TYjmR8ZJeRDNboXcu0opsb2RXZvPdfHjX1QVpnHn8op_s80f1qDnxE2b2d1pNKpF-WrCrAPkcSDaThqgO3PxwUDD6zWVsgOtI-x4A373Vm2n2vRX2t-l03ti5HN4ZAYGtdpD_PGrh5Piy32vRa35HZYFcjSz5o2hICirpEUF0tnHsFMjx0NNMS3WiBOIvOQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
🇦🇪
بالتزامن مع تبادل الضربات
الإمارات ليست برئية ، حيث أظهرت بيانات تتبع الطيران تحليق طائرة تزويد بالوقود جواً من طراز Boeing KC-135R Stratotanker تابعة للقوات الجوية الأمريكية فوق منطقة الخليج الفارسي ، بالقرب من سواحل الإمارات .</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83578" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83576" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUN_7ALzk8ppSYc0004XmHXeM4SUru26FDBM8JlbI_AaiAnAsBFItu5gSFEvn80ZPdYRiTZb7BNG36sm9smvUm0_ckW0vPeu_gXdQA8xN4EnUoORk4Sxv7FBaH6iZt8-pzsO6ov08qxgkFDdMIBjOKiptkIbI4u22u7MZ26S6jdrZmvysksjWz_MuigESZ8mS_WTUyM5VXsuHRAiXCJdBIscutZnycHBUHKhhkiiXWBsZ-a6OG0n75J-SZtNQn8MPKK4e3_kHngFY1hkSnTrnNqz8scvHZbtMmzapP30wzlSUdvgDgvc3v4admgKKPW7jnybthabVRJFca1K3tNzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون ریختن
خون بریزید
خون در برابر خون
پل در برابر پل
برق دربرابر برق
برج در برابر برج</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83575" target="_blank">📅 07:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83574" target="_blank">📅 07:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/83573" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83572" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على مركز قيادة العمليات الخاصة للعدو في منطقة التنف السورية. بالإضافة إلى تدمير نظام راداري، تم تدمير عدة طائرات هليكوبتر خاصة تستخدم في العمليات الخاصة، وفي انتقام لدم الشهداء الذين سقطوا الليلة الماضية في إيرانشهر، تم القضاء على عدد كبير من القوات الأمريكية المجرمة.
لا يزال السيطرة الكاملة على مضيق هرمز في قبضة مقاتلينا الشجعان، ولن يتم تصدير قطرة واحدة من النفط أو الغاز من هذه المنطقة طالما استمرت جرائم أمريكا.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83571" target="_blank">📅 07:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veRXBs0YWIxcPhAYJUOa8p95ClvMlB4ht8gt_uXD0mvMLKSXzn3mzTe__Sn3la8S_sTSDKeNk9qH-M1sdTkVcKym1Y4U7uubI8YoOQiPpxwCUsKj-7pyuf0zNUvKg36F1V7XnApQB3AiVlXf3xPiSZV15SvLUAA9Ny3nIhBuJFFtQQuBvRpbyRQzFBK2PkE2VRokND3BDXxsmMWxxJ8fYmc9BrvmUqw1PvFOKiW05YtMDRfHa8mvMOgxkZZifwk4K3MJfAjLwa34Xeet5MhM435oVmyyKw9SYX3Mtz_yEgZSY_Nz7n1sByXeIg2rM4xpY8QSMnH9hb6rOK8TdpFHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83570" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات عنيفة تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83569" target="_blank">📅 06:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات البحرين مجددا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/83568" target="_blank">📅 06:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هجوم جديد على قطر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83567" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83566" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83565" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83564" target="_blank">📅 06:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-LMUysa1TjaTm3vZ4OtBvP-HmZhtkvhnNRPdu6KrvtAuwZa1gwVWqqrCOvOtx-efE8GLbDZ9HXlF6mRDwRvCuU3g67bdvhY2MpYDno_2yyOrZg5_OZc6kIVOe4n2pnPVfm5-c4axBD3PK-5mNBDbVks4jHefbcBQK-Rb2QjdB6hG21Gp6PbRtKyAKFWChUEV84ElpNYf6BC3dB6cRENPCqAXZ7orwAhL2Oj4mf6FwMLOEITQ0ODLE65zWVgtKj2kYL5uhJzwp2O5qtRYuKZCruBCcUnFvu-L54c9qP2pcwOghj8j6Mc9NdCG4hOK8H-XsXUYim9o35huePsFQnqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83563" target="_blank">📅 06:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc0nE1nbGnJBk_P2ideO0rvgjsOR_2TX8rzMtQqH5ieqc3uLIyBID7976-_lxdC0Xs86OCNXsNSh0Uo0cXHdgD1TloW0-eK-O1tMhSUa8U11ojGD9VVr0tVI0MJe_zfUl45lsTLRPvDYbO4rBLZCneJsCS3xUaIlEgixjEnBGAwSzhg4trKKCJAJnwqJ7B04xFFbmm0UZCFDju9F2fAc3K9cf3ZlKjxPzw06Xj9vA2xnduhjztDOSPjmAuI7B9vhmB2d8ws2JM7rko36huFhnRn-IA-YxE3PcZ7pU2TkBjyxcqYoyjXCVtueN9g0cJ7GGGpDbtWffKfrZCaV2x1LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83562" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDYh6qaGynJ8mq8i5KCrqXsAZpRRKhQ9BkNq35dTmL2SH2kBkcc6iQUGL4pRT985nuLtBLyuijyutVh6aPeQxqy-Qw2tpoMiuN6wMnBb_vY8FQOsWjM-lA9_1tGtp1v7cVvVP4OynksHYbne6h8FOzUXSoWO3VzM2tk7UrliqEpCyp6wwe60x31z-b27CNIxL0wWizR6ZdOkXRimSzT3TAzHjo5Qiue_48Keq1Z5wOoCGZCmhPFhHVJ3-0o_WpL-QjyEGME04O6Bo_lj_1-7NWPt0tM8PmYGzZ38fSXJUD7z4zcXHxzjmPZcVX5L3C3uLLIlIEPPvZMDtci0DdP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83561" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83560" target="_blank">📅 06:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
هجمات بطائرات مسيرة تابعة للجيش على مراكز دعم الجيش الأمريكي الإجرامي في الكويت.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83559" target="_blank">📅 06:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من القاعدة الأمريكية في أربيل بعد استهدافها بعدد من الطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83558" target="_blank">📅 06:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات في الدوحة</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83557" target="_blank">📅 06:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83556" target="_blank">📅 06:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83555" target="_blank">📅 06:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت تحاول الصد وسط انفجارات عنيفة وتساقط شظاياها على منازل المواطنين في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83554" target="_blank">📅 06:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة في أربيل بعد هجوم بأسراب من الطائرات المسيرة الإنتحارية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83553" target="_blank">📅 06:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpWquTerW2y0SQUFnOM7ICTwwwXir3RcJPPwPwI32h0xnVGbSMszhn_QvtLX4f4G5ZviscuQfGvUaI3yLmK2aYuLGxa-WPLDFOjw6ulqmp2UMjOfnzKKIXuh_rmpJwPnxJ_YyOP4NzoVAH9ZmZ-rd8aMW2EqEVW2D67UHe0_Q02CGw_e2ZVl1Iv_AytwQItPvPhKqnsT53Z0ZuohMBtPzAzUJO8sc2iMVMj8qaqBp7SVrzYjOaAwObw1jW8YgJbnH3IPRHB-FT4vIKGwbrfrLBXEoJKMLWHf0jf11yLc8iblw1KGzQAt3JcwVq0ju4aKvaCnRgdrWXoxnm8lRZbb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83552" target="_blank">📅 06:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83551" target="_blank">📅 06:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83549" target="_blank">📅 06:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباترويت في سماء أربيل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83548" target="_blank">📅 06:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83547" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83546" target="_blank">📅 05:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇷🇺
هجوم روسي واسع على ميناء أوديسا الاوكراني .</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83545" target="_blank">📅 05:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83542">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $   But park your ATCAM near Persian Gulf cost more</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83542" target="_blank">📅 05:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قطر تعلن اصابة مواطن نتيجة الصواريخ الاعتراضية الأمريكية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83541" target="_blank">📅 05:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
الدفاعات الجوية الكويتية حاليا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83540" target="_blank">📅 05:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من القصف الصاروخي الإيراني الذي طال القواعد الأمريكية في البحرين.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83539" target="_blank">📅 05:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي:
اليوم، في الساعة 9:40 مساءً بتوقيت الساحل الشرقي للولايات المتحدة (ET)، أنهت القيادة المركزية الأمريكية (CENTCOM) أحدث موجة كبيرة من الضربات ضد إيران.
شنت القوات الأمريكية، بما في ذلك الطائرات المقاتلة والطائرات المسيّرة والسفن الحربية، ضربات دقيقة استهدفت عشرات الأهداف العسكرية الإيرانية، مثل مواقع المراقبة الساحلية والدفاع الجوي، والبنية التحتية اللوجستية العسكرية، والقدرات البحرية.
وتمثل هذه الليلة السادسة على التوالي من الضربات الأمريكية ضد إيران.
وبناءً على توجيهات القائد الأعلى للقوات المسلحة، تواصل القيادة المركزية الأمريكية إضعاف القدرات العسكرية الإيرانية ومحاسبة إيران على الهجمات الأخيرة التي استهدفت السفن التجارية.
وينتشر أكثر من 50 ألف عسكري أمريكي في أنحاء الشرق الأوسط، وهم في حالة يقظة وجاهزية قتالية كاملة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83538" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpMMeC2OlDi562QyXt_7JUfYs9ru2t5dL71Mkl68TAGBM3ytZklSLYQSM885RUehGkzh-x1ifYh7u2QSEXFXRzw6EVMbXskyrYhCRdAsmWzcQqCm0rmrqXjvFSsXMKUSMovP0THrG4GgN55PtFJebp_YcNywwiCNOcwuuB5Z4gX2kCSvgDzXKBXMws4nDVIS3iqiEGhNXora74eCNV6fvPTtF7SW8nR9klIM9h4b8if02fOxFYhXlAvf6mOJAtLvZc96wONQVhdveUTkK2E8c2NcoS8OXJ3N1ADwd-OWSYdb9FyDxYAbZG2Ci5jnL_Cgq6rx30JG8ZTFIkp4HJK79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83537" target="_blank">📅 05:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت ثلاثة صواريخ أرض-جو من طراز MIM-104F باتجاه الصاروخ الباليستي، لكنها فشلت جميعها في اعتراضه. يُذكر أن البحرين لا تمتلك منظومة ثاد المضادة للصواريخ الباليستية، مما يجعلها عُرضة لمزيد من هجمات الصواريخ الباليستية التي يشنها الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83536" target="_blank">📅 05:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVz5Je8F8SgYpr0vDROJw6JzJ9ngN48IfJPcBDO32FCxuRO5HkGz5xNG3mJEY9v5rsTbroK-XDI7rXebPSqXVXBCpcIJEG-2vBbopxqpAW43qw8FVS4k6ACKN7ngA1f9JK8kXCEw3FI9PTwKiPJfJfLGpjGm_I61kQ74fV0WCxgEKSgfAWeHnajJ7UAYljn-k0IALpoABGcF8PwbghT6Hu9gwkgrLL6jGzvNns9PHeGqNTUNfpAVG8U6M5HahGBP5RKWbeJoaFD4Mwx1gFvapPUjFeoILO1MwDzURzxYgStAbPK49IbGO5BmdC-aEaHn9Exz0Gv13m5i42ION_GqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $
But park your ATCAM near
Persian Gulf
cost more</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83535" target="_blank">📅 05:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
😆
ترامب: يجب سحب تراخيص القنوات التلفزيونية التي لا تغطي الخطابات</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83534" target="_blank">📅 04:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83533" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇷🇺
🇮🇷
🇨🇳
🇰🇵
🇺🇸
ترامب: يمتلك خصوم الولايات المتحدة، بمن فيهم روسيا والصين وإيران وكوريا الشمالية، القدرة على اختراق البنية التحتية للانتخابات الأمريكية.   لدينا نظام انتخابي منهار تماما ولا يمكن لأي شخص الدفاع عن سلامته.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83532" target="_blank">📅 04:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏ترامب: الصين حرضت صحفيين على كتابة تقارير ضدي.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83531" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83528">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYVMooN57Pq4fgLT8iIHIrjvNJoLP99FwmEJ18bhTKl_Ybfgy6N4qTSmAwAob70-FnriyCCJvMtdOiAqA9a1iPD1n8xZx4SwD6gqyKayjYlBjIMu8BSZBnEsw-2T-nuBWv5d0XkSZ3fzcs9qMG-cmz1YjF-0TiRF9xvBfMUwp_tBszvhCXknr9TA4BJzNO4nGG7WXOAYEQedVUR0MwYcBBPPiDyBlM3XE0MVj_ktvCwNZcsVfs1yVgjGLdOC9Ji08qNHeKQPHApjXJgg10Z1hO6Idbk30omyhq1w9lnkQwtcKkJlJZTNfTgcvivgh-tTr7DJqreX3tS62RF1-o7q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2e4c52cf.mp4?token=dbyfNN0jgFRawW0uXYbVlX8UwBJm-mBNM9siGaq9D9PrsE27PXs6n7D6EqXl5HZK5G6cMOipiDVcngxATnDt6TpVKSS_MHfKaXyfqheDjfy-_vuqQtQJ3DGrZTxOTVbKnq2O-PJhGz4Fb--lcOl7sB2CWX5gM4cnutgmqmjVYtt3a3e4f8aQmg91kWkBW6sxOcSjoUD5DYEy6kINgO5XAoZeGtR5tkl1A-JfmH_lrcdZ1FpeHUPjuwgNmz0xYpfYo3feDKiAad40rK7HWza89K1JF1jUyI29pZEGh0dHrH3SaQoGm6g_387pjrv7eUR8x1oe6TsZc8Ff_GRFNCN0GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2e4c52cf.mp4?token=dbyfNN0jgFRawW0uXYbVlX8UwBJm-mBNM9siGaq9D9PrsE27PXs6n7D6EqXl5HZK5G6cMOipiDVcngxATnDt6TpVKSS_MHfKaXyfqheDjfy-_vuqQtQJ3DGrZTxOTVbKnq2O-PJhGz4Fb--lcOl7sB2CWX5gM4cnutgmqmjVYtt3a3e4f8aQmg91kWkBW6sxOcSjoUD5DYEy6kINgO5XAoZeGtR5tkl1A-JfmH_lrcdZ1FpeHUPjuwgNmz0xYpfYo3feDKiAad40rK7HWza89K1JF1jUyI29pZEGh0dHrH3SaQoGm6g_387pjrv7eUR8x1oe6TsZc8Ff_GRFNCN0GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83528" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83527">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6f327901.mp4?token=u1tSrWfbfkOLXgc4P7JNiOVGugOcweufNqvCi__Uvb_1Dsb1-YF6t-6PYj4rsvYOGUYOy6Nez0M8mdht02dANOpH38WL2JMuy1OwvEXURZI4E879TqotMzIElS-PaCBqq6I7wKZVTP2co8QQfkKxJN6J97dCCr-epw0we50uDgz-gnS33SZ_zok_myzLWHOkJQgSkfoyAA503EuAxpnGC4ME8vGE3abErDAfZqxWcFBjt4kBEv_uIEwI1tl2AYehCcmBsRIfGaGpjQtUul6upQZe-Et0IqXDgut8m3l0MLKofctFXXMe8lSacN2EMGAJZ1oLOnDbubRnEF68wmXhRWB2sMa4aMCZPQVxLzBGvWXEvHY7NPZnKix_K92KT76JDbdNSJwnW2RqZtLatDWUvxaFnqWqRsUS2Qb0Gr1woLAiIIZpCw0iZ-izLp9ejmxg-JLHNZeZU8XqrFInrn-DPPhIrt6sb_hqE9hNVcn29eCpsWOzp6SRLizLlT-_kZDJcGatAWIZWBPE-Od5tgO3waT88YY5CcwNOsZ501Sq9TLY3rLl6rtKehQRgTf8omwTbidQENRXSh4tHGdgFvw_0jN3MQcZ0SkK-qE8glf-FlWz6WuG4HsyVvSRNXqBvPheYpOO5k3WVfct1RvFQaELqODpPDlINqhXNgwLYXi8-t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6f327901.mp4?token=u1tSrWfbfkOLXgc4P7JNiOVGugOcweufNqvCi__Uvb_1Dsb1-YF6t-6PYj4rsvYOGUYOy6Nez0M8mdht02dANOpH38WL2JMuy1OwvEXURZI4E879TqotMzIElS-PaCBqq6I7wKZVTP2co8QQfkKxJN6J97dCCr-epw0we50uDgz-gnS33SZ_zok_myzLWHOkJQgSkfoyAA503EuAxpnGC4ME8vGE3abErDAfZqxWcFBjt4kBEv_uIEwI1tl2AYehCcmBsRIfGaGpjQtUul6upQZe-Et0IqXDgut8m3l0MLKofctFXXMe8lSacN2EMGAJZ1oLOnDbubRnEF68wmXhRWB2sMa4aMCZPQVxLzBGvWXEvHY7NPZnKix_K92KT76JDbdNSJwnW2RqZtLatDWUvxaFnqWqRsUS2Qb0Gr1woLAiIIZpCw0iZ-izLp9ejmxg-JLHNZeZU8XqrFInrn-DPPhIrt6sb_hqE9hNVcn29eCpsWOzp6SRLizLlT-_kZDJcGatAWIZWBPE-Od5tgO3waT88YY5CcwNOsZ501Sq9TLY3rLl6rtKehQRgTf8omwTbidQENRXSh4tHGdgFvw_0jN3MQcZ0SkK-qE8glf-FlWz6WuG4HsyVvSRNXqBvPheYpOO5k3WVfct1RvFQaELqODpPDlINqhXNgwLYXi8-t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83527" target="_blank">📅 04:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83526">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تدمير منطومة باترويت في قاعدة أمريكية بالقرب من مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/83526" target="_blank">📅 04:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83525">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تدمير منطومة باترويت في قاعدة أمريكية بالقرب من مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83525" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83524">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83524" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83523" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83522">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83522" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83521">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب بشأن التدخل الصيني المزعوم في عام 2019: "لقد ركزوا على تقويض الثقة في الرئيس الأمريكي. أرادوا فقط أن يظهروا وكأن رئيسكم لم يكن على قدر كبير من الكفاءة، بينما في الواقع قام رئيسكم بعمل رائع."</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83521" target="_blank">📅 04:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83520">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097e67d111.mp4?token=X-oy0Zl8PTaK6CqOTWqh7wibN2sSJpEe--Go8Seg3rSOHtsd6zjXTSx1osLWIGSJeShi9riV562tVxmqz-iplganUV2r6uzDx1Eoy6l23MvS8vg4CYe_euehl0ccoZhWyZOAiFvRSOgkAv0pFNxJTe8iSASh3bgeHG7SD_jpaWKtr-hxEIUwwLdsAsDB6Yk_vvxEalyoSz3aQvIGrf0nOHeKEbjqJt4cLB3Sqg5d26BYbIVRpWFEqXTcsq_eQEhlHETkW6XIYVm5iBdFQjen36h_0UbGZFdggvm_mRiTjZkzaBvyUd_ar9KzkUVUzqw35td6MkdDr3PgbkgT9bZP4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097e67d111.mp4?token=X-oy0Zl8PTaK6CqOTWqh7wibN2sSJpEe--Go8Seg3rSOHtsd6zjXTSx1osLWIGSJeShi9riV562tVxmqz-iplganUV2r6uzDx1Eoy6l23MvS8vg4CYe_euehl0ccoZhWyZOAiFvRSOgkAv0pFNxJTe8iSASh3bgeHG7SD_jpaWKtr-hxEIUwwLdsAsDB6Yk_vvxEalyoSz3aQvIGrf0nOHeKEbjqJt4cLB3Sqg5d26BYbIVRpWFEqXTcsq_eQEhlHETkW6XIYVm5iBdFQjen36h_0UbGZFdggvm_mRiTjZkzaBvyUd_ar9KzkUVUzqw35td6MkdDr3PgbkgT9bZP4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏تم شراء بيانات عشرات الملايين من الناخبين في 18 ولاية أو سرقتها أو اختراقها من قبل الصين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83520" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83519">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامب: ‏يا إلهي، من كان الرئيس عندما خدعتنا الصين بهذه الطريقة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83519" target="_blank">📅 04:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83518">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13acd514fa.mp4?token=eQudq3p5ZstHfQD_fjgJOkezBy8VriwbM0FV0q4FgufuAuadcBJWZNoubiXTjQhq9ElStlMu7Qr3tjl1L4zgDrzkU2eN6v_0o0birT8hmkt4ekMfe4R1-r7l-PpVHrO3hg--lIfvKShEOUa1qbTDZY3cY6SiU6AeHYdKrlcMSXYwXoXX_DZ7Dtk5Ko589-nb-mTlVWRY4V9Bbk76KDtstZO9MiQJXgCNlaAXYm9M5XYD_wiYMGYZ3tbjae5B6tUo7sPehrTXSaIF8kA_KoMRONAUnytMvK180M4fMC_Vcg5rjgxR03_MRIgZCsLt2YSg4HZSvTd99IgHi_p1sv8b-xI3LBm7L-9DckGQIzy5DMO8hs0k2Qncn_NvMfea1Wyv2QyUY4iLD9dT-kcQdshcKMBcZUPZHFkmBTCob_xY1zpGUEyfCvDI82uJmcm9OKimFDc2HwUeYMO_MBYY-m0fMbky4zHeodODDyGQvlI3Ug9uDoBppBW7cd3zKBrNnsWo5Yi2pWNj4L_6q0mQcGCSPxcWRaGbEY-9YiE3-5EbscGAtYZKo_cWNPj0QdWpsad-Fy6Ogj7oXqC1xjZplHSGM6xvkftAvtHXGGp7bIxBrUihfzpWmPJdcYYD7h2hBJZVflB6DrNK4Y6zBWnN8XKsLt58U34-prF2dnv06cZqXmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13acd514fa.mp4?token=eQudq3p5ZstHfQD_fjgJOkezBy8VriwbM0FV0q4FgufuAuadcBJWZNoubiXTjQhq9ElStlMu7Qr3tjl1L4zgDrzkU2eN6v_0o0birT8hmkt4ekMfe4R1-r7l-PpVHrO3hg--lIfvKShEOUa1qbTDZY3cY6SiU6AeHYdKrlcMSXYwXoXX_DZ7Dtk5Ko589-nb-mTlVWRY4V9Bbk76KDtstZO9MiQJXgCNlaAXYm9M5XYD_wiYMGYZ3tbjae5B6tUo7sPehrTXSaIF8kA_KoMRONAUnytMvK180M4fMC_Vcg5rjgxR03_MRIgZCsLt2YSg4HZSvTd99IgHi_p1sv8b-xI3LBm7L-9DckGQIzy5DMO8hs0k2Qncn_NvMfea1Wyv2QyUY4iLD9dT-kcQdshcKMBcZUPZHFkmBTCob_xY1zpGUEyfCvDI82uJmcm9OKimFDc2HwUeYMO_MBYY-m0fMbky4zHeodODDyGQvlI3Ug9uDoBppBW7cd3zKBrNnsWo5Yi2pWNj4L_6q0mQcGCSPxcWRaGbEY-9YiE3-5EbscGAtYZKo_cWNPj0QdWpsad-Fy6Ogj7oXqC1xjZplHSGM6xvkftAvtHXGGp7bIxBrUihfzpWmPJdcYYD7h2hBJZVflB6DrNK4Y6zBWnN8XKsLt58U34-prF2dnv06cZqXmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سينشر تقييمات أمريكية سرية تُظهر أن أنظمة فرز الأصوات عرضة للاختراق من قبل الصين وروسيا.  ‏الصين نفذت أكبر اختراق معروف لبيانات الانتخابات بدءاً من دورة عام 2020.  ‏الصين حصلت على 220 مليون سجل للناخبين الأمريكيين.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83518" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83517">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSVZQZpu60Qjryat-7-6bI10SoT2fqKBAvPo-k_gYnD72usGIX0zAEzcfXv_N4JoAiXwNuDLfTSSTiabiL4ZHgWt6ptGjb_hj3zPt2KfQ1PtR9cSkcfXj0gFMun8vvxw-xUij3Vj8A6sb0Imqq0kgjdrX2FQmTYmDVwUzbE3Ng-6_19MQrfB6XSf7d2HJ9KrSXWpSYvhaq1OJUwjlJOy6lQsYmknrGDBM0G5L1SjGJ5LW_KanUURgF00_dPfIxDLoNshZ0RoYUskhzh13BJiYIYBpeMUKGNLu1D_-toEojL94GUOIwacJ4clZ1HvaTnU58WgMo0vl_5xYpydYVp3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البيت الأبيض ينشر : الأخبار الكاذبة، سي إن إن عدو الشعب!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83517" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nECx7C1xzU1gvkjHV6Sqib2WBo2iezBsygcXNlOO5QR13pzzH8uYGv7VeKr6x_Rg7cXrW7dVu_lvKMlM6aO4zFuYUSPU36WrmeoWZJ0QgI8Qb1_RZYJqGoJ91cKgesn-j7_xOnnFYxobCn-9nry3XiuQtleoCSxYrcz7VfucF-33LMXYSn5ws1g2PUjr4a2WjAUL4sHIF5TGwWJ2zrVZagEV7zzmW3mPmPs8VPWD6Jp-Ugz7ej3kH-0Mxp1GImqm-GQTfutiJYtLgmaH4TjuMZtVRNSCEo4gxWAZBiqdVAwjlpR_LEjyZMnz9v3TLsaUGN_T-uS5i9t-3qCMOGA9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية تظهر تعرض مستودعات أخرى لهجوم إيراني جديد في الكويت.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83516" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات في ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83515" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a8b9b061.mp4?token=kgzKQ0ASudsCdjJxTymkHJYQbTR1b2VkTAqJdUX3-C7o54bITzv14oPOpHWNlIhtcgw6XZegg3nJ1cun52wOtS3vDjTkhzlU05WC0qTyJ7PeNetOXMoghE6Q5JeBuT9l1fW3oE6XZOL7NPCLhXaWAi_s-HlpKw8wKSlNsPs-DfA7Ru9EfAmxPdSmFCe8LIcbRSvSYNQgL6Ywjs5s6tXpbZuv0wqVo1aIE_hfh20K5DfDLl1Ep0jHv8HKDMpe285LLJ83AET16B6DRCYCVcn2ez2P6BDiwptJE7UYtIigFtMdt7WQpi9wslpAbgpPKhvkxVENz4mHVV6t51OGVO9D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a8b9b061.mp4?token=kgzKQ0ASudsCdjJxTymkHJYQbTR1b2VkTAqJdUX3-C7o54bITzv14oPOpHWNlIhtcgw6XZegg3nJ1cun52wOtS3vDjTkhzlU05WC0qTyJ7PeNetOXMoghE6Q5JeBuT9l1fW3oE6XZOL7NPCLhXaWAi_s-HlpKw8wKSlNsPs-DfA7Ru9EfAmxPdSmFCe8LIcbRSvSYNQgL6Ywjs5s6tXpbZuv0wqVo1aIE_hfh20K5DfDLl1Ep0jHv8HKDMpe285LLJ83AET16B6DRCYCVcn2ez2P6BDiwptJE7UYtIigFtMdt7WQpi9wslpAbgpPKhvkxVENz4mHVV6t51OGVO9D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب، بصوت أجش، يكافح لقراءة جهاز التلقين.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83512" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامب، بصوت أجش، يكافح لقراءة جهاز التلقين.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83511" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98986b4537.mp4?token=CFIF_I0LXSdLBPSfQuf62KmDoJ3X_uBxEX3s3Bhp5QEgqT5Dx29a-M28y-FPlOwDiTr7kVuHMAGUQoL3C_RVtcCBuO9hMWOCok-AHz23zmEAniHS5uUHJFNGsU41bwNLWWvGHycU6cGJ7lFQmrrCRvL9Y-M2RPwKrOCqCwA_6CqMyVVXyGWdT6lwW3763FFOhM3Hzi82zuV5c3_2rRY7hHzRk-UhMVGFVlvqySxnyjeBI5lk_p4RSSO1e2GIpC-YFrgq4Ncroi8kNLih3txnVubtt89Sg0zafi0ZWiSMysMLfg5GQXxPSkpnmsaRYkcDxStIjbB7Td5meP9WYAEsYRx3wmgICNLELoVWFI-rY5dYykTDkPqc10AIpeAkQIDiCGewQ1cOMZNABZN5ZVzerceASb2rPM7E27P4u0mO0qbbj_KHH2jU-47z-lkU_ko7LfJ3YJYxjhTp0spPRFCc1S3CnQVo7XIDSCosEGHdadeMRrcJfyx4-OUWA3Y-ODFBy653rSyxQ0wdZOFOwA3C8UkedQKZM0mqFi0waIfqdQ2_1DLVONxuxvY1QkSweP53319B8x1WjB2EWkGx4XhVPORTIWMFhqi8usDiizEndN_2omM_fCTdR1akfbuoWaKROK9Dtngqjn679AkBK2BZftdSkSHEZ0ztluCe015HjuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98986b4537.mp4?token=CFIF_I0LXSdLBPSfQuf62KmDoJ3X_uBxEX3s3Bhp5QEgqT5Dx29a-M28y-FPlOwDiTr7kVuHMAGUQoL3C_RVtcCBuO9hMWOCok-AHz23zmEAniHS5uUHJFNGsU41bwNLWWvGHycU6cGJ7lFQmrrCRvL9Y-M2RPwKrOCqCwA_6CqMyVVXyGWdT6lwW3763FFOhM3Hzi82zuV5c3_2rRY7hHzRk-UhMVGFVlvqySxnyjeBI5lk_p4RSSO1e2GIpC-YFrgq4Ncroi8kNLih3txnVubtt89Sg0zafi0ZWiSMysMLfg5GQXxPSkpnmsaRYkcDxStIjbB7Td5meP9WYAEsYRx3wmgICNLELoVWFI-rY5dYykTDkPqc10AIpeAkQIDiCGewQ1cOMZNABZN5ZVzerceASb2rPM7E27P4u0mO0qbbj_KHH2jU-47z-lkU_ko7LfJ3YJYxjhTp0spPRFCc1S3CnQVo7XIDSCosEGHdadeMRrcJfyx4-OUWA3Y-ODFBy653rSyxQ0wdZOFOwA3C8UkedQKZM0mqFi0waIfqdQ2_1DLVONxuxvY1QkSweP53319B8x1WjB2EWkGx4XhVPORTIWMFhqi8usDiizEndN_2omM_fCTdR1akfbuoWaKROK9Dtngqjn679AkBK2BZftdSkSHEZ0ztluCe015HjuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتحدث عن حالة البلاد قبل عامين: "كان لدينا متحولون جنسياً للجميع"</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83510" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c351174ca.mp4?token=sLOlcQZbFvLvMibCO3O4URtSP-bUOVQXJSZXvFtmXCdyHeZ_0UBszgul7RR0_b-4Xl52uHRKjrkxARTS5lKCWZ_1le4Yf_mm1IodjHha91gu_yvA9S9cLnwO7axXIiTbXuB4bantL40unq1VIdUy6nSlwqKO006L2ZZrRidt5dGv4uPiR8piayqrEvKZHoKF9yh1E52DaqP7nHCBDBckA-VEmfpW7Yjv8IVLqt3U7ovNIne2QVMoFsUj53ZsiSZAYxsUBMh-gK921gR4lgCSE7xNyIGsc977kjvhK6F9k9mVqfBLtwbEAY-Ha9gkHFo_jgw2alUT-7VDQDyug3dVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c351174ca.mp4?token=sLOlcQZbFvLvMibCO3O4URtSP-bUOVQXJSZXvFtmXCdyHeZ_0UBszgul7RR0_b-4Xl52uHRKjrkxARTS5lKCWZ_1le4Yf_mm1IodjHha91gu_yvA9S9cLnwO7axXIiTbXuB4bantL40unq1VIdUy6nSlwqKO006L2ZZrRidt5dGv4uPiR8piayqrEvKZHoKF9yh1E52DaqP7nHCBDBckA-VEmfpW7Yjv8IVLqt3U7ovNIne2QVMoFsUj53ZsiSZAYxsUBMh-gK921gR4lgCSE7xNyIGsc977kjvhK6F9k9mVqfBLtwbEAY-Ha9gkHFo_jgw2alUT-7VDQDyug3dVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتحدث عن حالة البلاد قبل عامين: "كان لدينا متحولون جنسياً للجميع"</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83509" target="_blank">📅 04:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏ترامب: الولايات المتحدة الآن الدولة الأكثر جذبا بالعالم
‌‏كان العالم بأسره يسخر منا كأمة، ولكن ليس بعد الآن.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83508" target="_blank">📅 04:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
🇹🇷
🇮🇷
أكسيوس:
خلال زيارة ترامب إلى أنقرة، حذرت أجهزة الاستخبارات الإسرائيلية الولايات المتحدة من أن مسؤولًا إيرانيًا قد ناقش محاولة لاغتيال الرئيس أثناء وجوده في تركيا.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83507" target="_blank">📅 04:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83506" target="_blank">📅 04:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=SE9uhL2ad58S2LOdMpBrR9UiopHK4n1rbC1MXzPUVBCYajUc932Snwv0zcU1ni2KWmdjnxtjS6mmTGQlQJ6AGcJ92jkwcRL93ufyIM8HqsFHtx-lKumHo60mxUzm2G0GQq3aUxMxX-QAZLQm0w3MRBlm4yNrBVelrtLJY5A5DjMNda5waHyoazS0gFCAeJ0eAHugXMNvmSoRvW0CnbJ31v0ctivlWRWNt3H0i_nBG3Y_UesEVrzMVqDTXCJWeNuY3wQbVB_50MmtF6icc0ilQW6RKhTZko0guQbP89pRm43V3lBB9JAq4YPLETfJf6lo0dA4jg2rXGuC0YmGIOWkQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=SE9uhL2ad58S2LOdMpBrR9UiopHK4n1rbC1MXzPUVBCYajUc932Snwv0zcU1ni2KWmdjnxtjS6mmTGQlQJ6AGcJ92jkwcRL93ufyIM8HqsFHtx-lKumHo60mxUzm2G0GQq3aUxMxX-QAZLQm0w3MRBlm4yNrBVelrtLJY5A5DjMNda5waHyoazS0gFCAeJ0eAHugXMNvmSoRvW0CnbJ31v0ctivlWRWNt3H0i_nBG3Y_UesEVrzMVqDTXCJWeNuY3wQbVB_50MmtF6icc0ilQW6RKhTZko0guQbP89pRm43V3lBB9JAq4YPLETfJf6lo0dA4jg2rXGuC0YmGIOWkQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83505" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcC9zTUvIgt4BApg4-XIyMTA4wgly2fXLkr8wx_92_yPulUMhgHyXkltU8U1rFCFNUCaVg3sJMeO16yJAHtcoybkh71AJYpxTEMgAp7cxtpEPSrhJwHSbWW7ccmEyxTGL7jcZ6ojCN6oU_ywoaVMnn3jb3_SxGAHOxQE4Dr4i0MTpvB8FHQTQ207o5HBbIuNN2piNTOaRg9mrKTU_NLUDStg5-v3d6B8lcCViwvx1uq6gYItae5r5a2HynLIDvbr5pMoFmlnL0qgMLSN9mtF9_78VjSiD0ZaDdZXyG_-I3juqReqUzeWKgg8IwvhkuohxAKwIRs8UFOAKkSLHGF9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أبناء مدينة أم قصر يرصدون النيران المشتعلة في المعدات العسكرية ومنصات الصواريخ المتنقلة الأمريكية على الأراضي الكويتية بعد دكها بالصواريخ والمسيرات الإيرانية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83504" target="_blank">📅 04:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK029t3cZYbJiBYSY4-zFtzAbwDn778Yz7dVurviPE1oTJOmwQt7A56YXhxD9jp2B9GBvTAJv8enYVFjMQWuJW-7Gojml_MvAU54DKuTpPcSGd2cJNb86ImMhCTw74BuKwOCILzNQeUtDL2xSSSkkQ7mOaMLmQ54GEjYS6j5W_EUAvRIX0IXy2JMU6tPO6l0TMpo26orZZAk-e62CX5SVdi1FIdeqbscUeydoElQrOcpS866TOJlohvPMnLBzB2ngpa_U5NCIogG0BDTTSycPK8x8fGPnsCG9O1De11VP_2hVu9vQhj1lIAz6clZPwqsUMluOMy_oS1OuINDVXTGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83503" target="_blank">📅 04:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إستشهاد 2 وإصابة 4 مدنيين جراء العدوان على أحد الجسور في بندرعباس كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83502" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83501" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83500" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83499" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83498" target="_blank">📅 03:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQPHXIgnPQ2mgRnesk_ioHD-C-IYgcOnpx-1tEGWahpwpBC0iFt4U0qw0qyTMxDN9n8vITTlXUuaiphJxbQUsSy_rlDspbtcefQaK6sgkFUnPkAELulS5MVX0rxCoZ1UU7pNQ33Awu4Jq0BO6RwNQio3Hze5FNSok1CdHAlVPeEYgkCMsItH2EgQtLdxk-KOL0-X7nt0VxaoWSp4aU-lqYeIY2Aa1HdlWbmTZibWnuzEsnzax2Hy7ok0ne1ycqyTAxnHo1AKwuY7tZfPiUO_SKSsgZAqSZA7Jf_Y84u0LVZDAva8FH-PhXaPv1TrDxCi6n0NDws01L5UOlRRdpmh5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83497" target="_blank">📅 03:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8105b22245.mp4?token=L1_u3pLpQvtvR9PXIeBnI6jjG7pU5fO8VmSh89R448emesNIqlLzTzSvfkbzxb0zonvm-pFJvwSWMWZDMS3cFvUYZIQRoFI-uJtePddwo9wcO2TzFi4BBOFcvzJcsrnTIs3bjbgfDtCDi63PcvS07OijfG3LsHSgce99OLhUV-2esIJAmIU-fLWYYyjEcwhzDSsICyDFNjmsTHklRWJBQuZUWpm5JfkPMFFuMxT1EKzucqb8fgjVARERXDlRp8TEd6kpo-z7P8P0HgenTevknb-cMtM5kUIs4YS8uWcEr9ZHqFx3BnKI0foJUHWf6fqcg4pMmla57bA7ZOxgCkcrLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8105b22245.mp4?token=L1_u3pLpQvtvR9PXIeBnI6jjG7pU5fO8VmSh89R448emesNIqlLzTzSvfkbzxb0zonvm-pFJvwSWMWZDMS3cFvUYZIQRoFI-uJtePddwo9wcO2TzFi4BBOFcvzJcsrnTIs3bjbgfDtCDi63PcvS07OijfG3LsHSgce99OLhUV-2esIJAmIU-fLWYYyjEcwhzDSsICyDFNjmsTHklRWJBQuZUWpm5JfkPMFFuMxT1EKzucqb8fgjVARERXDlRp8TEd6kpo-z7P8P0HgenTevknb-cMtM5kUIs4YS8uWcEr9ZHqFx3BnKI0foJUHWf6fqcg4pMmla57bA7ZOxgCkcrLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83496" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83495" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=t7mGc-9ehZm7H3Xk93pJ5HgeBH1uQypK8OrTbUl9O17IDBOOGGIHOuYCpe4Pn8u8Xa9MfeYM4yYNaflb_5RiJtA6ztTQE02ZE_s0CfgGHWXunMdIWxuhuh8FRf3Syvy_r64kpreI1KsXR3vDBCvOiMQECkujWimVO6yfNETJujQh-iEVTjX47lum_PfJzFIPImbkRrb5aIluGTt3ASw8eLEdMG7El5OdO3FW_YJUX5N1xYlT531VOKwGexLHsCxSkViIVlEx8yu32OQ2Bqd9TGpBMWetWIk4uEwyecoyKsyRG6ebr8BO91O-YzMjtivQnPLZGNmWvamWjRp853AIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=t7mGc-9ehZm7H3Xk93pJ5HgeBH1uQypK8OrTbUl9O17IDBOOGGIHOuYCpe4Pn8u8Xa9MfeYM4yYNaflb_5RiJtA6ztTQE02ZE_s0CfgGHWXunMdIWxuhuh8FRf3Syvy_r64kpreI1KsXR3vDBCvOiMQECkujWimVO6yfNETJujQh-iEVTjX47lum_PfJzFIPImbkRrb5aIluGTt3ASw8eLEdMG7El5OdO3FW_YJUX5N1xYlT531VOKwGexLHsCxSkViIVlEx8yu32OQ2Bqd9TGpBMWetWIk4uEwyecoyKsyRG6ebr8BO91O-YzMjtivQnPLZGNmWvamWjRp853AIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ أخرى تنطلق من إيران صوب القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83494" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=pN--J2zvW-UvjVZLXyIoWMuBkUQg9buscTTuMfgZsuBFMSVjhEmztrekcHBWqO8Ikd_I-bxGrvCwq4oody_SHSAcDPj4e5XNIw-NyCc9rDA7fayLG_vU_oTLFUUTkbMwsJw87iSooI89csvvaKjUk04wErhl4yYRehgat3s0BDVgLJB5h8QzlGJ9jnkjnZSZCn3bQvq11V_63adPvdOkrJKVrat5NNUoZPRXR5dY3mQW4N_YOBwaNzUYPoqQ8zj2yRadSR_Y4MHE9ENL5quEcXNsP5mLqf1TtWAtTzJ5R2Ys66gT7mlmurgSsq2Kca9SycsqPBSYQnqzQF2_Wm9zBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=pN--J2zvW-UvjVZLXyIoWMuBkUQg9buscTTuMfgZsuBFMSVjhEmztrekcHBWqO8Ikd_I-bxGrvCwq4oody_SHSAcDPj4e5XNIw-NyCc9rDA7fayLG_vU_oTLFUUTkbMwsJw87iSooI89csvvaKjUk04wErhl4yYRehgat3s0BDVgLJB5h8QzlGJ9jnkjnZSZCn3bQvq11V_63adPvdOkrJKVrat5NNUoZPRXR5dY3mQW4N_YOBwaNzUYPoqQ8zj2yRadSR_Y4MHE9ENL5quEcXNsP5mLqf1TtWAtTzJ5R2Ys66gT7mlmurgSsq2Kca9SycsqPBSYQnqzQF2_Wm9zBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83493" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=VxtQID1c_mDwxPmefJzllZ9Y-3-UOb2VOhrsbyEws01BdxKRp_mCvr7jFR1_9At3Mm9p99iNiO1jt77hmMDpk_2nAWMAS1uArYw7u-DSslCZxXoz789j8BlAYwRa-TsKYttVU89mOkma4b_PoPOrb8ncBdRRQSVyRib4X_1UtjLrt1Cs6NSKzEg_MK7mVbho3wNAMMGtW_Igz_oPWK_6cZz0C-jtk5ZO8PZ80J-TiXBAp1frt6FiE_IUv0Rc_1hDRAA9wBWy2x5HBVOpCgKvRBoyB0ZdMjjIX4VhD-yv1QZ6ZaqOmZRZEKOcS8_Ej2tg7Q-U0jaUQQrksJuYPV24yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=VxtQID1c_mDwxPmefJzllZ9Y-3-UOb2VOhrsbyEws01BdxKRp_mCvr7jFR1_9At3Mm9p99iNiO1jt77hmMDpk_2nAWMAS1uArYw7u-DSslCZxXoz789j8BlAYwRa-TsKYttVU89mOkma4b_PoPOrb8ncBdRRQSVyRib4X_1UtjLrt1Cs6NSKzEg_MK7mVbho3wNAMMGtW_Igz_oPWK_6cZz0C-jtk5ZO8PZ80J-TiXBAp1frt6FiE_IUv0Rc_1hDRAA9wBWy2x5HBVOpCgKvRBoyB0ZdMjjIX4VhD-yv1QZ6ZaqOmZRZEKOcS8_Ej2tg7Q-U0jaUQQrksJuYPV24yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة بمنطقة الجهراء في الكويت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83492" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
