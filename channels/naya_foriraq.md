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
<img src="https://cdn4.telesco.pe/file/PGqyEqUtd610dwLFnQxhjIAX8EZDXSSnPsmic5sQp4kiXpSxBFjnoLFjOZna8MCyfIlIijoEg8AMlvqfBAGLBwD-WedCcKluuXbRpS1-IpWmAD04ONSs3wfoKYwLntoqxOqOg1rGbMZj6FqWoppj-w7VryBayZSoSN9NV4YtYbmtCJnbweab0h6ZVDmf-ZTnCKzciRV5cn9xpa4GtaXlMWNP1HWjwhdxXMna5gjLinBLcHQR0Q4RHHWXzgSmD-wtBfTzesCGUeLZDKb8olSrl0iX4sRVdypmLYKgxsrFji2MOw4b9DXMDRyvnbnG622dV3PtoQVyaTbhdgfkWILkJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
قوة من الحشد الشعبي تفكك عبوة ناسفة كانت موضوعة على طريق حديثة – بيجي في محافظة الأنبار غربي العراق.</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/naya_foriraq/77932" target="_blank">📅 19:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRb9wx5wOwyDymiawLN4A7m_9DA04RbGKWl9t0Ds8Kxbg3FIagf0izw-wcNYWAvxp-iySQzwDLgBqz4JoNJ5qPvtCTs4BmF7g7Qfqpng55dH5jTZN_IL0K1YyqksSotEMi8XsHzgH0VsYUdv_U9nLi16eo64Xu33lS-dOeZIad0GK3AwKvzi9uyGONch096jWi-Np5wdU2tVvhn9bjBah88Q0avINLMaXYxn3ynS5m-FpnOmCr8qUKJeCI_O-9mkuHRrTZPsUV7_71PJWu-oiZS6oz9SDTvUvRkRBx5jbO1sTUycdbBwgZ5kui1ec7QzjCqSN6D3cfNoFCX3cQx3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات صهيونية على مرتفعات الريحان بجنوب لبنان.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/naya_foriraq/77931" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمع دويها في مدينة أصفهان الإيرانية ناتجة عن تفجير ذخائر غير منفخرة ولايوجد حدث أمني.</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/77930" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
إندلاع حريق بوزارة الصحة العراقية في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77929" target="_blank">📅 18:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة صلاح الدين توجه بتعطيل الدوام الرسمي يوم الخميس 11 حزيران 2026 استعداداً لإحياء ذكرى جريمة سبايكر.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/77928" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0AkWfO_Wgjz97fwNo9USwPJAOKTsFAN1K_WRXtx7F-zAmaDqym_xm_5VH0ib92-TZ3MPhiNDf-GmKWHtqdVj3aoXDsg9WCt1c0rwPQxB0Lh_hfuse4t6K1E9QVeG820l9HSE4snTywQu9nMmATujyohHveT9TnJQsq-2JAPWFYjZbMNfxvgWKQDLZYQGOye4sLH8znqHgqY2LsZqWlpWanDTjniHy2eQILwIz5bOzS7nfOtmY2t9eXG8GcM5ZSyzgUL0bCr9Bkoz3e3u9EamR-fU3GIyIP7CyGM4i7e9N_d1mZVqyl3iKlgja2coLqgX9qxN4um0dIbCGi021bsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب الله يستهدف قوة الإخلاء بصليات صاروخية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77927" target="_blank">📅 18:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مجلس محافظة النجف الاشرف يصوت على توصيات لفتح منفذ بري مع السعودية من بينها احالة المنفذ الى الاستثمار!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77926" target="_blank">📅 17:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏴‍☠️
‏
رئيس الأركان الإسرائيلي
: الضربة التي نفذناها في إيران كانت تمهيداً لضربة أشد وأوسع بكثير</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77925" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة مرجليوت إيتان ديفيدي:
كان يجب أن تحترق الضاحية الجنوبية في بيروت، إذا لم يتم الرد بشدة على التسلل الارهابي إلى أراضي إسرائيل، فمن المحتمل أننا فعلاً مواطنون من الدرجة الثانية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77924" target="_blank">📅 17:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اعلام العدو: حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77923" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعلام العدو:
حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77922" target="_blank">📅 17:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث سير جديد على طريق (الحمزة - ديوانية) في محافظة الديوانية جنوبي العراق يسفر عن وفاة 4 اشخاص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77921" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
إصابة 48 ضابطا وجنديا في معارك جنوبي لبنان خلال الأيام الـ5 الماضية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77920" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
بعد تحقيق أولي - تفاصيل إضافية عن حادثة تسلل المهاجم إلى أراضي
إسرائيل
في منطقة سلسلة جبال راميم
1. خلال نشاط لقوات جيش الدفاع داخل جنوب لبنان - رصدت القوات إطلاق نار تجاههم. تم إطلاق النار على القوات التي كانت تعمل داخل لبنان، وتبادل إطلاق النار جرى مباشرة على سياج الحدود.
2. بعد أن قضت القوات على المهاجم وفحصت المنطقة، تم العثور على جثة المهاجم في الجيب الإسرائيلي خلف سياج الحدود. أي: رسميًا تسلل المهاجم إلى داخل أراضي إسرائيل - ولكن حسب المعلومات المتوفرة، لم يخترق سياج النظام ولم يدخل إلى المنطقة المدنية. الجيب خلف سياج الحدود هو بالطبع منطقة عسكرية.
3. كان المهاجم الذي عُثر على جثته يرتدي زيًا عسكريًا لحزب الله، وتم العثور على سلاح وسكين بحوزته.
4. في هذه المرحلة لم يتم العثور على أي أدلة إضافية. الفحوصات مستمرة - باستخدام طائرات بدون طيار من الجو، وقوات خاصة وقوات مشاة في الميدان، ولكن حتى الآن لم يتم العثور على شيء</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77919" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📰
أكسيوس عن مسؤولين أمريكيين:
نحقق لمعرفة إن كان إطلاق نار إيراني تسبب بسقوط مروحية أباتشي قرب مضيق هرمز الاثنين.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77918" target="_blank">📅 17:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/77917" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCRfIno8ELcg8Lk4aFNDw2YDKYcL-fk66N6F5FLsOmxHmmpxp7NicI2oGe9jFhTKuNYZ7mq1HKQ1LOt8jz7ahSD60izrs1mVYt1DtYcR7s4ltemOhKh32tmRWiWHO11zahldGwhDZKOXZp4i_mTX9p9lvgzTSf1Y_x3o4z3aG2593s1L3AOifSvlEBeqH3JScpJtPUtMlIXkgq1Hh4xx-hZqgHOGOI3kUPjhkzklbWt4iJTI4IO88pSwFzKwCdmuCAj4_SNxaqOs_qtcatY56VW-Xi29YIu0HP2k42tUvmR2uy18Ciy9DtKaCOi1YrKgT2qFbEpZfsx-abmXUzvhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNOYcDOweqITnY7s0QSTgKlhGLzY7M0cEmbPlEB9RDqCQmlh7-nbiCSUAjTYXZSIUk_JD156sDVMI4E5H8NZy0cftxmEzSJ7P8mqyBVfIPi1sK64xmLmQm7v_LEdi1POv8Rgfxr_xdFX0GPr5W5qr0bGpK_R4jDV7udAQzE7Owbbr9LKR0DJbkw3ief7yPAOPuhu9tEfG5ySjhGgPq4ukPJZNUVNyM_hbUUCFnIWwPElfkyq5Dpg2u67YzKEz2zh1cY9VXMfLYBxlu28J3f1Rk3bpu2-9tIHQJN4lvVA-KDpclFcLc0QwfnUSBi5go7O6ybBN-8Aq6re_lv928Sm7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
البنك المركزي الإيراني يطبع عملة جديدة بقيمة 100 ألف تومان عليها صورة الحرم الشريف للسيدة معصومة وعلى الجهة الخلفية نصب تذكاري لمدرسة ميناب.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77915" target="_blank">📅 16:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئيس وزراء الإسرائيلي السابق
إيهود أولمرت:
المستوطنون بالضفة الغربية ينفذون تطهير عرقي ضد الفلسطينيين في الضفة الغربية بدعم من المسؤولين الإسرائيليين.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77914" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الحكومة البريطانية تعلن عن عقوبات تستهدف شبكات أسهمت في تمويل أعمال عنف للمستوطنين بالضفة الغربية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77913" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
الحكم بالسجن 11 سنة مع غرامة مالية بحق عدد من المستوطنين سرّبوا معلومات لإيران بما في ذلك مواقع القوات، تحركات الدبابات وسقوط الصواريخ.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77912" target="_blank">📅 16:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اعلام العدو: التقديرات تشير إلى أن المسلح كان يختبئ في المنطقة منذ فترة طويلة، وهناك شبوهات قوية تدور حول وجود "خلية كاملة" تتحرك في المكان، ويُحتمل أنه خرج من نفق في المنطقة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77911" target="_blank">📅 16:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: هذا حدث غير مسبوق منذ بداية الحرب، كانت المرة الأخيرة التي تسلل فيها مسلحون من لبنان إلى أراضي إسرائيل في يناير 2024 الى منطقة معزولة. اليوم حدث تسلل مسلحين فعليًا عبر السياج الأمني إلى داخل إسرائيل إلى منطقة مدنية بالقرب من المستوطنات.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77910" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">إذاعة جيش العدو: هذا استثنائي بالتأكيد، خاصة في ظل حقيقة أن قوات الجيش الإسرائيلي تحتفظ بشريط أمني بعمق عدة كيلومترات داخل الأراضي اللبنانية مقابل سلسلة جبال راميم</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77909" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سيارة في مستوطنة حولون</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77908" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعلام العدو: تم القضاء على اثنين من مسلحي حزب الله المتسللين في منطقة مرجليوت وهناك مؤشرات على وجود مسلحين إضافيين.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77906" target="_blank">📅 16:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اعلام العدو: مسلح تمكن من الدخول الى اسرائيل واطلق النار على القوات الاسرائيلية من الجانب الاخر من الحدود</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77905" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزيرة خارجية بريطانيا:
على حزب الله إنهاء هجماته وإلقاء سلاحه
.
صار تكرموا</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77904" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منصات للمستوطنين تتحدث عن خشية لدى جيش الاحتلال من إمكانية وجود مجموعة أخرى من المقاومين نجحت بالتسلل من لبنان إلى داخل الأراضي المحتلة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77903" target="_blank">📅 15:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77902" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏴‍☠️
جيش العدو في بيان: الحدث لا يزال مستمرا. تواصل قواتنا عمليات المسح، بالإضافة إلى طائرات سلاح الجو التي تم إرسالها إلى المنطقة. نحن على اتصال مستمر مع السلطات المحلية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77901" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77900" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77899" target="_blank">📅 15:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77898" target="_blank">📅 15:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">كريات شمونه مسكاف عام المطلة   مغلقة حتى إشعار آخر بأمر قوات الرضوان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77897" target="_blank">📅 15:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3a3d474b.mp4?token=T9rLE_S7ePBer3S72JRgukTl4vg5KjyvacAkx8WJnNHV77mEpWzplVE-3RImQr998GwAzdL12s4ABiNI-OxRv2GFhehjoYCvpd0qxgLT3MfnBFXfv9i_Vt9GGaJOgrFnL65UTrPniHNygfjtoHWY5dhHEt0d1_BuWoXK0uB9B8-hr_02U-RH83dSp8xAM3iTAsY63mN3UC_Yao75DhiTvEv_dbK5g6LA4ZA5ETRVxHU42c5P_BfKyjY9BMmbslGbQw42hf80MgITR3pyV10E2JcVBzDXai_EoJF3_P2ScEmx4SOQyLTUbs5lOKe7-c1seGc8hkUh2FNrclq-dYum8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3a3d474b.mp4?token=T9rLE_S7ePBer3S72JRgukTl4vg5KjyvacAkx8WJnNHV77mEpWzplVE-3RImQr998GwAzdL12s4ABiNI-OxRv2GFhehjoYCvpd0qxgLT3MfnBFXfv9i_Vt9GGaJOgrFnL65UTrPniHNygfjtoHWY5dhHEt0d1_BuWoXK0uB9B8-hr_02U-RH83dSp8xAM3iTAsY63mN3UC_Yao75DhiTvEv_dbK5g6LA4ZA5ETRVxHU42c5P_BfKyjY9BMmbslGbQw42hf80MgITR3pyV10E2JcVBzDXai_EoJF3_P2ScEmx4SOQyLTUbs5lOKe7-c1seGc8hkUh2FNrclq-dYum8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عدد من انصار الجولاني يقطعون الطريق على صهاريج النفط العراقية في بلدة الهول</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77896" target="_blank">📅 15:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">كريات شمونه مسكاف عام المطلة
مغلقة حتى إشعار آخر بأمر قوات الرضوان</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/77895" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77894" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">إعلام العدو : نبحث عن مسلح ثاني داخل الجليل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77893" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من طيبة إلى العديسة حتى مسكاف عام
المقاومة تشتبك من مسافة صفر …</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77892" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شبح عماد مغنية في مسكاف عام</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77891" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">المقاومين تسللوا باتجاه مسكاف عام ..</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77890" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اعلام العدو: عدد المتسللين اكثر من واحد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77889" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">من العديسة إلى مسكاف عام
كمين العديسة اصبح داخل الجليل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77888" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هجوم بري من قوات الرضوان على مستوطنات الشمال</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77887" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قوة الرضوان تخترق الجليل</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77886" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/77885" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الكيان الصهيوني يصدر عدد من التعليمات بعد حادثة تسلل في منطقة شمال سلسلة جبال رميم:  - على سكان مستوطنات مسكاف عام ومرغليوت ومنارة الالتزام بتعليمات مسؤول الأمن المحلي، والبقاء داخل المنازل وعدم التجول داخل البلدة. تعمل وحدات الدفاع والجيش الإسرائيلي في المنطقة.…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77884" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعلام العدو: المسلح كان يقاتل ببندقية وسكين.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77883" target="_blank">📅 15:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
الإليزيه:
ماكرون يستقبل توم برّاك ويبحث معه أوضاع سوريا والعراق ولبنان</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/77882" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-zZAPIchVs-ueXljhv8uZPjiC4M0HPTkSCdnN79RGp6k328AO1e6zkFskT7wUfWZirqO2rcYkMyFKcaXitDvlyIaBRorF2vu86MFHENzaKUB-Bk6ZQyB9PnkXWIMTMgtCbBOqlNeT07ZYuHGp_XMVdsmFuCUMB8xf9YeXoH0Qv-9tXZX32QGz4hvFrkeLX0nzhL7spL3F_PHksqPul3UHpj4UCHnVR1L3oIZSk7qg5z16WDLwcMzCgUouWtSyP7hp0ll8_JaI59Vvqtmry0ACFFI9F7wRf_Qm4k1UbcSRiU5f4jH2IsCvEDAHun9hAwyEB1kvO-J0Cv5FSZkA6aoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: تبادل لإطلاق النار بعد تسلل مسلح عند الحدود مع لبنان قرب سلسلة جبال راميم بالجليل الأعلى.</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/77881" target="_blank">📅 15:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعلام العدو:
تبادل لإطلاق النار بعد تسلل مسلح عند الحدود مع لبنان قرب سلسلة جبال راميم بالجليل الأعلى.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77880" target="_blank">📅 15:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
وزير الخارجية الأميركي ماركو روبيو لعب دورا محوريا بإقناع ترمب بدعم الضربة الإسرائيلية لإيران مبررا ذذلك بأن عدم الرد سيمنح إيران ميزة ويشجعها على المزيد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77879" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
ماذا حدث البارحة ؟!
الطيار وكيل جهاز الامن الوطني العراقي هو احد عناصر حزب الدعوة تنظيم الداخل .. دخل الجهاز مع عبد الكريم العنزي وكان من مؤسسي الجهاز بعد ٢٠٠٣ ..
بعد فضيحة سوداني وتر غيت بوقتها التي انتشرت في الإعلام ؛ تم اعتقال شخص بالدائرة القانونية و شخص آخر بجهاز الامن بالجهاز اعترفوا انهم يتلقون أوامر للتجسس من قبل الطيار ؛ اغلقت القضية انذاك بسبب تدخل إقليمي وكون ان السلطة التنفيذية هي المتهمة استعصيت تطبيق مذكرات إلقاء القبض ؛ ابرز الشخصيات التي تم التجسس عليها " القاضي الأستاذ فائق زيدان ، الوزير مصطفى سند المرياني ، الشيخ قيس الخزعلي وعدد من أفراد أسرته ُ ، عبد اللطيف رشيد واخرون "
البارحة طبق جهاز امني مذكرة استقدام وتحري قد حركها نائب سابق على الطيار الذي استقدم وبعد التحقيق تم إصدار امر اللقاء القبض ..</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77878" target="_blank">📅 15:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇫🇷
‏فرنسا تمنع سموتريتش و4 من قادة الاستيطان و21 مستوطنا من دخول أراضيها.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/77877" target="_blank">📅 15:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو تكشف عن تفاصيل جديدة حول طلعة الهجوم الجوي التي كان مخططًا لها أن تنطلق أمس نحو إيران وتم إيقافها بقرار من المستوى السياسي:
- كان الحديث يدور عن طلعة هجومية كبيرة، جرى الاستعداد لها في المؤسسة الأمنية منذ اللحظة التي بدأت فيها إيران بإطلاق النار على إسرائيل أول أمس عند الساعة 22:00، واستمرت التحضيرات طوال الليل وحتى ساعات الصباح.
- كان من المقرر أن تنطلق الطلعة الجوية إلى إيران أمس في ساعات بعد الظهر.
- من بين الأهداف المخطط مهاجمتها: البنى التحتية الوطنية الإيرانية، بهدف تعميق الضرر الاقتصادي الذي يلحق بالنظام الإيراني (وذلك بعد الهجوم المحدود الذي نُفذ على المنشأة البتروكيميائية). كما كانت هناك أهداف أخرى لا يمكن الكشف عنها.
- التغريدة التي نشرها ترامب والتي دعا فيها إلى وقف الهجمات عند الساعة 12:30 بتوقيت إسرائيل، جاءت قبل وقت قصير — أي قبل ساعات قليلة فقط — من موعد إقلاع الطائرات، ولذلك بقيت الطائرات على الأرض وهي مسلحة ولم تنطلق نحو إيران.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77876" target="_blank">📅 15:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXEFfaJ2w7tGtTrl4IVnvzc1bzW_ORTBkTsf79r5LUrlzL7jevACY5tlfcfTRu47icztKPxcKeX8Y3DTuefNikdEmA92QQp7zZ_S5E-Nhnjf01SK-DTJzvPH_SWg6VXpReIeG8X1jjbJ-CRy7CaF2b2HMqFmb7lgwkWQjuVsNqhqKyfVEq0aUHFhEiOfwkW4lQBY-kKLaBVomaQwWqjHLpQhOs7JYCv8fTe2ffD_B0hN3xFIBKtxvSebUYNjHlhYqmx1nQgze7r7T4Rfy17MwDvXHoHJkR9zmH4p-VuzcOoldgQ7U4RQF2u4gCVTd_0R8BPnWm2OHR9AbTK8Qi1t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات صهيونية على جنوب لبنان</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77875" target="_blank">📅 15:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
المجلس الوزاري المصغر قرر أن أي صاروخ يطلق من لبنان سيقابل بهجوم على بيروت دون موافقة من القيادة السياسية.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77874" target="_blank">📅 14:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvzidcfXPivJ2VDTvyLP0GDT4ufUmUvD7qNir3Ouee1i7petu4QK3KVMaWFTUImrsFY2s8GrOrrPUoLHrwqCU3CjbPeHOTMZsySq0S3Szkf01nwG2VxJFBq5pi9i_j5Vw6nRB0kc2r6jeWm6WCSQ48v9vwgzdTlgulTsZ_OQ-TSjAoE2Rt0o__-4ZC-KU396em9X1QXwrYgdLlTVlvnIgmaHrhLFzrj6l6XU57n2xYH7U8G4bboRYKVqzUoU1GgB0u6fH9Zq-QqfbGN6QYzorDse8kVj49IQY0Se-DZBHLM4OoYLaF3e7LRfI_mG7fQMRbG_Zq3F8LPOiGXaB-T4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
وكالة مهر:
تعيين (ياسر الحجاج) سفيراً جديداً لجمهورية العراق في طهران.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77873" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1cd39643.mp4?token=nMFdy8nFl0zC0M5IGCCWm4TzTNj-15m3Q5ROZhqIXdroF5foGawIbI6agYGyLZ7DptG6Kumt5_L6NkyHL36CDDM0A6NpwBns4QnDRIo6YEbfblFIQESu_YaQ_x7yuQXgP7ThqO1BPP68ph3RSRlQUu8gaNBxixBlsJYyAm4pWtrWDAUmJP_eNLHazN6WjHOMryYykygZK4VH7IR_8BANOg21u9gDff9_bb9J4m-rxbKrfUePdT7jVPmCgMt1Hn1yA6gTz8ihDu34ibFFyxnmdVRDeem-k7mVITJqC24cIFTXJtZz-0JmNsW1hP2VfDo1bMryk7VYficSdr1GMgyTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1cd39643.mp4?token=nMFdy8nFl0zC0M5IGCCWm4TzTNj-15m3Q5ROZhqIXdroF5foGawIbI6agYGyLZ7DptG6Kumt5_L6NkyHL36CDDM0A6NpwBns4QnDRIo6YEbfblFIQESu_YaQ_x7yuQXgP7ThqO1BPP68ph3RSRlQUu8gaNBxixBlsJYyAm4pWtrWDAUmJP_eNLHazN6WjHOMryYykygZK4VH7IR_8BANOg21u9gDff9_bb9J4m-rxbKrfUePdT7jVPmCgMt1Hn1yA6gTz8ihDu34ibFFyxnmdVRDeem-k7mVITJqC24cIFTXJtZz-0JmNsW1hP2VfDo1bMryk7VYficSdr1GMgyTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدة حوادث سير لصهاريج النفط العراقية في الاراضي السورية بسبب سوء البنى التحتية في سوريا مما خلف خسائر كبيرة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77872" target="_blank">📅 14:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlDeqwPzMSv9RRITTbp6Dq3yV6Azc9zZ7FzvFhjIJYgR4Dn3QMbdahHsK-pluQSshqsopCshXXD-YvJgXMlbOBdpX14jeCR9o27xeDSYxfXh7CWLLQIYBTuWLMnHff_-OKeSiGcUCa3gVGhKgIqhQemBHp8-npCZM3KABIvFTf1zcFdiHCsEU_5Qi8UI0W-fUNfjMq4Fuy3BsulwdhOORJdEGHtJ3v-xXWAANs7pMbLu5rVciiix6KLWvC5igkEksmX402uiVUwRQTgO6L7DwXay0gEWuHjtfhZZe_GWvChV4Cs_za4UfGT7JowDcZ2N7WbBMLf89yJspv5hwzBhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: بموافقة الرقابة، تُظهر صور الأقمار الصناعية إصابة دقيقة لحظيرة داخل قاعدة رامات ديفد الجوية بصاروخ إيراني قبل يومين.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77871" target="_blank">📅 14:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
وسائل اعلام لبنانية:
قائد الجيش الباكستاني يرغب في الاطلاع من نظيره اللبناني على حقيقة الأوضاع في جنوب لبنان، المشير منير يريد الاطلاع من نظيره اللبناني على قدرات الجيش اللبناني على الانتشار في المناطق الجنوبية. زيارة قائد الجيش اللبناني إلى باكستان لا يمكن أن تتم من دون موافقة وضوء أخضر من الرئيسين عون وسلام</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77870" target="_blank">📅 14:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
قادمة من اقليم كردستان..
هيأة المنافذ الحدودية تحجز 13 شاحنة في محافظة كركوك تحمل بضائع مستوردة تم تزوير الباركود الخاص بها الى محلي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77869" target="_blank">📅 13:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الوساطة الأميركية بشأن أوكرانيا متوقفة حاليا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77868" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
بعثة إيران أكدت أن الوكالة الذرية هي التي أوقفت التفتيش بالمنشآت النووية عقب العدوان على إيران، إيران تعد مشروع القرار الأمريكي الأوروبي ضدها في مجلس محافظي الوكالة الذرية مسيسا واستفزازيا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77867" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bawIlm0zBYWaD0wt6ibWQyW9t4N3wrXDebRTpREci4Qp4AZscKE318tQuwIoJ6is39D22y8RHtkTUdWZc1YdkijazsLOjkm7r9xaspZfTSU8PR1ZmhwEEgN9uAvt22EhjwS58snYht-cHsLDsv6g5eM4yXduhPKS1by5EuZrJ7ruwD_aK63dcu0cspOVjYlmiyFal03C09KWkY_LJFAZgG7q4yGrN1AA_fWIQlbZHeky1Y0m2BeKkezXl5NN8ML099UbLH4txFYKTqQRKYOFaGoJSNVoVGOpSqcvlS_0N8N2bdJdRao-UACP7o7JYE1n-U0m4wQlrozlZEyND3rQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
الشيخ اكرم الكعبي يحيي الجمهورية الاسلامية وابطال اليمن على تأديب الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77866" target="_blank">📅 13:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لجنة تحقيق رسمية للأمم المتحدة:
السلطات الإسرائيلية متورطة بشكل مباشر في هجمات المستوطنين التي أدت إلى قتل وإصابة وتهجير فلسطينيين في الضفة الغربية، في حين أن قوات الأمن الإسرائيلية توفر الحماية للمستوطنين. وأكد التقرير أن السلطات الإسرائيلية سمحت لهجمات المستوطنين من خلال دعم مالي وعسكري، في ظل أجواء من الحصانة من العقاب التي خلقتها أنظمة القضاء وإنفاذ القانون.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77865" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله حول الرد الصاروخي الإيراني على الكيان الصهيوني:
إنَّ الرد الصاروخي الإيراني على الكيان الصهيوني دفاعًا عن شعبنا اللبناني هو رسالة التزام أخلاقي وسياسي وميداني من الجمهورية الاسلامية اتجاه لبنان بعدما تمادى هذا العدو بغطاءٍ كامل من الإدارة الأميركية في ارتكاب جرائمه ضدَّ بلدنا، وعاود استهداف الضاحية الجنوبية، في إطار خروقه المستمرة  لاتفاق وقف النار بما يؤكد استخفافه بكلِّ الاتفاقات الدَّولية، ولذلك جاء الرد الايراني للتأكيد أنَّ مصلحة استقرار المنطقة ودولها هو بذل كلِّ جهد ممكن كي تُصان الاتفاقات وأن يلتزم بها العدو الصهيوني قبل غيره، وهذه هي الرسالة التي أرادت إيران أن تبعثها بوضوح وقوة إلى كل المعنيين بجهود دعم الاستقرار في منطقتنا. وقد تزامن مع الدعم المشكور من حركة أنصار الله في اليمن في إطار العمل المشترك لردع الكيان الصهيوني وإفهام الإدارة الأميركية أنَّ دعمها للعدوان الصهيوني على بلدنا سيطيح بكلِّ الاتفاقات التي تسعى إليها خصوصًا في ظلِّ إصرار الجمهورية الإسلامية على تضمين أي اتفاق معها وقفًا شاملًا لإطلاق النار في كل الجبهات وبالأخص في لبنان، كمقدِّمة لفرض انسحاب العدو من أرضنا اللبنانية وعودة النازحين وإعادة الاعمار وإطلاق الأسرى.
إنَّ هذا الدعم الإيراني لحقوقنا المشروعة، وتحمُّل تكلفته الماديَّة والسياسيَّة يؤكد مرَّة جديدة أنَّ ايران هي من تساند لبنان وليس العكس، وذلك انطلاقًا من مبادئها وقيمها الإنسانيَّة، ومن عمق العلاقة التاريخية بين الشعبين اللبناني والإيراني، فإيران كانت على الدوام تريد الخير لبلدنا، وأسهمت في دعم مقاومته  لتحرير أرضه وفي إعادة إعمار ما هدَّمه العدوان الصهيوني، وموقفها المشرِّف إلى جانب لبنان يستحق من سلطته الشكر وليس التنكُّر والإساءات المتعمدة  استجابة لإملاءات خارجية، فكلِّ الأصوات المدفوعة بتلك الإملاءات  لن تؤثر على صدقية هذا الموقف الإيراني الشجاع والوفاء النادر في زمن تغليب المصالح على المبادئ، فالاتهامات الباطلة التي صدرت عن بعض جهات السلطة ضدَّ الدَّور المشرِّف لإيران الساعي إلى وقف العدوان الصهيوني على لبنان، مرفوضة بالكامل لأنَّها تجافي الحقيقة وضدَّ مصلحة لبنان،  فالتهجم الظالم على إيران بما في ذلك البيان المشترك مع العدو والإدارة الأميركية ضدَّها هو خارج عن كلِّ قواعد العلاقات الديبلوماسية واصطفاف مرفوض ومدان، ولم يخدم سوى العدو الصهيوني.
إنَّنا ندعو السلطة اللبنانية إلى اغتنام الفرصة المتاحة وتصحيح علاقتها الرسمية مع الجمهورية الإسلامية بما يخدم مصالح الدولتين، والاستفادة من هذا الدعم الإيراني من أجل تحقيق أهدافنا الوطنية خصوصًا على ضوء تشكُّل المظلة الإقليمية الجديدة المنبثقة من مفاوضات إسلام آباد، وبذلك تتمكَّن الدولة في لبنان من خلال مفاوضات غير مباشرة مع العدو، ومستندة إلى تلك المظلّة وعوامل القوّة التي تشكلها المقاومة وصلابة الموقف الشعبي وثباته والتفاهمات الدَّاخليَّة من تحقيق مطالب شعبنا في تحرير أرضه وعودة النازحين وإعادة الإعمار وصون السيادة الوطنية.
إنَّنا في حزب الله وباسم شعبنا وعائلات شهدائه والصامدين والنازحين وباسم كلِّ حرٍّ وشريف في وطننا نقدِّر عاليًا هذا الوفاء من قبل ايران ونحيي شجاعة هذا الموقف النبيل للولي الفقيه ولرئيس الجمهورية والحكومة والبرلمان وللجيش والحرس الثوري ولأبناء الشعب الايراني على وقفتهم المشهودة إلى جانب حقوقنا المشروعة وقضيتنا الوطنية، وهي الحقوق التي سنواصل الدفاع عنها من خلال مقاومتنا البطولية حتَّى تحقيقها مهما غلت التضحيات ليبقى شعبنا على أرضه يعيش بعزَّة وكرامة وحريَّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77864" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">إطلاق صاروخ أرض جو على طائرة حربية صهيونية جنوب لبنان
وإسقاط مسيرة فوق جبل الريحان الآن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77863" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8a2MXVivfeBhZmt-n8t4LYsD9IkC5GaKzdAnD9sc7-6FgrP-8P_bunA_Flzs8xJlkyLeESVl-fS7uhue5twE-WWIB41TQFt6aOQRu2W0zW8vAOm8m02wIV7TMt3BWkTqbwA-xEpJZsBtRSH1vcrC0cxqxoNe04jxbzEOgCAvKq_CUld8XvFuRE_dV8elfNst5_CF6zTpTwGJd2Q_kltS58YXVwZGgoa7RZu2GcHh6_zt2qjX-eAvglAKygXQus7sWq3uPVdbXhbAw5mMGDfxKnlQtN0ZtigR5TTJd-5FonSVcw4fnkkun6nkkn5LZHVkaVw-e0icZfPLc0ettvy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف صهيوني لسيارة على طريق المصيلح جنوبي لبنان</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77862" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب ظهر على الكاميرا أثناء عزف النشيد الاميركي، يتعرض لهتافات استهجان عالية في قاعة الغناء اثناء حضورة لنهائي مباريات احد الرياضات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77861" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل طلبت من نتنياهو ألا يرد؟  ترامب: لا، قلت افعل ما هو صحيح، لكنني أريدك أن تتوقف بأسرع ما يمكنك لأنهم يجب أن يتوقفوا.  كان ذلك يتعلق بلبنان ويجب أن يتوقف. نريد أن ننهي ذلك.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77860" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بشأن إيران:  إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.   لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77859" target="_blank">📅 10:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب بشأن إيران:
إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.
لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن يفعل ذلك؟ أنا لا أريد ذلك.
وسيكون لدينا - سيكون لدينا وثيقة موقعة تكون في الواقع أقوى من القصف.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77858" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs1kH1gh91eR57CxwzlJRqB4y6aerfBWd1OcfY0gdwywoAyjgOwIly8cp6-fsuqWAhc8T7Q-IoZ54lhoIca6Na2q3HJ3KR9ySKeq1-5I0qrg4teR_S9x259hphsLIolIpoGib9lMxmocLKXuWXb8vGVnqwA3rY_YmGLohu3sP4G5Oy0smbBGME-KCWlYho1NbBFwke0jrSOM6VDCY200IYj6fG3uEZsao0OtKTRsYQ-L5l6A1ctj5glOiomlmU4TmdCU1EMbCfAeJj1eVLu_ZgG0B24RnqmoRyLPoB8jRhq0yvJyVthoTwIIm8CUvMwjJwvcRHw0bVE0q5i_ZivZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
سي إن إن: كم مرة ادعى ترامب أن الاتفاق مع إيران "بات وشيكًا"؟
- أعلن دونالد ترامب منذ بداية المواجهة مع إيران ما لا يقل عن 37 مرة أن التوصل إلى اتفاق "أصبح قريبًا"، إلا أن هذه التصريحات لم تترجم حتى الآن إلى نتائج ملموسة على أرض الواقع.
- ويرى محللون أن هذا النهج يمثل "استراتيجية فاشلة".
- ويعتبر أن ترامب، من خلال المبالغة في الترويج وتكرار الوعود غير المدعومة بنتائج، أضرّ بمصداقيته الدبلوماسية.
- كما أنه بات عالقًا في محاولة الحفاظ على صورة "صانع الصفقات الكبير"، بهدف طمأنة الأسواق المالية وإظهار نفسه بمظهر القائد القوي، إلا أن تكرار هذه الوعود جعل المراقبين الدوليين والرأي العام أقل اكتراثًا وأكثر تشككًا تجاه تصريحاته.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77857" target="_blank">📅 10:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇱🇧
🏴‍☠️
تجدد الغارات الصهيونية على المساكن في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77856" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">إذاعة الجيش الإسرائيلي: لدينا قيود على الهجوم في بيروت ولكن ليس على العمليات في جنوب لبنان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77855" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVzIJ6D22GztOqic162ifWZ9WHvtmNC_1UY-YGxMfaQYCHHgxJN1BeITjloN3eFrCovEq_pcA1WVuKFtw_JetM-00Hv8Q83ax8lN_nrKbWbJ_DcH2-in3C5PaKwBbQodvy866uR3yRSC2a7q6aiPbS_GGNnYFpji3fRzRVWiAm_c4hxB7sP9uhNwLw7k3tAGO0jOhV44Wph3zpZjsgl_ZuIDFEgsHwEcPfk50XjlTcdQB0pPAD5k1TZhDqwQXaUeuTqd7eLtK5I9uF09kAPgC92k2BKbGXskm1kAUfbzRiyGAt45QsKcn_6WUt0WMmiLGpgM-m7phrIfTCxpkwFZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انفجار عبوة ناسفة في سيارة بالقرب من حي بالاشيخا من موسكو.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77854" target="_blank">📅 09:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203541429e.mp4?token=cCAS_bStt_9e5qfyjkPxLNeTJvK4HPwFXbCt2vmTX_Lcgm7PHNvo5M8gZWYSkrFMU0R-lJ-fxhMRzFkJl6k8UbVzEok3JbuLp_RL2YSRhaSQrn-9lye4lFcZJL57Lpr9KRYtQZEaIL61XPvTp_b4NUX7IAKehAXPdx8C-44JlqaNAuYzHazxbAugNx1ouuNfhEEZ_muHzMyjOsRCiv6hgrp_cHvOTuPuS2x7GcKySTMcSPL6DtVEKQ7FJjBgu5juEB3T9deIQycqpdQW3tw-8rnR879A_QenbYUzWvppRntm8FhZgGIiZcOevDvNBnjEmScW97KCDEQLeoBez_Hsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203541429e.mp4?token=cCAS_bStt_9e5qfyjkPxLNeTJvK4HPwFXbCt2vmTX_Lcgm7PHNvo5M8gZWYSkrFMU0R-lJ-fxhMRzFkJl6k8UbVzEok3JbuLp_RL2YSRhaSQrn-9lye4lFcZJL57Lpr9KRYtQZEaIL61XPvTp_b4NUX7IAKehAXPdx8C-44JlqaNAuYzHazxbAugNx1ouuNfhEEZ_muHzMyjOsRCiv6hgrp_cHvOTuPuS2x7GcKySTMcSPL6DtVEKQ7FJjBgu5juEB3T9deIQycqpdQW3tw-8rnR879A_QenbYUzWvppRntm8FhZgGIiZcOevDvNBnjEmScW97KCDEQLeoBez_Hsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثار الغارات الصهيونية صباح اليوم على بلدة دير قانون النهر في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77853" target="_blank">📅 09:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67efdca0ce.mp4?token=mkM_gojHqtLoKT9EsJ_FqEUuF63n-YS-5POq-wJMDzJDoUo4ehMcL1yD3PFOlO83hdBL6NtZqZSLA_AMVM4SAOG2nFpgLIJGTuAcaLXZgTwpntoADiVQmfxa8G5gX80pqZApNLhFKrAREac0OwR2S_Qkg0K5OA5aHBPJjQ55lK8co4yy8kjRk1B8-09WPxopmQaRTijEw8LOAdVlrz21oRZfQc_QViiQDjVOQkIulYnqwFgGJFDlManKnlreKMkPxbwigAAzXj6VlDELNxpvW3t9Lu3jALAcJb-XVn3AqWkjCxxbECpYtE89iU1OGLUlJFgKMiKax0k3WJ-uGpzY0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67efdca0ce.mp4?token=mkM_gojHqtLoKT9EsJ_FqEUuF63n-YS-5POq-wJMDzJDoUo4ehMcL1yD3PFOlO83hdBL6NtZqZSLA_AMVM4SAOG2nFpgLIJGTuAcaLXZgTwpntoADiVQmfxa8G5gX80pqZApNLhFKrAREac0OwR2S_Qkg0K5OA5aHBPJjQ55lK8co4yy8kjRk1B8-09WPxopmQaRTijEw8LOAdVlrz21oRZfQc_QViiQDjVOQkIulYnqwFgGJFDlManKnlreKMkPxbwigAAzXj6VlDELNxpvW3t9Lu3jALAcJb-XVn3AqWkjCxxbECpYtE89iU1OGLUlJFgKMiKax0k3WJ-uGpzY0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثار الغارات الصهيونية صباح اليوم على بلدة دير قانون النهر في قضاء صور جنوب لبنان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77852" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترمب: تحطم مروحية أباتشي أميركية قرب مضيق هرمز أمس الإثنين وإنقاذ طاقمها</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77851" target="_blank">📅 08:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: المحاولة الإسرائيلية للفصل بين إيران وحزب الله تواجه صعوبات كثيرة وما حدث بأمر من ترامب</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77850" target="_blank">📅 07:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
‏إعلام أميركي عن نائب ترمب:
لن نتورط بحرب طويلة الأمد مع إيران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77849" target="_blank">📅 04:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64615b9230.mp4?token=D34gPxi7XeF9QMced66FynUwwucbHJU2uzmUty25TLJ-nntMnzjYu2LOdw3oRE6D7-Y-KFz55lQ8oIsBOxTb-_z3SnKzjZlatR3vQ7U9MSh_gYXlw9DERWa-VfQLfsVVc8sEdNYX96a9YewzAShki1oEyC04BLoWoiYlTwjLLfo9m8Q5qy_VRKdxRpsMq9tgVOP--Hp5lR5fglMvE8qZo67Sbu3dojjWr1Ltp25b7Ud_S4PzfASs8mDGDMhHxMmyQSJos3Lu040C5LtdAoGfLKZx5XctGLSfRjsMlA52e_-4UhbfisGMZafmBBqUmvjaAy1DSzZU6RjSzYZ7fyr-SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64615b9230.mp4?token=D34gPxi7XeF9QMced66FynUwwucbHJU2uzmUty25TLJ-nntMnzjYu2LOdw3oRE6D7-Y-KFz55lQ8oIsBOxTb-_z3SnKzjZlatR3vQ7U9MSh_gYXlw9DERWa-VfQLfsVVc8sEdNYX96a9YewzAShki1oEyC04BLoWoiYlTwjLLfo9m8Q5qy_VRKdxRpsMq9tgVOP--Hp5lR5fglMvE8qZo67Sbu3dojjWr1Ltp25b7Ud_S4PzfASs8mDGDMhHxMmyQSJos3Lu040C5LtdAoGfLKZx5XctGLSfRjsMlA52e_-4UhbfisGMZafmBBqUmvjaAy1DSzZU6RjSzYZ7fyr-SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب ظهر على الكاميرا أثناء عزف النشيد الاميركي، يتعرض لهتافات استهجان عالية في قاعة الغناء اثناء حضورة لنهائي مباريات احد الرياضات.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/77848" target="_blank">📅 04:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLjgGhZC0LtFDZjJeauttZxPM7wpvjkysiAZUG48eE1_VOvkRMmYln6mnHVNJSgxe7eVs9S8aQ4nOmsYwE9DwbwQV8DSdz-8uZTqaXfP6xXPxKHxkbmqWUwmxVWiSL5AMGzyD0mGq3gjpe39sVgDwiwYwjgYFUJVK9Zz7rZ9TsdLYiaChHpcW0WHmxOWXyGUextM5S1YCxXzG8oPA-sm5_qOYT4toAHJRIP8GVqRpl1W3do99vv_lpaZ0o6E2tGKaZLo1O6WTwDpLw7JpKtaTy_bnOdejEnWBmm8OsNGUBMk3I39kPmIHl0O77E7UbEaJ_h9H4mw5Ab4Dpww71WATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏شهدت نهاية هذا الأسبوع عمليات نقل نفط سرية كثيرة بين السفن في الشرق الأوسط. ليس هذا نفطاً إيرانياً، بل نفط قادم من دول الجوار العربي لإيران. وهذا سبب آخر لعدم وصول سعر برميل النفط إلى 200 دولار حالياً.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/77847" target="_blank">📅 03:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
عقد الإطار التنسيقي اجتماعه الدوري في مكتب سماحة السيد الحكيم، بحضور السيد رئيس مجلس الوزراء، لمناقشة الملفات المدرجة على جدول الأعمال.
وبحث المجتمعون الشأن الحكومي، وقدم السيد رئيس مجلس الوزراء رؤية متكاملة لمعالجة الأزمة الاقتصادية، وعددًا من الحلول التي حظيت بدعم الإطار التنسيقي، ولا سيما المقترحات الخاصة بمعالجة أزمة الكهرباء، وتفعيل قوانين العمل والضمان الاجتماعي دعمًا للقطاع الخاص.
واتفق الحاضرون على إعداد ورقة باسم الإطار التنسيقي تتضمن أهم الملفات الوطنية، وطرحها ضمن ائتلاف إدارة الدولة للاتفاق بشأنها.
كما أكد الإطار التنسيقي وقوف جميع القوى السياسية خلف الحكومة نيابيًا وسياسيًا وإعلاميًا من أجل إنجاح برنامجها الإصلاحي، واتفق على ضرورة الإسراع في إكمال الكابينة الوزارية في أقرب وقت ممكن.
الإطار التنسيقي
الدائرة الإعلامية</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/77846" target="_blank">📅 02:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
تعليق رحلات مطار الإمام الخميني بالعاصمة طهران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/77845" target="_blank">📅 01:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
النائب الأول لرئيس البرلمان العراقي يدعو الحكومة إلى وقف تحويل الأموال لإقليم كردستان لحين إجراء التسوية الكاملة للمستحقات</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/77844" target="_blank">📅 01:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
ترامب بشأن إيران
: نحن نتفاوض الآن، وإسرائيل لن تعود إلى الحرب مع إيران</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/77843" target="_blank">📅 01:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
زلزال بقوة ٥ درجات يهز أجزاءً من محافظة هرمزكان الايرانية.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/77842" target="_blank">📅 01:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff02235e2.mp4?token=DheqfoRNaAvQCaPf5gsdkLrso6QN3FYnRSzSFfDg7jtp31eb1RDC-vGx0zZgkr-nIJjuxa2Z9n0jnrrKMJ7cYMldlgUoaRuhf2eTj-Qo1Vpwo-rb8jffFUg5Yw_JB5KntbuDUfu7djz7qQqqbWmqlBgiwgtMHZHA2V6GBukh8kHr-3pniCxdGcs60CguCwd4Xzv5gh3Gquc4E0ilSJrIHYPVoU0om5WyzuHp2WTRHNh9Xs1z7JUJUYmbSsyYLHs9HhcBadd6_1D8gt_s429VZ8xCmi9rSEf-Z41uIHIQUSjYy_yWjW2jE7Xy1rjvVwRj-5hLfYMYB0avTe_dn9YQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff02235e2.mp4?token=DheqfoRNaAvQCaPf5gsdkLrso6QN3FYnRSzSFfDg7jtp31eb1RDC-vGx0zZgkr-nIJjuxa2Z9n0jnrrKMJ7cYMldlgUoaRuhf2eTj-Qo1Vpwo-rb8jffFUg5Yw_JB5KntbuDUfu7djz7qQqqbWmqlBgiwgtMHZHA2V6GBukh8kHr-3pniCxdGcs60CguCwd4Xzv5gh3Gquc4E0ilSJrIHYPVoU0om5WyzuHp2WTRHNh9Xs1z7JUJUYmbSsyYLHs9HhcBadd6_1D8gt_s429VZ8xCmi9rSEf-Z41uIHIQUSjYy_yWjW2jE7Xy1rjvVwRj-5hLfYMYB0avTe_dn9YQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
😆
محولة كهربائية في محافظة ميسان جنوبي العراق تحاول الانطلاق نحو الجولان للمشاركة بالقصف على المحتل في فلسطين.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/77841" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇱🇧
🌟
المجد لسلاح المقاومة المفاوض الوحيد للشعوب المستضعفة في المنطقة ..</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77840" target="_blank">📅 00:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4d39775b.mp4?token=BFxP9_yoXt1MzX1suegGf5k7eu3HpupgnSvEEFFQ9eWqAqLPug9eM0tBwbHPH9MT6-2yIiJlW-58TZ5kk9xQlT0ztfB5L37eVJAYELVWSobmv80S_vlBGSNfYZ6l26ga10kq3AVfm-X2Fby_SUrCxfJiNfuUBwYnbVX5TpDjS4Zkhqy9vp6dSgdUNNz16HvB2MGbW16HInGdWxElHt25LHfABCkVrbMAOtnILGW5fyxz-0Y9iciwHtQdpCDxrPGOFg4shjeHPLiSSIri9ZKERjgDDYMfyl7d8zDUdxYZLWIgTay5XL0oaQNRDDGuHzDI_ajxnmUDcBN4c_qrUF_3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4d39775b.mp4?token=BFxP9_yoXt1MzX1suegGf5k7eu3HpupgnSvEEFFQ9eWqAqLPug9eM0tBwbHPH9MT6-2yIiJlW-58TZ5kk9xQlT0ztfB5L37eVJAYELVWSobmv80S_vlBGSNfYZ6l26ga10kq3AVfm-X2Fby_SUrCxfJiNfuUBwYnbVX5TpDjS4Zkhqy9vp6dSgdUNNz16HvB2MGbW16HInGdWxElHt25LHfABCkVrbMAOtnILGW5fyxz-0Y9iciwHtQdpCDxrPGOFg4shjeHPLiSSIri9ZKERjgDDYMfyl7d8zDUdxYZLWIgTay5XL0oaQNRDDGuHzDI_ajxnmUDcBN4c_qrUF_3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى لانطلاق المضادات الارضية لمحاولة التصدي للمسيرات فوق ايلات</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77839" target="_blank">📅 00:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e745845fbf.mp4?token=b49TwsOnsVfypBZfxzS9CCDi5AIZPw9K6oX0WJ8NDbpMWEOXyDIL6o4DHVsQ2MmaLHhL_gxZT3VpJ5rJrgaFuWOVW6zC9nRzSl8tVYEHtTj7YLW1a8rush74z3it4UT7o5i9sX9KD-RtsaYBZRhMDyB1u-hDASXBWFw1XwyOcAZgTNLeuY7TlIwEbZgKCAxifBOrjv3wLxFGKy5SqVJbRa2hcjzsio97L3l_Q6vyE_BF4r2cGG4Y2t7hprdGAKG5RH2HnQJBVwFBUlqE9I8eLCBBlDHi4ehVXLxPDnuAxUgHbPnKGweTHFX23RbWRcSeySUqwXr0PuY3tS3eeThNfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e745845fbf.mp4?token=b49TwsOnsVfypBZfxzS9CCDi5AIZPw9K6oX0WJ8NDbpMWEOXyDIL6o4DHVsQ2MmaLHhL_gxZT3VpJ5rJrgaFuWOVW6zC9nRzSl8tVYEHtTj7YLW1a8rush74z3it4UT7o5i9sX9KD-RtsaYBZRhMDyB1u-hDASXBWFw1XwyOcAZgTNLeuY7TlIwEbZgKCAxifBOrjv3wLxFGKy5SqVJbRa2hcjzsio97L3l_Q6vyE_BF4r2cGG4Y2t7hprdGAKG5RH2HnQJBVwFBUlqE9I8eLCBBlDHi4ehVXLxPDnuAxUgHbPnKGweTHFX23RbWRcSeySUqwXr0PuY3tS3eeThNfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشرات المضادات الارضية تنطلق لتصدي للمسيرات القادمة من اليمن في ايلات</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77838" target="_blank">📅 00:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17295a8332.mp4?token=aS-NV3qHmmh0-W0VKwlp9nFC0GTgya76Km_5h_P66_2ECjaqU0q1keAV2gI4H880ysWGNq9mDc_11HrIiI463SsnYbQwod0_Ex0VY-GXCqXCl8Yqw8vuDgHIclGBd5ldC-8B7ZgAGL5wD5HCdNKjsDWLHdbMpdN_iHaNiXK8I67yTg-x3ep138BWZpqae7LB7QVQ_vrRjyMSLEcDvDI-aikswolXRTYNpRjr8J-2h8mWRKGxElgCqSbQ86KEi7FqhdKIUuGPKLVWFDu8f4Ss3PCM89A2Yv9xt_8Is7j2LzPwrg0D92Ttv-LnNT79MhwzzhYXP5Rz6CHm-TUSFOFmrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17295a8332.mp4?token=aS-NV3qHmmh0-W0VKwlp9nFC0GTgya76Km_5h_P66_2ECjaqU0q1keAV2gI4H880ysWGNq9mDc_11HrIiI463SsnYbQwod0_Ex0VY-GXCqXCl8Yqw8vuDgHIclGBd5ldC-8B7ZgAGL5wD5HCdNKjsDWLHdbMpdN_iHaNiXK8I67yTg-x3ep138BWZpqae7LB7QVQ_vrRjyMSLEcDvDI-aikswolXRTYNpRjr8J-2h8mWRKGxElgCqSbQ86KEi7FqhdKIUuGPKLVWFDu8f4Ss3PCM89A2Yv9xt_8Is7j2LzPwrg0D92Ttv-LnNT79MhwzzhYXP5Rz6CHm-TUSFOFmrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الصهيونية تحاول التصدي للمسيرات القادمة من اليمن فوق ايلات</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77837" target="_blank">📅 00:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcd9f0ba7.mp4?token=anZmEWVrsT66xTkVsi0Jr8TcVJQo7Mlb1o-e6gnmIff4G1314_r3QcTagO5tzZ_9LVeavwLKL_LVAvl6XkZ2GhBFnYL9mm8gcuh2Xq0RRt4S50SK_YqivqRNnex_bB4sDbuHq56FJ7khyL2ACO259MAf8fBIxaW30PZ5-EVJoqNtic7uvvmcpXU8yklS19Y_BKx1ezheXt2nj6DXwJkxGP2CzBz-sBBkGIFHKH6CjD5iw23ouI2f-1psAnpkeRAwCxE3GVC6ErjWl4LEnyHq_t0v8AHimV_c_Ad4JyhGVIfEGoEjbgkoxGHJlHwD_vYOThF6MRKjLR_f5SYAPlB-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcd9f0ba7.mp4?token=anZmEWVrsT66xTkVsi0Jr8TcVJQo7Mlb1o-e6gnmIff4G1314_r3QcTagO5tzZ_9LVeavwLKL_LVAvl6XkZ2GhBFnYL9mm8gcuh2Xq0RRt4S50SK_YqivqRNnex_bB4sDbuHq56FJ7khyL2ACO259MAf8fBIxaW30PZ5-EVJoqNtic7uvvmcpXU8yklS19Y_BKx1ezheXt2nj6DXwJkxGP2CzBz-sBBkGIFHKH6CjD5iw23ouI2f-1psAnpkeRAwCxE3GVC6ErjWl4LEnyHq_t0v8AHimV_c_Ad4JyhGVIfEGoEjbgkoxGHJlHwD_vYOThF6MRKjLR_f5SYAPlB-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسيرة من اليمن تدك معاقل اليهود في ايلات</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77836" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">طائرة مسيرة فوق مستوطنة ايلات جنوب فلسطين المحتل.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77835" target="_blank">📅 00:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
‏الأدميرال براد كوبر قدّم إحاطةً للجنة الدفاع في مجلس النواب حول أولويات العمليات العسكرية الأمريكية في الشرق الأوسط، على أن يقدّم إحاطةً مماثلةً لمجلس الشيوخ غداً.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77834" target="_blank">📅 00:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يخترق شمال فلسطين المحتلة وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77833" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
طيران مسير من لبنان يخترق شمال فلسطين المحتلة وصافرات الإنذار تدوي.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77832" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭐️
هزة ارضية تضرب الحدود الإيرانية العراقية بالقرب من مدينة حلبجة شمالي العراق.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77831" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
