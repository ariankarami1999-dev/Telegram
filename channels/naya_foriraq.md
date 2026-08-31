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
<img src="https://cdn4.telesco.pe/file/q-amwDr7I5e1BWbrQdeoayd5MPzZyL29cczO1Znh6xIrpOiIftH2bRIj45dEO16e99qw02d_z3efx4ztwVr97JymO3i_tPzDUhmUlZIBjga6aiSIxHotRUk8PcVSSJBYMbLx3erhEGms23W-lvnHVQnnoVW1PS2jL6CUjuccGCZtuF1KJCu5Tedp0abNBxTVmA329IDnblmUSlA9VAql-g3RUH_qrLaOMApwIYVGKD4qMmY13W-UnBYe0zpmEuDxpyASwZJVndLlpcwfLogFizFR_Imv66utTC3QM1huSHUZOOWJHufoEss6EUFyN0uBgU1HdC8wBbET74hr9qAo4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-88896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترمب فحص خطة لهجمات محدودة ضد إيران في محيط مضيق هرمز</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/88896" target="_blank">📅 20:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇸🇾
اشتباكات مسلحة بين عصابات الجولاني والفصائل الدرزية عند اطراف محافظة السويداء السورية.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/naya_foriraq/88894" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ca3414a6.mp4?token=qrJ2TDRXZ6kVzdkIERtJr8bTDSsSW8O6gMtPT6x1ZUaH4siYPwimoPse-6BfahlfI-VbOBZKpq1kYyHTKd0dZTuBthu9ZPavow5yrSIM2q3zGfKNQ8fPlF0-tCG7U86XQ-rfm_xKeigve0hxuGX4pb5IIBt-GtgxphUjYfACTWhI-qY6GPRldSYrvxykQ8-_2__R3G7niu-FNcLSwyccuD8bC50R1WZLEhLQu2Ek1jUkc0aNfKcAujLLr7LHSA46A6r2PCTMmoJ8GfwHVweqDi0QiNlMS3m7Q9jkaQjWSOgfwNwOagFffuAm6f_SWDWWSUbn6XjV6P7VkjVa8aZbRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ca3414a6.mp4?token=qrJ2TDRXZ6kVzdkIERtJr8bTDSsSW8O6gMtPT6x1ZUaH4siYPwimoPse-6BfahlfI-VbOBZKpq1kYyHTKd0dZTuBthu9ZPavow5yrSIM2q3zGfKNQ8fPlF0-tCG7U86XQ-rfm_xKeigve0hxuGX4pb5IIBt-GtgxphUjYfACTWhI-qY6GPRldSYrvxykQ8-_2__R3G7niu-FNcLSwyccuD8bC50R1WZLEhLQu2Ek1jUkc0aNfKcAujLLr7LHSA46A6r2PCTMmoJ8GfwHVweqDi0QiNlMS3m7Q9jkaQjWSOgfwNwOagFffuAm6f_SWDWWSUbn6XjV6P7VkjVa8aZbRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ‏تمكن صاروخ إيراني من اختراق الدفاعات الجوية الأمريكية في قاعدة موفق السلطي الجوية بالاردن، وأصابة حظيرة طائرات.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/88893" target="_blank">📅 20:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله أكبر
🇮🇷
🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من إسقاط وتدمير طائرة مسيرة أمريكية من طراز  MQ9 فوق مضيق هرمز.</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/naya_foriraq/88892" target="_blank">📅 19:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي جيه دي فانس حول منشور ترامب لتدمير مركز الطاقة الإيرانية في جزيرة خارك:
يحب الرئيس تغيير أسلوبه قليلًا على وسائل التواصل الاجتماعي. سيكون أول من يقول إنه لا يعلن عن عمليات عسكرية على وسائل التواصل الاجتماعي، لكنني أعتقد أنه يوجه رسالة إلى الإيرانيين.</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/88891" target="_blank">📅 19:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ae530ed8.mp4?token=gr3idnvaFq8W2UxjzEwuhme4FrORg2raJ-V7MRsH5U_OnR_Ym1sq2vyjaTMyV4twuTOCDZxh_99FNsSxXeqmVOlG7I6WUZvNEr-8eZ2jTgsbVxvmu7ZF6DmTC6g7n3Yoafn3PDm1ARaTjiitzDgqZaCJhq9q-hJ7osxldVqcjnlfXx9Wkm8t0hAdjL1bGNANxzx2W12VlmTlTy7h_j2UcmjRmnYtytoZbbzJJ8BX2ZW11AZvQrILUkTONyqphl-DG1-0nkfPxBSeK0Q_-vF54nXuFXeuDLTVeCHuzeJg3i4EWDXLnAZ7ij4VbVDUXy4CJo2yu6sYQT67gJ37FyX8TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ae530ed8.mp4?token=gr3idnvaFq8W2UxjzEwuhme4FrORg2raJ-V7MRsH5U_OnR_Ym1sq2vyjaTMyV4twuTOCDZxh_99FNsSxXeqmVOlG7I6WUZvNEr-8eZ2jTgsbVxvmu7ZF6DmTC6g7n3Yoafn3PDm1ARaTjiitzDgqZaCJhq9q-hJ7osxldVqcjnlfXx9Wkm8t0hAdjL1bGNANxzx2W12VlmTlTy7h_j2UcmjRmnYtytoZbbzJJ8BX2ZW11AZvQrILUkTONyqphl-DG1-0nkfPxBSeK0Q_-vF54nXuFXeuDLTVeCHuzeJg3i4EWDXLnAZ7ij4VbVDUXy4CJo2yu6sYQT67gJ37FyX8TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88890" target="_blank">📅 19:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/88889" target="_blank">📅 19:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
إذا كان الغرض من العقوبات هو تغيير سياسات الدولة أو ممارسة الضغط إلى الحد الذي تتخلى فيه الجمهورية الإسلامية الإيرانية عن سياساتها القائمة على القوانين وإرادة الشعب، فإن مثل هذا الأمر لن يحدث.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88888" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حريق كبير داخل مطار الملكة علياء الدولي جنوب العاصمة الاردنية عمان لاسباب مجهولة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88887" target="_blank">📅 17:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd74b90fbc.mp4?token=djpUzdDlbtfc77zV2kgG_kwTDzx2IEe44H4jgYKPoNqsHzb24leK4ZtAqC9QYzulkhcekCTr3JGoAH12ZKsJbrDPyxEekMWbgTh_pHApt1TfdrEmI8KiiLbWf45j6mKWNxJ21amPbL7b5WaQEpSsiJ1_XushqwfckdOvzat_xVh1OLpYZ5EuzBHTn0JkkFRRWvf26AE9ddNbvtUM92l3_9KJ4eRVLwHnXuo_xf41SOII43sQo7-qdsV_wvCCYv1Nji4dG1XDzTzJGTpyq5t1iZAPMafwVO4_95OR4GuGnyE66Rcyu789aMQPGqV9U8Wm5-V3FsuwVWKEgBQiPRE-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd74b90fbc.mp4?token=djpUzdDlbtfc77zV2kgG_kwTDzx2IEe44H4jgYKPoNqsHzb24leK4ZtAqC9QYzulkhcekCTr3JGoAH12ZKsJbrDPyxEekMWbgTh_pHApt1TfdrEmI8KiiLbWf45j6mKWNxJ21amPbL7b5WaQEpSsiJ1_XushqwfckdOvzat_xVh1OLpYZ5EuzBHTn0JkkFRRWvf26AE9ddNbvtUM92l3_9KJ4eRVLwHnXuo_xf41SOII43sQo7-qdsV_wvCCYv1Nji4dG1XDzTzJGTpyq5t1iZAPMafwVO4_95OR4GuGnyE66Rcyu789aMQPGqV9U8Wm5-V3FsuwVWKEgBQiPRE-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول قوات عسكرية سعودية وأمريكية إلى محافظة المهرة اليمنية وعدد من المواقع في حضرموت على متن طائرات شحن عسكرية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88886" target="_blank">📅 17:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZUPQRxut_CMtCPekO9itwU61jcWI-M9jR3_oRlFLJgjiIEotUz4XyL2yG1kLv4WcwEONBJeCBp4TgOs2uQ3jCchszz96q99ArWId7-TE2QoOj7KMoLpsq7N0lcgqZpwjYWjwoLiisPRFRS1eWA6HnZLP_aL69p828tEuSdbhS3xQX32Z2YyldL0NUNugtnt0SmIEE6pXL8WSoQU6e4CLs2yuuhXswhzqXEwPvsC4jKCscErehYojcehB_PJysJ0jrqqQdHzhhyuTlGKzt0qvoYbUyhJElJfH7ftvK77WxBQE2GB8Vx3ObseX1P8whZJlqfbYLyKY1MvYl-IAyalOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحي الله اخوة بدر وحي الله حزب الله
اليوم الذكرى السنوية لدخول كتائب حزب الله قوة ابو إسراء وباسم مع تشكيلات القوة الحيدرية " العصائب ، سرايا السلام "  لفتح حصار مدينة امرلي ستالينغراد العراقية باكورة انتصار العراق على عصابات داعش الأمريكية المدعومة من الولايات المتحدة الأمريكية..
#المقاومة_حياة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88885" target="_blank">📅 17:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اشتباكات في البحر الاحمر بين انصار الله ومرتزقة السعودية في اليمن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88884" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
وزير الخزانة الامريكي:
قد يستغرق انهيار الاقتصاد الإيراني شهوراً.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88883" target="_blank">📅 16:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامب: سنوجه للإيرانيين ضربة قوية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88882" target="_blank">📅 16:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
🇺🇸
ترامب: الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88881" target="_blank">📅 16:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
🇺🇸
ترامب: الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88880" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الولايات المتحدة سترد على الهجوم الذي شنته إيران على القوات الأمريكية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88879" target="_blank">📅 16:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇹🇷
‏وزير الخارجية التركي: اتفقنا على تسمية رسمية لحلفنا "حلف مكة الدفاعي" ومنفتحين على توسعة الحلف.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88878" target="_blank">📅 15:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇹🇷
‏
وزير الخارجية التركي:
اتفقنا على تسمية رسمية لحلفنا "حلف مكة الدفاعي" ومنفتحين على توسعة الحلف.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88877" target="_blank">📅 15:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مسؤول امريكي:
لم نستهدف جزيرة خرج في الضربات التي وقعت الليلة الماضية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88876" target="_blank">📅 15:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
هناك تيارات داخل الولايات المتحدة ترى مصالحها في استمرار الحرب وترغب في استمرار الصراعات.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88875" target="_blank">📅 14:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
ضبط 7 مليارات دينار و5 ملايين ونصف المليون دولار و35 عقاراً تخص المتهم الموقوف علاء محسن خلف مدير مكتب المتهم الموقوف عدنان الجميلي، وذلك إثر التحقيقات الجارية معه.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88874" target="_blank">📅 14:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▫️
الحكومة العراقية:
- رئيس الوزراء سيجري جولة أوروبية لزيارة باريس وبرلين خلال النصف الأول من أيلول تلبية لدعوة رسمية.
- ‏نصدر 2,000,000 برميل نفط عراقي والصادرات العراقية النفطية تمر بانتظام.
- تم تخويل وزارة النفط بمنح 35 لتر لكل (كي في) ويكون سعر الوقود للمولدات مدعوما</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88873" target="_blank">📅 13:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTiZ7lNMcQdf8lXWYMfbFu4-HBVTcrA8JPY3it8TBVRR7-KKim6FcAzjdDk6Ujdj_VzI0vvPvJREzGzFNAw-1NVDRy6KPPgK2D3nClbGYkKtWkrdmVk0sGCXjeJwcD-ZeDtHzWFSCqXRmhoPfL_oRrtEzua_wWkdEL0nmu2XPzcBLcXbRB7ROaT4sDyf00ETaVDrlw03KJyzYn7_bYPyv2UTYGRjb5WaxcFclwLfKr6OMn7m-VoB4oTeq4VZ2vgAM7AKJhtWKkWgoojuVElXmYgzqdTBXp3M-NY0A-EOmWFZ55a2wxFyuGygFWjBnOyQmlAopfhxgEk5TCcrOiU4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل عمران زراري أبن شقيق النائب في البرلمان العراقي عن الحزب الديمقراطي الكردستاني بايز زراري خلال اشتباكات مسلحة في ناحية دارشكران ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88872" target="_blank">📅 13:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#ترفيهي
🇦🇪
الامارات تقر بالهجوم الايراني رسميا وتقول انها تحتفظ بحق الرد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88871" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترفيهي
🇦🇪
بعد أن أعلن الجيش الإيراني استهدافها بالمسيرات.. وزارة الدفاع الإماراتية تنفي استهداف قاعدة المنهاد الجوية بالصواريخ.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88870" target="_blank">📅 12:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
متحدث الحكومة العراقية:
موعد 30 أيلول المقبل سيشهد الانتهاء التام لتواجد بعثة التحالف الدولي على الأراضي العراقية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88869" target="_blank">📅 11:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
‏
مسؤولون أميركيون:
نراقب هرمز وسنهاجم من يهدد الملاحة هناك.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88868" target="_blank">📅 10:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
الشيخ حيدر الغراوي اعزه الله:
الوفاء الحقيقي لرسول الله (ص) لا يكون بالشعارات وحدها، وإنما بالثبات على الحق ونصرة المظلوم والوقوف في وجه الاحتلال والعدوان.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88867" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترفيهي
🇦🇪
بعد أن أعلن الجيش الإيراني استهدافها بالمسيرات..
وزارة الدفاع الإماراتية تنفي استهداف قاعدة المنهاد الجوية بالصواريخ.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88866" target="_blank">📅 10:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=jAhacWnvgtvBLgGn7dQOQH_JXFnV3t_lmQ1ifZxChHHJEqmamiqwKvWi1mqtFPOT-92ke91eeaLbA9MDJ3mUq-J7e-706HlpF8D03YAz4NJja0CLI916fKi6C1XPWM9ZEE_Z7TLweAuMH42xKNZaHozhIZ1KKFoxGlxpKA9Dfts4_Q1t9O7LhIjD84OXcG1GaZIgQ8Az7DExsWh45CdVkGXbNuM9fhUOALnhbPALR7iUN0qn8rWRq15_GHG1O4f_3ILzJPNK-74r1VZLjQKGiGKJCJbqNW0Vzk5cjPgZD8ycJBq6GX71ESYzJI3ok57KiZEEvr1aXICyYxrZpYCSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa1a420d2d.mp4?token=jAhacWnvgtvBLgGn7dQOQH_JXFnV3t_lmQ1ifZxChHHJEqmamiqwKvWi1mqtFPOT-92ke91eeaLbA9MDJ3mUq-J7e-706HlpF8D03YAz4NJja0CLI916fKi6C1XPWM9ZEE_Z7TLweAuMH42xKNZaHozhIZ1KKFoxGlxpKA9Dfts4_Q1t9O7LhIjD84OXcG1GaZIgQ8Az7DExsWh45CdVkGXbNuM9fhUOALnhbPALR7iUN0qn8rWRq15_GHG1O4f_3ILzJPNK-74r1VZLjQKGiGKJCJbqNW0Vzk5cjPgZD8ycJBq6GX71ESYzJI3ok57KiZEEvr1aXICyYxrZpYCSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/88864" target="_blank">📅 06:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
😆
ترمب: جزيرة "خرج" الإيرانية تتعرض للتدمير</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/88863" target="_blank">📅 05:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=fiO83DubEMPtVPf7dqPGsuLJiaUreHrFOWMGZ2l4NnQhb1ZQy75WnPMU7HtOHmYfmTbyRmnlQ_iS2SY2mLYoGDemc86PQnfwpQMRfCpm8VNT4F5DK9n4pEmwiK3GH0fvgxqSjzfkdD8q5ufnfBcy8IIQvl6PvfYxuMSSu6OIjMLqX6DhqkDZ6LncAeM0E78-JRBgX38hIXt-VkNh43o9DB32KUbermfmMrhKKcUp5AmAvlLcEdeM4z0jELd-YBU7EGmkmZsXCkOQH8JE2R7w_cXtkEYEp3Zj0nXXNYk8guYAU4KFt0JVCiEz6ug2Ybk-CnrsQoQl7_epmB1CjhPJ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79390d1f.mp4?token=fiO83DubEMPtVPf7dqPGsuLJiaUreHrFOWMGZ2l4NnQhb1ZQy75WnPMU7HtOHmYfmTbyRmnlQ_iS2SY2mLYoGDemc86PQnfwpQMRfCpm8VNT4F5DK9n4pEmwiK3GH0fvgxqSjzfkdD8q5ufnfBcy8IIQvl6PvfYxuMSSu6OIjMLqX6DhqkDZ6LncAeM0E78-JRBgX38hIXt-VkNh43o9DB32KUbermfmMrhKKcUp5AmAvlLcEdeM4z0jELd-YBU7EGmkmZsXCkOQH8JE2R7w_cXtkEYEp3Zj0nXXNYk8guYAU4KFt0JVCiEz6ug2Ybk-CnrsQoQl7_epmB1CjhPJ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/88862" target="_blank">📅 05:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=EjV38w_wWVOvSwHuupLnZiCa-tcGeRlyd4CruZMr6pM7vIh_YIlkt5GGrBTtpQwqxThH9ByIiRJelbq_ll0Fo8OBahNA-Hv_rLAQ-xgfT9bS4o9ET_ap7Nw4sHepZRZzc0ynjGZuufPlcEsWug3mPYhXAsVFymVFRxXDJq_exQ3eVMnmAbsVl3iPaPI1Vy64ok9JGnPHxa451Q0qPtj_n-dUhwxmz17Kcd90nF310K9lyzprGLQRekC5ywSVc5MD34xzsQG2intrT54AKKnTaAwWVmHaNN8Dov3dfM_dEIAZDQuY6PZUBWx153HyPsWiFZEHmgGwH0yJHBfQOmEt0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e138b9204f.mp4?token=EjV38w_wWVOvSwHuupLnZiCa-tcGeRlyd4CruZMr6pM7vIh_YIlkt5GGrBTtpQwqxThH9ByIiRJelbq_ll0Fo8OBahNA-Hv_rLAQ-xgfT9bS4o9ET_ap7Nw4sHepZRZzc0ynjGZuufPlcEsWug3mPYhXAsVFymVFRxXDJq_exQ3eVMnmAbsVl3iPaPI1Vy64ok9JGnPHxa451Q0qPtj_n-dUhwxmz17Kcd90nF310K9lyzprGLQRekC5ywSVc5MD34xzsQG2intrT54AKKnTaAwWVmHaNN8Dov3dfM_dEIAZDQuY6PZUBWx153HyPsWiFZEHmgGwH0yJHBfQOmEt0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع أعمدة الدخان من مصفى الدورة جنوبي العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/88861" target="_blank">📅 05:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
ما تسمى القيادة المركزية الاميركية:
زعم الحرس الثوري الإيراني في بيان صدر مؤخراً أن الضربات التي شنتها القوات الأمريكية لمنع الحرس الثوري من زرع ألغام في مضيق هرمز كانت "عملاً عدوانياً". هذا الادعاء باطل تماماً.
اتخذت القوات الأمريكية إجراءً محدودًا ودقيقًا ضد قوات زرع الألغام التابعة للحرس الثوري الإيراني التي كانت تشكل تهديدًا وشيكًا في مضيق هرمز. في جوهر الأمر، إيران هي من خلقت هذا التهديد، وقام الجيش الأمريكي بإزالته لحماية البحارة المدنيين، والشحن التجاري، وحرية حركة التجارة العالمية.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/88860" target="_blank">📅 04:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:  لحظة إطلاق الصواريخ في عملية "محمد بن عبد الله (ص)" المشتركة بين الطائرات المسيرة والصواريخ، والتي استهدفت البنية التحتية والمرافق الفنية ومواقع تمركز طائرات العدو في قاعدتين جويتين أمريكيتين في الأردن، وهما قاعدة "الملك حسين" و"الأزرق"،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/88859" target="_blank">📅 03:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترفيهي
🔻
الجيش الأردني:
اعتراض 8 صواريخ اخترقت المجال الجوي للمملكة.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/88858" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
وول ستريت جورنال:
تسعى إدارة ترامب إلى تجنب العودة إلى مواجهات عسكرية واسعة النطاق مع إيران، وهو ما قد يزيد من الضغط على مخزونات الولايات المتحدة من صواريخ الاعتراض وأنواع أخرى من الأسلحة.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/88857" target="_blank">📅 02:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dc0bc98.mp4?token=NNF_-tFhJlyx5_S7aVINknmJLEr8j4zJxF0UPPId1hcOzwqHUDCNe3gOtzZPLEF5VEm3ZFaeoyTA5r3loqC39Xo8chtLd8v7wL0ejnZxduKP05bisqlQwBB5TlPgfBKtyFSPz7QJ2lp-hgppnlzKGmXE-2DAGINZDMipSd8OwyRUi75WlCLkB1Iv2sOPiZSdv84m4vb8TqK-pHdeVj20_DjmE_AmzinZc3jMs3e6fqSVDAxHHGQGaVSEAXBw8Bjul-jEhBFPLQZnKDOgdjLgTFjRYR36zxvm0aryNbPXF3dPg2aAym470ws675KnTeasFxTOnLmjRpey05rKRY8wEa2oSf94gYllf28b5cpFH9PVUjfH0RjHknyoSffz_XUP1h8yu9hHpefBaIaNpsvnFAUUefdwbw5OFA5S3UcQhQufbgQvYMFGYArLbbWs--ieyuU5KW_a07ryJDJkDIqn6RNJNlwlGUNzvGL5wBeLIX1-tB41uke-xR2GfOFVOGbbeA-cp6koMaj5jAD2jk-5yjE7Ot4wI9dBQA4_4nz966pSEBRifMSj_4ZJ2gcMtBYKf20IZik-GaMBVp2pfKR5icQhwehqadavTMnVTEE3hByt627Z9aocnfs-60zo54fRklTI7_xu80FyCgb88KOfH4uhNeqXRoe72zenuV4tXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dc0bc98.mp4?token=NNF_-tFhJlyx5_S7aVINknmJLEr8j4zJxF0UPPId1hcOzwqHUDCNe3gOtzZPLEF5VEm3ZFaeoyTA5r3loqC39Xo8chtLd8v7wL0ejnZxduKP05bisqlQwBB5TlPgfBKtyFSPz7QJ2lp-hgppnlzKGmXE-2DAGINZDMipSd8OwyRUi75WlCLkB1Iv2sOPiZSdv84m4vb8TqK-pHdeVj20_DjmE_AmzinZc3jMs3e6fqSVDAxHHGQGaVSEAXBw8Bjul-jEhBFPLQZnKDOgdjLgTFjRYR36zxvm0aryNbPXF3dPg2aAym470ws675KnTeasFxTOnLmjRpey05rKRY8wEa2oSf94gYllf28b5cpFH9PVUjfH0RjHknyoSffz_XUP1h8yu9hHpefBaIaNpsvnFAUUefdwbw5OFA5S3UcQhQufbgQvYMFGYArLbbWs--ieyuU5KW_a07ryJDJkDIqn6RNJNlwlGUNzvGL5wBeLIX1-tB41uke-xR2GfOFVOGbbeA-cp6koMaj5jAD2jk-5yjE7Ot4wI9dBQA4_4nz966pSEBRifMSj_4ZJ2gcMtBYKf20IZik-GaMBVp2pfKR5icQhwehqadavTMnVTEE3hByt627Z9aocnfs-60zo54fRklTI7_xu80FyCgb88KOfH4uhNeqXRoe72zenuV4tXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
الحرس الثوري:
لحظة إطلاق الصواريخ في عملية "محمد بن عبد الله (ص)" المشتركة بين الطائرات المسيرة والصواريخ، والتي استهدفت البنية التحتية والمرافق الفنية ومواقع تمركز طائرات العدو في قاعدتين جويتين أمريكيتين في الأردن، وهما قاعدة "الملك حسين" و"الأزرق"، وذلك بإطلاق صواريخ باليستية.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/naya_foriraq/88856" target="_blank">📅 02:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWDuymaTfur9vOMO3tmKH2kJVFl61J9QYmaNeO0d4zrs7KCpCFLOyEndxGWnnyhHqpN7QLinSNOzKUPH8O0LJNYk1dJDXKFM7cttVSq98ReteZU09gRAKcE-EPalyx4XR_FomVhoWsNOfhch_gpq11LU1FELhQFSj1WjrKzf1zDWwxdySpiYMuVQNYXFDnKyvrg51qRijHusOdRuTATL533khaHbbsGn5E-9fkCwx4RbRGeW-08IczWletFoEpBumfV2GXixPEABrOoEej0GhwxI2VNTc0U4MdVUEvafqgnilEaP2zYEjJRJA2erNnaY3P5eOecVhh8WhoTzFwuNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الرشقات الصاروخية الإيرانية التي أطلقت نحو القواعد الأمريكية في الأردن.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/88855" target="_blank">📅 02:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
🇮🇷
الحرس الثوري:
بسم الله قاصم الجبارين
"فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ"
🔹
أيها الشعب الإيراني الكريم والثائر،
إن تواجدكم البطولي المتواصل وغير المسبوق لمدة 183 ليلة في الميدان، قد أذهل العدو وأثار دهشته، وهو مصدر أمل للمستضعفين ونور لعيون مجاهدي الإسلام.
🔹
قبل دقائق، قام مقاتلو القوة الفضائية التابعة لحرس الثورة الإسلامية، ردًا على العدوان الجوي الذي شنته العدو الأمريكي والصهيوني على جزيرة "لارك"، بعملية "تأديب المعتدين" من خلال عملية مشتركة بالصواريخ والطائرات المسيرة تحت اسم "يا محمد بن عبد الله (ص)"، حيث تم تدمير البنية التحتية الفنية والإصلاحية ومواقع استقرار طائرات العدو في قاعدتين جويتين أمريكيتين، وهما "الملك حسين" و"الأزرق" في الأردن، وذلك بإطلاق صواريخ باليستية، مما أحدث أضرارًا جسيمة.
🔹
حذر حرس الثورة الإسلامية، مؤكدًا أن العدوان والجريمة لن تحل مشكلة استياس العدو من إضعاف سيطرة الجمهورية الإسلامية على مضيق هرمز، وأن كل هجوم سيقابل بردود فعل أقوى.
"وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ"</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/88854" target="_blank">📅 02:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/naya_foriraq/88853" target="_blank">📅 02:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پاسخ کوبنده فرزندان ایران زمین همچنان ادامه دارد</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/naya_foriraq/88852" target="_blank">📅 02:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة السعودية.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/naya_foriraq/88851" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسؤول أمريكي: نتعرض لهجوم صاروخي من إيران</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/88850" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/755c0bd3e6.mp4?token=cPFFuvHM6wV_5DqyHEMz6S0Z-yjJgvWwXKBL7iJgWbsNR8SmlLfIPRoUzSniPzbrqomjOLounqRloHZSf_qtNSnoaS12LmSHeektkeFDntB1Qe4t-FcgutInOeRvk8XuErnwgY7uWeTolJvvWC5HKEc-x5hlzokTDP6f1GDpJYgriI3YEwK0Dfs68URTuoH7y_V1ShNRi8LRkHQERUrH42HAtu6DL9KXsjjETfRzzIpFITh4dEhFG7rQx_cA9u3ErFxOvmqfXERCP0a5crnIB7G__90WIPV1_ZMJZncgfqy1KFzrNdEy02nC1p2-PZKl9inzHc4b7sCvnqedcFMKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/755c0bd3e6.mp4?token=cPFFuvHM6wV_5DqyHEMz6S0Z-yjJgvWwXKBL7iJgWbsNR8SmlLfIPRoUzSniPzbrqomjOLounqRloHZSf_qtNSnoaS12LmSHeektkeFDntB1Qe4t-FcgutInOeRvk8XuErnwgY7uWeTolJvvWC5HKEc-x5hlzokTDP6f1GDpJYgriI3YEwK0Dfs68URTuoH7y_V1ShNRi8LRkHQERUrH42HAtu6DL9KXsjjETfRzzIpFITh4dEhFG7rQx_cA9u3ErFxOvmqfXERCP0a5crnIB7G__90WIPV1_ZMJZncgfqy1KFzrNdEy02nC1p2-PZKl9inzHc4b7sCvnqedcFMKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي على موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/88849" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbe0853d.mp4?token=p25u6NYRCtxvH4UK0ZUcBpz4EjI1RGH3GSwRccAw7sa6EF4LpSrjZ3Q10yYyAio0A0ZauuzqTX5H-cLHIC9hm-nrnohzqbA5NEVQSZQgW0ljgJ0LoumvvT3BlnOBqg0EY9Vc-9lKKPOnEbuKVmfJoOpHGiREovn5Szj9ZMU42OGoQskMS_omikpuQ-99Updnx6m4yM-Ga4LSDYWImd1N3DRprr5suGozOW2ynH18UQZVkrP7hdI3WbEuV8GxX5UmHU9T6Gwlpk7_a9pJxACSpE5hk2wC7rP8Vbuwc19Ih_zjL2GgH45Q5DkCT44I8XjRZswuZ4T3gnU6Ypzk_OrRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbe0853d.mp4?token=p25u6NYRCtxvH4UK0ZUcBpz4EjI1RGH3GSwRccAw7sa6EF4LpSrjZ3Q10yYyAio0A0ZauuzqTX5H-cLHIC9hm-nrnohzqbA5NEVQSZQgW0ljgJ0LoumvvT3BlnOBqg0EY9Vc-9lKKPOnEbuKVmfJoOpHGiREovn5Szj9ZMU42OGoQskMS_omikpuQ-99Updnx6m4yM-Ga4LSDYWImd1N3DRprr5suGozOW2ynH18UQZVkrP7hdI3WbEuV8GxX5UmHU9T6Gwlpk7_a9pJxACSpE5hk2wC7rP8Vbuwc19Ih_zjL2GgH45Q5DkCT44I8XjRZswuZ4T3gnU6Ypzk_OrRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انقضاض الصواريخ الإيرانية على قاعدة موفق السلطي الأمريكية وسط تفعيل مكثف لمنظومة الباتريوت الدفاعية</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/88848" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=BSbB4Ch8EXqUbJpg_9S7SycCmfq92Dup1i3z_gWWAFhNn0fhetl1hh8E56bfETj2GxLbSolQqToPz54BBdEG1TqFJaSfA8RhruqeENlj_RQj5ZTn82xcDk-Z6okvi0fmTMKWP4mCpqjkS3LX4uZztF5Xb3gYIk792A0taere4lC8gBm9FQR6kEcmhr9z5wvzTlIZBGcL-dSSvUj8YOSPXjvRxdFdexVoou89yv-ND-9vrHmNaVjUalsBLIq8TaceTc6Sq1rVXanjPkQRqyhkKRtlRdz0Nqac4XIKi2V3S6G6T51E6lcNtP-ABdINkWH7q81dPukurivSHfvJ1caX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=BSbB4Ch8EXqUbJpg_9S7SycCmfq92Dup1i3z_gWWAFhNn0fhetl1hh8E56bfETj2GxLbSolQqToPz54BBdEG1TqFJaSfA8RhruqeENlj_RQj5ZTn82xcDk-Z6okvi0fmTMKWP4mCpqjkS3LX4uZztF5Xb3gYIk792A0taere4lC8gBm9FQR6kEcmhr9z5wvzTlIZBGcL-dSSvUj8YOSPXjvRxdFdexVoou89yv-ND-9vrHmNaVjUalsBLIq8TaceTc6Sq1rVXanjPkQRqyhkKRtlRdz0Nqac4XIKi2V3S6G6T51E6lcNtP-ABdINkWH7q81dPukurivSHfvJ1caX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/88847" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/88846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=hLf_IjAzwXz2v8dbzIgXuGPjsBSywxzmVStQYdCsmTbz-fyHiA7yNlJVQmZI46LcX1N_4LO7jEjE5FZq3pT1XfDfNt8kB4TgRyP_9iYPAdQVasVMEpA_pEDhSBUDUw-TDEqML68B5jsK_lq0kF_Eyvsu0GG4z1y60hR-_YTrh73Ke5dkgT0opfheQi1ZwXxgZKQuMWK_33ayjLIoWreirywR40A0RYb6-NlpMZJfkQMj8w9LE4DzLHrWa511oq68zM6lAXuCH_YIozOw9_ha6N1iY58U6y6SZ2w0fM-ITKLSzYa-SUMRKP6kaMcMSKBp9UE_ru4rOM4QGum2oqqnEWVYsA-HOqBr6yZ_LzjkgPa4lYsL2bc-Wo2rqH9CcruNhLJGjStU9oSD8nvbkMHGz5jsK_h1hKcKFDyzxcacIceBunQcp8jZSPVeXvsdzEd70ibO5qlgcUU8gfuGbMr-hjvNxsSTaa3SlqESCKj06JEe4iOkQSzoRlk9PzvJEWkACME4MNUfxkv1-5koLnpSSU-Y02jYIgSZ_GRBIqihvfw1BNgMHTfroTZvTcSn-zCDgf0cLrTv2bZqMktYueN7a5QuMOIfxC9q-Rv0N3rZ_DPnndCZ3xVK36CFvZNO2o3mPUeukPURvS45NZIztdq5CG5gZ6OGHBRiNf0m7Fn1710" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e60316bfc.mp4?token=hLf_IjAzwXz2v8dbzIgXuGPjsBSywxzmVStQYdCsmTbz-fyHiA7yNlJVQmZI46LcX1N_4LO7jEjE5FZq3pT1XfDfNt8kB4TgRyP_9iYPAdQVasVMEpA_pEDhSBUDUw-TDEqML68B5jsK_lq0kF_Eyvsu0GG4z1y60hR-_YTrh73Ke5dkgT0opfheQi1ZwXxgZKQuMWK_33ayjLIoWreirywR40A0RYb6-NlpMZJfkQMj8w9LE4DzLHrWa511oq68zM6lAXuCH_YIozOw9_ha6N1iY58U6y6SZ2w0fM-ITKLSzYa-SUMRKP6kaMcMSKBp9UE_ru4rOM4QGum2oqqnEWVYsA-HOqBr6yZ_LzjkgPa4lYsL2bc-Wo2rqH9CcruNhLJGjStU9oSD8nvbkMHGz5jsK_h1hKcKFDyzxcacIceBunQcp8jZSPVeXvsdzEd70ibO5qlgcUU8gfuGbMr-hjvNxsSTaa3SlqESCKj06JEe4iOkQSzoRlk9PzvJEWkACME4MNUfxkv1-5koLnpSSU-Y02jYIgSZ_GRBIqihvfw1BNgMHTfroTZvTcSn-zCDgf0cLrTv2bZqMktYueN7a5QuMOIfxC9q-Rv0N3rZ_DPnndCZ3xVK36CFvZNO2o3mPUeukPURvS45NZIztdq5CG5gZ6OGHBRiNf0m7Fn1710" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دويلة الكويت تطفئ مشاعل أبار النفط وتبدء التعتيم خوفا من الاستهداف والرد الإيراني.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88844" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88842">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-iIVJ_6RL5rcvNmvIcvCCTECQo_FcWAoSF0HO1v_fXiBfZqQR5CEwGvlZqdH3UYyMW5zoeveuuW1yl66ntu-N4iVFnnlJ2tEFEW-uwnazHy_UsoP8evQvFIzWl0VweEeCO74B_vNVPA_VGVpui2gm3ibl42EWMOZj70iWxfetVB0TxAK8Hn2fz7G61OMuASwaoUG5RWfF-kwEjaNXoGwPVtOOHl5K9vmjMwf-EiW_-BevP5OKTCRBEYoHvt1GNZmdi8HiLHR_TMj_nHypgWDJTMVpXoRBNKGX70arDkcOxnNCWJY99JoOF4YGBee2ejJ-LRHfEPY_2DzvTvV-b1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aaf124627.mp4?token=X9evBrO2WPAYcgl8T8wEcKEH2Y_5KEHSzrzW9KgpBBdXYjND-W8X7F2Cdf0aSk4CoRAMpZrFkaJ8FLzM4ue45bNvYHFTuja5dmt6pgfkE4ZMJmMU_BiMfvd2T_IGf9DKOM0J8JGe0rDzjqynEzYJygdPlSqucT6Gpd99Pn9UhB6kyZTz5Wpd5xr09iO8zj1XmtHSP7LgOcrWBOcx9-Xtw2q5_k48KNXI5tFOqXRHBc_PuIFuWPicnyhngq2FzeJ7PlByinrDQly9NViv6Yo9C3Kr3tI89P0ql4Xwrbla-4lpwbw4hh6mcmtRstYZlYzT08gMC4qEOhuLS0mX0Vf5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aaf124627.mp4?token=X9evBrO2WPAYcgl8T8wEcKEH2Y_5KEHSzrzW9KgpBBdXYjND-W8X7F2Cdf0aSk4CoRAMpZrFkaJ8FLzM4ue45bNvYHFTuja5dmt6pgfkE4ZMJmMU_BiMfvd2T_IGf9DKOM0J8JGe0rDzjqynEzYJygdPlSqucT6Gpd99Pn9UhB6kyZTz5Wpd5xr09iO8zj1XmtHSP7LgOcrWBOcx9-Xtw2q5_k48KNXI5tFOqXRHBc_PuIFuWPicnyhngq2FzeJ7PlByinrDQly9NViv6Yo9C3Kr3tI89P0ql4Xwrbla-4lpwbw4hh6mcmtRstYZlYzT08gMC4qEOhuLS0mX0Vf5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88841">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88841" target="_blank">📅 01:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88840">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fcf5d931c.mp4?token=NHnOTNy1lco1baj3qBWaGAUV5zS9bcsVEHpB3lsVKocAWVbrGGFrY46vByqViCj_FWYGUsR2bGhBCD-p_i6FrCOKKt9gR3xQV9ReF8tFffxLBV4BNKav0QGQ6H205vj1Ov4q5qR655ioNBkq2xt6lpZh9yBiIRcGNaOdVJXrWRrbXweRMgWWqSI2FG6B9H35YGW5tuiJgyugpQSxz6JGWcMRRQyzGCXu9bcotU9cG7Jb5QvOYYoBjxvL4FT1knHoanknplMpH1hgqEhYEDIF7wLGUVpnDf2kAprgmqTwmTTipKFPIB2X3os4oaGkxnmdc536j284hUmJb8hLEl0hHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fcf5d931c.mp4?token=NHnOTNy1lco1baj3qBWaGAUV5zS9bcsVEHpB3lsVKocAWVbrGGFrY46vByqViCj_FWYGUsR2bGhBCD-p_i6FrCOKKt9gR3xQV9ReF8tFffxLBV4BNKav0QGQ6H205vj1Ov4q5qR655ioNBkq2xt6lpZh9yBiIRcGNaOdVJXrWRrbXweRMgWWqSI2FG6B9H35YGW5tuiJgyugpQSxz6JGWcMRRQyzGCXu9bcotU9cG7Jb5QvOYYoBjxvL4FT1knHoanknplMpH1hgqEhYEDIF7wLGUVpnDf2kAprgmqTwmTTipKFPIB2X3os4oaGkxnmdc536j284hUmJb8hLEl0hHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السماء تتزين بالصواريخ الإيرانية المتوجهة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88840" target="_blank">📅 01:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7130d96ff8.mp4?token=pT_qd6MxJ4tT2lnQ9hZp3vcMc9sJxh8LP1PSIDjIR965xEfwvGFGVIdArRyOqsEh-4Q9afDivKBiiwtGJ13Xr3NOqPHrQRWPkA11TLAQ8u0QRu77_-le8TxrRzuano1MFyj8zjAowumFkH6zdVaYh2JUwJwRkNhTpY_JPMwb4hjojObjrHm9c2S82DypRzH2_JJ16VYlCGy4UiFZN32fidT_YPHluer7EuohTcNvZOlTYNUgFd_TzAjTTt-UB8U1tkRrJEBsxeqqGG4mfGAEc044WsNxvvWwf1ygUx3LDvcFFuYg3plwyiLdRNmz3Yu1RmJ_hQKf8IBh7dN3dYgKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7130d96ff8.mp4?token=pT_qd6MxJ4tT2lnQ9hZp3vcMc9sJxh8LP1PSIDjIR965xEfwvGFGVIdArRyOqsEh-4Q9afDivKBiiwtGJ13Xr3NOqPHrQRWPkA11TLAQ8u0QRu77_-le8TxrRzuano1MFyj8zjAowumFkH6zdVaYh2JUwJwRkNhTpY_JPMwb4hjojObjrHm9c2S82DypRzH2_JJ16VYlCGy4UiFZN32fidT_YPHluer7EuohTcNvZOlTYNUgFd_TzAjTTt-UB8U1tkRrJEBsxeqqGG4mfGAEc044WsNxvvWwf1ygUx3LDvcFFuYg3plwyiLdRNmz3Yu1RmJ_hQKf8IBh7dN3dYgKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88839" target="_blank">📅 01:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315c7b50c1.mp4?token=IgBzEHrTHLrrtVEXTI3PdnmzXyppORCLmndsOpiR7k_TkPf0enGXoI4OtyU47_B7AZWDQwEhyZvuUWCF6ZoRK4Fk0aQOzwzPXu38Gz7q5k-cU9-PUvoLO8snNSTHtweMeI7YR6BW5FjL1KFGF9nLpigtnTYtciOFwRj1SLNteF_RK81XuvPh3JuyB12oiIIZRN38464CYAvgFnxP-t9y_nNnX4iOtbOJYOI-ArfUFbp3Tft8TvZSdDOi4UbAjBGhgGVzeO3yh2yA1RHFwZRsqlu9rJmUaQYWP0NpG-cawniv8mUZAdAKnWQ13hSIGg5JfBloVNfSwUk_n57Xfgij7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315c7b50c1.mp4?token=IgBzEHrTHLrrtVEXTI3PdnmzXyppORCLmndsOpiR7k_TkPf0enGXoI4OtyU47_B7AZWDQwEhyZvuUWCF6ZoRK4Fk0aQOzwzPXu38Gz7q5k-cU9-PUvoLO8snNSTHtweMeI7YR6BW5FjL1KFGF9nLpigtnTYtciOFwRj1SLNteF_RK81XuvPh3JuyB12oiIIZRN38464CYAvgFnxP-t9y_nNnX4iOtbOJYOI-ArfUFbp3Tft8TvZSdDOi4UbAjBGhgGVzeO3yh2yA1RHFwZRsqlu9rJmUaQYWP0NpG-cawniv8mUZAdAKnWQ13hSIGg5JfBloVNfSwUk_n57Xfgij7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية المتجهة نحو القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88838" target="_blank">📅 01:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">أسعار النفط تصعد بأكثر من 2%</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88837" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd66fd0ad1.mp4?token=iurA3oCLJanQuScOgEhjhY72vkZFEZffCqBq6dzTA0frGncwwqw5v517lbWSkOF0FnGcQuhDEjD1sSHpA0Q6TXNfGMdGeWT2CJN2GL2VduHrdz9_ylUusD_hIjfHimYzd62EbAM041mkTo9meebnqf5JRxaI2l6AuRJgWW8dxaHrq1GW6U8WzctQ8LD19MaNPYIBfPF7xhzT41fl18mhyt_3L8bMyugnSSIJK-ExS2k7MbLQ2gjgQBxtvudxRTy4lFBZBifsIsj2F6j5mxNLZ_qMfCDGyG9tA88GYgtXyiR2egdHqqy_4bJtuMm3OurUO-YqVIPcCC-YrEi1OR76SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd66fd0ad1.mp4?token=iurA3oCLJanQuScOgEhjhY72vkZFEZffCqBq6dzTA0frGncwwqw5v517lbWSkOF0FnGcQuhDEjD1sSHpA0Q6TXNfGMdGeWT2CJN2GL2VduHrdz9_ylUusD_hIjfHimYzd62EbAM041mkTo9meebnqf5JRxaI2l6AuRJgWW8dxaHrq1GW6U8WzctQ8LD19MaNPYIBfPF7xhzT41fl18mhyt_3L8bMyugnSSIJK-ExS2k7MbLQ2gjgQBxtvudxRTy4lFBZBifsIsj2F6j5mxNLZ_qMfCDGyG9tA88GYgtXyiR2egdHqqy_4bJtuMm3OurUO-YqVIPcCC-YrEi1OR76SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88836" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee455c5e0.mp4?token=UeegCEeg4dFJLfph4ZuPm5s3jthtjTdGpHlMwVWd73HJKQke4gbXfEn9VCUVXqaJxKJuDmMhHz1iKlsIXKdeUDwzbm0dlOwUFeV4cVVladphwehCK01vSqVZ7rxvSCC2RuIWtE6UmJKYTMr4wQhi20COv-AHCywVdyJ4YZMt8Oz4phQY1df6pwrK7wtUp-PNohKWk6zweYq5RQtHe39vF2s1DBV5tcWiLTVdHggT5ty-WxrH9-1451pwbtU4a3Y4mb6GPKF2C7oFCkn-e1unKrglAP9vQKzZ5_MmJx9GQdPEE5r5OkHzH2UYl2Uh7JlN_z4wK13GNKVrolL3clC3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee455c5e0.mp4?token=UeegCEeg4dFJLfph4ZuPm5s3jthtjTdGpHlMwVWd73HJKQke4gbXfEn9VCUVXqaJxKJuDmMhHz1iKlsIXKdeUDwzbm0dlOwUFeV4cVVladphwehCK01vSqVZ7rxvSCC2RuIWtE6UmJKYTMr4wQhi20COv-AHCywVdyJ4YZMt8Oz4phQY1df6pwrK7wtUp-PNohKWk6zweYq5RQtHe39vF2s1DBV5tcWiLTVdHggT5ty-WxrH9-1451pwbtU4a3Y4mb6GPKF2C7oFCkn-e1unKrglAP9vQKzZ5_MmJx9GQdPEE5r5OkHzH2UYl2Uh7JlN_z4wK13GNKVrolL3clC3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن تشتعل بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88835" target="_blank">📅 01:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39dbf9bd0.mp4?token=eKVy4B_90gG7OvipWJA9Vnln3_KGchYyVGUjK-LSo2WW3F60Zh6sptp6Lq_IVvLrSlmiBBhbyo1v6Vsy7lls27arRfdrX3q58wZ_rTrj4tdMEtvxF3dEhBQJ91rfI5ZGMIromhqXDfPT7eyH_Ni-6vOGIqI8i-7jPfAEy00dS3IJdwwZ5Qxr2dSvg9Gv0Q4tNXyYYAB_KuTVfgdjdH9JdwcIm_Z_GZBLrKAyJtAlfUxWy8Yt3k9LScyUXf0dHUJeHG2Ux4RxzAtMh7YfCGcBVzJUj4KSapRKQ3TWIerRF5BymPoeTSnuAFxTZluByNh0YFyXwkJosLYPiKi-43pO1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39dbf9bd0.mp4?token=eKVy4B_90gG7OvipWJA9Vnln3_KGchYyVGUjK-LSo2WW3F60Zh6sptp6Lq_IVvLrSlmiBBhbyo1v6Vsy7lls27arRfdrX3q58wZ_rTrj4tdMEtvxF3dEhBQJ91rfI5ZGMIromhqXDfPT7eyH_Ni-6vOGIqI8i-7jPfAEy00dS3IJdwwZ5Qxr2dSvg9Gv0Q4tNXyYYAB_KuTVfgdjdH9JdwcIm_Z_GZBLrKAyJtAlfUxWy8Yt3k9LScyUXf0dHUJeHG2Ux4RxzAtMh7YfCGcBVzJUj4KSapRKQ3TWIerRF5BymPoeTSnuAFxTZluByNh0YFyXwkJosLYPiKi-43pO1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي عنيف يدك قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88834" target="_blank">📅 01:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88833" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88832">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88832" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88831">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GolihkzM5Gspu3supMGhYhipdKr9P9ZrwrK0DhyvqErmSPj2jOaV1zTdNxrqE3BpIAgqcZyIKdJYS06BB4beinibQu5QbBjxaXpbZID4AQADAXu6vWfdFuo1He7u9LP8jyeT5oXia540JzEK-rQao0iYf8llIy-BfF0wTTWE3e-Sr-8MT2JBlcw9fehdvozHysBtHbid-gsJcF4Y8ryW3ltZ1T3oVxKKbyb4mV3xNvE-vrgKqYB_P_Z_Vki2QjfQ_EesJ69sW-8EX6m_jBR9MvG6ntriIFUvxEJZGkRBdd3VwGsjB7hgiD20ODwFD5UHWgAufIgq38Bm2tH2V5lidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية تدك قاعدة موفق السلطي الأمريكية</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88831" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgtJPFpgVooTCaOVk48--gx9LeuKZwHOXe4V97QCtdPiGhfZuATGlmCS1Ndlcp-vYdTCFksX1vgyDtgsmm9EC3WB0qzgvzbDLkWq8bamMwzhrsf6H98Mzag9ZxfbDBASiLP18oUbvDaicNlFjBJ8FR3YQkaMYzYVzm7CnJqH-Nw6vVPHkbU3CtnMsIgtoiJxfhCC3eC49baaVSwXtCoP3OHf4hFGRe5NufBSF2tCo5BqUAHQp_DxdcHlcWYoPKaN3sS5TVRvM6MhDEvMRIF_8bf9N72KfdSGj9TbirgSanNOt5TNBpMCV5e4YJCxD15AUUB7RttXsBnq8BQtKGqupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدفاعات الاردنية تحاول جاهدة التصدي للهجوم الصاروخي الايراني</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/88830" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac97b51cd.mp4?token=YEZE8ek7NIvJxtYOqKjjD8kMo5nlAjfTWeMKILKfM4dNq7fx9dTFewMv9sJdo4-5lVQdH66Zx0TxmtdrpRkyPrE7bo0HnbxEBeF5JdO1iFqHrYJOZVXM6tkNlC2hEpdqaJHnk71vf7BV_ye9uT9VzyJPIPIl17RTO2Dt-1viLFZjPHd4ubfTSZ2SQ_hxuIl8V6teG0MFsebbxQruAMkxpfIpsHksmXDB3OC-QbmlGCxV40IcvUPV3f1RPLK0jvJGpPsdAdQc3zAWzGcr4xiKL2vvXE2v9xPgHQhtGHMOvkPhvqkq2dCFdEeDYMLvTRcKvgg3ylywbh4KwOvo8EG-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac97b51cd.mp4?token=YEZE8ek7NIvJxtYOqKjjD8kMo5nlAjfTWeMKILKfM4dNq7fx9dTFewMv9sJdo4-5lVQdH66Zx0TxmtdrpRkyPrE7bo0HnbxEBeF5JdO1iFqHrYJOZVXM6tkNlC2hEpdqaJHnk71vf7BV_ye9uT9VzyJPIPIl17RTO2Dt-1viLFZjPHd4ubfTSZ2SQ_hxuIl8V6teG0MFsebbxQruAMkxpfIpsHksmXDB3OC-QbmlGCxV40IcvUPV3f1RPLK0jvJGpPsdAdQc3zAWzGcr4xiKL2vvXE2v9xPgHQhtGHMOvkPhvqkq2dCFdEeDYMLvTRcKvgg3ylywbh4KwOvo8EG-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88829" target="_blank">📅 01:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1671a7ac6b.mp4?token=jCYAovK9NeurZTB41rr0W7oVhDQSQv2dZswOmcP4I1E85xTfPnxRH7y-Zsy2ZEJzDWh3mI1hz6DEJM641cmXTIA6stRticz570QVlxfDzwruF3oxxjuz-B-gFha_H7yScfrtCrquxqZWJgZBaYK8LRoOt0OW6vjidgYZq0p9yNIuWcOnDeWVI-FlTlK_IFm6Jx0rVSdnmYh8rWNO6wbi52mfQlDUPZCcVECNFonKG6Cwfa4ozc4NuLKQW-RLAsa9D7lb7jq2imEXOvGUbC6z2cP1e-ww-via-oO1iOHA-MEZvC51RbOiVOmJ8cR8JudwCUbWVj-RYIwunSemWwrUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1671a7ac6b.mp4?token=jCYAovK9NeurZTB41rr0W7oVhDQSQv2dZswOmcP4I1E85xTfPnxRH7y-Zsy2ZEJzDWh3mI1hz6DEJM641cmXTIA6stRticz570QVlxfDzwruF3oxxjuz-B-gFha_H7yScfrtCrquxqZWJgZBaYK8LRoOt0OW6vjidgYZq0p9yNIuWcOnDeWVI-FlTlK_IFm6Jx0rVSdnmYh8rWNO6wbi52mfQlDUPZCcVECNFonKG6Cwfa4ozc4NuLKQW-RLAsa9D7lb7jq2imEXOvGUbC6z2cP1e-ww-via-oO1iOHA-MEZvC51RbOiVOmJ8cR8JudwCUbWVj-RYIwunSemWwrUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ إيران يشق الطريق نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88828" target="_blank">📅 01:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">القواعد الامريكية في سوريا تطلق صواريخ إعتراضية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88827" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc01134378.mp4?token=LAb1T8gXbRP_3ihZmAxzW8RlxcBwp_aDEiTJefK7G7sSy8oqDOw93osFG8e92R4CuDXfR-5GBemZhgdbN5wZPDnZt7lR0L60sm0SMz7MN4JakNZvNodSVwaPZjXcWq3Rh_M13DwpvBSZE_1kHCBjYP7X6A7m1SPoQPrvrVRmKvZUyfo4z5AGF5_g4KW5lChNhhkdkl1y6x67td8rjiz1_K__FhEfYm0YxbIVBaPkuJdop_tfuKe2iCvW7cqGNXdQvEJ__Ftw3F5nVK_OZQHW08rcZfGrCyXqJmRqwRMKo8fF8ylcOsNKhTMZ6oPav7ajkTmy9sM0uWS82Hg2XraRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc01134378.mp4?token=LAb1T8gXbRP_3ihZmAxzW8RlxcBwp_aDEiTJefK7G7sSy8oqDOw93osFG8e92R4CuDXfR-5GBemZhgdbN5wZPDnZt7lR0L60sm0SMz7MN4JakNZvNodSVwaPZjXcWq3Rh_M13DwpvBSZE_1kHCBjYP7X6A7m1SPoQPrvrVRmKvZUyfo4z5AGF5_g4KW5lChNhhkdkl1y6x67td8rjiz1_K__FhEfYm0YxbIVBaPkuJdop_tfuKe2iCvW7cqGNXdQvEJ__Ftw3F5nVK_OZQHW08rcZfGrCyXqJmRqwRMKo8fF8ylcOsNKhTMZ6oPav7ajkTmy9sM0uWS82Hg2XraRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  انفجار عنيف داخل قاعدة موفق السلطي بالأردن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/88826" target="_blank">📅 01:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انباء عن انفجارات في الأردن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88825" target="_blank">📅 01:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88823">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsHlFdsZTKjHJ1cZR4T4kXxmkrX8CP6rfM2fs37nuzdRDOCSZlBMObGiqzRfKpKiRBI6en-GUp7pNTM5_QangF5Pcpr-cwGef1oxKld4xcwT854cjn2C8UCZLXNrgFBjT7glVT8H0i56s1D6vOrOwth_7zUNz2MTd7gYazp1v63UfPOCEFSipBrp5yBOucEjGNKlzWwpXEijH8SL_p6vQ7qsuE9QWNcVUxWN8mV5-f2Jf8-9h1uX9CV4w1Ddwoa4DYMLdxT1om2vEKBWed1fbaKheuwC-uXFIMLbQDppzn7VxvsBXQYCrSla1StLG4kSwbt7RXtKMBJ_eB8m54ox4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHb6aeDkePbSMMfsxVA5LZJ-SLt6nZpI7DAkow04MMIQ-HqtRmTzdpzhgN8lOUrF9g0qwu1nyGjLfNNmUYkUrmuPm02IJBhZM9Z9NWDw_CtckjIzUV_Fl1TDDFWyK6eQ9V10PO7OwmGtOu0NeFEGWX2DSb_B0CqQKPRy-uG-PBzOXWBP3R9qY4JVnhZdA2sMyg3n18MW-LQSL92JfaXlvyRdgXic7MpDoWYEgje8m8-dE4N-vh_BvPxwQpY5zCG3QA3F48BKYqD2IaSVQoY3p2fE_zxPnuwGbenbyuvp7efbPio2f0a8vWW8bwCVEadELxfJWUBCPjKnvsWymgiw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88823" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88822">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88822" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88821">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انباء عن انفجارات في الأردن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/88821" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رشقة صاروخية أخرى تنطلق الان من إيران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88820" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88819" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
مشاهد متداولة لإطلاق صواريخ من إيران نحو أهداف معادية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88818" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
المتحدث باسم منظمة الطيران المدني الإيراني:
حالة الطيران في البلاد طبيعية، وتستمر عمليات مطار مهرآباد الدولي في طهران دون انقطاع. الرحلات والأنشطة الجوية في البلاد تجري بشكل طبيعي.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/88817" target="_blank">📅 01:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/478cd89f5e.mp4?token=ecxLpzoa25lE-nCGHTT3G6ruxwpOAf-5a9jUJqu25m-GhkQBSFOYIv7sNOaFSLYJ4LS8fVHsdc7VYydM5O-SvMk78s_E6v8aNS3xlw6fS_nlzjRsWtYFESJbu4aiJGNJla97tbED-ctXkfSbLxXakC5iSH9dj-DGzSA6-9_cAgMlUybBGB0u6SFBUegdmeIt-nx5Y_r6nQKCCZL5c7TELTTA3hRldwpyYdRn46TiTAH-Rt2YHTlwzrj5-dgEagt3vm06viE0VHd9xGlSbIZ2oVbA8RH5kt4x2HFwJCLt5IKRywrKvsRKxgn5OwCx-N5Wv5eJ3XU5Sb18TjMDPLNXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/478cd89f5e.mp4?token=ecxLpzoa25lE-nCGHTT3G6ruxwpOAf-5a9jUJqu25m-GhkQBSFOYIv7sNOaFSLYJ4LS8fVHsdc7VYydM5O-SvMk78s_E6v8aNS3xlw6fS_nlzjRsWtYFESJbu4aiJGNJla97tbED-ctXkfSbLxXakC5iSH9dj-DGzSA6-9_cAgMlUybBGB0u6SFBUegdmeIt-nx5Y_r6nQKCCZL5c7TELTTA3hRldwpyYdRn46TiTAH-Rt2YHTlwzrj5-dgEagt3vm06viE0VHd9xGlSbIZ2oVbA8RH5kt4x2HFwJCLt5IKRywrKvsRKxgn5OwCx-N5Wv5eJ3XU5Sb18TjMDPLNXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
أنباء عن إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/88816" target="_blank">📅 00:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88815">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
أنباء عن إطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/88815" target="_blank">📅 00:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQFre0G_ZxQCh1MHLqqUJl25wkaOnYj0B_mWyREp-mIR3NoJtS2ocR9hVJCd3B1NkCteDf9bNYtZy7q3CAzlcPXDleoEdUQ9GzztI-qpOHKhSbZdFSzV1Rs5w6UWTVUwMMSGH2rZkDXJaL7Z9JsJprRg-6uZMcacltTkEhrEqyIsFCTZFAbu1h0w8Q3M-ywWWCq_-Up2kwpF176inkl_6rQhIhg5s0JCOA9goJOFgPUm2hwvF7qQyTEGOj8BHRgUYcA1RAHQxLjVvkzkfJGfES1Jt-7TP6_OI2Qpn5WKQx-mw3nnrBDz4IJhYXOCPGQvPgCnLhDnPdFmNqgXCz3UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
إن اختبار عزيمتنا مرة أخرى لن يؤدي إلا إلى زيادة تكلفة إخفاقاتكم المهينة.
بلا شك، لن تمر أي جريمة دون عقاب على أي مستوى؛ بل إن رد فعل أكثر تدميراً وإيلاماً وتعليماً سيكمل سلسلة إخفاقاتكم.
انتظروا بخوف وحذر.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/88814" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/88813" target="_blank">📅 00:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwStQ4VifhHQxZHOWdoIFbKrvpQOQMwlmRjaaQvZrGBN-W6ygej0sy-QvVjQHIPEqw_L9JKG3t9aiJSnqyOVF4ep2FzbIvlcP90N2DT9TacD4JJi660o66zvvEH5BTpS8zwgNNC2FBWLNv11kIey0W_6oYc-W8iEWh0xcpbVANgJkmdu0cxA76u3QZlsw5mOXQSJL4BakzAwv5IBTubgfXjHSbfL3dx8KJZms-2yCk2SKiSgv4n50MO876hdEs83JXgfhjTeNNTdNwkNnFQIqx35E3ytDbMg7qrWGWOEzZFTqFB0boPhHlw_EXQ5U1TNszGL6pf1HfjmR-l_xng4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث بإسم الحرس الثوري: سيتم معاقبة العدو الإرهابي لعدوانه على جزيرة لارك.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/88812" target="_blank">📅 00:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">في خطاب انتخابي ومحاولة لإعادة انتخابه بالتزامن مع تراجع شعبيته.
🇮🇱
نتن ياهو: إيران تحاول استئناف برنامجها النووي، وطالما كنت في منصبي، سأمنعها من فعل ذلك مرة أخرى</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/88811" target="_blank">📅 00:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIfK4K9ToyuLUvpBdH7GA47y-jOQkzsbd_3dTWR4ML2XwBfFonKn_vAWFpdk_f3DBHfCwKKE42jkPcLxtakSaxhQ4GGmx2nkk_FAw0R3a4Jyau_I6-weL2Q6PW5Rlg2oK8JIoySG8Arv-yHz1AfMIZuL3y6wM3Ah_U4JKpQNCAOUB0hixzfrm66zr4BLDxPwGcZASWA34eNALBThfcxhyMywlkW2CuVhDLkGixEd-hqHjZKhBiMKWcLcP-fZbnyuO6LSvBZZiKNPUzi5qMYob42_DjZScKchofboxSdSW9Qg3JxBeCl9uHbaXfQ-j4epiY_zC31kfdwFecvUZZWZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري:  العدو الأمريكي - الإسرائيلي، مرة أخرى، وبسبب يأسِه من حل المشكلات الداخلية وتقليل مصداقيته بين دول المنطقة، يسعى إلى إحياء دوره المشؤوم وتبرير الرأي العام، فقام بعمل عدواني بالهجوم على جزيرة لارك، مما أدى إلى استشهاد وإصابة عدد من المقاتلين…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88810" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
شهود عيان لنايا:
ابو يمعة وعبدالله بندورة يهرعون للملاجئ وملك البحرين يرتدي بدلته العسكرية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88808" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz4CTcUEnfonOnjkk0z6KWOL7lJt50B5rHOR_lo4eIlLqkU_Mmr6vdis_tXlFSvLNCOgzJOo2ulr1b7X2iseSD3mIfR4lTNuVqd5IU7WBuDxrcLF8q4A5FW9RerySc9mFC1exkzCcbhQaqQUJy__qffKyILiebVA5M41su6uO9XkKEoDYJ0GIUjYrE8vZeTttdEYH7Nvenenh-3pykjnFCSfHiAGTx5eU68NVW71g-SKqcUWQCbRDyRNhe_fs9pUKcd6j8Wwqjtus_T3UnKZYkRFecxk-yCZzXBWhpiJz56Vv-u7Y6tjQN83O7VrdmZydSm_xyIvR7j8EUR1nTZPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88807" target="_blank">📅 23:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇯🇴
🇺🇸
‏
اعلام العدو:
الطائرة الأمريكية التي ضربت جزيرة لارك قبل ساعات قليلة انطلقت من قاعدة في الأردن.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88806" target="_blank">📅 23:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88805">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مصدر إيراني: إرتقاء شهداء جراء العدوان الأمريكي على جزيرة لارك جنوبي إيران.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88805" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88804" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8G2bww4oV-ulXarGzs7J7KRxmquu9nRpbkq8GuFjMb2o_eWYPvjHuOTHmKvkYJU9cbWlEP5_hvuTZUOpQ_nxJEycJE7_mbONScuC_BvkjDnZrKfBIfdFuh5_QUopMmTRfaZLJZ8EcGR2rvy5yH7IKsNu1bT7Zamr3dEZXdZqB6naW4JRZnHfYWObGxcSabGayl8BvIbFCga0xCc4slTdEu-tApHQQby5M--gYKdWt2I5jtssijsa2VaPrUcIva48eVVZ3b98l3kahQO6PNML0SkvwZTySS5kT_GA4YsHF47XER9-ATXMGveN-8nxaoM2RQMtlZhUU2W-QD7N36hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLbjf2GaolfZfvyDDU--r3ewo_dXZWDp3VZUM3K0qq3BE0Hl9oZAl-4cgIdbmKQ9K_oyhvH3I2ghcmvyZ1wQlNkQmEJNLQjkgvNCiu5P-sQyKstmP48eOWSjBdKMX13NNKsbGotxL2oftn9Odt0-No4iFrhPcPtQSWbs73i09F09c3EqSNyvG8B-5GdSgZF4CsNxuytzksYn-66wvfn0eiTMbkXzIVBmgORSEICguf48YaC2nCdhePXYNjajzAwB1nf8im2GqDNHkk8yhi_svjKKJCAV9EzQpPbfcpWspFbDOZc8-DD0v99-rKYprVbXLOL_MGA90rBquCKfrqxOtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🔻
‏شوهدت ناقلة نفط تعرضت لهجوم إيراني أثناء عبورها مضيق هرمز أمس، اليوم وهي متوقفة في مكانها ‏قبالة سواحل عُمان جزيرة أم الغنام.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88802" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88801" target="_blank">📅 22:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">العدو الامريكي يتبنى الهجوم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88800" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88799">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88799" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88798">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عدوان على جزيرة لارك الايرانية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88798" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88797">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370a134319.mp4?token=g3WlIFNTuC_2dVlPFXqdARSLezlm9QERwOtfsbmX2ykSbBiJWn6KN95N71EUJSx-Qb4mT1BahZhYP_mw77w90wB0aVEi76nB_vK90DKQ2RPZotH_jgGtAHVJONRnsm8vtjBXqIkLAD5rMLtBZINgZdDVzGcJ8N9a7Ntx76ScO7uL3VLIJvlhJrGcjNA0_u1AtULHqI5VQg2fR9I1t8CnWi_ishtZZQqSz6LLOxkEUK35LGx5wv8BHw_kE_4pGTnuCqSFNos4e6WtCmH23Lg6rgjkZo7BZ724TzZC6tqJzt_PEdkw5EIwmqUftfD767NMYkVwcUsKfuLK7jbAC4nibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370a134319.mp4?token=g3WlIFNTuC_2dVlPFXqdARSLezlm9QERwOtfsbmX2ykSbBiJWn6KN95N71EUJSx-Qb4mT1BahZhYP_mw77w90wB0aVEi76nB_vK90DKQ2RPZotH_jgGtAHVJONRnsm8vtjBXqIkLAD5rMLtBZINgZdDVzGcJ8N9a7Ntx76ScO7uL3VLIJvlhJrGcjNA0_u1AtULHqI5VQg2fR9I1t8CnWi_ishtZZQqSz6LLOxkEUK35LGx5wv8BHw_kE_4pGTnuCqSFNos4e6WtCmH23Lg6rgjkZo7BZ724TzZC6tqJzt_PEdkw5EIwmqUftfD767NMYkVwcUsKfuLK7jbAC4nibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: في إيران يقولون إن "بيبي" مجنون، أو أنه شخص غير عقلاني - وسيكتشفون قريبًا من هو المجنون، أو الشخص غير العقلاني الحقيقي.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88797" target="_blank">📅 22:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88796">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتن ياهو: منعناهم مرة واحدة - سنمنعهم مرة أخرى.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88796" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88795">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتن ياهو: الإيرانيون لم يتخلوا عن البرنامج النووي - نحن على يقين من أنهم يريدون استئناف برنامجهم النووي بهدف امتلاك سلاح نووي. التهديد لم يزول.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88795" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتن ياهو: لابد من اتخاذ إجراء حيال إيران. يجب إزالة التهديد الإيراني وإسقاط النظام.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88794" target="_blank">📅 22:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88793">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتن ياهو:
لابد من اتخاذ إجراء حيال إيران. يجب إزالة التهديد الإيراني وإسقاط النظام.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88793" target="_blank">📅 22:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
تقرير بحري غربي:‏
يستخدم الحرس الثوري الإيراني زوارق صغيرة لتحديد السفن العابرة لمضيق هرمز.
‏خلال عبور مضيق هرمز مؤخراً، استخدم زورق إيراني صغير كشافاً ضوئياً لتحديد هوية سفينة أخرى من خلال قراءة اسمها من هيكلها أثناء إبحارها عبر الممر العماني. وعلى إثر ذلك، نادت القوات الإيرانية السفينة باسمها، وأعلنت أنها "مُسجلة في نظامها" وتخضع للمراقبة، وأمرتها بإلغاء العبور وإلا ستواجه إجراءات قانونية.
‏إيران تعرف بالضبط من هي السفن التي تعبر عبر الممر العماني ومتى</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88792" target="_blank">📅 22:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m39f3QDPwcc6lqpcqF58l72qtZvF1b0zvGhNa4YZ7d4geMpj9rK1sRytNGg5HMbqwZSOPm7SLk3qtPDepfGGVcGJJmoqAogZHsuWRNsrzy2Rj4L4cQ8vkU1LeC0yHqBKd3JB5_9Yja8keIkw8TJ6CE_vKahoovhDNlE31JxV75VJtyVGN0_myEFpCdOtl6_zdq9g8nCcWex-Nk4X4RuzzgASs4O3jcY3hyvARWNl3xW_kuPcebwX0MvpY9IAIgrIRxBRiRdLSoEs_I0cY-A04E_KwUx3wdKruvfRUJhdGs4OfebQ91_Dj40MznXfHpW9bnAB0BqpcRP-8LfhAO5kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
على جميع الشركات الكندية التي تتعامل تجارياً مع أمريكا أن تنتقل إلى الولايات المتحدة الأمريكية فوراً. ‏كثير منها شركات غادرت البلاد منذ سنوات بسبب القيادة الأمريكية الغبية. ‏عند عودتك، لن تكون هناك رسوم جمركية!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88791" target="_blank">📅 22:03 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
