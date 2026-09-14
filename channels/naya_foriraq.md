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
<img src="https://cdn4.telesco.pe/file/a9UZFFyrL9mMNFMEGCmzUEQb4u5i9vnTITT7vPBjyjKQvt76jp6hcloscqZEWrrAyFam5DPo0rEtcfFlPdbALQbWWjCWJnpSQWwQ0uN2bnuP6oE24-wdh0HA2DswJiSmKzsFHKTGL4Tr45oytPmFUA8ruH_ACEyIuaHNzBffW-NpuIJT2cfW70kW62P-nbYhAoyNNVoK8-v753PkjhPxFK3xUAEziLQ4uNhpQtNENRNYHVv9hYHFWGWdrH_0Ba7kiePUPyrbNLallMYLMacjaZ4YOERITUH2k0Hqhhc5fnKSOc6UJ4dYwbmdxb4kaAMVbsbAR1crktWSLFeGpMQ87g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سماع دوي انفجارات في مدينة جابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/naya_foriraq/90497" target="_blank">📅 18:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
نتن ياهو:
حزب الله سيتعرض لضربات أشد إذا هاجم مرة أخرى.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/naya_foriraq/90496" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
إغتيال أحد علماء الطائفة السنية في مدينة زاهدان جنوب شرق إيران على أيدي عناصر إرهابية تابعة للموساد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/naya_foriraq/90495" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بعد رفض باكستان وتركيا وترامب التدخل..
بن سلمان يجري زيارة يوم غد الى مصر لطلب النجدة من السيسي وطلبا لتدخل الجيش المصري بحجة ان سيطرة انصار الله على باب المندب سوف يضر بقناة السويس</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/naya_foriraq/90494" target="_blank">📅 18:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
إذا كان العدو السعودي يتصور أنه وبعد 300 غارة شنتها طائراته خلال 5 أيام سيبقى وضعه آمنا مستقرا فهو واهم.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/90493" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات للتحشيدات التابعة للعدو السعودي وتعزيزاته في صحراء الجوف شمال منطقة الكنائس.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/90492" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات للتحشيدات التابعة للعدو السعودي وتعزيزاته في صحراء الجوف شمال منطقة الكنائس.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/90491" target="_blank">📅 17:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
العراق يوقع مذكرة تفاهم مع شركة توتال الفرنسية للمرة الالف كون الـ999 مرة الماضية لم يلاحظها احد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/90490" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSjceiiGYIF_nyg6CqnpO-ODb1MwzB2UbVtzkxGoXIMIxWi6WiwqW5Zd2BtukE1BjYkOlSP11phLU3npNSzmyenx0WfHhIdMROE2lQiQecYZNOZCDoLNZ2eFGKGpWt5OdCW58r-jXe4hRbEJNkezDmC7lVFViJtALmV6gDBzWLzBCpURZYdj9nMiGuqA1_Jkzyv_dR5j7RbbiLzBMmaiqFm3BoewjnG7ufXtdIiMvvbvf_o1LcYSqPZqcA0hMd-Nxap0PZGHxaDbhEEs5ZGHPG2leyKVuBgKtz86GrnboJfvRb7aJvyTi2rVtOl9L8fQR1H_ar91ErTa_fqX7lX_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط ترتفع الى 109 دولار للبرميل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90489" target="_blank">📅 16:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مسؤولين سعوديين لوكالة أسوشيتد برس:
تعرضت خط أنابيب سعودية حيوية لنقل النفط لضربات وسيتم إيقافها عن العمل بشكل كامل لعدة أسابيع لإجراء الإصلاحات</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/90488" target="_blank">📅 16:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba222bebd9.mp4?token=EfxbjJGma1cT2OspWGtveNzJK4Y5FL53PxDscXP6sygVwObLlnT1EMgLFNdKQgAD-_5NgK175PiHXZyResPKH77rKhmXPqou8NIQ_sKUTqq35UIA-6hAEKEjU1sWuhUb4vOR4uCfqShcOwywH5h90VZLM_OMYIlGVaDXxAxnVOuBO7pq4XjHM6hp78o7Y4tgUIKC9kCV-Lqx_GWivyTRlTPZqiaSPzjbyAvMK4oEB_dD5BGJvAkcnFZ74882c0Sd2UeJzM0iExo5Fj1fBsgOKnXQZclKK1W0c8AERNb4zqzp77ETvdnCXqOb85LsOK8bgpuz_3AOwYXduynGKfl0FhW1yzNkR5iG4oUHlQoK3Cc5YgrHE8QpmbVeqR7Lpk9OjQrn6v3STxl9cjdiKEAOmpOfK7vyS7GkB8RfAGp4HcHkyCEX8pxoBdQIPhdOO43Q3d2UBbBDwltjfns6eVsaZwZe_TUsxmv3_bkh0MxEWTkw-nsxusYW7WxTRPQZexMrZz5BOtdZk4pXMsiCswsPo35sBQ7BOJy6-CQq2PRYJvA40M2gep8TSjFjzDoxHb0gd1KkHpEu6Z7i7VRM_H6TFFhuiXQvdTlfo6pFA9ibyOUOrdTg6i_iue_bY1iO0xUg2pwjXROHVTSr2lXFxOYKt6kk6hgCpP9BKpVyfH0QgBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba222bebd9.mp4?token=EfxbjJGma1cT2OspWGtveNzJK4Y5FL53PxDscXP6sygVwObLlnT1EMgLFNdKQgAD-_5NgK175PiHXZyResPKH77rKhmXPqou8NIQ_sKUTqq35UIA-6hAEKEjU1sWuhUb4vOR4uCfqShcOwywH5h90VZLM_OMYIlGVaDXxAxnVOuBO7pq4XjHM6hp78o7Y4tgUIKC9kCV-Lqx_GWivyTRlTPZqiaSPzjbyAvMK4oEB_dD5BGJvAkcnFZ74882c0Sd2UeJzM0iExo5Fj1fBsgOKnXQZclKK1W0c8AERNb4zqzp77ETvdnCXqOb85LsOK8bgpuz_3AOwYXduynGKfl0FhW1yzNkR5iG4oUHlQoK3Cc5YgrHE8QpmbVeqR7Lpk9OjQrn6v3STxl9cjdiKEAOmpOfK7vyS7GkB8RfAGp4HcHkyCEX8pxoBdQIPhdOO43Q3d2UBbBDwltjfns6eVsaZwZe_TUsxmv3_bkh0MxEWTkw-nsxusYW7WxTRPQZexMrZz5BOtdZk4pXMsiCswsPo35sBQ7BOJy6-CQq2PRYJvA40M2gep8TSjFjzDoxHb0gd1KkHpEu6Z7i7VRM_H6TFFhuiXQvdTlfo6pFA9ibyOUOrdTg6i_iue_bY1iO0xUg2pwjXROHVTSr2lXFxOYKt6kk6hgCpP9BKpVyfH0QgBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتظاهرين السوريين يبدأون بمحاصرة المنافذ الحدودية والحقول النفطية احتجاجا على تردي الوضع الاقتصادي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90487" target="_blank">📅 14:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صوت الانفجار في العقبة تم سماعه من ايلات</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90486" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار يؤدي الى تسرب غاز الامونيا في المجمع الصناعي بالعقبة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90485" target="_blank">📅 13:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار يؤدي الى تسرب غاز الامونيا في المجمع الصناعي بالعقبة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90484" target="_blank">📅 13:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اخلاء ميناء العقبة بالكامل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90483" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انباء عن انفجار في العقبة الاردنية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90482" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انباء عن انفجار في العقبة الاردنية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90481" target="_blank">📅 13:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحقّ مدير عام شركة توزيع كهرباء الوسط عن جريمة الكسب غير المشروع
- قرابة (13) مليار دينار قيمة الكسب غير المشروع في أموال المدان
- الحكم ألزم المُدان بردّ (25.7) مليار دينار الذي يمثل قيمة الكسب غير المشروع والغرامة الماليَّة التي تعادلها</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90480" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
تحطم طائرة خاصة في مطار مصراتة الليبي كانت ستقل أحد الشخصيات والسلطات تقرر اغلاق المجال الجوي</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90479" target="_blank">📅 12:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بن سلمان يستقبل قائد القيادة المركزية الأميركية لبحث ملف انهيار المرتزقة في اليمن وسبل انقاذ بن سلمان من الورطة التي وقع فيها</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90478" target="_blank">📅 12:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط وأبها</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90477" target="_blank">📅 11:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90476" target="_blank">📅 11:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇸🇦
🇾🇪
القوات المسلحة اليمنية
​استهدفنا المرافق والبنى التحتية العسكرية من حظائر الطائرات الحربية والرادارات والمدرجات ومخازن التذخير في قاعدة الملك خالد الجوية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90475" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇨🇳
🇺🇸
الخارجية الصينية ردا على تقرير بشأن مساعدة كيانات صينية لإيران:
اتهامات لا أساس لها</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90474" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇺🇸
سقوط طائرة أمريكية MQ1 في سماء هرمز من قبل الحرس الثوري</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90473" target="_blank">📅 09:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f066tT35c9HsWrwZudRGCjuFwRTSMCmQWYWgCmQeJUiGQafGHp34YIHQmpACqHpdEc0g-7nBTU0OLbSKraHNFAPpGOMQDJgxtcFw5EZNMMb5zYWtcmHZSWWOf8GCMZB2nGJxxxAlexXWOwVcwcYfuiOaL1SpsEFWk6EIdIVLLHvNS3Ur2F5leRKc_cQUVWn88gQol3GIZ3rcbZt49vht0PleDzUzcsZDWmBODigfsKUShFCNPIpvbnTUA9IvPIo6JIukJEqQK9gy1997YsLWnlKkoxVtGVHSnhPGAhJ2vbUrD8ZFqejWNs5jIbOGqOlAfH4uuO77wmVT3g4D9GWuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
إعلام العدو:
مقتل جندي إسرائيلي خلال عملية عسكرية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90472" target="_blank">📅 09:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇸🇦
أبها وخميس مشيط تحت رحمة الصواريخ والمسيرات الإنتحارية اليمنية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90471" target="_blank">📅 07:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇸🇦
إنفجارات جديدة تهز السعودية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90470" target="_blank">📅 07:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇸🇦
إنفجارات جديدة تهز السعودية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90469" target="_blank">📅 07:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇸🇦
إغلاق المجال الجوي في مدينة أبها السعودية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90468" target="_blank">📅 07:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇸🇦
إغلاق المجال الجوي في مدينة أبها السعودية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90467" target="_blank">📅 06:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
مشاهد تبث لأول مرة يُزعم أنها من عملية إنقاذ الطيار الأمريكي الذي تم إستهداف وإسقاط طائرته في سماء إيران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90466" target="_blank">📅 04:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22c5506e3.mp4?token=fZRRmD0iYBnd7ipx-D1psRHqBgAI24R324PUySFtCRFFxow5gu4cmPSVOI2da8q9m81vDvDyFPmQoHo8RjsYuhG9OjxG6Resf-zNpMYDXhTf-w_5DsDxRlcZvYVdrOfBP8pBKz2q-hFzxjOvmnZEIXVDPYU8WU98EmwkCS8t1AQe94WlghqKh1ii-C6hfj2DwWF0szU-fAUdqBl3Ytj5GvLIaXSQlHeBCl2XCO9SNAsWvmcGm_q165T3gyL_D-LtzmxnF8xIx9Ht-iqFCoRz5qB5IATRBUaMfX4CEBTFqORfcCIef1AUeN7wZado0dTKxobHz0_gnaJEhfS5rDfFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22c5506e3.mp4?token=fZRRmD0iYBnd7ipx-D1psRHqBgAI24R324PUySFtCRFFxow5gu4cmPSVOI2da8q9m81vDvDyFPmQoHo8RjsYuhG9OjxG6Resf-zNpMYDXhTf-w_5DsDxRlcZvYVdrOfBP8pBKz2q-hFzxjOvmnZEIXVDPYU8WU98EmwkCS8t1AQe94WlghqKh1ii-C6hfj2DwWF0szU-fAUdqBl3Ytj5GvLIaXSQlHeBCl2XCO9SNAsWvmcGm_q165T3gyL_D-LtzmxnF8xIx9Ht-iqFCoRz5qB5IATRBUaMfX4CEBTFqORfcCIef1AUeN7wZado0dTKxobHz0_gnaJEhfS5rDfFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من الإنفجارات التي طالت مقرات الإنفصاليين الإرهابيين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90465" target="_blank">📅 04:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90464">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17baebc59.mp4?token=hYbinMQ0CvhxqfvspPea5rzQ3WHnL7o-LudTc3-n6-5LJPBiMmS3aGq6SKtPGO4Gs8JZDxIQSyUew2p1nSgrt9OcbhPPcBOTpSBx3y29QGmxHKZinqgQT-LNf1T6tgQImezklWOu6XdE52mVil2qXieC28yeuwV9xCuEyweemV3SEet9RSNJLKx2nYs5TqZITIvXxHZ-cHGi4yHsIYHWkG-b9KXL2mPygLtL7nuzmMyV6CEg5LQJDKU_LaCuWkLfSK8U5ogLQKzLvit5uWwGCm0fcc2UwqaDTriMR8zr3iwfvMzWLpglE1ML1KcFatle8DLWqXSh_-9fGxQxHkM7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17baebc59.mp4?token=hYbinMQ0CvhxqfvspPea5rzQ3WHnL7o-LudTc3-n6-5LJPBiMmS3aGq6SKtPGO4Gs8JZDxIQSyUew2p1nSgrt9OcbhPPcBOTpSBx3y29QGmxHKZinqgQT-LNf1T6tgQImezklWOu6XdE52mVil2qXieC28yeuwV9xCuEyweemV3SEet9RSNJLKx2nYs5TqZITIvXxHZ-cHGi4yHsIYHWkG-b9KXL2mPygLtL7nuzmMyV6CEg5LQJDKU_LaCuWkLfSK8U5ogLQKzLvit5uWwGCm0fcc2UwqaDTriMR8zr3iwfvMzWLpglE1ML1KcFatle8DLWqXSh_-9fGxQxHkM7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
موقع معادي أخر في السليمانية يشتعل بعد استهدافه بالصواريخ والمسيرات الإنقضاضية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90464" target="_blank">📅 04:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc104b6518.mp4?token=oHA_7CxboOjpZl6H9HrkpftOdez4dy8o8aJua-rHULJ9EomtyxnSBUq0yY1A4_JuaKlXNMmhoM_MV24vKQZtBAd35txFZRy0J6h5NAQlhf3Rbtqbaa8d0vRBBVBEysFNmfAY-dkXjInqNGx2C_vTbV_pcEkwg7VdmzA9fmG9cS0jDBB1KPlrguSJdPj1npA1Vtkhj3dvMQzHZipqipkKZuLP2u244z-bZLGB3QFTBHHVr6cQoeHkMBoPv1Kg9EHcbY9Mn-0Cd_0Nf_6IVtFok8qMvjIPWd_PxAIhqGG7TEqlDT_jN7LbP98eB0N2FLKXS64sPXbnX4C3Pdi48uhWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc104b6518.mp4?token=oHA_7CxboOjpZl6H9HrkpftOdez4dy8o8aJua-rHULJ9EomtyxnSBUq0yY1A4_JuaKlXNMmhoM_MV24vKQZtBAd35txFZRy0J6h5NAQlhf3Rbtqbaa8d0vRBBVBEysFNmfAY-dkXjInqNGx2C_vTbV_pcEkwg7VdmzA9fmG9cS0jDBB1KPlrguSJdPj1npA1Vtkhj3dvMQzHZipqipkKZuLP2u244z-bZLGB3QFTBHHVr6cQoeHkMBoPv1Kg9EHcbY9Mn-0Cd_0Nf_6IVtFok8qMvjIPWd_PxAIhqGG7TEqlDT_jN7LbP98eB0N2FLKXS64sPXbnX4C3Pdi48uhWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إستهداف معاقل المعارضة الكردية الإيرانية الإرهابية في السليمانية وحلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90463" target="_blank">📅 04:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5077c09cec.mp4?token=E0ODUfKCIkJRDAYDGM_r0f1JNSw_j1_6KscnseVWGr8IwwhbXeWn-7MAtcFbfYM-sf5Li4nTA3FDSZ92uBxt-yIBR1cd8h7yJ_EEWzJphAA4S1z3Ga8jmdhyabUh6EREOuot_0VSLoBRaV3cy_GWcwv2y6RljcvLHSLKBjYokkKrLTzmrTqpsM3l0sPiXpWFctt9DqlYFSL0DDSIsAf30Ptf0I_mR6bZBiKcvaGOy4jGuMUP3dUbzj1uSZIh629y-QZfmE9xZuVJux0Ba7VcDjW9zr_TNFLfXou1Z7_SsTqpxeUJPP3q2JhNheF4EwWDsqixK5PW4EEZgelYZx1SVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5077c09cec.mp4?token=E0ODUfKCIkJRDAYDGM_r0f1JNSw_j1_6KscnseVWGr8IwwhbXeWn-7MAtcFbfYM-sf5Li4nTA3FDSZ92uBxt-yIBR1cd8h7yJ_EEWzJphAA4S1z3Ga8jmdhyabUh6EREOuot_0VSLoBRaV3cy_GWcwv2y6RljcvLHSLKBjYokkKrLTzmrTqpsM3l0sPiXpWFctt9DqlYFSL0DDSIsAf30Ptf0I_mR6bZBiKcvaGOy4jGuMUP3dUbzj1uSZIh629y-QZfmE9xZuVJux0Ba7VcDjW9zr_TNFLfXou1Z7_SsTqpxeUJPP3q2JhNheF4EwWDsqixK5PW4EEZgelYZx1SVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إستهداف معاقل المعارضة الكردية الإيرانية الإرهابية في السليمانية وحلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90462" target="_blank">📅 04:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d668f759dc.mp4?token=KBhbizvTvu8RaBd1n3ZM9d7-nEqZMP6Wu5aURtZcZByPuPqBg0xLvnBKM9Hj6WB-2qwTSMrY6u4HnOmouW6uSDVkLsyemFEHY9mil6oFwPk4YVW4Z3hX003B4n6lPwqxpzoUMoJdAHUKtt-uVZlnyJIaPj4Iq2dmSoInK0YMSmdF7K23IGg_I2RG567A1jQuDuVRdb1w8z6qDczrcrYZPJdGSEr8ttSbeO4XGdXKk8g4MSTSiUPGue-scYhEKf0c4Pdxvm6U7SyMIVYWAd5zl_HK740XRRXqpHiETaATyNW52lQky8HDnsEstY4E7SY5qQb-yibW4cUFra1hWMTbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d668f759dc.mp4?token=KBhbizvTvu8RaBd1n3ZM9d7-nEqZMP6Wu5aURtZcZByPuPqBg0xLvnBKM9Hj6WB-2qwTSMrY6u4HnOmouW6uSDVkLsyemFEHY9mil6oFwPk4YVW4Z3hX003B4n6lPwqxpzoUMoJdAHUKtt-uVZlnyJIaPj4Iq2dmSoInK0YMSmdF7K23IGg_I2RG567A1jQuDuVRdb1w8z6qDczrcrYZPJdGSEr8ttSbeO4XGdXKk8g4MSTSiUPGue-scYhEKf0c4Pdxvm6U7SyMIVYWAd5zl_HK740XRRXqpHiETaATyNW52lQky8HDnsEstY4E7SY5qQb-yibW4cUFra1hWMTbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إنفجار أخر يطال مقرات الانفصاليين في محافظة السليمانية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90460" target="_blank">📅 04:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7b1032f4.mp4?token=sZPRn2UEqyeGaIqSLKAax1air4z2wMYeoRAS9X-pRqUELfhLhpuux0ihRy1Z_tEde6qGO8VDIW8sqZJNsbqH6GaOpQAmHWfqmJg8PdVX3seSGJhsXDwZoat7pWt_VtAM6u1Z9WXUSRsWHc8i2RvNCyWxH19QJa4O_8gvmEm1owYqVj0GQMwCYOENs1vibWA5e_qTI82d1R9Gv6J_hwM5YbjaAvitW5GpRBAVxDpa35DhN6nHHjzSsLuF_fwiwlaOjLON43oxBPSWg7NYuxESNfcRYpo_dfRtzBo7EC0thazSo81zfLU6WX2eIkmXqOMUg9M-kf-UHHCBLOnvylSOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7b1032f4.mp4?token=sZPRn2UEqyeGaIqSLKAax1air4z2wMYeoRAS9X-pRqUELfhLhpuux0ihRy1Z_tEde6qGO8VDIW8sqZJNsbqH6GaOpQAmHWfqmJg8PdVX3seSGJhsXDwZoat7pWt_VtAM6u1Z9WXUSRsWHc8i2RvNCyWxH19QJa4O_8gvmEm1owYqVj0GQMwCYOENs1vibWA5e_qTI82d1R9Gv6J_hwM5YbjaAvitW5GpRBAVxDpa35DhN6nHHjzSsLuF_fwiwlaOjLON43oxBPSWg7NYuxESNfcRYpo_dfRtzBo7EC0thazSo81zfLU6WX2eIkmXqOMUg9M-kf-UHHCBLOnvylSOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
نيران واسعة تشتعل داخل مقرات المعارضة الكردية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90459" target="_blank">📅 04:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e4717b1a.mp4?token=rRlic82fB8Kdv0PMlASkVs-fDfDputSnsIxfFnuswgoU1hFZWP9C37VlrLqyXsT3mXxhWlCeInMON94GiCfHuBwGib9nJ-hi9hi29nnnS_NrNteUfat0j-AcUiA6IFo9M4IvVLFrUV4aK_79co2PrzuSDbDD_rDlQX3wj-E81TGyMZXsaDJWg5B6Cj5k2wV1bQe6AKTfEzQoAS06y6DWU7ijpLwrZqRJj0rPMbtlWoCClL2s8yJYSXiCblAbGfoX_VRDdX6J4Ywg8fQbCuHOTmLxKs-ToYZBoPla7OHvE4jHnVj2ewOoj3Kk1aYq7yR1q46XDeyWf5BuBwbUpecaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e4717b1a.mp4?token=rRlic82fB8Kdv0PMlASkVs-fDfDputSnsIxfFnuswgoU1hFZWP9C37VlrLqyXsT3mXxhWlCeInMON94GiCfHuBwGib9nJ-hi9hi29nnnS_NrNteUfat0j-AcUiA6IFo9M4IvVLFrUV4aK_79co2PrzuSDbDD_rDlQX3wj-E81TGyMZXsaDJWg5B6Cj5k2wV1bQe6AKTfEzQoAS06y6DWU7ijpLwrZqRJj0rPMbtlWoCClL2s8yJYSXiCblAbGfoX_VRDdX6J4Ywg8fQbCuHOTmLxKs-ToYZBoPla7OHvE4jHnVj2ewOoj3Kk1aYq7yR1q46XDeyWf5BuBwbUpecaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في حدود محافظتي حلبجة والسليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90458" target="_blank">📅 04:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a8ccc74f.mp4?token=Sg1ZfuSTtjz6lji9cJAYqXdSKDa80WVrUPyJ7ZrxLYnwe_bPo_rjstQBZBAojXEr6HmVHP14PZSxe-qSqllRp-jn28bssgMfPF1Umn-35OniiyAYWYlYFcJ-jzWCpeK0HzQ1L3cA-H4mTv4Il32yS9uY5Xu7GhBkQRMHn99h1M_AGV3Mf_kccCfRlCzITn31W4HePB60UOLLlo9qNldNn4R-TBfj0yWERyg8Dm5mbME280QmjZrdkTSSuUvhP-JSZz_LcxVgkJVdCJDImsjThr-zm8qnOvgKgqng9n1SSOsxNhdD6wgMQrEIMkJzo-4p6BDIXOaa-LRJM8gdpbN0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a8ccc74f.mp4?token=Sg1ZfuSTtjz6lji9cJAYqXdSKDa80WVrUPyJ7ZrxLYnwe_bPo_rjstQBZBAojXEr6HmVHP14PZSxe-qSqllRp-jn28bssgMfPF1Umn-35OniiyAYWYlYFcJ-jzWCpeK0HzQ1L3cA-H4mTv4Il32yS9uY5Xu7GhBkQRMHn99h1M_AGV3Mf_kccCfRlCzITn31W4HePB60UOLLlo9qNldNn4R-TBfj0yWERyg8Dm5mbME280QmjZrdkTSSuUvhP-JSZz_LcxVgkJVdCJDImsjThr-zm8qnOvgKgqng9n1SSOsxNhdD6wgMQrEIMkJzo-4p6BDIXOaa-LRJM8gdpbN0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد النيران وأعمدة الدخان من مقرات الإنفصاليين الإرهابيين في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90457" target="_blank">📅 04:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e1608766.mp4?token=ISwfvsfT8WgOW-B9LnLeVWURwzgJfvqnuJz-H5_IIWAIvk0uxB3x9nLtYfaQspRB1ctQ48KKhigEK7k0MBdz4wsVBF0sChN4pTBua9TKvitg7JWxWvZb_h9pSjnmHX4F4q9pVAUWwOZYNcQeyoPE91nWH7NKJtPHi_NHk_p9F6EaQMpj6BV-q02aN4NqRLD7fbt3Lskvbndz42--At0woSSuYqSJ2gEb6Y2IdkkHwco_bGStBBVSWyawgD8ZD6r_4nLeTUXNPsZ_dE_2ND3r5-hrMARTlPTwpeQ-B6_Iu0_LMNaaLmrSFDXkRy4cCfjVaNwabgLCguo3on5XM87DuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e1608766.mp4?token=ISwfvsfT8WgOW-B9LnLeVWURwzgJfvqnuJz-H5_IIWAIvk0uxB3x9nLtYfaQspRB1ctQ48KKhigEK7k0MBdz4wsVBF0sChN4pTBua9TKvitg7JWxWvZb_h9pSjnmHX4F4q9pVAUWwOZYNcQeyoPE91nWH7NKJtPHi_NHk_p9F6EaQMpj6BV-q02aN4NqRLD7fbt3Lskvbndz42--At0woSSuYqSJ2gEb6Y2IdkkHwco_bGStBBVSWyawgD8ZD6r_4nLeTUXNPsZ_dE_2ND3r5-hrMARTlPTwpeQ-B6_Iu0_LMNaaLmrSFDXkRy4cCfjVaNwabgLCguo3on5XM87DuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم صاروخي يدك مقرات المعارضة الكردية في السليمانية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90456" target="_blank">📅 04:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce42da010a.mp4?token=UTYctRxXPhjIF7PNoICj4VYtrqhe9b3QpEaK5LvxndRS9jI2-RLAvMuyt2J3uhs7cE5A-T58MzzGpEC2JcCpeAbpUX3WZg2CS4wXGs5bWhXEYNeqFL9Y2erHH89mvqEyE9Ow-VZ78xqrp7auiEn1Qaei_o-PgERYDeF-1cAIk8CBf6yYWD9RNX9oin-CEhZ_7yX6DVptEKgc9Eq08XsG7e2-dTIK1uCLKpPh5QZY_hxIVBrdh84crRO22fXGSx_06RcnuzT61lJHNICQ0Z6_5hViB6rFtjeflMz5snAaO0KkVBebMQFIKKdi6Iycg55WWvIQrXn1iuiGJiGsEvPT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce42da010a.mp4?token=UTYctRxXPhjIF7PNoICj4VYtrqhe9b3QpEaK5LvxndRS9jI2-RLAvMuyt2J3uhs7cE5A-T58MzzGpEC2JcCpeAbpUX3WZg2CS4wXGs5bWhXEYNeqFL9Y2erHH89mvqEyE9Ow-VZ78xqrp7auiEn1Qaei_o-PgERYDeF-1cAIk8CBf6yYWD9RNX9oin-CEhZ_7yX6DVptEKgc9Eq08XsG7e2-dTIK1uCLKpPh5QZY_hxIVBrdh84crRO22fXGSx_06RcnuzT61lJHNICQ0Z6_5hViB6rFtjeflMz5snAaO0KkVBebMQFIKKdi6Iycg55WWvIQrXn1iuiGJiGsEvPT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
دوي انفجارات عنيفة في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90455" target="_blank">📅 04:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي: ‏ بعد أن قفز من طائرة مقاتلة أُسقطت فوق إيران، أصيب ضابط القوات الجوية الأمريكية برافو بكسور في ظهره وذراعه وكتفه عند ارتطامه بالأرض. وبعد إصابته البالغة وعلقه في وادٍ محاط بالمنحدرات، استجمع قواه وتسلق سلسلة جبال يبلغ ارتفاعها 7000 قدم…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90454" target="_blank">📅 03:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
مشاهد تبث لأول مرة يُزعم أنها من عملية إنقاذ الطيار الأمريكي الذي تم إستهداف وإسقاط طائرته في سماء إيران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90453" target="_blank">📅 03:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569e706fb.mp4?token=Y-fZXTQOyMcFUzdMg9t1H7IrNYSzXOirT2y4tFKBMtsWq6NHrH9nPvNacPxEsapip_sKgWZCQlflsVmCuU0eobXvz_ZJJ23tNGlzxsNlp4x_WkfkFdyYEweje97b-8C8aseQBlFEcyhEwepmYRuxIXeqE8Dj7M6EyeJpFoPuknyw8rBLKo12tquxjv-fyfJ9uqMunc1qi_47PAI4Y_qYQ7hS_ppJAkR7wz-7jtrYAvmrXYEHqa2VTHJXCRW_qupsM3R4xuuToUUOlqYoF8e71lfmXGLEU4XsWKdALwaf0msz8W4WLyyJT2fHW54qe4SMkdRH9fC8hMZQPJ8a_VliDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569e706fb.mp4?token=Y-fZXTQOyMcFUzdMg9t1H7IrNYSzXOirT2y4tFKBMtsWq6NHrH9nPvNacPxEsapip_sKgWZCQlflsVmCuU0eobXvz_ZJJ23tNGlzxsNlp4x_WkfkFdyYEweje97b-8C8aseQBlFEcyhEwepmYRuxIXeqE8Dj7M6EyeJpFoPuknyw8rBLKo12tquxjv-fyfJ9uqMunc1qi_47PAI4Y_qYQ7hS_ppJAkR7wz-7jtrYAvmrXYEHqa2VTHJXCRW_qupsM3R4xuuToUUOlqYoF8e71lfmXGLEU4XsWKdALwaf0msz8W4WLyyJT2fHW54qe4SMkdRH9fC8hMZQPJ8a_VliDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد أخرى من عملية البحث عن الطيار الأمريكي عقب اسقاط طائرته الحربية في سماء إيران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90452" target="_blank">📅 03:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b24b025b.mp4?token=nHEq9RGURYveV-L78lP32KQyycjqxABiuAFbrqxtCWArcH1Sr8AVTEa7LY5jA3vdA4PA96hCSX8ssghGZyx04nAfBhC8vioaiFQiBCBvi3htgO_7AIyNJffGsy0_QGHR8z_KZ3dvBM3VaNC-xtCYOPdd1dy9FsoQX-CDUgRmd81SOM44llJddvjK9_j8NU6ha5swbPhHyYeRGrzeLLsT3az0pf7SugzGv5znpwKbHJZhKrSpCh_h7QkJjd8okelkh0_opkZ3IrKbBidn5-FaLcvxJ-rLpkZrWUq3qKLXLGpc6giXHXUnZQcAgk1r3rGwU0Mb-o9hbC-8oY7o1CQozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b24b025b.mp4?token=nHEq9RGURYveV-L78lP32KQyycjqxABiuAFbrqxtCWArcH1Sr8AVTEa7LY5jA3vdA4PA96hCSX8ssghGZyx04nAfBhC8vioaiFQiBCBvi3htgO_7AIyNJffGsy0_QGHR8z_KZ3dvBM3VaNC-xtCYOPdd1dy9FsoQX-CDUgRmd81SOM44llJddvjK9_j8NU6ha5swbPhHyYeRGrzeLLsT3az0pf7SugzGv5znpwKbHJZhKrSpCh_h7QkJjd8okelkh0_opkZ3IrKbBidn5-FaLcvxJ-rLpkZrWUq3qKLXLGpc6giXHXUnZQcAgk1r3rGwU0Mb-o9hbC-8oY7o1CQozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي ينشر مشاهد يزعم أنها تعود للحظة العثور على الطيار الأمريكي بعد أن أسقطت طائرته في سماء إيران.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90451" target="_blank">📅 03:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
دوي انفجارات عنيفة في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90450" target="_blank">📅 03:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751012e241.mp4?token=MJAvhLjc_mUsiIuEYuCphfopsnYuvbcLgunBVQfNYE0SkkmRHe0Y4rJU_MxlgaxczLsw6yinNM-9qb9OoDpwd7xgMprJznSmbd8RqD6t2KAd7kx9kusobhExQyficof3hY1Bklgxz-l491o_qNhly-H4up7_CI65hv4dqqmTYVVXGQKVUIzJ3LUiI1WyqU_nD3PdQZ8qDOxL3i1YVWvcUY-y_vyU94iwIH4mjvu1rT_qka2Lfx-RtB07CreDKt7S2wmwqNChlYC1v1aupCNp6-oDh1_VJ8Ykqfn5XXXv16ImVEB-BsdRYTFHdeVogg7BCu3KFgIVuEBoM8GxvWqzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751012e241.mp4?token=MJAvhLjc_mUsiIuEYuCphfopsnYuvbcLgunBVQfNYE0SkkmRHe0Y4rJU_MxlgaxczLsw6yinNM-9qb9OoDpwd7xgMprJznSmbd8RqD6t2KAd7kx9kusobhExQyficof3hY1Bklgxz-l491o_qNhly-H4up7_CI65hv4dqqmTYVVXGQKVUIzJ3LUiI1WyqU_nD3PdQZ8qDOxL3i1YVWvcUY-y_vyU94iwIH4mjvu1rT_qka2Lfx-RtB07CreDKt7S2wmwqNChlYC1v1aupCNp6-oDh1_VJ8Ykqfn5XXXv16ImVEB-BsdRYTFHdeVogg7BCu3KFgIVuEBoM8GxvWqzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد تبث لأول مرة يُزعم أنها من عملية إنقاذ الطيار الأمريكي الذي تم إستهداف وإسقاط طائرته في سماء إيران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90449" target="_blank">📅 03:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287fa3322f.mp4?token=RvuhzQTbfj_zyKA2kxJpIsVxdNqQH1JMkd7I-ySjyoMwJM-i5fcDOuYd5WFOnEI9gM9mV1VFdI8oV3LHFWDvXwnvmRHHT8D1FSNuOzRngqnErzS_HtTTOw5X3OiHls5fGAk9LG4c1CohH2HiFYyg8tqOskLcQxMJWayUEqOR-x6ecFh8p-DrFHc6Ia8Y6JjTrAHmOquUbM10L0Xp5RXwPPpTfFQC5X0Af47QRrG0zHe6pd1iVK_R-5xDNDXzfJLP46P55shdjSANQ9OMrVkWvhhsNsxon3gYboQVPu-sufK6S0OmetwYzvZucjAXmPckOlFbCKtTKQClNUqwZJa1kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287fa3322f.mp4?token=RvuhzQTbfj_zyKA2kxJpIsVxdNqQH1JMkd7I-ySjyoMwJM-i5fcDOuYd5WFOnEI9gM9mV1VFdI8oV3LHFWDvXwnvmRHHT8D1FSNuOzRngqnErzS_HtTTOw5X3OiHls5fGAk9LG4c1CohH2HiFYyg8tqOskLcQxMJWayUEqOR-x6ecFh8p-DrFHc6Ia8Y6JjTrAHmOquUbM10L0Xp5RXwPPpTfFQC5X0Af47QRrG0zHe6pd1iVK_R-5xDNDXzfJLP46P55shdjSANQ9OMrVkWvhhsNsxon3gYboQVPu-sufK6S0OmetwYzvZucjAXmPckOlFbCKtTKQClNUqwZJa1kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد تبث لأول مرة يُزعم أنها من عملية إنقاذ الطيار الأمريكي الذي تم إستهداف وإسقاط طائرته في سماء إيران خلال حرب رمضان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90448" target="_blank">📅 03:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
إشتباكات صاروخية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90447" target="_blank">📅 03:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسراب من المسيرات تنقض على مواقع حساسة في جنوب السعودية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90446" target="_blank">📅 03:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90445" target="_blank">📅 03:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90444" target="_blank">📅 03:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هجوم صاروخي جديد يدك مدينة أبها</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90443" target="_blank">📅 03:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هجوم صاروخي جديد يدك مدينة أبها</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90442" target="_blank">📅 03:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فشل كبير لمنظومة الباتريوت الأمريكية في صد وإعتراض الصواريخ اليمنية التي دكت مناطق جنوب السعودية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90441" target="_blank">📅 03:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تنفيذ عملية تأديبية واسعة من قبل رجال أبوجبريل على آل سعود</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90440" target="_blank">📅 03:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تنفيذ
عملية تأديبية واسعة من قبل رجال أبوجبريل على آل سعود</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90439" target="_blank">📅 03:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtYh4j_IUck9hb4tWjb2Oy5ufKPgnJj5YADMe4LEVEbBk1JNcTWBdO5ReuRuGI0UV46jw27MWu3DF7pTwCG7Vr3BreJqnmt5WE9kxGyTdbKj2Nx4pf8XuWLim1aquJNgfi3y748E7EsyJYmOFNvLkf13RwCST9EisJe3aI3oBhA_3rkhtXdNXEJk6SkRm057tmOc-ZwqmhgvfRnEdkB_RE_SaTTmkjtw5BOIDXtDAe2XEAdMay76-FUEtOHUK2OHDHLZEbnE3JSpxlusGm8XAzNnW7H8-8DN8agbnhP_cF0cwySSi3vZ4kV5-Dz2gLyM8CVsmnvzPM1eoqQixlmZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdkxPgONpdG4RzR96UEx3KpW4suG7w_p7ZOc3RVuuiomx2KIU6Vzj939tbT9sju_tcN0bw1FZcEMiMOXToV2x45E8x2Cb-79yAb9Q1VbHGU-c0eUU70JI46ITSRTUtmV7W_k2I-nqx444JUO0r89KbrWNy4kmvSRb8AoBhM84BYT0kchnq8sknr_hYnpUVFUy4cl7gIY9m7vxO_Dnba45hbZddReThimSPXbcFYhNOU3pVW5Z3-UIyVEnrDiwZHllkU26odA6Cr8eUWlKLmOLnQKXT85ghZrSONb8aOonOVSQpT69GOElSMIITAqF9dC7380a-cbFYYi3JkYEhAUiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصابات مباشرة في منشأة نفطية بجازان السعودية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90437" target="_blank">📅 03:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXWfrq-_CTRSubYeAyduYaXBmTr22U81yz2jBFw8LfV2kJIvqHLB5O1YgifypJwf9hHGTuNnsfyfVf41CfD97DfLd0JluonYEOFQnneQPqtev7foWwFEPHkhM2_lwO1BfD4Hw62wPbKYCJjx-wFVGmlX4WL87Xl0DBvdJAHW8_6REAbo_eO4AKHeAQ3Ctohf2bSzJdvpHEMDO9XZG5Dj4Y2dNUE7DZlBPeWCMcYScMIegtHvd_vJTWUyqxIU_MXH23t_8FmCq7kdbBsxJ23PotqeYdxC6ESB8auNhbfiEilS8EjK6JVrOhdep7el5wJVBRQpwgwqZKcjaqFXpYgpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجران اصابة مباشرة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90436" target="_blank">📅 03:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90435" target="_blank">📅 03:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90434" target="_blank">📅 03:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90433" target="_blank">📅 03:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90432" target="_blank">📅 03:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90431" target="_blank">📅 03:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90430" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90429" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90428" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90427" target="_blank">📅 02:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90426" target="_blank">📅 02:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90425" target="_blank">📅 02:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
ترامب: الكثير من كمية الديزل تأتي من روسيا.  تتعرض مصانع روسيا لقصف من قبل أوكرانيا.  لقد طلبت من زيلينسكي عدم قصف مصانع الديزل والمصافي.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90424" target="_blank">📅 02:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تتمكن من دحر مرتزقة السعودية والسيطرة على منطقة كهبوب في باب المندب.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90423" target="_blank">📅 02:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e507f19a.mp4?token=b0vVNsx_KKKVihc-t9jg4zxdKa04Bpa5mtJBZQIRpExSfJGWGZW5IHDpKr-RXKTORc9ZwDOIq00jjwXd0NSl-rIe6v9YrJWzTlPu9vkN51RMFToyNqvRxWz6Zwmusv3nTAcgMxV7csIBLEbNf015a4YfqBdw8fAF09QEvhC543cP0HZ2e2MD2sqbgRsAPshnW6yJVyosCtDogDCPzorDnYwArtyqzJm6tONE5hAbpvQSbBrNFubPmjDKHr5WX-5cklOW1K9HRW49Ov5OVBIlSOnOj3IDmZhl1WH99jFfK-NesHgfw8bn6nFkWI0PMn8wt_QKz_ymURDUps49BCVqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e507f19a.mp4?token=b0vVNsx_KKKVihc-t9jg4zxdKa04Bpa5mtJBZQIRpExSfJGWGZW5IHDpKr-RXKTORc9ZwDOIq00jjwXd0NSl-rIe6v9YrJWzTlPu9vkN51RMFToyNqvRxWz6Zwmusv3nTAcgMxV7csIBLEbNf015a4YfqBdw8fAF09QEvhC543cP0HZ2e2MD2sqbgRsAPshnW6yJVyosCtDogDCPzorDnYwArtyqzJm6tONE5hAbpvQSbBrNFubPmjDKHr5WX-5cklOW1K9HRW49Ov5OVBIlSOnOj3IDmZhl1WH99jFfK-NesHgfw8bn6nFkWI0PMn8wt_QKz_ymURDUps49BCVqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
بعد ورود إتصالات من رقم أجنبي تطلب إخلاء مبنى..
إطلاق نار كثيف في حارة حريك بالضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90422" target="_blank">📅 02:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">“
🇷🇺
🇮🇷
🇮🇶
🇸🇦
🇾🇪
The war involving Iran and Yemen is bringing Trump to his knees.”  This statement by Trump comes amid a rise in global oil prices, which have approached $110 per barrel. What is amusing is that Zelensky was carrying out U.S. and NATO orders in an…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90421" target="_blank">📅 02:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
المراسل:
قد تكون كيانات صينية قد زودت الإيرانيين بصور الأقمار الصناعية.
🇺🇸
ترامب:
هم في الأساس يفعلون ما نفعله. أعتقد أنه تصرف بشكل معقول، وقد تصرفنا نحن أيضًا بشكل معقول.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90420" target="_blank">📅 01:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWudg8gm2NC0dS1zBY-9XLTu6xaycpyCd1IwauKKJ0iuRTiCKBMtf4xF5HI20LLHuTXtbNZVB9SmsinSIyATh6YU_Lwu93r3ZnOif1MLoEEvvbGtSZsoxNvllXrI0z7-qXKtzqjvIXTtzNy3s0ZMydw2oG0dnVf6I7VTTkPdEl9ClsZMnDyS0dUvGFTidZiGzf8FT6rDR2fUpBLlCg7ibiQZoinApyCa2RgIgSE7H1Py6vbWdqbqsSHOvE7Pgw--1O30Moqeyg4p4BjU3h7KOBqbeV992HLwgLe4DvX40mUr0VA0HUqsJML-6TRE7JCN-2c1sHYm2AJvN0UaYdkf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إرتفاع أسعار النفط العالمية حيث وصل سعر البرميل الواحد إلى 108 دولاراً.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90419" target="_blank">📅 01:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
إشتباكات صاروخية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90418" target="_blank">📅 01:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axZBXd0GRT5WtGaOj0XJljjiEIXo7HYIyPuntmrczpFOHKUm8rdzdx3kQFV53Srr-m6fjEEBMtGA_bN5ohIaE-sf0UBm7JCLwKGA_sV7-qwnX0tE-nwjluW49cEYLzsfwSkDuzNC1cXVNhDfOoCUgTwHWkcGTcbM7agX0uEC4tObycgBASB2nDUuxmmV32JaKh8f4NFFVwbCtnheKp6GHU1Yxy5FTpz7tot3a1ucACKyhibF-OlkdX3pIcDenu--k8NRql3vx1Iv5I9jGy1VwT2oW1fEUDOp178qABsWYZP-af6PbHQ_cSimzfIl7cvv2vkZWzFcCGk4My86_IkWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
الأمن القومي الأمريكي يعتقل ضابطًا سابقًا رفيع المستوى في جهاز المخابرات العراقي رعد العنبكي، خلال فترة حكم نظام صدام حسين، في مدينة ديترويت الاميركية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90417" target="_blank">📅 00:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f7cf570d.mp4?token=LzDsE1cJ2c4UZeGjUQbbeW6ok4HBeZcx6kZyY5FmDMY3MckD5rqkmAttbCMKoP_ju71bApqqGmIqZlk6z9oQyCuFExHL4Y72l5SMDAQzIcUMVrio2kpVj8t1mg99C8OUzYhxZs3G2Ae3EfzccbcV_2Ak7n5zYlGQ251PZIn5f7fTDdVBMnIgW8cgx6Lp4PNjsXY_LLQwpU8sH9MhE59SzJrkuymS8RQeaI-j2yqcGJRX8pIMDj-afrjtla5UxuSzksndUsEulw5kLfgxieTx5UIM_0qt5IDm6EUIF-ECMAzyt7HjoolRu7CV_JHsDlUMrNLHlYWJL7gj2Q_wNPtmXWoHj2cRNJYTOL2ui_qeEL68dOFgi3zfaZS0kjlnP1vwjPYa2RqCeZz_afh_nf4pltRPxToqu6g05AinTQV9s43NWLli_YFrcTW7kVThdcGR8FMutEKkj_RCUHe9Y63211LobnIVnPufXZJCgsjCVQIrWsxRZqMosuRka88Eh4-BlLZrhLeM4cOcaLvTwOTYO7jpAXlGC6p74NyURVjoJsl7xDFflyFyuVGhx-cHeUj1ldF0oYJpji4ukkxdr50e-NdPKvj-Sy0i6upqZnluXmEbMRRbUT3zEKRuaahMvTKfyY1N29KAMJNYYn958swAgJSofHuStK9eK5dhKyd8-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f7cf570d.mp4?token=LzDsE1cJ2c4UZeGjUQbbeW6ok4HBeZcx6kZyY5FmDMY3MckD5rqkmAttbCMKoP_ju71bApqqGmIqZlk6z9oQyCuFExHL4Y72l5SMDAQzIcUMVrio2kpVj8t1mg99C8OUzYhxZs3G2Ae3EfzccbcV_2Ak7n5zYlGQ251PZIn5f7fTDdVBMnIgW8cgx6Lp4PNjsXY_LLQwpU8sH9MhE59SzJrkuymS8RQeaI-j2yqcGJRX8pIMDj-afrjtla5UxuSzksndUsEulw5kLfgxieTx5UIM_0qt5IDm6EUIF-ECMAzyt7HjoolRu7CV_JHsDlUMrNLHlYWJL7gj2Q_wNPtmXWoHj2cRNJYTOL2ui_qeEL68dOFgi3zfaZS0kjlnP1vwjPYa2RqCeZz_afh_nf4pltRPxToqu6g05AinTQV9s43NWLli_YFrcTW7kVThdcGR8FMutEKkj_RCUHe9Y63211LobnIVnPufXZJCgsjCVQIrWsxRZqMosuRka88Eh4-BlLZrhLeM4cOcaLvTwOTYO7jpAXlGC6p74NyURVjoJsl7xDFflyFyuVGhx-cHeUj1ldF0oYJpji4ukkxdr50e-NdPKvj-Sy0i6upqZnluXmEbMRRbUT3zEKRuaahMvTKfyY1N29KAMJNYYn958swAgJSofHuStK9eK5dhKyd8-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المرشح الفرنسي للرئاسة:
الولايات المتحدة تستعد للحرب مع الصين، لن نشارك أبدًا في تلك الحرب.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90416" target="_blank">📅 00:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90415" target="_blank">📅 23:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ba7c6492.mp4?token=pN1iu1K_lj0CRTPLoQ0NmWSSfNmh4hFfm0WtgTtze2DXFbP6fdg4f2Q2JeV8LIR9u62y1gGTJJawcsXv6cT45V7yvxmYIpJLgJLT9GQuZOR_nwbq9qQ-MwxRwI0pNdQicqCEL4_C5HpxNI1sup3A146KZa0M5EkFNy4sRSztR0SVrn-07b7pukrsa7uKpsFHQ-fdHruk5NUFDpLntKsSK3ChJYPpVuWxrz4I8oXbDFKP9XVt6DbXmoHtNCxg-qJls2gBsdeeiI6wC3na98y82fvvjYE9Fs6HW8iCQiZG46Pabt2TEg7luBdhb2JP8Le9tnC7YRTZBUIYBFxaNanZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ba7c6492.mp4?token=pN1iu1K_lj0CRTPLoQ0NmWSSfNmh4hFfm0WtgTtze2DXFbP6fdg4f2Q2JeV8LIR9u62y1gGTJJawcsXv6cT45V7yvxmYIpJLgJLT9GQuZOR_nwbq9qQ-MwxRwI0pNdQicqCEL4_C5HpxNI1sup3A146KZa0M5EkFNy4sRSztR0SVrn-07b7pukrsa7uKpsFHQ-fdHruk5NUFDpLntKsSK3ChJYPpVuWxrz4I8oXbDFKP9XVt6DbXmoHtNCxg-qJls2gBsdeeiI6wC3na98y82fvvjYE9Fs6HW8iCQiZG46Pabt2TEg7luBdhb2JP8Le9tnC7YRTZBUIYBFxaNanZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇦
الشيخ همام حمودي
: العراق أكبر من أن يكون عضوا في اتفاقية مكة</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90414" target="_blank">📅 23:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90413" target="_blank">📅 23:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgSymdkGf20DXJ1LEbJk1qirS0897rVEsPjBBfW77-vKefrW_XVpFFnhj0CNEydqG7iorEJwcs44ZNdH5FoisNM613N4eDd6c3eonx_H1S6ZEuBlMkWzfPltIe-VfZlJVbtKHAHSQ_JnLnQjF4c0cjUA4n-NwjmxquDeyRmWVOM_KFkmG-ubE_925RrIF1izbbls5uVGpLUe27-rexJ4SiLIa7DhRplONltMjCA7pRcK4o1QgkLzHx3D9KROyIHBJyn9ULG7DAqmrRvKsDGSm1r7oVUy0LbzX4T4otmoVeqMRfO1OZPTncSIRGagd6olsBj6x0skkHCa966ohMqsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon inshalah</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90412" target="_blank">📅 23:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
السفارة العراقية بدمشق:
أعدنا ممتلكات في سوريا إلى أصحابها العراقيين.
😆
شارع بهمن حاليا</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90411" target="_blank">📅 22:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3bb77f66d.mp4?token=Fcw01QD-LmX2kbVO1E2FdHWmT3zOS7FL8i_j9Znnkad5ZI3S3EORQ_LpVW6Vi2P4JdH6ZgdGAjjKMJs0JSLqJIPk5uwJT_sJwoMsbxQVzZUm1Ji_yulN618jF9z-xPo7kLf_R4g5OReIp62waF4KurYrz20aAiOzNTXSo6kvKap48USxBHTuoxvM1sVKBRh5d32SMo-Jvc7sB29KlIa1tFpXtjSsqY4yWZPXUjKCMOXb4rx9bEJKazVa7oRZolV4BWE865L1DhtjFM4i3hUlcyn0Rn8lF40td8VKT21jnR85u9Z6JwwTzqD3sv9pboiO93WAc5DK5hptw293C39FRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3bb77f66d.mp4?token=Fcw01QD-LmX2kbVO1E2FdHWmT3zOS7FL8i_j9Znnkad5ZI3S3EORQ_LpVW6Vi2P4JdH6ZgdGAjjKMJs0JSLqJIPk5uwJT_sJwoMsbxQVzZUm1Ji_yulN618jF9z-xPo7kLf_R4g5OReIp62waF4KurYrz20aAiOzNTXSo6kvKap48USxBHTuoxvM1sVKBRh5d32SMo-Jvc7sB29KlIa1tFpXtjSsqY4yWZPXUjKCMOXb4rx9bEJKazVa7oRZolV4BWE865L1DhtjFM4i3hUlcyn0Rn8lF40td8VKT21jnR85u9Z6JwwTzqD3sv9pboiO93WAc5DK5hptw293C39FRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الصحفي: تقول إيران إن إحدى سفنها تعرضت للهجوم الليلة الماضية. هل كانت الولايات المتحدة هي التي قامت بذلك؟
ترامب: لا أريد أن أقول.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90410" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387e122db7.mp4?token=i16GDrg8Z1uHIHlSH8hTiEGCSdmS5iOhJrljIYio1cGfuEBwEbFFaajble0AwRe3I0bERosfyIRWIl__Nk1qS3yiYl1XssIkfVs_6hMi1XGvUZQ8tSOxFPgIkb42-h0gnHUUa7obI-g6115N8j0jKjjWskeF0O3R-KNjRYw6zH9GQs5YPB4wdhIKm3SiuSAZqJHzIJuO7uW_LPxRgqdD-UVr6WBzFsi3s6I-pvD0bKkZIS9s5lcZ73sqBXgY4z_Qkd-RFd-jExSCQEcR2hDSq3vSGcq1bNLecuY0qAIgiaFCGWg2-Z-0wHBNkmbi4KZ-DR1EO3jexh1lmIH0-cfkHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387e122db7.mp4?token=i16GDrg8Z1uHIHlSH8hTiEGCSdmS5iOhJrljIYio1cGfuEBwEbFFaajble0AwRe3I0bERosfyIRWIl__Nk1qS3yiYl1XssIkfVs_6hMi1XGvUZQ8tSOxFPgIkb42-h0gnHUUa7obI-g6115N8j0jKjjWskeF0O3R-KNjRYw6zH9GQs5YPB4wdhIKm3SiuSAZqJHzIJuO7uW_LPxRgqdD-UVr6WBzFsi3s6I-pvD0bKkZIS9s5lcZ73sqBXgY4z_Qkd-RFd-jExSCQEcR2hDSq3vSGcq1bNLecuY0qAIgiaFCGWg2-Z-0wHBNkmbi4KZ-DR1EO3jexh1lmIH0-cfkHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اعمال عنف وتخريب للممتلكات العامة في عدة محافظات السورية بعد قرار رفع سعر المحروقات رغم شحتها.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90409" target="_blank">📅 22:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99dac0b3e1.mp4?token=mACwlmeKtrxY3QfJFxBCF0hSCCn0OV1HADtQHNzzilPGHAnsD14ajyxbi7lHYt9dsu_1yjrHJ5oKysIdt-T3X2XZrY7SYO_H87jdOm7y-T9AUvBFm-mazzImXSiVT7x_HDNJDaLf1OzCcc4YF56kuCPzbCx6x_xXn28X5BHx8E9u-JRVjgVNPqD4uXgrYpuL9aeSgHTlno4AAROs0HGrX3gU9nSfe_3WblipZtKqILI7Hk293APctlf2u53MGsh9hHIkJN1TFshsXItqY_43xy_k_YwqyVWJMtlCmTMLtiHWSjI4laGOf5HsuYlojLsVL1wsIGS5IfeefWO6CL79ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99dac0b3e1.mp4?token=mACwlmeKtrxY3QfJFxBCF0hSCCn0OV1HADtQHNzzilPGHAnsD14ajyxbi7lHYt9dsu_1yjrHJ5oKysIdt-T3X2XZrY7SYO_H87jdOm7y-T9AUvBFm-mazzImXSiVT7x_HDNJDaLf1OzCcc4YF56kuCPzbCx6x_xXn28X5BHx8E9u-JRVjgVNPqD4uXgrYpuL9aeSgHTlno4AAROs0HGrX3gU9nSfe_3WblipZtKqILI7Hk293APctlf2u53MGsh9hHIkJN1TFshsXItqY_43xy_k_YwqyVWJMtlCmTMLtiHWSjI4laGOf5HsuYlojLsVL1wsIGS5IfeefWO6CL79ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
احتجاجات عارمة في محافظة إدلب السورية، على خلفية الانقطاع التام للمنتجات النفطية.
بدنا حرية
...</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90407" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6901b9a141.mp4?token=nFwdNSy6qQBEbi6_Z8ySVK_LvkEvFFheIBg54AO2Sh56fh-ZO9CDcD7JCR8wgDBkc-Q0e7vRYiHCbV8QIcBlY1Htvns3SDMGmG9irKH182lEqbWcanjs14fkwnSDI1udjKgJaO9DKN7NLTWHNKoycMbbxSBI9P3V0BoAdPtj9ScdeqVnZNQXli-RUXgFPilRweM1oi4TZvgvImX7BH0aFHe_o1-qeoWoKTRP0Ue0eTpPwjWl5GsGcO2vP9lOxsuG7mf0Sa8h0QWKN20z_5DDbF5Chc7vq5rgdeE5ksLbX5rMO4f2BAe-dy8EbT5I2V68SUF4GKJF8Fpr0qzJLbgDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6901b9a141.mp4?token=nFwdNSy6qQBEbi6_Z8ySVK_LvkEvFFheIBg54AO2Sh56fh-ZO9CDcD7JCR8wgDBkc-Q0e7vRYiHCbV8QIcBlY1Htvns3SDMGmG9irKH182lEqbWcanjs14fkwnSDI1udjKgJaO9DKN7NLTWHNKoycMbbxSBI9P3V0BoAdPtj9ScdeqVnZNQXli-RUXgFPilRweM1oi4TZvgvImX7BH0aFHe_o1-qeoWoKTRP0Ue0eTpPwjWl5GsGcO2vP9lOxsuG7mf0Sa8h0QWKN20z_5DDbF5Chc7vq5rgdeE5ksLbX5rMO4f2BAe-dy8EbT5I2V68SUF4GKJF8Fpr0qzJLbgDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
رئيس مجلس النواب الأمريكي: الإيرانيون ليسوا شركاء موثوقين في المفاوضات. بالطبع، إنهم يكذبون كل يوم. يجلسون على المائدة، ويخبرونكم شيئًا، ثم يفعلون عكسه. بالنسبة لبعضهم، هذا جزء من دينهم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90406" target="_blank">📅 22:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a73e5d62.mp4?token=SwuY6rPy3ElHS8R2--vVFn4zh5q6m2hLL1fCFzHXKEPSDO_-W-XFHrimNF1Npn_nbI82VCI4tFeM1Mfy0jOeLGIlcGUJOS42x6ETiUkreLALygZLzM9djW4_VXV5WzCM7SSGPjNNvn5-Ot95CxHHe6u_q43UGaPgaxnKMPP4J5x8eYIRMZWhBdTupTwmtbeeyhSBCfjjyCFw_zgDXddG28C1v63hHWEJo2kBW3S1neeSydH89nlXBZR37oMWHjQMFKSYGf2PHBJq5R-_Xhpkh2zmZCRYokhZtgLlTbHEkvqwfKLsqsL2K89GKS4qds-ZuOsOAh-MowQwiV1Plq3xCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a73e5d62.mp4?token=SwuY6rPy3ElHS8R2--vVFn4zh5q6m2hLL1fCFzHXKEPSDO_-W-XFHrimNF1Npn_nbI82VCI4tFeM1Mfy0jOeLGIlcGUJOS42x6ETiUkreLALygZLzM9djW4_VXV5WzCM7SSGPjNNvn5-Ot95CxHHe6u_q43UGaPgaxnKMPP4J5x8eYIRMZWhBdTupTwmtbeeyhSBCfjjyCFw_zgDXddG28C1v63hHWEJo2kBW3S1neeSydH89nlXBZR37oMWHjQMFKSYGf2PHBJq5R-_Xhpkh2zmZCRYokhZtgLlTbHEkvqwfKLsqsL2K89GKS4qds-ZuOsOAh-MowQwiV1Plq3xCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
رئيس مجلس النواب الأمريكي
: الإيرانيون ليسوا شركاء موثوقين في المفاوضات. بالطبع، إنهم يكذبون كل يوم. يجلسون على المائدة، ويخبرونكم شيئًا، ثم يفعلون عكسه.
بالنسبة لبعضهم، هذا جزء من دينهم.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90405" target="_blank">📅 22:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
حرب خفية امام أبواب مصطفى سند   الشركات الأمريكية والصينية والبريطانية تتصارع فيما بينها امام بوابة وزارة الاتصالات العراقية للحصول على فرص عمل..</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90404" target="_blank">📅 22:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a124353a22.mp4?token=D62sT_tIdKw0ImUryP0NAse8IPQK8eJaotQ5KCtIORs2tsKK8pk1KOvr8SV1p0t0PV6-YR8qQzElXDQeMVqS95EjDofs6-zuJekdRogQ5VIzvefdCR8X60eb4fgfvj9XyvW9XfMUJBRbl4HFMEp9h3qxAjlHTAJLeQS0dKixx59do6cIXzv0aslWtzr347NG423BFHCNlAG3kO7b7Y8DWUk5iuvnWSjjqECZRckK3udjABgi5xVDIbYmkA_oEloXpkdmkJm1jBZMaw-ATAEeV5FF99sEdQBYVcFwUPi6HR0e6YJEotuJYv1y-Y6c-fyKEuFM8b-t6N7t1nQsRQjVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a124353a22.mp4?token=D62sT_tIdKw0ImUryP0NAse8IPQK8eJaotQ5KCtIORs2tsKK8pk1KOvr8SV1p0t0PV6-YR8qQzElXDQeMVqS95EjDofs6-zuJekdRogQ5VIzvefdCR8X60eb4fgfvj9XyvW9XfMUJBRbl4HFMEp9h3qxAjlHTAJLeQS0dKixx59do6cIXzv0aslWtzr347NG423BFHCNlAG3kO7b7Y8DWUk5iuvnWSjjqECZRckK3udjABgi5xVDIbYmkA_oEloXpkdmkJm1jBZMaw-ATAEeV5FF99sEdQBYVcFwUPi6HR0e6YJEotuJYv1y-Y6c-fyKEuFM8b-t6N7t1nQsRQjVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
احتجاجات في البحرين مطالبين بالافراج عن معتقلين الشيعة الذي تم اخفائهم قسرا من قبل النظام البحريني.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90403" target="_blank">📅 22:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات المليشيات الموالية للسعودية بالصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90402" target="_blank">📅 21:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأميركية:
مجهزون جيدا ومستعدون لأي طارئ.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90401" target="_blank">📅 21:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZktUS5FzfYQP3F0hwu0r4BvIHfc1uhMH63fhwjsdap2AiiBACYH0vN1ZWxqh0mmgSR7ttpWrjo8KwzY3p7e4MDTkmvIqDWvlbOaGFuEopvPc0x0WFd5DE0R3KC6ltZtUyYhnR1P5NWQUzWFfztaOs9HhSZsl_2iTCcwMFIetOFnHEo9rQ8cTYiuvKE1ZNqabzZ5y42JflCweL98QstgHCLKKvliF1R30XxN4NEKSUiGoNQH8_EYGaDIg9KJwCyik4Q55Uc8fkRZJDH-pCRgt8HELvoHkCRvdYQMK5g3dHl0SrbHS7Q1EXTyqFDdCEArfQ6GmpccdIUlD04qPxJe_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عنيف في محافظة حماة السورية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90399" target="_blank">📅 21:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8zdlopWh-kBk4kYJznYujVRR3zm6mMGRH_uUivEsUjTOxo-tes416bQVR-XNAUFditLKxZ6rFCwDbOyWr1jMlzhZIeIztGOPkn1tgDUmxHRmUHsluZb0L1IoVAT2NNBfRrrZmdTyT8g0m3dTakph3o-ab-u4cvD1O8S0xKe6n_csoXcrYL2J56yh1Pi043V6XIzOkkaAQjHFnfMa01uhPpmmOTdxIRlfr9WPjXUnH85IDEVPLE2Km4fx1VXahcaG5DQhYwYw9or9b7LpC4nYyLO86wNd5Udt3VCl_R_4jIBMhfOPj_DIqNYPCYe9cmzFYs68tPM8eDKwEvlZlI6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
حرب خفية امام أبواب مصطفى سند
الشركات الأمريكية والصينية والبريطانية تتصارع فيما بينها امام بوابة وزارة الاتصالات العراقية للحصول على فرص عمل..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90398" target="_blank">📅 21:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
أفادت هيئة الإذاعة البريطانية (بي بي سي) يوم الأحد أنه تم تهريب أحد موظفي السفارة الأمريكية من المملكة المتحدة في أغسطس/آب الماضي بعد مزاعم بحيازته صوراً غير لائقة لأطفال .</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90397" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طيران العدو السعودي يستهدف سوق الخميس بمديرية خب الشعف بغارتين</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90396" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUXx587vV_FHoeGfJMXlmr-JGgJ8ziLOEvK46P1mMeTmQz9MTy6qpZuuGghqPCyTJzq0Yl_V1G9W91tvy7fM6mA-A6mM3WXLP76-gncl4wTJbuG0cm-TVxltItlEBU_953BwlSHLksI93hqfjawpSfyspppVuiRY2Z_Q9zLwufZgk8_0k3tpEcUV9FMAsbq-_Rsba36wVnt8JNxLV6COuJyMF7rrMffSDOVvkVe6CsUEeahewAl6CbrQ6zH1UXpq4bZvG9fs7YF5vs3hQQwkIQlOsijNLFZx0V3PI5ALHCNK-rVnZP6Bi-_-x9FTwLsiFH3g1z8rUo7denVINFHuJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtHLeX2oyh-JYGY_20iKGpNfE6cvSh3Qfpr7G81mWIYNGrW9a-1O1KE0FkkZUQufPng9Vi4-vKoviaVqgtLoh5-qSjArB2Cfw-IWGioRE0iWMrTlNQAh_GTZR7WLJMetfX9MAVfoIMh0a1DUHqslOmyUD23gTidY_-BKyOYANpypDZaxr3lkRINShlZpQ-lQRCUgUvFZdjCTe0kxLk0P9ZJQ044uKJJuDs8ionnGyqzSGDHlPRB-VN13848WzrUf705igsY8zM569037kfy0q0aVJqPxHwkf9G6ANO_X5l6yIWx0wrnnWvlPmv7p9s5m0ANoNJtYgRjQyQYOrkzLqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسالة أهل الثبات لقائد كتائب حزب الله، الحاج أبو حسين الحميداوي "ايده الله ونصره"</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90394" target="_blank">📅 20:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=hdcQm2nCIfoIvhcmLwO-_tmLicrHfqbXcEYyrvoBiMblqXy6IDmOzmT9N6tqvxVOsVtjpGfMvi1bVGwTkHkdsKy0DV26RlfreK8vZv6FAMreQ5wct6CpVnULITxlyLDlT-IdvOCX6rQR-o72UxoJJziLMp2bNvc1n3muQY1_s2yftqJKc4Myg6tqVWeMparr7tRpOeVsBQDynV-oYpZ9XMEbtqVDDqgeyA2nKtX_77qBYY_26N6bzyRnSOcOmw5LukOoe0VY2yLh2UGh8UsoIvSJlkucGG5KpFnwm6QzJPRgbkcTFSEOnUGG_UoG4QLmCJRjtU89j-2B0v05jrAH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=hdcQm2nCIfoIvhcmLwO-_tmLicrHfqbXcEYyrvoBiMblqXy6IDmOzmT9N6tqvxVOsVtjpGfMvi1bVGwTkHkdsKy0DV26RlfreK8vZv6FAMreQ5wct6CpVnULITxlyLDlT-IdvOCX6rQR-o72UxoJJziLMp2bNvc1n3muQY1_s2yftqJKc4Myg6tqVWeMparr7tRpOeVsBQDynV-oYpZ9XMEbtqVDDqgeyA2nKtX_77qBYY_26N6bzyRnSOcOmw5LukOoe0VY2yLh2UGh8UsoIvSJlkucGG5KpFnwm6QzJPRgbkcTFSEOnUGG_UoG4QLmCJRjtU89j-2B0v05jrAH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسجيل حالات اختناق بين عدد من موظفي معمل الأسمدة الجنوبية في خور الزبير جنوب البصرة نتيجة تسرب غاز الأمونيا داخل مصنع الشركة ونقل المصابين الى المستشفى لتلقي العلاج مع اخلاء الموظفين من موقع العمل.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90393" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
