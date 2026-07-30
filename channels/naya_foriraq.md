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
<img src="https://cdn4.telesco.pe/file/ClMgDAwcwIDs63KMp_3H8KfFmE7yoLtxxWy_04Z-o-i7lc77JT_-cKdLm5BK9fz1s7Q9XIm-rcXzs5tWVOQSBPYuw4gGgTkrZzgB1DApQL1aB4mfoQWYWkKuNxlVymBS-BcljUsldLrBQShGnaq03KYnUoy8HzJjTaOxZ3flRhOsdsN_o5yayyOnkwEaBCDNDgeq7XMcuVBArDeILqoFI3Zsghs__SND9oKInhfa5ZDjrSDEOmNEyY9XGqIwN3Lhu-1YeQkJEfSHSz13oeGyeBeNPISYWdX8rIEo-dT2x6buBALNjLyoSeHAl9ZPdWTukVIh8MOdQ4wK1biUFsiTvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-86380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية تضرب الحدود العراقية الإيرانية مركزها مدينة حلبجة شمال العراق.</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/86380" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
لمعرفة خطة تحويل الطرق والمسارات البديلة لزيارة الأربعينية في العراق التي نشرها الإعلام الأمني انضموا إلى قناتنا الثانية عبر الرابط التالي.
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/86379" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇦
🇷🇺
🇵🇱
تصاعد أعمدة الدخان من حدود أوكرانيا _ بولندا بعد انفجار صاروخ كروز روسي من طراز "Kh-101.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/86378" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/86377" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام العراقي:
القوات الأمنية الرسمية هي المسؤولة حصراً عن الملف الأمني ولن تسمح بوجود أي سلاح خارج إطار الدولة".
القائد العام وجه فوراً بتكريم عوائل الشهداء وتوفير الرعاية الصحية الكاملة للجرحى، بما في ذلك نقلهم خارج العراق إذا اقتضت حالتهم الصحية"، مطالبا "بتقديم الدلائل والبراهين بشأن الادعاءات حول انطلاق اعتداءات من داخل العراق".
"الحكومة لن تسمح بأية تصرفات فردية من الداخل، وفي الوقت ذاته لن تقبل بأي انتهاك يأتي من خارج الحدود".</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86376" target="_blank">📅 11:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
زلزال بقوة 3.4 درجة ريختر يضرب محافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86375" target="_blank">📅 10:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebaAHucrttciZGV8Sz1jbRBwJwNIpHuH9DdyWIdnlE2zXuTKg3oowrc3gRiWa-jnVKsemhqgVWP5dVKsTMQ0v4N2wGmeSawHH62IwyYwUYqp1sJHrvY9tKlu_GVn-8pWvhnltd960T_qBD5RxZPmFgbgSzrc2shWsqJkf3ig1lSMLCX5JZI1PDenXUixw0aoSGG5xaeCXuIyvjlVu7sUo-m0nzf4vxKSGUKHSK5F_u55Q2pb7kGHFEYtEomm_FP0_vsFsdcDxJxo90noFZ_9B7EdHtJUmROFZ99UYj3QgqdXiv4suBcQDemOmy6RDOjn0KcPLIAok6NBCyuZDFhbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: بمشيئة الله تعالى، سيتم معاقبة المعتدين في وقت قريب.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86374" target="_blank">📅 10:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86373">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الكويت: هجوم ايراني استهدف مبنى تابعًا لإحدى الشركات الصينية مما أسفر عن مقتل أحد العاملين، وإلحاق أضرار مادية جسيمة بالمبنى.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/86373" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86372">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86372" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86371">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-dPVmMo9uKN4m799SaPj-jKM4oQSmel46rLnAyzWvYKWf099a3RFS9NjabJV-bocf3H1jbNKqMmCUg47LDIG_9FTJ1PVh-vXFRigK1DB3-0t64MmTOqsg4j-5XPsnhMHXFdu6hlymD5zm2_xYWRSuQv_64YiTZBYZwwT6B4W4CjPgQ_tooCZhJsg0eUqGiwMWjXxZNwfiCKAAj_WqyVYFc9oE3a1jGOIZTOEHQ9JlJQPlRQEllZmZ8R7VctKRXGymDI7wwCcr40LY75DproKXPYmEE16mn9_5N6pHHxaJkKGKYa1-tXKtYSAJn5tqLo_2EKrnJxWLK3-k9BtUmhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر: عدم حصر السلاح بيد الدولة لا زال يتسبب باستشهاد المجاهدين في الحشد الشعبي والقوات الأمنية بلا وجهة حق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86371" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0suQx1dH2tzCrATzVKyXNVP4SguqhWdOWPGzSTC57mDVHsGbTseThCl3p_OWj44kPW6fMN6jODf-mO5VU5F_v6d5C5BOmlhqvElJIUZ_Q4cFEO3NzW3YtuQks5q6fmNzEPI_rra-keh-rF74KtzQC6vfbkg2NiBfQ4DdP9RCy0Q8_PzJr4bIWdCMt2UIZBX8np00Zqc5v_nTykGkrIM1CdKCMjz6dVRk4_sTB93lVq6qBiPuHfwVXJe0hLKH6RqPXABfhTJTCqszep0CTuoEHPJjERSl5_O6PIbKZ7h_bwzNlBca_Qb6754OXzbtvu0jtze9F3IRCc50obqctdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار النفط بالارتفاع بعد تجدد الصراعات في الشرق الأوسط حيث وصل سعر برميل النفط الواحد إلى ما يقارب 93 دولار.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86370" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86369" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86367">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86367" target="_blank">📅 09:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86366">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8NpnJGDyu9jVRMtB8w1ZiC5DwGFOqE15XaPaWHox_oXGeT7Ka_rljnpjENsGlCATmlmSql9_q0eqpisqsZW6X00gieel8g_AFYlA-Km-uLEV2_aMVdjURuPJWRbvjYt3boZkeY6jHNNM8I_JYj1vb5FOSk01T4xPqKUgPo90wHc7Ieip62ConJC4CA9LO7bAJc_SX1lXQq8iKXqNI4CHR56feepQHNNCs1GMvtGJkA3h4kVNPb9T7BuGHmycV-kDqNHtrZm6u5z7v7MG6OnqsDRvTP9fLvnokJgx76QwQbV47SWRJ6EETD0Uz-4VFiVZIKTjiZFAt8Tc2y4Pu31zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇯🇴
بعد فشل الدفاعات الأمريكية بالتصدي للصواريخ الإيرانية ؛ تظهر بيانات الملاحة الجوية إلى أن طائرات عسكرية ألمانية وفرنسية توجهت إلى القواعد الأمريكية في الأردن لمساعدة الاحتلال الأمريكي في اعتراض الهجمات الإيرانية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86366" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86365">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86365" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86364" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
الليلة الماضية، حاولت ناقلتا نفط، استفزازًا من طيور أمريكية، مغادرة الممر غير الآمن جنوب مضيق هرمز، ولكن بعد اندلاع حريق هائل في إحداهما، عادت السفينتان أدراجهما على الفور.
مضيق هرمز أرضنا، وبحارة البحرية التابعة للحرس الثوري الإيراني يسيطرون عليه سيطرة تامة، ولن يُسمح لدخيلٍ قادمٍ من آلاف الكيلومترات بالتدخل فيه. وبعون الله تعالى، سيُعاقب المعتدي اليوم.
ستتلقى الدول المتورطة في مساعدة المعتدي ردًا قاسيًا إن لم تُصحح سلوكها.
لن يُفتح مضيق هرمز ما دامت مبالغات وتهديدات المسؤولين الأمريكيين وتدخلهم في الحركة البحرية بالمنطقة مستمرة، ولن تُؤدي التهديدات والتدخلات إلا إلى تفاقم الوضع وتعقيده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86363" target="_blank">📅 08:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86362">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثمان الشهيد ليث علك أحد شهداء العدوان الأمريكي السعودي على العراق يصل إلى دائرة الطب العدلي في محافظة ميسان لتسليمه لذويه وتشييعه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86362" target="_blank">📅 08:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86361">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=AgORI1p2Ef5s4v6qS0HoKc1MVezpTINhFqH7rwXyuBjGuM_97LEVmYM-bPSFGca3IJyxvWkcG3RLIZkgU97ZzymYuWZtszcJMI4Gd-YD6zsTR8KKJ3bLp9gYMK8qbytJ_OHN3e_3RAO__qtTLnu1yrrkhST4bPvPk3Kq2wl7Hf0Zbmv9HgChUuc3KBlqSdxrKM10ef-k-cjSXpWwgxBpFSrRfTSxxl1Y3Q5ff1lem5-Mea9WJmylaqZXC1X4N3DSlJEX9IOtliByWKoqaWcYLhVSr7AEI1kcD9N1Ap7GXgOEzTjJJWVUhZkoa1sKQ3_h5mg-BMgBYG7MBHucJ512zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=AgORI1p2Ef5s4v6qS0HoKc1MVezpTINhFqH7rwXyuBjGuM_97LEVmYM-bPSFGca3IJyxvWkcG3RLIZkgU97ZzymYuWZtszcJMI4Gd-YD6zsTR8KKJ3bLp9gYMK8qbytJ_OHN3e_3RAO__qtTLnu1yrrkhST4bPvPk3Kq2wl7Hf0Zbmv9HgChUuc3KBlqSdxrKM10ef-k-cjSXpWwgxBpFSrRfTSxxl1Y3Q5ff1lem5-Mea9WJmylaqZXC1X4N3DSlJEX9IOtliByWKoqaWcYLhVSr7AEI1kcD9N1Ap7GXgOEzTjJJWVUhZkoa1sKQ3_h5mg-BMgBYG7MBHucJ512zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لانطلاق وفشل الدفاعات الجوية في قاعدة موفق السلطي في الأردن قبل دكها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86361" target="_blank">📅 08:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86360">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86360" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86359">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86359" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86358">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
مراسل نايا |
سقوط صاروخين بشكل مباشر داخل قاعدة موفق السلطي وتصاعد أعمدة الدخان بشكل كثيف وسط فشل فادح للدفاعات الجوية الأمريكية واستمرار دوي صافرات الإنذار</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86358" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpwBvInB_3FJK9kxYVVQaLQOpOmpl2ZhCtOF-2RxUXIO23BfmPtPkNzVxxikq9mxgLU2py6YpVZitMEAB-wwZuY9jN99UXHPDZ1Gbyy0hZ9j--0C7m_N7tpHuvNX8w4Hqwt35eWqg20Xukhct_Ilkww7wefcjL2LRNQUMeK3h3GhpxHlJ3Rh1xqjHn5GpviGEKZd6jrtGzOH97PJ8QHWtiE0i5kxYZrx2ZHAHK-LybPiyY3PF-YOU28qJizhwvFkRXrR_p6NGokSaTGa43Qu-XIQcA_pvqzyAmU-BIhqecipnTbpWkYZPRvA8pjXiVXahyN0fXctZPcQVe2QiSGpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-RwMotlcnE1O2K7a7uCHQ3w7E8vNHHn-lxSkRhpswX5lX8ZwXhe1zXG0D62AoJKgDPl2HKIgZGCgVyf4V-Knmrop3_PdJXUjlSBFOh_4mKYQ_QF28QsUiHA2jyEVhuar0MEmvVNdGCh-q5iBnL_VuYWXoqu4bUUAR31dbBFU_2OoFfvo-oflFL6H-6x1KGVRSq3kntklT3MFgN1F5rgF20nP0-bMFgsq8nBehorw5iJVwcRNUMLpuUvqTrYP7GrqlKYYCcVKzzDXPHuua31rzpbEVBQb7sVQlKEb1MiRLEP0w8KaZwDCdgweiJhEbSUiFC7JJCcz5nDJCpE0zI2mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86356" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86355" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=WaxDYvMWdh__KNIquCL-E7vwShQpl_iwps14I_mDOMku7rHSQpkYtdYKT6DAZred1KF24BPG9biQyGQZ0b07rt2y_bkjP0A-TVuudmUMeQvCDD_hLZDslxU4JdvvkeTUla98XeCHWD8FzeLtgCz5k-Mf82GMLokochM3XgQl75uGr0XjLajLUZBsgf3Irmlq6PX-R0sSKuLbxkg1z-gNhcnC3YjAo_6TqGcV2AcJlndr7-HjLWSjic0qDu3YKIMLoxwVi2IAns-fnSJh-gvNoIUaJYHk9Jb82T70C9fqxSOjG6lI_GOvQGyjnQ_6mxhB2KTfMPmXnG0i05ozC8hJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=WaxDYvMWdh__KNIquCL-E7vwShQpl_iwps14I_mDOMku7rHSQpkYtdYKT6DAZred1KF24BPG9biQyGQZ0b07rt2y_bkjP0A-TVuudmUMeQvCDD_hLZDslxU4JdvvkeTUla98XeCHWD8FzeLtgCz5k-Mf82GMLokochM3XgQl75uGr0XjLajLUZBsgf3Irmlq6PX-R0sSKuLbxkg1z-gNhcnC3YjAo_6TqGcV2AcJlndr7-HjLWSjic0qDu3YKIMLoxwVi2IAns-fnSJh-gvNoIUaJYHk9Jb82T70C9fqxSOjG6lI_GOvQGyjnQ_6mxhB2KTfMPmXnG0i05ozC8hJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للاطلاق الصاروخي الإيراني المكثف الذي يدك معاقل الاحتلال الأمريكي في الأردن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86354" target="_blank">📅 07:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86353" target="_blank">📅 07:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQAKGk_xuLPLX_fgwaSFSnWUmDXNHcIWrKyrZ72s2BWMfGWBXlvQWUpkHiOsEFUslmUkbGtmJHQdRgsN6E7TKyGLYoTE3geXIAXNtWPk2b0fPGDS1k46fXPICNNKRImYyB0-dqX91Bns5lR75qEmFK-ypmNNRhcbeZaU9POQMMJYhbOU2fG8ftHZlBIVeSEMcLIbuPkJRe0-WvKMFP2wxOc4BIs7KXJz1pdV7I7uUmiLMhVBJYAuATY4CeXQ2sp4-wnCTXm95qof47EimgqFRvHD83Y-6FEou0BA0kWVfbc7vBZOkl5Er3vKKd9EssbNKSYRni3epECsBTEoJx4VfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86352" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86351" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyLKM9ZxUw-wLflPRm_QDUfKX6lNST2m8Fzm20UKIJOeDfNn7SVGrC9HRHaI1PsxCjIiiwlNJXVXVF6g5gHiGg0WLdnvBBVui5qKXsvu1CL8I8SY52u0ONoWxMUMcpEj5nb8OaT6GVV_trIUg3KTaIPCk0jFwBDHvYcXNoZrhJf7T3HejwB_M-minzlTbLSnXBSB37JF71zeRtW_79VFnkBS6uT5V47XyuG3j8L8_iEwQdtdafbx6X5TsWp2j2fesarh3viRS1uf-P0A8Y6wl_helvl8Zs_TFirXLD_E2jUIItGPFpdl6vJtXMd4Lbn7pIlK3b1Ew7zvZiJPBHLdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86350" target="_blank">📅 07:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjBq3Kg1JulHOS5eDrL4RvPB4gyPs66isMIe9jKwW_d8nIgcWvrySJDWh62FWZxChT9jVA3PCOa4Z6iH90nCwF6h_jhYuc5xzVJOfBc0Fbso_kS73cVtE3j5iX-kI9i37on-tFlWFAcUR-i4yDyuhxcP07tocynsbYdvvE0Eczqo02LOfT5zc0k3lzTGFBImcpXBoXVpofKENhJohB8aM83t1uZpOQhkLXo_2mV9uAAuWYP9FdKfwpWA2BuwiZb6L2yq9MiFRzJSVdDo03n75TYGzC1OB3rVLHYVyNIUE_1jdgGSG_uS9cV5Xn7NErN0VslBVpXItw-IOn79_vmohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجات صاروخية مكثفة تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86349" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=DpBnkjPRrQIE23cxqFdESehD1gJORQoKGz6wB3pfjcWUJrUARroyg_6JHIxANYombxJTJ7_I6gMLwOU6DOtd2bd0BYk4Nm03VLNtYKY9oRJh6dtyy_WTNDD95jRTf8V3eqXufEwUmmgLle3wyK3awFepaOg9-QkAauqgfEg2qFgR6RlQfDCKnAjqzXdaZbGNmdM8ndVP3XZ0CxWOSoHmCcPeE3XylqfkmqvbTQeOvCDqLba1Si79FXlUmUObxd2OBm1iCxzt2nvw4tw_PxlXLAsv8Oc2j8GxGE6oOZ8Yo4KYKSKh7LAGQ_94R7LctlyWYtMUhwakXFtUUpZpHQSNvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=DpBnkjPRrQIE23cxqFdESehD1gJORQoKGz6wB3pfjcWUJrUARroyg_6JHIxANYombxJTJ7_I6gMLwOU6DOtd2bd0BYk4Nm03VLNtYKY9oRJh6dtyy_WTNDD95jRTf8V3eqXufEwUmmgLle3wyK3awFepaOg9-QkAauqgfEg2qFgR6RlQfDCKnAjqzXdaZbGNmdM8ndVP3XZ0CxWOSoHmCcPeE3XylqfkmqvbTQeOvCDqLba1Si79FXlUmUObxd2OBm1iCxzt2nvw4tw_PxlXLAsv8Oc2j8GxGE6oOZ8Yo4KYKSKh7LAGQ_94R7LctlyWYtMUhwakXFtUUpZpHQSNvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن بعد تعرضها لموجة صاروخية كبيرة استهدفت قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86348" target="_blank">📅 07:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=fhMBqVaZExzmxTjTpvhc6R-v_3KskL8QezubmIYP8l6gZifKXfASN4nftnMJDEFAzMSNxRi3z2r0WRz7-NjW1go6-ER2mjGkGSoHK2MUIEa8y2csOFLkF7_26n19ZKpWrfPAI801JsHyD8iVaDwwQCM2riGMctWXVMVBoSmlOxMUia--8icf6KdhvFd9dSMj-MCvsKU9Cv7r0_LpdCGve1K4xpbgz1jxFg81ePeMU9or9_kjPI0-CFj_13vGfLAcc5lbXQ39wu6lK_xLyA2Ld_m-k6I_uPyG87EHwkPhxu0b_pYFnp0f5CzvPqZMrHK7cjR3eFDO69MBnRpgTrZn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=fhMBqVaZExzmxTjTpvhc6R-v_3KskL8QezubmIYP8l6gZifKXfASN4nftnMJDEFAzMSNxRi3z2r0WRz7-NjW1go6-ER2mjGkGSoHK2MUIEa8y2csOFLkF7_26n19ZKpWrfPAI801JsHyD8iVaDwwQCM2riGMctWXVMVBoSmlOxMUia--8icf6KdhvFd9dSMj-MCvsKU9Cv7r0_LpdCGve1K4xpbgz1jxFg81ePeMU9or9_kjPI0-CFj_13vGfLAcc5lbXQ39wu6lK_xLyA2Ld_m-k6I_uPyG87EHwkPhxu0b_pYFnp0f5CzvPqZMrHK7cjR3eFDO69MBnRpgTrZn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86347" target="_blank">📅 07:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86346" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86345" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBul0XeKidtJnUXlGbBRlaE0Ho-UxZ6R7arlYL1XGDuIsxAIggWtdguI5Dm3xD1MRLf8q4qUwYI1CwUL3_-8zd2UuEzlmWSUkZmXNjAu42vOu_N-9OzwjQDMF5W7_g4j6B8TOShXlZ73Q7qp9deZko_nHl7B5c0yWsE_JTjv_5ZhDnUW1HCG3KNmGTSKd0wYb25KdEi2LA8STQQqkQwUQBxwqdSNia7ETjDYiPkahBGufADxKhD1pB68cRN79GXA8DCfOFFFa7gxs3C54Jldqoyf0oq1S_KWY-RHOryFWAEcA0GFtObXwAC6WxEMUzcIH1CP3j1S10N36N-8zbQOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86344" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86343" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/86342" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot2X1RaaGaceh5OHR8P1STYIZkrqhc9R0k0uORGyHgWp3R7OKhU68ayMLceWmuXnK5Sw4ZLI9ExNL-Ta40TWEiey4lTbIsFhy3ErwSf4ucwscNshr5P62Hpa0o_XtaQ-vcEHiHjEEqFjlZkhgYkJvP3EyEth2wVjsbYhwi2_vXDNAsvkZlXY7jwWYnIm7TxziTZffgzI_FQ45mC-l-fAsHl_n6K-Val6Luh32p_KnHp46sCknTQP698TAYy904MxYfMsQyAsmHr4YuL4-QnlNarwJAo6O_WkdqhAW9bXwET0AZdDAcA4zKR-V_y3MH8XLwQ7nhNk2LuNFfCcfccZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86341" target="_blank">📅 07:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaLgRLwSbfKk-97JyjEbzxDAv1pL6e9OpaB5783L9JDqoOVQ50u_eY-6fai_F_Sxu3KJNoq1lPxRrSqatooSRAQtrQFu49X5ygUyZC7-PYSjGfeLAIpmjm2TmNef4uyQ04ouAnPY2yolwebaTf6F6H7KbMMmw-hP1bwtqxNJel1mWX78epc4FymVbus2fV0fco36MgnY10t8MeA-0hYSNFsko2sqWtWHRZSfioEYotp0U5Mk8zKHugVIYukHl4LYJ-PUilIxJz2LR3lsuRIqErcqDeXVN7uEo27JtYk1DeLh38bGkx1nRmdpgFfG6etx-5eXaxAZ6MHAnwYwTn8vEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/86340" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/86339" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">إطلاق صواريخ من إيران باتجاه معاقل الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86338" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5367294f98.mp4?token=QzNWREoBMOBZFOeFvakd3gQfW788g-V6GXZPzXnV89ZxYHTUHROhpVCSz_nkhXqZA3_RYClRf1oKbto-SK6dmqayME9QrfseArsUgTBeo7XjMVPoKK8lAcL-aHBbrYI6FEcbJrvuqUhUzRQWNxtQrb8I40hYuwKAFCOucPHiQxgpbZp_EXiGiF7jKTC6Dw98qB40mfqF_rAQOsD9osbvDqmmX7Htsig5JixnGP46FlNi28ykU_h6FnnRzipiUuFdPfYjrasPZJmnI7TBYslADldamU22ipZP5s3JH2ZZQpmQOTOmgr-Y8-mICYtvGBA7Ca3kQIyZXPkMT7fTpH9i2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5367294f98.mp4?token=QzNWREoBMOBZFOeFvakd3gQfW788g-V6GXZPzXnV89ZxYHTUHROhpVCSz_nkhXqZA3_RYClRf1oKbto-SK6dmqayME9QrfseArsUgTBeo7XjMVPoKK8lAcL-aHBbrYI6FEcbJrvuqUhUzRQWNxtQrb8I40hYuwKAFCOucPHiQxgpbZp_EXiGiF7jKTC6Dw98qB40mfqF_rAQOsD9osbvDqmmX7Htsig5JixnGP46FlNi28ykU_h6FnnRzipiUuFdPfYjrasPZJmnI7TBYslADldamU22ipZP5s3JH2ZZQpmQOTOmgr-Y8-mICYtvGBA7Ca3kQIyZXPkMT7fTpH9i2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران حربي مكثف في سماء محافظة ديالى العراقية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86337" target="_blank">📅 07:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86336">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=IPW6xjJMqHS-CBhrsPlLl3uQ7yg8S08HEpRP2cCFc8Ut8gGBv0_V4zlyN7B7dB-CglSE_VdXKJFST0VCiJQJyMeOpgf4R4nQLVjemZTbTeKa3wxnbUEsIa2OcjWpIVTIpNONJg-hnh1M84HyyaZhXnrtEBwX4lVAHNgSd8SgMbqdbU2zM7P3PNvh5WixegcmSb_gE-SM_FmHM5vH8jPJSvnfRk87B3lKcz0iQDcJkI1ORwCptEruTwmvrO64XHvEXJHUz3jtO0JMTjPha8rb6kR87s53LYXjP4ol37YxZsOSm3JeoJvvqIxUtYGofD1fFUjShbjACFDoMW3owatLtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=IPW6xjJMqHS-CBhrsPlLl3uQ7yg8S08HEpRP2cCFc8Ut8gGBv0_V4zlyN7B7dB-CglSE_VdXKJFST0VCiJQJyMeOpgf4R4nQLVjemZTbTeKa3wxnbUEsIa2OcjWpIVTIpNONJg-hnh1M84HyyaZhXnrtEBwX4lVAHNgSd8SgMbqdbU2zM7P3PNvh5WixegcmSb_gE-SM_FmHM5vH8jPJSvnfRk87B3lKcz0iQDcJkI1ORwCptEruTwmvrO64XHvEXJHUz3jtO0JMTjPha8rb6kR87s53LYXjP4ol37YxZsOSm3JeoJvvqIxUtYGofD1fFUjShbjACFDoMW3owatLtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
نتنياهو حول إيران:
لا أعرف ما إذا كانت الدبلوماسية غير واردة، ولكنني متشكك في طريقة عمل إيران.
إنهم يكذبون دائمًا، ويغشون دائمًا، ودائمًا ما يماطلون.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/86336" target="_blank">📅 07:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86335">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال عن مسؤول أمريكي: الضربات الأمريكية على إيران ستكون أوسع نطاقا من العمليات التي تمت في الأسابيع الأخيرة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/86335" target="_blank">📅 07:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86334">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34643c0e8.mp4?token=h1htltJ1AB_RXL_zNkbxS6_oSH8LD2Uj_fmG6XLdZwEnP4dtxFEvxFSvZqwvQsGCXc-BU3CGB58Xl3tOe9_jKlGjMGU9HPoKYjwmgYeCocaDZi7dKqYr_plsAVRV0r7XmZqjR1BlxeGvLYm5MWj1hCuy_d1lrBvrdocEuCBaBwCxvP-n39pNiitJ5HtYoT7eMRXta_k1qPi4MUJwpQw5C8QTcvoNba7ciMB8l2IrZCSZEq6-1TFkKwRHsTs2laJ9S76_kxpJFNrRLG3MLF3LY-tqGIy4SGR4zok0AZin3uSlP9nCMAxQi1AKYvSLEEBYvMd_ieEna-jEh-RsX9gdaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34643c0e8.mp4?token=h1htltJ1AB_RXL_zNkbxS6_oSH8LD2Uj_fmG6XLdZwEnP4dtxFEvxFSvZqwvQsGCXc-BU3CGB58Xl3tOe9_jKlGjMGU9HPoKYjwmgYeCocaDZi7dKqYr_plsAVRV0r7XmZqjR1BlxeGvLYm5MWj1hCuy_d1lrBvrdocEuCBaBwCxvP-n39pNiitJ5HtYoT7eMRXta_k1qPi4MUJwpQw5C8QTcvoNba7ciMB8l2IrZCSZEq6-1TFkKwRHsTs2laJ9S76_kxpJFNrRLG3MLF3LY-tqGIy4SGR4zok0AZin3uSlP9nCMAxQi1AKYvSLEEBYvMd_ieEna-jEh-RsX9gdaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇷🇺
🇵🇱
تصاعد أعمدة الدخان من حدود أوكرانيا _ بولندا بعد انفجار صاروخ كروز روسي من طراز "Kh-101.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/86334" target="_blank">📅 07:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHiHFaNa5ZX_p8ciB_w4Epeq2qNsTwx5K4UUwaGXZKVPGno8O24vjIOiPQ7-GsrpFbDiz2cryMub75c4z6f1-qFjlCjNpu-XA7AJGCyoIOOgSyca6DGZtmGiObvPC85HaN0gzyL6awZ4t32Nh5N4FvfBHDYNIJHatvfpWVzbCSmBO1Wp6NhRcjj8m1y21K7qNaf6BFQw8qOE_GeGFLDzQAe7AxRF9BcQ3F_IdeDrQYBILUX8CyUy1sN7XYgULYtN_RrlhE0tHZqWIhD9DuoRsMcO4LisSHUEJlm6hgG5_QpeeMY2Nq1EMHoQ0ZNc2XzuCfeqEcYVUM86rNu81e1pwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7452bf19ff.mp4?token=T5ne2fmm2dGFrZObuwgGj_zfhM7PXOnby07-kf6DoG7d16_EB8BWsYj7ZCatpI6eJySNLBPyQMb3mMHkur2pyuO8K_ec2HQ8eMbiX1xqylD8fR_cpFZYGXB40ZzgXZT8uKP7hcfed__o05q0s9eWb_eLCvpSfv-Kuy70htMCTNI3W7C7Iio1dJd3SGh3YW3UkVg4ci539JqjzBeHH6CR20H0Tc4YI6uz34oRe9ik8IlxWYsjLdpI_2PbIZ3QeUzOBBxc13d1zcfcs5G2VNioujEh3gokaN8m8emGtUZzo7f6XVsKVydYqqkspi1-JN9Wl-wz7I2ZcHp_JS7xoyDdvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7452bf19ff.mp4?token=T5ne2fmm2dGFrZObuwgGj_zfhM7PXOnby07-kf6DoG7d16_EB8BWsYj7ZCatpI6eJySNLBPyQMb3mMHkur2pyuO8K_ec2HQ8eMbiX1xqylD8fR_cpFZYGXB40ZzgXZT8uKP7hcfed__o05q0s9eWb_eLCvpSfv-Kuy70htMCTNI3W7C7Iio1dJd3SGh3YW3UkVg4ci539JqjzBeHH6CR20H0Tc4YI6uz34oRe9ik8IlxWYsjLdpI_2PbIZ3QeUzOBBxc13d1zcfcs5G2VNioujEh3gokaN8m8emGtUZzo7f6XVsKVydYqqkspi1-JN9Wl-wz7I2ZcHp_JS7xoyDdvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری دیگر از حمله آمریکا به شهر اهواز</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86332" target="_blank">📅 06:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86331">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24578ec2c9.mp4?token=rPGWFVVCYE-t4zLYJzGuHltPAiq6ouiDGX41UjnNosGt2kihmHc32Hncn7JWkV7V9eu1EfMbKoGHGbZ8EDX7_2cVI-x4jj99OzusSicj0nIpdyGN29QMTA3JL4lAM0LFDhnpEvdlJYTvcbdruSjQ_GVEgfP_d0k_OAmyr9cMHeVnF53b0O7oaWKfe8yD9GU5DoMtf59iQZTGY2mUTK6Vr_z04S9agTjg3omB7xFCEOH5jjIkp15VeSjEDpCDBkQHVpEO5wSg0ZqgDPPJG9r2YNiUhqApVYyyk85_JzybZkpEjDQBjbebDBiHyElcmARaHOciy9IaeXhtKudYEGLObg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24578ec2c9.mp4?token=rPGWFVVCYE-t4zLYJzGuHltPAiq6ouiDGX41UjnNosGt2kihmHc32Hncn7JWkV7V9eu1EfMbKoGHGbZ8EDX7_2cVI-x4jj99OzusSicj0nIpdyGN29QMTA3JL4lAM0LFDhnpEvdlJYTvcbdruSjQ_GVEgfP_d0k_OAmyr9cMHeVnF53b0O7oaWKfe8yD9GU5DoMtf59iQZTGY2mUTK6Vr_z04S9agTjg3omB7xFCEOH5jjIkp15VeSjEDpCDBkQHVpEO5wSg0ZqgDPPJG9r2YNiUhqApVYyyk85_JzybZkpEjDQBjbebDBiHyElcmARaHOciy9IaeXhtKudYEGLObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار عملية البحث عن محاصرين تحت الانقاض جراء عدوان أمريكي غادر على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86331" target="_blank">📅 06:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEuZHcOO9iClTHhwFLT7KI_pebgZVknTFFIOLzq5LoJ53Pnol3HkewQ4Yysr0JHRd4hvBXKC6X-vq1MCbNwu8XLfhljZKU-b27P2T1S1s5fsoLyFV85LqmIvgd7P6AHPqkcAb32cWAspRPaBFYjxYKBlaecSRwXCbxlNB2G71a4sy8EOQN8ZRZlb48Zk55PL7zk0P3VF3b7YHHvmpCdvAPBGPyT2_ZfB0RR3DcWvhOf5_-FWVLr5E0a-BHayGiTz96iNb6qyPZcEit6BOWC86TDkqq9SJ4Vf-eki-euHFB88-sxdffb3COC0W5p6FQoAtbBWBCC5X5Gawo7UI1dZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
يُظهر الرسم البياني انخفاضًا حادًا غير مسبوق في إجمالي مخزونات النفط الأمريكية ("الأربعة الكبار": الخام مع الاحتياطي الاستراتيجي، البنزين، نواتج التقطير، ووقود الطائرات) خلال عام 2026 مقارنة بالأعوام السابقة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86330" target="_blank">📅 06:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocukl-EnEwjl7PNFfJ_mljF5E-8WgY_YXXCb01B3G1JUXMrZCVdZ5uen-qPnVZj5QrAliYLOaPKYlSWLRDK9UD49btmttehDk_eGkYbiV92UtoOgfd-wREOhTbb8YwVCo1lVpjNGANjCmBp84avUsG3K0xRKR0JaSExXBm1o-2vBmkfj9QVyiMGotLt8rbJ86YSmTws1kil-uM6cT-AS532hFY5_UjjFps3KZok_3BRphhO2wAAJwmIVOQfBZbTlsffDO7yA3or8vlqwmYxk_hE8SWhI_r9s-7XJQ_wfZ0zL3Rmm7gbFa_NFvmUIFHpl0e_wPPrRV1Dz4ESEB49iMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي الغاشم على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86329" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86328">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd89ac439.mp4?token=mPL59i1SsrITdAt0Xk46FgwNTD5GKCFUgeNtJLmsk8dHjlHhwn5vLaZZorMeMpOlqGbHzSbVXsjpGdkqidjlw0YAAZrvH1yBvbshicZ232JezR8WhtpSrQnUYnM7LbxYpvB_TvjD_BgepQTlbmEBqDBGX7IpTEQSFFZBAHZuJmXmHq6r3e9FKKjRmgtxwoq6M2PntziRk94dN70Hqv_B5wAitvAoIc7JaB4ggT_2oYh2eYNrU9KCtqRF16MawHI3iliZ4xd5RswClt4R0Q4UWPdj4OQnPPWBHIOO-c7MPJXN6jXnLpkOM_HxsArBv3c36RTzM5Bo_fSm9BIXr3sx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd89ac439.mp4?token=mPL59i1SsrITdAt0Xk46FgwNTD5GKCFUgeNtJLmsk8dHjlHhwn5vLaZZorMeMpOlqGbHzSbVXsjpGdkqidjlw0YAAZrvH1yBvbshicZ232JezR8WhtpSrQnUYnM7LbxYpvB_TvjD_BgepQTlbmEBqDBGX7IpTEQSFFZBAHZuJmXmHq6r3e9FKKjRmgtxwoq6M2PntziRk94dN70Hqv_B5wAitvAoIc7JaB4ggT_2oYh2eYNrU9KCtqRF16MawHI3iliZ4xd5RswClt4R0Q4UWPdj4OQnPPWBHIOO-c7MPJXN6jXnLpkOM_HxsArBv3c36RTzM5Bo_fSm9BIXr3sx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من العدوان على مدينة الاهواز</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86328" target="_blank">📅 05:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49818ac28.mp4?token=YxGcC9nnymswpfKq_yZrKdYdsRJnVtrtoyvJ-9-1YHmkuV0g794gOh6rYlX01eSj6VX2pyD96zosDpcGB1KLRA3i2YLv17lvHQv-bv-Dux1p0vcvvCfk3E9S2GnAMGvNzWf6XrfcOqZrOrVPZKwqZDbFVJ2-3bn_M05z44NRBWLAiBkokR4Ycvnnq4VF5GNYxhB_MzSJqoTQ4tu22kiWEZqraCryTLW2hCvH88p22bXdXO3Dp7_1z6iA_G_FFU-4UTHFuQNBjAUk6qaYVZbZBsCeYilTJVxskd5GRxjYKorc27eQgz2WHwADv2HanzHHR_8GVxUmOUzWmjWfcN9gDKOebVUhrT7HbdGrs_C70RKyLqkJTey8ZiBlTTkKlIrx8cLuuJ2M1hPpSWoXu3fACWEyl93u8nlsaN5QCoLKiGaMsEVc_fJOr9zwJf3DN9Z6Ek5NBUA5HN66aCyfdJyg4QYhNX-92BWgrZToi42lGIz8qO0ZCfqQ8zImUwBJY9ofkmhwJlCD9TBfzQjkTL5sQoB65XfMckvoFpe8MxP1z5_66U-7Tva2IufiCLzB2PFf2OigfoUG3ETTycfeGHwKlmsbGVaUkVyz_J54Y2J4adJKFkTSkczQgwWlmtEwgM5661VsR0_qPyR9tXA7r0jpX3iF4BTnd47jDoyP7CMkS98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49818ac28.mp4?token=YxGcC9nnymswpfKq_yZrKdYdsRJnVtrtoyvJ-9-1YHmkuV0g794gOh6rYlX01eSj6VX2pyD96zosDpcGB1KLRA3i2YLv17lvHQv-bv-Dux1p0vcvvCfk3E9S2GnAMGvNzWf6XrfcOqZrOrVPZKwqZDbFVJ2-3bn_M05z44NRBWLAiBkokR4Ycvnnq4VF5GNYxhB_MzSJqoTQ4tu22kiWEZqraCryTLW2hCvH88p22bXdXO3Dp7_1z6iA_G_FFU-4UTHFuQNBjAUk6qaYVZbZBsCeYilTJVxskd5GRxjYKorc27eQgz2WHwADv2HanzHHR_8GVxUmOUzWmjWfcN9gDKOebVUhrT7HbdGrs_C70RKyLqkJTey8ZiBlTTkKlIrx8cLuuJ2M1hPpSWoXu3fACWEyl93u8nlsaN5QCoLKiGaMsEVc_fJOr9zwJf3DN9Z6Ek5NBUA5HN66aCyfdJyg4QYhNX-92BWgrZToi42lGIz8qO0ZCfqQ8zImUwBJY9ofkmhwJlCD9TBfzQjkTL5sQoB65XfMckvoFpe8MxP1z5_66U-7Tva2IufiCLzB2PFf2OigfoUG3ETTycfeGHwKlmsbGVaUkVyz_J54Y2J4adJKFkTSkczQgwWlmtEwgM5661VsR0_qPyR9tXA7r0jpX3iF4BTnd47jDoyP7CMkS98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الامريكي:
في تمام الساعة العاشرة مساءً بتوقيت شرق الولايات المتحدة يوم 29 يوليو/تموز، نفذت قوات القيادة المركزية الأمريكية (سنتكوم) بنجاح سلسلة من الضربات المكثفة ضد إيران ردًا على محاولة شن هجمات صاروخية على القوات الأمريكية في اليوم السابق.
وضربت أصول سنتكوم عشرات الأهداف التابعة للحرس الثوري الإسلامي في إيران، بما في ذلك مراكز قيادة عسكرية، ومنشآت صواريخ وطائرات مسيرة، ومواقع مراقبة ودفاع ساحلية، وقدرات بحرية. وهدفت هذه الضربات إلى تقليص التهديدات التي تشكلها إيران ووكلائها على القوات الأمريكية، والشحن التجاري، ودول الخليج المجاورة.
وفي 28 يوليو/تموز، أطلقت قوات الحرس الثوري الإسلامي عدة صواريخ باليستية من إيران في محاولة لشن هجوم مفاجئ على القوات الأمريكية المتمركزة في الشرق الأوسط. وقد تم اعتراض جميع الصواريخ الإيرانية بنجاح.
وينتشر حاليًا أكثر من 50 ألف جندي أمريكي في الشرق الأوسط، وهم على أهبة الاستعداد، وفي حالة تأهب قصوى، وذوي تركيز عالٍ، وقادرين على القتال.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86327" target="_blank">📅 05:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdDU6KOeI4fCUEnfz0NvjIW5uqTPWY2LF2B1-KSy4lzLSAbdVx2LW9nOPq182LkVkZJ5HXw-xlqzLqkU2XZKy5hSQg2zkl57YxQrHN5u5_Gi5X3KMYLDX__5EUolHZTTzUNtK7LzedwmelxL_3NhF3bPrp9FyTZqrZv1vg2lsilWom-PtLmY2Oqmv9A_5KxK6Qj_0Xwk6sDkr1ctel_SuVL7zA-1C0GZls5Ti79iFK3li4t3P2P4JTJVVjRROXLKRpgV3VYHB2IfZ05geMTuj1-uaoVDAgVnl1LiQ9Wo-Bvr_s1vA0WIaaPy8Aefve5In8EMylGG2eFxX0gYu4scLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86326" target="_blank">📅 05:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86325">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f794cba83.mp4?token=c4ebq3xQ39pGKhLVL2JnKt_l-3yB5EqLpPx3qVTmNdGHdTXxzJ2jkfEh-arkHWtMMfG8-cmdn-qFnV4aTYftzKLCRlz1ZxlOfPBVaP5zovqwXUckh3ihfpD8LBIa3LH0mc6OAWbCgIj7joP3g1w4f1tUlHo4TZ-Is6eLo9rcYXo9m8YldwRVBICHiJJkglpDJ3qvWeyXpyHD3OsgJTiJ50sruM6E3Wndk_mfvOsHq1aiO89XvuGcritcpZdz6r10aI05BW08GM95OTB5Mr5fudijO6omgEDxhMtfwg7Ma-cZFcjGiDuV90RlYzJR8HTXULg8Y1TrDSfA4-DqlUO_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f794cba83.mp4?token=c4ebq3xQ39pGKhLVL2JnKt_l-3yB5EqLpPx3qVTmNdGHdTXxzJ2jkfEh-arkHWtMMfG8-cmdn-qFnV4aTYftzKLCRlz1ZxlOfPBVaP5zovqwXUckh3ihfpD8LBIa3LH0mc6OAWbCgIj7joP3g1w4f1tUlHo4TZ-Is6eLo9rcYXo9m8YldwRVBICHiJJkglpDJ3qvWeyXpyHD3OsgJTiJ50sruM6E3Wndk_mfvOsHq1aiO89XvuGcritcpZdz6r10aI05BW08GM95OTB5Mr5fudijO6omgEDxhMtfwg7Ma-cZFcjGiDuV90RlYzJR8HTXULg8Y1TrDSfA4-DqlUO_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان في سماء جزيرة قشم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/86325" target="_blank">📅 05:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86324">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3204e88b4.mp4?token=KOpoaTafigvldXEFsKN3ssaeupVsGM3M1gEjbtRYF0oQdSdvzEh7eH6yvS_qooVR6S9LWc_vCWQuIPBFnx_0Wa7MlXscVMvPGc8hrbqeT1fQnK2csIRnaa4FiuJkLeSHK5C774quKQ5CEzG7cGQ0ay1W0dvZYLI1W7cTRK5bNJHbevZsnbS90ZXI-TXFzk_WwGmoOrMBPI1epa3i6iaWcuyY7YPxmqjt2Mtn-z9QNZGD7wk_fXb-s93S52ebfSnFx3bBbDGD_sC6GmKuJVdwckZ6nepweBbTCpPpGokuwLN-vMhqCM9NxJBr-9TMNcU98pMJHnzKOYZW1_71AJdI3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3204e88b4.mp4?token=KOpoaTafigvldXEFsKN3ssaeupVsGM3M1gEjbtRYF0oQdSdvzEh7eH6yvS_qooVR6S9LWc_vCWQuIPBFnx_0Wa7MlXscVMvPGc8hrbqeT1fQnK2csIRnaa4FiuJkLeSHK5C774quKQ5CEzG7cGQ0ay1W0dvZYLI1W7cTRK5bNJHbevZsnbS90ZXI-TXFzk_WwGmoOrMBPI1epa3i6iaWcuyY7YPxmqjt2Mtn-z9QNZGD7wk_fXb-s93S52ebfSnFx3bBbDGD_sC6GmKuJVdwckZ6nepweBbTCpPpGokuwLN-vMhqCM9NxJBr-9TMNcU98pMJHnzKOYZW1_71AJdI3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من العدوان على مدينة الاهواز</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86324" target="_blank">📅 05:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ZAVARTH6oI5222w29yPXbAqT7ZvahGFOZXO1rfrBlCcEgH3DoK3YbPno109HlbD4KR0z48sub4SWZga1w7qWfSlWLbv8u-Ao0AwcP_687XqB3LuHFi-hBK-Quwu1lhgYY_famdNS1KoTQTc8H8l_Lp_5nTKePSB_bU6UzjMnuMhNtBDtiTOcb7T1_90F3Ns9R9bmMsVmTsBEQMeZgSb8frFvyG8qIkWqlQd3ZMEHPgRsE0cFZLnWjMuXsl-AISUwDwcavu1nnwxjXtBuHaIYMglcwv7vJTNcHxnYmW7YuNX9aQ434yO6RiqXKqSW88VgmdyqMZDl2DYdf6g8H4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fff119810.mp4?token=beERRAOVNGmqWipeXQvSHS7I776hYUdsa7wOzjmrWWoH2f2k9vbIkg_htDRPtrI2zGjXrPLVVWL3T7ZFuJ13iSdI-7LB2qI7lJl-WALtx8heB9I5jKSRts0ZLOzexVOY8BDqXROUPRcflmHSx8A7eMi5iajjoRLXKkQbow5BeYw_QOKPYQTG1j6pDC1e-JEA6x0KtNOCECW0wLEcYaORwLZMKF0mazqewGpJARdegTKTBI6q1bQgHGAZ33IGrlG0_CFfMzwmRGjEBla7sBkUED8Hg7H6S8p2KJJ7-5LV3JLgXg14i6q4q-E6LrAOKKV6pl-3LDXRcuoWeZ3fMmKyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fff119810.mp4?token=beERRAOVNGmqWipeXQvSHS7I776hYUdsa7wOzjmrWWoH2f2k9vbIkg_htDRPtrI2zGjXrPLVVWL3T7ZFuJ13iSdI-7LB2qI7lJl-WALtx8heB9I5jKSRts0ZLOzexVOY8BDqXROUPRcflmHSx8A7eMi5iajjoRLXKkQbow5BeYw_QOKPYQTG1j6pDC1e-JEA6x0KtNOCECW0wLEcYaORwLZMKF0mazqewGpJARdegTKTBI6q1bQgHGAZ33IGrlG0_CFfMzwmRGjEBla7sBkUED8Hg7H6S8p2KJJ7-5LV3JLgXg14i6q4q-E6LrAOKKV6pl-3LDXRcuoWeZ3fMmKyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الذي طال مدينة الاهواز قبل قليل.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86322" target="_blank">📅 05:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86321">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f49cff1c.mp4?token=DppbZjdsICCVg04wjICU76ndFi7t_BL1iPuaHwb7Q6g6aLMZi9LpFQe3xcwbBtOFKXNmwNueIEPLfacfgKO949Z5lIvjEDpGk-SW1qws3RBy6AboBdK1Wg2I_b4rL9zwvGNeyNuXY_86gJ3quc6wxRY3KnqEYiusaW2muOFOIDff6WUpjXur5H6fRzAFfgB13MhZPxVWICNd3K9JgCFyCnGBdoIN7yTYC16dxs8TvOhVe7W8MS7KnQLSaj558y-E8PAXMvxbGdqJK4aks_vAIEFUoTi5MZOVfbyDI0sXhZpnZdoREbtzxS9XM5Mv4uubtdCQmHNXwQBwrJL47vkq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f49cff1c.mp4?token=DppbZjdsICCVg04wjICU76ndFi7t_BL1iPuaHwb7Q6g6aLMZi9LpFQe3xcwbBtOFKXNmwNueIEPLfacfgKO949Z5lIvjEDpGk-SW1qws3RBy6AboBdK1Wg2I_b4rL9zwvGNeyNuXY_86gJ3quc6wxRY3KnqEYiusaW2muOFOIDff6WUpjXur5H6fRzAFfgB13MhZPxVWICNd3K9JgCFyCnGBdoIN7yTYC16dxs8TvOhVe7W8MS7KnQLSaj558y-E8PAXMvxbGdqJK4aks_vAIEFUoTi5MZOVfbyDI0sXhZpnZdoREbtzxS9XM5Mv4uubtdCQmHNXwQBwrJL47vkq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86321" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86320">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">توثيق أخر من العدوان الأمريكي على مدينة الأهواز الإيرانية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86320" target="_blank">📅 05:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d82a7c0bb.mp4?token=MVwwYXWZ4ci7rTzg5A1MfM5U5WNgolsCOsqHMqjmysJl0R8FQfhqbtldfjYMfpQfe9-XdIv9qDc2lRLM1COB1thH0_fXot9ehlPDyAgAVJ9hqZLdVC7qtLOFnKphBM1_g-9brwItwjwoSBp10vL2OqEVlyJD_m2aWylcWpe5dLRwftBTYnRBlrSFz7eVtC2M3x1GKL5hR17T_KDDz1Jr5GQBukyMglUB9wz4wm6iXP7W7bUohqRBMHCqmnkWEhM3y8YxlHtv3dbziMlzSViVSW0btTEqUys-Jq25PXXZ5d9SbVLC0dltdA6J6o_4QUwc2k7LppYzqcjK1gz39r3P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d82a7c0bb.mp4?token=MVwwYXWZ4ci7rTzg5A1MfM5U5WNgolsCOsqHMqjmysJl0R8FQfhqbtldfjYMfpQfe9-XdIv9qDc2lRLM1COB1thH0_fXot9ehlPDyAgAVJ9hqZLdVC7qtLOFnKphBM1_g-9brwItwjwoSBp10vL2OqEVlyJD_m2aWylcWpe5dLRwftBTYnRBlrSFz7eVtC2M3x1GKL5hR17T_KDDz1Jr5GQBukyMglUB9wz4wm6iXP7W7bUohqRBMHCqmnkWEhM3y8YxlHtv3dbziMlzSViVSW0btTEqUys-Jq25PXXZ5d9SbVLC0dltdA6J6o_4QUwc2k7LppYzqcjK1gz39r3P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان جراء العدوان الأمريكي على مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/86319" target="_blank">📅 05:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbCLlFKnXbpMtT7HM91iU9_44RnMPpocm0CVJ0HMMo_34IbFGcBL7e4p6oLzfWHGPtSqwVfI9ojmp14FwmYzF1c5gpVYnnpTt8uXaZDGspDbzRRLcrkbfVUSrSJGgmdP6KcWOEw5K84secZyCRM6DYbTF8qeidbKW2xpwFhzjATmZD1-zvcpOjrYt1BviqIip1ATR4vxkczNW_zM2Bkrn_3bPCwFi8DbMaz2XW2DQwU6lXcIkxMBL4obe_b5Okvw1EKEPXQz4IfP7cXLBiDP_XmSoNj5mF1zoT5MJLzBkRXfPf1UE5tEOsJ1RHtcPwKbL_S8N8aioLOOww-3SF1C7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الاهواز مجدداً</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86318" target="_blank">📅 05:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86317">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات في مدينة الاهواز مجدداً</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86317" target="_blank">📅 05:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
نيويورك تايمز:
إيران ضربت سفينتي غاز طبيعي مسال في ميناء مصري. ‏إحدى هذه الشركات هي إنرجوس سالم، المملوكة لشركة أبولو.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86316" target="_blank">📅 05:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86313">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrY0F9d_HvB3KwZg73Ne1xE3Wj9yjRntyUgMNtTwGaH1-WmvnT4ffuxRE0fRkt-Yv6qHxkWS19H9Zn0jz9RNyT_4aY9hg9OQBvA4EX6bshElyaw7CrSOakDFLKK79ZXZPtxPe8aLOcsCn0uAjjaBqjabH4bk2w7RDa1PWleI05RzTLTmhAPDsSOM8rnHL4jDRGQ6jTuUg0IcbgrWCUgToRNEZq_RTuy7ClC3dAKhArclxjhfQ9j-3h8LY1bdZq17tjhS8CdlVHkh_H7laXNYWYuG0XJybMk_ELALjp5sxLNWUSfSikDBoJarOAH0BG7pM5LetlbSqnZqU7Cr1k7f4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psctdBuSXVbjDybunDyclNMU7wb8q-mvw_yNQO0Q5J_R2srYCOwjVhq9eSlc3KvTvwlsq2gnwsGSn8UiWRh6r7b-UDvixYMgXJMZEZvV1vVoVOo_APSBLkWztT6IRavVuNZhFIEp9pWjcqwAal7VTtNP42z-Wk6c__C9oWliJCagnw2J3iesaPbbkotdAD_l-Zw5EKDHQMrmm4j5Cx7pD3jW9XxIEzoSyn4UKlz7r4KsUnYf1kY1cMPs3pOa5N-1_Slcdu3v3AE9VVhgZt_BDhOzMJmvasovRcthSwnwIf1EiDLugVAuONdTR7Puk12Rc7H5DfZKGoLM6sMTIGotSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNYzWoSfu7V1yZ4bS54_kuwhOXjy_aFatzcfR_vtlS2luY9KXdEFffSZIyqfhNYjHQAwq3FkXbEU50vly7o9IommvcKzKYZ1psgKx7zNOIYJ0m97Hu7g5DOwPNfAWDTbplcA1f2XZqEEX7uYO_G4yx7awC_mapmUafj_wnM0ILcdn3kkmDryo333d10-fWTex3hOfc-IyUumYJQ9vQxpKtL7QJ-h0jBEB-a5sOcqNGSEF-TxgY7DZ6k031yO8P1x6gffQGXw5XG5FTXCKz1DibsTbPSOw4LZlIYS2KQ-TgDBJNbT57_9IIliNGhvb_DYJroA15t4H7lCL0J7A9T2Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استمرار عملية البحث عن محاصرين تحت الانقاض جراء عدوان أمريكي غادر على منطقة سكنية في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86313" target="_blank">📅 05:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cfaca84e.mp4?token=Fi1mEyfevlMYosqmDEEHU8D9jRnp_eTT0wZMqaATtStEpA_RdA4r3PGul0PYd_A-LOhWgi4l3IU1Jdp1kqQQ01a6Ix5hqeGAc76i9Po_HFCE7rqiue-Pvm1sMJflYZCHA2tOTsrHzwPVkvb0L6ysI-uVGSpYj2wXO1nCxxyplrvXlYYOF2w2XvNskJEpknkHnIf0jRq-t7M0PS77eI6sQ2pK9mcK-_02nRnYq8fUYe7-G8vhzhrmc0GIQ6ukXLT-2yThfJ07LqA-iMFrTYwgU8_oMBLaz4T0WpH9biv0_FdKHJHkJCEeenqJazdqQcSQ0B8Uoreyrdp7aZ3lN8SZDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cfaca84e.mp4?token=Fi1mEyfevlMYosqmDEEHU8D9jRnp_eTT0wZMqaATtStEpA_RdA4r3PGul0PYd_A-LOhWgi4l3IU1Jdp1kqQQ01a6Ix5hqeGAc76i9Po_HFCE7rqiue-Pvm1sMJflYZCHA2tOTsrHzwPVkvb0L6ysI-uVGSpYj2wXO1nCxxyplrvXlYYOF2w2XvNskJEpknkHnIf0jRq-t7M0PS77eI6sQ2pK9mcK-_02nRnYq8fUYe7-G8vhzhrmc0GIQ6ukXLT-2yThfJ07LqA-iMFrTYwgU8_oMBLaz4T0WpH9biv0_FdKHJHkJCEeenqJazdqQcSQ0B8Uoreyrdp7aZ3lN8SZDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر هجومًا أمريكيًا غاشم على حي سكني في جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86312" target="_blank">📅 05:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l031nLDHOvd79HiAppHn4DU9vQIHQq5VfHqjXPrcN_YyG9FHc8fsmEqOH3hdE7gyw_b2xyVzlkqVdDxxiyhdsHHWFudBi5IzT4ZdAKp5UMLJ1c_lNYccyElWEJ-8eYDw9VmQv7dlSZSiZshP5ssQdl4pDSDRjWTBplehPoGvGQC9R6eJZsl5tEaTkEQDw4IG_TXxxbr-9gny5W93xp3k0sQgm2Xmimu5HiEHigu-oZXzWbQPrdlXVdK4Y4Fs76-TWOQISsLjTCLTFtAMTJ_PqnPH4_-oki4t4n73NMhvKzlKAS2lEARqmf5U-I3jNew1nymkkV7iQrOY-j4w7Yt5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86311" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286db0489.mp4?token=upJjjfVXijuuhCtYC8a-h06ExdskmEk8KcBhdEEDUTilkKL7QAyU9jEa_WzA7TdYYywNwekSLYau0ieCgZvGsTr-Vm4FjMfPyO3qzYqrMopknGIx6WWo0gnuUPXPmKbLO8A8LLk-PJOyFanZ_J8sIgABpmXMA8loDqYnZ26IEJBovTFfAELL3cxvhHH7gn4dahjXzNqARHIPgaoFk2F2wiE0irf9U-fIuP57S97eQoCS4RiEvusHnArvjecWdRKH2VoNgzd8YQZP3jh6vtAOLw3SlQvCYoWGXdsUHKdMEH2CUYkMJ-d6BCSbel2u28ISts3kh8pG_l10kHG_jITqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات البحث عن عالقين تحت الانقاض في جزيرة قشم عقب عدوان أمريكي على منطقة سكنية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86310" target="_blank">📅 05:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=E-s09R7zKU2hWKKlNtl99rE5ygoYWHLMBdYGEjCsfH3U8_K-Jvmv98fWAGpOocjeIAsxFETIK35dDxK0m9xplQjsuE9r1f6iMApM5SnJEFMiEQ9qt-UVns6t9mKz9R8B6EYiY-e0qjlBgftzMizWmK0LSyM07xe8Ike92vQMpY7KxCHcJScmoe2ribluShru0gZ0BOOpvrTFZ-gnHFRtC4I5YneVws9ntTtrgT6BGFjxiTstYMwrfeMPmqQ3pOmSENun2Otfl0R2mlWciUZrh4VoZWD1-G2oTuhr1nibm5pr0C6IQJiDdfD7OG51X162SOQBtVjtVVjssyrprfKqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5fb69b02b.mp4?token=E-s09R7zKU2hWKKlNtl99rE5ygoYWHLMBdYGEjCsfH3U8_K-Jvmv98fWAGpOocjeIAsxFETIK35dDxK0m9xplQjsuE9r1f6iMApM5SnJEFMiEQ9qt-UVns6t9mKz9R8B6EYiY-e0qjlBgftzMizWmK0LSyM07xe8Ike92vQMpY7KxCHcJScmoe2ribluShru0gZ0BOOpvrTFZ-gnHFRtC4I5YneVws9ntTtrgT6BGFjxiTstYMwrfeMPmqQ3pOmSENun2Otfl0R2mlWciUZrh4VoZWD1-G2oTuhr1nibm5pr0C6IQJiDdfD7OG51X162SOQBtVjtVVjssyrprfKqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض منطقة سكنية في قشم الى عدوان أمريكي غاشم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/86309" target="_blank">📅 04:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تصاویری دیگر از حمله موشکی کویت به شهر آبادان در استان خوزستان ایران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86308" target="_blank">📅 04:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb907f6861.mp4?token=toZzNDGwUlG9gnYIL6-NYgDUTKWzezypgpWQKNhvxgri8c-0ixNe31j7NPndKUN-EirLIQj6gCbdh6zic2l7UtqZqfDbMj06984pUpcPZOQG1ksbJ9oVf6aAq9cc1ENOPODGmPVYOkJuLfAh75wurTLsAzxBW01zylElKzzIeWKe2IY5xDxSSQ-vvKKqgaN-rimhaQ2lyz0q1gyIsadBgYcdR9EgYWYAmFf7deQr-jLQxo27YnzO01cLPC9MKS2ZsizSuuaCzQvnjRwdCxjb1_4ZGTFF5ZHP6ulMjhq8Cx5l-mkLeRQPbgQ7BfHkH6RwbsFHAuJX6GZQVUvtPSs9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb907f6861.mp4?token=toZzNDGwUlG9gnYIL6-NYgDUTKWzezypgpWQKNhvxgri8c-0ixNe31j7NPndKUN-EirLIQj6gCbdh6zic2l7UtqZqfDbMj06984pUpcPZOQG1ksbJ9oVf6aAq9cc1ENOPODGmPVYOkJuLfAh75wurTLsAzxBW01zylElKzzIeWKe2IY5xDxSSQ-vvKKqgaN-rimhaQ2lyz0q1gyIsadBgYcdR9EgYWYAmFf7deQr-jLQxo27YnzO01cLPC9MKS2ZsizSuuaCzQvnjRwdCxjb1_4ZGTFF5ZHP6ulMjhq8Cx5l-mkLeRQPbgQ7BfHkH6RwbsFHAuJX6GZQVUvtPSs9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي أمريكي في سماء البحرين.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86307" target="_blank">📅 04:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات في مدينة الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86306" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e5b35879.mp4?token=VwAcTlGBIiZfatSmMPvKaUouDpF8WE-oRgBLWAnEwMdGtk74z00ObvxriSQzrgOh3yKpiHZom-14wxaIcNzEjiuqlWfw_FYY5LerwjHzbVQCN6qvGPusRKKcf1NkGza-qyKd_09GYVIanwYcP4IcREHN2dVRW7TcPUaQlGENEdL18vP5L3p3TmMLkxGF5odSUK_8JAcsJuw57sYR1Wf-VDJ3jL9taFE-GaJ0f7r0zKDZXOkBJi6RsClBcD0YpOadbIEyWLzJWl6-x-Qj7CQNSvV7FuFZuCveUkz075ku83Kua2AAcUQOeQFUDVmimGeqPS4T4R22PZk-6FVcTNzAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e5b35879.mp4?token=VwAcTlGBIiZfatSmMPvKaUouDpF8WE-oRgBLWAnEwMdGtk74z00ObvxriSQzrgOh3yKpiHZom-14wxaIcNzEjiuqlWfw_FYY5LerwjHzbVQCN6qvGPusRKKcf1NkGza-qyKd_09GYVIanwYcP4IcREHN2dVRW7TcPUaQlGENEdL18vP5L3p3TmMLkxGF5odSUK_8JAcsJuw57sYR1Wf-VDJ3jL9taFE-GaJ0f7r0zKDZXOkBJi6RsClBcD0YpOadbIEyWLzJWl6-x-Qj7CQNSvV7FuFZuCveUkz075ku83Kua2AAcUQOeQFUDVmimGeqPS4T4R22PZk-6FVcTNzAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادامه حملات موشكی از کویت به آبادان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86305" target="_blank">📅 04:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
الهجمات على إيران مستمرة وتستهدف مجموعة واسعة جدا من الأهداف.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86304" target="_blank">📅 04:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي على محيط مدينة شادكان جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86303" target="_blank">📅 04:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77c0e383.mp4?token=WlmvJuDRR2KHoLke0uSf7B0WmU_QcXiQS9q3Em8G-1Yz0u2QzMUGLjwr_TjROeMNoY6U-aXbZkDwZW9QMD5gbf3hZI0BO4Yhj5ByA65LP7QWJMKdWJ-Vh6cz29REiW672lPCQ73KYwhzUiISApvkmHUPRFWwLL1-qgquQBjFe6ImWxQU1nzMrkt_WewnPuMrthBelSpxwtphHsheofRUVZhiJYu1wUJDvnyG08uA0WHLj0FpREBUKnzeHS6ONBHxQzwQPMTHRQgIycQ1mz5n96D-cnIs-4PmN0O4mGFkF_a43heAn4J6gQRmuFprPxNr39CxaaKiamZdxXiCtd0ycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77c0e383.mp4?token=WlmvJuDRR2KHoLke0uSf7B0WmU_QcXiQS9q3Em8G-1Yz0u2QzMUGLjwr_TjROeMNoY6U-aXbZkDwZW9QMD5gbf3hZI0BO4Yhj5ByA65LP7QWJMKdWJ-Vh6cz29REiW672lPCQ73KYwhzUiISApvkmHUPRFWwLL1-qgquQBjFe6ImWxQU1nzMrkt_WewnPuMrthBelSpxwtphHsheofRUVZhiJYu1wUJDvnyG08uA0WHLj0FpREBUKnzeHS6ONBHxQzwQPMTHRQgIycQ1mz5n96D-cnIs-4PmN0O4mGFkF_a43heAn4J6gQRmuFprPxNr39CxaaKiamZdxXiCtd0ycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعرض منطقة سكنية في قشم الى عدوان أمريكي غاشم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86302" target="_blank">📅 04:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات في جزيرة قشم ومدينة بندرعباس مجدداً</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86301" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عدوان أمريكي غاشم على مدينة كازرون بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86300" target="_blank">📅 04:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86298">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادامه حملات موشكی از کویت به آبادان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86298" target="_blank">📅 04:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نائب محافظ خوزستان: مناطق في محيط مدينة آبادان تعرضت لهجوم صاروخي من قبل العدو الإرهابي الأمريكي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86297" target="_blank">📅 04:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الانفجارات مجدداً في آبادان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86296" target="_blank">📅 04:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مجددا صواريخ من الكويت تنطلق نحو الاراضي الإيرانية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86295" target="_blank">📅 04:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مجددا صواريخ من الكويت تنطلق نحو الاراضي الإيرانية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86294" target="_blank">📅 04:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f237080a.mp4?token=A3nwWtKMiaKxU-cmlGVAjCP-bhA35qlmwQ5J9peatj6dMrW1O6ohvu6k1Fm4QFiSmUDVwGIs9KlcibCR67085vWn0WSRFB2mZywq1u8rCIWXO7AbSbK4wNNVhW4N9rTswvbV0B5K6IGTey-gh6_Du89frveN4JtOf7KxcEOlkcyw3iKh2y6Agzg6QP2Dl8xw8-rl3hBFNCI3eMm8Go3toZS6ABmyIgmlmg2q4GpLVkpxwR_5cQ2bVQsmbSc8BPQn-W50hWFJaFCSVw7dByDewC8722IPbfwhNhHZM4AcqocFxUmsFr4H16ycFShS_EgGOMh_H0EkOOatjK-H_2omfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f237080a.mp4?token=A3nwWtKMiaKxU-cmlGVAjCP-bhA35qlmwQ5J9peatj6dMrW1O6ohvu6k1Fm4QFiSmUDVwGIs9KlcibCR67085vWn0WSRFB2mZywq1u8rCIWXO7AbSbK4wNNVhW4N9rTswvbV0B5K6IGTey-gh6_Du89frveN4JtOf7KxcEOlkcyw3iKh2y6Agzg6QP2Dl8xw8-rl3hBFNCI3eMm8Go3toZS6ABmyIgmlmg2q4GpLVkpxwR_5cQ2bVQsmbSc8BPQn-W50hWFJaFCSVw7dByDewC8722IPbfwhNhHZM4AcqocFxUmsFr4H16ycFShS_EgGOMh_H0EkOOatjK-H_2omfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة أطلقت من الكويت نحو مدينة آبادان جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86293" target="_blank">📅 04:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69adeaa37e.mp4?token=bxqLgOHSCdWHC_-2ZW76uLcu5u373nrEtTNMNqyUzpEVuUZMZhHZZygWHDexyK90zB_Z7XD8jHzsKhhuQzFrUHQHaNUYQWnE2fS7LrsV_PTzFWY9NzR_GtMKI7qzyksXna73D9X-SpgGJKEcCp-j8dy1APOHgufGAL4DrLRf0g57mxB8rJVS2kZhEFNAKkeXPe9lR-HuIUCPNDX8tnhUxdfBb8-ZTOxMKpbW5DktAF8SCIT0xa86GcjRekjOpbkiUPHOM1sXB5Ep2xZj1PUpjBljH1FducjaeB6XFQHxswcVhTN3DDXae3KHk8SYgbiBELoFc6Z9OSPzsBOKsHWNOaeFlX4-W5lediYH829RO-CN5h4-4KMtXG_LHduiixBH8yufKQHKv2AhMYE5jlLk5zYFcZiIeMFKIxdN_EhHEQXaNVrbbCGMgRyZYNa4SKl2fL6UtdTECW1xIri6KXywollbVXyM4QBsU-5t-zH2uDtmLbHXRwWp1nFBrZHOKixwFVg0GwnLPPrmychb9mQ8FFTEGt7im2HJhnsADn7GwmKn0Xj_kpaNu4Ol2wO4rH3NSMqYcZkkrmDJh6n9w6n94_Uznww2YHOaE7eBqdtiSp9Gce1QciSGEFE7cIR-s49GK4Inui5vONYw8isP-xVangVAkc9B9u6ibtJFOgmWmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69adeaa37e.mp4?token=bxqLgOHSCdWHC_-2ZW76uLcu5u373nrEtTNMNqyUzpEVuUZMZhHZZygWHDexyK90zB_Z7XD8jHzsKhhuQzFrUHQHaNUYQWnE2fS7LrsV_PTzFWY9NzR_GtMKI7qzyksXna73D9X-SpgGJKEcCp-j8dy1APOHgufGAL4DrLRf0g57mxB8rJVS2kZhEFNAKkeXPe9lR-HuIUCPNDX8tnhUxdfBb8-ZTOxMKpbW5DktAF8SCIT0xa86GcjRekjOpbkiUPHOM1sXB5Ep2xZj1PUpjBljH1FducjaeB6XFQHxswcVhTN3DDXae3KHk8SYgbiBELoFc6Z9OSPzsBOKsHWNOaeFlX4-W5lediYH829RO-CN5h4-4KMtXG_LHduiixBH8yufKQHKv2AhMYE5jlLk5zYFcZiIeMFKIxdN_EhHEQXaNVrbbCGMgRyZYNa4SKl2fL6UtdTECW1xIri6KXywollbVXyM4QBsU-5t-zH2uDtmLbHXRwWp1nFBrZHOKixwFVg0GwnLPPrmychb9mQ8FFTEGt7im2HJhnsADn7GwmKn0Xj_kpaNu4Ol2wO4rH3NSMqYcZkkrmDJh6n9w6n94_Uznww2YHOaE7eBqdtiSp9Gce1QciSGEFE7cIR-s49GK4Inui5vONYw8isP-xVangVAkc9B9u6ibtJFOgmWmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86292" target="_blank">📅 04:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86291">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/86291" target="_blank">📅 04:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صواريخ جديدة من الكويت تنطلق نحو أراضي الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86290" target="_blank">📅 04:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول أمريكي:
ترامب التقى يوم الأربعاء بوزير الدفاع السعودي الأمير خالد بن سلمان؛ نقل الوزير السعودي إلى ترامب رسالة من ولي -العهد السعودي محمد بن سلمان بشأن الحرب مع إيران والتصعيد الإقليمي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86289" target="_blank">📅 04:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86288">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر
إطلاق صواريخ نحو منطقة كيلو 20 مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86288" target="_blank">📅 04:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f16e8514.mp4?token=p5KvRQrOWm6rDE4cDOGYXTWLqcAwU7dMrrsQXFsDw3S-Dya4g6BxCX15sdNU5iV5EIzkcqjbb9MkLHFAmLERnLtxBvwQpjaM7GsHPwAJFnfb5-aUJtUZSXtEJdxuL7yYE62VfyzBoPjX3BV3ExpRBVzLh3dFaqYccD6Abqa-aJ970UYkEBJN4oRXBrXv8kBep1VLVraxXPRSp9QLxj4GErU7mXucu1AfpV0RYTJ8-4-sv2Thn6vTa0koqQE9Nk6ltWGix8LCUGmYBPlHJQeFB72zB46tu6h23iQRZc4NJssOgENLufW1s401rSfdVQ0KplxTq5aQ-Ft_K87I0xvuJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f16e8514.mp4?token=p5KvRQrOWm6rDE4cDOGYXTWLqcAwU7dMrrsQXFsDw3S-Dya4g6BxCX15sdNU5iV5EIzkcqjbb9MkLHFAmLERnLtxBvwQpjaM7GsHPwAJFnfb5-aUJtUZSXtEJdxuL7yYE62VfyzBoPjX3BV3ExpRBVzLh3dFaqYccD6Abqa-aJ970UYkEBJN4oRXBrXv8kBep1VLVraxXPRSp9QLxj4GErU7mXucu1AfpV0RYTJ8-4-sv2Thn6vTa0koqQE9Nk6ltWGix8LCUGmYBPlHJQeFB72zB46tu6h23iQRZc4NJssOgENLufW1s401rSfdVQ0KplxTq5aQ-Ft_K87I0xvuJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا
🇰🇼
🇮🇷
موجة صاروخية كبيرة أطلقت من الجانب الكويتي تجاه مدينة آبادان الإيرانية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86286" target="_blank">📅 04:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86285">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
‏بدأت القوات الأمريكية شن ضربات ضد إيران في الساعة الثامنة مساءً بتوقيت شرق الولايات المتحدة اليوم، رداً على محاولات إيران شن هجمات أمس على القوات الأمريكية في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86285" target="_blank">📅 03:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86284">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b08911d5.mp4?token=OYN22ZhNxOamuzdiHbBK_emCP2pKNc9n5PNyHALWixOE_VRXhVGqU2Rzoh6IJwyFh6gu5t4WgXwklsa5SEEp1qbWN_eYbT2BYYEYF8H5_NT0hhh587AEgaKUbsJXK5sN9xuNfVnvDj5BWJ3BMKdYjMy3UdN_e3GN5DeCxbxoJFyMol2rXGfGLrFtpWl9sII_RsQUUVA0elIBU7x6mJAHMQg2rV0jnyu00jeBMCnxsSD1PQ7gQmf8HryMhgDEEFSzDiznMSvHZgeGJXVZUN0qLThWYv6mCEx10aS-NP0l_2G7Ak4iA9lbjqinksWE5d_h8gQiMmnm2K8WUSKU-Eyjkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b08911d5.mp4?token=OYN22ZhNxOamuzdiHbBK_emCP2pKNc9n5PNyHALWixOE_VRXhVGqU2Rzoh6IJwyFh6gu5t4WgXwklsa5SEEp1qbWN_eYbT2BYYEYF8H5_NT0hhh587AEgaKUbsJXK5sN9xuNfVnvDj5BWJ3BMKdYjMy3UdN_e3GN5DeCxbxoJFyMol2rXGfGLrFtpWl9sII_RsQUUVA0elIBU7x6mJAHMQg2rV0jnyu00jeBMCnxsSD1PQ7gQmf8HryMhgDEEFSzDiznMSvHZgeGJXVZUN0qLThWYv6mCEx10aS-NP0l_2G7Ak4iA9lbjqinksWE5d_h8gQiMmnm2K8WUSKU-Eyjkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از شلیک چندین موشک از کویت به سمت ایران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86284" target="_blank">📅 03:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86283">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70000377da.mp4?token=oeldmQqRHM5Q-WTF8xkN-h-sdM8wwD7uG7Eib-FKbHCwU6XZbADCvLypOFOhqyCrHipBucQQo_mGPClfteH-CwNIOtNPvcQzHpUEpdZouqM3p4CVCiZOxzumT_H74zviGoUcAOd4VlvtS6vMP9Ix1sE5kyjj2ZXqLM1VX4zBRJOWwSUaddB_uTL2FVsF7Krn04r4sxsQ8GwnbypULRdRVcf4xSkCfgrYlbc0F2UcP8_TSmVQD854yP81tmO4fxPHmXVwsmGzJcqGcihMMAZxZ_AhvXVmIfpXZoxyaxo2QxksFUp7PBp27R1lqYtYIui1y6Vbt7UKPq6TMA8nMZmxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70000377da.mp4?token=oeldmQqRHM5Q-WTF8xkN-h-sdM8wwD7uG7Eib-FKbHCwU6XZbADCvLypOFOhqyCrHipBucQQo_mGPClfteH-CwNIOtNPvcQzHpUEpdZouqM3p4CVCiZOxzumT_H74zviGoUcAOd4VlvtS6vMP9Ix1sE5kyjj2ZXqLM1VX4zBRJOWwSUaddB_uTL2FVsF7Krn04r4sxsQ8GwnbypULRdRVcf4xSkCfgrYlbc0F2UcP8_TSmVQD854yP81tmO4fxPHmXVwsmGzJcqGcihMMAZxZ_AhvXVmIfpXZoxyaxo2QxksFUp7PBp27R1lqYtYIui1y6Vbt7UKPq6TMA8nMZmxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر لحظة إطلاق الصواريخ من الكويت تجاه الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86283" target="_blank">📅 03:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86282">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=o1AlTRTVs_XvP_KsJjQZrfHvGKExXadphEY8AF8JwFqaPA_GpFZ2KgXCCU9IbapDtvS-8Xk1FKnBEzwkpo69RO-PkkyOVr3PAbuZSDeWfNy3HkJV5QjOMKYZIRpcc9ELG0OvYTNN53Du-2qOLsJ7So_5bBgqtxiE6Cf38uX4YstODHfWSy79V6D4dyY30KHa1M1mZcAC8wR2o7x7YLJB8U3joSSZXDGKL9_2FTjRav5_l99-ujwK2GwOX_W2FE7s_LZmn29UiaEZsZWv4UnE7_S84tqWhjmUFXRUwkk9BVt-czjgXK5DpUJbf7yhyExjQrykiQzRYoej1Q-Q4yngoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d8b313.mp4?token=o1AlTRTVs_XvP_KsJjQZrfHvGKExXadphEY8AF8JwFqaPA_GpFZ2KgXCCU9IbapDtvS-8Xk1FKnBEzwkpo69RO-PkkyOVr3PAbuZSDeWfNy3HkJV5QjOMKYZIRpcc9ELG0OvYTNN53Du-2qOLsJ7So_5bBgqtxiE6Cf38uX4YstODHfWSy79V6D4dyY30KHa1M1mZcAC8wR2o7x7YLJB8U3joSSZXDGKL9_2FTjRav5_l99-ujwK2GwOX_W2FE7s_LZmn29UiaEZsZWv4UnE7_S84tqWhjmUFXRUwkk9BVt-czjgXK5DpUJbf7yhyExjQrykiQzRYoej1Q-Q4yngoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86282" target="_blank">📅 03:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86281">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عدوان أمريكي على بوشهر وبرازجان وبندرعباس وقشم جنوبي إيران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86281" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86280">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عدوان يستهدف مدينة آبادان جنوبي إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86280" target="_blank">📅 03:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86279">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات في جزيرة كيش جنوبي إيران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86279" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86278">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86278" target="_blank">📅 03:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86277">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اطلاق صواريخ من الكويت</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86277" target="_blank">📅 03:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86276">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ff8e3964.mp4?token=qgqiQANAplImRqupy1F4IeODFeG2AnhMk15v4A-2oRGbLDallbAOrnsmLaulXtPDM6D-8Y6G9t96WOCq-7o6gcInRM-0Qtyz7AuO9WO6zQOao35NlXanii6trbBToAd71L14eGu3VUaRAjSeI9AZjDTSnfrKqCyAle6NgSvTZ92PJoJbv2sdJw-mDkfxzPwLH_hjpJI7A5GHL7lf1XnUCvUczE9h3q7zPd7sgzEOSWIN_n6VigoeT1k51BEYwgG1mJbDKIp792oEDAsdsj3nnaXz91XYUxVNBO8LF4ezYue1jseDU5zfJ0tIzseLNlCvxhdTc9t5j1O0do4f0DM6eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ff8e3964.mp4?token=qgqiQANAplImRqupy1F4IeODFeG2AnhMk15v4A-2oRGbLDallbAOrnsmLaulXtPDM6D-8Y6G9t96WOCq-7o6gcInRM-0Qtyz7AuO9WO6zQOao35NlXanii6trbBToAd71L14eGu3VUaRAjSeI9AZjDTSnfrKqCyAle6NgSvTZ92PJoJbv2sdJw-mDkfxzPwLH_hjpJI7A5GHL7lf1XnUCvUczE9h3q7zPd7sgzEOSWIN_n6VigoeT1k51BEYwgG1mJbDKIp792oEDAsdsj3nnaXz91XYUxVNBO8LF4ezYue1jseDU5zfJ0tIzseLNlCvxhdTc9t5j1O0do4f0DM6eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران حربي يجوب سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86276" target="_blank">📅 03:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86275">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇦
لازال الطيران المدني يعاني في سماء السعودية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86275" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwoau0UJpj1ejDp0WPHrGNOyNGwnyLcJ03-M6TDPx5HgmZyovUf2Act_n8MNlyOd2AnqgCZUwuVzccdD9kE72ry4hn1OAGaYqCYvqNtiGHOeJzRvWZ6jJERv-TWSvRloHIBW-RYtyVgrHbtBuvTuDg_N-ffHnUnuzmxq-MW-BDpeQbr26_Duy3G_gchlsJYhSJ36yfUVKsMnpTKy9OnYD5lMpKr2XF9H7_bRe9il9BdHXs1523UYAXFGc4R7TB5_UpjxDRp_tD4pG0t4utNj545HWkmkX-Fgsgdrb__KhfaV0uRgw8NGaugTSY8Ym4yZPYIfhNO0l4NYuhsPR9o03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطيران المدني يتجنب الدخول في أجواء الرياض.  ثلاثة طائرات قادمة من نيودلهي ؛ جدة وتركيا لا تستطيع الهبوط في مطار الرياض</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86273" target="_blank">📅 03:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">إنفجارات في مدينة نورآباد بمحافظة فارس الإيرانية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86272" target="_blank">📅 02:42 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
