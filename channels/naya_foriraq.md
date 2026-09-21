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
<img src="https://cdn4.telesco.pe/file/a_3WjIVIYISIMsgv8675GW2cgHG0WWaOOOcI8niNhKpKpn797juWnbTYKAII-R9OtBRMsyCudfUn5gE4VSALtrKudArCj4Qfquqp5uD417Uru_Nb9AplFyA_ESm0CwWovMcpUsiSRgCZj2MtP8j2KleEWQPwrdO2t70RzU_IPA9leaFfd_-ytkukJmvGQChGWi1TaW20GSRF8UYK28z26eRWqYejY56WnCi_bqMgebnyFllWjEvkzBH4i6c6zxu02mVpUagGllaxAaSX01vTxuqZLwc1GNG1U1uP74aGMpDy8XPYUwHxgYzvsH3M7VujX2UU9L0setXBohTlyfKPRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار انسحاب قوات الاحتلال الأميركي من العراق باتجاه الأردن.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/naya_foriraq/91182" target="_blank">📅 20:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
في تصعيد كبير استهدف العدو السعودي المجرم  محافظات الجوف وتعز وصعدة ومأرب بـ 157 غارةً جويةً وصاروخاً، من خلال طائراته الحربية نوع "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران وجيزان.
ليبلغ إجمالي غارات العدوان منذ بدء التصعيد 917 غارةً وصاروخاً.
هذا العدوان الكبير لن يمر دون رد بإذن الله تعالى.</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/91181" target="_blank">📅 20:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxRNzQQzTOb0ZclblEhnTrb0X0EaxMf9b7pXC9ahsDnbj4cMvozp8zwiEBJuRXPqAspCKFWWpt2YAriRXur-nrkYvBdhESLoubJiWhush3PESiBTUE6gZtQ7ssCIHYaJTsgxPmBEWRxjVlfk8fqvAJ6oe5u3FtWpyrMqPHxM2oy4PrUyVCByiNBRA6MLXOuWWgM5lwfm-5xhYLhbNwc9MBPUAxuF4YP13bkiuo9XCKDNoWm_iqfat0kgWLeu6LPnnIev0kjG2dnsCcDiNV_EqV-lfXdbd_bjCOgxPMsQ_m-FhViRwYhMP1WyQV-RXg9f9Qooknj2TpuI-LnNfRBZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بقائي
:
عندما تغلق إدارة ما أبوابها - حتى في وجه الصحفيين الأمريكيين الذين لا تحبهم - وتمنع المراسلين الأجانب، بمن فيهم الفريق الإعلامي للرئيس الإيراني، الذين تفضل إسكات أصواتهم، فإنها لا تدير الوصول؛ بل تحاول إخفاء الحقيقة وتعزيز حملة التضليل الإعلامي من خلال انتهاك الحق في الوصول إلى المعلومات.
‏أمة كانت تفتخر في يوم من الأيام بإسقاط الستار الحديدي، تجد نفسها الآن تقف خلف أحد أبنائها.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/91180" target="_blank">📅 20:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اعلام فرنسي يزعم:
‏العراق سيعلق رحلات شركات الطيران الإيرانية الخاضعة للعقوبات الأمريكية.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/91179" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfTeWftsp9OG1h0a5cqP_2mD7GlKuZUhgiAdnNkXJ7wJGSWbzCB6XGsuFOU9A9-I2cMVjYAx6jUXA5mxtWazIjo7lg68kAV3S95OYrGB2x1wjR4k___m51uiJyR666GGsV2ViSiyEtQW_6l_xzih_mz6TepCXVPukNzGCO00u0fIAQi-axKgv5Pfeyf9kk2ieJ5AALn8etScVmAIufISUwE3RuoNVQT6lwBnAwFTgRKltNEU4uColJRMZSxbFsl7VYuk0tnqW1YFFPtCT1m2vZeKb0DKItLO0dzJ7R6w_GRiVpny7POGFKM6NX75X1pnREAHbTiFSQWCgtF5kUPo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط: 99$ للبرميل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91178" target="_blank">📅 19:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NckEuWeb-9XAbAqfnEnkZq66hJYvX4lyWSr6ruAXCzCGQWTm9d5IONnjliDjnCiXOUPKAwYGrBMCoRlx3LCVceX-PA0MQWCjcV7GqPsnqrRDDfJaNuXpnuzOlzy2ES9i8TJRR3V_1SWjyeo7sIeBuzqABr7bfOGKiuHuLo07DNyFH4pb1b678ovzHYxpigsiCQ7l70Pb1LKkUApGKLlc5l5sWYi7MjdrfT59HkMZTqxUbO3361Tm7Gs1ImEp4QtJfAnIQmWRMyRl-J4GcxucaokFEy3nmnaFmt0cT1QQZ3I_H7bVOIOoCPnl3C4NEKAImycplLyG_gp--Qi1p-CyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇱
🇺🇸
وزير الخارجية الايراني عباس عراقجي يعلق على مقال في صحيفة "إسرائيل هيوم":
لم يعد اللوبي الإسرائيلي يتردد في إظهار دوره وتأثيره علناً فيما يتعلق بالسياسة الأمريكية تجاه إيران؛ إذ تصرح صحيفة مملوكة لميريام أديلسون -والتي تُعد بمثابة لسان حال هذا اللوبي- صراحةً بأن السياسة الأمريكية يجب أن تُصاغ بحيث تدفع الولايات المتحدة أيضاً ثمناً لأي عمل ينطوي على عدم احترام أو عدوان ضد إسرائيل! حان الوقت لتتحرر واشنطن من هذه القيود.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91177" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExtjnsthFVNnAzlopdEsgb-V6iiGIRXgk4_L1yeP6s3cpAciEDJAhI6hKAjWRLOf-VFeyC61lJWhpG45DC6tmEkSBuVuS6QNBN4En1RHOyCvUKKvDSayThc1lDBW_NBz1mQtr34OSrvAMhpuRTYLsH2Je4m_QE7EdE-47PhuTJVdr3uqnmqK5xRAHZZ5xQXI9_vfeC8mscPqrA9qYkfiw6TCh9HEy1ZkSAo00f4qydbjEIAydEVscOZ1Xlkj6IEYu7qXHgbaa4ugVr7YRvhP_GZezxeumNZ-p1Eg74bP862i4tmAGfGlAilAjVjFEHPPeYlunpYsznmD2n_QijA2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب على منصة "تروث سوشيال":
الولايات المتحدة تعمل على صفقة ضخمة تتعلق بشراء البوتاس من بيلاروسيا. ستكون الأسعار أقل بكثير مما ندفعه حاليًا لكندا، وهو خبر جيد جدًا لمزارعينا ورعاة الماشية. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91176" target="_blank">📅 18:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
🇮🇷
شركة الخطوط الجوية الإسلامية الإيرانية:
رحلات شركة "هما" (اسم قديم لشركة إيران إير) من ثلاث محطات انطلاق: طهران، ومشهد، وإصفهان، إلى مطار النجف، تجري وفقًا للجدول الزمني المحدد.
رحلات شركة "إيران إير" في مسارات طهران - النجف، ومشهد - النجف، وإصفهان - النجف، وكذلك مسارات العودة من النجف إلى هذه المدن الثلاث، مستمرة، ويمكن للركاب الاستفادة من خدمات الشركة الجوية في هذه المسارات وفقًا للجدول الزمني.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91175" target="_blank">📅 18:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91174" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91173" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">السيد الحوثي:  العدو السعودي عاد إلى التصعيد بقصف مطار صنعاء واتجه إلى التحشيد البري الكبير لإبادة شعبنا وحشد عشرات الآلاف إلى صحراء الجوف والمخا والساحل الغربي والبيضاء وتباهى عملاؤه بأنهم متجهون لاجتياح ما تبقى من بلدنا وأشرف على التحشيدات في كل الجبهات…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91172" target="_blank">📅 17:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">السيد الحوثي: هل يقبل التركي والباكستاني أن يتدخل السعودي في كل سياساته؟ وهل تقبل الدول الخليجية بذلك؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91171" target="_blank">📅 17:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">السيد الحوثي:  الكيانات المتعاطفة والمتباكية مع العدو السعودي على منشآته النفطية وردود قواتنا هل ستقبل بالقيود التي وُضِعت على الوارد التجاري لتبقى في دولة أخرى للفحص والتفتيش قطعة قطعة!! هل ستقبل الكيانات المتباكية مع العدو السعودي الإجراءات التي تضيّق الحركة…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91170" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">السيد الحوثي: وفود من العدو السعودي والبريطاني كانوا يذهبون إلى جيبوتي لتشديد الإجراءات بما يزيد من معاناة شعبنا عبر التضييق الاقتصادي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91169" target="_blank">📅 17:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77280b847c.mp4?token=V51M4hrTpUtu2cGZdqsQsAruYNGKSzGUls_KLi1_MJ3iGjT6US_ZI8D2_-K3XJNZS7JcAI_vyWT_Sg6un0IJEPmZbHpe5ehDLHAhwmZpdSWy0Ghsaz2XNInbkFQtcGzQdHju5qCkk7ojy6-rAUuVYVGES3ZALbY3DWUrFC-g_F44pUcBLpfg2nnzQ8JtIWeUMANM1L_d62QgIREgGMQVqHRF5FuOqzr6eejP8DojE5d2rbsyKJDXLs-1s30F-R0cDzxgEfJTzQXklCEzVYKdjrFEBcI21kLi5kGBcAwjNFkxfOVz79oGTMQRfxmXpeH_40hqAib649FBc6HWmk1Frg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77280b847c.mp4?token=V51M4hrTpUtu2cGZdqsQsAruYNGKSzGUls_KLi1_MJ3iGjT6US_ZI8D2_-K3XJNZS7JcAI_vyWT_Sg6un0IJEPmZbHpe5ehDLHAhwmZpdSWy0Ghsaz2XNInbkFQtcGzQdHju5qCkk7ojy6-rAUuVYVGES3ZALbY3DWUrFC-g_F44pUcBLpfg2nnzQ8JtIWeUMANM1L_d62QgIREgGMQVqHRF5FuOqzr6eejP8DojE5d2rbsyKJDXLs-1s30F-R0cDzxgEfJTzQXklCEzVYKdjrFEBcI21kLi5kGBcAwjNFkxfOVz79oGTMQRfxmXpeH_40hqAib649FBc6HWmk1Frg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91168" target="_blank">📅 17:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/91167" target="_blank">📅 17:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">السيد الحوثي: كل الجرائم السعودية التي ارتُكِبت في اليمن قوبلت بالتفرج لغياب المبادئ في التوجهات والسياسات المعتمدة لدى معظم الأنظمة، لو انتظر شعبنا العزيز للأمم المتحدة أو لمجلس الأمن وغيرها من المؤسسات أمام كل تلك الجرائم لما فعلت له أي شيء</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91166" target="_blank">📅 17:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
🌟
اكسيوس:
ترامب فكر في شن ضربات على الحوثيين في اليمن خلال عطلة نهاية الأسبوع، قبل أن يقرر عدم القيام بذلك.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91165" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">السيد الحوثي: الموقف العربي والإسلامي من العدوان السعودي على اليمن كان متخاذلا عدا محور الجهاد والمقاومة وبعض أحرار العالم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91164" target="_blank">📅 17:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
🇾🇪
كلمة للسيد القائد عبدالملك بدرالدين الحوثي عند الرابعة عصر اليوم.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91163" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
هجوم إرهابي في مدينة ايرانشهر جنوب شرق إيران؛ إستشهاد أحد عناصر الأمن كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91162" target="_blank">📅 17:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📰
وكالة رويترز: مكالمة هاتفية جرت بين ترامب ورئيس المرتزقة في اليمن رشاد العليمي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91161" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
وكالة رويترز:
مكالمة هاتفية جرت بين ترامب ورئيس المرتزقة في اليمن رشاد العليمي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/91160" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bd78ec90.mp4?token=Ug1-_n6wgt2mP5GprRSrQxQ3_pHWb6XHwYvOtj8skKT9lbWn5j84LGLJWCJ-4E5DMw5s24ngAcwdUQOEKbHe_OMRLNh7aYfSFzI2MFENMVWuy9ozhIDVHhD5cwpqnaHNgA7e3WHWiSiSyIaKXImJbmJjrqRUBp_cLVRBo3RUjmesZmW_TtWsZuHnFy4EtdZbVV9uSfNcPcG5SPIQcaktN2sD4EFon_0TSGb-i2z-6UGI13UEt77fdRmzeinfY-xIMvSCe-AlceqtPFYc8buQtCrgIV9uucqx6bboPFGQhCRBh7RYqjC2xxcFU4bIZqEiRglWJ4mTspUmtlxSXKvrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bd78ec90.mp4?token=Ug1-_n6wgt2mP5GprRSrQxQ3_pHWb6XHwYvOtj8skKT9lbWn5j84LGLJWCJ-4E5DMw5s24ngAcwdUQOEKbHe_OMRLNh7aYfSFzI2MFENMVWuy9ozhIDVHhD5cwpqnaHNgA7e3WHWiSiSyIaKXImJbmJjrqRUBp_cLVRBo3RUjmesZmW_TtWsZuHnFy4EtdZbVV9uSfNcPcG5SPIQcaktN2sD4EFon_0TSGb-i2z-6UGI13UEt77fdRmzeinfY-xIMvSCe-AlceqtPFYc8buQtCrgIV9uucqx6bboPFGQhCRBh7RYqjC2xxcFU4bIZqEiRglWJ4mTspUmtlxSXKvrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية ينشر  مشاهد لاعتراض وتدمير طائرة مسيرة من طراز MQ-1 تابعة للجيش الأمريكي صباح اليوم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91159" target="_blank">📅 16:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
🇾🇪
التلفزيون اليمني:
- الوفد الوطني التقى المبعوث الأممي ووضعه أمام موقف اليمن من العدوان السعودي
- الوفد وضح للمبعوث الأممي بأن العدو السعودي رفض إنهاء الحصار على المطارات والموانئ اليمنية، وإزالة القيود الاقتصادية والإنسانية وصرف المرتبات
- الوفد الوطني وضّح أن تلك الحقوق هي مطالب الشعب اليمني اليوم أمام الأمم المتحدة وأمام كل من يريد أن يعرف خلفية التصعيد الحالي
- الوفد الوطني أبدى للمبعوث الأممي أن الجانب السعودي يتحمل كافة التبعات نتيجة عرقلته ورفضه الحلول الإنسانية.
- تم التأكيد على أن السلام هو مطلب الشعب اليمني والمجال مفتوح للحل من خلال المطالب الانسانية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91158" target="_blank">📅 16:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جيش العدو: نجري حاليًا مراجعة التفاصيل.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91157" target="_blank">📅 16:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تفعيل الدفاعات في شمال الكيان</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91156" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صافرات الإنذار في المالكية بالجليل الأعلى</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91155" target="_blank">📅 15:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صافرات الإنذار في المالكية بالجليل الأعلى</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91154" target="_blank">📅 15:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏ترامب: يجب إنهاء هذه الحرب السخيفة التي لا تنتهي مع أوكرانيا</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91153" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزارة الخارجية اليمنية تعلق على اقتحام المسجد الاقصى: ندعو المتشدقين بالدفاع عن المقدسات لاتخاذ مواقف عملية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91152" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v05pF9HS1jhUkqY-WIo5rKmlz2nG7uKe7hutgYepwI4L7BGaqlTNdumC7TmzhPqI-eejY16sQ-OSWtNVC5fvun-AmxlvfSoB6ayVTSgaRAVdSdrsdiyFlV-wgZAiPQBY6B9PtEjps7-YV4bBSZc9movkwI3UMABEGjhlpanTMQakYWHnkjqabPqhsqvWC-HJ5oslrGoCsRFzZnv7v3NRata8S-RpPQ6wV4rn76npWu4xnJg-IZoMOtioHnCMlHw_owj8OKlikWW-pQZwMQz3nPkjtlXxMLwPvDe7A7Lu6YRxyx7fkwa6pXFQ-yaXLapoIR9vEbOMJghArAp-dwvxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حق شهداء المقاومة ومجاهديها وجماهيرها أن يفخروا؛ فالمواقف تُختبر عند المفترقات الكبرى. وفي مباحثات تنظيم السلاح وترسيخ السيادة الوطنية، لم تطرح قوى المقاومة أي مطلب شخصي أو سياسي، ولم تقدّم أيَّ مصلحةٍ على مصلحة العراق.
إنما هاجسها الأساس هو سيادة العراق وقراره الوطني واستقلاله، ورفض الوصاية والتدخل الخارجي؛ وهي مبادئ تستحق التضحيات وتتقدم على كل الاعتبارات.
حقًا هي "مقاومة.. حتى يكون العراق سيد نفسه".</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91151" target="_blank">📅 15:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA8dRzeP31InrREIj5mYV4cetbaIMRQU8NEPvk5jmbXFzyehRRYI9hUIi75HC6rfgxt2LyaqPD_WEsdlUYDffqWIJIFRFxos7v2DuL38mruHzK-PMiYZwM17UOHYWYu5TaRlW1xBaFPO4VhdEBN_ZpyLDbilDkLo5MMK1rGLWn-i_WRIURX_Y_msrRsftsP4SJ6E3ao6mI9fp8i5M6Kfm_jI7FRb_GAHnl4QDNwXiVS9Y9JPLzR4FKa5iYjikNu9gszk2cxAbDCKbKLCxrdV6mh4zX8penMT97O4MQeGsenFywJL6h2pgjuJaTL939GyYPpC4piBE11kSqLZsPwt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل 5 جنود سعوديين من القوات البرية السعودية بضربة مسيّرة استهدفت آليتهم في نجران بينهم قائد الآلية خالد حسن الشهري، وعبدالله السلمي، وخالد السلمي، وإبراهيم المرزوق، وجابر الرزاق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91150" target="_blank">📅 15:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8QMxVrxESm6FBoFlQ9582xqEpU5-jREUo3rBTKXhK-7J-ZIfvDvQ2U6yRnR3bEUnsSGz6sEBuOi79eh6OmC4ZJaqV0ed7MV-xa3r-AGnVGV0h4tcjrLmM9wyNxF36wH-NqlwGdYyp0J5cWqocxxx8zOshE9XsULDC_uohExaZC9cRSu61bNNaoasqCUf7nzFLbHNtFPtSU9SWu2yWY6xSVunBnbj9rKCkWlLwL03MSE6R2nlbbDo9N6TOIbLOwCRRYSr2MtMWNrd6g9vr8D1TJs9OtvNDAnvsk4df6ER1rD6dJLsXQNznk4LgpukJAPbFIFMZQ62O_JiIEWNguBnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرع عدد من الجنود السعوديين بعد استهدافهم من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91149" target="_blank">📅 14:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصرع عدد من الجنود السعوديين بعد استهدافهم من قبل القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91148" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
مسرور البرزاني امام مدير مكتب القائد العام للقوات المسلحة العراقية: في عام 2014، وبتوجيه مباشر من الرئيس بارزاني، توجهت قوات البيشمركة إلى مدينة كوباني للدفاع عنها، مسجلةً بذلك صفحة مشرقة في تاريخ الدفاع عن شعب كردستان.
تصريح لن ينتقده نواشيط اربيل ويقولون شدخلنا بكوباني كما ينتقدون السلاح الشيعي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91147" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
ترامب يغرد على خلفية حظر دخول مراسلي مجموعة الصحف الاميركية الى البيت الابيض.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91146" target="_blank">📅 14:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">المتحدث باسم رئاسة إقليم كردستان: قوات التحالف الدولي لن تبقى بعد يوم 30 أيلول الحالي</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91145" target="_blank">📅 14:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
بلغ استهداف العدو السعودي للقرى بمديرية الظاهر وأجزاء من مديرية حيدان أكثر من 135 صاروخا وقذيفة خلال 12 ساعة وما زال متواصلا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91144" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فاينانشال تايمز:
ترامب يضغط على زيلينسكي لوقف استهداف مصافي النفط الروسية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91143" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار يهز مدينة منبج في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91142" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار يهز مدينة منبج في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91141" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE-Wt-xN5LBjaSg4gKWVhM2L0KYhXquMvBE8m0rFtar6juBabc5w-Y1vvJ9rQUU7NGbf-7GjiBauv7hJneNCs1f2bty2sShF1Q8idehvvJ2sflvwu5XrALMzeVvBeBnWpboGgeJbrOfk0FFK_k1DSZq5OIVUv5lClryVXd9y_p5hFaf6GVt16dJI4f13plLl8XQGlcKXujsZA3ZgrB89IT-uoN5chZxxG1S7hOfmd--EkLbl592dfZvYtogLWBGWFaORXT79buFcOAksRfZAaSbrF9njlgiPEE8yDUTn0KJAiJj9l0l3nJa4nq3_61b2yUP_xeLL8sVJebjEmsuwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمليات التجارة البحرية البريطانية: ناقلة نفط كانت تعبر المضيق قد أصيبت بمقذوف مجهول. وأصيب اثنان من أفراد الطاقم بإصابات طفيفة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91140" target="_blank">📅 13:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91139" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbsNr2MdhXUe6zdPsSskhQP6n-5X_zSUxqVYIu1bDDRODD4Yi4w1y7-SK6vmkcPuqQJSAUmkkhktgwKn5--5NipjwbXhi1nUuLfhi1Zjvkdir7ov6WyK4yow22i686VwZMu5WJu4eQmiVohH2usIRmNBcih-8BGho5nbX5Axz8wOIi9qkrgLA8n_--NWv-G_YxUuFZidq_l6j2SaEy9tAapUH4KQR2fWXLiE7A9DK0b7H4-J3i8uZQlZwECWzkLLI1k8bpnKY7nsG5h_baQsFpouBmpqsAMS0XeCnq-UAnQo6kSAMty7IZJBMLRC7RJdo0ZigeDZt1fzjYTWqaxmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91138" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
الحكومة الأفغانية: ندين الغارات الباكستانية على أراضينا وسنرد في المكان والزمان المناسبين.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91137" target="_blank">📅 12:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
🇾🇪
كلمة للسيد القائد عبدالملك بدرالدين الحوثي عند الرابعة عصر اليوم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91136" target="_blank">📅 12:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇾
إنفجارات جديدة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91135" target="_blank">📅 10:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار ضخم أخر في مستودع للذخيرة يشعل سماء ريف حلب الجنوبي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91134" target="_blank">📅 10:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
الحكومة الأفغانية:
ندين الغارات الباكستانية على أراضينا وسنرد في المكان والزمان المناسبين.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91133" target="_blank">📅 08:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
الحرس الثوري:
إذا حدث هجوم جديد، فبالتأكيد ستحدث تغييرات كبيرة في دفاعنا وهجومنا المضاد.
هذه التغييرات ستشمل تغييرًا في جغرافيا الحرب، وتغييرًا في الأسلحة والمعدات الحربية؛ سنُدخل أسلحة جديدة بقدرات جديدة إلى ساحة المعركة، وسيتفاجأ العالم.
أهدافنا أيضًا لم تعد بالضرورة تلك الأهداف السابقة. لدينا أهداف جديدة لم تتعرض للهجوم بعد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91132" target="_blank">📅 08:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من إسقاط وتدمير مسيرة أمريكية من طراز MQ1 في أجواء مضيق هرمز جنوبي إيران.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91131" target="_blank">📅 07:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
اللواء السابع بالحشد الشعبي يشتبك مع مفرزة جوالة لعصابات داعش الارهابية في حوض الثرثار ؛ العملية أدت العثور على زورق وأسلحة ؛ المنطقة شهدت قبل ايام عملية استهداف لأبراج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/91130" target="_blank">📅 04:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🇺🇸
صحيفة وول ستريت جورنال :
إدارة ترامب تستعد لفرض عقوبات واسعة النطاق على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91129" target="_blank">📅 04:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇶
🇺🇸
من المقرر أن يلتقي وزير الخارجية الأمريكي روبيو برئيس الوزراء العراقي في الساعة 4:30 مساءً بتوقيت الساحل الشرقي، كما سيلتقي بنظيريه الياباني والكوري الجنوبي في الساعة 11:15 صباحاً بتوقيت الساحل الشرقي</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91128" target="_blank">📅 03:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارات في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/91127" target="_blank">📅 02:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
أسعار النفط العالمية تلامس 104 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/91126" target="_blank">📅 02:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=jmVOrLn0JeOiq044LRuJbuXqyW5gkztHq1nKIGxsacF0Ok2SD7ikrOsQB5CMs-mVXgpYT0PHEJG8V1Outm8dNkhG9_p1DWmsPnmf_hqjHLz3WBm0hBCFrFj3hwHViL193NMeHb9B9Dz35f8QhnObDMGx3Ywl6O8a_IJjrIu2nIwHg50RccbzOQH1ymfZ5WSKXuBhmCi1W0OSneijMiyuH_FFWHZYnTVVcDEDfqsdw2rztJiHDpfUt1sQ-f2PvjJcxrbyfujJ0N-RnEcS_R4rlxCAt1c2QevgdyUfsGZZ04aj7Yw3_skRb5ompoCrowzzX0JVdMWFzuOk_8t2B0kVjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b112650d.mp4?token=jmVOrLn0JeOiq044LRuJbuXqyW5gkztHq1nKIGxsacF0Ok2SD7ikrOsQB5CMs-mVXgpYT0PHEJG8V1Outm8dNkhG9_p1DWmsPnmf_hqjHLz3WBm0hBCFrFj3hwHViL193NMeHb9B9Dz35f8QhnObDMGx3Ywl6O8a_IJjrIu2nIwHg50RccbzOQH1ymfZ5WSKXuBhmCi1W0OSneijMiyuH_FFWHZYnTVVcDEDfqsdw2rztJiHDpfUt1sQ-f2PvjJcxrbyfujJ0N-RnEcS_R4rlxCAt1c2QevgdyUfsGZZ04aj7Yw3_skRb5ompoCrowzzX0JVdMWFzuOk_8t2B0kVjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم جديد يهز ريف حلب السوري</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91125" target="_blank">📅 02:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RvCU4M6ddM95KkxO-OGgwiNwZxQv5r4mzHwL0ciqRXVteKTPkRcdX1fXSZYVpuJcfAAxn15IeVxlmhKXs2TC7PCk7EJCgAjpS0156nRVfu1vbMF1g0xHQvzqSRV6d-IRGenZz-PJEeVSnavoLptUqzJQWtCjXXf_ZUepWkYZCN9f56MaNxGCyrCvdhL0i2VuJNWvY7tBAEGvM5JwIqM3I8GEHtpSp4lzZls9YyW0L7i-k93sQLgm26w_KBYAisxEmUTcYvhZfuWpiMBKqwdRyLNqn-LSK1pj9sPRIeYlxB4Dt-IqF0QlDgOh7uLYGPXW2ZdcGo2fWz7RBcYtvL3pb7PfhlrmhUfj_fxF6yu2KsY6jHSoYtnwVCD7sYlSP2t9LH8nGIhDLBLJjvBN0KYz24Hik78m9lGuPU4FrzwXMrDmdDoo-zaL9wY6OJ33K2aijhLnMBwibRkR5vxIBIDYd4pgaoWRszYQkZW05JbDvUepn2EqtBQlA8Hm27Vv5IIIwQSiDrIEvb-VPwS_P_i3EqBd1fMlkNrizz5HfhM6GIjvIJ9QzeyaaO59SzLq2iRXnuTHktKK6bCBIP9ZlNSiWkvrNexTTCOzeF-_oz8BR-G0wi9I7_ll5k7DM-w5f_T2MUr0pUENffidXrkn-8bvtp-Dma1ningpe3OrRWA3X10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a87bdc94d1.mp4?token=RvCU4M6ddM95KkxO-OGgwiNwZxQv5r4mzHwL0ciqRXVteKTPkRcdX1fXSZYVpuJcfAAxn15IeVxlmhKXs2TC7PCk7EJCgAjpS0156nRVfu1vbMF1g0xHQvzqSRV6d-IRGenZz-PJEeVSnavoLptUqzJQWtCjXXf_ZUepWkYZCN9f56MaNxGCyrCvdhL0i2VuJNWvY7tBAEGvM5JwIqM3I8GEHtpSp4lzZls9YyW0L7i-k93sQLgm26w_KBYAisxEmUTcYvhZfuWpiMBKqwdRyLNqn-LSK1pj9sPRIeYlxB4Dt-IqF0QlDgOh7uLYGPXW2ZdcGo2fWz7RBcYtvL3pb7PfhlrmhUfj_fxF6yu2KsY6jHSoYtnwVCD7sYlSP2t9LH8nGIhDLBLJjvBN0KYz24Hik78m9lGuPU4FrzwXMrDmdDoo-zaL9wY6OJ33K2aijhLnMBwibRkR5vxIBIDYd4pgaoWRszYQkZW05JbDvUepn2EqtBQlA8Hm27Vv5IIIwQSiDrIEvb-VPwS_P_i3EqBd1fMlkNrizz5HfhM6GIjvIJ9QzeyaaO59SzLq2iRXnuTHktKK6bCBIP9ZlNSiWkvrNexTTCOzeF-_oz8BR-G0wi9I7_ll5k7DM-w5f_T2MUr0pUENffidXrkn-8bvtp-Dma1ningpe3OrRWA3X10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91124" target="_blank">📅 02:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da96c42899.mp4?token=t7aDLcgm4nXAqzxu1PlNx8RFaU6fJaiJiSQVyVDRldOFtdtb6ZHSLqBeM5HE6lIUiLRZbFXa0i-1oqd1QeH0fiLgrnu-Ktl9opnTeYhu1MJvG83XM2NVQ_AHTL38jfKSMfEFw3ErM_TfNWpVRyYV7pgBR96VTJLwaNivREuN7ByHtO9phITwHEpVO8AxNo24_HLDstwvIwBQrFGlneGpOY-4yPFwH4BMegCFatNo0dVkJ7XQemsHvpwedohceFzMWu2Meft1kIoStQigCwR_zg46g3agZPCYWLPsOGPKU7fqnrflSe77OmRcPuLfCc_hvi0f2U6h9udldWA9yOaBhVf19WvB-IMC4NbELNvm4MszcaVVizBbpQmyqeo7nN8c_mwOwJ7g_mlfTx_d3qw5Rh6x08xUTfa6J9EcP8OEEJtv66_4PLiTZc_Zews0cwIixeJ_5iLZOVfuJpV6vaY1WxO-WfTqR0HClTX6_MNOO1FaM44W-UPY4yJOqq3WGZpP0IBv1NKRR3KWcuj0mp1ueA54X-Z2zS9yog8HvgnqN7Bb86Pz2L2girxvElnjONMqfG9A7776Daudkmn9cur9fdQ2TV2LBgsYzbjpvsmvDfg58GINuqJ247Q4FAHOU5BIp2wx_uMvBy48wwEVi5QBTJRL4d9qlHNdymsxwA3P9GI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da96c42899.mp4?token=t7aDLcgm4nXAqzxu1PlNx8RFaU6fJaiJiSQVyVDRldOFtdtb6ZHSLqBeM5HE6lIUiLRZbFXa0i-1oqd1QeH0fiLgrnu-Ktl9opnTeYhu1MJvG83XM2NVQ_AHTL38jfKSMfEFw3ErM_TfNWpVRyYV7pgBR96VTJLwaNivREuN7ByHtO9phITwHEpVO8AxNo24_HLDstwvIwBQrFGlneGpOY-4yPFwH4BMegCFatNo0dVkJ7XQemsHvpwedohceFzMWu2Meft1kIoStQigCwR_zg46g3agZPCYWLPsOGPKU7fqnrflSe77OmRcPuLfCc_hvi0f2U6h9udldWA9yOaBhVf19WvB-IMC4NbELNvm4MszcaVVizBbpQmyqeo7nN8c_mwOwJ7g_mlfTx_d3qw5Rh6x08xUTfa6J9EcP8OEEJtv66_4PLiTZc_Zews0cwIixeJ_5iLZOVfuJpV6vaY1WxO-WfTqR0HClTX6_MNOO1FaM44W-UPY4yJOqq3WGZpP0IBv1NKRR3KWcuj0mp1ueA54X-Z2zS9yog8HvgnqN7Bb86Pz2L2girxvElnjONMqfG9A7776Daudkmn9cur9fdQ2TV2LBgsYzbjpvsmvDfg58GINuqJ247Q4FAHOU5BIp2wx_uMvBy48wwEVi5QBTJRL4d9qlHNdymsxwA3P9GI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية للانفجارات في مستودع للذخيرة ببلدة العيس وتساقط الصواريخ على المناطق المجاورة.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/91123" target="_blank">📅 02:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde2971876.mp4?token=KmmfxqxlBNLxhSHjFM_6Q34JrudI8YGfD7Qz0oCsz1xpdukjpMtaBOoeIfR7DCZ5dIULi4tgY8AqvEM6Pn_hV-zgxo-yh59-qHW10vLJJjTxieAMJXbIOhYV0uAJKPOu9i2wvEJlH6VPFT1uOTbIrEaG5Q-751BzFAAR06vPoXdCYiZLVQDHmibgkiCc5YdhQB9BH1HsSPHzK-8KwRNYNP9pzkjXXPqDVDxmGXMs3oaykI2DeGgl4KSxR-VKrAl67RYLrkI5gn6F2bIIiSgKAge-c_MaLSK9HeNXjC95Fz-5lXUKReGAXQSIMK9kecKMgZ9xy_UWr8-Jj72ObW_OiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde2971876.mp4?token=KmmfxqxlBNLxhSHjFM_6Q34JrudI8YGfD7Qz0oCsz1xpdukjpMtaBOoeIfR7DCZ5dIULi4tgY8AqvEM6Pn_hV-zgxo-yh59-qHW10vLJJjTxieAMJXbIOhYV0uAJKPOu9i2wvEJlH6VPFT1uOTbIrEaG5Q-751BzFAAR06vPoXdCYiZLVQDHmibgkiCc5YdhQB9BH1HsSPHzK-8KwRNYNP9pzkjXXPqDVDxmGXMs3oaykI2DeGgl4KSxR-VKrAl67RYLrkI5gn6F2bIIiSgKAge-c_MaLSK9HeNXjC95Fz-5lXUKReGAXQSIMK9kecKMgZ9xy_UWr8-Jj72ObW_OiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة جدا تهز بلدة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91121" target="_blank">📅 02:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=pFSlKMKLDNznzzxl565DJy1LyK1HsLgmqKJSRIp66rag-NVjGEbMw8dIiUGx91QLpQTf228GgHJZRDv3w2Z6Kp9CRDFKb_pKZoM-R-Ad2mUhU_OQsqGOgcR2m_tlAhfGmQg7Hvfqv1-FFzo4-QC9KxT8pW4x_iHLNNsxF9_VXXYSO_qNmtrYLOf9_j9xV8I20tba1yuU7Vmj7GwwZqP3OirwXHyPVTHKWoWOdSzOhHENB4JY6hyRYDP3yXc5NYnF37AbZyGnN0xUsJ8O_YY-HdrWoWzSnqXeX4YKY_Iy2qF15jJWUWizojrwUy7kBoCySvJeXho4e6oQE_qyyRKlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8eb87be9.mp4?token=pFSlKMKLDNznzzxl565DJy1LyK1HsLgmqKJSRIp66rag-NVjGEbMw8dIiUGx91QLpQTf228GgHJZRDv3w2Z6Kp9CRDFKb_pKZoM-R-Ad2mUhU_OQsqGOgcR2m_tlAhfGmQg7Hvfqv1-FFzo4-QC9KxT8pW4x_iHLNNsxF9_VXXYSO_qNmtrYLOf9_j9xV8I20tba1yuU7Vmj7GwwZqP3OirwXHyPVTHKWoWOdSzOhHENB4JY6hyRYDP3yXc5NYnF37AbZyGnN0xUsJ8O_YY-HdrWoWzSnqXeX4YKY_Iy2qF15jJWUWizojrwUy7kBoCySvJeXho4e6oQE_qyyRKlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تساقط الصواريخ على المناطق السكنية القريبة من موقع الإنفجار في منطقة العيس بريف حلب السورية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91120" target="_blank">📅 02:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=RRyZIL3WpyYkA9N4IG36EogRG3Ut6xf-hfRDUSDJoZIjjr_XQwcKzvSbUcoOGRoed5wPraMau46upvzf1UccXV3SlldbSVhwo9CQ97fAmYTpBOgrseW7RxS1fVCDAtbIVCJth16kmXBikl9d8iPfwoloZI3re1owG-P5PTHVdBgXpkcpChH3rNQO62_FPvy0eQKav2YhCXKAza3cK73QuxCw1J2mLMH49JG0oac3nb2zq_FbMdupUt61HD5hnOl701CRip8yTCxki6_XxZIPiKEYizg5SW8wgQPy0WGQamr41kxl39q28wIQtzKOkxmst1GjotMYHVvkjnPxBp7izoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba1da90c7.mp4?token=RRyZIL3WpyYkA9N4IG36EogRG3Ut6xf-hfRDUSDJoZIjjr_XQwcKzvSbUcoOGRoed5wPraMau46upvzf1UccXV3SlldbSVhwo9CQ97fAmYTpBOgrseW7RxS1fVCDAtbIVCJth16kmXBikl9d8iPfwoloZI3re1owG-P5PTHVdBgXpkcpChH3rNQO62_FPvy0eQKav2YhCXKAza3cK73QuxCw1J2mLMH49JG0oac3nb2zq_FbMdupUt61HD5hnOl701CRip8yTCxki6_XxZIPiKEYizg5SW8wgQPy0WGQamr41kxl39q28wIQtzKOkxmst1GjotMYHVvkjnPxBp7izoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تظهر حجم الإنفجارات وتطاير الشظايا جراء انفجار داخل مستودع للذخيرة في بلدة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91119" target="_blank">📅 02:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=Uigka9cqjOBFOnNGCRilLbVpksISe1w7hosyjo0ZC-8XvYMkpmR457VcMPVELbtAYXxl_xqggKwO3N_-0TXb0xSEv8bDkWPQ-hcgiMW_hS-r89f1AJJyCoYjwCWfZQzLPu7dhgZsXZ3tBN9UsjnZ8bkMdTXBX5MMPli6ybqTsC2UTl5LKi7aRPy8CK7Vr1KZHK5vE9cKFx0W4lX4S4fDyh3rTlYBhS2R-U2PBBFykrgTdixT8h92Z8Fo6vg0iWKieybIWlnboCUbYBzbvUJCq_nTJmfB-ViF69KgLpUxqo7o0Qvcykk1o6gQ3yMqkVvwWD6aC1mjAfPwcp5RkfaRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18d21c1595.mp4?token=Uigka9cqjOBFOnNGCRilLbVpksISe1w7hosyjo0ZC-8XvYMkpmR457VcMPVELbtAYXxl_xqggKwO3N_-0TXb0xSEv8bDkWPQ-hcgiMW_hS-r89f1AJJyCoYjwCWfZQzLPu7dhgZsXZ3tBN9UsjnZ8bkMdTXBX5MMPli6ybqTsC2UTl5LKi7aRPy8CK7Vr1KZHK5vE9cKFx0W4lX4S4fDyh3rTlYBhS2R-U2PBBFykrgTdixT8h92Z8Fo6vg0iWKieybIWlnboCUbYBzbvUJCq_nTJmfB-ViF69KgLpUxqo7o0Qvcykk1o6gQ3yMqkVvwWD6aC1mjAfPwcp5RkfaRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91118" target="_blank">📅 02:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=Sm4DV7L7o31YSxdX_MdyesQWykpvniCdx9xwV7B6eKBjOUnGB2o-tfA4Ks_YinOpLP9CSn_sDKD9xGnKsa97QvH8rJeJgFI-eqn5xHn-3vMM0MbVi_ssZnGlg1sgByognnQOaP5_K4TIcma4KeoGVZZLtuHY1ELD3GRzK9Lcc3LlwiiSYgBdVQdc47Glv20_kVjYytVv6Q7iM6P-gh4hn_cRJG8AHNNRv6pLo0aJQqkRifhzwzais6EE_4cxxyePExQ-p47OKgQ-2uDiHrQ6P-uRqZk3HNGAgYXBc070URgljrsKLyb7I3xUhmcxobL6Z4xJTKNxcCfW2dz5ePtJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f307feb1ca.mp4?token=Sm4DV7L7o31YSxdX_MdyesQWykpvniCdx9xwV7B6eKBjOUnGB2o-tfA4Ks_YinOpLP9CSn_sDKD9xGnKsa97QvH8rJeJgFI-eqn5xHn-3vMM0MbVi_ssZnGlg1sgByognnQOaP5_K4TIcma4KeoGVZZLtuHY1ELD3GRzK9Lcc3LlwiiSYgBdVQdc47Glv20_kVjYytVv6Q7iM6P-gh4hn_cRJG8AHNNRv6pLo0aJQqkRifhzwzais6EE_4cxxyePExQ-p47OKgQ-2uDiHrQ6P-uRqZk3HNGAgYXBc070URgljrsKLyb7I3xUhmcxobL6Z4xJTKNxcCfW2dz5ePtJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في منطقة العيس بريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91117" target="_blank">📅 01:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=qYALpBC4wbU5rMnKVHvJNfAOxmvx6SQDEDCWaJxO3-d3qw-jrOY-Dixx0iGLOsWqKdpfCJw1WDiHGruG9l20kGeGJmv1rl1dBBSJKHO4yzi3S0CbL2L_uNRsIQeZAjaulPDbvNOeVHghr56W8hPXX7QQGgFpLpki2txrWj_9ifvQzjXf5rPf6YrwhKvwzyB8B2-3_9JnwZDYZh_ieEZClgRwOOuEBvUlovC0d5tLWA0EfEeRiozXeihVJ9c-vI3VWBNIFd0_GaHc4gYO-FwPOAOIYRjBKIu3JohaygkqC2uhtJ_BCQDb0KVY-37-YCIMEUVAIz5UsyzeHB68KT1XpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c39943a5.mp4?token=qYALpBC4wbU5rMnKVHvJNfAOxmvx6SQDEDCWaJxO3-d3qw-jrOY-Dixx0iGLOsWqKdpfCJw1WDiHGruG9l20kGeGJmv1rl1dBBSJKHO4yzi3S0CbL2L_uNRsIQeZAjaulPDbvNOeVHghr56W8hPXX7QQGgFpLpki2txrWj_9ifvQzjXf5rPf6YrwhKvwzyB8B2-3_9JnwZDYZh_ieEZClgRwOOuEBvUlovC0d5tLWA0EfEeRiozXeihVJ9c-vI3VWBNIFd0_GaHc4gYO-FwPOAOIYRjBKIu3JohaygkqC2uhtJ_BCQDb0KVY-37-YCIMEUVAIz5UsyzeHB68KT1XpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من نقطة قريبة للإنفجار الذي طال مستودع الذخيرة في ريف حلب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91115" target="_blank">📅 01:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇮🇷
الولايات المتحدة الأمريكية تصدر تنبيهاً أمنياً يحذر جميع مواطنيها من السفر إلى إيران "لأي سبب من الأسباب" ومغادرة البلاد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91114" target="_blank">📅 01:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=fu7pD1EMi63teS_Bz1fEmAKxxqkCyjvukcvRfubiUMn6i8SR86aV_KnnqJ0fVMrYcWfSnH_l6YREsakK-i7Cd87Oph6K6rDQ2BvLNEKwX9s2JS0bwSRlTvvSuwm3bz3RdmxbdSl7KBM9yDLtRg8-8DqrMG6XDKWXcWwlscehLxOpaBXWgFFkEoxZvdgkblGF7N2FKEJyfIANR8tS8Wm_FhBuIVAj65QHAu3G26f_0_mTa2EKC_I4vHsFEX6Uat0vxbuv9tJVX8U5RTaoyfv96emkYEpjVYKqpeT7GXpuu8FPph0BVloHhUz4J6dA06hP3Ez6R4qaHaiRyy5SFy-_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8a8ec7c2.mp4?token=fu7pD1EMi63teS_Bz1fEmAKxxqkCyjvukcvRfubiUMn6i8SR86aV_KnnqJ0fVMrYcWfSnH_l6YREsakK-i7Cd87Oph6K6rDQ2BvLNEKwX9s2JS0bwSRlTvvSuwm3bz3RdmxbdSl7KBM9yDLtRg8-8DqrMG6XDKWXcWwlscehLxOpaBXWgFFkEoxZvdgkblGF7N2FKEJyfIANR8tS8Wm_FhBuIVAj65QHAu3G26f_0_mTa2EKC_I4vHsFEX6Uat0vxbuv9tJVX8U5RTaoyfv96emkYEpjVYKqpeT7GXpuu8FPph0BVloHhUz4J6dA06hP3Ez6R4qaHaiRyy5SFy-_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات كبيرة جدا تهز منطقة العيس في ريف محافظة حلب السورية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91113" target="_blank">📅 01:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=mQPT4wGiICdxMl2upxWNXECIZKCzfCYDFD9orhEg4DPclZUrDdFEQXp1uON6b8t1bNfvriztLs-J-7bnkzZ5Qq2kzSti5hV8S706uxw0KI-zfgNhuT22ey_Oazmhl5HpKmtevFheN24JHwZKlEIFhX3q5HQfYhljQnV7j6x4bnwGJGKRJdb1XIghH5SvRe9mKALTfH7MWBrfaRd5Uhv4jmdA_ha2rf2TCwhb7XOWJ1-HXPYP_2FPth_yoOuGuLGO7plfCy9Ot5L2lgK7YsG01tTLkCvHSJ4FA_Tc6oRERd4I494H6bnGRkQAK_C5-6tMkDahGuZF3Dmlz_Aou7enQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718fc4469.mp4?token=mQPT4wGiICdxMl2upxWNXECIZKCzfCYDFD9orhEg4DPclZUrDdFEQXp1uON6b8t1bNfvriztLs-J-7bnkzZ5Qq2kzSti5hV8S706uxw0KI-zfgNhuT22ey_Oazmhl5HpKmtevFheN24JHwZKlEIFhX3q5HQfYhljQnV7j6x4bnwGJGKRJdb1XIghH5SvRe9mKALTfH7MWBrfaRd5Uhv4jmdA_ha2rf2TCwhb7XOWJ1-HXPYP_2FPth_yoOuGuLGO7plfCy9Ot5L2lgK7YsG01tTLkCvHSJ4FA_Tc6oRERd4I494H6bnGRkQAK_C5-6tMkDahGuZF3Dmlz_Aou7enQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تطاير الشظايا من داخل مستودع للذخير بعد حصول إنفجار كبير بداخله.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91112" target="_blank">📅 01:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=KiLKfzCQ56X-xdULBytR8SYeCmqCj2hxK9hndNvs0v9s7qoCZacTC5crawattQURFDjmJ3sR3di9aowGWQ5x6pdU6ZvgM4cZRhh26n3q1ulRqQm8QrkivNzX7WJMsDGHEI6yGEgWd3vqDcQphm6S0H8EZLjhhbRejXLTs7-sEzCkagJPEWZNCg8EA3WFuUSNQYNRXzmFPAwvxIuquzfxeieKrVypOVYdweZ3t7WzVJOUrnS8BxAFwcvmfnDV1J6oCM_u41jQsD5hc9LzqYeGBgFTF2mlcMo1K6j1pPUhsPYsgDzaNM8KlnTFY1ylqzxeVn4Vm5lsXMcNaaEVX0pTSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cccbe5bf0.mp4?token=KiLKfzCQ56X-xdULBytR8SYeCmqCj2hxK9hndNvs0v9s7qoCZacTC5crawattQURFDjmJ3sR3di9aowGWQ5x6pdU6ZvgM4cZRhh26n3q1ulRqQm8QrkivNzX7WJMsDGHEI6yGEgWd3vqDcQphm6S0H8EZLjhhbRejXLTs7-sEzCkagJPEWZNCg8EA3WFuUSNQYNRXzmFPAwvxIuquzfxeieKrVypOVYdweZ3t7WzVJOUrnS8BxAFwcvmfnDV1J6oCM_u41jQsD5hc9LzqYeGBgFTF2mlcMo1K6j1pPUhsPYsgDzaNM8KlnTFY1ylqzxeVn4Vm5lsXMcNaaEVX0pTSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مستودع للذخيرة بريف محافظة حلب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91111" target="_blank">📅 01:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4d094526.mp4?token=Ce3B7-1fU7PHr7CGmDKPs7t7p9UQwqMUMMh7HfiHEe8VCEtyBRZaCXuWRWNmA0jel0OtGqZat7MWCso-SEEjM6QMzvAwkZQ6xQBdGrpH8vB41G-iZ6TsjGBWOW9XCc1VZ1B3Y15_9jcRG3LiMbhEON3KTm8WmcDRZN51btom8nz29cSQwm-vSKukxpXspd2J4lDocdj8rF7X6vQinl36Q3d1rOZIA_0R0ex0W3_8cyI28iXRb27y9Lf4svGGo-CSc3L9s9PYI-XeB4dv0dZJOyE7SBv7y6EVdHI_zUKrmbWvlOk3rn6r8xF5K8cKcdBc4TxL8WcPxZx3wQXh6XFeOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4d094526.mp4?token=Ce3B7-1fU7PHr7CGmDKPs7t7p9UQwqMUMMh7HfiHEe8VCEtyBRZaCXuWRWNmA0jel0OtGqZat7MWCso-SEEjM6QMzvAwkZQ6xQBdGrpH8vB41G-iZ6TsjGBWOW9XCc1VZ1B3Y15_9jcRG3LiMbhEON3KTm8WmcDRZN51btom8nz29cSQwm-vSKukxpXspd2J4lDocdj8rF7X6vQinl36Q3d1rOZIA_0R0ex0W3_8cyI28iXRb27y9Lf4svGGo-CSc3L9s9PYI-XeB4dv0dZJOyE7SBv7y6EVdHI_zUKrmbWvlOk3rn6r8xF5K8cKcdBc4TxL8WcPxZx3wQXh6XFeOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ثانوية في مستودع للذخيرة بريف محافظة حلب</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91110" target="_blank">📅 01:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764ed078be.mp4?token=WYQ2Ww8YkyuZc07iNewOJhpX21GrXzeJCaQxZ9JdleVP32T4ArSmbZdDE8-Eei4DOU-SbLIWkf2y2AgTv2OE2RTwWQxk6fQgEhFbbdsIMrMAYliHXQvLCBilWapkI61C_w3kbFndp8ah8GIomYr-1BI0UM0tjCbyAWgn4XZpcoMlXu5OHGNJq94yJ4H5r7P29fejhtFkNl5h9ZGqO_0yjUIgkLlUZz4cZWwyT07t1WEw7hAyz1u4EGSbfhaVun8zV87OidFhv32zl0Z32ocLVdULY7rHxcG89kocbBwV2e56Q-4v2bHia4dsvDCq3kE481VzkQxVhnfv4V9eGk1WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764ed078be.mp4?token=WYQ2Ww8YkyuZc07iNewOJhpX21GrXzeJCaQxZ9JdleVP32T4ArSmbZdDE8-Eei4DOU-SbLIWkf2y2AgTv2OE2RTwWQxk6fQgEhFbbdsIMrMAYliHXQvLCBilWapkI61C_w3kbFndp8ah8GIomYr-1BI0UM0tjCbyAWgn4XZpcoMlXu5OHGNJq94yJ4H5r7P29fejhtFkNl5h9ZGqO_0yjUIgkLlUZz4cZWwyT07t1WEw7hAyz1u4EGSbfhaVun8zV87OidFhv32zl0Z32ocLVdULY7rHxcG89kocbBwV2e56Q-4v2bHia4dsvDCq3kE481VzkQxVhnfv4V9eGk1WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار يطال مستودع للسلاح في ريف محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91109" target="_blank">📅 01:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c708edac.mp4?token=qciAq2HTOxr_1I7dXpBQIsoE5nZBVHO5BZOimDpJ_d5q9T08qKq2ntpRn63RngFSLqETA4Yt4ZgUrrURPwwxlcmvLTqZvqENPfKqljDYOgS8H163mOK41si1nd20tWRxTh5J5hK_7zw5xdeTU7KN0A1hcxwkQS3IVcxuIlXpYMx8Q1DJrhM7AJt8vA4M-F2vOXFcF3ZAME4ondonLscq8go0OVQIjm2n8uXjMwkOlUkshCteI26LrjUSMq0mNGg5blxpFcJbJxAUgrEvsYu5m9CkSeans5JeFmmSzpAdD1w_F-s-icw96iimRffiM0ezu7ZKydxqHziW9uHBaJKT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c708edac.mp4?token=qciAq2HTOxr_1I7dXpBQIsoE5nZBVHO5BZOimDpJ_d5q9T08qKq2ntpRn63RngFSLqETA4Yt4ZgUrrURPwwxlcmvLTqZvqENPfKqljDYOgS8H163mOK41si1nd20tWRxTh5J5hK_7zw5xdeTU7KN0A1hcxwkQS3IVcxuIlXpYMx8Q1DJrhM7AJt8vA4M-F2vOXFcF3ZAME4ondonLscq8go0OVQIjm2n8uXjMwkOlUkshCteI26LrjUSMq0mNGg5blxpFcJbJxAUgrEvsYu5m9CkSeans5JeFmmSzpAdD1w_F-s-icw96iimRffiM0ezu7ZKydxqHziW9uHBaJKT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91108" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22d9b2a4a.mp4?token=piwcpfqTeMdCKkoVA5olEoozWo9hfPS1QcsP4XJ5G9EGWwvzUZ9DW8NLS9q665dfU2w12WVc1qM9wij34OrS7LBNqO2cvVOoZqHW2y9VVck5tMR3RUyEA3ztRaJduUZA_VT8Idb2E3kIkplpTJVnDJBnNCbpUHBVcXsG9Cax-Vao9mC2y__YMtIlLpLUyelBVrubbkCrnq6MAjo2_tj6AIFXuk_sbqSsAARpcmUmO1UQOQBJRj3Iz65lN5p1vpm9V6NQ7Itq9CwaJkbP_qmeA_b31vrRJZqspB89YAj14IqYWIxA1ADaY77hZ3pZSND9L0Rs9mSz8smPLzRUbZNypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22d9b2a4a.mp4?token=piwcpfqTeMdCKkoVA5olEoozWo9hfPS1QcsP4XJ5G9EGWwvzUZ9DW8NLS9q665dfU2w12WVc1qM9wij34OrS7LBNqO2cvVOoZqHW2y9VVck5tMR3RUyEA3ztRaJduUZA_VT8Idb2E3kIkplpTJVnDJBnNCbpUHBVcXsG9Cax-Vao9mC2y__YMtIlLpLUyelBVrubbkCrnq6MAjo2_tj6AIFXuk_sbqSsAARpcmUmO1UQOQBJRj3Iz65lN5p1vpm9V6NQ7Itq9CwaJkbP_qmeA_b31vrRJZqspB89YAj14IqYWIxA1ADaY77hZ3pZSND9L0Rs9mSz8smPLzRUbZNypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91107" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d62f6ced4.mp4?token=qFPBYEnC5F4nduPh6p-mSWfr8LWwCIcdqgAvyeDs48jQkMOEo5xT08EzW374xQAj874BZ2aMX9ap6gTc0om3dVU6qJgOlzk27-dkyUALDf6PmlpzjeyaaJ_HfsTdpmG6hCcSthwsqguGOQ_3b-35USg_P84fLUz_Q8FvIN5nIK9Ftefg5Z0AwqQjXAIYJG7Szhsws9t8r_eYPvf0I_SJ1INgXnLaHtGxpwhm7NOn1xyHox-DKIg7wB-azkCCKAWEvI1zmqye7z43jfGUB39C98h7EzjiiE6et14Z8GbC6GlAO0YKVh5h2yrg64Xw2uAS4hm9mqx8KKpLmtRqGUUUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d62f6ced4.mp4?token=qFPBYEnC5F4nduPh6p-mSWfr8LWwCIcdqgAvyeDs48jQkMOEo5xT08EzW374xQAj874BZ2aMX9ap6gTc0om3dVU6qJgOlzk27-dkyUALDf6PmlpzjeyaaJ_HfsTdpmG6hCcSthwsqguGOQ_3b-35USg_P84fLUz_Q8FvIN5nIK9Ftefg5Z0AwqQjXAIYJG7Szhsws9t8r_eYPvf0I_SJ1INgXnLaHtGxpwhm7NOn1xyHox-DKIg7wB-azkCCKAWEvI1zmqye7z43jfGUB39C98h7EzjiiE6et14Z8GbC6GlAO0YKVh5h2yrg64Xw2uAS4hm9mqx8KKpLmtRqGUUUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني في ولاية نيويورك الاميركية يؤدي إلى إغلاق جسر بروكلين التفاصيل غير معروفة للان.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91105" target="_blank">📅 00:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇸🇦
🇾🇪
استهداف للعدو السعودي بعشرات الصواريخ والغارات لمناطق مأهولة بالسكان في محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/91104" target="_blank">📅 23:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🇮🇶
منظمة الطيران المدني الايراني بخصوص ايقاف الطيران بين العراق وايران:
حتى الآن لم يصدر أي إعلان رسمي من الحكومة العراقية أو وزارة النقل أو سلطات الطيران في البلاد بشأن التعليق الكامل للرحلات الجوية بين إيران والعراق.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/91103" target="_blank">📅 23:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af45cd761b.mp4?token=AH88JDl-Xwke_H1uOXH5dsyDS8JSB9U3aD26aBnpFeMtCih97VPC8C_lfPRwAXli4qxZCpL_okk8d-MT8ARXcdybDW0-v8tcvRXsO5qtiXN0MvTulsNLfwRNvA94INifYdEJdNydR6mYQQGBzS-SqGTdZeLKOdffkZpBZ5lVHF-fyLaOV1v15iOwsnAislXEf5FB5e6ZUvRKrPqJ0h3W0fuU_Q31MkisBS-K7pA0tyd7WgG85IV_jIf05jbhhKQLhwlTGIz7deZ8l8vAnYEizzMBzx0-TyXe5god97kwxTVndF91UjrkGUUCR944cI9iD1k8uiAdfT81GRJBQl4iljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af45cd761b.mp4?token=AH88JDl-Xwke_H1uOXH5dsyDS8JSB9U3aD26aBnpFeMtCih97VPC8C_lfPRwAXli4qxZCpL_okk8d-MT8ARXcdybDW0-v8tcvRXsO5qtiXN0MvTulsNLfwRNvA94INifYdEJdNydR6mYQQGBzS-SqGTdZeLKOdffkZpBZ5lVHF-fyLaOV1v15iOwsnAislXEf5FB5e6ZUvRKrPqJ0h3W0fuU_Q31MkisBS-K7pA0tyd7WgG85IV_jIf05jbhhKQLhwlTGIz7deZ8l8vAnYEizzMBzx0-TyXe5god97kwxTVndF91UjrkGUUCR944cI9iD1k8uiAdfT81GRJBQl4iljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
مشاهد مرئية لأبناء البحرين الغيارى ينتفضون احتجاجًا على الاعتقالات التعسفية بحقهم والتغييب القسري بحق علمائهم ورموزهم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/91102" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
إدارة ترامب مستعدة لفرض عقوبات على المحكمة الجنائية الدولية.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/91101" target="_blank">📅 22:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ميليشيا البيشمركة تعلن توحيد قواتها في محاولة لعدم خسارة الدعم الامريكي.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/91100" target="_blank">📅 21:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعلق الدراسة غداً الاثنين في كليات جامعة الملك خالد في أبها وخميس مشيط خوفا من رد فعل اليمن على الاعتدائات السعودية الاخيرة.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/91099" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 28 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف استهدفت محافظات تعز والجوف ومأرب ليبلغ إجمالي الغارات منذ بدء التصعيد السعودي على بلدِنا وشعبنا 760 غارة جوية.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/91098" target="_blank">📅 21:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سومو
: حجم الطاقة التصديرية لهذا اليوم بلغت 4 ملايين و254 الف برميل.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/91097" target="_blank">📅 21:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية الايرانية تسقط طائرة اميركية مسيرة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/91096" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91095">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6R0Qt2By0HFp5vPU1zxZg3RqovBK9PJgxqa3m6-WNJu06IYy5y_WqNqoE7JAXM7zUeWNqZpX81axJx4cpOz7TcVqTEN70KRT7lpeqsQjyUG3zekDKPTXKt-wGM4hZvuMKGTho8yG0E0vi4a3VAHSa_0zvZkt2AzxpBneUVuRCGVmcEoY704qnwOZ6Et0Z21M_nSwmLTdJq76hJD_Pzjs1dP5B45h4kQs0BFed-Qf4--PmT_IbhBUfPkp_Br28ss-zpJDzl3BtovzA3O0uHqDqXE_fZL_SDO8P6M2ILr_N-sbCQaHd7PeA9fkT2Xworgs7wRCm8GFUB_ceRPkbczkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: أنا فخور بالإعلان عن أنني، اعتبارًا من الآن، أحظر على شبكة "سي إن إن" الإخبارية (المعروفة بنشر الأخبار الكاذبة)، و"إم إس إن أو" (التي غيرت اسمها مؤخرًا من "إم إس بي سي" بسبب قلة المشاهدين والمصداقية)، و"بوليتيكو" (التي تلقت اشتراكات غير قانونية وسخيفة…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/91095" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇷🇺
الاعلام الروسي:
الهيئة الفيدرالية الروسية للإشراف على الاتصالات وتكنولوجيا المعلومات ووسائل الإعلام) أنها ترصد تدخلاً خارجياً في العملية الانتخابية، حيث يتم إطلاق موارد تصيدية متنكرة في هيئة مواقع إلكترونية رسمية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/91094" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🔻
ماذا يعني صعود حزب البديل في ألمانيا ؟!   الحملة الانتخابية للحزب المتهم بالتطرف والقرب من روسيا :  ‏-تطبيع العلاقات الألمانية الروسية ‏- وقف الهجرة  ‏- إعادة تشغيل خطي أنابيب الغاز نورد ستريم 1 و2 ‏- الخروج من الاتحاد الأوروبي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91093" target="_blank">📅 19:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇦
🇺🇸
‏
وزارة الخارجية الاميركية تحذر:
نظرًا للوضع الأمني ​​الراهن في المملكة العربية السعودية، يُشترط على موظفي الحكومة الأمريكية العاملين في المملكة الحصول على تصريح خاص لجميع رحلاتهم الرسمية والشخصية إلى مدينتي الطائف وينبع.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/91092" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuC3XBrzqECBg-aWgyvL0Ei2rmgcXsr5h5ojfep8t33RPyActIxwJNfwJ_ooi5E_cmor1WacJwRgWTV7BLUX14pjo2LrRzymyt2zcqS-_iXy0RtqRdNxdy9dXZ7rkEnrUKtTscxswTKV9GHnWw4mqym5sxjOheExdfwsGppro3DEYbTzgur-1crIpZ9RhKK0kqPHV-q81KfXKEdy4DYjn5BduhfGusXqY9VtPmO_aSu3AEQKWiU5lXpbpi9kv0X-VKH9IYAI-bDC7vXz4E7tHFOop8-oaARfKPEbg2rO_T2NGLMzKHKT3n9UoS-DV1Sb5Pp0YB5sTbh65Zkpz6y07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
كما إننا نأمل أن لا يكون انسحاب التحالف الدولي بداية لتدخلات خارجية في الشأن العراقي مما يخدش سيادة العراق واستقلاله وهيبته.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91091" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuSqrtchuMVXq8JOr2MKd45dwhtkj2CuAn5Y0WEOa6FtjXU2rp6-d3OrTwm0gPn3CPdXw6jSoDEXfBfCu34kmlDYWyBxdZu8Tvs71YjgDdgkAY9FRCn3CAL_eFPgQlI8Sj6idNyZ92kfJ8KpV3OyhnSpJvy6212rCuCVDsLXsxn9Ji8_2J4cQJpJtqFcnao2MBRzdxWvi9S93V3jHLZLCdiZvPMFrjvZ3BWG6hKiv-V-1R7GGpHoXQVxdEALYWQ2xyV7_3V3kvQeI6S-tXefdrSgRnEJBMbXb5_vkNGHBKVyOewQYHXcWKOJX4Hafu-Ow3gU-1TXOTEmS7uocujfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏
الأمير تركي الفيصل:
إيران وإسرائيل تسعيان إلى الهيمنة على المنطقة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91090" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdEXZco_vsOy2Scg0Ekvn7tuzYhB5kEldL6IPRmaISWifTBqNYGnWFo_rtxJe2c6TfOlFC-1Qqe-jCyv1KNpEifRmO6gdSBIYi0qyHYP-LfYEc35SuPPtOJdV3Bp2VIh4i15JUO-qKdyaom8j79cHx67bQM4FVX4Q9v1vm5GvNkkJ49Q4UuOCeGm6JDVbf-sG3dUSkbXneLlnloV7Dv5dDVv-KeRA8uezw-d-alnrGL0mDzA7KTKf5q-6UPm3WrLWgZdCMa9Obqnwjswe1QKpH5f4bl4KEdoGVZgELCizXTIQQLLvQPV-JX6J13X90O2PClWZiTAEC6lsdbaQ3BGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
استهداف برجي طاقة كهربائية على طريق بيجي_حديثة شمال غرب العراق.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91089" target="_blank">📅 18:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">"
⭐️
If you have a
verified
Telegram
account with a blue checkmark, we kindly ask you, our esteemed subscriber, to support our channel by promoting the link and sharing updates on the channel."
في حالة تمتلك
حساب تلغرام موثق بالعلامة الزرقاء
نطلب منكم عزيزنا المشترك دعم رابط قناتنا بعمل تعزيز لغرض نشر حالات على القناة
⭐️
https://t.me/boost/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91088" target="_blank">📅 18:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91087">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سماع دوي انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91087" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab2e5ea9.mp4?token=lbNgvpFhT0puiLvhft01ZfMmitzmgUy-0IUhSedFTHJKEPw5gt-xMbf6LMTTzJRJfgQ4d6TQwLo1LzcC7OcwT9dGJVDfAD9Mj4Dva9kMuJ7rQzLL95QFwpdMuy89_Sw7P-OTi3bMNka2Kp7C2LYU1beFSWbvQ3CVhGId_IFWnPlwjT0bMxKhStSvnyCG2zDeh8BxC1m9ThtZQJ1NuWBSgwUL3eP0cknWw8OalYCF_Zjm_uDqVv4wposYeDhuu5LWpIijuqiJx01Tj0jILmJ-LC0xw1Qlp_GSli9YezXKvuT17JX-oCIinww6E9Ap5YcqraFtP0pYl_bGiXe6q3NY3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab2e5ea9.mp4?token=lbNgvpFhT0puiLvhft01ZfMmitzmgUy-0IUhSedFTHJKEPw5gt-xMbf6LMTTzJRJfgQ4d6TQwLo1LzcC7OcwT9dGJVDfAD9Mj4Dva9kMuJ7rQzLL95QFwpdMuy89_Sw7P-OTi3bMNka2Kp7C2LYU1beFSWbvQ3CVhGId_IFWnPlwjT0bMxKhStSvnyCG2zDeh8BxC1m9ThtZQJ1NuWBSgwUL3eP0cknWw8OalYCF_Zjm_uDqVv4wposYeDhuu5LWpIijuqiJx01Tj0jILmJ-LC0xw1Qlp_GSli9YezXKvuT17JX-oCIinww6E9Ap5YcqraFtP0pYl_bGiXe6q3NY3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية للهجوم الذي طال قواعد الاحتلال الامريكي في محافظة اربيل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91086" target="_blank">📅 17:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W55-qBjm4UFlCUWfH3UEMbfE2RIZ6sU2-SsxrqzlpqwcvHlR9C9WePN1TaD647bPjMNE-Sj4D_q58OOcxbtDiCPkM5rQdGABFY3hIiwOhcQMqPCYut72Jxi6vho_jrX97kIarw9jr8x7f4Tz85vbztbutMcK29f7Hn1vzVPyE45FORgg0zrGtOkvK-puGakqMGApMHpPQPei_f_tJ2mUbX98grxQATBNwQ8AF-O_Ug9a0kUZy_1xwUJX1zfUSIkaS0keAvs-oZUO7M8T24egeh4T4xi4WNVO3pIgVHoHd1SD9QLKOvO7srQIRHGVioSrPtmTfnESRwcUC2_wHJWxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اضافية للهجوم الذي طال قواعد الاحتلال الامريكي في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91085" target="_blank">📅 17:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217ba455fd.mp4?token=pdrr4nkCWEa8MjDbJt6EgJ_FYHCVG0fxErKG1c-qfYmtotlJ6rdXpDabm0yaMfbw1ZQWwRykMK6uXtnH5YBZH4JEhFpCQ7zmGG8BCkhyuOg2SQI-403ezJtLCLYvIDqZu98O-fMnLuOhlTTnPJXwDxxwUMiD099AjQE8TwdhQXRZSAP2fuc9vmOooHYSsQgGM2Pcg3NYsbyOLuje-yvHpeIgmEGwfioD7ZgKkTg6f6aEaY9igXSZ89aYMftzIwRXwD7jDOvttiCd8F9vxiWqxahZ_LzpRNggiR6YOVnSKNLBUNV43xJoQplVX_YPxY-NvmUe-Qh7Cs040uj5LEoSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217ba455fd.mp4?token=pdrr4nkCWEa8MjDbJt6EgJ_FYHCVG0fxErKG1c-qfYmtotlJ6rdXpDabm0yaMfbw1ZQWwRykMK6uXtnH5YBZH4JEhFpCQ7zmGG8BCkhyuOg2SQI-403ezJtLCLYvIDqZu98O-fMnLuOhlTTnPJXwDxxwUMiD099AjQE8TwdhQXRZSAP2fuc9vmOooHYSsQgGM2Pcg3NYsbyOLuje-yvHpeIgmEGwfioD7ZgKkTg6f6aEaY9igXSZ89aYMftzIwRXwD7jDOvttiCd8F9vxiWqxahZ_LzpRNggiR6YOVnSKNLBUNV43xJoQplVX_YPxY-NvmUe-Qh7Cs040uj5LEoSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق لأولى لحظات الإنفجار الكبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91084" target="_blank">📅 17:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c53d118b.mp4?token=lDlwb_pjsVnCVWu_y0izwR5KA8S7OlkHiikoDXp60iAS2aREp5GZWilPRX51Ebz9VOUtMHd4Qq75nWOE9PHDMhVMwVW8hmLut0ETZMfFKeV71QOVfzyGHAc3VaduiYd8GTxtXrXfVMUMYVYTKPdNKr9l4JpTCk4WsU4GIYfi1R_Lk5uOXr6jyqle1EEZkvvZVhseFr8q1sXctbhT_uJkKLOhDuao4ecAAJ6KEkBuAkZn82ZbikZ0QYP9CT_TsBQ9ye-5fNHIRrbT1qE7cwXVC3cC5WZdCxLr3uPWHq8nIU5wXh1Ed58p2oVan5W3JvlE9eWhPe09AwVxjLG9J_sX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c53d118b.mp4?token=lDlwb_pjsVnCVWu_y0izwR5KA8S7OlkHiikoDXp60iAS2aREp5GZWilPRX51Ebz9VOUtMHd4Qq75nWOE9PHDMhVMwVW8hmLut0ETZMfFKeV71QOVfzyGHAc3VaduiYd8GTxtXrXfVMUMYVYTKPdNKr9l4JpTCk4WsU4GIYfi1R_Lk5uOXr6jyqle1EEZkvvZVhseFr8q1sXctbhT_uJkKLOhDuao4ecAAJ6KEkBuAkZn82ZbikZ0QYP9CT_TsBQ9ye-5fNHIRrbT1qE7cwXVC3cC5WZdCxLr3uPWHq8nIU5wXh1Ed58p2oVan5W3JvlE9eWhPe09AwVxjLG9J_sX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من محيط مطار اربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91083" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=WgEKi7GBSQm-ygS2vjRUQx4Pvgq2DXVHFakS8ylbVVqnyJXabHCHjw8IPvdGQVU3fK5cTdjrWSY1iXa5wwkAPXwVVDt-dSNjgSpNrKadGYBWbRKnu2_-VmZKfAm7DXMJA24XfIQYE7AYWMhaYofpeImUXk6Jtk65VAtGbDrBCANJPNR5YQ0dbw66-IrvIF40pWvpSUqPXH-y87o4wlavotbCT5akZpdh_Ipuj8DeFAxdB-kqQ8oGiP20zhbXjsYj-ueiMcBsqaWqGpXrDZgL7yEdNQTs6NT0kWUZV0dFNRXANnvpFZhLNvB3qN1iVp9qpzTeXC475DrhmZQBVwVZkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a9c2ef40.mp4?token=WgEKi7GBSQm-ygS2vjRUQx4Pvgq2DXVHFakS8ylbVVqnyJXabHCHjw8IPvdGQVU3fK5cTdjrWSY1iXa5wwkAPXwVVDt-dSNjgSpNrKadGYBWbRKnu2_-VmZKfAm7DXMJA24XfIQYE7AYWMhaYofpeImUXk6Jtk65VAtGbDrBCANJPNR5YQ0dbw66-IrvIF40pWvpSUqPXH-y87o4wlavotbCT5akZpdh_Ipuj8DeFAxdB-kqQ8oGiP20zhbXjsYj-ueiMcBsqaWqGpXrDZgL7yEdNQTs6NT0kWUZV0dFNRXANnvpFZhLNvB3qN1iVp9qpzTeXC475DrhmZQBVwVZkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الإنفجار الكبير الذي هز محيط مطار أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91082" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=GZEVNatGoGi2UUPIVkYqQm-zqPpg7AxnHBnPJeUWBVh6Pi_MIW06TFrPWaFj0b7ThBiG65aFn9tlw8AKJdxIskftG9enJOu5kXXo-zo-GeDdhI0sA_vMdnTbX-FmViqUpwGZG8v4LgIbF1VaUXLUAF35Cbb1uOcVpd1iRIOBPffm2ECNexlDQZ3XJhUKMp4k_UcDj_4oqE-ecVNWoQ89kCf_zdyHragdobO5S5QnYqNnscMgV9ZfgnY52krrVcWR1nqFRjnnTCT10YlpYQuxQLOGz0jZa4A8bMSS3kS79qEqC9Kxz0dgQFUA6cWVYr3Kfs8TEIOC9f1fDu1U2a2hSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1de0d9f90.mp4?token=GZEVNatGoGi2UUPIVkYqQm-zqPpg7AxnHBnPJeUWBVh6Pi_MIW06TFrPWaFj0b7ThBiG65aFn9tlw8AKJdxIskftG9enJOu5kXXo-zo-GeDdhI0sA_vMdnTbX-FmViqUpwGZG8v4LgIbF1VaUXLUAF35Cbb1uOcVpd1iRIOBPffm2ECNexlDQZ3XJhUKMp4k_UcDj_4oqE-ecVNWoQ89kCf_zdyHragdobO5S5QnYqNnscMgV9ZfgnY52krrVcWR1nqFRjnnTCT10YlpYQuxQLOGz0jZa4A8bMSS3kS79qEqC9Kxz0dgQFUA6cWVYr3Kfs8TEIOC9f1fDu1U2a2hSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق أخر من الإنفجار في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91081" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=kjpNv6IFEfZVfeUSVYHHvhrHCZs6ityv6D-oE_hNv58u_VLOIhOPWA9UzkGTqHpAuycuHKg67N6nvi_UaLAAE9p2Fk1T4ddDwwzJVKaCyxSaf5zjsL3oOCfDsAKI2qR2PanXBMujc46Y9CJWS-p5jTH2X9gYyqkCbjC-c7F_25Adkf3LJV_q2_3j31qkWrIMBE0YltpizqQK-S6lVsBZt2qfVai7EGmKaREaHptSYfvJ72bbM8uFvjXYMvXCJ6Bd6A3-O_pP9WbuqfRJajNhuCKH6WReEMpBgdNZlsV0kmcbSKXbwU1gbKX1eudLugGhIAxlVoE0sv2cMAMyKTSsLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2917e33c9a.mp4?token=kjpNv6IFEfZVfeUSVYHHvhrHCZs6ityv6D-oE_hNv58u_VLOIhOPWA9UzkGTqHpAuycuHKg67N6nvi_UaLAAE9p2Fk1T4ddDwwzJVKaCyxSaf5zjsL3oOCfDsAKI2qR2PanXBMujc46Y9CJWS-p5jTH2X9gYyqkCbjC-c7F_25Adkf3LJV_q2_3j31qkWrIMBE0YltpizqQK-S6lVsBZt2qfVai7EGmKaREaHptSYfvJ72bbM8uFvjXYMvXCJ6Bd6A3-O_pP9WbuqfRJajNhuCKH6WReEMpBgdNZlsV0kmcbSKXbwU1gbKX1eudLugGhIAxlVoE0sv2cMAMyKTSsLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91080" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
