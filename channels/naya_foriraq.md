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
<img src="https://cdn4.telesco.pe/file/R4iz227nIC58QkdJbhGGjs66IoEyc0b7yd6mUI1FktF10AQfueS6EX-IW3MOuvYdFqITqH38hEWGUVDXx869JV3TKyXxWn4qB2mLEOO6B0um-pCFj0sojrDyRNmZo19OSUPQAOXxMp4Z1njWXQU32afHyj6J74B_edeHfFioAPcgu6YBear02B6pce3pDtMPKC96B2374ZJS3a2hf75EGjh2p-sMUaxUDx2LZ1pEer3aj539F9ASpIKp4kwVnQyBamM3kSMQJe-LqP_ZNf4S1WPdMLcStD4P9-Yy4OF8OM0tmfwJvw_e2RYl0aDON73VMYPNg2vW_mGsCEJOWzb5PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 261K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-82707">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">استهداف سفينة نفطية قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/naya_foriraq/82707" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/naya_foriraq/82706" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/naya_foriraq/82705" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزارة الخارجية اليمنية: سنبدأ مرحلة جديدة بالاستعانة بالله لانتزاع حقوقنا كاملة غير منقوصة وسيكتشف النظام السعودي أنه أوقع نفسه في مأزق إستراتيجي كبير وسيدفع أثمانا باهظة نتيجة لذلك</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/naya_foriraq/82704" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارة الخارجية اليمنية:
سنبدأ مرحلة جديدة بالاستعانة بالله لانتزاع حقوقنا كاملة غير منقوصة وسيكتشف النظام السعودي أنه أوقع نفسه في مأزق إستراتيجي كبير وسيدفع أثمانا باهظة نتيجة لذلك</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/naya_foriraq/82703" target="_blank">📅 15:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الطائرة الايرانية تتجه لمطار صنعاء</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/82702" target="_blank">📅 14:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/82701" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">غلق مضيق باب المندب؟!
والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام
EU this, winter are to cold</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/82700" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">استهداف مدينة زايد العسكرية</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/82699" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/82698" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/82697" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82696">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">المتحدث باسم انصار الله: في عمل عدواني سافر ووقح، استهدف العدو السعودي المجرم مطار صنعاء الدولي بسلسلة من الغارات الجوية، منهياً بذلك مرحلة خفض التصعيد ومتحملاً عواقب عدوانه. ونؤكد أن هذا العدوان لن يمر دون رد وعقاب</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/82696" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrDsBWbGas-eyGqLn0o0g8zC3tCDJ1FFl8pCf3jNeVFu4pAzsKVVpkktTiCuCErg0B2046hzJJ9PB-B4ybS777vNcz1NOXQj9WYGgF1o849bPwfjYO8HBgttGdS9CKKZOB6k1vmSVmz9eI1bGbGkD1J4c6zdPvQIIYJXRsZ3IcwIZLd644OXbqnQGMFbOQJ2wIjmgIv0AJzOowEDXy8JSlZ9nTv1SPYrO_H6F9r-sgFVK7bdFBj9XZCN8AFqR9Y8jfoF5qplYneWj2htopgKa4DICKdzzB8p0d55MaJR4E3VzGCskDqweaXbaGSXiEWgf6aTa2ZDzPQ65GkPoss0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة ايرانية تقترب من صنعاء رغم عواء المرتزقة التابعين للسعودية</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/82695" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZQ4gRSAgZj2qmXu9Q6ru1LkMzNrLtwefLxk1IT67iQ50a547LPkYfdHjjs9A4Pv0FSbfUCn-nPw0aJtYFUDonmp84nd2bDoYqbO7n7xMR81W5NlmU2f-eKJINkmKkOUL7VIh9JDILM_YuuemMvX9Mh4f1_RFCsC8abs7SP1a5kkL3EOWP1N7lsPgCLQVGDndF566899Sm1uvmcYO9t9xcicbFXMHqwwFViMg9preBZiyDvVtLFwVc4IgoguDp4dhgTrlQab_BNyLSb-H7Ilnb9C-qT9vRd0-INyd1Gbc8ydDDBVuswtRj034GayWD1ungWOwvEqYR75zqUCFvtGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مطار صنعاء</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/82694" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQwXY6b4PVcxm6qIC3fSUi7n5ntQCx9ZhmzOljw4I_ZoAVd2OOthc9PNB57Znciyc9QqN7WsWlTy_ORdPY4ZYiSRaL3-22W-Bmb5meWzVv2_9RhwUzjfj_3OgXHtakSIXxWJoiZQxENEy7x85tsWg9lmyI1EnWKhtAaZcPAwbDpX0LPkMqyIsqIXWPwXFQ1MSAtug-2P1a2DZERtMYhBjjejSjU8w5bpAsxxMBNHniqJrmguT29TpTfI7yngfz86vSJd0jRZ9SWSKHilXWKu3vAUDqxxt9uY06JA7p14HGOK8mBeraW_4K6HfQxVG1bubt5FPJvBAiA4GuiReESRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار صنعاء</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/82693" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJR8JZgecpOOEbKcsm8ZDOERsQwQYEUrkKWUyhH1O88Wd5s9EXXuva7lHoRz9oYhMO2qvwqaepTKjjVMncyOv9KKqJ4tfXFEdfEDV-nHno8IAolbk36l2BwgiU25pQDFzoI7bsDw5-sJ-D3bhVZcsZ5jTQnM3Xg76VsmESsVF7i2LV40sm8g7X531a6T_38vIZgjuZDrxmv7Kv9ju8M628gg_EBaQUG39LVap_fMRW2XMPcbdMLh_g6Z3IJRoYGS5S_JoKKfEyzPHKLwdfcV6G4v1E-ixQcfUP2qEj8X8fItWhHqMUoY02KxxwFE-MRrtBBF-oyFDPjGazniCi1dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات سعودية تستهدف مطار صنعاء الدولي</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/82692" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/82691" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82690">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/82690" target="_blank">📅 14:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82689">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaG5B48VVSGwLP2xZ4BovXSA1u1zd4riU_Q-HB-5RDY1dRyEtfxejXDjxhUXpAnFYwGBwotTNxX-3ZDkrn0gw3ULhVDwarVSdWV0DtSxYNsWHB3z55q4blH4b1bto4baHJsKpY0u3Ha1xuaPTTE85ZDfyxj14_FmxgA-yUdBI7CfNfTqpXqL9aAJkaBd9jIooFjxd9TBeadT27k2aDDokclXvZegMte-cwL9e_CZv-Ha6LgSOGCrtOAcQgswPkSKxZxUjum7MfJUfH6CS50a-TTpWKaIDW-osk3-w5QjJ4aVV2eG43x7iGF62rYsaq6kUiXQyVwkdBj0q0X8yBATCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس وزراء العصابات التابعة للسعودية في اليمن ‏يعلن حالة الانعقاد الدائم لـ"حماية السيادة وردع التصعيد".</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/82689" target="_blank">📅 14:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نائب محافظ خوزستان: تعرضت ثلاثة مواقع في آبادان لهجوم من قبل الجيش الإرهابي الأمريكي. حتى الآن، أصيب شخص واحد.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/82688" target="_blank">📅 14:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">العصابات التابعة للسعودية في اليمن: سنتصدى بكل الوسائل المتاحة للطيران الايراني الذي يذهب لمطار صنعاء الدولي وسنلقنهم درسا يسمع به القاصي والداني.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/82687" target="_blank">📅 14:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجارات في عبادان</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/82686" target="_blank">📅 14:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات في عبادان</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/82685" target="_blank">📅 14:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند يوجه بحظر كافة منصات الرهان والمقامرة الإلكترونية في العراق</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/82684" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محافظة اربيل في شمال العراق تعلن عن تعرضها فجر اليوم لهجوم بثلاث بمسيرات استهدف مخيم للمعارضة الايرانية الكردية في منطقة داراشاكران التابعة لمنطقة بيرمام.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/82683" target="_blank">📅 14:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند يوجه بحظر كافة منصات الرهان والمقامرة الإلكترونية في العراق</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82682" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇸🇾
عصابات الجولاني:
خلية تنتمي لداعش هي المسؤولة عن التفجيرات في دمشق خلال زيارة ماكرون.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/82681" target="_blank">📅 13:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇺
المتحدث باسم الكرملين دميتري بيسكوف:
تحالف الراغبين مخطئ في اعتقاده بإمكانية إلحاق هزيمة استراتيجية بروسيا، تحالف الراغبين المزمع عقد قمته في باريس من دعاة الحرب ومجموعة من الدول التي لا تريد السلام</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82680" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏العصابات التابعة للسعودية في اليمن: نفد الصبر وسنرد على اختراق إيران والحوثي لأجواء اليمن.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/82679" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
العصابات التابعة للسعودية في اليمن:
نفد الصبر وسنرد على اختراق إيران والحوثي لأجواء اليمن.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/82678" target="_blank">📅 13:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة مهر: اشتباكات في المياه الإقليمية للخليج الفارسي ومضيق هرمز وسماع دوي انفجارات في محيط مدينة بندر عباس وجزيرة قشم.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82677" target="_blank">📅 13:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة مهر:
اشتباكات في المياه الإقليمية للخليج الفارسي ومضيق هرمز وسماع دوي انفجارات في محيط مدينة بندر عباس وجزيرة قشم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/82676" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbb1i2SEAFXEUHdUwj2DEey9H_xkGLsS94Y-T5cobS1wf5OAVJigKJZRvGoOKl9A_7w4Y6BtatxsLaN21nON9wzawaMMRK4eheljoC5ZzrJwOUk89jB-MquxuWuQx3MhmEqF3IEIw4KUTUko9nQjVee3xvsUwiMoh-VbgVLaJKElWgMPGVkGrvEOHPK5GIxoBUO3aupGY0peef-ZrwRPcNIBrGG9hhWhTQxvgwAE22XC5dXt4yuFlR0nCYYzMjlcgEHt3mwYOjgh6TURZf9fc_FylTe9Jrrw1s3EtDtYVQlwFvA42343lr-WxmCC3e747-ZPSOz7hKzKhKBwX02xaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇭
السلطات في البحرين تعتقل شابين اثنين على خلفية حضورهما مجلس عزاء الإمام السجاد (عليه السلام)، وهما الشابان أحمد صادق الشعلة وعبد الله عيسى الشماع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82675" target="_blank">📅 12:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
المتحدث الرسمي للخارجية الايرانية
بقائي:
▫️
السلام على أهل العراق، وأهل النجف وكربلاء، وعلى الذين اعتبروا أنفسهم جزءاً من حزننا وأظهروا أن رابطة المحبة والتعاطف تتجاوز الحدود.
▫️
وإيران لا توافق على طلب الوكالة الدولية للطاقة الذرية للحصول على حق الوصول إلى المنشآت النووية الإيرانية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82674" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇷🇺
🇺🇦
جهاز الأمن الروسي FSB :
يعلن عن إحباط عملية أمنية واسعة للنظام في كييف كان مراد منها استهداف مطارات عسكرية ومدنية داخل روسيا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82673" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
🇮🇷
مصدر ايراني لنايا الانفجارات التي تسمع في محافظة اصفهان ناتجة عن تفجيرات مسيطرة عليها.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82672" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
🔳
اليوم العب بيهم جولة.. من أمام القنصلية الكويتية في البصرة، المتظاهرين الغاضبين على إستشهاد الصياد العراقي يبعثون رسالة تهديد إلى دويلة الكويت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82671" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN1oQVwsojPu-STevnvrj7qml-Okbh7xlpb_A6SRypXLizrUFz8MjSceGB3uM-BnVaTSC_w-YLgfikQnU_PsI8izS1lhGVzsPw0JSQb7JruXDSW44i1HNACOMkY5bvVVgsb3yD5ThsEwpptTTfP8n76OMnDEFVnMmWPjenX5mZfdaP2TP0HryvQ7AEbmxOYEjMl0-IDwgAI7BH3uQHcyWUSkyqV1Z5cSlHIUTlShA6FwLJ7bRuGAwCvE4BfzlEYlroq-aBm1fVY5GnDxo0axpFfZFTkZTxzZVv4xu2YfsfrfhxOL3JC4JNcjpVkO8D5BzxJXCyzlIv8tdO83M9CnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء العراقي:
استرداد 375 كيلوغراماً من الذهب في قضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82670" target="_blank">📅 09:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارت عنيفة في البحرين</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82669" target="_blank">📅 09:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارت عنيفة في البحرين</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82668" target="_blank">📅 09:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=VttfIFta2eYMtJEG3AZ7JogpagiAgc3eTKwnC5cnKqCB0r5VXLyEA7R2WtHyvJeKKupHUIKaEvJBA9_w_JwJ-pGYmAmJMVvMDQCwmnXGsNAZng-LsZQm_g9A5OWxo-Op4b1e9RDsLbnnG7_0WVLzh9_5E1Zz2xacaDCKbV_My7eq7Ov2xXxnysOzfAwTGooAHm5lHF2KKWZ-d5Qj4pZ61piN8wU8dmcdUEUPUTT9Q-QM45m8n2IznZLHV4do7mefWmx0ykI-X1My3TLcN6aFicOSawuNr13gjF35IQvR3jYsvmUJSvw8457ao23tfwqcnQq1Ndt9g-AynDu1ZKL57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=VttfIFta2eYMtJEG3AZ7JogpagiAgc3eTKwnC5cnKqCB0r5VXLyEA7R2WtHyvJeKKupHUIKaEvJBA9_w_JwJ-pGYmAmJMVvMDQCwmnXGsNAZng-LsZQm_g9A5OWxo-Op4b1e9RDsLbnnG7_0WVLzh9_5E1Zz2xacaDCKbV_My7eq7Ov2xXxnysOzfAwTGooAHm5lHF2KKWZ-d5Qj4pZ61piN8wU8dmcdUEUPUTT9Q-QM45m8n2IznZLHV4do7mefWmx0ykI-X1My3TLcN6aFicOSawuNr13gjF35IQvR3jYsvmUJSvw8457ao23tfwqcnQq1Ndt9g-AynDu1ZKL57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات شاهد في طريقها الى قواعد الاحتلال الاميركي في المنطقة.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82666" target="_blank">📅 08:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">إطلاق موجة واسعة الان نحو قواعد العدو الأمريكي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82665" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
أبناؤكم الشجعان في القوة البحرية لحرس الثورة، بالإضافة إلى استهداف منشآت وبنية تحتية للجيش الأمريكي المتجاوز في منطقة جفير في البحرين، والتي اشتعلت فيها النيران، قاموا في المرحلة الخامسة من رد الفعل، بضربات صاروخية وطائرات مسيرة استهدفت ودمرت رادار مراقبة جوية بعيدة المدى (FPS) ورادار كشف السفن في سلطنة عمان.
الطريق الوحيد لفتح مضيق هرمز لحركة السفن هو إنهاء تدخلات الجيش الأمريكي المتجاوز في هذا المضيق واحترام سيادة الدول على مياهها الإقليمية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82664" target="_blank">📅 08:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نفديك تهوس كارون</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82663" target="_blank">📅 08:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إطلاق موجة واسعة الان نحو قواعد العدو الأمريكي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82662" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شوش لحد عبادان
َالمحمرة تخلف الشجعان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82661" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82660" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استهداف سفن تجارية مخالفة قبالة سواحل الإمارات</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82659" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82658" target="_blank">📅 08:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdJXnkLho6vwlKVGlaRpmcaO3PtpoDk6cVszlhn5JBXDeVZB2xJ1RTHaTj7Tyu_GTyKzo1FWNnjoYWKfKZfEvJZaTOpFAyCYaQVVjp2RSnSimSZdqTmADN-3ABNWKMbBOONBlFc_DP5oq9SlX7dPjxTwLWagzJdWLI53QjeZ9dpSKJQn540CP-oZiWwsldmuWZRIowpF-u0FwJdHpv8x0cIqpO7j1dN8k0CpAtWOiNmU2etCyUMR3t-gwgIVIYFDEHd0443z09vnAvzL7ZedFY89hw-WN_gU55RHgg4xKs-DLx7X5Lk5Z0q0C3FHOR0krAeL5alZhd5YNDlN_QJjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
اسقاط مسيرة أمريكية في مدينة بندرعباس جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82657" target="_blank">📅 08:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موجة صواريخ جديدة تنطلق من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82656" target="_blank">📅 08:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82655" target="_blank">📅 08:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">موجة صواريخ جديدة تنطلق من إيران نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82654" target="_blank">📅 08:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🇷🇺
قناة
دي دي جيوبولتك المقربة من روسيا :
طيران روسي مخصص لنقل الشخصيات عالية الأهمية هبط قبل قليل برحلة من موسكو الى طهران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82653" target="_blank">📅 08:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  مجاهدي قوة الجوفضاء التابعة للحرس الثوري، في المرحلة الثالثة من عملية "المعاملة بالمثل" وردًا على انتهاكات النظام الأمريكي المستكبر والمتجاوز، قاموا بتدمير مخازن الوقود وأنظمة الدفاع الجوي "باتريوت" في القاعدة الأمريكية في علي سالم بالكويت،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82652" target="_blank">📅 07:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مسؤول عسكري اردني:
أي محاولة للمساس بسيادة البلاد ستواجه بكل حزم.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82651" target="_blank">📅 07:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82650" target="_blank">📅 07:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82649" target="_blank">📅 07:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703c922c.mp4?token=ng_53-njBr2CdfQYyKUHZShwyaATOg9oPJO6lvrMpiI0EFXCfVO4RorYzgDxOjuX0zOxu5W-PaL7I9iiJLPntOGs9XVWwA5C5kexK0pZhGfxm9_T0aLKD4DOi2ADw7_9gynMiLN0A-edMdYuAqxLMD1DKguikt81h4RyPh3QvhkYGn2eUNSdL_VsHwJozfj7jNINKnkg1SZly0TB-K85tLQeLV0k6dAb3TxnCXoJ1Clv2UUTjyaHhTSpp1oT4CIOYcHtAvDdUntjsqoWEiyaWRMiY4o3-S7XAbet8B4uFv1MVDheDoP-Ss7PBYj7kNbyzBivAJu4Iiz5fh9hbths1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703c922c.mp4?token=ng_53-njBr2CdfQYyKUHZShwyaATOg9oPJO6lvrMpiI0EFXCfVO4RorYzgDxOjuX0zOxu5W-PaL7I9iiJLPntOGs9XVWwA5C5kexK0pZhGfxm9_T0aLKD4DOi2ADw7_9gynMiLN0A-edMdYuAqxLMD1DKguikt81h4RyPh3QvhkYGn2eUNSdL_VsHwJozfj7jNINKnkg1SZly0TB-K85tLQeLV0k6dAb3TxnCXoJ1Clv2UUTjyaHhTSpp1oT4CIOYcHtAvDdUntjsqoWEiyaWRMiY4o3-S7XAbet8B4uFv1MVDheDoP-Ss7PBYj7kNbyzBivAJu4Iiz5fh9hbths1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82648" target="_blank">📅 07:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82647" target="_blank">📅 07:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات جديدة في الكويت</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82646" target="_blank">📅 07:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwawJqZWZ9fJRyENTQpgiRbBloWGeQOqRq71FHVRrxFrEAnB0jIYftv4QV16HcR__rzVosKChLXozIggZeQGJHkS7inaznsZWdTBYSh9Z8qbcSNvjzKCQeGyfNbSH8azY9cGRP9S4k86nXTjmoIwVKp2nbV86b02ydA2jRgme99p2GCBCLe_01MJHUixU3luNFpJ-KMNSv9Jsx19p4TGi9vQiwqLhFCydr2u9utgEnv_5ZP8N-Lbjt_M96ipOIXlmlAWGit_8Zxf0e97cKj500QA5VwEE3MwgmTIewEoDQKe0fJ-1pYPRns8yjyis9lBwuEliQrQPEy1EUoYodE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
We will stop any ship not following our order,
Hurmoz from 0 to 30 km under our control</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82645" target="_blank">📅 07:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4f4be296.mp4?token=u7oBUURR6fSQGX3OzyB_K2BOOp6lpGAGIhp6zy60cpI5Dcs0i5xdJFXzH0PqtYHLw8XJmX6jr-DzI47a2qNOQ63tMbKsydNt9WR66kTTmA97Qz0ppKwxmdPn0WZqvGC97w7ippC_g1jXffzf08bsP-HnIpB9yOlCXod5oFp1L_bljjmD0v4H9DvPAszlETvu-X4RGnm3hF7zFWkmdnw2-Jj3H_BwWKs6juYeATg-Q2x0HsxXdS9a6hDIDr0AfMRrB_S9mR4PAQFciQkdz7g2qBbfmGLO9fC80wx35beLtoe2GJwWN2NhjB2EGHtpucvs041s7hEoF4areVOwdKQfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4f4be296.mp4?token=u7oBUURR6fSQGX3OzyB_K2BOOp6lpGAGIhp6zy60cpI5Dcs0i5xdJFXzH0PqtYHLw8XJmX6jr-DzI47a2qNOQ63tMbKsydNt9WR66kTTmA97Qz0ppKwxmdPn0WZqvGC97w7ippC_g1jXffzf08bsP-HnIpB9yOlCXod5oFp1L_bljjmD0v4H9DvPAszlETvu-X4RGnm3hF7zFWkmdnw2-Jj3H_BwWKs6juYeATg-Q2x0HsxXdS9a6hDIDr0AfMRrB_S9mR4PAQFciQkdz7g2qBbfmGLO9fC80wx35beLtoe2GJwWN2NhjB2EGHtpucvs041s7hEoF4areVOwdKQfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سحب الدخان تملأ سماء القواعد والأصول الأمريكية في البحرين بعد إستهدافها وإحراقها من قبل القوة الصاروخية الإيرانية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82644" target="_blank">📅 06:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c1059f20.mp4?token=CfUq4B8ouFiXiOUuainXHsvtcy8xvaitzD22LgtfvZANz-ZSQWaZnr1Nfvum12v8NR3WBD0x0bIZ6g5OiycoLqNpZM-liGF8pBlNeFB3ajfUruUISkXikpRlb3CLaFe2s6Y269MmIztP1qddKRsgDGmfCzlglBm4XK_cz9UEht55I49ldsHf6jG8vshAP1R8i9-yXqN_3F16N1h6pB59IJW9t2i3htg2MP2anjIQ85CcMhGNhBDcGg1VL-EJCNdrLOLJCo5ztPwVRxkVFdvtQLQwknlOeA4gR7rf64JFVFfKGHj_zRIVUN9gZxgEWL2qZ8zxRnaKNGSQmgeYCpHQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c1059f20.mp4?token=CfUq4B8ouFiXiOUuainXHsvtcy8xvaitzD22LgtfvZANz-ZSQWaZnr1Nfvum12v8NR3WBD0x0bIZ6g5OiycoLqNpZM-liGF8pBlNeFB3ajfUruUISkXikpRlb3CLaFe2s6Y269MmIztP1qddKRsgDGmfCzlglBm4XK_cz9UEht55I49ldsHf6jG8vshAP1R8i9-yXqN_3F16N1h6pB59IJW9t2i3htg2MP2anjIQ85CcMhGNhBDcGg1VL-EJCNdrLOLJCo5ztPwVRxkVFdvtQLQwknlOeA4gR7rf64JFVFfKGHj_zRIVUN9gZxgEWL2qZ8zxRnaKNGSQmgeYCpHQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد في سماء البحرين عقب الضربة الصاروخية الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82643" target="_blank">📅 06:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2dde51952.mp4?token=sdxxNRo_xywiBSF0wIeXmoQncz_QAOzUJz1Qf2dFED2EDAR0ytI515HPrSCZC7UgSKOrvoFpOJxpv46l-XE_JIYDWiWt1vrqnMTR9oMERprAnQJfgM3AMVtmutwUliPc8Y6RFSW4z43xQC0HgaSHH-MpHpi_NO0oLRRcwX_T8DWxYNk1L4-b5rmHG76roXb6onXMNmUE6irhR9tBBeC33tdLhNfBfUtOkqdUyaUlZchMg2-lHn-T_8tqU63BdCCXDLGRE6YOJKXNDkOAH9Op-0hgvfgXg5VY2fgkzRbKgJsdYmmk6_yPelCi03eWJVkZrsaURhXi92rdrGPYYbtzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2dde51952.mp4?token=sdxxNRo_xywiBSF0wIeXmoQncz_QAOzUJz1Qf2dFED2EDAR0ytI515HPrSCZC7UgSKOrvoFpOJxpv46l-XE_JIYDWiWt1vrqnMTR9oMERprAnQJfgM3AMVtmutwUliPc8Y6RFSW4z43xQC0HgaSHH-MpHpi_NO0oLRRcwX_T8DWxYNk1L4-b5rmHG76roXb6onXMNmUE6irhR9tBBeC33tdLhNfBfUtOkqdUyaUlZchMg2-lHn-T_8tqU63BdCCXDLGRE6YOJKXNDkOAH9Op-0hgvfgXg5VY2fgkzRbKgJsdYmmk6_yPelCi03eWJVkZrsaURhXi92rdrGPYYbtzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  استهداف مقر إحدى الشركات التجارية الأمريكية في البحرين والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82642" target="_blank">📅 06:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b44a7e1802.mp4?token=cgxE4T7p0dXBQO6nzDJoC1Qh7txOv4eu2TppCKxLcYwrIc5onBYYMO7WkeAKk6o-HirX35PxHTTR1uRSFKzTjGpVFssY2HZjPpuylF2bN1WhqceSpV48ZHj6LWke_C9qZkWYIBabqsMJUlBaHh-z4PZMbzWAWNxvuTFkQbmsuRNs0yaM2BFrQkRKUS4aswdazTKt78TKRFg1CeC9KpFELlfDDJEwbkizdYrCfFvT0_KPI79BF0VttHhIMGl-kuHn2MEfl6wKVzsuTVea3hZ5QuFZhbC-j-c2zdba-x6EJGurft35m3lrTmB91V8OQPn914SKwrWUJKHCLPU8nVf5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b44a7e1802.mp4?token=cgxE4T7p0dXBQO6nzDJoC1Qh7txOv4eu2TppCKxLcYwrIc5onBYYMO7WkeAKk6o-HirX35PxHTTR1uRSFKzTjGpVFssY2HZjPpuylF2bN1WhqceSpV48ZHj6LWke_C9qZkWYIBabqsMJUlBaHh-z4PZMbzWAWNxvuTFkQbmsuRNs0yaM2BFrQkRKUS4aswdazTKt78TKRFg1CeC9KpFELlfDDJEwbkizdYrCfFvT0_KPI79BF0VttHhIMGl-kuHn2MEfl6wKVzsuTVea3hZ5QuFZhbC-j-c2zdba-x6EJGurft35m3lrTmB91V8OQPn914SKwrWUJKHCLPU8nVf5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82641" target="_blank">📅 06:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وصلت الصواريخ وانفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82640" target="_blank">📅 06:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82639" target="_blank">📅 06:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رشقة صاروخية تنطلق الان نحو القواعد الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/82638" target="_blank">📅 06:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على هذه الاعتداءات، قام مجاهدو  الجوفضاء التابعون للحرس الثوري بتدمير مراكز مهمة لإصلاح وصيانة المروحيات، ومنصة طائرات الاستطلاع الإلكترونية من طراز P-8، ومركز قيادة وتحكم الطائرات بدون طيار التابع للجيش الأمريكي القاتل للأطفال، في قاعدة…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82637" target="_blank">📅 06:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
الجيش الأمريكي:
فلوريدا - أكملت القيادة المركزية الأمريكية (سنتكوم) موجة جديدة من الضربات الهجومية ضد إيران في 12 يوليو/تموز، حيث استهدفت عشرات المواقع في مناطق متعددة بذخائر دقيقة بهدف تقويض قدرة إيران على مواصلة مهاجمة الملاحة الدولية العابرة لمضيق هرمز.
وضربت قوات سنتكوم، ولأول مرة، أنظمة الدفاع الجوي العسكرية الإيرانية، ومواقع الرادار الساحلية، وقدرات الصواريخ والطائرات المسيّرة، والزوارق الصغيرة، مستخدمةً طائرات مقاتلة أمريكية، وسفنًا حربية، وطائرات مسيّرة هجومية جوية وبحرية أحادية الاتجاه.
ويُعدّ مضيق هرمز ممرًا بحريًا حيويًا للتجارة العالمية، وإيران لا تسيطر عليه.
وتتمتع القوات الأمريكية باستعداد تام لضمان استمرار حرية الملاحة أمام السفن التجارية، على الرغم من استمرار العدوان الإيراني غير المبرر، والمضايقات، والتهديدات، والتصريحات التعسفية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82636" target="_blank">📅 06:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5-xotnFzop4VLOWj8O1fljJCqVO7ei3outlPjAcom2NJmCu_lpZUxV4GiaPbrMtSLOKqYr6WYFzvXa0d5E-IxshtCsufYxXilksALWGqfC3JY9z2_5Ck1d83cCHOWvVa5c23ln8bdi60_RJCaCUOG-HfpRAlF4WNslnVBIFxeAvphQEq4VgI67xS-_g3B27NKjr0Yyd0mu4iFVc35FTyiSAnRUu6CKbSVrk205mxgS8fxOaAES3uT-RiWIquiB61yWQvG6Czwv4nEUzyj7SPJzcLKcWb7h4wDA5tRLp2Hgf2LphwmonT_Kt9j4fq4YC6hIgbm4CqNqDyJG8Jc5IWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
عقب تبادل الهجمات بين إيران والولايات المتحدة..
أسعار النفط العالمية تلامس 80 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82635" target="_blank">📅 06:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  بسم الله قاصم الجبارين وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ کله
🔺
في الليلة الماضية، وبعد عملية قامت بها القوة البحرية لحرس الثورة الإسلامية لإيقاف سفينتين متورطتين، اللتين أطفأتا أنظمتهما وتحركتا في مسار غير قانوني،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82634" target="_blank">📅 06:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوي انفجار في بندر عباس جنوبي إيران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82633" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
بسم الله قاصم الجبارين
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ کله
🔺
في الليلة الماضية، وبعد عملية قامت بها القوة البحرية لحرس الثورة الإسلامية لإيقاف سفينتين متورطتين، اللتين أطفأتا أنظمتهما وتحركتا في مسار غير قانوني، مما عرّض الملاحة في مضيق هرمز للخطر، كشفت القوات الأمريكية "التي تقتل الأطفال" مرة أخرى عن طبيعتها الوحشية من خلال التعدي على القواعد الساحلية التابعة للقوات المسلحة في الجمهورية الإسلامية الإيرانية.
🔺
في المرحلة الأولى من الرد على هذه التعديات، أضرم مقاتلو الإسلام الشجعان النيران في عدة مخازن كبيرة للصواريخ ومخازن الوقود في القاعدة الجوية "الأمير حسن" في الأردن، وذلك عن طريق إطلاق الصواريخ والطائرات المسيرة.
🔺
تستمر عمليات الرد بالمثل التي يقوم بها مقاتلو الإسلام، وسيتم إطلاعكم على نتائجها في البيانات اللاحقة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/82632" target="_blank">📅 05:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e8cbafb1a.mp4?token=OEbPzI8cR8ZjXof7_kTB39dXTNn3yW3fqUN90VwMLRb1RKeYEY9f-sD6FGPZs2Ato11zWos6I2zq638_dYFon_qAmuaJoAiXVHrFJtZAdlDsEHulRPgkEDLBRmh4NXPH3USBVylANsnnmG_4iAJO8RKvP-vN4Cn8prQLaJkpzbb1VEQAcoz4rzyjPaiTL9ipiqc8UNZcdtaOpm96CFHBcavq5XHbQuZDoVluMHGaOyBBPjN6Gu7NMViuIkBBqJuoYYHoe1uS3sauDNzBsllrOvVYtnGNejPrRNxtW9fSKYbyrMhgWEiELgCilZd8_nvoKKkuvcsQpRfyHOKkEB4rGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e8cbafb1a.mp4?token=OEbPzI8cR8ZjXof7_kTB39dXTNn3yW3fqUN90VwMLRb1RKeYEY9f-sD6FGPZs2Ato11zWos6I2zq638_dYFon_qAmuaJoAiXVHrFJtZAdlDsEHulRPgkEDLBRmh4NXPH3USBVylANsnnmG_4iAJO8RKvP-vN4Cn8prQLaJkpzbb1VEQAcoz4rzyjPaiTL9ipiqc8UNZcdtaOpm96CFHBcavq5XHbQuZDoVluMHGaOyBBPjN6Gu7NMViuIkBBqJuoYYHoe1uS3sauDNzBsllrOvVYtnGNejPrRNxtW9fSKYbyrMhgWEiELgCilZd8_nvoKKkuvcsQpRfyHOKkEB4rGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النيران تشتعل داخل مقر الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82631" target="_blank">📅 05:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">النيران تشتعل داخل مقر الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82630" target="_blank">📅 05:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zl4_cx_TDh5RcJ7hC2WbQOoLfZfA7BVvJ9-EBiZh8jcxbc0RFbJlXWKANAFnScekCNlzYQ-UhGJTxuMPOgnw0diajekqwYwx9GloU_lGpiZNI0_jiuwMSFxo9GhvzwzOWiO4pIYKKwnbeJuthM4qpuP3l1Z53etlmDzJRrXwiJnpA-r0-H8PRiRNqDjn89oVrK1PGl-ZNrtmG-l7ctHxSdNzXxdNTn6Y7UBQCxC2q16bOm4UshreW_KFcLen_T4AZxoS4S78BcNCBCH5sS-4xlNBT1fyYb2ffMmoULLZNJ-4gxNjVvNEK2jFJECVtSoc1mDlEPB2B5v_5haboVE53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82629" target="_blank">📅 05:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b1b68cef9.mp4?token=X7jjnK07vZWghCHZMIRdoQ8CbautGdgtCYa3d-2ZtDw-2He3OXeAMCEtbxkWV328nr144xDeCWAYfblxk1PjB24c3pqvh6NTJ7XUy8qnLwZBsMBcpCg6f9hgsV8Hz0ZTQsOD1WjcLl50FgR0KrTrClgLIGPd9Egci1q4CMPNnTACz9Zc0_r7X-5oi96HlPlYlwadWNJ8_Tm_f3Fg1FfL4Qo52qPYGNQB9v6tKM6ZQ3PYG60BGRvSU_xY42BCIh3eapTdzGu0aFatc85xSt2Zlg-5qn8_dCp4qkfd3N8e8_1v5wqRa-WS84VyWphx15D6WMuphD9NxZ9FFtnNKawsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b1b68cef9.mp4?token=X7jjnK07vZWghCHZMIRdoQ8CbautGdgtCYa3d-2ZtDw-2He3OXeAMCEtbxkWV328nr144xDeCWAYfblxk1PjB24c3pqvh6NTJ7XUy8qnLwZBsMBcpCg6f9hgsV8Hz0ZTQsOD1WjcLl50FgR0KrTrClgLIGPd9Egci1q4CMPNnTACz9Zc0_r7X-5oi96HlPlYlwadWNJ8_Tm_f3Fg1FfL4Qo52qPYGNQB9v6tKM6ZQ3PYG60BGRvSU_xY42BCIh3eapTdzGu0aFatc85xSt2Zlg-5qn8_dCp4qkfd3N8e8_1v5wqRa-WS84VyWphx15D6WMuphD9NxZ9FFtnNKawsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية كبيرة تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82628" target="_blank">📅 05:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umHlKzfzqrcOkxdosNKqT7YH_L1_3H-0mKA2aXPC-0MUCXJ_kTjWTYHl5x07pZQX7eyGXlWcPzy-9ldFdfCC55SYfds4OXW0KiN6N33n5e3CQglQooSrSH5pFCjMc5oHSsCOQIMgKC7gEMuSPhfPUqoqkbm7GoLz6uBtkEWwW3Fjxgz640CAIQGxXzbmdpvlFvgi7POYO5wPy0Y5g_wmA5yUuwRXv3H2oWRBEugSMMY2CtYa37sWPlJLcMpHR0du5e_QEtZdPqY0_BmwgFAWwc0aLWUJUvkcvgeWjY2IDSLgtkTQyOAFjWfP_CnLxx8XETcyV3kfSP4WWl-JT_aqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozW7TiTYrGFdnR3dmdR0hmyNwRE-D4wSPCXxPqmdtzZH0PwqGlDs72mQI-2GvZZb0z8VhJlRQEuuBaeilm7b395mU-v15D8LC3F_z4nGriHK7g5ttHtn2R_Pw3uqsK6b119Mp7nTQtoIW_QrIm_GQ6M8ES6sJ3SuR75-gFvva9CSCSoKhshEHnwuuv5EV0iIyhDXsLR8aDTJ1uYd_rz-XMFZNni0U7BoepoPpgAy0oAsdqcisBCuSCDRbWimsWshvvhZVrOLmYzbUSlkPo_SztEc6OyeXFLcDZRxUiGUgjbSa7olbpBeY10zo79k0hzp6K0yTIyn9SeaDssqVRTFvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f265dd887.mp4?token=YCsFYyjGXAmLarXBDQJBtJhKsBr4fu4ArCgljG0fnyTbEbU2clgOWpBgYswLlHML0qXZT-HPOlZtPmILPzt6c8i3sTUtEMuTH9eWwzoRLLUhNmWqfQrUFxl100WGZdBNdnOzuNn6U-h8sd0PcT8ntG6HfZZBI5L5ClWfRKXebf6wpuUAI27y811czMwKoEVrNCcmNa-b_ke5mRvhlOUI3pjqXoCTgaijoBaqxGKAy6d0VdXLnTVkNCRnuZJR-JcXa-gGgcMcHBvOazu7zzeM2brIUl4lXDCwIJ6QzLCjx9YdruFPt5rIEVRuR3Q88MM4iylnW3WXbQMLnrpcsvt6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f265dd887.mp4?token=YCsFYyjGXAmLarXBDQJBtJhKsBr4fu4ArCgljG0fnyTbEbU2clgOWpBgYswLlHML0qXZT-HPOlZtPmILPzt6c8i3sTUtEMuTH9eWwzoRLLUhNmWqfQrUFxl100WGZdBNdnOzuNn6U-h8sd0PcT8ntG6HfZZBI5L5ClWfRKXebf6wpuUAI27y811czMwKoEVrNCcmNa-b_ke5mRvhlOUI3pjqXoCTgaijoBaqxGKAy6d0VdXLnTVkNCRnuZJR-JcXa-gGgcMcHBvOazu7zzeM2brIUl4lXDCwIJ6QzLCjx9YdruFPt5rIEVRuR3Q88MM4iylnW3WXbQMLnrpcsvt6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات جديدة تنطلق</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82625" target="_blank">📅 05:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موجات جديدة تنطلق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82624" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82623" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نفس نیروهای آمریکایی در منطقه را خواهیم برید</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82622" target="_blank">📅 05:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82621" target="_blank">📅 05:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هجوم صاروخي على البحرين وصافرات الإنذار تدوي</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82620" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات عنيفة تهز الأردن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82619" target="_blank">📅 04:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pmy_zqMOqsUKZB4bYpDoocBC08wy3ld08EboUEsfSJlPcZDJguqgl92SDzxCVJfRnBMxXYmchEnvkTeWnaVZ3ivYYXCQToCjfL7xnYiYkVgTPFczpC1GcolXgvoowJRk2mypigwOOxNI2CH_683fq1fxHGponw_7k-kAaa5t6E7Lz4Mk6bLaJDqJUFiU9IXHWVrxvouXI9p4nsDU7cobrJj3VW8fO82tsMsXYMOYADWFkv8-xKe48OCE0L0xdLmp-491uaFQ2LPs-QGqI3m3prEL6cZpOMwZ3bi9VnqRkzzENQB3lW4p1X7uS5kdg_RIQSu8I8u1SY_B7rRmwnSuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApN5W7J8LiwPMlOkcb7m9TJ_LqnBx16IkIPL2lw-W6B-B6Jr8zDl2JZ4_EbnCrQMTd7iFnMEIbReamIs2jZ4Gam3LJJP5ABhZimWBH6erRIxV4Ahu5ZPJnDux4AtrxnVL-7fdjK060kN6g1lB2FmAhjgfGC014027G4rBVu10SyeJ9VDTXMq5HZ5_i4SkH34ySAadDdDUZETmj0L27DihRG949plAaOc_ti0yE-ldO2a7kAd9XaHIrCJgZMw2TWNad3EpjvEH170koHFZgphOao74OgYnjZSP756GmcPuo3o3yox9HCQ5QiwIcObbav0xbLsI5nDbMxI6QA1AhtIrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رشقة صاروخية كبيرة تنطلق نحو الاهداف المعادية في المنطقة</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/82617" target="_blank">📅 04:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfkguwaur_u9hKz6isdx0W3DNzwZoUmoR4kZdjlkQM881v5WQzXa9JLfua0yaeY7J6E1AjLzbcxPO62mF3QNcGGfLHyMyzkNiSupgfDOQLDh5PSYRM9XwnhzNQbx5NPG_KEmPRGMHO5AHWQe_hicsSxd4eMY5zZQeLBOQiPgS9lXbST-YE_W6uvEuSnpzBzT-rneyRygJcnCqBLpE8uuxzdqI7S8vHfGXPaha2nvabKhvBMbxTXFaP8yROEIkBoAYkWmZ4r9k_wimpB-nDC2fWc1EOTHUw58wYfAsckgElrlnlWYAtIQhP7XVKmf5EXEY5LJ03vT-R3ye5n_cdG2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر  موجة صاروخية جديدة تنطلق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82616" target="_blank">📅 04:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPpfELdcC_iPXfGCdZIG9C0C77KjFFXJYDMwzgpzRINdBtPxcWQHvKsdwmqSkO86-uOhGb-lo61mV8JRC49ZxX6ZPgmZpw-wMbp9zMOqCbQKDCcwB95qD6RC6Obo5bL7iqSR2PpXjcPwG3GB8rE0Ac-BER45nTDaCzbDmDryeYistnHl8Ela17Pu1CzpHzBEEs4K9IncYCGRiG5ZA0VJU2g4YNLq-EPwUw-5XY7Lr5ejdlGU_s2t9K8MiZlh1yOMHjHDGdDKLpVGOG9xDRwHxiTGnXNVOCr_rs_dwUFzkATwV1GkutFsihWLKrL8824i9nPJHRgEAKrIohP7kYEZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
موجة صاروخية جديدة تنطلق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82615" target="_blank">📅 04:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">إطلاق موجة صاروخية من إيران نحو الأهداف المعادية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82614" target="_blank">📅 04:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2I-Q9BN_AU9W-aGKvtUikBa6wNhj_O5xl4pQBpC2bKPvlnbx6HkKQE-NVWul9gExvnzvbOx6QBt0wVHO9Swj5hKLSww1v-EdJVjRXATT0Dgn9u-HACotjYOatVk-KFLbqpwathS2f_5PIR6IiLS1eBFQrk-cGVV3MpRxsF9v02GQsKlkRisrcJIktMmL8klC6vpJRdpRRG_q7O8wW3qHuN0HjEoKCAHqotq8kJGWrZum0TIBarhUptT14beM1NyAN10CD4Kr_lRyI_fgOvINMWmvKHtvx9i2bMzt9XJZbp5hM-FReACkgRuQFLc_J_IYq2gGmXWEzrsHYEQkBKMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يَا ذَا اَلْبَطْشِ اَلشَّدِيدِ...</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82613" target="_blank">📅 04:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">يَا ذَا اَلْبَطْشِ اَلشَّدِيدِ...</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82612" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول أمريكي:
الضربات الأمريكية ضد إيران لم تنته بعد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82611" target="_blank">📅 04:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82610" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
مصدر إيراني:
عودة الهدوء إلى محافظة خوزستان في جنوب إيران بعد عدة هجمات أمريكية طالت عدد من المدن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82609" target="_blank">📅 03:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مصدر إيراني لنايا:
الأنباء التي تتحدث عن انقطاع التيار الكهربائي في جميع أنحاء الأهواز غير صحيحة وكاذبة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82608" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82607">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة تنفيذ العدوان على مدينة الأهواز الإيرانية</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/82607" target="_blank">📅 02:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82606">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عدوان على مدينة انديمشك بمحافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82606" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد إطلاق صواريخ من الأراضي الكويتية نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82603" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات في مدينة اميدية ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82602" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
