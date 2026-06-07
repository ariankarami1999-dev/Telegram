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
<img src="https://cdn4.telesco.pe/file/mYPFNtUJSKMzDgyWg0Af8qSkYhCQmoszHErjlWIggJhRd2gkSGP4m-4AwxaMRPZBkVOgpwDnZ3IF5yzJFlZ0mRg_11icQNFrf5QuFAbm0EgJUCKIePBNVUlnxaUdWnoUq-PHEZYI8Lwqz3N9OYGuPyNIDZQ2zJNHz_uk7A3AuiSSETnzCImGS-8oY8hZPfmeCBEkJM-DiktS9L2an9Uf54ZZom08USeiuvpIgHaSgmMbkMp-GUnYA-XcLzy_3mgpVZ8s2z2TjSrjmcxuD3kkcJNwJn2j5OTlMrCmF9f3xuSWusGk8OCIi6fwtGYZvXY1clL6q7N3OUJZuebdQSsLTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
<hr>

<div class="tg-post" id="msg-77341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇬🇧
ذي تلغراف:
تعاني جميع الغواصات النووية الخمس من الفئة Astute التابعة للمملكة المتحدة من أعطال في الوقت الحالي، وهي مُحتجزة في الميناء في انتظار الصيانة أو الإصلاح، بينما لم تصبح سفينة سادسة تابعة للبحرية الملكية جاهزة للنشر بعد. يحذر القادة البحريون السابقون من أن هذا الوضع يضعف قدرة بريطانيا على ردع ومراقبة أنشطة الغواصات الروسية.
يبحث البيت الأبيض في خيارات لتأمين السيطرة على جزر تشاغوس، بما في ذلك اقتراحًا بأن تشتري الولايات المتحدة الأراضي من موريشيوس بعد نقل السيادة من المملكة المتحدة. الخطة هي واحدة من عدة بدائل تدرسها إدارة ترامب وسط مخاوف بشأن مستقبل قاعدة دييغو غارسيا العسكرية المهمة استراتيجيًا.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/77341" target="_blank">📅 20:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a16708e60.mp4?token=XSNJGRDK4MDoB4nA75M9P_7RFRf4oXZwychyqHfK1jGwL-MrzcCZmcT1wifA1eAgvo14OPZI4oEogg-4bMZFEJIbVxaMs0J6XroBFmDFVU8A6a62EhDgSlcX6Vo51HMTi0R7nHXJk2sZaaiGl_FLpV2BadaK8U0xjJsuLNVHDTCQ95hFvg7KfyIr5hCRXSJ4lZq8l4xFxFUgOiRy2XTyiTfd68FIWnTzhSGoU8grCI_YEGAUUQpn3uAP1YaVQ2E0ad3Ts4w1x2o1H_V6vgPjFJTvYezT0hhKN95ueQhJhRomrZVxLaWvvkol5b6HKhhMxkYgZIBonhfyl51GzgGtO0VRqVFd8aygLi6wl-7Yj3MJFd8xfNkRL8Q_vBSYuCaKJLjr5cbSjo3DeSG6SwZJ1WewcgYTIbtPhtX19XjKnSLuH04TQnoyEdYSn7h6jrhLwi3vR3mXarI9RhIYH2pvQ606C_sBP8XbwSm9UuBn_ZQ1OkSodaTBO9WddRYz4v6-Yryy7GLz2wV4czoAP0xAscdOv8O14B8SpYmoCrkQ1lTRjCP9wjAzS2_MgUtPm2N9hnKnzMbSN_iMHj9MCyzs8QKQUSAE0PlzJmYBVRVGYipCurjxb-j5gzBNlQs0TCdicCJMPozJ9HapSpoB7reqQRv71Cq8JI4UmeSIMt58gF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a16708e60.mp4?token=XSNJGRDK4MDoB4nA75M9P_7RFRf4oXZwychyqHfK1jGwL-MrzcCZmcT1wifA1eAgvo14OPZI4oEogg-4bMZFEJIbVxaMs0J6XroBFmDFVU8A6a62EhDgSlcX6Vo51HMTi0R7nHXJk2sZaaiGl_FLpV2BadaK8U0xjJsuLNVHDTCQ95hFvg7KfyIr5hCRXSJ4lZq8l4xFxFUgOiRy2XTyiTfd68FIWnTzhSGoU8grCI_YEGAUUQpn3uAP1YaVQ2E0ad3Ts4w1x2o1H_V6vgPjFJTvYezT0hhKN95ueQhJhRomrZVxLaWvvkol5b6HKhhMxkYgZIBonhfyl51GzgGtO0VRqVFd8aygLi6wl-7Yj3MJFd8xfNkRL8Q_vBSYuCaKJLjr5cbSjo3DeSG6SwZJ1WewcgYTIbtPhtX19XjKnSLuH04TQnoyEdYSn7h6jrhLwi3vR3mXarI9RhIYH2pvQ606C_sBP8XbwSm9UuBn_ZQ1OkSodaTBO9WddRYz4v6-Yryy7GLz2wV4czoAP0xAscdOv8O14B8SpYmoCrkQ1lTRjCP9wjAzS2_MgUtPm2N9hnKnzMbSN_iMHj9MCyzs8QKQUSAE0PlzJmYBVRVGYipCurjxb-j5gzBNlQs0TCdicCJMPozJ9HapSpoB7reqQRv71Cq8JI4UmeSIMt58gF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب ينوه بإستخدام الجولاني لتنفيذ المشروع الصهيوأمريكي ضد لبنان:  أودّ أن أرى هجومًا أكثر دقةً وفعاليةً على حزب الله. أكثر دقةً وفعالية. يمكننا مساعدتهم في ذلك، أو يمكننا أن ننصح سوريا. سوريا تبذل جهدًا كبيرًا في إصلاح أوضاعها. لديهم قائدٌ كفؤٌ للغاية،…</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/77340" target="_blank">📅 20:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حالة تأهب قصوى في إسرائيل على خلفية التهديد الإيراني بإطلاق النار الليلة.</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/77339" target="_blank">📅 20:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
بعد تقييم الوضع، تظل سياسة الدفاع التابعة لقيادة الجبهة الداخلية دون تغيير وستظل سارية حتى يوم الاثنين، 8 يونيو 2026، الساعة 20:00.</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/77338" target="_blank">📅 20:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b577c328.mp4?token=K3kSWIH_ae-erQV23moSbkM7k1DssMTfXabH8aoavMqmCuHfZirf48WQCcX5KF_j-ovTP1LZDtbNr95Y4DsVZUrrbShHFPKFV_aueW9Euvd0hhP-HRoDza6jawoq6pun2xM96xVI-4JctrpMKk2FFuBHCSY9jl8cvypGAPQshBbVTjhbyxYWnvYmoeia5_WTuq8AVi2gLUYylmf5nZdbH6QDHu2glft7i8gZ9Rj_RK_vIWZix56D6u2inBoJDvfbeCsdJnkToV_N4uyaIwPMgIAOBqmvQtnyho6VE_XPK4CS1iIVLX_qkNwGtOpJwrx1-6Qa-2K-2ukMh2UELhOnUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b577c328.mp4?token=K3kSWIH_ae-erQV23moSbkM7k1DssMTfXabH8aoavMqmCuHfZirf48WQCcX5KF_j-ovTP1LZDtbNr95Y4DsVZUrrbShHFPKFV_aueW9Euvd0hhP-HRoDza6jawoq6pun2xM96xVI-4JctrpMKk2FFuBHCSY9jl8cvypGAPQshBbVTjhbyxYWnvYmoeia5_WTuq8AVi2gLUYylmf5nZdbH6QDHu2glft7i8gZ9Rj_RK_vIWZix56D6u2inBoJDvfbeCsdJnkToV_N4uyaIwPMgIAOBqmvQtnyho6VE_XPK4CS1iIVLX_qkNwGtOpJwrx1-6Qa-2K-2ukMh2UELhOnUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان صهيوني يستهدف الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/77337" target="_blank">📅 20:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
قيادة القوة الجوية العراقية ترد على ما نشرته مجلة "فوربس" الأمريكية بتاريخ 28 أيار 2026:
تود قيادة القوة الجوية العراقية أن تعقب على التقرير الصادر عن مجلة "فوربس" الأمريكية بتاريخ 28 أيار 2026، والذي تناول قدرات وجاهزية طائرات F-16 العائدة لقوتنا الجوية. وبناءً على المسؤولية الوطنية والمهنية، نؤكد أن التقرير المذكور افتقر إلى الدقة في معلوماته، وجاء مجافياً للواقع، مما استوجب هذا التصريح الرسمي لتصويب المغالطات، ودعوة وسائل الإعلام العالمية إلى توخي الدقة واستقاء المعلومات من مصادرها الرسمية والموثوقة.
وفي هذا الصدد، نود إيضاح الحقائق والوقائع والبيانات الرقمية المعتمدة الآتية:
أولاً: الكفاءة البشرية والقدرات الفنية والتقنية
الطيارون:
تُقاد طائرات F-16 العراقية من قبل طيارين عراقيين على مستوى عالٍ من الكفاءة والاحترافية، ممن تلقوا تدريباتهم المتقدمة في الولايات المتحدة الأمريكية.
الكوادر الفنية:
تفنيداً لما ذُكر حول غياب القدرات التقنية، نؤكد امتلاك القوة الجوية العراقية كوادر هندسية وفنية عراقية تتمتع بمهارات وخبرات كبيرة في هذا المجال، إذ تم إشراكهم في دورات تخصصية مكثفة في الولايات المتحدة الأمريكية، وحصلوا بموجبها على شهادات معتمدة دولياً تؤكد جدارتهم وقدرتهم على إدارة هذا الملف بكفاءة عالية.
دور الشركة المتعاقدة:
نوضح للرأي العام أن دور الشركة الأجنبية المتعاقدة يقتصر على الإشراف وتأمين قطع الغيار التي يطلبها فنيو القوة الجوية العراقية، وليس إدارة الجهد الفني المباشر.
ثانياً: فاعلية الطائرات وإنجازاتها العملياتية والقتالية (من 1/12/2014 ولغاية 1/6/2026)
إن الجاهزية والفاعلية القتالية لطائرات F-16 العراقية لا تحتاج إلى تخمينات، بل تتحدث عنها لغة الأرقام الدقيقة والإنجازات الميدانية طيلة الفترة من 1 كانون الأول 2014 ولغاية 1 حزيران 2026، وكما يأتي:
الإحصائيات العملياتية العامة:
تنفيذ 20,071 طلعة جوية.
إطلاق 2,753 صاروخ هيل فاير بدقة عالية.
إسقاط 13,176 قنبلة بمختلف العيارات ضد أهداف معادية.
الواجبات القتالية لمحاربة عصابات داعش الإرهابية:
تنفيذ أكثر من 1,300 واجب تعبوي.
قتل 675 إرهابياً.
تدمير 280 مضافة ونقطة تحصن تابعة للعصابات الإرهابية.
ثالثاً: التواجد الدولي والخطط المستقبلية
التمارين العالمية:
تعزيزاً لمهارات صقورنا، شاركت طائرات F-16 العراقية في عدة تمارين تعبوية عالمية مشتركة مع دول كبرى وصديقة، مثل الولايات المتحدة الأمريكية وفرنسا وإيطاليا والأردن، والعمل جارٍ وفق خطط مستقبلية لتوسيع هذه الشراكات مع دول أخرى.
التطوير والتسليح:
إن قيادة القوة الجوية مستمرة، وحتى هذه اللحظة، بتنفيذ جميع الواجبات الموكلة إليها لحماية سماء الوطن، وتمتلك رؤية استراتيجية واضحة لتعزيز أسرابها المقاتلة بطائرات ومعدات حديثة من مناشئ عالمية رصينة ومتنوعة، بما يضمن سيادة العراق وحماية شعبه من أي اعتداء.
ختاماً، تجدد قيادة القوة الجوية العراقية ثقتها التامة بمنتسبيها من الطيارين والفنيين، وتؤكد أن سلاح الجو العراقي سيبقى اليد الضاربة والقادرة على ردع أي خرق أو تهديد لأمن واستقرار بلادنا العزيزة.
قيادة القوة الجوية العراقية
7 حزيران 2026</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77334" target="_blank">📅 19:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2876be8636.mp4?token=sLEmYqtxGIZ_v2Wgd4sKblsSXK8J1QrP4y3Xr_54LYfo_yTmZFa6oEgZtOwfrEkUpKXrNDXhU6fcm-QHroo5SeKC7BW9h3B3FRJBlFYKGpHkQqospqYXdmHXOikCeVwJGDu6kCoP8EribCffi7Bwmidtsg7UhJEeTvlqjAIKHha4GZp0DkBe3oxC6Kkdoo97MFUed2icnnhguSNexHoGHaKHj8e0gvtMJpS6R60gzoVsGZVndV8-TMvCq73WPkx2OGLymNk2tfFCiyrTss1GARbHBQRj4b9tUtoWgkjsWqfUp2KGZLAjB3c4jS2MU5CqiyGNPtF0O5sKtTec11MUv58fZPVpoYArVWSmqfAL3gSDe03os8tn6Q2NRiT79EIkhU-KcsmWgwgu0gjIaidlK3YXY7z7LUY2Woo200bxbO_5T5EeKunbFy2wK1sBF0H-Mo1uGbCgx0Uu3jhO_5jV4XOx-P9Jcluq0Fke6M0iGy32XUptoQFb7pMeLDuY8xPJkNMRfYDHeEwr9YTHuuoRwRhoa_lCl7yeo0ZX7OjD6zwMGysmvS-0X9UkU0q_GUXfr3yCT_YZPtWiWWNkzDcgEetToY5-J-TT8iOhcsp51f1d2XH_7GkdURp4Mtg30o9QDMtQRgV0rydsaHJ091OpX0-fEHKhyBBlwLXpV8ESJO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2876be8636.mp4?token=sLEmYqtxGIZ_v2Wgd4sKblsSXK8J1QrP4y3Xr_54LYfo_yTmZFa6oEgZtOwfrEkUpKXrNDXhU6fcm-QHroo5SeKC7BW9h3B3FRJBlFYKGpHkQqospqYXdmHXOikCeVwJGDu6kCoP8EribCffi7Bwmidtsg7UhJEeTvlqjAIKHha4GZp0DkBe3oxC6Kkdoo97MFUed2icnnhguSNexHoGHaKHj8e0gvtMJpS6R60gzoVsGZVndV8-TMvCq73WPkx2OGLymNk2tfFCiyrTss1GARbHBQRj4b9tUtoWgkjsWqfUp2KGZLAjB3c4jS2MU5CqiyGNPtF0O5sKtTec11MUv58fZPVpoYArVWSmqfAL3gSDe03os8tn6Q2NRiT79EIkhU-KcsmWgwgu0gjIaidlK3YXY7z7LUY2Woo200bxbO_5T5EeKunbFy2wK1sBF0H-Mo1uGbCgx0Uu3jhO_5jV4XOx-P9Jcluq0Fke6M0iGy32XUptoQFb7pMeLDuY8xPJkNMRfYDHeEwr9YTHuuoRwRhoa_lCl7yeo0ZX7OjD6zwMGysmvS-0X9UkU0q_GUXfr3yCT_YZPtWiWWNkzDcgEetToY5-J-TT8iOhcsp51f1d2XH_7GkdURp4Mtg30o9QDMtQRgV0rydsaHJ091OpX0-fEHKhyBBlwLXpV8ESJO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب يهاجم مقدمة البرنامج كريستين ويلكر ويصفها بالفاسقة والغبية وكذلك ABC وCBS وCNN ويغادر اللقاء غاضباً.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77333" target="_blank">📅 19:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
وزارة الصحة العراقية:
وفاة 21 شخصاً وإصابة 19 آخرين بينهم زائرون إيرانيون في حادث انقلاب حافلة على طريق الناصرية - البصرة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77332" target="_blank">📅 19:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGZ9irYPPGwJjJiQRFIaPLIoq5FnIpa5TT5IUNPl88AOcUNiGyYZHkAdI30yWP8ZaZopuYr3V-UuJh4G4baxMDS_ZQEgmMhVkcp64zG2ed8Vd-RbdJGL1lj-nPK4du4tAAZgIfYDhkL8Y7EuPEyFIwinX9lwjMrQb-iDKO9pMSGY5rN27IISE9c6TkBDXNKl1mZbH4E2_h_q-0q0gu3uvrHeX5CKxqoY7LglrlD7fYNKqYPJ4Ip1nKcxzf38AvzjQ9irohqRE5yfnSZOagtDdLoXS4KfVpgDU3p4-xoKAPfUmxD9j0tuDCl9Yai0VoMtqmwqlqJ0yckQebnJJE4j1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77331" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف مهدداً: إنهم لا يلتزمون بوقف إطلاق النار ولا يؤمنون بالحوار، ومن خلال الحصار البحري وانتهاك الاتفاقيات المتعلقة بلبنان، أظهروا أنهم لا يفهمون إلا لغة القوة. إن الحصار البحري المفروض على إيران، والضوء الأخضر الأمريكي…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77330" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6E3slUxxHMwyHM3Zqal2JrPVNMuQ99EOokoXcREzQSRr-snGlSdYsGUWmAm8b4H-27AqnvIsyXALq7qXXVPOmaWLwbpFyT44lqvEjbbt5NXKLrIRpT-mpG783yhk2gPOqbY-rB9YBWATfC1qRIEJzS82MWpKWs7H0vkyZy7cIHDkGgBEYkwtJKQVaPLDMSSeJF7o2VsoZ8Cfv-u__oTIptgGc-5-1T935VDQnk53Pw-XXNFFmwS3bWdTdhNYqSYdWZvtKzAZhzpIPN3Q6cCMOMSbylHostk3eV-xauAk4wug8-DRlTeV-t5TSBWpijZ7HRBUGluv3MZWvldc16LVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف مهدداً:
إنهم لا يلتزمون بوقف إطلاق النار ولا يؤمنون بالحوار، ومن خلال الحصار البحري وانتهاك الاتفاقيات المتعلقة بلبنان، أظهروا أنهم لا يفهمون إلا لغة القوة. إن الحصار البحري المفروض على إيران، والضوء الأخضر الأمريكي الذي منحته الولايات المتحدة اليوم للكيان الصهيوني، يحوّلان القواعد والأصول الأمريكية وقواعد الكيان الصهيوني في المنطقة إلى أهداف مشروعة. وقواتنا المسلحة مستعدة كعادتها.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77329" target="_blank">📅 19:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
قطر تصدر إشعاراً للملاحين الجويين يغير مسارات الرحلات الجوية عبر مجالها الجوي، موفرة بذلك مسارات بديلة للطائرات المغادرة من مطاري الدوحة والسعودية وسط التوترات الإقليمية المستمرة. ويسري هذا الإشعار في الفترة من 7 إلى 14 يونيو.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77328" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVlDz6kajLXYbtOFu_PwWA4YvyoDZYV2t-V0162jiKcTYdHj58wgORqe07IV9VeVDicojkRPSZ2TMo634mYq7TlhHodJBskJ2NNAWosJWafWC2Dx6vXLdufHgKgxSO-178l3-RyYVEnr7qOj0Rldd7q7qRZldBQkqDoAolbSodGeo6p1gViTWv9_NEopCj125O651kUGuE-90eFWD-NS--u6z-iFC3mbnNjwa_7sqUwIOvOCosvb0-UtGmKF7Igkk2qpy5aMWj-4qhRleKkajkyaWcQ9hllreZCgIOS9XnwBhTzMR3j1y83HAnOvQJdTzbhqcovYtjEHbobX_5ES9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال الصهيوني يعلن عن مقتل جندي وإصابة قائد شرطة مستوطنة "تسور ناتان" بجروح خطيرة جراء عملية إطلاق النار التي وقعت اليوم قرب كوخاف يائير.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77327" target="_blank">📅 19:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
01-06-2026
تجمّع لآليات وجنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بصليةٍ صاروخيّة كبيرة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77326" target="_blank">📅 18:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax_7IXq2oH-hiWYjOolvaRf8GPQcOk9IT7J9pGgo8qXBD_5l1XsawVT0iOi_5m1-HmcaEN-k3D0hqaINKbjJtQPQ1awxYNkNQN5_ORlHrGYrbA9iYHULRrBU3wBVx0gtgsmbcU_WHvMYkDOQ4Ybstn_LaMEG_3LRqAGvlLR2XWg0IAz0SBxLKz8DwdGkjoIDUGt16lfk8tUjE1JeYWhENQ0eEXacmGYx90SIj9QKsKq3dDI_gs_u_GMLpr18Cc9-TCMtMtSSJ4z4L3nNfhaBOE5K3Jsx_L0aCGfwCAUU61hrd252-PcMHX_SS4_o-hqfKTZ9g0z7EQRZXzM5_c19wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
غارات صهيونية جديدة على منطقة الحوش بمدينة صور اللبنانية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77325" target="_blank">📅 18:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c064312c.mp4?token=QyzHE4-UWBe8oY7_8qm307zSkr-krJV0DTcvtRp9qPuFQ4gs-6oHsAnqczwDRJ0tOX6PWTBEIUqXAv6etMlMdCRWJaqEqZXn2a2__WoQ0-QTIRvUUO0wunvo9lZPdDDrERF0xDryYu_VZ0vJtZ14OG5KOldSEzSVtlfJlkfRtbCnrBu1z2cEqXxI1ezxK1aObJ8qjd2WvHrwtPoKilANR41xdGzImqLBvhUGVKHM_R-bkLx-7dhmyKiIsk4JRl3a-m8qPOxg5h1IxkdvpEhAFs75wzlzToMA3TeV-00_ZRedlCikEDgfIvRkvTJ5T2uws6-yRtDhOVeIDUoB6YCpoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c064312c.mp4?token=QyzHE4-UWBe8oY7_8qm307zSkr-krJV0DTcvtRp9qPuFQ4gs-6oHsAnqczwDRJ0tOX6PWTBEIUqXAv6etMlMdCRWJaqEqZXn2a2__WoQ0-QTIRvUUO0wunvo9lZPdDDrERF0xDryYu_VZ0vJtZ14OG5KOldSEzSVtlfJlkfRtbCnrBu1z2cEqXxI1ezxK1aObJ8qjd2WvHrwtPoKilANR41xdGzImqLBvhUGVKHM_R-bkLx-7dhmyKiIsk4JRl3a-m8qPOxg5h1IxkdvpEhAFs75wzlzToMA3TeV-00_ZRedlCikEDgfIvRkvTJ5T2uws6-yRtDhOVeIDUoB6YCpoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران ربما قامت قليلا بتعزيز قدراتها العسكرية خلال وقف إطلاق النار.  سأقضي نهائيا على التهديد الإيراني إما عبر التفاوض أو سأدمرهم تماما وسيكون ذلك سهلا للغاية.  أعرف مكان جميع المواد النووية الإيرانية.  إذا قتلت إيران مزيدا من الأمريكيين فسأفكر بجدية…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77324" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مؤشرات مرتفعة لضربة تنسيقية مشتركة خلال الساعات القادمة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77323" target="_blank">📅 18:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
وزير الخارجية العراقي فؤاد حسين: لجأنا إلى طباعة 25 تريليون دينار لمواجهة الأزمة المالية، والبلاد قد تواجه كارثة مالية إذا استمرت الحرب.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77322" target="_blank">📅 18:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عدد كبير من الاصابات في الضاحية الجنوبية لبيروت بعد العدوان الصهيوني</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77321" target="_blank">📅 18:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
أوبك بلاس:
الدول السبع المشاركة تقرر زيادة الإنتاج بمقدار 188 ألف برميل يوميا اعتبارا من شهر يوليو.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77320" target="_blank">📅 17:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامب: سبب فرض الحصار البحري على إيران هو أنهم حاولوا فرض حصار والآن قمنا نحن بفرض حصار عليهم، لا أعتبر الحصار البحري على إيران حربا لكن من أراد وصفه بالحرب فأتوقع أن بإمكانه ذلك.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77319" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامب: منفتح على إجراء محادثات مباشرة مع المرشد الإيراني إذا رغب في ذلك</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77318" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامب: الإيرانيون أقوياء وفخورون بأنفسهم وهناك أمور لم يتوقعوا يوما أن يفعلوها لكنهم سيضطرون لفعلها</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77317" target="_blank">📅 17:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامب: لقد أقروا بأنهم لن يمتلكوا أسلحة نووية. كان لدينا بند في الاتفاقية ينص على أنهم لن يطوروا أسلحة نووية. وكان الجميع راضين للغاية عن ذلك باستثنائي"، أريد بنداً إضافياً لضمان عدم تمكن إيران من الالتفاف على الاتفاق قلتُ: ماذا لو لم يطوروا، بل اشتروا واستحوذوا؟…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/77316" target="_blank">📅 17:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامب: إذا أحسنت إيران التصرف قد نبدأ حينها الحديث عن الأموال والعقوبات</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77315" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏ترامب: لن يفرج عن الأصول الإيرانية أو يخفف العقوبات مبدئياً في أي اتفاق</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77314" target="_blank">📅 16:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: لن يفرج عن الأصول الإيرانية أو يخفف العقوبات مبدئياً في أي اتفاق</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77313" target="_blank">📅 16:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلام العدو: مقاتلتان شاركتا في الهجوم على الضاحية وأسقطتا 10 ذخائر وتم ابلاغ ادارة ترامب مسبقا بالهجوم.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77312" target="_blank">📅 16:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">إطلاق صاروخ أرض جو باتجاه مقاتلات إسرائيلية في أجواء قضاء النبطية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77311" target="_blank">📅 16:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وسائل اعلام: ‏الغارة على الضاحية استهدفت مبنيين لحزب الله وليس شخصيات</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77310" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعلام العدو عن مصدر أمني: الهجوم على الضاحية الجنوبية مرتبط بالموقع وليس بطبيعة الهدف نفسه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77309" target="_blank">📅 16:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هجوم من جنوب لبنان باتجاه الكيان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77308" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اعلام العدو: رؤساء مجالس مستوطنات الشمال يعلنون أن الجيش الإسرائيلي أبلغهم بتنفيذ غارات في بيروت</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77307" target="_blank">📅 16:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">النجباء …  اصحاب الأقدام الثقيلة   ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77306" target="_blank">📅 16:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جيش العدو يزعم: بتوجيه استخباراتي، هاجم سلاح الجو الإسرائيلي هدفا ثمينا في الضاحية الجنوبية ببيروت</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/77305" target="_blank">📅 16:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عدد كبير من الاصابات في الضاحية الجنوبية لبيروت بعد العدوان الصهيوني</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77304" target="_blank">📅 16:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98402d3774.mp4?token=ROqrBuWvlSPOUogQjQod521jeBz0eADkHxIJ2p8Z4mJDSqMfsYy5nv3AFwIo7USwJyHWxxqLzWKCiTiCX_kYBBuLg9dEfyRDPB3G8W0Rvz7egze_8STA7GiVZBGAuK2frpq8y0VV_whei1JnAkANX12xcKCU9S2NESlQ7olZLvcQ_F549KwTlZ8ZK2o4hOhfzE5KVPz5RtPxFgutT5-prPeGvYwGXmHy8XWdVuRt8bo9AOkbzI2aupcPjbL7y31Vx-85V9zDEf3bSCA9U_NvM6BPBna5JO8eC0iA_t2TR9Ka1TumxcnKAIJ5xCiHCg4_j-GiCXcKSU-TYWtCEvcGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98402d3774.mp4?token=ROqrBuWvlSPOUogQjQod521jeBz0eADkHxIJ2p8Z4mJDSqMfsYy5nv3AFwIo7USwJyHWxxqLzWKCiTiCX_kYBBuLg9dEfyRDPB3G8W0Rvz7egze_8STA7GiVZBGAuK2frpq8y0VV_whei1JnAkANX12xcKCU9S2NESlQ7olZLvcQ_F549KwTlZ8ZK2o4hOhfzE5KVPz5RtPxFgutT5-prPeGvYwGXmHy8XWdVuRt8bo9AOkbzI2aupcPjbL7y31Vx-85V9zDEf3bSCA9U_NvM6BPBna5JO8eC0iA_t2TR9Ka1TumxcnKAIJ5xCiHCg4_j-GiCXcKSU-TYWtCEvcGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات إخلاء لمصابين نساء وأطفال جراء الغارات على الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77303" target="_blank">📅 16:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مسلحين تابعين لحزب العمال الكردستاني يعترضون طريق منتسب سابق في حزب العمال ويقتلونه بإطلاق نار في إحدى قرى قضاء البعاج التابعة لمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77302" target="_blank">📅 16:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1cb8381b6.mp4?token=rHLbGgijOeMUJsICybMi8WP8MiN_QouXbgBsa0EQ5hEq7PUrI3DrXpNargNMLlFk-ZInLO7p0RG3P4yC-QDhRn0B_x6UygSUlTp_qavyweKb513shIjW6_EX6T7At6IpQiQ3rUxlQ7Bw4jFUbD_7OT-Qdl-d-fLBoaKWsCW-3nyr9PTdfvKouYFL-RgjdfZNPNMqX30z6EDRmRS0kbULoVG3lCQJFYTQd--hHrT02u1gi1isHx5K6Rp_h4k06sknNq-RYE33Dm143bhBaGcUEbiBAzmc9XRpoJyHe8lP6YKiugMFoX55HJnVSPAagx_HzLYib0iOdy2XKdFBZ71lCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1cb8381b6.mp4?token=rHLbGgijOeMUJsICybMi8WP8MiN_QouXbgBsa0EQ5hEq7PUrI3DrXpNargNMLlFk-ZInLO7p0RG3P4yC-QDhRn0B_x6UygSUlTp_qavyweKb513shIjW6_EX6T7At6IpQiQ3rUxlQ7Bw4jFUbD_7OT-Qdl-d-fLBoaKWsCW-3nyr9PTdfvKouYFL-RgjdfZNPNMqX30z6EDRmRS0kbULoVG3lCQJFYTQd--hHrT02u1gi1isHx5K6Rp_h4k06sknNq-RYE33Dm143bhBaGcUEbiBAzmc9XRpoJyHe8lP6YKiugMFoX55HJnVSPAagx_HzLYib0iOdy2XKdFBZ71lCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو: في الأسبوع الماضي، هدد وزير الخارجية الإيراني عباس عراقجي بأن طهران سترد بقوة في حال وقوع هجوم على الضاحية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77301" target="_blank">📅 16:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
الولايات المتحدة قدمت مسودة قرار بشأن الاجتماع الفصلي لمجلس إدارة الوكالة الدولية للطاقة الذرية، الذي يضم 35 دولة، المقرر عقده هذا الأسبوع. المشروع يتضمن (يجب على إيران أن توفر الوصول الكامل دون تأخير من أجل التحقق وان تقدم على الفور تفاصيل دقيقة عن المواد والمواقع النووية)</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/77300" target="_blank">📅 16:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">المبنى المستهدف في الضاحية الجنوبية لبيروت: تم استهدف شقتين بـ3 صواريخ متتالية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77299" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRlRmgIGBJA4U99i7dNon__t9N_QzAIIPdrfEMPkxJjfWz44Bt-RSJkM8UOXECM6n6pNl6vH_4zqa7cuCtmCvqhiNUWeGHcTDNpV_p6MuEB3F_uWOuCUkbMXYmJWQZQmBi0_b5u56WpsgEFyzrAEBkvDn4Axqwb8GplB4WgAFTR0ppZKW8v0yNamJJfdIWzkZqRiY8FQNoUbusaEgI28io7Ai6dKQ_ooIIQ-4h4uSejNIfobQGTIb2y-hHywZMuRDGW0zkXi9ozwU8lByo6X0b_lJ_p_VsneKEr1p7Yk3V8RXzWhHXvDBOcEhvGDcsPJpXa0opxNnfTFASH9Mw9q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: الجيش الإسرائيلي يتحدث عن استهداف بنية تحتية وليس عن اغتيال.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77298" target="_blank">📅 15:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الموقع المستهدف في الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77297" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2defzH0CpfsFK4mtAZAdD_GJcu35NXUj85Y3jXtjLu-AqHIP8iXmz2E8xTpJDn2JVMj9YMP9yLUb9voFI75ehM6uZgznVmAvVMZAPTJNlXNp2IX3YD_WmiKLc8eTX36WRUQzSGeHb9qAdxBClYTXc1_qSK1v_5UMfF3DDmbTNKvHLa33x1zFtFbWshKiKZW_OBngAtq4d1CZ93jEZz-EAYLV_Mf0DMoNkLX-tgyTKRkFxZ6_UqI7_u4-_CDzc1M67chh8sS2CLnF4UcXLEt7B42XxWGwBFHp5jstrRzzSWT_ZydwxdEmG3kn6UMWYchFp8DXf4pemQmIkkUpF6mFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو: قصف سلاح الجو قبل قليل بنية تحتية تابعة لحزب الله في الضاحية الجنوبية لبيروت، تفاصيل إضافية لاحقا.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77296" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a4b936ec.mp4?token=p3tOtsscNYGFAIHAWyU2GfZZEDTN0Nm6KxUrNVHXKnoP7F0ZBggv9EtOeG6PA5pADJpaLfSUlYoTuBrOzxORiwAtSgs_G2NJAZmO1hbLzNiNQsZb_aihyD2CLlSpst4ivupY-jAdcatoyNuC-KaRGW_XmFPjrv2ikb312_31EqYAkC1ADqhPycptD-QH_w5H_Fac2f7HBOiOF8y77rEsBdhNtXixgbgKAT6A1bE--fOCPtYZFjds1ssE9Ob48Qga_WJ1rQw-zWVLmt4RC_moYeIGl1i8_hbEP38J63Co33Xa574D9RcJ-QL39-7NkUgA0X0DYzLWJS1bvrkC1ugP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a4b936ec.mp4?token=p3tOtsscNYGFAIHAWyU2GfZZEDTN0Nm6KxUrNVHXKnoP7F0ZBggv9EtOeG6PA5pADJpaLfSUlYoTuBrOzxORiwAtSgs_G2NJAZmO1hbLzNiNQsZb_aihyD2CLlSpst4ivupY-jAdcatoyNuC-KaRGW_XmFPjrv2ikb312_31EqYAkC1ADqhPycptD-QH_w5H_Fac2f7HBOiOF8y77rEsBdhNtXixgbgKAT6A1bE--fOCPtYZFjds1ssE9Ob48Qga_WJ1rQw-zWVLmt4RC_moYeIGl1i8_hbEP38J63Co33Xa574D9RcJ-QL39-7NkUgA0X0DYzLWJS1bvrkC1ugP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الإسرائيلي والشاباك في بيان: وفقا لتوجهات نتن ياهو، قصفنا مقرات عمليات لحزب الله في بيروت ردا على اطلاق الصواريخ</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/77295" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مشاهد من الضاحية بعد العدوان الصهيوني</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/77294" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/468dd2f79b.mp4?token=ARYTh7nGlwuGCLPcpp0n3x_Ye2Bt6ORgt2b-DZPxcttk7fkQZaqambi4KQLZtqwAtp9qZdLSaia1FmLbEecVHNV8D2vreJt1lCvamLsBWvK4dBPJW5juKVcUv3AErMN7JKg9meu7BbcqFtaFV3c9kO4QUATDGmYVjFWLEURkDQbvM10YmKGI7jDL2Hx5tPuH2UwlZ1AKN7KZeNy5lbQRHEG_GV827Y1YrEZBN6bDMLe_sjHrK5K6cWYuvnadSD68hXO7tFbXm1CAL_FBvh4ja6q5V6GTEy0id1saSLomjGau5xDY5vO41XyQut5u8cY0MKIvb3W3aHlU7cgYn5Y79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/468dd2f79b.mp4?token=ARYTh7nGlwuGCLPcpp0n3x_Ye2Bt6ORgt2b-DZPxcttk7fkQZaqambi4KQLZtqwAtp9qZdLSaia1FmLbEecVHNV8D2vreJt1lCvamLsBWvK4dBPJW5juKVcUv3AErMN7JKg9meu7BbcqFtaFV3c9kO4QUATDGmYVjFWLEURkDQbvM10YmKGI7jDL2Hx5tPuH2UwlZ1AKN7KZeNy5lbQRHEG_GV827Y1YrEZBN6bDMLe_sjHrK5K6cWYuvnadSD68hXO7tFbXm1CAL_FBvh4ja6q5V6GTEy0id1saSLomjGau5xDY5vO41XyQut5u8cY0MKIvb3W3aHlU7cgYn5Y79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو: الجيش الإسرائيلي شنّ غارة على الضاحية الجنوبية في بيروت</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77293" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">3 غارات تستهدف الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/77292" target="_blank">📅 15:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d2232f57.mp4?token=CYbvhMXLyUmBOaB6tARildpAI5HzVEbPD4JAIwe7CaEBcj6Ir7fKUuwBgNZHaW6aZXH9vbYk0tXs_H1-cRvKt46N6baglAo-JEhdVYHOrTXYgDfccKfE4XiI66F4muNT7gYj7NXTKruLeNsKP3M4PdRiId-1uwQc3LPOwupn1nxOO9GLzAvtj5lKhjhWqXhoZTwn_uV3iQMvAUEKDMUoqqBhJsnjfR9jlaFlAO1WSSA3zk2Fmk6gkV9tr7-WWrs5__UUV8Bspa_GuCNaxHtZgEpkC6sfS2g0my8iudwCBonAT5ZgwxVSvbBo972zGUIJwMIfgoGD4TjFJXuAzRc0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d2232f57.mp4?token=CYbvhMXLyUmBOaB6tARildpAI5HzVEbPD4JAIwe7CaEBcj6Ir7fKUuwBgNZHaW6aZXH9vbYk0tXs_H1-cRvKt46N6baglAo-JEhdVYHOrTXYgDfccKfE4XiI66F4muNT7gYj7NXTKruLeNsKP3M4PdRiId-1uwQc3LPOwupn1nxOO9GLzAvtj5lKhjhWqXhoZTwn_uV3iQMvAUEKDMUoqqBhJsnjfR9jlaFlAO1WSSA3zk2Fmk6gkV9tr7-WWrs5__UUV8Bspa_GuCNaxHtZgEpkC6sfS2g0my8iudwCBonAT5ZgwxVSvbBo972zGUIJwMIfgoGD4TjFJXuAzRc0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان صهيوني يستهدف الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/77291" target="_blank">📅 15:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad1ZVSDv35Kp18I_soZM-BPujISq7bsJ5LWGDHt0CN3RaaBPLyTryoTA5kQWt4KuReIT-Drc--qf0M_PZQtSeS6mCow06OMiE1coqppWte2guhz9I-kSKp8taQ-SpJ382MOfQ0Ud2hWmgoFcR0WgcFvyxMSZMDh3PQKyvnG1AfaV7_iaqybof326F7wieeohP2rIE_8xmTgurxSySYx5d0tBx_CB0O8_2d8eEGBX8F4d_XYSHTS9lEECtDLnLOofutFqyo85xlqcA9z0MO-vFl0n9KsKs6L4kEuzXKot9j2ySGA3n1INshpgrXT7cN8GFR4ctarnfOGUzv9rjeaxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان صهيوني يستهدف الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77290" target="_blank">📅 15:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIM-JDz7bawHs0TS10YG4VixXm-7MHldcDzsJEYIkZhD3gyZd0WfFUln1WA8AZwNkxMl5gWLtpknFJelPscDc_q90w-gwUtcvXVVsSGCtwJCAxQEZmciQGWU30uDKrW6CvK_QL-de2iF2NL7idQCpY_fm6CbIGjZI9zBwbZ1tlh1VKIeFmPeD2njEtSS_lW7sqveWMLu_TNKZSHQnVaYiq2rH7eNy3TuhGjb2Ikqkw5MBvWTecOeSJfQtuLvxftbRsobu7oLvyQ4W_xdiXhhHPso05DMc3ZSzBEaNNZuKp0A18mmf0-IEiUfM0-HClI9GksZ9S8AAjxl8OtBEGgL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بعد تصاعد حملة مطالبات الموجهة إلى شركة آسياسيل لإلغاء سياسة "الاستخدام العادل"، متابعون يلاحظون اختفاء الصفحة الرسمية للشركة على منصة فيسبوك منذ ساعات</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77289" target="_blank">📅 15:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔥
🇮🇶
سوالف الگهوة   رسالة رئيس مجلس الدوما الروسي السيد فياتشيسلاف فولودين إلى رئاسة مجلس النواب العراقي .</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77288" target="_blank">📅 15:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية العراقية تستدعي القنصل الأميركي في العراق ردا على طريقة التعامل مع النجم ايمن حسين لاعب المنتخب العراقي وتسلمه مذكرة احتجاج رسمية وتوضيح خلال ٧٢ ساعة .</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77287" target="_blank">📅 14:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0NraI3kHL5PS2bRc7RqCiqbVJ8MEthlLLyWYFbtIYTYQAsns8ATzX0Vi9HDyDfMSxcEOQ8Jh8NBhnZ3Sj5gWXfn1N7imL2tXeS90lj4nzWD4tssBgAlUs3CMuKlXEgQ69XalVbxyN8xeQ7LH6vLMkL8PhhllLUhWoRNHKXurKfAdNSWU3KrhJpgkK5K5HNVVeKcmMdsFsYW-HMfnGeUPEBo5xjW30z9CB0xcdEMVXjvdT6c08yP4WovxYIa4WCVt2vQtxF7lzHDbeuTGjOdXEUHqXgvpZw75Me2GdV7t8L4CIGbLGxwQCgDuwSKpw4L27ggkfxHN4l_9SFvSPWDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فائق زيدان.. بوتين العراق
يطبّق رئيس مجلس القضاء الأعلى في العراق مشروعًا وطنيًا يتمثل في محاربة أركان الفساد ورموزه. فبعد قضية الجميلي، نُشرت وثيقة استدعاء بحق النائب حسن الخفاجي، كما تتحدث مواقع صحفية عن أسماء أهم وأكبر ستقع خلال الأيام القادمة تحت طائلة القانون بتهم الفساد وشرعنته.
ونجد أن القضاء العراقي بدأ يطبق ما يُشبه نهج بوتين بعد عام 2000، أي بعد انهيار الاتحاد السوفيتي، إذ إن أسماء مثل أوليوكاييف، وبيليخ، وزاخارتشينكو، وخوروشافين تُعد من أشهر قضايا الفساد التي انتهت بإدانات قضائية في موسكو.
فهل سيتكرر المشهد في العراق؟ وهل يستطيع القاضي العراقي فائق زيدان الوقوف أمام جبل الفساد الهائل الذي بُني منذ عام 2003، خصوصًا أن الحكومة الحالية ليست كالحكومات السابقة التي كانت، بحسب منتقديها، معطلة لعمل القضاء، بل ومتهمة بالتجسس عليه وفقًا لما تداولته بعض التسريبات الصحفية؟
الأيام القادمة كفيلة بالإجابة عن هذه التساؤلات، وبيان من سينجح في القضاء على آفة الفساد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77286" target="_blank">📅 14:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 04-06-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في بلدة العديسة (تلّة العويضة) والأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بأسرابٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77285" target="_blank">📅 14:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مسؤول ايراني:
يتم حالياً تحصيل ما بين 1.5 إلى 2 مليون دولار في المتوسط من كل سفينة تمر عبر مضيق هرمز، تُودع المبالغ المحصلة وفقاً لقانون الميزانية في الخزينة وتُصرف في الأماكن المحددة. جزء من هذه المدفوعات ليس نقدياً ويتم عبر التيثر أو السلع أو المقايضة؛ بحيث تقدم بعض السفن بدلاً من الدفع نقداً سلعاً أو خدمات ويتم خصم قيمتها من المبلغ المستحق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/77284" target="_blank">📅 13:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw2zKQ5GoU6cLO38QwSCG86daxvc6E5_SvAQOp_OFfBdWuFQWBXlVoTnDp4E7E6UQ2vUl1R2T5rJJd8WEH17X-3Z4YD4ZOHsqaCOC4hK9S4UNIeTyqdXNHsyJFx6QAnKnZb-QqPameHFi1M2glCI4GAzzGRkpgkuoD_WNTCUQjhZtvMmIBfC5U03CcgxpFPTqeBzxBKKXKgGOdzNPb-HNhiRId7LfW9cX-jym2rCgLG1RUgHXjs1h1n14e8-wqXaKNQp9fwGl6JL5vfkYTNy7yXjhQ-yK4QcTWrVL9Z-UgKJNVhMRthyLJEI1QFNIrBr3DqlQjUJB7DV4Sk_bIGiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
احتراق دبابتين صهيونيتين من جديد في زوطر الشرقية جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77283" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32dd98f8e1.mp4?token=Ef00tZCXp3JBENcpuExlVqge6yCpDxY04J-KDdCcNBhxAS9vseOIPvuRweZKTkRWz6iS17zvUH0mHcaQkRcRceo3iJWxOUeGRu7zlQZmzjlXxR3H5ua8I6JVXxQgHwGFGYhL42aBV49r93daDzLoXtlSA9LAa9ls_SbXQlU98cleYDMcYG4g-zmw1TEeoHKBeZV7KEJiTOk9bQGgJUJ9Rei0g2IZmhaAWmldKM8yTkcDIYfKSFcDb9lPn7WOyP1wO5tv5M1TMZZRuHBpZAmsiNmB2k6ywl0i_7aNoX0CUyZ-X-ttIIMvpjQ3NnYa-UPs5XFEglJcwDa9GjcDbMZKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32dd98f8e1.mp4?token=Ef00tZCXp3JBENcpuExlVqge6yCpDxY04J-KDdCcNBhxAS9vseOIPvuRweZKTkRWz6iS17zvUH0mHcaQkRcRceo3iJWxOUeGRu7zlQZmzjlXxR3H5ua8I6JVXxQgHwGFGYhL42aBV49r93daDzLoXtlSA9LAa9ls_SbXQlU98cleYDMcYG4g-zmw1TEeoHKBeZV7KEJiTOk9bQGgJUJ9Rei0g2IZmhaAWmldKM8yTkcDIYfKSFcDb9lPn7WOyP1wO5tv5M1TMZZRuHBpZAmsiNmB2k6ywl0i_7aNoX0CUyZ-X-ttIIMvpjQ3NnYa-UPs5XFEglJcwDa9GjcDbMZKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
استهداف صهيوني لعجلة في بلدة معركة بقضاء صور جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77282" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
تسلل مقاومين شمال الضفة الغربية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77281" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇦
زلينسكي يصرخ متألماً
شنّ الروس مجدداً هجوماً على المنطقة الحساسة المحيطة بمحطة تشيرنوبيل للطاقة النووية. أصابت قذيفة أحد مباني منشأة التخزين المركزي للوقود النووي المستهلك، وهي منشأة بالغة الأهمية، في ضربة روسية شنيعة للغاية. تعمل وزارة الخارجية الأوكرانية ووزارة الطاقة وجميع أجهزتنا حالياً على إطلاع جميع شركائنا على ما حدث.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77280" target="_blank">📅 12:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdrdkhupEUs4rbONALLLLy3YJhFnF5Ckbg8-1vbgadQdCnjlg5T0iZwonjdsnve1NquzAbu0ecczUSyrBTPVZDN6m7jfgQCatYBjsMwqxvp3XS4JXrhtf_crnbuqrnlbjIHoTR4k-EWgyP5k1UgN3Afu3uXi0xcMQ0TM0HlzqIRuiUrR6b40eQ56gx8vKAPyyklbj8pe1tEs2aLkVgwbPjR_8rIsRiRwxTSW92MCFR9_I4aQSP7R1pY4rosRzIoDaAlGU7dC2QxBQiZDToMd0Fg5l4rZfXIm7tbGkSuC5uwFJzOqEPh_ruRSL8FZSRIkUDZ7WRNx_dqWqJrqdQBKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0Fk7BvHSa8oIfOMPU5sPlxPhFGHa1UqXwOflfj01h3mU-JBJINsvEBH18d3zfNaN-ks-lUwo5qbE2ICFREXAXgLJRTzvEKeRj74U_7GOhkTe0WpysOzfEVRoOHTqQutiGc_jBdc2rBecdxhkmf9HELeEuA-g_HkVwDpFHMRFWIS19nHU_0l93l70_3IwDGRQtSlD1SA3D4j2vvL5UeFwHpfKsBlRNHmEL2Y08NwuY1seD78_dejoZvxFCZE1dUBFwr5OZPCgxJF1Mir7R_uDvy1BuG28uXWP7nvJrhY6LIY-bFVm8JN8IiFzABSyuJzaPh15r4uk8_joF0BG07nFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إصابة أحد منفي العملية الفدائية بعد اشتباكات مسلحة وارتفاع عدد إصابات الصهاينة إلى 7.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/77278" target="_blank">📅 12:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa629274.mp4?token=LYmjKy0h64pGQQvTbEiqTzET7lVP0BiHZYW9TveCqC5wm1YFKT44JVEyDsKMHi644F3TTLzhg0cePhBaKkQkSl7nFneoDG1jFmhiBokFceOuSfU1LfG6Rou_SIu_k1P3Qcyb7DbHpv4ITPqvEaklVQ0SIUaqShi6zv7NXGlElHiO4Wu_mCtP8S1yzN7wF3B7kiyvNpeveogxxKYGP8wI-GbCf7XFNaR65WrNARu6uUVg3Cukwr0MibretCvhf4N0qU0J9DX4VauDaJYeWoSUZf1CK_xehLuIGXboMJa_agcDDmLzt1AR3gNXWKwJWITdlb-xrDv0h21eMgGqYf25Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa629274.mp4?token=LYmjKy0h64pGQQvTbEiqTzET7lVP0BiHZYW9TveCqC5wm1YFKT44JVEyDsKMHi644F3TTLzhg0cePhBaKkQkSl7nFneoDG1jFmhiBokFceOuSfU1LfG6Rou_SIu_k1P3Qcyb7DbHpv4ITPqvEaklVQ0SIUaqShi6zv7NXGlElHiO4Wu_mCtP8S1yzN7wF3B7kiyvNpeveogxxKYGP8wI-GbCf7XFNaR65WrNARu6uUVg3Cukwr0MibretCvhf4N0qU0J9DX4VauDaJYeWoSUZf1CK_xehLuIGXboMJa_agcDDmLzt1AR3gNXWKwJWITdlb-xrDv0h21eMgGqYf25Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات الاحتلال تبحث عن منفذي العملية الفدائية شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77277" target="_blank">📅 12:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴‍☠️
أحداث أمنية بالجملة
احتراق دبابتين ميركافا صهيونيتين جنوب لبنان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77276" target="_blank">📅 11:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147558d9cd.mp4?token=PvAd9KKj3JnsZssfGtAD8fwUz89j-zxbymCk_SUHPpW2heXPeSKVXqmwbHxefNaVaBok3YzqGHaLBsTMya6OVOfIoOxj1bj7tKoKGRaChjtf6E3c2NEcBWliolqjwShboqdjt17a3sdQbRY5_YVSmsPBL6qoAWcBYCHFCNteBsuEgNnay581On_BhleMia2zDqcZE0xzL-FmPzk3l1T66mVFuafs_PSoNA1_mSnZdYBi9Ed9F1JVgVbnGN8X625OG51zgsZahY4RGCLrlOt1J129Rr1nyZSqrrq4pmsX9g351mVTzypGRGipYRSOTfOTTYqC9gSMRuN76JqG6ZJEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147558d9cd.mp4?token=PvAd9KKj3JnsZssfGtAD8fwUz89j-zxbymCk_SUHPpW2heXPeSKVXqmwbHxefNaVaBok3YzqGHaLBsTMya6OVOfIoOxj1bj7tKoKGRaChjtf6E3c2NEcBWliolqjwShboqdjt17a3sdQbRY5_YVSmsPBL6qoAWcBYCHFCNteBsuEgNnay581On_BhleMia2zDqcZE0xzL-FmPzk3l1T66mVFuafs_PSoNA1_mSnZdYBi9Ed9F1JVgVbnGN8X625OG51zgsZahY4RGCLrlOt1J129Rr1nyZSqrrq4pmsX9g351mVTzypGRGipYRSOTfOTTYqC9gSMRuN76JqG6ZJEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إصابة أحد منفي العملية الفدائية بعد اشتباكات مسلحة وارتفاع عدد إصابات الصهاينة إلى 7.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77275" target="_blank">📅 11:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tseJQrBoybKePb8Dq0arTUSX3WwYRLLgl7rU88WKKO72fEKYUFPPFhEf96Q2NiTnVgZ9YBWpqQEB8U1jCcd2Iyr4IoJ9saGU28QtDKpvpTUnry4Dn4EpdIwOSMHA9YC8agi59xZ-zq6kHcl9mezaHPzdmZNfhDxpzfJStO-dYn5rhI5j2LjJIBSiCfQ7Vd1lpHku5rguiRIu4NfQfNTa1PGY7-wBoC_es47Muzl9iOdZYgXJnIWoQRP6TlsknP4HXRL03ycgBVf98t0uRxfFbspuNtrIafDlkw3P9ZQsn7ENWhCImkdxdnEPRmwlOYBAJQOn7p2Wlkzfsz3XTPRUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
مشاهد من محيط الحدث الأمني شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77274" target="_blank">📅 11:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
صفارات الإنذار تدوي خشية تسلل مقاومين إلى مستوطنة تسور يسحاق</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77273" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b93ad27b.mp4?token=OYwCilovjTFArxOuppXG0vAhOHz9Z851biuvfvz5aUw9rwsUR1h5zTfZ9t_UqkW3a67y9fSmyjTLZrsZqzfu7pzXDOn1UxkQtaswN5U-ZbBojtrsnxL7lB9qs6QiwDU0iDQbERjHdXj4jl_5QV71wpJvXrzygtx_vyZ9OZVA78pk80c7McctGVMn7s9vtMSPYJWIGbTfuOgOTNhEepCzSnQ5QKjHsCkPrfhql6EJ3OSD-uLNf9DOtxck5DGwL3f8ku4R26BFk-zrmhVRXt2UpVyQUAcM7HcZhDwVE5GCD1hRRmmuK_5VHmNFt9qhbJp_w4-g9LgCixM0b4rxpYt0qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b93ad27b.mp4?token=OYwCilovjTFArxOuppXG0vAhOHz9Z851biuvfvz5aUw9rwsUR1h5zTfZ9t_UqkW3a67y9fSmyjTLZrsZqzfu7pzXDOn1UxkQtaswN5U-ZbBojtrsnxL7lB9qs6QiwDU0iDQbERjHdXj4jl_5QV71wpJvXrzygtx_vyZ9OZVA78pk80c7McctGVMn7s9vtMSPYJWIGbTfuOgOTNhEepCzSnQ5QKjHsCkPrfhql6EJ3OSD-uLNf9DOtxck5DGwL3f8ku4R26BFk-zrmhVRXt2UpVyQUAcM7HcZhDwVE5GCD1hRRmmuK_5VHmNFt9qhbJp_w4-g9LgCixM0b4rxpYt0qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات الاحتلال تبحث عن منفذي العملية الفدائية شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77272" target="_blank">📅 11:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627522356f.mp4?token=YzexFTF6qwedZkUYqoAUcUzIHeS5V2NSwi3g-WMKZBDNiq5smPHx3oiWDdeluNHhtuMnzKxtQ5a6kMu-4QHeMzpYN1N0u5zf5T1D98dpFkoSM8gm1Rhk9KWSO1O5OnQ5NXOIDwdlXfpPfJplQ68I9PHtELgHogwDPEkYpuokd3_GgfqDqfM-HwQQ63gvD_5BeU6JIoBGdyKoC2vZiBZmv-POLT3lpHmdsNP6p7Cd0I_VnkOqqLQetERvSnZ0qHCqX28lWsHEHUZU7dElkNMypxuYzbBCAOyH7t2BEma6PlPDTXfMleiDZUZDlE2D1pY8pzX8nQ3uJXhv8Yem6fHRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627522356f.mp4?token=YzexFTF6qwedZkUYqoAUcUzIHeS5V2NSwi3g-WMKZBDNiq5smPHx3oiWDdeluNHhtuMnzKxtQ5a6kMu-4QHeMzpYN1N0u5zf5T1D98dpFkoSM8gm1Rhk9KWSO1O5OnQ5NXOIDwdlXfpPfJplQ68I9PHtELgHogwDPEkYpuokd3_GgfqDqfM-HwQQ63gvD_5BeU6JIoBGdyKoC2vZiBZmv-POLT3lpHmdsNP6p7Cd0I_VnkOqqLQetERvSnZ0qHCqX28lWsHEHUZU7dElkNMypxuYzbBCAOyH7t2BEma6PlPDTXfMleiDZUZDlE2D1pY8pzX8nQ3uJXhv8Yem6fHRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إصابة عدد من حراس الأمن الصهاينة نتيجة إطلاق نار من مركبة داخل مستوطنة كخاف يائير</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77271" target="_blank">📅 11:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDtx7_wLYkNIOmd_4DUluzQDqNYRKGydth28rNmr_oNjyhtapHO9dIAdy4ipmLcAi1YbnALdHq3zZy2lOhb-bqga_l4IMdRA2VgoeWcyggVwV7rQLsznHu7volKxkHfxiXuVP8wHLHfJrHxTurbG6lBTH-YLJ1Em8WkMfUjr8xnNJoNYp9nUmMZaBFX5QancQmWHHD-4o4Cev8DqsbZTx2Xwz6PKnJGCwwfjo5VozACX_v7yl2wDB3PjLGUYEYsgYIebKkDtX5myZRBuCf2dkIA6AfMwzE4cnc6ceuyobzJEub-pfl0bk2nbgkq6lm7At0sEx1waciC4FLy9318hCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/77270" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzpfbvd6P_ZDCmh1OVG7znWoFHpKHroRLUxZdSpkHdO_ztvIvbbd0jX9XuFT-fvr66HyQ3hf-qCAuJuSUW-0FUtWOmzC_QXxtuzG1YpV6GN67dceP4nU_ydTALuZddglNMCV1JwdRwKAmQqriXqr4wCcKIJupE9pd47U5E2v3tFseP0VLaKwC_lPMlkjARsGdf0zN_73Q71qiidwm9Z3_SRhHEkVZl-DmarrZRO2Vu27iYgvh12SJ4hpXQ07e8Qd1qraEP47R5B0nMtQIKNCIlsjeIxcmNIiJo-2fcg0t0rGxY0AWw2-Oia2pOnWwQMA4aOVgxhs9H6LLx17tsFlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: ارتفاع عدد الإصابات إلى 4.. حدث إطلاق نار متسلسل، أطلق شخص النار على المارة في كوكاف يائير. هناك جريح، ثم استمر إلى تسور يتسحاق وأصاب شخصًا آخر. في تسور ناتان، تم الإبلاغ عن إصابة أخرى بسبب إطلاق نار. الحدث لا يزال مستمرًا</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77269" target="_blank">📅 11:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9305112b1.mp4?token=eXSR6g9nD2n-as4vqr3Ahp8S8dUeCuY-1j-BZMekp5uZ1rPFIIYKIt7KjbdpQL89vO_cOeatX4RFMBc2usJykF8TxVLZJcjpDk5m-qMopqI8XuWaWvi4NQWQ4CpzkYKIHL-iAAzuNADAkBl4oD33EUoa6QAinUfmHTAzXI3y0u5JZbio2gdEWfBahvuPwQ770VTvURjvT7Txlkm04O1gdguGQPWmmVU6L1PEmDI8NFBVYVh1rtpt5E4J_qx25Pmb00b1nlJJs7sVpf4sL868BqZS_hWt2UTzTdOMSFa8K2XNN7n2-RjwrSQ8CIgVjKFvItwd8bntRvJ06orfX1Hh8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9305112b1.mp4?token=eXSR6g9nD2n-as4vqr3Ahp8S8dUeCuY-1j-BZMekp5uZ1rPFIIYKIt7KjbdpQL89vO_cOeatX4RFMBc2usJykF8TxVLZJcjpDk5m-qMopqI8XuWaWvi4NQWQ4CpzkYKIHL-iAAzuNADAkBl4oD33EUoa6QAinUfmHTAzXI3y0u5JZbio2gdEWfBahvuPwQ770VTvURjvT7Txlkm04O1gdguGQPWmmVU6L1PEmDI8NFBVYVh1rtpt5E4J_qx25Pmb00b1nlJJs7sVpf4sL868BqZS_hWt2UTzTdOMSFa8K2XNN7n2-RjwrSQ8CIgVjKFvItwd8bntRvJ06orfX1Hh8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إصابة عدد من حراس الأمن الصهاينة نتيجة إطلاق نار من مركبة داخل مستوطنة كخاف يائير</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77268" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNcjEziGDTt-030UqtGn64LmzXdQtocNhWiS8RXBybV3rzjb7cS1h7VnEwquHvbzTtuG82nVsFrQqSZfnXN79LWBT2bWEjJW_KaqKeXRfc7pNly4buFtBUkChZm2-kKa6TlnigywYtyzfi5Y_0v2KVtf2dvNUd9UgUA0Zl3Um1Sl5iPQ-p1-Ait9otrYYePNj-WtORomezIes7xzOHqx6I5S8BIqCEirPWehyQehqhQV8DiUiqaln3fqbDQZ04guzZiTCeK0YllEg48N-jbzacFvI_GXWfpS299nj57HjI-e07s5ehR_l8bS4cd3CIuTtw6T1BgHBDARYGHQxVu5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77267" target="_blank">📅 11:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حدث أمني نتيجة عملية إطلاق نار في شمال الضفة الغربية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77266" target="_blank">📅 11:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77265" target="_blank">📅 10:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
‏موقع واللا الصهيوني يدعي بدء الجيش الإسرائيلي عمليات برية على أطراف مدينة النبطية جنوب لبنان</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77264" target="_blank">📅 10:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
محافظة ذي قار تعطل الدوام الرسمي في جميع دوائر المحافظة يوم الخميس القادم بمناسبة الذكرى السنوية لمجزرة سبايكر.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77263" target="_blank">📅 10:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774316044f.mp4?token=HihzKYo4Ow4y76dBOW0s8n6AqkbIn77OGJ0i8nusoWzI7BcZn_B7V34f_GANZmivbCk9jEZXKLd7mhLgyM3J-mozy3NMfVKuP1GRE4E4wHCFruU22nJl7f-hWY1lWKxhtom4c-C8F8z5WX1CWvGoweTUX8eJmgBuNzq2WUryb0BCW6e3HxK3r02V-irHi6r6z-PAly7JBHWeEIBpMUlMTiiv6zlfc-uAhQhIoXQk3if-o_8dOnOdtWZZatS0kQhftSjAOhs9FdQ3A1UHdhszU_RSx1H0_aO8vUza2fKi1JCDLHIPa5ClL6-aLhXIrRODDAtQDF3s0gCcE3KXAdvN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774316044f.mp4?token=HihzKYo4Ow4y76dBOW0s8n6AqkbIn77OGJ0i8nusoWzI7BcZn_B7V34f_GANZmivbCk9jEZXKLd7mhLgyM3J-mozy3NMfVKuP1GRE4E4wHCFruU22nJl7f-hWY1lWKxhtom4c-C8F8z5WX1CWvGoweTUX8eJmgBuNzq2WUryb0BCW6e3HxK3r02V-irHi6r6z-PAly7JBHWeEIBpMUlMTiiv6zlfc-uAhQhIoXQk3if-o_8dOnOdtWZZatS0kQhftSjAOhs9FdQ3A1UHdhszU_RSx1H0_aO8vUza2fKi1JCDLHIPa5ClL6-aLhXIrRODDAtQDF3s0gCcE3KXAdvN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77262" target="_blank">📅 09:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5968b0cc8e.mp4?token=if5yjjHmvSVllP7QaXzXq996r7mcaHOqiOQ0ZBYMWN2kU4jCxkJ6M23Mykg3V0CmeJzcbE3Di6HbJOl2miRtBHfZ38ZFDk2BY5DKDkT48ALdlpEMtTfI6WZ_kHgZfrjAxCD0eTGJmNT4I6wiWjwxfFeWcIekC67kaP27J50cUrLSA7H2OkyMaJR-mHuPB9Lon79efGkP2uhHuOI6Dum6Es-QruGbgBrkRAVpqgCoGL8C9ilRjWy3Ng9wNq0DQyZKyUmMDKfqzcxWaU83deyPD7eLoN2Xy1h6P7MA-nCjkk-rXI3eFl0sVU37Pdh8JIRimHin0yrCDQQ53_98-_fgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5968b0cc8e.mp4?token=if5yjjHmvSVllP7QaXzXq996r7mcaHOqiOQ0ZBYMWN2kU4jCxkJ6M23Mykg3V0CmeJzcbE3Di6HbJOl2miRtBHfZ38ZFDk2BY5DKDkT48ALdlpEMtTfI6WZ_kHgZfrjAxCD0eTGJmNT4I6wiWjwxfFeWcIekC67kaP27J50cUrLSA7H2OkyMaJR-mHuPB9Lon79efGkP2uhHuOI6Dum6Es-QruGbgBrkRAVpqgCoGL8C9ilRjWy3Ng9wNq0DQyZKyUmMDKfqzcxWaU83deyPD7eLoN2Xy1h6P7MA-nCjkk-rXI3eFl0sVU37Pdh8JIRimHin0yrCDQQ53_98-_fgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
سماء شمال الكيان المحتل نتيجة إطلاق رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77261" target="_blank">📅 09:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/77260" target="_blank">📅 08:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77259" target="_blank">📅 08:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇷
تم إبلاغ فريق إيران في كأس العالم بأنه يجب عليهم مغادرة الولايات المتحدة والدخول إليها في نفس اليوم الذي تقام فيه مبارياتهم، ولن يُسمح لهم بالبقاء في الولايات المتحدة لأي فترة من الزمن. إيران هي الفريق الوحيد في كأس العالم FIFA 2026 بأكمله الذي سيُجبر على السفر ذهابًا وإيابًا، وسيقضي وقته في المكسيك بدلاً من ذلك.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77258" target="_blank">📅 07:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة العراقية في واشنطن :
امريكا دققت على شخصين ضمن وفد بعثة العراق وقد تم استكمال إجراءات دخول أحد الشخصين، فيما تعذر دخول الشخص الآخر !!
وتؤكد السفارة أن إجراءات الدخول إلى الولايات المتحدة تقع بشكل كبير ضمن اختصاص سلطات الهجرة الأمريكية، ولا تخضع قراراتها لتدخل أي جهة أخرى.
#شراكة_ستراتيجية_وكذا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77257" target="_blank">📅 07:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
وكالة يونهاب
الكورية
: أعلنت كوريا الشمالية عدم التراجع نهائياً عن وضعها كدولة نووية، وتعهدت بعدم التسامح مطلقاً مع أي تهديدات.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/77256" target="_blank">📅 00:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febee0c094.mp4?token=s2oulauRgcveKB64M_nXSWhhCyp7MJulCiu5VMIzhozyMiKhFb-lR7fmzbT8hqDVOtR3CeN_wZuIEX2lAf7VURIlb4cNE8yQYA1V9cHWIQtdZptPrxgnPNiXySANo16bhAEksosF5S-BSeStKXWoP56JMZcnhqtT-_I9RfKpV09BrgKk6PNUbJaxSWlbh5lJ-Rue5tnCxBu_BYVZAvMIVgIeydSnVyeFPZn63YoLXcNf7Kzt3y9G88g5mLQyVaWnaLJI0pj-WhFgTW4UCyhu8IxFLX_4WEIM_x-4q4LbbYUxGQ9L0p70pRjK_neArqhL--wICesey1jLvvx6uIGa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الله يلعنكم ويلعن شرفكم".. الاعتداء على السائقين الاردنيين في سوريا وطردهم من قبل انصار الجولاني</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77255" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رويترز
: ‏واشنطن ستتيح أصولا إيرانية لدول الخليج لدعم إعادة الإعمار وإصلاح الأضرار التي تتسببت بها إيران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/77253" target="_blank">📅 00:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcnc0882Bp_KDXmeVqPD5aaFu8PxFKuKyv3z619_epgnwIhzp3U-vjRQDV0Ok64DYXF_tcPDWJnz0nTUpRbO7NaxJFKCpGcAa4GT6g0VDjBJVbdwRQMzIVDE-K9Ia-mdJh3RP5i4cNNGKhQQkIvtKDZfwBqn_Yl_JQc1fF09N-XYRo-nrrNdZi1QNtWwfsewn16tCEffO-lyo5IR-ldRlMvF0RPAZZ6y5zviRKgEGFr127_YyDc0VxVQTsfPhT91-XtHMCVwjEkNeavIHg64yVmVXxTMtfC0sxFw5p4H3OKKMHn254esowP48vxlAQbNqfQvwVDC6WANMCENazBrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
متداول: أختفاء تذاكر مباريات العراق في المونديال البالغة 1,408,000 مليون دولار
وثائق تكشف شراء 3150 تذكرة لمباريات العراق أمام النرويج وفرنسا والسنغال في كأس العالم، بقيمة إجمالية بلغت 1.408 مليون دولار من منحة FIFA المخصصة للمنتخبات المتأهلة.
وبحسب الوثائق، تم تسليم التذاكر إلى إحدى الشركات دون عقد رسمي، ما أثار تساؤلات بشأن مصيرها ودعوات لفتح تحقيق عاجل لكشف ملابسات القضية والجهات المستفيدة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77252" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRHzNc3Ss8GQUpfD4c7XUjuIEODt__qtrIAOhAQT2OthhX0V48DF2MHemhYhWA2ybQb_l7qNYmoJv4V6X09TajZB2_4CCO4fNM-Yxjy_ByWbfszMQNC2sKwslGTlx1CQZAeQ4wB6BKFeYiLqwM52Hx-ltDtjYaU_z-jfjnW0hWaSpgT8yrTsRgT3aebq5WmN7nOo4_6m0otU1VY6PvFoey1-i2i64wWAnT4A21PsZDmd9kn18rlRBDhX07vZeipHtVf1UumNu0RsF5IBSgIwSlw964lE4KecAFWRmKSNbEiNRKaZvKDyTek5AAWx6VW0ZythdIgidMwo7UJZEK6LNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بيان لمحافظ كركوك محمد سمعان اغا من القومية التركمانية يقول فيه انه بحث مع اردوغان في اسطنبول "أوضاع التركمان وسبل دعم حقوقهم واستحقاقاتهم السياسية"!
مراقبون: هل بحث اوضاع التركمان وحقوقهم واستحقاقاتهم السياسية يكون في بغداد ام اسطنبول؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77251" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
جنود جيش الإحتلال الذين قتلوا اليوم بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77250" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🌟
وزير الداخلية الباكستاني في اجتماع مع وزير الداخلية الايراني في طهران:
أنا هنا لتسليم رسالة خاصة من المشير الفريق أول عاصم منير، رئيس أركان الجيش الباكستاني ورئيس الوزراء شهباز شريف، إلى آية الله السيد مجتبى خامنئي، المرشد الأعلى للثورة الإسلامية، بشأن الوضع الراهن.
وزير الداخلية الايراني:
أُثني على الدور الفاعل الذي تقوم به باكستان، الدولة الصديقة والشقيقة، في الوساطة لتهدئة التوترات بين إيران والولايات المتحدة.
يُخصص جزء من زيارة وزير الداخلية الباكستاني لمناقشة القضايا الثنائية، بما في ذلك أمن الحدود، ومكافحة المخدرات، ومكافحة الإرهاب.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77249" target="_blank">📅 23:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdBFeu8-l_zFE2zHmJR-bkU4KkKO3JElttEHkiiYi6DX2yx5ASM9hIJofRzm_ugCrBPhyjGkgNjAeluT2WJPsa6vgnw__GGWmry6mSSeQY5r2u-z6QiU_60vm-U9ZQ2df8qSe622y7gFzSYTky0U4hraxd_vqRTsM30FxbMYfcviE01Fvh54D_haMECwGZGnGVcGL1nrel6B6cckiukeVCPO1vTBwE-C8xbFr5ZFd1vwYPm7TVAAnspgFat4NobCA2stinFdmulxNcVDsRXmemSGg1w0_zB5UlUjJ_9HAlGSbeoAXUHoWAO4h486oOLRe8m_AwyK85Pevzhg5sDfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
اكتمل العمل بالكامل! قام الوطنيون الأمريكيون العظماء، ومعظمهم من ولاية أوكلاهوما العظيمة، بالإضافة إلى دوغ بورغوم، وزير الداخلية، بتفقد السطح الأزرق الداكن المعقد للغاية، ولكنه قوي، لبركة الانعكاس، قبل غمرها في مياه نظيفة وجميلة. تم افتتاحها في الأصل عام 1922، لكنها لم تعمل بشكل صحيح أبدًا - والآن تعمل! شكرًا لك أيها الرئيس ترامب، شكرًا لوزارة الداخلية - والأفضل لم يأتِ بعد مع ممشى ترامب في نصب لنكولن التذكاري، وقوس النصر، الذي سيكون، إلى جانب قاعة رقص البيت الأبيض، عند اكتماله، أعظم مبنى في واشنطن. الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/77248" target="_blank">📅 23:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137470719c.mp4?token=rc3ojUdgVF-nDD_pmxXEI6L8KL6cKXYIb7Np-xlweEJe4GlYc6_f0s-MJWX3gYagH2KtIlznmanD0dE-fkleTV2HSMqt_MBkxB8DYm3v9uIl2XJsuncwuHWbOl8oT6DS9XzZvMkR7p27a8Pm3JNs16yzHWKBeT0V7hdnjkaHIHcnxpzRYTFu1IXn1xlC8lZS-Y6fz59T2jYcUHIyyFXnDBRQ5EyfpF5vJYKt6FxR2rq0J96Ad9JntqU6dEVTJojBNHNryy-ecf7mGzMNGOUhafaP-D6JLR1JnXo3mHYnI8puYYvrJKETRDuKBP6aY7FbA8Y1swDzs03q73HFUF5Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وزير الخارجية العراقي فؤاد حسين:
لجأنا إلى طباعة 25 تريليون دينار لمواجهة الأزمة المالية، والبلاد قد تواجه كارثة مالية إذا استمرت الحرب.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77247" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🤙
وزارة الدفاع الروسية تعلن أن دفاعاتها الجوية اعترضت 339 طائرة أوكرانية مسيّرة فوق عدة مناطق بما فيها موسكو خلال آخر 13 ساعة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/77246" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f2362693.mp4?token=GWHjfqqds3FciIhacFSDTsegJ-JNajzXeYfAThPJjurD3PFNDqEj_XUcf9LCygMJ_p1IKJsrC_RPg98X9_w8OhkHKToP8b2qeily9U9J6-HBspD_4GO21TGs41iP_84WOObVoYAFmwQmnv3rJqZccglL8Agif2tzPTMDqAJA55rSsLOas4GQbBe-Y3I1g8iRFQc0asylCNHQpkt_kzuKaJnsR86yIjmHy-I9dGx69MntN3HYFWmjPletp_rc51RyseMbSLqctbMbO60oG5RFOtfxWxx4aMZaXCpz-0ffopzQ0qS6D8xNbE7TTYJq99zWHajH6nhRY7GJsVX3AFEHKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النائب الكردي السابق علي حمه صالح:
هل يمكنكم إخبار بغداد أن 50 ألف برميل شهريًا المخصصة للتكرير المحلي حولتها الاحزاب الكردية إلى تجارة وهرّبوها إلى تركيا بواسطة ناقلات تركية! يتم تكرير 40 ألف برميل نفط يوميًا في مصفى لاناز ونقل الديزل والبنزين إلى تركيا بواسطة ناقلات تركية، محققةً ربحًا شهريًا يقارب 60 مليون دولار! والباقي يكرر في مصفى كار. جزء منه يُباع بـ 750 دينارًا. والآن، رفعت الشركة سعر البنزين التجاري إلى 1075 دينارًا للتر. أين ذهبت الأموال؟ حوالي ٨٠ مليون دولار شهريًا، أي ما يعادل ١٢٠ مليار دينار لمصفاتين... يا للعجب! يُظهر هذا الفيديو مصفاة لاناز، حيث تنقل ناقلات تركية الديزل والبنزين إلى تركيا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77245" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة خارك</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77244" target="_blank">📅 22:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsBfkijiHE7KxPq1sibweBHvTO2meAqsg4HP8Jm-l7lRau6jP5J218zJfodeKYSQfAE9VLWQ0D44iChWKgLA5DCppSSN3NPXVRLe3Kapm_t0atGoSCXpqeBGd7gAAgeMXqN4p17Ga4JgPk_EwisCK88-BPXOxEz85UoK1P3TdSCkFKvI_5p40d_rcNmqVhOh8bBq3cMj3u4fPifZxlsN8Nl_E9dC_nFCPUIw03RyKhy8_xOemukfNalIi7J3NZmTbzqvi3EJUfa6JQ4J5ykpYWMeT2xQ8Xz6phJ-kIaW0aiwcJzIdV7RAn2Fm3fouVVBlsCHFA5IY_LYCOrytAvrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقتل جندي من وحدة إيغوز متأثراً بجراحه التي أُصيب بها يوم الخميس في جنوب لبنان.   مقتل جندي من لواء جفعاتي يوم أمس.  إصابة 4 جنود إسرائيليين بجروح متفاوتة اليوم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77243" target="_blank">📅 21:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
وزير الداخلية الإيراني يتسلم من نظيره الباكستاني رسالة من قائد الجيش عاصم منير إلى قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/77242" target="_blank">📅 21:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77241" target="_blank">📅 21:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e387c11b4d.mp4?token=bNeN2B_WDuxqAWPncEyfQVk1doFsOt43jVg0WuKOoL30Wu0Ju7m95Pdxy0YzgpQgynhjQhXat_es22QONJrGW2Z9IpNp6nOD2Vd5yjSKZ9G4x_ey9WGCjBGDY8vzghuWLYOd3n1PU63rIgj-2KZd6wddE1P9g6DU0tSMnZ9eRRYdqIjwWc8_NT7gOpnXNlE-L6F3fcEdPCz6aGvq5l6YB5ks569pHaC_xZ9bjpK9g-JrOFyNL1bQw245Ql57px8InlZHGH7e69aABxMQtt22b4Krr_dH_7MeNeAqhQq0MhbKwd50WrTPyKGoz3sk_8Jm5twpPpUvfzI7Bk3AWay9SIhk8BdoJ1V1hRu_sVBvy2hCIWMRWdJNJ8dgptX5p0oXJXXmg3TrXEcup8hlhIxvNpSi1w9MeefxDsZ6L-C0uvunsfnPae-rPpNqDqrRQHmM4QpCYyX0eAsrFF0SdhmHql8MUz1OhjXr6tvagTt3gtXHMf0xMcKWpOalHQZhWFVUXHMKgL5pxvYqGwfZnoOWsKWixS9aEbnHzKIEVMWnelykWdvv0eeokh9-r9nb6UXoxBpHuSghmBUPtga3uIsS82tQ1o9PDBcrSgdwZCjQz2yrw57IyPKos6pKYqkKEJi3trmm1SGt2v-42I8CCmcmgCmkaew454DWehIP-MzKg8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لن تبقى لكم دبابات.. إستهداف دبابة ميركافا تابعة لجيش الإحتلال الإسرائيلي واحراقها في بلدة يحمر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77239" target="_blank">📅 21:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI10oALC6syVe_3L3HTRtNC_DdF7M0xXQrvLKW9snHS1pCGGgUEB9rV5KUmBqquEz_YvlYi3BAm69Qp83KOA1o8cY9uUAB8pET5mgbCbU_wD0CrRTSAODfybWtZf3oyiLKCjZdRjJb4BJ91ny1xY8L5NvJaoNQGUi503mAel1_3sfQyJMMhaqtT9R0NC8NRDzCAmMHVmOSJC-QPJEJp-KtD_jCWfnUUSfA9QW21OmRrlt6891vCMIFagFL8xvCeIkLLy91yEQjDgVj8KDUw8JwtVP_14lVDZCJKPF-jx_s0EJeq6o4im1eNHBHP_CbeBUJwrFttzOzfmgbyc51grPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
مكتبة باراك حسين أوباما، في غضون 10 سنوات، عندما تنضج تمامًا!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/77238" target="_blank">📅 21:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمعت في جزيرة خارك هي نتيجة تفجير ذخائر من حرب رمضان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77237" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
