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
<img src="https://cdn4.telesco.pe/file/DttAYQKfVWPjagU2q5aNNSZCupPBEG2xkyfDLqAcS3yM7qvX69FtYml7LryfnBz_ufzoVCd3XcymPk0vj-DT6ZVxpcDdBcNOn-2N81sA-a6QqbdU2Oj28wiESjNs_poO8B-AAEevsbInmlONAsJovemL0DkwOBzVFM0YmN8WPljWCf8O4SRXJIJqcSC-SihgrbQ4N27gBsaDJvLMYhXTZOhUEaEC2dpG96F_qpATDyGsqRD8e4c88xidx5hW7qfTzvGtmW0DH7fiLDSV8f5APE9uiEK6-hZwIQCFT6aJ4cJkCofjx9HGcXOti4vgs0aFvKNETpQTdESj4R12wUKCQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 250K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUUkn5p6BlU7APyzcR5b5twmy1A7N31bHxgy5Rv41K7xppdHJpDcBCjfdkCT_Tuz5UilSvrREyXZZa-leEjOIwZdUYMMJFW_ymv-sHAB6Dqtg5toR_9V9pqb6xK0ABP4DSzgiCRM6qLvhPLm9WdT9P8lctSmkxYu30QkA-JmSp8RtAHug_tfctwIQC1ax5HG5Q0s5QutfjXexPF6DfuLECRjWxiZO_6IG-WBK0A1m7ePgqS-6-_0KF2KJx0HUR8EMmKHIyaifIKZwhWNSCFsUA8y47coINpKpKcFg3_-muzcZ75S_gAzcgRzgZRJzDltY-ZNtn2qu7v4k0hw2d-tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في إشارة إلى القوة والصمود، تم الإعلان للتو أن عشاء مراسلي البيت الأبيض، الذي انتهى بشكل عنيف ومفاجئ في 25 أبريل، سُجل موعدًا جديدًا في 24 يوليو. هذا الإعلان أمر جيد للغاية لأننا لا يمكننا أن نسمح للأشخاص المجانين بتغيير طريقة حياتنا، أو حتى جدولة مواعيدنا. لقد طُلب مني أن أكون هناك، وأن أتحدث، من قبل وييجيا جيانج، رئيس جمعية مراسلي البيت الأبيض، وقد قبلت. لا أعرف ما إذا كنت سأدلي بنفس التصريحات السيئة أم لا، على الأقل فيما يتعلق ببعض الأشخاص، لكننا سنكتشف ذلك قريبًا. على أي حال، ستكون تذكرة "ساخنة"! ومن المثير للاهتمام، أن المكان سيكون ولدورف أستوريا، في شارع بنسلفانيا، وهو مبنى وقاعة حفلات قمت ببنائها.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/naya_foriraq/76759" target="_blank">📅 21:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10423e85a1.mp4?token=ge9qkYL4058z2LQXXkCc94CFmrka7K8Mpmr4_4kZgxHa3r886bF8WN_CAcoLc7UV2RwyaDrco4P-poNfczEQWG8WAnBZOtsnA3qQ8sjP7DCppg0CoinxNTQIYY6lZl-QAMFvPDr5yO84F_BEBEJLyaBHJLmNUY7HVtXqfQdqgJoyX6LABPiUcOSpdcdsv1-W6FgtZ_BLFWBTvXDRwyO_OOooQXgS7Rajqn2T5zP9orfDry2D3SrFCY4OL7c2WbwIpp5yG4LWOnhFU_lu43rkqLROO1uXAJQi3qSVn23jymWgVVsnJaxQr-ToJ5PgUI09Hy8HqN-iebmF3HlNILHIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في حكومة الجولاني مساجد مدينة حلب السورية تتحول من دور عبادة إلى ساحات رقص.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/naya_foriraq/76758" target="_blank">📅 21:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
مشاهد جديدة من "حرب رمضان" تظهر دمار واسع في مناطق سكنية بالعاصمة الإيرانية طهران بعد تعرضها لقصف صهيوأمريكي غاشم.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/naya_foriraq/76757" target="_blank">📅 21:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
‏
وكالة الطاقة الذرية:
لا نتصور التوصل لاتفاق مع إيران بدون مراقبة برنامجها النووي بصرامة.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/naya_foriraq/76756" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇦
ليلا عبد اللطيف فرع أوكرانيا "زيلينسكي":
قد يكون هناك هجوم واسع النطاق هذه الليلة على أوكرانيا.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/naya_foriraq/76755" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
توقفت وكالة المخابرات المركزية الأمريكية عن المساهمة في بعض التقييمات الاستخباراتية لمكتب مدير الاستخبارات الوطنية، بما في ذلك تلك المتعلقة بالحرب الإيرانية، نتيجة لخلاف دام عامًا بين الوكالتين حول نطاق العمل والمهام.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/76754" target="_blank">📅 20:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKbxo7I7g68qKk2j_gec9NmtmbysmeK5otk3qI2IJ2YwCMPlLWBJQvlTDkexfqVjXGjqCMsazeA_HGDLRssGu2ks9qeo_dcqGeKJwG_mbBzm9rZ6Jco7ieoarswualLfkAsoClQ0gVDDIQwzC4Py4SZ8v-aVz5e70uYHS1OAzjq8MTzjtj4x-1na2BzagWveSH51crYkkpvKwkm30pEqc19dDghWcloM9VHvr6bqltAKj-ty9P6sIeXfGJS4rN3rvfxgscRGrpV62JDUd2IpMa09V9kMC-Rm-8SZ74-rTnRKvuDnvJSHy7Xi_BqkEzL8sggCVAS1_q6SH_HHZSbjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تقارير الأخبار المزيفة التي تفيد بأن جمهورية إيران الإسلامية والولايات المتحدة الأمريكية توقفتا عن الكلام قبل بضعة أيام خاطئة وخاطئة. كانت المحادثات بيننا مستمرة، بما في ذلك قبل أربعة أيام، وقبل ثلاثة أيام، وقبل يومين، وقبل يوم واحد، واليوم. حيث يقودون، لا يعرف المرء أبدا، ولكن كما أخبرت إيران، "لقد حان الوقت، بطريقة أو بأخرى، لكي تبرم صفقة. لقد كنت تفعل هذا لمدة 47 عاما، ولا يمكن السماح له بالاستمرار لفترة أطول!"</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/76753" target="_blank">📅 20:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏴‍☠️
رئيس المؤتمر اليهودي العالمي (WJC)، رونالد لاودر:
منذ 7 أكتوبر، أنفقت جميع المنظمات اليهودية في الولايات المتحدة معًا أكثر من 600 مليون دولار أمريكي لمكافحة هذا الفيضان من معاداة السامية.
هل ساعد ذلك؟ هل منع كل هذا المال - أو حتى أبطأ - الكراهية ضدنا؟
الجواب هو لا.</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/naya_foriraq/76752" target="_blank">📅 20:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD-6buzosN2ycYa2I4KlDOhWvbh9vI9Pr8OyTwNQm7v3f-hu1qLztEs4vslHnZMx9Uzik3Mr0BY7GDE5FvY_BdT6fTCH68hozc9ioZ6nl6n--mcNJ1T894HafFgR_y-xJST3zpANTm6HVJR_L9EyFsB-1fEJ1s9UeD5hH3MGFJzH0z-aWAuRxa0DfrOEAuCNc3PbekuxUi1RQhDpKdOVOmCkkcR1r5KgrUy-78_8tklY9pMp_qeN8yGCpS7uhdL-uMT2mD_i2efOQp9yGyF-YshsSsVbqJBcNa1CoAyQwvjy3DdZ0yuZg2XA_-ka1O0-7enQn2W2FzUBw7gC7sHTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
‏
جيش الإحتلال الإسرائيلي:
سنصدر إنذارا بإخلاء الحي المسيحي في صور إذا لم يتم إخراج عناصر حزب الله.</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/naya_foriraq/76751" target="_blank">📅 20:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اندلاع اشتباكات مسلحة في السيدية بالعاصمة العراقية بغداد ؛ حصيلة اولية مقتل شخص وإصابة اثنين ..</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/76750" target="_blank">📅 20:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25b0f6837.mp4?token=B1vBliOa9dbed24KqRQQuESxNd2-9owzNjzqf7nJ2OeUaw0dL9v-jPaGU4Xtxgc7UQBBtUNat8fK6YIR0y6jbfKTIEYXVUTz0tW9h3aMLU-Mxf6HMMOrrfdOodE52Ql4-u2yyLbRtosdzNByrHYsmTgdM-N2DRR7vympueiizSHzZXXf7f-8FXir6MnvUi8u7fX-IItXDORZicJpOfqUTqX4i1Nr9eXv-RFnjuroJcOOaN_SS0AEsA8HUfzf3iO-TzJMOcv6y87YjfmZF12q9BK0d0LICIsSn5ZVpuKFIjtWXfs1_Q8G00mmYi_svhAqJA2PlgINcMLBBSvoZGfXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25b0f6837.mp4?token=B1vBliOa9dbed24KqRQQuESxNd2-9owzNjzqf7nJ2OeUaw0dL9v-jPaGU4Xtxgc7UQBBtUNat8fK6YIR0y6jbfKTIEYXVUTz0tW9h3aMLU-Mxf6HMMOrrfdOodE52Ql4-u2yyLbRtosdzNByrHYsmTgdM-N2DRR7vympueiizSHzZXXf7f-8FXir6MnvUi8u7fX-IItXDORZicJpOfqUTqX4i1Nr9eXv-RFnjuroJcOOaN_SS0AEsA8HUfzf3iO-TzJMOcv6y87YjfmZF12q9BK0d0LICIsSn5ZVpuKFIjtWXfs1_Q8G00mmYi_svhAqJA2PlgINcMLBBSvoZGfXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي: لقد توددت عُمان إلى إيران للسيطرة على مضيق هرمز.  ‏لن نخفف العقوبات المفروضة على إيران مقابل إعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/76749" target="_blank">📅 19:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0336d45622.mp4?token=AIwNbNseOihNF_7MznJwV1K0fYEC8gXw0egpr5evuSoKCIxp4UqODfOMEmikM-GZ33HCrVPCnvNwzn2HIeNxolppHDSqbljCD6UrpxlpLtmmHLX067cIn_oreQPkFqyZBY1z_q0ZPByJzVNL8cLhNSsSeuBLJsCy16lX0uL-vQqYhkzXtoR4WDVa5wsTfL7LfXI4gFm7TlK10edEf7Ak5cMgi4y_ZIElyeyc889A2YLp1jVwXFBhACszV5jFgqDGLu_I0WY7MLaLe4bHRdkENHSyzRia4p1Jj8kIHpxJrnufKmEdbg9kDyGDaOqZZ0eArNIM8wj1cTWxxA4CSSTpuRJkeHxX0LB5aFVPc-sAKwbc9XGRfIcWXRoTWH-QvzR50P_NcYNcdxD3oQj2Z_S-EsV3hLANEtXBa2ZbD_nYJRvDwBoN3tqaNWjr3Qf3CxFwsfCraHHEXAIfE8l5_wGM5WbV67PT98bCX35CCSE49YK49ZEpt8fezZxzJd1BkyvPcfaw-g7zIDSPWmR9c4gtuuoQK09GHu6qYAVXZvmNVG-yO64dDbBMW8tpjtXyDGPkXcsCHuPLoYPibzw9yeQBMf4ATOBQes3Jn1EkYuFXQNdVp8mRN6GQE-XM14goSOtDgAWtXT_MSMHY1NXy7SPBBT-adnps7hXHRw5ylk1yY-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0336d45622.mp4?token=AIwNbNseOihNF_7MznJwV1K0fYEC8gXw0egpr5evuSoKCIxp4UqODfOMEmikM-GZ33HCrVPCnvNwzn2HIeNxolppHDSqbljCD6UrpxlpLtmmHLX067cIn_oreQPkFqyZBY1z_q0ZPByJzVNL8cLhNSsSeuBLJsCy16lX0uL-vQqYhkzXtoR4WDVa5wsTfL7LfXI4gFm7TlK10edEf7Ak5cMgi4y_ZIElyeyc889A2YLp1jVwXFBhACszV5jFgqDGLu_I0WY7MLaLe4bHRdkENHSyzRia4p1Jj8kIHpxJrnufKmEdbg9kDyGDaOqZZ0eArNIM8wj1cTWxxA4CSSTpuRJkeHxX0LB5aFVPc-sAKwbc9XGRfIcWXRoTWH-QvzR50P_NcYNcdxD3oQj2Z_S-EsV3hLANEtXBa2ZbD_nYJRvDwBoN3tqaNWjr3Qf3CxFwsfCraHHEXAIfE8l5_wGM5WbV67PT98bCX35CCSE49YK49ZEpt8fezZxzJd1BkyvPcfaw-g7zIDSPWmR9c4gtuuoQK09GHu6qYAVXZvmNVG-yO64dDbBMW8tpjtXyDGPkXcsCHuPLoYPibzw9yeQBMf4ATOBQes3Jn1EkYuFXQNdVp8mRN6GQE-XM14goSOtDgAWtXT_MSMHY1NXy7SPBBT-adnps7hXHRw5ylk1yY-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
28-05-2026
آلية لانشر قبة حديديّة تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/76748" target="_blank">📅 19:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbfO3Ug9zLx_PY7Q3tnrmuDltxWTyR4KBT4coGJ4Sf2y7io8dOZJAceO2LTilKSnyI7HSy_b-P3btx5nfIVqYHJF7lC2b1MxXNHAaqdUtYCei4qWiJQwCsrCpvBrY5UILTI1bRt3cqXJ4l1Mx0Dx_UIVCVQOw6-3ZcZ58f9U6GTHCuPC6ai40-x2FeZ_75lpe6f8vHjmK9U5OH4MQimtMqJFLvyWO1G6f3zbtnNuo9jwW_f_7dypQquEqIqpKDfObBIAsdrdB_HbZbGMjaiuDbVxw55m12NtyTc_ja5MmWXFbsj1sR-09B6UyWcEvu9Axlo2v25xAUc7HZYn6Ht0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبرا يا آل صفي الدين فأن موعدكم الجنة</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/76747" target="_blank">📅 19:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🟢
الناطق باسم كتائب القسام "أبوعبيدة":
نحن في مواجهة عدو خسيس لا يقر بحرمات الاتفاقات وأساء قراءة المشهد وأخطأ التقدير.
فاتورة الحساب ستبقى مفتوحة حتى يدفعها عدونا.
قوى المقاومة جرعت العدو الويلات وأبناء لبنان سطروا الملاحم.</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/76746" target="_blank">📅 19:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNBL-4HRj7f70u0kCw91mJTC_DGyCH49mSE9OjXJYUNVyY-m2uxGGrd8_Vyse20BO65ICnZT8OnkHOufG3C7TSp-hiHzezlY87vteR694ozXvGEOi5VNSAKFkatxob2VctDHHkTxGyJydmO_0WE-pZKf5ruHoOTFCZJDgiZeSR0IIVvCsRIpEsNGdW6qi07WR5MKMfJUDafGsRujqhvGQgn6dU8Hfq-4dQqxxhj8tGbT2BjKgJkKRSoPS8qKfKzAPCZx5MWIMRkF6cPexIURZM2qXtV6FB5MgAeks8YbCoCg7EnUl2GkOtaUUSGBsBV-nXvK3hqXxUbepRIqwiky_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدثين أمنيين صعبين في جنوب لبنان ؛ 8 إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/76744" target="_blank">📅 18:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
مصدر خاص لنايا   تم العثور على مبلغ يتجاوز ال ٣ مليون دولار في منزل عدنان الجميلي بصلاح الدين …
😆
واكيد مصدر الأموال مال سلفة ويه نسوان المنطقة</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/76743" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og6Hjo1hW6I9zEnompAQeg4FK6zmh_yjxRkLE1dnDcqLEr-lux1cs8h0GDNxGP6A8qe1Yhb17zdiFyK0dqx5U6qI1Ii4bJtwRmudARjSVQNkv6Kezet3ny-AYRsJ9H424IkkzrcMw5O3JBYtX_Bn97QVi42AakrP2dJ5ti6it6I5rXOkevetiOOM7gaY4P1ru0lQxzWgGv0zwPbIYFWIRSAhMpFeezUfkNBK1fY1JNqhzYu0LRupZG85zX84htFtx1vLXFrtLjvFORvPv2AP2gZ-KFMlRHfIPPJuV2TgllPkmg2i-B4i7matJGXqPy0Ia34RH0LWPOk6No-gSrXxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
كتائب الإمام علي (ع) تقرر فك الارتباط بتشكيلات الحشد الشعبي والمباشرة بإجراءات حصر السلاح بيد الدولة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76742" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:  لا تزال إيران تمتلك الكثير من الطائرات بدون طيار.  ‏ نحن نجري محادثات مع إيران.  ‏وافقت إيران على التفاوض بشأن جوانب برنامجها النووي.  ‏ آمل أن يُعاد فتح المضيق وأن ننتقل إلى حوار حول مواضيع أخرى.  يمكن إبرام اتفاق مع إيران اليوم…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/76741" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدثين أمنيين صعبين في جنوب لبنان ؛ 8 إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/76740" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d84411262.mp4?token=by8qkj_JOuZi2M05OPS4eJ4aldT5jIJ4Z5eQIDj9VTYsxau6wn1YRMYXbFQj8qXh6EnCkRUKuPYbRYMz88mM8kV8gd8By06ILZ_0BeaItHMjFYN2zpec1X57-0_Vwiqv00Xgaj3v4Tonou6D9dwncJYdNEHte9gsQgUEKDAdslHKPAA0jPPZ3FQXg4URpUxF5fMoqLrIcP6y7EEDJv0F_iLnQ24F35e0766hY9neB80-2XGwD2ntAsl31INTMb3vWjIPj3WCBC-A9A4GOifYE7d0Ngq1xoRIp0UNXgrXkUlMhUJB2wBC2y_U6vz5D7EJGnFb0W-gJx3r9bjDkxfZZTeudtgggdoxGdtWr6Q3SW8in3z3yPNSV0-3CwvCpMJzNJKTkNuGNzv6qYPyJ0whVCiBxcwCiFyiwWSzS9z-cJFsD-3qOWmnnNziURJ8a1l74QCQQ1z6SyrI-sL4ONF6cYjjF6cSGgPnfp38EDHbJ6XOIUA9RxNINqwxZwskSXUAkiIXhtqAXdKJ1l49neqcK_VFzY52OKBWS-0aHxihTfaPgxFxFutWX9syp7R02ijiSeP6BUdai6GVWMMXwf74j2rVdAbHE929kxJY14zVsdsYoXbdbJcjpmV-d8JRsMQA4gGHySAw-pLtovozPXdoVsLIDMOjLbQZKNM8ncJDlXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d84411262.mp4?token=by8qkj_JOuZi2M05OPS4eJ4aldT5jIJ4Z5eQIDj9VTYsxau6wn1YRMYXbFQj8qXh6EnCkRUKuPYbRYMz88mM8kV8gd8By06ILZ_0BeaItHMjFYN2zpec1X57-0_Vwiqv00Xgaj3v4Tonou6D9dwncJYdNEHte9gsQgUEKDAdslHKPAA0jPPZ3FQXg4URpUxF5fMoqLrIcP6y7EEDJv0F_iLnQ24F35e0766hY9neB80-2XGwD2ntAsl31INTMb3vWjIPj3WCBC-A9A4GOifYE7d0Ngq1xoRIp0UNXgrXkUlMhUJB2wBC2y_U6vz5D7EJGnFb0W-gJx3r9bjDkxfZZTeudtgggdoxGdtWr6Q3SW8in3z3yPNSV0-3CwvCpMJzNJKTkNuGNzv6qYPyJ0whVCiBxcwCiFyiwWSzS9z-cJFsD-3qOWmnnNziURJ8a1l74QCQQ1z6SyrI-sL4ONF6cYjjF6cSGgPnfp38EDHbJ6XOIUA9RxNINqwxZwskSXUAkiIXhtqAXdKJ1l49neqcK_VFzY52OKBWS-0aHxihTfaPgxFxFutWX9syp7R02ijiSeP6BUdai6GVWMMXwf74j2rVdAbHE929kxJY14zVsdsYoXbdbJcjpmV-d8JRsMQA4gGHySAw-pLtovozPXdoVsLIDMOjLbQZKNM8ncJDlXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
لا تزال إيران تمتلك الكثير من الطائرات بدون طيار.
‏ نحن نجري محادثات مع إيران.
‏وافقت إيران على التفاوض بشأن جوانب برنامجها النووي.
‏ آمل أن يُعاد فتح المضيق وأن ننتقل إلى حوار حول مواضيع أخرى.
يمكن إبرام اتفاق مع إيران اليوم أو غداً أو الأسبوع المقبل.‏
إذا أرادت إيران بيع نفطها عبر مضيق هرمز فعليها إعادة فتحه.‏
أي تخفيف للعقوبات المفروضة على إيران مشروط بشروط.
في المرحلة الثانية على إيران التخلص من اليورانيوم عالي التخصيب.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76739" target="_blank">📅 17:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
31-05-2026
آلية نميرا وناقلة جند تابعتين لجيش العدو الإسرائيلي في بلدة دبل جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76738" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
الاعلام العبري: رسميا رئيس الموساد رومان جوبمان.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76737" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
مكتب المرجع الاعلى السيد علي السيستاني يتوقع 17 حزيران الجاري أول أيام شهر محرم الحرام للعام الهجري الجديد 1448.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76736" target="_blank">📅 17:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76735" target="_blank">📅 17:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzaCzl56fd2eirmmFIxMuC2CBgv290DkGQX2JsIXMHBdAtz4Gnn76T76gssoiwB1XTyEbNeuLvueZLLy_Cw9bx41vBhrFglObPOAam_hNCl7n52g9IsMyvEmHYfJttgzEytYhe3MMAVHdGsMY91XRmPsiBeU1aaFslmtJt_HDNu84Q2n6kMVs1Fsauzc3oMn_ndeXuv5unIL_tieBLMNA51Y_raoNf509Jt6HRDIz48pXVtt3GXpDkoUns7EV0H7uO5F8NHrqQG3quAhVieCH7oH8TL-GbegSvCfDEVKJfgfeA3rq6rmfk92uc6brsS42GgDUaSqig8NVT9Mgk7pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاعلام العبري:
رسميا رئيس الموساد رومان جوبمان.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76734" target="_blank">📅 17:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeItg-oytYQ89LITVPZCCNOj0uItBzeNYid2dyvWVzVD350H-LY0vOzRSZkgpEwbczjKlNGnkZWDcNYzbxY8HTRY5_p28EbOucIsOGtFifyaBn0GHCcjheLq87tMI1Uq79Q3SGiV4HfCyt-jWGYCcQx9rvQvhA_LlStaVKnoYNkiEOMgBbdrIY9bZ2iUZOTzFRWohNVOCqQX6VxVRRpY7JQPKYD-AY79wzCq2jZiYmR_I3TQzP62xFQnT99IYhYO_5FANDz7ya5ymyC-fUwlma70_020au0iG42CEHJ3763KWa4FF_X1jKAw2o6ziBshRE9npz1Z3Qeao4UE30rZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب:
بولت سيتولى منصب مدير المخابرات الوطنية بالنيابة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76733" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt9jKi2ZtCKAZZ0nA11H4I6HhEQmstf2UsbW0a1U78WJr7ZqPqYhilh7_oi3MVOp5EEaVdsAhK4N6IxypNqkJ-Y_prVFgjrFPkW6wBQfhsRV_GifqyLsb6MNnguevp2wQoegySdTMMzCtr3XUzRHcDqwDaISzkFyJJvvwBBHX1_nj2wrRNY-nayEoNi4kf_VqlM9IZX_Z2qbZ_6-cahAH9xRe6SbV6NmCYZV1LC24zFlR9N7CggCMfHtVAlczli6G0xRkaPF-4r52HhRDrlrrI7iWXdH_y4T8vLOQtJO_dPp9uTK1WQcK_PppWBAMI9Bts2Zn6om5PuHSNrkRfTN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بداية جولة المحادثات بين إسرائيل والحكومة اللبنانية في وزارة الخارجية الأمريكية</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76732" target="_blank">📅 16:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇦
‏"أ ف ب"
: أوكرانيا تعلن عمليات إجلاء إجباري لآلاف الأشخاص من عدة قرى في منطقة "خاركيف"</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76731" target="_blank">📅 16:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtcB3QHXfm-BmlpgjZhzQVUKJYH1VO_3aC92TlfqQWJI6xL01RuNpShYs1coAbTlfUKqnKCwjue03toHMPmIpynxt-IzKN0SWvmFcq7B3E8vKQZ9XQmWvwksna9g0vX4hyraBvhgOd6oXmC8-zGyLiWxtl1pwXYkXtV2Kn2q3KHCeeULYzGVUXtnajPrFpu3rtC8MIkmvT3jgzm5J0SAShWHy1lNyrVB7Xe6Q1FoSldrI8Fa6TywlTImxdhak0v1HuSOvd_yvJVkVDXlKuWH4AiIIGQOklARv1q2tW6BTCGh4Veacdc6usjNnRT-eY7DEsvf-rMmLR6TMQ5PwCDUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المدير الذي ظن ان لا احد يستطيع المساس به
وهب الحسني يعيد شكل وزارة النقل العراقية ..</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76730" target="_blank">📅 16:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e25b4b3d3.mp4?token=vylNxzT9CHD6Z_doqDisUkqyoUEVAX41zGmgR92W7ShyVju1UFtnETIW0qud-QfOsuRwvIJuZCxwJvFd2uC6ilRsyKho934HyJxyVTylu0y6m2aXykIar7wvuKZgvkTfoTwWzxo0khd7ytWho-lsrKPI3lGZX4YRgqluUvGiyv0Nli0_sqDcAHc2z7bCDeJvOeb_zksuq2BVGEaZuoir5vfuDxsiPDMAo4FUlUl7Pa51yiB_Vpr-RJKG3HEg1AnTrjbZEeWgQBzl2yu29Wu7hsZEAIPc88NoXFx57IRKRww26QxECXVTDGdEebQNRAB6fBB1xWOe5Jw12mBVKp07gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e25b4b3d3.mp4?token=vylNxzT9CHD6Z_doqDisUkqyoUEVAX41zGmgR92W7ShyVju1UFtnETIW0qud-QfOsuRwvIJuZCxwJvFd2uC6ilRsyKho934HyJxyVTylu0y6m2aXykIar7wvuKZgvkTfoTwWzxo0khd7ytWho-lsrKPI3lGZX4YRgqluUvGiyv0Nli0_sqDcAHc2z7bCDeJvOeb_zksuq2BVGEaZuoir5vfuDxsiPDMAo4FUlUl7Pa51yiB_Vpr-RJKG3HEg1AnTrjbZEeWgQBzl2yu29Wu7hsZEAIPc88NoXFx57IRKRww26QxECXVTDGdEebQNRAB6fBB1xWOe5Jw12mBVKp07gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بريطاني من أصول عراقية يقتل ثلاثة من ذويه، والقضاء العراقي يصدر مذكرة إلقاء قبض بحقه.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76729" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026 مستوطنات نهاريا، كرمِئيل، صفد وكريات شمونة شمالي فلسطين المحتلة بصلياتٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/76728" target="_blank">📅 15:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76727" target="_blank">📅 14:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c179fc637b.mp4?token=atbKa86QfGohXYCb7slog5sKiJLlzpNKiv69Lv1EfyHNDYFLBlmQhEB6TnQGkAXZFqqLFLO1hlLSxPLXLqtn1VWnPbuX-B5ECQIWHytQUBIwRZgoapoDkk0KPq2FgYb3MheY6Nj4X2Dxfp-ODbcxfIPFxLZ5iy4sMVUyHReRuRglylU4DMnZJh4E8ctmNhdxsxQpJBTtnft5eEQkCvlf6MCCpagOmg1tlY0uTpLjr4IsXOG7cj7RcQM_Rb2PUz8HUFMUPIknFn6fBKpqgdi1drdIhvaUfwkGj8EbJ5yqqAzs2UooqMyjwMFHvRhsRQj5Oz6Lmr4CoOA3vnzEDHLifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c179fc637b.mp4?token=atbKa86QfGohXYCb7slog5sKiJLlzpNKiv69Lv1EfyHNDYFLBlmQhEB6TnQGkAXZFqqLFLO1hlLSxPLXLqtn1VWnPbuX-B5ECQIWHytQUBIwRZgoapoDkk0KPq2FgYb3MheY6Nj4X2Dxfp-ODbcxfIPFxLZ5iy4sMVUyHReRuRglylU4DMnZJh4E8ctmNhdxsxQpJBTtnft5eEQkCvlf6MCCpagOmg1tlY0uTpLjr4IsXOG7cj7RcQM_Rb2PUz8HUFMUPIknFn6fBKpqgdi1drdIhvaUfwkGj8EbJ5yqqAzs2UooqMyjwMFHvRhsRQj5Oz6Lmr4CoOA3vnzEDHLifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
السؤال هو: من اين جاء الحلبوسي بـ500 الف دولار ليقدمها كهدية وما هي ثروته الكاملة اذن وما هو منصبه في الدولة ليكون هذه الثروة الطائلة وحتى لو كان لديه منصب هل راتبه يكفي لمنح فقط هدية بنصف مليون دولار وهل مهنة التجارة في الدهن الحر تجارة رابحة الى هذه الدرجة؟!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76726" target="_blank">📅 14:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76725">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الإسرائيلي:
إصابة جنديين بجروح إثر استهداف قوة إسرائيلية بمسيرة في جنوب لبنان من قبل حزب الله صباح اليوم.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76725" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76724" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
وزارة الداخلية البحرينية:
نظرا لاستمرار توتر الأوضاع الأمنية الراهنة منع سفر المواطنين إلى ايران والعراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76723" target="_blank">📅 13:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
مشاهد من عمليات اطفاء النيران المشتعلة في سفينة MSC الأمريكية في المياه الاقليمية العراقية بعد تعرضها لاستهداف صاروخي من قبل الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76721" target="_blank">📅 12:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76720" target="_blank">📅 12:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني: عبرت 24 سفينة مضيق هرمز خلال الـ 24 ساعة الماضية بعد الحصول على تصريح بالتنسيق مع الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76719" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
بعد فشله الذريع ؛ نتنياهو:
لقد تصدعت أركان نظام الإرهاب في إيران. ولن يعود إلى ما كان عليه، وسيسقط في نهاية المطاف
أي متآمر شرير ضد إسرائيل يعلم أن مؤامراته ستفشل. والثمن الذي سيدفعه سيكون باهظًا للغاية. والثمن الذي دفعته إيران بالفعل باهظ جدا
لا يوجد جهاز استخباراتي أو جهاز إحباط أفضل من الموساد. الموساد منارة للقوة البشرية، والتقدم التكنولوجي، والجرأة العملياتية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76718" target="_blank">📅 11:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a980d64c8.mp4?token=XdXJZ1Z5B2KhTkVVXDKYE6wvNy-AU_m5WqFhS91KYz3HAmRQ69XqJ0hr5tBBZHuY66I8SRY1SRopZYmMKUbqcCKxpL3_v7wSs-2ZCKJZVLktGR3EaRComE5uQf1-gHNgF_GeyG_WYA-SQ-OMtnf-gXS1wofehTyJFOHFhVsyOi7jdwW-EpxK679LqnOmsN4bM0biKYcCCT886LERRg_8T7yant7iguAN3VQw3TNBUT1inI21YyWTT6o44MSXsxtwxDSRmBY-OxCNE3oW9QHQ8J6HY6UWUArQ8W2sDTbghZkpWzH9j6N4sqgConv8m-IBr5XNzOiFvPDOJzQhWizv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a980d64c8.mp4?token=XdXJZ1Z5B2KhTkVVXDKYE6wvNy-AU_m5WqFhS91KYz3HAmRQ69XqJ0hr5tBBZHuY66I8SRY1SRopZYmMKUbqcCKxpL3_v7wSs-2ZCKJZVLktGR3EaRComE5uQf1-gHNgF_GeyG_WYA-SQ-OMtnf-gXS1wofehTyJFOHFhVsyOi7jdwW-EpxK679LqnOmsN4bM0biKYcCCT886LERRg_8T7yant7iguAN3VQw3TNBUT1inI21YyWTT6o44MSXsxtwxDSRmBY-OxCNE3oW9QHQ8J6HY6UWUArQ8W2sDTbghZkpWzH9j6N4sqgConv8m-IBr5XNzOiFvPDOJzQhWizv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني ينشر مشاهد من مضيق هرمز الخاضع لسيطرة الحرس الثوري الإيراني وانتظار طوابير السفن للحصول على إذن العبور.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76717" target="_blank">📅 11:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
🔥
⚔️
Another Vision , game of thrones . Hezbollah against IDF ..</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76715" target="_blank">📅 10:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇱🇧
هزة أرضية تضرب قضاء بعلبك في لبنان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76714" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
انفجار يهز جانب الرصافة من العاصمة العراقية بغداد، وأنباء اولية تتحدث عن مهاجمة منزل بواسطة قنبلة يدوية في الراشدية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76713" target="_blank">📅 10:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
تقوم إيفانكا ابنة ترامب وجاريد كوشنر بتطوير جزيرة خاصة ضخمة خارج الشبكة في البحر الأبيض المتوسط.
إيبتسن جديدة
⁉️
😱</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76712" target="_blank">📅 09:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: "الجبهة اللبنانية تُداس فوق رؤوسنا. الإيرانيون يُقيدون أيدي الأمريكيين، الذين بدورهم يُقيدون أيدينا".</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76711" target="_blank">📅 09:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📰
فايننشال تايمز:
تدرس الولايات المتحدة نشر أصول قادرة على استخدام الأسلحة النووية في دول إضافية تابعة لحلف شمال الأطلسي في أوروبا.
على الرغم من أنه لا يُتوقع التوصل إلى اتفاق قريبًا، إلا أن بولندا وبعض دول البلطيق مهتمة، حسبما ذكرت التقارير، باستضافة قواعد للطائرات ذات القدرة المزدوجة القادرة على حمل الأسلحة النووية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76710" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: "الجبهة اللبنانية تُداس فوق رؤوسنا. الإيرانيون يُقيدون أيدي الأمريكيين، الذين بدورهم يُقيدون أيدينا".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76709" target="_blank">📅 08:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa6457510.mp4?token=bwvU56vcQKNwyf1FGk7Yfsao4UpIZuXsktnMpqC3zLaOGNeA7su-3gUfCWXfg0W3Y_hzIeQYREOryLBt3mC6SaS8wuhRl_cCRDQGy6PZPmO-Tw17pJXus7w-XzjO4rWb976HKKPYf5cRDDevV2phR2QNZNjJ12JUluNa2S13hVpeWzoLyTXSSHlhHsGlbUlY63dRQ54w_-g34Uk3BI5YrNWv7cr4fYC_1SIsyhD3CeFMcJrusBchl8Q4ACRtYa7V1Omc-5W1Icp7XiT1ICVDFNlh6AY2xaX0ZzFd5WXXv2cDTZNpO-a0WKV-dIBy4eEv8k7TNoyOnoCQt_lRsjZDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa6457510.mp4?token=bwvU56vcQKNwyf1FGk7Yfsao4UpIZuXsktnMpqC3zLaOGNeA7su-3gUfCWXfg0W3Y_hzIeQYREOryLBt3mC6SaS8wuhRl_cCRDQGy6PZPmO-Tw17pJXus7w-XzjO4rWb976HKKPYf5cRDDevV2phR2QNZNjJ12JUluNa2S13hVpeWzoLyTXSSHlhHsGlbUlY63dRQ54w_-g34Uk3BI5YrNWv7cr4fYC_1SIsyhD3CeFMcJrusBchl8Q4ACRtYa7V1Omc-5W1Icp7XiT1ICVDFNlh6AY2xaX0ZzFd5WXXv2cDTZNpO-a0WKV-dIBy4eEv8k7TNoyOnoCQt_lRsjZDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇷🇺
انفجارات واندلاع حريق كبير في مصنع أوكروبورونبروم للدفاع في كييف بعد قصف روسي كثيف.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76708" target="_blank">📅 08:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDrCsbYazcM90vB3TlbUsAL24LOizw7s4wVOA-WJD4PMvR-tEJMYDYrWg52F6X1pRVuIatIvr1YlOgLJ-vE2WBuMyD3v0wpxE938am-gHceWXl1KUiAgqW5JJHQrlDcyRN7unc3MLSD8HgcAHJkd11T9F8ti7Z25nbojEqL8BH-SwLVCIlSpXhAwtHzG4w-y85_klZcQurIZsF391GDGWeEd53InaHgMpdwWijjR7l3gTbf0hPBs7EOSQ9lJ57o1BDkIpA6N2CN2zjokbOawjX_zJbYmGH7SUytAZG9jJxobJmBkmnjS-Xs7i4anr9ewEEbO5UXu5FvFKB1Fw0a7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
إذا استسلمت إيران، واعترفت بأن بحريتها قد ذهبت وتستقر في قاع البحر، وأن قواتها الجوية لم تعد معنا، وإذا خرج جيشها بأكمله من طهران، وألقى أسلحته ورفع يديه عاليًا، وصرخ كل منهم "أستسلم، أستسلم" بينما يلوح بشدة بالعلم الأبيض التمثيلي، وإذا وقع قادتها المتبقون جميعًا "وثائق الاستسلام" الضرورية، واعترفوا بهزيمتهم أمام القوة العظيمة والقوة للولايات المتحدة الرائعة، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة شينجزي ستريت جورنال (WSJ!)، وشبكة CNN الفاسدة وغير ذات أهمية الآن، وجميع أعضاء وسائل الإعلام الإخبارية المزيفة الأخرى، ستقوم بتغطية عناوين الأخبار بأن إيران حققت انتصارًا رائعًا وذكيًا على الولايات المتحدة الأمريكية، ولم يكن الأمر قريبًا حتى. لقد ضل الديمقراطيون ووسائل الإعلام طريقهم تمامًا. لقد أصبحوا جنونًا تمامًا!!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76707" target="_blank">📅 05:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1AwSPgLL48CVbIjaCQBxBDQWsuoOXEEvpwKfvCbOqscSb3AzaAnDrLe0cfy2OSL1u_q-iJsnmTBvzejF_-N_jnXUm9LwTtdJLVMMCGjAgx5Kdax6GUTldb0xtSQ9W79r73Zx_xoPs7EZ6D0ZKGkLQ6glS_Qkn6fxfp7IGOoXnjfRyobih6D9Y54g6mhxM2bdZ8JD9jAlIW2cC0ryI_1R-S7SSqVfwK6vvrE7jCFh5r1ByIxv15cyXgIYpt__90s3iDKUDGl1yIJLJ5vxYpe4mWMff52Lj1EY1kN5QfRlFzzEayyI-kZegZUM1bXrZq03-_wCWJ-bpEyrMVVbqLyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابات مباشرة لصواريخ حزب الله في مستوطنة شلومي شمالي فلسطين المحتلة ؛جرحى بحالات حرجة في صفوف الصهاينة وإندلاع حريق كبير بالمكان.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76706" target="_blank">📅 03:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✌
👌
👍
ضربة جوية دقيقة للدفاع الروسي
عمود ضخم من الدخان يتصاعد فوق كييف بعد إصدار السلطات المحلية إنذاراً بهجوم جوي.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/76705" target="_blank">📅 02:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770d1e923f.mp4?token=KP3IRcr4hXGcQcQ7ZA050h7Ujthr-UQcgT0qw9w0zUxeGxQ5HntSXymaLrBlpGTC0dn398freaDsUfkUPO-xqdShqLam7Wd6hBHiyHscxyykppZmSMawV_GNFrDgTICCcnkFsN92GqgR2Cxa0D-EX6XodTRVCoiRW_7IEUezVMrldvDNMcrhtunRCygEu43G6gTUg-NYy9qJwLj49VVRubjDrMXSc0WRpCwoq8Bt35NWvAfn4sFFA2X0Rwg93uvJftw_WF7V9Gf-CAePGI5Ht9zamEOY4hjd7H8XThrYNFI8JDiPeBa6ls-mAgMqKHuJDXKWoCx4slMy81G30OyGdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770d1e923f.mp4?token=KP3IRcr4hXGcQcQ7ZA050h7Ujthr-UQcgT0qw9w0zUxeGxQ5HntSXymaLrBlpGTC0dn398freaDsUfkUPO-xqdShqLam7Wd6hBHiyHscxyykppZmSMawV_GNFrDgTICCcnkFsN92GqgR2Cxa0D-EX6XodTRVCoiRW_7IEUezVMrldvDNMcrhtunRCygEu43G6gTUg-NYy9qJwLj49VVRubjDrMXSc0WRpCwoq8Bt35NWvAfn4sFFA2X0Rwg93uvJftw_WF7V9Gf-CAePGI5Ht9zamEOY4hjd7H8XThrYNFI8JDiPeBa6ls-mAgMqKHuJDXKWoCx4slMy81G30OyGdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق رشقة صاروخية من لبنان نحو عمق الجليل المحتل وصولاً إلى محيط بحيرة طبريا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76704" target="_blank">📅 02:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaU5jZn8jFrBFkOB9D5R-j1q-pdwptyXY9PcGUKIOy5ucvMWd-SFAf4SDp5vUx5BEcaIE2cOjKKsCIjw8c-hLTjUn8PH1AlTgyyKBE9TJO5E3VUmDIkuIVqkTEwmEdRqGsI5ZnyZMfcJHsOmASu4GqiH_WiRjPGDzhFxIzjZNb48BbFMX8nXBXZXc0OJoBzLumJHVhvdzVvY4zvmMs6yijOzzIAgxdUFWSWU8mx3zPKn8zvgf40TB6tDvzAH6xRvx7vm_2T0uFye4iQUOpD1uaPyiBVKPp6slrUm7cHqMYYesb2zWzJ4-qUAQYFdlpILYcX08X48dZPoGdUCzsS1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يزعم مخترق على الدارك ويب ان بيانات ٧٥٠ الف مشترك لشركة كورك للاتصالات العراقية تم اختراقها وعرضها للبيع</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76703" target="_blank">📅 01:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIWKDhcJMTvgJw2Rx-xH6JF7-Ka1qQox_9Ip67ZlDeGBX-cwe2tLtwfvpFlDbK7ULW2MiT5_EGvhJZzH0WRvpbUDK3V66xkxZj6wvUyjHgI_XE-3-GHLJMJjk8CFWSEKgZsvwRp2GMpfAQQwvAcXeNRe2GXem3yjE6BiKVvYxz9j6iQoxYdC-qUj9rNqd0HdMZn0hdWquNkZLJsIRc6ERsyUmoG0jo3gty3RYI3FUrg2TfnpXLmU0P5mmn_E-VKU-xgb5fACTLjK820W5E0107bjdnc5JiCCBsnbXbn8KYHjeIzx1sLB9gUh9Y2Bvrldf8nwPMUKTHV3R-Xe27_2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزال كبير يهز جنوب إيطاليا بقوة ٦.٥ على مقياس ريختر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76702" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مقتل جندي أمريكي في قاعدة الحرير اربيل</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/76701" target="_blank">📅 01:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقتل جندي أمريكي في قاعدة الحرير اربيل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76700" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76698" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية
:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/76697" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e03f0c9ce.mp4?token=ObdJo8oETBkiDjjKIFQ6wo0m9pzZzwGymVcQHcyWS-RQc55pLz5FEfnc9uyyGVzeBjPTpu0UBAOxjj2ndRAUP3BHVkbRUEzZsg857g3sbceBDdAKUH_zVbvJTgdaXphmJDUTjV-SInCG3aETwAMitaMmBvxFzPXUsugc_84W_wlgJxtwhwc0aWpb8gSFGzVbesS367dlmi95dD--NJ4ORb6RqFXIdZAUje9MXJWLBygaysXMNC3uyvaka0ViDgxjRbE6To85Lzhs6fPopFWTjlNQwbgL1_wswMYnEafQyw6U5TN5QTDfscTOnvDa_e82SBY0mdoAK7msx_Eh08f_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e03f0c9ce.mp4?token=ObdJo8oETBkiDjjKIFQ6wo0m9pzZzwGymVcQHcyWS-RQc55pLz5FEfnc9uyyGVzeBjPTpu0UBAOxjj2ndRAUP3BHVkbRUEzZsg857g3sbceBDdAKUH_zVbvJTgdaXphmJDUTjV-SInCG3aETwAMitaMmBvxFzPXUsugc_84W_wlgJxtwhwc0aWpb8gSFGzVbesS367dlmi95dD--NJ4ORb6RqFXIdZAUje9MXJWLBygaysXMNC3uyvaka0ViDgxjRbE6To85Lzhs6fPopFWTjlNQwbgL1_wswMYnEafQyw6U5TN5QTDfscTOnvDa_e82SBY0mdoAK7msx_Eh08f_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات التجارة البحرية البريطانية: تم إبلاغنا بوقوع اصطدام ثانٍ لسفينة الشحن في ميناء ام قصر العراقي مما أدى إلى اندلاع حريق تم إخماده. لم ترد أنباء عن إصابات بين أفراد الطاقم. يُنصح السفن بالعبور بحذر والإبلاغ عن أي نشاط مشبوه إلى عمليات التجارة البحرية البريطانية.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76696" target="_blank">📅 01:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
🇮🇶
الإطار التنسيقي: هيئة الحشد الشعبي مؤسسة أمنية رسمية ملتزمة بالدستور والقوانين النافذة وأوامر القائد العام للقوات المسلحة، وتمارس مهامها وفق الأطر القانونية المعتمدة ؛ الإطار يؤدون مشروع حصر السلاح بيد الدولة وفك الارتباط بين هيئة الحشد الشعبي عن الأطر السياسية والحزبية والاجتماعية انطلاقا من الدستور العراقي وتنفيذاً لتوجيهات المرجعية الدينية العليا
ياليت جور بني مروان عاد لنا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76695" target="_blank">📅 01:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚔️
🇮🇶
🇺🇸
نقلا عن إعلام العدو
المختطف العراقي محمد باقر السعدي من نيويورك : دفع قائد "" إرهابي "" مزعوم من كتائب حزب الله ببراءته أمام محكمة أمريكية بعد اتهامه بدعم هجمات على المصالح الأمريكية في أوروبا والتخطيط لهجمات في الولايات المتحدة، بما في ذلك استهداف كنيس يهودي في نيويورك.وخلال جلسة الاستماع، أعلن قائلاً: "نحن في حالة حرب" واتهم الولايات المتحدة بقتل الأطفال بصواريخها.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76694" target="_blank">📅 01:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
ترامب: كان هناك خلل صغير اليوم - كان الإيرانيون مستائين من هجمات إسرائيل على لبنان.لذلك تحدثت إلى حزب الله وقلت لهم لا تطلقوا النار، وتحدثت إلى بيبي وقلت لهم لا تطلقوا النار، وتوقف كلاهما عن إطلاق النار على بعضهما البعض،واتفاق سلام مع إيران قد يكون أفضل حتى…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76693" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
ترامب:
كان هناك خلل صغير اليوم - كان الإيرانيون مستائين من هجمات إسرائيل على لبنان.لذلك تحدثت إلى حزب الله وقلت لهم لا تطلقوا النار، وتحدثت إلى بيبي وقلت لهم لا تطلقوا النار، وتوقف كلاهما عن إطلاق النار على بعضهما البعض،واتفاق سلام مع إيران قد يكون أفضل حتى من نصر عسكري.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76692" target="_blank">📅 01:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇫🇷
مندوب فرنسا في مجلس الأمن: إسرائيل تعزز من سلطة حزب الله بقصفها المدن والبلدات اللبنانية، ولا شيء يمكن أن يبرر استمرار العمليات العسكرية الإسرائيلية في لبنان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76691" target="_blank">📅 01:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXUuQPQvpwr9p8uuRedVPfyjEfJlmBHvFGrrY9YKN5rmMk1dxsE85zgz6eq8kSnDmD-s9I5M2Z16AJDysAcRalfl2REirZJO9tl8lRmiWQvSozwDEVBBty3DHy6LMVu_mf48p--t-eCu5Uaeooow7O53Op18AVglzncdw1sSfi-YAQnnae_nSTb_Q4J2pqApcyrYj67T-sgiDMCN7N6DsgmRUzA9X6O_DmwvER55t0UseTWMphewbPu0K_6ykO9pEx28l5L_gsaP074Cpn1ze4mc1eJOCKLv2Q3bqJx7lr8j1sTRe2ULaXgkTeNqp3F6T7_lYf0AmqJDfnqEjb195A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
قاليباف في حوار مع نبيه بري: أرواحنا وأرواحكم واحدة، والرابطة بين إيران ولبنان لا تنفصم، وإذا استمرت جرائم إسرائيل في لبنان فسنوقف المفاوضات ونقف بوجهها.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76690" target="_blank">📅 01:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">إعلام أمريكي : إطلاق نار في عيادة طبية بكندا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76689" target="_blank">📅 00:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
حزب الله يعلن إعطاب مدرعتين واستهداف دبابة ميركافا خلال تصدّيها لمحاولة توغل إسرائيلية جديدة باتجاه بلدة حداثا جنوب لبنان، مؤكدةً استمرار الاشتباكات حتى لحظة صدور البيان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76688" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇫🇷
🌟
وزير الخارجية الفرنسي:‏فرنسا تطلب اجتماعا طارئا لمجلس الأمن بشأن لبنان، وفتح مضيق هرمز أولوية قصوى لأنه ليس لدينا أي نية لنواصل دفع ثمن حرب ليست حربنا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76687" target="_blank">📅 00:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جلسة طارئة لمجلس الأمن الدولي حول لبنان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76686" target="_blank">📅 00:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
⚔️
🔴
فصيل اصحاب الكهف العراقي :
نعلن بأنّنا على أتم الاستعداد وأيدينا على الزناد، ونعلن أيضاً بأن منطقة ايلات وميناءها في أراضينا المحتلة ستكون منطقة عمليات لتشكيل أصحاب الكهف في حالة تعرّض أهلنا في بيروت والضاحية لأي استهداف بالتنسيق مع محور المقاومة، ونكرّر تارةً أخرى بأن من يريد منا أن نترك المقاومة عليه أن يجلب كتاباً من المرجعية حصراً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76685" target="_blank">📅 00:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚠️
إلى المستوطنين في شمال فلسطين المحتلة، المنطقة التي تضم: الجليل الأعلى الجليل الأسفل الجولان وحيفا إنذارٌ عاجلٌ سيصدر قريبًا، ترقّبوا. يتبع  ️ ️ אל המתיישבים בצפון פלסטין הכבושה, האזור הכולל: הגליל העליון הגליל התחתון הגולן וחיפה אזהרה דחופה תפורסם בקרוב…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76684" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
حزب الله يطلق رشقة صاروخية نحو مستوطنات اصبع الجليل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76683" target="_blank">📅 00:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
حزب الله يطلق رشقة صاروخية نحو مستوطنات اصبع الجليل.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76682" target="_blank">📅 00:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4962391a74.mp4?token=ZGcRssLPspLSojsrThna2PVXuuoBzEZRhCUsu-Qqyf1AXjNQwmpscshfUcSvYQS2m6P2GZBJ7tm_R4ugHEHo8O306Y-fTX1TVOUXet_3cXB6zor_AuSJo29uxOkiPggFomNRpbaPXyW-nSbdua_mERaRpx8l-65HD3jimL84tPbBuIupvewLI9Vl7fyh2dQjreL0NFkZD1WFm07hkBwQjBRPnraLM0Xb_7B2KeEYMefCFrL7IHXnmBk0oC36zX_uGX3nG1JciO2iiwBdvAuRWJtgtdh-xA-CKhnHenFrkl2n8FpQNW5BlHvXHJus1tdETMFHaeBPRgs0-T6W1YPxLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4962391a74.mp4?token=ZGcRssLPspLSojsrThna2PVXuuoBzEZRhCUsu-Qqyf1AXjNQwmpscshfUcSvYQS2m6P2GZBJ7tm_R4ugHEHo8O306Y-fTX1TVOUXet_3cXB6zor_AuSJo29uxOkiPggFomNRpbaPXyW-nSbdua_mERaRpx8l-65HD3jimL84tPbBuIupvewLI9Vl7fyh2dQjreL0NFkZD1WFm07hkBwQjBRPnraLM0Xb_7B2KeEYMefCFrL7IHXnmBk0oC36zX_uGX3nG1JciO2iiwBdvAuRWJtgtdh-xA-CKhnHenFrkl2n8FpQNW5BlHvXHJus1tdETMFHaeBPRgs0-T6W1YPxLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لبنان همیشه پاره‌ تن ماست..
ساحة الثورة وسط العاصمة الإيرانية طهران تعج برايات حزب الله دعماً للمقاومة الإسلامية في لبنان وقرار القيادة الإيرانية بالرد على العدو الصهيوأمريكي دفاعاً عن محور المقاومة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76681" target="_blank">📅 23:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae667f98ea.mp4?token=kxuVz2iwAJHGqjJ48R9Rb1jjZolP0gZ-EVAtfIqmggA61J_T5BI2Mw4Y3sX2Kx3_7R3PrMrF4AS2hS14gpSXsDb2mkeQy2Dd6UU3jdPCmT3XKq8asV-ALHkJCtH3ipPVyYrdfFjZSvC3qOmV96_36ulIXJ3eR3Ho-elcbqIcc-PKW0Y9q2G_M5yT7tVmcIiZ-LEgAHGdwmlc2G73tK4iY2zuAtqYhseM4H8PpBqfCP7k7_OA9km23MM-0Fk85AnU8iZa1XBWnDptgvAO6Sl5M27PQZJRiTkAY-kBmPsUdtTMmCZEehLE6xSQniABvrhooIEjowu8BO1szks_55YkjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae667f98ea.mp4?token=kxuVz2iwAJHGqjJ48R9Rb1jjZolP0gZ-EVAtfIqmggA61J_T5BI2Mw4Y3sX2Kx3_7R3PrMrF4AS2hS14gpSXsDb2mkeQy2Dd6UU3jdPCmT3XKq8asV-ALHkJCtH3ipPVyYrdfFjZSvC3qOmV96_36ulIXJ3eR3Ho-elcbqIcc-PKW0Y9q2G_M5yT7tVmcIiZ-LEgAHGdwmlc2G73tK4iY2zuAtqYhseM4H8PpBqfCP7k7_OA9km23MM-0Fk85AnU8iZa1XBWnDptgvAO6Sl5M27PQZJRiTkAY-kBmPsUdtTMmCZEehLE6xSQniABvrhooIEjowu8BO1szks_55YkjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات التجارة البحرية البريطانية: تم إبلاغنا بوقوع اصطدام ثانٍ لسفينة الشحن في ميناء ام قصر العراقي مما أدى إلى اندلاع حريق تم إخماده. لم ترد أنباء عن إصابات بين أفراد الطاقم. يُنصح السفن بالعبور بحذر والإبلاغ عن أي نشاط مشبوه إلى عمليات التجارة البحرية البريطانية.…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76680" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76679" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
بنيامين نتنياهو:
تحدثت هذا المساء مع الرئيس ترامب وأخبرته أنه إذا لم يتوقف حزب الله عن مهاجمة مدننا ومواطنينا - ستهاجم إسرائيل أهدافًا إرهابية في بيروت.موقفنا هذا لا يزال ثابتًا.في الوقت نفسه، سيواصل جيش الدفاع الإسرائيلي العمل كما هو مخطط في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76678" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPsqAvZwb1DXL9HLj85SUJjbeEZ73ZOfg_T1Iu35IrmFYQdv_xuVgP0PxipwGGUwqgrQOA2QenWxDrKc1NAdVi4YV8aH8sk2jy2e3N5wjGa29qSYkuqrsfdw6cBuZBznINVLicevnVoxaT7kD45O5E7YX6qLmVJi2uBTovtvfOw7PxMrws2FrYbSmghsvFEjTe50bSuEQ6fP1SBqX718UM7pdJS4nRWLTY6j2QkCqdkCTKlbsb_vj86A1dTQjgUIJMHYYVcAsdqIZpMQzGHVnTAKiAOUBuDLoSyQk7Jz5csSe7_igJ0fumjfpLXw-C08QEnK-JdFTlVsPycl8U3jDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصحافة الإيرانية في اول مانشيت لها
لن يكون ذلك أبداً من دون حزب الله» أو «أبداً بلا حزب الله»</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76677" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/76676" target="_blank">📅 22:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🌟
تحديث  أصيب 7 جنود آخرين، من بينهم 4 ضباط، في الحادث. 3 منهم في حالة خطيرة، واحد في حالة متوسطة و3 في حالة طفيفة. من بينهم قائد وحدة شاكيد برتبة مقدم، اثناء معارك مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/76675" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a07ca0f04.mp4?token=CeD7elCx2C4RbKuvIZqCN8UMgV6W9m3tmBf3BFMynU9MU_A2VybCK8MH23tNX_OjM7o-2Iuu_gXAntkT-zLT6hfxcCmBexVM4g5C7w9hdO8p2BL1fyVFCFdSiMxOrVe2BlHuAD72c7Py8lAI2tGTahYJOxreEmLFFl3D4_Bn7vg14GZX5k7tWkBHWlAjJUkjS6Y7SSBIA3o-Ju-xTJc3sfIA-l9IjnIEbFfUbxlQZxUq_6M8YAKbrobf37Pm-nmaR5_C7vJ8c-jmXFW_onTCAGxaT8NW24fReu6H8xr60KLNLElDy7UKgvDq9iM9xZZkAEFwXaEcRLRK7BjxZ_w24UTaz1kY3DsRO0kD2w4LtrvRVcQF6OIOq_7sFl8Xp5DqO61dvBnwOabRFVriESN_5VRsdeVyNQ725pODjvLU8TzqikWuN__XzUkTXYnaNnPcgaiRNFP6AZelC6Y83cqylAWPushQgBmus16M2pouhxXGK_artjIwk2_02TpFzCI_ZGYC2RrCaHm3Qis-KG3PtXpu7ei-SdLbkUYtLzqMbmOP2LWGD4cdOzWLZcUJfpnYNde_m3mYYoEH7wXw_6s74jaYWIIkeKh52JImRfCqZacxthaB4rdtOSaEI9uOkWMmLzu2XwqNlZLQcZNJKViUTr-8RIJRe6aLtBPeSMODtXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a07ca0f04.mp4?token=CeD7elCx2C4RbKuvIZqCN8UMgV6W9m3tmBf3BFMynU9MU_A2VybCK8MH23tNX_OjM7o-2Iuu_gXAntkT-zLT6hfxcCmBexVM4g5C7w9hdO8p2BL1fyVFCFdSiMxOrVe2BlHuAD72c7Py8lAI2tGTahYJOxreEmLFFl3D4_Bn7vg14GZX5k7tWkBHWlAjJUkjS6Y7SSBIA3o-Ju-xTJc3sfIA-l9IjnIEbFfUbxlQZxUq_6M8YAKbrobf37Pm-nmaR5_C7vJ8c-jmXFW_onTCAGxaT8NW24fReu6H8xr60KLNLElDy7UKgvDq9iM9xZZkAEFwXaEcRLRK7BjxZ_w24UTaz1kY3DsRO0kD2w4LtrvRVcQF6OIOq_7sFl8Xp5DqO61dvBnwOabRFVriESN_5VRsdeVyNQ725pODjvLU8TzqikWuN__XzUkTXYnaNnPcgaiRNFP6AZelC6Y83cqylAWPushQgBmus16M2pouhxXGK_artjIwk2_02TpFzCI_ZGYC2RrCaHm3Qis-KG3PtXpu7ei-SdLbkUYtLzqMbmOP2LWGD4cdOzWLZcUJfpnYNde_m3mYYoEH7wXw_6s74jaYWIIkeKh52JImRfCqZacxthaB4rdtOSaEI9uOkWMmLzu2XwqNlZLQcZNJKViUTr-8RIJRe6aLtBPeSMODtXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن مقتل الرائد د. أوري يوسف سيلفستر  ، عمره 30 عامًا، من تل أبيب، طبيب كتيبة شكد (424)، لواء جبعاتي بمسيرة من حزب الله.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/76674" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🌟
أصيب ستة مقاتلين، من بينهم ضابطان ومقاتل في حالة خطيرة، اثناء معارك مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76673" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن مقتل الرائد د. أوري يوسف سيلفستر  ، عمره 30 عامًا، من تل أبيب، طبيب كتيبة شكد (424)، لواء جبعاتي بمسيرة من حزب الله.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76672" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw99PFfQJLAeyJn5zP21B8_Ue6vDJfpqHjwDrSuKUhsdDsQWWILvMDwosF3xDySN_Aqsdr75Wy_MedHVL22Vcw_wcWfiMZ4ZiupU0CIB60LA_arq3e5wIU73VnZMMTZvXuemP9DJ_oIDSHCgtNXY7-EK5S9f0U6Axfml5jamC9H8t0OreZBHfFoeq_P4LSLXNFPpJtGX3Kw8GqMbzHgFI0upmFae6_Eo0quJ61XY4137ChEEzNhR3jSfg7qHRwiJYIyGjK9S4JTdyBdQqKy222dON_PiXDGdWq_M8HThw-XrvybOh5JM5QSsOo2FBjpIYdANg1zSL7rgfC_PJaipcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم جيش العدو : مقتل جنديين في جنوب لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76671" target="_blank">📅 22:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بن غفير: سيدي رئيس الوزراء، لقد حان الوقت لنقول لصديقنا، الرئيس ترامب: «لا».</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76670" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0gFwYpA4a4nNA-4f_bSzbOmFc8UoJ9AzRKFk_TT_LtDNo7c2SuxoF55HZL_rjTJkHL9g68_Ho96_D1dTSK1HE0xntBl71c9EZoBpEqJgCEokeSfqi5PW8UNQfBZTs6BGTGpqy1bXzQ2XgR2klviScffreDxF8iU7s4t_J1m36uNULhy6zbFJ7jR7VfonE2BFdm98q74FB-onWcDECG_2yZni41FkCcLv0SnS2hvQNj6quVs-aeEm44VSy6TdCG0_7D6fwRyNe743s04LlOFx_m2IqhX_z7v00rOK25CcP7ZeySft7mKJqjuiTWVaQZ9B_TSBZzZAeqZo3MJaqQYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مؤسسة إدارة الممرات المائية في الخليج الفارسي:
‏منذ أن بدأ الكيان ⁧ العمل في أوائل شهر مايو، أرسلت أكثر من 300 سفينة غير إيرانية معلومات للحصول على إذن بالمرور الآمن عبر ⁧ مضيق هرمز ، ومعظمها كانت ناقلات نفط.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76669" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">زعيم المعارضة الإسرائيلية "يائير لابيد": إسرائيل تحت الوصاية الأمريكية الكاملة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76668" target="_blank">📅 21:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عمليات التجارة البحرية البريطانية:
تم إبلاغنا بوقوع اصطدام ثانٍ لسفينة الشحن في ميناء ام قصر العراقي مما أدى إلى اندلاع حريق تم إخماده. لم ترد أنباء عن إصابات بين أفراد الطاقم. يُنصح السفن بالعبور بحذر والإبلاغ عن أي نشاط مشبوه إلى عمليات التجارة البحرية البريطانية. السلطات تُجري تحقيقًا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76667" target="_blank">📅 21:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بينيت: لقد فقدت الحكومة السيطرة على السيادة الإسرائيلية.    ليبرمان: هذا ليس رئيس وزراء - إنه دمية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76666" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76665" target="_blank">📅 21:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026
دبّابة ميركافا جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76664" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صحيفة "معاريف" العبرية:
في الساعات الأخيرة جرت مناقشة في المؤسسة الأمنية الإسرائيلية حول امتلاك حزب الله لمحلقات مفخخة مجهزة بكاميرات رؤية ليلية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76663" target="_blank">📅 21:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚠️
إلى المستوطنين في شمال فلسطين المحتلة، المنطقة التي تضم: الجليل الأعلى الجليل الأسفل الجولان وحيفا إنذارٌ عاجلٌ سيصدر قريبًا، ترقّبوا. يتبع  ️ ️ אל המתיישבים בצפון פלסטין הכבושה, האזור הכולל: הגליל העליון הגליל התחתון הגולן וחיפה אזהרה דחופה תפורסם בקרוב…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76662" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76661" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76660" target="_blank">📅 21:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrJS2iCfm37mLGeilDgrPffZhoNHaoTAgiWeu57Ndqyptat485dQq42s1oIxjIzzYc2b_jBXQqVfaKZLnVTvx5w5wSxjBY0mD8clHDmXA_JBh_BPsTp11YWp9a7AT5X8AxxVof9Trkbb8_p8L3TV6w5Bzm_blzhJyQwH_ldDGDaIyLuqBaebguGA0H6Wr8EmXwFHFoZar-Gze_gJCnkF10Mgt8KuFweEP-2tATSoi7tNh1wtuicuAh2z-Xxchd-el4XHXQDNQklNsZyVINDrrIbElNRLBg3jexhECFctgjUSAKhjIA0Alev9rrtxAvO-5bJwN4k5IFkEnID01dQoCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور يعيش اقوى حالته منذ قيام الثورة الإسلامية في ايران
لكن البعض ترك الباص ونسى هذا العز ، تهديد خاتم الأنبياء جعل اقوى دولتين تتراجع عن مهاجمة مجموعة شيعية لا حول ولا قوة لها إلا بعزة الله ورسوله .. افيقوا يرحمكم الله</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76659" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkraLHXdnOfUTFnhkp9oZAEAWRaso1sLDR4WfcEB-L1NfZs8l8AFMuQP-KhH6ugELqgjrU2rOWTjOkVchwSIbytUaYejTHLv4Mv9RYZ8M66L9UWJQai6xt7K3b-2OCY-y8GS0vuZsiS-1kvmG4nymS17AbVqn5ot8CiuWncFFB5uf97GyNdVmY5XM1p01iqLYHKkhN7yMcTxmS04eD0ywvmyrLgaeZtoAC-mcl9qMGLsXpw6YJQVL3KJI64XNSjUdvdOIm8tm-FdCDeZdjMjUFKFi9V0agOxI01vZQuCQ5-_tN7yCn_YLUVIPD7GgVD_lIi07Ztx8rpfeYZMa3WqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: المحادثات مستمرة، بوتيرة سريعة، مع
جمهورية إيران الإسلامية
. شكرا لك على اهتمامك بهذه المسألة!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76658" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">إعلام العدو الأسئلة:
1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟
2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟
3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟
4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76657" target="_blank">📅 21:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">يبدو ان مجموعة في حزب الله تقاتل بنظام الفيلق   أطلقت الان رشقة نحو الجليل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76656" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
