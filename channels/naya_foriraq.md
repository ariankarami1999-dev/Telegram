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
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/78005" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uooZuRscRjc2XTRLVWgJA9zayAFX22F_eE190tRI17b2llPgBodA5wLT66QbTa1wU-0b9HoGtdPx49_4ocvcKdeu-f7AaZkyhXZJEynDmgmqOhm1D5v7Zg73-F2_E3msNagd0GIVTpaj1H4uRdUmtS3mK0E7SUo5zA8uo1SRZ4lSbhULs7A7SWUkgrpV-WKLMUqoRksatTStgqdqvAeFEpjL-5-LibyTikc5tctv4VcAqBWcjMi2TI0xSNWp7fM_ZugYQkJ-1nNyrobAMoC4YALjxxCtxVKUGl6zi17IASM9nv24dXsBB11GXRPkI0qHExpSdPCY0SfIvInnRKBRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">It seems MBS wants his country to get f*ck from Iran again
🫣
. PM 8 spotted over the Persian Gulf flight from KSA sky
✈️
..</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/78003" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏مسؤول أمريكي: هاجمت القوات الأمريكية عدة أنظمة دفاع جوي وأنظمة رادار إيرانية حول مضيق هرمز</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/78002" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">😆
We didn’t mention F 15 because Kuwait air system defense are already ready</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78001" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/78000" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-poll">
<h4>📊 Which airplane will Iran destroy this night ?</h4>
<ul>
<li>✓ CH47</li>
<li>✓ UH64</li>
<li>✓ UH 60</li>
<li>✓ MQ9</li>
<li>✓ MQ4</li>
<li>✓ A10</li>
<li>✓ C130</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77999" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مصدر بالحرس الثوري لنايا
ننصح الشعوب المسلمة في غرب اسيا التي تسكن بالقرب من القواعد او التواجد الأمريكي بالابتعاد فورا عنها بمسافة لا تقل عن ١٠ كم ..</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77998" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ايران احد دول القوى العظمى حاليا سوف ترد على امريكا اقوى دولة بالعالم وتهين امريكا مجددا كما اهانت وفرضت معادلة بيروت اسرائيل
وسوف نرى من لا يرحم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77997" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ايران تعلن أنها سترد بقوة على العدوان الأمريكي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77996" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتصدى للاجسام المعادية في سماء بندرعباس</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77995" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تفعيل الدفاعات جوية في بندرعباس</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77994" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب : هذا رد على ما فعلوه بمروحيتنا الليلة الماضية، وأعتقد أن الرد يجب أن يكون قوياً جداً، وهذا ما يمثله هذا الرد."</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77993" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=fvRa8BSsOm0d2IycJmwStELNuz8qWVQ0m6Xm4lhsDxFKIWphVMu35Q5AFKDYmaHncRkxcBS5SimlcK_TPKMFMMYBMDNAc0IO9DMVwK0VBGd55tIkJpjT11S9yh0Xy5ab2D6CqmUeGqHxFkKvg4Xm3hbIj8oHkCki4csbwHuFuZiStAhX05ku3P0NOS4yN_Hb-FWZzi8fXMskVV9aY2IbcwLyyQ4AthWQ3EXGfxTsVacZ0mVaGdDEZ2WMG7jI-lrSvhC9INAMuw8RtblT_WcgBoP_3TUAYK7q1Rl5lnctvX7h1g7J4TtqE_J7uPGbcbhAZ8ZMNt11dFj5_ZAZqMpq8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=fvRa8BSsOm0d2IycJmwStELNuz8qWVQ0m6Xm4lhsDxFKIWphVMu35Q5AFKDYmaHncRkxcBS5SimlcK_TPKMFMMYBMDNAc0IO9DMVwK0VBGd55tIkJpjT11S9yh0Xy5ab2D6CqmUeGqHxFkKvg4Xm3hbIj8oHkCki4csbwHuFuZiStAhX05ku3P0NOS4yN_Hb-FWZzi8fXMskVV9aY2IbcwLyyQ4AthWQ3EXGfxTsVacZ0mVaGdDEZ2WMG7jI-lrSvhC9INAMuw8RtblT_WcgBoP_3TUAYK7q1Rl5lnctvX7h1g7J4TtqE_J7uPGbcbhAZ8ZMNt11dFj5_ZAZqMpq8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77991" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77990" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تفعيل الدفاعات الجوية في جنوب إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77989" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77988" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77987" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77986">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سمع دوي 4 انفجارات حتى اللحظة</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77986" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77985" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77984" target="_blank">📅 00:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77983" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تلقت المنظومات الاستراتيجية في "إسرائيل" توجيهًا لرفع مستوى التأهب تحسبًا لتصعيد محتمل مع إيران.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77982" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
إعلام أمريكي:
قال العديد من أعضاء مجلس الشيوخ إنهم يعتقدون أن إيران استهدفت عن قصد طائرة هليكوبتر من طراز AH-64 Apache تابعة للجيش الأمريكي، ويتوقعون ردًا أمريكيًا في المستقبل القريب.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77981" target="_blank">📅 00:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني مطلع:
لم تُنفذ أي عمليات عسكرية جوية هجومية في مضيق هرمز خلال الـ ٢٤ ساعة الماضية.
إذا ارتكب العدو عملاً إجرامياً آخر بذريعة إسقاط مروحية عسكرية، فسيواجه رداً حاسماً.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77980" target="_blank">📅 00:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c218f38b76.mp4?token=vhJOrsSf2SthfsS2az1RyMhfMEeoD2A5rrmK_u6XcyzyouLhqBfd2LY-qL-9ZZEN46iJcHtUKYkVzAZ4-HdTVkkJBoxo9IZg1wQTJxK9a9ZIqN_U5Zo_y26DCGpU0dRdiqafX-GAe0bX-BW27YpaDgElHPFbcIX4t3dv2PUX1AVMVp_0h3xWjkLQgdydndNs0KYJuvlIcTdz8twcOAoQ9OmrQik2YUdunUZZ9S_4ep_GDrolVnKo2eNU7dFmRBD53HfYBYw7g5o_6u6hR8oOhf8OCwe4YAFGCgbGB_a5qkS-2sAwl25wb9akf-zllxOoO8xvnx9Ytev9xwF5HOxr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c218f38b76.mp4?token=vhJOrsSf2SthfsS2az1RyMhfMEeoD2A5rrmK_u6XcyzyouLhqBfd2LY-qL-9ZZEN46iJcHtUKYkVzAZ4-HdTVkkJBoxo9IZg1wQTJxK9a9ZIqN_U5Zo_y26DCGpU0dRdiqafX-GAe0bX-BW27YpaDgElHPFbcIX4t3dv2PUX1AVMVp_0h3xWjkLQgdydndNs0KYJuvlIcTdz8twcOAoQ9OmrQik2YUdunUZZ9S_4ep_GDrolVnKo2eNU7dFmRBD53HfYBYw7g5o_6u6hR8oOhf8OCwe4YAFGCgbGB_a5qkS-2sAwl25wb9akf-zllxOoO8xvnx9Ytev9xwF5HOxr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
جي دي فانس حول إيران:
قد تتم الصفقة في الأسبوع المقبل، لكن قد تتم أيضًا بعد أشهر من الآن.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77979" target="_blank">📅 23:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭐️
إعلام العدو:
رصد اطلاق صاروخ من اليمن.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77978" target="_blank">📅 23:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
مساعد وزير الخارجية الإيراني: إيران لا تقف وراء الهجوم الذي تعرضت له مروحية أباتشي الأمريكية فوق مضيق هرمز.  هناك احتمال بوقوع حوادث كهذه بشكل غير مقصود بسبب الأجواء المتوترة بمضيق هرمز.  لم يكن هناك أي استهداف متعمد من قبل إيران للمروحية الأمريكية فوق مضيق…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77977" target="_blank">📅 23:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭐️
سماع دوي انفجار مجهول في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77976" target="_blank">📅 23:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭐️
سماع دوي انفجار مجهول في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77975" target="_blank">📅 23:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromأثر</strong></div>
<div class="tg-text">هناك حكاياتٌ لا تُروى بالأسماء، بل بالظلال التي بقيت على الجدران بعد انطفاء المعارك.
في ليلةٍ بعيدة، كانت مدينةٌ صغيرة تواجه العالم وحدها. وكان ثلاثة رجالٍ يتقاسمون خريطةً ممزقة، وقليلاً من الضوء، وكثيراً من الإيمان. لم يكن أحدٌ يسأل من أين جاء الآخر، ولا أيُّ رايةٍ يحمل، فحين يشتدّ الحصار تسقط الألقاب وتبقى الأخوّة.
مرّت السنوات، تبدّلت الوجوه، وتغيّرت الفصول، لكنّ بعض العهود لا يطالها الزمن. تشبه أشجار الزيتون التي تنحني للعاصفة ولا تنكسر، أو البحر الذي يعود إلى شاطئه مهما ابتعد.
لهذا، حين تضيق الأرض بأهلها، يعرفون أنّ هناك قلوباً في الضفة الأخرى من الحلم ما زالت تسهر معهم.
حکایت‌هایی هستند که با نام‌ها روایت نمی‌شوند؛ با سایه‌هایی روایت می‌شوند که پس از خاموش شدن جنگ‌ها بر دیوارها باقی مانده‌اند.
در شبی دور، شهری کوچک در برابر جهان ایستاده بود. و سه مرد، نقشه‌ای پاره، اندکی نور و ایمانی بزرگ را با یکدیگر قسمت می‌کردند. هیچ‌کس از دیگری نمی‌پرسید از کجا آمده است یا پرچم کدام سرزمین را بر دوش دارد؛ زیرا وقتی محاصره سخت می‌شود، لقب‌ها فرو می‌ریزند و برادری باقی می‌ماند.
سال‌ها گذشت؛ چهره‌ها تغییر کردند و فصل‌ها عوض شدند، اما برخی عهدها از دسترس زمان دور می‌مانند. شبیه درختان زیتونی که در برابر طوفان خم می‌شوند اما نمی‌شکنند، یا دریایی که هرقدر دور شود، باز به ساحل خود بازمی‌گردد.
از همین رو، هنگامی که زمین بر اهلش تنگ می‌شود، آنان می‌دانند که در آن سوی رؤیا هنوز قلب‌هایی بیدارند که همراهشان شب را به صبح می‌رسانند.
There are stories that are not told through names, but through the shadows left upon the walls long after the battles have faded away.
On a distant night, a small city stood alone against the world. Three men shared a torn map, a little light, and an abundance of faith. No one asked where the other had come from or which banner he carried, for when a siege grows severe, titles fall away and only brotherhood remains.
The years passed. Faces changed, and seasons turned, yet some covenants remain untouched by time. They are like olive trees that bend before the storm but never break, or like the sea that always finds its way back to its shore, no matter how far it has wandered.
And so, when the earth grows narrow for its people, they know that on the other side of the dream there are still hearts awake, keeping watch beside them through the night.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/77974" target="_blank">📅 23:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
مساعد وزير الخارجية الإيراني:
إيران لا تقف وراء الهجوم الذي تعرضت له مروحية أباتشي الأمريكية فوق مضيق هرمز.
هناك احتمال بوقوع حوادث كهذه بشكل غير مقصود بسبب الأجواء المتوترة بمضيق هرمز.
لم يكن هناك أي استهداف متعمد من قبل إيران للمروحية الأمريكية فوق مضيق هرمز.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77973" target="_blank">📅 23:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
مصدر مطلع مقرب من فريق التفاوض الإيراني:
لم تُرسل إيران أي مقترح جديد إلى الولايات المتحدة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77972" target="_blank">📅 22:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
اندلاع حريق قرب سجن بغداد المركزي مقتربات مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77971" target="_blank">📅 22:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سماع دوي انفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77970" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6702ff2d3c.mp4?token=tOqX3nE4WjjvzsHpjavc40jXGUkrA9pRwoyN7-O-3y8paiQOdfHcak_UQizU_kGrvbbIcKBWbW5x4cQiVX7N6cVfHKhwj7W6FPxbmi0qUezVY6LDidkvNYwxSW_u9KchX9L-1kj6uWO6_-hES8REVqaY8WKCLWLge5HkuTyodHCZQXfuuYg6nH-HjMwVbj20HwAtQlfLkIrCr6lvFkL28jFWX2t4k9uWASY-QYL7Jkl2K_dk4P1ZzuTaGBc5pjOAJL981OJAdh2DpcN8QKnRNtgFhAnM4Cb3EWJNuCR7MvT2V02YTT42W8Hhnc2hQCUfnhh9dChQp-j0nMB6M1Goqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6702ff2d3c.mp4?token=tOqX3nE4WjjvzsHpjavc40jXGUkrA9pRwoyN7-O-3y8paiQOdfHcak_UQizU_kGrvbbIcKBWbW5x4cQiVX7N6cVfHKhwj7W6FPxbmi0qUezVY6LDidkvNYwxSW_u9KchX9L-1kj6uWO6_-hES8REVqaY8WKCLWLge5HkuTyodHCZQXfuuYg6nH-HjMwVbj20HwAtQlfLkIrCr6lvFkL28jFWX2t4k9uWASY-QYL7Jkl2K_dk4P1ZzuTaGBc5pjOAJL981OJAdh2DpcN8QKnRNtgFhAnM4Cb3EWJNuCR7MvT2V02YTT42W8Hhnc2hQCUfnhh9dChQp-j0nMB6M1Goqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي في سماء محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77969" target="_blank">📅 22:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dceed2faf2.mp4?token=Pp2yB6AELJFVJO-YWWofLPZ-wKS2we9YO1H0c5p3zU7ZpVMykivFxUIVgYfFtMWBh8lOh4yzgzw36YRlQIbzIWA8ymuUY7qQQyL0q6Qt3PklvASUHbu79mO9rhdk_6FetBnUKL8NHUsjwq0M_AFSrq0VIn5FSM56c3xGeZAifPz2eOCXqz0c3P2wV2cPhhsNHo6TjL0Cn2mlTdNtfBxOCwxWLMWd238qm6fiU5qzHw-StnuD5nCHSjbHqQJLQWmEs6m7yE2gKRGmplTAvo5YHI5DG1DuM7v9qzRgRv4kGQ0qOwQrKev6ABeBTE_no1gylGSsmAMoPyDOjWSW9ZV-nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dceed2faf2.mp4?token=Pp2yB6AELJFVJO-YWWofLPZ-wKS2we9YO1H0c5p3zU7ZpVMykivFxUIVgYfFtMWBh8lOh4yzgzw36YRlQIbzIWA8ymuUY7qQQyL0q6Qt3PklvASUHbu79mO9rhdk_6FetBnUKL8NHUsjwq0M_AFSrq0VIn5FSM56c3xGeZAifPz2eOCXqz0c3P2wV2cPhhsNHo6TjL0Cn2mlTdNtfBxOCwxWLMWd238qm6fiU5qzHw-StnuD5nCHSjbHqQJLQWmEs6m7yE2gKRGmplTAvo5YHI5DG1DuM7v9qzRgRv4kGQ0qOwQrKev6ABeBTE_no1gylGSsmAMoPyDOjWSW9ZV-nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
تحلق سبع طائرات تزويد بالوقود تابعة لسلاح الجو الأمريكي حاليًا فوق الشرق الأوسط، ست منها تحلق بالقرب من الخليج الفارسي</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77968" target="_blank">📅 22:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سماع دوي انفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77967" target="_blank">📅 22:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نايا - NAYA
pinned «
⭐️
قابل توجه دنبال‌کنندگان ایرانیان عزیز  ما هیچگونه فعالیتی در پیام رسان‌های ایرانی (ایتا، بله، سروش، روبیکا،...) نداریم ؛ در صورتی که تصمیم به ایجاد کانال یا هر گونه فعالیت در این پیام رسان‌ها، از طریق کانال اصلی خود اعلام خواهیم کرد.
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/77966" target="_blank">📅 22:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭐️
قابل توجه دنبال‌کنندگان ایرانیان عزیز
ما هیچگونه فعالیتی در پیام رسان‌های ایرانی (ایتا، بله، سروش، روبیکا،...) نداریم ؛ در صورتی که تصمیم به ایجاد کانال یا هر گونه فعالیت در این پیام رسان‌ها، از طریق کانال اصلی خود اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77965" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsCsNAR26zFvZ2AW7RKGb2tto1pZLkg7sa8PF8dV3P2CQiuT8b5gA0Pi3t0qV9gkZTYeYv2LRlUG80DIZvArJgCoVllLKaVScSEFdg9Jl2sp-v6vF3VGp6-cj1n24qGcx52_hgh3hCgjMew4u2N8m0PbuHdW93ObHVZMX-vtC88s7W3oHkhGJ7I-18zQUCi2cKSMQbwdx7FWoLlOta7ulg4pbQPATsPLGGAB9H1FrLzfquowe28ZHRE6Sg2ka2NYrc5vsH2lMQJb6kuSN3lRgIvYLknu9XhhWNQ9Xe_upHVloyfcU9xwkUzo82uEoWPZgIxYgpruqBHGvdkBh6Izzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
تحلق سبع طائرات تزويد بالوقود تابعة لسلاح الجو الأمريكي حاليًا فوق الشرق الأوسط، ست منها تحلق بالقرب من الخليج الفارسي</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77964" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
عراقجي:
بمجرد الإعلان عن موعد مراسم وداع الإمام المجاهد الشهيد وجنازته ودفنه، وتحديد القدرة الاستيعابية لاستقبال الزوار الأجانب، ستقوم السفارات فوراً بإصدار تأشيرات الدخول للزوار.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77963" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي الإيراني:
القوات المسلحة في أعلى مستويات الجاهزية القتالية والدفاعية، والحمد لله، تم إصلاح الأضرار.
القوات المسلحة على أهبة الاستعداد للتصدي لأي شر أو عدوان على أعلى مستوى.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77962" target="_blank">📅 22:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
مسؤول إيراني:
مروحية الأباتشي الأمريكية لم تكن تحلق فوق المياه الدولية.
سنرد بقوة وبشكل فوري على أي هجوم أمريكي تتعرض له إيران.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77961" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
الناطق باسم القائد العام للقوات المسلحة العراقية صباح النعمان:
عملية حصر السلاح بلغت ذروتها المُلزِمة ولا خيار خارج مظلة القانون.
-إنهاء المهمة العسكرية للتحالف الدولي أواخر أيلول المقبل استحقاق غير قابل للإرجاء.
تكامل منظومتنا الأمنية يشمل البيشمركة كركيزة دستورية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77960" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcMxIF4eihdNiO9Sr8qwFKaxATdbpJ4O1InmYH-UESJBOMsCnMPCG51BPrFjXsQwVF_ggCrQiX8WyjtWYJoZlaPHbI3Njz2U8Uaecmy9reGD-4RPilL-tbzE0hEN-cUlc52yhr_84IS3wN9Dd4x5wmr0h6tbywnPBiPZs2zceKRKkqps1DKlrjqCPMbAbAR7y68sQ-C4I4zf7cEcQ4Cvx29PxKJIGcW4uXgW8h9TRptqfZUicsJ2mSofTJT09q4PzZsg1g7Jm3cZn-HSV-o3zagxJJRwwFhbVnYX_DKmwzDYZ_1tb2Omd7l1bRuOet1KFSZnIHzfG2E_HOMIBNzhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/77959" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77958" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77957" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">We are ready for them …</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77956" target="_blank">📅 21:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8I0EA0-LH3hoNcNm2JwnsT-ScafHhCV5Gu4Fce-MhRKAxQUigFq9hqj16-he5h4eZoPFJ9FvMxp7zHRITGf7hz58omzbosFrPLXobrX9aVhQnAMa8f1s7D-Ht4IP6_v4FUlRJ2HJEWr65k8bCh5OJ-eN8sPZIio7QYcrn3H6axUdFoDnSu3g0SXemtcm6e02hp-Lp5jBQvqpXOxL3qoFOUTX2UiZgDbPHmDBsJPXcK0pSzlJmbS9m5TA9Nf-kobJsrmIq-mJ10UuSuujsZp6Y9eeh3y8yoG_0BuYaq1usTCaS9RP7jl213vDa1_n6vZnQnpySgxKHyNRvJVWcDYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
‏
إن القوات الأجنبية القريبة من أراضينا معرضة لخطر دائم بسبب أخطائها البشرية، أو الحوادث العرضية، أو احتمال وقوعها في تبادل إطلاق النار.
‏لتقليل المخاطر، فإن الحل الأمثل هو رحيلهم.
‏نحن نفضل لغة الدبلوماسية، لكننا نتحدث لغات أخرى أيضاً.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77955" target="_blank">📅 21:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
عضو في البرلمان الإيراني:
إذا كان الأمريكيون يعتزمون انتهاك وقف إطلاق النار أو شنّ أي عدوان، فلن تتهاون إيران مع أي طرف في الدفاع عن نفسها. جميع القواعد العسكرية الأمريكية في المنطقة تقع ضمن نطاق قدراتنا الدفاعية، وسترد إيران بحزم وحسم على أي تهديد إذا تجرأ العدو.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77954" target="_blank">📅 21:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭐️
إعلام العدو:
أمريكا سلمت ايران عبر ابو ظبي ٣ مليار دولار لكي لا تقصف اسرائيل مجددا.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77953" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية فوق نهاريا دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77952" target="_blank">📅 21:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
غير واضح إن كانت المفاوضات مع إيران ستستأنف بعد تعهد ترمب بالرد على إسقاط المروحية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/77951" target="_blank">📅 21:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
إعلام أمريكي:
أفاد مصدر مطلع بأن طائرة أباتشي تعرضت لهجوم بطائرة إيرانية مسيرة من طراز شاهد. كما أكد مسؤولان أمريكيان أن طائرة مسيرة إيرانية هي التي أسقطت المروحية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77950" target="_blank">📅 21:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77949" target="_blank">📅 21:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
ترامب: تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة،…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77948" target="_blank">📅 21:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea4dbbdb9.mp4?token=B1hHcbKrBhjWTcNqto_6RKMqGZ71n4W-98DJ__j1WQ7TgjP4IHOce-s_vRpRQ79ZNF6qPawNCcJseA3w3D5BDr5mk_kBLJgFuxvgUOF10sEklV6dcQ815olMAW43TKpNq5k8Qt7hNXnH89N9SBeX86gM14I2buhTSBJDgCBO4xl9HQp-hxF4mJDfYyiSyRHi7mDaD62xMvJk49mEeFtbKJYm0Wt5s3aXSfCcGWxRI-1ohTgAOlKBrIyeHvOVTeDjui-KEiI38y7GXNyQfD-ZNojQOxbtcTO4Zx5e4XtaPIgyt13KRlfUXYTcZtShdq7QnM1x5zsvGHzvn1qVq6se3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea4dbbdb9.mp4?token=B1hHcbKrBhjWTcNqto_6RKMqGZ71n4W-98DJ__j1WQ7TgjP4IHOce-s_vRpRQ79ZNF6qPawNCcJseA3w3D5BDr5mk_kBLJgFuxvgUOF10sEklV6dcQ815olMAW43TKpNq5k8Qt7hNXnH89N9SBeX86gM14I2buhTSBJDgCBO4xl9HQp-hxF4mJDfYyiSyRHi7mDaD62xMvJk49mEeFtbKJYm0Wt5s3aXSfCcGWxRI-1ohTgAOlKBrIyeHvOVTeDjui-KEiI38y7GXNyQfD-ZNojQOxbtcTO4Zx5e4XtaPIgyt13KRlfUXYTcZtShdq7QnM1x5zsvGHzvn1qVq6se3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجارات تطال خط أنابيب الغاز الرئيسي في جمهورية داغستان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77946" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97029f70e0.mp4?token=sjrKinvUjVPjMlirF4YJf4fgLmsvqn85e52c4zVOpyf_yZRH9N5-YTBsEpVltb7E3P6KNFF0tZ10f0Gqn5DreuHnQtlvLmAgvWybDRbjFjLb2j0YgI-nWcIfyOvappndXkAUuBzK_5zG3eF1PUmKu4d8WYOfyaQU3n4eWIie7Zhlt7UYrif90Ic_75ETXmf4dCHFBZpTuRxXn3i1VetkEwf4o2-wxMIa_aFbzffkkpHvVYV5E19JjDMDnPcbD3lH5EuBs6ys5CFiu8NhArn71SmDiiOPUhMWLkuwci7SaQSyHUtZAf19pReP-L1ydjXBBu_paJwtuCb5pe2Rmng1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97029f70e0.mp4?token=sjrKinvUjVPjMlirF4YJf4fgLmsvqn85e52c4zVOpyf_yZRH9N5-YTBsEpVltb7E3P6KNFF0tZ10f0Gqn5DreuHnQtlvLmAgvWybDRbjFjLb2j0YgI-nWcIfyOvappndXkAUuBzK_5zG3eF1PUmKu4d8WYOfyaQU3n4eWIie7Zhlt7UYrif90Ic_75ETXmf4dCHFBZpTuRxXn3i1VetkEwf4o2-wxMIa_aFbzffkkpHvVYV5E19JjDMDnPcbD3lH5EuBs6ys5CFiu8NhArn71SmDiiOPUhMWLkuwci7SaQSyHUtZAf19pReP-L1ydjXBBu_paJwtuCb5pe2Rmng1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية فوق نهاريا دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77945" target="_blank">📅 20:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تحذير نتنياهو لمجلس الوزراء - قد نضطر للتعامل مع الإيرانيين بمفردنا، دون دعم أمريكي، وبكل ما يترتب على ذلك من تكاليف.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77944" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭐️
‏
شركة CMA CGM للشحن:
تكلفة تجنب مضيق هرمز وصلت لـ 300 مليون دولار في 2026.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77943" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewK9Q1G4lzsCqGuDCDFw-9niVj7eE58DUj_v57ydWxYHWLRhopld1GFveKH97MMtUUTpRwp-TYMjBXTp7Ti9C6ZCoDyNIG1e-6SpbQwrZ0sW5Wu2eKEVZ8D5w-SS0uh2hGprQhfrOgF8l8gxrIMr84VILcP4Ah_O56DLc2W5Qh5MW_bAra4900fTZNH4qCpsS9mwKbYICD3D6WD3kuX9xQvaTvXLUh7FTSsRdOWoE8jvT3FSoyEWiSUKHIul8kQVLafVsU011fYUwJIH6qMoE696ZILaktYQ4CfCukWKUAOjboJra-kCOSZiaS3vrpDTb4KLQqEZ6ixvwE33lBZ-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b837162cfc.mp4?token=BEw7QTqcc3hpBDnh6AYRSeiA-DdPB0idbSB2Ta0nF8yQ1jZGm6xomzqqw04ydSp5z9EMZca_3INlwO--_UBsCexNt-9kyaCQASrV-P0UhPNqhVdKKYVrtvUseE2MlYGI5mHYcDDqDkoviQeWC231Vy_7aneHW1ee1zI-GezWy0MUudnz1Q1jIJij-p5xca1N26XWlUPSej9NJcm5_OSkLEx8CrX2-E6hr3AJ33YhcFUZEIA3AAt670N06TTdT2wasYO3HvJZ8Moi-R0m8_p2rqp10mT6mSaztJpjtWvWC3OQ0lEP-VyKDfiPTgNg1oULBqdX-ZsT4III6CvRbgjzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b837162cfc.mp4?token=BEw7QTqcc3hpBDnh6AYRSeiA-DdPB0idbSB2Ta0nF8yQ1jZGm6xomzqqw04ydSp5z9EMZca_3INlwO--_UBsCexNt-9kyaCQASrV-P0UhPNqhVdKKYVrtvUseE2MlYGI5mHYcDDqDkoviQeWC231Vy_7aneHW1ee1zI-GezWy0MUudnz1Q1jIJij-p5xca1N26XWlUPSej9NJcm5_OSkLEx8CrX2-E6hr3AJ33YhcFUZEIA3AAt670N06TTdT2wasYO3HvJZ8Moi-R0m8_p2rqp10mT6mSaztJpjtWvWC3OQ0lEP-VyKDfiPTgNg1oULBqdX-ZsT4III6CvRbgjzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
صور الأقمار الصناعية تظهر أضرار في رصيف نقل الغاز الطبيعي المسال التابع لشركة أدنوك داس آيلاند في أبوظبي بالإمارات؛ ‏يظهر على اليسار ضرر أصغر في صندوق التبريد، بينما يظهر على اليمين سواد أكثر وضوحًا على المعدات المساعدة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77941" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
ترامب: تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة،…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77940" target="_blank">📅 20:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭐️
نيويورك تايمز:
كانت إحدى العقبات الرئيسية في التوصل إلى اتفاق مع إيران هي مطالب ترامب المتغيرة وإحباطه من عملية التفاوض.
وفقًا للوسطاء، شعر ترامب بالإحباط بسبب عدم قدرته على التحدث مباشرة مع المرشد الأعلى الإيراني، مجتبى خامنئي، وبسبب بطء وتيرة المفاوضات من جانب طهران. ويقولون إنه قام مرارًا وتكرارًا بتغيير الشروط التي ناقشها فريقه بالفعل مع المسؤولين الإيرانيين.
في الجولة الأولى من المحادثات بعد وقف إطلاق النار في أبريل، أفادت التقارير أن مبعوثي ترامب - ستيف ويتكوف وجي دي فانس - اقترحوا اتفاقًا تعلق إيران بموجبه تخصيب اليورانيوم لمدة 10 سنوات.
يقول المسؤولون الإيرانيون إنهم قبلوا هذا الإطار، لكن ترامب طالب لاحقًا بتعليق لمدة 20 عامًا، مما ساعد على إخراج المحادثات عن مسارها.
في الآونة الأخيرة، وبينما كان المفاوضون ينتظرون رد خامنئي على مشروع الاتفاق، أفادت التقارير أن ترامب أضاف شروطًا جديدة متعلقة بالبرنامج النووي الإيراني والوصول إلى الأصول المجمدة، مما زاد من انعدام الثقة الإيرانية في المفاوضات.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77939" target="_blank">📅 20:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6QINPBE5dAnZMTXV6ph3aZNCx9YMFaAvotwYm0PwBlB3LUFP95AkPY5akDUTDH2Rbr9JxSlPy-oEEbPka9b3lIa2utfN0_imfOrq0NN98xlYhMcii5scfifqtRKuIF0loG_JI7R_wwt5ndWxuYOkN3b6JNuWwFEDmhjB0e82likmqjBUEgL811mxh8bCSCS1djf9TjUfHSx8U_txsW2k5crkOVqsRdOvm0aymaxtFnw_rJomq7S1Ecy8YjQb8PXLzntQR__hnbqTAD4xWfZ-vk6QAfa1W7phJwtSA1-RMDReeSgKTJu6Z6797quls3CLEPd8UNYJ6kyR7KKPrkDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة، الرد على هذا الهجوم. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77938" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc7W6FPatMFfY5bltFB1LXvxDzZYu11h6WKUzB6rsyoYMtBC-bkaX_Rjqz66GHuj3Kb3DfyXmzS7QhOlhKccmqb1sKDklJBZZJ0Hi-YVRpjXwIcHW3CXCV5unU1xCcHuulkvPkvhDS64tgynqV5akOxx0TBS9FYtobMXRudqty_BsXFYLxj4hwcwRvx6iXZI8emL-TVTa3chCu8ZsuGM-5PjfkSp_BMe3_b8AbuO6MqvyzvIuSRelLH7bxcvk3sUYMYuOCobJfVcUbIjQjWwYMzF6ZB37gugjGDOnUG9f17_aD6m7CVU4GUOaMhdlwaLhqmV5woSMx6vnU9EesT09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية:
تتضح الأمور بسرعة ملحوظة.
‏لقد نفذوا عملية "علم زائف" من خلال نشر طائرة بدون طيار مقلدة من طراز "لوكاس" لضرب مطار الكويت - مما خلق ذريعة مثالية لتسويق أنظمة الدفاع الجوي المضادة للطائرات بدون طيار التي طورتها شركة "باوروس" تحت ستار الحماية من الهجمات الإيرانية.
‏مربح بالفعل!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77937" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czNCc9Q4sPqEhA1n4O4ssgcbEUXg7SCvxJu4UIojyAwtdboc4u8ZrXYZLOFRq-rtCHphvWKCYWGCvk0Vs5bAw7fYohsjm8mXmGaPfJ_eXMfFL5ky-fAueTNdF_1AV5LF8JzPCVQ3QNOCBqI_ER5tdvaME2z5YDo9fdfjenfVgCjZ_VDfVSh5vFqf6CHHv0jnedKikIyZn5q34KeK0Ml4KK4IxUSfnkeySAFj3lb1WNAWE9QbXYEUDgeQh-nATHKN8a15CczOzIdkITI4cFJlmMk6nC4hLunRp_1Q4WoTsj340T4odsD66a1mEK5oZ67ECMYOhUjmNE1WR1Y0YV-rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
‏نُفضّل لغة الدبلوماسية، لكننا نتحدث لغات أخرى بطلاقة أكبر. إذا أخلفتم بتعهداتكم، فسنتحول إلى اللغة التي نُجيدها.
‏أنت تركب الحصان الذي سرجته!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77936" target="_blank">📅 20:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de89130b37.mp4?token=cVYXB49otI8bjbrRQmWPhVXbSzy5LLnN2b2BCsj4RvyiVZoxOoSyN5hlHX64rBSjOw_7cawKcyOk0MVQhIuK1I54baL0-njkJ39BXVoKhjOxsLtA2fj1bT-9rkpGW1BDSGhY7Q09btnZRxdxyFzBu8d9qOHbakjH0KzSG2FPFEtvv0IES3qU_nkoiE2yVxGTRoxgA3Gc1wQ2T9GElGgIIOd60UZLA-KaN-LJ1kCxYIYyv0EVxmuEtetvpjsLH-AquJleEyfBrsjIc5-_SZo5zGRPyqqPMqljVnB5lFIQDbMEeKdxAYpV05-R1kVsNawavRB5-AofHk5wstuQpUhMnW6dEKo7mjoMLgcYu6EzafFm1xr4sdj5SIiFO-yEvLHMrwpZ2fvDdXtHWNilzunyNYd5o0MxpPjZOfSm8qxGKtC-lEei_kCQNVx_VJiRN3GZsGRKmipb2swXgoPUkdWSQbq_RHnTqB2ZqxgYhMpeAfhk2llYg1cU-15lklloz71PcBNfgaDyiLkbSJMsY7SPCdmMNvH5YhrJ_EXpVmpDxT71j2cFy1QtdJEVg0OwZEBfoNFdQ2qnrCAAW2A3UmEWtrcrLJVCFfBVl4_nenX_BThUAHbAMHz5SR0U0ET3N6-GCsnHeLpWzlzLF1jkQ2hxSeT3j6AT51pgm9AX0jJW6W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de89130b37.mp4?token=cVYXB49otI8bjbrRQmWPhVXbSzy5LLnN2b2BCsj4RvyiVZoxOoSyN5hlHX64rBSjOw_7cawKcyOk0MVQhIuK1I54baL0-njkJ39BXVoKhjOxsLtA2fj1bT-9rkpGW1BDSGhY7Q09btnZRxdxyFzBu8d9qOHbakjH0KzSG2FPFEtvv0IES3qU_nkoiE2yVxGTRoxgA3Gc1wQ2T9GElGgIIOd60UZLA-KaN-LJ1kCxYIYyv0EVxmuEtetvpjsLH-AquJleEyfBrsjIc5-_SZo5zGRPyqqPMqljVnB5lFIQDbMEeKdxAYpV05-R1kVsNawavRB5-AofHk5wstuQpUhMnW6dEKo7mjoMLgcYu6EzafFm1xr4sdj5SIiFO-yEvLHMrwpZ2fvDdXtHWNilzunyNYd5o0MxpPjZOfSm8qxGKtC-lEei_kCQNVx_VJiRN3GZsGRKmipb2swXgoPUkdWSQbq_RHnTqB2ZqxgYhMpeAfhk2llYg1cU-15lklloz71PcBNfgaDyiLkbSJMsY7SPCdmMNvH5YhrJ_EXpVmpDxT71j2cFy1QtdJEVg0OwZEBfoNFdQ2qnrCAAW2A3UmEWtrcrLJVCFfBVl4_nenX_BThUAHbAMHz5SR0U0ET3N6-GCsnHeLpWzlzLF1jkQ2hxSeT3j6AT51pgm9AX0jJW6W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
04-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77935" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae1a9c1cd.mp4?token=q9P9ws2MmWsa9P6V6LTJHNC2zpf8iDve9VCRZQSHD1MUnlw9cV3pN0i08GzSjhC0L7_5RyjdZArYqeapfxbdPmjFQMJyxf5LfSI2fZXIyukR0ZqtVybbWafWIa1X849_6fVvDQl78w6qrCUlg_7_KSwJxidUse-GxOSp6YFr3Av1bmUkSXPkmUQwhnxcw85lTvynZ1e0AKt8PC-HCVY0HP3eHGqI-6YAuzb0HUY0FrJDTV2zfQ7f9SEF8vI37IPE5Ufdb9e606AdGcVO3HCyYhObl-rOiqi-dNRoX9mmsg-SAYsSrKHG0QyTOX3pZiTC0ciobI1ARDZ5-a6-X2F-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae1a9c1cd.mp4?token=q9P9ws2MmWsa9P6V6LTJHNC2zpf8iDve9VCRZQSHD1MUnlw9cV3pN0i08GzSjhC0L7_5RyjdZArYqeapfxbdPmjFQMJyxf5LfSI2fZXIyukR0ZqtVybbWafWIa1X849_6fVvDQl78w6qrCUlg_7_KSwJxidUse-GxOSp6YFr3Av1bmUkSXPkmUQwhnxcw85lTvynZ1e0AKt8PC-HCVY0HP3eHGqI-6YAuzb0HUY0FrJDTV2zfQ7f9SEF8vI37IPE5Ufdb9e606AdGcVO3HCyYhObl-rOiqi-dNRoX9mmsg-SAYsSrKHG0QyTOX3pZiTC0ciobI1ARDZ5-a6-X2F-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مرور رتل عسكري كبير في قضاء بيجي بمحافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77934" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية:
لا نتوقع ارتفاع الحركة عبر مضيق هرمز لمستويات ما قبل الحرب قبل أوائل 2027.
نتوقع أن يظل جزء من إنتاج النفط بالشرق الأوسط معطلا حتى نهاية 2027.
الاضطرابات بمضيق هرمز أدت لخفض الإنتاج بأكثر من 11 مليون برميل يوميا في مايو.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77933" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
قوة من الحشد الشعبي تفكك عبوة ناسفة كانت موضوعة على طريق حديثة – بيجي في محافظة الأنبار غربي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77932" target="_blank">📅 19:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRb9wx5wOwyDymiawLN4A7m_9DA04RbGKWl9t0Ds8Kxbg3FIagf0izw-wcNYWAvxp-iySQzwDLgBqz4JoNJ5qPvtCTs4BmF7g7Qfqpng55dH5jTZN_IL0K1YyqksSotEMi8XsHzgH0VsYUdv_U9nLi16eo64Xu33lS-dOeZIad0GK3AwKvzi9uyGONch096jWi-Np5wdU2tVvhn9bjBah88Q0avINLMaXYxn3ynS5m-FpnOmCr8qUKJeCI_O-9mkuHRrTZPsUV7_71PJWu-oiZS6oz9SDTvUvRkRBx5jbO1sTUycdbBwgZ5kui1ec7QzjCqSN6D3cfNoFCX3cQx3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات صهيونية على مرتفعات الريحان بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/77931" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمع دويها في مدينة أصفهان الإيرانية ناتجة عن تفجير ذخائر غير منفخرة ولايوجد حدث أمني.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77930" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
إندلاع حريق بوزارة الصحة العراقية في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/77929" target="_blank">📅 18:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة صلاح الدين توجه بتعطيل الدوام الرسمي يوم الخميس 11 حزيران 2026 استعداداً لإحياء ذكرى جريمة سبايكر.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77928" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0AkWfO_Wgjz97fwNo9USwPJAOKTsFAN1K_WRXtx7F-zAmaDqym_xm_5VH0ib92-TZ3MPhiNDf-GmKWHtqdVj3aoXDsg9WCt1c0rwPQxB0Lh_hfuse4t6K1E9QVeG820l9HSE4snTywQu9nMmATujyohHveT9TnJQsq-2JAPWFYjZbMNfxvgWKQDLZYQGOye4sLH8znqHgqY2LsZqWlpWanDTjniHy2eQILwIz5bOzS7nfOtmY2t9eXG8GcM5ZSyzgUL0bCr9Bkoz3e3u9EamR-fU3GIyIP7CyGM4i7e9N_d1mZVqyl3iKlgja2coLqgX9qxN4um0dIbCGi021bsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب الله يستهدف قوة الإخلاء بصليات صاروخية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77927" target="_blank">📅 18:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجلس محافظة النجف الاشرف يصوت على توصيات لفتح منفذ بري مع السعودية من بينها احالة المنفذ الى الاستثمار!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77926" target="_blank">📅 17:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
‏
رئيس الأركان الإسرائيلي
: الضربة التي نفذناها في إيران كانت تمهيداً لضربة أشد وأوسع بكثير</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77925" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة مرجليوت إيتان ديفيدي:
كان يجب أن تحترق الضاحية الجنوبية في بيروت، إذا لم يتم الرد بشدة على التسلل الارهابي إلى أراضي إسرائيل، فمن المحتمل أننا فعلاً مواطنون من الدرجة الثانية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77924" target="_blank">📅 17:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعلام العدو: حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77923" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اعلام العدو:
حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77922" target="_blank">📅 17:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث سير جديد على طريق (الحمزة - ديوانية) في محافظة الديوانية جنوبي العراق يسفر عن وفاة 4 اشخاص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77921" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
إصابة 48 ضابطا وجنديا في معارك جنوبي لبنان خلال الأيام الـ5 الماضية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77920" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
بعد تحقيق أولي - تفاصيل إضافية عن حادثة تسلل المهاجم إلى أراضي
إسرائيل
في منطقة سلسلة جبال راميم
1. خلال نشاط لقوات جيش الدفاع داخل جنوب لبنان - رصدت القوات إطلاق نار تجاههم. تم إطلاق النار على القوات التي كانت تعمل داخل لبنان، وتبادل إطلاق النار جرى مباشرة على سياج الحدود.
2. بعد أن قضت القوات على المهاجم وفحصت المنطقة، تم العثور على جثة المهاجم في الجيب الإسرائيلي خلف سياج الحدود. أي: رسميًا تسلل المهاجم إلى داخل أراضي إسرائيل - ولكن حسب المعلومات المتوفرة، لم يخترق سياج النظام ولم يدخل إلى المنطقة المدنية. الجيب خلف سياج الحدود هو بالطبع منطقة عسكرية.
3. كان المهاجم الذي عُثر على جثته يرتدي زيًا عسكريًا لحزب الله، وتم العثور على سلاح وسكين بحوزته.
4. في هذه المرحلة لم يتم العثور على أي أدلة إضافية. الفحوصات مستمرة - باستخدام طائرات بدون طيار من الجو، وقوات خاصة وقوات مشاة في الميدان، ولكن حتى الآن لم يتم العثور على شيء</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77919" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📰
أكسيوس عن مسؤولين أمريكيين:
نحقق لمعرفة إن كان إطلاق نار إيراني تسبب بسقوط مروحية أباتشي قرب مضيق هرمز الاثنين.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77918" target="_blank">📅 17:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77917" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCRfIno8ELcg8Lk4aFNDw2YDKYcL-fk66N6F5FLsOmxHmmpxp7NicI2oGe9jFhTKuNYZ7mq1HKQ1LOt8jz7ahSD60izrs1mVYt1DtYcR7s4ltemOhKh32tmRWiWHO11zahldGwhDZKOXZp4i_mTX9p9lvgzTSf1Y_x3o4z3aG2593s1L3AOifSvlEBeqH3JScpJtPUtMlIXkgq1Hh4xx-hZqgHOGOI3kUPjhkzklbWt4iJTI4IO88pSwFzKwCdmuCAj4_SNxaqOs_qtcatY56VW-Xi29YIu0HP2k42tUvmR2uy18Ciy9DtKaCOi1YrKgT2qFbEpZfsx-abmXUzvhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNOYcDOweqITnY7s0QSTgKlhGLzY7M0cEmbPlEB9RDqCQmlh7-nbiCSUAjTYXZSIUk_JD156sDVMI4E5H8NZy0cftxmEzSJ7P8mqyBVfIPi1sK64xmLmQm7v_LEdi1POv8Rgfxr_xdFX0GPr5W5qr0bGpK_R4jDV7udAQzE7Owbbr9LKR0DJbkw3ief7yPAOPuhu9tEfG5ySjhGgPq4ukPJZNUVNyM_hbUUCFnIWwPElfkyq5Dpg2u67YzKEz2zh1cY9VXMfLYBxlu28J3f1Rk3bpu2-9tIHQJN4lvVA-KDpclFcLc0QwfnUSBi5go7O6ybBN-8Aq6re_lv928Sm7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
البنك المركزي الإيراني يطبع عملة جديدة بقيمة 100 ألف تومان عليها صورة الحرم الشريف للسيدة معصومة وعلى الجهة الخلفية نصب تذكاري لمدرسة ميناب.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77915" target="_blank">📅 16:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئيس وزراء الإسرائيلي السابق
إيهود أولمرت:
المستوطنون بالضفة الغربية ينفذون تطهير عرقي ضد الفلسطينيين في الضفة الغربية بدعم من المسؤولين الإسرائيليين.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77914" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الحكومة البريطانية تعلن عن عقوبات تستهدف شبكات أسهمت في تمويل أعمال عنف للمستوطنين بالضفة الغربية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77913" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
الحكم بالسجن 11 سنة مع غرامة مالية بحق عدد من المستوطنين سرّبوا معلومات لإيران بما في ذلك مواقع القوات، تحركات الدبابات وسقوط الصواريخ.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77912" target="_blank">📅 16:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اعلام العدو: التقديرات تشير إلى أن المسلح كان يختبئ في المنطقة منذ فترة طويلة، وهناك شبوهات قوية تدور حول وجود "خلية كاملة" تتحرك في المكان، ويُحتمل أنه خرج من نفق في المنطقة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77911" target="_blank">📅 16:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: هذا حدث غير مسبوق منذ بداية الحرب، كانت المرة الأخيرة التي تسلل فيها مسلحون من لبنان إلى أراضي إسرائيل في يناير 2024 الى منطقة معزولة. اليوم حدث تسلل مسلحين فعليًا عبر السياج الأمني إلى داخل إسرائيل إلى منطقة مدنية بالقرب من المستوطنات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77910" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">إذاعة جيش العدو: هذا استثنائي بالتأكيد، خاصة في ظل حقيقة أن قوات الجيش الإسرائيلي تحتفظ بشريط أمني بعمق عدة كيلومترات داخل الأراضي اللبنانية مقابل سلسلة جبال راميم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77909" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سيارة في مستوطنة حولون</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77908" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اعلام العدو: تم القضاء على اثنين من مسلحي حزب الله المتسللين في منطقة مرجليوت وهناك مؤشرات على وجود مسلحين إضافيين.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77906" target="_blank">📅 16:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اعلام العدو: مسلح تمكن من الدخول الى اسرائيل واطلق النار على القوات الاسرائيلية من الجانب الاخر من الحدود</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77905" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزيرة خارجية بريطانيا:
على حزب الله إنهاء هجماته وإلقاء سلاحه
.
صار تكرموا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77904" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منصات للمستوطنين تتحدث عن خشية لدى جيش الاحتلال من إمكانية وجود مجموعة أخرى من المقاومين نجحت بالتسلل من لبنان إلى داخل الأراضي المحتلة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77903" target="_blank">📅 15:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77902" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
جيش العدو في بيان: الحدث لا يزال مستمرا. تواصل قواتنا عمليات المسح، بالإضافة إلى طائرات سلاح الجو التي تم إرسالها إلى المنطقة. نحن على اتصال مستمر مع السلطات المحلية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77901" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77900" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
