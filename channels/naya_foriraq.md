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
<img src="https://cdn4.telesco.pe/file/Bu24iHtvEjUJy_zTHrL41MdZFXfH9Qjo9PouDhTgXf5fk1A-1cfA0zbArS3Eg2jpCFdCRlCvVxxlOG3vDX2YwxV1sAy6hKeY4awqJi8-cG17qyM6Bl36GRxAo5YicF_4AR2jWYtCN-sCD19ts4m7AVlwA9df2PzoY4PUaKQfzv9dzY4vJ1WYHxFp5sbN2hwrT9qJ4otdfSj7VvSja3GzvKGKLqyhs-tWJ5ErVtvRyycO3ZPMnvUnYO-iti_l6EWVSwH1V4EDNeeDaT8iIORPd90rs0Nm3JaXYKDQnnZWFgD2bu2tDlflg4aIpK5kxArP8flm-hY3mm6AKeskcJPgxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 261K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-78439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
عصابات آل خليفة في البحرين:
القبض على 3 أشخاص إثر قيامهم ببيع ملابس عبر مواقع التواصل الاجتماعي ، مطبوعا عليها صورا وشعارات تحريضية ، تتضمن تمجيدا لعناصر إرهابية.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/naya_foriraq/78439" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/naya_foriraq/78438" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
أمين سرّ مقرّ تشييع قائد الثورة الإسلامية: لا توجد أيّة خطط لإقامة مراسم الجنازة في الخارج، وجميع الترتيبات جارية داخل البلاد.</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/78437" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
الإعلام العبري: في إسرائيل يوجّهون التعليمات ؛ لا نعرف عن ماذا يتحدث ترامب، نحن مندهشون. في إيران ينفون ؛ ترامب ادعى مؤخراً 38 مرة أن هناك اتفاقاً. حتى يتم نشر بيان رسمي من إيران - يجب اعتبار هذه التصريحات كذباً.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/78436" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/78435" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية تصدّي المقاومة الإسلامية بتاريخ
02-06-2026
لمحاولة آليات وجنود جيش العدو الإسرائيلي التقدّم باتجاه بلدة حدّاثا جنوبيّ لبنان بصليةٍ صاروخيّة وقذائف المدفعيّة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78434" target="_blank">📅 21:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏الكويت تبث مشاهد للحظة القصف المركب الذي استهدف مطار الكويت واسفر عن اضرار جسيمة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78433" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني:
نحن على أهبة الاستعداد للردّ بحزم على أي خطأ من جانب العدو.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/78432" target="_blank">📅 21:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
ترامب: واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/78431" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب يتراجع عن قصف ايران وتدميرها للمرة الألف بعد ان قصفها في التواصل الاجتماعي لمدة ٩٩٩ مرة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78430" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هههههههههههه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78429" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diER-FdxSLe94W1tGfDzOFr6VUpj3MyJAlW21DIbPFM_6JsFm-ysmFBN-GZdcVwf8h-jUnWl8eQQPSZf_e-TJn-sHvxgErA-HBsC_Jnbc_oHez-356-rusQgAb8EVS760Ps3-iE2JVivNwUujtWvj8CcD131dnRXkAu53z2uNu6ED4mvj1t_nZOj_l6kXlNKxCu8BvyR9RzPXGajkQB2H0F5zHVCi8KHCV6T6mo4UNTKOz0xM_OWWOSYKDnXzdZouPgag6gcIIqV9mF8nh9Pa1uTSuj9nwfQd17GFWRNDCUJ8qE3HOLKpuhlJ1JqeESkkIYcQYHgKrpYaAd6G3zjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
واستنادا إلى حقيقة أن المناقشات مع جمهورية إيران الإسلامية قد رفعت إلى أعلى مستوى من القيادة الإيرانية وتمت الموافقة عليها، فقد ألغيت، بصفتي رئيسا للولايات المتحدة الأمريكية، الضربات والتفجيرات المقررة ضد إيران هذا المساء. تمت الموافقة على المناقشات والنقاط النهائية، في كل من المفهوم والتفصيل الكبير، من قبل جميع الأطراف المعنية، بما في ذلك الولايات المتحدة وإسرائيل والمملكة العربية السعودية والإمارات العربية المتحدة وقطر وتركيا وباكستان والبحرين والكويت والأردن ومصر وغيرها. سيظل الحصار البحري ساري المفعول والتأثير الكامل حتى يتم الانتهاء من هذه الصفقة - سيتم الإعلان عن وقت ومكان التوقيع قريبا.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78428" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
أي خطأ من جانب العدو سيُقابل بردٍّ يفوق الخيال.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/78427" target="_blank">📅 20:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
انتشار فرق وعجلات الإطفاء والقوات الأمنية الأمريكية في محيط مبنى البنتاغون.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/78426" target="_blank">📅 20:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
قائد المقر المركزي لخاتم الأنبياء:
من جهة، تتحدث الولايات المتحدة عن الاتفاق والتفاوض، ومن جهة أخرى، تتصرف بخبث. هذا التناقض الصارخ بين سلوك الولايات المتحدة وخطابها هو السبب الرئيسي لانعدام الأمن في المنطقة، وقد عرّض أمن التجارة والاقتصاد الدولي والدول للخطر، ولا سيما مضيق هرمز.
‏ إن قادة الولايات المتحدة، بسبب افتقارهم إلى الفهم الصحيح للأمة الإيرانية الشريفة والشجاعة وقواتها المسلحة القوية، عالقون في حلقة مفرغة، والأكاذيب المتكررة للولايات المتحدة هي إحدى علامات ذلك.
‏ لا يمكنهم أبداً التعويض عن إذلالهم وهزائمهم المتتالية في الحرب مع إيران الإسلامية أو إخفاء نزعتهم الحربية من خلال الدعاية والحرب الإعلامية.
‏ نحذر من أنه إذا حاولت الولايات المتحدة شن هجمات ضد إيران البطلة مرة أخرى، فسوف تتلقى رداً أشد من ذي قبل، وستصبح نيران الحرب أكثر انتشاراً واتساعاً، مما يتسبب في انعدام الأمن في المنطقة.
‏ بالنظر إلى التهديدات الأمريكية الأخيرة ضد البنية التحتية النفطية الإيرانية، يُعلن أنه إما أن تكون صادرات النفط والغاز متاحة للجميع أو لن يتمكن أحد من القيام بذلك.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78425" target="_blank">📅 20:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
أمين سرّ مقرّ تشييع قائد الثورة الإسلامية:
لا توجد أيّة خطط لإقامة مراسم الجنازة في الخارج، وجميع الترتيبات جارية داخل البلاد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78424" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي يزعم:
لا يزال مضيق هرمز مفتوحًا للعبور.
تم إنشاء مسارات آمنة للسفن التجارية التي تعبر مضيق هرمز.
المسارات متاحة لجميع السفن التي لا تنتهك الحصار المفروض على إيران.
عبرت مئات السفن في الشهرين الماضيين.
القوات الأمريكية في حالة تأهب للدفاع ضد أي عدوان إيراني.
إيران لا تسيطر على مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78423" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd5e6ba15.mp4?token=RnqRrGYVGyLuO77hOfjcLBHKYjdEtlDK3g9AvLh2FRKiA_LG2TDTipL-4Q3dyDFSVJWRP73EfROiT2lKdQMGyeAOXwelsvy5N8eDZeHI8BomajQSaTo7C4HqAWK6gaU7gWBvq1eg6J9Wn9UwrtLZsdSP9YVnIZCc3CZG7OZ6wLuK0lnr6EMgbwqQMTavrTTEq7wdZkw-kXlvQy_je4M_MoCgdAKnPY-jxvBLzn5WAHJGAACsb-k7kHPLOf3WV9t2wumBDaqKWM52mQXSSzWQKponSMW5ERrV8UVf63557FqHcqxC4M-2DclDmJWfOSXonGWcgOvIMesVtqw5exx877fzsCA9Vg1gVQ00oMRd1on6onaX1UqYaleEcE0JK7fYMA1zLwEqHmVScLH0--_nTdfSDUxGXxoLZbGyKawc6qiboYLcDd-_rzH0oseSljq1KuZJzVaZO07UscIdhQfgx6QgkBvIBXfhG7jZQEIFW-K3x8skVRg9cWN622-BMn6PjVcGGDjmSy1f0ny70y0AxUjukxnnaSmVL1KKV5oHLqps50hVHunl1aitrPUTbXXSXUchPOwxlMssxL8XuOxwvd3ovNGicS-S_j3hPd1CGcju0ynuFoeMckJOtIACJRhLS9SpEU3fAyvmjMOqZ5ZHGLBKXIRp09MW6eT8TFgMCpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd5e6ba15.mp4?token=RnqRrGYVGyLuO77hOfjcLBHKYjdEtlDK3g9AvLh2FRKiA_LG2TDTipL-4Q3dyDFSVJWRP73EfROiT2lKdQMGyeAOXwelsvy5N8eDZeHI8BomajQSaTo7C4HqAWK6gaU7gWBvq1eg6J9Wn9UwrtLZsdSP9YVnIZCc3CZG7OZ6wLuK0lnr6EMgbwqQMTavrTTEq7wdZkw-kXlvQy_je4M_MoCgdAKnPY-jxvBLzn5WAHJGAACsb-k7kHPLOf3WV9t2wumBDaqKWM52mQXSSzWQKponSMW5ERrV8UVf63557FqHcqxC4M-2DclDmJWfOSXonGWcgOvIMesVtqw5exx877fzsCA9Vg1gVQ00oMRd1on6onaX1UqYaleEcE0JK7fYMA1zLwEqHmVScLH0--_nTdfSDUxGXxoLZbGyKawc6qiboYLcDd-_rzH0oseSljq1KuZJzVaZO07UscIdhQfgx6QgkBvIBXfhG7jZQEIFW-K3x8skVRg9cWN622-BMn6PjVcGGDjmSy1f0ny70y0AxUjukxnnaSmVL1KKV5oHLqps50hVHunl1aitrPUTbXXSXUchPOwxlMssxL8XuOxwvd3ovNGicS-S_j3hPd1CGcju0ynuFoeMckJOtIACJRhLS9SpEU3fAyvmjMOqZ5ZHGLBKXIRp09MW6eT8TFgMCpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إجلاء أشخاص من عدة طوابق في البنتاغون</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/78422" target="_blank">📅 19:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/216e6c3a98.mp4?token=JLztvPbleYrXN5E0yd3NsfbqX28w-8Da9KjX774LNkO2VGMRpvQpn_a7-Jm0eCX3CYv2qIPnBNU14Z6wqcbIQ3OjY63MBFSc8iw4xsv5_eIYYjqZnrIXFsSl39D0ScD5pDvMrPC-0RLBIAAJh1FLE8xl57HXZIeHqLowH0QOCskoVBsNcs6LIyYjPr6OHzkPR9KTY-5bQMM31BtuCY9bPSxb5R-LYnholdU2oid7uQCluNe3zEsRIwsuFV0S0FbqRA8IM9nLGF6Fg1wNnRBa5S-FQ40VzUBX6KD82_ZJlgm00inElnfPURX0D1ANPX-CmvYTCt4rpQwj8WYDrgvA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/216e6c3a98.mp4?token=JLztvPbleYrXN5E0yd3NsfbqX28w-8Da9KjX774LNkO2VGMRpvQpn_a7-Jm0eCX3CYv2qIPnBNU14Z6wqcbIQ3OjY63MBFSc8iw4xsv5_eIYYjqZnrIXFsSl39D0ScD5pDvMrPC-0RLBIAAJh1FLE8xl57HXZIeHqLowH0QOCskoVBsNcs6LIyYjPr6OHzkPR9KTY-5bQMM31BtuCY9bPSxb5R-LYnholdU2oid7uQCluNe3zEsRIwsuFV0S0FbqRA8IM9nLGF6Fg1wNnRBa5S-FQ40VzUBX6KD82_ZJlgm00inElnfPURX0D1ANPX-CmvYTCt4rpQwj8WYDrgvA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
السلطات الصهيونية تقرر إيقاف حركة القطارات مؤقتًا بسبب حالة الفوضى واقتحام متظاهري الحريديم للسكك الحديدية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78421" target="_blank">📅 19:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8-Ux9GVNR1WCsUUKvWj7kUdyGOKgvZbvMy9NrEQCr9-8ijSAZgEyUN3fqXfcTQx6Xgrs4kl0O7Hs76Ti_lWz_fNmRIC4NsbABKXWTODeXlYV4qg8Svns8sSbkLNwj0ZIgYYvajRyxb5QuHYsiyGM-0wfIHTzIL3Nuv4ygTKqh1JMFwE3Gp2QsTycXY4R8HcEWf8T1a57_0drZDGxrg3z7F9JNekGA1aIPvP9qUW2hhgRXfUwp6LmW6IJ13JJUYpLiX9AoA384uDwAm5cFi7cl-a6flPnTYWGKZnicsh1T-TKW0TPcRv5qlFjPszcZajaczD40UHSIan8I4iO49BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
ستعيد الاستراتيجيات الخاطئة والقرارات المتسرعة ضبط مجلس الإدارة بأكمله نحو الأسوأ، وتفجر البنية التحتية للطاقة والأسواق وتخلق مستنقعا لا نهاية له ستظل عالقا فيه لسنوات.
سترى إيران مختلفة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78420" target="_blank">📅 19:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3857e4ec6.mp4?token=IatA_8TCdXaCMzKJd5IxR9DRiedyfkd6FkfOfKxHnJu2E5NN3mqGhNBzhFTu4-wf9pWTYG7oJvuVP90vrHfn3kT_n8u0WHEyUQ4c1wY4rUHFe0HZWC-J3OFJ4p1fIweGySWTJjHzd0x65T4jCrewsdXsHcwlPqUsGfLcj9WfCT218j4s2H93fJSRfOYP6lo6z1_cdM1P3E-xtNaf2JgsTJDqCLz8qY-9s-XmDKuGFssvIAVReBD1Ud8iqw4-UAeTs512Gc-ixSXsy3IqBckkonqM5PFwx0UNP83SvmMQvhEW0zC1sDZ_uD8z72es9UsQpUPx76WJFjCAdk2oP0HkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3857e4ec6.mp4?token=IatA_8TCdXaCMzKJd5IxR9DRiedyfkd6FkfOfKxHnJu2E5NN3mqGhNBzhFTu4-wf9pWTYG7oJvuVP90vrHfn3kT_n8u0WHEyUQ4c1wY4rUHFe0HZWC-J3OFJ4p1fIweGySWTJjHzd0x65T4jCrewsdXsHcwlPqUsGfLcj9WfCT218j4s2H93fJSRfOYP6lo6z1_cdM1P3E-xtNaf2JgsTJDqCLz8qY-9s-XmDKuGFssvIAVReBD1Ud8iqw4-UAeTs512Gc-ixSXsy3IqBckkonqM5PFwx0UNP83SvmMQvhEW0zC1sDZ_uD8z72es9UsQpUPx76WJFjCAdk2oP0HkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني العراقي:
ضربتان جويتان تستهدفان مفرزة إرهابية تضم قيادياً جنوب بهرز في ديالى.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78419" target="_blank">📅 18:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38df04259a.mp4?token=MP7B6y8RFySEriNHIZ4RXAy5qPXFeQf3g4__R0UZpb02gO4q0B0YVhpDEyJO887QjfsYkdJ1L95nYZ_uGGyHfK9kJ8GCONax8p4lcyJkKaUVSjFWnGnVubODAHYCVXnHdh_MEaRvNfhtONZN82kQz9Wb2M8LEXzE6-sqM4obvu6IiPZYYRrB3NNCxQLA8DlWigiS-8T9YghVbunyFbMk7bvxIpS-HdyolLC_phzE2ZAUaF2NNqBiNuBi2n8GXQiVqrvhClAg8eZyj3vIC9F1vP3TEWLetzZ9YHrC4AD9DnREdQlaWr3PGzy5vd2gWKVr3anQ_aqMriw9Xfb0OqTsxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38df04259a.mp4?token=MP7B6y8RFySEriNHIZ4RXAy5qPXFeQf3g4__R0UZpb02gO4q0B0YVhpDEyJO887QjfsYkdJ1L95nYZ_uGGyHfK9kJ8GCONax8p4lcyJkKaUVSjFWnGnVubODAHYCVXnHdh_MEaRvNfhtONZN82kQz9Wb2M8LEXzE6-sqM4obvu6IiPZYYRrB3NNCxQLA8DlWigiS-8T9YghVbunyFbMk7bvxIpS-HdyolLC_phzE2ZAUaF2NNqBiNuBi2n8GXQiVqrvhClAg8eZyj3vIC9F1vP3TEWLetzZ9YHrC4AD9DnREdQlaWr3PGzy5vd2gWKVr3anQ_aqMriw9Xfb0OqTsxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة تستهدف مواقع المعارضة الكردية الايرانية في قضاء قوشتابا بمحافظة أربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78418" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية في جنوب إيران</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78417" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
‏المتحدث باسم البنتاغون: رصدنا مشكلة بجودة الهواء في المبنى لذلك تم إغلاقه.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78416" target="_blank">📅 18:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
‏إغلاق البنتاغون بسبب حادث أمني يتعلق بمواد خطرة مشتبه بها، ‏وفريق متخصص بالمواد الخطرة يتعامل مع الحادث.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78415" target="_blank">📅 18:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kA7nY8mtxTIzQPQ6OzPNoIZsxOcHt4TgoblnG29ny6VjJLShcJwrygcVm0qHuK9PWoB9MwWaYalBqAsr593OiwtW5Fi_5sKMI5_OrJtLvoapgVME1zNPIh1UwyRFaKRBPzGl4FGyHEk1bKXfqXvqy8svE580aYX9EChIh8iod52emG8a3YBDtsMUTk1xTL0OHbm5GgEHplu-mnyAh1iReFTSmgZHAZlDX4m5S_zyvnrAccODt9wiShwfLAzpaWcklALC9BFiTKBLEhs3ZLeeVWImnGJPL3_m8AgtpyUyX7H24ZdNRKnXy62jctt9jUpmY2nvNBr4nBh2WvRBqRoxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvoN17yGHVVnCHRJTuXrIAet2Njwkv8CttO73fwnO7bgIUeTLEXiA_jw9cCkJdE2D_7j1CSr75pu-mloTBzzPvwKpJzDAZ4jnYqxPca8Fq1h6026yGFNuaV4_UpCRAh1ZhmFdl0qbZbrCoZmNrUAJOSZ6niVu4O4PcG-wH--v6qC38P7iZwrBBTZzk2zjLLT0M-eIBFrzpnY2RUaOB7aL3_Hoc39r5Ha35E_dFcDql4hMXBJccHGPjqN5XwmBUT1xK-iRI9hq4dHuFUg2kXQQyNjdjZajSROgdA027p6TpKa25EZ5ZTaiMEJA-LcnWhbsJBElbz2vkEWMoSs6zVBAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نظام ال خليفة في البحرين يقوم بحذف تغريدة اقر فيها ان شضايا الدفاعات الامريكية سقطت على منازل المواطنين واسفرت عن اضرار وينشر تغريدة جديدة يقول فيها ان الاضرار خلفها ايران.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78413" target="_blank">📅 18:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
‏إغلاق البنتاغون بسبب حادث أمني يتعلق بمواد خطرة مشتبه بها، ‏وفريق متخصص بالمواد الخطرة يتعامل مع الحادث.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78412" target="_blank">📅 18:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=BQsJO3dLUeng1MlF1r_UBg8S3Z1h1mg-SE5xrNv6AnFJLGtVQZGr42LG-gh2xqaQEyMoyDlSGoAG2JwKzQM97QpHbMATzRQSo3igqSrVuU9MAGIfmx_zRYOJbyVEVFRVD_FXC5vVqT_4Ur7yiL1v2Ihpq3qYAb1QXPI1tQuM9x_k-02JSVQC-mHbL973zDPuv4JrJIcppWgFFmT2kdZtit2CN-b8kq9ZK_ImStqeNpFxXOyh-PgOx9Sqg1zo-7ima7xxllOu8pKSVy0AG1YsIXB2AkuyHI5a527POXhJoUsftM_rW0ZVngq1GF_5NKCbM1K-W7rlfIntbpsndcOwhiY6VvokYvGSZNTlQvsFW8e0GdyTLhlpvG6egjuDlRzuG6FLeoLdgYxM2mIceIsMVv08pXezLmOWIfeG-7ksCucVc3USk0M7xpzJlyX1QX86Hf8EXT8G-iNQP14u_Pu9eY1ETUI0_BkvuaBjxaP4RMClO4ZfXGuDuNqs5V_nhQifnyCq3O3Ok1a0CZjfC6_q8fKCuywbQrxRtxLxwtgpIlZVYSb1asgwtzsPa4X48lv4V0JCHJyyQWaJ1S9O9Q9Z3f6wu9DndmM0JYwnC8J6g0W5lXKB4k4W-V1u3drMC_qotr3Khxejq3UtCN_ZXPSYW60AwAFweU_W_P7gv9KESAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b32e9f76.mp4?token=BQsJO3dLUeng1MlF1r_UBg8S3Z1h1mg-SE5xrNv6AnFJLGtVQZGr42LG-gh2xqaQEyMoyDlSGoAG2JwKzQM97QpHbMATzRQSo3igqSrVuU9MAGIfmx_zRYOJbyVEVFRVD_FXC5vVqT_4Ur7yiL1v2Ihpq3qYAb1QXPI1tQuM9x_k-02JSVQC-mHbL973zDPuv4JrJIcppWgFFmT2kdZtit2CN-b8kq9ZK_ImStqeNpFxXOyh-PgOx9Sqg1zo-7ima7xxllOu8pKSVy0AG1YsIXB2AkuyHI5a527POXhJoUsftM_rW0ZVngq1GF_5NKCbM1K-W7rlfIntbpsndcOwhiY6VvokYvGSZNTlQvsFW8e0GdyTLhlpvG6egjuDlRzuG6FLeoLdgYxM2mIceIsMVv08pXezLmOWIfeG-7ksCucVc3USk0M7xpzJlyX1QX86Hf8EXT8G-iNQP14u_Pu9eY1ETUI0_BkvuaBjxaP4RMClO4ZfXGuDuNqs5V_nhQifnyCq3O3Ok1a0CZjfC6_q8fKCuywbQrxRtxLxwtgpIlZVYSb1asgwtzsPa4X48lv4V0JCHJyyQWaJ1S9O9Q9Z3f6wu9DndmM0JYwnC8J6g0W5lXKB4k4W-V1u3drMC_qotr3Khxejq3UtCN_ZXPSYW60AwAFweU_W_P7gv9KESAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
05-06-2026
جنود جيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78411" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAZaaZr49LDbLVQ97sRIHGbHpK1behLvrFwxm4zHL3px2mKO6qd7Q2vF1vXwLGGVr2MlTIgPQDXwmutq4Uoc7XfbOJ6-f4aG0p6xvnXI1eHwjFdjOWwlSmal38XZgpAcuX_8QFjp41HBbYSL_SXLbZFfPeOTsfLFBaIQ8Y1OwSQ_HW8U9NYfeRUr2Yn1ggR7nlKfwNsfwJ5rw2HMoLgKOqNMYbBMPdb8lKtz0xs1dCfLM7D5Cbbo_36GhFWAzKBVduNnVpFml81c3EoTM5fJB8fDme_lHbH5WtgAliulogtQbBzweoUhRn40P7QsBVwb2V2CWMAvxHIQ54_a7k0qJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تظاهرات واحداث شغب وقطع الطرق يقوم بها الحريديم في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/78410" target="_blank">📅 18:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">في خبر غير مهم
وزارة الخارجية العراقية تعرب عن إدانتها للهجمات التي تعرضت لها الاردن والبحرين والكويت
جا والهجمات التي تعرضت لها ايران؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78409" target="_blank">📅 18:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad94def5d5.mp4?token=n8m6LEzVOhD-0bfPh9IL4D4jVkwgOjO7e8bBy1dDlq55gVAHHPSoBuN5r1KWGrkfS9pS3KO-CHeVTughsKyfLHTXnHTE8EYiJKZrAGl_QCSiuEp2bc7kvOQEXZlpAsJ1Smg7HNz7dDlf4Z66o-9SOfpWy2lcCZ5YU8d0q__61LpXQpkDecVJxwWjd7q8h-dcjHxWPYz2Ud5Ngyn-eziD-WrxXoEydZbO7wsKas0YI1E9Qaz0aLMoXSMrUAdZNglqQMSN2QkPujOzGdn8PofLG05h3fG-anNqLStJnSIfvm7YSGUavd-CyU7rBC2KvRTaN9yRpH_24aJUJg9DAwbKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad94def5d5.mp4?token=n8m6LEzVOhD-0bfPh9IL4D4jVkwgOjO7e8bBy1dDlq55gVAHHPSoBuN5r1KWGrkfS9pS3KO-CHeVTughsKyfLHTXnHTE8EYiJKZrAGl_QCSiuEp2bc7kvOQEXZlpAsJ1Smg7HNz7dDlf4Z66o-9SOfpWy2lcCZ5YU8d0q__61LpXQpkDecVJxwWjd7q8h-dcjHxWPYz2Ud5Ngyn-eziD-WrxXoEydZbO7wsKas0YI1E9Qaz0aLMoXSMrUAdZNglqQMSN2QkPujOzGdn8PofLG05h3fG-anNqLStJnSIfvm7YSGUavd-CyU7rBC2KvRTaN9yRpH_24aJUJg9DAwbKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تظاهرات واحداث شغب وقطع الطرق يقوم بها الحريديم في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78408" target="_blank">📅 18:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
🇮🇷
رئيس لجنة الامن القومي في البرلما الايرانين إبراهيم عزيزي عن تهديدات ترامب:
صدورها أمر طبيعي لأنه يفتقر إلى أوراق القوة الحقيقية ترامب لم يحقق أي مكسب يذكر لا في حرب رمضان ولا خلال الأيام الأخيرة وتكبد تكاليف باهظة جداً من دون أن يجني الشعب الأميركي أي فائدة ملموسة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/78407" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تقرير CNN:
إيران تجدد أنظمة الدفاع الجوي في جزيرة خارك بينما ينقل الجيش الإيراني شحنات صواريخ. إيران وضعت ألغامًا على خط الساحل لجزيرة خارك.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78406" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78405" target="_blank">📅 17:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78404" target="_blank">📅 17:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
اسقاط طائرة مسيرة في جرود بعلبك-نحلة في لبنان من قبل حزب الله وطيران العدو يقوم باستهدافها بعد سقوطها.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78403" target="_blank">📅 17:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d49169c1.mp4?token=bUJLyufjIdnxh2lqus7kiKJAMqOoKRRlowY91BAb-DCrFKXG_a6TsiChmi7V78l-ZL7FGxY4CbA54uqr5OYv6grSnWTdqYOx1uC91qD2R11jlNebmj9GdzfDYW1abBZRoYj3LvHgBUB_OEWKf9-izSG2bgSf06q-hrr3PGIAi40oKAh8aiyqdW0JxZ14LLBOi1ESLr69RQ6-vvFV0zKNQxqUawc6nx-CvxcPb-cYU3PB7_5z3Kh4jvzo9BuHIT4J9XF_J0V7KPNygf2jgL9q7hqM_z8eW6ib3fSpTm-xIlFTjB01l8QfhEh0hZ8MUyTuhcDGB2H6tiqq5l4A-1ftAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d49169c1.mp4?token=bUJLyufjIdnxh2lqus7kiKJAMqOoKRRlowY91BAb-DCrFKXG_a6TsiChmi7V78l-ZL7FGxY4CbA54uqr5OYv6grSnWTdqYOx1uC91qD2R11jlNebmj9GdzfDYW1abBZRoYj3LvHgBUB_OEWKf9-izSG2bgSf06q-hrr3PGIAi40oKAh8aiyqdW0JxZ14LLBOi1ESLr69RQ6-vvFV0zKNQxqUawc6nx-CvxcPb-cYU3PB7_5z3Kh4jvzo9BuHIT4J9XF_J0V7KPNygf2jgL9q7hqM_z8eW6ib3fSpTm-xIlFTjB01l8QfhEh0hZ8MUyTuhcDGB2H6tiqq5l4A-1ftAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اسقاط طائرة مسيرة في جرود بعلبك-نحلة في لبنان من قبل حزب الله وطيران العدو يقوم باستهدافها بعد سقوطها.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78402" target="_blank">📅 17:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامب: لقد ألقينا 250 مليون دولار أميركي من القنابل عليهم الليلة الماضية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78401" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏وزير الخزانة الأميركي: واشنطن ستستخدم أموال إيران لتعويض أضرار حلفائنا بالخليج.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78400" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامب: أفضل الاستيلاء على جزيرة خارك لكنني لست متأكدا مما إذا كانت لدينا الرغبة في الإقدام على ذلك</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78399" target="_blank">📅 16:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامب: القصف الليلة سيكون أكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78398" target="_blank">📅 16:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
وزير الخزانة الأميركي:
واشنطن ستستخدم أموال إيران لتعويض أضرار حلفائنا بالخليج.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78397" target="_blank">📅 16:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: نهاية إيران قد حانت.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78396" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامب: سأتذكر أن "الأكراد خيبوا أملنا".</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78395" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📰
أكسيوس عن مسؤولين أمريكيين:
تهديد ترامب مجددا بقصف إيران هدفه الضغط عليها لإبداء مزيد من المرونة في المفاوضات بشأن برنامجها النووي</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78394" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب: أرسلنا الأسلحة إلى المتظاهرين الإيرانيين لكننا شعرنا بإحباط شديد من الأكراد لأنهم لم يسلموا الأسلحة للمتظاهرين</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78393" target="_blank">📅 16:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب: أريد الآن التوصل إلى اتفاق. أفضل ألا أضرب الجسور ومحطات الطاقة لكون الناس لن يستطيعون شرب الماء، أنا لا أريد فعل ذلك.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78392" target="_blank">📅 16:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامب: الإيرانيون يشعرون بالخيلاء الشديدة وقد مارسوا التنمر في الشرق الأوسط على مدى 47 عاما</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/78391" target="_blank">📅 16:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامب: إنهم يتفاوضون من أجل التوصل إلى اتفاق معنا، لكنهم متكبرين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78390" target="_blank">📅 16:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب: سأقصف ايران بشدة إذا فشلت في توقيع اتفاق</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78389" target="_blank">📅 16:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: تقوم الولايات المتحدة بتحليق طائرات فوق طهران، وهم ليس لديهم أي فكرة عن ذلك.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78388" target="_blank">📅 16:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامب: كان خياري دائمًا هو الاستيلاء على جزيرة خرج.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78387" target="_blank">📅 16:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامب: خياري هو الاستيلاء على جزيرة خرج.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78386" target="_blank">📅 16:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامب: خياري هو الاستيلاء على جزيرة خرج.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78385" target="_blank">📅 16:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">البيت الابيض يستدعي ابو محمد الجولاني للمثول امام ترامب يوم الأحد المقبل في محاولة لدفع الجولاني للصدام مع حزب الله</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/78384" target="_blank">📅 16:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بالمسيّراتٍ الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78383" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏رويترز: أسعار النفط ترتفع بعد تهديدات ترامب</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/78382" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترامب: سنستولي على جزيرة خارك وغيرها من مرافق الطاقة الإيرانية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78381" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة شديدة الليلة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78380" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfB1fFLCpCeQy3Ol-Sz9aA7-dk9xnPj1rCr6oHnoFdNesL5Z_ean2Gsjn-iHO68QzmSEhVxKZ_HzIagUQMQDWjwtn2bWxHbgumLgmsZ4hpS7bo81wghc3R-u4GGDdFqPPPcnf-CbRfzQHFbD28E9Exwutginh-bskmlwm4fChQFeABDHFx7FwpMeP7392FmaUaJeMui8n9fevVX0ehrf78z9GAIUVKeVeultx4ga1f4KDBC6WDwcTNrEwx4vrnBuhaJ1uI0DsvdqU8rtk4UoAT37QBGfVGwoZdsVqzYAqBncOCwSz6o9wZQB5VqSRyor6ulULfEQVXjPe-uRAuX4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة شديدة الليلة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78379" target="_blank">📅 15:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏴‍☠️
اذاعة جيش العدو:
مقاتلة من قوات الجيش الإسرائيلي من سلاح المدفعية أُصيبت في وقت سابق اليوم بجروح متوسطة، نتيجة انفجار محلّقة مفخخة في جنوب لبنان. تم نقل المقاتلة لتلقي العلاج في المستشفى وتم إبلاغ عائلتها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/78378" target="_blank">📅 15:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">البيت الابيض يستدعي ابو محمد الجولاني للمثول امام ترامب يوم الأحد المقبل في محاولة لدفع الجولاني للصدام مع حزب الله</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78377" target="_blank">📅 15:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
وكالة فارس عن
مصدر مقرب من فريق التفاوض
:
- إن ادعاء سي إن إن حول المفاوضات الجديدة بين إيران وأمريكا في خضم الاشتباكات فجر الخميس غير صحيح.
- أن الجمهورية الإسلامية الإيرانية تمسكت بمواقفها وخطوطها الحمراء المعلنة خلال سير المفاوضات ولم تتراجع عن مطالبها الأساسية.
- أن النص الذي أكد عليه الجانب الإيراني سابقًا لا يزال أساس مواقف طهران، ويتوقع فريق التفاوض أن يضطر الجانب الأمريكي في النهاية إلى قبول الأطر الرئيسية لذلك النص.
- الضغوط السياسية والتهديدات العسكرية الأخيرة من قبل أمريكا ناجمة عن مقاومة إيران لمطالب أمريكا غير المنطقية التي تتجاوز الاتفاقات قيد النقاش، وأضاف: «السبب الرئيسي لتصاعد الضغوط هو تمسك إيران بمواقفها في المفاوضات.»
- أن النص الذي تريده إيران، بسبب تأمين مصالح ومطالب طهران، لم يحظ حتى الآن بموافقة كاملة من الجانب الأمريكي، وهذه المسألة تعد من أهم العقبات أمام التوصل إلى تفاهم نهائي.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78376" target="_blank">📅 15:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f18740522.mp4?token=HLuAaWffiYRI99wxFadQjFJALgVwlj8VYkJmoU0dFsJufBS2Duk4JWUExVMaM8cyQIIb8_Rijb0Ej_jOj5DTSLYFdm_Dr5SqQmdECYbiiN2ET8V-Ape4KCcdMIVzCp2lDbMwn1cBHskg_xe_mV3BtxLAanhsTTRggIitv6SnP7zCIMFB3GY5_l0VsjblhSDP0zR20zLBMnziCHebcfkr5JINset0G8Npr8WQhvuA9JwpY23R1PqnQKwTuCXTKprudXWtlOiLmr_TVAXdk6f-fHwDFEa2Ne3lRT4ef8aFzpBuFomQBJD3N-v3owve925U5inYGdYnGj2EAcW9Jc0Bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f18740522.mp4?token=HLuAaWffiYRI99wxFadQjFJALgVwlj8VYkJmoU0dFsJufBS2Duk4JWUExVMaM8cyQIIb8_Rijb0Ej_jOj5DTSLYFdm_Dr5SqQmdECYbiiN2ET8V-Ape4KCcdMIVzCp2lDbMwn1cBHskg_xe_mV3BtxLAanhsTTRggIitv6SnP7zCIMFB3GY5_l0VsjblhSDP0zR20zLBMnziCHebcfkr5JINset0G8Npr8WQhvuA9JwpY23R1PqnQKwTuCXTKprudXWtlOiLmr_TVAXdk6f-fHwDFEa2Ne3lRT4ef8aFzpBuFomQBJD3N-v3owve925U5inYGdYnGj2EAcW9Jc0Bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي الارهابي:
تصرفنا ضد الناقلة غينيا بيساو أثناء محاولتها نقل النفط من إيران عبر خليج عمان. أطلقت طائرة أمريكية صاروخين من هيلفاير على غرفة محرك السفينة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78375" target="_blank">📅 15:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رغم تكرار استهداف الجيش اللبناني..
الرئيس اللبناني: لن ننسحب من المفاوضات مع اسرائيل رغم الضغوط وسنكمل الطريق حتى تحقيق مصلحة وطننا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/78374" target="_blank">📅 14:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏وزير الدفاع البريطاني يعلن استقالته إثر خلافات مع ستارمر بشأن الإنفاق الدفاعي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78373" target="_blank">📅 14:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCMakkQ1HKbMk6Zd8E7mETdpa_ouHI0u0T6OSXOWWuQBLMG10KvXTVArNXKjqI4iQn6eAzfls8JjMjHnNd2AOKoU8_5L8Uj4ZJE6Uj-mgFAHfQ-Pp_1pnOJDQlB-7Scxi4Wva01iqjqwKIpRdIbFmvdyNrQhKZPjthQOxHvKutZcryElQNGNCVsJpi-CLJE_9tx-27aiRJNnBPBxiSrFoc-wwOKl1ZDovhiBd3eE40CYluewVvCgYrkqiKxMO7EomCWWK-jGKgwLg-shKWcYQoOABQSMkpTtvkk1RsJAYv3bAwNJPe6KKckVgLKkSbrjvQWJQDx1Q2cKQQS8fmICpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محكمة جنايات الكرخ تصدر حكماً بالحبس لمدة سنة على المستشار السابق لرئيس الوزراء خالد كبيان بتهمة الاختلاس المالي</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78372" target="_blank">📅 14:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇳
الخارجية الهندية:
3 سفن هندية تعرضت لهجمات نفذتها البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78371" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الايرانية:
نظراً للتوترات التي تسببت بها القوات الأميركية المعتدية سيبقى مضيق هرمز مغلقاً حتى إشعار آخر وعلى الجهات التي حصلت على تصاريح عبور أن تتحلى بالصبر وتنتظر توجيهات جديدة منا.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/78370" target="_blank">📅 12:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78369">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📰
رويترز: إيران والولايات المتحدة لا تزالان تتفاوضان بشأن اتفاق مبدئي</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/78369" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار في سماء الأردن قرب الحدود السورية من جهة السويداء.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/78368" target="_blank">📅 11:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
وكالة فارس تنشر تفاصيل جديدة عن عملية اليوم:
نفّذت إيران خطة استخباراتية وعملياتية معقدة للهجمات التي استهدفت بعض القواعد العسكرية الأمريكية في المنطقة صباح الخميس.
🔹
ألحقت الهجمات أضرارًا جسيمة بمعدات باهظة الثمن للقوات الأمريكية، على الرغم من أن المسؤولين الأمريكيين لم يكشفوا بعد عن تفاصيل حجم هذه الأضرار.
🔹
أفاد المصدر العسكري بأن القوات الإيرانية كانت تراقب مسار وموقع طائرتين أمريكيتين كبيرتين من طراز P-8 منذ إقلاعهما. رُصدت إحدى هاتين الطائرتين من قاعدة دييغو غارسيا الجوية في وسط المحيط الهندي، والأخرى من قاعدة أمريكية في غرب أوروبا باتجاه جنوب الخليج العربي.
🔹
وبحسب معلومات قدمها هذا المصدر العسكري المطلع لمراسلنا، فقد استُهدفت مواقع هاتين الطائرتين في قاعدة الشيخ عيسى الجوية في البحرين وقاعدة علي السالم الجوية في الكويت بأسلحة إيرانية دقيقة.
🔹
أفاد مصدر آخر بأن إيران، باستخدام الاستخبارات والمراقبة الميدانية، رصدت نشر ما لا يقل عن ثلاث طائرات مقاتلة أمريكية من طراز إف-35 في أحد حظائر الطائرات بقاعدة موفق السلطاني الجوية في الأردن حتى اللحظات الأخيرة قبل إطلاق الصاروخ، ثم استهدفت الموقع الدقيق للحظيرة بصواريخ بعيدة المدى تعمل بالوقود الصلب.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/78367" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/78366" target="_blank">📅 11:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745a3cf224.mp4?token=qfXN_OrzLwo8i_IZgH60I0f9BTqrx26c_yQq3qgMDKnfweMqEukDWV5l36AtivgPlWH5odZfY9IKbS6uB4u3UOAa6OId5vgUd7NlU_GRtk5ubMfd9idbMuRQ0rpmhXeOxM71WqR4K2j_VSAjUaFJIubBzJfXycx5fHGDyUhRrJmrAmslLjGv5dL0hj6rcZ6QIuom9KlA7rO26EVp6iK2phCQGXzEtB1gxA06vK3O5cCFyL_qNPprA5IUVGsgh7oQ9nIsbbJWSNz4ofmiHOcJgUoAofalrNk8mOxg4DF0WFy8rdiLl1t7U09HCnatk8aKmTjvWEFSPGyb8j-FH-X6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745a3cf224.mp4?token=qfXN_OrzLwo8i_IZgH60I0f9BTqrx26c_yQq3qgMDKnfweMqEukDWV5l36AtivgPlWH5odZfY9IKbS6uB4u3UOAa6OId5vgUd7NlU_GRtk5ubMfd9idbMuRQ0rpmhXeOxM71WqR4K2j_VSAjUaFJIubBzJfXycx5fHGDyUhRrJmrAmslLjGv5dL0hj6rcZ6QIuom9KlA7rO26EVp6iK2phCQGXzEtB1gxA06vK3O5cCFyL_qNPprA5IUVGsgh7oQ9nIsbbJWSNz4ofmiHOcJgUoAofalrNk8mOxg4DF0WFy8rdiLl1t7U09HCnatk8aKmTjvWEFSPGyb8j-FH-X6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/78364" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وكالة فارس عن رئيس منظمة الطوارئ في طهران: إصابة 3 أشخاص بجروح في حوادث مرتبطة العدوان الأميركي</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/78363" target="_blank">📅 10:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏الجيش الأردني يعلن تعرض الأردن لهجوم ب 20 صاروخا أطلقوا من إيران فجر اليوم باتجاه منطقة الأزرق</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/78362" target="_blank">📅 10:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/78361" target="_blank">📅 10:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/78360" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
🇺🇸
🇮🇷
تاكر كارلسون يتحدث عن إيران:
لقد علمتنا الحرب في إيران أنه في الواقع، ليس الأشخاص الذين تنتخبهم هم من يملكون زمام الأمور في القضايا الكبرى. شخص آخر هو كذلك. في هذه الحالة، بنيامين نتنياهو.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/78359" target="_blank">📅 09:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVS98aNaHiivOcYGwKM5yscxOEKG8QHOVMwXmkbNnFrifan_La1h54jd2xfj4JDuDQEj9flj3tu8kys7ZLBFVKXhgLUA8g3wG_ffTaKlU0rWlkaCzhVJ9aKs9PqF1mii-1RK7AJ-xt-YcRzaCSLSqptxI_zbQ6D-pXombtcQz0UGYJp516ihslaWVf-f7xekMtqP74lEllmAqkSnLC4GjT82zWLDzct7MUCmiUQPt_WOA4SMZea-EJ5j9yFi1fmmRPH8uO9GEdtkE81PERIVLSD5Bv_nD-QV8ETuRzDI4qNtwL5Y4CeGFWblPl4QKU9jdYGlLbzcV0BGw1c4Kb48YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الداخلية البحرينية تدعي إصابة بسيطة لطفلة جراء سقوط صواريخ اعتراضية أثناء محاولة اعتراض الهجمات الإيرانية  احتراق مركبات وتضرر منازل في المنامة ومدينة حمد جراء سقوط شظايا مسيرات</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/78358" target="_blank">📅 09:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCWwozzu4nBot5CoPGk0JhfHw7K2-1W02uu--G17a5jJpwre_tiz_infpQ7zGAeMHWw4Pk9-bzs4QUbKKafhEH7CHquN7PyoobzCl_ZZHTfcGpQ44536ogaRMdPpAs4GUzBh2NRk7edCN4UtD2tWGCvsWRgiy4KZi7BUHFILDmvSnOt9lMc0UQtFzb5wOvqY9HD9SWwe74kWTmlg9HNRU1noF4Ke5PBRVSQVvK5x3WStBgvsNyWFOZcnji0WqcpzaPJuxlAPEtzw0p02Yb_0L86eYfRpCk0xx-w0pddrsOtyAyPNLivovK1bM1f-q2sQeLMiQCSlKdJSgn6qCqq9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الداخلية البحرينية تدعي إصابة بسيطة لطفلة جراء سقوط صواريخ اعتراضية أثناء محاولة اعتراض الهجمات الإيرانية
احتراق مركبات وتضرر منازل في المنامة ومدينة حمد جراء سقوط شظايا مسيرات</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/78357" target="_blank">📅 09:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسلل طيران مسير من جنوب لبنان نحو مسكاف عام</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/78356" target="_blank">📅 09:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تسلل طيران مسير من جنوب لبنان نحو مسكاف عام</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/78355" target="_blank">📅 09:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اغلاق المجال الجوي الكويتي كليا بدأ من الان الى اشعار اخر.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/78353" target="_blank">📅 09:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: في حال عدنا إلى القتال مع إيران، فإن لبنان سيتحول إلى ساحة ثانوية. ولذلك، بدأ "الجيش الإسرائيلي" بالفعل تقليص قواته في لبنان، لكننا سنشهد بالفعل اليوم هجمات إضافية في لبنان، مع الحرص على تجنب استهداف الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/78352" target="_blank">📅 09:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b906ec55b.mp4?token=QV78mu5a0mxpbC5CUpyb27qZPtArjRb2XScRgK_OCerOMDmm0Eyi6Dw6pJX2g_zrQjjUSprkEPK3W14RnliRcwm0TUgImW6caBh3GZZ3QGFTYvDYNnsIAYrmD7r_mUt0OH1H94X3PN35dzgqsjfPrc_YJ_HPFbnGKYRFP5fk_jsC7DPhgwQvPktZ6B-w2syzbn75QbcKn_RltG_YRpJJnOo_mabRIuszdx_8UupdOEEMDeUZdhebfrQkkFUSiFvZKO5ziV3fCuLpK3eK90_bp_CTCQ40XKmyzhKHH3TYDF-7ywK3fmD--ZAVhh7Vyg1r_5OeUUcM3R3GsBiqocOiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b906ec55b.mp4?token=QV78mu5a0mxpbC5CUpyb27qZPtArjRb2XScRgK_OCerOMDmm0Eyi6Dw6pJX2g_zrQjjUSprkEPK3W14RnliRcwm0TUgImW6caBh3GZZ3QGFTYvDYNnsIAYrmD7r_mUt0OH1H94X3PN35dzgqsjfPrc_YJ_HPFbnGKYRFP5fk_jsC7DPhgwQvPktZ6B-w2syzbn75QbcKn_RltG_YRpJJnOo_mabRIuszdx_8UupdOEEMDeUZdhebfrQkkFUSiFvZKO5ziV3fCuLpK3eK90_bp_CTCQ40XKmyzhKHH3TYDF-7ywK3fmD--ZAVhh7Vyg1r_5OeUUcM3R3GsBiqocOiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
غارة صهيونية تستهدف منزل مدنيين في سهل طاريا بالبقاع الأوسط شرق لبنان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/78351" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMV5thf6w0DltBmN2pjPND-IQEpCFblZnS0qIGZv9mXYX_wn2WcQuIEuTNmAYACcoGM9TTZIJJJfn18dHaGJs4BF8IvB2GQxDo5UzxkBTwH4QA4McTF2JOiBLhJhGEb2w_b1WJAZEL7z1jLsq1ufgZU4NZx1njqok5IEXvrgf9G4X_JpVtksJ6moKD4eee2VE04gkMXX9M_tYubQpQ--2ESf6e0-ORceXuEiFqjAIBNBB13Zr0MboEzJx7XtRXVt4FnUBvz5sBrKkIEz6a-lVkSFoOY8ZsBSNfK14eFet1y2kKvVw7HSjNbueFjwAVzbuWPL3gigQ9-0oyHJR9A14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران لفصائل المقاومة
العراقية
التي نزعت
لا تكونوا مثل قصة الأسد العاشق  …</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/78350" target="_blank">📅 08:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeCY1Nm4oozu_bwUcgy_ugChgh1qxd8zf_ZsEiZiJUm2iPzPILc8BKx_09aWJPDH7K2dyzEhitPQbmIE8lmvgh0sJLnUQZ8OKk8WEDPOERi7FpALSzpzdGHZsXLPKBIr_5FL5qrswtTYxTmEPlMJgocViHyZ5KP-JG6fYLoqA6iVn1fDQuajYyPdgaitbLC8xTTZ270AI68FepICiQlkPPOQqHokZNY7pMGAXeu-0YawHCNIvo8-jgJfGuKAXlsXQoZmWCYyyGGbKzuj_cu47g9211HSC7D3aZvvKoXu7mmrpjLwUAx0yEmfpE--9uRbZRPzsBoGqxEbc6syba-f9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مضيق هرمز الآن يخلو من جميع ناقلات النفط بشكل تام.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/78349" target="_blank">📅 08:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d5a664ee.mp4?token=ibVveBkRyjOe82GpdHxREYAoIuifYSG_KGJnDovKr5OZIENu308dE1ZpSJ-toz6DROzdklb8UykTbojiTs1YllyPCEQBRLV-N8eovdRHYoF3wad9alP5r7JJZagyCvupYnDnro2AWpMWCzNP1-VclkNc13A1ErBXMpgh3lQZ2B892BbZe6c9VU4JQeFPA0LQvDWI8lfNfDhO1V7IdDzNy0cdYiHGDlwLjZUMXeOOS5MQGTG6bvLqSYXLo13zyeYUy70sVyJ_FvxCnkbDsjL2Jt2d_WwZ-75WRedtweIIAzmK1AUoPoBdCsIh1_cpMnK8fubKty_9h5pejFTBkAOaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d5a664ee.mp4?token=ibVveBkRyjOe82GpdHxREYAoIuifYSG_KGJnDovKr5OZIENu308dE1ZpSJ-toz6DROzdklb8UykTbojiTs1YllyPCEQBRLV-N8eovdRHYoF3wad9alP5r7JJZagyCvupYnDnro2AWpMWCzNP1-VclkNc13A1ErBXMpgh3lQZ2B892BbZe6c9VU4JQeFPA0LQvDWI8lfNfDhO1V7IdDzNy0cdYiHGDlwLjZUMXeOOS5MQGTG6bvLqSYXLo13zyeYUy70sVyJ_FvxCnkbDsjL2Jt2d_WwZ-75WRedtweIIAzmK1AUoPoBdCsIh1_cpMnK8fubKty_9h5pejFTBkAOaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قوات الاحتلال الصهيوني تشعل النيران في أراضي المزارعين الأردنيين عند الحدود الأردنية الفلسطينية ؛ في الوقت ذاته تقوم حكومة الأردن بالدفاع عن الاحتلال وحمايته وصد الهجمات عليه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/78348" target="_blank">📅 08:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏بيان لـ22 دولة يطالبون إيران بالتوقف عن مهاجمة الأمريكيين على أراضيهم</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/78347" target="_blank">📅 07:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
توثيق يظهر بوضوح لحظة تجاوز الصواريخ الإيرانية، منظومة باتريوت الأمريكية واصابة قاعدة موفق السلطي الجوية في الأردن بشكل مباشر ودقيق.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/78346" target="_blank">📅 07:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇧🇭
البحرين تعلن تعرضها لاعتداءات جوية إيرانية جديدة</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/78345" target="_blank">📅 06:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صاروخ إيران يخط السماء الأردنية مستهدفاً القاعدة الجوية الأمريكية</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/78344" target="_blank">📅 06:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZDj02AkdeXL2bxVRx0elapnpMnA2CuyTvFJhZu5WgI5XFOJ-lieE9jn7LOVYmY7Ulqed1lBHm7DCqDHyfGgvl50iFIXR-ix0gZc9L0j-26-eOGBoQGjP49QvJzPGlgSb8caGC9W7b9RSDMgK9fBJmR5GtyhTvXkZGStKP8P8ZYyEJA6BEuv6QyuYmmKW-OkmfCAUqdZFzhL_sCQoRANBASibHNwTWE9QFjprn0xFduUORp3Iv9p7WdWcC8L3SkmfGWhpmlrvO9D_bsg9Afg90qATbn3JGAgooKnyzOnmu0BwkSMke0OmeF_fLh8Rmd9S618sxX45971-qIPkrB9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارة الاحتلال الأمريكي في الأردن:
تشير التقارير إلى وجود صواريخ أو طائرات مسيّرة أو قذائف صاروخية في الأجواء الأردنية.
يُرجى التوجه فوراً إلى مكان يوفر حماية علوية والاحتماء في مكان آمن.
ابقَ داخل المباني وانتبه إلى الإعلانات والتنبيهات الصادرة عن السلطات المحلية.
ستواصل سفارة الولايات المتحدة في الأردن متابعة الوضع وتقديم معلومات إضافية عند الحاجة.
﻿</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/78342" target="_blank">📅 06:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQB8SBjO7lfH0H5Pv7bRsbtSBQDo25qsdJXbou06rhvpwAb6nWzvzMI7YQIoK-qP0vnZgN1ciIj-yF16cjKYtnoKWVJ41qegGZgeHlhXQM58TGc-WtkyvDQCTt6jdVjIVPg2ucNoxHer2-OZurJUY83lBBsTJAR-mpejGGxwCpFh6P18W6jqhRCUjAmHt47vaDcp1IsJKCfWyaRpX8Jz-tk98mU8lfzGfoTntBHSrebLOyHJJQdps0DhshU2aR1xFPETvK_3QnirjXln-t-0mTJci2hfb1sTsNb-GRdTbn6KRrlUZ-q4ko8jI9FqO5kVuGgwnC4ZqHSffhaS0LU5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني:
إلى الشعب الإيراني المؤمن والبطل، الذي أظهر خلال أكثر من مئة يوم من الصمود في ساحات المواجهة مستوى جديدًا من الوعي والمقاومة؛
عقب ما وصفه البيان بـ”الإنجازات” التي حققها مقاتلو الإسلام فجر اليوم في مواجهة العدو الأمريكي، وبالتوكل على الله، قامت القوة الجوفضائية التابعة للحرس الثوري – ردًا على الهجمات الصاروخية للجيش الأمريكي على موقع ترفيهي ومجمع إنتاجي ومحيط ثكنة عسكرية قرب كرج ونظر آباد، إضافة إلى قاعدة محلية للحرس الثوري في بريشوا – بتنفيذ ضربة تأديبية صباح اليوم.
وأوضح البيان أن العملية نُفذت عبر 12 صاروخًا باليستيًا استهدفت مواقع تمركز مقاتلات F-35 وF-15 وF-16 الأمريكية، إلى جانب منشآت مهمة للجيش الأمريكي في القاعدة الجوية ومركز القيادة والسيطرة في الأزرق، مشيرًا إلى تدمير تلك المنشآت وعدد كبير من المقاتلات.
وأضاف البيان أن عمليات مقاتلي الإسلام ستستمر ما دامت اعتداءات العدو متواصلة.
“وما النصر إلا من عند الله العزيز الحكيم”</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/78341" target="_blank">📅 06:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13df2979dd.mp4?token=hPqblaKDzbK7W4grYlpQZd0weE8F6P2vaBtuvcsDUcmMm9S4K-BlFUXIv3rtIk8zpzscdzC1oQUS9TgAUq-TkeLjyJactAHZ_e7Rg_ve52oT4QeYFtPzAyUnzs-Ak-9LzPgG1bFCz3F3_p1vBZilmIUnKUEbKb1KYsANuf-g1pnpgf6OHQOQt3y5HGC0Z2L3_aG6AbWApdsl7T72jVDcS9A0fFVupnmGYdNM74r691tx-4XAc6hTl-k-NYFXyX2hj05Eqn266PmvMMb8YNM-pLnTfggDycmSAiuMTG4ixwtd7ggQZqTqPE1Jr353qPvfZVNsNnmsugxZyuhmmE0WDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13df2979dd.mp4?token=hPqblaKDzbK7W4grYlpQZd0weE8F6P2vaBtuvcsDUcmMm9S4K-BlFUXIv3rtIk8zpzscdzC1oQUS9TgAUq-TkeLjyJactAHZ_e7Rg_ve52oT4QeYFtPzAyUnzs-Ak-9LzPgG1bFCz3F3_p1vBZilmIUnKUEbKb1KYsANuf-g1pnpgf6OHQOQt3y5HGC0Z2L3_aG6AbWApdsl7T72jVDcS9A0fFVupnmGYdNM74r691tx-4XAc6hTl-k-NYFXyX2hj05Eqn266PmvMMb8YNM-pLnTfggDycmSAiuMTG4ixwtd7ggQZqTqPE1Jr353qPvfZVNsNnmsugxZyuhmmE0WDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات شاهد ١٣٦ الحيدرية في سماء الكويت باتجاه القواعد الاميركية</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/78340" target="_blank">📅 06:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/78339" target="_blank">📅 06:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d8e15dba.mp4?token=I-Hq_BLgucvYA7YDR1ySbxc3uaYe2a45vyKEMfTbcHH9oyDMsSiImzzaUIQ_D9PBjBjvPq07J7Jd3q0W78wsOvETfVOe6wr--qqEfYHHmi7BG-9k-Bpf90EJAab31QcQx509ncecCwnree2tvKDH50xZcIJcHcv4hwNDXHWuBdwCUg2nZj1q_WQXxX-zSoDy3SGaAkW_ePEuzCeQ6Nhe83JNQW-ugLEutGs9AyZE2q8NjxI1rMzmlCXc4-YMkHXzd-r09rJGA5mbIiOqO7xuWZVrpbf9OeXc02zZUPFh4NVcxs0DaVSYXPM3txu3f5rvo-ksJZi4ZOIPdCrpUkN2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d8e15dba.mp4?token=I-Hq_BLgucvYA7YDR1ySbxc3uaYe2a45vyKEMfTbcHH9oyDMsSiImzzaUIQ_D9PBjBjvPq07J7Jd3q0W78wsOvETfVOe6wr--qqEfYHHmi7BG-9k-Bpf90EJAab31QcQx509ncecCwnree2tvKDH50xZcIJcHcv4hwNDXHWuBdwCUg2nZj1q_WQXxX-zSoDy3SGaAkW_ePEuzCeQ6Nhe83JNQW-ugLEutGs9AyZE2q8NjxI1rMzmlCXc4-YMkHXzd-r09rJGA5mbIiOqO7xuWZVrpbf9OeXc02zZUPFh4NVcxs0DaVSYXPM3txu3f5rvo-ksJZi4ZOIPdCrpUkN2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق تصدي الدفاعات الجوية الإسرائيلية لصواريخ ايرانية في اجواء محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/78338" target="_blank">📅 06:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa610bcbe1.mp4?token=IA1EmXZkbGT68-8gXgzWF8_oDubfL28ZDBmcpZht6v7hNltMcM74-hEKiqEZ0r5CS1MCbMgtmGpUZOGkobs43hMI23HQ6e8RjhSQXh6ygkvl4691YpD6Fus9rSDseXVftVw0pU93MShWlpTV2tDLDljAx_PYagELuLlh7hP2ZDKYcD5MfRItZyS68GiwSX46O6QXtaCrZffk90GAadd0WGNlb2LLX0X1JD4Ydpo3iyGyRmpMWEk9B1lmgZE_q9jlgDIxhg7DgbEcn9GK1rCmBtgOi8FafrQW9V6T036qg1EqDloClxyQD4QrG37UqM23H7TVfkv2AH2AjMr46tDQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa610bcbe1.mp4?token=IA1EmXZkbGT68-8gXgzWF8_oDubfL28ZDBmcpZht6v7hNltMcM74-hEKiqEZ0r5CS1MCbMgtmGpUZOGkobs43hMI23HQ6e8RjhSQXh6ygkvl4691YpD6Fus9rSDseXVftVw0pU93MShWlpTV2tDLDljAx_PYagELuLlh7hP2ZDKYcD5MfRItZyS68GiwSX46O6QXtaCrZffk90GAadd0WGNlb2LLX0X1JD4Ydpo3iyGyRmpMWEk9B1lmgZE_q9jlgDIxhg7DgbEcn9GK1rCmBtgOi8FafrQW9V6T036qg1EqDloClxyQD4QrG37UqM23H7TVfkv2AH2AjMr46tDQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرد الإيراني على العدوان الأمريكي مستمر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78337" target="_blank">📅 06:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_GHBya7BM7eK6ARrY66chjtL5TkpAnXVkLo73pAPuu1NgXLoAs6AJURdgF8VKSi3t8HVWnQxe0AI6oQtxSE29EfZeVArwhr5VBcLyDcmiBKdSGOZrBowUm92L7RRQhNju2oOUeyscS8Deo1p1JHMosVOKyOA667VG_r3gyK6Yu1vp-w3Wf2B6BaVWaVQ5WcHsdLVOQ8XAu84DBOFlJGrEqe_wrJbwRV-oMppS4GtHWgpnqU-E2dJGuEEiegyWkacUrG3-5pF4Md453d4Jtx66KtibpZM8A24VQWdWIh_7UtC1M8tqFpNDi9_b-EIq6m4tMYHqV5g0qAIO58ofXnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر   موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78336" target="_blank">📅 06:15 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
