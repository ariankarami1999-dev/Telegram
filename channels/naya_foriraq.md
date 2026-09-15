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
<img src="https://cdn4.telesco.pe/file/lng4DGvryZJtooZpgi_BFwsGaqijfKz6qbrkFT6ZKvGHZOusPMmbqikRvgqHL68Wq_u7u2gTFH6CFNu6JRSzKVmkIYrzcqsCrc9yRoc-mLrQZbJ72vfPJHDjlZnXENP8x1MIH60R6OIXpqf9_Z9SVRj5RHO8EOVEUglZal8rrF1NEr4sOWYWzJLOX4ak6xVSb-v2hsm57_LOyqw2N8H_JhAfJyzwFbNitZ8zFH9RKIp9IOUUHhQkS9N2oBreiMtqerkQza4-_Z2TgSbA71BYqvDNYgMfViliQkwQAFeonWwzC8pAw0aEE6mnEYW9AgVaWqCxo-zDAF0QH9pVlPeoLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
🇮🇷
🇬🇧
أعلن المركز الوطني البريطاني لأمن المعلومات السيبرانية أن فاعلين سيبرانيين مرتبطين بالدولة الإيرانية قد استخدموا عائلة برمجيات تجسس تُعرف باسم "CHOSEN BRICK" لسرقة الرسائل الإلكترونية والرسائل وغيرها من المعلومات الحساسة من خلال حملات "التصيد المستهدف" على منصات المراسلة بما في ذلك واتساب وتليغرام.</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/naya_foriraq/90637" target="_blank">📅 22:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏وقالت هيئة رقابية تابعة لوزارة الدفاع الأمريكية (البنتاغون) إن الضربات الإيرانية ألحقت أضراراً بمئات المباني العسكرية والدبلوماسية الأمريكية، فضلاً عن عشرات الطائرات.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/naya_foriraq/90636" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/naya_foriraq/90635" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات في ابها</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/naya_foriraq/90634" target="_blank">📅 22:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/90633" target="_blank">📅 22:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/90632" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/90631" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90629">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/90629" target="_blank">📅 22:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
‏مجلس الأمن يعقد جلسة طارئة لمناقشة التطورات في باب المندب.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/naya_foriraq/90628" target="_blank">📅 22:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وتكافح القوات المدعومة من السعودية في اليمن لوقف تقدم الحوثيين، ومن غير المرجح أن تستعيد ميناء المخا الرئيسي على البحر الأحمر، والذي سيطر عليه الحوثيون الأسبوع الماضي، وفقًا لعدة تقييمات عسكرية من أوروبا الغربية.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/90627" target="_blank">📅 22:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90626">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
‏العقود الآجلة للخام الأميركي ترتفع 4.38 % لتبلغ عند التسوية 105.83 دولار للبرميل.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/90626" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90625">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🇮🇷
مكتب الميزانية في الكونغرس
: تكلفتنا بسبب الحرب في إيران بلغت 38 مليار دولار خلال الأشهر الخمسة الأولى، الحرب استنزفت مخزونات الأسلحة الأمريكية بما في ذلك الصواريخ الاعتراضية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/90625" target="_blank">📅 21:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90624">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
الاعلام الغربي:
إدارة ترامب تعيد توجيه 52 مليون دولار من المساعدات العسكرية الأمريكية المقدمة إلى سلوفاكيا ومقدونيا الشمالية وتونس والعراق، وذلك لدعم بنما وبيرو والإكوادور وكولومبيا.
أفادت وزارة الخارجية أن هذه الأموال ستدعم الجهود لمكافحة تهريب المخدرات، وتساهم في تأمين قناة بنما، وتمنع المنافسين الاستراتيجيين من اكتساب النفوذ في نصف الكرة الغربي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90624" target="_blank">📅 20:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3jdzrnpBAXX8ea-6J7UpZl_D41d8USqelcH8Vnm8N6zYXDegRM2Xy17G9euwXQxxD1q2VPE9OgL3uGTlsrK0wc-uCAEHucaeukANtCBxMLzuHpDqqUuw1hQHsv0SX4kDjQA45HeR0UiYB-eJY5Bmhmhucb9OtMTnn6i-E_0lfBVlR_NEsxHCFhCD8qrjFZ3DJ8g4r3oezRaZ9TpPNSsJntvpunOpLkfNnDkXHg-JB0whwciSYopW4DAdjQIzTQlOhqMGYNkcJSqCj1sVmvodORqkDf6TKFCYx_xrOFrCuenWLyeHHKlEI1gsIwCsyOfx47cK5stmDdhFnU3DRHHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس جمهورية العراق السابق عبد اللطيف رشيد
يفتح معرض خاص للصور خاصة به بأسم "معرض لطيف رشيد" في السليمانية.. وفي المعرض هناك جناح خاص للصور خلال تسلمه منصب رئاسة جمهورية العراق.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/90623" target="_blank">📅 20:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇱
اعلام العدو:
إن مساعدة إسرائيل للمملكة العربية السعودية في مجال الاستخبارات تهدف إلى ضمان حرية الملاحة في مضيق باب المندب.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90622" target="_blank">📅 20:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
متحدث باسم الوكالة الدولية للطاقة الذرية
: إيران لن تستسلم. برنامجنا النووي سلمي.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90621" target="_blank">📅 20:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90620">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbdBfrWtuD6AEa6d2O3CSnnPKfmkili9WkNVozt_xBzCMTKQuL_5KRV6_ZsUz9HWjxXkDG13yWWHrRwpprpxZ-4RNwPQyWHTKmHwGLDAIn_bJ7kvGLMl2ViGLPE78vMrOLZXrcm77P3-3ELevCXY-dUqge894WlGwWBFCHksCubtz79Vyr5LUkQxrOOkWSHhIfpxzHEFVqIxxE7kbkj8OmwJWtM2GsEXZfi5l-pn59qD5QcNziFlo_LTAloUMOJCC4j7hR8S62yNkpmNrGqcB1zAojCJ5n2ZofN6cS_L5VYD6V-bAF8VS_5kG6wJw0LKeEAg9Uw95GIguauo9yYHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
:
الزعم
: إيران بلا دفاعات.
الواقع
: تعرضت مئات القواعد والمنشآت العسكرية الأمريكية للقصف، وأُضرمت النيران في عشرات الطائرات الأمريكية. (المصدر: البنتاغون)
هذا ليس سوى غيض من فيض!
سنكشف عن الحجم الحقيقي لخسائر القوات الأمريكية في الوقت المناسب.
وسيكون العار مصير من يزعمون زوراً أن إيران بلا دفاعات!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90620" target="_blank">📅 20:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90619">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
قادة جيوش الولايات المتحدة وإسرائيل والدول العربية يعقدون اجتماعًا سريًا حول إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90619" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90618">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdTyDl9CSutfSFzYaxtT3Qt7dLB_34MuI7xSO82gSHgLrAtm0XzHJAn2o-XGGpZXqF9tcIBWkOPE7-h4_hwCTeKjxkVvYnT97px45RetKLuP-T_xLBYI74yuhK89rHiRuAKJmqeqz2VjAV6AOMi1u8TGmwhWa9TOZSfATHtOZJeE9FVn6CO3vVQ6E4guvwuC8s0E4KeCZLBFVh25VaWG-kt7akmhlk5Ugi8i0JJjt6hiEQh_5hU_HzXk78Eaj_Ni8liqYdjnP7R4RSzVHoNq9ZMzupXFhC0ew3ftig3Tvx1OdbFwLd-VxdZXbEKbbs5AlQEJpjyiGsqBFIjXwBcP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد البحرية في حرس الثورة:
يصادف اليوم مرور مائتي يوم على تطهير الخليج الفارسي ومضيق هرمز من الوجود الدنيء للجيش الأمريكي الإرهابي وأعداء الإسلام؛ حيث بات مضيق هرمز الآن تحت القبضة الحديدية لمحاربي الإسلام. وبإذن الله، لن نرفع قبضتنا عن حناجر القوى العالمية الجشعة، ولن نسمح بعودتهم أو بأي وجود ظالم آخر.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90618" target="_blank">📅 19:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90617">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
‏
مسؤول أمريكي:
فرقة عمل أمريكية تقدم المساعدة الاستخباراتية للسعوديين وتخطط لتقديم الدعم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90617" target="_blank">📅 19:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90616">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDG3G9-KxJVgPbitzR51V4Zdne6hjpp6tPjIb29RX3MZjG4d4JbSeWmNfBq_AwSKxYOFInmoHxi_LU6QpEvBM5YFEqSIt2EyEphELsVdZUxhQtju4psJoEz2y2URoyzNd-2lhh4UjyVxDqnre8529Vo6ttUDaRbFdtrqNmQS6WXMuY7vWjPSNuczdLGPG3jRQec9EYVwZUSb8xdtAFBDpuAHoTd4rYtJwztCGzYZpimvMJm9Y6YPjRdtphN0a2mR4tX1l3cQpCPA5L-hoUjfJPIpIRDLnRnNweWnapcoLBiFromxp9_RN9Nmq1ZW-RVBrUdzxICKMSKPXe_noq8-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
جيش العدو الصهيوني يختطف مراسل قناة (Press TV) الايرانية عند حاجز قرب بيت لحم.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90616" target="_blank">📅 19:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90615">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
جيش العدو الصهيوني يختطف مراسل قناة (Press TV) الايرانية عند حاجز قرب بيت لحم.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/90615" target="_blank">📅 19:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90614">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
بحرية حرس الثورة الإسلامية:
نعلن بشكل قاطع أن مضيق هرمز مغلق وتحت سيطرتنا الاستخباراتية، وأن أي سفن تدخل طرقاً غير آمنة ستتعرض لحوادث.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90614" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90613">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
وسائل اعلام ايرانية:
انتخاب إيران لعضوية اللجنة العامة للمؤتمر العام السبعين للوكالة الدولية للطاقة الذرية في اقتراع سري.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90613" target="_blank">📅 19:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90612">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc2xmx49pJDV5TB5jHA3MW8azKj5YlpWgMtL6tr5tUIpXwbNaPruxiwYXIdA6Ty92jI4gAgvvMbG1jry6R2LAdHHLZMsMjogLCuO2rCTCRdUGfT84bjx1ideSKccrsqsfeRqCW819ViYNWiicGOlKTrqeaG5kvME-VAmxkD4ba5FbZvapYZBUWUt68jAuZvPl3JmOLVDOYCQs-QYSUGOcax0-PK41PM0WkcAMZGh9P1CUQ6mEIAhaR1uyWUgHWecUxbrzZyR4gmj9Q2UpRJK1lS39YmTpl2NM-3e94-xn8kKo107qmIfoBDxLdmx8pgm604H3-6ZRSutGgZ7ZOhSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
محمد باقر قاليباف لبافل طالباني:
خلال حرب الأربعين يوماً كانت لدى الأمريكيين أطماع بشن عمليات أمنية وعسكرية ضد إيران انطلاقاً من إقليم كردستان العراق لكن بفضل مساعدة اصدقائنا في الإقليم والاستجابة السريعة للقوات المسلحة الإيرانية، تم إحباط هذه المؤامرة المعادية. يسعى الأمريكيون والكيان الصهيوني باستمرار لبذر بذور الفرقة بين الجيران - ولا سيما بين إيران والعراق - خاصة في ظل الظروف الراهنة، وبعد أن أُجبروا على الانسحاب من الأراضي والأجواء العراقية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90612" target="_blank">📅 19:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90611">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
مصدر للتلفزيون الايراني:
مقاطع الفيديو المتداولة للطيار الامريكي المزعوم مفبركة، أن هذه الصور ليست سوى إنتاج هوليوودي وجزء من عملية نفسية تقوم بها الولايات المتحدة للتغطية على الهزيمة الثقيلة التي مني بها جيشها في توغله في جنوب أصفهان. وفقًا للتحليلات الفنية، من المستحيل علميًا أن ينجو الطيار من السقوط الحر على ارتفاع شاهق وبسرعة 160 كيلومترًا في الساعة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/90611" target="_blank">📅 18:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90610">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
التحقيقات بشأن استهداف السعودية قيد التحقيق وتحليل النتائج.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90610" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90609">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
‏
الطاقة الذرية الصهيونية:
في إيران 440 كغ من اليورانيوم المخصب ما يعادل 10 قنابل نووية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90609" target="_blank">📅 18:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏المستشار الألماني وفق تدخل بالشأن الداخلي: نشجع بغداد على المضي بنزع سلاح الميليشيات بـ"حزم"!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90608" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مصدر لنايا   لا يوجد اي هجوم على مكة المكرمة ؛ النظام السعودية يحاول تحريك مشاعر بعض التكفييرين في العالم على غرار ما فعله في شوارع وأسواق العراق تحت رنة الحرائر والاعتداء على النساء .</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90607" target="_blank">📅 18:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90606" target="_blank">📅 18:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90605" target="_blank">📅 18:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏المملكة المتحدة والولايات المتحدة وهولندا تصدر بيانًا تحذيريًا بعنوان كشف برامج تجسس تزعم انها تستخدمها جهات تابعة للدولة الإيرانية لاستهداف المعارضين</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90604" target="_blank">📅 17:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90603">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
🇾🇪
المتحدث الرسمي باسم انصار الله في اليمن محمد عبدالسلام:
يواصل النظام السعودي شن غاراته العدوانية على اليمن، وقد تجاوزت أكثر من  350 غارة خلال بضعة أيام طالت الأملاك العامة والخاصة وأدت لشهداء وجرحى من المدنيين.
إننا نحمل النظام السعودي تبعات استمراره في انتهاك سيادة اليمن واستهداف الناس وأملاكهم.
إن التصعيد العسكري العدواني ضد اليمن لن يحقق أي هدف للنظام السعودي، بل سيؤدي إلى مزيد من تعقيد الوضع، وسبق للنظام السعودي أن جرب الخيار العسكري ولم يحرز إلا الفشل، والعودة لخيار فاشل ينم عن عقلية عدوانية لا تؤمن بحوار ولا سلام.
وعن نتائج العملية الأخيرة في الساحل الغربي فقد تم تطبيع الوضع والحمدلله، وحضرت مؤسسات الدولة لتؤدي وظيفتها في خدمة الناس، ولم نشهد أي من مظاهر الانتقام الأمر الذي يعكس الالتزام الأخلاقي والإنساني للجيش اليمني، وفي المقابل تستمر  السعودية على نهجها في ابتزاز العالم وتخويفه بحجة المخاطر التي تهدد الملاحة الدولية في البحر الأحمر وباب المندب وتحريضها بمعطيات كاذبة لا أساس لها من الصحة في محاولة لجر بعض الأطراف الدولية إلى مغامراتها العبثية في اليمن وتجريب ما سبق أن جرّبته وكانت نتيجته الفشل الواضح للعيان.
وإنه لمن المستهجن أن يسقط النظام السعودي في تبني حفلة افتراءات، ولا نعتقد أن من مصلحة الأطراف الدولية المجازفة بمصالحها بناء على أكاذيب النظام السعودي التي أدمن عليها طيلة اثني عشر عاما ومستمر فيها ولم يعد يصدقه أحد.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90603" target="_blank">📅 17:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90602">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
رويترز:
السعودية تبلغ مصافي نفط أوروبية أن شحنات الخام المقررة لهذا الشهر أُلغيت بعد إغلاق خط أنابيب الشرق - الغرب.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90602" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90601">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تعليق الإنتاج في 3 حقول نفطية ليبية بعد إغلاق حرس المنشآت النفطية خط شحن الحمادة - الزاوية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90601" target="_blank">📅 16:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90600">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
السفير الأمريكي لدى الكيان الصهيوني:
لا أعتقد أن الوضع بهذا السوء. ما نشهده هو مناوشات مؤكدة بين السعودية واليمن، لكنها لم تمتد فعلياً إلى المنطقة بأسرها. وهذا هو الخبر السار. لا تزال الولايات المتحدة والحوثيون ملتزمين بوقف إطلاق النار، وهذا أمر جيد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90600" target="_blank">📅 16:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90599">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد ضرب تحشيدات تابعة للعدو السعودي وإحراق أعداد كبيرة من الآليات شرقي الجوف</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90599" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90598">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii5zItPOjvWGY_omO30tyz3xW6g9fEWixBLfUFPFOKAltexeZhrM2icMrf_B20X4rhfDo5jaOww5EsaxUnJ6H4SK8tr9rVlkQOX3hXhoWk6XBffDZTIQBirKu0brjUDgxlUxn9df2R9aAEC5uziUk29DL57LH4AxbbtzDd10_CE3fKT2G5uQiduySMXfHa_p0LT817x9x03GoMVDIblR31R05eHsECp0cUvnj9NUN4xEmwekYck7D02zF9SdS6t_Lt7VGSG_okrUwheEF05TNky9iMp3yy2CJS36zwgqiOthKRsI4X1DYaQXHewTIdeZj54AaGoA8LDSnggD1D3rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن سلمان يصل مصر والسيسي يستعد لحلبه مستغلا المأزق الذي وقعت فيه السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90598" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90597">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1eMYMIdeMlwOY6i8jq9OKv753fzk6fD_77B1GSnP3rwCphL67efiJm9hPUIVwBxFnNzEkUPvoJof5KhAvbBxPUJ93fp2hMYdmfNHHn1UZ-2cpffw_y7nCcRkCimQUcFVU3MhBuftmez53Rinasew9EelUKAjbx_vQHXfnmtn4x47YRIZzxge9C31EmpZHdpBPyW1OVyMKfq2iekWdMDzx-mOxdkPKgfs0pbmCGXE6Z4CiDB406Eh27VLkIAWh6CKUCdNFlzIYNBk41aq-Mej8C_ENuGnzAxpkPARF1CLEyTm9cQWe1jPwef-DMLgMpj1rbAN7OO5NgCjxsgkkfzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد رفض باكستان وتركيا وترامب التدخل.. بن سلمان يجري زيارة يوم غد الى مصر لطلب النجدة من السيسي وطلبا لتدخل الجيش المصري بحجة ان سيطرة انصار الله على باب المندب سوف يضر بقناة السويس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90597" target="_blank">📅 15:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90596">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a01ecf561.mp4?token=o9RZ6lDYXXaQUXc26rMH2zHMZTn8RrGCdBz7Bzmh48EQyGoOhKPAcSY1j8ymOwCkey11C1gZbEVU-1ofqYK2Zf89H-oc6GDuMupyKeiV-MW93CjOT-mRNWk6ASdz09az5qcCOCi7T_HvqCq57OAvazpYc5sgn3JXyU7ioGcbfDZF7nJQKGjrDJ6ewnLY5_LtkSHCnmwYsoQ0OjMLka1bv-PlSW15aBpUUiym7n1GPMZzMlGkiJTgLf8ldx3Q0Qyh7IfsE1dHP5-wvxB9TLlG8g3XM1GiOCYlJ3wQUTtgMuhe-S-bUqxql__eQbsZb-LqGGz3KTCRS9RrB-QJpkMdbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a01ecf561.mp4?token=o9RZ6lDYXXaQUXc26rMH2zHMZTn8RrGCdBz7Bzmh48EQyGoOhKPAcSY1j8ymOwCkey11C1gZbEVU-1ofqYK2Zf89H-oc6GDuMupyKeiV-MW93CjOT-mRNWk6ASdz09az5qcCOCi7T_HvqCq57OAvazpYc5sgn3JXyU7ioGcbfDZF7nJQKGjrDJ6ewnLY5_LtkSHCnmwYsoQ0OjMLka1bv-PlSW15aBpUUiym7n1GPMZzMlGkiJTgLf8ldx3Q0Qyh7IfsE1dHP5-wvxB9TLlG8g3XM1GiOCYlJ3wQUTtgMuhe-S-bUqxql__eQbsZb-LqGGz3KTCRS9RrB-QJpkMdbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#متداول
صافرات الانذار تدوي في الاراضي السعودية بعد الهجوم الواسع الذي شنته القوات المسلحة اليمنية قبل قليل.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90596" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90595">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDXvjHVsIWaCqTXB6ABOGHmxGYlWnyStu3-kneeMXoDn6YXGHA41py3ZmkATg9gBXPeJe1v-IcDnknzNsgqxwEoNM0nKvyCM8KMkzdr4mV5UibB2YI2H9p3FB__JvZYpKGs2vl-pK0w9OgxoF3IyZm_RnF-oZ28WMMNoPrH8AM73WAFhGVDEDUXzhZUihv7qvXKgeUAvQ7j1bY-OiIV6zehqVba-fYU8qzs6Rg4Jp_IXJAtFX3dvOF-l6sirBdL9MIfOkdmqX_9qq-iJYMdNcIjp-1oCdnbRODxALXoy8niQDUusaG_7gp36YNmuWuL9ZuGWOz5_5V4xwYyAuWmxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط تنخفض عند 105$ للبرميل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90595" target="_blank">📅 15:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90594">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇫🇮
الرئيس الفنلندي:
سنقدم حزمة مساعدات دفاعية لأوكرانيا بقيمة 290 مليون يورو تشمل معدات طلبتها كييف بشكل عاجل.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90594" target="_blank">📅 14:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90593">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnCdcMWoAJwgQFos88Lup_Ur9iFu7HDDdUyJMoT0UycaVXgFyTPrwPZg5eFeq5p2YfWwsnCv2JK14xMJ9XMyfPEFsFmMtsLoGY-PYwbvq3s0Psh6ty1nxt4eU6d3-8UMQ4kh50xdlUnxdCl5jmsou3-3fQtuUVcg4jrAbCVLwUiWzyXJMZp1zk4GgLydODn8AlNWMA20-tyG4Bk9CXkwlc3rjF2-AMP3xBc17BB5ZUj8tLmqSBCbsQYaaLY-SgdVhSWbewa4__z4wVn2hIXg6nXBXqCTnrurrJ39TXcdy8gEf5xNelF9FAcONmk8Xisk-R9GQ5wID4IHfMgdnZ0ExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇴
النظام الاردني يبدأ بمحاكمة صحفي اردني لنشره الصواريخ الايرانية وتغطيته الحرب الجارية في المنطقة!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90593" target="_blank">📅 14:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90592">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
🇮🇶
وزارة العدل الايرانية:
سيتم نقل 49 مواطنًا إيرانيًا مسجونين في سجون العراق اليوم عبر الحدود البرية في مهران إلى البلاد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90592" target="_blank">📅 14:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
مركز الأمن البحري العماني:
سحب ناقلة النفط "إلجايا" لأحد الموانئ العمانية عقب تعرضها لإصابة بمقذوف مجهول.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90591" target="_blank">📅 13:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90590">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
ثلاثة مصادر لرويترز:
واشنطن قاومت حتى الآن طلبات السعودية لتدخل عسكري مباشر ضد الحوثيين إلى جانب الدعم الاستخباراتي.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90590" target="_blank">📅 13:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90589">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز أربيل شمالي العراق
🇮🇶</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90589" target="_blank">📅 13:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90588">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7EKEDU4yD3KajNrrsfAnNILuwYDC5W3u7u_6dCDTNKJSmfTEQok-Pg4qAeUkyrmWH7FQh2wCVFG2g55P6vLAmg1ZTkhJqoD2-Y8--9xHOS2uAM3-8v2Yd0omf8dDkld2k2QZOu7_ct4XtcquWxtC1bu3S_aznENnrcE_gAUzkKezsoVz8BSYZXGZnqi69sOmfbAnRW10jeSZ-fiV8eCh993Mlu9oWZjua6hkhkIYj76JtIFV_KxDNlIZ_oDUGPm02BcCBOdyzNFq7EHd9MyiwOd2UzGrZFNvUmYpkKFCh6a5_YfPECil_OBlKPoDcZpAQeEITv7tZ8LHpZ8KxjWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف الحركة كليا داخل مطار الطائف وسط السعودية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90588" target="_blank">📅 12:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90587">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkfuBi2HQF78hbT7OFeU5fos7eJBijLCJMwCw-z-stepnCkNodYhsmE784_I38jZ2xL8cqhVxOSHw4pBwYGRzsvZkf7nUn7CDBHAXjNRLO85S1oNqioEep7MTPnNkGbf50JTmXnCq0sXAh_fTQvy_kxpddKp8Uhdgfk5h43BuoovJsbDvI1ocV3wl3JYvs0U20VjpN7vzyDRcnqXjNR7w5OzEGvjuD0uSgvFh4W_GMAWxwxtyy9UZlm7Md6p0VH9nIb-3o9JwOGI77w3shycArvDSis8rTSGYIc5LpZlYk4em1zHEenEmrzmYhrI8e6FlJMW5ooV7QEjJrer6w8jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
🇮🇶
نشاط للقوات الجوية البريطانية المحتلة في سماء محافظة الموصل العراقية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90587" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">طيران العدو السعودي يستهدف مدرسة أبو أيوب الأنصاري في مديرية حيفان اليمنية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90586" target="_blank">📅 12:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تفعيل صافرات الانذار في مكة المكرمة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90585" target="_blank">📅 12:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تفعيل صافرات الانذار في مكة المكرمة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90584" target="_blank">📅 12:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات في مكة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90583" target="_blank">📅 12:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هجوم يمني صاروخي ومسير يدك اوكار ال سعود في الطائف</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90582" target="_blank">📅 12:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات في الطائف</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90581" target="_blank">📅 12:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90580" target="_blank">📅 12:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90579">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90579" target="_blank">📅 12:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9068b786be.mp4?token=BlNLytxv9Caz34Z2pua6FxNCEUa_LRmKl3xKHKjCVciC5Sg1T9UBPhyQusVGe0U43MfF7aPt1_o2S_412zF5wL_KZZ3Vk0214a4L-n1GXwFooOzdupQvBtw5ZfuzLhx6CAaji3MQ1Y-24otcd6nUE2nykwhjJyyEXPzf2rUvfpY817stH9SRfHmy8TB4KtWcZ0eu8GDFAoGuFQUDjCxhd9SQNbL4s0Q_LKGjPNchzt4bkKE8uXphUVG26y4R6kmcI2TpmZLBn3FD1YjqADdgRkwa5TwRhWfpTY07FPmEAi2Ej-LzST8pXvkSf_jo2H9enAk9CEKmW9g-Ti4JlzLelA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9068b786be.mp4?token=BlNLytxv9Caz34Z2pua6FxNCEUa_LRmKl3xKHKjCVciC5Sg1T9UBPhyQusVGe0U43MfF7aPt1_o2S_412zF5wL_KZZ3Vk0214a4L-n1GXwFooOzdupQvBtw5ZfuzLhx6CAaji3MQ1Y-24otcd6nUE2nykwhjJyyEXPzf2rUvfpY817stH9SRfHmy8TB4KtWcZ0eu8GDFAoGuFQUDjCxhd9SQNbL4s0Q_LKGjPNchzt4bkKE8uXphUVG26y4R6kmcI2TpmZLBn3FD1YjqADdgRkwa5TwRhWfpTY07FPmEAi2Ej-LzST8pXvkSf_jo2H9enAk9CEKmW9g-Ti4JlzLelA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة الزرقاء الاردنية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90578" target="_blank">📅 12:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90577">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o87VHVzAE-oip2WTpNIsLN5toYncjcQvCYR0eMZPagmn6l0mtObbPlIskJZthLASgZIJ3GVG2cmeTiZBHpzEvloBTb5m52HmoC6WpfgV705dqcQ_NTp-gUsCXPJNLgM-gr8jouF7t6Uri08NrPm_s31n89LHMTZCSIMvOBpWrAiQxSOvOX6KVFrUqkLgyWcY5fbptJ9jlgjvJ_NDKfKDgNyjAM0UpaDLG0pV4LvM9SJVaXxBTI-QVPgzTL0eQ_YgPO1pnKRB2mS-nRy0X1JWyrcdYG4e0c1JozP7zxizrB7EoK-P6rvo7q7xL5gj_ZueUBrPGOnmCZsqXym1sASexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة الزرقاء الاردنية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90577" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90576">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNg9r562VlAK4JsjbQD6W9oBqKCppFW8ActdfYcslHPY3E3e5nlLf0ZIR9Hy5In2m9w5D_hCo2rwBCiiRQ5RzZK0dPufUOIsDW_5si5eEPo1De-6mTtTu3Tdu2MD81l2rsaYBxaRLcxaw32uCo2FCI5r1aYS0PVDSpGIuDi98UlUMuGWXkkYx00GORonVmcPJ05KZcvlSAyoRmuw-fTX33IbSFhFzi3BajHD0j4NxP35fbedDt920S6JI9P-e8sMROWHRjdG1cprH_aVqNaMthP9aMA68B0Bwyh1cshDI67OaWs-5-AQhkNXieEL27ghbx96NePwa2yO4JLqblP3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية
: تأجيل بدء العام الدراسي  إلى 11 تشرين الأول.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90576" target="_blank">📅 11:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90575">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات تهز أربيل شمالي العراق
🇮🇶</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90575" target="_blank">📅 11:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90574">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات تهز أربيل شمالي العراق
🇮🇶</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90574" target="_blank">📅 11:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90573">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
لأول مرة في تاريخ امريكا
‏سعر الديزل المتوسط في الولايات المتحدة يصل إلى أعلى مستوى قياسي قدره 6.27 دولار للغالون .</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90573" target="_blank">📅 10:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90572">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90572" target="_blank">📅 10:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90571" target="_blank">📅 10:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90570">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428c901001.mp4?token=PMLJzij6TlsC3Jtr1vkyKoB3Qssv6RxRliSpbqim8REPmzQAKYWHGbdJwuIopme0pw33vNzp8cdZm43O3THclv7cbBNl8yVQrqubmcb3uMTg80ZL0OzVyOJhO5V7mcGIzlftoj-j85WRPN-3RzgrtkGc-i-YK5zQu2x7nHZL7sXvfWGPvYLYA59xx6GV8_UxZOcRfukD-6zVDCCpfTeGw85FkH3stx36IW9mXXkAwn9WtfcwKR2XUbZ5AWJ5P_iAPecNoZ-g4v_pGnPGlzFP8RdxLoJWhV80_vZ69PAaG7i4u0iGwQ9IfXZ0uSOtKfEhKk7xG_XHQieMfIkz0UQukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428c901001.mp4?token=PMLJzij6TlsC3Jtr1vkyKoB3Qssv6RxRliSpbqim8REPmzQAKYWHGbdJwuIopme0pw33vNzp8cdZm43O3THclv7cbBNl8yVQrqubmcb3uMTg80ZL0OzVyOJhO5V7mcGIzlftoj-j85WRPN-3RzgrtkGc-i-YK5zQu2x7nHZL7sXvfWGPvYLYA59xx6GV8_UxZOcRfukD-6zVDCCpfTeGw85FkH3stx36IW9mXXkAwn9WtfcwKR2XUbZ5AWJ5P_iAPecNoZ-g4v_pGnPGlzFP8RdxLoJWhV80_vZ69PAaG7i4u0iGwQ9IfXZ0uSOtKfEhKk7xG_XHQieMfIkz0UQukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
قلق ومنهار وخائف ولا يستطيع الوقوف على قدميه
ناشطون يتداولون مقطع فديو يظهر به الأمير عبدالعزيز بن سلمان في لقاء صحفي مباشر بعد انسحاب القوات السعودية الموالية لهم من اليمن وسط تكهنات بتناول الأخير جرعة من الهروين او أدوية معينة جعلته يظهر بهذه الصورة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90570" target="_blank">📅 10:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90569">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
🇮🇷
🇺🇸
إدارة الولايات المتحدة تدرس "هدنة نفطية" مع إيران تركز على فتح ممر آمن لناقلات النفط عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90569" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
🇸🇦
اعتداء سعودي على مديرية صعدة في اليمن العزيز</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90568" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90567">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccu2pjwVwM9BFWoktBpMM2zLfUHUY7yNU_sWCEkFHcFRNC6PROnlgQcle_cmvhQGOVdVcB9uVX-0Z39yWpPxBgEw6TJ9QF1d8rCl26kuZj7I-_G32EdYV6qx80oJm9oW4v6kiL3SLfcRP2wmNRPPDVkNdbAQu2f1bQbVDngyXAkmkVs4ePBm-x7a1dQ8y11sINWF5BBZ11ZszArThpkvMQncPxeR59468F_pSNr-UeXZyTHVfK1K8Q36zBslUKJY9zf_x5m8Nm_kCaokYUOlAw6iEmqaeE2P0YLN9gP6HgXB_a_Nr52GZ55KLtE6NyTy3SEzlTYUbg7mO2r2ojBJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
البنتاغون عن عمليتها ضد ايران:  22‏ مليار دولار للذخائر المستهلكة، 7.4 مليار دولار من الالتزامات التراكمية، و3.7 مليار دولار في خسائر المعدات، لكنها لا تشمل إصلاحات البنية التحتية.  ‏أكثر من 50 طائرة تضررت أو دمرت حتى الآن.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90567" target="_blank">📅 09:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9F4iKVQ2Di87pPvKhHBa6I7YbdaQipT5jeWh10WpeotGiVzTxS1XnT1YPxhLrdtORKyOkrSsjWk43P1FzgOT63boH19xfSu98oqQl44uEcia3EohJtM52p3XQljrVVJ1rPeC5_1ClT6cVWINl6uzfxGCp48lTLHHtHTsqTDFif8lGf6g-VelvZb6KC4if31L0YdyGP-tWCV1AKqtg9ERLSPfDgCNGXmTd3t5O9BoZH7Kb-smQ713N57K_PafUQvOg5mdr4mipJDBAUos9EGTzbcgEJkHWWuxoWVa3IZKenSaNEL7S7JvbUoxkZSObU2Tjvh5oKjCbt8X9wXaRWFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الان توقف العمل بمطار أبها جنوب السعودية دون معرفة الأسباب والتفاصيل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90566" target="_blank">📅 09:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-N7E6wzs5K5WqSGK8d5h9-WXuNtxy9rUpmdn-vQ6HIbwkT-4PfXlpON7XuxTicIuHd8d1VDAWlu3BOaoa4uzAPvJvJWxstvXfZC85eZFAriZcTCyFXPp9dtTuJV0HrifPqB4S6Zva6OuXYawTp1m7oOFnJJLSvnTNbbUCcH8KPFVX0d3o4Dkt2LFmTcjEyAdWVFuKL14IyHmFb0LLoh8k64xO1fcmEf93boEuxgnMqqa7Xr1BFzEM18QfK2UWzMe9MbMsX2qCmdgwJDX6soemD986HGOlqQRqSlT2edo43efyY9weP_sN0CHGO0n3GHN82aOK0K0t8K-56OQYbC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الان توقف العمل بمطار أبها جنوب السعودية دون معرفة الأسباب والتفاصيل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90565" target="_blank">📅 09:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90564" target="_blank">📅 08:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله أكبر
🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من رصد وإسقاط مسيرة أمريكية من طراز MQ1 في الأجواء الغربية لمضيق هرمز.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90563" target="_blank">📅 06:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJlmv6NKa_NuDPVts--ISD3PoOV1k4DOV8SOu7omdIj-GHclfsmMIx2roifFt-Ub4BpKyl4bT_NPddrUwvMZ7jU4cA3Btmf8ntdMG7cz_-ukfCRFM9baZVE_MCmQrPaBjqCnKF8E2wF3S3G_sl2TV54HlMmc5Fyj-9NWA8IYCzgzRPoZz5UG1tY1JmAPstt3U_nbTHR_oKyIhu4sVLwu9pJ5l0AYyqQLMA0kHMnl3ouEQEqVBqJw3EX0OCad_qQfGniB9_eknG07a69lWx9iAHN8JGOdIsaoNNH3lcSWZkqxqAgxJusDKNhg7Bno95VKSz-DF4_ucmTdeqFj9_hqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90562" target="_blank">📅 06:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
وول ستريت جورنال:
تحذر شركات النفط الأمريكية من أن أزمة الوقود العالمية التي توقعتها نتيجة للإغلاق المطول لمضيق هرمز قد حانت الآن، حيث تتناقص المخزونات التجارية وتقترب الاحتياطيات الاستراتيجية من حدودها القصوى.
قال مايك ورث، الرئيس التنفيذي لشركة شيفرون، إن العديد من العوامل التي حمت الأسواق في البداية من حرب إيران قد استنفدت الآن.
تفاقمت الأوضاع بعد هجمات الطائرات بدون طيار من العراق، والتي أدت إلى تعطيل خط الأنابيب السعودي الذي يربط الشرق بالغرب إلى حد كبير، مما أدى إلى إزالة ما يقدر بـ 2.5 مليون برميل يوميًا من سوق يعاني بالفعل من القيود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90561" target="_blank">📅 06:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
رويترز:
تراجع حركة المرور بمضيق هرمز عقب تصاعد الهجمات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90560" target="_blank">📅 06:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90559" target="_blank">📅 05:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90558" target="_blank">📅 05:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇸🇦
🇺🇸
🇾🇪
منظومة الباتريوت الأمريكية تفشل في صد الهجوم الصاروخي اليمني وإصابات مباشرة بالجملة في المدن السعودية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90557" target="_blank">📅 05:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ1oheVibrluTYgxccbw_zGcOU_UlZW00axqbnO0dqX1Kdu0Two3WNWSmvPABCn0NHePE_XfBYjZ1notKsrnA32pJGSmsOJB6wNFy1iOu7rIQiJY-0D2nWWH4qAgwJvZU5oI3kodmFT3fDJ9bJdyWeZWzbqe3MRa9LWL4CZ_QDZunBsaVmzaKVb78Aumn-bCUNOXRsKFiGvBqKMgims5SLyRO4-YU1I77itwcQRp6HdbiK5ZjllAOthI2DPHMgJD-dMoKEhB67RsLb5gW4QiZawZO-QMKBHu7oHNox25ffv-661D13hdv5dIOY3PzpztqmvkimbpH6wqIUOgIxLD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الطيران المدني يترك أجواء جدة عقب الهجوم الصاروخي اليمني.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90556" target="_blank">📅 05:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
🇺🇸
🇾🇪
منظومة الباتريوت الأمريكية تفشل في صد الهجوم الصاروخي اليمني وإصابات مباشرة بالجملة في المدن السعودية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90555" target="_blank">📅 05:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90554">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات في الجدة السعودية جراء هجوم صاروخي يمني واسع.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90554" target="_blank">📅 05:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90553">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اصابة مباشرة في منشآت نفطية بجازان جنوبي السعودية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90553" target="_blank">📅 05:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90552">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جازان تلتحق بالمدن التي يتم دكها في هذه الأثناء من قبل القوة الصاروخية اليمنية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90552" target="_blank">📅 05:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مدينة أبها تحت رحمة الصواريخ اليمنية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90551" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90550" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات في الجدة السعودية جراء هجوم صاروخي يمني واسع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90549" target="_blank">📅 05:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90548" target="_blank">📅 05:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90547" target="_blank">📅 05:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
🇸🇦
سماع دوي إنفجار في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90546" target="_blank">📅 05:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
مجلس النواب الأمريكي:
تأجيل التصويت على قرار لسحب القوات الأمريكية من الأعمال القتالية مع إيران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90545" target="_blank">📅 04:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
المحكمة العليا الأمريكية ترفض طلب ترامب بتقييد التصويت عبر البريد قبل انتخابات التجديد النصفي في نوفمبر.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90544" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇦
السعودية:
تعرضنا لقصف يمني بالصواريخ الباليستية والطائرات المسيرة في أبها وخميس مشيط والطائف؛ إصابة 13 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90543" target="_blank">📅 02:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYWhYliFRBAe1yj8dMGiPYnpkHBmuGaQgYPrZIWVypYqLZ0fywzOF-SbHdVKs4GT5G6jFb8Bp2oYkompPMP7zDzF0Up-3e17Pr8JYJM1glmgTpN83ro7_9AptABCC9uBm4DtH3l8gHvxBDzFKbaT2p7_UIxMI8oOpOW632TMg-v0jKNVf6qiwB1zl1x0HOjrDxFqSdACza5vL0JnVucvzSJ31wIr9rsgAzh6fsAt461eYM0QJ8FX54UYZHD0OvousUNAQjbwwaWcs_zj_-VgSsRL2RYO0CWUsSeQ7f4qnnxttuPvZANEwhWob6xjnf37NmlW8kxXp21Yyo_1SUNwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشقة صواريخ يمنية تدك خميس مشيط وأبها جنوبي السعودية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90542" target="_blank">📅 01:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90541" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90540" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90539" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2GVxLTsQJibN4cQA9ETIeUg0jJ3pPKP9Y277_ZYJ1hlNx6E67iTllNfRy8DnuXHdiSrkfWUN-BbKljjl7HKhj7_oEppamSfqna6dEwhZuL8eT8k6a8MQXQszga4H20Am8-rOedPuEknNHrPrrolOrDm9Hu68aiDSgFkjz0ySpTBfati0mZYrIwLJOYlo-C_9LxXi8m_OyNFMOvyuWZqou-crLLmmGvcjD1KGqt8f1ms5DnHCgGemsi8W5S4QGhhaK0IGnVywEiG7rS3bDjfYEw10d8kpL_0Ds34g8H_nPzhSdjjQ7da2YplKYqb9BP_WBPtXuNLQHoAGsCJdZIVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
‏رشح ترامب الضابط الذي شارك بعدة عمليات ارهابية في العراق ويسلي هانت لمنصب سفير الولايات المتحدة لدى السعودية، وهو المنصب الذي سيشغل شاغراً منذ أن بدأ ترامب ولايته الثانية في يناير 2025.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90538" target="_blank">📅 01:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
‏تم إقلاع طائرات حربية تابعة لحلف الناتو في ليتوانيا بسبب احتمال وجود طائرة مسيرة بالقرب من فيلنيوس.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90537" target="_blank">📅 01:20 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
