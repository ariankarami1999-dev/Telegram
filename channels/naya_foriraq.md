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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 21:07:56</div>
<hr>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صواريخ انشطارية إيرانية استهدفت البحرين</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/83015" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehkyvmACseNy3XZscZUYtflXm6c4TQd3td_u2IZiC8aIb0uYbmTobHY_p-j7NwDY6IRDHYEAF3lFOKRN578puDNj_ONyQZzCTjON9VwtiL9AeK-SmDnlpN9DPe6-KqvlvQLnHCNmaDGH2K9OUu7PpKyT8f6lNPtwkma802nO4qdYPxqUWJSVE6NqXD_85XnSump_Rd-RIwQsrpGxbRcqu7cjSVXX3bMrSdfbyXnsis6mRmUyUSgVf4F1-5TroOS_g8SotA2r5wKOMW9_43jN3k76UjD_SmjiO3Gbe49TfHjAxb2yEIBVKTgTFqM7EpW_7ZjOMd7mf-bYnK291jtvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية في سماء البحرين قبل دكها للمصالح الأمريكية</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/naya_foriraq/83014" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الكويت تتعرض لهجوم صاروخي جديد</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/naya_foriraq/83013" target="_blank">📅 20:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/83012" target="_blank">📅 20:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
النزاهة العراقية تطيح بمدير الأشغال العسكرية إثر مخالفات ومغالاة بعقد تأهيل مستشفى القوة الجوية - الرستميَّة بقيمة (92) مليار دينار. حيث تم القاء القبض على عميد وعقيدة و 5 موظفين</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/83011" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">إعلام خليجي عن ‏مصادر أميركية: واشنطن تراقب احتمال تدخل حزب الله في أي تصعيد إيراني</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/83010" target="_blank">📅 20:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/83009" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/83008" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
مصدر خاص لنايا ينفي وقوع انفجارات في تبريز أو شيراز.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83007" target="_blank">📅 20:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83006" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83005" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏‌ترامب بشأن مشروع قانون العقوبات على روسيا: "هذا تكريماً لليندسي. كان هذا مشروعه... وهناك احتمال كبير أن يتم إقراره، لكنهم يرغبون في إضافة إيران وحزب الله إليه."</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83004" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ترامب عن الشهيد أبو مهدي المهندس: سليماني - لقد قتلته... وصادف أن قُتل شخصٌ سيءٌ للغاية من العراق في نفس الحادثة. لذا لا أعرف إن كنت قد أسديت لك معروفاً أم لا. لم أسألك هذا السؤال قط.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83003" target="_blank">📅 19:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامب: يمثل النفط العراقي أولوية لنا، وسنُشرك شركاتنا بشكل أوسع في العمليات النفطية داخل العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83002" target="_blank">📅 19:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83001" target="_blank">📅 19:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏ترامب: لا أؤيد فكرة فرض رسوم، ولكن في الوقت نفسه، ليس من العدل أن نحمي هذا المضيق للعالم أجمع، ثم لا نحصل على أي تعويض، ونحن نفعل ذلك منذ سنوات عديدة. لقد أزعجني هذا الأمر منذ 25 عامًا...</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83000" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب عن رئيس الوزراء العراقي: ‏"لقد كان مقاتلاً عظيماً وكان من أشد المعجبين بأمريكا... لديهم احتياطيات نفطية هائلة... لديهم ثروة هائلة."  ‏"لديهم قائد عظيم، رئيس الوزراء الجديد. إنه قائد عظيم. أعتقد أنه سيبقى في منصبه لفترة طويلة... إنه شاب ووسيم، وهذا لا…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82999" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية الإيرانية في محافظة خوزستان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82998" target="_blank">📅 19:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82997" target="_blank">📅 19:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82996" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏ترامب: لا نعتقد أننا بحاجة إلى وجود جيشنا هناك الآن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/82995" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ترامب: نحن موجودون من أجل العراق إذا احتاجوا إلى الحماية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82994" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامب: نحن نحب العراق</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82993" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: إسقاط طائرة استطلاع نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية فجر اليوم في أجواء محافظة البيضاء وسط البلاد.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/82992" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7YYWnoPLGFnCOQ5gKvpp7iJduXxlkHv7qVaZJtAVnWkYbIYZfqXhFBQusQFFHiDok8ceHgbx6K6-_D5iXna1Y4m2zTMbDRdgJy3md6TE3vTzCDsPvVZptF9NHt0_l9orWWX_jiL2noT_4fsBSHyJ8hyQ4M5bNzJzuaVBqJTtJ487XCSDVryJCJW74xFTEqGeigfmhmVrz16EqvNffx00gpenyry-vDiZPciKWZoElH3vvH3Dd8RO_CtboHilCGrqz2GtEg3QsE26zHbXg2hG4dFnY3XrSH4UEG-qdnjjz1vfZ5lrsE_BYbSFULciQvKxHwCU0bQMCUnsrf2Sk_Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s57qNaUiUEAQLtAwDihspomtI9Nfpz-i7oHmqqA8HZqPpYlUWwA93SoYrmSQzHrjGwPizGqjncTX9Qs9NHazLjTkXcJD0fmeJgbZojlh2n6uqu0g8foWblLOSQIfi-4Ga86wO_qzGa7RiSxspfGn4iY5RIr0IRwgepxmL3D8MdDsPPw6GfSr9l-czQ0NwUpHbqwRm_Puy0MP2l0HpItMA0gDAS-rQejuP3nKFxJOP1rOltSMnK1sMBy4wjp8ekAxEZiNQAA_CDpElx85CKKVHguYK6M3bsZPhy7OWHvDqmJSYdjRRYHRUuY64WrdJz4Ia0rlTVP8y-0_lOn0Y13KDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد من سماء الكويت بعد الهجوم الصاروخي الذي تعرضت له قبل قليل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82990" target="_blank">📅 19:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939d8150e4.mp4?token=W_imUD3INL7NEFx38es_nkW6rdlO-gCYjcYtOOzXkuJvPgFUGBA60tEj-Bkv9uckW3tcURa53OrYzYhjrVqcVc1U5cQastrtm0WGqj9f5T1w70vpXxmmzBOqhzUkHRmuvbzhTqwpRDfLpnuda03h-gfGbrxT_wu8nYxrm2sHP5mrSJki3kTGuX9V-E6f9KYrha4lPJJLWDMi6onXsjrIYgtvLuCqPMfv3vyUUu7bb6Ew1aMpalCT2bRcBUQJ04l6-NjbxRj7Gdn9AomqO67REHY4WZZsZ1VN3CxVqcigS4EgOtip5q0EMoFo29GeVORmttoXNfYM7R_2kbgsdoZmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939d8150e4.mp4?token=W_imUD3INL7NEFx38es_nkW6rdlO-gCYjcYtOOzXkuJvPgFUGBA60tEj-Bkv9uckW3tcURa53OrYzYhjrVqcVc1U5cQastrtm0WGqj9f5T1w70vpXxmmzBOqhzUkHRmuvbzhTqwpRDfLpnuda03h-gfGbrxT_wu8nYxrm2sHP5mrSJki3kTGuX9V-E6f9KYrha4lPJJLWDMi6onXsjrIYgtvLuCqPMfv3vyUUu7bb6Ew1aMpalCT2bRcBUQJ04l6-NjbxRj7Gdn9AomqO67REHY4WZZsZ1VN3CxVqcigS4EgOtip5q0EMoFo29GeVORmttoXNfYM7R_2kbgsdoZmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت من جديد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/82989" target="_blank">📅 19:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNf2lve20IT3k6Ug2vD75CuHuCJUtSugH4Brbq0c8mHVDI5RjMje2m7WDoRoZfnllpzcgO7D31h9G7KMxos9ZYhoflifLe2eEG2IWu0kXVcdhve8ObLpOvuQLJgpC9GaKdMEHaqytQz_IChbUUS-ewmFSBbYc8n2ZjGvm3iDgNZlg3X_1Xl0P3xtvKdvmOuLjpya1c7sKNFh-pgbKk-zHRiygpm3VXlKkOXIu67nVEIzZXuOz6MA3tb7Z9XVwMPovNgmKqJrCZ3kE0AXCjxo9EWCKi4i_L1GqgLaWiPIaZWTdlaFkHYjqZSFOrA1aM2b3JQ6sl8q2e947blwflW9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أبو مجاهد العساف لأنصار الله في اليمن: نعلن تأييدنا المطلق لخطواتهم المباركة وتصرفات ممالك الخليج وعصابات الجولاني لن تمر مرور الكرام وسيبقى الحساب مفتوحا
▫️
مشاركة قوى المقاومة ستكون فورية وحازمة إذا اندلعت حرب ضد الجمهورية الإسلامية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/82988" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJKR2ATexx1L_tjlo3s4OxfaH1x7f-LqOOeVhE58x5R_tegDBZBxDRUcwmdUhWuHB4HA21tyeJbkOoYRHK7fhjWwueeiUaOVupTNPzl4fgkSlrLMGQn96gbHSEXqTR0MkfyxAh7XX8XD_deZKy8BUm0608t0d_gNHNeDoflEfP5GHqKyQe4DI4yrvO0COaBW3ymAnixhIkIOkt9SNTUqdsHsWOOkkswEPoSZFidQ2sJUG-0sc6P6q8HRqJKRXM_tt2Nr7LOPJaT_NJyVadsuWRqeLmMIQOysAxc4hd25ycJ0c2OnRcTg3B8kTv3YVuXbiMLSnAUIlNJQyZIiDdZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ينشر صورة تظهر بها خريطة أمريكا الجديدة حيث تضم كندا وغرينلاند.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82987" target="_blank">📅 19:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/82986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82986" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82985" target="_blank">📅 19:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/82984" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇺🇸
شركة الهندسة المائية والكهربائية في جزيرة كيش: الاحتلال الامريكي استهدف إنتاج المياه والكهرباء في جزيرة كيش.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82983" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
أنباء عن سماع انفجارات في جزيرة قشم جنوب إيران</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/82982" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82981" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82980" target="_blank">📅 18:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/82979" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82978" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مشاهد من لقاء رئيس مجلس الوزراء العراقي علي الزيدي  بترامب</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82977" target="_blank">📅 18:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de22772ff.mp4?token=QamZzz_KR1oM2QJ9Si8vF8zmgyrzsW0HwV2gdqXwa6RmahiZmfAFQ5guzGog6hMbnkRiIvGm1UeY5VDtZCWoV_jln8C9iSqYV1uPMx-MdnKSAdjuBfW72foU3Ptc2QvfV6TJ4PiRYcYegmfivh9WVfmK0lc_l6BEyVwfijgfFY25M-O6hWDGpqIsGZnzcmVkw2QlSX6r2ZFMujC3VOmYlbfvm6os-lnrGktOubiqCrm5RkrwInEIFwZyvbTP5vcGLinLsL_Fsa6KnzA9Eu5OBguYiv9Rw2rl_y0ZoH2164SH_tBIZnq5tMkU5h6bWxfvaHdjPTi38qX8EiWafGNcuSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de22772ff.mp4?token=QamZzz_KR1oM2QJ9Si8vF8zmgyrzsW0HwV2gdqXwa6RmahiZmfAFQ5guzGog6hMbnkRiIvGm1UeY5VDtZCWoV_jln8C9iSqYV1uPMx-MdnKSAdjuBfW72foU3Ptc2QvfV6TJ4PiRYcYegmfivh9WVfmK0lc_l6BEyVwfijgfFY25M-O6hWDGpqIsGZnzcmVkw2QlSX6r2ZFMujC3VOmYlbfvm6os-lnrGktOubiqCrm5RkrwInEIFwZyvbTP5vcGLinLsL_Fsa6KnzA9Eu5OBguYiv9Rw2rl_y0ZoH2164SH_tBIZnq5tMkU5h6bWxfvaHdjPTi38qX8EiWafGNcuSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الوزراء العراقي علي الزيدي يلتقي ترامب</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82976" target="_blank">📅 18:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
ترامب:
لقد قررت استبدال الرسوم البالغة 20٪ التي تفرضها الولايات المتحدة على سفن مضيق هرمز باتفاقيات تجارية واستثمارية
سنفرض حصارا كاملا ولكن فقط على السفن القادمة من الموانئ الإيرانية والمغادرة منها</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82975" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
حدث أمني اخر في عمان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82974" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/82973" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8332e5e9.mp4?token=MILUNOEkfkH0UJEp421PEqZJHS0AjcQybcQnnznB75hKmLmCZHlFw7LvmNtHTanKbmu8qgJsWDet9AMZBV9V8Ksw4rWKfUVDUUTnJWr2qZgiP0Em-Z8Y5vplOByvKtF_0CK_rmJJRqYI1cg9W5Uf6QpP0J6F-e95a1igzf34KHAnnqzvMP5mX8T7nuWhM3GnOHlEdRmew_dOluTp5NkmSSUdzd5FK7R48EJ_UghU7rfZ2lNopLTfzJh420xYchaJqIGysMl57aLiLmF430EGmpMHQ9zuTtLi8g7iZTS7M-8xosNOzscLYq0x_1r3FVeLNo5eURYPBZQI0qlYMWOi9xja_4tIdb2Zl93o0MS8MWWIIHtRZ7PQ6ztDOue-LYeu8_FJ85vuBsTSx16gjZaUtzRZ7KgqqPKZ1ysfjILYb0K5Y8MS1gKTEE4AhTeSver2gW-DdMkQFoMNxqOznatbbtqWVw9KEoCpCFMzZSU0y8fAl-fo1OrMeuKgGFFRt3lq35tj5PUkksSXcMl0vsBOuFKchkkUsfEzaeNpMn-89Cf8ggNVSWTpCn7NK48bnzwJ6p6G_kNDKmkNfObU7ZUqe2M4DGpcP19gjcrGZUIfFws78TLcG4_uVl9G4uS5Z7R8wA1cdZEx6ATOB1Ns7GbXk_M3wJH7rhBYUofFcDtBnsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8332e5e9.mp4?token=MILUNOEkfkH0UJEp421PEqZJHS0AjcQybcQnnznB75hKmLmCZHlFw7LvmNtHTanKbmu8qgJsWDet9AMZBV9V8Ksw4rWKfUVDUUTnJWr2qZgiP0Em-Z8Y5vplOByvKtF_0CK_rmJJRqYI1cg9W5Uf6QpP0J6F-e95a1igzf34KHAnnqzvMP5mX8T7nuWhM3GnOHlEdRmew_dOluTp5NkmSSUdzd5FK7R48EJ_UghU7rfZ2lNopLTfzJh420xYchaJqIGysMl57aLiLmF430EGmpMHQ9zuTtLi8g7iZTS7M-8xosNOzscLYq0x_1r3FVeLNo5eURYPBZQI0qlYMWOi9xja_4tIdb2Zl93o0MS8MWWIIHtRZ7PQ6ztDOue-LYeu8_FJ85vuBsTSx16gjZaUtzRZ7KgqqPKZ1ysfjILYb0K5Y8MS1gKTEE4AhTeSver2gW-DdMkQFoMNxqOznatbbtqWVw9KEoCpCFMzZSU0y8fAl-fo1OrMeuKgGFFRt3lq35tj5PUkksSXcMl0vsBOuFKchkkUsfEzaeNpMn-89Cf8ggNVSWTpCn7NK48bnzwJ6p6G_kNDKmkNfObU7ZUqe2M4DGpcP19gjcrGZUIfFws78TLcG4_uVl9G4uS5Z7R8wA1cdZEx6ATOB1Ns7GbXk_M3wJH7rhBYUofFcDtBnsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
جیل Z من شاشات الألعاب الی ميادين الجهاد!
المقاومة الإسلامية حركة النجباء تحذر: آلاف الشباب ومحلقات FPV على أهبة الاستعداد لتنفيذ العمليات ضد قواعد الاحتلال الأمریکي
🔥
"Coming soon: FPV drone operations in Iraq."</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82972" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82971" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
استهداف ناقلة نفط مقرها الامارات ترفع علم ليبيريا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/82970" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkMUwLecXalQ8Q0EiGzCmiKDJYjra33rYQKjZwKnUnnQIaETM2Xuoq5zHtVthzel9aud-zBoDmxrY2pjfJ7SUIJXPJkOoZY1hqL_zoJbb8jnaT7Gi5PqvKS8SMK45wpnLfPcqEqnjodzptsTaXS0D3RS0H32rWP6HTI_8PGSpr9oF0KQSj954FPbMr6ns9jKG6TM1vtJ71Rg5W7rvMNwJcXTKl2bNhuLWmOKexmOTcK3vTuh8Ja-Fz9jQoWbhW7MiHAq_MEPNZXe41yQPwXkSsl4wT5kyLN-EAWC2pdnFsHD9KuCOT1i4cFFUNjNrthC2VauaHeipbYfUZehFSWdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82969" target="_blank">📅 18:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82968" target="_blank">📅 18:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رئيس الوزراء العراقي علي الزيدي يلتقي ترامب</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/82967" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قوة مسلحة تابعة لعصابات الجولاني تحتجز السائقين العراقيين في مصفاة حمص والسائقين يناشدون الحكومة العراقية لانقاذهم واعادتهم الى البلاد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82966" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
‏مندوب أميركا لدى مجلس الأمن: إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82965" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
‏
مندوب أميركا لدى مجلس الأمن:
إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82964" target="_blank">📅 17:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82963">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/82963" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نادي النصر السعودي يلغي معسكره التدريبي في ابها ويعود الى الرياض بعد هجوم انصار الله</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82962" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مواقع متخصصة في تتبع حركة الملاحة الجوية تظهر استمرار إغلاق مطار أبها السعودي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82961" target="_blank">📅 17:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82957">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIk087OGv21E1kbTzoeJUbCqfHhOUmjmlAvLyTPdUxG8y4jtEctOpVjsDtIAsu-LO43LnefrOYEhs3-kmD_TWrAoVWuwY54VbenXAQxrMifErcGaXkK0EG1_r_p_egv6Gojte-zTMfgOA1TIqPONqKVP5MFEI76vpvU-GeI4UFHYjWCmbljlAXh6SY8ZE7zuWGyKjyk3r2o4mGoMJZWCUi2GWiiyqTG9RuhjwajY7OUhdbIcWiWYQkYIoHyGUdz3IYeMqyhb8J6sCByMUJo6x4J5Y6oqavTuyTIdgZtzV0x9lu3ZXSBGZAh8Qi9me1Rjgtszf9Ux9s7Wxgn4aYf9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
الاعلام الحربي اليمني ينشر:
نحذر جميع شركات الطيران من العبور في الأجواء السعودية وعليها أخذ تحذيراتنا على محمل الجد حتى رفع الحصار عن مطار صنعاء الدولي
We warn all airlines against crossing in Saudi airspace and they should take our warnings seriously until the blockade of Sana'a International Airport is lifted</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82957" target="_blank">📅 16:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قوة امنية من بغداد تدخل ناحية الزوية ضمن محافظة صلاح الدين شمالي العراق وتبدأ حملة تفتيش واسعة عن (احمد اسماعيل فرحان) احد المتورطين في قضية عدنان الجميلي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82956" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سوالف الگهوة  رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82955" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سوالف الگهوة
رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82954" target="_blank">📅 16:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82953">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaWMcqCR0RESGBnth05AfRzZ1wOr_OryBZ8bpFiyfZixpoiYKngDBpOHpJXIWqyimDi7LTQ-73vAava-4_dWKXi3cjVlx25aJ3nBSp64mhLaejTKBDaHi8OHUDgF4WGbt7PZBqE89AtmWVje6lyjwGjtjgEC1aTEyoG7w4KZCgZGzT67VxcUpXCtHlai1DgbzdxzRmn4qlswhzvne4K4kVB23-KElpe9IUynyqCzQpMBbNz34dLc2XunHsSrWp9ojPP98deGKHXhe5Y3fBnfajum2kD8IVTnarZe-hPnzBxglDdcto7wbLWzVau0bHIcOWHB3qUjq-lyC_YsYSTh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نحو 180 نائب ايراني يوقعون للمطالبة بإعلان انتهاء اتفاقية إسلام آباد مع الولايات المتحدة ومواصلة عمليات الانتقام لقائد الثورة الشهيد وسائر الشهداء</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82953" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82952">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتن ياهو يجري زيارة الى مفاعل ديمونا ويقول:
لقد أزلنا حاجز الخوف. لا أستطيع أن أقول ماذا سيحدث في إيران حاليا، ويمكن أن تحدث أمور كثيرة. نحن مستعدون لكل سيناريو.
أقول لقادة إيران: لا تراهنوا على أن يسود الهدوء إذا هاجمتمونا، لا تراهنوا على أن تكون هناك إعادة للرد نفسه، سيكون ردنا مختلفا، وأقوى بكثير.
انتهت الأيام التي يقصفنا فيها أحد ولا نرد عليه بضربة مضاعفة. هكذا سنفعل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82952" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
الهيئة الإيرانية لإدارة مضيق هرمز:
قبل التصعيدات الأخيرة التي قامت بها القوات الأمريكية في المنطقة، والتي أدت إلى إغلاق مضيق هرمز، خلال فترة ثلاثة أسابيع بعد توقيع مذكرة التفاهم، قامت أكثر من 200 سفينة غير إيرانية بالتنسيق معنا، وقد حصلت معظمها على تصاريح العبور والتأمين.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82951" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اندلاع حريق داخل مطار البصرة الدولي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82949" target="_blank">📅 15:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏وكالة سلامة الطيران الأوروبية: يُمنع على مشغلي الطائرات العمل ضمن المجال الجوي للبحرين والكويت وقطر والإمارات العربية المتحدة، أو المجال الجوي فوق مياه خليج عُمان.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/82948" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏وكالة سلامة الطيران الأوروبية: يُمنع على مشغلي الطائرات العمل ضمن المجال الجوي للبحرين والكويت وقطر والإمارات العربية المتحدة، أو المجال الجوي فوق مياه خليج عُمان.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82947" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الاعلام الايراني:
عدوان امريكي يطال مبنى تابع لوزارة البيئة في قرية سيد جوذر بمحافظة بندر عباس مما أدى إلى استشهاد ثلاثة أشخاص..</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82946" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04058516a3.mp4?token=eqUO883jfrOnSm_uxof-6UBacoNCV6KGMwh00sX51sy1tsaS4kBkv3UWPLuWgGuqp6NTy14rFv9DD_LWj6r0XGxTKv05AKhTSjRXqG-tedkzW-5IcWQJbwouoABWI5zoxZhLrpKzdDE0rRQsclSTUKZxwuKGR0EggtjoB2QCup6D91kNzS3_TM91BpRjKiFTb69tifvSGZh0mdhS5QAVn09TgCXLMSCqll6vZgsWsyDKv_0loveT8F-BZpkHvnt7sebZPQof9pN7kc1eOQIvUzwJoX6_O2Gw0Lrbor2mrggiRfeLRZQua2E6DCnnzpxazni7w97Tf7j7qg6LomiIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04058516a3.mp4?token=eqUO883jfrOnSm_uxof-6UBacoNCV6KGMwh00sX51sy1tsaS4kBkv3UWPLuWgGuqp6NTy14rFv9DD_LWj6r0XGxTKv05AKhTSjRXqG-tedkzW-5IcWQJbwouoABWI5zoxZhLrpKzdDE0rRQsclSTUKZxwuKGR0EggtjoB2QCup6D91kNzS3_TM91BpRjKiFTb69tifvSGZh0mdhS5QAVn09TgCXLMSCqll6vZgsWsyDKv_0loveT8F-BZpkHvnt7sebZPQof9pN7kc1eOQIvUzwJoX6_O2Gw0Lrbor2mrggiRfeLRZQua2E6DCnnzpxazni7w97Tf7j7qg6LomiIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قوة امنية من بغداد تدخل ناحية الزوية ضمن محافظة صلاح الدين شمالي العراق وتبدأ حملة تفتيش واسعة عن (احمد اسماعيل فرحان) احد المتورطين في قضية عدنان الجميلي</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82945" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اندلاع حريق داخل مطار البصرة الدولي</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82944" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محافظة خوزستان: تعرضت منطقة في مدينة آبادان لإصابة قذائف أطلقتها قوات العدو الأمريكية. سيتم الإعلان عن تفاصيل إضافية بعد الانتهاء من التقييمات الأولية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82943" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82942">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عدوان امريكي يستهدف عبادان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82942" target="_blank">📅 14:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عدوان امريكي يستهدف عبادان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82941" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
اللواء رحيم صفوي:
قبل 15 عامًا، نظر الإمام الخامنئي إلى إغلاق مضيق هرمز كأداة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82940" target="_blank">📅 14:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82939" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
صدرت تعليمات استثنائية من سلطة المطارات الإسرائيلية إلى وحدة التحكم الجوي الإسرائيلية، تنص على "عدم السماح للطائرات التابعة لشركات الوقود الأمريكية بالهبوط في مطار بن غوريون".</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82938" target="_blank">📅 13:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏شركة ستولت للناقلات: حريق بأحد ناقلاتنا أثناء إبحارها قبالة سلطنة عمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82937" target="_blank">📅 13:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏شركة ستولت للناقلات: حريق بأحد ناقلاتنا أثناء إبحارها قبالة سلطنة عمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82936" target="_blank">📅 13:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKGBmo5ztM4PZjg-pGezuyRCDnKS8ee_C5cyhA1S75aWJFWFUQy_sN93I5PLtrEk6f0JybXqQuuBCMAVh6to7fTneO_BShcNx0yWLQ2d9nNcQqf9pzKxUnTe_luDmmp1fo31tdvS6Zq157BTz99SazYhUqAdxRtvBkPE6Ik10j1gGVx54JscHFrzvqPZQkrIqUbF2AaFILVfvmEf8u1Io_lZFR99ZMlmm7ks6j4mwSIqs0jYyrJQPdD7ejsQcf8G2TWJk7h8eVPvGLJu0dtLbtgV199qznYkbqdXmDXNv-WvzEaYUhfPdBZiNik0t9E74Y6RLA09V3gzzvDL2cUfiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTegcaUYzsZOM2MGndM8zP53FrZwCXOUEO3ZhQurqINnm2qQzGV95lbW9MbkA1_lM9W14yhOKdwif7SnXCYADgREwUpMTkohpjWgmTgpsqO4P773uAab4FvZgbPgBHFXon-9Tix_81m8QaaRA99MvCOj8ZeMQ6j_d5fYnb8Dy_FGev3KC_V-4Kp8FTqgDJFcjw_4r_Rg2AXvV9dSdZOgVkqi8XMSp5bRsmiufxYIBlnw-wT_djQ9FIKXb-mhDyKyRqP9p99gnbBziiCXLfEMljC0Vsi5CH4GzFtSvsatneFeCCHlkDNEwg_xbAOBF4bwJJ_fGpWa4l4ee0RENEiq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوي انفجارات في بوشهر جنوبي ايران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82934" target="_blank">📅 13:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFJiz1Za9RENcCxGHQ0_7j6xzhjkz9VjJuq6OLb9NC5t5ysYjYVrVZ-iOLumqCnH4S6EsC1f8bgLGMqWmyFVHPgN-MPcBF_tyqs3Lc8mGzOFRZZMojBuUCyb0jmckKHzkUtqI8SOd9Fj_MuXBmOxEHut_uKeGns2QWMpf32Ja5P_1LpNzaLZsxNNLzp1WLl8pQ9LKdURMn7qNGxyHiaeMub4veBQa_7RKcTD-5w79RcxgWOgAE5XTzHOsh15V_Z-m11j3hvwqIkCfA6xuyVJWUVkwcEO_mONLvLVGT93lPmCF0ZC6qF5r2EL4N0-P30v7GVfCRZy7a0zfzJmeT80Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWi1oteFijPTH3hJJNNPuRLUZWJu9oTeS8Uszdc4TUwuk-Qo1OQfvyDi2x4g6I9loHB6IzfoqwrKEr6Yb3MnwgiqdL3moL85r7W56YJQXjMCySKZAPe8k_PDFthKtBLHnCUOCtCGh0_btGr2NPZtRMWtLql9mxHlu_zAwJ59FLRtVjVJbcX0XehKf_nW23hTSfW_VmAXbyXfWl1-0S987qwQnhP-VZYh4RFBaTFJPto_EEZpBxA7dh2Y9moT3jLgmjXIYTJKS-FDmeIQaUzrayE9J54M1OFzIER6AF6WVObxpxDcafU97VTXu0xfsK3Z_BjijO860nir5XZpIC_93Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة إلى الدول العربية مكتوبة على صاروخ "خيبرشكن" قبل الإطلاق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82932" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
رصد إطلاق صاروخ من منطقة وسط قطاع غزة باتجاه البحر.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82931" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوي انفجارات في بوشهر جنوبي ايران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82930" target="_blank">📅 12:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
اعلام العدو الامريكي:
تفاصيل خطة ترامب بشأن الرسوم الجمركية في مضيق هرمز لا تزال قيد التوضيح لكن ترامب مصمم للغاية على تطبيق رسوم بنسبة 20٪ على حركة المرور عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82929" target="_blank">📅 12:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/82928" target="_blank">📅 12:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82927">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82927" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزير الخارجية العماني: نتحمل مسؤولية للعمل مع ‌ إيران⁩ والمجتمع الدولي للتوصل لترتيب يضمن حرية الملاحة بمضيق هرمز</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82926" target="_blank">📅 12:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزير الخارجية العماني:
نتحمل مسؤولية للعمل مع ‌ إيران⁩ والمجتمع الدولي للتوصل لترتيب يضمن حرية الملاحة بمضيق هرمز</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82925" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgeHzaAtbFMPoNNZrfOD9-Yqx5HUn3SHhWAtj0SOhktMHE0jmkV9ZHj2DCvcVE1zisKiFT46abERlSFaDW0FlN1sNXgpw5-qB-Z3LOXMVs_Wzw8qHyH18Yc7t0166pQZQ1HTX-iR8ghMSQdBBSEIQiwjbetS8hfLS_HAk6H9wLsw0E5_HmW5pkbX8rNjXsnFta7jRZub77VuDy29gW1WLzD4i2StXYweYMhCHs13ADipvB1q0NueUpJWqvCHYvTAeV7AN3wipynTlw5kCy4lWrvV1LQz7CLa06Qw-Nqv4fh5sl_WSjFFUPjuhvCbo5nfLb-m5q_YEHDh_XLUaaKskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت تتجاوز 86 دولاراً للبرميل لأول مرة منذ 12 حزيران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/82924" target="_blank">📅 12:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الإمارات تُجبر على الإفراج عن 55 صيادًا إيرانيًا كانوا محتجزين لديها.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82923" target="_blank">📅 12:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
مشاهد اطلاقات صاروخية من الحرس الثوري صباح اليوم حول قواعد الاحتلال في بلدان الخليج.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82922" target="_blank">📅 12:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
عمليات بغداد تنوه لتفجير مسيطر عليه لمخلفات حربية اليوم ضمن مقتربات مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/82921" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🌟
استشهاد 3 مواطنين من عائلة واحدة في محافظة هرمزغان الإيرانية جراء العدوان الغاشم الأمريكي.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82920" target="_blank">📅 11:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjhk5JSa3vMNLaMPnUwdEMHUzUcpOZxVTLn88mknTLtHd8nxBo4PYYHmdNX71rky17-1gSVF-mf2soQAPNbGSC3GnSXEf9IfqJdBgZwHrt048aWwpo_5p4mqNcreKRB3RVGVWe1ic2qQSYL7KfYBo_SqDreRUWhYnqJV8A8NDfirWOAdTgs0aQWIh9k0GL_UbgjrDMjWhofLfPCZjEQEwsHVSfUW7666PNMERkaUcJgA_Aut1Kle9Ty_1nbxXNPCWb8sGSyTqJ4hPi70y5BZCMvfBH1n98ucP4o3zf5Sjsjcoi3eq5draR4Jos1fOGKpllJg26sBFtwcGqG26vmHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت تتجاوز 86 دولاراً للبرميل لأول مرة منذ 12 حزيران</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82919" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
وزارة النفط الايرانية:
استمرار تصدير النفط الإيراني دون انقطاع على الرغم من إلغاء الإعفاءات الأمريكية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82918" target="_blank">📅 11:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlkvffGrq-4KSJ2CIYP0GeWcwcVAE4m3gtRCCQQOIINo53y5u2lUdY35tCjN1iwWK2IckatF99WGz5ZZpDVoQ8wexLslnKCLAvdr3xwL_7tAgw2EVWaFvxC4YzZNgQCwkGIRaei7AQqq_PHNoSrJZq1vaR7m4K7_XxxjopSbnNOxyG2ph7PfKgcY7PEFvot2RGYiOcSLOE6Eh6qZGu2kWfvk7rQUXSqbrzUqlg_RC4QwF4X_Ok8T8t-UxlAcXBTg25WE8y3W-opgZXKAUCAzSxbEOZnGtto3L1nJTc_hN5fXwFc-EMTGbV89FxmGpdcVyqZIgVYdcVug0MEPg9W75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
التجارة البريطانية:
استهداف ناقلة نفط بصاروخ عندة سواحل عمان اثناء محاولة عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82917" target="_blank">📅 10:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇨🇳
‏
الخارجية الصينية:
قلقون بشأن استئناف الصراع بين أميركا وإيران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82916" target="_blank">📅 10:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82914" target="_blank">📅 10:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9c004a63.mp4?token=Yapc7kwBqG0Err2VVYqIYCLhrzFL24h5kCxVU0kl3fkEBgs9libytGiaW_7ugejNMLKc04KxBrRWSZjJtVheYsrocBi0Iw6TsiTxD7a7dHUx8NJkxHldI4qd_1PYazjU6UyO5IuI0kXshlmrjYvd7Xa3qVnkg5BudI-6BGR2sGwaj2TeUgRq-xWaSFwru6QCFLCXFAbB4IgPakngaWHycdFnXRkjxM1o3ojzynEev16YfkYmnwiG9Qz8dYz-xAZ9nE7NQgdN9HRn6RfajfjPFNGA4qI1wrsxqDXBUNVSiP4xmHgq15oXH-hlAAhOwjF4Rcj6clqKgtydttTNT3qIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9c004a63.mp4?token=Yapc7kwBqG0Err2VVYqIYCLhrzFL24h5kCxVU0kl3fkEBgs9libytGiaW_7ugejNMLKc04KxBrRWSZjJtVheYsrocBi0Iw6TsiTxD7a7dHUx8NJkxHldI4qd_1PYazjU6UyO5IuI0kXshlmrjYvd7Xa3qVnkg5BudI-6BGR2sGwaj2TeUgRq-xWaSFwru6QCFLCXFAbB4IgPakngaWHycdFnXRkjxM1o3ojzynEev16YfkYmnwiG9Qz8dYz-xAZ9nE7NQgdN9HRn6RfajfjPFNGA4qI1wrsxqDXBUNVSiP4xmHgq15oXH-hlAAhOwjF4Rcj6clqKgtydttTNT3qIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرازيل لولا عن ترامب: قال ترامب في منشور إنه سيعيد فتح مضيق هرمز، ولكن على كل سفينة يسمح لها بالمرور عبر المضيق، يجب على صاحب النفط أن يدفع له 20٪.  ألم يكن هذا يُسمى قديماً قرصنة؟ كان يُسمى قرصنة.  يجب على دولة مهمة مثل الولايات المتحدة، التي بذلت…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82913" target="_blank">📅 10:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82912" target="_blank">📅 10:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac97608a61.mp4?token=eAjeYfpBEu1NQDdwCscWORzrT3d4UvkLAPm1-C03Dlh6r-iePdod-AYFZ8DOSk55apHnDl6KOil_KmoOGcUTx7m6r0jtEEU7OhJKU58Tbz7pgJkzBLC2qFDCnaoNisbtXAlpZHHPq1PndFtXwOvXYxfMOIQjOdxWCeZE1PdaBo_6HuxpMAj7khngzcE5sfg5-6SPftoZeicQY2XjCCWFrxneo0G0gksLLTQY3zVfkUkb48LLvaweFKBZaGdOORBhJodDholFhqn_TTQXx9B-bfP-1tHb6jthzvEga7cJwhOa_NUeinRsmoyTYkDQA6xndR48Dqs-SnIYnlTTqV--2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac97608a61.mp4?token=eAjeYfpBEu1NQDdwCscWORzrT3d4UvkLAPm1-C03Dlh6r-iePdod-AYFZ8DOSk55apHnDl6KOil_KmoOGcUTx7m6r0jtEEU7OhJKU58Tbz7pgJkzBLC2qFDCnaoNisbtXAlpZHHPq1PndFtXwOvXYxfMOIQjOdxWCeZE1PdaBo_6HuxpMAj7khngzcE5sfg5-6SPftoZeicQY2XjCCWFrxneo0G0gksLLTQY3zVfkUkb48LLvaweFKBZaGdOORBhJodDholFhqn_TTQXx9B-bfP-1tHb6jthzvEga7cJwhOa_NUeinRsmoyTYkDQA6xndR48Dqs-SnIYnlTTqV--2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: من يتحكم في مضيق هرمز حاليًا؟ هل هو ملكنا؟ أم ملكهم؟ أم أنه محايد؟
ترامب: نعم، نحن نتحكم فيه. هم يمكن أن يثيروا المشاكل. يمكنهم فعل أشياء ليست جيدة، ولكن نحن نتحكم فيه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82911" target="_blank">📅 10:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
مصدر ايراني الانفجار الذي سيسمع في اصفهان وطهران ناتج عن تفجير ذخائر حرب مسيطر عليها.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82910" target="_blank">📅 10:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الهند تستدعي نائب السفير الإيراني بعد مقتل بحار هندي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82909" target="_blank">📅 09:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇱🇧
في وقتٍ تحاول فيه إسرائيل استباحة لبنان، وتسعى الولايات المتحدة إلى تعزيز وجودها العسكري فيه،
الرئيس اللبناني يدين الاعتداء على السعودية والاردن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82908" target="_blank">📅 09:01 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
