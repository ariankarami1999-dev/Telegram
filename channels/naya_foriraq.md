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
<img src="https://cdn4.telesco.pe/file/mS2imGDr675hJ8BXp3mRkUQ_ZEafQTKKiL8CoLokq8OPRpG1z5D_8or4yLr28va6PjJQyCHTwbTOxtUux3JH9PGq_baAWflqybossL7_40CsPQd3FBJATjqe86Ks2Aa2RlNejQ-w8YWtH3pmjIkIsZrejsg3GPT8_-wKQnPXRFqlJuNbQUTsosnaiPLjXeRKUPKfgfzjSyBNLq34OiiOJcEraAyzw0Bpkq8STWb9b5-HLK8Ye9jwhmHnZi8sUEa0N9XCkqxXehLLBUCrLiwPYF-jXmCvQVcvYg9L0px62fiail2YCysZO_lyTDbTPU4zxWq4ixhge4sgigRgkSDM8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فانس: ترامب ملتزم بتحقيق وقف كامل لإطلاق النار في المنطقة</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/naya_foriraq/79479" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فانس: هذه الهدنات دائمًا ما تكون معقدة بعض الشيء.</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/naya_foriraq/79478" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فانس: حثنا ترامب على "طي صفحة الماضي" لإعادة تشكيل العلاقات مع إيران</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/naya_foriraq/79477" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فانس: هدفنا هو إعادة تشكيل الشرق الأوسط من خلال الدبلوماسية المشتركة</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/naya_foriraq/79476" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فانس: تم إحراز تقدم كبير في الساعات الأخيرة</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/naya_foriraq/79475" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/naya_foriraq/79474" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCFt2XLFVQR6gg6h2FQsEwFc340nibuF8paYuU1ndj3VjZdG_bIbPcBfkiClI0IK0fPw4HdHYtHRIK4_KnSwsTCB6ofmvmKFLwnvH-k7Izs9T6R3GJp8FuqVejFCzx3YkUnMLGV02l1fvH6zwzc97Y09imt3DjPNPmqWC0RwAFaAh_QuV3T2uLByTsSTB5TcXbuSchTUFEY2Y7b4qc63qLbIcXqvTWFSH7oVox3uhj1rcoXtMTyS--9-pzYx2kDEkB32GPAWlopkHJYpLQ-fgmkHJ1R-Xfd73dRWx0ARfadFiA9lecHVf1gi1w7KaBRMS6z7ph5cSDvbdYZqnXkF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/naya_foriraq/79473" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/naya_foriraq/79472" target="_blank">📅 16:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-06-2026 آلية هندسية تابعة لجيش العدو الإسرائيلي في أطراف بلدة أرنون جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/79471" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/naya_foriraq/79470" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQpzmUtV_mCiPvwXfPKrNwz5sIk8KRGZ34WYJvhDa5igczdGGTUlz3RhEKDFBnSLXt-DB4qGa804IwvB-FDlqdFLMlZklthJXbgmb7UtpQGjzy_hrQ07nz9efTHvvBs0Xw0Z0Xi_8Jg2dmZ8sdQvssCyzdAdAs78djy1P-eUxoMY4hBDVW7OxLx926RT08XG65ZGj5DSFWtgm9V2UNJgmKc-ZrlQMiCQ6CN_crUiE1y8LfGlsF6BsWFPe2624fyBDLisa9eJsYboeaEnnln6FajrPSuhA4vHaWpEjVheEKBM7_zcR8-BPwLEUuN34T0DMa-TIJK28mrZZY3P7yxmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿ وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِندَ رَبِّهِمْ يُرْزَقُونَ ﴾
تدعوكم المقاومة الإسلامية في العراق كتائب سيد الشهداء لحضور مناسبة الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي واستذكار سيرته العطرة ومواقفه المباركة.
حضوركم وفاءٌ لذكراه الطيبة، ورحمةٌ تُهدى إلى روحه الطاهرة.
📅
يوم الاثنين 22/6/2026
🕐
الساعة الخامسة مساءً
📍
بغداد - البنوك - شارع الكنيسة</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/79469" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiT8ewQNS14nIts3HcpszNKoUYWLoLlawfnQ_2Iq5d01NYYPdAocPheOoy6yJwnwYo8zecDAhADYvHAhlLRSAjEqOAbvUJHfTwp9DYzhQZOVyR4KDZxXNXrvNfO7jpWFTjvaWDF1EQlI6Q3o8CfbMSOTqdRPrjOWhrZSdPVh7J9HYBVakCPJt5QN6Ah56z8XIGFP9wbJcjkkk3ylBwIOW4hDInTWv-Bjy3-CHtBqvmJN2fVkrlqXTXK7I49par7Xn-drL53rYySQ3AMa29ghs_JZCOehYvO0LG5NJYXqZFWvEVCVVC-6O3VMop0v2sHA1D32z1yve2H8bVCsGoDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران الشيعية
استخدمت مضيق هرمز من أجل شيعة لبنان
برأيك لم لا تستخدم تركيا و(الخليفة اردوغان)
مضيق البسفور من أجل غزة!!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/79468" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy7d2Fs0JwfLra41C8mst4CIzPmep_3VjHxlong7WydQAml8d-Z-tQ2LTummghxvAiPhXhI2BT6EjAMMREsL3gEgXQwhKJ4dV-pUER7mxNKmptEQPufTjQkc7ZzSLXdWLWy6BYo0dRWyu_hhBXhAfb7ydarz3BGBuseF6XWbTEypSA0KgA43ovYPyiW9qOlErWChvZUf2y9ocaVDtgp_smabBvsuib1H7uz-Ey702vQJsE6lLCkXE37pjDFDtufz6jOKgJYrPFWx6nVoIhvYxpj74H51HvzkByrhYcdq2JSNrP2c0bjtW7Wn_vB2cMMad1QiUk72jsFYHWNTI5EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعمدة الدخان تتصاعد بالقرب من سجن بادوش في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/naya_foriraq/79467" target="_blank">📅 15:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
‏
وزير خارجية باكستان:
أميركا طلبت نقل مخزون إيران النووي وتوصلنا لحل "خفض التخصيب".</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/naya_foriraq/79466" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
مجلس محافظة الأنبار يعفي (رهيب حميد هايس) من إدارة مؤسسة الشهداء في المحافظة اثر خلافات سياسية داخلية داخل المحافظة.</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/79465" target="_blank">📅 15:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3460aaf297.mp4?token=H3UJ8j0zZqbjtnEC9HuuOAs_9L98hbbB0-bOd720DqA_VBUO6IFBZ1O6VqS8-tV1c1yBV_U3ObyaYpbrFwDozwqgrq2hHrmvgLg3gqV-Bupxz12siZASfCko0Qiq1CSdWW-aEdmmYglkZZERbBbaIgwlg7hBfGR4T2SFXwHbamNnWNdF9ndX8Myws4H72c8YGEt9GDvo7bO3k3gtFlgak6ce9gJyi7EcnsAKXcwf__11lXLb5tS5gEvvVd1oxFE0C1xOY2MfMVrD1BkHj5KehUJ5V9nTCWI8CqcIEkEEG1J_AQZaM9to3PZ4imBByx9mLi2CRdiGZTK4hmB88APzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دهوك ضمن اقليم كردستان العراق قرب احدى المستشفيات اثر مشاجرة عنيفة.</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/79464" target="_blank">📅 15:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
محافظة بابل تقرر تقليص ساعات الدوام الرسمي إلى الساعة الواحدة ظهراً في دوائر المحافظة إعتباراً من يوم الأثنين الموافق 2026/6/22 ولغاية نهاية الدوام الرسمي ليوم الأربعاء الموافق 2026/6/24 لغرض فسح المجال امام المعزين والمواكب الحسينية.</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/79463" target="_blank">📅 15:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10626f3f5b.mp4?token=bLfy2zwVzyoErAOX4QF0mK-5FE1i5cEZ7rfBuhFEdAKbeOei-SDTLypAfrneQF_L6CcM0qKdusr8Ynabojs-meTdzxyk-GlAFb3dQskXLZeKirpLe7I2puUEPz8Zqm-JppKAOvU_BDRzJRW5Gd8pFjC_7YVDx0H-qGFNizvnX3OLAwFYIhIm2kgTzv0MvB9Eq1wsKJO29Fhzh-OThEYfYl3R7zF1PpFC6V6lGJu71KFvZF_YFv1pB132r9XylO5qojQncLo4aMuTpnI4LALRunLm-e36kQMoX0M-PoAamNJcQbfpk205UWpiF5cEuvBvW3ukEpo8QkQltYQw8r7fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قاليباف ينشر مع بدأ المفاوضات</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/79462" target="_blank">📅 14:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcfQNDZqDt4HmBt1OIaNgUh-uz7OQIMGi9iEvhEQ0WdEo-EgNp-zkth92YxlAXfzYyrppe5sq1_hZlTKOesNUeMQKTNyHdm6-qFHr9VIhAW0VxpWiic1XK1ROi-b_hcTsP_yXMRsKlqfkgTJrKaveMjRr7Vl_faAKeLUUk_lc9yK57p1LM51qm-QC94dH5xNZ8pUR4TcpY0SMNau7Twy59tv6YHUu3PDt_lxv_cIHKlhGpRpMTrw0tf_LuPTE6uYRU-qGa67JWlsyhnDiAoJjcVdBPAD8demKAQDEV-YJ1jpNnsaz9KYtVSbwmxNxm9fGr_RF1KwtePOGFfEdMfeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضيحة تهز إقليم كردستان العراق..
ضبط رجل الدين السلفي البارز وأستاذ جامعة السليمانية (عبد اللطيف أحمد) متلبسا بإقامة علاقات جنسية مع طالبات قام باستدراجهن.
أكثر من 10 طالبات أخريات ضحايا له تقدمن بدعاوى قضائية ضده بعد إحالته إلى القضاء للتحقيق في القضية</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/79461" target="_blank">📅 14:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🫡
خلية الاعلام الامني العراقية:
في تمام الساعة 02:00 والساعة 02:20 من هذا اليوم، تم تنفيذ ضربتين جويتين ناجحتين على مضافةٍ لعصابات داعش الإرهابية في مناطق مترامية في عمق صحراء محافظة الأنبار. ​وقد خرجت قوةٌ مشتركة من أبطال الفرقة الخامسة والصنوف الساندة بإمرة قائد الفرقة لتفتيش المكان المستهدف. وسنوافيكم بالتفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/79460" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم الثلاثاء تزامناً مع ذكرى استشهاد الإمام أبي الفضل العباس (عليه السلام).</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/79459" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
وكالة مهر:
اجتماع سويسرا سيناقش 5 بنود من الاتفاقية من بينها بند وقف إطلاق النار الشامل في لبنان وبند الأموال المجمدة لإيران.</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/79458" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
في السابق، كانوا يقولون إنه يجب التفاوض بشأن صواريخ إيران أيضاً؛ لكنهم الآن يقولون إنه كما تمتلك الدول الأخرى صواريخ، يجب أن تمتلك إيران أيضاً صواريخ باليستية. القاعدة تغيرت</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79457" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
- تحذر مصادر في الجيش الإسرائيلي من وجود عدد من الحالات الأخيرة التي ركز فيها حزب الله على استهداف كبار قادة الجيش الإسرائيلي الميدانيين في جنوب لبنان، وهو ما يثير مخاوف جدية ويتطلب تغييرًا في أنماط العمليات.
- يُقدّر الجيش الإسرائيلي أن حزب الله قد أعاد إنشاء نظام مراقبة وجمع معلومات استخباراتية مقابل الخط الأصفر في جنوب لبنان، وأنه يشن عمليات ليلية لتحديد مواقع القيادة العليا في الميدان وشن هجمات.
- يقول مسؤولون عسكريون أنه لا يمكن تجاهل حقيقة إصابة قائد سابق للواء 401 بجروح خطيرة جراء هجوم جوي بطائرة مسيرة، وإصابة نائب قائد الفرقة 36 بعبوة ناسفة، ومقتل قائد الكتيبة 52 في هجوم جوي بطائرة مسيرة، ويجب الأخذ في الاعتبار أن حزب الله يستخدم التكنولوجيا، لا سيما ليلاً، لرصد النشاط اللاسلكي والإشارات الدالة على وجود قيادة عليا في الميدان. وأضاف المسؤولون أن هذه الجهود تتطلب مستوى عالٍ من المهارة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79456" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية: استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/79455" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
المتحدث باسم الحكومة العراقية:
استكمال الكابنية الوزارية سيكون في النصف الأول من تموز المقبل أي قبل زيارة واشنطن.</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/79454" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZh3fznDi33Fi9vlWmwFPjCodsYTxFtnDpVwRz_J1SYgI2D_yksTmGFUWA5QeE55r2KkpVWENjCbO0svav-UoB20cx8Rj7Bc_vqT1vz75Ra4YQV08W_Qkv9qRCBTwSWfhc-41i6LbHIS7YRGTWxL6r5DCedKDF3ZMbcV33sWZDY3hnH53A4Aoa7QOp5tfxJv1A-KH2LGwHF-VBhHNweI1cI1RSBIk8YJl22xaCjbvtE1aBkeS_CG_MFJbYFO1NPd43BOhxysxBzlCpu0yPyyW1Ua_rcEaOYsLNc4rC2MQ5hgQFRbBSqH0rAMTwMR4xNh6OLRo4URiXBAJc82mbBjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
رسالة نائب قائد كتيبة 52 في جيش العدو بعد الكارثة التي حلت بهم على يد حزب الله:
كانت الأيام القليلة الماضية من أصعب الأيام التي مرت بها الكتيبة. فقدنا قائد كتيبتنا وجنودًا أعزاء سقطوا في المعركة. الألم عظيم، والفراغ هائل، وقلوبنا مع عائلاتهم المفجوعة.
رغم الألم، أنجزنا أهم مهمة ممكنة - إعادة رفاقنا إلى ديارهم. بعد جهد كبير وفي ظل ظروف صعبة، تمكنا من إنقاذ القتلى من ساحة المعركة ونقلهم لدفنهم في إسرائيل
اليوم سنرافقهم في رحلتهم الأخيرة. سنقف شامخين، ونحني رؤوسنا إجلالاً لذكراهم، ونضمن أن يظل إرثهم وروحهم ومثالهم نبراساً لنا.
هذه لحظة حداد، ولكنها أيضاً لحظة وحدة. الكتيبة قوية، والمهمة مستمرة، وسنواصل القتال بكل قوتنا، بمسؤولية ومهنية وشجاعة - حتى يتم إيقافنا، وللمدة التي تتطلبها كل مهمة!
أيها العائلات العزيزة،
في هذه الأيام، أنتم أيضاً تحملون عبء المعركة على عاتقكم. إلى جانب المقاتلين والقادة على الخطوط الأمامية، تواجهون القلق وعدم اليقين والتوتر المستمر. نيابةً عن قادة الكتائب والجنود، أود أن أقول لكم شكراً. شكراً لكم على صمودكم وإيمانكم ودعمكم وقوتكم التي تمنحونها لأحبائكم كل يوم. أنتم جزء لا يتجزأ من
من عائلة الصغار وقدرتنا على إنجاز مهامنا حتى في أصعب اللحظات.
"سنعود من مهمتنا مرفوعي الرأس، بعد معارك دامية."</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79453" target="_blank">📅 13:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
‏
الرئيس الإيراني مسعود بزشكيان:
لن نتخلى عن حق تخصيب اليورانيوم.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79452" target="_blank">📅 13:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCZDP9cvt-PxZOKWruB5r6CbvsarqMxzYaatTEWaWceAilI1k5uaLHoWzqPZ21CUGG2hDO5wEOWBjs6JlvT4VaUEmpq22rWYvldcq4eCX1R0aeTRJJVie_WxLr5s_6Gw01xv4ZWRf_R0bFv6WN4bOK56-ks8Ppvkroifc0fBa8MwtyxIBzoD6xJKeXh_Dfjpawvkh_sB2iNADobYwiQijyl63g2ak4s-1B6AHdIePIepZqaE07_QtxqKyXBUp9Fa-5XmfUoG5pzqBeZSnqBEq95vC0nVErq4bYQi6Z-5wDYzLZ9JXSpmvA6LXNTKRCL75Wv2FWfPgjDZ3PccJYTm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🌟
مطار بن غورين يشهد إخلاء طائرات التزود بالوقود وتوزيعها على قواعد سلاح الجو في الكيان المحتل حيث تبقى طائرة واحدة في  الساحة الغربية لمطار بن غوريون</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79451" target="_blank">📅 12:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
هارتس العبرية: نتنياهو أمام معضلة، إما البقاء في جنوب لبنان والمخاطرة بجنوده وبالعلاقة مع ترامب، أو الانسحاب وتلقي هزيمة في مشروع حياته.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79450" target="_blank">📅 12:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNeoX7vjSlUboH0k1EEzHnxTHti2F3TSlXvnWuy3bkiX8U3KONZnufiLX4gf0wyHd2CYc3nHxvFxKXvkJo0lboJ7SC6-1xf7grXJ3yIdhxnoEIl6H72NI_Mu8HsmmlzcyEoMtil-tWV4OdHKmxja3VfkFv_X8Hn0Qdgzdjd-7g-2zR6aBJfpQnwvzs_fq_LPeBtoidHujIf2YNofPs5m1p8ikHxYLTGa4ztMHW2P8_ikP9HKF7VmZUfseB2_dq1a5evZDmat65Hl1lWQPUf_yWJXttckgZxberc-Q9snlNw6sIGQ-BqtYF6FvsXwtwXhrD1_q2YrlQ2vAEHE9XBmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يراد منه دثر إسم قوات
الحشد الشعبي العراقية
تدريجيا من الذاكرة العراقية
الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79449" target="_blank">📅 12:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79448" target="_blank">📅 11:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مقتل اسرائيلين اثنين بظروف غامضة في لوس أنجلوس</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79447" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79446" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=kBy0AMGwSSeigKzntbErqFEprp22CvFJ6shqlbfe2JK7KH-GwH1pQKZYXlEfhaV8Q4KzSz4jj-tC0sg7ATF2N2X6Pd9uQNtksuFZ7EXJ0RGlveXLg16WX97yxy23yN-_4WbKWfjFlkNpsZ2dKVSWZGSAAk2XuYaA8tNo9JnsxtCiDPXd1NNjac0aaasZYn45c3pzkDJkXaKhRYQR2DmCEImj-1Kgvazc9QClwjUe_eDfNPG52N4gl0OWRiSnQR8PjKQeFnIpRckGQKCG4-xFPrNdSTZS-8EFVhMh1X0dCUGA3TQ1nav1cRDnp8B2u24SFToGZEiNRt84qXL7OFzlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f73573e0.mp4?token=kBy0AMGwSSeigKzntbErqFEprp22CvFJ6shqlbfe2JK7KH-GwH1pQKZYXlEfhaV8Q4KzSz4jj-tC0sg7ATF2N2X6Pd9uQNtksuFZ7EXJ0RGlveXLg16WX97yxy23yN-_4WbKWfjFlkNpsZ2dKVSWZGSAAk2XuYaA8tNo9JnsxtCiDPXd1NNjac0aaasZYn45c3pzkDJkXaKhRYQR2DmCEImj-1Kgvazc9QClwjUe_eDfNPG52N4gl0OWRiSnQR8PjKQeFnIpRckGQKCG4-xFPrNdSTZS-8EFVhMh1X0dCUGA3TQ1nav1cRDnp8B2u24SFToGZEiNRt84qXL7OFzlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بث مباشر لتوقف حركة السفن التجارية في مضيق هرمز بعد إعلان إيران لوقف المضيق يوم أمس.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79445" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=DJ7NCskD4T14zZNfNV1uljU6miyZQ3OrlwpVgOH8rquMPF4EyhvUyNBNM16nB_d3qG3C4XQw_RF539tmoGyD4ZJkT9STrKZFbOpo-hC55Ce4J8SJsjpewJXs-eUZKEftmcWT4jPHhJsNXyZ3-PkZV3h-uQ7HmmvrLuH-og4OQEKKsmVtrjAcy84C9nVAhp7HZpbkWLh70y24HR2h-d2zLecK0443k2J2k_NDGnwIsGP8dZFDaa7sErZpL5TQZQN4SBxCh1Uy4Wi6myrtUdmLn6DwWqhNLYy0k4GfnNviWfDNUbkZu05a12p9KYcS6kbHJMkGusS3-4wZfzPsclsRUwv7NhY8GGjFDkmG49SGnPDRoFPh1TdEVEn4Wt44et_1HnnLOy9qFwkEiHZXWqb_i79lpG_lK1eO0SfnIKZY3GNjlLBKi-t2ORf8pbCQ-UlUMFl9-_-QP11w4FJjDH6HI-OMZKR-6fD383OYQNulOGCZUbqaEYcKMd60Zhx64QMeltB5MuxbbUR2Z-vsVPaT3cxEvsUQGFLYRT0ga821pkRGCkbv2RSTSBSzBTaCf9_57jdICG5PtRmnGd9RUMfQBCODkRrVw5651X-489_D3u89jmFuipcbN33B__VVlDsa9YEOFvAyWGjhHRpBjKMGpUhyqwYUE33ZWYpiYZHlQ3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d381d8e4f.mp4?token=DJ7NCskD4T14zZNfNV1uljU6miyZQ3OrlwpVgOH8rquMPF4EyhvUyNBNM16nB_d3qG3C4XQw_RF539tmoGyD4ZJkT9STrKZFbOpo-hC55Ce4J8SJsjpewJXs-eUZKEftmcWT4jPHhJsNXyZ3-PkZV3h-uQ7HmmvrLuH-og4OQEKKsmVtrjAcy84C9nVAhp7HZpbkWLh70y24HR2h-d2zLecK0443k2J2k_NDGnwIsGP8dZFDaa7sErZpL5TQZQN4SBxCh1Uy4Wi6myrtUdmLn6DwWqhNLYy0k4GfnNviWfDNUbkZu05a12p9KYcS6kbHJMkGusS3-4wZfzPsclsRUwv7NhY8GGjFDkmG49SGnPDRoFPh1TdEVEn4Wt44et_1HnnLOy9qFwkEiHZXWqb_i79lpG_lK1eO0SfnIKZY3GNjlLBKi-t2ORf8pbCQ-UlUMFl9-_-QP11w4FJjDH6HI-OMZKR-6fD383OYQNulOGCZUbqaEYcKMd60Zhx64QMeltB5MuxbbUR2Z-vsVPaT3cxEvsUQGFLYRT0ga821pkRGCkbv2RSTSBSzBTaCf9_57jdICG5PtRmnGd9RUMfQBCODkRrVw5651X-489_D3u89jmFuipcbN33B__VVlDsa9YEOFvAyWGjhHRpBjKMGpUhyqwYUE33ZWYpiYZHlQ3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر: الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79444" target="_blank">📅 10:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
مصادر:
الجلسة الرسمية الأولى في منتجع بورغنشتوك في سويسرا ستُعقد عند الساعة 2.30 بعد الظهر بتوقيت القدس المحتلة ؛ الملف الأول للنقاش بعد الجلسة الافتتاحية هو تطبيق البند الأول المتعلق بوقف الحرب خصوصاً في لبنان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79443" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🍅
الأردن: محاولة تسلل إلى المنطقة العسكرية الشمالية الحدودية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79441" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=FCVcCpice6aEF-TSQk9PDQCw1_CB--6znVchUfcMDKF8IOUfIX0QVfbnLBzx4gVY1mzALSPiNx2dj88qBvDm4KWH0O3mG27dL4atD0UdFHvwqXZel0CRaCD_J-Rd61gSYN9HvbqQaIV0N0sf5JVXbfA5HWYckaHKmehmQkMCkBhYT8M1xkarCVB9VPZDPVKlQDP92AheGapAmgRICMa93XcSpI8_-feH4bDf2wIAsaQia2JweeLgRORQcAOPB_UFLxOMnYA_KpJZ-C9QbHEJ1VUYPHAPiSWPdW_C1hJ1LH0py4N5C8x7hLkaCx0w-Alwm4UgCoCXHGGRE8yRW5TnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbff44506.mp4?token=FCVcCpice6aEF-TSQk9PDQCw1_CB--6znVchUfcMDKF8IOUfIX0QVfbnLBzx4gVY1mzALSPiNx2dj88qBvDm4KWH0O3mG27dL4atD0UdFHvwqXZel0CRaCD_J-Rd61gSYN9HvbqQaIV0N0sf5JVXbfA5HWYckaHKmehmQkMCkBhYT8M1xkarCVB9VPZDPVKlQDP92AheGapAmgRICMa93XcSpI8_-feH4bDf2wIAsaQia2JweeLgRORQcAOPB_UFLxOMnYA_KpJZ-C9QbHEJ1VUYPHAPiSWPdW_C1hJ1LH0py4N5C8x7hLkaCx0w-Alwm4UgCoCXHGGRE8yRW5TnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قائد الجيش الباكستاني عاصم منير ورئيس الوزراء شهباز شريف يصلون إلى سويسرا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79440" target="_blank">📅 09:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/79439" target="_blank">📅 01:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
وزير داخلية إقليم كوردستان العراق:
أربيل وبغداد اتفقتا على توفير ضمانات أمنية لحقول النفط بهدف استئناف الإنتاج والتصدير، استجابةً لمطالب الشركات بعد الهجمات التي استهدفت الحقول مؤخراً.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79438" target="_blank">📅 00:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLQbIjj57M9NuRCoPUcOk7RnT2ZGH3ZUI9uw6y5UdQX1f4J4iaCsPyEMCzLnmiUL2Bf4k_DSYcvlu9LotIqrEDwqpddgCcGQj98QNFcrk6925odLMCgeNeFhR9GYn5veFvBjsig5IjzSBD7aaUmOr_lp0xkI1Xwkqu_wa3m4FOi2cizFLugtItD-3o3iLXP27aeR6fM6k8413Vrb060DtiBRKQO_nNfG6_lrd3NacCZK-brCHMjnjMu7AoPWJcsqsIRLTh68rDUwgtCObj25QElbX02Qd7kmx6--huDHc1xSlIfRT0Kxjl-vrLJpzpg9IzmJE9z59IUNWnY1QMvptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/79437" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79436">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9HrE8eGACe_z3mTJAExQWy_n9VfdFvlm-39G7YS3QT0aSzoS3A-zLmLw_2Irkx8Y7hp5XDRQLUcRElzSWtU7W7Kbq5275rNmOnpKgp3JLA1ijFNw6OQXd9_maAyc5Q9XeLlJCvztQwgHhHZpmv1Vy-_Pe8ROA5u9tU3cDk5PEINTrDweHXIzyE8IhbQJj3ENturgPQxCak9yHgj7IkFtA1xd2FX1eQ-seNeF3f48N-657Nzv69J0-3D8S4BDaKXhkItm8XaYz06ZmRU86oG0NW4iSNyQO3yo6KYX7qGTe4yZnVfIMiSicmh671qt_tHpMXguNgmCSJQUiIm9UqkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/79436" target="_blank">📅 00:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=lVH8qaKwn9Qy4MWVDGNPq9JtZLLrcUowwasrOw2F_w2O995cbsRrPsn-cQAROPH8uxphA2U2aRyCcXqLMCLHXJ69XUhH5_MwendWZfSgxoelBn8cpK63hkmoWlTPlyU2Or2B-XLgaJwrKfKEE4LWTpI8Q0wpi3N04aHMaFhJnrfb0B8GV2MHKzcBI46PAMxC7_5zsD-ChgAiq78bDAMc09Nm1mMTSC7DlOFHeyVeRtmiKvI6YLQlsPyO9mUo5Uio5lp7IvJeeDqX6ymRzJteVH8kW43QVlCi2LB3Tr4Ep1wc6fzK0ifZtHM2TxxSZNO-5us7GxplPxa-aXE9JPortw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b774e6bfe5.mp4?token=lVH8qaKwn9Qy4MWVDGNPq9JtZLLrcUowwasrOw2F_w2O995cbsRrPsn-cQAROPH8uxphA2U2aRyCcXqLMCLHXJ69XUhH5_MwendWZfSgxoelBn8cpK63hkmoWlTPlyU2Or2B-XLgaJwrKfKEE4LWTpI8Q0wpi3N04aHMaFhJnrfb0B8GV2MHKzcBI46PAMxC7_5zsD-ChgAiq78bDAMc09Nm1mMTSC7DlOFHeyVeRtmiKvI6YLQlsPyO9mUo5Uio5lp7IvJeeDqX6ymRzJteVH8kW43QVlCi2LB3Tr4Ep1wc6fzK0ifZtHM2TxxSZNO-5us7GxplPxa-aXE9JPortw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول الوفد الايراني المسمى ميناب الى سويسرا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79435" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=teElIwkIAK3b-GtRyjscthYBif18m6-k8Ew4ZyCORy6lKkIUHkeTYqJNRRyX95iVUNncjEE5hGqjZ-jQkqpNfDBueOT00wjhkKvF06DRvPAYYWPIbwPtNng8UjFWsrC2-82nA-xk6NLO0NRFLLsxvSIIHZ8-F9hhQzCK4SW-qsMfDKTP61HN361R4_FC7m9PkSKTS-t8BXvOUWAK8PRVrmSkojz25ecLTge2ZXNwhbCqf8yTRhoA61R0CHeDvMcaBX063f-c8JSo6IyemfIYD4AiUMi8XDrYYSFHmqGRbMJWEvYhXpVpjFR0eBGDIqWzNI74MM2z2r0FM-3l0xw9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d0f703ef.mp4?token=teElIwkIAK3b-GtRyjscthYBif18m6-k8Ew4ZyCORy6lKkIUHkeTYqJNRRyX95iVUNncjEE5hGqjZ-jQkqpNfDBueOT00wjhkKvF06DRvPAYYWPIbwPtNng8UjFWsrC2-82nA-xk6NLO0NRFLLsxvSIIHZ8-F9hhQzCK4SW-qsMfDKTP61HN361R4_FC7m9PkSKTS-t8BXvOUWAK8PRVrmSkojz25ecLTge2ZXNwhbCqf8yTRhoA61R0CHeDvMcaBX063f-c8JSo6IyemfIYD4AiUMi8XDrYYSFHmqGRbMJWEvYhXpVpjFR0eBGDIqWzNI74MM2z2r0FM-3l0xw9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
فانس يغادر واشنطن متوجهاً إلى سويسرا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79434" target="_blank">📅 00:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
مجلس الوزراء يقرر تعطيل الدوام الرسمي في  الوزارات والمؤسسات الحكومية كافة، يوم الخميس الموافق 25 حزيران الجاري، تزامنًا مع إحياء العاشر من محرم الحرام، ذكرى استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79433" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
تعطيل دوام الرسمي ليومي الاربعاء والخميس في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79432" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تحليل نايا...تلة علي الطاهر.. لماذا تسعى إسرائيل للسيطرة عليها رغم الخسائر؟  تُعد تلة علي الطاهر من أبرز المرتفعات الاستراتيجية في قضاء النبطية جنوبي لبنان إذ يبلغ ارتفاعها نحو 700 متر فوق سطح البحر ما يمنحها إشرافًا واسعًا على عدد من البلدات أبرزها مدينة…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79431" target="_blank">📅 23:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCpjeBNprNLxYlmI3jM6NQ2eFpw5aKIvB9o1YxheG869kuWIZEwhI911RIxjQZD_-vK3SXftR0wuJXpgCqkGAs1xi3_MaHRVYDxgSwEEfpaQdtMEALDruUsrYuKiNWAaTPhqQwoIYfTfJeHO3b_cAUUPO-TfumfW_5h1DWXIUIDqY-EhfbGC1jC5fUqpSdcU9lzpSw9Ov5oPFlUSqwUVON5B7UXA6hTliSDwGmjOeSCsIHxhKTZyy7Jbyrq6HDNP61CLuYBle5f1FOasJJdq_NRDtvBMPSzx_8lAAwPw2MWzu4ay5s3UpZAryWKVxXOEQFpxzdaIVu662E-QMEeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الصحافة الإيرانية من اجل لبنان اغلقنا هرمز .</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79430" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIXampKgeatHH4_HPlRxDbrK7qepOwpde8ir4_xABlPGkAOPjoRdrSBjk-HR-IvSU1ge24ZsFGrLgDmlgYfJXz4X7_JZo_QRvhW5DFCsZSuiHZk0Kx74tpqdMWE6NPeFW-XsRlWiCqNY4pMA6UAuXValenyeMvitR9zovtbQ1WikXI0yaprpogNxKMwmCgFIXqUB7T3erx67fvzJNqTh6V6xP5SVSaZ5ferj661C9GP8Lks-5wRV2QSL6y5qKS58EFMknOcKyf0DclONXwOz4tvQzM1ZOhFFL5rkIr0K1dftc4tG3ntrS6pWAf0zWVo6bbhV3fvcC6tAKK1go9lnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
: يجب أن تفرض الولايات المتحدة رسوم المرور على مضيق هرمز ولصالحها.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79429" target="_blank">📅 22:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_syNEPDH2y7Ka5zIeJh9wfC4M998ZqmfeF04NUNl8KyS3vCP4cVT-6xpCrd6Kj6YR9bHAC4Tswatz1hzWy53CHYWuofxajdepUfRRb6svTtLtK10wBfqSzK6LT13SabFhPMPFuvRz6P3efOvRBhDWhpRPHxeoP7SNA8kcl8Eobc2pb4X-pF9vRdWWBommwHL4W94PyLmDjL9rTzgKqXuMm5SBPFW2WgWQ1on586wiMdqeDrIKlPX7I3g3wt-v-oUSDtRFxFL98Z1_Zp5v3lQHqTA0efkbkA7Gb3V6K7TzzLXqb6-9bvTTadsAepyqDFrVvWvFW__YLmisJtgftErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajztNUnKcpqeElPw6_ttgy51RUjZgo9fzF1dZsTjQltlqBkixcSrxPJAJAnjeZjIh5jmBCuB1kWk9YEDErf8izPtFJb0J2-8GSLVd2ff6EaN9O9XNvThvmUGI2onqNx8KbuiO4nRmMCP-TachBQzcqJJqH7VluKUcywadZt5K6V2Tljp2JjIq9Yih4bJgxpDx4BRD7oZIsm1XZ-TwFjbV5yNJXdo0ZCiW7T_V_6iBxDTLCEUC5shh9BIY1O5OmG6SVuPr1ogUARkrroLrXS8eTDm0H_RDulZg_d25h3wWDGpe5dhbPmXtZWhb1GuZrmw_ftuNYl4RIyzfAbG6GKuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBdL5mhG7StfICFWE7DsmCmXdYWdaje6c3LCkw9IL0VNC4V185rc6dy985OEZZX6urBvBMlCwUeoMumny847AyuruIo5gBcvsrI6-ooXMSQQdkpWx4H-eXhzddmCk06z_4nyZ704piHoaeokeiQtDC3VOmAHTb2-6TUl1rSnm9qt4IqOv-STEFQ4HZeWGy0jkKw_QLydzTSIT9WlRczwKvjHidKs-L2pwbaV6CTSS14-Ijb4Omin57y0jmDq75T2c7FywHYL6FPzAsL5zOusI7swqQ6SDl6Kue9FzRE9cs4pqG0Xmxz8EurHRFD3xtan6l08zfLPcQLnTmlntw0eQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79426" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يسمح بنشر إسم أحد الجنود القتلى في جنوب لبنان وهو "دور بن سمحون"قائد كتيبة 52 ونائب قائد الكتيبة ، بينما لم ينشر أسماء الثلاثة الآخرين حتى الآن.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79425" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭐️
إشتعال النيران بالقرب من قصر الحلبوسي في قضاء الكرمة غربي العراق جراء هجوم بطائرة مسيرة مجهولة العائدية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79424" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
حزب الله:
لَن نَخشاكُم ولَن ننكَسِر... قطعًا إنّا غدًا ننتصِر.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/79423" target="_blank">📅 21:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79422" target="_blank">📅 21:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله.. جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79421" target="_blank">📅 21:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQEXLpy9XoynKDncRG4c3qTXIOXUUieUTD22KhqurR5hEg2GqmIZXInJC7LA3y9Knwy_OMMHsilbmKilBl8_tn8RIvzyBkNUFt40ZubSFARbKBDSeKbPbn4CCrwDF-0UIK0ZqrDABaYlUIraZzTzcJ3RGo07vDRMKUL4Lhc3u8EvAwsRwoygh93_Z0AuciVmkMCCeydcKw1nwUpiLIso_gEDMk-3_v3VpvhBsVcIulgSqIrKxwDt5s7IoVtvFti5rU51awJ4L79-RxlijY5G0yVeGnWVHm-7Fx4ZNhMYc9OleBvQ5jWc0M5VH5LTVB5xzc1iPWbjiq1drSaX3av97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
على يد أبناء نصرالله..
جيش الإحتلال الإسرائيلي يعلن رسمياً عن مقتل جنديين وإصابة 3 بحالة خطيرة خلال الإشتباكات في علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79420" target="_blank">📅 21:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة كربلاء المقدسة تعلن تعطيل الدوام الرسمي يوم الخميس المقبل الموافق التاسع من محرم الحرام.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79419" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f02dc4e97.mp4?token=GApenTUyLjPSFjgxTXiUImL_iiTVjeAAGCxMyUxZ-lCawcn9GtpGYgooaOaUaEsWQ2qtmg7GFKJy8c-7A7C4c0VAtVZqcjWCn4hABKQ7LONRFFMAisiRi-M4aXIyGhE5UT6M9ZGq_8zCpV938ROnfYs5rxwXKm2PUssdPsh2r8pgGVDHQ5aK5Bbh8qi4-3ws3xkNHhQ8fYEn6YWT__PaWnPnt0Ie16nOfIXQjk9hAcnAuhsRFIGXP3VhztItkSxu5of48DVMlPczN4eiFPEXft85LEZGnjneX93hcIrXh11Y0IE2clmfFBCIlhIEtbAk-Hjv9n380eWYtLxMxsv9tE2e5WzZraTvLPGTyZ2QmH_CDRp0klHmfOH-3KlGkdVS2ecVe0BcB_5AzVZWALFCCunMzyoe7i2qhqFmTFQxrPok-6Tn5hvONBZ9xOgJgB-dWTkv4d-Hx-pPIvuJ3KlU8SoxFeE7nFMe_mOlftcEY5I__O-CrXtCNgzPoEOl0vXr4JCU-scMYLKDk8oIbFykn0JlyAm9j1EMpjyBMQ6n_1rbfBlcyOLTzmUFhSgfXJ__MRY8zKr5BUmIDpcGkjPRJEPM7-XkWZOLefCKEGbADpU6TeZ-9s0LIqeF5bF5XzowBeI0H8z3Mv9D-XWaf0dqpHezmtuwniEcTl_L6argqII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
جرافة (D9) تابعة لجيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان بمحلّقة
#أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79418" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭐️
بلومبرغ:
‏قال الرئيس دونالد ترامب إن احتمال انهيار الاقتصاد العالمي كان سبباً رئيسياً لتوقيعه اتفاق سلام مؤقت مع إيران. ويكشف هذا الاعتراف عن نقطة ضعف رئيسية للولايات المتحدة قبيل الجولة المقبلة من المحادثات مع طهران.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79417" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e205a6fd.mp4?token=lTEkRngXAjTVIzzOoaDwUmm3f7Y8I61Vamv4--L2T8lk_bq2EdI5oNzZORYI4Za0RZi-VQq1AhaNjYrb3lg22DA0qw6ZEmd7xI2dDeEPesSo_k_1OAN24zG8h_to42k4vcz1tmf9SespPJbeuEkZ-9bsJZncaWMuqIfFO0mcaVNPN263nbL3eTzYUF2AQlQICGv3n348_bTUbe2cM2llnH2-tPsXdgrTIDnjsH7GYa69DKO2KgZ70S5NSqlvV2Ex26u5O--c_zFalJm0FajHqhNZ8VvIS5pecw_1Sc0p2WgGw8E9yAh90AQvKLcd22gJW2wXyBKQlhWfUohO8VHqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هيهات منا الذلة..
أبناء البحرين يخرجون بمسيرات حسينية تحدياً لعصابات آل خليفة المتصهينة ويرفعون فيها الشعارات الكربلائية بذكرى أيام إستشهاد الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79416" target="_blank">📅 20:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emy3mwmPnrNBLSfpWGkr8wrnxb8ut1YUrq_mqjQbadEpSKFfMwOwsHWyE6_uJ9wzJyn2JaJoE21PCk2CLobamqK38tVxQ-qZuDOdH_c02Oc37Rxw_A7CnMmtDeQHM5QKQ2aT6oKZV1f-pDjQo_GEhkHsCfbff3DvxZzA4g1YRa7RvI51UnlrcyXuDiV5zhJEfzLPapFzzAUpjFbunykjP0njBBUhMzMMvgX3hpBj5wsCQqD9KxKdILOZ9gj37i0srG8RH-8tkfptvdU6ftRoBvelgbm-pA__dOCpyS_Yle2GAh0CgQ38XayYRMAKPE9QnSiMGOqTZTSjjRICAq4W9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الجيش الأمريكي: تبقى القوات الأمريكية حاضرة ويقظة لضمان الالتزام التام بجميع بنود الاتفاق مع إيران، وتطبيقها بكامل قوتها ونفاذها.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79414" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcO94VNWx1-rMXOBxMwCuhSnrHBZZXOUmaJoVU8hKo9XFh0qop2OwNXgL0u_RFpAybq69krGhpa83iVqg_wZnvv5Q6TPtANFn3ixayjqk1Xt2iuDy6iM8BOqSzDresWats-Bo38Y0uUc6koltPMdMRZ2JuhnuBgHL3nSUxFIIepp5-eS0PuxO9rTu0e1sCl_1ft3p43vU1VgluNUAYnVb7RA1V1ZccQqyDbegcHbA48HSQ2sxgvd-NMSXluC0J9XjhhRPMkeWsQDA_ktDHGtPd2AjC8eqfjj0OiNzcOsSr3cKKALKP8FhipdZQDRyYwu676QW303Z-zajzuwQrS7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79413" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTtwEUvPEeVSqANcVcbR2XAIwIzENn8dvkDcac9qx-cnKWRnwAEtas9TmsaEzRhekhgSsBLFjYXaYCJHTFuNUnJQiVUgN2QUNpe8dZPIVomlQvDP8we07TPH2H9uK4QgT25ixu26cus_8JBcsHVJPpygHFlyEpny-tz4dPlukXRyMcYE9aoP-VC_XE4R71uL4TtRIbTreI7i1QKdavq8uLrAzCUFRlmwqRR8aFDUJ8LnramMOAY91VLAvdz_Jl4kXocf4jI7_dktdXSD5RVxW7YXGOoYbT3qN--M4VzHBRu8AYxdmmjKhbn4rxyFgKgxcYz8jU-jNW2otiWVrZ_PsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:  مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!  ‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79412" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هزة ارضية في مصر بقوة ٥.١ على مقياس ريختر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79411" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf9pBzmCu8aUmJPr-oY44BEZ1o77RRp16Q1FC1v0GmFyOWTa4NO2E4zkwEiilmVgSCUxiIxpAMzVvYLMKs4ph7LF5-4LAZLrLaJBznt5tMXi0Gc9s-9wiJuYY91XjoLGuwBCB6Q6dbmIdHE89p02wZzS0o_CPe86QVW0R3ok1AaSUUdZmVoe5h5gsnP3EwX463enTcf0eAELPizgkkiS1ZXbgjK1HjV9r9YJ5tIvTeJJ5dcmcagLeZypET-cL4Hkr4kU73x8BmgL3GpY0u6_kkEiTFpRUagoJnfDu36nXrF09dC8ljce1JRQxzmPBENfwxxJU0_W_a0Ni1QafUGqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
لاول مرة
تنشر منصة كاف التابعة لكتائب حزب الله في العراق صورة تظهر نوع من المسيرات تشبه لحد كبير لمسيرة صماد ٣ اليمنية بجانب العلم العراقي ؛ لم تكشف الكتائب عن طبيعة المسيرة او مواصفاتها التي ظهرت بجانب مقاتل يرتدي ملابس عسكرية تشبه لحد كبير ملابس متطوعي سرايا الدفاع الشعبي التي تعتبر اقدم مجموعة عراقية مسلحة ظهرت إبان مواجهة عصابات داعش في العراق .</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79410" target="_blank">📅 19:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">أنباء اولية عن مهاجمة قصر الحلبوسي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79409" target="_blank">📅 18:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79408" target="_blank">📅 18:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات مجهولة عنيفة تهز الگرمة بمدينة الفلوجة غربي العراق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79407" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuFdUAl-eyWoh8d6wWFLWLQ8tEJhxTjwuPbUU_S4huRiL__G8KKvcK_IwoLLorYFw9LiinPzt8Ms7sxZaD6ZIgbI1mHHYkIn2QSZiS2BNij9RCWCa86JC9PwPj63ob4MsExRVLoT8JFSvHCEuBRrhsOyY6ZmVxZRZG6SrpTS1kvfCSrglXgFuYxtnQpvw7Mfgc2wG_5R2SuI7XZAjHU5c3UePRE7s4S6M0bzSHwgzNFeoD6G0f7uIDKWKIvJrciCb-jkZwaZsaovMWuugDsKpjhc8gVOrEPEZlHx6ISHNmveU9ucy5mReS86gH1CCsAs1pS680nWC30wjZcPOuPQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙃
🇮🇷
فضيحة من العيار الثقيل   زلينسكي الذي لم يحمي سماء كييف ولا خاركيف يريد ان يضحك على بعض دول الخليج التي فشلت منظوماتها الأمريكية بالدفاع عن سمائها في المواجهة الأخيرة مع ايران ؛ من خلال التسويق لمنظومات أوكرانية مستخدما تطبيقات الذكاء الصناعي وفديوهات…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/naya_foriraq/79406" target="_blank">📅 18:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.  يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79405" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز.. إعلام العدو: نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79404" target="_blank">📅 18:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79403">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
بيان صادر عن العلاقات الإعلامية في حزب الله:
في ظلّ الادعاءات والأكاذيب التي يواصل العدو الإسرائيلي ترويجها بشأن مزاعم خرق حزب الله لاتفاق وقف إطلاق النار، في محاولة لتبرير اعتداءاته المتواصلة على لبنان والمجازر التي يرتكبها بحق المدنيين، تؤكد العلاقات الإعلامية في حزب الله أن هذه المزاعم عارية تمامًا عن الصحة، وتندرج في إطار محاولات العدو المستمرة لتضليل الرأي العام، وفي سياق محاولته الواضحة والمفضوحة لتخريب الاتفاق بين الجمهورية الإسلامية الإيرانية والولايات المتحدة الأمريكية.
فقد تجاوزت حصيلة انتهاكات وخروقات العدو الإسرائيلي منذ فجر يوم الجمعة 300 خرقٍ واعتداءٍ موثّقٍ، تنوعت بين  الغارات الجوية من الطائرات الحربية والمسيرات، والقصف المدفعي من مختلف العيارات، وإطلاق القذائف الفوسفورية، على أكثر من 25 بلدة وقرية، من بينها مدينة النبطية، وقد أدت هذه الاعتداءات إلى سقوط أكثر من 111 شهيدًا و176 جريحًا. فيما تشير المعلومات الأولية إلى استخدام العدو للقنابل العنقودية المحرمة دوليًا.
وقد بلغت حصيلة الانتهاكات والاعتداءات منذ صباح هذا اليوم إلى الآن ما لا يقل عن 180 اعتداءً، وأسفرت عن سقوط أكثر من 28 شهيدًا بينهم ثلاثة شهداء من الجيش اللبناني و35 جريحًا.
ومن الثابت أن هذا العدو الكاذب والغادر لم يلتزم يومًا بمندرجات اتفاقات وقف إطلاق النار، لا في 27-11-2024 و 08-04-2026، ولا بعد إعلان التوصل إلى مذكرة التفاهم بين إيران وأميركا بتاريخ 14-06-2026، ولا حتى يوم أمس الجمعة 19-06-2026، بل واصل انتهاكاته وخروقاته للسيادة اللبنانية عبر الاعتداءات الجوية والقصف وتدمير البيوت وترويع المواطنين وقتل المدنيين.
إن هذه الوقائع الجلية أمام العيان تُبيّن بصورة لا لبس فيها الجهة التي تنتهك اتفاق وقف إطلاق النار وتقوّض التفاهمات القائمة، بل إنا ما يرتكبه العدو الإسرائيلي من اعتداءات ومجازر لم يعد مجرّد خرقٍ لاتفاق وقف إطلاق النار، بل يشكّل عدوانًا موصوفًا واستكمالًا للحرب بكل ما للكلمة من معنى. وعليه، فإن المسؤولية الكاملة تقع على عاتق الاحتلال الإسرائيلي الذي يصرّح مسؤولوه علنًا وبصورة متكررة رفضهم للاتفاقات القائمة ورفضهم الانسحاب من الأراضي اللبنانية المحتلة، وعلى جميع الدول والمسؤولين وفي مقدمتهم الولايات المتحدة الأمريكية ممارسة الضغط على الكيان المحتل لإلزامه بتنفيذ الاتفاقات ووقف الإعتداءات، بدل رمي الاتهامات يمينًا وشمالًا.
ويؤكد حزب الله أن من حقّ لبنان وشعبه ومقاومته الدفاع عن أرضهم وسيادتهم في مواجهة الاعتداءات والخروقات الإسرائيلية المستمرة، ولا يحق لأي أحد أن يسلبه هذا الحق الذي تكفله كل الشرائع والقوانين الدولية، وأن ما يسعى العدو لتثبيته من حرية الحركة للاستمرار باعتداءاته أمر مرفوض ولن يمر دون ردّ، وأن طرد الاحتلال من أرضنا هي مسألة وقت.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79403" target="_blank">📅 18:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
بعد ساعة من إغلاق مضيق هرمز..
إعلام العدو:
نتنياهو يوجه الجيش بوقف عمليات لبنان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79402" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
غادر الوفد الإيراني المشارك في مفاوضات "ميناب 168" إلى زيورخ، سويسرا، قبل دقائق.
يتألف الوفد من: الدكتور محمد باقر قاليباف، رئيس مجلس الأمن القومي الأعلى، والسيد عباس عراقجي، وزير الخارجية، وعلي باقري، نائب الأمين العام للشؤون الدولية في أمانة مجلس الأمن القومي الأعلى، وعبد الناصر همتي، محافظ البنك المركزي، وحميد بورده، نائب وزير النفط ورئيس مجلس إدارة شركة النفط الوطنية الإيرانية، وكاظم غريب آبادي وإسماعيل بقائي، نائبي وزير الخارجية، و... أعضاء الوفد الإيراني.
ووفقًا لتصريح بقائي، المتحدث باسم الوفد الإيراني المشارك في مفاوضات "ميناب 168"، فإن هذه الزيارة تهدف إلى متابعة تنفيذ التزامات الطرف الآخر، حيث يتم اختبار كل اتفاق وتفاهم عند حلول وقت تنفيذه.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79401" target="_blank">📅 18:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:   نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79400" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f58ccb.mp4?token=tFh5kSiY3yyT5ja0ckFBjsnPle2iv_4oJwNjPMuP374HBpevYOQgxGtUk2YZ-mgOkEOpw2y7Ahafr6juamY6Nw4EiulO0R9iBGla0fWPeoeE6U9QaXizKbGASf-eWhV66oakRwc5_EfIJaZ4k9dCvY9AXq0p1y7M959d_2_qNiMQ6hj3su5TF6boU6jfJ8zdlYqvjQQcbZsaxwRBl81t_0GO10W_Nw6s_xum566Sn79hdsA5VxnJLcEk-hPOMKKsa1DJeNWXgOrXg8BZn9m32-2al941v2LSXRpUD294i7GEkadZoEy6_UGna24CC3l3RkD0xrMdzpyg-DYZExFkTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79399" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThzGIwb2YbvNX2T70srj126iV5_6AEScONWQAttomx2AIB9kl0GofX3JDPm-6CRPf41Ae8V_-Jx7vT1NLwnPZMKa2r1yzlBRIWg0BBvz3c5FgwJWth9seFWNt_P_66ZS-J2chn3MBjgfpjgSajr_eDVKB8XRVzG8kvgJF3rY40kHhQq0YwzscF9gE-bcwcnplLGHwdtnuTLDxqsXMf_FkKUV5dOmaLG-ws67xnEfyzbDIS2oyxshXxCN9JV7pfIuql4I8VYo5uhyfnyFZZpDNgiuCX3sY7P96KeUdikXf0P_zLdVz-Uqi5vKF0jWcGef_G2kSCStrPhXfZZQCzO4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تناقش الخطط الاستراتيجي لبناء العراق عبر المغنية شذى حسون وأغنيتها الشهيرة للنشيد الوطني  " ناعما منعماً "</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79398" target="_blank">📅 17:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
الخارجية الباكستانية:
محادثات تقنية أمريكية إيرانية ستعقد غدا في بورغنشتوك بسويسرا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79397" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMi8QMQtQGmHlButIEs81xsCjUOGgZPTsXY_S9Gu8V8MluVzMigQUE7l0RcQ6mgk7LGeTywzkvkaE7OXCz-C-VOeYat6vN8xJHZ228Z41pZnhpd-tRne5O30UCFeAhdUl1JvMaB0rUbT6CQ_kklYgF17x1mqwP3571ptk79cQCCCBDn8lU7Fzdprc6sTp60qodLgrCDV1vhIjpWhL7zh-CJBuEzC7iquO60utPynZD-5uPgKv-37WW3qXKm7AHj3rLLTqv-bpE1clta3Xdmthh05BNA-OrrA6Y9XtnwRij_y3vcM2J5mr_-LW04Jir4R2NP4-A9T4U-uP-FTaHxitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب يصعد تجاه ايطاليا:  طلبت رئيسة الوزراء الإيطالية، جيجيوريا ميلوني، مرارًا وتكرارًا، التقاط صورة معي خلال اجتماع مجموعة السبع في فرنسا. إنها لا تحظى بشعبية كبيرة في إيطاليا، ربما لأنها رفضت الولايات المتحدة الأمريكية، وهي دولة تحب إيطاليا وتحميها حقًا،…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79396" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79395" target="_blank">📅 17:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
بيان صادر عن بحرية حرس الثورة الإسلامية:
نظرًا لجرائم النظام الصهيوني في لبنان، وانتهاك التزامات الولايات المتحدة في تنفيذ وقف إطلاق النار، فإن مضيق هرمز مغلق أمام جميع السفن. نؤكد أنه تم إغلاق مضيق هرمز، ويجب على السفن عدم الاقتراب منه؛ وإن فإن أمنها سيكون مهددًا بالخطر.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79394" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFxuCjdULc5-_Iow9FkdP8hJ9Z7YhZD7pC8CmDQNoBU_8g47cniVVjSxmOZJVcPun9EggCvOCzkStsnicuDw3k1LiUZSErAg0uQ_2f5bhxKaf6HFKteQmqyEU_ZiKrzDgW_2buu-CJP7WvX1y0B5pE8UlURtXLsKk1TZjJdKil-AgollMxmiKJz4or-cWUUrH_xwo7pvM98eni0Xj3y9euS-VpQOGFrr76eHNqfklD47ssFJIHcd8zkvb_F9vBBe9iOr1Djc7Cz5jTJHlNNAKsQcK-d2Dj75JWeEd_ZzgEgkn30Cd0UvPnBaOJuoN0jnALJBaBMcoX5TYCQrezcUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
ترامب يشارك تقرير يهدد فيه نتنياهو بعنوان "ترامب يملك أوراق اللعب في فرص نتنياهو الهشة لإعادة انتخابه".</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79393" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرار الخارجية والتصريحات جاءات قبل بيان الحرس الثوري مما يعني عودة عراقجي في الساعات القادمة إلى ايران بناءا على التطورات في لبنان   ايران من اجل تلة يقاتل بها حليف تنسحب امام مفاوضات دولة كبرى  يخشها بعض سياسي العراق بسبب تغريدة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79392" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فانس: الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79391" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فانس:
الرئيس ترامب قرر منح المفاوضات فرصة وذلك خلافا لمواقف بعض الأطراف داخل الحكومة الإسرائيلية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79390" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اعلام العدو:
ما تحاول القيام به إيران هو رفض أنصاف الحلول والأمر الواقع في لبنان وفرض حل جذري لمسألة التواجد الإسرائيلي في الجنوب. قد تكون هذه مغامرة ولكنها قد تكون ناجحة أيضا بالنظر إلى رغبة الإدارة الأمريكية بإتمام الاتفاق، وفي ظل توتر العلاقات بين ترامب ونتنياهو.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79389" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79388" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وسائل اعلام تزعم: عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79387" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وسائل اعلام تزعم:
عراقجي يتوجه إلى سويسرا الليلة برفقة وزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79386" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">في محاولة لمطأنة الاسواق العالمية..
فانس: لا يوجد دليل على أن إيران تغلق مضيق هرمز.
جرب وادخل
😄</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79385" target="_blank">📅 16:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:  ﴿وَإِن نَّكَثُوا أَيْمَانَهُم مِّن بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِي دِينِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَيْمَانَ لَهُمْ لَعَلَّهُمْ يَنْتَهُونَ﴾ (سورة التوبة، الآية 12)  نظرًا لنكث الولايات المتحدة العهود…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79384" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxoDGbLNOQTde8n7KsYQadYn5eRE71purQ0dL-9UJHoPXo_Tkl2-6-GsQkhbk5R5hAYkf1qyZ8R8OGNQGpqih033P_TLUAA6GT_yYH1-jRApeaXcykCsS_aRTkjSgV3No5vnZjb8Hi66OwdFlxsJ16SS8IRVjB-a2VWpNqGP_Em3tOcg3o5vFEGr3fRP_Xpf9wsEWZKXzNlD4stoGlO28ZzTs1IxRwdlePXSxqPqD3lvC0P8ovuNK0PSZigA8fChvLK6jwX3h6LCpKs-NKDr3nQp3-7drj8IOXADISj8viWq88UfYdbqxhofy_c1_43Xk2AQrrQA3AcG5YItciVyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الرغم من الإغلاق
ارتفاع اسعار النفط بالسوق المجازي الى اكثر من 80 دولار بعد اعلان ايران اغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79383" target="_blank">📅 16:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79382" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مجددا.. النائب عن حزب تقدم (مهيمن الحمداني) يطلق النار على عمال بناء كانوا يقومون بترميم جامع الخنساء في الحارثية ضمن العاصمة بغداد مما ادى الى اصابة عدد منهم بجروح خطيرة  متى يتم حصر مهيمن الحمداني بيد الدولة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79381" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقر خاتم الأنبياء يعلن إغلاق مضيق هرمز</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79380" target="_blank">📅 16:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مصدر امني لنايا : اصابة المواطنة (سناء محمود خلف) والدة زوجة النائب (مهيمن الحمداني) بطلق ناري في منطقة الفخذ ضمن منطقة الحارثية نقلت على اثره الى مستشفى الاميرات الاهلي لتلقي العلاج وبعد التوجه الى المستشفى والبحث والتحري تبين وجود خلاف بين النائب و زوجته…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79379" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
بحرية الحرس الثوري حددت مسارا من جنوب جزيرة لارك لدخول وخروج السفن من مضيق هرمز وإذا لم تلتزم السفن بالمسار البحري جنوب لارك فإن مسؤولية أي حادث تقع عليها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79378" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
فوضى واعتداء داخل محكمة كركوك بين احد المواطنين وعناصر امن.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79377" target="_blank">📅 15:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🫡
وزارة الداخلية العراقية توجه بتشكيل لجنة تحقيقية عليا للتحقيق في حادثة وفاة شخص يحمل الجنسية اللبنانية كان قد أُودع التوقيف في العاصمة بغداد إثر مشاجرة مع أحد أقربائه.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79376" target="_blank">📅 15:52 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
