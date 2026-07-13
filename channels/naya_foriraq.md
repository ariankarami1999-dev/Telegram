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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-82771">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocxAXHhNniTJHgsFIv9V1WzR2uZSHmZH4dIMf-rg7r7Zo_xPKc1TJlvrfZc7EKNk5ECucUxtnEXlEDt8gpkSk5t84uTvSglkWnI_w1EN9jVkcpOn35nAvgUCf0sL7_dgzgT-fnP95_14F57qiNmqyGA5yfqGcX_bp4ozuoa2GVV-DD_NAaiZjhn9rXfA5-M4CeyY60E8-x54BJ5-JQK1OxCUX1TmnpWrDAa8GrUjDlr6OP_6w2egPntv71TR2u-QhvD5EyzPVciUg1_M4jXj_9ytMjZjzJKZTG5aAaFgNQqolPnoCRVo4oObJU0G8SrcZXx5ULkK-8AzzEc4IiWekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
عضو حركة أنصار الله في اليمن: لقد فتحوا على أنفسهم أبواب جهنم والله استرجهم إلى مهالكهم.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/naya_foriraq/82771" target="_blank">📅 20:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82770">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي في حركة أنصار الله:  صنعاء لم تبادر لفرض تنفيذ اتفاق العام 2022 لأن أولويتها كانت وقف العدوان على الفلسطينيين في غزة  المعطيات بعد عمليات إسناد الفلسطينيين أثبتت قدرة صنعاء على فرض الحصار على من يحاصرها</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/82770" target="_blank">📅 19:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي في حركة أنصار الله:
صنعاء لم تبادر لفرض تنفيذ اتفاق العام 2022 لأن أولويتها كانت وقف العدوان على الفلسطينيين في غزة
المعطيات بعد عمليات إسناد الفلسطينيين أثبتت قدرة صنعاء على فرض الحصار على من يحاصرها</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/naya_foriraq/82769" target="_blank">📅 19:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
‏المنظمة البحرية الدولية: نعارض فرض رسوم على عبور أي مضيق يستخدم للملاحة الدولية</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/82768" target="_blank">📅 19:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
حكومة إقليم كردستان: إلقاء القبض على متهمين بالفساد وتسليمهم إلى بغداد ومصادرة 358 كيلوغراماً من الذهب</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/naya_foriraq/82767" target="_blank">📅 19:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامب: إعادة فرض الحصار على إيران.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/82766" target="_blank">📅 19:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇸🇾
في سوريا وتحت حكم الإرهاب الذي يقوده الجولاني حتى قوانين الرياضة تغيرت حيث أصبح لديهم قانون: إذا لم تعجبك صافرة الحكم... اضرب صاحب الصافرة ؛ مشاهد من الدوري السوري الممتاز يتلخص باعتداء لاعبي نادي النبك على حكم المباراة بسبب انزعاجه من الإجراء المتخذ.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82765" target="_blank">📅 18:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الشرطة البريطانية تلقي القبض على 12 شخصا بحدث مرتبط بتهديد محتمل استهدف فعالية إسلامية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82764" target="_blank">📅 18:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82763">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82763" target="_blank">📅 18:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82762">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgnjTJMOPMY3GHxk1dufTonFEumuknjJIZ4GACscCJ9wqN2crshh-yIQCPk1x0sJlK2vyJ8sgwBqhz6LbbzsaS14VlP6hZ1ZlOSYQWqzyjL5cnUAAEjyVOvcG65uhxh2vbUhX_2dAf4JKg1qvfjjisUJPmcdeJ87sbfHKBwdIgi0Gne8c5bV6wadpxk-X4c6Mp7LkHyQGklDhPsgz6ZfapD8zSykWjxH8Z42F2EAkUmoABQ2bACoBwrcOWQhIx01hWZu3hDZ_RQ0ooNRxErP3R32s8Z7XMuOojSlWOoG5gyGxjgl3ZSHqQmzDIwhthPHaUnuHPdmwgTx5hzCnNrMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع أسعار النفط بنحو 5% بعد اعلان ترامب استئناف حصار مضيق هرمز</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82762" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82761">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLvgIjz46c04SbfNW-Uuh_lbM0MGpkDtCP2IZnm85jbT7-5NQ2VXOfRCHrbdWdzNUhJlMBIWDz6ZBkei7N-U7Iu8i0g7oA3Yfb68n9-baDsa1Gu5iNwHeEsKEcpsoyyWVBMBjxYljADXpWj3PPQzj6Dvh-Ur4RHLQxWU4j3L3MdRCZN_c-VWnUsmlr0kFH7GX_ciapLcOTiOBndx_e0daEtpeJMFU5DW7pJY0hwnW4lAWeuD0kDkCUU1CigUV6VWiCBa7nnPrW95-aYCQK1m8-heAzHtZZ5Y0AUn6B3QFiSMTIXWTuBW45B7ilXjRSnQf-6WuvolDalcsftOzJx2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: إعادة فرض الحصار على إيران.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82761" target="_blank">📅 17:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82760">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب: إعادة فرض الحصار على إيران.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/82760" target="_blank">📅 17:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82759">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇨🇺
🇺🇸
‏الولايات المتحدة تفرض عقوبات على وزارة السياحة الكوبية وكيانات أخرى.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82759" target="_blank">📅 17:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82758">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكية ‏روبيو:
تسعى المحكمة الجنائية الدولية إلى أن تصبح الحكم غير الخاضع للمساءلة في قانون عالمي جديد، مخوّلة بمحاكمة واعتقال مواطنينا كيفما تشاء، وتهديد السيادة الأمريكية تهديداً وجودياً. سنلقّن المحكمة الجنائية الدولية المعنى الحقيقي للعزيمة الأمريكية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/82758" target="_blank">📅 17:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82757">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
عضو المجلس السياسي الأعلى
لانصار الله
محمد علي الحوثي:
‏نحمل امريكا ووكيلها السعودي مسؤولية العدوان والحصار بتصعيدها بالقصف الجوي على الاعيان المدنية (مطار صنعاء) بعد فترة من خفظ التصعيد ونعتبر ذلك تجاوزا وانتهاك مباشرا للقانون الانساني واستمرارا في ارتكاب جرائم الحرب اليومية باستمرار الحصار والتجويع للشعب اليمني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/82757" target="_blank">📅 17:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82756">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئيس الوزراء العراقي يصل واشنطن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82756" target="_blank">📅 17:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82755">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇷🇺
بوتين:
الرد الروسي على هجمات العدو سيكون مماثلا وأكثر قوة بمرات.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82755" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82754">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله علي القحوم:
الرد على استهداف مطار صنعاء سيكون قوياً ومزلزلاً، ردنا لن يتأخر ومعادلة كسر الحصار مستمرة مهما كان والأعداء سيتحملون المسؤولية الكاملة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82754" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏المرتزقة التابعين للسعودية يصدرون تعميماً يقضي بإغلاق جميع المطارات أمام الحركة الجوية حتى إشعار آخر خوفا من رد انصار الله</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82753" target="_blank">📅 16:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الشرطة البريطانية تلقي القبض على 12 شخصا بحدث مرتبط بتهديد محتمل استهدف فعالية إسلامية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82752" target="_blank">📅 16:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏رئيس المرتزقة التابع للسعودية يدعو قيادات المرتزقة لاجتماع طارئ لمراجعة التطورات الأخيرة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/82751" target="_blank">📅 16:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عضو الوفد الوطني المفاوض لانصار الله عبدالملك العجري:
نعبّر عن امتناننا وتقديرنا للخطوة الشجاعة والإنسانية للجمهورية الإسلامية في إيران لقيامها بإعادة العالقين اليمنيين من جرحى ومرضى</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82750" target="_blank">📅 16:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
المبعوث الأممي إلى اليمن:
نحضّ كل الأطراف على خفض التصعيد وندعو إلى الانخراط في الحوار والمفاوضات برعاية أممية
اذا هاي عود خابرني عاليوتيوب</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82749" target="_blank">📅 16:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">المتحدث باسم مقر خاتم الأنبياء: نحذر قادة دول المنطقة من أن أي تعاون أو دعم لوجستي للجيش الأمريكي سيُعتبر بمثابة حرب ضد سيادة وأمن إيران.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82748" target="_blank">📅 16:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">المتحدث باسم مقر خاتم الأنبياء: ستتعامل إيران بحزم مع أي محاولة لإحداث اضطراب أو زعزعة الأمن في حركة السفن التجارية وناقلات النفط، سواء من قبل الجيش الأمريكي خارج المسارات المحددة من قبل إيران، أو بدون إذن من القوات المسلحة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82747" target="_blank">📅 16:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
المتحدث باسم مقر خاتم الأنبياء: لن نسمح لأمريكا بالتدخل في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82746" target="_blank">📅 16:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff97123423.mp4?token=ZWiHnMlQZwpvUa660gyPXWjh4wp_mCF4gHawWhxjrggvDnNHhcsy40lNcjMXLcC9eO-r-74D7X1ptFiuOBsNJtQ62LpgAnkaREzNQ9T4B0VtbWrDVXhf9xLW0yJQmQeQJW6wS39SyZOiRlQ3DDkiHlUeP-1wZ7HpsNx1kY9Gg45JHCr5MSgnGXjKV8RAPSKRAaFm3CV5sekofbUNpPS1Y3t6_05ZYpuZ80T7RaEEquNXDq4ZV9b-q7z4bHbsCCYzkaCrtde7dp02ZWck8-BA28dDBQMGvPYDVx9ROIl962wHhnG1G46vZ4G7baSnWxGe4v00KG-9s-eBaLLbFBbV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff97123423.mp4?token=ZWiHnMlQZwpvUa660gyPXWjh4wp_mCF4gHawWhxjrggvDnNHhcsy40lNcjMXLcC9eO-r-74D7X1ptFiuOBsNJtQ62LpgAnkaREzNQ9T4B0VtbWrDVXhf9xLW0yJQmQeQJW6wS39SyZOiRlQ3DDkiHlUeP-1wZ7HpsNx1kY9Gg45JHCr5MSgnGXjKV8RAPSKRAaFm3CV5sekofbUNpPS1Y3t6_05ZYpuZ80T7RaEEquNXDq4ZV9b-q7z4bHbsCCYzkaCrtde7dp02ZWck8-BA28dDBQMGvPYDVx9ROIl962wHhnG1G46vZ4G7baSnWxGe4v00KG-9s-eBaLLbFBbV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المتحدث باسم مقر خاتم الأنبياء:
لن نسمح لأمريكا بالتدخل في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82745" target="_blank">📅 16:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82742">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LS-asx2yF3jlVeSQCL5uzC1Mh-WvmvKVECINsA74tQgIboa13cAWhmpnFks1AjH_GZZkaUgcWouXB_vxMIRaXX6Z2cih7Hjr19GboOr0F-__UnlH0WfjBi7-ZQAVL-l-kTtpUWQxAl8PxkEGgq3Gu89JsDmsLGheJnuKjaS-yIkEougmKc0URnF4xsIBQbf4l6stXTJkcHQlVesL2C2JRpUrlQIl-YWvEi9lArSDz3DMwSTsJT-VqHSsbnAzYl9Cho73EFFS0V3SsI0po1LM-mpgLpOl6t-Zoo1d9hq-fHux4ySkohVW2mLLrgXArbQtd-zkf17osA-sJ5U_sltg_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HXMSyz-fIxWmlfN_i4bracNCiDHwKDvmNOgcWlWUCHqXktoaHp3A3BXapwQv9t9NeDn4cUGY2wP9AjlssyYjZWcB8WP0KcD3gVH_xmTKLbD_OIf0dxp32trz5ZQR0jHbTaUXnC7SpdrFoKkanE7mb4TSJgH2_3DbwSCtLMEQL5LSmbjPXr41vEcQtXYNesUPr9O_ghlOdNjg4d8-AT58Xn0ZoNLY0whCxVrmcLQrSakOlc7pEsYPc8IAY3zr3ErAuQYjPjfP3rB3KVKXM9WqiEPejGYZUyi97l0iv4HP5F44XMU-Jz-ZZkbUXsgzekflOjKoYeHlxTLkEKnruB4j4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ4JWB3Oj_AADxsYvAPo7gbVA9GVrfQQRSrSWP92c6eZQA2VF_WwAp7vsYyCKB6mkgoi_toeI9hiYTO7tuE_a4mV4Z6ekEhnNlaS8eUw1xMY4S_FiOYpx0F2CqYwk38aBDF1MIsa_DReR5KZ8yQ0pvlwIcOXokVWyEb9ecNsXbC027h0FQ4chPv58ThBTXZdAWpmGhLbBTMQbysDMYnlIwl_cZBWBrWEpslmF_3e1X8SWfwnQ2brla1eXIhfTDK_c5iyaXwSiY6nWku5rZVc8SMY02_5dHWQrkKkL3Y5v1a_0sF70yOL-SVVZQSmSUqMM6VWjxnFm7R2zRH19AmKyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقرير هام وحصري  خاص لنايا يظهر توقف مئات السفن التجارية في مضيق هرمز بسبب الحصار الإيراني البحري وعجز الولايات المتحدة عن فتح الحصار علما ان اللقطات تم التقاطها الساعة واحدة بتوقيت طهران اليوم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/82742" target="_blank">📅 16:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82741">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1092166d6e.mp4?token=iJoLZOsLDtNlJSyt-bV7PqMBQFLqF5AD6HF863Xevyi7crK2vcW9cVPZbIxJA8J1sZM8SiOv9IkArNJmz-_e5ws_ODFhfLcnoLMaf9eaTVnv6ryT35_Rxl4D6WDbm0kbUmOilhUQjN_X9prJCfGbhYWfGOpX_NdNNikEES9TKTn3mTnuoQIbUxQO6PbouEhIQRJERb9BpyF6QZYwqSQAyECSae7NhzVX1bSG80uzRdcwaktXhPVD0294iz17PohGi6jcyx32UDGSWUjvnESvqI-2Hq7JjzXphgEWH1uXSqM3c_g3LhzC08D9ohTZiUX0CzSQcPJJBqWf22FE-kYnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1092166d6e.mp4?token=iJoLZOsLDtNlJSyt-bV7PqMBQFLqF5AD6HF863Xevyi7crK2vcW9cVPZbIxJA8J1sZM8SiOv9IkArNJmz-_e5ws_ODFhfLcnoLMaf9eaTVnv6ryT35_Rxl4D6WDbm0kbUmOilhUQjN_X9prJCfGbhYWfGOpX_NdNNikEES9TKTn3mTnuoQIbUxQO6PbouEhIQRJERb9BpyF6QZYwqSQAyECSae7NhzVX1bSG80uzRdcwaktXhPVD0294iz17PohGi6jcyx32UDGSWUjvnESvqI-2Hq7JjzXphgEWH1uXSqM3c_g3LhzC08D9ohTZiUX0CzSQcPJJBqWf22FE-kYnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقرير هام وحصري  خاص لنايا يظهر توقف مئات السفن التجارية في مضيق هرمز بسبب الحصار الإيراني البحري وعجز الولايات المتحدة عن فتح الحصار علما ان اللقطات تم التقاطها الساعة واحدة بتوقيت طهران اليوم</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/82741" target="_blank">📅 16:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82740">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇶🇦
قطر تقرر تخفيض سعر البيع الرسمي للنفط الخام بانخفاض قدره 5 دولارات للبرميل في محاولة لجذب المشترين بعد الازمة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82740" target="_blank">📅 16:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82739">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تقرير هام وحصري
خاص لنايا يظهر توقف مئات السفن التجارية في مضيق هرمز بسبب الحصار الإيراني البحري وعجز الولايات المتحدة عن فتح الحصار علما ان اللقطات تم التقاطها الساعة واحدة بتوقيت طهران اليوم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82739" target="_blank">📅 16:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82738">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/528d1edefe.mp4?token=HFtCdlWWDh1stRiz9RQc3xaemJjXkZRoU-8g2Z85-4X28sZmD58FMuNi72uwGzdMTRl0XfpsY5IPVTvAQgZU2x1lkKAcKD2qg03jux3y5yyfMXhzj3yoRXioLJkmsM-OrHwAIZr7nff0j6KT1DFXTF2pIvaXtkkXlprJY5Hc7pj5Y5gPE7fCbV2W47pRIF8SDTC3A_hofnK9U3QLyUens46UDG2JThYhr_0iv1JMw0tJEF2j3A12csNC3vqREakqFBo0iZ_Z2uIApJwWOK72Ks5P5N6lPE3-OVpOPPzaSdP0vTp2Jp1iqi3D_QHv0mwuVRZKSiAafFREdI8DcjPcuUx2yptUfche0mvP307MO7hGmW50Z6BOc2S1qnUPqqFzw_yOowxp2mmTRlZLFMxN317g-v09goWrngVPvxb0Hm4WAaXM3xbZJvB023V0epcWocUDxuLThtZaHbbwDxC39WSk5XCKAbtnF9E_Ky8Tui995Jmv3CIg53Jl9kRHjtTFhpITj74VqWyt7kVGbM6PjCVan-aWOdWzvCq-kanU1O0dKCquBL-84pKPd1cEf9RKCz2I0XmvXi_fJspRb7ZB-vEzAkoEA8byA8EpF8Ri-FcoABY2XbthsZ6u1W1ZHkPnC8VUsI36ZclB7imeGFdEMuUYHldC-OxT8OQPuULl0-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/528d1edefe.mp4?token=HFtCdlWWDh1stRiz9RQc3xaemJjXkZRoU-8g2Z85-4X28sZmD58FMuNi72uwGzdMTRl0XfpsY5IPVTvAQgZU2x1lkKAcKD2qg03jux3y5yyfMXhzj3yoRXioLJkmsM-OrHwAIZr7nff0j6KT1DFXTF2pIvaXtkkXlprJY5Hc7pj5Y5gPE7fCbV2W47pRIF8SDTC3A_hofnK9U3QLyUens46UDG2JThYhr_0iv1JMw0tJEF2j3A12csNC3vqREakqFBo0iZ_Z2uIApJwWOK72Ks5P5N6lPE3-OVpOPPzaSdP0vTp2Jp1iqi3D_QHv0mwuVRZKSiAafFREdI8DcjPcuUx2yptUfche0mvP307MO7hGmW50Z6BOc2S1qnUPqqFzw_yOowxp2mmTRlZLFMxN317g-v09goWrngVPvxb0Hm4WAaXM3xbZJvB023V0epcWocUDxuLThtZaHbbwDxC39WSk5XCKAbtnF9E_Ky8Tui995Jmv3CIg53Jl9kRHjtTFhpITj74VqWyt7kVGbM6PjCVan-aWOdWzvCq-kanU1O0dKCquBL-84pKPd1cEf9RKCz2I0XmvXi_fJspRb7ZB-vEzAkoEA8byA8EpF8Ri-FcoABY2XbthsZ6u1W1ZHkPnC8VUsI36ZclB7imeGFdEMuUYHldC-OxT8OQPuULl0-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لا يمكن أن تتوقع منا الدول أن نقوم بحراسة مضيق هرمز مجانا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82738" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82737">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دويلة الكويت: الفصائل العراقية استهدفت عدداً من المراكز الحدودية ومنصة حفر بحرية تابعة لشركة نفط الكويت، مما أسفر عن وقوع إصابات بشرية وخسائر مادية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82737" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82736">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🗽
‏ترمب: سنتقاضى رسوما مقابل حراسة مضيق هرمز</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82736" target="_blank">📅 16:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82735">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏ترامب: لن يحتج أحد عندما يُطلق على الايرانيين النار... إنهم مجموعة سيئة من الناس</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82735" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82734">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب: قادة إيران مفاوضون محترفون.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82734" target="_blank">📅 15:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82733">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6IQSdex7SvoqKx3Kky5PjJAzhqfYIb5tvF-kq6z3--ECRxV8uB_UszVuEAxkgI2jHFXP98qqzIDn2v0XOkikUAY9qfsm455TJtV_E_ujAeHnLtmVK-7HNFhp2Q1drnucYKYC_awTUAixZ7vJK54wdVpLTnir2kttYZJkF7_zOo4933WOcMDbvVYacyb2LiFF0vtISov-10FscXKvx7vc0pmoFpTZfw2IXmdcdGtKx09JtWYTaalUkAQX8MFYolLkdwDzPIocP7zUXSSKRnluOToWa72mksHqY6NwFy1roLIgdn_ZOPuSoBd5vZERJZCwgZPR1MWLUSXdHbJ7k-Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوفا من رد انصار الله..  تحويل مسار رحلتين للخطوط الجوية للمرتزقة التابعين للسعودية قادمتين من القاهرة وجدة من عدن إلى جيبوتي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82733" target="_blank">📅 15:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82732">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🗽
‏ترمب: سنتقاضى رسوما مقابل حراسة مضيق هرمز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82732" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">المتحدث الرسمي باسم انصار الله:  بسم الله الرحمن الرحيم ولا عدوان إلا على الظالمين  دون أي وجه حق أقدم النظام السعودي على قصف مطار صنعاء الدولي بعدد من الغارات في انتهاك فاضح لسيادة الجمهورية اليمنية وخرق كبير لهدنة 2022م. إن هذا العدوان السعودي العسكري الغاشم…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82731" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">المتحدث الرسمي باسم انصار الله:
بسم الله الرحمن الرحيم
ولا عدوان إلا على الظالمين
دون أي وجه حق أقدم النظام السعودي على قصف مطار صنعاء الدولي بعدد من الغارات في انتهاك فاضح لسيادة الجمهورية اليمنية وخرق كبير لهدنة 2022م.
إن هذا العدوان السعودي العسكري الغاشم والمباشر وبهذا الشكل على منشأة سيادية كمطار صنعاء الدولي يعد استمرارا لعدوانه السابق الذي استفتحه باستهداف نفس المنشأة عام 2015م، ويكشف حقيقة نوايا ذلك النظام أنه وراء الحصار المفروض على اليمن، وأنه نظامٌ عدواني لا يؤمن بأي سلام مع الجوار اليمني بل يريده جوارا تابعا لا يملك قرارا ولا استقلالا ولا سيادة.
إنه ومنذ اتفاق الهدنة لطالما تمت مطالبة النظام السعودي بسرعة تنفيذ خارطة الطريق لكنه تمادى في المماطلة، رافضا كل الحلول لإعادة تشغيل مطار صنعاء الدولي، وكذلك المضي قدما في تحمل مسؤوليته والوفاء باستحقاقات السلام.
وعليه فإننا نحمل النظام السعودي كامل المسؤولية نتيجة هذا العدوان المستجد، ولن يكون دون رد إيمانا بأن الدفاع عن النفس والوطن والشعب واجب ديني ووطني وأخلاقي وإنساني وحق مشروع تقره الشريعة الإسلامية والقوانين الدولية، والبادئ أظلم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82730" target="_blank">📅 15:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏ترامب: سنسيطر على مضيق هرمز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82729" target="_blank">📅 15:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56eaa7ce23.mp4?token=s-hezkmEqBcH631tOZETw-a1Y5v_bDVLO_jTj_h1Y3-vp_rI0KEXQkAaQCSj1SF8wH9j7MUADxMvQ4PCQS_ytXnmSRqo5TajrE8pI5GjJZl3NqQZ4v52ZU9miOOyBZUaTEkL3CGpCFBhLdRvsCwz0jx6g1fwzMwzYw9b5FESOr9TAMKfIDGAMVetjPYyrXkvqKgfASP-yrNAzWUZSX43MX4T5Vln3GMYVddvYBG0cYw9BkZZ09PqZVTAojCufXt4-WGmFtvXfRNT90kfzZNyOe8Wc3RVCcFS3004ID6p1X2Lc7HqK3uU7CuO5MtATYnS49FBNj-1YHUsoy3t8iwhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56eaa7ce23.mp4?token=s-hezkmEqBcH631tOZETw-a1Y5v_bDVLO_jTj_h1Y3-vp_rI0KEXQkAaQCSj1SF8wH9j7MUADxMvQ4PCQS_ytXnmSRqo5TajrE8pI5GjJZl3NqQZ4v52ZU9miOOyBZUaTEkL3CGpCFBhLdRvsCwz0jx6g1fwzMwzYw9b5FESOr9TAMKfIDGAMVetjPYyrXkvqKgfASP-yrNAzWUZSX43MX4T5Vln3GMYVddvYBG0cYw9BkZZ09PqZVTAojCufXt4-WGmFtvXfRNT90kfzZNyOe8Wc3RVCcFS3004ID6p1X2Lc7HqK3uU7CuO5MtATYnS49FBNj-1YHUsoy3t8iwhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ايران تكسر الحصار عن اليمن.. مشاهد من هبوط الطائرة الايرانية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82728" target="_blank">📅 15:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
‏ترامب: قد نشهد إغلاقاً حكومياً في سبتمبر إذا لم ينتهِ تعطيل العمل التشريعي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82727" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌟
‏
ترامب:
قد نشهد إغلاقاً حكومياً في سبتمبر إذا لم ينتهِ تعطيل العمل التشريعي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82726" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">النظام السعودي بعد الرد اليمني:
الحوثيين المجوس استهدفوا الكعبة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82725" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573a9ba1cb.mp4?token=Kw0VExKkEHGf3XkI0zH3lM1objj3J22wLugvF0mTfrj-latTzBvWehFOipo39yEoKFONj3SUgBy4tI17DEC0t-Hmlwbk-y3dh-ONiadrGcVbfdMKx7h0FZA_7VPzEk2aAV8SYX-OfwwWHp3baxiYFZNSiYQjeF_YDrTqif_wTViKizQHYMLv3tO22xtkttGSgH6OaqsxpGab6HyAOF2sFZ3NVL-k090dTCUvSrC-ljafLRmw8VIY1RnHWro1W5x6ECKtJWsmvYzDkvJLy5jg35eCf0ZsJjnLfvEPQdgayUvuo03NFm2taWDd6hYQ3-Hp6YuM-WZr6bRGhhpAxrvgLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573a9ba1cb.mp4?token=Kw0VExKkEHGf3XkI0zH3lM1objj3J22wLugvF0mTfrj-latTzBvWehFOipo39yEoKFONj3SUgBy4tI17DEC0t-Hmlwbk-y3dh-ONiadrGcVbfdMKx7h0FZA_7VPzEk2aAV8SYX-OfwwWHp3baxiYFZNSiYQjeF_YDrTqif_wTViKizQHYMLv3tO22xtkttGSgH6OaqsxpGab6HyAOF2sFZ3NVL-k090dTCUvSrC-ljafLRmw8VIY1RnHWro1W5x6ECKtJWsmvYzDkvJLy5jg35eCf0ZsJjnLfvEPQdgayUvuo03NFm2taWDd6hYQ3-Hp6YuM-WZr6bRGhhpAxrvgLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ايران تكسر الحصار عن اليمن.. مشاهد من هبوط الطائرة الايرانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82724" target="_blank">📅 15:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f94869577.mp4?token=JwY594vsZ8nvxNY91lSGP1QLrovONuOgDxbdfAC3twCTYTY_bsgmY8M3KMlK6vhntJbO81KYfwCb7mawu27hb8y86RyD1VyS_7l1nh97QvSNlvzJw6nVrXEGh2DJhAYRRdpizAXcNZKFpNLFpVGSfGgFHL7sBcymGaQKSYk33tU4eKnMMCgMw25ZzqOLvRXvNKydu6iHWkVy_QnxU45QBxRxRBo_gKdh6byeQmZpf2397FUHkoyjoca9gYkfVevNuTnnrLeqxPEJ6b445cX94auoiT78uRe9ieTjF4gX4Ro4CVjzjlAgiHMPbxx7n2CunMmaemUFaaQG70KLSpdSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f94869577.mp4?token=JwY594vsZ8nvxNY91lSGP1QLrovONuOgDxbdfAC3twCTYTY_bsgmY8M3KMlK6vhntJbO81KYfwCb7mawu27hb8y86RyD1VyS_7l1nh97QvSNlvzJw6nVrXEGh2DJhAYRRdpizAXcNZKFpNLFpVGSfGgFHL7sBcymGaQKSYk33tU4eKnMMCgMw25ZzqOLvRXvNKydu6iHWkVy_QnxU45QBxRxRBo_gKdh6byeQmZpf2397FUHkoyjoca9gYkfVevNuTnnrLeqxPEJ6b445cX94auoiT78uRe9ieTjF4gX4Ro4CVjzjlAgiHMPbxx7n2CunMmaemUFaaQG70KLSpdSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتقنا والله لغارة ع خميس مشيط
و ع مطار جدة
والرياض وارامكو</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82723" target="_blank">📅 15:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">المكتب السياسي لأنصار الله: منطق القوة والاستعلاء والتكبر الذي ينتهجه النظام السعودي ومن خلفه الأمريكي لن يحقق أي نتيجة ومصيره الفشل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82722" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">المكتب السياسي لأنصار الله: الاستهداف يأتي في سياق تنفيذ الرغبة الأمريكية بإبقاء حالة الحصار الجائر والمفروض على شعبنا منذ أكثر من 10 سنوات</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82721" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">المكتب السياسي لأنصار الله: جريمة استهداف مطار صنعاء تمثل عدوانا غاشما على شعبنا، وتعديا سافرا على السيادة وانتهاكا صارخا للقوانين والمواثيق الدولية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82720" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">المكتب السياسي لأنصار الله:
جريمة استهداف مطار صنعاء تمثل عدوانا غاشما على شعبنا، وتعديا سافرا على السيادة وانتهاكا صارخا للقوانين والمواثيق الدولية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82719" target="_blank">📅 15:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
🇾🇪
🇮🇷
بعد كسر الحصار وأصبح متاح لاي مواطن عربي ياكل مندي اليمن باريحية بسبب شجاعة إيران
ما يسمى مجلس الوزراء اليمني المدعوم من السعودية يتوسل : نحث الدول الصديقة على عدم السماح بتسيير رحلات لليمن خارج القنوات الرسمية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82718" target="_blank">📅 15:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏رئيس المرتزقة التابعين للسعودية في اليمن يوجه برفع الجاهزية خوفا من رد انصار الله</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82717" target="_blank">📅 15:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رفع حالة التأهب في جميع مطارات السعودية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82716" target="_blank">📅 15:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هبطت هبطت في صنعاء.. هربوا هربوا فوقهم فوقهم يا ولي،،
ان بندقية ابو الفضل طومر لاتزال بأيدينا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82715" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRrPfKyksbx9C0Nyz6vH76ABoKueZPUPFrsEb8ZVfGnrEXb07xFGCWWrU5-c8DbBcOWQDF-EefBokDczdN5yooL7pUQ0WpaxkOZna9o79mzsktL4Fl3N3UxfyWW0dYiD2uHvYpR8P6fCi8nEvdrfQQzhL6H6bwYTavXt_vOIbJVatxheC3iFNKWTI3Ey3T6OI_8ev4FfOd_hM8izyFvd0UDCl5X3OGbLtYEU3o61DXfT7b_bYOM4ISso13ZH9yyVJgskiUwsrkLd22QaLSOqmQ_LF-a4aX1Xu32WBkg4YBiflBmQQqkR_Eotw_SxtpZLroiVwaBitWWFhGM9dXRqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو المكتب السياسي لانصار الله حزام الأسد: هلطت الطائرة بسلام ووصل الوفد وكسر الحصار بالقوة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82714" target="_blank">📅 15:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مدير مطار صنعاء الدولي:
تحالف العدوان ارتكب خطأ كبير باستهداف مطار مدني بدون أي مبرر وهي جريمة حرب</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82713" target="_blank">📅 15:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
ما نبالي والله ما نبالي
واجعلوها حرب كبرى عالمية..
رجال ابو جبريل و يوسفي بالميدان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82712" target="_blank">📅 15:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نايا - NAYA
pinned «
غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/82711" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/82710" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82710" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نَقتَفي زيدا ًإماماً
هِي َوالله ِالسعادة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82709" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استهداف سفينة نفطية قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82708" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtR76dmtU4qmTF9pllSY25h2g2GAgvxmYHrBMVr5ZBGOtc7150RTOyha3J8dWMxCGtAWmVO__hhSWX1yi8k8_15weFKRV8IxwPUluS_x3eQ1odKiIMyyl7lnYFI4anP-nJZaGjgU4X1Hyuk2QldQCLKPQXPzxXJLTV5FsZLQSLtul-h0NqnJn7IyxigiuhoCikmUJf6RK-ojlTx3swzMKf7633dNywmqFDRu3-CD4UgEOvBVrq1Bs6Fl_EZaieNw0fUeBfzL2ai9HfL9yK0t3i8NylA2BDKfiRpzNnDugVjqEMsccavwNwfjuMv1-WSmhJ_KhV8cusK_BgfrGrR_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة نفطية قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82707" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82706" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82705" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزارة الخارجية اليمنية: سنبدأ مرحلة جديدة بالاستعانة بالله لانتزاع حقوقنا كاملة غير منقوصة وسيكتشف النظام السعودي أنه أوقع نفسه في مأزق إستراتيجي كبير وسيدفع أثمانا باهظة نتيجة لذلك</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82704" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزارة الخارجية اليمنية:
سنبدأ مرحلة جديدة بالاستعانة بالله لانتزاع حقوقنا كاملة غير منقوصة وسيكتشف النظام السعودي أنه أوقع نفسه في مأزق إستراتيجي كبير وسيدفع أثمانا باهظة نتيجة لذلك</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82703" target="_blank">📅 15:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الطائرة الايرانية تتجه لمطار صنعاء</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82702" target="_blank">📅 14:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82701" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">غلق مضيق باب المندب؟!
والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام
EU this, winter are to cold</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82700" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استهداف مدينة زايد العسكرية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82699" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82698" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82697" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">المتحدث باسم انصار الله: في عمل عدواني سافر ووقح، استهدف العدو السعودي المجرم مطار صنعاء الدولي بسلسلة من الغارات الجوية، منهياً بذلك مرحلة خفض التصعيد ومتحملاً عواقب عدوانه. ونؤكد أن هذا العدوان لن يمر دون رد وعقاب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82696" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrDsBWbGas-eyGqLn0o0g8zC3tCDJ1FFl8pCf3jNeVFu4pAzsKVVpkktTiCuCErg0B2046hzJJ9PB-B4ybS777vNcz1NOXQj9WYGgF1o849bPwfjYO8HBgttGdS9CKKZOB6k1vmSVmz9eI1bGbGkD1J4c6zdPvQIIYJXRsZ3IcwIZLd644OXbqnQGMFbOQJ2wIjmgIv0AJzOowEDXy8JSlZ9nTv1SPYrO_H6F9r-sgFVK7bdFBj9XZCN8AFqR9Y8jfoF5qplYneWj2htopgKa4DICKdzzB8p0d55MaJR4E3VzGCskDqweaXbaGSXiEWgf6aTa2ZDzPQ65GkPoss0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة ايرانية تقترب من صنعاء رغم عواء المرتزقة التابعين للسعودية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/82695" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZQ4gRSAgZj2qmXu9Q6ru1LkMzNrLtwefLxk1IT67iQ50a547LPkYfdHjjs9A4Pv0FSbfUCn-nPw0aJtYFUDonmp84nd2bDoYqbO7n7xMR81W5NlmU2f-eKJINkmKkOUL7VIh9JDILM_YuuemMvX9Mh4f1_RFCsC8abs7SP1a5kkL3EOWP1N7lsPgCLQVGDndF566899Sm1uvmcYO9t9xcicbFXMHqwwFViMg9preBZiyDvVtLFwVc4IgoguDp4dhgTrlQab_BNyLSb-H7Ilnb9C-qT9vRd0-INyd1Gbc8ydDDBVuswtRj034GayWD1ungWOwvEqYR75zqUCFvtGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من مطار صنعاء</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82694" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQwXY6b4PVcxm6qIC3fSUi7n5ntQCx9ZhmzOljw4I_ZoAVd2OOthc9PNB57Znciyc9QqN7WsWlTy_ORdPY4ZYiSRaL3-22W-Bmb5meWzVv2_9RhwUzjfj_3OgXHtakSIXxWJoiZQxENEy7x85tsWg9lmyI1EnWKhtAaZcPAwbDpX0LPkMqyIsqIXWPwXFQ1MSAtug-2P1a2DZERtMYhBjjejSjU8w5bpAsxxMBNHniqJrmguT29TpTfI7yngfz86vSJd0jRZ9SWSKHilXWKu3vAUDqxxt9uY06JA7p14HGOK8mBeraW_4K6HfQxVG1bubt5FPJvBAiA4GuiReESRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار صنعاء</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82693" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJR8JZgecpOOEbKcsm8ZDOERsQwQYEUrkKWUyhH1O88Wd5s9EXXuva7lHoRz9oYhMO2qvwqaepTKjjVMncyOv9KKqJ4tfXFEdfEDV-nHno8IAolbk36l2BwgiU25pQDFzoI7bsDw5-sJ-D3bhVZcsZ5jTQnM3Xg76VsmESsVF7i2LV40sm8g7X531a6T_38vIZgjuZDrxmv7Kv9ju8M628gg_EBaQUG39LVap_fMRW2XMPcbdMLh_g6Z3IJRoYGS5S_JoKKfEyzPHKLwdfcV6G4v1E-ixQcfUP2qEj8X8fItWhHqMUoY02KxxwFE-MRrtBBF-oyFDPjGazniCi1dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات سعودية تستهدف مطار صنعاء الدولي</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/82692" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/82691" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انباء اولية عن غارات على مطار صنعاء</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82690" target="_blank">📅 14:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaG5B48VVSGwLP2xZ4BovXSA1u1zd4riU_Q-HB-5RDY1dRyEtfxejXDjxhUXpAnFYwGBwotTNxX-3ZDkrn0gw3ULhVDwarVSdWV0DtSxYNsWHB3z55q4blH4b1bto4baHJsKpY0u3Ha1xuaPTTE85ZDfyxj14_FmxgA-yUdBI7CfNfTqpXqL9aAJkaBd9jIooFjxd9TBeadT27k2aDDokclXvZegMte-cwL9e_CZv-Ha6LgSOGCrtOAcQgswPkSKxZxUjum7MfJUfH6CS50a-TTpWKaIDW-osk3-w5QjJ4aVV2eG43x7iGF62rYsaq6kUiXQyVwkdBj0q0X8yBATCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس وزراء العصابات التابعة للسعودية في اليمن ‏يعلن حالة الانعقاد الدائم لـ"حماية السيادة وردع التصعيد".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82689" target="_blank">📅 14:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نائب محافظ خوزستان: تعرضت ثلاثة مواقع في آبادان لهجوم من قبل الجيش الإرهابي الأمريكي. حتى الآن، أصيب شخص واحد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82688" target="_blank">📅 14:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">العصابات التابعة للسعودية في اليمن: سنتصدى بكل الوسائل المتاحة للطيران الايراني الذي يذهب لمطار صنعاء الدولي وسنلقنهم درسا يسمع به القاصي والداني.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82687" target="_blank">📅 14:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات في عبادان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/82686" target="_blank">📅 14:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات في عبادان</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82685" target="_blank">📅 14:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند يوجه بحظر كافة منصات الرهان والمقامرة الإلكترونية في العراق</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82684" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">محافظة اربيل في شمال العراق تعلن عن تعرضها فجر اليوم لهجوم بثلاث بمسيرات استهدف مخيم للمعارضة الايرانية الكردية في منطقة داراشاكران التابعة لمنطقة بيرمام.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82683" target="_blank">📅 14:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
وزير الاتصالات العراقي مصطفى سند يوجه بحظر كافة منصات الرهان والمقامرة الإلكترونية في العراق</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82682" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇸🇾
عصابات الجولاني:
خلية تنتمي لداعش هي المسؤولة عن التفجيرات في دمشق خلال زيارة ماكرون.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82681" target="_blank">📅 13:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇷🇺
المتحدث باسم الكرملين دميتري بيسكوف:
تحالف الراغبين مخطئ في اعتقاده بإمكانية إلحاق هزيمة استراتيجية بروسيا، تحالف الراغبين المزمع عقد قمته في باريس من دعاة الحرب ومجموعة من الدول التي لا تريد السلام</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82680" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏العصابات التابعة للسعودية في اليمن: نفد الصبر وسنرد على اختراق إيران والحوثي لأجواء اليمن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/82679" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏
العصابات التابعة للسعودية في اليمن:
نفد الصبر وسنرد على اختراق إيران والحوثي لأجواء اليمن.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82678" target="_blank">📅 13:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة مهر: اشتباكات في المياه الإقليمية للخليج الفارسي ومضيق هرمز وسماع دوي انفجارات في محيط مدينة بندر عباس وجزيرة قشم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82677" target="_blank">📅 13:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
🇺🇸
وكالة مهر:
اشتباكات في المياه الإقليمية للخليج الفارسي ومضيق هرمز وسماع دوي انفجارات في محيط مدينة بندر عباس وجزيرة قشم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82676" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIsBFvIMdRk36RtWFiCSQs3uy97ehuo1p_SbT7HXI54Kzcsk2atsnQG5gJ0Omj5p9PDxIFEaH_ypLHU9AjD9Hj6tDmgbF8ehqypb6gzmLmPltm3XkHfCZeUZOkinoG7hd2nq7KTlhvCwc5gxECGnQFnckaRpHQAKIZA4aQNolWD_jhnjjcTJs4YFohDb5ztJo5terAoz8GFR8h1PLKFksHUqtZ30ukrUmyoHwPdEa9uK6H8-pbtJn2p9-C3eLu66tw8mWKkD3EPEX5mOAmSN_37PCDqS6jorTqM4stsvSlXEh7OuXBRbvutVnWUyq0FSDScarWNabNeegmMqi1yZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇭
السلطات في البحرين تعتقل شابين اثنين على خلفية حضورهما مجلس عزاء الإمام السجاد (عليه السلام)، وهما الشابان أحمد صادق الشعلة وعبد الله عيسى الشماع.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82675" target="_blank">📅 12:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
المتحدث الرسمي للخارجية الايرانية
بقائي:
▫️
السلام على أهل العراق، وأهل النجف وكربلاء، وعلى الذين اعتبروا أنفسهم جزءاً من حزننا وأظهروا أن رابطة المحبة والتعاطف تتجاوز الحدود.
▫️
وإيران لا توافق على طلب الوكالة الدولية للطاقة الذرية للحصول على حق الوصول إلى المنشآت النووية الإيرانية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82674" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇷🇺
🇺🇦
جهاز الأمن الروسي FSB :
يعلن عن إحباط عملية أمنية واسعة للنظام في كييف كان مراد منها استهداف مطارات عسكرية ومدنية داخل روسيا.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82673" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
🇮🇷
مصدر ايراني لنايا الانفجارات التي تسمع في محافظة اصفهان ناتجة عن تفجيرات مسيطرة عليها.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/82672" target="_blank">📅 09:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
🔳
اليوم العب بيهم جولة.. من أمام القنصلية الكويتية في البصرة، المتظاهرين الغاضبين على إستشهاد الصياد العراقي يبعثون رسالة تهديد إلى دويلة الكويت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82671" target="_blank">📅 09:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN1oQVwsojPu-STevnvrj7qml-Okbh7xlpb_A6SRypXLizrUFz8MjSceGB3uM-BnVaTSC_w-YLgfikQnU_PsI8izS1lhGVzsPw0JSQb7JruXDSW44i1HNACOMkY5bvVVgsb3yD5ThsEwpptTTfP8n76OMnDEFVnMmWPjenX5mZfdaP2TP0HryvQ7AEbmxOYEjMl0-IDwgAI7BH3uQHcyWUSkyqV1Z5cSlHIUTlShA6FwLJ7bRuGAwCvE4BfzlEYlroq-aBm1fVY5GnDxo0axpFfZFTkZTxzZVv4xu2YfsfrfhxOL3JC4JNcjpVkO8D5BzxJXCyzlIv8tdO83M9CnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء العراقي:
استرداد 375 كيلوغراماً من الذهب في قضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82670" target="_blank">📅 09:27 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
