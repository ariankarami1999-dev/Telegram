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
<img src="https://cdn4.telesco.pe/file/pDgYGZG-hmf7-a7_YYynH1Hm1UP4tkto-tgftya1oVN7OPKia9R70tE5aCtHC_kf3qLfy53ZhDsjVxfWfMimsEO3Y3yRDxg-zdGOKce_0LaIAE_S5buvmotGXY403fOYGiJlovNnbmasqKSfP_fEKUu-0rmDpBQJPERM-JuXiI4Sa7yPMx4IFXRdxP7AHBTCbwBZlk6rh_QHFc8u_ysPtqqPlCtqPv6_33dLCHdbrmWzjLJZr-zU-qjxKh_mFT6MFw76HHEOClAVwsN--Hg9eTQdMt90mESou_4H238WUFeqxKH7i1SvYV30UscibVs5dzd6-xFNR3v9l1uYZJla3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 01:41:10</div>
<hr>

<div class="tg-post" id="msg-89255">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامب:
إسرائيل لا ينبغي أن تقلق. هل تعرفون السبب؟ لأنني الرئيس وسأعتني بإسرائيل.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/naya_foriraq/89255" target="_blank">📅 01:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89254">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
سماع دوي إنفجارات مجهولة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/89254" target="_blank">📅 01:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89253">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRY8ca9sjyIE3gHJIlJwUG1ymIAyz5NIhWDmlqG94b8TLEC-eNNJvbI31lBKJGPHunYyMnIbAY9u6q0rYNDIfERj6omkbGXv--1BqxlEFJaWbzFOT7rmo2DUYzFxD_aOZ3RfzAOuSq5dk6vELoz6AA8ul1sAf8iftIRc-MEZ4eWxxZKBx6BELTNFDld79vUQfQBUwwfJ2zd1J5XJLd5IUguQFMUibTCn8ONIPBq5bDpNxLXCrW-Wu5cdH84o8p0G10W-K_pKF7qLKUKxhCK6y3vq2N2ApQ2WyCQO8Kx7sct-4Plj5BHET4Yqnf6JH_QXmtXuTwbG5Ec8sM633IaQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: أعلنت خرائط أبل للتو أنها غيرت اسم بحيرة أونتاريو إلى بحيرة أمريكا، وبذلك أصبح هذا التغيير المهم للغاية في الأسماء، بين خرائط جوجل وخرائط أبل، كاملاً ومصدقاً عليه وملزماً. شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/89253" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89252">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تم إطلاق صافرات الإنذار في مستوطنة نيلى الواقعة في منطقة بنيامين. وذلك بناءً على معلومات استخباراتية حول وجود مقاوم في المنطقة، تم استدعاء العديد من القوات، بما في ذلك وحدة "دوبدبان" ووحدات الاستعداد المحلية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89252" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89251">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">المراسل: إذا كنت تريد أن يثور الشعب الإيراني، فهل سترسل وكالة المخابرات المركزية (CIA) لتزويد الإيرانيين بالأسلحة؟  ترامب: لا أريد أن أقول ذلك. لن يكون من المناسب أن أقول ذلك. أنا لست ضد ذلك.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89251" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89250">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
🇸🇦
🇾🇪
بعد الحصار الايراني واليمني:
‏تراجعت صادرات النفط السعودية إلى أدنى مستوى لها في تسع سنوات، حيث تهدد هجمات على ناقلات النفط عملية التعافي.
‏بلغت صادرات النفط في البلاد حوالي 3 ملايين برميل يومياً في شهر أغسطس.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/89250" target="_blank">📅 21:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89249">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=d4Lk5dgdbAaegJUJF1mUmSoQsEqYWhoVBJcvMM3g3ze1zX0v686cwKtirWietUSsG_9mWXP3YOA1RxHRhBuoKIf3CyPlQWWG5SE9OjhLRt7iYGbr4RQAwa0dnwfas2Vso4xF6xi64E--kz3x4x8m6PiXTNweGOnShGafChn7JLnHdl6nrr_FXSwo4ixGNOy8oP2Pw-62yjVBGY-QDIDHAaTzdD05Z_0zp6TT8xz7eXVK4sBtbZTd1xxM-IVyhegMC-r-QnCR5wc4WTcRvGvS-ije9_gyNviQtHToDMwVejHyM4V2psGNIi9uU-AwYHporN9L2zBQ0lstsY16CnXAFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376c3a971.mp4?token=d4Lk5dgdbAaegJUJF1mUmSoQsEqYWhoVBJcvMM3g3ze1zX0v686cwKtirWietUSsG_9mWXP3YOA1RxHRhBuoKIf3CyPlQWWG5SE9OjhLRt7iYGbr4RQAwa0dnwfas2Vso4xF6xi64E--kz3x4x8m6PiXTNweGOnShGafChn7JLnHdl6nrr_FXSwo4ixGNOy8oP2Pw-62yjVBGY-QDIDHAaTzdD05Z_0zp6TT8xz7eXVK4sBtbZTd1xxM-IVyhegMC-r-QnCR5wc4WTcRvGvS-ije9_gyNviQtHToDMwVejHyM4V2psGNIi9uU-AwYHporN9L2zBQ0lstsY16CnXAFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب يعيد ما قاله قبل ٨٠ يوما : السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89249" target="_blank">📅 21:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
🇺🇸
‏
ترامب يعيد ما قاله قبل ٨٠ يوما :
السلطات الإيرانية تطلق النار بالرشاشات والقناصات على رؤوس المتظاهرين.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89248" target="_blank">📅 21:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية: لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89247" target="_blank">📅 21:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">▫️
مسودة تقرير لوكالة الطاقة الذرية:
لم نجر منذ فبراير  أي عملية تحقق بالمنشآت  الإيرانية المعلنة باستثناء بوشهر،فقدنا منذ يونيو 2025 القدرة على تتبع المخزون النووي المعلن بمنشآت شملها القصف.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89246" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBZ1uv5ADZDOYyAlNKHrbtWVC4Y3mwbcAw7wkELrl2ATHvvQzw4or5flaYZFtoaqjvZAuHIuU8g5CnyQY-H38d7DcWKqBjQraAKVInxT0LtsS0gan6f1vcgpSHVJC89K-KUUJibJpcMNsBVmTFss6hZvVmae7_2WmBo-XozKctaEOzi5rGO8cH1IZplUBj2LlotYRxkeQXYmZalv4sSRTPscZru9Oz7mHVubX2HT4EtFPsV8WEb3EtWA4UpLXZfoAQh4kC73beIbHlkd-EEMaKrK2nPP40dCurevUfJ7IJVN_oZ1JqII43_XYGwkaD8jxmM_8pADYf7SDYO4w14zhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
عثور على ثلاث عبوات ناسفة في وارشو عاصمة بولندا بالقرب من محطة سكة الحديد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89245" target="_blank">📅 21:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇱
🇺🇸
الاعلام العبري: ‏
بعد الهجوم، وجهت الولايات المتحدة رسالة إلى طهران عبر قطر: إذا استمرت إيران في التصعيد، فإن واشنطن مستعدة للانتقال من ضرب الأهداف العسكرية إلى ضرب البنية التحتية للطاقة والنفط.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89244" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇮🇷
المتحدث باسم الأمين العام للأمم المتحدة:
أعرب الأمين العام عن قلقه إزاء التقارير التي تفيد بوقوع ضحايا جراء الهجمات الأمريكية على إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89243" target="_blank">📅 20:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
:سنطيح بالنظام في إيران - سيسقط. جميع أنظمتنا تعمل على إسقاط النظام، إذا هاجمونا، فسيكون هذا الهجوم الأخير لهم.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89242" target="_blank">📅 20:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEdm4x1ZeCDsVYzvNjaqUaQ_cn9AyGc0hrpu3O2RYMh9wATntTM5Gc5v_-jFJmaNmor5nxtB4mGHqNz6TCgwaYh94tjoWrb0PAZDxFZxm-IiUAOg8HLo-xYoJIw-_dD6fqFR8CtmS2Zs0mn0K6xupiLKBPKyGnOWk5pCMB4kvwoYI-YAhdu6Ml-ovxkLdp42p6LXEwSBurROTyJ0DtDPS5b1fjWJHIMIirrz9Ao__11FV3qXabvSMd_nQsO6pgdjzpQJy0BK_l_Lb3Ymvx9c8dJMMVe1Vb77lyd_ohGYAF5YXHOjQkatTMr1XYrLr6v7KdDxj_Rmwq0vHgPFMOwZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
بعد 18 عامًا، تتبنى إسرائيل مسؤولية اغتيال الجنرال محمد سليمان عام 2008، وهو المستشار الأمني المقرب والأعلى رتبة لرئيس سوريا.
وصلت فرقة من القوات البحرية الخاصة عن طريق البحر وأطلقت عليه النار من مسافة قريبة، ثم اختفت.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/89241" target="_blank">📅 20:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89240">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJsYfipLr7ZA9SjJmEFeD5Vpug5hU6ARG-aEThEvjr2VA1TrrXeHPUlj7ylJd93BjwLKx9HQIOso07bxi20sh8wT1ybEElyJIqopl4uFKwehgAZLVATYw3cdYEDCjmRbT8D0xrZEj9HDelc2SVNR852Eznzdo34CAF0fKDMwbVvoT3xJwES42t88bWXBIPp3m-xmfv71ZDbhJGub_IUp-Qm3IYoyWsGIokp5Os-8luAG2bPfdKgLxEqX4FHm16HCfehlPRXPs-OzJ0EEmPcL6c2CjFHdwCI5C77-p7JAUy8w2rHE2hyd76gfxlxNAShTnnvsEtMPQ-hHIIf-GEkNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الشيخ اكرم الكعبي:
إن بقي جندي واحد بعد تاريخ ٩/٣٠ فلن نتركه يعود سالماً وسترسله إليهم جثة هامدة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89240" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇹🇷
🇮🇱
اعلام العدو عن مسؤول إسرائيلي رفيع:
لا نعتبر تركيا عدوًا إنما خصم بعد خطواتها في السنوات الأخيرة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89239" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي ماركو روبيو:
لا ينبغي لأي دولة أن تساعد إيران في التحايل على العقوبات. ولا ينبغي لأي دولة أن تساهم في إيجاد آليات تمكنها من تحقيق إيرادات تستخدمها لتمويل الإرهاب ومحاولة بناء سلاح نووي. وإذا قررت الدول القيام بذلك، فسيتعين علينا فرض عقوبات عليها أيضًا.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89238" target="_blank">📅 19:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu6j2F7-iHFh1GZyarU0HZSPEkSLqIVz7ABqutNxV9A4Cx-gP9J84lMK5gEoH2BeA26ccP3dg2XyXC1BxTvCcdVBHEaMLljiH8quck6l-q5cY3N-H18PnRbWOU0esGD6qtut1Lv06sbxQDVlXhbJis0KvNYNcXFarCU2Dv0D1x5cnkKZGGdZosC2ke6bjxzWGLAkZFE-les6-UdV2T0292lxIJ4ePfhIKBIFphMLk9S52SBIl_7m6oKd7M_s8B7quUC3mCwaiGkWJdjdG7utcxQzWjjqe1egxam-jJxekbA6R_fACcO5yzRvtRZzgnaUFKqS3-TiJK75SwoYpOzthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
‏
ترامب:
الآن وقد أصبح مضيق هرمز تحت سيطرة الولايات المتحدة، هل نغير اسمه إلى مضيق ترامب؟ مثل أمريكا نفسها، سيصبح الوضع أكثر سخونة من أي وقت مضى!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/89237" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89236">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89236" target="_blank">📅 18:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89235">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/89235" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89234">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
إذا امتلكت إيران سلاحا نوويا حينها سيُدمر نصف العالم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89234" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89233">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
ارتفاع صادرات العراق من النفط الخام إلى 2.340 مليون برميل يوميا وهو ما يعادل 71% من الصادرات النفطية قبل اغلاق المضيق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89233" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89232">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e648c65e.mp4?token=FCSU5WMIMqzzmvnsgJpKfkpNYsvfMgPCqv7i_fZatuMb_6X0BMhO4m44ylaQRs7ebe0AqBdj7rhTJVqs5-Fpuud3ff4bTAY6BsLDzGb8Ok7i9I6tdoBYRYNRGNMj-ftK-OKSP_76A-emfhepvq7b2WCF9vmKN8c5FIS71wG62koVeJaIsW033g3F-ovcgMXIewPKNkRrMTbQ7xQamYS2EGHDDzdG64YdqQ-loOk_P7-N41tEHuUHTKlua2CzKXeNBJMdYgBwc_YnBc5KXIzYuZNlkBPn2YADFGknzHqtKs8UQeWDZ2vf2Rg7mLHkHQVDXAU7iQYtu42IxRLe0pRprw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e648c65e.mp4?token=FCSU5WMIMqzzmvnsgJpKfkpNYsvfMgPCqv7i_fZatuMb_6X0BMhO4m44ylaQRs7ebe0AqBdj7rhTJVqs5-Fpuud3ff4bTAY6BsLDzGb8Ok7i9I6tdoBYRYNRGNMj-ftK-OKSP_76A-emfhepvq7b2WCF9vmKN8c5FIS71wG62koVeJaIsW033g3F-ovcgMXIewPKNkRrMTbQ7xQamYS2EGHDDzdG64YdqQ-loOk_P7-N41tEHuUHTKlua2CzKXeNBJMdYgBwc_YnBc5KXIzYuZNlkBPn2YADFGknzHqtKs8UQeWDZ2vf2Rg7mLHkHQVDXAU7iQYtu42IxRLe0pRprw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاقمار الصناعية تظهر منطقة متفحمة واسعة في مجمع عسكري أمريكي بجوار مطار أربيل الدولي في اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/89232" target="_blank">📅 18:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89230">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXKHI9Gp4QyYymLc_CXPltIZRf0rHrfJeVnR6x_AwpotaclxTlQrb0TF03U_X7QRlA97xmJHRpyuNwxkFvxDQ7loXH3yQ50pnPEEdr0-wCM2v5ycmApZ81Ut8-UkzUCdygpdYGDwZaAZ401Gb3QPNxQmpFy7wzvPfZl8ek0C295fhsBYcJyNH53shHeAb6hd3MYYjpypIKYecOnZVHqoN9FhR8jmdXghZL_CAk92YxWPE3QPAHWEN65Fe_G1ue01vd2H64HnH9ICitgoCFUCSVrKawIosAxrPay9l1HwH6UxD1scbsxcxypj9aKK5d_Yk_0_FmHHfXPK0bff4Atoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upmW_9tFFMoxbe_V7pe-5YrLfVL2ljzQOLcYDN_VAXRcxE35Xm-gm3yT3Rm9weInE1CaxD1oKaNVUS4jeUenUKcQBPtyy2am_Y1XA2Vaq3fj__STV5QIblyBA-PnsKSLuJw6Lszsq3PseJ1AkT5PruqW0sfZIGzYi0INgLbvSckby2yQlhx21FFdjnKW0zCYtU9RG0Wq3Ff-jXrWltNaobLBiglMCJhqPPGnNPTT_4Nqpw-9SKAX0QhKjM7HIv0CVrZAygY6coeOrYcYikMIZnESlhdIUUjfHKIQcYnorrihvi4Vixf39-4Aj2U2hbvskwoXHBNnnDzaL4_gVnQALA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشتباكات مسلحة داخل العاصمة الاوكرانية كييف بين منتسبي الاجهزة الامنية في البلاد
مكتب المدعي العام الاوكراني وجهاز امن أوكرانيا اتهم جهاز الاستخبارات العامة بالعمل السري لصالح روسيا وجهاز الامن الفدرالي الروسي
وشنوا الهجوم على جهاز الاستخبارات العامة وحسب المصادر عدد القتلى حاليا عند جهاز الاستخبارات وصل ٣ اشخاص للخطة الجارية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89230" target="_blank">📅 17:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89229">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حدث امني في مضيق هرمز: استهداف ناقلة نفط وإصابة شخصين كحصيلة اولية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89229" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
حرس الحدود الإيراني يصادر سفينة تحمل 382 ألف لتر من الوقود المهرب في شمال الخليج، ويحتجز 11 مشتبهاً أجنبياً.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89228" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الوكالة الذرية:
لا نعرف الوضع الدقيق لمحطة أصفهان للتخصيب ولم نجر أي تحقق ميداني في أي منشأة نووية بإيران منذ فبراير</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89227" target="_blank">📅 17:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7p--7O-aKreAH6Ey3rrf4SXUMXgENByqcx0bVyFXUxYG17gaPuY3KKYiJF-e06Ab_bOxJvVD3ZBdXlOeQVjzXh2f--uwiGCqVFfQcABtC-Ignf8LUoL7nMD0GOWrRi0r7jx62ot0K5RIPclO7ExrjboZtuIOihOtJUJuxq1ka1243toYxEDbg0O9yABl1VuD0ftYK_Pd-4ismvYdKp65BGDLZfMnx59e6XdSa9m7ZvZaZV63FXqOw_xnmqTkSuFQXFax7Etaza_q7NOpAslO8RzbiHNtHRZFEFWzge7f6OkFkthDYjSt6SPzGcNh5oNhDKZcdug3hO-01wKrmsdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
يزعم تيم هوكينز، المتحدث باسم القيادة المركزية الأمريكية، - بينما ينكر جريمة الحرب الوحشية في ‌سيريك - أن الولايات المتحدة لا تستهدف المدنيين!
‏يبدو أنه نسي سجله العسكري: كاكاراك في عام 2002، وموكاراديب في عام 2004، وديه بالا وويتش باغتو في عام 2008 - وهي هجمات أمريكية موثقة في أفغانستان والعراق أسفرت عن مقتل مدنيين، بمن فيهم نساء وأطفال.
‏لقد نسي شيئًا آخر أيضًا: حتى مسلسل Homeland، وهو مسلسل تلفزيوني أمريكي الإنتاج، صور في موسمه الرابع غارة أمريكية بطائرة مسيرة على حفل زفاف في باكستان - وهو هجوم أسفر عن مقتل حوالي 40 مدنيًا.
‏إن الحقيقة مروعة لدرجة أن الدعاية الأمريكية نفسها لم تجرؤ قط على طرح الادعاء الذي يطرحه هوكينز اليوم.
‏سيريك ليس مجرد قصة. المدنيون حقيقيون. الضحايا حقيقيون.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89226" target="_blank">📅 17:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLdTJar98zQ9tzBuWjk2SsgBIXnhFDj8CRcC50JzFOck-LQX1bcDjQUhPvsxyyDoodD-oECzqWANt6qvIe6PaPGg31kFrFP3GTfyR-4UI8uHUdUX03QfWj8OnZM2VSi8moGR5RPmy0I72GDnYTsNcsW7mvTKMchADhB-E0BtspKtNlK0JfEnMlz6VyfsOmmeRbUa3d8j3-dqOvn1Th21mLZQpmbCUqKYvQBxkYRweZWLM0hd1ECuSZGRf3WYiYktjH5sa_L1el6yyuDHt9S9XuETESjYx7NIR4O6ronHt-yFuly4zGxT2iF93Z3psFltIqhOP4bcWTGgKeoCKVjZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
الجمهورية الاسلامية الايرانية تكلف مصطفى طرفي قنصلا للجمهورية في محافظة البصرة العراقية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89225" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6900ea796b.mp4?token=Z9ey7mZ-LSbk2ZW7EBUD-wMOD_d8pE97juwq3vk-Cj59aZWoCxO2UGMVSoFXc1DPd4n-igTJQvBNQrdu24HLac6xxNPLaqtjsRtuRIjHOmjKyvZk_D26XvSdfLqXgjGZCi_oqPiBxokXNEQLh--frKjRI9JZHhMyvQX6iFHbnb4D2nOKPxDR0Xt_-N39QppXvgDaMz8Ta9K70I1UO4PsswwNhMfR38bRXylfaGmT0yLTrV1bOaBir7oBMdoVzGxpGmsQtFgzi2b_DWlvKM8AiK0muENn6NlJNilkF0Mx6cxyghMS-bB4bNj9t6WJP_GytXnpzUB8QN2zikbZITicoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6900ea796b.mp4?token=Z9ey7mZ-LSbk2ZW7EBUD-wMOD_d8pE97juwq3vk-Cj59aZWoCxO2UGMVSoFXc1DPd4n-igTJQvBNQrdu24HLac6xxNPLaqtjsRtuRIjHOmjKyvZk_D26XvSdfLqXgjGZCi_oqPiBxokXNEQLh--frKjRI9JZHhMyvQX6iFHbnb4D2nOKPxDR0Xt_-N39QppXvgDaMz8Ta9K70I1UO4PsswwNhMfR38bRXylfaGmT0yLTrV1bOaBir7oBMdoVzGxpGmsQtFgzi2b_DWlvKM8AiK0muENn6NlJNilkF0Mx6cxyghMS-bB4bNj9t6WJP_GytXnpzUB8QN2zikbZITicoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89224" target="_blank">📅 16:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89223" target="_blank">📅 16:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3j1TahFvmIUZHZO0cjNjzEdLzU5wwvGpSTQmzXJg70IjvkLaR8duDaA-dnktbn_qGBcjFb83yMAY3rd1EaOkUThJMDgDaxSfUh_L-5j36-9qX7eCrJmheoPtJ2ZwGQ77Ov9pWzyiFqPsckIDIaWOcx4EbeZo4CKjkLe9XA8AmTMUpXK-NaFjIqw3RYWy4VzTBiUG2MfazbxNZfAO8Zb3h7nwhCn9NC8u_VifHao7pS3E6K6LDnJCGZt-aUvhEwxTbca8giD2odaLpw5TAEwdybntmRlgRpCub6gM0OiZm3iCx4ngm4BtRTLQlBN-6b4Ch5pVSWbaie0eDAvJ-IqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
بيان وزارة الخارجية الايرانية بشأن العدوان العسكري الأمريكي والرد الدفاعي الإيراني:
تدين وزارة الخارجية بأشد العبارات الأعمال العدوانية التي ارتكبتها الولايات المتحدة مساء الثلاثاء 10 شهريور بحق وطننا العزيز، وتؤكد عزم الجمهورية الإسلامية الإيرانية على الدفاع الحازم عن استقلال إيران وسيادتها الوطنية ووحدة أراضيها.
إن النظام الأمريكي، الذي أصابه العجز في مواجهة العزم الحديدي للشعب الإيراني في الدفاع عن كيان إيران، شنّ مساء الثلاثاء 11 شهريور 1405، مرة أخرى، هجوماً على عدة مناطق مدنية ومنشآت خدمية، من بينها عدد من أبراج ومواقع الاتصالات، في محافظات خوزستان وسيستان وبلوشستان وهرمزغان وكرمان، في انتهاك للسيادة الوطنية ووحدة الأراضي الإيرانية، ما أسفر عن استشهاد وإصابة عدد من مواطنينا، وإلحاق أضرار بالممتلكات العامة والخاصة.
وفي هجوم للعدو الأمريكي على حفل زفاف في منطقة كوهستانك التابعة لقضاء سيريك في محافظة هرمزغان، استشهد وأصيب أكثر من 70 من مواطنينا، وكان معظمهم من النساء والأطفال.
إن هذه الجرائم الوحشية التي تشكل انتهاكاً صارخاً للمبادئ الأساسية للقانون الدولي، تذكّر بالجرائم الأمريكية-الصهيونية السابقة خلال العام والنصف الأخير، ومنها الجرائم في ميناب ولار.
ورداً على العدوان العسكري الأمريكي، قامت القوات المسلحة للجمهورية الإسلامية الإيرانية، استناداً إلى حقها الأصيل في الدفاع المشروع، بتوجيه ضربات دفاعية ومدمّرة إلى القواعد العسكرية الأمريكية التي كانت منطلقاً وداعماً للعدوان العسكري الأمريكي على كيان إيران.
وتطالب الجمهورية الإسلامية الإيرانية دول المنطقة، بصورة مؤكدة، بمنع المعتدين الأمريكيين من استخدام إمكاناتها وأراضيها للتخطيط وتنفيذ العمليات العدوانية ضد إيران، والحيلولة دون استمرار واتساع نطاق نيران الحرب في المنطقة، وعدم السماح بتحقق المؤامرة الأمريكية-الصهيونية المشؤومة الرامية إلى فرض انعدام الأمن الدائم على المنطقة.
وتتقدم وزارة الخارجية بالتعازي باستشهاد مواطنينا الأعزاء، وتذكّر بمسؤولية جميع الدول عن ملاحقة ومحاكمة ومعاقبة مرتكبي ومنفذي الانتهاكات الصارخة للقانون الدولي الإنساني.
كما تذكّر وزارة الخارجية، مرة أخرى، بمسؤولية منظمة الأمم المتحدة، ولا سيما مجلس الأمن والأمين العام للأمم المتحدة، تجاه أداء واجباتهم وفق ميثاق المنظمة. وسيؤدي الصمت والتقاعس العملي لأركان الأمم المتحدة في مواجهة الانتهاكات المستمرة للمبادئ والقواعد المنصوص عليها، ولا سيما البند 4 من المادة 2، من جانب عضو دائم في مجلس الأمن، إلى مزيد من فقدان المنظمة لمصداقيتها، وسيشكل تهديداً متزايداً للسلام والأمن الدوليين.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89222" target="_blank">📅 16:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd743adb9.mp4?token=lgFyb_EveSFRjgDH-73Kyv3ZJfphxAV-mKHp62OW1TzzKy3_O18cHtm0Sq365ssuEGjRwQWFVmMTM5I5HfkDEqgRcfyBBDat19wLMyF6-_snhXIo5edr_SeCRa4yOnHqx0UVL1l_4qUuDGjWuFIcrd1sNh9FXvfPvBUes6j0pWB3YygAmw5bnERqFkUSwOAF7MaVn_2LPYC_urhOMk0-d8eqfiSntuc8XKxy_Z45g9ZciavazbktlrKORyC9Hv7EUf2hG8slyl5IFFiDWuSXBH_hQ1FDdEMHB_l0XZUimoxOUSA4M7vWey2SDiPEIhlNvnaBk61dpv8-8fUyl3YFLzhMLCPTOMrvVUcAAMYGxzujG3yohzgvIxtZuvWhc0ccLbm0XBK7y-eGVvTGR32X781_Ov2ltLH7arQ7PhsfZJq00WdjXgfpBybyRtffWfAMnU9O-wIz9HXPVkmL8xI8sbpLL7PUkVIQivsUI525abKLBk4RA-y75WCvVHHlMH-gZEATSazB1HvyWcwIRvR6c7J-8IoqLWmxuzvdr7KumGyXeZ__GMW9B0eJdwFiM3rzNS4C4Qbj1s7dPD8HQUkwrAH9IO57CC-bZn9bsCqFLjJcMbFQ0iNNrL2ZIufB-prdtFKwKHeCRpc6hPFpE4JTvQEc4JwKSBZPYLnn7do71wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd743adb9.mp4?token=lgFyb_EveSFRjgDH-73Kyv3ZJfphxAV-mKHp62OW1TzzKy3_O18cHtm0Sq365ssuEGjRwQWFVmMTM5I5HfkDEqgRcfyBBDat19wLMyF6-_snhXIo5edr_SeCRa4yOnHqx0UVL1l_4qUuDGjWuFIcrd1sNh9FXvfPvBUes6j0pWB3YygAmw5bnERqFkUSwOAF7MaVn_2LPYC_urhOMk0-d8eqfiSntuc8XKxy_Z45g9ZciavazbktlrKORyC9Hv7EUf2hG8slyl5IFFiDWuSXBH_hQ1FDdEMHB_l0XZUimoxOUSA4M7vWey2SDiPEIhlNvnaBk61dpv8-8fUyl3YFLzhMLCPTOMrvVUcAAMYGxzujG3yohzgvIxtZuvWhc0ccLbm0XBK7y-eGVvTGR32X781_Ov2ltLH7arQ7PhsfZJq00WdjXgfpBybyRtffWfAMnU9O-wIz9HXPVkmL8xI8sbpLL7PUkVIQivsUI525abKLBk4RA-y75WCvVHHlMH-gZEATSazB1HvyWcwIRvR6c7J-8IoqLWmxuzvdr7KumGyXeZ__GMW9B0eJdwFiM3rzNS4C4Qbj1s7dPD8HQUkwrAH9IO57CC-bZn9bsCqFLjJcMbFQ0iNNrL2ZIufB-prdtFKwKHeCRpc6hPFpE4JTvQEc4JwKSBZPYLnn7do71wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مع قرب الانتخابات نتن ياهو يحاول جاهدا للفوز ويصل قطاع غزة: نحن نسيطر على 60٪ من قطاع غزة، وما زال هناك المزيد ولن نخرج من القطاع.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89221" target="_blank">📅 16:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ملك الاردن يعلن تغيير رئيس هيئة الاركان المشتركة بعد فشل السابق في التصدي للصواريخ والمسيرات الايرانية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89220" target="_blank">📅 15:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأميركي:
نجري محادثات شاملة مع كل من يدعم إيران. رسالتي إلى الجميع هي أن يبتعدوا عن إيران</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89219" target="_blank">📅 15:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">في خبر غير مهم
▫️
‏السعودية تدين استهداف إيران لناقلتها المسماة بـ"سدر" خلال عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89218" target="_blank">📅 14:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">في خبر غير مهم
▫️
‏السعودية تدين استهداف إيران لناقلتها المسماة بـ"سدر" خلال عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89217" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏سعر الغاز الأوروبي يرتفع الى أعلى مستوياته منذ 3 أعوام بسبب تصاعد التوترات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89215" target="_blank">📅 13:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b99536758.mp4?token=VRMQBqnpvU26-x3_r-eZPPiyWT8-9itAR24zm0tRGenbkjkjkzhRyd2uy6egG0RY1fH7cVjnGB_lL25irFWbOAz0TswN6grDdrw7lm3u5W-ljMkvhmvB7mxxUWkRns57a-j4SysHRSpR_5fMOr81TUY3bzOdV4KFejIAsgTHbvwvpU0PDm-kIVZyxIHHIhHgPq82VtDHlpBLqfYS-JORA4cECpA8DPxUbSQr2w1PikdChlsi1huDL0kwWNqH-TsSo3x7wZnB6K3tih0PW6CObHzMaHGia45EcMYvG7l75mqPkRNcs-Ib4-J9d0y81P_rJADJ0HzSv3nTM-0Y4aRnFKOWwGLANT_mXY_MuLw8U0ZcyCEoKeXZHadgGHTb_2a3OJC_a9Z_H63XSjjMCfSy1Vx_drsyylx4jYhxVuWHxGampQbtdaWXo80ebpcvSxqslJXUQxjuLGvtDD4Z8CnyM2SZhOaVZlpjt5ejnKmKLzdpCYn-7vzxtEHVUW4a30-rolXMs-pW49fGaPc1SOag-mDqSwLmGiryzn9GYTJPg6U-3qEXz3cqpiO7zA4e3KEtpmvewugfSCgXYU4yIRipFzvNXB9VJgocPdB-zupXH1JgK0Z8LjPDfsUHlFNQXN0w-UoIEX07eXiEslTrxB47RFt1ElnjCGLEpWGlUk4VVHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b99536758.mp4?token=VRMQBqnpvU26-x3_r-eZPPiyWT8-9itAR24zm0tRGenbkjkjkzhRyd2uy6egG0RY1fH7cVjnGB_lL25irFWbOAz0TswN6grDdrw7lm3u5W-ljMkvhmvB7mxxUWkRns57a-j4SysHRSpR_5fMOr81TUY3bzOdV4KFejIAsgTHbvwvpU0PDm-kIVZyxIHHIhHgPq82VtDHlpBLqfYS-JORA4cECpA8DPxUbSQr2w1PikdChlsi1huDL0kwWNqH-TsSo3x7wZnB6K3tih0PW6CObHzMaHGia45EcMYvG7l75mqPkRNcs-Ib4-J9d0y81P_rJADJ0HzSv3nTM-0Y4aRnFKOWwGLANT_mXY_MuLw8U0ZcyCEoKeXZHadgGHTb_2a3OJC_a9Z_H63XSjjMCfSy1Vx_drsyylx4jYhxVuWHxGampQbtdaWXo80ebpcvSxqslJXUQxjuLGvtDD4Z8CnyM2SZhOaVZlpjt5ejnKmKLzdpCYn-7vzxtEHVUW4a30-rolXMs-pW49fGaPc1SOag-mDqSwLmGiryzn9GYTJPg6U-3qEXz3cqpiO7zA4e3KEtpmvewugfSCgXYU4yIRipFzvNXB9VJgocPdB-zupXH1JgK0Z8LjPDfsUHlFNQXN0w-UoIEX07eXiEslTrxB47RFt1ElnjCGLEpWGlUk4VVHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد سعيدي، أمين لجنة الأمن القومي في مجلس الشورى: يجب أن يعلم العدو أن الجمهورية الإسلامية الإيرانية سترد بقوة على أي إجراء جديد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89214" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇹🇷
أردوغان:
يجب ألا يُفسر موقف تركيا بشأن العضوية في منظمة شنغهاي للتعاون على أنه تحول عن الغرب. هدفنا هو زيادة نفوذنا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89213" target="_blank">📅 13:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شبكة NBC الامريكية:
ايران تشن هجمات إلكترونية على بنية تحتية أمريكية مختلفة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89212" target="_blank">📅 13:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇦
انفجارات في كييف.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89211" target="_blank">📅 13:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مضحك
🇮🇱
اعلام العبري:
توجيه تهمه لجندي في جيش العدو الاسرائيلي بالانضمام لداعش.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89210" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نايا - NAYA
pinned «
🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/89209" target="_blank">📅 12:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89208" target="_blank">📅 12:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d68394667.mp4?token=ttSZOGgZx9S8hyES5avGuhtLNocA6ccqE_negXG5PzMI_qc3FBkb2dinqbCSQpvbYyGw-63kRjMeSnDko_4Poc95rsGh_Ri4zFFfWb64LaTi58F5cVjL_xUgduDmhKM0QTahxr8ATdbE51HqWVAHLg_o07ojIi5clEpgT4MjNOmd9Kb9mbBSyL0kG-M45LPLokmvfYMcWeH65WLDhfraL7XyudLWSSCQ0ax_XFBPS96taNjGOz4RD8cFDTOi7Yl5OS2PRK_MNkw2CfNKzy2X-Edmj1sjRs0yDHNOgjC48mkBksn0rRInVxxlhCUiEnYpQj0qR1xheD8z4K3_tilawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d68394667.mp4?token=ttSZOGgZx9S8hyES5avGuhtLNocA6ccqE_negXG5PzMI_qc3FBkb2dinqbCSQpvbYyGw-63kRjMeSnDko_4Poc95rsGh_Ri4zFFfWb64LaTi58F5cVjL_xUgduDmhKM0QTahxr8ATdbE51HqWVAHLg_o07ojIi5clEpgT4MjNOmd9Kb9mbBSyL0kG-M45LPLokmvfYMcWeH65WLDhfraL7XyudLWSSCQ0ax_XFBPS96taNjGOz4RD8cFDTOi7Yl5OS2PRK_MNkw2CfNKzy2X-Edmj1sjRs0yDHNOgjC48mkBksn0rRInVxxlhCUiEnYpQj0qR1xheD8z4K3_tilawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تم رصد حريق في مجمع عسكري أمريكي بالقرب من مطار أربيل الدولي.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89207" target="_blank">📅 12:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOST_WVnlZnrbixFD0aQGgglbbMInIsMbhVxi83fn-5YBGL4r4M4Ep0gCtIZIhA1XuA-LL1UGAOYEKDKxcm9eMQyyR9pQgIc5xj80wvGc6ST7FwMnBi7odKbfsMz1YjRocCY8KHByXINot42Af8kpaQp2wAgYvo5cpmKp98LYVlCTXupB5XN5lmPHuaYkz14Pm1d8NKR0ZvTP1OzCGWy9bZnW4sbYsNOEDo0NWBvuBpWgs_aCEoGEQutqf9q_T2OiRTiuFKY6O5cchJ01h61A4oyPf0wC-UU6nNCSQR0Q_ZnWTMZQaU88UvRw0qeut1hm0AHCx5oYxK7SpS5HQ4ZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
مروحية اميركية تطلق نداء استغاثة فوق الامارات.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/89206" target="_blank">📅 12:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
الحرس الثوري:
تم تفجير ناقلتين نفطيتين انتهكتا القانون وإيقافهما بعد اصطدامهما بلغم. سيتم مضاعفة العقوبات على شركات الشحن التي تنخدع بالولايات المتحدة بدلاً من اتباع الإجراءات القانونية.
العلاقات العامة للحرس الثوري الإسلامي:
بسم الله، قاسم الجبرين
وقاتلوهم حتى لا تكون فتنة و تكون الدين لله
يا شعب إيران الإسلامي الباسل الصامد، لقد ألهم صمودكم في الميدان الأمم، والعالم يشهد عملية إيقاظ الشعوب وتضييق الخناق على القوى الإجرامية المتغطرسة.
الليلة الماضية، كرر جيش أمريكا الإرهابي سيناريو الترهيب الذي نفذه مراراً وتكراراً في عدوانه على دول مختلفة، وهو مهاجمة حفل زفاف لإظهار قسوته ووحشيته وإرهاب الناس. غير مدركين أن الشعب الإيراني ليس شعبًا يخشى هذه الألاعيب، وأن هذا ليس عصر إذلال الأمم وخضوعها. لقد استيقظ العالم، وهذا القرن هو قرن إرادة الأمم في الانتصار.
بهذه المناورات الوحشية، لن يضعف تحكم قواتنا في مضيق هرمز.
أود إبلاغكم، أيها السادة، أنه قبل ساعات قليلة، انفجرت ناقلتا نفط، حرضهما الجيش الأمريكي على إنزال طاقميهما ووضعهما في أيدي عملاء أمريكيين لعبور طريق غير شرعي، وتوقفتا عند مرورهما فوق لغم بحري، وهما الآن تحترقان.
وكانت البحرية التابعة للحرس الثوري الإيراني قد حذرت سابقًا من مخاطر العبور عبر ممر ملغوم، بالإضافة إلى ذلك، تم التخطيط لعقوبات إضافية لشركات الشحن التي تقع ضحية حيلة الولايات المتحدة وتضع سفنها تحت تصرف العدو بدلًا من اتباع المسار القانوني، وسيتم تنفيذ هذه العقوبات قريبًا.
والنصر من عند الله وحده، العزيز الحكيم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/89205" target="_blank">📅 11:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">أسعار الغاز الأوروبي تلامس 74 يورو للميغاواط/ساعة مقتربة من  ذروتها مع استمرار اغلاق الجمهورية الاسلامية لمضيق هرمز.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89204" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
🇺🇸
وزير الحرب الصهيوني:
مستعدون للدفاع والهجوم بتنسيق كامل مع أميركا.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89203" target="_blank">📅 11:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89201">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات جديدة تهز الكويت</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89201" target="_blank">📅 09:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89200">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🇷🇺
🇩🇪
تشك الشرطة الألمانية في عملية تخريب بعد حادث متعمد في محطة كهرباء فرعية في بيرغهايم أدى إلى تعطل عدة خطوط نقل وتعطيل منشآت ريفا . وأفاد السكان بسماع انفجارات ورؤية ومضات خلال الليل.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/89200" target="_blank">📅 09:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89199">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🇷🇺
🇩🇪
تشك الشرطة الألمانية في عملية تخريب بعد حادث متعمد في محطة كهرباء فرعية في بيرغهايم أدى إلى تعطل عدة خطوط نقل وتعطيل منشآت ريفا . وأفاد السكان بسماع انفجارات ورؤية ومضات خلال الليل.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89199" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇷🇺
عمدة موسكو :
تدمير 3 مسيّرات أخرى كانت متجهة نحو موسكو</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89198" target="_blank">📅 08:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f8e598b.mp4?token=ZDzk0ROx8iM1wy4ZvWC55iK9CVccR2FaH0jl8cXcUcIM7nZWzaG9__1jw3F53O7JBzKPKPqueGzPZ8UOwCb6myNKd1q2L4vjhBirpdB1crCe7IzRBnFWnAWw8FcBFaDZXWol7H4hPBFVmEyJJegWomaYtmL73EBPOcRqOBMSXGlA0Y0TnHtUVajlUxTefEVBjSqD7wwqzOZaQywixRiLdE0edyqh2Ofv03S4qs6_JbLSpbmI72RIiDhhw4sSt0gQzbqgCZDiEUCjC03xjsmkkLninPbX_XtM4rP9Xh1RqyEYvSE4Nmo950p-GeImyjaRfHPeQ6gJiJtI_843X2eEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f8e598b.mp4?token=ZDzk0ROx8iM1wy4ZvWC55iK9CVccR2FaH0jl8cXcUcIM7nZWzaG9__1jw3F53O7JBzKPKPqueGzPZ8UOwCb6myNKd1q2L4vjhBirpdB1crCe7IzRBnFWnAWw8FcBFaDZXWol7H4hPBFVmEyJJegWomaYtmL73EBPOcRqOBMSXGlA0Y0TnHtUVajlUxTefEVBjSqD7wwqzOZaQywixRiLdE0edyqh2Ofv03S4qs6_JbLSpbmI72RIiDhhw4sSt0gQzbqgCZDiEUCjC03xjsmkkLninPbX_XtM4rP9Xh1RqyEYvSE4Nmo950p-GeImyjaRfHPeQ6gJiJtI_843X2eEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
Trump’s Target Bank;  For Those Asking Where U.S. Taxpayer Money Is Being Spent?!
Naya exclusively publishes video footage showing CENTCOM  target bank in the Iran “ Serik” , and how a wedding ceremony has become one of the targets of the U.S. military.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89192" target="_blank">📅 08:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
جريمة حرب أمريكية في مدينة سيريك جنوبي إيران، حيث إستهدفت حفل زفاف بقنابل شديدة الإنفجار، لتخلف 5 شهداء وعدد كبير من الإصابات حتى الأن، بينهم الكثير من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89191" target="_blank">📅 08:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇱
🔻
معاريف :  أطلق حزب الله طائرة مسيرة باتجاه الشمال: تقييم الجيش الإسرائيلي - إيران وافقت على هذه الخطوة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/89190" target="_blank">📅 07:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
🇺🇸
رويترز :
الأسواق الآسيوية تتراجع بشدة مع ارتفاع أسعار النفط وعوائد السندات بسبب القتال بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89189" target="_blank">📅 07:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89187">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5HySqNFdPt26Ajld_JB8x-BEdsvbfJWzqudpI3xI2kyW9ksGtruOAAondLue-mjkT3Ar-UFPVPgm4yyy_e90kaluohm2HyaS4Oc1lzagQcjr80uGtbNFy6ocHJ56nAmAfkNjFaOdhiPkzk6ASVWLAWt6TTf579r8nGTQ3Qz1C0g90OFSC3eBQYeYnSFNk38yuOVr0PnFnl7DMJkMbNvq7y44szZ-XLdTGysmkjQ1ppoecZ6rybnLUfi8y3IfEtXhR-iIPGRLFcwpU-YxRR9_RS_myF7Dc8wsb_s1CuWfMhgE09rUvkAof3FKi-hPUVI1y64HK8S-7knPbTI5VWvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
Save this song
🎧</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89187" target="_blank">📅 07:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89186">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89186" target="_blank">📅 06:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89185">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89185" target="_blank">📅 06:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89184">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عدوان أمريكي على نقاط في محيط مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/89184" target="_blank">📅 06:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89183">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوي انفجار في شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89183" target="_blank">📅 05:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89182">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83359493e.mp4?token=McTENATpqgkzqZgXGuDTMdyMyK5AsiOiUFyAOROkS-2yqbM0IJMNY7-yZr7sGPi6EwyzHfw9wDijHHCY-C3ETSXLzEQ6BXjO2vUl4czUX2X_7ohcrW7_ILu64Zy5HjIsPQ3PJ_PX6gNflOpBjenWfetV0y0MNp1ZZf87m6Wi73kWAn57dMQ5FP-6TGhJquA_nxaCjWyWklwBfoU55JFvf8OJ5IpPB_zCh0m0RU3qOi0w8SXxmBNxareuVD2kjAQQq54n0L24zB5wR5z9uiIfiqRl3qas3J5NXbVx4gNww0yE5VMvT_yLK-awyPbUZ6iVjyza8tMIqQdQVfWrMrEpyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83359493e.mp4?token=McTENATpqgkzqZgXGuDTMdyMyK5AsiOiUFyAOROkS-2yqbM0IJMNY7-yZr7sGPi6EwyzHfw9wDijHHCY-C3ETSXLzEQ6BXjO2vUl4czUX2X_7ohcrW7_ILu64Zy5HjIsPQ3PJ_PX6gNflOpBjenWfetV0y0MNp1ZZf87m6Wi73kWAn57dMQ5FP-6TGhJquA_nxaCjWyWklwBfoU55JFvf8OJ5IpPB_zCh0m0RU3qOi0w8SXxmBNxareuVD2kjAQQq54n0L24zB5wR5z9uiIfiqRl3qas3J5NXbVx4gNww0yE5VMvT_yLK-awyPbUZ6iVjyza8tMIqQdQVfWrMrEpyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات صهيونية عنيفة على منطقة دوحة كفررمان بجنوب لبنان.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89182" target="_blank">📅 05:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89181">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية إختراق طيران مسير قادم من لبنان.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89181" target="_blank">📅 04:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في شمال فلسطين المحتلة خشية إختراق طيران مسير قادم من لبنان.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89180" target="_blank">📅 04:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات جديدة تهز البحرين في هذه الأثناء</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89179" target="_blank">📅 04:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89178">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89178" target="_blank">📅 04:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89177">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLfXlUZbwIYrEEm2Mv8TKWJvx9eEgb3x5GCNz-0KCmwXRwZ7MPNlADkcIFUYolqW_E6zky8gDIiDjcP8yT90qFdFptK4To9Ufny_IjXJIh-bEsEziSWtYUGr2uqjxDZfBpr2WUAihw0d95O_zE6JoTdAF0iFdH8qNtdTsKPTbzJ5DYK_idAq27pmZnnmhBLjbWNxlrTLDn76JuzLGD900jhkp6I2ark0nLoWZ2PTQE1xHWopA4ihF7usI4Hs5_g53ZrkbsVtgSRReH2WeEuEebcyFXyk_oFg7tXSvWyQemYSH2XCeLWEamLoMDXMt3nbFpC2Gxaw7-3KjBxZ0kQeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أنا لا أحاول إجبار إيران على الجلوس إلى طاولة المفاوضات، كما ذكرت قناة ABC الإخبارية الكاذبة. لا يهمني إطلاقًا ما إذا وقعوا على اتفاقية لا قيمة لها بالنسبة لهم. أنا أفضل وضعنا الحالي بكثير، مع سيطرة شبه كاملة على مضيق هرمز، واقتصادهم ينهار تمامًا. إنهم فقط يجسدون ما لا مفر منه. متى سينتفض الشعب الإيراني ويقاتل؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89177" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89176">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgHmE2RjHEdAPz0aJRJKGj4X43m8j72MUcyRaWOZMS9CYgAJAXapQPn0Szg8sfs9yjRmv5F-oY5sYeY1htWnWf2TAKeXk5tO-l12lIsDAkX_efLqgkVme8WsNSfR8IZVdn_ogXy0tQUcuJUZssmB6wmHh-Yxi_FEKAHmbt6Jgxawg-xkAO14ViIFqFD5ZvKagb4ogX_5T5BpCn1ScxWEWIF3oRIgv0GA2skvKLxnjHeqRXKW2DwsfzquetUkbWTlacxp7gv1C3SoMJYstP-7m_SMBJ7eeKFiB-M2T-sMu-8enAKaFsDkwBqZkXQJb8Nifw9lnFewsSgOeES8cGykQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النفط يلامس 97 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89176" target="_blank">📅 04:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89175">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89175" target="_blank">📅 04:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d9d5c89e.mp4?token=Pqh2v0IEv7EWH6to00bJvleaKTmI4sjJQa7jPT5BKUOi2Z7mooaUV-Eyr1dGKqfW1h9rx9_s4vhpri2WPe0ED2W5DYNDXu-4DvzjA34EtZkolFcOPDMd14Art2mv3A77oIov6wc9S1Bt6Eul-azUA5GpubcRpYYNfN7vdOgxyvrdwlYCq3GjBcvvwcHoWuh2FJD0EA3wj-OBd7Qrev33WQxHe7kHNYEkVQ6rmF4EYHwk_Gko5Yd2pwc_NYXtxqKONwd9-YgEFOcOLBKKHwgMSipWzukAytR_6KAWXbhwLtBReDutAC5ZqYsnxfo8FK0AU8O_L8EexNLVH4sAdAS9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d9d5c89e.mp4?token=Pqh2v0IEv7EWH6to00bJvleaKTmI4sjJQa7jPT5BKUOi2Z7mooaUV-Eyr1dGKqfW1h9rx9_s4vhpri2WPe0ED2W5DYNDXu-4DvzjA34EtZkolFcOPDMd14Art2mv3A77oIov6wc9S1Bt6Eul-azUA5GpubcRpYYNfN7vdOgxyvrdwlYCq3GjBcvvwcHoWuh2FJD0EA3wj-OBd7Qrev33WQxHe7kHNYEkVQ6rmF4EYHwk_Gko5Yd2pwc_NYXtxqKONwd9-YgEFOcOLBKKHwgMSipWzukAytR_6KAWXbhwLtBReDutAC5ZqYsnxfo8FK0AU8O_L8EexNLVH4sAdAS9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات جديدة تهز أربيل</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89174" target="_blank">📅 04:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
مسؤولون أميريكيون: ‏ الجيش الأمريكي يهاجم ناقلتين تابعتين للحكومة الإيرانية.  ‏سنستهدف ناقلة نفط إيرانية مقابل كل سفينة تهاجمها إيران.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89173" target="_blank">📅 04:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">إنفجارات قوية تهز محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89172" target="_blank">📅 04:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
تحذير من المتحدث باسم مقر خاتم الأنبياء المركزي:  بسم الله الرحمن الرحيم.   الجيش الإرهابي القاتل للأطفال الأمريكي، بعد سلسلة من الإخفاقات في الحرب المفروضة على إيران الإسلامية، وهزيمته أمام شعبنا الصامد والمقاوم في وطننا العزيز، قام بشن غارات جوية وحشية…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89171" target="_blank">📅 04:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إنفجارات جديدة تهز أربيل</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89170" target="_blank">📅 04:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89169">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
مسؤولون أميريكيون:
‏
الجيش الأمريكي يهاجم ناقلتين تابعتين للحكومة الإيرانية.
‏سنستهدف ناقلة نفط إيرانية مقابل كل سفينة تهاجمها إيران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89169" target="_blank">📅 03:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89168">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
تحذير من المتحدث باسم مقر خاتم الأنبياء المركزي:
بسم الله الرحمن الرحيم.
الجيش الإرهابي القاتل للأطفال الأمريكي، بعد سلسلة من الإخفاقات في الحرب المفروضة على إيران الإسلامية، وهزيمته أمام شعبنا الصامد والمقاوم في وطننا العزيز، قام بشن غارات جوية وحشية وقصف على بعض المواقع العسكرية والمدنية في المناطق الجنوبية من إيران، مما أدى إلى استشهاد وإصابة عدد من المواطنين الأبرياء.
في رد فعل على هذه الجرائم والأعمال الإرهابية، قامت القوات المسلحة للجمهورية الإسلامية الإيرانية، بفضل أبناء الشعب الشجعان في الجيش الباسل والحرس الثوري الشجاع، بشن هجمات قوية ومؤثرة بالصواريخ والطائرات المسيرة على المواقع الأمريكية الإجرامية في المنطقة، مما أدى إلى تدميرها وإلحاق أضرار جسيمة بالبنية التحتية والمرافق والأسلحة والمعدات، وأدى أيضًا إلى مقتل أو إصابة عدد كبير من القادة والجنود الأمريكيين.
ستستمر هذه العملية الهجومية كدرس قاسٍ للأمريكيين حتى يندموا على جرائمهم.
نحذر من أن استمرار أفعال الأمريكيين الشريرة في المنطقة سيواجه ردود فعل أشد وأوسع وأكثر تدميراً، وأن أي دولة تتعاون مع الجيش الأمريكي المعتدي يجب أن تتحمل عواقب ذلك الخطيرة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89168" target="_blank">📅 03:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89167">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات في الأردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89167" target="_blank">📅 03:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89166">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e0d9f677.mp4?token=vR92xnsRAoy3HTDjB2GClxtVBs7vPJMYmDFYoGR2TtgDp2IAcBk0zHsvV7Wl9O_ZWdEdQzN76nm8dmYxYYn5Lk5d_LlunYs97GxdQYeq6AxERu5r0fleH0PM2ZOYrz5DMRZu4yLfxGyvOUKlvZrc1BC4Uw1MhlxFxJ7O0bs9fs3swVNF0SXFMA_m837mfSrXTC6zYWF2tI4GAWcjQ7STSJQ6AOdLLm81Ho2jk-RwjA5vSCYVTOqJwG8WIc1hUPV9t3dFGVRGZqBp6vbv5AG3xBnBKBFLTWayaj2oBsS44sJ85y2-Y6gLcwZ_96TWtq9HwOaekCUGT1nFCFkLyJPDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e0d9f677.mp4?token=vR92xnsRAoy3HTDjB2GClxtVBs7vPJMYmDFYoGR2TtgDp2IAcBk0zHsvV7Wl9O_ZWdEdQzN76nm8dmYxYYn5Lk5d_LlunYs97GxdQYeq6AxERu5r0fleH0PM2ZOYrz5DMRZu4yLfxGyvOUKlvZrc1BC4Uw1MhlxFxJ7O0bs9fs3swVNF0SXFMA_m837mfSrXTC6zYWF2tI4GAWcjQ7STSJQ6AOdLLm81Ho2jk-RwjA5vSCYVTOqJwG8WIc1hUPV9t3dFGVRGZqBp6vbv5AG3xBnBKBFLTWayaj2oBsS44sJ85y2-Y6gLcwZ_96TWtq9HwOaekCUGT1nFCFkLyJPDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف بالون تجسسي أمريكي في سماء أربيل بواسطة مسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89166" target="_blank">📅 03:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89165">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استهداف بالون تجسسي أمريكي في سماء أربيل بواسطة مسيرات الإنتحارية</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89165" target="_blank">📅 03:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969bbbd207.mp4?token=V-cKWZM1_UPVgTe5MjTcHpwJWuMV-wFDZIAM31UfVwaendKsMhROj7liM4ZT1Dipiuol_pmuzOtY8UCYwK39gSwk1-ZPjIwk1iw-p_ErfY1w5nLiWj0cpxyVsONhr6mrB5R6idygF4I9F1u4Ym-A42TVSKwCdr8_Fl0PyT9AN1xpETtDV8vSO6O2RiGVkS9EcOyYbON8-OUWWqRlsTj_ZC2zNOKL6mmZwH9ltAxhuA45DGMkJlSA1dZsXZAJWVxA8FYCT54XPAWZTs0ANKbHsJU69BGGsAUSI3jK0JQ3eN_OcTlX7gThxrRu9tEbjaSDoKpcsuoP38xeypEzEVyrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969bbbd207.mp4?token=V-cKWZM1_UPVgTe5MjTcHpwJWuMV-wFDZIAM31UfVwaendKsMhROj7liM4ZT1Dipiuol_pmuzOtY8UCYwK39gSwk1-ZPjIwk1iw-p_ErfY1w5nLiWj0cpxyVsONhr6mrB5R6idygF4I9F1u4Ym-A42TVSKwCdr8_Fl0PyT9AN1xpETtDV8vSO6O2RiGVkS9EcOyYbON8-OUWWqRlsTj_ZC2zNOKL6mmZwH9ltAxhuA45DGMkJlSA1dZsXZAJWVxA8FYCT54XPAWZTs0ANKbHsJU69BGGsAUSI3jK0JQ3eN_OcTlX7gThxrRu9tEbjaSDoKpcsuoP38xeypEzEVyrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89164" target="_blank">📅 03:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPTDPix-OdXL_jn20xD2bkgesn-3oUsEjkwaw_AUCGgILUMAdJkrbfDtb53CUD81WrpsObe4OQ1T1nzPtbik7QPmf2En5CXwxVUeV2xgXTPiZeck3DJlzeaw8P9Io9FlR-Yz0L2QM0l_9CTiiGl94THrBdzP8tPa46x2tg2qKl3nY3x78wCc7l0UNDUysYO4OE3krHKqPXNw_N41fFblgO0kMh4K58uH3_earGUkK-ZppiHX5cKA6TcNhEeZ7Ps0xx8ylWlACg6yXgaGHzfPbWHfOotvnCW9hSUXSPS9NBjNft-6kUFAeh1SL8qyGduVx_NwSmgqennRuHUKQtZOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تأكيدا لما اعلن عنه الحرس الثوري.. إشتعال النيران في القاعدة الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89163" target="_blank">📅 03:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82dcc6038.mp4?token=T2r3zbkVOibN6ve8yEGXZPGfv4du84JwxUQWQSFtDeCZN4WB60_ByyTdszrOmGlIK1TMZFAgMX9D2z2DsGezfTFGn5Z8ib7RhsPKEaNfa5GbaQICHN1caIYsZ3eAWnmVVvZhjlBbjqdF3yR4uiPtH7lx5GyAc5C8veECCRgTmnUT8EwKDA4Yo0nCCnZonwhfLu_DW94anS45uwlIZXPvUt1EWFxmED5iTQWVDaWBRyi1Vvj4O7N3h5375MgNT0FOBfhXOzKLkVpW1amv21Y37_XDJiu07AbZPWdJZfrQJC1ExDsh5ffP-rwmnnxPz9VqZyDd0V8lEXM9vtTI1prJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82dcc6038.mp4?token=T2r3zbkVOibN6ve8yEGXZPGfv4du84JwxUQWQSFtDeCZN4WB60_ByyTdszrOmGlIK1TMZFAgMX9D2z2DsGezfTFGn5Z8ib7RhsPKEaNfa5GbaQICHN1caIYsZ3eAWnmVVvZhjlBbjqdF3yR4uiPtH7lx5GyAc5C8veECCRgTmnUT8EwKDA4Yo0nCCnZonwhfLu_DW94anS45uwlIZXPvUt1EWFxmED5iTQWVDaWBRyi1Vvj4O7N3h5375MgNT0FOBfhXOzKLkVpW1amv21Y37_XDJiu07AbZPWdJZfrQJC1ExDsh5ffP-rwmnnxPz9VqZyDd0V8lEXM9vtTI1prJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أعمدة النيران والدخان تتصاعد من القاعدة الأمريكية في أربيل عقب هجوم صاروخي وبالمسيرات من قبل الحرس الثوري.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89162" target="_blank">📅 03:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f9def1c1.mp4?token=e029GzM9synD3aOz4aOKKpOv43tf4gkrcE2nKlvp4XmgQAzd7Dk-ddd213OjCYkqS91LQggmLtXM9DoeTzNZJjtpazlr19I4V7HHUK7IHp2Oe50kpoX5SflvSpAyd4ZFMJru3gf-4lhiyu8FSrNSbzZNsvcgoz84_GcWfZZ5l3hfMWBLQrLkQ0akd2s-G3VJp_mChiM-rNAtvYKqZ3F9IlvKqbN8zVJmm_xAcnsC0dZg7jzgdZS4PGhofnFPSabX9XdgVME5KDOAHj0_JJuZqefJeKmwQXDlUz-Uhz3PLKErnfHW7RW0QzEKNhIQjtFUUDoGimwPXnQwwooYNLjf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f9def1c1.mp4?token=e029GzM9synD3aOz4aOKKpOv43tf4gkrcE2nKlvp4XmgQAzd7Dk-ddd213OjCYkqS91LQggmLtXM9DoeTzNZJjtpazlr19I4V7HHUK7IHp2Oe50kpoX5SflvSpAyd4ZFMJru3gf-4lhiyu8FSrNSbzZNsvcgoz84_GcWfZZ5l3hfMWBLQrLkQ0akd2s-G3VJp_mChiM-rNAtvYKqZ3F9IlvKqbN8zVJmm_xAcnsC0dZg7jzgdZS4PGhofnFPSabX9XdgVME5KDOAHj0_JJuZqefJeKmwQXDlUz-Uhz3PLKErnfHW7RW0QzEKNhIQjtFUUDoGimwPXnQwwooYNLjf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تأكيدا لما اعلن عنه الحرس الثوري.. إشتعال النيران في القاعدة الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89161" target="_blank">📅 03:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ece92424e.mp4?token=Ux2C73JStRZUXdRvyteWT7tyLlUVJFn1G03r3VBFCaQmaoCnt7axbYK51vxgHZaJztv7aqDdXAjbdd4mUIGMmvXtFJcyM3iu0Z2YPOvU0Upyge_EW9hwpIOk3CZ-4gVSAQLbz2ZI1A1sy1pOWWvexac3Sp20wn9VdKhLpoIkuHbcBJS83eajaTXcQ5nEq5gJwej4BM6jPbY0UV4oq4VZpZ59ohQ9IDZZUdn6nAuVWWtQV7t6IjD5R5rnJaH6VsWUxIdTkk9DrpsErnD5jleDnbgDMAxOiduHRIuVaQUAe-iVC2esg3DIEZHMFkNeYsS11JH88Wrboghbo2BKBEhdfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ece92424e.mp4?token=Ux2C73JStRZUXdRvyteWT7tyLlUVJFn1G03r3VBFCaQmaoCnt7axbYK51vxgHZaJztv7aqDdXAjbdd4mUIGMmvXtFJcyM3iu0Z2YPOvU0Upyge_EW9hwpIOk3CZ-4gVSAQLbz2ZI1A1sy1pOWWvexac3Sp20wn9VdKhLpoIkuHbcBJS83eajaTXcQ5nEq5gJwej4BM6jPbY0UV4oq4VZpZ59ohQ9IDZZUdn6nAuVWWtQV7t6IjD5R5rnJaH6VsWUxIdTkk9DrpsErnD5jleDnbgDMAxOiduHRIuVaQUAe-iVC2esg3DIEZHMFkNeYsS11JH88Wrboghbo2BKBEhdfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري:   قام مقاتلو القوة البرية لحرس الثورة الشجعان بهجوم مدمج باستخدام الصواريخ والطائرات المسيرة على القواعد الأمريكية في أربيل، مما أدى إلى تدمير مركز إصلاح ومخازن للمعدات الفنية لجيش الإرهاب الأمريكي، وتدمير نظام توجيه منطاد التجسس الأمريكي في…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89160" target="_blank">📅 03:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
الحرس الثوري:
قام مقاتلو القوة البرية لحرس الثورة الشجعان بهجوم مدمج باستخدام الصواريخ والطائرات المسيرة على القواعد الأمريكية في أربيل، مما أدى إلى تدمير مركز إصلاح ومخازن للمعدات الفنية لجيش الإرهاب الأمريكي، وتدمير نظام توجيه منطاد التجسس الأمريكي في القاعدة. كما قام مقاتلو القوة البرية الشجعان بإشعال خزانات الوقود في القاعدة، وقتلوا عددًا من المعتدين.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/89159" target="_blank">📅 03:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات جديدة تهز الكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89158" target="_blank">📅 03:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
واشنطن بوست:
القوات الأميركية تعترض الضربات الإيرانية حتى ساعات متأخرة من الليل.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89157" target="_blank">📅 03:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d072c568f0.mp4?token=eQDZiP3Dyey_kVHrXihhUjd-cfX9RQIjfc0XHlolkEbijj8RXomXhW8UnCHRRb0GnHGt0BzJhQauJAxtWMxNCmwcMRt6dIwv02oHV0joTYsNjjLT5zZUVRc77Pq7SvKizAMGZUQfiKo2gezWoyA6VPkVemmql6YPld_5R0w-3L-d0Q6zw2N5O6cV-AJiuQJJvTM6p-0PdnBeptz2eNtZHI1OL2-E44YzWxGDTguL-C5AxuJsflNcn_GvSfSVtgOwInNiBli8RBCYatKgcFZXyPGBM-5oJ4D2W7m3bKYydGF5iuypR-Zzi9-zODgSO_20whQg9ge0TdAsVTWmX4QSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d072c568f0.mp4?token=eQDZiP3Dyey_kVHrXihhUjd-cfX9RQIjfc0XHlolkEbijj8RXomXhW8UnCHRRb0GnHGt0BzJhQauJAxtWMxNCmwcMRt6dIwv02oHV0joTYsNjjLT5zZUVRc77Pq7SvKizAMGZUQfiKo2gezWoyA6VPkVemmql6YPld_5R0w-3L-d0Q6zw2N5O6cV-AJiuQJJvTM6p-0PdnBeptz2eNtZHI1OL2-E44YzWxGDTguL-C5AxuJsflNcn_GvSfSVtgOwInNiBli8RBCYatKgcFZXyPGBM-5oJ4D2W7m3bKYydGF5iuypR-Zzi9-zODgSO_20whQg9ge0TdAsVTWmX4QSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيف يهز أربيل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89156" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">استمرار الإنفجارات في أربيل شمالي العراق وسط هجمات واسعة بالطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89155" target="_blank">📅 03:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوي 4 انفجارات في البحرين</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89154" target="_blank">📅 03:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20633795a.mp4?token=b74AXtnN5ZPFzYCSUozJGrZUDF5tObspbaHqy8vi5Q4KX_yMjmOQG6Iu9xRWaksIABpgTtayT30hpz6Y_rn5IX2sFH8iiWnUTHODf9nuQCyYOJ3iGA2EeGBCNaSdDcw6U7ygr1MREfJbEidoHE2F0rDInDL_5BSITC-32caeccAOVbE7LzaeqS2Ee24yByyHRE7H8-0e277bQBvgnYGDtBMf3VzdimEVxmQdS8wwwUG2Rlr0wIrjt8kuj0dJhg3UfT1X0OhkogZnJpZTkBbuxadUJbd6JgO3BZFYv2QBmBOUw2C8z_p4NM1-yoWdZMmPtbacd_1N0BDCDLzc-GBCdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20633795a.mp4?token=b74AXtnN5ZPFzYCSUozJGrZUDF5tObspbaHqy8vi5Q4KX_yMjmOQG6Iu9xRWaksIABpgTtayT30hpz6Y_rn5IX2sFH8iiWnUTHODf9nuQCyYOJ3iGA2EeGBCNaSdDcw6U7ygr1MREfJbEidoHE2F0rDInDL_5BSITC-32caeccAOVbE7LzaeqS2Ee24yByyHRE7H8-0e277bQBvgnYGDtBMf3VzdimEVxmQdS8wwwUG2Rlr0wIrjt8kuj0dJhg3UfT1X0OhkogZnJpZTkBbuxadUJbd6JgO3BZFYv2QBmBOUw2C8z_p4NM1-yoWdZMmPtbacd_1N0BDCDLzc-GBCdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديد تهز قضاء سوران بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89153" target="_blank">📅 03:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe8fe7da1.mp4?token=QmBFYMV_ROvAHx7x_PEUIMr0ZZ6pWUKVruhItgvPjQYJRnhzLkAivUT1rLndJhe6J2zOqRW3iqb-ImTdkv38lnbQpBR5GmC0znquahp3oj-WaXup-cycrhvpFeg1u6nhJ9caOcww8V7oq-mjwFwzUjtJuyrDUORBM4otd7Lm7y0C8pQm7eXp4RfDQq0tIDnap2kCEQwmuSUK5s9APm5n-bJF3bOqHshQjKZCNr6PhhsHIphZ37l0dfWWMMguS2xrFBFhw3c4nfSKjLpBsNTljmNhFXGiFlr3lK0BnAF4VsH0KpiGBTSkgjzA8YSAYzTCCUZ328RWo7di3VMOfugKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe8fe7da1.mp4?token=QmBFYMV_ROvAHx7x_PEUIMr0ZZ6pWUKVruhItgvPjQYJRnhzLkAivUT1rLndJhe6J2zOqRW3iqb-ImTdkv38lnbQpBR5GmC0znquahp3oj-WaXup-cycrhvpFeg1u6nhJ9caOcww8V7oq-mjwFwzUjtJuyrDUORBM4otd7Lm7y0C8pQm7eXp4RfDQq0tIDnap2kCEQwmuSUK5s9APm5n-bJF3bOqHshQjKZCNr6PhhsHIphZ37l0dfWWMMguS2xrFBFhw3c4nfSKjLpBsNTljmNhFXGiFlr3lK0BnAF4VsH0KpiGBTSkgjzA8YSAYzTCCUZ328RWo7di3VMOfugKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89152" target="_blank">📅 02:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوي 4 انفجارات في البحرين</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89151" target="_blank">📅 02:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عدوان أمريكي على نقاط في محيط مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89150" target="_blank">📅 02:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89149">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c515323a.mp4?token=SWMXGLnHTpDn2Sv9sMSjY-S5_GS9AIWyK73Pf6f3fdDIdqRpT7mgFrOyuXMDH8oMEb_mvMaE10i8Wba1hDyimNKmvlXtZF4aE7dmrutxvs5jQ2_y4yHT0dstvQdrCSregAPD04jMIock4AGM9ZGj_ubODfmV7NCXLNXo3-tYgaiN2i7uQcEynWiKGq8sfsVMwrC4uW_C5UP5PUFQGc7xXXT3WoxlaNte4bljVFiR790NQRnk1d1MU8cSChdKHMQO2wadTt0bp8Z8H2dv5uAxf1kUAO8vp2-ZfFpCaf7wvpjolEWhwu0qjjLEQPqDTIS57rY1z0zxxegQ48Iqh9Dviw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c515323a.mp4?token=SWMXGLnHTpDn2Sv9sMSjY-S5_GS9AIWyK73Pf6f3fdDIdqRpT7mgFrOyuXMDH8oMEb_mvMaE10i8Wba1hDyimNKmvlXtZF4aE7dmrutxvs5jQ2_y4yHT0dstvQdrCSregAPD04jMIock4AGM9ZGj_ubODfmV7NCXLNXo3-tYgaiN2i7uQcEynWiKGq8sfsVMwrC4uW_C5UP5PUFQGc7xXXT3WoxlaNte4bljVFiR790NQRnk1d1MU8cSChdKHMQO2wadTt0bp8Z8H2dv5uAxf1kUAO8vp2-ZfFpCaf7wvpjolEWhwu0qjjLEQPqDTIS57rY1z0zxxegQ48Iqh9Dviw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة انتحارية تحلق في سماء أربيل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89149" target="_blank">📅 02:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f89d8f81.mp4?token=YISdGWBmP8OuzDEPEvHlzmYXg5Ant0ukCEULripk2WKYsumduMd8pDWqELQJZaxJQYLuhL3Yed621B_SaOyZo3r75V07IvdcZjVAIk5Vl8VVwOE2bN2UPD9U5FanrkhccPPMwb4gKwXgJAiuBtTd96ySCC0rkLudEIfQV0UzFbKpXazctl1hur1VL1k5Qoqkixsb86IAjuT7yOynXG9HByKR7u8jEf8nhyPHpG4UwtNP5ScsPcczULaRTTFyEPoYYiM40Ie6pEBYjwN50hRYYF9JDHECUwuMIvMxRkZlGT1AvkYi_ulSDm0LAEZmCk0aNEWWQhatO6sqTlOpcyXwrJQlwbIV-W9T-dQmgAOJGIE8Vz5X7POa8Y4gC_cMyicoq9K9HiamHZIWidsdlOMdmRWo2mb-WZx3V0Z3Ds0ixX-aYWYg-RTy3QNhsl4JoNVKO4sh43o9Ivt68PHNm32H1zOiaaTGO7suDdgjGfbqiVJw7HbVepUzNiPuOjwCCy739Z_8f5m6AbFbjmWiO-Z6WC4ah5VktR3ds6OyQmQ9GjOkVh_TVdiLQ7PaxA1TSP3g1fkQZ7Thr402a0Ys26tocOpDavXMiv-UqLfTMBflCyL4UDNdtrjTxCQnISgTFYrWPkzrRkWqISiJ-h0Hxq1XzJERU-QbIFHk7gSzFhZGcz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f89d8f81.mp4?token=YISdGWBmP8OuzDEPEvHlzmYXg5Ant0ukCEULripk2WKYsumduMd8pDWqELQJZaxJQYLuhL3Yed621B_SaOyZo3r75V07IvdcZjVAIk5Vl8VVwOE2bN2UPD9U5FanrkhccPPMwb4gKwXgJAiuBtTd96ySCC0rkLudEIfQV0UzFbKpXazctl1hur1VL1k5Qoqkixsb86IAjuT7yOynXG9HByKR7u8jEf8nhyPHpG4UwtNP5ScsPcczULaRTTFyEPoYYiM40Ie6pEBYjwN50hRYYF9JDHECUwuMIvMxRkZlGT1AvkYi_ulSDm0LAEZmCk0aNEWWQhatO6sqTlOpcyXwrJQlwbIV-W9T-dQmgAOJGIE8Vz5X7POa8Y4gC_cMyicoq9K9HiamHZIWidsdlOMdmRWo2mb-WZx3V0Z3Ds0ixX-aYWYg-RTy3QNhsl4JoNVKO4sh43o9Ivt68PHNm32H1zOiaaTGO7suDdgjGfbqiVJw7HbVepUzNiPuOjwCCy739Z_8f5m6AbFbjmWiO-Z6WC4ah5VktR3ds6OyQmQ9GjOkVh_TVdiLQ7PaxA1TSP3g1fkQZ7Thr402a0Ys26tocOpDavXMiv-UqLfTMBflCyL4UDNdtrjTxCQnISgTFYrWPkzrRkWqISiJ-h0Hxq1XzJERU-QbIFHk7gSzFhZGcz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحرس الثوري:
مشاهد من الهجمات الصاروخية المكثفة التي استهدفت أهدافًا أمريكية في الأردن، في الموجة الثالثة من عملية "معاقبة المعتدين".</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89148" target="_blank">📅 02:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
الحرس الثوري:
شن مقاتلو القوة الجوية التابعة للحرس الثوري الإيراني هجومًا مكثفًا بالصواريخ الباليستية على مواقع طائرات الاستطلاع المسيّرة من طرازي RQ-4 و MQ-9 في القاعدة الجوية الأمريكية في الأردن المعروفة باسم الأمير حسن، مما أدى إلى تدمير عدد من الطائرات المسيّرة، ومقتل عدد من الطيارين والفنيين.
🔹️
بالإضافة إلى ذلك، تم إشعال النيران في العديد من البنى التحتية الفنية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/89147" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
