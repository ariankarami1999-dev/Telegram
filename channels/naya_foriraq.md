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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 21:18:32</div>
<hr>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/83982" target="_blank">📅 20:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/83981" target="_blank">📅 20:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83980" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الاميركية:
قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.
‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى مستشفيات أردنية، وقد غادروها لاحقاً. أما الأفراد الآخرون الذين خضعوا لفحوصات طبية لإصابات طفيفة فقد عادوا إلى الخدمة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/83979" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">البحرية البريطانية: تلقت بلاغا بتعرض سفينة تجارية وعسكرية في خليج عمان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83978" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">البحرية البريطانية:
تلقت بلاغا بتعرض سفينة تجارية وعسكرية في خليج عمان</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83977" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=aHYSBlJ5eUu8IPdT5-lcGKQmDlT9gYa7kdi1brgDP8SJccpTj6pb5qOzdauxRj7DwtWzeBos5yOodcOJZHRE03LYIoQxVqGAEBpSK0i_ChNj0XEBT1TPB0QbrQRBoiNiqZGbu14urnBSAme1rW-vj-svYEqc5-I0y4Qsf3iIjNi3itfuDNq_K-tjaP6bbyeSgN1sMnnjm0TlJ1gkBOgj6mxTcAdba5NyLW0aaLQUj8BuAivHJh0ePYN2QE3CuOG_qrLmsjEPjP-gIkaVzY2VzERZ7HFynFJQtUbk3y4SCqUphejhgZf-rUS76-TK_OgURQvQYoIyiD5VUTfVvsy1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=aHYSBlJ5eUu8IPdT5-lcGKQmDlT9gYa7kdi1brgDP8SJccpTj6pb5qOzdauxRj7DwtWzeBos5yOodcOJZHRE03LYIoQxVqGAEBpSK0i_ChNj0XEBT1TPB0QbrQRBoiNiqZGbu14urnBSAme1rW-vj-svYEqc5-I0y4Qsf3iIjNi3itfuDNq_K-tjaP6bbyeSgN1sMnnjm0TlJ1gkBOgj6mxTcAdba5NyLW0aaLQUj8BuAivHJh0ePYN2QE3CuOG_qrLmsjEPjP-gIkaVzY2VzERZ7HFynFJQtUbk3y4SCqUphejhgZf-rUS76-TK_OgURQvQYoIyiD5VUTfVvsy1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بث مواطن اردني مقطع فديو اظهر فيه الصواريخ الإيراني وهي تتوجه نحو القواعد العسكرية الأميركية في الأردن ..</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83976" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
بيان مرتقب لقائد الثورة الإسلامية السيد مجتبى الخامنئي حول التطورات الأخيرة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83975" target="_blank">📅 20:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZrb5jp6cDcZKmzXF6q8SiX1YJ2GvO8J7y78a6YG4_nifDlSFsuh9pYtrUePmWGyD998PwwbXD0nfhTGUFJm7IUOQZIMhXicHGyjWpVcxFtliHK06tCAIt184ELM8HqqqgAxI7nqr16lhb90ICPxPU3ONkLd7v_JZtSLnHRO_LSD6DFVYHGRTZiUot3EcBsq9dB_pW_FoMsBfM8zq1IaIRaoNEUK4WlJ1GxexIV9x8RFRfxoivo0v_DWFFD1vJUnPUP7wPJHQ5OZOSE18nKibfMTKDiyrBNiPVfXl7vxgGcat_W3s7O_fAWcy5nD80_PfgPYUZ2UzsVhSoVCCFfb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇷
عقد القنصل العام لروسيا في البصرة أندريه كالينين لقاء مع نظيره الإيراني علي عابدي
وشهد اللقاء تبادلا معمقا لوجهات النظر حول عدد من القضايا ذات الاهتمام المشترك، حيث ناقش الجانبان الأوضاع في الخليج الفارسي وانعكاساتها على دول المنطقة، كما تطرقا إلى سبل تعزيز التعاون العملي بين البلدين وتوطيد العلاقات الروسية الإيرانية بشكل عام.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83974" target="_blank">📅 19:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
🇺🇸
**نماذج من جرائم الحرب الأميركية في الهجمات الجوية على جنوب إيران خلال ١٠ أيام **
>> تمثل هذه القائمة جزءًا من جرائم الحرب التي ارتكبتها الولايات المتحدة منذ 17 تير في المحافظات الجنوبية من إيران، وتشمل:
>>
▫️
استهداف البنى التحتية للمياه والمنشآت الحيوية.
>>
▫️
استهداف البنى التحتية للنقل المدني (الجسور، وخطوط السكك الحديدية، والمطارات).
>>
▫️
استهداف البنى التحتية للموانئ، والمنشآت البحرية، وقطاع الثروة السمكية.
>>
▫️
استهداف منشآت حماية البيئة.
>>
▫️
الإضرار بمستشفى الأطفال في الأهواز.
>>
▫️
استهداف المدنيين.
>>
▫️
استهداف البنى التحتية للاتصالات والبث الإذاعي.
>>
▫️
استهداف المصانع والمنشآت الصناعية.
>>
▫️
استهداف البنى التحتية النفطية.
>>
▫️
استهداف البنى التحتية للأرصاد الجوية.
>>
▫️
استهداف المباني الإدارية المدنية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83973" target="_blank">📅 19:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
ندعو الشعب المسلم في الكويت بالذهاب لمراكز التسوق وتخزين الطعام والمياه وشراء كميات كبيرة منها قبل فوات الأوان او الذهاب والسفر خارج الكويت قدر المستطاع ..
الليلة لن تكون سارة مطلقا لبلد تحول لقاعدة أمريكية يعتدى منه على دول الجوار ؛ قد تكون أقسى ليلة على الكويت ابتعدوا عن تواجد الأمريكان في بلدكم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83972" target="_blank">📅 19:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
بيان مرتقب لقائد الثورة الإسلامية السيد مجتبى الخامنئي حول التطورات الأخيرة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83971" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHh52vIVdIDUzuPOJdlaeSRdaSJdLlWBRI6C3TcrV5wq42lxbN5Sy93k71MXCrl-9WFvwLAV_uR3DRhstOVL1_whK-a7NUkOMJ9irTXkQGSnpxSTTUb9zTBRSbGgdbxWHTEyOWURKEbaPrVPPt2xS_I0vofl-VQ9kyed-80-bampzrogNMPc_wDdPDPe9p4DOZ5nMiSKI4xmob7cvimRoZuMI1WwMd4Ov9Zt3ocd25lF0XiJUZ50JGK7Et5XXJqGBo66BQiTJ5_nfs1vzqMTypIL-bST4U3rZOSHsasm3-5GWw5BJU9Vw3UFaaTDfKX00UA6btj09_z7beKv01QpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعودية تدين العدوان ع الأردن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83970" target="_blank">📅 19:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الكويت تعترف:
السيطرة على حريقين اندلعا بموقعين مختلفين بالبلاد بعد ضربهما بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83969" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مواطنون من الكويت يدعون لجعل الدوام الرسمي من المنزل بسبب الوضع الأمني المتأزم ..</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83968" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ab3c3911.mp4?token=owTyh9S1-zXlDZKFBpz8JgrCHM0Qfm6l0FxclenYeBYo3gedVryfC5fpi8LHekSTzUQrfAQlMtowQ9FMLPzIiKtrHrhPc2_u7qVRwnpeLuotDmUhHcxjxRxjs24RxJhsTJGSNorGg7VlwENwdoG7FaRsl1Vq_DdnSDtzbYj9VVsdcnZbJigx70RnCaBFOFfnknAvCZVbR17jhrcCZxHx2Dg-KHHCBproxCFLv5Qemvg8PmZs7uzVIBeFRuQZ0fCw1iH2nt-3IAYsfMIBnclJCLzQHNjmbPgKQNuDMJ5p-6c1jFfNqD_yVkZk_fTtfxBEDrWc7LUpFjgLxBd2OXqTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ab3c3911.mp4?token=owTyh9S1-zXlDZKFBpz8JgrCHM0Qfm6l0FxclenYeBYo3gedVryfC5fpi8LHekSTzUQrfAQlMtowQ9FMLPzIiKtrHrhPc2_u7qVRwnpeLuotDmUhHcxjxRxjs24RxJhsTJGSNorGg7VlwENwdoG7FaRsl1Vq_DdnSDtzbYj9VVsdcnZbJigx70RnCaBFOFfnknAvCZVbR17jhrcCZxHx2Dg-KHHCBproxCFLv5Qemvg8PmZs7uzVIBeFRuQZ0fCw1iH2nt-3IAYsfMIBnclJCLzQHNjmbPgKQNuDMJ5p-6c1jFfNqD_yVkZk_fTtfxBEDrWc7LUpFjgLxBd2OXqTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ان فشلت المنظومات الأمريكية في التصدي للصواريخ الإيرانية   الكويتين يطلقون حملة طف الضوء ..</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83967" target="_blank">📅 18:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnztDoM9Ksluqp7RNrE5fJ3RwP4865T0EX842AcWyFPICG1EUFvA4boVTR3rkSKUk8hGBarg7czoFEwI7eUH6FTaSAz2gGq0NAkUUGi22YVC59RcVKKWWxf72Yd0G4XH8Zcnc5pKv94XfN_jQ4KRk_L8ZxNHWS4FRpbIreUPVE4PzVOX6-jBddI2JMgjzkUADhZlfemRBItMUHQ2xjzfiF7QaDjLhsxkSMQcxp5w2oBEVAYxv6SClLRkb2BQjoEp47jxAqAlSOUi30AL9F_LqFXnqkJvXRhqED40pZTT3X1OtiQT9EXOBayAFjnUJFNK91jGhNvXp-ECFgjSa8wAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد ان فشلت المنظومات الأمريكية في التصدي للصواريخ الإيرانية
الكويتين يطلقون حملة طف الضوء ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83966" target="_blank">📅 18:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGXKXN8PaRLAhvjMYd21YnblDNHQMBltoOhTS_pvOXRjvTjRC9PJBaf-3JvFguZYzptBg37_YIEizyKcWIGzderRSaBzx3HZjheocVR1wylWjdnwHMCCHY8d--0ixt1pQ9JNNkr6Yp31skcN73KlhxIPkuk2wIhox5Au1phLIHyLgk2EWg5TZgDGqehkqi-i4TfDRo7y3Bgp_uQrWnC3a6GEp-B3_SQDBwwmrT1PVJb3G9_jSk4vFvMuTiOGv4e87sQCpe9GnLpx8fZomM3ns0eht_8y62dEvBvYBgvoms4XDOU_0ljkXVAW1LUUNPFRcyIuTrigT_2BqZ7u31VOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
فدای یک تار مویت حاج رمضان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83965" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWHdwDMG7nHf7aToc3SF2AWr4kKWQOB7n4qUfgOCsIklV2aO7qIAvvBJIx0Nw0-flp7kLa6X6ZdX6g13SH3ZLUiU4Qr45nMPD3bafTRVKn3Rw9Wz47ETOJ3tCLLYQ4nCXSSTDHoe3gHu1SvWBL7inh5NUuFrCIZe1S2CHLovD72c6F9Rckitgyxu6nm3KfNW1DzR1ayifvLWa4O646Ly606EcwkwOzh5nNE3cTSmY53tvMR964ppId125J964wBRwi2vkNtCrDfb11IJNGvTVf0gV7Bn4Vbu4XHiBwYGj_iqtyTB6jlk57EodJfGza8Dw5eshNxJfHXexJDQBH8CQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنون من الكويت يدعون لجعل الدوام الرسمي من المنزل بسبب الوضع الأمني المتأزم ..</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83964" target="_blank">📅 18:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
مصدر لنايا:
3 اسعافات عسكرية تتجه الى قاعدة عيسى الجوية في البحرين.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83963" target="_blank">📅 17:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
مسؤول رفيع المستوى في القوات المسلحة الايرانية:
إذا هاجمت الولايات المتحدة الليلة البنية التحتية المدنية في البلاد، يجب إخلاء مطارات دبي وأبوظبي، بالإضافة إلى موانئ الفجيرة وجبل علي على الفور.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/83962" target="_blank">📅 17:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اعلام سعودي:
الحوثيون متورطون باختطاف ناقلة المواد الكيميائية ASANA في خليج عدن عبر مسلحين صوماليين.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83961" target="_blank">📅 16:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇺🇸
‏الجمهورية الاسلامية الايرانية تعلن تعليق العمل بكل التزامات مذكرة التفاهم مع الولايات المتحدة الامريكية.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/83960" target="_blank">📅 16:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6032498f26.mp4?token=SNUOt5pLYlasjUmXau9jR9s52KiLPbyjVdz7gxQQO-LOsVWSFMlInCLpHrTzHDD__BbsSYvbg2Z7VLK6E_v2SYL-zUNM03onSi15u-ioZyLUqLPBil7pjNBV0hzQ0DIK2_iDxFz45J66x9L-6ReJGVJfrAQkmXjSgNW1NWZx5DttOuUpu9JLUQ4AOwm01abzrvge7EHb_FNjp5a-QVXQbhVAyC74nl-ItrhKsBPu1vBkoA66Q6odcvtqMjLx91iShlODTevCo9f-is5_Xx-RqgX3vVzT_GdXYEQXfMJWTfCE7__ygrEP77fW6XU7qYPM5Y7XwFt17moPULsdhkaTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6032498f26.mp4?token=SNUOt5pLYlasjUmXau9jR9s52KiLPbyjVdz7gxQQO-LOsVWSFMlInCLpHrTzHDD__BbsSYvbg2Z7VLK6E_v2SYL-zUNM03onSi15u-ioZyLUqLPBil7pjNBV0hzQ0DIK2_iDxFz45J66x9L-6ReJGVJfrAQkmXjSgNW1NWZx5DttOuUpu9JLUQ4AOwm01abzrvge7EHb_FNjp5a-QVXQbhVAyC74nl-ItrhKsBPu1vBkoA66Q6odcvtqMjLx91iShlODTevCo9f-is5_Xx-RqgX3vVzT_GdXYEQXfMJWTfCE7__ygrEP77fW6XU7qYPM5Y7XwFt17moPULsdhkaTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هروب جماعية وأزدحام غير مسبوق من مطار الكويت  بسبب القصف الإيراني ، المطار يعاني عملية تغير في الوقت بسبب صعوبة الطيران في الأجواء الكويتية..</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/83959" target="_blank">📅 16:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XANy9mv24ZMqlmRxqZkFRF4sZiOMx65bG2pPUE0XTH1ADWH6tnBvqhFUeoEm3Jv-dJoYoeNQ55owAL7kbSqujKyNA0NDXkpTEoATgYcOTf022ZhzazS_ckYJr6jeGu7Y0Jdtvm6oHhT1v0LCCx7vIyyHbUR4Te6VLaZ7LH2UIURto8ePm9WPEwU_UeZXyCcpgxAK0Hlgeti_sU291qjiGoJZYF8mlwNEflxwIOhRi78kX755KB8rypSFB6AbUOPtW47cXDaqrVtsC0raik9Ioa7pEdSXmZxGKppmNnIDGTLWTEDpyWsdyilbf_K2l8V3wlYof3yIjP0C4z0kriZFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد فشل اداء منظومة الباترويت الامريكية امام الصواريخ الإيرانية
الكويت تفعل منظومة لا تصور " فضحتونة "</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83958" target="_blank">📅 16:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56b067435.mp4?token=bCghd5IamV0krWNmrrRBlqs_U44owSWqxgBwQ5jTctG-3yTwPqEhK1YeH1leXmPPVa-jtvs55yPcXIIzNvYEU29UOfGC0sDBYOV07dhdb-6_GtD4P8gXQpSwxhUQUyw1erJRsEeNQlkMkUrPdGAGktZkp1qh-dYghnIQkY9ehpFgxvrteZkcXhBRlPipN6yhm6D8S89sPLP9z7pqU5X2wZeYDU6LIqL0PcieGs8UfYYUDZ4vDRkNNnwOF4O4h_aHdsfZsJgXB979oz4BGAH5Stipye5hDEyhKkbCp--Z1T4dFrXDHiB4zAgxzReMLavOPkycOTou5NB6eDk2ilJ0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56b067435.mp4?token=bCghd5IamV0krWNmrrRBlqs_U44owSWqxgBwQ5jTctG-3yTwPqEhK1YeH1leXmPPVa-jtvs55yPcXIIzNvYEU29UOfGC0sDBYOV07dhdb-6_GtD4P8gXQpSwxhUQUyw1erJRsEeNQlkMkUrPdGAGktZkp1qh-dYghnIQkY9ehpFgxvrteZkcXhBRlPipN6yhm6D8S89sPLP9z7pqU5X2wZeYDU6LIqL0PcieGs8UfYYUDZ4vDRkNNnwOF4O4h_aHdsfZsJgXB979oz4BGAH5Stipye5hDEyhKkbCp--Z1T4dFrXDHiB4zAgxzReMLavOPkycOTou5NB6eDk2ilJ0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الايراني الذي استهدف مواقع المعارضة الكردية الايرانية في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83956" target="_blank">📅 16:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff89045e5.mp4?token=q8EH9mprdMMt-320ywZk80I3YmeqFFUoDh36nm1Z2tPloP43BfXbkwjlN8Xh3MaKEvPY6JRz5bmitrjZD12VBT0S26lhqo06SzR5KsCGYbqWKst8FTdBfJ3Am-fagkLxz9mvw64yKZK4aWup2VtCkR_6XIqfA-WrPpd1pMZJUnP2WB_7f7Cvqjz92FS6KtNdznsRETQYUqvql7PPz3bG_kEQCu9fbPFVZdGyvEGDFlwtJNHX3spdbCjyF_HlANhtO4IFi82iaZDCYJ0s76AZqmvRduVBrvz4DHZs3KCbq2BPbmIOztvK92E5CrhsYePWht_kCaBWvvrkJfXZnggm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff89045e5.mp4?token=q8EH9mprdMMt-320ywZk80I3YmeqFFUoDh36nm1Z2tPloP43BfXbkwjlN8Xh3MaKEvPY6JRz5bmitrjZD12VBT0S26lhqo06SzR5KsCGYbqWKst8FTdBfJ3Am-fagkLxz9mvw64yKZK4aWup2VtCkR_6XIqfA-WrPpd1pMZJUnP2WB_7f7Cvqjz92FS6KtNdznsRETQYUqvql7PPz3bG_kEQCu9fbPFVZdGyvEGDFlwtJNHX3spdbCjyF_HlANhtO4IFi82iaZDCYJ0s76AZqmvRduVBrvz4DHZs3KCbq2BPbmIOztvK92E5CrhsYePWht_kCaBWvvrkJfXZnggm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من مقرات المعارضة الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83955" target="_blank">📅 16:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcWUpMOBX8Kc7q7n9iIK78H1eyIHBGgxK2vchfhIujpZmTH8pdT4OZrLcM1rIE5YcrqmtKitsONC7Nz0Gjq28ND2ZlHDNRkrvCmmWkOskaOiaF-VQMf83NsyCNYHyAkYW5_QomlIkYSykGRL8Jm41T6CQLQElk7sYROq3KoqAhNSKopHX2MMxKfvyNflj8z459BS1GuBd5p29UoV_uWr0rNO31_DaotDbNUZ_aZxeekJ9SFP6_xtRzLOEP2l_N7c1tscXZmTFwfXF5bJKZVdp9Z5xSrf6Ln0kKCAgUf_aHMKuUrSwm5fsff1Hh3aZ9lFfor-KQgJVbjYWFp8YyTGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc714b302c.mp4?token=W6nO5F3Hpli7aBVHE-pWXwx4bHKFQcQgJtRlaHL2dQwR31WvmvQsH-Nvtlt50kuNppj6qVPmpfWT_eUbEOI33nbHimdeU6aoXb0fz31UTEXSBi9W04EFtfJMm7Sa2Jh3Duhdx7XkRWd8TE-CnP-mbrnBnXkhKR0tP3BI4R5K0otJ6t6dKBj21NfnKISRFnAzDMad2d23XXLF7E5-oDI_33Ux5Bh3w-U5e4ArjQ3gpqclRvwF9fe4WDYXv8AZonb9VP7PWSm-h6m_Cp92kPlgUTY5gzDprGNY7Cls6wP9f72NhnUM6jHJZgzi29IU0k-g8PRIBIfVjO6tK5JaWFv0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc714b302c.mp4?token=W6nO5F3Hpli7aBVHE-pWXwx4bHKFQcQgJtRlaHL2dQwR31WvmvQsH-Nvtlt50kuNppj6qVPmpfWT_eUbEOI33nbHimdeU6aoXb0fz31UTEXSBi9W04EFtfJMm7Sa2Jh3Duhdx7XkRWd8TE-CnP-mbrnBnXkhKR0tP3BI4R5K0otJ6t6dKBj21NfnKISRFnAzDMad2d23XXLF7E5-oDI_33Ux5Bh3w-U5e4ArjQ3gpqclRvwF9fe4WDYXv8AZonb9VP7PWSm-h6m_Cp92kPlgUTY5gzDprGNY7Cls6wP9f72NhnUM6jHJZgzi29IU0k-g8PRIBIfVjO6tK5JaWFv0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من محافظة السليمانية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83953" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2abaf633.mp4?token=JLQ4c_Ti66uYqd0HSdObj1jT9D2GRtrovMQ5ua6Yutnjwe4q8Z4kU3S1cIvV3nKognx2dwx4dq2ajFLKOccHQNgRyXdTORwA0RU38iR6GHHA3zh-iOBdxxqIA0Bno3uaAE1JTVatX7N2t2HuXKe0YUDyRhbQhsCoOtWirWa8zpP4OKcfQCBesTSwHhFWUkRTDyj8lC4KKr8_-V042YbRheXmMniv2rV-hvr9b7kuQ1Kc8ns1tAEOM_NQkVz4LuPioT9d0Ok1wU5gn57vOK__8BJcVaqWhpQZo9mijeFXKVOOppFGG0NueaCSt9lsQPfzAo1i4ZzKCgXR5q6EpUEvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2abaf633.mp4?token=JLQ4c_Ti66uYqd0HSdObj1jT9D2GRtrovMQ5ua6Yutnjwe4q8Z4kU3S1cIvV3nKognx2dwx4dq2ajFLKOccHQNgRyXdTORwA0RU38iR6GHHA3zh-iOBdxxqIA0Bno3uaAE1JTVatX7N2t2HuXKe0YUDyRhbQhsCoOtWirWa8zpP4OKcfQCBesTSwHhFWUkRTDyj8lC4KKr8_-V042YbRheXmMniv2rV-hvr9b7kuQ1Kc8ns1tAEOM_NQkVz4LuPioT9d0Ok1wU5gn57vOK__8BJcVaqWhpQZo9mijeFXKVOOppFGG0NueaCSt9lsQPfzAo1i4ZzKCgXR5q6EpUEvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83952" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e783804844.mp4?token=KArJsV5yOXhdVW7Z0_YRawBZX7PNsU95KiIqTHPfhepL_SdRMgfiDNy6lDQkpsAkFGe1Wej9cbnyjlrzAnaotUZ3dvFtObnYYJ22TLCE1crfkWY0lIG7rYtD5nfKZronMK4mIeErirtYs4MLAm3y_AN4iS7sEfP36EW-yYKP6wgsHnHLIxK9iEFrpP8MIDFHK6tup-2Vr-y56mKFg1-8v4ec-TIjOV0TLcyIG00FvRkSbuT1E7AqTD5nCUqUfl-cLxMlAxZmddD_GVrf8_jQ18eBZvr3Nwnzp3Ti29tFZOmvF6iydOWayujWFoC0vN2Q1_2dackr_jnVSEoiAA3jBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e783804844.mp4?token=KArJsV5yOXhdVW7Z0_YRawBZX7PNsU95KiIqTHPfhepL_SdRMgfiDNy6lDQkpsAkFGe1Wej9cbnyjlrzAnaotUZ3dvFtObnYYJ22TLCE1crfkWY0lIG7rYtD5nfKZronMK4mIeErirtYs4MLAm3y_AN4iS7sEfP36EW-yYKP6wgsHnHLIxK9iEFrpP8MIDFHK6tup-2Vr-y56mKFg1-8v4ec-TIjOV0TLcyIG00FvRkSbuT1E7AqTD5nCUqUfl-cLxMlAxZmddD_GVrf8_jQ18eBZvr3Nwnzp3Ti29tFZOmvF6iydOWayujWFoC0vN2Q1_2dackr_jnVSEoiAA3jBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة السليمانية بعد هجوم استهدف مواقع المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83950" target="_blank">📅 16:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSovsQDGsElsNYgTcyoMBC2VJzSVz1E9_K7tBHJzjROzmvuphVxiBNN6NRXHypT5_Cyxd4n8PyO3I0ziV7gSBjYrNnVTPQ9-yf9tkux3ZCyPiOAaOBALVhWQFRojnYp-AgmGTzsylwkL2MoMf1rgkvDxwpxm6r0Z12078OjcaNkEqG9ub_FDtkfthKIhluuSjHL2zBiTAKPVoLpQ52Ri5OGqrIJLG_xusS5LeTbtnRwP6d7qyDO2xOLevgOtfdO4_GbOF1jNDnove94drOJijzzyvgTlDuV8bHAvF2Yb4OX3XUJFmhlhSX4UWGOi-TgxbacfEZyBARByvvrhFv8NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0Ho5qqh6qDyrx2N-c07V4ihcA25XXSR8WqUP0Toc-9jFi4U8ntZX2ZbR52obWgBcf-y-u6gltr9fq8uvszyQ3owtPsvYBBtEEzSqxQMV4H7hoR-pWvVhkic-wyqGv1ZrTA-2dQFbhInxmsyRTlmNlGDbswiofm4-_JLu31P-JbucWxxT2Oys5jh6DIhEtKfTBJK35oKP6i915lSwUrI6808t3qiMqpAYEzSN9YbFrn8GpoWHLkew_VT40kEeefTFDZmrR34XMGm8_8VeDzKLxR4jA82PUrUBmNxilSaSflD_BXcT-VVh_Uq8RuUlJrLoxpZjTV0al4G7hR0FbOajQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83948" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoKMPvZMRdHOc3kwtwL46Dyf6etg20Bt7jinT3H-ORiTmts_BPtVaWMl7Ol9CYbtXyet7jeRgkS7pR75XMsmEI9S1_KY7m3CWR7BFvgmrDlY47QrLc1oXIxOSnkQ0S5latV6oNBmLlC0cehQBudl7xYQbdLjunrmJwcOzvkS1DuN-AvRIRrEoP6lhhAre6iCdjPcoAN6xDVYqik_Is7By4hBy7qT53yNbL1UApfrKRjjRfBs3p1KU2JNAYUzWStMijdRR8G7F1bvwYY4GULkjhp0OlswOM69zJBqAPs4kyMrMSTjWAvnt52TIZTS-mU9N4KNShYxTBls1fpMA_kyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من القاعدة الامريكية في الاردن بعد الهجوم الايراني</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83947" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83946" target="_blank">📅 15:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83945" target="_blank">📅 15:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83944" target="_blank">📅 15:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce6a72292.mp4?token=RtW46wAj8CqSgJaarhgQNuwx_VjwfdCfPoXxXDi57ckNrjZdEP33HnOl9YVFjunxg7WOJhBk7pQTrcOPCdfmJi5oDcUxvr_CuVXZ-IYUKspAOMi6MwWtOrKkbeiAgzpepBqNoBlUZOX5uU1Dx8ktOz1PYK1CJxZwxen60uGPaSa1te1-5wm7h3teTwBFCU2jcW1v8ixzFsNCIh0xg5XziGRW7WSRCIXPpPYWCSTeyKxaJWFSUxfreIuoXhprELTHn0_o-6mQ7Mx0yqYHibk6pn5yvNUrFB-7PnOHhoyipqJtFJaupaon677jDV5KSozyC9cefe_bPFSvPLNlb5NXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce6a72292.mp4?token=RtW46wAj8CqSgJaarhgQNuwx_VjwfdCfPoXxXDi57ckNrjZdEP33HnOl9YVFjunxg7WOJhBk7pQTrcOPCdfmJi5oDcUxvr_CuVXZ-IYUKspAOMi6MwWtOrKkbeiAgzpepBqNoBlUZOX5uU1Dx8ktOz1PYK1CJxZwxen60uGPaSa1te1-5wm7h3teTwBFCU2jcW1v8ixzFsNCIh0xg5XziGRW7WSRCIXPpPYWCSTeyKxaJWFSUxfreIuoXhprELTHn0_o-6mQ7Mx0yqYHibk6pn5yvNUrFB-7PnOHhoyipqJtFJaupaon677jDV5KSozyC9cefe_bPFSvPLNlb5NXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83943" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f86a8ce4.mp4?token=YA3N58exChzDzfZe-GKXustBvDtA5bESAhhPJtzNS5dbXTzMcPe96DZufX9AJKDi5MmPFJR1_D21T2q-fGpri6jw2DZcQKQ4AeZ1BAAbY92bPCfTmXR-l4vM2RmgX15qHnKa_jV-kB09k0qwvdeNETCvWEh26jRoSg-lhD7iNYF-XdceLdOt71XpuvPPsgXpX8EdyflpG-O1zgRJdJLnhxkuJKxVBnI1Ywo1s7PrWMDKAv5ygnIzthJ4I4-ztqsENmEtII7WCMQZ8vXtSz_UjNeQmSTZ2fj6ZUd388joYExFqjeEjIuqrsaPIVTnLkb0R3wNk91uagAxXwydJ_uVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f86a8ce4.mp4?token=YA3N58exChzDzfZe-GKXustBvDtA5bESAhhPJtzNS5dbXTzMcPe96DZufX9AJKDi5MmPFJR1_D21T2q-fGpri6jw2DZcQKQ4AeZ1BAAbY92bPCfTmXR-l4vM2RmgX15qHnKa_jV-kB09k0qwvdeNETCvWEh26jRoSg-lhD7iNYF-XdceLdOt71XpuvPPsgXpX8EdyflpG-O1zgRJdJLnhxkuJKxVBnI1Ywo1s7PrWMDKAv5ygnIzthJ4I4-ztqsENmEtII7WCMQZ8vXtSz_UjNeQmSTZ2fj6ZUd388joYExFqjeEjIuqrsaPIVTnLkb0R3wNk91uagAxXwydJ_uVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83942" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0ddcdc3f.mp4?token=HUex52jk5JCGqB5hSpprYqr31nOdNx_DBPnb1T5UeqxEjpPo0kk9utZ5o__kHWixP9JXYwbBMbWC8PzuUPzbJKTwc8uMCJhFyphBZTC0CSTtdHd1WplNfRFtj1UQwofiXtVBw4lI9VrwR4F5re2KC4ZZGhVVCtm76GSbuhu7cetU2kBQ5FDLnu09g7_sOD6ftMobv1GUiDX_zAhgV_yOlkpr9aJloEnV6xXsBmwMY8s8iP1AFaGBh2ByN70PN43B8tZnhko7N1wp8hrJDYK3ZRIy6tnEFv59z2EfLEAzB8hMui2HlM9M44Hf6p9eHr7_4Osp7MZnER6-pHUoqRmpYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0ddcdc3f.mp4?token=HUex52jk5JCGqB5hSpprYqr31nOdNx_DBPnb1T5UeqxEjpPo0kk9utZ5o__kHWixP9JXYwbBMbWC8PzuUPzbJKTwc8uMCJhFyphBZTC0CSTtdHd1WplNfRFtj1UQwofiXtVBw4lI9VrwR4F5re2KC4ZZGhVVCtm76GSbuhu7cetU2kBQ5FDLnu09g7_sOD6ftMobv1GUiDX_zAhgV_yOlkpr9aJloEnV6xXsBmwMY8s8iP1AFaGBh2ByN70PN43B8tZnhko7N1wp8hrJDYK3ZRIy6tnEFv59z2EfLEAzB8hMui2HlM9M44Hf6p9eHr7_4Osp7MZnER6-pHUoqRmpYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من أكاديمية سعد للعلوم الامنية في الكويت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83940" target="_blank">📅 15:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/naya_foriraq/83939" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83938" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83937" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تصاعد اعمدة الدخان من أكاديمية سعد للعلوم الامنية في الكويت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83936" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القاعدة الامريكية في الاردن تحترق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83935" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هكذا تبدو المشاهد صباحا من الكويت حيث صوت الغارات والقصف الإيراني لا يتوقف ..</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83934" target="_blank">📅 15:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوي انفجارات بمنطقة الميناء بالكويت</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83933" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
انفجارات عنيفة تهز مدينة أوديسا الاوكرانية ، أوديسا هي قدس روسيا وتتواجد بها اكبر قاعدة لحلف الناتو ..</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83932" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83931" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز قاعدة الجفير في البحرين مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83930" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83929" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇦🇪
وزير الدفاع الكويتي يزور جرحى مستشفيات الكويت التي تعج بالمصابين العسكريين الذين يعملون داخل القواعد الأمريكي ، وزير الدفاع الكويتي يؤكد ان لو لا جنود منظومات الباترويت هم غير موجودين بالكويت</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83928" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف عجلة واوكار للتنظيم الارهابي</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83927" target="_blank">📅 14:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxBATl-bYcXZ7vSoLCERc0PRQdfzgQ8wlSq2f4TxEkI7C2lSzJ5xS57fmVir1T9Uo2PwMVV3mUWVF0HvUrtw1Q0QUaDE0rD9xNJWlMzfmNx4p7PvhCEa7uc2H-rB5tNHl7zrL_bNk4_X7jwHd0Pm3BvuvnLb-24OhXgIAh_YXEbrcaR3tY2v9FZdG3Yv_LkMqSODDR-S5fVkzBvUV16J9_jfLEbXZIxBj580G5jiFt8AYXEUUbMgheee1FUmKPged7xVmOeRl8WuJB5v_kCLC0vItn48cncdSHfP6_stOMGoi15BracjGOQHi8iTJoCAi6Al0rweOX2ygHEwsPgFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابة مباشرة للقاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83926" target="_blank">📅 14:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83925" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من القاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83924" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">موجة صاروخية إيرانية باتجاه القواعد الأميركية باتجاه غرب اسيا الان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83923" target="_blank">📅 14:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83922" target="_blank">📅 14:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن تتزين بصواريخ الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83921" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83920" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83919" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUuRsAEUhUcFaOlXt8a1kw_0Q91DeM0WbDrv4KKqE1VjH17QGF3x8ezYgLF_hSSkG9mMLrCFJPt3JbQLhiC4jdJaJikmUY70FgK_BxnWB47zSchCcGhewCd0yZ_wTV6kiWSfYrvHBMK1bhSuXcZAuVae1gKktrfujO4SefrwkmtLbBL3PdEXK_5nLuPGc0gK-6YuT8t9Y-sJ5othqf1wbL8hSsGu2aBOEbt9hm1tAZRoyC4cf8RGdi2ObhETEzsr2HrQg2qJypk6XvzGhhXJ4BQM920SCBiwIVCzfIK917a5cYiopWtFUGm3706oj_mEhezr0Bire-kqhFdNDHandw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83918" target="_blank">📅 14:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83917" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الكويت: تعرضنا لهجمات إيرانية اليوم بلا توقف</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83915" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ايران تطلق دفعات صاروخية جديدة باتجاه القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83914" target="_blank">📅 14:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مشاهد من مدينة الزرقاء الاردنية قبل قليل خلال الهجوم الايراني الصاروخي والمسير</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83913" target="_blank">📅 14:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83912">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNIOUlrpffwDaWuOa6PnzLZneqgoKt1P6rTZTaK3zjeO50dp0hvXQE1sD80pIt9kfd1V6oIQ2xPzgUL4kuo0LElnSJFHr1xwq8wxAAWXUlyGKzzA7d3V7dxfCC_OPIN_4qsVX1TAIV2iLTPLSEt9V8VH8H4url6ry9soLqFFbXPvR8Zu_WIwbNWfZ38YpqDq2pnO4zdku54JJ5avN9QZL5NQx-A-OW09k7otjXXyzfw7LTqFwUn6pOsSZ-DxJbqPuNc_OMF0wAqpNgALv17jhFXAqbTAjAY2Ciu52V5h99neIwW1GnVbU7QxRMF-D9qRJfbDPmi5HhPa2S9dt3JbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يوجه سؤالاً نيابياً إلى وزير الكهرباء العراقي:
ما جدوى توقيع اتفاقية جديدة مع شركة جنرال إلكتريك (GE)، في وقت ما تزال فيه نتائج الاتفاقيات السابقة مع الشركة وغيرها من شركات الطاقة محل تساؤل، ما مصير العقود السابقة وما أسباب تكرار التعاقد مع الشركة؟!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83912" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83911" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجارات في قاعدة موفق السلطي في الاردن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83910" target="_blank">📅 14:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
حرس الثورة الاسلامية يبث مشاهد للحظة إطلاق صواريخ "خيبرشكن"، "ذوالفقار"، "فاتح 110"، "حاج قاسم"، والطائرات المسيرة "شاهد" في الموجات من 17 إلى 20 من عملية "نصر 2".</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83909" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83908">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الجيش الاردني يزعم التصدي لعدد من المسيرات</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83908" target="_blank">📅 13:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83907" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83906">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83906" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83905">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هجوم بالمسيرات يستهدف القاعدة الامريكية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83905" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83904" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجارات في الكويت والاردن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83903" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دفعات صاروخية اخرى تنطلق من الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83902" target="_blank">📅 13:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇵🇸
🇺🇸
🇮🇷
🔻
رويترز :
عاشت ⁧ الكويت⁩ واحدة من أسوأ لياليها من الهجمات الإيرانية الانتقامية منذ بدء الصراع في الشرق الأوسط، حيث تم استهداف محطة توليد كهرباء ثانية في غضون يومين وتعليق الرحلات الجوية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83901" target="_blank">📅 13:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5xiK16F4WQ9lkDleAl1oSiQM4hNqFPL5Am0tlngBlRpdFTU8BMgbmIeBNAQRpZbfOXzfGXbqBEx3tULH05c145FttX53I1dRkfkymkZmWsGTwxBnlqyU53y971DcAzxx6E6H-3ix7HNdq5cHl1kW71gzuzo2UP_mvD_hW0th9dgETHs7mdYLbYXK9WYJLAKOYKQEfOsTWrt4ASCyTxC0tzXHzvLIWsySSvtQB8yeR7Pf_26H9_iqhyi35w-32wUCx9HPqE4QXBeJVN-FDqHrNteehRXBwzPZPlAy2h0EJjdXCs91W3wYkM63pcxtQXYk1RDKy8ntK9MffYZ6ewftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
الْأَعْرَابُ أَشَدُّ كُفْرًا وَنِفَاقًا
⚠
عرب های بادیه نشین کافرتر و منافق تر از دیگران هستند. / ۹۷ توبه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83900" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تحليق كثيف للمسيرات في المحافظات العراقية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83899" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسراب من المسيرات تخرج من ايران</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83898" target="_blank">📅 13:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQoHVvRgowpfUsQeRDlGyxq5WgAwpdITGCZgc05IXH6zAP5Ur8cT-4xherU-nVXaEV_xfI2rmNFEkDwoyq2C1r3CisK1X6F0SmdAj7fbdeSs1sd5TfmakQ7PYKOOA7IAao07UAhTU9UzNt2U8oq06U0zhbbagbLu9SNEriZxLxyynZG7GTLbJbAi52mCIVpUCwNqwJ_5DDgDm2k4HGG_AaYvGEc3hZldtTpfmq3NiOwN9TYhrvcX9SFkcWWlNL_PX1bTQiK1sI0P9EC9FhHClQrB8nd-1eWsSNoZRh6kJJCJvtHWyQrQidS_W2E8EZIoNMFeyH8Y9ARHSxF9SpOdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6VUVzTXgOVlqTml02Grzy6buVRbixdF3BHkTqu-q4yecn4PvxaPRqetztM9DpPPeropx6gSMcdVERpupdKI2mluyM0t3nOfmCw3sRyZ2YuzI-E_8csxCXxgb97pbsXV3eaOgRNFYCHpj9pR5BrocgwytowvbvbkRKRY06XCiskZ_4d97rcjuEGOaEV7_sxjROJ0KfeHHRhBZSi3WBEBHmdN68kN5sLOCwPacpegf__MvBWQFzAwNSH-YRXv2wasPSs94BgqpSQmsU62jHrEPUtT6jDcH6Hw73BmwMd0Rwkz4Y3blVpRy50VcLQPxaBmGq1XLh0v0-l68-zItlmgDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
فوری |
موشک های ایرانی به سمت پایگاه های آمریکایی شلیک شدند
@Naya_Press</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83896" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عدة رشقات صاروخية ايرانية تنطلق من الجمهورية الاسلامية باتجاه القواعد الامريكية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83895" target="_blank">📅 13:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ايران تبدأ بدك القواعد الامريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83894" target="_blank">📅 13:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83893" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ايران تبدأ بدك القواعد الامريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83892" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حريقين اندلعا في موقعين مختلفين إثر هجمات إيرانية في الكويت</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83891" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حريقين اندلعا في موقعين مختلفين إثر هجمات إيرانية في الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83890" target="_blank">📅 12:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83889" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83888" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇵🇸
🇮🇷
شظايا صواريخ الباترويت الأمريكية تساقطت البارحة بشكل عشوائي مما جعلها تتحول إلى مصادر دمار لمنازل المواطنين الكويتين</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83887" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
الخارجية الأمريكية : وننصح الأمريكيين بإعادة النظر في السفر إلى الشرق الأوسط .</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83886" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
🇮🇷
مراسل نايا: دوي الانفجارات في مدينة مهران ناتج عن تفجير ذخائر حربية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83885" target="_blank">📅 11:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني موجهاً رسالة للشعب الأردني والجنود.
أيها الشعب الأردني الكريم والجنود الأشاوس؛
كما أدهشت استمرار تواجد الشعب الإيراني في الشوارع لمدة 140 يومًا لدعم الثورة الإسلامية العالم، فإن استمرار ردود أفعال مقاتلي الإسلام، التي تواكبها معونات إلهية وتحقق نجاحًا حاسمًا، قد أذهل العدو وأدخله في حالة من الارتباك والهزيمة، ودفعته إلى الانسحاب من ساحة المعركة واللجوء إلى جرائم حرب وعمليات غير إنسانية ضد المراكز والمؤسسات المدنية.
الجيش الأمريكي القاتل للأطفال يحاول إخفاء هزيمته في الحرب المباشرة مع قواتنا المسلحة من خلال مهاجمة المستشفيات والجسور والسكك الحديدية والموانئ والمطارات وقتل المدنيين.
في فجر اليوم، ردًا على أعمال الشر التي ارتكبها العدو الأمريكي الليلة الماضية، أطلق مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية عملية "نصر 2" تحت شعار "يا أبو الفضل العباس (ع)"، حيث شنوا هجومًا صاروخيًا وطائرات مسيرة مكثفًا ومتزامنًا على مواقع طائرات مقاتلة ومنصة إطلاق كبيرة في قاعدة أمريكية في الأزرق بالأردن، مما أدى إلى تدمير كامل على الأقل طائرتين وثلاث طائرات أمريكية، وإلحاق أضرار جسيمة بعدد آخر منها.
الآن، حان دوركم أيها الشعب الأردني الكريم والجنود الأشاوس. وفقًا لفتاوى جميع علماء الإسلام من جميع المذاهب والطوائف، فإن الجنود الكافرين المهاجمين للأراضي الإسلامية دمهم مباح.
الآن، الجيش الأمريكي الذي دم القتلة، والذي قتل مئات الآلاف من المسلمين في أفغانستان، ومئات الآلاف من المسلمين في العراق، والآلاف من المسلمين في إيران، واليمن، ولبنان، وليبيا، والسودان، والفلبين، وفلسطين، هم في متناول أيديكم، وتقتضي واجباتكم الدينية والإنسانية أن تقضوا عليهم بأي وسيلة، وأن تطهروا الأرض المقدسة الأردن من قتلة المسلمين الأبرياء.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83884" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🙃
تعرضت مخازن عملاق التسوق الروسي شركة وايلد بيري الروسية لهجوم بمسيرة أوكرانية في العاصمة الروسية موسكو ، تشتد الهجمات الاوكرانية مدعومة من بريطانيا وألمانيا وفرنسا على موسكو بسبب تجنب موسكو المواجهة بين تلك الدول او الضربات الخجولة على تيار البندريين في كييف</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83883" target="_blank">📅 11:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaNib9A_9y9DNyuFRAHIO6vCLvVm6Ki4skcanEfNMVYsTVV3xYSEhtr9vO18W1VEPlAOxTie44n5oyj9sh-hytlX1DckyY73qyOrplq_FHU71tVbkDMlEiu-6dgx539HlwVpNuMxzYsNI45gneTmjUGZAOlu41ZR0dntMmZY7LIc-szLED9bF7umKqnJzhCHWDG0nhWgRIzUIY1v-AoScfeArN-fXfg7V_knKEtr_n76ii__7o-n7YLyQ6IQkUzk-OUzYhPxMb98xXAH_0-6G2ZyAoNzVmIQYUjdc1zX4NB2ocOIZBPpGFFd6DaM4TpEOU6Np_GHxqP99I29CHR_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لليوم الثاني على التوالي
الكويت تطلق حملة ترشيد الطاقة بسبب الهجمات الإيرانية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83882" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83881" target="_blank">📅 11:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تصاعد أعمدة الدخان من الموقع الأمريكي المستهدف في الكويت.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83880" target="_blank">📅 11:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
🇺🇸
السفارة الأميركية في الكيان المحتل تصدر تحذيراً من السفر إلى إسرائيل والمنطقة بسبب "التوترات الشديدة" في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83879" target="_blank">📅 11:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انقطاع الماء عن اجزاء من الكويت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83878" target="_blank">📅 11:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز سماء كريات شمونة شمال الكيان المحتل جراء إطلاق صواريخ من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83877" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83876" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
