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
<img src="https://cdn4.telesco.pe/file/Bu24iHtvEjUJy_zTHrL41MdZFXfH9Qjo9PouDhTgXf5fk1A-1cfA0zbArS3Eg2jpCFdCRlCvVxxlOG3vDX2YwxV1sAy6hKeY4awqJi8-cG17qyM6Bl36GRxAo5YicF_4AR2jWYtCN-sCD19ts4m7AVlwA9df2PzoY4PUaKQfzv9dzY4vJ1WYHxFp5sbN2hwrT9qJ4otdfSj7VvSja3GzvKGKLqyhs-tWJ5ErVtvRyycO3ZPMnvUnYO-iti_l6EWVSwH1V4EDNeeDaT8iIORPd90rs0Nm3JaXYKDQnnZWFgD2bu2tDlflg4aIpK5kxArP8flm-hY3mm6AKeskcJPgxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 261K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وكالة فارس عن
مصدر مقرب من فريق التفاوض
:
- إن ادعاء سي إن إن حول المفاوضات الجديدة بين إيران وأمريكا في خضم الاشتباكات فجر الخميس غير صحيح.
- أن الجمهورية الإسلامية الإيرانية تمسكت بمواقفها وخطوطها الحمراء المعلنة خلال سير المفاوضات ولم تتراجع عن مطالبها الأساسية.
- أن النص الذي أكد عليه الجانب الإيراني سابقًا لا يزال أساس مواقف طهران، ويتوقع فريق التفاوض أن يضطر الجانب الأمريكي في النهاية إلى قبول الأطر الرئيسية لذلك النص.
- الضغوط السياسية والتهديدات العسكرية الأخيرة من قبل أمريكا ناجمة عن مقاومة إيران لمطالب أمريكا غير المنطقية التي تتجاوز الاتفاقات قيد النقاش، وأضاف: «السبب الرئيسي لتصاعد الضغوط هو تمسك إيران بمواقفها في المفاوضات.»
- أن النص الذي تريده إيران، بسبب تأمين مصالح ومطالب طهران، لم يحظ حتى الآن بموافقة كاملة من الجانب الأمريكي، وهذه المسألة تعد من أهم العقبات أمام التوصل إلى تفاهم نهائي.</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/naya_foriraq/78376" target="_blank">📅 15:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f18740522.mp4?token=HLuAaWffiYRI99wxFadQjFJALgVwlj8VYkJmoU0dFsJufBS2Duk4JWUExVMaM8cyQIIb8_Rijb0Ej_jOj5DTSLYFdm_Dr5SqQmdECYbiiN2ET8V-Ape4KCcdMIVzCp2lDbMwn1cBHskg_xe_mV3BtxLAanhsTTRggIitv6SnP7zCIMFB3GY5_l0VsjblhSDP0zR20zLBMnziCHebcfkr5JINset0G8Npr8WQhvuA9JwpY23R1PqnQKwTuCXTKprudXWtlOiLmr_TVAXdk6f-fHwDFEa2Ne3lRT4ef8aFzpBuFomQBJD3N-v3owve925U5inYGdYnGj2EAcW9Jc0Bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f18740522.mp4?token=HLuAaWffiYRI99wxFadQjFJALgVwlj8VYkJmoU0dFsJufBS2Duk4JWUExVMaM8cyQIIb8_Rijb0Ej_jOj5DTSLYFdm_Dr5SqQmdECYbiiN2ET8V-Ape4KCcdMIVzCp2lDbMwn1cBHskg_xe_mV3BtxLAanhsTTRggIitv6SnP7zCIMFB3GY5_l0VsjblhSDP0zR20zLBMnziCHebcfkr5JINset0G8Npr8WQhvuA9JwpY23R1PqnQKwTuCXTKprudXWtlOiLmr_TVAXdk6f-fHwDFEa2Ne3lRT4ef8aFzpBuFomQBJD3N-v3owve925U5inYGdYnGj2EAcW9Jc0Bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي الارهابي:
تصرفنا ضد الناقلة غينيا بيساو أثناء محاولتها نقل النفط من إيران عبر خليج عمان. أطلقت طائرة أمريكية صاروخين من هيلفاير على غرفة محرك السفينة.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/78375" target="_blank">📅 15:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رغم تكرار استهداف الجيش اللبناني..
الرئيس اللبناني: لن ننسحب من المفاوضات مع اسرائيل رغم الضغوط وسنكمل الطريق حتى تحقيق مصلحة وطننا</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/78374" target="_blank">📅 14:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏وزير الدفاع البريطاني يعلن استقالته إثر خلافات مع ستارمر بشأن الإنفاق الدفاعي</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/78373" target="_blank">📅 14:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCMakkQ1HKbMk6Zd8E7mETdpa_ouHI0u0T6OSXOWWuQBLMG10KvXTVArNXKjqI4iQn6eAzfls8JjMjHnNd2AOKoU8_5L8Uj4ZJE6Uj-mgFAHfQ-Pp_1pnOJDQlB-7Scxi4Wva01iqjqwKIpRdIbFmvdyNrQhKZPjthQOxHvKutZcryElQNGNCVsJpi-CLJE_9tx-27aiRJNnBPBxiSrFoc-wwOKl1ZDovhiBd3eE40CYluewVvCgYrkqiKxMO7EomCWWK-jGKgwLg-shKWcYQoOABQSMkpTtvkk1RsJAYv3bAwNJPe6KKckVgLKkSbrjvQWJQDx1Q2cKQQS8fmICpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محكمة جنايات الكرخ تصدر حكماً بالحبس لمدة سنة على المستشار السابق لرئيس الوزراء خالد كبيان بتهمة الاختلاس المالي</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/78372" target="_blank">📅 14:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇳
الخارجية الهندية:
3 سفن هندية تعرضت لهجمات نفذتها البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78371" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الايرانية:
نظراً للتوترات التي تسببت بها القوات الأميركية المعتدية سيبقى مضيق هرمز مغلقاً حتى إشعار آخر وعلى الجهات التي حصلت على تصاريح عبور أن تتحلى بالصبر وتنتظر توجيهات جديدة منا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/78370" target="_blank">📅 12:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">📰
رويترز: إيران والولايات المتحدة لا تزالان تتفاوضان بشأن اتفاق مبدئي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78369" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار في سماء الأردن قرب الحدود السورية من جهة السويداء.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/78368" target="_blank">📅 11:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📰
وكالة فارس تنشر تفاصيل جديدة عن عملية اليوم:
نفّذت إيران خطة استخباراتية وعملياتية معقدة للهجمات التي استهدفت بعض القواعد العسكرية الأمريكية في المنطقة صباح الخميس.
🔹
ألحقت الهجمات أضرارًا جسيمة بمعدات باهظة الثمن للقوات الأمريكية، على الرغم من أن المسؤولين الأمريكيين لم يكشفوا بعد عن تفاصيل حجم هذه الأضرار.
🔹
أفاد المصدر العسكري بأن القوات الإيرانية كانت تراقب مسار وموقع طائرتين أمريكيتين كبيرتين من طراز P-8 منذ إقلاعهما. رُصدت إحدى هاتين الطائرتين من قاعدة دييغو غارسيا الجوية في وسط المحيط الهندي، والأخرى من قاعدة أمريكية في غرب أوروبا باتجاه جنوب الخليج العربي.
🔹
وبحسب معلومات قدمها هذا المصدر العسكري المطلع لمراسلنا، فقد استُهدفت مواقع هاتين الطائرتين في قاعدة الشيخ عيسى الجوية في البحرين وقاعدة علي السالم الجوية في الكويت بأسلحة إيرانية دقيقة.
🔹
أفاد مصدر آخر بأن إيران، باستخدام الاستخبارات والمراقبة الميدانية، رصدت نشر ما لا يقل عن ثلاث طائرات مقاتلة أمريكية من طراز إف-35 في أحد حظائر الطائرات بقاعدة موفق السلطاني الجوية في الأردن حتى اللحظات الأخيرة قبل إطلاق الصاروخ، ثم استهدفت الموقع الدقيق للحظيرة بصواريخ بعيدة المدى تعمل بالوقود الصلب.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78367" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78366">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78366" target="_blank">📅 11:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745a3cf224.mp4?token=qfXN_OrzLwo8i_IZgH60I0f9BTqrx26c_yQq3qgMDKnfweMqEukDWV5l36AtivgPlWH5odZfY9IKbS6uB4u3UOAa6OId5vgUd7NlU_GRtk5ubMfd9idbMuRQ0rpmhXeOxM71WqR4K2j_VSAjUaFJIubBzJfXycx5fHGDyUhRrJmrAmslLjGv5dL0hj6rcZ6QIuom9KlA7rO26EVp6iK2phCQGXzEtB1gxA06vK3O5cCFyL_qNPprA5IUVGsgh7oQ9nIsbbJWSNz4ofmiHOcJgUoAofalrNk8mOxg4DF0WFy8rdiLl1t7U09HCnatk8aKmTjvWEFSPGyb8j-FH-X6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745a3cf224.mp4?token=qfXN_OrzLwo8i_IZgH60I0f9BTqrx26c_yQq3qgMDKnfweMqEukDWV5l36AtivgPlWH5odZfY9IKbS6uB4u3UOAa6OId5vgUd7NlU_GRtk5ubMfd9idbMuRQ0rpmhXeOxM71WqR4K2j_VSAjUaFJIubBzJfXycx5fHGDyUhRrJmrAmslLjGv5dL0hj6rcZ6QIuom9KlA7rO26EVp6iK2phCQGXzEtB1gxA06vK3O5cCFyL_qNPprA5IUVGsgh7oQ9nIsbbJWSNz4ofmiHOcJgUoAofalrNk8mOxg4DF0WFy8rdiLl1t7U09HCnatk8aKmTjvWEFSPGyb8j-FH-X6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78364" target="_blank">📅 11:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وكالة فارس عن رئيس منظمة الطوارئ في طهران: إصابة 3 أشخاص بجروح في حوادث مرتبطة العدوان الأميركي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78363" target="_blank">📅 10:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏الجيش الأردني يعلن تعرض الأردن لهجوم ب 20 صاروخا أطلقوا من إيران فجر اليوم باتجاه منطقة الأزرق</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/78362" target="_blank">📅 10:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78361" target="_blank">📅 10:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلاغ عن حادث على بعد 21 ميلا بحريا شمال شرق صحار في سلطنة عمان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/78360" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
🇺🇸
🇮🇷
تاكر كارلسون يتحدث عن إيران:
لقد علمتنا الحرب في إيران أنه في الواقع، ليس الأشخاص الذين تنتخبهم هم من يملكون زمام الأمور في القضايا الكبرى. شخص آخر هو كذلك. في هذه الحالة، بنيامين نتنياهو.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78359" target="_blank">📅 09:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRhApQa-RX1SCpBfocq743Z47S0KddqzU0w6pbxJmGqRDyRPeHF4GzswhJ0st4vsZ8n8MC-34WfqwtHFNcwqMbFtwbroikFXeEy39pglaDbcF9bTyR1zpgwoeO50ijBH2nVBXVyrz3ktdX8DzM3snunQF7MTbC3dv8Rr_GPaNWXgy9DmTr7wPa4FXhwTVFtu3NOaAu9s-MJ7apCccrnmxxdPkfmGZCvBab1WIIAaFecEDfAD06YWCU3Yel4rny3O5By5yc1Z3ltelJ10iy5crQnY3M2g8WYPTF0ebhJhh1bfLLEmXZoXTDm-BiifxB5WOVFQvyE1L9U3ypUk9XgZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الداخلية البحرينية تدعي إصابة بسيطة لطفلة جراء سقوط صواريخ اعتراضية أثناء محاولة اعتراض الهجمات الإيرانية  احتراق مركبات وتضرر منازل في المنامة ومدينة حمد جراء سقوط شظايا مسيرات</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78358" target="_blank">📅 09:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCWwozzu4nBot5CoPGk0JhfHw7K2-1W02uu--G17a5jJpwre_tiz_infpQ7zGAeMHWw4Pk9-bzs4QUbKKafhEH7CHquN7PyoobzCl_ZZHTfcGpQ44536ogaRMdPpAs4GUzBh2NRk7edCN4UtD2tWGCvsWRgiy4KZi7BUHFILDmvSnOt9lMc0UQtFzb5wOvqY9HD9SWwe74kWTmlg9HNRU1noF4Ke5PBRVSQVvK5x3WStBgvsNyWFOZcnji0WqcpzaPJuxlAPEtzw0p02Yb_0L86eYfRpCk0xx-w0pddrsOtyAyPNLivovK1bM1f-q2sQeLMiQCSlKdJSgn6qCqq9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الداخلية البحرينية تدعي إصابة بسيطة لطفلة جراء سقوط صواريخ اعتراضية أثناء محاولة اعتراض الهجمات الإيرانية
احتراق مركبات وتضرر منازل في المنامة ومدينة حمد جراء سقوط شظايا مسيرات</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78357" target="_blank">📅 09:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تسلل طيران مسير من جنوب لبنان نحو مسكاف عام</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78356" target="_blank">📅 09:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تسلل طيران مسير من جنوب لبنان نحو مسكاف عام</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78355" target="_blank">📅 09:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اغلاق المجال الجوي الكويتي كليا بدأ من الان الى اشعار اخر.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78353" target="_blank">📅 09:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: في حال عدنا إلى القتال مع إيران، فإن لبنان سيتحول إلى ساحة ثانوية. ولذلك، بدأ "الجيش الإسرائيلي" بالفعل تقليص قواته في لبنان، لكننا سنشهد بالفعل اليوم هجمات إضافية في لبنان، مع الحرص على تجنب استهداف الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78352" target="_blank">📅 09:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b906ec55b.mp4?token=QV78mu5a0mxpbC5CUpyb27qZPtArjRb2XScRgK_OCerOMDmm0Eyi6Dw6pJX2g_zrQjjUSprkEPK3W14RnliRcwm0TUgImW6caBh3GZZ3QGFTYvDYNnsIAYrmD7r_mUt0OH1H94X3PN35dzgqsjfPrc_YJ_HPFbnGKYRFP5fk_jsC7DPhgwQvPktZ6B-w2syzbn75QbcKn_RltG_YRpJJnOo_mabRIuszdx_8UupdOEEMDeUZdhebfrQkkFUSiFvZKO5ziV3fCuLpK3eK90_bp_CTCQ40XKmyzhKHH3TYDF-7ywK3fmD--ZAVhh7Vyg1r_5OeUUcM3R3GsBiqocOiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b906ec55b.mp4?token=QV78mu5a0mxpbC5CUpyb27qZPtArjRb2XScRgK_OCerOMDmm0Eyi6Dw6pJX2g_zrQjjUSprkEPK3W14RnliRcwm0TUgImW6caBh3GZZ3QGFTYvDYNnsIAYrmD7r_mUt0OH1H94X3PN35dzgqsjfPrc_YJ_HPFbnGKYRFP5fk_jsC7DPhgwQvPktZ6B-w2syzbn75QbcKn_RltG_YRpJJnOo_mabRIuszdx_8UupdOEEMDeUZdhebfrQkkFUSiFvZKO5ziV3fCuLpK3eK90_bp_CTCQ40XKmyzhKHH3TYDF-7ywK3fmD--ZAVhh7Vyg1r_5OeUUcM3R3GsBiqocOiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
غارة صهيونية تستهدف منزل مدنيين في سهل طاريا بالبقاع الأوسط شرق لبنان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78351" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMV5thf6w0DltBmN2pjPND-IQEpCFblZnS0qIGZv9mXYX_wn2WcQuIEuTNmAYACcoGM9TTZIJJJfn18dHaGJs4BF8IvB2GQxDo5UzxkBTwH4QA4McTF2JOiBLhJhGEb2w_b1WJAZEL7z1jLsq1ufgZU4NZx1njqok5IEXvrgf9G4X_JpVtksJ6moKD4eee2VE04gkMXX9M_tYubQpQ--2ESf6e0-ORceXuEiFqjAIBNBB13Zr0MboEzJx7XtRXVt4FnUBvz5sBrKkIEz6a-lVkSFoOY8ZsBSNfK14eFet1y2kKvVw7HSjNbueFjwAVzbuWPL3gigQ9-0oyHJR9A14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ايران لفصائل المقاومة
العراقية
التي نزعت
لا تكونوا مثل قصة الأسد العاشق  …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78350" target="_blank">📅 08:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeCY1Nm4oozu_bwUcgy_ugChgh1qxd8zf_ZsEiZiJUm2iPzPILc8BKx_09aWJPDH7K2dyzEhitPQbmIE8lmvgh0sJLnUQZ8OKk8WEDPOERi7FpALSzpzdGHZsXLPKBIr_5FL5qrswtTYxTmEPlMJgocViHyZ5KP-JG6fYLoqA6iVn1fDQuajYyPdgaitbLC8xTTZ270AI68FepICiQlkPPOQqHokZNY7pMGAXeu-0YawHCNIvo8-jgJfGuKAXlsXQoZmWCYyyGGbKzuj_cu47g9211HSC7D3aZvvKoXu7mmrpjLwUAx0yEmfpE--9uRbZRPzsBoGqxEbc6syba-f9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مضيق هرمز الآن يخلو من جميع ناقلات النفط بشكل تام.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78349" target="_blank">📅 08:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d5a664ee.mp4?token=ibVveBkRyjOe82GpdHxREYAoIuifYSG_KGJnDovKr5OZIENu308dE1ZpSJ-toz6DROzdklb8UykTbojiTs1YllyPCEQBRLV-N8eovdRHYoF3wad9alP5r7JJZagyCvupYnDnro2AWpMWCzNP1-VclkNc13A1ErBXMpgh3lQZ2B892BbZe6c9VU4JQeFPA0LQvDWI8lfNfDhO1V7IdDzNy0cdYiHGDlwLjZUMXeOOS5MQGTG6bvLqSYXLo13zyeYUy70sVyJ_FvxCnkbDsjL2Jt2d_WwZ-75WRedtweIIAzmK1AUoPoBdCsIh1_cpMnK8fubKty_9h5pejFTBkAOaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d5a664ee.mp4?token=ibVveBkRyjOe82GpdHxREYAoIuifYSG_KGJnDovKr5OZIENu308dE1ZpSJ-toz6DROzdklb8UykTbojiTs1YllyPCEQBRLV-N8eovdRHYoF3wad9alP5r7JJZagyCvupYnDnro2AWpMWCzNP1-VclkNc13A1ErBXMpgh3lQZ2B892BbZe6c9VU4JQeFPA0LQvDWI8lfNfDhO1V7IdDzNy0cdYiHGDlwLjZUMXeOOS5MQGTG6bvLqSYXLo13zyeYUy70sVyJ_FvxCnkbDsjL2Jt2d_WwZ-75WRedtweIIAzmK1AUoPoBdCsIh1_cpMnK8fubKty_9h5pejFTBkAOaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
قوات الاحتلال الصهيوني تشعل النيران في أراضي المزارعين الأردنيين عند الحدود الأردنية الفلسطينية ؛ في الوقت ذاته تقوم حكومة الأردن بالدفاع عن الاحتلال وحمايته وصد الهجمات عليه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78348" target="_blank">📅 08:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏بيان لـ22 دولة يطالبون إيران بالتوقف عن مهاجمة الأمريكيين على أراضيهم</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78347" target="_blank">📅 07:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭐️
توثيق يظهر بوضوح لحظة تجاوز الصواريخ الإيرانية، منظومة باتريوت الأمريكية واصابة قاعدة موفق السلطي الجوية في الأردن بشكل مباشر ودقيق.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/78346" target="_blank">📅 07:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇧🇭
البحرين تعلن تعرضها لاعتداءات جوية إيرانية جديدة</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/78345" target="_blank">📅 06:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صاروخ إيران يخط السماء الأردنية مستهدفاً القاعدة الجوية الأمريكية</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/78344" target="_blank">📅 06:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMhapgjexQJj7xJt49p_1BLmkojAwtXyvygmLQjlF7ODTdJKdpRy_FwMKU091kVvaEqQgrVkyGcC6RkrrQzYBZRMWFUZ8Zy28wO5DdwE4WZ4Ism0SQ73oRvMlxQ3rzOFnPXeSDRAVobirKfXeo2hTX5Iwlgl7gBDZ5RuO1VQegWRxvFVpsBssRf_4TNZlvApkRIJ4OAGB9-le_IyRkWM_b1GrjaCQea4AcIJBCGHJiDTjAJjoTq3ybunHWVzExUCkay4rOmg45v02egVBnqJ_bug9hjG_ySw54bFwCdoP7_bri9apqkcRxWhP9P0SoNtsFFYg0kTiltBST9Puw3cAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارة الاحتلال الأمريكي في الأردن:
تشير التقارير إلى وجود صواريخ أو طائرات مسيّرة أو قذائف صاروخية في الأجواء الأردنية.
يُرجى التوجه فوراً إلى مكان يوفر حماية علوية والاحتماء في مكان آمن.
ابقَ داخل المباني وانتبه إلى الإعلانات والتنبيهات الصادرة عن السلطات المحلية.
ستواصل سفارة الولايات المتحدة في الأردن متابعة الوضع وتقديم معلومات إضافية عند الحاجة.
﻿</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/78342" target="_blank">📅 06:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEDX4s70sm2astJkgJXeoxCwSTHNA6QOGlJmED7ZEdmfSshEWcGUi5WmcvQnsFyybevyE--4QRy8b0Ea-YUeEuUKAW9aklvF6_rUU3YU1aPJOD-GpnmpGM-IlxMj4w9tvCOZt03g9FqB2-VHe-ZcDBCToipu80gKa77lIlx2pWbKj7PcGmOX3fZ0Gyk9kmUNef596ojH-fdtmiLemwQ8_ysi4Y90uFMyuoNYiDDWQXY8mwWodOok6bD7hswUW75ugH79ROkgL_hlcff4nNk9e9YuoxwXo9Lc22nveyyhC8VesXXHHPjX8gmM3ci6DYlin7qGblFYcGyHAJhBp2Pa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحرس الثوري الإيراني:
إلى الشعب الإيراني المؤمن والبطل، الذي أظهر خلال أكثر من مئة يوم من الصمود في ساحات المواجهة مستوى جديدًا من الوعي والمقاومة؛
عقب ما وصفه البيان بـ”الإنجازات” التي حققها مقاتلو الإسلام فجر اليوم في مواجهة العدو الأمريكي، وبالتوكل على الله، قامت القوة الجوفضائية التابعة للحرس الثوري – ردًا على الهجمات الصاروخية للجيش الأمريكي على موقع ترفيهي ومجمع إنتاجي ومحيط ثكنة عسكرية قرب كرج ونظر آباد، إضافة إلى قاعدة محلية للحرس الثوري في بريشوا – بتنفيذ ضربة تأديبية صباح اليوم.
وأوضح البيان أن العملية نُفذت عبر 12 صاروخًا باليستيًا استهدفت مواقع تمركز مقاتلات F-35 وF-15 وF-16 الأمريكية، إلى جانب منشآت مهمة للجيش الأمريكي في القاعدة الجوية ومركز القيادة والسيطرة في الأزرق، مشيرًا إلى تدمير تلك المنشآت وعدد كبير من المقاتلات.
وأضاف البيان أن عمليات مقاتلي الإسلام ستستمر ما دامت اعتداءات العدو متواصلة.
“وما النصر إلا من عند الله العزيز الحكيم”</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/78341" target="_blank">📅 06:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13df2979dd.mp4?token=ZIJa41sC1HAydR_ejkW2LuLiFm14JFFyuaElaOjnX7vJ1Kiz8o67FOAty6XlO_KmhRKQfXjsyQ_ak_wdSRBO2MejfN-_rFIMv_4f2n7z1As-5q9GLycYCagG7UL8SgDpo92M_H20lCr2QRzA5Uvz4ptRCCVoNnLPhOPp34U8XnrB1fR5L2mau60AhzViDgzTsmcn9K4bXOtiy-zKkax9z0gIJwV3nqrO4I1G6HKUlNbXEgM4VXY3iMkDanoDf465Lb-CSeorFhUPcftsCENet62lRkVDLwOCQDqOh3422PGFQJrOhG84a9F0eMYuxIpDJyXAiU-dSJ78QyMNrRTr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13df2979dd.mp4?token=ZIJa41sC1HAydR_ejkW2LuLiFm14JFFyuaElaOjnX7vJ1Kiz8o67FOAty6XlO_KmhRKQfXjsyQ_ak_wdSRBO2MejfN-_rFIMv_4f2n7z1As-5q9GLycYCagG7UL8SgDpo92M_H20lCr2QRzA5Uvz4ptRCCVoNnLPhOPp34U8XnrB1fR5L2mau60AhzViDgzTsmcn9K4bXOtiy-zKkax9z0gIJwV3nqrO4I1G6HKUlNbXEgM4VXY3iMkDanoDf465Lb-CSeorFhUPcftsCENet62lRkVDLwOCQDqOh3422PGFQJrOhG84a9F0eMYuxIpDJyXAiU-dSJ78QyMNrRTr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات شاهد ١٣٦ الحيدرية في سماء الكويت باتجاه القواعد الاميركية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78340" target="_blank">📅 06:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78339" target="_blank">📅 06:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d8e15dba.mp4?token=kT2KqYe5f1zyK5snJ7CJcwhRNlwbwokVozheXdLccqUZEB-vTXrYaTr-J7GOaFh8m0h1XgmU6kv8ny1wKXsktfkeLya4A6EuRbAerXHHAEldLH_lXsewpgxMposEnwj7suXV95q4g17ZotskgqRTXufYS095_D1XaeNdoWOiBtWz7axN7MF0RukeiFG5FrT56C34aOb04bDTokCXghsntyJo6oO6BHNCFAGhGbjk_SNq7Hasn_GdSVfc50AMv63_hcXjcG6yDHTF9oeltqGRlWoJgBdg_1rR4aolsrf0kkWRqs0DzjjUewmZcRFW_x5I0qiLvOBptBrXiuPaGiMKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d8e15dba.mp4?token=kT2KqYe5f1zyK5snJ7CJcwhRNlwbwokVozheXdLccqUZEB-vTXrYaTr-J7GOaFh8m0h1XgmU6kv8ny1wKXsktfkeLya4A6EuRbAerXHHAEldLH_lXsewpgxMposEnwj7suXV95q4g17ZotskgqRTXufYS095_D1XaeNdoWOiBtWz7axN7MF0RukeiFG5FrT56C34aOb04bDTokCXghsntyJo6oO6BHNCFAGhGbjk_SNq7Hasn_GdSVfc50AMv63_hcXjcG6yDHTF9oeltqGRlWoJgBdg_1rR4aolsrf0kkWRqs0DzjjUewmZcRFW_x5I0qiLvOBptBrXiuPaGiMKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توثق تصدي الدفاعات الجوية الإسرائيلية لصواريخ ايرانية في اجواء محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/78338" target="_blank">📅 06:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa610bcbe1.mp4?token=RJZb8wdn-P6yPD_-m4Px6uerCBOYaATFwWi9fzbfcc-gKFlI_JM87zrLuBTWH0-YVFWmmCeutf_9ZwR8GfOtLb-0SrMu7Rjq8uq2Zj5-NGSbHCZmfNFxPCaUbqdpI_OrRKmPni8-UAKbCezlCp4O59soZYsidVbhEG81TZb_DJSoCm01Ht8fpxz4DRHGoAKRjX_YsfZTxWQSue_JTKuiJEog8i8DugNhxcKMvlsWCLKsUhllHyHYy_jnA9qO7Ny_FCENG8LoajSloUdrYaDOhMtg45xVz9ZlsFZodtCP42OBuBgx7GyzuxYWQPIPd4Q8zi-V7dVj4kWzUTR-AFXAjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa610bcbe1.mp4?token=RJZb8wdn-P6yPD_-m4Px6uerCBOYaATFwWi9fzbfcc-gKFlI_JM87zrLuBTWH0-YVFWmmCeutf_9ZwR8GfOtLb-0SrMu7Rjq8uq2Zj5-NGSbHCZmfNFxPCaUbqdpI_OrRKmPni8-UAKbCezlCp4O59soZYsidVbhEG81TZb_DJSoCm01Ht8fpxz4DRHGoAKRjX_YsfZTxWQSue_JTKuiJEog8i8DugNhxcKMvlsWCLKsUhllHyHYy_jnA9qO7Ny_FCENG8LoajSloUdrYaDOhMtg45xVz9ZlsFZodtCP42OBuBgx7GyzuxYWQPIPd4Q8zi-V7dVj4kWzUTR-AFXAjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرد الإيراني على العدوان الأمريكي مستمر</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78337" target="_blank">📅 06:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbeuEtjyaPkhLSpLAMsdmGSktg9avMLfttFS4QnMktxDBjeJqForoQwLPF3P9laU49H0fOdYJ28zonHQY70y9JUDWvMuLtdurnZk9wPTk_OS_nmTkOpU5WS_FEQOCVqf3M67lvtacLgVW3x6pgN3ZCRBwtZWsAOPqEC5Dfl8kvnJcGLBcSmWZLqacikg4Cbc3oB439hbmi0VwJvug5iN6MSsCOhjo-k1op8y6ohCQs29Cb6b-kSQBr7P8y_NAfwp_THMP7DHv64342ZcVCLpDZwZBnDoKUE_T-qQPIsoSZ8yGj824csRyi9rhW7Jzw1xj4dGTriAJdPjjt3Dk7b5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر   موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/78336" target="_blank">📅 06:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله أكبر
موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/78335" target="_blank">📅 06:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اغلاق المجال الجوي الكويتي كليا بدأ من الان الى اشعار اخر.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/78334" target="_blank">📅 06:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">bye bye  everyone...</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78332" target="_blank">📅 06:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f40c8d945.mp4?token=rm3W3e6vkY88AXLUbV_7edjE6LoKd9mwWxJtegx1S94ieZVsodom-tPG5CZnwH7ZovHYaNfY_DoXi_tcReuZuu4b8K6NIirS8T19X2PQNmnFHZddsKCYURz9uMyEhv5Zfzn09-4ZzIizTCwNTk_xEitWI4D256xf-L_VIsTibEYPdQ_h7-1cYhvefwWFc58yNqFdY3ibweSNjomuScUds7wgB4UW1atSKxjv0tChE2kzZjDCo1nt7T2Wahxi8Nw5S2mmdolLXlj8iLIWHYdhCZy24geqpdqwJ4cVdO8s1FTuc5noBhG8qvu61iqtAHkQUIJC9DntGfpQJ8380ld4gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f40c8d945.mp4?token=rm3W3e6vkY88AXLUbV_7edjE6LoKd9mwWxJtegx1S94ieZVsodom-tPG5CZnwH7ZovHYaNfY_DoXi_tcReuZuu4b8K6NIirS8T19X2PQNmnFHZddsKCYURz9uMyEhv5Zfzn09-4ZzIizTCwNTk_xEitWI4D256xf-L_VIsTibEYPdQ_h7-1cYhvefwWFc58yNqFdY3ibweSNjomuScUds7wgB4UW1atSKxjv0tChE2kzZjDCo1nt7T2Wahxi8Nw5S2mmdolLXlj8iLIWHYdhCZy24geqpdqwJ4cVdO8s1FTuc5noBhG8qvu61iqtAHkQUIJC9DntGfpQJ8380ld4gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من المنامة اعمدة الدخان ترتفع من مقر اسطول الخامس</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78330" target="_blank">📅 06:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0684c909a5.mp4?token=oAhd0oLOVfEh9qWUOfkpgxiNMqqPrA2PmeOmpU--EA01uUOw7mu95r76Y1Sv41a-eel4upPSpOL11xyeapXnYg1wPXB7I7eZd3hJOl60yhrcwc-b8zj9oy6cOOmrGJm6np-cABkcmjKHXiTwqQDWIOW-d7wPJ2s3XBZjyp3Kpp95_3afVuMRrubYJ7cMkZZ0ZNEucERvD1WqFNWODBRZnD7121fhPAIgL0nAeuabRN1Omb_lynAaV6YRMUWap1gYuPDc1NOHiCtfGzC76s84aGXjX3XbFhR6nFANOMvE5rYVqbtEFQ4gzSyFDEE5E7BSBnSZIyCqNNUFAh_cayai34w6QVdHhG0Lo1H_MKSOJiMqZoZXg5zZJgydMA3MFx_b5F4KSrBd1ocvXbP1ZEY1okTrRpLA7RbJHW1gNk0WbkqYVe7SWT1fuNUJosFY2X3bYVltwhqg_eBhSaU4XCRt4sQgKBhj6asz4YV3MBm0WiPiTWGvDf-Su3XP4Tfoeq1wwACk7tMRqQzy0l7A5Bk5K0xtwAnp4WUA5dkeBWn3z2WyH42vKZLQun4pjvot7n6ngDWIIy6ULGLWMdPQbRFlI5o8BWgNHCrnX0F_uQP8bgXPlA_eN0eQoXnSZ4HCFkNeoM0i3CqoLFq-JzYZvBLQSEgR10TsuXDD40Mi0s_Liy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0684c909a5.mp4?token=oAhd0oLOVfEh9qWUOfkpgxiNMqqPrA2PmeOmpU--EA01uUOw7mu95r76Y1Sv41a-eel4upPSpOL11xyeapXnYg1wPXB7I7eZd3hJOl60yhrcwc-b8zj9oy6cOOmrGJm6np-cABkcmjKHXiTwqQDWIOW-d7wPJ2s3XBZjyp3Kpp95_3afVuMRrubYJ7cMkZZ0ZNEucERvD1WqFNWODBRZnD7121fhPAIgL0nAeuabRN1Omb_lynAaV6YRMUWap1gYuPDc1NOHiCtfGzC76s84aGXjX3XbFhR6nFANOMvE5rYVqbtEFQ4gzSyFDEE5E7BSBnSZIyCqNNUFAh_cayai34w6QVdHhG0Lo1H_MKSOJiMqZoZXg5zZJgydMA3MFx_b5F4KSrBd1ocvXbP1ZEY1okTrRpLA7RbJHW1gNk0WbkqYVe7SWT1fuNUJosFY2X3bYVltwhqg_eBhSaU4XCRt4sQgKBhj6asz4YV3MBm0WiPiTWGvDf-Su3XP4Tfoeq1wwACk7tMRqQzy0l7A5Bk5K0xtwAnp4WUA5dkeBWn3z2WyH42vKZLQun4pjvot7n6ngDWIIy6ULGLWMdPQbRFlI5o8BWgNHCrnX0F_uQP8bgXPlA_eN0eQoXnSZ4HCFkNeoM0i3CqoLFq-JzYZvBLQSEgR10TsuXDD40Mi0s_Liy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78329" target="_blank">📅 06:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رشقة صاروخية من لبنان نحو الشمال المحتل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78327" target="_blank">📅 06:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOaLYcC0TRK4Qasls_rzh1nr4VYpGylbPOyhzxsQ0uFZEDPYYKjfbiJxOp_lUBXtnaXPAZyunFaBJ_XnYifwfDpqy-lQpmafkaDw4J8FPihpcWtsP6VTUdpXrGU_QURxxOFpbE87gMozQnrEh4NsBsIc_rBPUwFP50MgWR6O4frcu6USpJZIrpizl1bvukdiCFhZzQxh1AbXfMJ2r-pL-O3OxREBS1WzbmCQoDbmmn1499pfv2rhETMAm5_-MFRLXD2tAShrVjCrZpVjI-jkn5Ao6dubspGSEPwxXRzufvkQwZZa9xLKjp5Lr1PyV92vvc_2ZQHXDZWCWTkLUGBXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد في المنامة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78326" target="_blank">📅 06:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01d0bb352.mp4?token=Q4azfk1aVBRO5SyvUgwC4FNyAmZ2KyKVXYa64C0wstpF__N2wbXcYuWBj4m-WVJMchh3-H5DQB_M0aY79dNG43KRP2g9-Su_yj4ceKFHm2uRY2i-tN8vQOt5JfxDiokfDlfN6j3qI4wpuUzDp0w-JlZ-_5-Xc5ofSguQ2fIj8x3Jz62ACykd8DiKBp7xfxTHoyA8e0e2QEx4qq9zzqVm5U0c-x8Go63l_IrrPgn0b2-uddvp8QUgmYpSLMUgXvyru_0pRlN6uNIf4Iu3YGKwXurT-hdN30DaY97JCZ47Ifk5Qc1bM8MsFKyqNmrpY_zd3Qnfo01SuY8qPnL7GcnPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01d0bb352.mp4?token=Q4azfk1aVBRO5SyvUgwC4FNyAmZ2KyKVXYa64C0wstpF__N2wbXcYuWBj4m-WVJMchh3-H5DQB_M0aY79dNG43KRP2g9-Su_yj4ceKFHm2uRY2i-tN8vQOt5JfxDiokfDlfN6j3qI4wpuUzDp0w-JlZ-_5-Xc5ofSguQ2fIj8x3Jz62ACykd8DiKBp7xfxTHoyA8e0e2QEx4qq9zzqVm5U0c-x8Go63l_IrrPgn0b2-uddvp8QUgmYpSLMUgXvyru_0pRlN6uNIf4Iu3YGKwXurT-hdN30DaY97JCZ47Ifk5Qc1bM8MsFKyqNmrpY_zd3Qnfo01SuY8qPnL7GcnPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فرزندان سلمان فارسی پایگاه‌های آمریکا در غرب آسیا را با موشک‌های خود شخم خواهند زد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78325" target="_blank">📅 06:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بحرين تدك مجددا بالصواريخ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78324" target="_blank">📅 06:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78323" target="_blank">📅 05:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/78322" target="_blank">📅 05:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/78321" target="_blank">📅 05:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/78320" target="_blank">📅 05:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
فرزندان سلمان فارسی پایگاه‌های آمریکا در غرب آسیا را با موشک‌های خود شخم خواهند زد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/78319" target="_blank">📅 05:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بزن که خوب میزنی</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/78318" target="_blank">📅 05:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">إطلاق موجة صاروخية جديدة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78317" target="_blank">📅 05:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله أكبر
الهجوم الصاروخي الإيراني مستمر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/78316" target="_blank">📅 05:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">this is only the beginning...</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/78315" target="_blank">📅 05:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بحرين تدك بالصواريخ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78314" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/78313" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c8317158.mp4?token=qjfywqIvglFB69nP3DqxBP4nOeX9yYHqlE_zGurWdRphVpG9oot15UtOz0fxqMZKGpk4Hypn8Q6iUfZrcaJ6zlAbWabZo2Hs_LBMVVR5WZOo9EcumL2YBw8ej_Pm0MSHAYkp2U8KfrZEl86sAFCTN8BzI-q1e9mVbkI-aDbY9R-ez2yWJGoUiB9k-KXfbiiEudy4l-7cQsmoA0rwQJsN_N4Vyy7I20JE87La1b8hGdAJXLgs4IPwx6ZaPjsuuHz5ZSN6qjZqt7pKBdaSpfnDFXk__arLy9iiwVjezmxbUcRWcMr6EK2kGi4LLgNsdeACdYEIiYBIMcAFQ8SPCqaZUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c8317158.mp4?token=qjfywqIvglFB69nP3DqxBP4nOeX9yYHqlE_zGurWdRphVpG9oot15UtOz0fxqMZKGpk4Hypn8Q6iUfZrcaJ6zlAbWabZo2Hs_LBMVVR5WZOo9EcumL2YBw8ej_Pm0MSHAYkp2U8KfrZEl86sAFCTN8BzI-q1e9mVbkI-aDbY9R-ez2yWJGoUiB9k-KXfbiiEudy4l-7cQsmoA0rwQJsN_N4Vyy7I20JE87La1b8hGdAJXLgs4IPwx6ZaPjsuuHz5ZSN6qjZqt7pKBdaSpfnDFXk__arLy9iiwVjezmxbUcRWcMr6EK2kGi4LLgNsdeACdYEIiYBIMcAFQ8SPCqaZUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوحة فنية من صواريخ إيران في سماء الاردن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/78312" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78311" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78310" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fd2a0c7a3.mp4?token=bgHbNk7fNoJbdGXNMqTveIWqEud7r92EhLt-k3bcZhiKUSV2LHVV4ckw66g21DMjX8iPVRBMLAa4iS8IXCRLxGt0KejX1zDpXPwqKVrA882m9TnekPCmIS6GONWflT3kFow5HznKRmDZVldJJ1x45KHmkP7QCubkvHzw1GVOtsdVh7oNOhUwy-uuIc6ctwmFitgvnJDHxhzYa_v4bUtE8kK8yHW01IJUIGlocB-vrd1AqHFxyGYV0r_ynOzcWVOcCIl2dU_yfArJcbMzV8jkNGGZW2dZPFB8kEO4lPjhB5LLQiTpr2Xf0JlkVDPv1JVK6RqxROo81cmKY78uP8nuG1LUOuU95SLHhzM1Lr_jyBeDlqylApIrrSyQgnIdPCL90Gw6dr_PFTNYP7CZFqtTZP9hm6Nj7lIb9GNmXe9iMAufmJrBLHiEnJDY7NtetUEb-6_WJsY93-CfhXwje631ICF35hKIegt8JuP8nFt0TjF_aTXYeTOV6ufuC6Ad0NLbMXYPCPLEd035K3EyU4hyOxsBAkvm_NYkDvSUhlr5ciciPc-wYFPm-X-45C3B-gmN77sJ8jOQ-r9siytYA2K7rCyJtWozZQAd8NATbw7-o9mZcH2cmVvlv7-wtizfOLsnJ-v2a9TiXi0r2rlrzzfEfcXRpfR7l8-IzhZjlTFMKe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fd2a0c7a3.mp4?token=bgHbNk7fNoJbdGXNMqTveIWqEud7r92EhLt-k3bcZhiKUSV2LHVV4ckw66g21DMjX8iPVRBMLAa4iS8IXCRLxGt0KejX1zDpXPwqKVrA882m9TnekPCmIS6GONWflT3kFow5HznKRmDZVldJJ1x45KHmkP7QCubkvHzw1GVOtsdVh7oNOhUwy-uuIc6ctwmFitgvnJDHxhzYa_v4bUtE8kK8yHW01IJUIGlocB-vrd1AqHFxyGYV0r_ynOzcWVOcCIl2dU_yfArJcbMzV8jkNGGZW2dZPFB8kEO4lPjhB5LLQiTpr2Xf0JlkVDPv1JVK6RqxROo81cmKY78uP8nuG1LUOuU95SLHhzM1Lr_jyBeDlqylApIrrSyQgnIdPCL90Gw6dr_PFTNYP7CZFqtTZP9hm6Nj7lIb9GNmXe9iMAufmJrBLHiEnJDY7NtetUEb-6_WJsY93-CfhXwje631ICF35hKIegt8JuP8nFt0TjF_aTXYeTOV6ufuC6Ad0NLbMXYPCPLEd035K3EyU4hyOxsBAkvm_NYkDvSUhlr5ciciPc-wYFPm-X-45C3B-gmN77sJ8jOQ-r9siytYA2K7rCyJtWozZQAd8NATbw7-o9mZcH2cmVvlv7-wtizfOLsnJ-v2a9TiXi0r2rlrzzfEfcXRpfR7l8-IzhZjlTFMKe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق موجة صاروخية جديدة نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/78309" target="_blank">📅 05:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpY79GiP133hnWHTHZl-Va7tjOjNyuuX_AxoUQOV48aMUf9LL9oVTg8rAMW5sVlIiCFK4Dkwkrq-DqUw8lqwhOYvOwdPMDssQbd0oyW7yYNZ5GWNS6h8UKNu75UG5AlPnET5J8gT_Q80RZb3VdIkh0pE8bd3hzV2CzVWtCWShOYFt7LDpI2SuucXP_9gYVR6oamEmoabNOP7hr6PiI94MmWb2YPoisj8PaRo36OUpnL0v19Tw2j4I-KqY_IAIfuGRIR9wT0TJA_H9nDbfEn9v8DOCkGdXFcZQJiyIHWpSlYpk_qufQpmrrWanVma9vvvf3NMV3lJsdjMNVotaaAKh6qv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpY79GiP133hnWHTHZl-Va7tjOjNyuuX_AxoUQOV48aMUf9LL9oVTg8rAMW5sVlIiCFK4Dkwkrq-DqUw8lqwhOYvOwdPMDssQbd0oyW7yYNZ5GWNS6h8UKNu75UG5AlPnET5J8gT_Q80RZb3VdIkh0pE8bd3hzV2CzVWtCWShOYFt7LDpI2SuucXP_9gYVR6oamEmoabNOP7hr6PiI94MmWb2YPoisj8PaRo36OUpnL0v19Tw2j4I-KqY_IAIfuGRIR9wT0TJA_H9nDbfEn9v8DOCkGdXFcZQJiyIHWpSlYpk_qufQpmrrWanVma9vvvf3NMV3lJsdjMNVotaaAKh6qv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تدك قاعدة موفق السلطي في الاردن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78308" target="_blank">📅 05:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1fd3d135.mp4?token=WOnAp53ou2_LJkHwyXX4C87jw-fgAr1rG02zc9ctIp1frfJi1PgOrbqJM1Pe4-oLJKdC9fomFz_zu-I2Je66FkXLmUp4j8furl_r8Q5lLGZHu_s8Zsski1VJ2uTU4isW0b3u1D1-SVPe1jr-VHT4KBAkS_-RQsaHB1wc2LRQl4lb2MkDVXMKNiJ3qjHt0A82tWxHSQKDRkQ9HXrLqUtt1XILqt9uGZ9I34nEz_tZI42PkyK5gibl-KrLYvY5kxpckEgQhuA59frqlD50aTnCNiTuE7R_EEhPEA99CYC54egp4uNKiS77KewTXH3TAAgtg0BZVRo1JVvLTQxcNxHwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1fd3d135.mp4?token=WOnAp53ou2_LJkHwyXX4C87jw-fgAr1rG02zc9ctIp1frfJi1PgOrbqJM1Pe4-oLJKdC9fomFz_zu-I2Je66FkXLmUp4j8furl_r8Q5lLGZHu_s8Zsski1VJ2uTU4isW0b3u1D1-SVPe1jr-VHT4KBAkS_-RQsaHB1wc2LRQl4lb2MkDVXMKNiJ3qjHt0A82tWxHSQKDRkQ9HXrLqUtt1XILqt9uGZ9I34nEz_tZI42PkyK5gibl-KrLYvY5kxpckEgQhuA59frqlD50aTnCNiTuE7R_EEhPEA99CYC54egp4uNKiS77KewTXH3TAAgtg0BZVRo1JVvLTQxcNxHwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة جدا هزت القاعدة الامريكية في الاردن وسط فشل المنظومات الدفاعية بصد الصواريخ والمسيرات</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78307" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الاعلام العبري:
يبدو انها عمليات اعتراض فوق مستوطنة كاتزرين بالجولان.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/78306" target="_blank">📅 05:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD0u7uAeuzZB9DCL0RohCGz2T6kPFChcT_5wli6cxvYDb33IukueL9UfVKGpPzeZjc_LGlmaILLW8TpS8AHxA3Pv5EFGgF_0bppYUDVG7e6tdZhlcK6QXwkDQxoHzK6AO63yfc8OOxAph9y75FAKs2pTiwUfM8ZnuSZkpr9MyL1mvrKnO87SOcrJVbBpMhIndR6RBPkk5UpalziOWnq3xtKroL0PHV4avHPl75eXbiOUsB0c--12aofDzGl6JH_fKw80MSoW7xdxgN0P6cG9Ro6QO54gJkjtirF6QxNae1oiGKzIBeqm1nSVgsPVbkQtQSEg2iBjkWAR3dw8JucsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvseC2wX2zmiGHCEOpwfQ0wjvQ903Z9F-VPEt8IEPMddanz9c6PjcTVk5fZj_BCM5UeFLvsP2QxA3H_8PmS6mEs38pVnHyQ653Dm-TxHpgUA_mJu7FGtmCSa7YtGdKiMZec0oKD-FNPWxsEn_RzHnk49SDSXvi6-54NGsLLwmbITF0QboyGgGEY5V0BhJw2c63QADBpwOqFV0P4vXDyTgozvF0XdfiGq-FxW2QIfiRBqeBMD2Wuso61YpeCk4sLLgCARSltpWojrQW1G2qon8Nyh0-Rdq4K9ohLnRM3cKWTLYYZvWqGWFFTf0UKii5u-5jQUQocy9ODxhWcNB_DF2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من ايران الإسلامية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78304" target="_blank">📅 05:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59423f289f.mp4?token=aIdxDE16eBZsD9UzIwepUqWH1I9JJFEpKRikeEaFwZP1lSRA1zjRnwvthMkv6eATOLnhVcopLlVrQ359YzcgpyGj1fGHtN6aLeu5_xVIdg9CDOOLZ0OzvXTpvYiHYSbPnRr5-3_kXkd26Up29bt6NYqWPdgvY13HmwAP0tg2tcxaSokrKMB-djkDvyYXduMFlUlxUlfDNIp23tITCVtIBVGg8wuK9kmS3YWXZXDE6_MeejBRcPIJwFfe_Ma498yI7fpr4NnhsaC_baPqq_ZJCqxX_T0hHgy3YVsicPJBAtxd3YD24mJgynu6MuWnWbxWjGED-JqCMUlPMbZ54s_B4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59423f289f.mp4?token=aIdxDE16eBZsD9UzIwepUqWH1I9JJFEpKRikeEaFwZP1lSRA1zjRnwvthMkv6eATOLnhVcopLlVrQ359YzcgpyGj1fGHtN6aLeu5_xVIdg9CDOOLZ0OzvXTpvYiHYSbPnRr5-3_kXkd26Up29bt6NYqWPdgvY13HmwAP0tg2tcxaSokrKMB-djkDvyYXduMFlUlxUlfDNIp23tITCVtIBVGg8wuK9kmS3YWXZXDE6_MeejBRcPIJwFfe_Ma498yI7fpr4NnhsaC_baPqq_ZJCqxX_T0hHgy3YVsicPJBAtxd3YD24mJgynu6MuWnWbxWjGED-JqCMUlPMbZ54s_B4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مرور الصواريخ الايرانية نحو القواعد الامريكية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78302" target="_blank">📅 05:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6cb1d450.mp4?token=Mq9tu0zT35bOn0GYBRGZfQigVJUSNX0Wi5s4jqoQRVuC6Ph8R1uWmjPUWl7gJ9yTZtY2eq0fgeHlbjqPHgv3hXNwA_M_-gyjw-r_jESzZ3-Jk6tctObh-lV42TcKWtf5J5557aPJSyuvOOMGdZ9JjcfNyQiKXyVfdZsYCruWE_153wo4xdyBWMCYfNTmSmbq1a-JFC-agApMYarjxghY9NBfWRVh6EKpbsSBjVt4GnVVYUbLdjrFDtky0xC4h-snNJ3jw-REQvE7p7Vbh9HHzD7yay5E3gPLA9-8Eu4bvWlJXu4mRYn0kKvi__3AKSbGLVpnDxXJkFKvesOzSEB1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6cb1d450.mp4?token=Mq9tu0zT35bOn0GYBRGZfQigVJUSNX0Wi5s4jqoQRVuC6Ph8R1uWmjPUWl7gJ9yTZtY2eq0fgeHlbjqPHgv3hXNwA_M_-gyjw-r_jESzZ3-Jk6tctObh-lV42TcKWtf5J5557aPJSyuvOOMGdZ9JjcfNyQiKXyVfdZsYCruWE_153wo4xdyBWMCYfNTmSmbq1a-JFC-agApMYarjxghY9NBfWRVh6EKpbsSBjVt4GnVVYUbLdjrFDtky0xC4h-snNJ3jw-REQvE7p7Vbh9HHzD7yay5E3gPLA9-8Eu4bvWlJXu4mRYn0kKvi__3AKSbGLVpnDxXJkFKvesOzSEB1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لمنظومة الباتريوت الامريكية في سماء عَمان الاردنية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78301" target="_blank">📅 05:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccdd98686.mp4?token=RGvhtbuYsxjRPvWZZT5q0-5wI3uLgywwnbvEacB5BmT6ENuq8r7pCOO-iqf2ofKDvMmmlJrN2CjvWt0IkBqNBk2miFCdzNg8DPKKLDMKuPjS18_ypc_EfY7dtelSqtZh30WizQfZuH6lfahiUuQw7hEPIyNOwyPNGqs3XXzq_NeR50OzeHwIcmQAiCoZiApbX-29Qq8HPXelsXzN7-aRBqQ6mCYk3NcVcxodAnG3AqAKjsDMx2ta8VrHNF0HyuyDMyDIY-oYAsjrvddbWwii7eR_edyT8XOCC1O5kz0aEmPHvGsWuxQNKlOJddGxvjtCfEYbU_4o2v8JyRDRjbmGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccdd98686.mp4?token=RGvhtbuYsxjRPvWZZT5q0-5wI3uLgywwnbvEacB5BmT6ENuq8r7pCOO-iqf2ofKDvMmmlJrN2CjvWt0IkBqNBk2miFCdzNg8DPKKLDMKuPjS18_ypc_EfY7dtelSqtZh30WizQfZuH6lfahiUuQw7hEPIyNOwyPNGqs3XXzq_NeR50OzeHwIcmQAiCoZiApbX-29Qq8HPXelsXzN7-aRBqQ6mCYk3NcVcxodAnG3AqAKjsDMx2ta8VrHNF0HyuyDMyDIY-oYAsjrvddbWwii7eR_edyT8XOCC1O5kz0aEmPHvGsWuxQNKlOJddGxvjtCfEYbU_4o2v8JyRDRjbmGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مرور الصواريخ الايرانية نحو القواعد الامريكية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78300" target="_blank">📅 05:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f6116ba5.mp4?token=XiD26idJlW95SLPNvDYDrJLXWf5Sb1Qudkm_j18MY9c0BEKErltGdSs9RIFjUMI8x_Kv-JngvUmb-HP2BYYZLUVDJTFlWo0hC3HkskitQOlfQBCAADDflZDjcDxRay0sfX91V7uSrHKPuQ2whngelA-KIPEiSuADqplc25KQG91PAXfPyWfRbTI7iTRqRzaq-6wTyLhcANbBH53Vf2BGrYgT_m9wh_oROnL5dlDybk8xPWnAjYQOc1qZov1j18k5SzMHIJ0xlsQlAEz5TN5DFGBFA5YJuIWnQgiIMc5m6iV8cAXtZtWiq6fwMRrMI7WoG7s6HmcL6orqj_JgPFQ-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f6116ba5.mp4?token=XiD26idJlW95SLPNvDYDrJLXWf5Sb1Qudkm_j18MY9c0BEKErltGdSs9RIFjUMI8x_Kv-JngvUmb-HP2BYYZLUVDJTFlWo0hC3HkskitQOlfQBCAADDflZDjcDxRay0sfX91V7uSrHKPuQ2whngelA-KIPEiSuADqplc25KQG91PAXfPyWfRbTI7iTRqRzaq-6wTyLhcANbBH53Vf2BGrYgT_m9wh_oROnL5dlDybk8xPWnAjYQOc1qZov1j18k5SzMHIJ0xlsQlAEz5TN5DFGBFA5YJuIWnQgiIMc5m6iV8cAXtZtWiq6fwMRrMI7WoG7s6HmcL6orqj_JgPFQ-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية كبيرة تدك القاعدة الجوية الامريكية في الاردن</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/78299" target="_blank">📅 05:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOizmNCk_pdYZNC4mjzShIZC8_fw-g4usbwZr_m73zR1bf295wEed_SsUIW9Cop52JGZZqp17pZ_z55QRF_mMY8Ji410I3k16TUv6fU2XAb3d1gK8mZ6-mgoPuCDoYd45YqTcGWSxXQ_M0VKT8IdgvUh5EuDaB6Smm3uTirKDplsVBodoePKuvSc2uEDPS8Zm9iCbJVL_Dhvt-hrxPMHtHhlOcBp3KiH2bS1woeXrX9ZvXCoqESjtzMBkWohPmMCAJv-LXD-MEIaZ03kGH6391fuBkV_A7_OiPhryuF7guD2t2AInIGAcRNYxf0BnjQYY_hOdcqv3ISB448rgppJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الهجوم الصاروخي على قاعدة موفق السلطي الأمريكية في الاردن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78298" target="_blank">📅 05:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDKmA40iYKhiuFeatiSg2hmV_zi9yLQJznnpK6N0DlOEooOv7yDNgiyzSwtgteXGZBSC5Nxf3jZC5btqo6jKeBd80W6G8r1PI7KiqLN8h3BTWppbIBE7qynxbM_IVoCojBieygl7-99QlCJPf011aVxQ3mTtnQkFeeOqbhKOYe3utkdg5-eva0cEKgEr9oCW4vwY-qivr-xTqKAome__1hLyG41kLX02lwPFHn7gh-9oR4lN7-rV7JrXl0XkS0tS6EFAzzyOmrD983QMJJoKxJXoEvWgLmtY0Vlxo4MVFolvUMddPtJuD4hnk1X56ayuOCOSk4g0P2PN54wynavI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القاعدة الامريكية في الاردن تحت مرمى الصواريخ الايراتية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78296" target="_blank">📅 05:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579233c7b5.mp4?token=Gcln0Qkhfj970z81I1josLqCtm0irTAif5rvahyqqeG7kB32YisH4zwb_mLV9jo58fAvm_bHNqDeifAp1EABgFN4Cl_cIxE5_zs91E-TfMcQLGSlcSuyiCQuTvhABwbB2KKnzVuZlNwjujW-NBMoh6Wq8uAwMZo3YgjrUe0umVKMircQ23Evu9UPIqWO7r3w16XOSCJ4xlr5aB_XhbIj_90tg_Ji57-9PwLwQBHwn9pQtBczSgzSJkIGz-gAxizmaaywVVWlg3ki6_ebzvz0otUI1pUQqOJZqWTj25OOKK8eA9a1m8ay9uRyq9WBdAPDPQv9YZAh6sYlgH3M5RyxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579233c7b5.mp4?token=Gcln0Qkhfj970z81I1josLqCtm0irTAif5rvahyqqeG7kB32YisH4zwb_mLV9jo58fAvm_bHNqDeifAp1EABgFN4Cl_cIxE5_zs91E-TfMcQLGSlcSuyiCQuTvhABwbB2KKnzVuZlNwjujW-NBMoh6Wq8uAwMZo3YgjrUe0umVKMircQ23Evu9UPIqWO7r3w16XOSCJ4xlr5aB_XhbIj_90tg_Ji57-9PwLwQBHwn9pQtBczSgzSJkIGz-gAxizmaaywVVWlg3ki6_ebzvz0otUI1pUQqOJZqWTj25OOKK8eA9a1m8ay9uRyq9WBdAPDPQv9YZAh6sYlgH3M5RyxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية تشعل سماء الاردن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78295" target="_blank">📅 05:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0950be8894.mp4?token=vEjKb_-gemtXLpAURIICIEYbJzOhcpSYJQyAKbcHZZ_EKet5nH-1QZkP_fBbrn_Fj_z8tPvUDcJRGFBQ2l3kJX88XoEeiqchkl-ufyChRQCX9AV_qQqKFMT7HtWwdXgrOMFWAWVB2n9VNWSy6BpFQAIzr1GPjzgqK9BJws2jafdx3iMq2WKgiLiIKl1cDYPaQ_bGo_Me1uJPtOqSQ4ixY_NfyrCFgskjWj2qPjuivmEEaMpPPjDaNNNU5ZRGfKex98P9zfbkJHRXLfWITUoV8jWfrEApYGaaHVAV0u3WZjZ1WwHKbvM-4WGKNdNT3cTPBm-6j_SgscbSeuMMvh-XyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0950be8894.mp4?token=vEjKb_-gemtXLpAURIICIEYbJzOhcpSYJQyAKbcHZZ_EKet5nH-1QZkP_fBbrn_Fj_z8tPvUDcJRGFBQ2l3kJX88XoEeiqchkl-ufyChRQCX9AV_qQqKFMT7HtWwdXgrOMFWAWVB2n9VNWSy6BpFQAIzr1GPjzgqK9BJws2jafdx3iMq2WKgiLiIKl1cDYPaQ_bGo_Me1uJPtOqSQ4ixY_NfyrCFgskjWj2qPjuivmEEaMpPPjDaNNNU5ZRGfKex98P9zfbkJHRXLfWITUoV8jWfrEApYGaaHVAV0u3WZjZ1WwHKbvM-4WGKNdNT3cTPBm-6j_SgscbSeuMMvh-XyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القاعدة الامريكية في الاردن تحت مرمى الصواريخ الايراتية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/78294" target="_blank">📅 05:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5062295b.mp4?token=rOS2ISCbWNtq8EE9ELTAfCD4-Li_PVTF93fMp3kU4qP112mOeCwxNl7Cu74xdur8ENoRNR87xbs1loNnaTBpHL-XsMOCjGAq2sz1CyHaLxS9bdOa9nIf5LXZSnuPN78tLldmLw5BUxxHCkPmD73KMi52VeLyjGRrjyaIY4RNeyJEnj46ZRYdhO0uThXpr2P_Ygko57FQ9gSzfJjT1bfOdokb-E8LgqnxKxgU9iUIB0oRB-Br1Dyr8svXSiygCrQyCb4-ByrgjbHKNqicvQa5kzl_e1OgmP02DtDhncxs1UCs1Cylys7aE-xXfs0oeLDM6-f2ibyzyyzi59UGoHJlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5062295b.mp4?token=rOS2ISCbWNtq8EE9ELTAfCD4-Li_PVTF93fMp3kU4qP112mOeCwxNl7Cu74xdur8ENoRNR87xbs1loNnaTBpHL-XsMOCjGAq2sz1CyHaLxS9bdOa9nIf5LXZSnuPN78tLldmLw5BUxxHCkPmD73KMi52VeLyjGRrjyaIY4RNeyJEnj46ZRYdhO0uThXpr2P_Ygko57FQ9gSzfJjT1bfOdokb-E8LgqnxKxgU9iUIB0oRB-Br1Dyr8svXSiygCrQyCb4-ByrgjbHKNqicvQa5kzl_e1OgmP02DtDhncxs1UCs1Cylys7aE-xXfs0oeLDM6-f2ibyzyyzi59UGoHJlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القاعدة الامريكية في الاردن تحت مرمى الصواريخ الايراتية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78293" target="_blank">📅 05:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78292" target="_blank">📅 05:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tISJ4o3seHTTM13JRJw6OMoS0MCWwjBj9sl0ustzfiGx93nqMSwkK2yQEITrWSm0He1SHQQYh_KIlAn6A1f5FS-YsxSa2B3816OeC5eU1OaE_saOhGbQIid1kPozCZWPIz1O6S8Cnp5z4WJ5CMpWYLxpiW1XPFN6jiVGaiRPU7IISFTk5M549nHJ9yTfRZTL7ZQNGgpfkfp3YlvugkxudI5kiGvL2k6Rlj0HX9lG02sW3KmHtErjFnEJgNKuzUxor9hN1TAKU6BJXfw9hmEjUFv0etVo5H_x6BV2VFk9iGe2owViIn6FahLv7LKTExrUn-SJUo4GF_R1PyDJjdXZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اضافية من عشرات الصواريخ وهي تنطلق تجاه القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78291" target="_blank">📅 05:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92669279f.mp4?token=B25lgChvOOhTvMoTIy5eCFjgA1nrrM6igYR0OQMIvNQjlQjmDDAGcWfPleQTLEzNyWTKRHrpj632rmAC2f60mctTNgaCyxcMy9bS8ekxDEyHLOS0mQ4GT-mCYDT8DYclRJ_Jx0rYJceyq5lc8h8Lqz0rZZ1VrFncYCkZPIZgjBt5y38kNFRg8ofPSoRG5XY7txC_0lVZshH7USH9AEeIZ3wF5HGkA2E8Su-jBMercaYkAxwJuN0kzcZZ0Bkjkcyccsm7cImFgB_3NknOK4uWrt5ATXtl-fecFQ-aiOqL_mMVmDV52Z6yz_goy0EaznUl7baS4UcRnD5T534AvkWZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92669279f.mp4?token=B25lgChvOOhTvMoTIy5eCFjgA1nrrM6igYR0OQMIvNQjlQjmDDAGcWfPleQTLEzNyWTKRHrpj632rmAC2f60mctTNgaCyxcMy9bS8ekxDEyHLOS0mQ4GT-mCYDT8DYclRJ_Jx0rYJceyq5lc8h8Lqz0rZZ1VrFncYCkZPIZgjBt5y38kNFRg8ofPSoRG5XY7txC_0lVZshH7USH9AEeIZ3wF5HGkA2E8Su-jBMercaYkAxwJuN0kzcZZ0Bkjkcyccsm7cImFgB_3NknOK4uWrt5ATXtl-fecFQ-aiOqL_mMVmDV52Z6yz_goy0EaznUl7baS4UcRnD5T534AvkWZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ البالستية تنطلق نحو الاهداف المعادية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78290" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6fd00819.mp4?token=jsqJo4wRegG4cwGN5aXMWtFTyC2Yq_A7rHQsC4ltQVlzaDHsKwxUy35pgF76ZCIyqhLRU1zU6fVEKPWx-QDjIFVO96TnPkmMcodad-ALxLKSNa_UCH2YTfn2oRRTlmIajt0bFmAKNGKHGzKkQG6757j_wfQHJQEw1qi-nr8H5569jclbnrsEbH6G-SN6UTf7YdD75ISDIFsjJf6oiw9sXbxGNmyfKqfKVErI06yPmz8G2TU7AXFw24_ygGH3N2zzt2bcmrg1GJcrsdo1JpfOUWqmJ8DGRcm7d6AgPf4mOfrNq85ru_xPw5L0r4Z7WRwO6tJLZx3nPj1ssXnKE4Gczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6fd00819.mp4?token=jsqJo4wRegG4cwGN5aXMWtFTyC2Yq_A7rHQsC4ltQVlzaDHsKwxUy35pgF76ZCIyqhLRU1zU6fVEKPWx-QDjIFVO96TnPkmMcodad-ALxLKSNa_UCH2YTfn2oRRTlmIajt0bFmAKNGKHGzKkQG6757j_wfQHJQEw1qi-nr8H5569jclbnrsEbH6G-SN6UTf7YdD75ISDIFsjJf6oiw9sXbxGNmyfKqfKVErI06yPmz8G2TU7AXFw24_ygGH3N2zzt2bcmrg1GJcrsdo1JpfOUWqmJ8DGRcm7d6AgPf4mOfrNq85ru_xPw5L0r4Z7WRwO6tJLZx3nPj1ssXnKE4Gczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ البالستية تنطلق نحو الاهداف المعادية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/78289" target="_blank">📅 05:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2lf_uigjZ6DAQ6ZtoMP34xZc-GprY5AtZCioXzurmZGksMKaoxpI-s--6rAUghH8mSmw7aeZWtie2LzkkTsgruObL-Li7fXBYF_GWYchNrIYeC5y22_FvSc1Lxlkbpy5GlqHb-qBVfK6YzTRwF-rNEvgv6l3H6Ak4__UH1x255OpLcZXaP374NN3B8a9_W9gFBH3jCF5sIN7CGzGFEBILnXr9JRAznHqHCZL58EwTgDi5ge73IZ2wfQcoD7t5EkcRRGxYULd7P7-lshqVaxeIiP4UySzPaahVbr2i_u-HX4ZwQ0XpDOBBepk2h_ZOyyNmaiciS8f5dvrIQS5sZM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJz3UWvHT7Hfh36tZ-tC5LT6-I_8wU4vBzmpB0KF0LpOvZs4pyUFWgH-Q-04fXa0K-eGBy08KT083OzljvtZBDAxYi3s18on7vEYq01mlXa9PGWvrTr7tUw5nfNy-V1AwmcU9_74XvmoAXo_J7EwaHgeg-_qt6w0xpReAyyDx3a5xp5JZrHpWQ2NZjWUIcqpC3zWheBFP-1nZO27CwnMkxFhg5OPBwDg5_VXYKQadWFyXD5CiegYtIVefvgoN9uh150Xj8ahVD8t0AMh8WZI3tGJrEBEuvVT1LIRUNdL7SfmxFd7UAtYeztyFIG_cTbcmPx3-W5eR26N-NVOx0bqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kh4gGYpEYZS-VfTBsya9xtjbpRyrFqBQNHOCiG0vrPwv8Jomx4xn9A1s1a0pFht8FaWI880eTvs2qTJ71R58TwxvlXTO7o9wEtgLtJAcrvU49WZ7I-CpRR1K5z7cdassz-qKjIVinzYx6zN-kWyRu0KiQfFmaGXv1hPZQwwUWRAFDzMoA9W4-8Im50sKvPw-FU7oPQUAI4KfjgxBfD7k-60OmPcgUc1HFRROzKr0LFoeOBxJywtM4WrCOdxIXxVkqKfqPi9UFIXouo_KIZHlR7ygjRNTY5YuxFlAc2qrP0f8kvhfINDV0SD5DW8xFP5VkqqpmUeAWDYhZI6NP_PH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/78286" target="_blank">📅 05:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/78285" target="_blank">📅 05:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvIhbbI3fXxwSvy1qj4J97IHB-n26NaMmH5ENauo1Mb9hFK11rxNGUDivj7aDsq5Bt0Sq2JpVcyTpA8dnHIO3PGqW_iPJyb7nbTZQ9Xe25IZIM7qkFyqBdFWH4q1EDWbGnqR0qqK83K1Us421W1f_uDpaIrpJys7tJEG3EEXpfnr8mvq8kmTHr3r9gdRNHwvQ9X1om5v3eKOB2Y817ORGIbCdvGDbnz83R5Q6Q3ywdfUExjSCFvHJcDj66iDyv_aVh0-90n5vWlvs5XvyImUGt465JRlshnR6f_zWHvFw6VOt6NLcjGlhm8fgQkhxM7e2ws5JZ80c33tnvulHDPf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ من إيران نحو أهداف معادية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/78284" target="_blank">📅 05:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78283" target="_blank">📅 05:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-GayGr3Ro61RiQ71mCWVnfXNPPUZHt5imNokrwDbasxxd1G2OPzbWqr6iRybdVd_qIbD5F9ADIcLwv7F3PpkxBuLNjmKTJkSrHlwrWhupoXpVBgR1m1imy6WUCKtY45T5kp8CNBPZDcC6VJhJ6A0kr1A6a3dNtqHNUbNcRKyUmjuIQYjG8dQ82SCdZGIFTxCymFutuwNHFPPUm9rWkIgLkkBsSRVGYluZRQ2YaGJa0J08klXykRkN-jb3N0O5BhPpuY0wzB0q2Hpv6ID0P5No437uAa-_Do202lv_iyoQNwS5ZnpS4IgnRwlqqkz9M5QuBGPZW245zKPnE7AhOPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
: أطالب الجمهوريين في الكونغرس بالتمرير الفوري لمشروع قانون المصالحة العسكري المرتقب بقيمة 350 مليار دولار.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78282" target="_blank">📅 04:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوي انفجار في منطقة قرجك بالعاصمة طهران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/78281" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b316badf94.mp4?token=pftfRpim-GXBWrTC1GniZKID6Mw2AbhjCZb-SdFAwh2IhaCDmoXgldp6KQpvU5Hq5a3w8_GHXiQ4gL10Kd-vs70S1USxOHbcHZ7KCmsXpZ154rRw2GbKhXl3h5uQqcALvJWN0XXmOYyb-U2ExqIlIVNacaa-gZw4_Efv5j_1b9Y-pQemO6ivEpCjtpqL2mQdRL8iDjwgowcn-SFpvxmN-1Ve59t0NzPZXNtizUB3Uo4rIH0QEU1hH37GnEhonWZJc-TrhtRJX4oq4LRLFmvLJbdZMVo_GCWCWShlFDYLMoOY6Cx7TX0c4HBdL4e8WJp1t7d5fwPa2HJi4OnsXuOB6mhT9ypbw7sjsOq9WdPYpOMbu5fc6nUlfMSFxhh5TUvuFzWcTJ6NX4RBKnZ2umYZKBtS1EeXHGyoGwgtGsEeZABMGIOMoXNVoI7ju7H8lF3XbvkZ6x13gQXtacauETsGZM7hy-werXDApoq1RX7ZKOUvNWREa193e3Q5oWF0EE5ESJ6w9tU1fSFKDHWWcLC56BvpUBTNyL8p_gVXLKbdBFrs4gSPQyiklMukGvIpt1KLEu3OzfUbwfAqX6K6y24iAa7pyl3mZpDatxlwhAEKwmykgkDI9GkKF_WY_MPcpvRMIQixHVK9QR106qD-GJbXd1u2THmIgUHBbyhmsUb50p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b316badf94.mp4?token=pftfRpim-GXBWrTC1GniZKID6Mw2AbhjCZb-SdFAwh2IhaCDmoXgldp6KQpvU5Hq5a3w8_GHXiQ4gL10Kd-vs70S1USxOHbcHZ7KCmsXpZ154rRw2GbKhXl3h5uQqcALvJWN0XXmOYyb-U2ExqIlIVNacaa-gZw4_Efv5j_1b9Y-pQemO6ivEpCjtpqL2mQdRL8iDjwgowcn-SFpvxmN-1Ve59t0NzPZXNtizUB3Uo4rIH0QEU1hH37GnEhonWZJc-TrhtRJX4oq4LRLFmvLJbdZMVo_GCWCWShlFDYLMoOY6Cx7TX0c4HBdL4e8WJp1t7d5fwPa2HJi4OnsXuOB6mhT9ypbw7sjsOq9WdPYpOMbu5fc6nUlfMSFxhh5TUvuFzWcTJ6NX4RBKnZ2umYZKBtS1EeXHGyoGwgtGsEeZABMGIOMoXNVoI7ju7H8lF3XbvkZ6x13gQXtacauETsGZM7hy-werXDApoq1RX7ZKOUvNWREa193e3Q5oWF0EE5ESJ6w9tU1fSFKDHWWcLC56BvpUBTNyL8p_gVXLKbdBFrs4gSPQyiklMukGvIpt1KLEu3OzfUbwfAqX6K6y24iAa7pyl3mZpDatxlwhAEKwmykgkDI9GkKF_WY_MPcpvRMIQixHVK9QR106qD-GJbXd1u2THmIgUHBbyhmsUb50p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي: نفّذت قوات القيادة المركزية الأمريكية (سنتكوم) ضربات دفاعية إضافية ضد أهداف متعددة في إيران، في العاشر من يونيو/حزيران، بتوجيه من القائد الأعلى للقوات المسلحة. شنّت قوات سنتكوم ضربات استهدفت قدرات المراقبة العسكرية الإيرانية، وأنظمة الاتصالات،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/78280" target="_blank">📅 04:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الجيش الأمريكي:
نفّذت قوات القيادة المركزية الأمريكية (سنتكوم) ضربات دفاعية إضافية ضد أهداف متعددة في إيران، في العاشر من يونيو/حزيران، بتوجيه من القائد الأعلى للقوات المسلحة. شنّت قوات سنتكوم ضربات استهدفت قدرات المراقبة العسكرية الإيرانية، وأنظمة الاتصالات، ومواقع الدفاع الجوي في مختلف أنحاء إيران. وأطلقت قوات مشاة البحرية الأمريكية، والقوات الجوية، والبحرية الأمريكية ذخائر دقيقة على أهداف إيرانية شكّلت تهديدًا للقوات الأمريكية والسفن التجارية الدولية العابرة للمياه الإقليمية. تأتي هذه الضربات ردًا على العدوان الإيراني غير المبرر والمتواصل. وتبقى القوات الأمريكية متأهبة، وقادرة على القتال، وجاهزة للتدخل.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/78279" target="_blank">📅 04:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سماع دوي انفجار في مدينة كنگان بمحافظة بوشهر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78278" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6727b644.mp4?token=HN5u-2KDuepuceW-d8dayFjehc7Podq1tJ0z8vdyzCHtgGPiCLhiJMFS9WxSHZYYGXl7SHleDCcssr6fMp9VAQhe466L-qDmOjoDzW5Fu1TBlWLiyCLiZXvhCkR201onJH-yCwkDdddo_6HQAui4f6BCBRaCzoCeaE5LUkVRDUmStOD40pDUS6UQv5TY_L9qpaUd2roDvWr37XQ9MmYpepKyQw8Y3nxEsodd6-8zhmg45deyh7ptBIJlJhd6rVatfz-ysEhyLh02bgUrmMubu7XjPuOwc7yCdYxZ91uT366LcjYNBv6NcOvIN-jUoSge5uFLW-IkCskOXw2YtMdyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6727b644.mp4?token=HN5u-2KDuepuceW-d8dayFjehc7Podq1tJ0z8vdyzCHtgGPiCLhiJMFS9WxSHZYYGXl7SHleDCcssr6fMp9VAQhe466L-qDmOjoDzW5Fu1TBlWLiyCLiZXvhCkR201onJH-yCwkDdddo_6HQAui4f6BCBRaCzoCeaE5LUkVRDUmStOD40pDUS6UQv5TY_L9qpaUd2roDvWr37XQ9MmYpepKyQw8Y3nxEsodd6-8zhmg45deyh7ptBIJlJhd6rVatfz-ysEhyLh02bgUrmMubu7XjPuOwc7yCdYxZ91uT366LcjYNBv6NcOvIN-jUoSge5uFLW-IkCskOXw2YtMdyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار في مدينة كرج الإيرانية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78276" target="_blank">📅 04:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNkJxl6D2URqQN24W9NRcDK774sQ-6mWeHH91eBrGiJfg967iR0MxvKF32aAb0zSOl4GPpnwXOvPdla3fSh0qBjgUZbMWcY5-a1gIV-_WVqCkW4dvPkFQINI8tmvPHuHn3eUvS9-HdHCuyfmiGKiR1wrtIKerWN8FJ3D7kl6dgEFUCIJyTo7d1XlPoGq-4cLvyFUSRgjT65E679J606j7Gtg3UOsFFFmylccW5wlzw0EE5LetbHM9cYUuuv0KJFL5U72-_1oWd08WEQKLdiJziHknVeaq3qLEfoS0xSnd7DpvJZAuW-GZDrJLLgWrppZJbgfqzxM5V-u5QYeQhdSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد القوة الجوفضائية لحرس الثورة الإيراني "السيد مجيد الموسوي":
هل تُعرّضون مضيق هرمز المقدس للخطر؟ سنجعل المنطقة جحيماً لكم من جميع أنحاء إيران.
هذا هو رد فعل جرأة الأمريكيين في المنطقة، بإذن الله.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78275" target="_blank">📅 04:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b4f3cc6f.mp4?token=sK7KX0oS2SlEoXyp4VpQR9RGG3LNRIM0Mj0qs4Sa-rOe0W6rEWSkM_TgfU9Ej3injwy96jw07TILGZArT1lQnJ5C6kDDCVGkbuiej4XSrfoRcavl0dpTvIYnR-Uts0-Rltoj9t4AeRM4rusEDW1G1jj0xxooHPzibJZyqmUnhFeuPiS3IPzH9WDicTDNJ7GHEpXESQawrHEjOZAp0A6YdSuBXWhssh-dGAhI9Kx3u9fxPGmre2aKAElxPC3IgQwBhr0grZocFrHJhljGjhc7GtCLVF7ELlUXRT9RHY2ENLfbgRcNMc3TtfOaC8A7Bm4smv1q4nt8Aa0gAt5czBGY1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b4f3cc6f.mp4?token=sK7KX0oS2SlEoXyp4VpQR9RGG3LNRIM0Mj0qs4Sa-rOe0W6rEWSkM_TgfU9Ej3injwy96jw07TILGZArT1lQnJ5C6kDDCVGkbuiej4XSrfoRcavl0dpTvIYnR-Uts0-Rltoj9t4AeRM4rusEDW1G1jj0xxooHPzibJZyqmUnhFeuPiS3IPzH9WDicTDNJ7GHEpXESQawrHEjOZAp0A6YdSuBXWhssh-dGAhI9Kx3u9fxPGmre2aKAElxPC3IgQwBhr0grZocFrHJhljGjhc7GtCLVF7ELlUXRT9RHY2ENLfbgRcNMc3TtfOaC8A7Bm4smv1q4nt8Aa0gAt5czBGY1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق متداول للانفجار في مدينة كرج</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78274" target="_blank">📅 04:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تفعيل الدفاعات الجوية جنوب طهران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/78273" target="_blank">📅 04:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوي انفجار في بندرعباس</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/78272" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">توثيق متداول للانفجار في مدينة كرج</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/78271" target="_blank">📅 04:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c8699f17.mp4?token=NeqKkeC-N7CYj9eGzI6orYK_QMDM9wyoT-j4lZGjUn9AoeQEaKdlUjT7-4GnHdOyRTVqB_-1RwqEPLRNuGUeMStacGl-TpbXjP4ro7XYBDAui9ZCBwOfgA80YSrutRx43hAYmf62UI4bDq47_xBHigIvy1pI2vp0B_SKDsHHusA1O_L9krHnhINMUFXmGqPRmdspLjozSHdlyUIxkWJBSI2Jkn0WtFxMaqtroNc91xm5QHrH2vQZ3Ag8zNJx1kiggkc7rzCslnpvOayuBZ3Qe7hTDDGZqZQ9e2dQUJMFEUDF3_-xOs3T_DYZBDvDjqyPSws1KlpY7c6YqB0edk3kxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c8699f17.mp4?token=NeqKkeC-N7CYj9eGzI6orYK_QMDM9wyoT-j4lZGjUn9AoeQEaKdlUjT7-4GnHdOyRTVqB_-1RwqEPLRNuGUeMStacGl-TpbXjP4ro7XYBDAui9ZCBwOfgA80YSrutRx43hAYmf62UI4bDq47_xBHigIvy1pI2vp0B_SKDsHHusA1O_L9krHnhINMUFXmGqPRmdspLjozSHdlyUIxkWJBSI2Jkn0WtFxMaqtroNc91xm5QHrH2vQZ3Ag8zNJx1kiggkc7rzCslnpvOayuBZ3Qe7hTDDGZqZQ9e2dQUJMFEUDF3_-xOs3T_DYZBDvDjqyPSws1KlpY7c6YqB0edk3kxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار مجهول في محافظة ألبرز الايرانية</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/78270" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/78269" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78268" target="_blank">📅 04:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار مجهول في محافظة ألبرز الايرانية</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/78267" target="_blank">📅 03:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار مجهول في محافظة ألبرز الايرانية</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78266" target="_blank">📅 03:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78265" target="_blank">📅 03:48 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
