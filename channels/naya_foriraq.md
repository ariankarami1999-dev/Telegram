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
<img src="https://cdn4.telesco.pe/file/VzOfS0lM8TNe6-jKa8nqaS97QwVg47-PqGFJJNphjqWhDZoqBj-riFN_kdZNp_BztIibcfIq5AoKDIef14EcYnVHP8AsgI5cMpEy_LxtqYtwm71QeBy0b8CTnXc_Rk5R-keJJqNsEySu3wxqbltYLVAb7ZQzTDfREoxlf9d_XnPPzm9XRO1IMRn7cOWo7LC_UJ8VJyXqdozdDW-eQDq2V8AK_v9tmBpqf-084RWyNQFHQ8FD4Tkj0xL1LwjRbZ_dIfMCKKIwHePyzCQh_HzvVJbZxmXhXKDV289BXfF_jYAYX2M_m7YbgVSJJZ4apzKskaR6lXNlpgpqXfqfiJNKzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-92240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">القوات المسلحة اليمنية تشن الهجوم هو الاوسع منذ هجوم الساحل الغربي على مواقع المرتزقة في تعز وسط تقدم للانصار والسيطرة على مناطق حيوية مهمة</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/naya_foriraq/92240" target="_blank">📅 17:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=WirWCLssqomkSDl0ffWRywHiPRDJw528FbpL39ygAfuaWpV46VUAnjAGMRGHpQbRI7dIm-1temvcn7AIupWcz45FEbNQBo6CsGiNda_0afrQOD75DWVuQ0iRrvcKjsz9KOKqQNrHTw3pVi7cyrkwQ1YkG2bqiLMW5XpBdFzdwf_8wncllnhfi3sn1UIKoYqZ8-P1_J_KIwCfqTARGLVK4tTIbJ3ZF4NJNhkvP-2XgMMEJDIyzh_dRkHa1hr3bk4Ea5d-oyr7rINkuHVlO-cCOuIiw-c6tiNq8oHvPPEcCgZHhXzSfKvhbQt-teLKV1FLQjkZHIlvAVE8o6RepdknmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e4750734.mp4?token=WirWCLssqomkSDl0ffWRywHiPRDJw528FbpL39ygAfuaWpV46VUAnjAGMRGHpQbRI7dIm-1temvcn7AIupWcz45FEbNQBo6CsGiNda_0afrQOD75DWVuQ0iRrvcKjsz9KOKqQNrHTw3pVi7cyrkwQ1YkG2bqiLMW5XpBdFzdwf_8wncllnhfi3sn1UIKoYqZ8-P1_J_KIwCfqTARGLVK4tTIbJ3ZF4NJNhkvP-2XgMMEJDIyzh_dRkHa1hr3bk4Ea5d-oyr7rINkuHVlO-cCOuIiw-c6tiNq8oHvPPEcCgZHhXzSfKvhbQt-teLKV1FLQjkZHIlvAVE8o6RepdknmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇶
🇺🇸
إستعدادات الحشد الشعبي لبدء الإستعراض الكبير المزين بنعوش رمزية للشهداء، في العاصمة العراقية بغداد إحتفالاً بطرد القوات الأمريكية المحتلة من العراق.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/naya_foriraq/92239" target="_blank">📅 16:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
حادث إنقلاب عجلة يستقلها ضابط برتبة عميد ركن ورئيس أركان فق21 سابقاً في الجيش العراقي وبرفقته امرأة وهم بحالة "سكر" في منطقة اليوسفية بالعاصمة العراقية بغداد.
"لا يابه دمجوا الحشد بالجيش"</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/92238" target="_blank">📅 15:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
نتنياهو:
من الواضح أن مساعد الطيار كان انتحاريا.
قد يتكرر الحادث لأن هناك مؤشرات على أن إيران ووكلاءها يحاولون شن هجمات ضدنا في موسم الانتخابات.
هناك ثغرة بشأن فحص الطيارين ونعمل على معالجتها ونتعاون مع الإمارات لضمان عدم تكرار مثل هذا الحادث.
سنتمكن خلال أيام من تحديد ما إذا كانت لمساعد الطيار صلات بإيران.</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/92237" target="_blank">📅 15:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92236" target="_blank">📅 14:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92235">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الاعلام الامريكي: ترامب يعتقد أنه من الممكن تسريع قصف إيران بعد الانتخابات</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92235" target="_blank">📅 14:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92234">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGaVyA0rcZvs_4X4GuOGLdJL8t29cVoXg79_YsVG4zkCTBqjELdfft77MSoQ9cNg5fbo_1uWVKAAQOeCyyz4Qn3gl0bpVEeF9ZPXbTfwpIHzaTmkgjRFQ8hSlkwiPJb7A-76dWLhzzpum8BUnOiPf2S1fGqUfjUFX843IQZKwdBzzz0dKfPDBubC3L6cLuo_MgLluS1Wh9E8jIIQs9LMPLp9to_bfqy0OuRPdPmnwqIvqKaz-XMc9Vtk1SMcaumA1F3mC9kqVzWMxD9VYwI145uhofKrVG9-1Tohruq5iXTGc_rG8J0ekJ-oMK0uS2lzjCEPZMjLUFScie2P-4AnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات الطالباني تخلي سيطرات كفري–سمود، وبرلوت، وكلار–ميدان، وإحدى السيطرات في منطقة سرتك التابعة لحدود دربنديخان لاسباب غير معروفة وانصار البرزاني يتهموها بالخيانة وتكرار سيناريو كركوك 2017</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92234" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92233">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
بن غفير:
سأطالب في الكابينت بتسليم الطيار المخرب، الذي أراد استهداف مئات الإسرائيليين، إلى إسرائيل، وهنا سيشعر جلده جيدا سياستي في السجون، فحياة من الجحيم تنتظره هنا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92233" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92232">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92232" target="_blank">📅 13:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92231">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رويترز تزعم: مسؤولون من سوريا وحزب الله التقوا في تركيا الشهر الماضي في أول اجتماع بين الطرفين</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92231" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92230">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
وزارة الكهرباء في اقليم كردستان العراق تعلن تقليل الكهرباء لعدة ساعات بسبب اعمال صيانة في حقل كورمور.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92230" target="_blank">📅 12:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92229" target="_blank">📅 12:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92228">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارة الدفاع التركية تعلن البدء في تسليم قواعد الجيش التركي في محافظة نينوى إلى القوات المسلحة العراقية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92228" target="_blank">📅 12:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92227">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=HHGROBPuaW0OnngXlBkNLEVjAsKnoXV9w9x5s_81SvixJwWeKU6ul9ZvZbWc2Tb_XtGGLhnbNBNz8qLy-hHNSAKur7sdKCH7trcpAM4SYQvWaXBmMGe0P6aKQLL4Tnsa-FXc3uqIJ5ybWHXBiQR8uj0IHKuCoMgwQji0mRqHVq0rgNd4mL_dXlj6VGgLohzpjfCQcgUXNaou3ESqXgvIaJKdUAWMCXg8PMNja3ksNAX6_hJRxFJFmkI3UvdmgnrXvQVwfrcos0AgLejNTRBUlAQobEMWkUSDpvs5XNZXknJRRN2nntt--ShqdMExf0f90QePm_0ksDgLjq7cvU4FaJci0FJYZCa0NnIzzAhrhkhdKohwF_nKYdZuAkYsdIUguY3RRYHm5-nuUd-eO0DXw4LY61juP4B-4ZoB2ULZeuFxHnPOWCxXiN3qG3weNP21Im52ZluNXd-DoiQCXpVZ-DuqNG1k4p0AnY9cYckGBa0s_JlfU-UpD5heuZB_TrVuP8a1KhrJ7Hjbzo3vu-ZtG89PG8P8Xk3lyO5dx87auS2JNkl5GKqTEv_iS041xCG2orv6w9abbFYM8VIlB30OSTlrXWJuRu8u8bp6V_rX-5lGGb4L1HXcBgELGGsepU668zvM4dlvc4K13vNsCDwuNo29yP0r0Rzkf1AcecZC5Ek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5bb77711e.mp4?token=HHGROBPuaW0OnngXlBkNLEVjAsKnoXV9w9x5s_81SvixJwWeKU6ul9ZvZbWc2Tb_XtGGLhnbNBNz8qLy-hHNSAKur7sdKCH7trcpAM4SYQvWaXBmMGe0P6aKQLL4Tnsa-FXc3uqIJ5ybWHXBiQR8uj0IHKuCoMgwQji0mRqHVq0rgNd4mL_dXlj6VGgLohzpjfCQcgUXNaou3ESqXgvIaJKdUAWMCXg8PMNja3ksNAX6_hJRxFJFmkI3UvdmgnrXvQVwfrcos0AgLejNTRBUlAQobEMWkUSDpvs5XNZXknJRRN2nntt--ShqdMExf0f90QePm_0ksDgLjq7cvU4FaJci0FJYZCa0NnIzzAhrhkhdKohwF_nKYdZuAkYsdIUguY3RRYHm5-nuUd-eO0DXw4LY61juP4B-4ZoB2ULZeuFxHnPOWCxXiN3qG3weNP21Im52ZluNXd-DoiQCXpVZ-DuqNG1k4p0AnY9cYckGBa0s_JlfU-UpD5heuZB_TrVuP8a1KhrJ7Hjbzo3vu-ZtG89PG8P8Xk3lyO5dx87auS2JNkl5GKqTEv_iS041xCG2orv6w9abbFYM8VIlB30OSTlrXWJuRu8u8bp6V_rX-5lGGb4L1HXcBgELGGsepU668zvM4dlvc4K13vNsCDwuNo29yP0r0Rzkf1AcecZC5Ek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار يهز محافظة دير الزور السورية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92227" target="_blank">📅 11:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار يهز محافظة دير الزور السورية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/92226" target="_blank">📅 11:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات عنيفة تهز كييف</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92225" target="_blank">📅 11:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اشتباكات عنيفة تخوضها القوات المسلحة اليمنية مع مرتزقة السعودية على جبهة تعز</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92224" target="_blank">📅 11:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb59079283.mp4?token=DTaYZPixmnX-GUJRVw9gWEy4FNCFVQBJbV6xhDPNzBPCMF6tc8Q8e_heoBunVXqVG7auLH8cvzxI-26qBcJoYTfSYOtfnv4eEXJtdmniMhzLYc5UUk57FE0XNWBMHJw3H5a6m8E8zyGRZX2SFOiWD7qEUc9kPltJeFZ45sHhB8BVqLw7vkx_ptaBEob12IZpAnfg9ti-WFjutOmmH9nfsbLLpD41rS9j8S97PXlefIaS2QBZAll3Zotnj-RmhxUPdpIggnzzoQ3KVzZXp35cQiwZuawxrHCoZGX2KBB-exS4BkogV-v1ZZ5pi5_S-jFYobIPm9NP31n4GaOzcUf97A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb59079283.mp4?token=DTaYZPixmnX-GUJRVw9gWEy4FNCFVQBJbV6xhDPNzBPCMF6tc8Q8e_heoBunVXqVG7auLH8cvzxI-26qBcJoYTfSYOtfnv4eEXJtdmniMhzLYc5UUk57FE0XNWBMHJw3H5a6m8E8zyGRZX2SFOiWD7qEUc9kPltJeFZ45sHhB8BVqLw7vkx_ptaBEob12IZpAnfg9ti-WFjutOmmH9nfsbLLpD41rS9j8S97PXlefIaS2QBZAll3Zotnj-RmhxUPdpIggnzzoQ3KVzZXp35cQiwZuawxrHCoZGX2KBB-exS4BkogV-v1ZZ5pi5_S-jFYobIPm9NP31n4GaOzcUf97A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات عنيفة تخوضها القوات المسلحة اليمنية مع مرتزقة السعودية على جبهة تعز</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92223" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">العلاقات العامة لحرس الثورة:
- يهنئ الحرس الثوري الإسلامي، مع إحياء ذكرى شهداء جبهة المقاومة الإسلامية في العراق ومنطقة غرب آسيا، ولا سيما القائد الشهيد الفريق قاسم سليماني والشهيد أبو مهدي المهندس، وجميع المجاهدين المؤمنين الذين نالوا شرف الشهادة خلال عقدين من المواجهة مع المعتدين الأمريكيين، الشعب العراقي الأبي، وجبهة المقاومة الإسلامية الموحدة، والمجاهدين الثوريين في العالم الإسلامي، بهذا الانتصار التاريخي.
- إن إخراج أمريكا من العراق جاء نتيجة صمود شعب هذا البلد الأبي وتمسكه باستقلاله. فقد أثبت الشعب العراقي، بصموده التاريخي، أن الإرادة الوطنية هي السلاح الأقوى في مواجهة أطماع قوى الهيمنة. وإن انتصار إرادة المقاومة العراقية الرافضة للهيمنة على الاحتلال الأمريكي، يمثل صفحة مشرقة في تاريخ نضال شعوب المنطقة من أجل الحرية.
- إن إخراج المحتلين الأمريكيين يمثل في حقيقته فرض الإرادة الراسخة للعراق البطل على النظام الأمريكي الإرهابي والمشعل للحروب، وحكام البيت الأبيض الذين يفتقرون إلى الحكمة. فأمريكا التي اعتادت التحدث بلغة القوة، اضطرت اليوم إلى الانسحاب من أرض احتلتها لمدة عقدين.
- رحلت أمريكا؛ لا بالمفاوضات ولا منّةً منها، بل بعزيمة شعب صمد، ودماء مجاهدين ضحوا بأرواحهم، وإرادة مقاومة لم تنكسر أبدا. وها هو العراق اليوم، شامخا وحرا، يقف على أنقاض احتلال دام عشرين عاما، ويشهد بزوغ فجر الاستقلال.
- لا شك أن هذا الحدث المبارك والتاريخي يمثل الخطوة الأولى في الثأر لدماء شهداء العراق، ولا سيما أبو مهدي المهندس، وبفضل الله سيكتمل الانتقام لدماء هؤلاء الأعزاء بإخراج أمريكا بالكامل من المنطقة.
- يجب على أمريكا أن تغادر المنطقة، وأن تترك إدارة الأمن لشعوبها نفسها. فقد أثبتت تجربة عقدين من الاحتلال أن الوجود الأمريكي لم يجلب الأمن فحسب، بل كان هو نفسه مصدرا لانعدام الأمن والإرهاب وعدم الاستقرار في غرب آسيا.
- بعد عشرين عاما من التدخل العسكري، أُخرجت أمريكا من العراق وسط مشاعر الكراهية والنقمة الشعبية، وقد تكبدت، بحسب اعترافها، نحو خمسة آلاف قتيل، مع الإشارة إلى أن هذا الرقم لا يمثل الإحصائية الحقيقية، وأنفقت أربعة تريليونات دولار. وهذه الأرقام تكشف حجم الهزيمة الأمريكية الثقيلة والمخزية.
- إن خروج القوات الأمريكية من العراق حدث تاريخي كبير وذو دلالات عميقة، وإنجاز عظيم لمحور المقاومة. ولا شك أن الشعب العراقي الأبي، بمواصلته هذا النهج المقدس، سينهي أيضا التدخل الأمريكي في اقتصاد بلاده ونفطها، وسيصنع مستقبلا مشرقا لنفسه من خلال الوحدة والإرادة الوطنية.
- لم تكن أمريكا يوما ولن تكون سندا يمكن الاعتماد عليه؛ فالحقائق والوقائع الميدانية تؤكد أن أمريكا راحلة، وأن الشعوب هي من يجب أن تبني بلدانها.
- ويمكن القول بحزم إن إخراج أمريكا من العراق هو باكورة إخراجها من عموم غرب آسيا وجغرافية الأمة الإسلامية.
- إن هذا الانتصار الكبير هو ثمرة الإرادة الوطنية العراقية، وجهود قوى المقاومة، والدعم الشعبي، والإجراءات الفاعلة التي اتخذتها حكومة هذا البلد.
- وفي الختام، يؤكد الحرس الثوري الإسلامي ضرورة تحلي حكومة العراق وشعبه وقوات المقاومة العراقية البطلة باليقظة والحذر إزاء المؤامرات والفتن المحتملة التي قد تخطط لها أمريكا وأعداء هذا البلد، بهدف إعادة إشاعة انعدام الأمن وعدم الاستقرار في هذه الأرض المقدسة.
ويعلن الحرس الثوري، بصفته من أبناء الشعب الإيراني، وبحزم أنه سيواصل الوقوف إلى جانب شعوب المنطقة المطالبة بالحق والرافضة للظلم، من أجل تطهير غرب آسيا من بقايا المعتدين الأمريكيين، وكذلك من النظام الصهيوني القاتل للأطفال والعنصري، ولن يتوقف حتى التحرير الكامل للقدس الشريف.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92222" target="_blank">📅 10:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
ستباشر الحكومة العراقية في دعم المؤسسات الأمنية بشراء منظومة الدفاع الجوي الكاملة، لتعزيز السيادة الجوية الكاملة للدولة العراقية، وتشريع قانون الحشد الشعبي وتثبيت مكانته في المنظومة الأمنية، كجزء لا يتجزأ منها تحت إمرة القائد العام للقوات المسلحة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92221" target="_blank">📅 09:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
القوات الأمريكية لا تزال مخولة بشن ضربات على الأراضي العراقية في حال تم اكتشاف تهديدات للموظفين الأمريكيين والمصالح الأمريكية في البلاد.
ستركز القوات الأمريكية الموجودة في الأردن على مقاتلي تنظيم داعsh، وستتدخل في حال عاود تنظيم داعsh الظهور بقوة تتجاوز قدرات العراق وسوريا، وفي حال طلبت أي من الدول المساعدة.
أما الميليشيات الموالية لإيران، فستكون مسؤولية عراقية بالكامل.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92220" target="_blank">📅 07:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇵🇰
الحكومة الباكستانية:
قتلنا 22 إرهابيا ودمرنا كميات من الأسلحة في غارات على مواقع في أفغانستان.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92219" target="_blank">📅 07:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇱
نتنياهو:
زودنا البريطانيين بمعلومات استخباراتية تفيد بأنه سيقع هجوم وأنه مدعوم من إيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92218" target="_blank">📅 05:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3bb44f934.mp4?token=VuEPEaCM2QmHlpCHvMZzuWtbTJnfUPVuJJRcmvYPm6Osj6zKquDySKp0LYHWK_08bNlPJozTyAAWfLyour5sa1FJLOUOTiUV-Fofu65QkbGnPfSBzKyVWkjmSBDo_Rhf3zVythiOeURQZReAS-bMn7rXW4ZcSVtXUHYveY1V6SedvvP_PaITW7hmbtmdxiXkICeXIDXlki7nqa1BhkVPtz15tSm0wzqdZIBE9M3C4pTyOBuDYaOOyDPCzydWApmGC-XfZX6p-V0RyARad1aHorxXnLkBHbzJubScBllqzRCJ66OQINlMGkfo4Z5hevwnKOLtSwpEr7HpfknDeSI925JSJxKDDmnV4MHLmEBquq-YPuL5R4fSLAI5RZHR-VoESqnvgCfohpAjLP2m2O6kvzGlO9TtdL9pGUFU9cjpnxVwK_XxvUY-4FnwduTa-6MGVAxx9psMthh1JhIndzP3Tn7jEZ9jMyckvmDVVNBUzQEneYQvKWOjC-dFpDzuJwqT1r8cW3yJXKkIWHil8eX0iA0PB7OCUWts1hI1GsEhn-Zfqswhggv22gaTft2qH9IW3uCyxbckm59uRfHb3lkz_k6WIB3nznjfRvKt5GuzRDAw55QfAnvAnXaimJRD_M0i20JYSdPDo9qHG5oeXVUP9W46bCTBtnGEFp5cUsgdtBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3bb44f934.mp4?token=VuEPEaCM2QmHlpCHvMZzuWtbTJnfUPVuJJRcmvYPm6Osj6zKquDySKp0LYHWK_08bNlPJozTyAAWfLyour5sa1FJLOUOTiUV-Fofu65QkbGnPfSBzKyVWkjmSBDo_Rhf3zVythiOeURQZReAS-bMn7rXW4ZcSVtXUHYveY1V6SedvvP_PaITW7hmbtmdxiXkICeXIDXlki7nqa1BhkVPtz15tSm0wzqdZIBE9M3C4pTyOBuDYaOOyDPCzydWApmGC-XfZX6p-V0RyARad1aHorxXnLkBHbzJubScBllqzRCJ66OQINlMGkfo4Z5hevwnKOLtSwpEr7HpfknDeSI925JSJxKDDmnV4MHLmEBquq-YPuL5R4fSLAI5RZHR-VoESqnvgCfohpAjLP2m2O6kvzGlO9TtdL9pGUFU9cjpnxVwK_XxvUY-4FnwduTa-6MGVAxx9psMthh1JhIndzP3Tn7jEZ9jMyckvmDVVNBUzQEneYQvKWOjC-dFpDzuJwqT1r8cW3yJXKkIWHil8eX0iA0PB7OCUWts1hI1GsEhn-Zfqswhggv22gaTft2qH9IW3uCyxbckm59uRfHb3lkz_k6WIB3nznjfRvKt5GuzRDAw55QfAnvAnXaimJRD_M0i20JYSdPDo9qHG5oeXVUP9W46bCTBtnGEFp5cUsgdtBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هطول أمطار مصحوبة بعاصفة رعدية قوية بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92217" target="_blank">📅 04:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
شرطة مقاطعة تكساس الأمريكية:
إعتقال مشتبهاً به بعد تهديد موثوق بمهاجمة مبنى الكابيتول في تكساس.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92216" target="_blank">📅 03:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e16f07e28.mp4?token=WVfz1hRGthlT4hjhWxbp_-WuBR_Ju12x_dSUfJuscTGZbJrnD2EEpP1WG0-hmLvkyqJ2yM0UBDq_1FVXd5fIntdVl-E3tx2tuuqCKcLdapYSaBE1EHLpR6fRrB8XW5oK9SjYzR025Mw0pOiBqsBXtpaMcxBC4DUYEINN1nQSDxcsLSSOgjBocFkJnbdwLhAihOVhPYm-8YLFHCeaL1MWL6yTvzkJAkfODolHWZE5DKf5nZwjF-TI6cYaYOOXCSAhg0NJRiJsNzlpyswvB4XWpOHnCdXp5Pnw89EGNVNZ05h2EX7X22KmPGEv8HIZ-qk0iouTfqndJAoJQAkoEdECnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e16f07e28.mp4?token=WVfz1hRGthlT4hjhWxbp_-WuBR_Ju12x_dSUfJuscTGZbJrnD2EEpP1WG0-hmLvkyqJ2yM0UBDq_1FVXd5fIntdVl-E3tx2tuuqCKcLdapYSaBE1EHLpR6fRrB8XW5oK9SjYzR025Mw0pOiBqsBXtpaMcxBC4DUYEINN1nQSDxcsLSSOgjBocFkJnbdwLhAihOVhPYm-8YLFHCeaL1MWL6yTvzkJAkfODolHWZE5DKf5nZwjF-TI6cYaYOOXCSAhg0NJRiJsNzlpyswvB4XWpOHnCdXp5Pnw89EGNVNZ05h2EX7X22KmPGEv8HIZ-qk0iouTfqndJAoJQAkoEdECnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محافظة البصرة في الجنوب العراقي تحتفل بخروج الاحتلال الاميركي من ارض العراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92214" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219db791e6.mp4?token=Nu7eQE4ynG3XKhBxYpUldhzM2F0QseLb6EAhNN5I49Dlgz97SsU9b8Ydou5zwezIBV6pNzR4-vXGL7t3jamWkasJwneft7wRDfemMKW8OhcUeKtD9-wYelS_oV6wiwmnkp0l08t8DyLNMhOBzEaE_MpqSplFlpFhw2JUXiSJhIwpe23IbZ_s5KVbKc73El2uaf-7u8XaHL6v7pjdAuATTqV6jhvitPaIHugaOqvrnYTsLX5Gg29WTWN55kpjBG5SSsxFObpKwiVAl8e2Yh2OL90SSJoZWxSWGngpkFYFQcjRrBza_3_vx-2fBHGTZe0pvKTZqpPt7JTLOoVZMFTE6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219db791e6.mp4?token=Nu7eQE4ynG3XKhBxYpUldhzM2F0QseLb6EAhNN5I49Dlgz97SsU9b8Ydou5zwezIBV6pNzR4-vXGL7t3jamWkasJwneft7wRDfemMKW8OhcUeKtD9-wYelS_oV6wiwmnkp0l08t8DyLNMhOBzEaE_MpqSplFlpFhw2JUXiSJhIwpe23IbZ_s5KVbKc73El2uaf-7u8XaHL6v7pjdAuATTqV6jhvitPaIHugaOqvrnYTsLX5Gg29WTWN55kpjBG5SSsxFObpKwiVAl8e2Yh2OL90SSJoZWxSWGngpkFYFQcjRrBza_3_vx-2fBHGTZe0pvKTZqpPt7JTLOoVZMFTE6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: تصفون الإيرانيين بأنهم مجانين. كيف يمكن إبرام صفقة مع أشخاص مجانين؟  ترامب: ربما نقوم بتدميرهم. يجب علينا اتخاذ هذا القرار. إما أن ندمرهم أو نعقد صفقة. الوقت قادم. الأمور ستنتهي قريبًا جدًا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/92213" target="_blank">📅 00:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb9329cb.mp4?token=lrz6KvuPE5qey77Bjxuj2_u6M0Bo7SuIWp727YKCNBuRmerJl9P6AK-7xL58b-9R8PsLoI5U0P9Ut5yTmJe0_ucTesCRRO8EFZD1xjxdxRXwOUiWOzMnxZ_8tqgOjFfgKgezYu_HV9MiAhCL4vIiR4GCD6ZIzen6O0X7UjATtedvXQaNOeBj8QmOeRaanZD8aiuIhSTzcGJ9y6N8xf4WkQtcJl5d4Y3qzuUwHJq0isU8ZcDNM3y8lP3F7cClUDXrRWtA9xW8mxMe6oFe5M3zBa3OEQQ0EHjTSnvtQcqFNGbLJsXaOAZTXWQXHQKqzjVnoQQAB9GPmHZNSmKfiWYuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb9329cb.mp4?token=lrz6KvuPE5qey77Bjxuj2_u6M0Bo7SuIWp727YKCNBuRmerJl9P6AK-7xL58b-9R8PsLoI5U0P9Ut5yTmJe0_ucTesCRRO8EFZD1xjxdxRXwOUiWOzMnxZ_8tqgOjFfgKgezYu_HV9MiAhCL4vIiR4GCD6ZIzen6O0X7UjATtedvXQaNOeBj8QmOeRaanZD8aiuIhSTzcGJ9y6N8xf4WkQtcJl5d4Y3qzuUwHJq0isU8ZcDNM3y8lP3F7cClUDXrRWtA9xW8mxMe6oFe5M3zBa3OEQQ0EHjTSnvtQcqFNGbLJsXaOAZTXWQXHQKqzjVnoQQAB9GPmHZNSmKfiWYuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  أن نتنياهو روى قصة عن سباك إسرائيلي تولى قيادة طائرة تابعة لشركة فلاي دبي لإنقاذها من التحطم. ويضيف ترامب: "لا أعرف إن كانت القصة صحيحة، لكنها ما سمعته من بيبي".</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92212" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامب
:  أن نتنياهو روى قصة عن سباك إسرائيلي تولى قيادة طائرة تابعة لشركة فلاي دبي لإنقاذها من التحطم. ويضيف ترامب: "لا أعرف إن كانت القصة صحيحة، لكنها ما سمعته من بيبي".</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92211" target="_blank">📅 00:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47151339e0.mp4?token=bP7SKJDPvWDOwd_WJyhcelxyKT9YX-KllA1cWK6_Lbf33hg1piVtfkmYlFoxel0k0PoLBXF28Fw0Rpkkwx-4h7LOL4yILMSGm_LpIFRupTwrPIlPs5SuAL_f7IqjDkVNfd01cWzxofWkIRa2pcFFXR9Xm0Gggv6Dt3_NLOGMYophgQEoT3GzqoK42wwmT0EOEcXst91P-vDmJsTFFJi0C8QwDImJQWjBXhhLpd2Gy3xy2FCe9UQYG6WYLljahoZXNUXgIagJiPLCKVqbsxQQHxRUa4Btwgsf9SCMpY3ljKNepRS7w1IzHA0gCS6F8WmKKCpf2hgl1RTwLGVktf4mrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47151339e0.mp4?token=bP7SKJDPvWDOwd_WJyhcelxyKT9YX-KllA1cWK6_Lbf33hg1piVtfkmYlFoxel0k0PoLBXF28Fw0Rpkkwx-4h7LOL4yILMSGm_LpIFRupTwrPIlPs5SuAL_f7IqjDkVNfd01cWzxofWkIRa2pcFFXR9Xm0Gggv6Dt3_NLOGMYophgQEoT3GzqoK42wwmT0EOEcXst91P-vDmJsTFFJi0C8QwDImJQWjBXhhLpd2Gy3xy2FCe9UQYG6WYLljahoZXNUXgIagJiPLCKVqbsxQQHxRUa4Btwgsf9SCMpY3ljKNepRS7w1IzHA0gCS6F8WmKKCpf2hgl1RTwLGVktf4mrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
🇮🇷
ترامب حول إيران:
لقد خسرنا 18 شخصًا في مواجهة إيران. وإذا نظرتم إلى العراق، فقد خسرنا 4500 شخص.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92210" target="_blank">📅 00:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92209">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92209" target="_blank">📅 00:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92208">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92208" target="_blank">📅 23:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92207">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نايا - NAYA
pinned «
ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/92207" target="_blank">📅 23:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ما الذي حدث في ساحة التحرير وسط العاصمة بغداد !</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92206" target="_blank">📅 23:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: خطط الطيار للسيطرة على قمرة القيادة فوق الأردن وتحطيم الطائرة في الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92205" target="_blank">📅 23:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
وزير الحرب الأمريكي هيغسيث
يعلن عن إنشاء قيادة جديدة للحرب المستقلة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/92204" target="_blank">📅 22:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
الاعلام الحربي لعشيرة الشغانبة يؤكد تحرير سفينة ثانية من قراصنة الصوماليين.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92203" target="_blank">📅 22:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0dd16c8ad.mp4?token=WFWCHq6cxGtuIzc14hMQICUFqDcE4IQS3DW9NDGHXPZKd7tY1mRVPx6RKijIlHEt2fXVjVy_hGyZgl1kILEA5Hm0Ns_tpQeDYh7WrAvE0r4yAV9wHsc15-7mLv6GDkBUEWTnFIdBn7Ew5aM5HgyobFSukg8e9sNF2il6DyGPEnIBOk_v9rcVwKDQumr8c5oytV-GhcvyJ3ys00hod0iRpa6oeBggL0ZOamD0Zety4oS163QOiM7R71gwaycuggHsUyG81eGz9JNPE18PQCIQKJvb_VkMZzgzAfnjh_GsZntvI8w12qAB3sTcixB1nV1IMUvuZbGuxXq5faUdtI5Jgq7CIvnNkNvRwRdUeHghrksFf8naUlur6uxzLSkGElN68_jmTc27ZyE8z4Z8pPQid2bKBE1pxkR-HbhCb9U8V4mrvZv34flweyjqPJJ3ciBPM66P3HOF_GjDS3tDGEamtYN7qZT9eSJXbL9PHusVgzYkWoEVg39BbLmySmrSeltJ-GeV8yvQSnsnBW7E9NJrR8happBTcxKbnWZwGjWqkJ6Ixl4ssNCg_wTAMZxkK3EJWxkgddYjgcrQ9-xJr2Kb5cDEh3Z-8dipMZSG_HueXxA2dH8n_796sxTfxNOp-d37PyETCp77YAZ3SFUTXlZ-JUleTJSxvp20qpdxlvjCbmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0dd16c8ad.mp4?token=WFWCHq6cxGtuIzc14hMQICUFqDcE4IQS3DW9NDGHXPZKd7tY1mRVPx6RKijIlHEt2fXVjVy_hGyZgl1kILEA5Hm0Ns_tpQeDYh7WrAvE0r4yAV9wHsc15-7mLv6GDkBUEWTnFIdBn7Ew5aM5HgyobFSukg8e9sNF2il6DyGPEnIBOk_v9rcVwKDQumr8c5oytV-GhcvyJ3ys00hod0iRpa6oeBggL0ZOamD0Zety4oS163QOiM7R71gwaycuggHsUyG81eGz9JNPE18PQCIQKJvb_VkMZzgzAfnjh_GsZntvI8w12qAB3sTcixB1nV1IMUvuZbGuxXq5faUdtI5Jgq7CIvnNkNvRwRdUeHghrksFf8naUlur6uxzLSkGElN68_jmTc27ZyE8z4Z8pPQid2bKBE1pxkR-HbhCb9U8V4mrvZv34flweyjqPJJ3ciBPM66P3HOF_GjDS3tDGEamtYN7qZT9eSJXbL9PHusVgzYkWoEVg39BbLmySmrSeltJ-GeV8yvQSnsnBW7E9NJrR8happBTcxKbnWZwGjWqkJ6Ixl4ssNCg_wTAMZxkK3EJWxkgddYjgcrQ9-xJr2Kb5cDEh3Z-8dipMZSG_HueXxA2dH8n_796sxTfxNOp-d37PyETCp77YAZ3SFUTXlZ-JUleTJSxvp20qpdxlvjCbmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
أفراح عارمة تجوب شوارع العاصمة العراقية بغداد احتفالاً بانسحاب المذل للاحتلال الأميركي من العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92201" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy4f1uu7-OZ8xGQLukzThw8NYNON4XuYxFt4H7fbJUPO4cFf7fUKrpja-Ta3SdqmnVBgsgNS9MeKNESSXuofiKvQH0xqo6bailVaCDr9BAkzj5AUHeAXdm9ws9DHnw0VuFCsDo5czIWjgVwzd7RutowMci22wepXTlH0GmQAtrGkgfZwwETo6TzuiK_sUMD28c1AlJklfCWUvzM9Iw2gHW5Jv9X5zm0KOVHZ1fAGtdgiuUyj0RWZShqp-64t18cGSwaVtxYfC6CJwyg5ZEK6YgYnfkST2mxh0Os3xo8c6bcTyzRhkGGNxcaxtJqQ2MQmtqdnxtwBGtYqwtx_3pR6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلام على من ارعب قاعدة التوحيد الثالثة ..
أسرى ولكن حرروا الوطن ..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92200" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
ثاني خط غاز ينفجر خلال يومين في سوريا بعد خط غاز الذي يمر بدير زور.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92199" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks26IMJr_lsKsA9yEqz65zGdxyTWpOOHbRZ-mpQfzEsFFJG3CEbEEs5zEsjim245Fd5yl7l8W6KgenE8v5jPi8QCalMUlbnrd9orQMcKuPIPjDF7Xv3io9ILem_5fH7Pa3CeLj9E0kjY2fMysyswRQx4IU8r4j8Aigs5xlOJkU1fdzutXPib09ReZfD07pYYguL_xZmxHn1jKMyfT9TaQWffOtzU88naU7_I2LNz3s2NvgDvSwm4YyWp5UMusSP5AKfQW1U8lcYG4Xsnfwp_DKKRv_SWXFPL3_T-E9h9tUSzLkuvCxGQmxHGu3OOWffk1_71MF4LyO0JpYXSLAOFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92198" target="_blank">📅 22:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LITrfZWBi_Ki251-U53n-Uh_pKi0YpkD7L_cLc4wg77_IswsxK7UVB2HTVftDL8mkcOclKE0VcQqC7yKBm1ylCc0kJk2htWdAfAM89MNCG1PsiP0z5KzCimHB-Aq9qx4dGWWaCRiZK8Hm9cykKnGWGcPkRnA-Pvr4byngccEgPSAHXYruJ2bINyPeGzRGY7cu-yJXrA1cfU3tOUnSHFxvqpDK-wfWmcUp_MIsEYV-QYBXezubXZZGIngDNOc5dUnmwzVkOypllTTA7wAYAMU2DaRT0vpvSJmG3g0nilwqxwaMq_H94oxaaqJMd6spfUlnUwtA5aO-bqssGk_t6-ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
توم باراك:
بعد ثلاثة وعشرين عامًا من هبوط أولى القوات الأمريكية في العراق، أكمل الرئيس ترامب عملية إعادة قواتنا إلى الوطن، ليس بالانسحاب، بل بتوحيد جميع جوانب المعادلة الاستراتيجية: بغداد، وأربيل، وحلفائنا الإقليميين، والمصالح الأمريكية، في صورة استراتيجية واحدة، في لحظة بالغة الحساسية. لقد جعل الأمريكيون والعراقيون الذين خدموا وضحوا على مر السنين هذا الأمر ممكنًا؛ ويُكرّم العراق، الذي يقف اليوم على قدميه، خدمتهم. وبهذا التوحيد، فُتح بابٌ كان مغلقًا لفترة طويلة، وهو الفرصة المتاحة لرئيس الوزراء الزيدي والشعب العراقي لتوحيد جميع القوات المسلحة العراقية تحت قيادة دولة واحدة، مع اعتبار أمريكا حليفًا لا مجرد حامية عسكرية. إنها براعة سياسية معقدة مطلوبة لتحريك جزءٍ بالغ الأهمية في معضلة إقليمية ضخمة لا تزال تبحث عن خوارزميتها. أحسنت يا سيادة الرئيس.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92197" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed93d8315.mp4?token=gHx5tdCMVCGZI-rK6SsxJIEdiWdErTyKNaf3tF9PwA3k38PlU64M554cAW2cSJkkZzfdSsiovyy7LIQ-xBg1GDMv7K1xXJ1IO5ekOpRkzSj880BVOb3fzsLbEhWiCoFv83iV0_s-E1t6kvN5wicTYfwuFV8oBKe1Midz4OEyAt_1Wit-ZXFTIt6GTxLuRpb0ahaO7UP8IhMqaObFOQR5_VEi2IVgSMBEKoF7XGPm6LS5YLMQkTIoQ5nvaXV0VYyHTYEMxw7wF8dTwU1Jma66kPxBMJUykmszIcire3US-IhdhG19ulmSpyJ8DGuDaQoItQ2_u6uOuk1s-WKcBkZIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed93d8315.mp4?token=gHx5tdCMVCGZI-rK6SsxJIEdiWdErTyKNaf3tF9PwA3k38PlU64M554cAW2cSJkkZzfdSsiovyy7LIQ-xBg1GDMv7K1xXJ1IO5ekOpRkzSj880BVOb3fzsLbEhWiCoFv83iV0_s-E1t6kvN5wicTYfwuFV8oBKe1Midz4OEyAt_1Wit-ZXFTIt6GTxLuRpb0ahaO7UP8IhMqaObFOQR5_VEi2IVgSMBEKoF7XGPm6LS5YLMQkTIoQ5nvaXV0VYyHTYEMxw7wF8dTwU1Jma66kPxBMJUykmszIcire3US-IhdhG19ulmSpyJ8DGuDaQoItQ2_u6uOuk1s-WKcBkZIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثاني خط غاز ينفجر خلال يومين في سوريا بعد خط غاز الذي يمر بدير زور.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92196" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92195" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f5a08cf9.mp4?token=KCjNSjxvTzZszXSVIkaCIvXjmy8hHusUTl_2MWoFvfTYADQq6-aAzHM9E93e4VwXu6L7MhCrE-b3QBLMxDhqD6ukAl5wvmZXECUY0q3_1rk-YaTnKMIbjlnFkJwfN5hGRkuuVi3ChCqubD3K79u-AALi61Z9PGQDAeVRJ0LSZf2lSUQtyUyJqLACbhxCuS1s3T6aTuvKm3mDkdzFVrTNfjKFa5t9tk9NjWAFjaYELv7nIFg5hOoX8-eK_Y7IwwTRqeyq_Z9WfiWL_CIxa7a8hp612RO4XcR7pc-8nzKSlH_-9CTt2qI9yYjnHSsfxab_eqB3kW-eD06RqvaiEXjwZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f5a08cf9.mp4?token=KCjNSjxvTzZszXSVIkaCIvXjmy8hHusUTl_2MWoFvfTYADQq6-aAzHM9E93e4VwXu6L7MhCrE-b3QBLMxDhqD6ukAl5wvmZXECUY0q3_1rk-YaTnKMIbjlnFkJwfN5hGRkuuVi3ChCqubD3K79u-AALi61Z9PGQDAeVRJ0LSZf2lSUQtyUyJqLACbhxCuS1s3T6aTuvKm3mDkdzFVrTNfjKFa5t9tk9NjWAFjaYELv7nIFg5hOoX8-eK_Y7IwwTRqeyq_Z9WfiWL_CIxa7a8hp612RO4XcR7pc-8nzKSlH_-9CTt2qI9yYjnHSsfxab_eqB3kW-eD06RqvaiEXjwZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيران لا تتوقف من الموقع الذي حصل فيه انفجار بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92194" target="_blank">📅 21:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bf201505b.mp4?token=akaGK9RanAY7uxuE7HhV6ozUfqW-3GkggMPV0bbcYgqgyTOlCyNoF0LBQdaH3BEge5SmeBUuA9hIS14TXORoZo70vr1mCOH0VDCwb4qZxhTtvKx7RG1VDkGH69nHnrjeS6pPsTaIFy4GPaCUVJholVX2om3Mn2BWuuiVuGcZrJ2f17g88Mj4Ng2ixSNVSviNEafbXO7cAi9JfWIkbRa5fMUVpSWZ85USBjtnFAree_MoGZjtDj6tW8UwHJ3mrP4z3BEZYFn2vvcmLrTohdJGbDjj_j806TREBBwxDMFNB6naAgqa2BcNd7O67Zqb9Ps_oskoEEzfFTz4UjdHDWBFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bf201505b.mp4?token=akaGK9RanAY7uxuE7HhV6ozUfqW-3GkggMPV0bbcYgqgyTOlCyNoF0LBQdaH3BEge5SmeBUuA9hIS14TXORoZo70vr1mCOH0VDCwb4qZxhTtvKx7RG1VDkGH69nHnrjeS6pPsTaIFy4GPaCUVJholVX2om3Mn2BWuuiVuGcZrJ2f17g88Mj4Ng2ixSNVSviNEafbXO7cAi9JfWIkbRa5fMUVpSWZ85USBjtnFAree_MoGZjtDj6tW8UwHJ3mrP4z3BEZYFn2vvcmLrTohdJGbDjj_j806TREBBwxDMFNB6naAgqa2BcNd7O67Zqb9Ps_oskoEEzfFTz4UjdHDWBFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92193" target="_blank">📅 21:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764dd602ed.mp4?token=oYKCL6qYN25DWqfopycML_vQHVDdEA4MsHmBeO8Qvsq3SfeqArx1w91HOeRIYwAX6pIk05RHSS0skeIfFuv5W6P5yRrKCFpC9tCB9-c-WkO5s22bJ7DhgX9nslt9bys5T4m1l-qYLiGgaQm4VM_9sLf52sljt5sPFlccM34IwfwQ_kB048AuwKvlMPbSAkHsMAg56WwcJg6EWy4PF6zTpE4GN2oCY5Og3c5U5tehD0BuRfoXelxkyiHUuBa4kuI7el6C9S5VMN8eude2Mcp8Xh9PmJvuFfMTvvFYuEHlh5QaPoL7OcrI978qNlxqsWY2Q4XO0_Geotl_idEtUm5yDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764dd602ed.mp4?token=oYKCL6qYN25DWqfopycML_vQHVDdEA4MsHmBeO8Qvsq3SfeqArx1w91HOeRIYwAX6pIk05RHSS0skeIfFuv5W6P5yRrKCFpC9tCB9-c-WkO5s22bJ7DhgX9nslt9bys5T4m1l-qYLiGgaQm4VM_9sLf52sljt5sPFlccM34IwfwQ_kB048AuwKvlMPbSAkHsMAg56WwcJg6EWy4PF6zTpE4GN2oCY5Og3c5U5tehD0BuRfoXelxkyiHUuBa4kuI7el6C9S5VMN8eude2Mcp8Xh9PmJvuFfMTvvFYuEHlh5QaPoL7OcrI978qNlxqsWY2Q4XO0_Geotl_idEtUm5yDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92192" target="_blank">📅 21:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92191" target="_blank">📅 21:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-PLJWJ_q_cFKZ9i0esKv1M85iZQKnygxTGAFgPQ8crKL9zBMSmMs9a7zXvEmy7gtooHhPpITu15n9bN-hE65gOsDdfBSLiY_Xplrg81_XL7_DRHn4LYMwc9jTfVeapCtPuIOm7FYronX_USAU6TMPzVcgWmyxczQspuAl9qKkhaEdIvAw2bVjKkplN8AWRfrafs2bOjc2u27yAP1o1fkeyQn6FwUexc_1nooUSL3K52DGjgTkQLXHN1oU8PS8pqX6FV3I1ly3kk_vJegpFetHvLHwsBSX6H3WLN_2aL5X_HDhrwVi4ZwlXN8ToWGL6tuWEPN5V-qsCZOWm6BEZztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
انفجار عنيف في ريف دمشق بسوريا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92190" target="_blank">📅 21:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2263171641.mp4?token=vHzNJe-PWGvGEKbvHcdXsroogaOW-GDy91IGHS2kvh45LFw_A8nUU6v6EAcDbQI5Wlo2STJaz8zEXG4gRQhlpOrnT7L0_3oxnw2ZyxsF3X_l0fNnDmtTMBj-Qf7JGxvTOVSJf3UHtknFzmBDeYyqMHEPAGTNAdZymF9awDxGCI7qwujrpwxv9o0sJYbiYem4Dw2kdzlWN8ztb0MzpCm7_ZdlKER83UucEOW6d18HO9He7chxpY1DS6hJ62JN8WHD2zex7cZBMiqQvOnwtvAIy3LhjRKXELRrLGOI9jJij5vyTqwGjDD20cexb3UNb9YnygL0_S4mzmw30ybwr53dZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2263171641.mp4?token=vHzNJe-PWGvGEKbvHcdXsroogaOW-GDy91IGHS2kvh45LFw_A8nUU6v6EAcDbQI5Wlo2STJaz8zEXG4gRQhlpOrnT7L0_3oxnw2ZyxsF3X_l0fNnDmtTMBj-Qf7JGxvTOVSJf3UHtknFzmBDeYyqMHEPAGTNAdZymF9awDxGCI7qwujrpwxv9o0sJYbiYem4Dw2kdzlWN8ztb0MzpCm7_ZdlKER83UucEOW6d18HO9He7chxpY1DS6hJ62JN8WHD2zex7cZBMiqQvOnwtvAIy3LhjRKXELRrLGOI9jJij5vyTqwGjDD20cexb3UNb9YnygL0_S4mzmw30ybwr53dZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من مقرات الاحزاب المعارضة الايرانية في محافظة اربيل بعد استهدافها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92189" target="_blank">📅 21:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92188" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08354de256.mp4?token=RksxYS3lnhQ57kyk50D2ralFS-_obgANxXWZTWM8L5CQYQ4mJsUZyaZ0eg6_-rEvthSSb03v29piHlXbBU5u1EZOF-H1etcXEOP2qLdScriizARbmKK0ATY5NmwRiTzw2CuDY9KaWdBAUPUqRm8IEdohBGlTg3uhW3j8uA6WtEDVboPY1RT3BSipPk4IJfPofzc4HI6v3p9CZLbOQcfN3quvEthn2DRrQKEtVdlzZsyxpOndFMPCDD4c0x5sJNE4QcoK-56mxDI-4hp1tOBe2p3u9cpZr-g9q2YH8OWYtDGSSzW-OnYhFq16l2r-1ogVMDmaL2f8XGlFtgvrVgG-eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08354de256.mp4?token=RksxYS3lnhQ57kyk50D2ralFS-_obgANxXWZTWM8L5CQYQ4mJsUZyaZ0eg6_-rEvthSSb03v29piHlXbBU5u1EZOF-H1etcXEOP2qLdScriizARbmKK0ATY5NmwRiTzw2CuDY9KaWdBAUPUqRm8IEdohBGlTg3uhW3j8uA6WtEDVboPY1RT3BSipPk4IJfPofzc4HI6v3p9CZLbOQcfN3quvEthn2DRrQKEtVdlzZsyxpOndFMPCDD4c0x5sJNE4QcoK-56mxDI-4hp1tOBe2p3u9cpZr-g9q2YH8OWYtDGSSzW-OnYhFq16l2r-1ogVMDmaL2f8XGlFtgvrVgG-eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
ترامب عن العراق:
لقد قاموا بفصل الجميع في العراق - الجنود، والضباط، والشرطة، لم يكن لديهم أحد لإدارة العراق، وهكذا ظهرت تنظيم داعش، نحن نفعل الأمور بطريقة مختلفة تمامًا. لقد تعلمنا من الحماقة التي ارتكبوها في العراق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92187" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
ستشهدون أحداثًا مهمة قريبًا جدًا.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92186" target="_blank">📅 21:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d11445f42.mp4?token=sw0fSyVIW1vsoGs4UHovjEgoc3Ll10TeU7Z1m93aS9fw7BHlNzLs20Kta9VVqLpERVyqmPeXtjnGzzjQsrJpkqDY1PjaTLTvs70J_rd_0pUmok55sQS0E3CCXVAqEHse5KxxFDHSSIzIa24634ICFrYsZrjrZC_9Jykcnl9QCAH-Q6yUobNRAeBCLOEBeDElAcsvvQe5JeiqpeVCxFgQw0GvuFped8h6Z6QXptKO6VQcAvMXcJJSb6_-z_F1ayM3RWDBpSQZwm8RAtcNeVXiHFPLiR0jiLuVZ-2TROLqGTq3-qlPluid2Qt6eOrPkG78SwL3lxm1NEcdt0Ll4wmctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d11445f42.mp4?token=sw0fSyVIW1vsoGs4UHovjEgoc3Ll10TeU7Z1m93aS9fw7BHlNzLs20Kta9VVqLpERVyqmPeXtjnGzzjQsrJpkqDY1PjaTLTvs70J_rd_0pUmok55sQS0E3CCXVAqEHse5KxxFDHSSIzIa24634ICFrYsZrjrZC_9Jykcnl9QCAH-Q6yUobNRAeBCLOEBeDElAcsvvQe5JeiqpeVCxFgQw0GvuFped8h6Z6QXptKO6VQcAvMXcJJSb6_-z_F1ayM3RWDBpSQZwm8RAtcNeVXiHFPLiR0jiLuVZ-2TROLqGTq3-qlPluid2Qt6eOrPkG78SwL3lxm1NEcdt0Ll4wmctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اعمدة الدخان تتصاعد من قضاء كوية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92185" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92184">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇸🇦
حرائق كبرى بمستودعات عسكرية في الرياض العاصمة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92184" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92183">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
اعمدة الدخان تتصاعد من قضاء كوية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92183" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامب :  ويسرني اليوم أن أعلن أن آخر القوات الأمريكية ستغادر العراق! لقد مر وقت طويل، مع اتخاذ قرارات سيئة للغاية جعلتنا نتورط في هذا المستنقع في المقام الأول، ولكن قريبًا، سيصبح ذلك جزءًا من التاريخ. إن هذا يوم عظيم لأميركا، والأهم من ذلك، أننا نغادر العراق…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92182" target="_blank">📅 21:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb1176520.mp4?token=D3fkDNdn7n113Hkswhd7O-trOtS9A3RTNf85eoPH5id1NXW5PWPPdsCoLJ6BD-nkeyLurr38ehHRyddfmk6LJv-R2L-mjV16lLX27gIMkjIQSll0IQsp78j3i5M4BH5BBZ74Vdkb99jxWPa9TUq8IWVKi-ZhNHVp7i4ar3aI0cwWLHAXWsLG6WqOF2P6PV3VeR-SZUAVkR_JlnWA-AXDvHrOhGXV1O1oLcUNMLTTsubZizyDzXNi4YCsMZ9E1ZEcqjv_Y2GeFbzlVu4hYNWoFXpd0UNOq7ZyrgC6SdWiM5ImddRQuq1lNKaaU3AlP11f5uU4GFmNYUXvcGSwuXhssg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb1176520.mp4?token=D3fkDNdn7n113Hkswhd7O-trOtS9A3RTNf85eoPH5id1NXW5PWPPdsCoLJ6BD-nkeyLurr38ehHRyddfmk6LJv-R2L-mjV16lLX27gIMkjIQSll0IQsp78j3i5M4BH5BBZ74Vdkb99jxWPa9TUq8IWVKi-ZhNHVp7i4ar3aI0cwWLHAXWsLG6WqOF2P6PV3VeR-SZUAVkR_JlnWA-AXDvHrOhGXV1O1oLcUNMLTTsubZizyDzXNi4YCsMZ9E1ZEcqjv_Y2GeFbzlVu4hYNWoFXpd0UNOq7ZyrgC6SdWiM5ImddRQuq1lNKaaU3AlP11f5uU4GFmNYUXvcGSwuXhssg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92181" target="_blank">📅 20:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
اصوات قوية مجهولة تسمع في محافظة اربيل.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92180" target="_blank">📅 20:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb0IwLgi5_Zt_B2e4budUK5T6VPbM-4RtQRj1-0JUEDg68r3oFFYjeZ4tYy7nrJfNNROQ5TKUItp_i9NQWbMXiFkvppBQqX8ecTcZPCU3MO4zFunD6pr8Nwc80Sj0c7CMK5fs-zL3eNha834jOyRueL-LrSxogrQj7N33RI4U6rBBlB6MSUQ409JimekltQau_j0K3Ry9mlmsBcYwi23Ljmms2FtL9u7SGJsvDRAsGIpkCavrexppAko0FRuvy3_sS--8EeyApEou0nmoi275mF4jsu2eJvGfYqzbTRBYOxRC3iRV6vrLsiJnQOsX1vsNpn8ehMx-42OawGaKhqQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب :
ويسرني اليوم أن أعلن أن آخر القوات الأمريكية ستغادر العراق! لقد مر وقت طويل، مع اتخاذ قرارات سيئة للغاية جعلتنا نتورط في هذا المستنقع في المقام الأول، ولكن قريبًا، سيصبح ذلك جزءًا من التاريخ. إن هذا يوم عظيم لأميركا، والأهم من ذلك، أننا نغادر العراق مع رئيس وزراء جديد رائع، علي الزيدي، وهو شخص دعمته منذ البداية وأؤيده بالكامل. لقد فاز في انتخابات لم يكن من المتوقع أن يفوز بها، وقد فعل ذلك بأغلبية ساحقة!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92179" target="_blank">📅 20:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 51 غارةً جويةً وصاروخاً من خلال طائرات "F-15" أقلعت من قاعدة خميس مشيط والعدوان الصاروخي من نجران وجيزان، استهدفت شبكات الاتصالات المدنية والأعيان المدنية فى محافظات مأرب وصعدة والحديدة وتعز وعمران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1209 غارة جوية وصاروخ.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92178" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
🔻
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي:
الحاج الأمين للدائرة الإعلامية: المقاومة انتصرت والمنتصر من يفرض شروطه
أدلى الحاج أبو حسين الحميداوي، الأمين العام لكتائب حزب الله، مساء اليوم بتصريحات إلى الدائرة الإعلامية التابعة لكتائب حزب الله، أكد فيها على الآتي:
أولاً: لقد انتصرت المقاومة الإسلامية الظافرة في هذه الجولة مع الاحتلال الأمريكي، والمنتصر فيها هو من يفرض شروطه على العدو، وهذا ما يجب أن يتفهمه الصديق.
ثانياً: المعركة بين الحق والباطل بدأت منذ بداية الخليقة، وقد تتغير الأسماء والأدوات والتواريخ، ولكن المبدأ يبقى واحدًا: صراع بين الخير والشر، لم ينتهِ حتى قيام الساعة. وأضاف الحاج الأمين أن الواقع يُقسّم الناس في هذا الزمان إلى ثلاثة أقسام:
1-أن ينحازوا إلى معسكر الباطل.
2-أن يتمسكوا بمحور الحق (ونحن إن شاء الله من المتمسكين بهذا النهج).
3-ومنهم من لا يُحسب إلى هؤلاء ولا إلى أولئك.
ثالثاً: لا داعي إلى التكهنات والتحليلات، فلم نصل إلى نتيجة مع السيد رئيس الحكومة، فقد انتظرنا جوابه إلى آخر ساعة، والأفضل أن نبدأ من جديد لننتج اتفاقًا متينًا يحفظ للجميع حقوقهم.
رابعاً: إن ثنائية المقاومة الإسلامية والأجهزة الحكومية الرسمية أراها منقبة وأمرا حسنًا، ولا داعي للتحسس منه، والكثير من دول العالم تمتلك أكثر من جيش وأكثر من منظومة عسكرية. نعم، يجب أن يكون القرار الأساسي في السلم والحرب واحدًا، أو على الأقل متفقا عليه، وهو أمر مقبول لدينا.
خامساً: يجب على جميع مجاهدينا في العراق إيقاف جميع العمليات العسكرية والأنشطة اللوجستية المتحركة، ما عدا العمل على استهداف الطيران المعادي المنتهك لأجواء البلاد، إلى أن تكتمل الدفاعات الجوية الحكومية بإذن الله.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/92177" target="_blank">📅 20:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cea8ec4b2.mp4?token=MTajTwtI7LFjFRp6Vc8RO20S8klpbTmtcDb8eusUdcKWbDnkOcEOs_6wW65lZ8DJs1fX-fJjZUq7Ga9cIacfo37zIQsCWHAAIvwL7RxMvMPgyRXbywQ3Y0vCFtXsijy0fJBhVXFtMBz2i1MG5mmPLit2y2IFbJiohypryjAnXKNTVQ5uax_QHKA9ovJ-YgPYWjnwedIUTl302IILxWuI7ILcv-K__4T_2LJeYep-q-t7U35ZIYhkD99XWE42QxtFBlTyoSnqkArI6zqbD-ZYU30yxZfLLBKPvB-Q5jwIWcVVJ1_IElo0vvuZEnKlyOmIIqI909WTFLUsx7ZwNSgHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cea8ec4b2.mp4?token=MTajTwtI7LFjFRp6Vc8RO20S8klpbTmtcDb8eusUdcKWbDnkOcEOs_6wW65lZ8DJs1fX-fJjZUq7Ga9cIacfo37zIQsCWHAAIvwL7RxMvMPgyRXbywQ3Y0vCFtXsijy0fJBhVXFtMBz2i1MG5mmPLit2y2IFbJiohypryjAnXKNTVQ5uax_QHKA9ovJ-YgPYWjnwedIUTl302IILxWuI7ILcv-K__4T_2LJeYep-q-t7U35ZIYhkD99XWE42QxtFBlTyoSnqkArI6zqbD-ZYU30yxZfLLBKPvB-Q5jwIWcVVJ1_IElo0vvuZEnKlyOmIIqI909WTFLUsx7ZwNSgHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
لحظات من هبوط الطائرة التي تقل ركاب صهاينة في اسرائيل التي انطلقت من السعودية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92176" target="_blank">📅 19:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee006731e.mp4?token=RYawBUoAaw7ezNMN3Ki3JgEJn50U0NcCpysEBdxPPh2mhiPmCX5VxBfRMyxAyf4w8U87QKKmAXJBb0mK1tF14xtSuH0OlXh8DyEqaEsnOgc9gbU9062m-Xxf9AWoevLpnKibVUrpiuVTAXoDDO1R0OchMrkVkQy5jgyU8bQFLpUunVgJn-xfRUnevxp45jXEmCg8OxQBz7BEnlTrHGFef3hPikQSe98TvctwVni8WsfZCzmvOz7VKwrmeTAeidqy2AyoCuuXU3H_ccQBo_YXZkL1vD3mq2ggFo9S4Zh7nUqrO8vY3WE9HjDnW91mnrZwHErYSlImBlZLwBDvfsMnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee006731e.mp4?token=RYawBUoAaw7ezNMN3Ki3JgEJn50U0NcCpysEBdxPPh2mhiPmCX5VxBfRMyxAyf4w8U87QKKmAXJBb0mK1tF14xtSuH0OlXh8DyEqaEsnOgc9gbU9062m-Xxf9AWoevLpnKibVUrpiuVTAXoDDO1R0OchMrkVkQy5jgyU8bQFLpUunVgJn-xfRUnevxp45jXEmCg8OxQBz7BEnlTrHGFef3hPikQSe98TvctwVni8WsfZCzmvOz7VKwrmeTAeidqy2AyoCuuXU3H_ccQBo_YXZkL1vD3mq2ggFo9S4Zh7nUqrO8vY3WE9HjDnW91mnrZwHErYSlImBlZLwBDvfsMnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الطائرة البديلة الى تل ابيب قادمة من السعودية بعد الخدمة الـVIP التي قدمها النظام السعودي للصهاينة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92175" target="_blank">📅 19:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u38dhSRWQcoMnOLRaGLTo_3wazGW4gJJxyG2P4VkMwv3POuYOO99f6RoAlyi23Nne66BBKu_FoXpg7CgEwz3HCVVXCIOjezDaq00mqAD1UfoVHVziJc42j8jr5X5bvgz7OK805oWqbV1nfBDWflKxSD8rC1BXPzUXUSherrEtlMSWM0lD5p8a-3gTsMC7wCQRiwYFdW80e9BHoHd57hKF13D7IbARJscJe4XqNM8vHxyt2UQA1OtTqU64_Ck-8ZnQnEvHx4iYk3-M_Pa9AFBZhAUr7ay3BIse2VwR06Ng990jsDND0LZuhMYNc0aEMYOEsSnGMvC_O-IQR5x046btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منظمة العمل الاسلامي: نؤكد ضرورة رفع أي حجوزات أو قيود مفروضة على الأموال والعائدات العراقية الناتجة عن تصدير النفط بما يضمن أن تكون موارد العراق تحت إدارة الدولة العراقية وبما يخدم مصالح شعبها</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92174" target="_blank">📅 19:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTFDynkSed7ca5YPUeapLNrmdb9CrH7kYZ9XL5hMc_cBpt44hdXlLTpzezYGQXdj4UW80o2P9sWQH9KEOaWWHeWRgeyZ0Tc9i4YmQJu4-Dw1-dMtdfbrjnQWQHKZsd9tCr1U7TY1HxrS_WVntU5_m1rUw-UFlA6H3ztgJSyoFNm2B-hksr1bsx1IlUdz3ZhZqDE1HqvjeAvFUg01W6dDqyHuB07nR2Y8uLB-KIy6hhOmBNvqRCM0E14kbfYTAeoBRmCrZ26rirkfGJdQYfOJVNdfOoidJVg9euDYy_4l_AOO4sTvkkW6QpfSeg5LgwrWyyiTkq93Wh7QCPPYpWTwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولى المشاهد من قاعدة فكتوريا في العاصمة بغداد بعد تحريرها من الاحتلال الامريكي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92173" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee502fdcdf.mp4?token=oGgPdHpJBUyl9x8duMBgtv2YLmGPVg4R4NRG94DcVMLYC0XkaDK8VzkTv5eRmW185oiKJBR0WaT4Y-wK6eWK7y99FoE1dG5cFLUOXyTTJ6zjvtPYRt1VAoq1m9QrMATVf2x7nGtGR-lNcZ-ix9gwEXK-_5E6dluywMTCuOjjKJHf-jSgMrBfUrEXgcPk76wN6kbyrVjyPKQSUhKcb_4sjcXMTD43On6qmJ1hEC5CrjzxWwX4QawYr_ovDycqSHm-ljdERu-tdwkFdbn2044mtpSj-gkXErKw3yRGlxJooJd__nkUULBxJmrSeGRNRfRu_L46SQEK_HdA20Eqp7QcWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee502fdcdf.mp4?token=oGgPdHpJBUyl9x8duMBgtv2YLmGPVg4R4NRG94DcVMLYC0XkaDK8VzkTv5eRmW185oiKJBR0WaT4Y-wK6eWK7y99FoE1dG5cFLUOXyTTJ6zjvtPYRt1VAoq1m9QrMATVf2x7nGtGR-lNcZ-ix9gwEXK-_5E6dluywMTCuOjjKJHf-jSgMrBfUrEXgcPk76wN6kbyrVjyPKQSUhKcb_4sjcXMTD43On6qmJ1hEC5CrjzxWwX4QawYr_ovDycqSHm-ljdERu-tdwkFdbn2044mtpSj-gkXErKw3yRGlxJooJd__nkUULBxJmrSeGRNRfRu_L46SQEK_HdA20Eqp7QcWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تأكيدا لنايا مرة اخرى
🇮🇱
مستوطن صهيوني: حينما نزلنا في المطار السعودي قدم السعوديين لنا الكعك والبسكويت والعصائر والقهوة ثم بعدها قدموا لنا الطعام الساخن ووفروا لنا فريق طبي يعتني بنا واحد تلو الاخر طوال الوقت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92172" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d721dc53.mp4?token=c6CefBCbZKbrrK1hiRsArt2A65ReY-vqAiCyoOLBMkM5HSGX6rR6a9l2zQVOsoEijjV5vAipoePvvwRSpZTtSoqkW7VeRb6XyezqK88C-Zwj8QyKm0IHGroDL1jYaiKIepWXbmM5FracoRyaVc61vB3FIAc7TVca7nXKqHXGql8_h38x8fdmJtRT6vLdlQ-G6aCBwwLmxf_y1gvONEPMbBtgVmjQVdoHJW-Ry3L6P3YoppIhk4Ae0B2jTr9z3eSwsuSGMEgzzlWm6JrWEEwklx1nExgsfQVkUU-TSpuJy7zUawEcu5ehgeKjy22mQVARUT91eHl7xP2Al8K7f8Yohq8W0OEo93M8OraQ08DEyfxztU2gxhmAU6dmxcJKoZNXOhWidtn5gORMc0cQS2mQ9pwrgkfuSjdV3Pyqr8uyDvYGFCImB5Ob54GCMpBXLvIVA1ZXwyhuGNMKsUpauM-CyWMDBXaq1lufhnBinh7FuCwQD23xG26fSyNUA91I1B4jlmaOFbZQVru1Aa0IVIFbcjKBTWzve22y4_C-r1asifeUzyxjbG4D8sBTc8wGbD4-bfIn0Ir25wgqa73dHLvFWoZ_wwPfrGFIwcLVW-NLmrQ002TezJ2LR35QnymwZ_65KofBS83CtkL1oWVrM7t5afG3fZUIQwvSPQIp9wS7trM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d721dc53.mp4?token=c6CefBCbZKbrrK1hiRsArt2A65ReY-vqAiCyoOLBMkM5HSGX6rR6a9l2zQVOsoEijjV5vAipoePvvwRSpZTtSoqkW7VeRb6XyezqK88C-Zwj8QyKm0IHGroDL1jYaiKIepWXbmM5FracoRyaVc61vB3FIAc7TVca7nXKqHXGql8_h38x8fdmJtRT6vLdlQ-G6aCBwwLmxf_y1gvONEPMbBtgVmjQVdoHJW-Ry3L6P3YoppIhk4Ae0B2jTr9z3eSwsuSGMEgzzlWm6JrWEEwklx1nExgsfQVkUU-TSpuJy7zUawEcu5ehgeKjy22mQVARUT91eHl7xP2Al8K7f8Yohq8W0OEo93M8OraQ08DEyfxztU2gxhmAU6dmxcJKoZNXOhWidtn5gORMc0cQS2mQ9pwrgkfuSjdV3Pyqr8uyDvYGFCImB5Ob54GCMpBXLvIVA1ZXwyhuGNMKsUpauM-CyWMDBXaq1lufhnBinh7FuCwQD23xG26fSyNUA91I1B4jlmaOFbZQVru1Aa0IVIFbcjKBTWzve22y4_C-r1asifeUzyxjbG4D8sBTc8wGbD4-bfIn0Ir25wgqa73dHLvFWoZ_wwPfrGFIwcLVW-NLmrQ002TezJ2LR35QnymwZ_65KofBS83CtkL1oWVrM7t5afG3fZUIQwvSPQIp9wS7trM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تأكيدا لنايا مرة اخرى
🇮🇱
مستوطن صهيوني: حينما نزلنا في المطار السعودي قدم السعوديين لنا الكعك والبسكويت والعصائر والقهوة ثم بعدها قدموا لنا الطعام الساخن ووفروا لنا فريق طبي يعتني بنا واحد تلو الاخر طوال الوقت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92171" target="_blank">📅 19:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ced3ab6da.mp4?token=av9UIXkBFcQKmWR2YGnBLFKnFaDlsNRveZaCi6Nl7yc71Uv4vVeP494wBiOqaTMyYKm15UbSknPkh7GdNlFv1PAvssSL3OdqBsMvI46sEmOxO04Uak37-H9IOUbgkcJOI2ewFx1JZJzWQdV65aUpMYWkItXihU2BmHvvnwu06xJ_GXjtP0I65LlbmTqFFkoYSxE6v0sRhvBfE6iHQ-Zf_ol3OmVUCYexReNcNoRua_e1UvFYH4I2hKEb4ICOl9xrLPjWxHrOmqdKlDtcQJNgbu_iobGQ2yI2rKqc3kkcWIjqXCuP4OrG9EI7PGdI9jY_Huq3A6gBWWM2m_y5hGhkUxtjB9l_SO9jJKplaJO2APq0WdMbaT3MHp4STphC5w_h5HcVFa087s8HtAOwr88KS7QKwdqE1SgcF-vM0jHzHQZKzKVKQ_Ven2Xcqn8brrdWMzFYLluWjp21WDk9RveqElcGb3F0DCUO4MGYuTsdtolHPwu01q7UV3ksAjrH80AxFDmUNHYObwbDhMZTjYptaxpKVHbkTV5lbCvxRNWfEe6i3dGEigckcITWYbe8gno9zX743_hlGC8udRcm-afwVLfjdnE8_MzrUJnHz8WP_uyxzqQBWXagkivTk-SdGJa5IKh-vwKynYeUDRybfO2qvY-5mozoLQCecjRCglPMRYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ced3ab6da.mp4?token=av9UIXkBFcQKmWR2YGnBLFKnFaDlsNRveZaCi6Nl7yc71Uv4vVeP494wBiOqaTMyYKm15UbSknPkh7GdNlFv1PAvssSL3OdqBsMvI46sEmOxO04Uak37-H9IOUbgkcJOI2ewFx1JZJzWQdV65aUpMYWkItXihU2BmHvvnwu06xJ_GXjtP0I65LlbmTqFFkoYSxE6v0sRhvBfE6iHQ-Zf_ol3OmVUCYexReNcNoRua_e1UvFYH4I2hKEb4ICOl9xrLPjWxHrOmqdKlDtcQJNgbu_iobGQ2yI2rKqc3kkcWIjqXCuP4OrG9EI7PGdI9jY_Huq3A6gBWWM2m_y5hGhkUxtjB9l_SO9jJKplaJO2APq0WdMbaT3MHp4STphC5w_h5HcVFa087s8HtAOwr88KS7QKwdqE1SgcF-vM0jHzHQZKzKVKQ_Ven2Xcqn8brrdWMzFYLluWjp21WDk9RveqElcGb3F0DCUO4MGYuTsdtolHPwu01q7UV3ksAjrH80AxFDmUNHYObwbDhMZTjYptaxpKVHbkTV5lbCvxRNWfEe6i3dGEigckcITWYbe8gno9zX743_hlGC8udRcm-afwVLfjdnE8_MzrUJnHz8WP_uyxzqQBWXagkivTk-SdGJa5IKh-vwKynYeUDRybfO2qvY-5mozoLQCecjRCglPMRYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92170" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj60uN9NFo1rnga7Ra6Aj_uSr2_QH4l4AirSlW1ehrU0SzAunv-G_b_Lc6Jl8nnT47H3hvYGn5zyPYbRSxdmTqOVG-0JdDM258Dl7lQAoe9fbkGK83LHJqWCV3Ma7gvPBXs8ruiTxx0cIOSM_smLz5xpJXHGKt4_mfI4_Ptu3x8W9QmAImLqLIuSj_-Ta-vIFm27zQ6zJpK1dJntApbZInmn5N3mqGKZ18vKd0HejuuBBtiId-NUW-UkFe6IXYVtqUB8asmnbfh500T3OD0iBhaDazex8A2gMDiTHb_RF4bK5xQP6BRr1EZ9TRMh1jlxJfGFBSimTEq09_HsJpaz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي بالعاصمة السعودية الرياض.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92169" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJm4SV3m6rjvE2f4PNhwsiTNdtbfE3dNHPK_R0pOgQcfkqqRo4witGMy8TKKCWWzu11lzZICGKV_vrx9dFDlPGS655GB9hXwi0-sfsuNohyKyNYP9e4oTZdR4JMdE24YHAqTmkNmOjjxCIUUpCsOskS_y94QT3ufngkMQrmrfBa7ISwz9g7W8Q1eEtzZYATCt0csZ6v2iOqYKK3m-D18Ko6ujtGhaHlbflXgJYSNme7S_PTas-yaicI4P-bmWLTpG38aXnCKTmBO43bCNshIPxmrhB2EXJTCGnFrdIEWe7l0r2DVWO-WnMfQGMNTYzzlFDJehCy77YrwSn45fNFePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستر : الواوي الذي طيح حظكم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92168" target="_blank">📅 18:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtUDnPvOTcyz3oHFMtbBb7C4AtFhJH1kTH5eptYDaPGOCYDJFdJwKrZAKUt4gdjVCNUca-2G3JXGoHmyxVtYru2lgtq1sILhZaEkfIaXmcbYl3BUGmCP-J4PS05yCHP4dSrCCzVc-JUAM-1hqi8HaG3hnbpFeRhbSnfEtyFdI3wek_trVAmsrjxdKlK_5dlpIBMWHcNJAg6Ovq2Ibito2lDmAUaIgss7udlkIQVgrfSxhSsuLqh-DGZNd0u8qi8WK57ug-wZqMLlB9YAVzsQmyOpKXcxO1P9aIOKx-2uPE0kcvLCG8TTx8HdBpHamUrVviKpVwgnGLNRgL8ORMvxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخاناً أسود يتصاعد من حقل عين دار النفطي السعودي بالقرب من خط الأنابيب الشرقي الغربي</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92167" target="_blank">📅 18:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الانفجارات سمعت في الخبر و مقتربات البقيق غرب السعودية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92166" target="_blank">📅 18:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92165" target="_blank">📅 18:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0264db5cd.mp4?token=j42eYCBC3IXcWwgnKGEojM5swMvbH8Yem_TleyAI0toKtQq_tfZfNtcAbMRV_VXd3ZyOJgnPLiCRbdTc4JCwkvpSHc0W53bUg1cLEIlUPQBznuXugX7pRJBXOXg6aonrFyRe06NIPXPwqWlQ7aZsImYi_y1a7-OyTlhlJQHI-oDUaGUV2zz_e73mJvyfXhSd4Jc5tyO4G87l7ZKbyOdTVo4V71ZmFF1P3fYhJDKfpL1qfoZdHcyxhxDKZa7Rmw7WBW3Ghbr8lY5qZ9f6fl5uoIG1fwK7FrsQ2pRkXeOloeDEb7tG-5TXP72wbejSxqZ7FR6m5Fr3PF4H4nKJeBPadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0264db5cd.mp4?token=j42eYCBC3IXcWwgnKGEojM5swMvbH8Yem_TleyAI0toKtQq_tfZfNtcAbMRV_VXd3ZyOJgnPLiCRbdTc4JCwkvpSHc0W53bUg1cLEIlUPQBznuXugX7pRJBXOXg6aonrFyRe06NIPXPwqWlQ7aZsImYi_y1a7-OyTlhlJQHI-oDUaGUV2zz_e73mJvyfXhSd4Jc5tyO4G87l7ZKbyOdTVo4V71ZmFF1P3fYhJDKfpL1qfoZdHcyxhxDKZa7Rmw7WBW3Ghbr8lY5qZ9f6fl5uoIG1fwK7FrsQ2pRkXeOloeDEb7tG-5TXP72wbejSxqZ7FR6m5Fr3PF4H4nKJeBPadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد اطلاق صواريخ من الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92164" target="_blank">📅 18:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92161">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBinqxTdbny9Mkrgo7efhifly2RoCHfeaASZVmvqLWA3tmEQZE0HXYp2BmtDmXz9NtyRH3zoetfFbush02NoCPERM_-TFY9qI_C3GX7GXYv9VkGMydQJlnukEsrDiewY0cvJoukH4p-Xoh00UaMcWKSIBW8uwUA4PaJSh7O8wjY85dDXJ8_6HeuBDnL2NdUhRLsBN_ivfdF6Yum6enELBNe0GLDLN8NgG6hR20meq_i4NQaRaiw7buewFILJM4O8dSMbER85XrLxCpg-ma938lcq_P8PwqE9rqUKpTK9hYa8Wd0HJD1-Nf9UdHwVeAw04roKH5AbvAPtDUUrOftrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEG4hOUFmfjYyVe_BjqkX-07dPg5-dgcO_tLQq_RciArutEnaLA4MOr31r_AYYxxG1AGqFvXNJcGv2znOtpCGHvmxWOK3k6lZMb63T0Z1O4W9n_dMdnihB-X50AFHuPLmpM-egcqo6HnJlO4IECjVnYpEpCISHarpuVAqUV_LEnLKaq59l6mTkXa8UCCs37Cogm2htRiz5d_T2NjLVbJrV52A20uvhVDuDuQaTimTVS9vU5xUphTTvu9gFoYiHm641SkeV_KkTDecBj6b35GCcK2E1uVj6Xqoi2rIS6AheC5ENtYHqdl4lI_fQb9Zj3CCu7oKi2u5hZ0LbvbV7n0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0_-PD2I34SePg3NhLrhXRJe89Gdw4vvqczLEJ2qKBPiPqo7kNOdbDUmJpnnmF-K3mQejtfp_9J6mFJNBYP3EAXtMJcuZAmDFXagI6jSRibZEFSvhkXoOPAN8Fn5mHQLIyresYxS8zkHS25u-6tDUGIYs8DK4zFix4-wqpWxe8NCVrB1Np9e1Cuo3dcwqhMbx-Z35RCnIdD33Gc9QhsZ1NXVl21SCIg7id952FfPLYRv4luZ5KIuQcPS1iXJFxei8ntQ_GLPxtox3XjADy7JCtGkwZDI9yaA740pGiKJOELCbZZM_VFixWk75UBi_Y0tYtERe2pkjf1lF35hEieyrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇮🇶
اخر ما صورته عدسات الكاميرات للهروب الامريكي المخزي من العراق: طائرات الشحن التابعة للتحالف تغادر المجال الجوي لإقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92161" target="_blank">📅 18:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
مصدر لنايا: ال سعود يقدمون القهوة والتمر للصهاينة في مطار تبوك وخدمات اخرى افضل من تلك الخدمات التي تقدم لحجاج بيت الله الحرام.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92160" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
‏
إعلام العدو:
نتن ياهو سيستقبل طائرة فلاي دبي البديلة في مطار بن غوريون.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92159" target="_blank">📅 18:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
حزب الله ينشر:
من مجاهدي المقاومة الإسلامية إلى سيد شهداء الأمة السيد حسن نصر اللّه (قدّس سرّه):
يا سيّدنا... سيبقى صدى صوتك يشعل بنا الثّورة، فنرفض الذلّ والهوان، ونطالب بثأرنا الكربلائيّ من كل ظالمٍ ومتغطرس، وستشهد الأيام ألا إنَّ حزب الله هم الغالبون.
ترقبوا الرسالة الكاملة عند الساعة السابعة والنصف من مساء اليوم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/92158" target="_blank">📅 18:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شهود عيان لنايا   انفجارات عنيفة تهز المنطقة الشرقية في السعودية .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92157" target="_blank">📅 18:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92156" target="_blank">📅 18:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92155">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شهود عيان لنايا
انفجارات عنيفة تهز المنطقة الشرقية في السعودية .</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92155" target="_blank">📅 18:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارة الخارجية البريطانية: ننتقل مع العراق إلى مرحلة جديدة من التعاون الأمني والدفاعي</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92154" target="_blank">📅 18:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfiCMJC4XIKa9WR59fJjuEM4EZZfUfwXhn7A7qjI3CFyTeJ83BmS0yO1I2ALtBMaJcDr--uhRZC9Efw4p-DbLWNFVsGe_JQQuNZImTAl6yZdwQsh9Lkdu4gtfzzmZRj7aEGEeDrURI57J_7GfHTO91u0bKBQfR535L9AJJCn62bXGwrfZjJEgacUuYeL2jHpGnBSOuMzBT91tfsHKrZm2IAHT44nykSxpel79jXW-0vmO-Me0CIF7GvLSl87yqoLHKCBLXwTwOZ-ZsHL2RXJibw5gFx7fH7VpPqegBqymlCj_M4Z-DOf__0pFLJvIRUuTO4UaubWjFniuu0bcVPEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr31JQJogcq9SAJH7g1if3EE6yCmKzhEfSzTmWic1IJ8Mt_3vVvcjws7F9iTDsZXFzeUc46Jn6-pYvV0ocvjw_hEuNHY5emnsOfm_9X9ea8o6I9K4uq2b57WYYMNnpiqFjmu0smIaltUH8qoyU8vQnGZOo9Nd9hSVzEmhbPTVwUG2wEIEch0WR9dqFbxjhl6VlR-CstZm-Tq5sH_lQ5PUGAbb8f_2TLyy1etB1tQJybN8melKkbF_Em9pgnTu255efZemyX34BwUEpB2xoofEh_4uFDWLW3wvrrudWqa4d6Rr0jCqbWb3kC2U0e9Dl1lFTSBRo6FE5HOZDz0mhRb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9GSE9-KvF5Wk-hQUJ4g3-rfdEX1b8C57-B2FjL61L2jfYZEFPklmxu0sH8T9sGxMpbkGCphHF9ZxcMw9zO9JPkZw1iOJEVluc6Y5a2nNEKmywUGV_wvbH76l9rEjeSwkxcPSckJVC5D3HgaGYVo4eUrra6WTiKmekXjmIf3CVXgLwjwwQEJae58zN4n-iuIqJkMPtr3bb4mFrYVXTMLLjNd2Nc47TzGcYFEjXsVMgjtlJu39ehuijUvjOH-GRFHyXcp3urSWFQyZuNjZVY9nL9aPI8snQrTCzfv42CwWxMk3TppBOvSoPDSsSLvVvHdOSEH_927W2jsBYsLRehToQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلاح الشيعة الباشط سودة بوجهة الفرط بيه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92151" target="_blank">📅 17:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44874274af.mp4?token=XWO8UwZMKQ7ko4ShFotVBpHBygAdgsf2YxUGMiMIhw4gUf_JcjmBuFN30jVobIUX5dmpQurwN0UFYf5KyhvmZ4Dk7vVKx-t2_r_BI6Fc8CnGxNURjgEU6F1xSN_OBHBPOlsTpIDmhmL__KDD-phMy6CsR4HAen6mtMSSdgxwrjTHUEMY31Zc7-pzlfVEcjw4ma6xya-XbPH_yYa63yjmsbO7FxGzVL1GVANaPoIR67B2fg_tXBAtgszgn6PWw0eqj6bX5-x3ycNih1WuOXHbhF9JWwwfFeIShZtbAAiPMjF5of1BQj17qAjIfaq5BGa-fJ8NZ5T_ckvpFAywl4d_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44874274af.mp4?token=XWO8UwZMKQ7ko4ShFotVBpHBygAdgsf2YxUGMiMIhw4gUf_JcjmBuFN30jVobIUX5dmpQurwN0UFYf5KyhvmZ4Dk7vVKx-t2_r_BI6Fc8CnGxNURjgEU6F1xSN_OBHBPOlsTpIDmhmL__KDD-phMy6CsR4HAen6mtMSSdgxwrjTHUEMY31Zc7-pzlfVEcjw4ma6xya-XbPH_yYa63yjmsbO7FxGzVL1GVANaPoIR67B2fg_tXBAtgszgn6PWw0eqj6bX5-x3ycNih1WuOXHbhF9JWwwfFeIShZtbAAiPMjF5of1BQj17qAjIfaq5BGa-fJ8NZ5T_ckvpFAywl4d_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گالوا ما يضل محتل بهاي الگاع</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92150" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92149">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4557c1107.mp4?token=g5jAZZPF6C-tputm8E3aVjF7r9V2EmJYH5EBxGLESfuxgLd87I6q68aVPErR34-4pdwcMcgfXYSM8zAMsRfzeOyOzVGUUCN4m7BcqV7nH0vZsFB_gOcIyHt4YIdEjRWCaTqa6ds20x-ndqhQQJISTSOGLI9pFhxDtWx6c9tikENYfd1FTQKTkbJv2uojq5jzLt_c2X8XGDVsqK8XsYXSEB6tNJAlV2gkuTMfR45ylwBFW3KYObnsVK40S6GZCdW8LN9N7UF07UggbjxsgeejvCOX9M1Py9Uysi_Zp6sJ4JecwnElW2H5EYCRbcaUh6BRgXW5mAhSr4zUR7Gh7ZLaOYya3ioJySwzHS6AYQkzTE-se0BwYWLhdfawy8VAnKqGREvTLxB-zbyYGgJimHj9g3kC6tyL8DST64fGfzgSRndF4-sG38QVVX9jffIGM6U7RrpPgZs8SL9z0syjQ1wY2BClAAGQ1dMpk6j97bi35VZHT6NJHNFJ1z0joHj_TYMPEEIkFZjbdw-sg3DZenjrhyA1oj6I1S9H0EdplEaP6rJc_ke9slUwWudkgj_rBUrC1XQkA--Xwf7pvVst7JOTUyw0-HYBnQqOddKltxSAZ-xp87mPeFuZ-kWVtG9tbhT5QNyQ2SxB5dGDtitZg4rKJh34htp1tMoJ76bsj83L1Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4557c1107.mp4?token=g5jAZZPF6C-tputm8E3aVjF7r9V2EmJYH5EBxGLESfuxgLd87I6q68aVPErR34-4pdwcMcgfXYSM8zAMsRfzeOyOzVGUUCN4m7BcqV7nH0vZsFB_gOcIyHt4YIdEjRWCaTqa6ds20x-ndqhQQJISTSOGLI9pFhxDtWx6c9tikENYfd1FTQKTkbJv2uojq5jzLt_c2X8XGDVsqK8XsYXSEB6tNJAlV2gkuTMfR45ylwBFW3KYObnsVK40S6GZCdW8LN9N7UF07UggbjxsgeejvCOX9M1Py9Uysi_Zp6sJ4JecwnElW2H5EYCRbcaUh6BRgXW5mAhSr4zUR7Gh7ZLaOYya3ioJySwzHS6AYQkzTE-se0BwYWLhdfawy8VAnKqGREvTLxB-zbyYGgJimHj9g3kC6tyL8DST64fGfzgSRndF4-sG38QVVX9jffIGM6U7RrpPgZs8SL9z0syjQ1wY2BClAAGQ1dMpk6j97bi35VZHT6NJHNFJ1z0joHj_TYMPEEIkFZjbdw-sg3DZenjrhyA1oj6I1S9H0EdplEaP6rJc_ke9slUwWudkgj_rBUrC1XQkA--Xwf7pvVst7JOTUyw0-HYBnQqOddKltxSAZ-xp87mPeFuZ-kWVtG9tbhT5QNyQ2SxB5dGDtitZg4rKJh34htp1tMoJ76bsj83L1Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانب من الاحتفالات في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92149" target="_blank">📅 17:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92148">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حادثة طائرة فلاي دبي كانت محاولة لتنفيذ عمل إرهابي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92148" target="_blank">📅 17:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92147">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1fc55825.mp4?token=QBksAmw_eFsgt0uXaQZcgrUjIaJ8txcOW4Y75qRpqB4lFvFqVYSw21YlGiLqlRRUQUy4jCmUBu0g5N2XoOFWkHoHyhss9Wy5GS4wXIUjChvNexyXdkj8jC_RVidhEjl_MHGSJN-DYhB1w86A2fsWarkFfRBk2eLuFOTF6tf0_eZ0WYacRTU6FSYLIs8KoOsGNle1sJyasHIDICH-HS4tLh2N63oLFF83E7GswhQewfLKZO042cIkZtxv5H1cpHOdG-CAioVCP5M-BSMEnYaQ7eHVPzxHVPw3aLPuO7IrdlKRjwBpcvZgomWrzYN8M3UaJ5WrXHTkbugOALPiBPFPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1fc55825.mp4?token=QBksAmw_eFsgt0uXaQZcgrUjIaJ8txcOW4Y75qRpqB4lFvFqVYSw21YlGiLqlRRUQUy4jCmUBu0g5N2XoOFWkHoHyhss9Wy5GS4wXIUjChvNexyXdkj8jC_RVidhEjl_MHGSJN-DYhB1w86A2fsWarkFfRBk2eLuFOTF6tf0_eZ0WYacRTU6FSYLIs8KoOsGNle1sJyasHIDICH-HS4tLh2N63oLFF83E7GswhQewfLKZO042cIkZtxv5H1cpHOdG-CAioVCP5M-BSMEnYaQ7eHVPzxHVPw3aLPuO7IrdlKRjwBpcvZgomWrzYN8M3UaJ5WrXHTkbugOALPiBPFPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانب من الاحتفالات في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92147" target="_blank">📅 17:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9qjuXdRLJRq5SyvDqqrOG7S6qprZGoJEa_r2qMO30_y90MZVsRLQY7Jz1YQCujtpB4VckqZxwi8mMIkrK5Uz1ky4eJcT7f-lVI0vNGfXg-EZ8_Rn6fX3Ud_q-B0tbSNy1mgF_nlJr6iGD9Ioe3Lt8D012FZgyF12LvzGaW4HgnzXlZjTibJN-Nre_9S8TlscTYmopXCu2_MlszBvGkrx85iRdsTPwb6-jlq1nnbZ6KrhIvKqorWGWNyV1vhFjQl7ug6_bxI6wYMklW8Oo8SZ6JXHIlfDC7UiAABEa9cjaCv_12lAVKCA55nEcNUPGX0qAv62glQWfaxyQpFgVxDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ii3-RL72pZlgSi6tA-omhNR7Dal-Khx6LpT1sISA6ctGw1B3ELiE7gSSFBE8DPjLOT9GdjZdSVp9OF4jcBULYcgozsr-YaZQZmHTEs1rH04WmaUfjfz4RgzVJogSMigxX04kt1-sU1205mGPQG80_0oTHiHI4VWGeMb4siQGCv5U6hB2718r2MoIz2fgWocFX3zA8yEl3NtwqCiX2fPhXtw78P7Q4btFBBgAWyXnp3-ikoJtJ-jFzpPt24genSDYdzaWeB-m1nJnbGtWMpe55FzQzcopgczj5PTMAdxJXr8KgmwqpWgdog0fF81HzclG-GvOF5oGHXpn9fLRhWQqFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعداد حاشدة تحتفل في العاصمة العراقية بغداد بمناسبة دحر واذلال قوات الاحتلال</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/92145" target="_blank">📅 17:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وختاماً نقول:
منذ أكثر من أربعين يوماً، انخرطت المقاومة الإسلامية من خلال اللجنة الرباعية المُشكلة من الإطار التنسيقي بالاتفاق مع الحكومة العراقية في مفاوضات لبحث عملية تنظيم سلاح المقاومة مقابل تحقيق سيادة العراق الكاملة والشاملة، المتمثلة بانسحاب القوات الأمريكية والناتو وكافة أشكال الوجود العسكري الأجنبي من العراق(أرضا وجوا وبحرا)، مع احتفاظ المقاومة الإسلامية بحقها في الرد المباشر على أي خرق أو انتهاك أمريكي أو صهيوني لسيادة العراق، غير أن رد الحكومة العراقية لم يصلنا حتى هذه الساعة رغم توقيع ورقة الاتفاق رسمياً من اللجنة الرباعية المكلفة من طرف الإطار التنسيقي وكذلك أطراف المقاومة المتمثلة بالفصائل الأربعة.
وبناءً على ذلك، تعلن المقاومة الإسلامية أنها غير ملزمة بأي توقيت أو اتفاق قد تحدث عنه –أو يتحدث عنه- أي طرف حكومي أو سياسي.
إن سلاح المقاومة سيظل أمانة بأيدي مجاهدينا، وكما كان دوماً فأن بوصلته ستبقى موجهة ضد أي عدو يستهدف العراق وشعبه، وفي الوقت ذاته، ستبقى أبوابنا مفتوحة أمام أي حوار يضمن سيادة العراق وعزته والانعتاق من هيمنة أمريكا الشر والجريمة والطغيان.
عاش العراق حرا أبيا سيد نفسه
والسلام عليكم ورحمة الله وبركاته
المقاومة الإسلامية في العراق
30 أيلول 2026</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92144" target="_blank">📅 17:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92142">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">البيان الكامل للمقاومة الاسلامية في العراق
بسم الله الرحمن الرحيم
﴿وَلَقَدْ سَبَقَتْ كَلِمَتُنَا لِعِبَادِنَا الْمُرْسَلِينَ * إِنَّهُمْ لَهُمُ الْمَنصُورُونَ * وَإِنَّ جُندَنَا لَهُمُ الْغَالِبُونَ﴾
حينما احكمت قوات الاحتلال الأمريكي قبضتها على أرض العراق سنة 2003، فاحتلت البلاد وقتلت العباد، لم يكن أمام الأحرار إلا مواجهة من جاء بديلاً عن الطغيان البعثي، فكانت عبوات المقاومة الإسلامية تمزق آليات المحتلين وتحيلها خراباً، وتمطر قواعدهم بالصواريخ فتجعلها ركاماً طيلة مدة بقاء الاحتلال في عراقنا العزيز، فما كان لجيشهم المنكسر إلا الهزيمة عام 2011 بذريعة الاتفاق الأمني مع الحكومة العراقية آنذاك، ليسجل العراقيون بذلك الانتصار الأول على أقوى جيوش العالم؛ جيش الولايات المتحدة الأمريكية وبإسناد قرابة الثلاثين من جيوش حلفائها.
وما لبث العدو الأمريكي أن استوعب صدمة الهزيمة في العراق حتى بدأ بتعزيز مخططاته الخبيثة وتنفيذها في سوريا بعد تحشيد مرتزقة التكفير السعودي في محاولة لتفكيك بيئة المقاومة والممانعة وتضعيفها في المنطقة، فما كان لرجال المقاومة الإسلامية إلا أن هبوا لفرض الاستقرار والأمن وطرد التكفيريين من أرض السيدة زينب (عليها السلام).
وحينما بانت بشائر انهزام جيوش التكفير المدعومة بالمال السعودي، سعت أمريكا الشر إلى نقل المعركة إلى أرض العراق في محاولة خبيثة لاستغلال انشغال رجال المقاومة العراقية في سوريا، فزحفت العصابات الإجرامية إلى المدن العراقية واستباحت حرمها وسبت نساءها، وقتلت أطفالها، فما كان لرجال المقاومة العراقية إلا التوجه لمواجهة المد التكفيري الذي كاد أن يسقط العاصمة بغداد.
وبعد انهيار المنظومة الأمنية والعسكرية العراقية في المحافظات الغربية وتهديد العاصمة بالسقوط، طلبت الحكومة برئاسة السيد نوري المالكي من المقاومة العراقية التصدي لهذا الخطر الذي داهم العراق، فانبرى رجالها بسد الثغرات واستحداث المواقع الدفاعية وإيقاف زحف العدو، بل ومطاردته.
أما بعد صدور الفتوى المباركة، فقد كان من أدوار فصائل المقاومة هو إنجاح الفتوى باستيعاب وتدريب الجزء الأكبر من المتطوعين على مختلف صنوف الأسلحة وتفويجهم إلى سوح الوغى في معارك تحرير المدن العراقية المستباحة وإمساك الأرض بعد تحريرها.
وفي خضم المعارك مع التكفيريين وبعد أن لاحت هزيمتهم في الأفق، فقد تم إعادة تدخل العدو الأمريكي للمشهد العراقي بذريعة الدعم الجوي ضد عصابات التكفير -المدعومة أصلاً أمريكياً- فتمكن الأمريكان مرة أخرى من استعادة تواجدهم العسكري، ولكن هذه المرة مدركين ضرورة تجاوز خطر المقاومة العراقية باستحداث قواعد الاشتباك؛ فأنشأ الاحتلال معسكراته داخل البلاد بما يؤمن له –متوهماً– عدم وصول صواريخ المقاومة أو عبواتها لقواته، إلا أن المقاومة كانت له بالمرصاد وتمكنت من تطوير صواريخها ومسيراتها بما يؤمن تهديد وجود قواته ودك قواعدها، فكانت جولات المنازلة بما يتناسب وقواعد الاشتباك الجديدة في مرحلة الاحتلال الأمريكي الثانية.
وفي غمار الأحداث واستهداف تواجد الاحتلال طيلة المرحلة التي أعقبت هزيمة داعش، ولا سيما في عمليات الإسناد لشعب فلسطين وإيران الإسلام، استهدف طيران الاحتلال الأمريكي المواقع الدفاعية للحشد الشعبي في القائم وعموم المناطق القريبة للحدود العراقية السورية، ومعسكراته الرسمية في أطراف المدن العراقية، واغتيال القادة في بيئتهم المدنية، وفي مقدمتهم الحاج الكبير قاسم سليماني، والحاج أبو مهدي المهندس، واستمر مسلسل الاغتيالات للقادة ومنهم الحاج القائد أبو تقوى السعيدي والحاج القائد أبو باقر الساعدي، ومؤخراً اغتيال القائد الكبير الحاج أبو حسن الفريجي، وسقوط مئات الشهداء والجرحى إثر الاعتداءات الأمريكية على الأرض العراقية.
ولم يكن أمام المقاومة الإسلامية بفصائلها الأربعة إلا مقاومة الاحتلال بشتى صنوف الأسلحة المتاحة طيلة هذه السنوات التسع، وعلى مر مراحل تغيير الرئاسات للحكومات العراقية، كانت المقاومة توجع الاحتلال بضرباتها الذي أخطأ في حسابات قدرة الوصول لقواته وقواعده مرة أخرى، فكان خياره مجبراً هو الخضوع لإرادة المقاومين والخروج من عراق المقدسات مذلولاً، منكسراً، على الرغم من محاولاته لإخفاء هزيمته بتأطيرها بالاتفاقات وغيرها من الأكاذيب.
إن المقاومة العراقية المتمثلة بفصائلها الأربعة وثلة من المجاهدين الأشداء هم من حملوا السلاح بوجه المحتلين، ووضعوا أرواحهم على أكفهم، وتحملوا أعباء هزيمة الاحتلال الأمريكي، فداءً للدين والوطن، لتكون بداية تعزيز السيادة العراقية.
وختاماً نقول:</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92142" target="_blank">📅 17:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92141">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f12290f3e.mp4?token=JNWoavXvmMCcTNSu9Xc83OD9j6hZEAenj2ikyrx7HoOpsbMJy7L9sv8dLwhwdl-UmfVzhXRq3-4_xScOtI7T1QoQcg3hMj5dZn1Wwiu6lT9b6Q0sZQRSE5uPlIlEaYIppBBPKNteyve4s54qEaGb_DIu_pgRaAYO_HiYiPhPC5JXo1sNOWx2XLs11vzHW_qG0ONrD8-ztJI6sjCFAvwJk1lEYexJqpAtqZAYCIWFJT8jWDzIxPWKFwOLNIMrSTn8Y7ZWp3uLmhIH_xJae6DaDKpD9pCRuYY8hqzqrjoQpY-_h1rVA1F19yf-f_QGICdRvV0v2pKLBK6Os5touEi93mM-Y6tjeB7mSFpeIe8bpJRyHg1-1MTuIHXTD13mMXxNlcENA9oUfqqJeJa4BXPy8Zs1GivI-GzQrMwRgtOWVYcCitfZPDoVDbk1AHo6PLl7c70L-BchU1pmskwQtFkA1cxdLqSDXSsLU6E_PtzJ4GjQgjIsMBa2kvVHUiodZ7bhMzL4LCmKB-koWpRTkh9W5fC2k2HsnEYj5tEpspknauApnGVX60JkyogcfERv-u6LQ3NJ8Xk_pQyfBY89yUT_qORx5nzEs3zLcr5BXuxjMR2RJlTs5mvTpgpBK7eAKpneYmWhDGkp42O5Y9CNAkMS8XjIA_a0ntIVNetzwlLzkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f12290f3e.mp4?token=JNWoavXvmMCcTNSu9Xc83OD9j6hZEAenj2ikyrx7HoOpsbMJy7L9sv8dLwhwdl-UmfVzhXRq3-4_xScOtI7T1QoQcg3hMj5dZn1Wwiu6lT9b6Q0sZQRSE5uPlIlEaYIppBBPKNteyve4s54qEaGb_DIu_pgRaAYO_HiYiPhPC5JXo1sNOWx2XLs11vzHW_qG0ONrD8-ztJI6sjCFAvwJk1lEYexJqpAtqZAYCIWFJT8jWDzIxPWKFwOLNIMrSTn8Y7ZWp3uLmhIH_xJae6DaDKpD9pCRuYY8hqzqrjoQpY-_h1rVA1F19yf-f_QGICdRvV0v2pKLBK6Os5touEi93mM-Y6tjeB7mSFpeIe8bpJRyHg1-1MTuIHXTD13mMXxNlcENA9oUfqqJeJa4BXPy8Zs1GivI-GzQrMwRgtOWVYcCitfZPDoVDbk1AHo6PLl7c70L-BchU1pmskwQtFkA1cxdLqSDXSsLU6E_PtzJ4GjQgjIsMBa2kvVHUiodZ7bhMzL4LCmKB-koWpRTkh9W5fC2k2HsnEYj5tEpspknauApnGVX60JkyogcfERv-u6LQ3NJ8Xk_pQyfBY89yUT_qORx5nzEs3zLcr5BXuxjMR2RJlTs5mvTpgpBK7eAKpneYmWhDGkp42O5Y9CNAkMS8XjIA_a0ntIVNetzwlLzkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتهاء كلمة المقاومة الاسلامية</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92141" target="_blank">📅 17:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92140">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcc56e602.mp4?token=MsfwCxAAIVXC4bbVugMZJKgbreRSQc_rf4iGSiPiTzO1R6zm4AbN9_2NprZqzDxXRBPJf0mUTj0S0iFU24MkLq_yv0hX0f4pZv56EyorfxbFX6KYYyHm4bA7UuLP3_qeUZ_r7s69WFO7Yes0JwsQc8iehvOLA51i7ee0EVeR0Wrl0SXik8IOD-VRtlcbythWPd5TMOmUTbtZwFB9gSrOqpJhHDCLlKI0oCryVn3gHqLSEMJ_49H9-_pBgoyWfaS1FeuKbAai07vcrR20u7qoSjEw1ybKZWFwZtVwZ0b4uiSyP7Z6mtbyAg0FqPrHfYSQpSZ0aURxtlHEP6k-pm8vVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcc56e602.mp4?token=MsfwCxAAIVXC4bbVugMZJKgbreRSQc_rf4iGSiPiTzO1R6zm4AbN9_2NprZqzDxXRBPJf0mUTj0S0iFU24MkLq_yv0hX0f4pZv56EyorfxbFX6KYYyHm4bA7UuLP3_qeUZ_r7s69WFO7Yes0JwsQc8iehvOLA51i7ee0EVeR0Wrl0SXik8IOD-VRtlcbythWPd5TMOmUTbtZwFB9gSrOqpJhHDCLlKI0oCryVn3gHqLSEMJ_49H9-_pBgoyWfaS1FeuKbAai07vcrR20u7qoSjEw1ybKZWFwZtVwZ0b4uiSyP7Z6mtbyAg0FqPrHfYSQpSZ0aURxtlHEP6k-pm8vVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد جعفر الحسيني: رد الحكومة العراقية لم يصلنا لهذه الساعة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92140" target="_blank">📅 17:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92139">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92139" target="_blank">📅 17:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92138">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">السيد جعفر الحسيني: انخرطت المقاومة الاسلامية في مفاوضات عملية تنظيم السلاح اي سلاح المقاومة مقابل تحقيق سيادة العراق الكاملة المتمثلة بانسحاب القوات الاميركية والناتو وكافة اشكال وجود عسكري اجنبي برا وجوا وبحرا مع احتفاظ المقاومة الاسلامية في حقها للرد المباشر…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92138" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92137">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">السيد جعفر الحسيني: ان المقاومة العراقية المتمثلة بالفصائل الاربعة هم من حملو السلاح بوجه المحتلين وتحملو اعباء هزيمة الاحتلال الاميركي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92137" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92136">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92136" target="_blank">📅 17:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92135">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">السيد جعفر الحسيني: عادت القوات الأميركية للدخول إلى العراق بحجة محاربة الإرهاب</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92135" target="_blank">📅 17:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92134">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiJbOJTYOzOG9KAPn7pES4EixheFEiDde-eeAUBk0KecjdHehDNGUwvVapr6NBgkKlXTcDLKpB8qDxX9O9tyv3xmCxLUXAs5pZ4T1LIWeYX9kjng287HXcCsZnimGYK06kkXNxjuTI3il5KFDJAkCj1qpCMAMHvJxkYNWobxwr-YWAdX9GHz8IklemOTmCZYyltBnYydTMISs8yArm7kwcwzlqG14FIRk-A-W9uItIWH6b9q88TSU-EX6uwnw6TmfGDA3uLl7wuDFVrTc-i_QoF6nNwGc2GjWnhHjtaIgsEUDkuymQ2QqrL2RL2NSrPzsjCHQH8M4zQVHvAEPzX2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد جعفر الحسيني: بعد صدور فتوى المرجعية كان دور فصائل المقاومة إنجاح الفتوى من خلال تدريب النسبة الأكبر من المتطوعين</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92134" target="_blank">📅 17:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92133">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518dc989ba.mp4?token=MxIQvIlomPIUWnqiJqa6BAcMD2UojcIBSQfSUTMQCmco1NiX6FNebbJgYuhwbIAyJ0mIRrzmymf26y7JzhDBH_CeNqMUuUxcC5hlRtZ91L7zVAKCdojyd5exbUfcrqgtOWogO9ahZrwG8mwmN-pcxGuZESgJ3SyjXVPnm8rGhq3j58JuDrhGgqow0ovcaLv8GTQmVMrmBF1h4pbxpVloGRKb-Nq8k-MrDCb3AeXCnKbc2Y6hLkEdUd3dHpiHsTaDvbCk0u3TsvvnIo-RB3H88WVWj4CjzvzgNVonn99ApHTFQXDX83BJuTWK4njExHsBKsSDk0oXBfZDcsgZ6dxfCQjPldVJhfTi0Qh2wqH4gou6eCS467FgExed_x9YDohWc6368njAX01w-R87iFyL5mBO-gv0_vvUbtBZSf09pvQrfvs4wNyV1VYU6vatTEUNelEgy67I5ePe04vyv2oK3WO6mLirfrTh26O-wuuu9mlmA1bN_31EHviH6CrB_sXmUwDeOG_rB0skzkacDHVId1fBCf2zzsp9uUBkhPZZV90Yy758T1Sa7tLjI4eu2aPyD8jtbp0Dv4Gzjw0lKOo3MR-if1aHaScRBxG8B5UtYkNIF5vlTGPbr7nGxxjlcCdv7ps0yNwjcGBZ-6c5FrsX2J-b0JjDHjaqTMRmu7bRb84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518dc989ba.mp4?token=MxIQvIlomPIUWnqiJqa6BAcMD2UojcIBSQfSUTMQCmco1NiX6FNebbJgYuhwbIAyJ0mIRrzmymf26y7JzhDBH_CeNqMUuUxcC5hlRtZ91L7zVAKCdojyd5exbUfcrqgtOWogO9ahZrwG8mwmN-pcxGuZESgJ3SyjXVPnm8rGhq3j58JuDrhGgqow0ovcaLv8GTQmVMrmBF1h4pbxpVloGRKb-Nq8k-MrDCb3AeXCnKbc2Y6hLkEdUd3dHpiHsTaDvbCk0u3TsvvnIo-RB3H88WVWj4CjzvzgNVonn99ApHTFQXDX83BJuTWK4njExHsBKsSDk0oXBfZDcsgZ6dxfCQjPldVJhfTi0Qh2wqH4gou6eCS467FgExed_x9YDohWc6368njAX01w-R87iFyL5mBO-gv0_vvUbtBZSf09pvQrfvs4wNyV1VYU6vatTEUNelEgy67I5ePe04vyv2oK3WO6mLirfrTh26O-wuuu9mlmA1bN_31EHviH6CrB_sXmUwDeOG_rB0skzkacDHVId1fBCf2zzsp9uUBkhPZZV90Yy758T1Sa7tLjI4eu2aPyD8jtbp0Dv4Gzjw0lKOo3MR-if1aHaScRBxG8B5UtYkNIF5vlTGPbr7nGxxjlcCdv7ps0yNwjcGBZ-6c5FrsX2J-b0JjDHjaqTMRmu7bRb84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد جعفر الحسيني: بعد صدور فتوى المرجعية كان دور فصائل المقاومة إنجاح الفتوى من خلال تدريب النسبة الأكبر من المتطوعين</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92133" target="_blank">📅 17:04 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
