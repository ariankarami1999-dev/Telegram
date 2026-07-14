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
<img src="https://cdn4.telesco.pe/file/neMkp4YDm-U23zIJe-Tbtsa75mqsOMphTGny4Uf9MtoekQeIRBrSjewvCPhMDotLbNti7u3rt4sGcZTB3gnBcKYW-SGhbg8bSauArVBIdx7SrmdfR513ydZGOrCWNrbQ9GOph69Mj85P9ggxIFHw3NsJepbnCD50R9ylzQRbAtgRZjNOY0cuLhB8Ot009QHLohLu9RcniwUwrEXE_JKWj1SivOZ3aC1oaaMTq4a2rId0DLYZyzTq0mFOuJzO61oC9YiQnyg5NuL818ivWpKH44XL5_5W1Xdxgrzz5xN1ysAluHipHcs50VU-OzKkSuVStD3rhFqtNUysXAJ9amjVoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 262K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 18:12:24</div>
<hr>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قوة مسلحة تابعة لعصابات الجولاني تحتجز السائقين العراقيين في مصفاة حمص والسائقين يناشدون الحكومة العراقية لانقاذهم واعادتهم الى البلاد</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/naya_foriraq/82966" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
‏مندوب أميركا لدى مجلس الأمن: إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/naya_foriraq/82965" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
‏
مندوب أميركا لدى مجلس الأمن:
إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/naya_foriraq/82964" target="_blank">📅 17:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/82963" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/naya_foriraq/82963" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نادي النصر السعودي يلغي معسكره التدريبي في ابها ويعود الى الرياض بعد هجوم انصار الله</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/82962" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مواقع متخصصة في تتبع حركة الملاحة الجوية تظهر استمرار إغلاق مطار أبها السعودي</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/82961" target="_blank">📅 17:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIk087OGv21E1kbTzoeJUbCqfHhOUmjmlAvLyTPdUxG8y4jtEctOpVjsDtIAsu-LO43LnefrOYEhs3-kmD_TWrAoVWuwY54VbenXAQxrMifErcGaXkK0EG1_r_p_egv6Gojte-zTMfgOA1TIqPONqKVP5MFEI76vpvU-GeI4UFHYjWCmbljlAXh6SY8ZE7zuWGyKjyk3r2o4mGoMJZWCUi2GWiiyqTG9RuhjwajY7OUhdbIcWiWYQkYIoHyGUdz3IYeMqyhb8J6sCByMUJo6x4J5Y6oqavTuyTIdgZtzV0x9lu3ZXSBGZAh8Qi9me1Rjgtszf9Ux9s7Wxgn4aYf9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
الاعلام الحربي اليمني ينشر:
نحذر جميع شركات الطيران من العبور في الأجواء السعودية وعليها أخذ تحذيراتنا على محمل الجد حتى رفع الحصار عن مطار صنعاء الدولي
We warn all airlines against crossing in Saudi airspace and they should take our warnings seriously until the blockade of Sana'a International Airport is lifted</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82957" target="_blank">📅 16:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قوة امنية من بغداد تدخل ناحية الزوية ضمن محافظة صلاح الدين شمالي العراق وتبدأ حملة تفتيش واسعة عن (احمد اسماعيل فرحان) احد المتورطين في قضية عدنان الجميلي</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82956" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوالف الگهوة  رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82955" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سوالف الگهوة
رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82954" target="_blank">📅 16:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaWMcqCR0RESGBnth05AfRzZ1wOr_OryBZ8bpFiyfZixpoiYKngDBpOHpJXIWqyimDi7LTQ-73vAava-4_dWKXi3cjVlx25aJ3nBSp64mhLaejTKBDaHi8OHUDgF4WGbt7PZBqE89AtmWVje6lyjwGjtjgEC1aTEyoG7w4KZCgZGzT67VxcUpXCtHlai1DgbzdxzRmn4qlswhzvne4K4kVB23-KElpe9IUynyqCzQpMBbNz34dLc2XunHsSrWp9ojPP98deGKHXhe5Y3fBnfajum2kD8IVTnarZe-hPnzBxglDdcto7wbLWzVau0bHIcOWHB3qUjq-lyC_YsYSTh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نحو 180 نائب ايراني يوقعون للمطالبة بإعلان انتهاء اتفاقية إسلام آباد مع الولايات المتحدة ومواصلة عمليات الانتقام لقائد الثورة الشهيد وسائر الشهداء</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82953" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتن ياهو يجري زيارة الى مفاعل ديمونا ويقول:
لقد أزلنا حاجز الخوف. لا أستطيع أن أقول ماذا سيحدث في إيران حاليا، ويمكن أن تحدث أمور كثيرة. نحن مستعدون لكل سيناريو.
أقول لقادة إيران: لا تراهنوا على أن يسود الهدوء إذا هاجمتمونا، لا تراهنوا على أن تكون هناك إعادة للرد نفسه، سيكون ردنا مختلفا، وأقوى بكثير.
انتهت الأيام التي يقصفنا فيها أحد ولا نرد عليه بضربة مضاعفة. هكذا سنفعل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82952" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
الهيئة الإيرانية لإدارة مضيق هرمز:
قبل التصعيدات الأخيرة التي قامت بها القوات الأمريكية في المنطقة، والتي أدت إلى إغلاق مضيق هرمز، خلال فترة ثلاثة أسابيع بعد توقيع مذكرة التفاهم، قامت أكثر من 200 سفينة غير إيرانية بالتنسيق معنا، وقد حصلت معظمها على تصاريح العبور والتأمين.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82951" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اندلاع حريق داخل مطار البصرة الدولي</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82949" target="_blank">📅 15:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏وكالة سلامة الطيران الأوروبية: يُمنع على مشغلي الطائرات العمل ضمن المجال الجوي للبحرين والكويت وقطر والإمارات العربية المتحدة، أو المجال الجوي فوق مياه خليج عُمان.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82948" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏وكالة سلامة الطيران الأوروبية: يُمنع على مشغلي الطائرات العمل ضمن المجال الجوي للبحرين والكويت وقطر والإمارات العربية المتحدة، أو المجال الجوي فوق مياه خليج عُمان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82947" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الاعلام الايراني:
عدوان امريكي يطال مبنى تابع لوزارة البيئة في قرية سيد جوذر بمحافظة بندر عباس مما أدى إلى استشهاد ثلاثة أشخاص..</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82946" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04058516a3.mp4?token=eqUO883jfrOnSm_uxof-6UBacoNCV6KGMwh00sX51sy1tsaS4kBkv3UWPLuWgGuqp6NTy14rFv9DD_LWj6r0XGxTKv05AKhTSjRXqG-tedkzW-5IcWQJbwouoABWI5zoxZhLrpKzdDE0rRQsclSTUKZxwuKGR0EggtjoB2QCup6D91kNzS3_TM91BpRjKiFTb69tifvSGZh0mdhS5QAVn09TgCXLMSCqll6vZgsWsyDKv_0loveT8F-BZpkHvnt7sebZPQof9pN7kc1eOQIvUzwJoX6_O2Gw0Lrbor2mrggiRfeLRZQua2E6DCnnzpxazni7w97Tf7j7qg6LomiIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04058516a3.mp4?token=eqUO883jfrOnSm_uxof-6UBacoNCV6KGMwh00sX51sy1tsaS4kBkv3UWPLuWgGuqp6NTy14rFv9DD_LWj6r0XGxTKv05AKhTSjRXqG-tedkzW-5IcWQJbwouoABWI5zoxZhLrpKzdDE0rRQsclSTUKZxwuKGR0EggtjoB2QCup6D91kNzS3_TM91BpRjKiFTb69tifvSGZh0mdhS5QAVn09TgCXLMSCqll6vZgsWsyDKv_0loveT8F-BZpkHvnt7sebZPQof9pN7kc1eOQIvUzwJoX6_O2Gw0Lrbor2mrggiRfeLRZQua2E6DCnnzpxazni7w97Tf7j7qg6LomiIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قوة امنية من بغداد تدخل ناحية الزوية ضمن محافظة صلاح الدين شمالي العراق وتبدأ حملة تفتيش واسعة عن (احمد اسماعيل فرحان) احد المتورطين في قضية عدنان الجميلي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82945" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اندلاع حريق داخل مطار البصرة الدولي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82944" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محافظة خوزستان: تعرضت منطقة في مدينة آبادان لإصابة قذائف أطلقتها قوات العدو الأمريكية. سيتم الإعلان عن تفاصيل إضافية بعد الانتهاء من التقييمات الأولية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82943" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عدوان امريكي يستهدف عبادان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82942" target="_blank">📅 14:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عدوان امريكي يستهدف عبادان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82941" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
اللواء رحيم صفوي:
قبل 15 عامًا، نظر الإمام الخامنئي إلى إغلاق مضيق هرمز كأداة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82940" target="_blank">📅 14:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21964afa00.mp4?token=Rq0Qzc8avzrmmS6r5etiPD_tLGCry5pRm36Tz1RwMOszMIpHkW5QMJNDurLy9SiBYSxccN-8tvg7F6a0ev_LufLM_WMUjqM3q9AWCyXdUSJhiCR6j16kKso_CjOaLmA3X6viQWsoVq1-Rw8CtJF_fP2WGRFfZgFs0-Dep0Y2X4wdH1JGmHrBb75upk2DojyXRdbA7j9VNYig1WGNPNa1CJ9cVrNPow1G4JOUzIZG07EDMwa4MsDLRTtt-5oeel_HkQOCVsQt2ul6jPSzMIXkgvu6wLxxl3KROliB2BLiArPfLz5bgSMfnKhnj_qR3Wcz9cbEHaOttf_NP_RrnkTRjTrRj4BY1Ai3miu4b9ibM3ssulzEaG14VJvCzQcp3-HZaPJEj7il1mep_q84QHpswnDBkMj33uSpOlweqnwWFXzG_4jAH8Jb6TXRlnW4XxPH4SsPDrHajn1N0BpNlHpWDecJ6LeRXSH6VHTPWup6BHE9Fu2XXUz_Fc485R7Lmt1OOSymyofxKyXOPlXCOngJ626B-OJ6hYE0Ft6VKu3jToHI_ibJ0bY5Tmb25uSuw1xXeDzdKhf7sNVxPyfnYAy7vg79dOWZ4AVovp5_O1pQL7SRTZG5s02l4i0SX3V1z-k1VryNH98yX0Slr5ycvx9r0G_CA_Wh_ZoTi7Ywq86wxt4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21964afa00.mp4?token=Rq0Qzc8avzrmmS6r5etiPD_tLGCry5pRm36Tz1RwMOszMIpHkW5QMJNDurLy9SiBYSxccN-8tvg7F6a0ev_LufLM_WMUjqM3q9AWCyXdUSJhiCR6j16kKso_CjOaLmA3X6viQWsoVq1-Rw8CtJF_fP2WGRFfZgFs0-Dep0Y2X4wdH1JGmHrBb75upk2DojyXRdbA7j9VNYig1WGNPNa1CJ9cVrNPow1G4JOUzIZG07EDMwa4MsDLRTtt-5oeel_HkQOCVsQt2ul6jPSzMIXkgvu6wLxxl3KROliB2BLiArPfLz5bgSMfnKhnj_qR3Wcz9cbEHaOttf_NP_RrnkTRjTrRj4BY1Ai3miu4b9ibM3ssulzEaG14VJvCzQcp3-HZaPJEj7il1mep_q84QHpswnDBkMj33uSpOlweqnwWFXzG_4jAH8Jb6TXRlnW4XxPH4SsPDrHajn1N0BpNlHpWDecJ6LeRXSH6VHTPWup6BHE9Fu2XXUz_Fc485R7Lmt1OOSymyofxKyXOPlXCOngJ626B-OJ6hYE0Ft6VKu3jToHI_ibJ0bY5Tmb25uSuw1xXeDzdKhf7sNVxPyfnYAy7vg79dOWZ4AVovp5_O1pQL7SRTZG5s02l4i0SX3V1z-k1VryNH98yX0Slr5ycvx9r0G_CA_Wh_ZoTi7Ywq86wxt4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مستشار قائد الثورة والقائد السابق للحرس الثوري
اللواء رحيم صفوي:
في عام 1997، كان لدينا 2000 صاروخ، وفي ذلك الوقت، قال الإمام الخامنئي: "2000 صاروخ قليل، ويجب أن نصل إلى عشرات الآلاف من الصواريخ لتغطية عدة أشهر من الحرب." في هذه السنوات، اعتبر حرس الثورة الإسلامية كل نجاح بمثابة رد على الثقة التي تلقوها من قائدهم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82939" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
صدرت تعليمات استثنائية من سلطة المطارات الإسرائيلية إلى وحدة التحكم الجوي الإسرائيلية، تنص على "عدم السماح للطائرات التابعة لشركات الوقود الأمريكية بالهبوط في مطار بن غوريون".</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/82938" target="_blank">📅 13:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏شركة ستولت للناقلات: حريق بأحد ناقلاتنا أثناء إبحارها قبالة سلطنة عمان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82937" target="_blank">📅 13:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏شركة ستولت للناقلات: حريق بأحد ناقلاتنا أثناء إبحارها قبالة سلطنة عمان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82936" target="_blank">📅 13:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKGBmo5ztM4PZjg-pGezuyRCDnKS8ee_C5cyhA1S75aWJFWFUQy_sN93I5PLtrEk6f0JybXqQuuBCMAVh6to7fTneO_BShcNx0yWLQ2d9nNcQqf9pzKxUnTe_luDmmp1fo31tdvS6Zq157BTz99SazYhUqAdxRtvBkPE6Ik10j1gGVx54JscHFrzvqPZQkrIqUbF2AaFILVfvmEf8u1Io_lZFR99ZMlmm7ks6j4mwSIqs0jYyrJQPdD7ejsQcf8G2TWJk7h8eVPvGLJu0dtLbtgV199qznYkbqdXmDXNv-WvzEaYUhfPdBZiNik0t9E74Y6RLA09V3gzzvDL2cUfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTegcaUYzsZOM2MGndM8zP53FrZwCXOUEO3ZhQurqINnm2qQzGV95lbW9MbkA1_lM9W14yhOKdwif7SnXCYADgREwUpMTkohpjWgmTgpsqO4P773uAab4FvZgbPgBHFXon-9Tix_81m8QaaRA99MvCOj8ZeMQ6j_d5fYnb8Dy_FGev3KC_V-4Kp8FTqgDJFcjw_4r_Rg2AXvV9dSdZOgVkqi8XMSp5bRsmiufxYIBlnw-wT_djQ9FIKXb-mhDyKyRqP9p99gnbBziiCXLfEMljC0Vsi5CH4GzFtSvsatneFeCCHlkDNEwg_xbAOBF4bwJJ_fGpWa4l4ee0RENEiq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوي انفجارات في بوشهر جنوبي ايران</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82934" target="_blank">📅 13:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFJiz1Za9RENcCxGHQ0_7j6xzhjkz9VjJuq6OLb9NC5t5ysYjYVrVZ-iOLumqCnH4S6EsC1f8bgLGMqWmyFVHPgN-MPcBF_tyqs3Lc8mGzOFRZZMojBuUCyb0jmckKHzkUtqI8SOd9Fj_MuXBmOxEHut_uKeGns2QWMpf32Ja5P_1LpNzaLZsxNNLzp1WLl8pQ9LKdURMn7qNGxyHiaeMub4veBQa_7RKcTD-5w79RcxgWOgAE5XTzHOsh15V_Z-m11j3hvwqIkCfA6xuyVJWUVkwcEO_mONLvLVGT93lPmCF0ZC6qF5r2EL4N0-P30v7GVfCRZy7a0zfzJmeT80Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWi1oteFijPTH3hJJNNPuRLUZWJu9oTeS8Uszdc4TUwuk-Qo1OQfvyDi2x4g6I9loHB6IzfoqwrKEr6Yb3MnwgiqdL3moL85r7W56YJQXjMCySKZAPe8k_PDFthKtBLHnCUOCtCGh0_btGr2NPZtRMWtLql9mxHlu_zAwJ59FLRtVjVJbcX0XehKf_nW23hTSfW_VmAXbyXfWl1-0S987qwQnhP-VZYh4RFBaTFJPto_EEZpBxA7dh2Y9moT3jLgmjXIYTJKS-FDmeIQaUzrayE9J54M1OFzIER6AF6WVObxpxDcafU97VTXu0xfsK3Z_BjijO860nir5XZpIC_93Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة إلى الدول العربية مكتوبة على صاروخ "خيبرشكن" قبل الإطلاق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82932" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
رصد إطلاق صاروخ من منطقة وسط قطاع غزة باتجاه البحر.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82931" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوي انفجارات في بوشهر جنوبي ايران</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82930" target="_blank">📅 12:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
اعلام العدو الامريكي:
تفاصيل خطة ترامب بشأن الرسوم الجمركية في مضيق هرمز لا تزال قيد التوضيح لكن ترامب مصمم للغاية على تطبيق رسوم بنسبة 20٪ على حركة المرور عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82929" target="_blank">📅 12:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82928" target="_blank">📅 12:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uplB-wbGSBYeSbfIGsYkZUAJxrYf0T8KCcqJbidmiva8Yc9UqqMxdN1Ll3Ng7lVvTS9k1f9S_n4BFSfg0gz_lpZccDqgJXeECoTwcdUXOlPVRS_Ap4YH1ZiEKqf8C03NwBVfiMEJaTLB56U0J35xGxw3wlxBUK2StADKTbi6Rx8uXdkQDPTlbyhexvWDpQ2ESNobUaBteFxwWlOa3-bGeWJB9jo5WqTS-HObOj2lgfU9vI8pYJbDODSM2RQU35GUvcrE23NhG4h4oRYhGLY3IISbMpGmngLGmSRHc1PlqZHEMZ8ti3gatB4dcMQG0a66PGQ5gHIRpGeSPVDW9GHGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇬🇧
وزارة خارجية الجمهورية الاسلامية:
تُدين وزارة الخارجية الإجراءات العدائية للحكومة البريطانية في تصنيف "الحرس الثوري الإسلامي" باعتباره تهديدًا بموجب قانون الأمن القومي في البلاد، وتعتبره إجراءً غير مبرر وغير مسؤول، ومخالفًا للمبادئ والقواعد الأساسية للقانون الدولي، بما في ذلك مبدأ المساواة في السيادة بين الدول ومبدأ عدم التدخل في الشؤون الداخلية للدول.
"الحرس الثوري الإسلامي" هو جزء لا يتجزأ من القوات المسلحة الرسمية للجمهورية الإسلامية الإيرانية، وهو إلى جانب الجيش الإيراني مسؤول عن الدفاع عن وحدة الأراضي وسيادة الدولة والأمن القومي لإيران. إن بطولات "الحرس" في الحفاظ على كيان إيران وخدمة السلام والأمن في المنطقة وكرامة الإنسان، وخاصة في مواجهة الإرهاب الداعشي، واضحة للجميع.
إن تصنيف الحكومة البريطانية لمؤسسة رسمية في دولة مستقلة باعتبارها مؤسسة أمنية، هو إجراء مشين ومثير للفتنة وينتهك القانون الدولي وميثاق الأمم المتحدة. هذا القرار، وخاصة في ظل الظروف التي تشهدها منطقة غرب آسيا نتيجة لجرائم الولايات المتحدة والنظام الصهيوني القاتل للأطفال، يظهر مدى سوء نوايا وموافقة صانعي ومؤيدي هذا القرار.
بريطانيا، التي لديها تاريخ طويل من التدخل في الشؤون الداخلية للدول وسياسات استعمارية في جميع أنحاء العالم، وخاصة في منطقة غرب آسيا، وقد اعترفت الأمينة العامة لحلف الناتو بأنها كانت شريكة ومسؤولة عن العدوان الأمريكي-الصهيوني الأخير على إيران، لا تملك أي مكانة أخلاقية لتهمة الآخرين.
في حين أن الادعاءات الأمنية التي لا أساس لها تشكل أساس هذا القرار العدائي ضد إيران، فإن بريطانيا نفسها تستضيف وتدعم شبكات وجماعات إرهابية وعنيفة.
تؤكد الجمهورية الإسلامية الإيرانية، مع الحفاظ على جميع حقوقها بموجب ميثاق الأمم المتحدة والقانون الدولي، لحماية نفسها واتخاذ إجراءات مضادة ردًا على الإجراءات البريطانية الخاطئة، أن المسؤولية عن العواقب والنتائج السياسية والقانونية والدبلوماسية المدمرة لهذا القرار المناهض لإيران تقع على عاتق الحكومة البريطانية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82927" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزير الخارجية العماني: نتحمل مسؤولية للعمل مع ‌ إيران⁩ والمجتمع الدولي للتوصل لترتيب يضمن حرية الملاحة بمضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82926" target="_blank">📅 12:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزير الخارجية العماني:
نتحمل مسؤولية للعمل مع ‌ إيران⁩ والمجتمع الدولي للتوصل لترتيب يضمن حرية الملاحة بمضيق هرمز</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82925" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgeHzaAtbFMPoNNZrfOD9-Yqx5HUn3SHhWAtj0SOhktMHE0jmkV9ZHj2DCvcVE1zisKiFT46abERlSFaDW0FlN1sNXgpw5-qB-Z3LOXMVs_Wzw8qHyH18Yc7t0166pQZQ1HTX-iR8ghMSQdBBSEIQiwjbetS8hfLS_HAk6H9wLsw0E5_HmW5pkbX8rNjXsnFta7jRZub77VuDy29gW1WLzD4i2StXYweYMhCHs13ADipvB1q0NueUpJWqvCHYvTAeV7AN3wipynTlw5kCy4lWrvV1LQz7CLa06Qw-Nqv4fh5sl_WSjFFUPjuhvCbo5nfLb-m5q_YEHDh_XLUaaKskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت تتجاوز 86 دولاراً للبرميل لأول مرة منذ 12 حزيران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82924" target="_blank">📅 12:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الإمارات تُجبر على الإفراج عن 55 صيادًا إيرانيًا كانوا محتجزين لديها.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82923" target="_blank">📅 12:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
مشاهد اطلاقات صاروخية من الحرس الثوري صباح اليوم حول قواعد الاحتلال في بلدان الخليج.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82922" target="_blank">📅 12:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
عمليات بغداد تنوه لتفجير مسيطر عليه لمخلفات حربية اليوم ضمن مقتربات مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82921" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🌟
استشهاد 3 مواطنين من عائلة واحدة في محافظة هرمزغان الإيرانية جراء العدوان الغاشم الأمريكي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82920" target="_blank">📅 11:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjhk5JSa3vMNLaMPnUwdEMHUzUcpOZxVTLn88mknTLtHd8nxBo4PYYHmdNX71rky17-1gSVF-mf2soQAPNbGSC3GnSXEf9IfqJdBgZwHrt048aWwpo_5p4mqNcreKRB3RVGVWe1ic2qQSYL7KfYBo_SqDreRUWhYnqJV8A8NDfirWOAdTgs0aQWIh9k0GL_UbgjrDMjWhofLfPCZjEQEwsHVSfUW7666PNMERkaUcJgA_Aut1Kle9Ty_1nbxXNPCWb8sGSyTqJ4hPi70y5BZCMvfBH1n98ucP4o3zf5Sjsjcoi3eq5draR4Jos1fOGKpllJg26sBFtwcGqG26vmHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت تتجاوز 86 دولاراً للبرميل لأول مرة منذ 12 حزيران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82919" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
وزارة النفط الايرانية:
استمرار تصدير النفط الإيراني دون انقطاع على الرغم من إلغاء الإعفاءات الأمريكية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82918" target="_blank">📅 11:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlkvffGrq-4KSJ2CIYP0GeWcwcVAE4m3gtRCCQQOIINo53y5u2lUdY35tCjN1iwWK2IckatF99WGz5ZZpDVoQ8wexLslnKCLAvdr3xwL_7tAgw2EVWaFvxC4YzZNgQCwkGIRaei7AQqq_PHNoSrJZq1vaR7m4K7_XxxjopSbnNOxyG2ph7PfKgcY7PEFvot2RGYiOcSLOE6Eh6qZGu2kWfvk7rQUXSqbrzUqlg_RC4QwF4X_Ok8T8t-UxlAcXBTg25WE8y3W-opgZXKAUCAzSxbEOZnGtto3L1nJTc_hN5fXwFc-EMTGbV89FxmGpdcVyqZIgVYdcVug0MEPg9W75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
التجارة البريطانية:
استهداف ناقلة نفط بصاروخ عندة سواحل عمان اثناء محاولة عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82917" target="_blank">📅 10:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇨🇳
‏
الخارجية الصينية:
قلقون بشأن استئناف الصراع بين أميركا وإيران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82916" target="_blank">📅 10:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGASR3hA3tzzQoB3-S_AyZysQDWHNRSNUToYEYM2ugP_61UqF7ZVrifWsDBkznPNIviDbEIBD0qOL2Do9IhFAxiJesJHCkLS9QP0X6oeqFl97qbFtLu3WImzUJsDOmj6JRWADeA1E7LH8XLKjMpi4wYyOVlBKz0PIoavfc4FHTZ9DXmhuVkChSRzDzaPcUjkGpl9K1MbmKQaqD-P7tOjyCuRF_tH8S4vfQ0JuGt00DzcxIp5CNBdlAvuIXFtCIHsJGiQzRf1W0S3itPSPVquLj_CFOYzDTUqTIXz36EcakRt5oqAR53moHmSUWSYTpLeRfVeLGVzZ7zcrui_WkiDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aba1af594.mp4?token=A42o_9vOsXWamYfJTcd5Y3InxABO-NM2z_ldmiovnp4WRteoMqZw3vMkro5UWMk05YVstU_h0bv414SXXZWs3b4mWYEGDOWygekfqbgwjQ8x16nK0Pkb0eBTgKuNZ04egWA9Y7qmeGckT15p_8x5ZVLWxDle1-Lz7BG843fzH_nzU29Ti2bSyibjz-Jwt4ZMbYeBvZfXJaajvL1AjBBqyUc3RccgXkyx-m-oGM99az3qCw-RJQ9937j3vGCdlryuIpEkLXa4OK5ckZICQ1UJ6jWVrWnSBAQjCrwIALCptk_kiqrRW-PoSJWdzxDTjpRckijbe89dGFQWHC5dxmXc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aba1af594.mp4?token=A42o_9vOsXWamYfJTcd5Y3InxABO-NM2z_ldmiovnp4WRteoMqZw3vMkro5UWMk05YVstU_h0bv414SXXZWs3b4mWYEGDOWygekfqbgwjQ8x16nK0Pkb0eBTgKuNZ04egWA9Y7qmeGckT15p_8x5ZVLWxDle1-Lz7BG843fzH_nzU29Ti2bSyibjz-Jwt4ZMbYeBvZfXJaajvL1AjBBqyUc3RccgXkyx-m-oGM99az3qCw-RJQ9937j3vGCdlryuIpEkLXa4OK5ckZICQ1UJ6jWVrWnSBAQjCrwIALCptk_kiqrRW-PoSJWdzxDTjpRckijbe89dGFQWHC5dxmXc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
اندلاع حريق كبير داخل حاويات مرفأ بيروت بلبنان.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82914" target="_blank">📅 10:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9c004a63.mp4?token=Yapc7kwBqG0Err2VVYqIYCLhrzFL24h5kCxVU0kl3fkEBgs9libytGiaW_7ugejNMLKc04KxBrRWSZjJtVheYsrocBi0Iw6TsiTxD7a7dHUx8NJkxHldI4qd_1PYazjU6UyO5IuI0kXshlmrjYvd7Xa3qVnkg5BudI-6BGR2sGwaj2TeUgRq-xWaSFwru6QCFLCXFAbB4IgPakngaWHycdFnXRkjxM1o3ojzynEev16YfkYmnwiG9Qz8dYz-xAZ9nE7NQgdN9HRn6RfajfjPFNGA4qI1wrsxqDXBUNVSiP4xmHgq15oXH-hlAAhOwjF4Rcj6clqKgtydttTNT3qIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9c004a63.mp4?token=Yapc7kwBqG0Err2VVYqIYCLhrzFL24h5kCxVU0kl3fkEBgs9libytGiaW_7ugejNMLKc04KxBrRWSZjJtVheYsrocBi0Iw6TsiTxD7a7dHUx8NJkxHldI4qd_1PYazjU6UyO5IuI0kXshlmrjYvd7Xa3qVnkg5BudI-6BGR2sGwaj2TeUgRq-xWaSFwru6QCFLCXFAbB4IgPakngaWHycdFnXRkjxM1o3ojzynEev16YfkYmnwiG9Qz8dYz-xAZ9nE7NQgdN9HRn6RfajfjPFNGA4qI1wrsxqDXBUNVSiP4xmHgq15oXH-hlAAhOwjF4Rcj6clqKgtydttTNT3qIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرازيل لولا عن ترامب: قال ترامب في منشور إنه سيعيد فتح مضيق هرمز، ولكن على كل سفينة يسمح لها بالمرور عبر المضيق، يجب على صاحب النفط أن يدفع له 20٪.  ألم يكن هذا يُسمى قديماً قرصنة؟ كان يُسمى قرصنة.  يجب على دولة مهمة مثل الولايات المتحدة، التي بذلت…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82913" target="_blank">📅 10:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc63a69c5.mp4?token=Nwmbgmau2YGsYGNCtUk0cpgcDtb85HR4EQ4f_vX5GLBnLcZhQBMZ_ONykdXCvJanpgmma2rwak4CMNqu4xoNA0gmlBsuAjEElvfd91Ci1xIeA6teMBWYlc8PtAO9O-cJd1jTglC4oli6iammLoFUUS6UN0KosfUB5RLwTVsH-V7guofu9m_o5XTm4dHXrHSbAD_x6ADxxPiJ4SmGlCgLQVwwBtAjCn5jbxov1uh79cBoV2Ged7jbwxyWZtbdcg7boPVqjw6mLRJge3nl8qdcl77FMj2qc29VwLlvLo8ngLQpZztjAPSI-a3LS-CcIlqpb7UKtKigu3VM7A7jNs_hbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc63a69c5.mp4?token=Nwmbgmau2YGsYGNCtUk0cpgcDtb85HR4EQ4f_vX5GLBnLcZhQBMZ_ONykdXCvJanpgmma2rwak4CMNqu4xoNA0gmlBsuAjEElvfd91Ci1xIeA6teMBWYlc8PtAO9O-cJd1jTglC4oli6iammLoFUUS6UN0KosfUB5RLwTVsH-V7guofu9m_o5XTm4dHXrHSbAD_x6ADxxPiJ4SmGlCgLQVwwBtAjCn5jbxov1uh79cBoV2Ged7jbwxyWZtbdcg7boPVqjw6mLRJge3nl8qdcl77FMj2qc29VwLlvLo8ngLQpZztjAPSI-a3LS-CcIlqpb7UKtKigu3VM7A7jNs_hbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرازيل لولا عن ترامب:
قال ترامب في منشور إنه سيعيد فتح مضيق هرمز، ولكن على كل سفينة يسمح لها بالمرور عبر المضيق، يجب على صاحب النفط أن يدفع له 20٪.
ألم يكن هذا يُسمى قديماً قرصنة؟ كان يُسمى قرصنة.
يجب على دولة مهمة مثل الولايات المتحدة، التي بذلت جهودًا طوال الوقت لمكافحة القرصنة، ألا تصبح الآن دولة قرصنة. يجب ألا يفرض رسومًا على ذلك، لأن المضيق ليس من مسؤوليته.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82912" target="_blank">📅 10:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac97608a61.mp4?token=eAjeYfpBEu1NQDdwCscWORzrT3d4UvkLAPm1-C03Dlh6r-iePdod-AYFZ8DOSk55apHnDl6KOil_KmoOGcUTx7m6r0jtEEU7OhJKU58Tbz7pgJkzBLC2qFDCnaoNisbtXAlpZHHPq1PndFtXwOvXYxfMOIQjOdxWCeZE1PdaBo_6HuxpMAj7khngzcE5sfg5-6SPftoZeicQY2XjCCWFrxneo0G0gksLLTQY3zVfkUkb48LLvaweFKBZaGdOORBhJodDholFhqn_TTQXx9B-bfP-1tHb6jthzvEga7cJwhOa_NUeinRsmoyTYkDQA6xndR48Dqs-SnIYnlTTqV--2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac97608a61.mp4?token=eAjeYfpBEu1NQDdwCscWORzrT3d4UvkLAPm1-C03Dlh6r-iePdod-AYFZ8DOSk55apHnDl6KOil_KmoOGcUTx7m6r0jtEEU7OhJKU58Tbz7pgJkzBLC2qFDCnaoNisbtXAlpZHHPq1PndFtXwOvXYxfMOIQjOdxWCeZE1PdaBo_6HuxpMAj7khngzcE5sfg5-6SPftoZeicQY2XjCCWFrxneo0G0gksLLTQY3zVfkUkb48LLvaweFKBZaGdOORBhJodDholFhqn_TTQXx9B-bfP-1tHb6jthzvEga7cJwhOa_NUeinRsmoyTYkDQA6xndR48Dqs-SnIYnlTTqV--2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: من يتحكم في مضيق هرمز حاليًا؟ هل هو ملكنا؟ أم ملكهم؟ أم أنه محايد؟
ترامب: نعم، نحن نتحكم فيه. هم يمكن أن يثيروا المشاكل. يمكنهم فعل أشياء ليست جيدة، ولكن نحن نتحكم فيه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82911" target="_blank">📅 10:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
مصدر ايراني الانفجار الذي سيسمع في اصفهان وطهران ناتج عن تفجير ذخائر حرب مسيطر عليها.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82910" target="_blank">📅 10:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الهند تستدعي نائب السفير الإيراني بعد مقتل بحار هندي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82909" target="_blank">📅 09:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇱🇧
في وقتٍ تحاول فيه إسرائيل استباحة لبنان، وتسعى الولايات المتحدة إلى تعزيز وجودها العسكري فيه،
الرئيس اللبناني يدين الاعتداء على السعودية والاردن.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/82908" target="_blank">📅 09:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
رسالة مهمة من الحرس الثوري الإيراني للشعب الأردني: استهداف منصات مهمة ومواقع تواجد العدو الأمريكي في قاعدة جوية في الأردن بصواريخ باليستية. قسم العلاقات العامة للحرس الثوري الإيراني:  بسم الله قاصم الجبارين "قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/82907" target="_blank">📅 08:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇧🇭
انفجارات قوية تسمع دويها في البحرين.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82906" target="_blank">📅 08:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇧🇭
انفجارات قوية تسمع دويها في البحرين.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82905" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇧🇭
انفجارات قوية تسمع دويها في البحرين.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82904" target="_blank">📅 07:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الأردن تقرّ باستهداف قواعد أمريكية على أراضيه بأربعة صواريخ.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82903" target="_blank">📅 07:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
الحرس الثوري: تم تدمير رادار "باتريوت"، ورادار التحكم الجوي التابع للأسطول الخامس البحري للجيش الأمريكي، ونظام راداري إنذار مبكر من طراز "سي-رام".
أيها الشعب الإيراني المجاهد والواع؛
قام مقاتلو القوات البحرية والفضاء التابعة للحرس الثوري، في المرحلة الثانية من الموجة الثانية لعملية "نصر 2"، تحت شعار "يا لثارات الحسين عليه السلام"، ردًا على جرائم الجيش الأمريكي القاتل، بشن هجوم صاروخي وطائرات مسيرة على الأسطول الخامس البحري لـ "الشيطان الأكبر" في البحرين، مما أدى إلى اشتعال خزانات الوقود في هذا الأسطول، وإصابة وتدمير رادار "باتريوت"، ورادار التحكم الجوي التابع للأسطول، بالإضافة إلى نظام راداري إنذار مبكر من طراز "سي-رام".
في هذه المرحلة، تم تدمير مركز التحكم والمراقبة الخاص بالزوارق غير المأهولة بالكامل.
العمليات الردعية مستمرة.
"ولا النصر إلا من عند الله العزيز الحكيم".</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82902" target="_blank">📅 06:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEBA0GHylB9pIblt1ZtGbGqjiYlEdVQsIVJd7mqUFKIcKQhvbr7jnQlRJIuyi04_Cgl7yWaQgWZJdLtGsHcrFt2klSMCVi4DSkIFXpCdrHlt24Xc5We0XZZHXB2djIa7PXjmSbrODPOiy2iNKuy5x5luEDOZGrbVPyrU1rsBGtJdbHePobojcNt5Od6X4a0v67EdOOpa3BVg4w638_0BVGwKTT4-M9PwGjhM1zpYTfexvQl4MFuY4gIQlKXxKEj8cUGaz66VG7qIRWBVtpXQGlc5BZzHhAkygla3utn8Z0rEEIl395KoBL0x65mY0Wt-VnHXWsqZnAp655pTmfjzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
🇺🇸
يركز نشاط القوة الجوية الأمريكية بمساحة تمتد من منطقة السواحل المطلة من شيراز إلى أصفهان، تحاول من خلالها أمريكا تحييد النيران المباشرة ومراكز المراقبة المطلة على خليج فارس ومناطق النيران غير المباشرة "الدرونز، الكروز" باتجاه مضيق هرمز.
ومن المعروف أن طول مضيق هرمز هو ٣٠ كم، ويفقد ١٠ كم منها بالأراضي العمانية التي تعتبر مياه غير صالحة لمرور السفن بسبب العمق وعوامل أخرى كالتضاريس، فتكون بذلك المساحة هي ٢٠ كم فقط. وعلى سبيل المثال وليس الحصر، بندقية عيار ٢٣ ملم قادرة على تشكيل تهديد حقيقي على أي سفينة تمر بهرمز، فكيف إذا تحدثنا عن راجمة صواريخ أو أسلحة أخرى؟
الملاحظ أن الضربات جاءت بعد نشاط لطيران مراقبة وتجسس من طراز إواكس E3 Sentry، ناهيك أن حرس الثورة أعلن في بيان رسمي عن إسقاط مسيرة MQ9، مما يعني أن الأهداف يعتقد أنها منتخبة بعد عمليات ISR. كما أن الجيش الأمريكي طوال فترة التفاوض كان يجري عمليات استطلاع بمسيرات MQ4 للبحث عن بنك أهداف جديدة. جابهار؟ لماذا جابهار أو تشابهار؟ تابعونا لتحليل قادم!
🛰️
🔍
🇮🇷</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82901" target="_blank">📅 06:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82899">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_M819Kv6v7pj50cGMA_TNNBvJKNmpTSOdlUZhyx27JSmuGUx3M9ytIvrH0cDrzMu6bA7W9A2l-Ykj17ugchtlWb5cjwBcEhNaPpHNHn6NC1H4hqwIKoxz2vCALWCio9xZQjnUI3vtizq6Dzy8CqlU0jrYviC47_RHsG5PgKzj0_DDEqfaEK5JXKitKoVNNZMA5SmVIfWRaPGU-Jc1XFSYMHUq7hbDq7y55FCPkoOwxCdFVRtsduAIsDVfYvYJz-gP3sThCXiXSTn2snSzOSJG7LKqy3b5Cp9rWuy9gHzMjbo32wqz1ZIglWphwfl2Cs6Nt-q7Q8R-RLtr7duu2TNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPrQdDjD89yDjt0w5WbMPId-zB0YFOT_0RzhiTV6pYfEcVSE7OK5NshIielZqKo50u9Ah1X_wLh9vrVd-Ha9aedTJ_xA8FsnFnPILysnu5DunrZbr2NMUU5fjKK3r2OiL47UTVgYC05mkM89ICc5bEQpqg4tKaMsaHh8fTTyF1IkSVnR4EqWFPP51vETZmAO41uW5f6-RfA5euI5iJGyQfbx1G7go_S_h3sCGf2iRYvKpO_YzDhw5qlcHisKaulai-iIZcUJXTrRKJSpGXJ2IQr21ey438OKKfknNbH0MlYADeWVYwVcEkwd__1GhdbnR4G6WfGDq9DZBhjAFPCjoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الناتو ليس بريء بما يجري على إيران‏..
طائرتان أخريان من طراز إيرباص A330 MRTT تابعتان لحلف الناتو، وتشغلهما القوات الجوية الملكية الهولندية، في طريقهما من أيندهوفن إلى مسقط، عمان، عبر الغردقة.
‏يأتي هذا بعد وصول طائرتين أخرتين من طراز MRTT تابعتين لحلف الناتو إلى عُمان قبل يومين</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82899" target="_blank">📅 06:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3938ea72a2.mp4?token=idvfA3zKZPIipSGefh8nobjIbyyRsutk0FgpuBgL-rjuWeDczAXWsY2kV8o1re-MXLzBHa8SSp02eloRnPk6KRv_PGVD__VU1cp6TnStH6e3JcHAEvg65S9KxbkAxpe3NqT5XaHQC42bN2kJvBuZJJztizWAgsxhuzMKUjZWNCFTzXeEAdVuhzpMvrYp-6TMSMEnYby_9GLM1RXUKQ-RwbXvWPs6cR7uTNfIrTFjU50w4E6QyBDcqUblYYBol83POFkRTaqexbw6W-LnQRCWIfK80QgNmgAXQ9IuqXGIX81kHM8A657l1453xK8pGskNHoQK8VrRgo-qlXxuc9F_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3938ea72a2.mp4?token=idvfA3zKZPIipSGefh8nobjIbyyRsutk0FgpuBgL-rjuWeDczAXWsY2kV8o1re-MXLzBHa8SSp02eloRnPk6KRv_PGVD__VU1cp6TnStH6e3JcHAEvg65S9KxbkAxpe3NqT5XaHQC42bN2kJvBuZJJztizWAgsxhuzMKUjZWNCFTzXeEAdVuhzpMvrYp-6TMSMEnYby_9GLM1RXUKQ-RwbXvWPs6cR7uTNfIrTFjU50w4E6QyBDcqUblYYBol83POFkRTaqexbw6W-LnQRCWIfK80QgNmgAXQ9IuqXGIX81kHM8A657l1453xK8pGskNHoQK8VrRgo-qlXxuc9F_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
أكملت القيادة المركزية الأمريكية (CENTCOM) أحدث موجة من الضربات ضد إيران في الساعة 10:15 مساءً بتوقيت شرق الولايات المتحدة، يوم 13 يوليو.
خلال هذه المهمة التي استمرت خمس ساعات، نجحت القوات الأمريكية في استهداف أهداف عسكرية في أنحاء مختلفة من إيران، بما في ذلك بوشهر، وشاه بهار، وجاسك، وكُنارَك، وأبو موسى، وبندر عباس، بهدف إضعاف قدرة إيران على مهاجمة السفن التجارية. استخدمت قوات القيادة المركزية الأمريكية ذخائر دقيقة ضد أنظمة الدفاع الساحلية الإيرانية، ومواقع الصواريخ والطائرات بدون طيار، والقدرات البحرية.
يوجد حاليًا أكثر من 50 ألف جندي أمريكي منتشرين في جميع أنحاء الشرق الأوسط. تظل القوات الأمريكية يقظة وقادرة على إحداث ضرر وجاهزة.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82898" target="_blank">📅 05:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عدوان أمريكي يطال مدينة جغادك في بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82897" target="_blank">📅 05:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عدوان أمريكي يطال مدينة جغادك في بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82896" target="_blank">📅 05:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هجوم صاروخي إيراني جديد وإنفجارات عنيفة تهز البحرين.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82895" target="_blank">📅 05:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
في المرحلة الأولى من الرد على عدوان العدو، استهدف مقاتلو القوة البحرية التابعة للحرس الثوري، في الموجة الثانية من عملية "النصر 2"، تحت شعار "يا لثارات الحسين"، عدة مخازن للدعم اللوجستي للأسلحة، ومركز اتصالات عبر الأقمار الصناعية، ومبنى إقامة قوات أمريكية في قاعدة "جفير" في البحرين، مستخدمين الصواريخ والطائرات المسيرة لتدميرها.
العمليات الردية مستمرة.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/82894" target="_blank">📅 05:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات في مدينة بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82893" target="_blank">📅 05:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974be2116e.mp4?token=uXPFMdi6ZmjCgHu05kJhVecd_WAopyY0IUNTewhqIwMND9oVOIkCy6bIfHB5gEjvHDZ6MKmfkdOhWd3wi2lMnrpiPf9Y83DjYUOFey8TmVnc_tdqUVXNdR8FUFa4JsmWBnM3F0DhvmZOUbOxr2IlPs94MuGMEs81UVbNFl27Uo9qNT4sNYlvBDscAI-WqHO4xgHTzAg2w5vlLGgG8-eBSRytt6QjRvyyQ-Vs5r6HiWAePIpg38j-DaS6udSvmCV4cbumKUA7ZXdRKBHt3SwRIUw6Kk30iEkmU7AWfmqR6AXKEIUZxnIUBqG7hw1Lg-YhK3_8i1bHqhNtHU_I1z0UOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974be2116e.mp4?token=uXPFMdi6ZmjCgHu05kJhVecd_WAopyY0IUNTewhqIwMND9oVOIkCy6bIfHB5gEjvHDZ6MKmfkdOhWd3wi2lMnrpiPf9Y83DjYUOFey8TmVnc_tdqUVXNdR8FUFa4JsmWBnM3F0DhvmZOUbOxr2IlPs94MuGMEs81UVbNFl27Uo9qNT4sNYlvBDscAI-WqHO4xgHTzAg2w5vlLGgG8-eBSRytt6QjRvyyQ-Vs5r6HiWAePIpg38j-DaS6udSvmCV4cbumKUA7ZXdRKBHt3SwRIUw6Kk30iEkmU7AWfmqR6AXKEIUZxnIUBqG7hw1Lg-YhK3_8i1bHqhNtHU_I1z0UOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب عن موت ليندسي غراهام:
لقد عاد للتو [من أوكرانيا]. سألته: "كيف حالك؟" فأجاب: "حسنًا، أنا بخير، لكنني متعب."
وبعد فترة قصيرة من تلك المكالمة، رحل.
إنه أمر مدهش حقًا
.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82892" target="_blank">📅 05:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56952ca04f.mp4?token=e7CuX2jAA5L44wg4UilCGf8E9VWbCbM5kgWjEuH2TFjVOOjdOx71Tb3ElPvJguoezBf7EJAK27X45Xms5zLVwAuvW2yzRX_ycLjaoYOCfDxNvcgXOEJ3lQpmuGj8N0MgPDMiesfgBPWa8sLTQMUzqSMgQDZouE2OItRwBBcsiXH7EP18O3zqdKfhVvFB4_14HnKhpYq5OWRaSyxkQKaa0khdGgKZWElIi0P6krbwRV10U1c7VLMpzxO2nqWZi7AFyzyp27GXN9DEOUEovK5dEhr4cdnvIg0xf62ZmyRT217D9QJfw0G2Ky76xFSReJTHRAHP99EFfwmOqkD_3rO0A4EQwC9ZDza5HkQ-ENfR3rSOqREZvpQYDKdRuAsn-as-N5KwsclwUHwJqC8Lu2daM_hR5rzWhj4yV-sdUrppybhIY7Nnww_O45zh99Izx78rEli91zRJH49LT96Qf98kdX2IrSVoxXtKdorSDJuisKkbc87kIbj6Uzt9-7cx1lwh7Bi_c1oRJIQYnaz6SvAn7bxN37uWU8t1ZIz2QNerYLxtEwXyQ152mCaE3BrkVhlbmhIibwAB-g__NIN-ReZARBr_yNu6qvddEjmk-dw_q73ZtEUQfJ_ducdAoB4x9X-nSuMNKwG3ZRY6JJM2t0p1Nuo91H7BLwqgdlKIyX-VRMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56952ca04f.mp4?token=e7CuX2jAA5L44wg4UilCGf8E9VWbCbM5kgWjEuH2TFjVOOjdOx71Tb3ElPvJguoezBf7EJAK27X45Xms5zLVwAuvW2yzRX_ycLjaoYOCfDxNvcgXOEJ3lQpmuGj8N0MgPDMiesfgBPWa8sLTQMUzqSMgQDZouE2OItRwBBcsiXH7EP18O3zqdKfhVvFB4_14HnKhpYq5OWRaSyxkQKaa0khdGgKZWElIi0P6krbwRV10U1c7VLMpzxO2nqWZi7AFyzyp27GXN9DEOUEovK5dEhr4cdnvIg0xf62ZmyRT217D9QJfw0G2Ky76xFSReJTHRAHP99EFfwmOqkD_3rO0A4EQwC9ZDza5HkQ-ENfR3rSOqREZvpQYDKdRuAsn-as-N5KwsclwUHwJqC8Lu2daM_hR5rzWhj4yV-sdUrppybhIY7Nnww_O45zh99Izx78rEli91zRJH49LT96Qf98kdX2IrSVoxXtKdorSDJuisKkbc87kIbj6Uzt9-7cx1lwh7Bi_c1oRJIQYnaz6SvAn7bxN37uWU8t1ZIz2QNerYLxtEwXyQ152mCaE3BrkVhlbmhIibwAB-g__NIN-ReZARBr_yNu6qvddEjmk-dw_q73ZtEUQfJ_ducdAoB4x9X-nSuMNKwG3ZRY6JJM2t0p1Nuo91H7BLwqgdlKIyX-VRMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
السيناتور الأمريكي "روجر مارشال":
أنا أؤيد استئناف القصف على إيران، لكنني أُعرب عن حزني على "
مئات الجنود
" الذين فقدناهم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/82891" target="_blank">📅 04:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
ترامب:
من الممكن أن تثير إيران المتاعب وأن تقدم على أمور غير لائقة لكننا نسيطر على الوضع</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82890" target="_blank">📅 04:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
قبل ساعات، حاولت القوات الأمريكية، التي لم تتعلّم من الهزائم المتكررة، وتحريضًا منها للسفن، إجبار عدد منها على عبور مسار غير قانوني. سفينتان نفطيتان مخالفتا وقعتا ضحية خداع أمريكا، وعندما أطفأتا أنظمة الملاحة وتجاهلتا التحذيرات المتكررة من مركز التحكم الأمني لمضيق هرمز، أقدمتا على تعريض حركة الملاحة في هذا المسار للخطر، وفضّلتا العبور عبر مسار مُنَمَّن، فتعرضتا للقصف وتوقفتا عن العمل.
القوة البحرية لحرس الثورة تعلن للجميع أن التعاون مع العدو المعتدي القادم من مسافة آلاف الكيلومترات لانتهاك حقوق أهل المنطقة، وأن العبور عبر المسار المنَمَّن لا يؤدي إلا إلى الندم والخسائر والتأخير في إعادة فتح مضيق هرمز، وخلق أزمة طاقة في العالم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82889" target="_blank">📅 04:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usKYlhdW1ktce_rnJASj2CMfl_c4O21YsSzDSdrlFOxlPkR3uvFQd2a3yIwusunoITnzntW6YXeF1h-nY5KtQGqRZBri7p4g3cvXt9DYV3w4tinDiUbEtpf9wM7EqWjwYvSU4YQhW8mpuZbrxIFIt9YPHQXiSRDxT5186yWWbjpb0vqmNpwiR0lYDH5wVqeduyWtkQIW7MLlUCiuKMiiB5GcgEBZTY3fjFEhi4eKrNMAiCNSVYtSGvMeAx0sKEnxa08XV5SaSgMxsIRBF7gQzPMa7uZSTtfwv6_154FEkiXBSfS0EOdj8WVvjzarjVUszrFM0fU4QObK9Z7fD4YHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E74Fy_VMDBCsFpHViwVS4zkjpI5ENhLxlmj6Xom05USh16d-kT4F733m5EhZPsqeqKszVIxpnRNw0da1Sbhg-nnizzxU-32bDNDWf1YZaNU5NBsB5-jTpuloUWge6V36tNTiqdnkTX9f8oof-Wi4UXVRo3g7AknWhev7iD_rErWKKI_bmozM5cwnCMMBi9luYwRU0WHhD95zC0HjJk10i-zERXMocJv1XukqmZcjit1JeCET8IBDB9fgLscsRe8rlvCUp4_qSyM2qr1D1Pop_GZsRHL1rEjStRD-iYrDSw2hnMcG65mNXVUa3Vcsqaxpe_BOl-3b1MAzwW-qMd6Vvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إطلاق موجة صاروخية من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82887" target="_blank">📅 04:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82886" target="_blank">📅 04:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82885">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82885" target="_blank">📅 04:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6RLKkuTYWYkXF7533mFW3rXHqik5lmOqho4ekAailaxg9nUh7Pj8IQhSBqdsl3jaT94OUbcpJqpDGXrFroUAuzaSmwDbTvw8czwVNx9nljF9bavVVlzHjKErKk6xU6AS4utBlch5NAUCVIxz4x4pfW_YYCRh8uIKgGTxtG_nU-QxDoEi_eTQv_WAY0F6X-y1CIB_KTPuPb7o8pu1dR2xD3hGJoJSXOPrbdPPnT1p9I5ctCT7d_xG3xRY_PSWbT4Zu8yiWcXf73ZC0TiqP_JPHkuLc1rkX0dxNSD_kj4l8HJI0IL4gB2btfUIUdi5KGBkNmyGOu4-uH1w8coQK0_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تتجاوز 83 للبرميل الواحد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82883" target="_blank">📅 03:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb90d7f52.mp4?token=H3McOfAHQCch1SqmuIO3rb_-mlyUUwL7LnKbR7XSZt_a5AUH1gFsy49LT1HUFwRhqc-ILu5dxvO7NG7vwOH6UqV6kw86vai7eu5wY8-19q9BrCfmhNt_H6RN05hHLwr-CrAWfqFpLKtFe6Ut1lECBEpEjnz1rd9ojP7awYsC-GFHuwJMNDughS3aNXzNnhGTDk2yxmKpTV9OYboOag4fwsDYAiKYBrE-QUhmieLX0x2UmCqwqrps67YbfVEZhwDf_iOsxLigs5ipC4nDJ-pYlS-hKmdF_OZxiq71DCmTfOMNI5_sPX1bnPwL5G5sA-B-rV20BiLDxpprKpxYth0Nrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb90d7f52.mp4?token=H3McOfAHQCch1SqmuIO3rb_-mlyUUwL7LnKbR7XSZt_a5AUH1gFsy49LT1HUFwRhqc-ILu5dxvO7NG7vwOH6UqV6kw86vai7eu5wY8-19q9BrCfmhNt_H6RN05hHLwr-CrAWfqFpLKtFe6Ut1lECBEpEjnz1rd9ojP7awYsC-GFHuwJMNDughS3aNXzNnhGTDk2yxmKpTV9OYboOag4fwsDYAiKYBrE-QUhmieLX0x2UmCqwqrps67YbfVEZhwDf_iOsxLigs5ipC4nDJ-pYlS-hKmdF_OZxiq71DCmTfOMNI5_sPX1bnPwL5G5sA-B-rV20BiLDxpprKpxYth0Nrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أثار العدوان الأمريكي على مدينة سراوان جنوب شرق إيران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/82882" target="_blank">📅 03:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات جديدة تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82881" target="_blank">📅 03:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7404b32d.mp4?token=ZOW9v760bEa9V2roi1s3CntyU88Aw1k_t64RcdjoAy9_5ulm1Jfgk2iOOazgSydxIzn9VGhF637DEK9wHG88LTDPE88t3TQrV6amj8Rl5y9IBT109vtex5_K3P0_HcpRqV5fx6MTbc6hrCFbQX_ijVMe8cQcSilBxkmsT5wwqpy72eOZ1Snmd9NqVJ_5pvU_NE4Ub-V7a6NWtlcDB6F8u_bTHcFGBHeL4qKFluerywnBfkVmzxci9p8yCkYZSQ-tz7ltUkMBQgdupyBsaxkXSDKEftuP12MIi4OzGnABdRuN4stixiTNHx_6UYCuBDWCb4A0HrxGtpp7hJFYIYiZPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7404b32d.mp4?token=ZOW9v760bEa9V2roi1s3CntyU88Aw1k_t64RcdjoAy9_5ulm1Jfgk2iOOazgSydxIzn9VGhF637DEK9wHG88LTDPE88t3TQrV6amj8Rl5y9IBT109vtex5_K3P0_HcpRqV5fx6MTbc6hrCFbQX_ijVMe8cQcSilBxkmsT5wwqpy72eOZ1Snmd9NqVJ_5pvU_NE4Ub-V7a6NWtlcDB6F8u_bTHcFGBHeL4qKFluerywnBfkVmzxci9p8yCkYZSQ-tz7ltUkMBQgdupyBsaxkXSDKEftuP12MIi4OzGnABdRuN4stixiTNHx_6UYCuBDWCb4A0HrxGtpp7hJFYIYiZPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أثار العدوان الأمريكي على مدينة سراوان جنوب شرق إيران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/82880" target="_blank">📅 03:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
تعطل الأنظمة المصرفية في البحرين وسط أنباء عن هجوم سيبراني.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82879" target="_blank">📅 03:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/82878" target="_blank">📅 03:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkWCyBSe92NOv0fesNkScv6cdobBg0lFkeOmc2MWj7A6C2NrqbQ67KrH9GTV6-P56PvFSvV5ozduX9EiazhYNR7uegnffoWU6Nn_AWNoYsNEt43qqOQj_61vPfno4cRSlg2T_8uvl8f4uK0oLNh8wjzDxmTawUzEh6oqlZX10_jJmU0GS19MrJtbGcXg55CLDRweoIt7UzTR_XPednE9OCo2Tn1IQZCWIQ4k5SpWVsj9syvPYkoDl2neOxEXPwWimuz2i1mTOafblseRk5ZDnEnSfe6tZ6awVj6a2R-UJIhVe9aYfQFeVzNFWBmp2_2f2pa5EPDAbjICISjPIGDWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82877" target="_blank">📅 03:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82876" target="_blank">📅 03:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوي انفجارات في مدينتي ماهشهر وبندر امام خميني (سربندر) بمحافظة خوزستان جنوبي إيران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82875" target="_blank">📅 03:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/82874" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هجوم صاروخي إيراني وانفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/82873" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هجوم صاروخي إيراني وانفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/82872" target="_blank">📅 03:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e9569807.mp4?token=CPDfDnQeOLztP5xfLp6diI4Jd_a_eSDJIe_Myfy28C8x9jyJal4WEoLkq99rJsjz7GZWguVrAJ6C2Ji9G0mbvlNALL4lsjYi00_ubDwc2fChZvYpQzt9rk0R_3gVHhjf9Nm-mvrR1P4XBaEHHg5niAsJ2CQ9vVZmYbIlyGHcAt4zfUkbQyAfO90w32KmxA3yNMtEnUp-7l4KkqbmkfeAVtaQdHG1guI8OrXfFX21DQ8TTXkxct3MEqf1mAZNwN1xxcZy3LFj7598qFp0nRpqVV72AmpKXDIYB5x0v51ykZPwEQ3KKpBsyRwlItO4VXXuC4EuVe0fZnmxsMchXvxbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e9569807.mp4?token=CPDfDnQeOLztP5xfLp6diI4Jd_a_eSDJIe_Myfy28C8x9jyJal4WEoLkq99rJsjz7GZWguVrAJ6C2Ji9G0mbvlNALL4lsjYi00_ubDwc2fChZvYpQzt9rk0R_3gVHhjf9Nm-mvrR1P4XBaEHHg5niAsJ2CQ9vVZmYbIlyGHcAt4zfUkbQyAfO90w32KmxA3yNMtEnUp-7l4KkqbmkfeAVtaQdHG1guI8OrXfFX21DQ8TTXkxct3MEqf1mAZNwN1xxcZy3LFj7598qFp0nRpqVV72AmpKXDIYB5x0v51ykZPwEQ3KKpBsyRwlItO4VXXuC4EuVe0fZnmxsMchXvxbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي استهدف مدينة سراوان ضمن محافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82870" target="_blank">📅 03:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5498fd1ddc.mp4?token=mbMVeLQBUS2N10nMnZX_DIsA4NrxjgD1gItQ1L3LXwTsz1n-M0R2vza8vn4g1GVtXPO9-0wIrAIByr1BTA5LUNbTc2VE6ijkVVb_mAGmXbgwpDeI5C_o_jtYEY7G0BnBmBiKgakg20S_0fuKW1y_k7S7PP8l4lqjWw6j3fF2iS_rsFzwXGeNmxkF5SKtbNIclqOidFfxv4jZsSWaI1b-c6bJb3IfxrfS6iIC1NqL-DqGkZ_Col0Sodtc_TU1QMRYqxKQsqVVj5Yv1MklUkMY9DfBB-KGG8KUnFMUaauz0RoRaa-7zYHnRqLXsrUgNMipU6i0Sgo4IF0QorrVXcfXkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5498fd1ddc.mp4?token=mbMVeLQBUS2N10nMnZX_DIsA4NrxjgD1gItQ1L3LXwTsz1n-M0R2vza8vn4g1GVtXPO9-0wIrAIByr1BTA5LUNbTc2VE6ijkVVb_mAGmXbgwpDeI5C_o_jtYEY7G0BnBmBiKgakg20S_0fuKW1y_k7S7PP8l4lqjWw6j3fF2iS_rsFzwXGeNmxkF5SKtbNIclqOidFfxv4jZsSWaI1b-c6bJb3IfxrfS6iIC1NqL-DqGkZ_Col0Sodtc_TU1QMRYqxKQsqVVj5Yv1MklUkMY9DfBB-KGG8KUnFMUaauz0RoRaa-7zYHnRqLXsrUgNMipU6i0Sgo4IF0QorrVXcfXkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغاشم الذي طال جزيرة كيش الإيرانية.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/82869" target="_blank">📅 02:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭐️
اكسيوس:
دعم الرئيس الأمريكي دونالد ترامب ولي العهد السعودي الأمير محمد بن سلمان قبل أن تشن السعودية ضربات على أهداف تابعة للحوثيين في اليمن.
جاءت هذه الضربات في أعقاب مخاوف سعودية من أن طائرة إيرانية كانت تنقل على ما يبدو أسلحة وموظفين عسكريين إلى الحوثيين، واستهدفت مطار صنعاء.
رد الحوثيون بإطلاق صواريخ وطائرات مسيرة استهدفت السعودية.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82867" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8r0xMt_QGgeemZ88xmaky6msrZn5b5tNKJukM3pDepIfS-a0m2DLGGCpbBf84PxHtskjh0aO8gLiExq7cxdUSzSTHVkQMkSADtVOd85Id0R9I5-NfyLg0B7U0DbcXZemDfWkBLG50ejZf8D-8PS6DvReZrITLlctqG0V0C7OzF9eJ4yriDKR4cP5KmkRHLJUv1GoIlYWM9RAxCHVanrSyycAWL68gTCKcb2tUPm4Sa4pp5aLbPeRU5uSgG5PBAaWJx2NCcWNBwnaYsu_7YttIe4_FcdtyGpJbnWs5Bse-5n3FNIP-uwcoMae26XqMMAPkIEnpfhkE_dM5HrBvjcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تتجاوز 83 للبرميل الواحد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/82866" target="_blank">📅 02:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سربازان آقا سید مجتبی با کسی سر شوخی ندارند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/82865" target="_blank">📅 02:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
شیرمردان سرزمین فارس پایگاه‌‌های آمریکا و منافع آنها در منطقه را به آتش خواهند کشید.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/82864" target="_blank">📅 02:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
شیرمردان سرزمین فارس پایگاه‌‌های آمریکا و منافع آنها در منطقه را به آتش خواهند کشید.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/82863" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/82862" target="_blank">📅 02:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/82861" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوي انفجارات في أبو ظبي.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/82860" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/82859" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82858" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma_1f3PcfSx23x10TkcWWfLhfBEVgVIxkBv_mxP5C7pVksAuAi2kMVWh6bANGILsCci3A8TCjE88aJSEu0Ql4H7zScJCWL-8HgURvFy4spqPuk6Z_2vaVpi_XkOMJocBCQIKR6kigwGTu58HDoyzV7fG_KU_3HF-mxKh8bzcmPz88UHmYK2w4Fy_roIeAfoo87oyClpffwsIQNZDuE6QvBu-eHXGTeBUQRAMuzMfAawDIsj3wAM5gKEWIGEeUJ44UhM8z6PbYV5TbGEWEcs9p1BsvGopxWvCn__luRoAQQsig_SH3YakvXK0tK0guYPzNZda6icERtYlHG4FzQ1rJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب عن إيران: لقد دمرنا معظم صواريخهم، ومعظم طائراتهم بدون طيار.  لقد دمرنا قدراتهم في تصنيع الطائرات بدون طيار: بنسبة تزيد عن 92%.  لقد دمرنا قدراتهم في تصنيع الصواريخ: بنسبة 89%.  لديهم بعض القدرات، ولكنهم لا يمتلكون أي قدرات تشكل تهديدًا لنا. هذا أشبه…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/82857" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارة الدفاع الإماراتية:  تعرض الناقلتين الوطنيتين (ممباسا) و (الباهية) للاستهداف بصاروخين جوالين إيرانيين في الممر الجنوبي لمضيق هرمز بالمياه الإقليمية العمانية.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82856" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/82855" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
