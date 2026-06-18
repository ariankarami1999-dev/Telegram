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
<img src="https://cdn4.telesco.pe/file/NR1vxTSY2mIJ4gsEyvk5cFoUPwdBiSGR-bDJNfzw7BNengGlMhyp5mZJKB404PgwImPHiefJf3mJVT5pHMaka9m4y2t8k6BdjAo_BZAdd_b5aMJEuE6SfZFRiUbzjKB8T0OZGs-QuT5UFO4Wdxlr3j6ZFkSLRDQr2GBYZwQktMYRmH4cRX9dG8pKcHB-gO8FaK5MV-PFrmOymgYXY9gAdaFlEpqU147eiWSFlahWoa2mp8PIwzguZAV8FpWWy1_MOKmycPO4SkqhdsQZ_eMlyQiA06144vyYvC8E82NEwUvMDMROen6B6umhC9-Pfbyz7StVb2RLfhrkpvqtHa59Bw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-79207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول التصدّي لمحاولات العدوّ الوصول إلى مرتفع علي الطاهر:‏
يحاول جيش العدوّ الإسرائيليّ، منذ 4 أيّام، التقدّم باتّجاه بلدة كفرتبنيت ومنطقة علي الطاهر عبر أكثر من مسار مدعومًا بقصف مدفعيّ عنيف يستهدف المنطقة وإطباق جوّيّ استخباريّ تنفّذه طائرات العدوّ الاستطلاعيّة. وقد تصدّى مجاهدو المقاومة الإسلاميّة لجميع هذه المحاولات عبر استهداف تحرّكات وتحشّدات العدوّ بالصواريخ والمسيّرات والمحلّقات الانقضاضيّة، ممّا كبّد العدوّ خسائر كبيرة بين ضبّاطه وجنوده وفي آليّاته، اضطرّ خلالها إلى التراجع وزجّ الطائرات المروحيّة تحت غطاء دخانيّ ومدفعيّ في الليل لسحب خسائره.
يوم أمس الأربعاء 17-06-2026، الساعة 8:00، وبعد رصد قوّة مشاة من جيش العدوّ الإسرائيليّ تتسلّل للتموضع في الأطراف الشماليّة الشرقيّة لبلدة كفرتبنيت، وبنداء يا أبا عبد الله، استهدفها مجاهدو المقاومة الإسلاميّة بسرب من المسيّرات ومحلّقات أبابيل الانقضاضيّة وأوقعوا أفرادها بين قتيل وجريح، ثمّ استكمل المجاهدون هجومهم بصليات صاروخية وقذائف مدفعية باتّجاه منطقة الهدف.
وعند الساعة 1:50 من فجر اليوم الخميس 18 - 06 – 2026، وأثناء محاولة العدوّ التحشيد مجدّدًا عند منطقة المعبر، استهدف المجاهدون دبّابة ميركافا بالأسلحة المناسبة وحقّقوا إصابة مؤكّدة ما أجبر القوّة المتحشّدة على الانسحاب من المنطقة.
تؤكّد المقاومة الإسلاميّة أنّ قوّات العدوّ لا تزال تتواجد عند الأطراف الجنوبيّة لبلدة كفرتبنيت لجهة أرنون، وأن منطقة كفرتبنيت - علي الطاهر ستبقى عصيّة على توغّل العدوّ، وسيسطّر المجاهدون فيها ملاحم كربلائيّة دفاعًا عن بلدهم وشعبهم.</div>
<div class="tg-footer">👁️ 350 · <a href="https://t.me/naya_foriraq/79207" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
🇮🇱
إعلام صهيوني نقلاً عن ‏ترامب: من المحتمل جدًا أن أدعم نتنياهو في الانتخابات المقبلة لدينا علاقة جيدة لكن على نتنياهو أن يكون أكثر عقلانية.. وأنا مستعد للالتقاء معه</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/naya_foriraq/79206" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79205" target="_blank">📅 17:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvKqj7K2ATDCUOaJ5MCYK6tfB-BbR-7D9Ocw5cRyluZUHYjKe3b4zK6IYBIPVASmnWCc4SG_07CSAz9K7lIiifdZbjNDOp4Toe7Uer4QlWhkHdqOGdZYStDdBLg-BxXUlmSPrvWY1-6lPx61ofabeV2vTFzTK_p1KEvTq4J23pshAyY9p9UWZDiKgGPs3NBYSnglhJjaRKc0IO2qOqe12HX_C3yKcaUVmM5VyZz4cFL9fdVgdqcZj5y69sKfm93hSK1CXicz4AbOj1ZG0UAmAlWdot_VrTvjP-QKVXew0Wte3eJcEaBgi0ZkvP6IalhpHYYZlCY_tHVsupvveJgiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب من غمرة أحلامه يغرد: "النفط يتدفق، وإيران لن تمتلك سلاحًا نوويًا أبدًا (سيكون العالم آمنًا!)، وأسواق الأسهم مزدهرة، والوظائف في مستويات قياسية، والأسعار في انخفاض (القدرة على الشراء!). بلدنا قوي وآمن ويحظى بالاحترام أكثر من أي وقت مضى. على الرحب والسعة!"</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/79204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مدير عام وزارة الأمن الصهيونية: الحوثيون والميليشيات العراقية يملكون القدرة على التسلل بريا إلى إسرائيل</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/79203" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية: الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/79202" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية:
الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/naya_foriraq/79201" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzZDPrA6rwY1JxJqzeNam24UliwyGtW45mjqHzkrLKn-m0el6C1EPlgb_LgIaIwh6zzcuTzNEWz4rMKRPSyIvldBpGkswbVG0EPEzXFvTcQwjgiKNsYTX2M28lwaxJGenh0Knu8-CXq9wIY0-xDuLZ5O_py8UKvAUDs7yF7SkvRFc1Aw1cOlezjl6z5B92f6qrAOXW7dnHrTnfHEGtWoofVIwrRMhhCYw5nU4fYfMtDkgYBHtEAlLLPVQQ1SV1YVWiE_fGu6JfgIkmwnU8uR3oCva-rIdbu5Vqz8g8GC02DUu_Wh8knJS8_eIM681em4e3zND-Ud8lTo3ObmxAMhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة
يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.
التاريخ: يوم الجمعة 2026/6/19
الوقت: الساعة الخامسة مساءً
المكان: بغداد الصالحية - أمام السفارة الايرانية</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/naya_foriraq/79200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79199">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
يعتقد مسؤولون إسرائيليون أن الرئيس ترامب قد يؤجل شحنات الأسلحة أو يفرض حظراً على توريد الأسلحة إلى إسرائيل في المستقبل إذا لم يسحب نتنياهو قواته من لبنان.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/naya_foriraq/79199" target="_blank">📅 17:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
التلفزيون الباكستاني يعلن الغاء زيارة رئيس الوزراء شهباز شريف المقررة إلى سويسرا دون تحديد الاسباب ويقول ان المفاوضات التقنية الأمريكية الإيرانية ستبدأ بشكل منفصل ووكيل وزارة الخارجية سيمثل باكستان في اجتماع سويسرا.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/naya_foriraq/79198" target="_blank">📅 17:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد.. نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/naya_foriraq/79197" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/naya_foriraq/79196" target="_blank">📅 17:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف:
زيلينسكي إرهابي وروسيا ستشن ضربات منتظمة على أهداف في أوكرانيا حيوية وفعالة لقواتها العسكرية رداً على هجمات كييف.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/79195" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان وإخلاء عدد من الجرحى في صفوف
الجيش الإسرائيلي
.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/79194" target="_blank">📅 17:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متداول:
تكليف (نزار ناصر) بمنصب محافظ البنك المركزي العراقي.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/naya_foriraq/79193" target="_blank">📅 17:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79192">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2da43f07.mp4?token=gs3efZeUnuRZF-59uL4rRzizqbSq19_zng0vQFeEXX7_1RdIgc-GVkH88Jbm9u9x8QEi6gZ0pwfRquTqmDsEX3CbgjahmqP7ML1X3VU1GaR3rnTDLJ_GSggMPN3eg-NBV5oK9uK85OBn77LMzXNwo0zYZYQFH0MVDPx7tIJkkUpMDUUWWORQ_-P8dY74rWV63xsz07rXpHH3uGMi5uxT3-fi5yP20LDnd_OgnI27DB7yo06O0WORgiH4Ctx04rYpBSlxIm4lp0m4s3N8q3JP8F1Pg0bo-tE-xqp6HbKYOzdkK_WQwlIv6ioTTPyWwPO09ubaU6q_V04LbY6k4rpAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ظهور كائن نهري نادر غير معروف في محافظة ديالى ومواطن يتسائل هل هو حلال او حرام اكله تمهيدا لتحويله الى منسف.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/naya_foriraq/79192" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMw66rrx3k6KgwTuH-ryPdHzAZQbGqOOubMHmit06uluWeFMNcnwT3OJuvKG8VMt7hKADoSLfvMU9mg8x33-Ot_YNBs0bACMEzm4MhLKPn1hVUTsDGHZjDgUh2L1Nv6APHqwOGRMbQFxd-yr3inVomso2t1S3Dets84mdzLgO2dufC_XMyRBGzLUGBeisZXtm6DOa3jx0a73vjfytFnlSkLEB1VjOfODffCSGLG76PLC0Dey64SE6NU-NV3qbGu9mp6BQiGd2_pTWtEcSs86VE0_T5jyufKSbWWWC4oSGZEEAepVXJuylbZSPeBby-687ILrwb9qkWlDoqOurNlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يعيد نشر تقرير بعنوان "البابا ليو يشيد باتفاق السلام بين الولايات المتحدة وإيران".</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/79191" target="_blank">📅 16:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الخلاف الامريكي الاسرائيلي يتصاعد..
نتن ياهو: أمامنا تحديات إضافية تتطلب التمسك بالمصالح الأمنية والحفاظ على العلاقة مع أصدقائنا الأمريكيين.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/79190" target="_blank">📅 16:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79189">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇬🇧
‏بريطانيا تقرر تزويد أوكرانيا بـ150 ألف طائرة مسيرة بحلول نهاية العام ضمن حزمة تمويل بقيمة 752 مليون جنيه إسترليني.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/79189" target="_blank">📅 16:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79188">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
القائد العام للقوات المسلحة يكلف باسم البدري برئاسة جهاز الأمن الوطني العراقي.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/79188" target="_blank">📅 16:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79187">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174a7917f4.mp4?token=JYyaKjHfAIJRXinNbHmPDjk4cHPvM93FlE0Q2_C0RdlkWDO0IANHQRFuelO4gpbOoTkthXWkjCpAju77ODotft117mjirsPwu8dZ_asAsxHz5bPj0GUjSLJH0-dhkBFO8ud6_YHLtOdzeQeROMXQAvf9jE7DrCRyiD-s9JKq8IQwmAvwGWvQKGrqumd9ka_7vOATdJPMxEp8GtyDTJNK8f_Y3zREani1I_eq44mFNzN5TO6Xa1dAnfdj-qQvm6_5OcQKy-UiAdUD2sKqkaeROP3L-tMO2rL4o-hlRcuVrK7tcmfCQOm1ZOllIm0NKWejRJIHBMmqTOZi0xjYBjYJ7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جندي في جيش الاحتلال التركي ينشر مشاهد يُظهر الطريق العسكري الجديد الذي تم تشييده بعمق 9 كيلومترات في قرية باساغا بمحافظة دهوك ضمن اقليم كردستان العراق
يمتلك جيش الاحتلال التركي 139 قاعدة عسكرية في إقليم كردستان رُبطت جميع هذه القواعد والمقرات بشبكة من الطرق العسكرية وقد قُطعت عشرات الآلاف من الأشجار ونُسفت جبال وتلال الاقليم لبناء هذه الطرق.
اين مسعود وميليشياته التي تضيق على شباب وجمهور الحشد الشعبي والسائحين ممن يرفع العلم العراقي من هذا الاحتلال؟</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/79187" target="_blank">📅 16:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79186">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
المتحدثة باسم الحكومة فاطمة مهاجراني:
هذا الانتصار اليوم هو ثمرة جهود القوات المسلحة وكافة أركان المجتمع والحكومة.</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/79186" target="_blank">📅 15:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
الأنواء الجوية العراقية تبشر الشعب العراقي:
موجة حرّ خمسينية تضرب البلاد بداية الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/79185" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcqSYB3Pa_f5qePSftBJwfOikirhhOEX2Lu4XaRpHdRFpAH1buUOCJdeC7-Opge-UkvL1T1eheGz1sdb5mFmnx6HD_SbVNFO15Huj4ny4Ga6J8Yrg3gPKRW8_P8fS0eGUddiT4R1ZligzCxpktdaNaBn_i7lAbM_TIG2RixLI3UFo5BOBTBnc7CLatpmx7J8eIo9o75LCNhfszGxre1ORZkegXM_-m0TYBmDLjEh7z_i6lUkqGPX3BoENT6HqD_9iyO7TKOFHCxJRSFVujGtIP_j0KV3rFklWFYVarQOKjh2T29z4M4j8HMqgs1diPzWdQxVH586Y7R_Zvq4L9vvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
توثيق أخر يظهر كثافة استخدام القنابل المسيلة للدموع وإطلاق الرصاص الحي من قبل عصابات آل خليفة نحو المعزين بذكرى أيام إستشهاد الإمام الحسين (عليه السلام) في منطقة أبوصيبع البحرينية.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/79183" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعلام العدو:
اتفاق جيد لإيران وسيء "لإسرائيل"، سيبقى اليورانيوم المخصب في إيران، وينهي الحرب في لبنان، ويضمن إعادة إعمار إيران.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/79182" target="_blank">📅 15:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
سي إن إن عن مصدر إسرائيلي:
نتنياهو يرى أن الاتفاق النهائي لن يحدث وأن طهران لن توافق على تقييد برنامجها النووي، نتنياهو يسعى للتأثير على الاتفاق مع إيران عبر إعلاميين يمينيين وأعضاء بالكونغرس.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/79181" target="_blank">📅 15:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjL2V44BVtBoMcPuaNRJnq951AI1HMTd-mdHcfGQ961yycg6xZmcDHCVb7ZxbZaCE49QUdqd3zWlKXUYd3lHucI7goBxclC53TF2f6Dz828mjZ0TsU337gXVRhRDH6eU8VnWvVVsaugRFaB4mam99TcgbbIc48O-lyNS1FF1Gt-n3tJ9a2KJ8vYA_XC7j12CZbICa_pxEPHQp22lPHwRsT6-ZFbzBV3dDK86bknuYUlrFNEwcsTRMZtjaYyNf1ePVKMHFi5sBtrhWxm_KOZf4lCgJ-Oih9w2oT-7jmPjhWXguo_mnaLCaj7oPlTpYGacIz0xCAx1RITg45wXq2n91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPUTiCX0mu6qN-qAGEF-pr52P5kVR3_TpBtdM2FUzJ81vY_ejozrr_n7i0fPTyWHFHW4ceSfUaumgm9Bbtlm_w1PKXtEW3lw69-MXvwYPTA9PCXhh0UQRVGmWnKlqUOtMSkau-cNd7nyBWCLlHDmWFFGV4XzFABcugLRGS3R8sDJmeIeuZ4Y06bbD3E34ej0O5J6X7jDbBcY5gp4wwvcxHB0GsH7SQs2cdOwzu14SQLGFQueDNRuF6hYDHVlGSlapG8PUPMRmvk4CKycLnufl454THrx3U2q2aQkmcSL5T0omszhW5ZIeDDKfdeBPbPtBpZqmbu8K4JtgRkCYGPK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8YJeI0cFiizC3qaBJcdJSRa9WN5BjNZbequKWbq-Uq23TKBbSoWnUQlKsAtkBTh7Nprdf8kf9DaBhdLIGTYZSi5YTvLzIe3dyfJIvmwi0iYGKumGeUyOm4h5lqYNa3-kfUgZHfLvduyYxEp9ORd1h76G6VS9_Yy_jqeYpSyFEZCwp4GDP0MG1s4S7XH04TYp51E2M_B5MWwu7oQkabINJQoBI-6B4xSEFwlVvqNmwPI9r0ovgrMfGf4Il35YCP_Ot3xz1MgxogV6QsNLkpyGV9eH2GxL8GGR25EAQ0MXtjBTLf5LCMgtR7nNKj2Uf4rHeQy_kuTYLuN8dqeP_BDqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان ينشر بنود الاتفاقية مع الولايات المتحدة رسميا.
- تُعلن الجمهورية الإسلامية والولايات المتحدة وحلفاؤهما في الحرب الحالية الإنهاء الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان، ويتعهدون من الآن فصاعدًا بعدم بدء أي حرب أو أي عملية عسكرية ضد بعضهم البعض
- تتعهد الجمهورية الإسلامية والولايات المتحدة باحترام سيادة كل منهما والسلامة الإقليمية والامتناع عن التدخل في الشؤون الداخلية لكل منهما
- تلتزم الجمهورية الإسلامية والولايات المتحدة بالتفاوض والتوصل إلى الاتفاق النهائي، في مدة أقصاها 60 يومًا قابلة للتمديد بالتراضي.
- فور توقيع مذكرة التفاهم هذه، ستبدأ الولايات المتحدة في إزالة حصارها البحري ضد الجمهورية الإسلامية كما تتعهد الولايات المتحدة الأمريكية بسحب قواتها من محيط جمهورية إيران الإسلامية في غضون 30 يومًا بعد الاتفاق النهائي
- عند توقيع مذكرة التفاهم هذه ستبذل الجمهورية الإسلامية قصارى جهدها لاتخاذ الترتيبات اللازمة لضمان المرور الآمن للسفن التجارية مجانًا لمدة 60 يومًا فقط
- تتعهد الولايات المتحدة مع الشركاء الإقليميين، بوضع خطة نهائية متفق عليها بشكل متبادل بقيمة لا تقل عن 300 مليار دولار أمريكي، لإعادة إعمار وتنمية اقتصاد الجمهورية الإسلامية
- تتعهد الولايات المتحدة بإنهاء جميع أنواع العقوبات المفروضة على الجمهورية الإسلامية، بما في ذلك قرارات مجلس الأمن وقرارات الوكالة الدولية للطاقة الذرية وجميع العقوبات الأحادية الجانب، الأولية والثانوية، وفقًا لجدول زمني متفق عليه كجزء من الاتفاق النهائي
- تؤكد جمهورية إيران الإسلامية مجددًا أنها لن تحصل على أسلحة نووية أو تطورها. وقد اتفقت الجمهورية الإسلامية والولايات المتحدة على حل مسألة التخلص من المواد المخصبة المخزنة وفقًا لآلية يتم الاتفاق عليها بين الطرفين كما اتفق الطرفان على مناقشة مسألة التخصيب، وغيرها من المسائل المتفق عليها والمتعلقة باحتياجات الجمهورية الإسلامية النووية، وذلك في إطار عمل مُرضٍ يتم الاتفاق عليه في الاتفاق النهائي.
- في انتظار الاتفاق النهائي، تتفق الجمهورية الإسلامية والولايات المتحدة على الحفاظ على الوضع الراهن الحالي لبرنامجها النووي، ولن تفرض الولايات المتحدة أي عقوبات جديدة، ولن تنشر قوات إضافية في المنطقة.
- تتعهد الولايات المتحدة بأنه فور توقيع مذكرة التفاهم هذه، وحتى انتهاء العقوبات، ستقوم وزارة الخزانة بإصدار تصاريح لتصدير النفط الخام الإيراني، والمنتجات البترولية ومشتقاتها، وجميع الخدمات المرتبطة بها، بما في ذلك المعاملات المصرفية والتأمين والنقل والشحن
- تتعهد الولايات المتحدة بإتاحة الأموال والأصول المجمدة أو المقيدة للجمهورية الإسلامية للاستخدام بالكامل عند تنفيذ مذكرة التفاهم هذه وتتعهد الولايات المتحدة الأمريكية بإصدار جميع التراخيص والتصاريح اللازمة وفقًا لذلك
- تتفق جمهورية إيران الإسلامية والولايات المتحدة الأمريكية على إنشاء آلية تنفيذية لمراقبة التنفيذ الناجح لهذه المذكرة والامتثال المستقبلي للاتفاقية النهائية لعام 2001
- بعد توقيع مذكرة التفاهم هذه، ورهناً ببدء تنفيذ الفقرات ١ و٤ و٥ و١٠ و١١ من مذكرة التفاهم هذه واستمرار تنفيذ هذه التدابير، ستبدأ جمهورية إيران الإسلامية والولايات المتحدة الأمريكية مفاوضات بشأن الاتفاق النهائي حصراً بشأن الفقرات الأخرى.
14- سيتم اعتماد الاتفاق النهائي بقرار ملزم من مجلس الأمن التابع للأمم المتحدة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79178" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
بيانات ملاحية:
ناقلة فرنسية للغاز الطبيعي المسال تعبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79177" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-06-2026 آلية هندسيّة تابعة لجيش العدو الإسرائيلي في أطراف بلدة مجدل زون جنوبيّ لبنان بمحلّقة
أبابيل
انقضاضيّة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79176" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
بناء على الحاجة العملياتية تنتشر قواتنا في المنطقة الأمنية بعمق 10 كلم داخل الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79175" target="_blank">📅 13:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79174" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزير الحرب الأمريكي: مضيق هرمز ممر دولي وحيوي لكثير من دول العالم ولكن نحن لا نعتمد عليه ونأمل أن تتحرك الدول المستفيدة من مضيق هرمز لفتح المضيق</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79173" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3273200eb6.mp4?token=ibPdrIkh4lglgYyn3DnDrxl-yQvbHh-R2y_D9xFpLAZKJZxb-FYf4oemoM9iLARqAP1Hz2ONTZwn-or07ZsoQl2Sf23uxj_S-UBTshLDyxq4sS7gR0Ce7enVpzf7kB5MVylpssA8MRrFjGx3zs8y8PTiuZY_evMK1Rz7l7l9GgMI-5JmLqlUlKi1IZY9FvFHJjDJWTRQJp2ygzf8SWoBhbmFiwqez0OCeRLcNyZqTzB1N66tZEaft6ppcT0q6XMGVXo4f-lvfPZ3UJJLc52xqwVBejY6XU0Wr5BS_E_JfVhCx1y4vzcWqfkIO89JKemr-orTTWtfBwTweYI-VmGASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79172" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79171">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtRY8wZYH8U7sX2f2qWk-y1teMWEJ6fqriaSMyMiAgO54wRpe30HNNKaRYAtKFTJ-MwxMs16fLEyW5WsExg_XO6lG1iHBpmJVb9-gKEDwymtsMi2gZMDITqgrqKxQxBupnIE8acao6qeKl7i-4WyN9-2PI69IIOtN9E7AT4Hi7qM5Xd-Hz2DJr65NKJGp-fb69eBJEB7bWxgaQg52NJLiPIQ6t2QiKFVY-I24-oLKa1p-N9TBBQvNLFZfzusWljunZVNaHysmdW5a6jPV8RXbw2NAYHwQERVoUvr5zPz-h2wwKuuwulbW18XtzNJFnelJORxV0jdRZQ56AjUFLsLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
"هؤلاء الحمقى الذين يظنون أنني لم أكن حازماً بما فيه الكفاية مع إيران، في حين أن سوق الأسهم قد سجل للتو مستوى قياسياً، وأسعار النفط "تنهار"، إما أنهم حسودون، أو أناس سيئون، أو أغبياء. لنجعل أمريكا عظيمة مرة أخرى!!!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79171" target="_blank">📅 12:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=XgjUkXqqR97M5y2xrnInk-pTrzIttR1xUZQpAYTIUfKA57nzBOtSlL0vRpD7Kdv9KIQ08C3X9JTnoj3lXJGCCb9e-FGYB-VB6jBi2AFJsy0ZX8mgzd5SofI7bU4rnC8QcVIHWYLQ4us9ERDRCxmlD6yHAiTO91UowZGsXmD7OzgGeHtDn0R5j6Wilz_vqHf8U-Z0TgR5WZIzoG95PxCryi1p5sAmofYoWsAREniKt-NAJ3fUqiPcoayqnO3lE1JdwFpjJeVv2B9_U2SlrTmnhWF267a7sFyDO4nOBZFKBvLfhDromQJkw-P3TmZekobe8hcyXyeAnR7ptUsD29xQBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bbebb7bbf.mp4?token=XgjUkXqqR97M5y2xrnInk-pTrzIttR1xUZQpAYTIUfKA57nzBOtSlL0vRpD7Kdv9KIQ08C3X9JTnoj3lXJGCCb9e-FGYB-VB6jBi2AFJsy0ZX8mgzd5SofI7bU4rnC8QcVIHWYLQ4us9ERDRCxmlD6yHAiTO91UowZGsXmD7OzgGeHtDn0R5j6Wilz_vqHf8U-Z0TgR5WZIzoG95PxCryi1p5sAmofYoWsAREniKt-NAJ3fUqiPcoayqnO3lE1JdwFpjJeVv2B9_U2SlrTmnhWF267a7sFyDO4nOBZFKBvLfhDromQJkw-P3TmZekobe8hcyXyeAnR7ptUsD29xQBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79170" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭐️
المدير العام للوكالة الدولية للطاقة الذرية:
حان الوقت للجلوس مع الفرق الأمريكية والإيرانية لاتخاذ خطوات ملموسة.
سنشارك في المفاوضات التي ستعقد في سويسرا بين واشنطن وطهران.
هناك خيارات عديدة بشأن التعامل مع المخزون الإيراني من اليورانيوم.‏
الاتصال مع إيران في أدنى مستوى له.
إذا لم يفتح مضيق هرمز حتى نهاية يونيو فسيكون الاقتصاد العالمي في منطقة حمراء.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79169" target="_blank">📅 11:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79168">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇷🇺
الدفاع الروسية: أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79168" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79167">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇾
هجوم مسلح يستهدف حافلة تقل عناصر تابعة لمايسمى بالأمن العام الجولاني في ريف محافظة الحسكة السورية؛ مقتل وإصابة 10 أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79167" target="_blank">📅 09:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=DEZeN_SGUG4OPgi-_FjL2rrIgjp_svseY3nSyu_g8drdB30NaP3wCz7gcrl6SV01WADDDD4dwEzIt8lGTEnzRfP2inlzOVc76XuG3PTRQR5RnroefCNaXkz6QtLXu2q4N8Kj8hMoy-jZlHgrOn-ONnByn6LTt6_KHZ19jjgETZxbvEwJ8yM7Zzt66IGeuDoQy-IUWgl5faRTezjgMXcT_nWpfEdDIEO3zfYHX-HmOAgR_y-hXYsEXAYG4XejJ5t-86LUZc3cvuzJtN3Lvr6DIKi3sjB0t0WNYLS3qtL20DOfb2AT_l1lbT7dpRzeuGDyGkUHNAruEumfkdc2GWr_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8438843fc4.mp4?token=DEZeN_SGUG4OPgi-_FjL2rrIgjp_svseY3nSyu_g8drdB30NaP3wCz7gcrl6SV01WADDDD4dwEzIt8lGTEnzRfP2inlzOVc76XuG3PTRQR5RnroefCNaXkz6QtLXu2q4N8Kj8hMoy-jZlHgrOn-ONnByn6LTt6_KHZ19jjgETZxbvEwJ8yM7Zzt66IGeuDoQy-IUWgl5faRTezjgMXcT_nWpfEdDIEO3zfYHX-HmOAgR_y-hXYsEXAYG4XejJ5t-86LUZc3cvuzJtN3Lvr6DIKi3sjB0t0WNYLS3qtL20DOfb2AT_l1lbT7dpRzeuGDyGkUHNAruEumfkdc2GWr_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79166" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
عصابات السلطة البحرينية تستمر في مهاجمة التجمعات الحسينية ومجالس العزاء بمنطقة أبوصيبع وسط مواجهات مع سكان المنطقة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79165" target="_blank">📅 09:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
لا يزال استهتار البعثات الدبلوماسية الأجنبية في العراق مستمر
اصابات خطرة لمجاهدي جهاز الامن الوطني العراقي بعد تعرضهم لحادث سير من قبل رتل تابع للسفارة الأمريكية على طريق مطار بغداد ؛ ثلاثة جرحى كحصيلة اولية من الضباط …</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79164" target="_blank">📅 08:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
أسقطت قوات الدفاع الجوي 555 طائرة درون أوكرانية خلال الليل، 180 منها كانت متجهة نحو العاصمة موسكو.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79163" target="_blank">📅 08:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm8WzINVH4E-0aORjKcySjk2nAjcRT1ZhfM3j4hrcTZKIuLcqHD7zwuMv-2jmgj6q4t5sxTV722WVhnHYl3P6uX0XlGJB-Ui8aNaoIWiUQZYbI_mHLtU-_jvtIeXb1Y1vofUCLlB45iAU8BerO-eKDGY6tfDzTS106W4ly3jllThff12VjsFYRZr8fhDYyIxNKNqvaOmlNCLy7Hafuob4qZXoLJsJ2FBi31g5lj8bLNZbo7AhEsHl71zMo0StNFECDXOHOGksPc_lZd-2MCe2pilSnBZYFYKYL5AJ89L6F1ldQP-C6RRbE5GQimWhuFG3rxtx0LcpWILCO678Of0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5a5ACxIUHlAdqc9W29ctZys1GaOMkCQj36fpvQSFmEPOz9o0aErW4m62xVsrOqaMFIBOIIil61wfjs0CwekFK7R8f_wO55d3gPy5paOhWn_2lCI6sUqz3ALIYUjs4RD9LnPbF0z-JFYWwdyEdvPGumaeQgKMu5xsN_xqD6Rpgx2rjBwCi9_oyQ10whf87cJtoFELJR1FY9eQq00zG_9BoIgu_cRzEEkC_FeE3u2tVSpKGtSXzQffP2SLjalC37Pa5PS1YN85-IkVjucjdGX48OwkAdReYiTF2fYydFKRwijiwsywMV9T9OMA47_GODtQtVg_7baZrly4W3qf9_xBvi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8e1fc0d5.mp4?token=PMFvH0UW79SY_hpuPO1Xju1k0Fk8F8cQxaKQ8FhtVqOMJ-4nt61bL3QSz31W5YQGRPwojkvB_qnp41o1XbuBJUSiv_r8kQd7mDGpFJibeGZgPe2SyWCUH40vkMqv3xslJ9zPkFn0urj52oMDOhcjzYTAPaQUBxqAyIGtNjkkWul7NpxPg5U5FJJjmMudBdHe2VAqleLRKwLAsfbsNmZHF3mw16tbfNM01LFiw7NHmKj09YvlLbqMcCkaYUgwkYGasPYG1JMmBgU3wBiJqXqd1ZbPKYMWtFdEac9sjTHvMCUSazCrVXhjgqQia5_BuzvFsUvg_hK6sw71ClT8Cu9b5a5ACxIUHlAdqc9W29ctZys1GaOMkCQj36fpvQSFmEPOz9o0aErW4m62xVsrOqaMFIBOIIil61wfjs0CwekFK7R8f_wO55d3gPy5paOhWn_2lCI6sUqz3ALIYUjs4RD9LnPbF0z-JFYWwdyEdvPGumaeQgKMu5xsN_xqD6Rpgx2rjBwCi9_oyQ10whf87cJtoFELJR1FY9eQq00zG_9BoIgu_cRzEEkC_FeE3u2tVSpKGtSXzQffP2SLjalC37Pa5PS1YN85-IkVjucjdGX48OwkAdReYiTF2fYydFKRwijiwsywMV9T9OMA47_GODtQtVg_7baZrly4W3qf9_xBvi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لحظة توقيع اتفاقية التفاهم بين الرئيسين الايراني والاميركي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79161" target="_blank">📅 03:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية: تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/79160" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
🌟
وزارة الخارجية الإيرانية:
تم رسمياً توقيع نص مذكرة التفاهم من قبل رئيسي أمريكا وإيران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/79159" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏اندلع حريق في الطوابق العليا من مبنى الإمارات في دبي
‏أبراج فاينانشال: سبب الحريق مجهول</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79158" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
قالبياف:  بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.   وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.  بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/79157" target="_blank">📅 00:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=GIJde_Ns3kvneVbZJZtRsfkxRujpBoafqR-WdRlerTDFfIA_BiV91IIpGYOSvRpDxJ1nKQrhrcK8yyboHIHc8q2j_2cZhecZkPYYOKMh2UlQT4hW5_fLke6Za6NtF-xdlcb2_tQQVIXPh9droagSJI9pUdQ2sGqg4oORcEy9wvVSrqetNy6QV-sJ5-tHfJrnhTzfjhqt6p9ioKRmrYcMq8wecpzheGjTwLHbHl312jZTF_mJOOt643Brx6LrujIhuCbeXe2R8O75vBhA3Ub32xCaatSdwnaldDviVBrMRSAWhIkmN9U10dHA8Xqxx0YZQM_V3fl5nbwS9ggFnhtvLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30ecaca4a.mp4?token=GIJde_Ns3kvneVbZJZtRsfkxRujpBoafqR-WdRlerTDFfIA_BiV91IIpGYOSvRpDxJ1nKQrhrcK8yyboHIHc8q2j_2cZhecZkPYYOKMh2UlQT4hW5_fLke6Za6NtF-xdlcb2_tQQVIXPh9droagSJI9pUdQ2sGqg4oORcEy9wvVSrqetNy6QV-sJ5-tHfJrnhTzfjhqt6p9ioKRmrYcMq8wecpzheGjTwLHbHl312jZTF_mJOOt643Brx6LrujIhuCbeXe2R8O75vBhA3Ub32xCaatSdwnaldDviVBrMRSAWhIkmN9U10dHA8Xqxx0YZQM_V3fl5nbwS9ggFnhtvLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالبياف
:
بمجرد أن دخل وقف إطلاق النار حيز التنفيذ، رأيتم أن العدو قام بأعمال في الخليج الفارسي، و تم الرد عليها على الفور.
وكان أحدث مثال هو الحادث الذي تورطت فيه طائرة هليكوبتر أمريكية.
بالإضافة إلى ذلك، تم إصابة سفينتين حربيتين للعدو كانتا تحاولان المرور عبر مضيق هرمز وعانت من حرائق واسعة - وهي مسألة أكدتها أيضًا صور الأقمار الاصطناعية.
ومن ناحية أخرى، تم استهداف أي مطار في أي بلد انطلقت منه طائرات مقاتلة للعدو. حدثت كل هذه الأحداث أثناء مشاركتنا في المفاوضات في نفس الوقت.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/79156" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
‏ترامب: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/79155" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
‏ارتفاع إنتاج النفط الخام في جنوب العراق بنحو 500 ألف برميل يومياً ليصل إلى 1.5 مليون برميل يومياً، فيما ارتفع إنتاج حقل الرميلة إلى 650 ألف برميل يومياً. كما أعاد العراق تشغيل حقل غرب القرنة 2 بإنتاج يبلغ نحو 150 ألف برميل يومياً، في إطار تعزيز الإنتاج وتعافي عمليات التصدير.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79154" target="_blank">📅 22:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
‏
ترامب
: سيتم توقيع الاتفاق مع إيران خلال الـ 48 ساعة القادمة، ومن المحتمل أن نبقي الجيش في الخليج لفترة من الزمن، وإذا كانت الدول الأخرى تمتلك صواريخ باليستية، فمن "غير العادل" بعض الشيء ألا تمتلك إيران أي صواريخ، والغبار النووي أقل أهمية من عدم الانتشار النووي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79153" target="_blank">📅 22:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79152">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امريكا وانهيار سياستها الخارجية؛ ‏الرئيس البرازيلي لولا:
لم أطلب عقد اجتماع ثنائي مع ترامب لأننا
نتفاوض بالفعل.
‏ما فعله كان عملاً شائناً تجاه البرازيل. وهو يعلم ذلك.
‏لهذا السبب قلت إنه لا يزال يتصرف كإمبراطور.
و ترامب كثير الكلام وقليل الاستماع.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79152" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g__rnL45vuwu9SASCDZ0R_wEsU-FIth3Icn64zWsl-0FY8AbEw3KRay5tm1Ddxqx2VT4t-zmja2MHl82c99kwhITJKgcvebhmnNLvJhO8BzZNPtnV9_9YwnU_tTvHqO2_ZHQSXCdDLwXigwVpA2sWprlMyED_XxgVLXiOnyaykuK9HqpiXqcF8mQweeoWCkJccKHvpNI-NiFur0bTS_VEzekXIyjcyoOZ3BhIGnQrqt4XhRnjY8G3642iAqd5SIpPRc5f6EKAwDUDv6LTqV9pBueSjQk99dLVkSRe-NyC3QxBwlgAWxCAzeAVxRQpwmEE2dIbe-9B87FhUs5OitE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إيلون ماسك يعلن دخول ستارلنك للعراق من خلال زيارة توم باراك للعراق !</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/79151" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=MR0lfSkpphHEshHe7wz1XLjSpUb-iR4hWwn8BqGCzIhfiMmMUFbeSMTAjAQPSE4GXFFs6E-bTJzwNERJsMRq2qtzg5E4KutlXGFn2vx42E_78UtxYrfPgD71TpucVmmiHWC1Ohhq3thUDd4Hq-At11bgB8vDuLR3rp2E4KZFzrAjihe28ZYF059yvy_H3wTMiXVyt5pApklUvtlDEYMLyfLk2vIKoXZl5Jt1PkCf6AV6d_LJnxvbYsZvk-axQZeLzV7T74OSsxVs-VuiG0_38t1oSXGUxQS_WRNktuxTKs7y0N2ZjjRd2wD3Q6EmM_7-rLOt1omcUqzPjr6-n0VLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a82aaa5f.mp4?token=MR0lfSkpphHEshHe7wz1XLjSpUb-iR4hWwn8BqGCzIhfiMmMUFbeSMTAjAQPSE4GXFFs6E-bTJzwNERJsMRq2qtzg5E4KutlXGFn2vx42E_78UtxYrfPgD71TpucVmmiHWC1Ohhq3thUDd4Hq-At11bgB8vDuLR3rp2E4KZFzrAjihe28ZYF059yvy_H3wTMiXVyt5pApklUvtlDEYMLyfLk2vIKoXZl5Jt1PkCf6AV6d_LJnxvbYsZvk-axQZeLzV7T74OSsxVs-VuiG0_38t1oSXGUxQS_WRNktuxTKs7y0N2ZjjRd2wD3Q6EmM_7-rLOt1omcUqzPjr6-n0VLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ضربة قاضية من طائرات إف-5 على القاعدة الأمريكية في الكويت خلال حرب رمضان.. الطيار الإيراني يتحدث:
تم التحليق على ارتفاع أقل من 50 قدمًا (بينما الارتفاع القياسي 500 قدم) لتجاوز دفاعات الكويت المتعددة الطبقات وأنظمة باتريوت.
العمل في صمت لاسلكي تام؛ على ارتفاع منخفض جدًا لدرجة أنها مرت بين سفينتين وكان سطح السفينة أعلى من الطائرة المقاتلة.
احتراق مروحيات العدو في الحظيرة  قُصفت قاعدة العدو بقنابل متطورة، ثقيلة، دقيقة، وساحقة.
دُمرت مروحياتهم المتطورة في الحظيرة نفسها قبل أي رد فعل.
دُمّرت القاعدة بالكامل، وبقوة ضاربة هائلة، لم نرحم العدو الغاشم.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79150" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79149" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cli2R4T3oqHlrhffY2eefakfZCRD2XWEJs9ENvWWgfMzQxscN-UmvJNrSefM_xXxmvWvjB2NGfEp2zyxvS7YstlHyWlVy59XT1ulO3oHHcKfum9zZ0XKx6D52VAdV8dWFVD8x32SEt-XoNufA9UuWeLoHM4Dl_o5Cje8WscpkswZUNJPNyE2Z8AsE0miTPQF1N2T2ysi_zH7n6ImKelUJzMcGpyUu_7ap0pafsQpuUB5kO_iyZd09vP0ZK1PXb2kjDOs69Kj61eBp6S6J0OuGENMCLn8mqnilANugCdNJe6w85umOtcRELqURr9C7jG9FEwTulcwTG4bgy-Foz31_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏اعلام الاميركي: ترجيحات بمقتل 8 من طاقم الـ B-52 التي تحطمت في كاليفورنيا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79148" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79147" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
إذا كان المقصود أن علينا الاستسلام من أجل رفع العقوبات فذلك لن يحدث أبدا.
غير صحيح أن جيشي أمريكا وإسرائيل عديما الكفاءة ورغم قوتهما هزمناهما خلال الحرب الأخيرة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79146" target="_blank">📅 20:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد محمد بن سلمان.. ترامب: أفغانستان تقبل مؤخرتنا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79145" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن الحرب على إيران: أيضاً، ستنفد احتياطياتنا في غضون أربعة أسابيع تقريباً، كما تعلمون، هناك احتياطيات في جميع أنحاء العالم، وستنفد بالفعل، وسيكون هناك وقت لن تتمكنوا فيه من الحصول عليها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79144" target="_blank">📅 20:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79143" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79142" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:  حسنًا، إن إلغاء التجميد - إنه سؤال سهل الإجابة عليه.   لقد أخذنا الكثير من أموالهم، وقد - أموالهم التي أخذناها منهم.   عندما لا تكون أموالنا، فهي أموالهم، وقد جمدناها في وقت معين.   أعتقد أننا سنضطر إلى إعادتها، أتعلم؟   إذا لم نقم بإعادتها،…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79141" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79140">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79140" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يسخر من محمد بن سلمان:  لقد تحدثت إلى ولي العهد السعودي عدة مرات - إنهم سعداء للغاية لأنهم لا يزالون... يجب أن تجعلهم سعداء أيضًا، أتعلم؟   نحن نستخدم مطاراتهم، وليس أنهم يمكنهم إيقافنا إذا لم نرغب في ذلك.   ذهبت للحصول على ذلك الوغد الصغير. لكني أخطأت.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79139" target="_blank">📅 20:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79138">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO3i-4CIzyTPVXgDPSFUX1ppe0t_PbaeQm4BfGecINhLTk9vcEWx2psB7579gAEtgaRhJ5g-kBzfAs3im2U-wGWML_nuT5Y-YJ0k40Pa_rKQeLH8oqzhZ8ZUnOayWAuCKXxEEfs-tdK9jvWqq7_NKPIC2YVwKoMX-aZzlN60fB19ACNt4BmX4tKeqO3JDtEVXPa4LT8G5fglOitiocwgWfVNXUfIQiUxELpnLojMOl4cWwcwEdX3pTX_524MikltTeD391BPzwNd6YfMwNm6r0ec4sKnG4HAwLMHhwLAML_1-77eCgisST-1eTsQ2dK3HMwmiBNJDigSrqVtOkCIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ إعتراضية في سماء مستوطنة المطلة في الشمال الفلسطيني المحتل دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79138" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=ChemeG9Qdoup__3_2Da_lLTxfQQZL-9-hTzJK4fKCGB4OhOKZo-AMewKUen6CridBv_AYSJSyc63TGePvx68bKgMdzLuDPdrsSOvo2SclEgIqcubD6-KMFliKHSvnHpZL2H3zySTmi1Vu5yDdgRZglwJw2HZqtF76CauGGZYVpkyMROpTm5nr0mRBx5jbjeJUvcAoaQB8Uz7GCdG_mP3g2mChKKbHf-DofcWy1TGGrtb0jq4ND4la5H2gKja2uLvwCpLaJTrwIR9rTTltfQvkKMI0tpx5PTu-leTd7mE_6TOCDy3X8cT5MmqXJnEcaVqazVxGEqsnwaVKipPQeScqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=ChemeG9Qdoup__3_2Da_lLTxfQQZL-9-hTzJK4fKCGB4OhOKZo-AMewKUen6CridBv_AYSJSyc63TGePvx68bKgMdzLuDPdrsSOvo2SclEgIqcubD6-KMFliKHSvnHpZL2H3zySTmi1Vu5yDdgRZglwJw2HZqtF76CauGGZYVpkyMROpTm5nr0mRBx5jbjeJUvcAoaQB8Uz7GCdG_mP3g2mChKKbHf-DofcWy1TGGrtb0jq4ND4la5H2gKja2uLvwCpLaJTrwIR9rTTltfQvkKMI0tpx5PTu-leTd7mE_6TOCDy3X8cT5MmqXJnEcaVqazVxGEqsnwaVKipPQeScqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏إن توسيع نطاق اتفاقيات أبراهام هو الأمر الآخر الذي نأمل أن نحصل عليه. ‏وأعتقد أن المملكة العربية السعودية، إذا قادت الطريق، ستكون قد قدمت خدمة كبيرة لنفسها.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79137" target="_blank">📅 20:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
🇸🇾
‌‏ترامب: الرجل المحترم في سوريا، الذي أصبح الآن رئيسًا لها، قام بعمل رائع، فقد أعاد بناء ذلك البلد في عام ونصف، مثل بلدنا إلى حد ما، عام ونصف، بحجم مماثل تقريبًا.  ‏قالوا: "لا، من فضلك لا تضعهم هناك، إنه رجل عنيف للغاية، من تنظيم القاعدة".  ‏قلت: "حسنًا،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79136" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=TC4xiv1R421qIRxmSSjg-xZX68dmtiGVItZlBRNy_6DTIhMB1-SVwcAoxlysCHrPB_z9TUxhYBpnHWnyPnwThsfUV77PYZ106NKNJQp5RJzfO8B6qzS5IiC5iTPLhVxiUuz3GOGVzEQvxEFBTEb6DC-n96l4V1_ZKUjja1Y7wMT6lA-8OH5_HYoVIN7uXFsuAa_uwBCQ9grao34GpO4HC9dgH52brRPrs1Yb_MQqyLKY8A5NZ0r-f0xDgkYzfLJQdfG-gvYrjkBjf3rm1_4jIzzibeLgjmtPG7YtnTADTUes2REchtKsSibD95QEGGi24bMfz_esjj6wpdLx65UWJ721YnSLyg8UGQSMGstxsDDwLaUhpHbx55UqGy_W45FEwi31SR8oKraGOBRvvg2ttHjfcSHnThM5Z2vUFOnNsU8HRIg5mN5nEGXbWcFQ6N6oCQO0-aHQYFyDOq7DG8zfumw143F3FWjGtvSTUhaA3Rw3Cx3bhbFDm6HwqIBM13mWhhi6BPCoj4rnXGPZtgiQt2QLHdHa4qfPJTBtZpaXDdSgjWezX0bp8jdV-cQJCckLm0FV6hosy8f0J3lIKv0foEXec_fpnL_1Pa2XzlDmVoafjsPxe6cSdh-WHDndf_2N2DPYnbCwj6yJYVDY3rYzf92jusztnBusDmDnRaGh-TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=TC4xiv1R421qIRxmSSjg-xZX68dmtiGVItZlBRNy_6DTIhMB1-SVwcAoxlysCHrPB_z9TUxhYBpnHWnyPnwThsfUV77PYZ106NKNJQp5RJzfO8B6qzS5IiC5iTPLhVxiUuz3GOGVzEQvxEFBTEb6DC-n96l4V1_ZKUjja1Y7wMT6lA-8OH5_HYoVIN7uXFsuAa_uwBCQ9grao34GpO4HC9dgH52brRPrs1Yb_MQqyLKY8A5NZ0r-f0xDgkYzfLJQdfG-gvYrjkBjf3rm1_4jIzzibeLgjmtPG7YtnTADTUes2REchtKsSibD95QEGGi24bMfz_esjj6wpdLx65UWJ721YnSLyg8UGQSMGstxsDDwLaUhpHbx55UqGy_W45FEwi31SR8oKraGOBRvvg2ttHjfcSHnThM5Z2vUFOnNsU8HRIg5mN5nEGXbWcFQ6N6oCQO0-aHQYFyDOq7DG8zfumw143F3FWjGtvSTUhaA3Rw3Cx3bhbFDm6HwqIBM13mWhhi6BPCoj4rnXGPZtgiQt2QLHdHa4qfPJTBtZpaXDdSgjWezX0bp8jdV-cQJCckLm0FV6hosy8f0J3lIKv0foEXec_fpnL_1Pa2XzlDmVoafjsPxe6cSdh-WHDndf_2N2DPYnbCwj6yJYVDY3rYzf92jusztnBusDmDnRaGh-TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب بشأن حماس: ‏عندما ولدوا، خرجوا وفي أيديهم رشاش.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79135" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
‏ترامب عن محمد بن زايد: ‏محمد في الإمارات مقاتلٌ لا يُستهان به. كان يُلقي القنابل الأسبوع الماضي، فقلتُ: "من بحق الجحيم يُلقي كل هذه القنابل؟"، كانت الإمارات. إنه مقاتلٌ بارع.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79134" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79133">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79133" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=oVhrDRh7vfRWf9bVLw2ta-cFizT4AWcwJP-Bl6TNG07GLei8UZJD-WMZILj685SMw_N4QFwdwk2u6KLFPrC-inMD2Hy7zwN2sjscobuOCWaQQLQ49AVu_SlGqzzqTpIvIqDys_a3sYy4L4D_jrhQqzZpd0blB3sseGoYl4fq59ndZMCTJ-dI82qd9tKmPNJCGBXEC9qnEhEd-qnWlzaGXLhX8e_kwhk7rGMjPQjamUwj_G5yheR2zpnq8zxIBYEmrZhQQKBYbuXWrhcYCo7UAhdzklyjghjqQhBcsIck50kzgRysmpJU8tytgHVKEugRP1u6RYgxH7FVqZ5iZd8Osw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=oVhrDRh7vfRWf9bVLw2ta-cFizT4AWcwJP-Bl6TNG07GLei8UZJD-WMZILj685SMw_N4QFwdwk2u6KLFPrC-inMD2Hy7zwN2sjscobuOCWaQQLQ49AVu_SlGqzzqTpIvIqDys_a3sYy4L4D_jrhQqzZpd0blB3sseGoYl4fq59ndZMCTJ-dI82qd9tKmPNJCGBXEC9qnEhEd-qnWlzaGXLhX8e_kwhk7rGMjPQjamUwj_G5yheR2zpnq8zxIBYEmrZhQQKBYbuXWrhcYCo7UAhdzklyjghjqQhBcsIck50kzgRysmpJU8tytgHVKEugRP1u6RYgxH7FVqZ5iZd8Osw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لدينا القدرة على الوصول الى اليورانيوم المخصب في ايران.  لدينا عدد القنابل النووية الأكبر في العالم ونأمل عدم استخدامها.  ‏من يبيعهم سلاحاً نووياً سيُقصف هو نفسه، إذا باعوا سلاحاً نووياً، فقلة قليلة فقط قادرة على ذلك، ستُقصف.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79132" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79131">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب عن إيران: سوق الأسهم رائع للغاية. وفي كل مرة قلنا فيها شيئًا مذهلاً، مثل "سنقوم بتسوية الأمر"، كان يرتفع.   وفي كل مرة، في كل مرة قلنا فيها شيئًا سلبيًا، مثل، "خمنوا ماذا، لن نكون قادرين على تسوية الأمر"، كان ينخفض — بشكل كبير جدًا، كبير جدًا جدًا. …</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79131" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=pKgtpxYp7N8b31uvawE9HPXg-3EbqXM6OEK6ErGMYTTtc8RB_qIoOLFI64YMeN8QvdlZlfLI6BfD8LSwIzm0yNQ_Q9YUKf8l4sq8kzyVsRlCrBAws5wf7TFZfIovfKU4Dwvuy1gUOy2MPTFioYA4mrS8mkh8yt-4T4tsqVlST0kf55-rwaaFUQUZpF-5Vi4QlJyGFNkjYR86oJMtgqppIipy4ylpAlz0u5IPfUJNuJdiwkXhgnTFdDFIwHRt_8xo3RqyCqwIjdjb_LdY1lcqezP5PpCbydkrWqgkDVUa95JIWXT0DM8BD4SeXFsJ_zAUAtgit6yWFxFZDtLjusnEaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=pKgtpxYp7N8b31uvawE9HPXg-3EbqXM6OEK6ErGMYTTtc8RB_qIoOLFI64YMeN8QvdlZlfLI6BfD8LSwIzm0yNQ_Q9YUKf8l4sq8kzyVsRlCrBAws5wf7TFZfIovfKU4Dwvuy1gUOy2MPTFioYA4mrS8mkh8yt-4T4tsqVlST0kf55-rwaaFUQUZpF-5Vi4QlJyGFNkjYR86oJMtgqppIipy4ylpAlz0u5IPfUJNuJdiwkXhgnTFdDFIwHRt_8xo3RqyCqwIjdjb_LdY1lcqezP5PpCbydkrWqgkDVUa95JIWXT0DM8BD4SeXFsJ_zAUAtgit6yWFxFZDtLjusnEaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نتنياهو ينفعل قليلاً أحياناً، لكنه كان شريكاً جيداً.  ‏نحن الشريك الكبير، وهو الشريك الصغير جداً.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79130" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=WncXcFefZan0MSVcCwAQemYZluAJzlNhgOmKRSHT6XDO9DDdA0MBPXv1qxAUab8-JBEsGuKT8BkVoWoIZVIexUuDDWh2D66oT6bPxNIIdBzYf80jit02IGWgNAaf9E29BEUlQyKGCAG6CHVfEeJWT_SgcthQelteYIYAlgnHsx2KfARhLKlggxZFrDE2gow-UC7FAkZ2ULlF1zevTunX6L9Zm7bw0wV8iHdVc68mpx8aQwA40ACw4vGReDNjyv3EN0AocdYHlpb_yKbnBMMWkhkAfhUvaI4-vLAH4Qai5hmkjxanu2GQXIB0KtjUHBq17wYO55crA2nGuYPonSgBcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=WncXcFefZan0MSVcCwAQemYZluAJzlNhgOmKRSHT6XDO9DDdA0MBPXv1qxAUab8-JBEsGuKT8BkVoWoIZVIexUuDDWh2D66oT6bPxNIIdBzYf80jit02IGWgNAaf9E29BEUlQyKGCAG6CHVfEeJWT_SgcthQelteYIYAlgnHsx2KfARhLKlggxZFrDE2gow-UC7FAkZ2ULlF1zevTunX6L9Zm7bw0wV8iHdVc68mpx8aQwA40ACw4vGReDNjyv3EN0AocdYHlpb_yKbnBMMWkhkAfhUvaI4-vLAH4Qai5hmkjxanu2GQXIB0KtjUHBq17wYO55crA2nGuYPonSgBcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: أبلغنا الإيرانيين بأننا سنعود للقصف إذا لم يلتزموا.  ‏القادة الجدد لإيران أذكياء، بل أذكياء جداً. ‏إنهم أقل تطرفاً بكثير. أعتقد أنهم يحبون وطنهم حقاً. إنهم طيبون.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79129" target="_blank">📅 19:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=ARiOOOIFpLwrCiABQtd04KBD_xLIOjIrklCmiZd4BO94YxI-8omuE_gh_gxWkV4KASBdZVumjBXqLTuUIb8m6TXKqCAn1XlCoD9IYTTVO1UzU0VQXkYNuJ_b-6I1WjfPcX5fblHny_aFW6FtWbMLNwK-R0g62cocb8T52Tpx3euBXqe67DDSbQ6pamyutMlb0cXhxztlJhD0i8CRBHZdXl_tOSos7dMVs84E_qXs1as4cadKyy8xARLWStNz6T0FG02OdHjX0yJj0G0-Y9TyTOk768K_q36PoL7l9_IqcKZkGgOxG1MrMSaLZTL5shFuBhfeZA6szDnkfMQxTdTgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=ARiOOOIFpLwrCiABQtd04KBD_xLIOjIrklCmiZd4BO94YxI-8omuE_gh_gxWkV4KASBdZVumjBXqLTuUIb8m6TXKqCAn1XlCoD9IYTTVO1UzU0VQXkYNuJ_b-6I1WjfPcX5fblHny_aFW6FtWbMLNwK-R0g62cocb8T52Tpx3euBXqe67DDSbQ6pamyutMlb0cXhxztlJhD0i8CRBHZdXl_tOSos7dMVs84E_qXs1as4cadKyy8xARLWStNz6T0FG02OdHjX0yJj0G0-Y9TyTOk768K_q36PoL7l9_IqcKZkGgOxG1MrMSaLZTL5shFuBhfeZA6szDnkfMQxTdTgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:  حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.  ‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.  أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.  ‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه -…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79128" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=jDRQ-2527DV5fnDBT1IbTaH9gvyT4SlMjRi6kFn0ZAAbWjxVOekzZKZP7DnnszN1_FoWAmdPrJKWOjFLuqLdyFSAtwGYJV21o7DpilJ9RUjKewhU2Clicxv8oIa_68xoJvh30g9JPKBW-31tMFzAQBYD_MP4J64NibHoWGg7ordsGAHG5PJRDYb-BD2rZAE_yjFhgg68khxIhlRr22u7-nMu425rD_zuqdlSp0kjsNDUAajTK6cijDOK6_qVptavjIwDA4ogUXnFFwosXge57Qt1SUq6YKSBePS2cF5kDvnFIG_QLU5ZWCVwpTwaSH6sWR3F8KU8OEzP1AepklEW6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=jDRQ-2527DV5fnDBT1IbTaH9gvyT4SlMjRi6kFn0ZAAbWjxVOekzZKZP7DnnszN1_FoWAmdPrJKWOjFLuqLdyFSAtwGYJV21o7DpilJ9RUjKewhU2Clicxv8oIa_68xoJvh30g9JPKBW-31tMFzAQBYD_MP4J64NibHoWGg7ordsGAHG5PJRDYb-BD2rZAE_yjFhgg68khxIhlRr22u7-nMu425rD_zuqdlSp0kjsNDUAajTK6cijDOK6_qVptavjIwDA4ogUXnFFwosXge57Qt1SUq6YKSBePS2cF5kDvnFIG_QLU5ZWCVwpTwaSH6sWR3F8KU8OEzP1AepklEW6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:
حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.
‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.
أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.
‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه - كل شيء وأكثر من ذلك بكثير.
‏أعتقد أن القادة الإيرانيين سيتصرفون بشكل مختلف تماماً.
إذا لم نقم بهذه الصفقة، كان بإمكاننا إسقاط المزيد من القنابل لمدة أسبوعين أو ثلاثة أو أربعة أسابيع أو سنتين أخرى.
لو واصلنا القتال ما كان مضيق هرمز ليفتح إطلاقا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79127" target="_blank">📅 19:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
مشروعهم في لبنان إنهاء حزب الله عسكرياً وثقافياً وسياسياً واجتماعياً وشعبياً ليسهل لهم ابتلاع لبنان، ونتنياهو أعلن صراحة أنه يريد إسرائيل الكبرى.
لم نمكن إسرائيل من تحقيق مشروع إسرائيل الكبرى فنحن كسرناه.
عدد آليات العدو المستهدفة 518 آلية وعدد الطائرات المستهدفة 85 حيث أسقطنا 12 مسيرة و12 محلقة وأصبنا مروحية.
لا وجود لمناطق صفراء أو حمراء وعلى إسرائيل أن ترحل.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79126" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
وكالة إرنا: لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79125" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ يوم الجمعة 19 يونيو/حزيران. ولا تزال آلية إضفاء الطابع الرسمي على الاتفاق قيد المراجعة من قبل الجهات المختصة في البلاد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79124" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY9U2EUep5GEHr1LVlas0uHFzeOQIZbQ0i2P53uRf4UrJ-Nw9iyDAO9Lo-YFxvtovYI6IC3ti4KYRlUPqxORWywmj7B9bKcqp86ZeIPVP5CQU8TDQmE4qBbMi47PFTZ0K7Tj87LKcyCqw9QhhE7h0VEVV5M9gXE8-nvCWVXwWJawhL85tTPTnX7keowji61id3wSZwU3rNOuVku-0tokzbmadWY_nAqohcTkyLUtnfA-kEn2dmCm-y92O56izyDajWARU37zuru4opIwbRwvRn5NcvMGGiVb_-iLxsym6B45ZP1L5d6eVNrwDms8JFsV7DIcX7zyAB6R9R7zqtMyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الغاء رحلات جوية من مطار النجف الأشرف في العراق إلى عدد من المدن الإيرانية دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79123" target="_blank">📅 18:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79122" target="_blank">📅 18:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=kdISkKEtfEyIMXEkHOF9GZ1Jx1wo2vhigEV6yiLkPkbBXDERvygONaRkAkxjg94JaKul4xXzdGAbzWe4Ni5o7ReMuH9RW2fjdkMm1kDnPiNucGUzTbLq95IlyWA5L1uUzM_ySyb3RTPibfHZ8s2Aqwp78c4pyb888ENRrHlbsp0-cCZWntPDI4w1qXJnH6FKIxIjUlHoFLd8n__4ZpHvd8BMJlsUsQoMHjJZz8RbS0YgU25HvpzgFINC5G-TeQ66lh7sqRxG-sQS518jIyrZ847ijgnjY4oj-HhjnE7rmIXbxxInD2c9fKFxz-kTPJa5wKN123XlJoaZSEgIQi7m-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=kdISkKEtfEyIMXEkHOF9GZ1Jx1wo2vhigEV6yiLkPkbBXDERvygONaRkAkxjg94JaKul4xXzdGAbzWe4Ni5o7ReMuH9RW2fjdkMm1kDnPiNucGUzTbLq95IlyWA5L1uUzM_ySyb3RTPibfHZ8s2Aqwp78c4pyb888ENRrHlbsp0-cCZWntPDI4w1qXJnH6FKIxIjUlHoFLd8n__4ZpHvd8BMJlsUsQoMHjJZz8RbS0YgU25HvpzgFINC5G-TeQ66lh7sqRxG-sQS518jIyrZ847ijgnjY4oj-HhjnE7rmIXbxxInD2c9fKFxz-kTPJa5wKN123XlJoaZSEgIQi7m-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇳
‏ترامب: سنساعد الهند إذا تعرضت للهجوم.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79121" target="_blank">📅 17:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1WutjXksMET2Ru9E9lCsu74S8BIF7aBINqf7GgcXInY5mtC0cpoSOlfQ_Hevj_ewTcBDtI-7InXXSnmtQtogCUWHl97Xu3pj_vzYzSvjA8N6xe26Qx6R3FY4LOFZh8XgWC2nddErg8rxUTYeuvDDEqZ9fYdZ4NUxWvyLX0DRQDOy6HOT6DOeAl3Tnv8icin_dQ9wZd1Z4qbXaeVRnets7rUPZZ142Jbzy3VZo7t_D-kEeX-RV1EtPTsl33uK_jCXngVTwechV9BRzvFa6pfVv0QigcM5SChanyjdfOnJy2yieps_dHHSFkjcGi6u1vdauXppnPdkFDEbumCxnr5GdMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1WutjXksMET2Ru9E9lCsu74S8BIF7aBINqf7GgcXInY5mtC0cpoSOlfQ_Hevj_ewTcBDtI-7InXXSnmtQtogCUWHl97Xu3pj_vzYzSvjA8N6xe26Qx6R3FY4LOFZh8XgWC2nddErg8rxUTYeuvDDEqZ9fYdZ4NUxWvyLX0DRQDOy6HOT6DOeAl3Tnv8icin_dQ9wZd1Z4qbXaeVRnets7rUPZZ142Jbzy3VZo7t_D-kEeX-RV1EtPTsl33uK_jCXngVTwechV9BRzvFa6pfVv0QigcM5SChanyjdfOnJy2yieps_dHHSFkjcGi6u1vdauXppnPdkFDEbumCxnr5GdMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب: نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79120" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">المجلس الإسلامي الأعلى في العراق:
استجابةً لنداء الوفاء.. بلدية طهران تُلبي مطالبات المجلس الأعلى وتشهد بغداد تشييعاً مهيباً للقائد الشهيد الامام الخامنئي*
استجابةً للمطالبات والنداءات الروحية والوطنية المتكررة التي أطلقها المجلس الأعلى الإسلامي العراقي، وتأكيداً على عمق الروابط الوجدانية والجهادية التي تجمع الشعبين الأبيين، أعلن رئيس بلدية طهران رسمياً عن تلبية هذه الدعوات المباركة.
حيث تقرر أن تشهد أرض العراق الطاهرة ،أرض المقدسات والشهادة مراسم تشييع جثمان القائد الشهيد، الامام الخامنئي، وذلك في تاريخ 8 تموز (يوليو) 2026.
وتأتي هذه الخطوة التاريخية تلبيةً لقلوب العراقيين التي نبضت بالوفاء لقائدٍ عاش مدافعاً عن قضايا الأمة، ليمتزج تراب العراق بفيض وداعٍ مهيب يليق بمقام القائد الشهيد، وسط ترقب واسع لمشاركة ملايين المحبين والمقاومين في هذا الوداع الأخير.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79119" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13deced209.mp4?token=S5-26y4Nt4V31UrZ7BQFgOX89WZMGIY-X83xvPbfIT5xZY4xuHlzAh-5CBlRtDtfIh4mrUucH2YaZqiVavUeUQhwENPOsiquVm9ELoOJDZhVr1Qbry1YB5VzV5JN1kBxM__SbSYRYAkgs4ruXRZ-oEHdFVEqfPWq3RSprgLcuiUXuavylOhWOlMXllQZd5CcmN5Su2qIuEXLHDqaJFO3CPpZ9dF7o1P5XD3Y09r2dUlVKqG1B2GovOW5sauTcuuvpW5C6z7-mjv6FxNqPpx60EEs4JxsnjHbi7RtgT32v7dO6dMGht_QtLQIly2IWQLQ3mXUAcZo4INvlsOK2VG1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13deced209.mp4?token=S5-26y4Nt4V31UrZ7BQFgOX89WZMGIY-X83xvPbfIT5xZY4xuHlzAh-5CBlRtDtfIh4mrUucH2YaZqiVavUeUQhwENPOsiquVm9ELoOJDZhVr1Qbry1YB5VzV5JN1kBxM__SbSYRYAkgs4ruXRZ-oEHdFVEqfPWq3RSprgLcuiUXuavylOhWOlMXllQZd5CcmN5Su2qIuEXLHDqaJFO3CPpZ9dF7o1P5XD3Y09r2dUlVKqG1B2GovOW5sauTcuuvpW5C6z7-mjv6FxNqPpx60EEs4JxsnjHbi7RtgT32v7dO6dMGht_QtLQIly2IWQLQ3mXUAcZo4INvlsOK2VG1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل:
هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب:
نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79118" target="_blank">📅 17:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله:
بسم الله الرحمن الرحيم
(يَا أَيُّهَا الَّذِينَ آمَنُوا إِن تُطِيعُوا فَرِيقًا مِّنَ الَّذِينَ أُوتُوا الْكِتَابَ يَرُدُّوكُم بَعْدَ إِيمَانِكُمْ كَافِرِينَ * وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ آيَاتُ اللَّهِ وَفِيكُمْ رَسُولُهُ ۗ وَمَن يَعْتَصِم بِاللَّهِ فَقَدْ هُدِيَ إِلَىٰ صِرَاطٍ مُّسْتَقِيمٍ * يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ حَقَّ تُقَاتِهِ وَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسْلِمُونَ)
مع اطلالة شهر محرم الحرام ودخول أيامه المثقلة بالأسى والبطولة، حيث تجسَّدَ جهاد الإمام الحسين (عليه السلام) وأهل بيته وصحبه بأوضح صوره في طف كربلاء، وأثبتوا فيه أن «الجودُ بالنَّفْسِ أَقْصَى غَايَةِ الجُودِ»، لتبقى تلك التضحيات العظيمة منارةً تضيء درب الأحرار في كل زمان ومكان، وتعلّم البشرية جمعاء أن الحياة بلا كرامة لا قيمة لها، وأن الثبات بوجه الطغاة أمر إلهي لا يجوز تركه أو الحياد عنه مهما بلغت التضحيات وعظمت البلاءات.
وامتداداً لهذا النهج الحُسيني الخالد، ننهي جولةً أخرى من جولات الحرب ونخرج منها بانتصار ناجز، وندرك تماماً أن المعركة لم تنتهِ بعد، وأن أمامنا جولات ومحطات هي أكثر خطورةً وضراوةً؛ لذا، يفرض علينا الواجب والوعي أن نكون على أهبة الاستعداد لأي طارئ، متمسكين بسلاحنا، وأيدينا على الزناد.
إن هؤلاء الأعداء من الوحوش البشرية لا يمكن الوثوق بعهودهم أبداً، وأن التغافل عن مكرهم هو الغباء بعينه؛ فالمعادلة واضحة: لن يرضوا عنا ولن نرضى بظلمهم، فكيف نرضى عنهم وقد قتلوا إمامنا الخامنئي في وضح النهار وبين ظهرانينا، وقتلوا العبد الصالح عروة المجاهدين الوثقى السيد حسن نصر الله، واغتالوا علماءنا، وحصدت آلتهم الإجرامية أرواح عشرات الآلاف من شيوخنا، وشبابنا، ونسائنا، وأطفالنا في غزة، ولبنان، واليمن، وإيران، وسوريا، والعراق؟!
فأيُّ صفحة تُطوى؟ وأيُّ جريمة تُنسى؟ وأيُّ مجرم يُسامح؟! لا سامحَ الله من يسامحهم. إن قتالنا مع الباطل ممتدٌ وفي معارك صفرية تطيح بها الرؤوس وتحذف فيها دول، ليرتسم من خلالها عالم جديد، ونحن نعلم يقيناً أيَّ عالم نريد؛ عالم تسوده العدالة والكرامة وتتحطم فيه عروش الظالمين. إنها معركة الحق ضد الباطل، ولن تنتهي حتى قيام الساعة.
أما أولئك الذين وقفوا مع الخنازير وأبناء القردة، فعليهم أن يترقبوا أمر الله وحكمه فيهم، فلا نامت أعين الجبناء والخونة، وأنّ خدعة (الصفحة الجديدة) لن تنطلي علينا، (يُخَادِعُونَ اللَّهَ وَالَّذِينَ آمَنُوا وَمَا يَخْدَعُونَ إِلَّا أَنفُسَهُمْ وَمَا يَشْعُرُونَ).
وفي الختام، نتوجه بآيات الفخر والاعتزاز والامتنان إلى صناع النصر وبناة المجد:
شكراً لحزب الله، درة تاج المقاومة الإسلامية وعنوانِ عنفوانها.
شكراً للقوات المسلحة الإيرانية الشجاعة.
شكراً لرجال اليمن، أهل الصدق والوفاء.
شكراً لكل أبناء المقاومة الإسلامية في فلسطين، والعراق، والبحرين، وأرض الحجاز عامة، وخاصة أهل الشام.
وشكراً لمجاهدي التبيين الذين أبلوا بلاءً حسناً في معركة الحق، ولكل الأحرار من سياسيين، ورجال عشائر غيارى، وعلماء دين مخلصين، وإلى شعوب أمتنا الإسلامية الذين نصروا قضايا الأمة العادلة، مجسدين أسمى معاني التضامن والوحدة في هذه المرحلة المصيرية.
وعظيم الامتنان والتبجيل لمراجعنا العظام الأعلام، الذين وقفوا موقفاً تاريخياً، مشرفاً، شجاعاً، وواضحاً لا لبس فيه؛ فبيّض الله وجوههم في الدنيا والآخرة كما بيّضوا وجوه الأمة، وجزاهم الله خير الجزاء عن الإسلام وأهله.
﴿سَلَامٌ قَوْلًا مِّن رَّبٍّ رَّحِيمٍ﴾
الأمين العام لكتائب حزب الله
17 حزيران 2026 ميلادية
الموافق لـ  1 محرم 1448 هجرية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79117" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-xqLXAGJKrPj24pih3vTxIvytbB31GprNwjWv61Mpva8BspFSRtzzZn0BN2Cb2-WykcwikImFdtSBxMVKE5JaheW39hVM9B2GsvBcctUebvwPCFjqEjh5AAExS2oJko9GSTb5oc9zoiYzU1lERCmeR0M9hv3dbIUkQPzdHF0RkQKmi4FSLoBOA1glDdNWjG2kBnQi3b8HNxRjg0shpnsDYo5AjERFo2JIJApfH26eR_KZ5ZHB9aI8usylP_9zVuOTFXPAs-yfSF_7QpWINjEJWDjhUhJHrtyjxlQhso6I-gshvVyeXaPhgqPPv53-DFHY8WbMwETugar_XD8dTVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
سأعقد مؤتمراً صحفياً خلال 45 دقيقة من فرنسا. ثم سأتوجه إلى فرساي لتناول العشاء مع القادة الفرنسيين والأوروبيين الآخرين، ثم أعود إلى الوطن الليلة! كانت الرحلة ناجحة للغاية، ولكن ما أراد الناس التحدث عنه في الغالب هو حقيقة أن إيران لن تمتلك سلاحاً نووياً، وأن مضيق هرمز سيُفتح على الفور! أرقام رائعة في جميع فئات اقتصاد الولايات المتحدة مع عدد أكبر من الناس يعملون اليوم أكثر من أي وقت مضى. يتم استثمار أكثر من 19.1 تريليون دولار في الولايات المتحدة الأمريكية مع المصانع وكل شيء آخر يحدث، ولكن الأهم من ذلك، أن أرقام سوق الأسهم الأخيرة مرتفعة للغاية بسبب التسوية، وبالمثل، أسعار النفط تتراجع</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79116" target="_blank">📅 17:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي يعلن اصابة 5 جنود صهاينة في جنوب لبنان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79115" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=QGkw5CBKNEABUwtDfgrPpjhwMx-y16dFxhrnTL8_zwAdaUz2mmzrELAYOZCoE4SzR_uBkJU4BGcbzGeRXjJ50-06pQ-3WdHhZooIQg1xKXahHZWo8EgwQdCzxoSsyBAMch0IXmy8z8p4gllWGALAvzvhE64WMzoPGtyIKeJRn0CIhf0GS2e_5Q0W4pYS0jRBJKvQ-2Akg0Y6MhYI5VaZYiW_AljILhH092Qe3T0EVa9FUJNLYsU6Y9C3HhUHSMHfxH3MTPOm2UbVAsQf-xKy7_5PzvQo287L25-hXQmEd-pRaFtW2yHirViCIan0Jigiu-V_TKexAGSbKS8_GeDl3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=QGkw5CBKNEABUwtDfgrPpjhwMx-y16dFxhrnTL8_zwAdaUz2mmzrELAYOZCoE4SzR_uBkJU4BGcbzGeRXjJ50-06pQ-3WdHhZooIQg1xKXahHZWo8EgwQdCzxoSsyBAMch0IXmy8z8p4gllWGALAvzvhE64WMzoPGtyIKeJRn0CIhf0GS2e_5Q0W4pYS0jRBJKvQ-2Akg0Y6MhYI5VaZYiW_AljILhH092Qe3T0EVa9FUJNLYsU6Y9C3HhUHSMHfxH3MTPOm2UbVAsQf-xKy7_5PzvQo287L25-hXQmEd-pRaFtW2yHirViCIan0Jigiu-V_TKexAGSbKS8_GeDl3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79113" target="_blank">📅 16:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79112" target="_blank">📅 16:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79111" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=G_RGnyaAOVqiTVx0CO7sPPr2LdQeZn36Tn1rDGEJ0MghvpuFhk6RO0a9Cul3IfCp-RTkjH5RNfygtWwaaZXfimwFnHYlcRlntSPmUDwK_AK8LqGrJHqZovhbHZ26hXZiMSm1Solet2Xan4r5HoQFk13Wbj4lPPeTHpySL8p4eYBaQRL_mHND_ydy48O33_e2SrwGfDdg71uxGY-wuDBxn8ESPogZGIiYeReDCq4GBAyplMgyArFCajXk99wwW5ZvLsPRCMbfPwlDRndSMkS44L7Wqv5y0AxVngu2Gonrj2EN-5e4AcAx8tOqrS78TthG0TUaaAwsBLzCZ0MffgSOWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=G_RGnyaAOVqiTVx0CO7sPPr2LdQeZn36Tn1rDGEJ0MghvpuFhk6RO0a9Cul3IfCp-RTkjH5RNfygtWwaaZXfimwFnHYlcRlntSPmUDwK_AK8LqGrJHqZovhbHZ26hXZiMSm1Solet2Xan4r5HoQFk13Wbj4lPPeTHpySL8p4eYBaQRL_mHND_ydy48O33_e2SrwGfDdg71uxGY-wuDBxn8ESPogZGIiYeReDCq4GBAyplMgyArFCajXk99wwW5ZvLsPRCMbfPwlDRndSMkS44L7Wqv5y0AxVngu2Gonrj2EN-5e4AcAx8tOqrS78TthG0TUaaAwsBLzCZ0MffgSOWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79110" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الحكومة السويسرية: توقيع مذكرة التفاهم سيعقد بمشاركة ممثلين رفيعين عن الولايات المتحدة وإيران وقطر وباكستان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79108" target="_blank">📅 15:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79107" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWVK6ptbZjJCShRxDMyLq-rV1sZE-LVv-_H3eDW0HB9SFxRpD92tEs2veWW5CblIihH47XoiymZODbiae4EQepEvmOw4C16q_lLuL9ZClw3wGim2rmej1syAVI0PNQl5axe6xw_fqLPtZs1guQMpsg5owFl54XjUcsOBfRK4yHcFC3Foy76I_hlO6fEGWqxbdGd2ndsW1MriNX8-ylLN5ZbkJoJ18GhICXbkMh8qrkr1CxPTPwLp8URPWx-s-33TLpCIN5GLG7jFiYRNpvcZTOT_xiaLWbJaB5aziEiNqUn-GMewUTdiTIRjuy65XuweE3iAf7MaQYSVin1NhbIowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختفوا وابتلعتهم أربيل
!
العشرات من شباب الوسط والجنوب بسبب باج معهم من الحشد الشعبي او صورة لسيد حسن بالهاتف او الشك فقط او العثور على اسمائهم ضمن قوائم رواتب الحشد الشعبي ادى الأمر إلى اختفائهم ، وسط صمت مخزي من القوى السياسية الشيعية الشريكة معهم في الوزارات وتقاسم الكعكة
المواطنون يناشدون الشيخ علي الزيدي مدير الامن والانضباط
بالحشد
و قادة الإطار التنسيقي ومن لا نزال نحسن الظن بهم لا سيما الشيخ
همام حمودي
و
إلحاج العامري وسيد قاسم الاعرجي لمتابعة امر المعتقلين الذين تجاوز عددهم ٧٠ شخص حتى اللحظة
!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79106" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#ترفيهي
الرئيس اللبناني:
لا خوف على السلم الأهلي ومن يهدد به أصبح ضعيفا وهو يبغي إخافة الآخر ليبقى موجودا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79105" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=ETYYE1AJVU7bk8tZrrvlNvN9dDcGmIg866xRj7PkZ8hy-AGdz-sIuIv0DaGXO2jZSqTmaKyUAh-uTNlKeFOgxWoEaIGDoPn4o66SDvub6gCsKb8GSCzh7d_xD5WYNuomokIt-vDonUYSRLp0NGRMUvZiRHiy08VcopWS3ETK9ZE_gRmZ2Mpx4Vnrzr5M-x__4yT7wRwu-shnkgQ6BkxiQgSlcowRBWG2LnTqmmvKduRf2te6mnEb59xDKNFU2G2sSJYmFfsSLGsTx9hAC0JP_GApb8tWsqSyR2GYuWyoFBK3J8mCGxYtVTuFeklsojaTAX2nDa7SZtOxBMfqpBWigQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=ETYYE1AJVU7bk8tZrrvlNvN9dDcGmIg866xRj7PkZ8hy-AGdz-sIuIv0DaGXO2jZSqTmaKyUAh-uTNlKeFOgxWoEaIGDoPn4o66SDvub6gCsKb8GSCzh7d_xD5WYNuomokIt-vDonUYSRLp0NGRMUvZiRHiy08VcopWS3ETK9ZE_gRmZ2Mpx4Vnrzr5M-x__4yT7wRwu-shnkgQ6BkxiQgSlcowRBWG2LnTqmmvKduRf2te6mnEb59xDKNFU2G2sSJYmFfsSLGsTx9hAC0JP_GApb8tWsqSyR2GYuWyoFBK3J8mCGxYtVTuFeklsojaTAX2nDa7SZtOxBMfqpBWigQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
تنفرد نايا بنشر مشاهد في حرب رمضان من مدينة إيلام الحدودية مع العراق تظهر انطلاق صواريخ توم هوك كروز مرورا بسماء العراق ؛ الصواريخ رصدت حوالي الساعة 8.50 بتوقيت العراق …
يوم ٢٨ فبراير</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79104" target="_blank">📅 15:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
محكمة جنايات النجف تصدر حكما بالسجن الشديد 4 سنوات لمدير مؤسسة السجناء السياسيين في النجف</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79103" target="_blank">📅 15:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79102" target="_blank">📅 14:59 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
