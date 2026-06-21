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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 02:32:20</div>
<hr>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuBYww0V-LrhIQJHZ0kGAb63GT_Io8E2U1oWHBpYK0_rTkhe3NUh0GmBPEmzSjysQ1NS052YQbedeb0_H2OPFgKw8bhSSE8oAHmtNb641D4FwHuKIErZTkmqKYRM3_7weZZ3ADCizPRthoNoeJIV7PTZqI3azjWFOyC6Gqi2SoIgBzQrnnFro-xDR6s5EHXMKP3LqTrNuq9tTdunJfyWEekYbj3t1sZsEu4K678jf4ygmunhBo2iXC9Q2AssPKRRWO6FAc_ecWtTk5FpIhXYCSsZTInbKr8l9jH69A2Xm66w9Vzy0jabE0Lj7u1MTdHH7ukwxAp5D3HwN-LVB0gWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة خاصة من المنتخب الايراني في غرفة الملابس إلى الإيرانيين وشعوب العالم أجمع
أحيا المنتخب الوطني مجددًا ذكرى شهداء ميناب المظلومين في لوس أنجلوس، وكتب:
من إيران القديمة، التي يعود تاريخها إلى آلاف السنين، إلى إيران المتحضرة اليوم، ظلت روح إيران حية وقوية.
جئنا إلى لوس أنجلوس بشرف، وتنافسنا بروح الفروسية، ونغادر هذه المدينة بكل فخر.
لوس أنجلوس، نشكركم على كرم ضيافتكم.
ونشكر جميع الإيرانيين الذين دافعوا عن إيران بكل قلوبهم وأصواتهم وأرواحهم خلال هذه الدقائق الـ 180.
نتمنى السلام والاحترام والصداقة بين جميع شعوب العالم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/naya_foriraq/79567" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwl5GmUM5xVnOe4FktQNPsf4zk1nZVUWxXkkpw57pM04phsV5BB_CNHd-avF0i2cW92RxOJvWvMHqgQCwOf-8ajm6bxtWbf--TKuijpe9zmmoYbDTOdk-ZjIsWEWJGW_NVUoxN3KrAEfna2MIlDZvfB0rcvMe6jBiLIFtmYLyse5lNUefFWBlsstd-Kdcgnc_Gpk24xDfPI_lZiBK-w29DdmvILPFYDNOzupHThFbXXmLnrUrpTuestORJ3ElDr0_IMGtmKzoq9rCej31dEkS4HjqrOXFHL8mhwCrGldqfkgpnGCS0HOkbcc2ztJXwWmHxG8SmrUp-Wv0epqe8l7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/79566" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
‏مسؤول أميركي: التركيز في سويسرا انصب على آليات لتجنب التصعيد في لبنان.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/79565" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bctBepCL7SgfGS9z5HmlErJCIrfGB77kQqvDjB95FQyOcWtdwhS2h_9q-Ad4hcx6yRXmhs03gpV_hMjKfzKXmlB0VvwWd1XjkPqhpnfjdvRNl7bJaE0rwYpOsGVvUndU9N0vwzkW0R68fvSMhr3r5oyMa5JMBQJRk56KMnM6NioVJ5rmoJ1DbORskVqBcwG2ZzN01NwedMq6WZUvH09B2xtAUkt70bSrxbl1sXtbJhpGOnTPWAmIw8GhKYqmdlCwQ3GDd6Tsop3S5TqkupxcbGKxgQFYUTDu_fmjjKBfejfyA7U1IrbiZXqVGj8ofOTItwWNd3i1w3pQHCOdJ4R3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العراق لاول مرة   مبادرة تدخل حيز التنفيذ الان من وزارة الاتصالات العراقية برفع سرعة النت بمعدل ٢٠ بالمئة على ان تبقى نفسى الأسعار بالقيمة السوقية  …  برأيك هل سيحقق سند الوزير الإنجاز كما حققه كنائب سابق في البرلمان ؟!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79564" target="_blank">📅 01:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79563" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbh6eAcbASOw9D894PTm7Dkmnkg3nqniFMUTP37nDDVMtRAq1tYqiDP5x-a6EPp7Qt9z6h7uh9l2QfHY3hhfE5XuflocatRyUeqPZ0yh88_VM8mlw6nrA2KAIobKkI_Had5lHl0ch7YA1GKPrTRKYaZEXkLFxVemLEUv3BwKlawrj1w4ewAV5bzeMSfxs41DDb4KLJKh_5kjp6vPSbP5RLlj6qOEbxFUgvsL7mWmV_j8oXO9lC-WrYUi8gP1s0h1JYfhXT9mB02zR6zOtTYm_l1CUTfAuCFz3V-Bbv2H5_OVbDK8Bu8mTjPqVDBX_dp5PRUskRqqydSnA39s3fT5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع ميمي مشهور على تطبيق اكس يصف صمود الحارس الإيراني بصمود ايران في مضيق هرمز ومنع بلجيكا من العبور نحو الثلاثة نقاط ..</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79562" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1GHPbTQaODP2duEsodZPrllRjbGr1dsn-mx6WKk_WWqSm8XFsl2_fmTg6R8cyurAOK0gJ58VdqIwSdYZSyo8_6PMTeHrvI-YH6Cf2qE2DprXsm83Xod6lcC6AFkIJJvUJD5YhQn0l26DAugLANPpiNRGb5aLKM-AI5SS0c_XnjmUDQlIOjA1ihkCFduvezqmXZt3MkZihJmFG0etYLSgn0805SDdsnuYcnxhBJmo9djKMUA8Yce7pLxZBx8QK2CrIQKGkYeBaSBcvdiB-DYyVZy_0Hg4_-sFGBbpn2o8XGdSTQ-Oxp_BpOMwpGOKZKRBIRz-3_hXdDfDjusJSExXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
اهدای پرچم گنبد حرم مطهر حسینی برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای
در اقدامی استثنایی و سرشار از نمادها و مفاهیم معنوی، آستان مقدس حسینی پرچم متبرک گنبد حرم مطهر امام حسین(ع) را برای تجلیل و بدرقه پیکر پاک امام خامنه‌ای اهدا کرد.
سید علی بزرگوار، فرزند خراسانِ عظیم؛ ملت عراق تو را نه بر دوش‌ها، بلکه بر دل‌های خود حمل خواهد کرد. چگونه چنین نباشد، در حالی که تو قهرمان تهران هستی و از «دروازه دوم خیبر» سخن گفتی</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79561" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEtmPELCvwP_8WUqZsjpnHLM7EeyR40AUnCpvUD1rWvyzKFVX9jJ0BMoh7VzaKg-0akKraxZWmlppVyyb93bbotN8lbnS19NGoTdL2IIpxfJmHMlL299u2Vi-k7IFKNMsxc0ufwrif3Cw4HoHHXlVECwL5F8qphkfA24bGk8I1SRxxUS9sK-PZki68tUivvqnMjk0OyFXJU2QkIYhw_abGIzgNWS1fzYQW6KxiZNeU05M_6h4EPe7434HU88V0zJ0ZeFCMay_sKe25qXzcAJK-iDoKhrEJaWYtnpEwPc9fJo8OPxjmNDjeaCxcTBLIU6qKoSy1JNaQB7OuslELCZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دفاع مقدس</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79560" target="_blank">📅 00:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79559" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3wLQMU0aIZcnsFd1mKFyraI1OeEH7u9e7A-WFVMiRpy-7TU57tnQaR52DX-T9OmIm63kO6jAycqYA4wU682SmiqlGvGUXF7pzSzvltGgTrj5leQvEjfxg6TazMsA4Se4KzFzXUQHcX7B8Z9Lj2E8J-Myi2bOhc5iBA6uua9Wdzo-WjWUoMIEfisTbfzxDrKMCfCKH4cNu6BlkcjVMw26DYUlb8d_bG4QcTcgpfNtqisio5GPMlB40QMo2wV37NXVKmHOd47MpaSXYhqoF9gQwPxW6oK0b9GgRr00rHKbQFapTr7qaFrYyPRBfq853Xdacm8eO5_3JeMxeEeSM9tbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
العنوان الرئيسي في صحيفة نيويورك تايمز الفاسدة والفاشلة: "ما الذي تغير بعد ما يقرب من 4 أشهر من الحرب؟ المحللون لا يقولون الكثير." حقا؟ انتهى جيشهم، وذهبت قواتهم البحرية، وذهبت قواتهم الجوية، ومنصات الإطلاق والصواريخ والطائرات بدون طيار وتصنيعها، قد اختفت تقريبا، وذهبت المجموعتين الأولين من القادة، وتضخمهم بنسبة 250٪، واقتصادهم مكسور، ولا يتم دفع رواتب جنودهم، ومضيق هرمز مفتوح، والنفط يتدفق، والولايات المتحدة. سوق الأسهم والوظائف في مستويات قياسية. هذا ما تغير، أيها الجبناء الفاسدون وغير الأخلاقيين، وأكثر من ذلك!!!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79558" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">طرد لاعب بلجيكي بالبطاقة الحمراء بعد تدخّل عنيف على أحد لاعبي إيران.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79557" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الغاء الهدف الايراني بداعي التسلل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79556" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
استمرار اشتعال النيران داخل محطة الغاز بقطر مع عجز تام للدفاع المدني لاطفائه.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79555" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
دبلوماسي أمريكي: المحادثات مستمرة في سويسرا حتى الساعة ونقاش جدي بشأن مختلف جوانب الاتفاق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79554" target="_blank">📅 23:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F21TlbLXSLdX0uLsPZYkXjvQ7vR53WGd6619Q_am7sLnjHKpdGjYq278_QJq2sZe40wk3CfrUM4ZbhgM0aaL6P-Tdp7cxndY8rjPSq2LjoWjGjtPt24T6RYaDU8IJfOfdSZ5qoXcziMpMOJTc3w_YqjltoLa6aOg-zGB8SYP4eQ-RJioCfQS86h8c14m5Yw07BLptv9GYpB16mjeQnfrp2zr117tVyLlHARdk2y4xckQOB6ILel5eKMv-0CLJgSgmgCuOWxYhk_aIOccyLNB1ZKizAWOWZkfehneR3DGtY4gNeTl0elxRiG3FVH0wkYv3ooCGfQx5K__I8agFK3FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79553" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🌟
دبلوماسي أمريكي:
المحادثات مستمرة في سويسرا حتى الساعة ونقاش جدي بشأن مختلف جوانب الاتفاق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79552" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ac74e6ac.mp4?token=otyV9EVsD6pUQ637ZMw7mX_NMU5ZEdBqjetbpBAgXrwjMYNo6DhdVp-_t9mETspyRYT8zejU6ta3A9g30PiOMnT8hppDdve22YoElY7d8RD5N1uSgENZSMbRAlJfbfAHEBu8iflTVMS5NLxOm5Dvag2PwZlcEZ5L_dCpVkVqB64QGi0Ay7E6zERv-Bdls0p9ge0qjzt55oWkdfzUXgUkx0x2AW5woMi2SIBodGvIfyKB6si8DgLZzBtmAzKkYZB7DVvV99yBGgj0stM-Eu9VzUMu4Zkw3m-V09EhoOCq2LrHFHGixw4lyawRWnrHz1pMRt-6qxwwi8_CgkP5uASJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ac74e6ac.mp4?token=otyV9EVsD6pUQ637ZMw7mX_NMU5ZEdBqjetbpBAgXrwjMYNo6DhdVp-_t9mETspyRYT8zejU6ta3A9g30PiOMnT8hppDdve22YoElY7d8RD5N1uSgENZSMbRAlJfbfAHEBu8iflTVMS5NLxOm5Dvag2PwZlcEZ5L_dCpVkVqB64QGi0Ay7E6zERv-Bdls0p9ge0qjzt55oWkdfzUXgUkx0x2AW5woMi2SIBodGvIfyKB6si8DgLZzBtmAzKkYZB7DVvV99yBGgj0stM-Eu9VzUMu4Zkw3m-V09EhoOCq2LrHFHGixw4lyawRWnrHz1pMRt-6qxwwi8_CgkP5uASJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اللحظات الاولى للانفجار الحاصل في محطة الغاز بالدوحة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79551" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4w8ZuN_nusafeULEDjUeJD1AEyQz5kfuByqfY69dkKP61CkyRLLVq3taYwstiiu0skPhh7vW_uHUIK6z8ARhyyTuspMVdK3WQ4kvJvrLyLjLNekSbPI8Sd6xCfyZRJZeftpGrDxi0lM3ziW8M0lHo6psAJRpXkBcwd8fLy2rjM2OVlxG2_0i5EnGmSnpBAFIB_Wt7a4uyDmJRiSJmfkddqY75o9OODQbBqc4PK0IaKHHeMn_x1TEHAJdnWTQcghzP1MRR2NubFPrnVoryCfe53lf7c8TT2oyru_g2QsqpU6JKKO0wKxg0i9xmUIt3wPugKokWV9PQsDfmRq1u7rrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاني:
أيها الجنود الصهاينة المعتدون والإرهابيون، لقد تكبّدتم خلال أقل من أربعة أيام 100 قتيل وخسارة بشرية! إذا لم تنسحبوا من جنوب لبنان بإرادتكم، فإن ملحمة عام 2000 ستتكرر مرة أخرى؛ ذلك العام الذي فررتم فيه من هذه الأرض بذلٍّ وهوان.
واليوم أيضًا، إذا أصررتم على العدوان والاحتلال، فستُطردون منها بالذل والهزيمة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79550" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6731b513eb.mp4?token=KQ0e4A0-CBiur_0CDra7RIpBZeT69tCpXv15d5TOxRd8lnehq3MHN8vwqaRf3UlwGKhrvmulbv43OpAi6m4yvRTKI7MCRJXaSFi_bg7j5YWYIXujrws82K5RhZOXt0uGxdlT6p9ZhBmXmcqrReP7ryrJb0DYutoY7xidVcjLC0dTxFKFJg5v5aYpYOTPTxdZnZvt9WAUGBOgCkpY5qCoXe9K7kTmc4wRfI40Lw8sV4zoH0EN1jnGobVdDu7mO4m3g2YHpKjSm2Qr6ITbToFtGDs39R4qkBdcmZr9sDusGp_woM8veND6fv3NJCshZnZ1BWJ9hInRl8x_O0wDsayR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6731b513eb.mp4?token=KQ0e4A0-CBiur_0CDra7RIpBZeT69tCpXv15d5TOxRd8lnehq3MHN8vwqaRf3UlwGKhrvmulbv43OpAi6m4yvRTKI7MCRJXaSFi_bg7j5YWYIXujrws82K5RhZOXt0uGxdlT6p9ZhBmXmcqrReP7ryrJb0DYutoY7xidVcjLC0dTxFKFJg5v5aYpYOTPTxdZnZvt9WAUGBOgCkpY5qCoXe9K7kTmc4wRfI40Lw8sV4zoH0EN1jnGobVdDu7mO4m3g2YHpKjSm2Qr6ITbToFtGDs39R4qkBdcmZr9sDusGp_woM8veND6fv3NJCshZnZ1BWJ9hInRl8x_O0wDsayR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اللحظات الاولى للانفجار الحاصل في محطة الغاز بالدوحة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79549" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLitAVyuMuVOYdLDVQy8_vl0BKttkZ8uYy7b7441KLIvmWANqa37-YUAmouDZ9eZ23PvyhG9Ak2w9x8OlCKzpxTv_cSr84JB6GWQa4vkRooTtw4oI1Ql_5g9lDYiZ0bIYWCevGoHXRAEh8Vi-ZQb7vCrxRGPbzYZ5IYmDDJCjqkm_N_ifZlxkdtuiWnxFn61PqDbLxgxgOo0y6EkaQhDncl4YcmYvTy3v7QbUMmnz-66Xykt_XOsDlHrVbT6zAnKGuIcelRWHxUhsr6-aDOMuGFlt6oTtE8mdbm9fMVemll5oAkyARO_aDsOy_-mX_U-PXLpajZci0JEZAZ2rGGXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBdyRskH7EZu20eXsuPtMwOzfKwEsQW0daK82KWKVt_mqiUazL1FKZrCHTEVIdlwQuNU3MhuGoyZa2jfrjCZNe2yyPuS1XeN6dbIJtYpHLzmvOUkTyVYFvOJtiz_1j9L70qpXXtAHlRjPBEBwtfsR8BEX2iIukcKkDAwCJcrFaNH9jcelJ89MAuDPJP8R9odqdHcyaK0Fffa1lNVKDEJIJs3jPu6GaUKEINwdsFqtgAn6A5EuHAz43GMD_fQMhE0cKYBY558S-hkMETmk-jxqkNpV72pCCE3oToaxFVZ8R-H3oK-Md2NZD6Vh4FODhOruTIKiMsCiZL7P9FA_vWrZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
انفجار قوي مجهول في احد المصانع بمنطقة رأس لفان الصناعية بالدوحة القطرية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79547" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79546" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBuJAzd1_7VxVVde5kowfJwNKzWFfgptTSjZBVKq__bFmQ5E1CcirwkUkSseE1aFeXb2DpzHFkllpivuK4CfY8iWR8WmXc8piFS_3xq9WAPYzOa6nMDbu6laMbQh0-CCNFFi2SMhnuCjIU_Y6PBt77k_AKvRlUFf65eK8igue8KidCqLqvmdizJDI3vqN4Tqcerzekawsi1SNwZb_PUHrYF9s4xYgXo17pWNmVBWZ72sPbcJtOVn_qnEDPhPbGBdNvoSYpnZ8-sysbHir5w03Qc1khsStluwFqJKGThLelkHUAO3-peW-40rNiRbYH_CDSHNjlF5wxtY2PXImdcYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79545" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
انفجار مدوي في العاصمة القطرية الدوحة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79544" target="_blank">📅 23:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuHVCQZ3tRt4YtYDBOpkVdnC8-QhxynlDVWAnzMETrHF7g2CspD39ZIA3KxQEabSiKVlEsXuCVFhnMbrzcy9eb80lpx4KulRkkz-Gd2CZHaB6qco5bph2hrfnSbSgMWoIv-v_bk2VHaypc8Hc-QoM-ikYnzb9mcJdzNoeBcbhF0kkHIAk7PZ5yleY1LCluTs0NRTCkpep2XeS-FzNeOQAoB9EsWTkpRfBOTE0Kd6ef4w-0k2DH2_vH1YARPEeZsjtReBBAEoWgCaV2T3rAQ3CVbVSSlQhwBm8lWDAxZW4qrVMwuW4s_hBF6bjl2MgbtlF-9Q9VG3iV79EqiU3LHo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:
بعد إنفاق تريليونات الدولارات على حلف شمال الأطلسي، لن تفكر إيطاليا ورئيس وزرائها حتى في المشاركة في جمهورية إيران الإسلامية وتهديدها النووي الخطير للغاية.
على مدى عقود، ندافع عنهم، ولكن عندما يتم اختبارهم، فإنهم ليسوا هناك للدفاع عنا، وبقية العالم. ليس جيدا!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79543" target="_blank">📅 23:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466ae28e94.mp4?token=lTd_n94f-X_O99V9T9-Y8S1L07MlVFKvAx7n9lFT4RNdWmB5zOWIqbAhigaz2tuk5JnwT_emqW5XPEgHjMCZCMBXNTiFPgyujzAxE6Dm9NJY7LvOcVCWbSAhU8P93AdSq016_rFEu21RBvnJISPSzScQMaPBLZmgNTa9OZm3cdbi6x4jdKeLOuPSUMcaFLbUN6w9_pP8rsmh-lBYqW9RFuyTSyKNj-2-s1o66zaJFIgqb4fd-p3WQ0Ko0QRK39fSVSWWKlKVhDJzXfsW1w0yiJTI-rUSHvbewpxvEpl69qINLjxZBbjo4_hVvOhk4WAfdSy-eiwDl2RpYLwMDOB0XUGmdMy9Rl64xp7OLtbQG6ssQhbVVMWiJMbk0hEgMu6WVjXCU4fq227brNspOB24-p5gBHorg1-nkOVeOUTQcUFI-n2a1zyiBvTS9hTTmEPbRA2XDoBUWEZuuz-ugjrvNq789RsYkBNqR0EofkNgyrud3pSO59XC0jL98cRgPkSsu0jJvaQFo1tM1TYZ804Rkg0cNuf57t5NuR-UXswXmeBaiM0YSVBtAvjhXCrIwlzlp5Nqjcf9ipowP4oIJZN1TQ5NyLUGgDibyhWcerJWtWey83JyQzZb80DAMbEHLqQn_P6af8ILV-p4pc11jnkc9S9LuPegyDExyz6kXnY1c48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466ae28e94.mp4?token=lTd_n94f-X_O99V9T9-Y8S1L07MlVFKvAx7n9lFT4RNdWmB5zOWIqbAhigaz2tuk5JnwT_emqW5XPEgHjMCZCMBXNTiFPgyujzAxE6Dm9NJY7LvOcVCWbSAhU8P93AdSq016_rFEu21RBvnJISPSzScQMaPBLZmgNTa9OZm3cdbi6x4jdKeLOuPSUMcaFLbUN6w9_pP8rsmh-lBYqW9RFuyTSyKNj-2-s1o66zaJFIgqb4fd-p3WQ0Ko0QRK39fSVSWWKlKVhDJzXfsW1w0yiJTI-rUSHvbewpxvEpl69qINLjxZBbjo4_hVvOhk4WAfdSy-eiwDl2RpYLwMDOB0XUGmdMy9Rl64xp7OLtbQG6ssQhbVVMWiJMbk0hEgMu6WVjXCU4fq227brNspOB24-p5gBHorg1-nkOVeOUTQcUFI-n2a1zyiBvTS9hTTmEPbRA2XDoBUWEZuuz-ugjrvNq789RsYkBNqR0EofkNgyrud3pSO59XC0jL98cRgPkSsu0jJvaQFo1tM1TYZ804Rkg0cNuf57t5NuR-UXswXmeBaiM0YSVBtAvjhXCrIwlzlp5Nqjcf9ipowP4oIJZN1TQ5NyLUGgDibyhWcerJWtWey83JyQzZb80DAMbEHLqQn_P6af8ILV-p4pc11jnkc9S9LuPegyDExyz6kXnY1c48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏وزير الأمن القومي الإسرائيلي بن غفير
:
إذا طلب ترامب من نتنياهو مغادرة لبنان، فيجب أن يكون الجواب: "سيدي الرئيس، لا".
‏وليس فقط رفض مغادرة لبنان، بل أيضاً رفض عبارات مثل "لا تضربوا هذا المكان" أو "لا تضربوا ذاك المكان".</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79542" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79541" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79540" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79539" target="_blank">📅 22:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0d08c52c.mp4?token=cA0pHdX0Uzc2bGGwaTLUzMPzcm8eYUr95hpxAoLQ4vX5izy5Ljm871cqz-DmNcluuEYHrYuVyebb8WKjehsD9RbdjyNgk8jBlsiyKklE5qH3xPWAJVQ0j8HTBIePEs9ADT7KwJ3VRgKmSa32DXw46nHJmY7PNnEXHm_Z29HAx4MM92Dnsfjlt4glMrC2MbH1U1des-T_-DObIJuUk3V9gCd6eCjn7FibGXV2Tav6cfnW6zG0tncFqUAM16mnDJMD0mqgoq9ZX5euO3ff3y3BonxFUAFv1A_BOcdAuCkZ6NiCHFubM9GES_PJWGUvD4z8giCUpMPbnvpI6r82lX5RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0d08c52c.mp4?token=cA0pHdX0Uzc2bGGwaTLUzMPzcm8eYUr95hpxAoLQ4vX5izy5Ljm871cqz-DmNcluuEYHrYuVyebb8WKjehsD9RbdjyNgk8jBlsiyKklE5qH3xPWAJVQ0j8HTBIePEs9ADT7KwJ3VRgKmSa32DXw46nHJmY7PNnEXHm_Z29HAx4MM92Dnsfjlt4glMrC2MbH1U1des-T_-DObIJuUk3V9gCd6eCjn7FibGXV2Tav6cfnW6zG0tncFqUAM16mnDJMD0mqgoq9ZX5euO3ff3y3BonxFUAFv1A_BOcdAuCkZ6NiCHFubM9GES_PJWGUvD4z8giCUpMPbnvpI6r82lX5RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من أرض الولايات المتحدة، خيبر شكن يهز شباك بلجيكا معلناً الهدف الأول لإيران</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79538" target="_blank">📅 22:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fe95c6bf.mp4?token=UfnUVNl_kOXOkfa1s-jZdLogbWXtk21yhKWdxFM3fOwcrtOlyutSH0D7bB6N282qdNqRUK-GtrmGj8rcohOSEw8DmOkY4LHyV81iG5_O3YLjNG0LdnxWmuvn66oR1kWf8Tk_B5ExWoNYokpvR0t4i1ri6_Pmkvs-1G4VpeetqPKnKpTt7QCItRhDODq0-r2JQWvg9Z3J9N85UObtzfnfr5jdgjRaf2-HQZfhWOeIICduBK1_tA-Adhi5wY7bReJVaUpyVgWjkOdNGf9C8DjoT363Hjxbl2joEZtLEE4qoBH8DT7RzDwNeOvAmgJJLm9AT4lsWZjRjgecNWYXVL2a4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fe95c6bf.mp4?token=UfnUVNl_kOXOkfa1s-jZdLogbWXtk21yhKWdxFM3fOwcrtOlyutSH0D7bB6N282qdNqRUK-GtrmGj8rcohOSEw8DmOkY4LHyV81iG5_O3YLjNG0LdnxWmuvn66oR1kWf8Tk_B5ExWoNYokpvR0t4i1ri6_Pmkvs-1G4VpeetqPKnKpTt7QCItRhDODq0-r2JQWvg9Z3J9N85UObtzfnfr5jdgjRaf2-HQZfhWOeIICduBK1_tA-Adhi5wY7bReJVaUpyVgWjkOdNGf9C8DjoT363Hjxbl2joEZtLEE4qoBH8DT7RzDwNeOvAmgJJLm9AT4lsWZjRjgecNWYXVL2a4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي من جديد  الجولاني للشيعة في لبنان: هذا المكون أحوج ما يكون بحالة إنقاذ في لبنان وليعلم الله اني حريص على هذا المكون والحزب لا يمثل الشيعة</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79537" target="_blank">📅 22:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e886f49876.mp4?token=fAtMQHkLZ5yzCgEBMcsyncNAs7oGJaivVaz824mzKU5_7bnxOq6nxILwt5emIF9Ci6cCG0Yz7S_U3o52g7pQ3gw4xqM6KHphAeui1G_GmqiFqYSZz3AVRCA7fQT7G686Bu5VNADDJLjaNw9EFBMvNqMkfJRzykhTiWoIgYTrG66P9X0XIbyifzK8e63l5wrfaer3je39XaP2v_wK5Q1_4MLSmo_wwNmqfgokSkyWosJmLTEsO_JlQssAncNcAfHwluYn-LFChvae5UDmFwS2qQK8WFeB9N0IuJN_b_RGEUWdAeKJCRND54jSPsd1IQ8NQAp9YyLR864_F77Vm6nYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e886f49876.mp4?token=fAtMQHkLZ5yzCgEBMcsyncNAs7oGJaivVaz824mzKU5_7bnxOq6nxILwt5emIF9Ci6cCG0Yz7S_U3o52g7pQ3gw4xqM6KHphAeui1G_GmqiFqYSZz3AVRCA7fQT7G686Bu5VNADDJLjaNw9EFBMvNqMkfJRzykhTiWoIgYTrG66P9X0XIbyifzK8e63l5wrfaer3je39XaP2v_wK5Q1_4MLSmo_wwNmqfgokSkyWosJmLTEsO_JlQssAncNcAfHwluYn-LFChvae5UDmFwS2qQK8WFeB9N0IuJN_b_RGEUWdAeKJCRND54jSPsd1IQ8NQAp9YyLR864_F77Vm6nYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
من ملعب لوس أنجلوس بُثّ شعار الفيفا باللغة الفارسية،قبيل انطلاق مباراة المنتخب الايراني مع نظيره البلجيكي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79536" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الحرب الإيرانية_ الأمريكية فيها عبث وليس فيها أهداف ؛ ليست من مصلحة إيران وامريكا استمرار الحرب وإسرائيل جزء من امريكا.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79535" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e1bfb39.mp4?token=eAuI2JhdF10_dKqzQ3kMs-89yR7mbR-ulg7AlcrAUfPqyouEdKbkpI5yot2tFhLEUgQhrfz8WT5SBxOkktEbvxa7wAPoiHRrRAD_D0rBAitvkOxk51Ax-EDSQB_QY8yadLLguA8vrFW-dQvOOm2jJfYCgB5yJSgoQ8us3uxv7XvT76emXkJ2BM7KQSU7g_iiomK3raGrw9ttTzS7KKQlQMBQorUCLoV3dGAbxf_ww9NVTsfMOTh-CLshrwVdxO-BuxQkSiiiOZgFjpvQrWzkFsoemfN4skfOmR3RdCy1ncwZsROO1J8H_Gt_Jpq1K96kDgmTTmVSEXI7afU6ec0zeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e1bfb39.mp4?token=eAuI2JhdF10_dKqzQ3kMs-89yR7mbR-ulg7AlcrAUfPqyouEdKbkpI5yot2tFhLEUgQhrfz8WT5SBxOkktEbvxa7wAPoiHRrRAD_D0rBAitvkOxk51Ax-EDSQB_QY8yadLLguA8vrFW-dQvOOm2jJfYCgB5yJSgoQ8us3uxv7XvT76emXkJ2BM7KQSU7g_iiomK3raGrw9ttTzS7KKQlQMBQorUCLoV3dGAbxf_ww9NVTsfMOTh-CLshrwVdxO-BuxQkSiiiOZgFjpvQrWzkFsoemfN4skfOmR3RdCy1ncwZsROO1J8H_Gt_Jpq1K96kDgmTTmVSEXI7afU6ec0zeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: حزب الله متعدي على الدولة اللبنانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79534" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5468982523.mp4?token=RJ8b2F7WG14lDsjpxyQLUIh2b--km0YMmuQTrVHDKzX8eb_QzPnL_PUj2kNA6SYceRH8TTVq4Nn3T9FmKhpskkT9g8Zyux2OhTo3rYfLkqumVMupi411yjDLAmVwDFpAfL0qck29UugRdfT2j1jgcbxa_vMvbKv4oD2IJRnktmEPsezDHSCc6DaPzYLYCW1-mv5rC0qFdKCvMFXyvV10uiTwwbCf12m3EtSmaUh3XPCVj9mmq_0CQwOXDnwvTfIh0k-XDZW7PizlN-WwA1OQXduVjEobhtgsCbkQAiUlZAy2Ex82vOeT1spEVOceJOZm3DR3uod2_4lnSozLPC2jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5468982523.mp4?token=RJ8b2F7WG14lDsjpxyQLUIh2b--km0YMmuQTrVHDKzX8eb_QzPnL_PUj2kNA6SYceRH8TTVq4Nn3T9FmKhpskkT9g8Zyux2OhTo3rYfLkqumVMupi411yjDLAmVwDFpAfL0qck29UugRdfT2j1jgcbxa_vMvbKv4oD2IJRnktmEPsezDHSCc6DaPzYLYCW1-mv5rC0qFdKCvMFXyvV10uiTwwbCf12m3EtSmaUh3XPCVj9mmq_0CQwOXDnwvTfIh0k-XDZW7PizlN-WwA1OQXduVjEobhtgsCbkQAiUlZAy2Ex82vOeT1spEVOceJOZm3DR3uod2_4lnSozLPC2jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي من جديد  الجولاني للشيعة في لبنان: هذا المكون أحوج ما يكون بحالة إنقاذ في لبنان وليعلم الله اني حريص على هذا المكون والحزب لا يمثل الشيعة</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79533" target="_blank">📅 22:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
مدرب المنتخب العراقي أرنولد:
مستعدون لمواجهة فرنسا ولدينا قناعة بقدرتنا على تحقيق الفوز.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79532" target="_blank">📅 22:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ced46cbc.mp4?token=m_EY0AAnDEWPqT5R5_JwiOm4Kb0LayT__w63ZiyNS6ToVVjP05Pfdh8Rz3c8QB4tMWsEPCFUZECzrEco1PcjYkY1RBXmuBxjlnxKcwPxu9quJauRTlMBUWY8bLbhHmOkpn6PoH2s0Ubu-BgIxoI6ieBGfwDsFKWOC3EoJurk2WQ4hzmd8_oUnZrrmhjv6Waa4AlwRKuv-XNGvfQN_vA9a1Yq80QL9pXY0OawoH3xIllowutXd3v16lkSGP19ouMrK3KRBBg5tbdwv68RznpqVshmEBr2b6H-gAcJjmsII0PWjpw0q07BvAVWVEJk4nPkVjxstsMcLq05tuE65A4WnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ced46cbc.mp4?token=m_EY0AAnDEWPqT5R5_JwiOm4Kb0LayT__w63ZiyNS6ToVVjP05Pfdh8Rz3c8QB4tMWsEPCFUZECzrEco1PcjYkY1RBXmuBxjlnxKcwPxu9quJauRTlMBUWY8bLbhHmOkpn6PoH2s0Ubu-BgIxoI6ieBGfwDsFKWOC3EoJurk2WQ4hzmd8_oUnZrrmhjv6Waa4AlwRKuv-XNGvfQN_vA9a1Yq80QL9pXY0OawoH3xIllowutXd3v16lkSGP19ouMrK3KRBBg5tbdwv68RznpqVshmEBr2b6H-gAcJjmsII0PWjpw0q07BvAVWVEJk4nPkVjxstsMcLq05tuE65A4WnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجولاني: على الرغم من جرحنا من حزب الله مستعدون للجلوس مع حزب الله على نفس الطاولة والحوار معه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79531" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a08c992c.mp4?token=VMjX9EyepxrCLTmFgBKrwgZLAO4JMWi00dgrXK9avxsiWoq461oTk9SVSIlvwj1C_cMfhigRL5v3FBd5z36fkc354GeLDrf07e-nrMjExJCa6fDBc6WnEWh3UJ1izU7t0TXgtBczvWNtAM_FneWoFPO1ElP4WHwRYTJWMcWXmygfgou_D6CW3V2RcfgMvfK6doF8ahBZ3rUD2yKFVc3hptGxZieoVgBpkI9VOFgH4PWeRWJkYLffZUwpT5hhVBymfrYKwJFhYUFhIiWsAMqYrnvY6VfRVwF4PKRLvwUDAn0fFdNWlKY8rKhj1iZzbtxLWMa5O5I59x6um_s_dgIiaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a08c992c.mp4?token=VMjX9EyepxrCLTmFgBKrwgZLAO4JMWi00dgrXK9avxsiWoq461oTk9SVSIlvwj1C_cMfhigRL5v3FBd5z36fkc354GeLDrf07e-nrMjExJCa6fDBc6WnEWh3UJ1izU7t0TXgtBczvWNtAM_FneWoFPO1ElP4WHwRYTJWMcWXmygfgou_D6CW3V2RcfgMvfK6doF8ahBZ3rUD2yKFVc3hptGxZieoVgBpkI9VOFgH4PWeRWJkYLffZUwpT5hhVBymfrYKwJFhYUFhIiWsAMqYrnvY6VfRVwF4PKRLvwUDAn0fFdNWlKY8rKhj1iZzbtxLWMa5O5I59x6um_s_dgIiaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي_آخر
🇸🇾
الجولاني يمد ايديه إلى لبنان لمنع الحرب الأهلية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79530" target="_blank">📅 22:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a9f04017.mp4?token=SzxpqjFBd_nnj8DC3v40zTn4EZPpsqrCPCxjiCzzzLFcLwbSAzxpryYXFtJodhVxW5uIbP8757cX5jcVri-FMi9x2uhN6qG4k-8zxDgkggJ__7qfas3n3KDndqQS9ysdbtISU_8cq2MEzanu-Vs6sx-YH8aKtreUeIbJAuiOZWNhYYqfja_6GKEVPwpBnNzbMVlOCE4hhBs7pYmwXt_dcSmvg0tfSAyGBx9Xzv0lzQeve7ltTeI3cAWJqAKcsSnUWl2QKkM1OQIWXdxNcAbQP9KyoBKSo9ncDAKemn1nKWc4iAX-loqeTf4TC7uggyRLFhWttByx46aldfS4c1hv3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a9f04017.mp4?token=SzxpqjFBd_nnj8DC3v40zTn4EZPpsqrCPCxjiCzzzLFcLwbSAzxpryYXFtJodhVxW5uIbP8757cX5jcVri-FMi9x2uhN6qG4k-8zxDgkggJ__7qfas3n3KDndqQS9ysdbtISU_8cq2MEzanu-Vs6sx-YH8aKtreUeIbJAuiOZWNhYYqfja_6GKEVPwpBnNzbMVlOCE4hhBs7pYmwXt_dcSmvg0tfSAyGBx9Xzv0lzQeve7ltTeI3cAWJqAKcsSnUWl2QKkM1OQIWXdxNcAbQP9KyoBKSo9ncDAKemn1nKWc4iAX-loqeTf4TC7uggyRLFhWttByx46aldfS4c1hv3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي_جداً  المكون الشيعي يجب أن يطمئن في لبنان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79529" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
نتنياهو: حققنا إنجازات عظيمة ولن نتخلى عنها. سنبقى في منطقة الأمن في جنوب لبنان طالما دعت الحاجة. وبالنسبة لإيران، مهما كانت التطورات السياسية، لن أسمح لإيران بالتسلح بأسلحة نووية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79528" target="_blank">📅 21:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287dedba32.mp4?token=E1sj_8XInFz15vaaaQ5jUcAOyJWGohjbHen5YvYqvGo30mpiRWsCahLX_u7bvNEST_S4MF0WSE82SbhWthWyl-myP1F9FJ3RNZM14BO85y3GopugIDFIlciWjDxq_Eq3gh23DoNA9-gKdnWZ0ehqu9KiRBsf-brIRxl67Zt31rGGg9R-269YU7DDS2a57m8KP6NucmdUz_-JrMj_7UbsyWyOwo0d5MrytDAHzyKlo9cbTKxfHNTMkCjqzQfXWp0xAPukswL0kMoiEWg0AtgTFHXZ4Ne5eAJnK5O12BMxXiCDd-RsEXXI66RmafH_5e3UR0FcVH9KA3yCYD-wWp5oDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287dedba32.mp4?token=E1sj_8XInFz15vaaaQ5jUcAOyJWGohjbHen5YvYqvGo30mpiRWsCahLX_u7bvNEST_S4MF0WSE82SbhWthWyl-myP1F9FJ3RNZM14BO85y3GopugIDFIlciWjDxq_Eq3gh23DoNA9-gKdnWZ0ehqu9KiRBsf-brIRxl67Zt31rGGg9R-269YU7DDS2a57m8KP6NucmdUz_-JrMj_7UbsyWyOwo0d5MrytDAHzyKlo9cbTKxfHNTMkCjqzQfXWp0xAPukswL0kMoiEWg0AtgTFHXZ4Ne5eAJnK5O12BMxXiCDd-RsEXXI66RmafH_5e3UR0FcVH9KA3yCYD-wWp5oDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجولاني يوضح السبب: حزب الله ينتشر على الحدود السورية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79527" target="_blank">📅 21:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef06d5c084.mp4?token=ohkQf35lpG-AIGEecsUneSkgIM3hrbXU0WlHttcdix5lKUuUcZxNzz6V-rCA4jX2ymqChQTraeiNqSq9F167-AfXtQaIUhbOG5nAFGeV6O53RxEohFe5n0AN0zFevR7vZMWztlZUDfp_OOOXOz7mi_PsUK5wazXnXp-ou6g6tcyvDdyf8LTYEQ6x6T0t77Px-_epEbb-7KbamF7Q76AJvnzBFk6XAY2bYjAdvm81jsySuXGHEZ1WJkAMUi3hH51phqyvqUxPCC8f8cfbQSYC2wbRpB370-N39VN1LTIEDlXR0behp98pD8uTUHJfC8G_4MFVqt7H9em_53EBzjbPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef06d5c084.mp4?token=ohkQf35lpG-AIGEecsUneSkgIM3hrbXU0WlHttcdix5lKUuUcZxNzz6V-rCA4jX2ymqChQTraeiNqSq9F167-AfXtQaIUhbOG5nAFGeV6O53RxEohFe5n0AN0zFevR7vZMWztlZUDfp_OOOXOz7mi_PsUK5wazXnXp-ou6g6tcyvDdyf8LTYEQ6x6T0t77Px-_epEbb-7KbamF7Q76AJvnzBFk6XAY2bYjAdvm81jsySuXGHEZ1WJkAMUi3hH51phqyvqUxPCC8f8cfbQSYC2wbRpB370-N39VN1LTIEDlXR0behp98pD8uTUHJfC8G_4MFVqt7H9em_53EBzjbPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79526" target="_blank">📅 21:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=LMXi0tQmIalQTrkYV5fXuhU0AlwgfQ5BkjFifhFMXOXl0tixcE_TG8uyv1gCtYw1uiWTrd2OhKZLnzc8zNbdv1G6z-QzahGFYRyAv53mPcCVJg9MZJ_iVqWI3Su6zsmAq5jo227x6VaQbXbwTkUeztHAeJGjqBjVlEPwvwlVluycIvrj7Juw7A7i0qe1BZyOvIGFzX0tQgO2WLdfyVfd4SakRLvfZkaVWpspJgqBUfWkA9_gkHAaPPhwGgqLxh3IUbDlg7iNcegQ-q5No9YBf1sBM-VKf8xmcuz_ko56LBdeoRwKI0VOs6fC6bcX1moNvYD8zLYQrjwm0G5S8Tk0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=LMXi0tQmIalQTrkYV5fXuhU0AlwgfQ5BkjFifhFMXOXl0tixcE_TG8uyv1gCtYw1uiWTrd2OhKZLnzc8zNbdv1G6z-QzahGFYRyAv53mPcCVJg9MZJ_iVqWI3Su6zsmAq5jo227x6VaQbXbwTkUeztHAeJGjqBjVlEPwvwlVluycIvrj7Juw7A7i0qe1BZyOvIGFzX0tQgO2WLdfyVfd4SakRLvfZkaVWpspJgqBUfWkA9_gkHAaPPhwGgqLxh3IUbDlg7iNcegQ-q5No9YBf1sBM-VKf8xmcuz_ko56LBdeoRwKI0VOs6fC6bcX1moNvYD8zLYQrjwm0G5S8Tk0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79525" target="_blank">📅 21:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: إسرائيل أبلغت أميركا بإمكانية الانسحاب من مرتفعات شقيف جنوبي لبنان.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79524" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cb16136.mp4?token=OfX27OSPO4A_z0n1YuK34bF7B0wAgR1nf4Go3133rpoIXT9uYbfDfcm-bEQXH4d3sew-JsnM-QTc_M1l2i9jB186W8t52-8OEoEGgjJS81Ou4oAYLWAEMTFpe-psyh24SXkK84mU9MJ0N6GUl5WUwqACLdHoSHozoYjnkikGgEGRmDLoDj1kZGWTHMVtczDcVkq1P7QZx5deL1riONdplZiYyJwTDtN2wV7gdWjDQh3MGBYGRIOa7UQ4lYfR67ml__8cJPH4rno-HHZGT1GxUoV41MKQ_VCWqGdfnbNeVhVhQPAU1PJ7cVhFgRbeiN1LqwhB_XoRytgS1JBFDBO1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cb16136.mp4?token=OfX27OSPO4A_z0n1YuK34bF7B0wAgR1nf4Go3133rpoIXT9uYbfDfcm-bEQXH4d3sew-JsnM-QTc_M1l2i9jB186W8t52-8OEoEGgjJS81Ou4oAYLWAEMTFpe-psyh24SXkK84mU9MJ0N6GUl5WUwqACLdHoSHozoYjnkikGgEGRmDLoDj1kZGWTHMVtczDcVkq1P7QZx5deL1riONdplZiYyJwTDtN2wV7gdWjDQh3MGBYGRIOa7UQ4lYfR67ml__8cJPH4rno-HHZGT1GxUoV41MKQ_VCWqGdfnbNeVhVhQPAU1PJ7cVhFgRbeiN1LqwhB_XoRytgS1JBFDBO1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79523" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇸🇾
الجولاني: لن تروا سوريا في لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79522" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭐️
أكسيوس: الوفد الإيراني لم يغادر والمحادثات لا تزال مستمرة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79521" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aaa354e4a.mp4?token=kbYvCJozCXbLBjoLpV2U4251GMAzuDH814eo_UIbh2YijEoz3rcI4ZmhbXYNyYDLvTmINTW_kv9O8bhd5glxPnuXlbga2rk5CcnatZegiORmn5ua-icADe-ptA0sYHbOFbzRdOpTM0J3A1YbXTfG35XSZ2vgQzbQGZskjjQHgxoFq7QQzyRmwqhuarWZMBsQrF2O_4gTuPaAquIGc2-TSUwfcME6rp1yTT0zg9MWKpz3Qntgf_q-XhrBCKUC7XuupC97jmbla0qZxCjZtZnHnEO-4LxpDh06SR-bAetUx_O8tIEogxZ7FnpLml9KPbnuEMiA_0fLs02jzQQ8WPqvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aaa354e4a.mp4?token=kbYvCJozCXbLBjoLpV2U4251GMAzuDH814eo_UIbh2YijEoz3rcI4ZmhbXYNyYDLvTmINTW_kv9O8bhd5glxPnuXlbga2rk5CcnatZegiORmn5ua-icADe-ptA0sYHbOFbzRdOpTM0J3A1YbXTfG35XSZ2vgQzbQGZskjjQHgxoFq7QQzyRmwqhuarWZMBsQrF2O_4gTuPaAquIGc2-TSUwfcME6rp1yTT0zg9MWKpz3Qntgf_q-XhrBCKUC7XuupC97jmbla0qZxCjZtZnHnEO-4LxpDh06SR-bAetUx_O8tIEogxZ7FnpLml9KPbnuEMiA_0fLs02jzQQ8WPqvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
دوي إنفجار مجهول وإرتفاع أعمدة الدخان في محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79520" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
رئيس الشاباك السابق رونين بار وزوجته شاركا في مؤتمر أمني في الإمارات بمشاركة كبار المسؤولين من العالم. خلال الزيارة تم تلقي تحذير أمني غير عادي، وبناءً عليه تقرر إجلاء الزوجين فورًا من الدولة إلى إسرائيل.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79519" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إسرائيل
أبلغت أميركا بإمكانية الانسحاب من مرتفعات شقيف جنوبي لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79518" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:  إن الجمهورية الإسلامية الإيرانية عازمة على متابعة تنفيذ التزامات الطرف الآخر بدقة وجدية. يُعقد اجتماع اليوم في سويسرا لمتابعة تنفيذ بنود مذكرة التفاهم بشأن إنهاء الحرب. ووفقًا للمادة 13 من مذكرة التفاهم، فإن بدء المفاوضات…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79517" target="_blank">📅 20:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
عضو في فريق التفاوض الإيراني:  تم الانتهاء من مسودة الإعفاء المؤقت من العقوبات المفروضة على النفط الإيراني.  كانت قضية لبنان محورَ مفاوضات اليوم، وحظيت باهتمامٍ أكبر من أي قضية أخرى في الاجتماعات الثنائية والمتعددة الأطراف والرئيسية.  لن تدخل بنود مذكرة…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79516" target="_blank">📅 20:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الفريق الإيراني المفاوض يترك محل المفاوضات.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79515" target="_blank">📅 20:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb5dd698d.mp4?token=ryJKL49CVXGJ-yhynMKH_X2m5UZwOK-cpxwAAwDYk1euyY6grsNjpl7hcZE9ismn5dF6p1CNrI73VZv97VE1O-K-WV4EbNSFYqlzs0wuzVKQE-Xz67cetAy83njmy2TibNE5VrI18rvPzwu5KwGXaOHDo2Ahu9V4hOP646Ns6fimK3qnQ11e-YyNuFQNAFQv9GfZc9VQo039L7gZTfYX-8amhrmZIiwuzOKyDuZKaiF5kpK9bKW9cIsjXdciZX86TqcFqwN6QReKMnyNcb1cYSrKBzMmh5sGGXDnhLO79GUA770Cb4khiJvyJhOSY1UOZ7MHx8OdWozmInjvrDIZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb5dd698d.mp4?token=ryJKL49CVXGJ-yhynMKH_X2m5UZwOK-cpxwAAwDYk1euyY6grsNjpl7hcZE9ismn5dF6p1CNrI73VZv97VE1O-K-WV4EbNSFYqlzs0wuzVKQE-Xz67cetAy83njmy2TibNE5VrI18rvPzwu5KwGXaOHDo2Ahu9V4hOP646Ns6fimK3qnQ11e-YyNuFQNAFQv9GfZc9VQo039L7gZTfYX-8amhrmZIiwuzOKyDuZKaiF5kpK9bKW9cIsjXdciZX86TqcFqwN6QReKMnyNcb1cYSrKBzMmh5sGGXDnhLO79GUA770Cb4khiJvyJhOSY1UOZ7MHx8OdWozmInjvrDIZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
الجيش اللبناني يسحب آلية إسرائيلية تم إستهدفها وتدميرها على يد أبناء نصرالله في بلدة دبين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79514" target="_blank">📅 20:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvAYcIeMO3cm7UUv9PlcxiEoQm0WpLaJxyHLCH-vHLu_lBkY6uFs5P2KzouJKkbRqRCk8epIwVWriqJ9hUPn0gIV2BlgDd6dOwcDvLhyWvEQ3xom0I8Sy83omktEtxMm0ELZb3Q5Gy7gi6luRzdmau1iN8w3ZDFGnwRmsBy79lLYvdQAidWLwGKQGrLbTU8G2_Epsri1zPg15INOrSYHeWQ7cr0vWB4WK0n4LN3vm3FsqOgCncDDKKmg23tw-OneX-YeAc1ou2W75lUMlpw6ScZ-5p3673tijQQXzChTaRuX3gRXeqL1x9nYOCBMp1OBAx9C5X2uRddogYdk5nxvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79513" target="_blank">📅 20:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الفريق الإيراني المفاوض يترك محل المفاوضات.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79512" target="_blank">📅 20:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: تهديد ترامب يوقف المحادثات في سويسرا، ويُلقي بظلال من الشك على استمرارها.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79511" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">طوفان ٧-٨ ادامه دارد
طوفان ٧-٨ مستمرّ
Storm 7-8 is ongoing
#كابوسكم_رمضان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79510" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0d5c6577.mp4?token=pzij6QFlnGWsBhgyHIDEck0BEJAHSlC_vxeX1oRdXDcPTxOf9HGEeI7lnrcZ7OrmbTL-B5NIEAjTl1i3AsHQ9D0Ci_TMpPCBoeu-JZk0J5UzYjaGxwuv4ifSg-k71zr8hD1dz56Su5gfdeRJgHJvVyAOgtLJhGow1NqOMCGdTc_oUlDr3OyR4SX72WQTVFCjjTRBiJISbE58pDRSdk74z4FbNM2qXOMcd4_Z45codSIW-QMTY83QPXafKQ64zjc8VuegyLmbUveK4ql4dOvayE0oDJ3rBnYdb6smbvGH8IU_fDYBFKMMATsYl7pPRLMZMBV5Q41b791Bbq-8AGgx-SpAK-dVG4fqt69VeRBx7T9lPCnVwa3xEzf_orF1w2QhonivNHX7DHgaxTF6qOrQyoa-iRV6HUHXYayTbaRkNIzYLa1ISb7uhXxSIRE7pRGAPIt3coBSGWor0IDZijZVam-hxoj_qa5nGYYeZnsSbWP9vrbbVNAtCfm2JFXJGEo-mYNqltZDrOgvIJ_VnKa4T6b2zhA8HNIUFiIAB8x2fmkz5whZnz_dM1tU_mxrxKrPWLbKfEy0yIlTv2KxzDjtMJ9qYXWzFe3X_HN0h8ISFx8XEWx1yrh1WkxZHa_k8BWmSSSuzssV_6nh9VOUyH6NyCTILJu08UkEII5MB_7iUjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0d5c6577.mp4?token=pzij6QFlnGWsBhgyHIDEck0BEJAHSlC_vxeX1oRdXDcPTxOf9HGEeI7lnrcZ7OrmbTL-B5NIEAjTl1i3AsHQ9D0Ci_TMpPCBoeu-JZk0J5UzYjaGxwuv4ifSg-k71zr8hD1dz56Su5gfdeRJgHJvVyAOgtLJhGow1NqOMCGdTc_oUlDr3OyR4SX72WQTVFCjjTRBiJISbE58pDRSdk74z4FbNM2qXOMcd4_Z45codSIW-QMTY83QPXafKQ64zjc8VuegyLmbUveK4ql4dOvayE0oDJ3rBnYdb6smbvGH8IU_fDYBFKMMATsYl7pPRLMZMBV5Q41b791Bbq-8AGgx-SpAK-dVG4fqt69VeRBx7T9lPCnVwa3xEzf_orF1w2QhonivNHX7DHgaxTF6qOrQyoa-iRV6HUHXYayTbaRkNIzYLa1ISb7uhXxSIRE7pRGAPIt3coBSGWor0IDZijZVam-hxoj_qa5nGYYeZnsSbWP9vrbbVNAtCfm2JFXJGEo-mYNqltZDrOgvIJ_VnKa4T6b2zhA8HNIUFiIAB8x2fmkz5whZnz_dM1tU_mxrxKrPWLbKfEy0yIlTv2KxzDjtMJ9qYXWzFe3X_HN0h8ISFx8XEWx1yrh1WkxZHa_k8BWmSSSuzssV_6nh9VOUyH6NyCTILJu08UkEII5MB_7iUjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في الأطراف الشرقية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79509" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
قاليباف: ألا يفكرون في أنفسهم أنه لو كان لتهديداتهم أي تأثير، لما وصلوا إلى هذه الحالة من اليأس التي هم عليها اليوم؟ نحن لا نعير أي أهمية للتهديدات الأمريكية. ‏عليهم أن يتوخوا الحذر في تصريحاتهم، فقواتنا المسلحة مستعدة للرد بطريقة مختلفة. مهما قالوا، فنحن…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79508" target="_blank">📅 19:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNr4SdOdqhF5HsN9zg6qtLHvnDX4MBQC5oQV11WNoZsLb2BLR6JDGvozEf1SLBcUWfrhwoJriWDZhwPwzq6d5Xovd6Me7DeEC_ipa6NORPP9WqUGaYByehmLgYhxaE9a2nxZSW4vha6gzppgLhJ5fG1dAj2DJO1Z-8Ymx3hr7RVWDCC8jAST_JOG76B26t0bzCx-AtUmoQ-TFAqJztvBxl2YlBLRsZzs4VVOpBH_eoQo6P6xJgUzqYobvSNyIq-b0vcG4KW3qb--QMOEWnNV-qlMMBccTnutkCciU4dptYr1akzdO3U7_XM9tks3sP9EosSf-RI3ZHByW58UMhMTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: الوفد الإيراني يحتج على تهديدات ترامب؛ إيران تدرس خيارات الرد المناسبة.  أعرب الفريق الإيراني المفاوض عن احتجاجه للجانب الأمريكي، وهو يدرس حاليًا خيارات الرد المناسبة على التهديدات اللفظية الأخيرة التي أطلقها دونالد ترامب. وفقًا للمادة…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79507" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: لا يزال من غير الواضح ما إذا كانت المحادثات الرباعية ستستمر أم ستتوقف.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79506" target="_blank">📅 19:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر
🇮🇷
🌟
مصدر إيراني مطلع: إذا لم تنسحب إسرائيل من لبنان، فسيتم إيقاف جميع المفاوضات. وستدخل إيران مرحلة رد فعل عنيف مع استمرار الاحتلال الإسرائيلي وجرائمه.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79505" target="_blank">📅 19:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
🌟
التلفزيون الإيراني: بدأت المحادثات الثنائية بين الوفدين الإيراني والقطري عقب المحادثات الرباعية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79504" target="_blank">📅 19:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني: خلافًا لما ورد في بعض وسائل الإعلام الأجنبية، لم تُعقد أي مفاوضات حول الملف النووي خلال الدقائق الثمانين الأولى من المحادثات. ركزت المحادثات على تنفيذ المادة 13 من اتفاق إسلام آباد، مع إيلاء الأولوية لقضية لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79503" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
نتنياهو:
حققنا إنجازات عظيمة ولن نتخلى عنها. سنبقى في منطقة الأمن في جنوب لبنان طالما دعت الحاجة. وبالنسبة لإيران، مهما كانت التطورات السياسية، لن أسمح لإيران بالتسلح بأسلحة نووية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79502" target="_blank">📅 18:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79501" target="_blank">📅 18:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
السيناتور الجمهوري غراهام:
لقد أمضيت أربع ساعات ونصف مع الرئيس ترامب يوم الجمعة. إليكم ما أعتقد أنه سيحدث بعد ذلك. إذا فشل هذا الاتفاق، فإن الرئيس ترامب سيسيطر على مضيق هرمز بالقوة.
ستتحكم الولايات المتحدة في مضيق هرمز. وسنفرض رسومًا على جميع الذين يمرون من خلاله لدفع تكاليف العملية.
وسنقوم بتوسيع اتفاقات أبراهام في السنة التقويمية 2026. سنجعل المملكة العربية السعودية تنضم إلى اتفاقات أبراهام.
وإذا اعترضت إيران على سيطرة الولايات المتحدة على مضيق هرمز، فسنقضي عليهم.
إلى الإيرانيين، إذا كنتم تستمعون: عندما تستخدمون حزب الله لمهاجمة إسرائيل، ستكون السياسة الجديدة هي أننا سنهاجم إيران.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79500" target="_blank">📅 18:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🌟
مبعوث الولايات المتحدة في الأمم المتحدة:
إن إسرائيل والإمارات العربية المتحدة "عملتا معًا عسكريًا" لـ "الدفاع عن بعضهما البعض" ضد إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79499" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله:
لقد بات واضحًا ومؤكدًا أن جولات التفاوض المباشر التي سيق إليها وفد السلطة اللبنانية إلى واشنطن، ليهز برأسه ويبصم على ما تسطره الإدارة الأميركية من إملاءات تصادر سيادة لبنان، وتنقل موقعه السياسي إلى ضفة المتصالحين مع الاحتلال الصهيوني وكيانه اللقيط.
ليس مأمولًا على الإطلاق أي خير ينجم عن هذه المفاوضات التصالحية، لأن منطلقها خاطئ ومريب وهدفها إذعان واستسلام.
إننا في حزب الله ندين مجددًا نهج التفاوض المباشر مع العدو الصهيوني وجولاته وما ينجم عنها. وندين وظيفتها التعطيلية التي تشكل عثرة في مواجهة مشروع العدو وجهود الميدان المقاوم والتضحيات الكبيرة لشعبنا العظيم، والتي يمكن للسلطة تثميرها والضغط بأوراق القوة هذه، لتحقيق انسحاب كامل وغير مشروط من أرضنا اللبنانية.
إننا نعتبر أن مواصلة الحضور في جلسات التفاوض المباشر هو تنفيذ لأمر اليوم الذي تُصدره الإدارة الأميركية للسلطة اللبنانية، التي تُلبّي متفردة بقرارها وبمعزل، مخالفة للميثاق والدستور والقوانين، وتستجيب لما تعمل له أميركا وإسرائيل في زيادة المخاطر على لبنان واستقراره واستقلاله وسيادته.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79498" target="_blank">📅 18:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVEsNOtmxlBXvv0BARLXZwXz4fvdCxvGNQFR-AT-bxLficnVmH3UhFZ17h8qLBra19317sdoLp7JPZGOJbjyiWWVZgUlEzX-SWItj40qGctAm2jIeJUNP7YmW397B53i3m6qu_qsHm7mrVglXi1ql6wT9aA3yCR-cfuXRYOggn_S_lBU19c9Kpvlm7yxU2dfVhTvnvIfbXQ9CessqN9e19HqQulEnDWTkmLMBTCXv9w7AJc_Ok7OBO-Sp_385cE7CAv8mJSnKwtTGEo0Osp0lyS9BK3sMlml2QHMeLNAw5dgDuqM7L4cFD9yeKnHQiQMlqu29aovrG1k4kbuevpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
لن ننسحب من المناطق الأمنية العازلة في لبنان - يسرائيل كاتس</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79497" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منظمة UKMTO: حادث على بعد 50 ميلاً بحرياً جنوب شرق مدينة الشحر في اليمن.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79496" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79495" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRO4UfjIfucl7vfknGTo_WadG15cs5-LHzJk2cUJ29-SMufxiw5Q1xiR2IecCndaxcrI597QQcnnL-Opf1F9CgBZOaFd4WypPvJfRGSdunB5SxI9TnDAymAGSUq2XpK0vFoP9vDlmJ6GJjIe8DbNiaC_T8-1jaA0LzarDRO4qWvRktaz0VLYg58ILG60I5mqRgodCCpIws0VfpqI2-PMNuMrCveCkjMVyMpBItEyRxx7uWwle1Mm6WVbSpTPqzcRFBQPXGHFju1HfQAtBL13uLqIE5GJlYj6xPMaOl7bHrPMH1Cpu610D8iuAaEIRl9gY6zJcGrFxAW3hZ2cmm_uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79494" target="_blank">📅 17:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-zUPNm4xFq3dAqds0VDYNOaEAIHmWMwVbFaGHr132egM4Mqak20c1iFb36qnp94jP-W32u0nr1SxQBQ5REB4ojrN8syImCBCFouFcIeBdc96eKOnCf3dIiWTrA8-JlvoCBTQUBdeROEfUcgQKUygOHECzW0RGjqEmnGpHESEEJNdQRks46G5ZqKNYWeTuGvwxdFuX0HVC1h-8rNijSdodhk1Xld_oEl3fRgFFcUgqGgd4cevbM--VKjNm8Dbt1AbLt8xFTOMurVFWfiVOFUS91qLWxj7wVTuIdxPzOHkt4RYJ0s3vfW2cc_OR2LFEtS6VUgkfJ6WEc34fSZXdl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
🇺🇸
ترامب:
سيستقيل كير ستارمر من منصب رئيس وزراء المملكة المتحدة. لقد فشل فشلاً ذريعاً في موضوعين مهمين للغاية - الهجرة والطاقة (فتح نفط بحر الشمال!). أتمنى له التوفيق!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79493" target="_blank">📅 17:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من الفريق المفاوض الإيراني: مضيق هرمز لن يفتح دون كبح جماح إسرائيل في لبنان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79492" target="_blank">📅 17:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79491" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
‏
ترامب:
على بزشكيان الالتزام بقواعد اللعبة وإلا سنستولي على إيران.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79490" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انباء اولية عن تحطم طائرة اسرائيلية في الولايات المتحدة ومقتل طاقمها</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79489" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZhGE8ts5VDxzp7BiaZD86KP_j0aSgepsksxlho9RDVsXllgBCgZClLTk-i-efbAA_1qkEkrhOb5H_Up2VHFotzl8-ufPLFsT4fzDvA8c0M407qWkURUsgCYhSMLoh3CQUwUPgL6hNKRbK8eE-LjU1nIYwLuYylc-WEvxPuCzExLwKwSXi2IFY4qzK1iYtxAcpyMsN07Nhg16H8TVrZEJ6EJ1BIhRvlP-8PMsaZyCPcNqRmq5JxBLUoQ8CP2pCiYLMcLx1iBDWdL2lxZm9H8ACblDahHLKUbSf8-Ep-47pggQHhgU7Ok7UkTVEVcs78RycxwonQVty4Kx6hjYd9EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
يجب على إيران أن توقف على الفور وكلائها المدفوع لهم بسخاء في لبنان عن إثارة المشاكل. إذا لم يفعلوا ذلك، فسوف نضرب إيران بقوة شديدة مرة أخرى، تمامًا كما فعلنا الأسبوع الماضي، ولكن بشكل أقوى!!!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79488" target="_blank">📅 17:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79487" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgdG1-wdCOBUoMhC6QqFSISP-FwN-t41mGNAX_OrwKcZCaB6J_GW5JaOMcmfihpa5PZ57zcPrUeC9TY5SWJ4__ULSYpWGI1WRjEfQwY5snM52q_PD-9valGjxkfiGQreFt3fPJZ9NAj9dmiAq0V6rUXZ3uKrxoiqbgLHm12TYsni5MxwvNzgw8HUOG0u6QS-GK6GnUqmfPz4In2wdDRgBgciAJcM26TcaCSlBXQ-cWOgLFdHgvVwrmr7ycVUA8z0YmkbbS7C2wThb96fW8wG8OJacnxw1VoUg65T1N6RL_UxgPZ02KOqCysLa7ndEnA0OAn0yqTlEIaQS7MI7L_MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب عن الانهيار الامني الذي تشهده المدن الامريكية بالتزامن مع تنظيم كأس العالم:
هناك الكثير من عمليات القتل تحدث في شيكاغو. 22 شخصًا أصيبوا بالرصاص، و4 قتلى على الأقل. لماذا لا يتصل بي الحاكم بريتزكر لطلب المساعدة؟ يمكنني أن أجعل شيكاغو مدينة آمنة في شهر واحد، وفي عام واحد، ستكون واحدة من أكثر المدن أمانًا!!! لقد تحولت واشنطن العاصمة من واحدة من أسوأ المدن إلى واحدة من أكثر المدن أمانًا في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79486" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏ترامب يهدد: المفاوضون الإيرانيون لن يعودوا إلى بلادهم إذا أغلقت إيران مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79485" target="_blank">📅 16:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🇺🇸
الوفد الإيراني يرفض التقاط صورة مشتركة مع الوفد الأميركي.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79484" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#ترفيهي  ترامب: أمريكا قد تصبح الملاك الحارس لمضيق هرمز وتأخذ 20% من النفط</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79483" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌟
ترامب: إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79482" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
ترامب:
إذا أغلق الإيرانيون مضيق هرمز فسيتم القضاء على بلدهم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79481" target="_blank">📅 16:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فانس:  إن ما يمثله اليوم حقًا هو بداية مفاوضات فنية لن تحل كل خلاف، ولكنها ستسمح لنا بالجلوس معًا كفرق، ولأول مرة في التاريخ، لمعرفة ما يهم الأطراف المعنية أكثر، ولتسوية تلك القضايا، وحل تلك المشكلات، والوصول إلى غد أفضل.  ‏إن سبب وجود القيادة السياسية للدول…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79480" target="_blank">📅 16:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فانس: ترامب ملتزم بتحقيق وقف كامل لإطلاق النار في المنطقة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79479" target="_blank">📅 16:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فانس: هذه الهدنات دائمًا ما تكون معقدة بعض الشيء.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79478" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فانس: حثنا ترامب على "طي صفحة الماضي" لإعادة تشكيل العلاقات مع إيران</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79477" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فانس: هدفنا هو إعادة تشكيل الشرق الأوسط من خلال الدبلوماسية المشتركة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79476" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فانس: تم إحراز تقدم كبير في الساعات الأخيرة</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79475" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مشاهد اولية من المفاوضات الايرانية الامريكية المباشرة في سويسرا</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79474" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCFt2XLFVQR6gg6h2FQsEwFc340nibuF8paYuU1ndj3VjZdG_bIbPcBfkiClI0IK0fPw4HdHYtHRIK4_KnSwsTCB6ofmvmKFLwnvH-k7Izs9T6R3GJp8FuqVejFCzx3YkUnMLGV02l1fvH6zwzc97Y09imt3DjPNPmqWC0RwAFaAh_QuV3T2uLByTsSTB5TcXbuSchTUFEY2Y7b4qc63qLbIcXqvTWFSH7oVox3uhj1rcoXtMTyS--9-pzYx2kDEkB32GPAWlopkHJYpLQ-fgmkHJ1R-Xfd73dRWx0ARfadFiA9lecHVf1gi1w7KaBRMS6z7ph5cSDvbdYZqnXkF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79473" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بدء محادثات أمريكية إيرانية مباشرة في بورغنشتوك بمشاركة الوسطاء القطريين والباكستانيين</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79472" target="_blank">📅 16:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-06-2026 آلية هندسية تابعة لجيش العدو الإسرائيلي في أطراف بلدة أرنون جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79471" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يراد منه دثر إسم قوات الحشد الشعبي العراقية تدريجيا من الذاكرة العراقية   الدكتور عبد الحسين الموسوي ممثل حزب الفضيلة التابع لليعقوبي الجهة المسيطرة على وزارة الصحة تلغي تسمية مكاتب الخدمات الصحية للحشد الشعبي وتكتفي بمسمى إسناد القوات الأمنية..</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79470" target="_blank">📅 16:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79469" target="_blank">📅 16:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiT8ewQNS14nIts3HcpszNKoUYWLoLlawfnQ_2Iq5d01NYYPdAocPheOoy6yJwnwYo8zecDAhADYvHAhlLRSAjEqOAbvUJHfTwp9DYzhQZOVyR4KDZxXNXrvNfO7jpWFTjvaWDF1EQlI6Q3o8CfbMSOTqdRPrjOWhrZSdPVh7J9HYBVakCPJt5QN6Ah56z8XIGFP9wbJcjkkk3ylBwIOW4hDInTWv-Bjy3-CHtBqvmJN2fVkrlqXTXK7I49par7Xn-drL53rYySQ3AMa29ghs_JZCOehYvO0LG5NJYXqZFWvEVCVVC-6O3VMop0v2sHA1D32z1yve2H8bVCsGoDRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران الشيعية
استخدمت مضيق هرمز من أجل شيعة لبنان
برأيك لم لا تستخدم تركيا و(الخليفة اردوغان)
مضيق البسفور من أجل غزة!!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79468" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy7d2Fs0JwfLra41C8mst4CIzPmep_3VjHxlong7WydQAml8d-Z-tQ2LTummghxvAiPhXhI2BT6EjAMMREsL3gEgXQwhKJ4dV-pUER7mxNKmptEQPufTjQkc7ZzSLXdWLWy6BYo0dRWyu_hhBXhAfb7ydarz3BGBuseF6XWbTEypSA0KgA43ovYPyiW9qOlErWChvZUf2y9ocaVDtgp_smabBvsuib1H7uz-Ey702vQJsE6lLCkXE37pjDFDtufz6jOKgJYrPFWx6nVoIhvYxpj74H51HvzkByrhYcdq2JSNrP2c0bjtW7Wn_vB2cMMad1QiUk72jsFYHWNTI5EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعمدة الدخان تتصاعد بالقرب من سجن بادوش في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79467" target="_blank">📅 15:28 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
