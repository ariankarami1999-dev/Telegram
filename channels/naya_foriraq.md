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
<img src="https://cdn4.telesco.pe/file/Uk0Y3rG8YZBBvgmbHCtuBvNd6gaEUfBwHWghSQkZcP2P9Dy2Aa9O0sLQYvgzAZTn7z34BizWzr-fcvZM1T6uLbPzHAqHRgAMxHWENrGqGPlUpms3DpF4wWrql7YZNxJLd3EwIW3SuJC62HlLwTkd03QBXFMznjKM7IeHTBysOUtozfBbDLptU5wSTQ0yXrptt8NU3Ojcyfd3mX5RLASmiAp8_CwmDvBNpspWb9V_vrzO-RjtARCzTCEJurEoXZFzzDpaZUHPStgX152EY2NXjyabKQB0SGzS3WuTjkphfngkEGvD5EmvaX3gYFa7y_v18vLSb0Yha8eEpLGAtW4HWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-89484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇷🇺
🇺🇦
نيويورك تايمز:
نظام المشتريات العسكرية الأوكراني عانى من عمليات احتيال وهدر وسوء إدارة جسيمة خلال الحرب. وتُظهر عمليات تدقيق سرية أن حوالي 1.2 مليار دولار قد ضاعت في عام 2024 وحده نتيجةً للمدفوعات الزائدة، وفشل العقود، وضعف الرقابة.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/naya_foriraq/89484" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">القوات المسلحة اليمنية تعلن إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية صباح اليوم في أجواء شمالي غرب مقبنة بمحافظة تعز</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/naya_foriraq/89483" target="_blank">📅 18:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXbDTfESoapN9ELVZJmN_Sob5OvJUPobP_MMMCuryvzyLEVJY_dkIy34W5K7waiwKYxZsCg9pQOZlkPwQg9BYl-OEj7upV78vDGYX_scOU9yW67Fb9HQ4zG9DOs9zpz4YiiYHnAFX2dqHB6bak5jzx3-HzJ7KHidH_OGV5B-sGoMAKubyhpdjbPWxzmf-f2JQ1ymfzuI1IFrZDWthNxX8FH4rtkSZWO4bx1TGt0u5clphtq_eCryG30LRUsDWtcRInZNPLnRboXHqU7VuMA481wDfk6Sx1BxRl5r7IOEx3wvicpCcKXla4S_-bU-HOmDjfGKqTFem7UaXfpdo_xr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف ساخرا:
استعدوا للإقلاع. الاستعدادات قبل الانطلاق:
ارتفاع أسعار الديزل إلى أعلى مستوى لها: بيعها على المكشوف
أكبر دائنيك يتخلى عنك: حظاً موفقاً مع تدخل ين++
النرويج تخفض 80 مليار دولار: فلنغير اسم النرويج إلى أمريكاواي
انخفاض التوظيف: نسبة الدين إلى الخدمة مع الحرب الإسرائيلية، حسب توجيهات من يحركونك
أوه. مخطط النقاط الخاص بالاحتياطي الفيدرالي يومض باللون الأحمر
😁</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/89482" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📰
رويترز:
تعتزم الولايات المتحدة سحب أنظمة الدفاع الجوي من كردستان العراق بحلول نهاية سبتمبر، وقد تنقلها إلى الأردن والمملكة المتحدة وقبرص.</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/89481" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
البنتاغون يرفض صرف تعويضات للجنود الذين لقوا حتفهم في الصراع مع ايران ويزعم انها عملية وليس حرب لأن الكونغرس لم يعلن الحرب رسميًا.</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/89480" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNbraj5zcCQpCAzkaDY9zdCzDsEDJwLZe51vAn6EiwN-eBPEP2VhUAQ_lo7lPEoavkFdDYACEJ7ICv6sahyCkK92j3ue0CS9uTBxAcO2LQbzkn3K4pTqniQfdWzy3jjV0ZAvI0yB54aASNKoG3odTEbeichmzyKtX3bNEKjlVpfQeqLgByFfiSUrhKcoZlgnTjMTRasq1FNkujoQKdEA9EXGF5TMykXLOdS5Vf_KGR-9N0ZAWqh7GSQvaBUPCflDOVDzqWwVUt-L-C17tinNU4FrIZOmc1Id-xx93fY00xjf47oasgPAY18u9IoOywbeHU19N6FY2m15LSG21o2byQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
حريق مجهول يندلع في محطة رأس لفان القطرية.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/89479" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#متداول
🇮🇶
بعد فضيحة تسريب أسئلة الرياضيات من وزارة التربية العراقية التي تعاقب على إدارتها وزراء من حزب تقدم.. تصاعد موجة الغضب الشعبي بين الطلبة وذويهم وسط مطالبات باتخاذ إجراءات حازمة وسريعة وفتح تحقيق شامل لكشف المتورطين ومحاسبتهم بما يضمن العدالة ويحفظ نزاهة الامتحانات وحقوق الطلبة.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/89478" target="_blank">📅 17:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AILktC5DJ9DYyUifPgjNfydJoeW09NyDyUQ_eIPK4LRNjuGIRFJc2motz_lMUrgZmyjhIZtbfWDUzsqEYCdebhQziSk2fuDEkS2qppN0VNPvHSxDRRya2sFPvero7sHb0Py6UGINQXQYfw_8PvNKPIo9Kok2M4QqKOS2ivj_cgmwEwFIETrWsq8qJqD_mesxbQO2tHOIXlEEycagDXLySL9CqiVeoAFfRz_5-gO1nBlUjQEB0eB8H-ctFwxV4y2jlp6FJAU04QnNSIJeCPDP7zWZ1xeomoZ_tk4MKz91EaHwrSMGAtKlHzb9emeDOi6AjEiQwiqQlMbwbkA1T_g5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR_5eR9VkfsxwVBe9QS-uEzP6MNscDzZXlxcJ9CPHqhEpIUaIPakpnPgfPwxy5c2xLkxPspibIr3fyyG90qPIQqoaVC2LBXo08p2SdWnDg2bouT2SMkYj82ZHRqkPIP91XdTkvZTwwjLGNF1fGfJf0x0Bzlw109B0Yb529Lz3ae3BNrMsc8jIJufEnbnjrXCL9rGpVLjBLSVltryPWTuatAW5P-jXGWrzhhbPMd1L-fBymzHaDtk2ri0ggiqRxzmV6alXQSaR4jNSS3-7vnrXGeMZB-54-CTTwoLECXKkdAwEapFnlEvDPq9tHtB9fy_-JWO9hzX7_2QnWiqsOArUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
محافظة بابل وعدد من المحافظات العراقية تبدأ مراسم تشييع عدد من شهداء الفتوى المباركة بعد مرور 12 عاماً على استشهادهم إثر العثور على رفاتهم قبل أيام في محافظة الأنبار.</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/89476" target="_blank">📅 17:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89475">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">العدو السعودي يستهدف بقذائف المدفعية مديرية شدا الحدودية في اليمن</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/89475" target="_blank">📅 17:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89474">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ضربة صاروخية دقيقة استهدفت اجتماع عدد من قيادات التحشيدات السعودية بصاروخ باليستي محلي الصنع.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/89474" target="_blank">📅 16:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محافظ البنك المركزي العراقي:
لا عقوبات من جهات دولية على القطاع المصرفي بعد اليوم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/89469" target="_blank">📅 15:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGBqzIxaQGZ-vF6OHYDZEMnVOLPIM6VcFk6XnSHB3NpcY3RH_Ghh8pwNedazYAA6KS_EY_TI-nTw3r05rI3WYAnhy7xcFMQTImyxF2NcckLKvxiuwnqRsjVEcOqgIFNcAgjO0Df8nvR970r1DhzPRpzxwM4feqFiWFkCNBkh9qC2dwT6WXfdJOWBOAR7c1l3qC40bLKJMmgyYGyNgoII1nnjaRWvxV8QnFeqps3mXATIytq_ci-FSgrNo9vYvSy-7sXi2K_nfQKj0wjWxQk0LhYM6gwowGyJL4yyKTPRauDM0KtqOaVRQNTSedNF65leQfqXx2-PrEfHtiT-EPCjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو الاء الولائي مغردا حول تنظيم السلاح: ‏تنظيم السلاح مقابل السيادة الكاملة والشاملة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/89468" target="_blank">📅 15:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اندلاع حريق في منزل وزير التربية العراقي بمنطقة السيدية غرب بغداد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89467" target="_blank">📅 15:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdpms-DbPlVnCqYE_-gOHfLA-dnOiRIEUG3-ssudHp7aKQ7zIqQNNErJgYnoB95mJcigwn9z8Kyz5k40bvGbtXrGQtvMOo5ykzSXdcPTtB_m3Zl7bcnZnoSg1tACGTTvUjU7HdSaFkN03vrhji66ZGL1LxVSlqQDWcyGDoKGqqOjk-UWNbr9B32Ulz-Q1gNtgy-Pnm_0XRk-kdrg2yVS0jJpK82qku2Hd9PhiJ5-jbxypt_e4MO129yIDMEHlWMWksjGiY1AEknOLJOdg76DCMQHH3_DOS5B0S6vtLFq9wytV5G12QeLiyLtXcDq0R753ppFW538l0Hu-RuSi5eNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
🇮🇶
هل اصبح معرض بغداد الدولي اداة لترويج كتب تنظيم القاعدة الارهابي ؟
جانب من كتب هادي العبد الله عضو مؤسسة سحاب الإعلامية التابعة للقاعدة وكتب الجولاني وكتب ثورة سوريا التي تضم الإيغور والشيشان وتنظيم النصرة تباع في قلب معرض بغداد الدولي للكتاب !!!
المطرب سيف نبيل تم منعه من دخول سوريا بسبب مقطع مادح الحشد !</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89466" target="_blank">📅 15:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73977c8d.mp4?token=n-navNCRMEDtfNknGY17TaL8G53oHSx04FOftKTqiuw8g1L0bXMWBvRQEaL5ce5DZOrd7dlK3F2ZFGIt829Wa6y16papVPqXM90MfXX0FjbH82KLa6qXM5XbXHvZHe55Yzfy1b_FpeiP897loeQWrbW8Sr7Nwaz01gEmF2vd8ih4i4P14lGJgEmMK0lqIcfHbgL1WDJV3zXFbAkfgGNAM4f_B_iFBSWwfrK3g2A4f1Sr8jMqEI7z5EhfgNr89jEZox0-ERpv9dp7N3ZMfg29lsaQd4q6Ri-R0KWWGXcYYjJtInb8zRroK597N543IAmmlbE4r9tDphVLxOU2ikBObw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73977c8d.mp4?token=n-navNCRMEDtfNknGY17TaL8G53oHSx04FOftKTqiuw8g1L0bXMWBvRQEaL5ce5DZOrd7dlK3F2ZFGIt829Wa6y16papVPqXM90MfXX0FjbH82KLa6qXM5XbXHvZHe55Yzfy1b_FpeiP897loeQWrbW8Sr7Nwaz01gEmF2vd8ih4i4P14lGJgEmMK0lqIcfHbgL1WDJV3zXFbAkfgGNAM4f_B_iFBSWwfrK3g2A4f1Sr8jMqEI7z5EhfgNr89jEZox0-ERpv9dp7N3ZMfg29lsaQd4q6Ri-R0KWWGXcYYjJtInb8zRroK597N543IAmmlbE4r9tDphVLxOU2ikBObw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وصل كل من المبعوثين الأمريكيين جاريد كوشنر وستيف ويتكوف إلى كييف.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/89465" target="_blank">📅 14:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشهدا لعملية نوعية استهدفت اجتماعا لعدد من قيادات التحشيدات السعودية عند الرابعة عصرا اليوم.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89464" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698ebc0493.mp4?token=dyaAMbL5KnszP5i5T4FMLbueuklMJKvSFKAC_v2kahGfVWEspey6BBfgP2Uz17f8NITXOwPOumMPIEi1U4f7SnswnyVtY9k4mYdFBKjK_WpDHQakhVkALfX6qALyOAPIsrPY-rc5XQ_8Dahmb6ptdE5JQKHd2hjaAUzbLAxYrg9-bK2QH80lU-KTq8immnbzuW0t0fT9slkDaSvM05oCnzIy1hbbNFnh_yBnNew6t1ht1nm_8pyt64oQN-sAOTU0J0TzyZyOtZUn6DYMUV_B0i09uXXbdzpodrGnld1LdRS_XPmbw21UgtI91ifWEpxm-5CuulUaLU85K5menaehSDymg9D28L354FKjlX0-8Ym31cztYD2tKU-xnHcNmUzbZZWm6t5iNFQekxFM7cfzGkeSg-DNnLMebBZXKjaW0TvcTVDWFgK81PZTTnf48icyLAASkipGSDVQIJfsGScuLYTg0rxO1aK3mBN6T0wI--fiQorKTupZtt3LIKOUS6fPSOc5edBvKMqxQJ_Rdz6WzQQBnNTR2M24fISe7jNU37fOLMlHzVWxmVmE569IJl5dyq-6Fnqg5PCed9wpZ2qO7n64dBBUjuavxIPDaZs185pGTrbu8j083XCEV7VSCzB6oM1X8cc41QA_87JQXGoa3omFtMKaiDHwg29X_FZM-Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698ebc0493.mp4?token=dyaAMbL5KnszP5i5T4FMLbueuklMJKvSFKAC_v2kahGfVWEspey6BBfgP2Uz17f8NITXOwPOumMPIEi1U4f7SnswnyVtY9k4mYdFBKjK_WpDHQakhVkALfX6qALyOAPIsrPY-rc5XQ_8Dahmb6ptdE5JQKHd2hjaAUzbLAxYrg9-bK2QH80lU-KTq8immnbzuW0t0fT9slkDaSvM05oCnzIy1hbbNFnh_yBnNew6t1ht1nm_8pyt64oQN-sAOTU0J0TzyZyOtZUn6DYMUV_B0i09uXXbdzpodrGnld1LdRS_XPmbw21UgtI91ifWEpxm-5CuulUaLU85K5menaehSDymg9D28L354FKjlX0-8Ym31cztYD2tKU-xnHcNmUzbZZWm6t5iNFQekxFM7cfzGkeSg-DNnLMebBZXKjaW0TvcTVDWFgK81PZTTnf48icyLAASkipGSDVQIJfsGScuLYTg0rxO1aK3mBN6T0wI--fiQorKTupZtt3LIKOUS6fPSOc5edBvKMqxQJ_Rdz6WzQQBnNTR2M24fISe7jNU37fOLMlHzVWxmVmE569IJl5dyq-6Fnqg5PCed9wpZ2qO7n64dBBUjuavxIPDaZs185pGTrbu8j083XCEV7VSCzB6oM1X8cc41QA_87JQXGoa3omFtMKaiDHwg29X_FZM-Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
مشاهد مرئية لتوغل قوات الاحتلال الإسرائيلي في محافظة درعا السورية ونصب نقطة عسكرية في اماكن تواجدهم.
عوي ولاك</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89463" target="_blank">📅 13:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfjd8gAKZ5KHHvWvgs7RllLx3hP-MeApKzsUzupCby9NvkD2CymYvSznPPSEFOiVwZxN06paAQzMV3QGEZma8d5OXTlRxLOoFNaUUzraUROs0HuOSSN25dEpyzlbBfFIHwBsYwsB09_zWbsyovBBUG40VYYsf7n1CLeH-4BVxJ21a0JPxDueFN_WO1vucAwJj6ERcNsukC0zqlx5bEdWjjRG6UoNwdZWd0XpNB5QDolw_JkvdJp2x5iy0en-uIVGgLVnPYNrsjmaJ97-syWdGEAN0ST4kDab1mCfPjEwQW42n2rnAdIDfrQ6EALtUf3Hnh2_PX2CTkayqZ0t5YwM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇷🇺
وصول مبعوثي ترمب كوشنر وويتكوف إلى موسكو.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89462" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
نييورك تايمز:
‏بلغ متوسط ​​تدفقات النفط عبر مضيق هرمز 6.7 مليون برميل يومياً في الأيام السبعة المنتهية يوم الخميس، أي أقل بنسبة 60% تقريباً من مستويات ما قبل الحرب</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/89461" target="_blank">📅 13:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjunLENrmLEZL40PwlEKgjhLPrv9yFvm5UVKsaqicAOqmHOg-HbvxT8CHr4wauhN3vdaPjBwpL822Kb3RUVLyEe9H2_z7MiC-SCEBbb1Q72MUD0o-d-URChb5ARe-AuAeYTICRDLOuCqPoG8D8HoVH1PtYpmVuarL_OjRokKtqpX4hnsuJBjrkAs0ARLgwlYxvezh-tXQY0AlYqaX8-1HE7EKAoxRUFsaCgQthDlTfksf0NIt4zlvUZZYkVbRw_m-SNrlViZeKeJ1fLD1zvDugPH_i_BiUMsQepojwUafge-N-FUZDZPti1uqREnRZJVMXCU5Txl4pHtyR2ZKE7kPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQ1s7mGEXKkVphcKCWA8LzbCUTMsGL-nxa6MjHvSCa_8vqDABQW4kuhqK2vc2oG02U8ednMZOY0fbjeEYcRwG69lsR1enG0TP-7afEpZN3scstGu2ANFK-P3F5K8qIghn2dvYDIbRnJNNm2-RRsctK6317bGCHacW8KdtszeCmwWN4iLbCSYxj1rc0PVbBl8j396aoYuyk79aTlOATCatseUwz4YG8CtoskXjBMwVyBKdglRZdTWr_67WLWKwwbLehomSTaBjznGse__G4eT8nhrLXuaGzsI_C5bXcAWlWmkVzhH2KpoN7n5aIKTa-Av8nKxHVSzs0RBunuTMf8f_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwzH222MOk7dxpzZCZyR_5X0Qfv6vJkl81DYS32giWrRPFFVYznH30IVGvGOEBjjweq1GLTVz-9x3_m6eMPx22eRWDMkSmToKI9OF-xxHGO9F2NYdNReaBxvVduYfrGrT273l3YBIgG55iihoZq2ehR1C2JJ9FpPZ2zRSVv0tIhsb9p7O4n7eDUXk7NsDIVmxHcpWNDd8U2PVKM9cAwkhojIK6ppr2QvqeSRpjgLgsMnw176_221tPi9sp718XsouIvKDy4P3plgq2xN-gUVCU6CV7bYIvm2pXBYxWKC5fhX3-yoAPbPs-fhzRKpsMPYzzbZPtoMUCm_LYFia7tMUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
في تصرف شديد العنصرية ويهدد السلم المجتمعي
🇮🇶
بدأت بلدية محافظة أربيل بإزالة لوحات المحال التجارية المكتوبة بالعربية وإلزام أصحابها بإضافة اللغة الكوردية إلى اللوحات بدلا من اللغة العربية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/89458" target="_blank">📅 13:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
شاب من الجنسية الكينية يحتج برفقة مجموعة من المهاجرين الأجانب أمام أحد المصارف الأهلية في العاصمة العراقية بغداد احتجاجاً على عدم السماح له بسحب أمواله المودعة لدى المصرف وإرسالها إلى والدته المريضة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89457" target="_blank">📅 12:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96b93cf3.mp4?token=J7xizgsW6WVFEjL9Kzko_d0EEDrAXltTt-ba7LB6Qt3ENtpHwMc1maRChyY2-oXDCDP3HFpvfqKCzt0OqIo4FPBVQl70jAIfxM3yMqdXgMUEEpFLd1C5_G0oBSUMUuglAbqEP5p7uWkql8cOCJNmdzilKjA3qROmakXDhmjj2PQj8xmyfw9I7bMrPUMEcXJxrxRcGTPiSzElGoPKrqTNh2jwKvteEZVsO-TrajDB7INe71Ldho_PGzautfxzVDn45jdcqCenyPJAD-fZIjlhgGHdcGBQ-_maiIy06nI3dZdjHNDrkbaFP8EtgrFPW2bhxDupTtQrk1ChntYT6VIW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96b93cf3.mp4?token=J7xizgsW6WVFEjL9Kzko_d0EEDrAXltTt-ba7LB6Qt3ENtpHwMc1maRChyY2-oXDCDP3HFpvfqKCzt0OqIo4FPBVQl70jAIfxM3yMqdXgMUEEpFLd1C5_G0oBSUMUuglAbqEP5p7uWkql8cOCJNmdzilKjA3qROmakXDhmjj2PQj8xmyfw9I7bMrPUMEcXJxrxRcGTPiSzElGoPKrqTNh2jwKvteEZVsO-TrajDB7INe71Ldho_PGzautfxzVDn45jdcqCenyPJAD-fZIjlhgGHdcGBQ-_maiIy06nI3dZdjHNDrkbaFP8EtgrFPW2bhxDupTtQrk1ChntYT6VIW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف
: الضربات القوية التي وجهتها القوات العسكرية الإيرانية إلى القواعد الأمريكية وضعت قادة هذا البلد في وضع يائس.
رئيس البرلمان في كلمته قبل بداية جلسة علنية للبرلمان:
لقد انتهى عصر الردود المتناسبة.
كما أننا هزمنا الولايات المتحدة في المجال العسكري والدبلوماسي، وبجهود شاملة من جميع أركان الدولة وصمود لا مثيل له من قبل الشعب، سنهزم الولايات المتحدة أيضًا في الحرب الاقتصادية.
توصية القائد الأعلى للثورة بالتحلي بحذر شديد وتجنب إظهار الضعف عن أنفسنا وعن النظام هي تعليمات استراتيجية.
الأمريكيون بالتأكيد أدركوا أن عصر "الردود المتكافئة" قد انتهى.
أي انتهاك للمصالح والأمن الإيراني سيقابل برد "أسرع وأثقل وأكثر إيلامًا".
﻿</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/89456" target="_blank">📅 12:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
اندلاع حريق داخل مستشفى ابن الهيثم وسط العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89455" target="_blank">📅 09:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Dp-veWR9F0bsjUKsnbT-6CqSHI8QfnHPAELKqcx6pOAMJ_mGLu33o8QUDlr1JUlyzXcjt9o323xI2na8rzW7f0DpYMTpW13IsECxEL7bZoqqNnTxGzQgaozVw0pz2obMuaMkrGEbecZ_Ryn5bKvoRZichdz5Mm9sQ9vvxdiRu70LCHdvf3W64QV5e-4lBvZepbL-pVVL7tXGKjB9dHe_tAB9We3l_3i_Pgq_bI7To-fVWRZzAknac-xwauokdpUKIdIXzycOdagn6rjrSA5t3RSFDgWF25ehlUjIv7MS2nVObMpduPFTaWYyNKz4tofR57CmRpf6_6nAYMTHjMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد اعتقال عدنان الجميلي وحسين طالب، وكيل وزير النفط ومدير التجهيزات النفطية في وزارة النفط العراقية،
لا تزال أزمة تجهيز الوقود تلقي بظلالها على المواطن العراقي، وسط أزمات متكررة ومتفاوتة في توفير المشتقات النفطية.
ولليوم الخامس على التوالي، تشهد أغلب محطات التزود بالوقود ازدحامات طويلة، دفعت المواطنين إلى الانتظار بمعدلات تتراوح بين 20 و50 دقيقة للحصول على الوقود.
وفي الوقت الذي يثمّن فيه المواطن الحملات الرامية إلى مكافحة الفساد،
ما الفائدة التي يلمسها المواطن على مستوى الخدمات؟
المواطن لا يريد فقط محاسبة الفاسدين، بل يريد أن يرى أثر الإصلاح في حياته اليومية؛ وقودًا متوفرًا، ومحطات بلا طوابير، وخدمات توازي ثروة بلدٍ نفطي بحجم العراق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89454" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-YGDNBz1GNo9gD53qmw-5ygbt35GNTS2VftgzRbsw0ZlNRzKlB-lP1hjNJHxxjiIN6bcQMmoNS-7elD5E5CveJtssxQ7fY4RVOgAnx0vBa7Y9R6E5I-CiLU-RUudXVzmxCMGZ2ASUQwVyrY-5imYYplZ06pbsmOgWfC2IduD1jS4K692MCEBw9SSVBLoSAlav7dg_Cq0SqLMRO_u36QuAa4agj5ywZpgS83PWHb85SGfnNhaLVwLIGGvl7toQzrePIt0S9BEvkqNk4ivMvR469wp7hkua1YyQC2mq7mB3EGCav6cjkC_WEA3miCgMZhSejgQbpGrxuvFKjZvlhSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89453" target="_blank">📅 08:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
لأسباب مجهولة..
خروج عدد من محطات التحويل الرئيسية للكهرباء في الكويت عن الخدمة، وقد أدى ذلك إلى انقطاع التيار الكهربائي عن عدد من المناطق في محافظتي حولي ومبارك الكبير.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/89452" target="_blank">📅 07:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
مسلحون من حزب الله أطلقوا طائرتين مسيرتين مفخختين باتجاه قواتنا في المنطقة الحدودية؛ الجيش الإسرائيلي يرد الآن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89451" target="_blank">📅 06:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxN21JVNYXWSdbqgsz7O3ukJv4pdQ0XF7PlY_uoYk6xs0yOa3DgPpUOH0bEdhABDKFAzSipi0y_pZDdQCu01mgKkjnIQUs0bfwfoK3EunJErivXuLRctEKrq0ka3yGKA7jGvn0iGkbPcNxOJl0l78oIbHFX3V9iu-3fJk-omV2M6o0VY_YbPW4VOza_RfpJAsVBR8wLmCtCG9AhFXjA7jebIwclcKxuaRrjyYT6WOPdVNHTd6A5-vCmDTPLltNg8OQK_dT7IP3dJAjNFZsdRqmlLeIkDaq0OL1kd8cHNdmzKz33lv8cgGUk-IQvA3QepRK_T3iqcoHvvmXDPJTbpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الصهيوني يصدر إنذار عاجل بالإخلاء لسكان بلدة عربصاليم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89450" target="_blank">📅 06:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89449">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvYQwBJMGDkzrAafeW6CHK_UYvseIi3qT60jIy3KXvKLFYvBBuCkFSBQ2YVi1cM_tD_FnGfIZRUZ7J5O3c3RKScbxsVakaUjO5_b6L_ZawxGKivlSb8bez-qQhPowwYu-k1VrvEmZ5x7H_25wIT64xZixbBSRV9gZ4CszuJnLASUeR4-C1ikBQgUySynHmQKsWWH8pbh2SPY-eFwqwqj2-iHFLVLa9FxCXFpMdibdvwvvvmvIxfvXgxsYkFUlCz_U0g6acqZEXZQfPVjeK1NL4mRIo2NkvgCOwU8vNy2YGNB6DLuFBOspwJ-X61KPYfbYxwjK0hXvh89pgd9sUbTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية تستهدف محيط النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89449" target="_blank">📅 06:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89448">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
الحرس الثوري:
قامت القوة البحرية البطلة لحرس الثورة الإسلامية باستهداف زورق (مركبة مُدارة عن بعد) تابع للجيش الإرهابي الأمريكي، كان يهدف إلى دخول المنطقة المحمية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89448" target="_blank">📅 05:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89447">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
🇸🇦
قصف صاروخي عنيف للقوات اليمنية تطال مواقع مرتزقة السعودية في محافظة تعز.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89447" target="_blank">📅 04:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89446">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb10a23f4.mp4?token=vPJwF8FqhMmim-OvPmDpNp-B_s1OJZpACDl074Ihk1ddr8ThuGAZKCgoG_bSwF1LGkqkI7-zs_ubT8kvjddJsqwRt29FwHwIsaxTNdvMuHgSsSGX3rBWTPxoQDmedoxqEtxjARZA6wY2T5aCBB9DdncNPY5YQeAOPwnnSNQd1nOL0CjWoRoENDLYnOa3Nn7yUXP761sgZgGcznPjdtfLa00-CBoK2b7Zsvvo5vI_oZAJvqPmfuJ6Fcw9ezNV-V-BYe4t_LBgdaLcBWKYaxNP6G4tgsy9dW5HQYrDx1DqWImQb-BhDBQ-XbKgqmgfjxZfBg2ejfGJlPs1TxtLoM--cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb10a23f4.mp4?token=vPJwF8FqhMmim-OvPmDpNp-B_s1OJZpACDl074Ihk1ddr8ThuGAZKCgoG_bSwF1LGkqkI7-zs_ubT8kvjddJsqwRt29FwHwIsaxTNdvMuHgSsSGX3rBWTPxoQDmedoxqEtxjARZA6wY2T5aCBB9DdncNPY5YQeAOPwnnSNQd1nOL0CjWoRoENDLYnOa3Nn7yUXP761sgZgGcznPjdtfLa00-CBoK2b7Zsvvo5vI_oZAJvqPmfuJ6Fcw9ezNV-V-BYe4t_LBgdaLcBWKYaxNP6G4tgsy9dW5HQYrDx1DqWImQb-BhDBQ-XbKgqmgfjxZfBg2ejfGJlPs1TxtLoM--cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي ينشر مشاهد يزعم أنها لإستهداف وإغراق ناقلة نفط إيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89446" target="_blank">📅 04:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89445">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
الحرس الثوري:
شنّت القوات الجوية التابعة للحرس الثوري الإسلامي هجومًا بصواريخ باليستية متعددة على حاملة طائرات ومدمرة تابعتين للجيش الأمريكي المعتدي، الذي كان يضايق السفن الإيرانية ويشارك في الحصار البحري.
اضطرت هاتان السفينتان الحربيتان إلى مغادرة منطقة النزاع بعد تعرضهما لأضرار وخشية هجوم جديد.
اضطر العدو المعتدي، الذي دأب على إطلاق ادعاءات كاذبة في مرتفعات الجولان لسنوات، إلى الاعتراف رسميًا اليوم بتعرض سفينتين حربيتين تابعتين للبحرية الأمريكية لهجوم.
إن اعتراف القيادة المركزية الأمريكية (CENTCOM) بهذه العملية دليلٌ قاطع على الهزيمة الاستراتيجية للعدو، وبرهانٌ على القوة الهجومية للحرس الثوري الإسلامي.
يدافع الحرس الثوري الإسلامي، إلى جانب القوات المسلحة الأخرى للجمهورية الإسلامية الإيرانية، بحزمٍ وحزمٍ عن الأمة الإسلامية الإيرانية.
إن الحضور المجيد للأمة الإسلامية على الساحة، والقتال الدؤوب للمقاتلين الإسلاميين الأشداء، يحولان دون تحقيق العدو لأهدافه الشريرة.
إذا استمرت الأعمال العدائية والعدوانية، فعلى النظام الأمريكي أن يتوقع ردودًا قوية من القوات المسلحة للجمهورية الإسلامية الإيرانية. نحن أقوى من أي وقت مضى. النصر حليف الأمة الصامدة للجمهورية الإسلامية الإيرانية، والهزيمة والندم مصيرٌ محتوم للمعتدين.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/89445" target="_blank">📅 01:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89444">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
مصدر أمني لنايا:
دخول رتل عسكري أمريكي إلى بغداد قادماً من محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89444" target="_blank">📅 01:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89443">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
مشاهد مرئية لاستهدافات المباشرة للحرس الثوري للسفن المخالفة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/89443" target="_blank">📅 00:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89442">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=vdgyHUnNiOnFsqyov6NZPLEvbX0ESV60yCPm-7Hq6dSlTCA25z64n4-H82bUwrAwQUT99Rey0Yc65HuKVAOAkh4MN_54ntMWRIXWRJnkPkXi5ZRd4JN1Zp-ckOqR7NhaS0ABP9XgDi3FpT1BSNeOdT-wk5zC6bksJgZSpuRIZfDr-BwTda5r44VX6LT_kdeJKYpASarLyhnc-3wghgTWpJv67FW6FGGMPu3ffOt5wuIR01T4tqHwzo7zrTQ0szJqOKwuPTitZ-aY7yOv_eU8mYlP7hxg0i_jfDNFv9Ei-Dc_aRVWqT3CxwTrWW7Mvdg-UynUFD1FMHImByffxa8S9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=vdgyHUnNiOnFsqyov6NZPLEvbX0ESV60yCPm-7Hq6dSlTCA25z64n4-H82bUwrAwQUT99Rey0Yc65HuKVAOAkh4MN_54ntMWRIXWRJnkPkXi5ZRd4JN1Zp-ckOqR7NhaS0ABP9XgDi3FpT1BSNeOdT-wk5zC6bksJgZSpuRIZfDr-BwTda5r44VX6LT_kdeJKYpASarLyhnc-3wghgTWpJv67FW6FGGMPu3ffOt5wuIR01T4tqHwzo7zrTQ0szJqOKwuPTitZ-aY7yOv_eU8mYlP7hxg0i_jfDNFv9Ei-Dc_aRVWqT3CxwTrWW7Mvdg-UynUFD1FMHImByffxa8S9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
‏هل حدث شيء ما في محطة رأس لفان للغاز الطبيعي المسال في قطر؟ تُظهر صور الأقمار الصناعية اليوم ظاهرة غير طبيعية لا تبدو كغيوم. رُصدت طاقة حرارية قدرها 80 ميغاواط صباح اليوم على جهاز VIIRS، كما رصد القمر الصناعي Terra طاقة حرارية قدرها 120 ميغاواط قبل أربع ساعات.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/89442" target="_blank">📅 23:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh8eOcvOnrsozNS9OSctDrA4r9zVc862pj91tEh5UfY594tcDhwxn4WjSUo0ekgk9hCJa6lSkSrKJs3WvgHXHmqNEaMicsK_0UEt8wYGRc8ECUJmQuKnjDYpG_SopBmD-nz3nOysZ8m8GdeTro09NLYP5Qm-DTP-swSfS_aSS9jqM8QsOlW0Rk1w4Dlnc9muDr2GfrK7eFLffF8GNsdUZNqqi9QJfuJDBUSBB85YON8dHP6US9ti945c2uUoeyrTK8bRhHx9LbK2iQr00vn5mdJYuMxubFH68oAW6POe9v4Me3KNfQXuJM3TdoJRxVtD0iY30X2gmE5Rh8u9t6ji4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🔻
انتحار جندي احتياط إسرائيلي يبلغ من العمر 46 عامًا وله أطفال، أنهى حياته نتيجة لصدمة نفسية من الحرب مع حزب الله .</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89441" target="_blank">📅 23:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89440" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89439">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=o04xNlSF2uqKDikXjQ7F2Wdi3BTKHxHxBIChfZJn38j1jwhQCQSks_Ny7qrQoQt37kR9EFXMU8sYMK1lAhWWymZ_gr8KwWmRIL6dKEmRrfHE65wHYJ7AxOx9DxDtkaSwlhssIMrfLKLhGy3lc7CT_rEgB941xGKBympaW2eHkl776YUz02yVYpv8Wc9s5i9kcqJeC_4YhARjsufUZxBOhQ2isYRHC861zECy_at-ZYfPsxNEG_5QuONdDthuKCbhtRtrsmb2UYQVIW-taYUJa15lBgcSSIMlDx9xOF-SLtIORlxBSmemQFcjlYdOxNTsJK1CQNbVEo7NubmJzOvPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=o04xNlSF2uqKDikXjQ7F2Wdi3BTKHxHxBIChfZJn38j1jwhQCQSks_Ny7qrQoQt37kR9EFXMU8sYMK1lAhWWymZ_gr8KwWmRIL6dKEmRrfHE65wHYJ7AxOx9DxDtkaSwlhssIMrfLKLhGy3lc7CT_rEgB941xGKBympaW2eHkl776YUz02yVYpv8Wc9s5i9kcqJeC_4YhARjsufUZxBOhQ2isYRHC861zECy_at-ZYfPsxNEG_5QuONdDthuKCbhtRtrsmb2UYQVIW-taYUJa15lBgcSSIMlDx9xOF-SLtIORlxBSmemQFcjlYdOxNTsJK1CQNbVEo7NubmJzOvPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
القوات البحرية للحرس الثوري الإسلامي:
تحذير شديد اللهجة من قائد القوات البحرية للحرس الثوري الإيراني: لا تنخدعوا بأمريكا؛ أي تحرك مشبوه سيتم استهدافه.
ردًا على عدوان الجيش الأمريكي الإرهابي الذي هاجم ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية
القوات البحرية للحرس الثوري الإسلامي:
أيها الشعب الإيراني البطل المستقيم؛
هذا الصباح، قام الجيش الأمريكي الإرهابي العدواني، في عمل وحشي ويائس لإغلاق مضيق هرمز، بمهاجمة ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية، مما أدى إلى إلحاق أضرار بها.
استهدفت البحرية التابعة للحرس الثوري الإيراني، بعون الله وتوفيقه، وبدعمكم ومساندة الشعب البواسل، وامتثالاً لآية القرآن الكريم: "فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم»"، ثلاث ناقلات نفط في ممر مضيق هرمز غير المصرح به، وثلاث سفن تابعة للولايات المتحدة الأمريكية في مناطق أخرى.
وعقب هذا العمل، تُوجه البحرية التابعة للحرس الثوري الإيراني تحذيراً شديد اللهجة لجميع السفن الموجودة في الخليج الفارسي وبالقرب من مضيق هرمز: لا تنخدعوا بالجيش الأمريكي الإرهابي، وتجنبوا أي تحركات مشبوهة لعبور الممرات المائية غير المصرح بها، وإلا ستكونون هدفاً.
والنصر من عند الله العلي القدير الحكيم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89439" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BEkZR4Og5iCOW3hhfxe3Hwn_iLoFZAOMG6n__vqp7p0JEAF012h81DJzNgrujl29Jow8kpKEQhr8L0RMrKnXKyGFREjyneE5QJi4Ss36ppJoDfUgCs8ltWpFoX83iMD3xMRABQf3XNznmU4J41AJ5sEQO9hRgngp_bX_VMcPljrgUsFxThLzXKx4GDH8VqfUjxF_eddh1TTjK-QFK5ylR1r8vEy62OpRFX9YoQj-Zogs2NkDfnAUp9pj_ajwZsIU2VSsRAEGh6KEWSleQMomyN68aIvQ3_ldERXF9bgcPj6nNb0rR4jdlzpyl_HuPERYZ4-SQUIoy7RxssH3TNL15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BEkZR4Og5iCOW3hhfxe3Hwn_iLoFZAOMG6n__vqp7p0JEAF012h81DJzNgrujl29Jow8kpKEQhr8L0RMrKnXKyGFREjyneE5QJi4Ss36ppJoDfUgCs8ltWpFoX83iMD3xMRABQf3XNznmU4J41AJ5sEQO9hRgngp_bX_VMcPljrgUsFxThLzXKx4GDH8VqfUjxF_eddh1TTjK-QFK5ylR1r8vEy62OpRFX9YoQj-Zogs2NkDfnAUp9pj_ajwZsIU2VSsRAEGh6KEWSleQMomyN68aIvQ3_ldERXF9bgcPj6nNb0rR4jdlzpyl_HuPERYZ4-SQUIoy7RxssH3TNL15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو حول إيران:
إذا لم نتخذ إجراءات ضد إيران، لكانت إيران اليوم تمتلك قنابل نووية تهدف إلى تدميرنا.
الآن، سيحاولون مرة أخرى. إنهم يحاولون مرة أخرى، وسيحاولون مرة أخرى إعادة بناء التحالف الذي حطمنا.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89438" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الإسرائيلي يطلق قذائف صاروخية باتجاه حدود الجولان المحتل عقب رصد مجموعة من الشبان يُشتبه بمحاولتهم زرع عبوة ناسفة في المنطقة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89437" target="_blank">📅 22:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/89436" target="_blank">📅 21:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اصابة عدة سفن مخالفة في مضيق هرمز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89435" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
الانفجارات في جزيرة قشم ناتجة عن اطلاقات صاروخية نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89434" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
جيش العدو الإسرائيلي يستعد لتقليص قواته في جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89433" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89432" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89431" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=m6qvWkaZh3YSq3Vj6TdX1HFjDz06oEhl1IIefwmCd7eZfefrIvBuz1dlmasIWOBD75nlDg1d9k0P9ra2PrQgXUA5wK9NSs1oOumEl94s8BQF8c7dHs1LEDzBWN_TDx-egWMUnaU0ZJOKBee92OBaoghYf1w3g7bHuMNemz0wpXiIkf_mp3rSfExsbZPE_CdXXSIY7HS5dW5Gl5X-lcO35RjffbYaIMoV34l-m3glrhPqdAb_w4rvm-gzjbPcw4-iQ4Jxcqb29hC_TcXduicUDr8fKdofJAP4HiejS4eW79SIAD2BX2MUrt6VUSxepmKR6fjgwwg3U08PDlLInt0LPVYY5bjdGUKc-paFqSH3VO5PLAbA1yRTU6kZ1Pxjsh0_0HJUywd37rACtPiGjRn9BDOVvfcnyPa3R5RRxol-GzvvYf_KL_sRiyayrRkyn-B_FSwqFrE-r5z8jbyBtTnACNEDwS_FL59oGNaHJYNYH-tEtZ5gnBlcX_KYpE--E81SKpo2oug8v6H1xiWc7nn987Sl_7ypFx2kmlOEdBafZcVtkdkCdkvRoypOhEjdGYGHrXvKCQi0A45uXii3Is9r9-a9PLecBb0s66Ofet3vSLbMSp-9EbVfTuE4H24bQY8c3KSuZhf5yzdZEzB_bDhSinr5rRo2hy7qsVRC4k4UVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=m6qvWkaZh3YSq3Vj6TdX1HFjDz06oEhl1IIefwmCd7eZfefrIvBuz1dlmasIWOBD75nlDg1d9k0P9ra2PrQgXUA5wK9NSs1oOumEl94s8BQF8c7dHs1LEDzBWN_TDx-egWMUnaU0ZJOKBee92OBaoghYf1w3g7bHuMNemz0wpXiIkf_mp3rSfExsbZPE_CdXXSIY7HS5dW5Gl5X-lcO35RjffbYaIMoV34l-m3glrhPqdAb_w4rvm-gzjbPcw4-iQ4Jxcqb29hC_TcXduicUDr8fKdofJAP4HiejS4eW79SIAD2BX2MUrt6VUSxepmKR6fjgwwg3U08PDlLInt0LPVYY5bjdGUKc-paFqSH3VO5PLAbA1yRTU6kZ1Pxjsh0_0HJUywd37rACtPiGjRn9BDOVvfcnyPa3R5RRxol-GzvvYf_KL_sRiyayrRkyn-B_FSwqFrE-r5z8jbyBtTnACNEDwS_FL59oGNaHJYNYH-tEtZ5gnBlcX_KYpE--E81SKpo2oug8v6H1xiWc7nn987Sl_7ypFx2kmlOEdBafZcVtkdkCdkvRoypOhEjdGYGHrXvKCQi0A45uXii3Is9r9-a9PLecBb0s66Ofet3vSLbMSp-9EbVfTuE4H24bQY8c3KSuZhf5yzdZEzB_bDhSinr5rRo2hy7qsVRC4k4UVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين
: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89430" target="_blank">📅 20:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
اغلاق قناة NRT المملوكة لعائلة عبد الواحد المعارضة للبرزاني في محافظة دهوك شمالي العراق من قبل مجاميع مسلحة بسبب نشر تقرير عن الوضع المعاشي السيء في دهوك.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89429" target="_blank">📅 20:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=fyNfVnanjnpmDdh8awFWzZHlidX0QPsJIgyxN2_-a0U4hMikyMqkBQWr2U_O2TTCqndZVRSxOZA_4GDOJGIubo17U0JAia8KguwTjS5JxC-MDbKaIW20bvkxy74C3iapjIN4xkaYwt5bWTn3PKvq_avq6FTmnsW7Vlx3AY7dmPHZL6J1f8Lf4DCP0QHvav0IwbejNhSNnrDWpm87144eD7r3qeE-HBJ6IjApQ7kCzwAVFiyTjAE90vU2jd6Ej47Q0IgwIpMAi0-PdELaI330xggaXavk6D79xDmfjdLjlFTX0tsOMSaXMhDfQEMiuR7ko4ACTG5pgUq43KfqAVXKYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=fyNfVnanjnpmDdh8awFWzZHlidX0QPsJIgyxN2_-a0U4hMikyMqkBQWr2U_O2TTCqndZVRSxOZA_4GDOJGIubo17U0JAia8KguwTjS5JxC-MDbKaIW20bvkxy74C3iapjIN4xkaYwt5bWTn3PKvq_avq6FTmnsW7Vlx3AY7dmPHZL6J1f8Lf4DCP0QHvav0IwbejNhSNnrDWpm87144eD7r3qeE-HBJ6IjApQ7kCzwAVFiyTjAE90vU2jd6Ej47Q0IgwIpMAi0-PdELaI330xggaXavk6D79xDmfjdLjlFTX0tsOMSaXMhDfQEMiuR7ko4ACTG5pgUq43KfqAVXKYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد آنية من مضيق هرمز تُظهر تكدّس ناقلات النفط بانتظار أوامر الحرس الثوري للسماح لها بالعبور.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89428" target="_blank">📅 20:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=b55OK3Sg6VSQ7WNteuHqf9EuWogEqRCdhv9FKxhe4bHwtrzcykQYwJPgJ-rAsRmNolc_wahKca4G4BuWhYm_kw4RELa2kPIhdxxdNqok75KFwjSqKgt2Bp5huxCeBXSoCZtt3RwWvZxC3B0i1G8O9auj0uQO42uqHp0THYOccQV0iFToDA9TtVdol0seMm4d38OHR6Q8T2LSmm6aQljTpDQBzlYvTtdqRodcJxDfqmjaaRzPDWKLsnjyz-dVR4Ib3iBXTOmofUdwx3kQhf-g-JnIGecmh70r5mJ_S7YC1KA4GEdWor2i1awuDQW6Fh0z5j4Uh_BqS4yh5PvLydqz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=b55OK3Sg6VSQ7WNteuHqf9EuWogEqRCdhv9FKxhe4bHwtrzcykQYwJPgJ-rAsRmNolc_wahKca4G4BuWhYm_kw4RELa2kPIhdxxdNqok75KFwjSqKgt2Bp5huxCeBXSoCZtt3RwWvZxC3B0i1G8O9auj0uQO42uqHp0THYOccQV0iFToDA9TtVdol0seMm4d38OHR6Q8T2LSmm6aQljTpDQBzlYvTtdqRodcJxDfqmjaaRzPDWKLsnjyz-dVR4Ib3iBXTOmofUdwx3kQhf-g-JnIGecmh70r5mJ_S7YC1KA4GEdWor2i1awuDQW6Fh0z5j4Uh_BqS4yh5PvLydqz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
الاعلام العبري: تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89426" target="_blank">📅 19:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89425" target="_blank">📅 19:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb25991r1I6xDICnET2Fq7a_vnBwdb7qQsKYnP6_m3jc58vLIFeyhkJVTUKOPSL2_VH4BHAyagz2-D2rJ7wXyc4e6Jh4-sW0EIe9e6zCp-I8mamiC-BINMcVyltRUCrh6rpwAbV48uKWJUOf6zGTzAg4MOwJZcxko31DGS2igg8wakvIvjYMIcWVp38fc9pryUB5I23q4mOFGpL5VopTAEb91OMrrTv-PWgHh73Z7LAfLMO4mmINHevN7h6pfSf45WY5UpPuri1AUC1TQxSi_8I28HvvTaY6VB7xFwEWcxH0ypWFB6P1JJiKhakVkLF8xAWmhRHCiskTRM-7TmekLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات اخرى قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89424" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات تستهدف ناقلة شمال الخليج الفارسي قرب السواحل العراقية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89423" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عدة احداث بحرية في الخليج</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89422" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حدث بحري</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89421" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدث بحري</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89420" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
السفارة الامريكية في البحرين:
نظرًا للتوترات في الشرق الأوسط، لا تزال البيئة الأمنية معقدة مع احتمال حدوث تصعيد غير متوقع.
تُذكّر السفارة الأمريكية المواطنين الأمريكيين بأن إيران استهدفت سابقًا بنية تحتية مدنية في البحرين، بما في ذلك فنادق في المنامة.
يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي مزيد من اليقظة والانتباه إلى احتمالية إلغاء الرحلات الجوية وإغلاق المجال الجوي واضطرابات السفر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89419" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
شنت قوات القيادة المركزية الأمريكية (سنتكوم) غارات جوية على ثلاث ناقلات نفط خام إيرانية في الخامس من سبتمبر/أيلول، بعد أن أطلق الحرس الثوري الإيراني صواريخ باليستية باتجاه سفينتين حربيتين تابعتين للبحرية الأمريكية كانتا تقومان بدوريات في المياه الإقليمية.
نجحت حاملة طائرات أمريكية ومدمرة صواريخ موجهة في تفادي عدة هجمات إيرانية غير مبررة. ولم يُصب أي من أفراد القوات الأمريكية بأذى.
وعقب فشل الهجمات الإيرانية، عطلت قيادة سنتركوم بشكل دائم ناقلتي النفط الخام التابعتين للحرس الثوري الإيراني، وهما ناقلة النفط "داوني" قبالة سواحل جزيرة خارك، وناقلة النفط "ستارك 1" بالقرب من جاسك. كما دمرت القوات الأمريكية بالكامل ناقلة النفط الخام الفارغة "كيلو" (المعروفة أيضاً باسم "نوكسن") في خليج عُمان، حيث استهدفت السفينة في عدة مواقع حيوية لإخراجها عن الخدمة بعد أن صدرت الأوامر لطاقمها بإخلاء السفينة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/89418" target="_blank">📅 17:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIuEpAHnEbN8jAoTmOx5YTPnaoa2lumUyON62Z-1HguI_hevg9Hz2xuwr1q0QaduWJApgGgy0wYvomvp3FlagL6VVwJUAkgVF9_wBmParaWont5JMlXDXyA-srTumibxQTQCICl0p9tVygd_TuIYaVzDpH5fCkXg5HId1o3Qgeqvho7WQbl0Pc5LYiu3u9X1S37VBCH8tClFPVoG-3274GjWTyMZTMHBeqEkEm7u1uLVp0AIyDTiwzyq5Ktynzks7nVIBnYDCmjlhmU6WAfeYb0sRcRCzOaq367xgSr_jK1EUQhA2t6TO_D0k7E7Wx2gSkZQexMptaTUsCPUjBr8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
بعد انتهاك السيادة من قبل اغلب دول العالم.. طائرة عسكرية ايطالية تحلق في الاجواء العراقية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89417" target="_blank">📅 15:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇷🇺
بوتين يصدر أمرًا بعدم شن هجمات على كييف لمدة ثلاثة أيام وذلك في إطار التحضيرات لاستقبال الوفد الأمريكي.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89416" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCvfIWqh0PtYHb3a7KTTMRO-3RiTuBtHFaFjAQy48-NGlC5bWFBuLwwCGG-uHTvMGMvG7FsrZsQXB92Jx-5W4ZSsQIQUusR9ks9m_k7FIQVj816zwOC5wlLswxq5wItpFnEui73eISti3rLYk9h1-PE_7OvyH2qYomdnXAwq26MD2tezsnFZ-l8Snb2nf9zkg7fIaC-d6bWTD2PjGWEkha5j6V4nb_sj4GpuACv_6bwjbeKLBUxrsKxp0qRo8naAD1Jq4myCInTZ7EsCdZ3iQf09x01j7BcojnyY3tAJQE8jKmXmgXeMl3cNdpCi28UfY67t5sBaG__Aa5llkzuCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات الامنية العراقية تلقي القبض على غسان الجميلي شقيق عدنان الجميلي المدان بقضايا فساد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89415" target="_blank">📅 15:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
🇱🇧
بيان صادر عن حزب الله حول العدوان الإسرائيلي المتمادي على لبنان:
يواصل العدو الإسرائيلي تصعيد عدوانه وإجرامه بحق لبنان، قتلًا وقصفًا وتدميرًا وتفجيرًا ممنهجًا للمنازل والقرى، ومحوًا لمعالمها، ونسفًا لكل مقومات الحياة فيها، دون رادع وبذرائع واهية، وقد أدى عدوانه الإرهابي يوم أمس إلى ارتقاء أربعة شهداء وسقوط عشرات الجرحى، في ظل صمت دولي مطبق وتواطؤ أميركي فاضح، ووسط غياب تام للسلطة اللبنانية عن تحمل مسؤولياتها، وإصرار مخزٍ منها على الاستمرار في خياراتها الخاطئة ونهجها التنازلي والاستسلامي وإطارها الذي يدوسه العدو كل يوم، والذي لم يجلب للبنان سوى العار والخزي، ولم يؤدّ إلا إلى تكريس الاحتلال واستمرار العدو في عدوانه وإجرامه بحق اللبنانيين.
إن هذا العدوان المدان والمستمر بشراكة وغطاء وتخطيط أميركي كامل، لا مبرّر له سوى الضغط على السلطة اللبنانية وابتزازها لدفعها إلى تنفيذ أجندات باتت معروفة الأهداف ولو كان الثمن إغراق لبنان في مستنقع فتنة داخلية. وإن استمرار السلطة في اللهاث خلف هذا المسار العبثي وغير الشرعي وغير الدستوري، يعطي العدو غطاءً لاستمرار عدوانه، ويمنحه مزيدًا من الوقت لتحقيق أهدافه وفرض شروطه وإملاءاته على لبنان.
إن ادعاءات السلطة أن مفاوضاتها المباشرة العقيمة واتفاق الإطار المشؤوم مع العدو يحقق إنجازات، يسقطها ويبددها استمرار الاحتلال والعدوان وسفك دم اللبنانيين والتدمير والتفجير. وإن الإفراج عن بعض الأسرى اللبنانيين، على أهميته، لا يمكن أن يكون غطاءً للتغاضي عن استمرار العدوان والاحتلال والقتل، ولا مبررًا للاستمرار في مسار أثبت فشله وعجزه عن حماية لبنان وشعبه، فيما سبق للسلطة أن أكدت مرارًا من أنها لن تذهب إلى أي مسار تفاوضي قبل وقف العدو لعدوانه.
إن السلطة مدعوة إلى إعادة حساباتها والتوقف عن المكابرة، ووضع العناد والمناكفات جانبًا، لما فيه مصلحة لبنان وشعبه، والعودة إلى الثوابت الوطنية الجامعة التي تحمي سيادة لبنان. وإننا ندعو جميع اللبنانيين إلى الوقوف صفًا واحدًا خلف موقف وطني موحّد يحفظ قوة لبنان ومنعته وسيادته في مواجهة العدوان الإسرائيلي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89414" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتن ياهو يزعم احباط عملية لاغتيال نجله</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89413" target="_blank">📅 14:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89412" target="_blank">📅 14:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية تتوعد مستخدمي الذكاء الاصطناعي لصنع فيديوات خادشة للحياء أو تحتوي على كلمات وإيحاءات لا تمتَّ بصلة إلى ثقافة وأخلاق المجتمع العراقي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89411" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89410" target="_blank">📅 14:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتن ياهو يتوسل لانتخابه: من سيُنهي ما يجب أن يُنهى؟ من سيُنهي هذا النظام في إيران؟ من سيُنهي حزب الله؟ من سيُنهي حماس؟ خصومي السياسيون يستسلمون لكل ضغط. أمريكا تقول لهم "لا"، وهم يرتجفون على الفور. هل سيفعلون ذلك؟ لا. لن يفعلوا ذلك. نحن سنفعل ذلك.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89409" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=gXXiwKVQEbTAJIm0QsLzdzP1-Ll1kO1MXj93urCUzpQY49t1pVfhRHadvydzUYKKS9iY-bXTQzndcCVsNkcBieUxUYRYFjQwRR0aTjX3zdPzn-yR1wFpHHYbkRtnScSpeMZy9AvbyZMxNI4UWYrNUWoIqRTMCJTCjuHkM7jgbSUPb1qaNPmRkSUeZdy99H0htraT8Mahq7bl6YZc5JgrNaaImS7PbijG3siM_Z0OwxSGF0Mi2TkwENXiUxt_uyfRRLSdnuWqyCVcOmmNT0TvW7VVEdcYI3l_4sk6u7hbt5Mz596pZ_jPbKaUYB0kWqCgSaWe0rv4MeazwMGiOib1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=gXXiwKVQEbTAJIm0QsLzdzP1-Ll1kO1MXj93urCUzpQY49t1pVfhRHadvydzUYKKS9iY-bXTQzndcCVsNkcBieUxUYRYFjQwRR0aTjX3zdPzn-yR1wFpHHYbkRtnScSpeMZy9AvbyZMxNI4UWYrNUWoIqRTMCJTCjuHkM7jgbSUPb1qaNPmRkSUeZdy99H0htraT8Mahq7bl6YZc5JgrNaaImS7PbijG3siM_Z0OwxSGF0Mi2TkwENXiUxt_uyfRRLSdnuWqyCVcOmmNT0TvW7VVEdcYI3l_4sk6u7hbt5Mz596pZ_jPbKaUYB0kWqCgSaWe0rv4MeazwMGiOib1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة البنزين تتوسع في العاصمة العراقية بغداد وطوابير الوقود تمتد إلى مسافات طويلة</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89408" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
العراق يعلن نجاحه في تفكيك مخيم الهول السوري ويعلن اغلاقه قريبا.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/89407" target="_blank">📅 14:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=osdi5UJNvcaM9oV7t4H1S-Q0PC11-i8KumK8QRBYNbN5PHqEferZakhNyXhO3dyAjNJpC80XsxvqPbpGLlhE-xa9Js3KbdMNHkC4O206MCcA-kBANQWof1q6o3ADmW412AdsPUgYV0c_fVig8vcAS3lVbFwWqgBRYTYnZXeMuzQnWo2BBwncttCRWjqcLDE9MOJjpmme7duwm9e-NY-tLx3vKEHdttz4X5mrrA8Hv14078E4MdbelBIoBhxygVI-3erEY8Q9QFZX9c438BcjQAUJFdvCtXfD9w4SNFnfuRDz0dd5rbDu0FDRPehoK4BV4exR3ceSSOcuP7-Nj3znHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=osdi5UJNvcaM9oV7t4H1S-Q0PC11-i8KumK8QRBYNbN5PHqEferZakhNyXhO3dyAjNJpC80XsxvqPbpGLlhE-xa9Js3KbdMNHkC4O206MCcA-kBANQWof1q6o3ADmW412AdsPUgYV0c_fVig8vcAS3lVbFwWqgBRYTYnZXeMuzQnWo2BBwncttCRWjqcLDE9MOJjpmme7duwm9e-NY-tLx3vKEHdttz4X5mrrA8Hv14078E4MdbelBIoBhxygVI-3erEY8Q9QFZX9c438BcjQAUJFdvCtXfD9w4SNFnfuRDz0dd5rbDu0FDRPehoK4BV4exR3ceSSOcuP7-Nj3znHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طائرة عسكرية امريكية تهبط في مطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89406" target="_blank">📅 13:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇵🇰
البرلمان الباكستاني وللمرة الأولى في تاريخ البلاد يمنح قائد الجيش عاصم منير سلطة قيادة رسمية على جميع القوات المسلحة الثلاث: الجيش والبحرية والقوات الجوية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89405" target="_blank">📅 12:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=Gf5BaKJ_dbAXGAhPYOJ5y54xxeiEPeIgwNMdRLObw4LQHxXdpW9DBU3OrhNQkfuerge-czK434ZN0HFhF3rDzajMv4HS0_VvXRwaWUP9O_hH46UJWNsygi5W9_-1PZxinGn8IZqtALjEkspTcrA3jVmf7QC82c-GP1yGEhiwfQLRMSJPn2UTC7flMKcDxbkG_UfgCiUe2yituQJ5td-LtgdVT5CfN4i0ayttJLCog3vbKMp90YQAAbWO4S_cNW4ycd6xN2ibmdmyePGmVoHVrB_twJ2SsMhn2BnJbIfjEAHm1ST4xRSjCGHFBGjX2EFhZpQ0z_vYUJs_MKmGt-rrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=Gf5BaKJ_dbAXGAhPYOJ5y54xxeiEPeIgwNMdRLObw4LQHxXdpW9DBU3OrhNQkfuerge-czK434ZN0HFhF3rDzajMv4HS0_VvXRwaWUP9O_hH46UJWNsygi5W9_-1PZxinGn8IZqtALjEkspTcrA3jVmf7QC82c-GP1yGEhiwfQLRMSJPn2UTC7flMKcDxbkG_UfgCiUe2yituQJ5td-LtgdVT5CfN4i0ayttJLCog3vbKMp90YQAAbWO4S_cNW4ycd6xN2ibmdmyePGmVoHVrB_twJ2SsMhn2BnJbIfjEAHm1ST4xRSjCGHFBGjX2EFhZpQ0z_vYUJs_MKmGt-rrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
زيلينسكي:
روسيا استهدفت مطارين في كييف و بوريسبيل قبيل وصول ويتكوف وكوشنر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/89404" target="_blank">📅 12:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=nOzwmfF_x111oqwV2OrexOvfwjB7Df9yEZXgPoc6KW3xpjU1bbdz2-TmdzyGKnVPdAxxrWxTOhfkh5vBR0MYpbagsDdju79Xx3oBPiIweXni4OyDpRib-Sfpaurr3OmN9z_vQOM_VUaWbQfRkPlMrhq-V7F_yrRUb0TMt2K0vGaOhSSoky4iypCJ_485PR20jwZqid6C7RW1qr-Vm3F0oGw763fAYp91l5u3X8EIM0M5bMdHKI4wq7yCezlq4z3BEu5tiHCwTKIVTstZ5anuuV4ft071lpq-dAnUEiDa52MT12wZ1ddSp-ihjLt61sTmn7khE53eB9EdIsTN-a77KlMIwfJHxnwCJ1bCJd5f6h-_J-UBm9fYeA13dS2rokXDGd1y-Hc4JjHOjVI36YvfWtuII8HYGladIHpccLaXdKRHDqNqSC1AcpdQZDmbiLSqZ0kMcb6KDyi3VBkuQuQ0Os8shwdLrwNWlBGITnKVnI7UA1C9b44TdcSb_Mx8TBu18FQVgxYyMUB-n4e1h-tEmI1BVBdXx6qlbS1k1gbBjI6GOWLhfJS_G-_5wy5VBDbuc0fp5KQhs7NMvvL5E9Nu80t_O95D1FS9a7JWv1cAeB9w0oTGe8hwFNWueQoqF06kWKSFMHVcu0o2XbxT79wqQWf3igYszA05bvAGPjhdJiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=nOzwmfF_x111oqwV2OrexOvfwjB7Df9yEZXgPoc6KW3xpjU1bbdz2-TmdzyGKnVPdAxxrWxTOhfkh5vBR0MYpbagsDdju79Xx3oBPiIweXni4OyDpRib-Sfpaurr3OmN9z_vQOM_VUaWbQfRkPlMrhq-V7F_yrRUb0TMt2K0vGaOhSSoky4iypCJ_485PR20jwZqid6C7RW1qr-Vm3F0oGw763fAYp91l5u3X8EIM0M5bMdHKI4wq7yCezlq4z3BEu5tiHCwTKIVTstZ5anuuV4ft071lpq-dAnUEiDa52MT12wZ1ddSp-ihjLt61sTmn7khE53eB9EdIsTN-a77KlMIwfJHxnwCJ1bCJd5f6h-_J-UBm9fYeA13dS2rokXDGd1y-Hc4JjHOjVI36YvfWtuII8HYGladIHpccLaXdKRHDqNqSC1AcpdQZDmbiLSqZ0kMcb6KDyi3VBkuQuQ0Os8shwdLrwNWlBGITnKVnI7UA1C9b44TdcSb_Mx8TBu18FQVgxYyMUB-n4e1h-tEmI1BVBdXx6qlbS1k1gbBjI6GOWLhfJS_G-_5wy5VBDbuc0fp5KQhs7NMvvL5E9Nu80t_O95D1FS9a7JWv1cAeB9w0oTGe8hwFNWueQoqF06kWKSFMHVcu0o2XbxT79wqQWf3igYszA05bvAGPjhdJiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇦
بسبب زيارة كوشنر صهر ترامب لأوكرانيا   ‏تم أمر وحدات من قوات الأوكرانية المدعومة من الناتو بالالتزام بنظام الصمت على الخط الأمامي من الساعة 00:00 يوم 5 سبتمبر إلى الساعة 23:59 يوم 8 سبتمبر ..</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89403" target="_blank">📅 12:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=LLKfbZbCIzdGxisQCRI9FSrNpvxmb1YJwMBMNASpqajA6FQAjA5MK934Fukz4zaTVfxguPU5enfNDnCg_qmSG5u1FC1eyjm6Eox73saABzAwtagHyh-NRq-kDl7ikrjRsJUd078jjtm7Ym2XUJxy34fm8VLYuuxtvYbQEGNcnGIph4J8LBHqQJGreq_PqC_u1G1608sRHU7OakUlzsWJpg_uoLuC1yx7QkVCii82-E7rdlG0K6cEbiC2UfA6q3eUbq6SZcn-PSP0qYU0Mqhqo0bIUednWS5Wp3UWPYNFk1dDRnnj-Wile7N2wzo3ce-KnXn2gqycKe8njLlykaF0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=LLKfbZbCIzdGxisQCRI9FSrNpvxmb1YJwMBMNASpqajA6FQAjA5MK934Fukz4zaTVfxguPU5enfNDnCg_qmSG5u1FC1eyjm6Eox73saABzAwtagHyh-NRq-kDl7ikrjRsJUd078jjtm7Ym2XUJxy34fm8VLYuuxtvYbQEGNcnGIph4J8LBHqQJGreq_PqC_u1G1608sRHU7OakUlzsWJpg_uoLuC1yx7QkVCii82-E7rdlG0K6cEbiC2UfA6q3eUbq6SZcn-PSP0qYU0Mqhqo0bIUednWS5Wp3UWPYNFk1dDRnnj-Wile7N2wzo3ce-KnXn2gqycKe8njLlykaF0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/89402" target="_blank">📅 11:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
🇺🇦
دخول اتفاق وقف إطلاق النار المحلي في منطقة محطة زابوريجيا النوويةحيز التنفيذ.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/89401" target="_blank">📅 11:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
مصدر امني ايراني...
الانفجارات في محافظتي طهران واصفهان ناتجة عن تفجيرات مسيطر عليها.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/89400" target="_blank">📅 10:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/89399" target="_blank">📅 10:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
تحقيق مع نحو 50 عضوا في هيئة الأركان المشتركة بشأن تسريب معلومات للصحافة عن حرب إيران.
التحقيق مع العسكريين يتركز على تسريب معلومات عن تراجع مخزون الجيش من الذخائر الحيوية.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/89398" target="_blank">📅 04:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل: أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/naya_foriraq/89397" target="_blank">📅 00:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇱
🔻
جيش الاحتلال يدعي اعتراض مسيّرة أطلقها حزب الله باتجاههم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/naya_foriraq/89396" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/naya_foriraq/89395" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/naya_foriraq/89394" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=kYHTtLAQFbIatex5fLRHS2crHIQcCmJuWgUAODRoTSmXtrFbFKONtoq8hCwp91ArGzdbQn_VoAU5N3KXLM244X-Wdzh2FMrA8LdQ-YjVgd3W6MIscQp5zXMrRDFx98OlX9C690G6VaustKQ_Wk6HFTO2KAF589AeOwPexGhups76xgyX_tyumRIa7bq_-x1dJiqj_8spZUfvzKN0EbuVUWcTG8rCrXkiJD6iYCgj_Y0NcUkcL0j40NqfI1gVuHHtSt3VSMng3URtlgBuxGxZNzerNewp08V2CnZZIWk9rxIe78BhOftV0qM5unbFDdDZtC6EmWUEsmrlwlYp6QPW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=kYHTtLAQFbIatex5fLRHS2crHIQcCmJuWgUAODRoTSmXtrFbFKONtoq8hCwp91ArGzdbQn_VoAU5N3KXLM244X-Wdzh2FMrA8LdQ-YjVgd3W6MIscQp5zXMrRDFx98OlX9C690G6VaustKQ_Wk6HFTO2KAF589AeOwPexGhups76xgyX_tyumRIa7bq_-x1dJiqj_8spZUfvzKN0EbuVUWcTG8rCrXkiJD6iYCgj_Y0NcUkcL0j40NqfI1gVuHHtSt3VSMng3URtlgBuxGxZNzerNewp08V2CnZZIWk9rxIe78BhOftV0qM5unbFDdDZtC6EmWUEsmrlwlYp6QPW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب: أتحدث إلى بوتين، وهو لا يسعى إلى مهاجمة حلف شمال الأطلسي (الناتو)، ويتكوف وكوشنر سيقدمان مقترحًا لإنهاء الحرب في روسيا.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/naya_foriraq/89393" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=Dt-u3ob18boO9cMenvdXkWd2z7lQmF-29Go_i55sjXhoi-HWXZgVWChQEF6C893DhC8Hmz3mj2yDxcMgopy6lGVONl1h0TOlYIaud_ubO3UJqa40_9XKyL-JZfw35AT8bdQTim9aTYmWX-sdHd4GV7x3Gr8PP456hMmHxekNT1fbq2cWALobzEcwo-Aqfg8Z3qZ1zn2DDLJqFIyT9A9TnS_k7_jIR4gjVLNIf5dZPevOr_iMej5njxwHmtgD5yxwd29Awx6sK6iyetcZnYXOn30vJhUdDnL4TXjbu4KqdBOJrWs0Ml2rpAthO8yN2EH6XtyvpHlnk4L5f6YTFzQ46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=Dt-u3ob18boO9cMenvdXkWd2z7lQmF-29Go_i55sjXhoi-HWXZgVWChQEF6C893DhC8Hmz3mj2yDxcMgopy6lGVONl1h0TOlYIaud_ubO3UJqa40_9XKyL-JZfw35AT8bdQTim9aTYmWX-sdHd4GV7x3Gr8PP456hMmHxekNT1fbq2cWALobzEcwo-Aqfg8Z3qZ1zn2DDLJqFIyT9A9TnS_k7_jIR4gjVLNIf5dZPevOr_iMej5njxwHmtgD5yxwd29Awx6sK6iyetcZnYXOn30vJhUdDnL4TXjbu4KqdBOJrWs0Ml2rpAthO8yN2EH6XtyvpHlnk4L5f6YTFzQ46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: قد نضرب "جبل الفأس" قريبًا جدًا.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/89392" target="_blank">📅 22:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=ll6ZQpEfpGz7GnYoTKOtwG7ILletFZ31OzEuePJFhVDONGB_2_Zz6tktESUykw95ZUoTN_pn6K6CpKn26ueRMfDcYEe-0jxN5Z_Lddz3YyGr7TD3mue2bK3uCpOzkK5mSnOqLe6f2ScKAyYP-ncDDhNoJf1pCIGbtYGJjBw1g8SIkIaVCuHFfwmhgDz0zBwHWLpX1r9pjZuJOfvmrwBynyzF_XmY-DHkphG-Tpyhfc3YDHC6W1BQLgMi5eOol-wD1FHT9YAd75Voj7PLA6W4eO6oiylfQtA-xW4PSgsNQ5GlgYa8VwfzNuYQJvwrkzO3j_D13Uel9lhgCmhOiKqGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=ll6ZQpEfpGz7GnYoTKOtwG7ILletFZ31OzEuePJFhVDONGB_2_Zz6tktESUykw95ZUoTN_pn6K6CpKn26ueRMfDcYEe-0jxN5Z_Lddz3YyGr7TD3mue2bK3uCpOzkK5mSnOqLe6f2ScKAyYP-ncDDhNoJf1pCIGbtYGJjBw1g8SIkIaVCuHFfwmhgDz0zBwHWLpX1r9pjZuJOfvmrwBynyzF_XmY-DHkphG-Tpyhfc3YDHC6W1BQLgMi5eOol-wD1FHT9YAd75Voj7PLA6W4eO6oiylfQtA-xW4PSgsNQ5GlgYa8VwfzNuYQJvwrkzO3j_D13Uel9lhgCmhOiKqGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟  ترامب: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/89391" target="_blank">📅 22:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=PipMGAD914V7X3oeQkqKlD6mS3KipXOchERMBB2FGbLqhKWah-bNy-L-X4dnYCzTz4Y5GrhNZZu54v9XkNPOr4oHAIZ4a-xupHKeqiswNIo4f6zCOXBfkTZS2qjkVuDC9f0kWzqK-8EXXDsnBPKRFV_WpVR5hAfn5aCP-vW5msYtTxkivF8qPcPm-cUv27vUtY1BJfWxGRBchzRYXTL_NiwMThaomGJy3dl0yQiqzLNZgjMDH0i-mhe2Lyp7Fvx-z1FiIP7LdJoWzu0FdkGoUjOfjxq-rjsm03MM_SgIGH4o-lUYoirLIfrPwiOu_rfibj2IawEOhShbNCwjlDGk74i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=PipMGAD914V7X3oeQkqKlD6mS3KipXOchERMBB2FGbLqhKWah-bNy-L-X4dnYCzTz4Y5GrhNZZu54v9XkNPOr4oHAIZ4a-xupHKeqiswNIo4f6zCOXBfkTZS2qjkVuDC9f0kWzqK-8EXXDsnBPKRFV_WpVR5hAfn5aCP-vW5msYtTxkivF8qPcPm-cUv27vUtY1BJfWxGRBchzRYXTL_NiwMThaomGJy3dl0yQiqzLNZgjMDH0i-mhe2Lyp7Fvx-z1FiIP7LdJoWzu0FdkGoUjOfjxq-rjsm03MM_SgIGH4o-lUYoirLIfrPwiOu_rfibj2IawEOhShbNCwjlDGk74i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟
ترامب
: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/89390" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihlXusTkUxv0uItBhOiCw0E2HQRnE4U6FAK8d5ZJUoHsNYOyJJ-HixDcY8QB5Q-JOoNlCJTjNDtP7uBT1KykiWVCpgoQu-CmL8QdosqCMHAUTS6rEmbklDECH7C5tWyExX41DtvUYXuIvJqoxjak9Srvg6_gbIWgWhrZPKnSIxW-NMV4gZwY5-WjaRVqlmAI7uC4wqeJLqqKzaYW6zs47zTJ_1TTbSeqNj7MZbRjDmI9AMkVyuh3rGw2wBl8t_97u7v3bS3JjkJ4UvhsjTtVBOvSJni3c-VRc20aBlZajeWDSRMCWaJmayhZG1oBUDQZutji0K4a3CZGIABGeRJuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدُ الله.. حُماةُ الأرض، حُماةُ العراق.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/89389" target="_blank">📅 22:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
🇺🇸
‏
الخارجية الأميركية:
صفقة طائرات هليكوبتر بيل 412 إلى العراق تقدر بـ 150 مليون دولار ‌.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89388" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=Z18IhhXDTKKqZb_q92aFORmFHQmNcii1YImj9h1oanaGMaFL-Yw-15w7zDrN5G1pWe3fBSUSVWjQOrl80poVWvqkZQmoSThoTQsw2-lLBKGLEtDTtUxLYQ2PT2-nOdxeXnhAbHYTXPkTAqD1G1mqYSAx_I3cf-tAlK2LdtnCViBJ5iaqASmwNSFXoaD0S_agzTp2kkqfcBMjh6yMB2zLgHUZWH8vPwd2iXKSC05e5As5uapHW2l1M9adtHA05aEqC6YPAV1m0PAYSOszsk8TzRjETN30PD66fuof8AzTPvsblbcIZLi6qxXiOqSMgpzeeTIzSZ2CMR_jBAC2KBW8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=Z18IhhXDTKKqZb_q92aFORmFHQmNcii1YImj9h1oanaGMaFL-Yw-15w7zDrN5G1pWe3fBSUSVWjQOrl80poVWvqkZQmoSThoTQsw2-lLBKGLEtDTtUxLYQ2PT2-nOdxeXnhAbHYTXPkTAqD1G1mqYSAx_I3cf-tAlK2LdtnCViBJ5iaqASmwNSFXoaD0S_agzTp2kkqfcBMjh6yMB2zLgHUZWH8vPwd2iXKSC05e5As5uapHW2l1M9adtHA05aEqC6YPAV1m0PAYSOszsk8TzRjETN30PD66fuof8AzTPvsblbcIZLi6qxXiOqSMgpzeeTIzSZ2CMR_jBAC2KBW8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في الاردن</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/89387" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">موجة انفجارات جديدة في سماء قاعدة الأزرق بالأردن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89386" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/89385" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7oJ3N8mbiZglohbE9JKosD1YMRdm6JvHRPDCUrUPWKut4BQUqG4mI8yV5aoxqyZI2bhcblJN-wEa3dwMeKQ41qv_vIPzIuWX1O0cmrv2bJPPKHPRu7QVdWrdIczzlh5P6GngAJ251RvZCb8ewiNeAr53s3OXB-XAoKpxApmGM0LZQNiQfeMH7xEaukEbxPkWHTftyvje9-xHBYicPw4shwDn9__53nlHLmwqotvDdGUsskH8UofWXAVxZu5TZlmC1WRDwQUFRFmQ7ljwbuamQKoJdXY6BI99v4qUOUDLoy2DOPDHcOlqabOWFq_M5MKNvaDUnWHEquOoKn4OG-d4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/89384" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89383" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3MyLEcO1tJzGhnIlz4wkWe1s0-cU0cqvlqeeMqb8cwzSjAiEix-LeO31jIxiv6vnObZtC5b_I57sqV7wJ3MqjawhzC9vOViihReENS7CS8Va44Q3Vh7tk0fBCmunCfSs7g_LjjrGdMGdyCeyFkhRUWS3umSuPkxZd5489ZGvrZIDM8K-odAVcm8H5Hk6KKY3fDSJ2aHELpmuPI_WpcCZHBKkzD7vxk6nx08lZwFRAsqlJjtMSs3gjhyM-n36S0bUIHF9bQDx1-JtVStJYhFIEfh4HZSZ_5mU5MMcWg1PYxIxi3CWsYZPXiZNbu6IfFBg50arscp2oLuw7toN8h27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: ‏إن تركيز الصين على تعزيز الأمن المشترك يعكس مبدأً لطالما دافعت عنه إيران.‏يجب على دول المنطقة أن تتولى زمام مستقبلها بنفسها، ولن يتحقق الاستقرار الحقيقي إلا من خلال بنية أمنية جديدة محلية المنشأ. إيران على أهبة الاستعداد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/89382" target="_blank">📅 20:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=tYeEsi76kvjJlO9T5XfHlY-ix1V7_qXY_y8DLJKs70gjS1933P1SChfn-fGnAoYTIUEtwCR_IxczBY_mIzHdT-sNmTtLtvQEBcuYq-Lcz06H1sl1LOHqhxlhWZLGgCeJGyQ5FJe-CnbJFEzvDkP5mWgFqTd_ollml0qo3hQuRueMU3tC14VRxGmmSmMAtvU12lrN7EvunigPdxe0RD4Mp60SfyLVFU0HwlPQL-cSKOtuYvwuSX0P-GnyjmmZsjHJW0IX8CmGFGCNa3NENDqPNRsykOberw_pXpbhcmmrspT-lknbGg8tCMueH83jYN1Bi6KdWhMIDRqbMOqd-cgq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=tYeEsi76kvjJlO9T5XfHlY-ix1V7_qXY_y8DLJKs70gjS1933P1SChfn-fGnAoYTIUEtwCR_IxczBY_mIzHdT-sNmTtLtvQEBcuYq-Lcz06H1sl1LOHqhxlhWZLGgCeJGyQ5FJe-CnbJFEzvDkP5mWgFqTd_ollml0qo3hQuRueMU3tC14VRxGmmSmMAtvU12lrN7EvunigPdxe0RD4Mp60SfyLVFU0HwlPQL-cSKOtuYvwuSX0P-GnyjmmZsjHJW0IX8CmGFGCNa3NENDqPNRsykOberw_pXpbhcmmrspT-lknbGg8tCMueH83jYN1Bi6KdWhMIDRqbMOqd-cgq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/89381" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89380">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89380" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89379">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الصواريخ الايرانية تصل الى الاردن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/89379" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89378">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل:
أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/89378" target="_blank">📅 19:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89377">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMabcS0FvVamltsrGElwm00Q9fedfcf0rW3glpQtL63aGszGs3GG1hBa2yhEZ-ycBZSTs6Bel8dmrORUluGn1ebDu6QOZYArw75wjs0rtR6ON18ahPDoIDCH7BAbhfPYzCFS_N76WAmJxYVyLRHUfIIMi8ZA2D_miTRWq8lNN1M3KXmYphNlpF7pPH_ErpyaX7GlFY7z4H-ZpZX8n3P-AV4Tjkyn4zWI486jbpL2WR-mB7YXcJlS1aQtBCpY3VXmm9OI0d0hEQ2dJHsnkyxmPX4gUyhjwa_TwKmN_p6CjvKbybzCkV6Kx440Nkdz8bbkepYn_otUPDOLT0dm6xHKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
يفضل المتطرفون اليساريون والديمقراطيون والشيوعيون أن نخسر الحرب في إيران على أن يربح الرئيس دونالد ج. ترامب الحرب من أجل أمريكا. بعبارة أخرى، يفضلون أن نخسر على أن نربح! هؤلاء أشخاص مرضى للغاية يعانون من متلازمة جنون ترامب الخطيرة، والتي يشار إليها أحيانًا باسم متلازمة جنون ترامب.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/89377" target="_blank">📅 19:39 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
