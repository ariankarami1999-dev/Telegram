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
<img src="https://cdn4.telesco.pe/file/KvMRwPuDtpbIO-7p1sCDSzxRBmR0cXQo5tlUFByk0WVBLCxPyft15WxNId2Hy4ZlqV7fp-IcH-9du0EfXk_ecw1e6GKIb3s2K0ICLqzz4iamRC1lWURO6SgizKpTf4vUWhhYMKkKQ20NCEQQ7kFiLxPG6exLxN4odnvlmlxg-Ob0kTW070k1b0PwpSurZWej-gT8E31UHb8ZKRyijobrC9kGcH2ZjZfbbTGpa8tD5qMnN68hhnk8Sn96maUsNiUasZk2bS0x9EDPChXTt--3yC_LEVa3s92UjlEX34r364uVojQTUPU6TxKqTRndFtMpaAbpihaFoaRkhp3sP7wh4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-92087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/naya_foriraq/92087" target="_blank">📅 13:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH4dJ8t5fsHPzKmRfrH3tJ17vp1dcA5FYl05L-cgkY-KUb8DZe3M7NbRxEwfrWbGoJ1eltams0Ojj57EbwTOyrVPaD4udY6YDi5D1ckihEg1YRc0rTyBi0yNugOB4cbgWgApGDLSwNchESmu8qH1Zf5Hvyc1QB4lnda49LBdsmu3hbejKVTmw-S0O0i2gvkGKykjcWgAzrJ8yC8-JKL_djRgDx_paCHYjCLYn3DEQCVDVicn3o96vrSRJ32_lhxXMYxxXVR6ZR-UDMNSj1tkgIj57oEwwQlTjvDGaim70Ik9Mhb_Q57kNFCS96DZMxFUnFAhBuye2VhUrZupSoZA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/naya_foriraq/92086" target="_blank">📅 13:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بدأ نشرة موحدة على القنوات الفضائية العراقية احتفالا بمناسبة دحر قوات الاحتلال الامريكي</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/naya_foriraq/92085" target="_blank">📅 12:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجار عنيف يهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/naya_foriraq/92084" target="_blank">📅 12:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇸🇾
🔻
بيان صادر عن حزب الله حول ادعاءات عصابات الجولاني:
تنفي العلاقات الإعلامية في حزب الله بشكل قاطع أي علاقة أو ارتباط لحزب الله بالخلية المزعومة التي أعلنت وزارة الداخلية السورية عن توقيفها في منطقة حوض اليرموك في درعا، ويؤكد مجددًا أنه ليس لديه أي تواجد في الأراضي السورية، ولا علاقة له بأي نشاط أمني أو عسكري فيها.
كما تؤكد حرص حزب الله الدائم على أمن سوريا واستقرارها وسلامة شعبها، وتدعو الجهات الرسمية السورية إلى التنبه للمحاولات التي تهدف إلى الزج باسم حزب الله بغية إثارة التوتر وزرع الفتنة بين لبنان وسوريا، والتحقق من خلفيات هذه الادعاءات والجهات التي تقف وراءها، والبحث عن المستفيد الحقيقي من تأجيج التوتر بين البلدين، وهو العدو الإسرائيلي الذي يوغل في  اعتداءاته على سوريا ولبنان، ويسعى إلى زعزعة أمن المنطقة واستقرارها.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/naya_foriraq/92083" target="_blank">📅 12:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp0KSGv17G2JKIldMd_JVwxFqPcMwZ0mzureZYNomAXwjsqGZSwFzybxNhgxn0aCtgX-eyoSVlcJk0oOAh-hi1Nj8YzOGyhgsiHuZ6mg6U9cV37ed0oWaFKYOxCp_UlUOXxIYA9IsGlAAfLfv7GC3OFhOOa4BMSjI8A_8ZsfFKVb5L948WJnfEvxQZ7hoaxSlUNbpX_gF_KbJVfk_pfJNG6C0wWbadDRibyfSBhaS_ble_ffmXQYUDFMgCTCVp8-gj5zAn1KV0oks-dwOWSsa9oS_KX-yY3H4CoWljMHjfloSDAIUai6KwzJbRAc34F7YUyn_e55-nJNccgoyPsQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
السيد مقتدى الصدر:
نعلن استقلال العراق وانتهاء حقبة التواجد الإمريكي والتحالف الدولي بصورة نهائية ونعلن حلّ لواء اليوم الموعود فوراً، وتحويل جيش الإمام إلى مؤسسة أنصار الإمام المهدي عجل الله تعالى فرجه الشريف ونطالب الجيش الإمريكي بتعويضات عن كل الأضرار التي حدثت بسبب احتلاله للأراضي العراقية، فعلى الجميع تقديم شكاوى قانونية بذلك.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/naya_foriraq/92082" target="_blank">📅 12:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=RszY0XAWsZOaw4bU4bsLauiT9-91ia-kdp8ZS4W_GyFgoW4o7iR_Jn3P7tf6V4157qRp5RvPPmKLMiAp2x-aI4RVnLZttsXHpKOkmCZQMp3lGFBq0I90e_N13LryjSnWsdHxVOVzlSkqJpRCU6fJeLLiEUYhQrMWibcB6_mdoSzzoJZk-DYx1CiWU2-8mzG67H1SRDcsL_mQEFr5U_k-B0Ha4pve5e4y6aDzRISZN7sh6J2pHat32RRUnEpDR0VCtB810VmnfamVtHaGAWjzp0o_n8fvZS4oFrL5BeIAxQiu8UTQQareWvhvPtYabW9Rl49YHGtTcimAfRTSxfudSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=RszY0XAWsZOaw4bU4bsLauiT9-91ia-kdp8ZS4W_GyFgoW4o7iR_Jn3P7tf6V4157qRp5RvPPmKLMiAp2x-aI4RVnLZttsXHpKOkmCZQMp3lGFBq0I90e_N13LryjSnWsdHxVOVzlSkqJpRCU6fJeLLiEUYhQrMWibcB6_mdoSzzoJZk-DYx1CiWU2-8mzG67H1SRDcsL_mQEFr5U_k-B0Ha4pve5e4y6aDzRISZN7sh6J2pHat32RRUnEpDR0VCtB810VmnfamVtHaGAWjzp0o_n8fvZS4oFrL5BeIAxQiu8UTQQareWvhvPtYabW9Rl49YHGtTcimAfRTSxfudSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وَيَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِينَ</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/naya_foriraq/92081" target="_blank">📅 12:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
🇮🇶
البنتاغون: غادرنا العراق.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/naya_foriraq/92080" target="_blank">📅 12:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇱
مسؤول إسرائيلي كبير: كان هناك طاقم إضافي من الطيارين على متن الطائرة كجزء من تدريب، وقد سيطروا على الوضع. هذا هو الحظ الذي رافق هذه الرحلة - وإلا لكنا في حادثة مماثلة لما حدث في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/92079" target="_blank">📅 12:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇱
إعلام العدو: صرخ مساعد الطيار "الله أكبر" وبدأ في طعن الطيار الرئيسي عدة مرات. تمكن طاقم الطائرة والركاب من اقتحام باب قمرة القيادة والسيطرة على الإرهابي.</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/92078" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/naya_foriraq/92077" target="_blank">📅 12:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">إعلام العدو: الطيار من أصل عماني.</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/92076" target="_blank">📅 12:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">إعلام العدو: الطيار كان إرهابيًا حاول اختطاف الطائرة التي كان على متنها إسرائيليون.</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/92075" target="_blank">📅 12:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مقتل اعداد من عصابات الجيش السعودي بكمين محكم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/naya_foriraq/92074" target="_blank">📅 12:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إعلام العدو: أحد الطيارين طعن الطيار الآخر. اندلعت مشاجرة. الطيار الذي طعن يحاول اختطاف الطائرة - ربما لتحطيمها على الأرض. اندلعت معركة داخل الطائرة، وفي أثناء ذلك، انخفضت الطائرة 4000 متر.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/92073" target="_blank">📅 12:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقتل اعداد من عصابات الجيش السعودي بكمين محكم للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/naya_foriraq/92072" target="_blank">📅 12:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فلاي دبي: الرحلة 1073 المتجهة من دبي إلى تل أبيب تعرضت لواقعة أثناء تحليقها.</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/92071" target="_blank">📅 12:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مشاهد تظهر لحظات من رعب الركاب داخل الطائرة التي كانت في طريقها من دبي إلى تل أبيب وغيرت مسارها نحو السعودية.</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/92070" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cb874bb7.mp4?token=DXVJgpSZnEaPME6DlnONisNScDREY2hVBOcCQDiDesNksuDwp8Zwnvn6JWXKoARg5YtvT2X9L7TB4iD3zgTvVWKZIzDrBX5rYTOTLIIT6xb6Dcfsm8lKGbCEi7yeIxiJKjqIneiH25uS1q8-JCLI2HHwWtSzipzHolIoCBvo1dhaKtwbA5gtuWbfmFekvmnOjkO4vlXIgwXGIBMNCuozCYsYyAyUOJt1D7dA918M9grAWfF-45s9Mx2OMHjXvLiGpncXnePtuiAOMhoNqk0sTeMseitwxEb2AUgzU3BCAs7qnvVeBbAgBqQlTXRKv8G2ngvByegvFftK_PlwDXmv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cb874bb7.mp4?token=DXVJgpSZnEaPME6DlnONisNScDREY2hVBOcCQDiDesNksuDwp8Zwnvn6JWXKoARg5YtvT2X9L7TB4iD3zgTvVWKZIzDrBX5rYTOTLIIT6xb6Dcfsm8lKGbCEi7yeIxiJKjqIneiH25uS1q8-JCLI2HHwWtSzipzHolIoCBvo1dhaKtwbA5gtuWbfmFekvmnOjkO4vlXIgwXGIBMNCuozCYsYyAyUOJt1D7dA918M9grAWfF-45s9Mx2OMHjXvLiGpncXnePtuiAOMhoNqk0sTeMseitwxEb2AUgzU3BCAs7qnvVeBbAgBqQlTXRKv8G2ngvByegvFftK_PlwDXmv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أولى المشاهد من داخل الطائرة التي كانت متجهة من دبي إلى تل أبيب وغيرت إتجاهها نحو السعودية عقب حصول إشتباك داخلها.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/92069" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏يقول أحد ركاب رحلة فلاي دبي من دبي إلى تل أبيب:  ‏"سمعنا صراخاً ورأينا دماءً. طُعن الطيار. كانت هناك لحظات ظننا فيها أننا لن ننجو."</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/92068" target="_blank">📅 11:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCbP7TLE66QNTxAoHtsgz1oNdOVdG3K4Okfs1PQz6jg1LJ0iYWUlUBHxP2QTQ_40KzC6nkfNIYXIl2cDbVnu1ycHwEzbLXbLhjR8xeqNrC31qAM9BRk5CLgjEunVAiWdShNX4Y0KPBs3AJwg811_HchRCsltaBEYbxyNVocZwnCnC6KY-SLj1AKNlF-twU5kdw8lxuRuGJ-hQIKQ5zz__WgqKkkwKvlFEAUiiOH1QcOIGSd90arJ6UrWVwjjctwkTv1xT3UmsCaZiSHQ6zNZq8Y1Os6sDB5hHuK-GNFHCqK4p0VmUU7fsRXu5QFJweGpJoevdvVwpjhnJzuLOqrmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏يقول أحد ركاب رحلة فلاي دبي من دبي إلى تل أبيب:  ‏"سمعنا صراخاً ورأينا دماءً. طُعن الطيار. كانت هناك لحظات ظننا فيها أننا لن ننجو."</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/92067" target="_blank">📅 11:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
مايسمى بالتحالف الدولي في العراق:
لم يعد هناك أي مبرر لوجود الجماعات المسلحة في ظل انسحابنا.</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/92066" target="_blank">📅 11:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
لا سلاح خارج مظلة القانون ومؤسسات الدولة وفقا للدستور وما تريده المرجعية وما يطلبه الشعب.
لقد انتهت المهمة بالانتصار، ومسؤولية حماية هذا الانتصار تقع اليوم على عاتقنا جميعًا.
بدأت مرحلة جديدة عنوانها سيادة العراق، وقوة مؤسساته، وجاهزية قواته، ووحدة قراره، والشراكات المتوازنة مع أصدقائه.
انتقال مهام العمليات المشتركة إلى مكتب القائد العام للقوات المسلحة صيغةً مؤسسيةً لإدارة هذا الجهد تحت سلطة الدولة وقيادتها العليا.</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/92065" target="_blank">📅 11:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
🇮🇶
‏البنتاغون:  الولايات المتحدة وشركاؤنا بالتحالف يختتمون رسمياً عملية "العزم الصلب" في العراق.  ‏سنواصل تقديم تدريب ودعم استخباراتي لشركائنا في العراق.  الانسحاب المنظم لقوات ومعدات التحالف من قاعدة أربيل الجوية يمثل ختام المهمة العسكرية.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/92064" target="_blank">📅 11:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">إعلام العدو: رئيس أركان الجيش الإسرائيلي ألغى زيارته إلى الولايات المتحدة في ظل تصاعد حالة التأهب.</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/92063" target="_blank">📅 11:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">إعلام العدو: في السعودية، أفيد بأن أحد الطيارين حاول إسقاط الطائرة وإلحاق الانتحار بالركاب والطيار الآخر منع ذلك.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/92062" target="_blank">📅 11:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏يقول أحد ركاب رحلة فلاي دبي من دبي إلى تل أبيب:  ‏"سمعنا صراخاً ورأينا دماءً. طُعن الطيار. كانت هناك لحظات ظننا فيها أننا لن ننجو."</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/92061" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
إعلام العدو: الشكوك تشير إلى أن أحد الطيارين حاول الانتحار، حيث قام بالطائرة بالهبوط السريع من ارتفاع 30 ألف قدم بسرعة تقارب سرعة الصوت، حتى وصل إلى ارتفاع 15 ألف قدم في فترة زمنية قصيرة. الطيار الآخر منع ذلك من خلال مواجهته له.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/naya_foriraq/92060" target="_blank">📅 11:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/92059" target="_blank">📅 11:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19cb92d392.mp4?token=AQzy0pbFRuc8WjiTeWzZTCmdqoApnVJ_mE1_QTavkpZ9sQXP7iAmBZHsXighfKPvkkazJxkDUmmdvrXHnRkloiC_gNeEjEp9RNLc8y_wPjkx8u9AwNymPN61RGca8d36qGJe6oSvQ4c29-Tnp1oiIt7944mWtvrNv01md-XykNYw7AZejmd_TmduMnKoqeITybdgmSpzZreCrIEbC7V_LFLQngO1DzomX4BkR97mC8LcBPi1shZ3DP-SLtsBQOYcdCFuFadOfhmV9EaXEVAgeIaesfsmED8-q7VrWkl0t8b2lrnSQ5vaMo61GmjMXnDVPAIL-lSCyCzR-i__7jBeb3xhwr9qzUfz8dYSSecwErHfYwClhTroTLUVgRnC8rCoAkihNkDyzQEswG6zYfoh2vPxM2XIO8hLQ0JrSD2rBE-odSlQMd6o9wfpgXUKZqARdZQOEAgNBmpAyu6FkQDyOieA-Uy8YMIoY4xJKlNAWkNPzMqv3ojRPNj9BEZ2gUpkePlpKHgeVMixj6iR8jK8JxK2xjFSN6omjXVMCxhs2NAJ2LI0SS6jari4sUPM5U1bBC4eXkhk07XRahEe6XJczxaWB5zIvKl0VyGyaK-yHrOocntmpZYjSo1V33CxZmnMzknIMytv343U5qEm3gnPbJH8411gdBwXqAjHB-A7Rxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19cb92d392.mp4?token=AQzy0pbFRuc8WjiTeWzZTCmdqoApnVJ_mE1_QTavkpZ9sQXP7iAmBZHsXighfKPvkkazJxkDUmmdvrXHnRkloiC_gNeEjEp9RNLc8y_wPjkx8u9AwNymPN61RGca8d36qGJe6oSvQ4c29-Tnp1oiIt7944mWtvrNv01md-XykNYw7AZejmd_TmduMnKoqeITybdgmSpzZreCrIEbC7V_LFLQngO1DzomX4BkR97mC8LcBPi1shZ3DP-SLtsBQOYcdCFuFadOfhmV9EaXEVAgeIaesfsmED8-q7VrWkl0t8b2lrnSQ5vaMo61GmjMXnDVPAIL-lSCyCzR-i__7jBeb3xhwr9qzUfz8dYSSecwErHfYwClhTroTLUVgRnC8rCoAkihNkDyzQEswG6zYfoh2vPxM2XIO8hLQ0JrSD2rBE-odSlQMd6o9wfpgXUKZqARdZQOEAgNBmpAyu6FkQDyOieA-Uy8YMIoY4xJKlNAWkNPzMqv3ojRPNj9BEZ2gUpkePlpKHgeVMixj6iR8jK8JxK2xjFSN6omjXVMCxhs2NAJ2LI0SS6jari4sUPM5U1bBC4eXkhk07XRahEe6XJczxaWB5zIvKl0VyGyaK-yHrOocntmpZYjSo1V33CxZmnMzknIMytv343U5qEm3gnPbJH8411gdBwXqAjHB-A7Rxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
موكب رئيس البرلمان العراقي يتسبب بقطع السير والحركة داخل المنطقة الخضراء وسط العاصمة العراقية بغداد ؛ وحالة اصطدام لثلاث سيارات نتيجة للإغلاق  . في الوقت غادر العراق وشوارعهٌ عمليات الإغلاق منذ وقت طويل !</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/92058" target="_blank">📅 10:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏مكتب نتنياهو: الحادث الذي تعرضت له طائرة فلاي دبي ليس عملية اختطاف.</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/92057" target="_blank">📅 10:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
مشاهد من القاعدة الأمريكية في محافظة أربيل شمالي العراق، حيث تظهر إستمرار عملية الإنسحاب المذل من خلال النقل الجوي.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/92056" target="_blank">📅 10:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">إعلام العدو: قاتل الطياران بعضهم البعض أثناء الطيران، ونتيجة لذلك، تم رفع حالة التأهب القصوى في جميع أنحاء منطقة الشرق الأوسط.
😆</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/92055" target="_blank">📅 10:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">إعلام العدو: قاتل الطياران بعضهم البعض أثناء الطيران، ونتيجة لذلك، تم رفع حالة التأهب القصوى في جميع أنحاء منطقة الشرق الأوسط.
😆</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92054" target="_blank">📅 10:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار أبها الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92053" target="_blank">📅 10:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">إعلام العدو: التقدير الحالي في إسرائيل الآن هو أنه من الممكن أن لا يتعلق الأمر بحادث أمني، بل بحادث استثنائي آخر وقع على متن الطائرة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92052" target="_blank">📅 10:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طائرة "فلاي دبي" التي كانت متجهة من دبي إلى إسرائيل تهبط في مطار تبوك بالسعودية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92051" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">إعلام العدو: التقدير الحالي في إسرائيل هو أن الحادث يتعلق بنوع من العنف، وهو أمر غير اعتيادي، ولكنه ليس اختطافًا.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/92050" target="_blank">📅 10:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الطائرة ظهرت مرة أخرى في تطبيق تتبع الطائرات.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92049" target="_blank">📅 10:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تم تعليق عمليات الإقلاع في مطار بن غوريون.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92048" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">إعلام العدو: من المتوقع أن تهبط الطائرة في السعودية بعد حوالي 10 دقائق، وبعد ذلك سيتم الحصول على صورة أوضح للوضع. في أوساط الأجهزة الأمنية، هناك من يرى أنه من غير المرجح أن تكون الحادثة عملية خطف مؤكدة.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92047" target="_blank">📅 10:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">إعلام العدو: الطيارون لم يتواصلوا مع أبراج المراقبة - سواء في إسرائيل أو في الأردن.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92046" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">إعلام العدو: لم تتلقَ الطائرة أي اتصال منذ بداية الحادث. يبدو أن هذا الحادث خطير للغاية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/92045" target="_blank">📅 10:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">إعلام العدو: في إسرائيل، يُنظر إلى الرحلة التي تم تحويل مسارها على أنها حادثة اختطاف. بدأت أجهزة الأمن في إنشاء نقاط تفتيش.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/92044" target="_blank">📅 10:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إعلام العدو: الطائرة لم تعد تظهر في تطبيق تتبع الطيران "Flightradar".</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/92043" target="_blank">📅 10:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">إعلام العدو: رئيس الوزراء ووزير الدفاع يجريان مشاورات عاجلة مع كبار المسؤولين في جهاز الأمن.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/92042" target="_blank">📅 10:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">إعلام العدو ينشر ادعية بعد خشية من عملية إختطاف طائرة قادمة من دبي إلى تل أبيب على متنها أكثر من 100 إسرائيلي.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/92041" target="_blank">📅 09:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">إعلام العدو: تغير مسار الطائرة وعادت في اتجاه إسرائيل، ولكنها لا تزال داخل الأجواء السعودية.  لا يوجد حاليًا أي اتصال بالطائرة، وهي غير مصرح لها بالهبوط في إسرائيل.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/92040" target="_blank">📅 09:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">إعلام العدو: خطر وقوع حادث أمني: تم إطلاق طائرات تابعة لسلاح الجو لاعتراض طائرة ركاب أقلعت من دبي متجهة إلى تل أبيب.</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/92039" target="_blank">📅 09:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">إعلام العدو: أرسلت الطائرة إشارات استغاثة، ولم يتمكن أحد من التواصل معها منذ ذلك الحين.  يُقدر عدد الإسرائيليين الذين على متن رحلة شركة "فلاي دبي" بحوالي 100 شخص.</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/92038" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
إعلام العدو: تم تحويل مسار رحلة قادمة من أبو ظبي ومتجهة إلى تل أبيب إلى السعودية بسبب مخاوف من اختطاف الطائرة.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/92037" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇦🇪
🇮🇱
طائرة بوينج 737 تابعة لشركة فلاي دبي، وهي رحلة تجارية متجهة من دبي إلى تل أبيب، تقوم الآن بالعودة إلى دبي بعد أن أرسلت لفترة وجيزة رمز الطوارئ 7700، ثم رمز 7500 الذي يشير إلى محاولة اختطاف.</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/92036" target="_blank">📅 09:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLvgitYY_IyIXCgtjMbKFLN9PnjU7gA55rpvI1nrRp1BUjl7phOyWnHsUAN2vYXJQRHRjKC0g-sROW1cIEEXtDAtTlNejmLyFCPwDzSkADLiAdpQcMVhwI8P1c-GWozVjytsjvzD-T1Qd1rsmDWSMqwSjVdTzSIPGr1hr8QGFUYg22FBSIkN01x1Xa3I_lGmUWzZtgjQI5DMHlpdKHtxGPl9sQEy-gwBkWULPZxUtxLnRW7NCZtpXWmtW24aQsWyLIaFI0HLrlImrFRU7OM27g9C1C1nAPTR6wj6TFQF3gFHcHQwvtWrMm5yHXcV3A5UEazwKQOciajt5T3siWckIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
🇮🇱
طائرة بوينج 737 تابعة لشركة فلاي دبي، وهي رحلة تجارية متجهة من دبي إلى تل أبيب، تقوم الآن بالعودة إلى دبي بعد أن أرسلت لفترة وجيزة رمز الطوارئ 7700، ثم رمز 7500 الذي يشير إلى محاولة اختطاف.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/92035" target="_blank">📅 09:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
رويترز:
إيران تسلمت الرد الأمريكي على مقترح الأيام السبعة وستناقشه اليوم.
الخلاف الرئيسي بين أمريكا وإيران يتعلق بترتيب الخطوات وليس بعناصر خطة الأيام السبعة.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/92034" target="_blank">📅 09:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d7e7391b.mp4?token=Iwzw67j3PoqZVpswBQRw6BZtJzoFQ2EUh3vgHsUmKiqhcXnQYpGV-Y6jrdGrHrxPkTnjANmrDoEDFZTCtnWqralufg8P5NbfxEeFSeV3UhJxNDnZsCelHKtoHMh5BdBZK6xYJeB5hP2aVyGJWevs8JC6tj1Tsrrn3bCjYteBGRsnr5lsM81R_K0SFc9dsTE05uVpZ8EtGmIck4MaY4j9pXss6ssHol-u2M7xSYoL69x_phEzuELhdSFytq2htXsISsfd8Q2_ChnEj1xKPEQQ9XFqn2q9ctbcGUJeVxLUdIxY0alPKlKu6oZBhUVwwvshPDeo5xjABgBsZWVDHm8T9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d7e7391b.mp4?token=Iwzw67j3PoqZVpswBQRw6BZtJzoFQ2EUh3vgHsUmKiqhcXnQYpGV-Y6jrdGrHrxPkTnjANmrDoEDFZTCtnWqralufg8P5NbfxEeFSeV3UhJxNDnZsCelHKtoHMh5BdBZK6xYJeB5hP2aVyGJWevs8JC6tj1Tsrrn3bCjYteBGRsnr5lsM81R_K0SFc9dsTE05uVpZ8EtGmIck4MaY4j9pXss6ssHol-u2M7xSYoL69x_phEzuELhdSFytq2htXsISsfd8Q2_ChnEj1xKPEQQ9XFqn2q9ctbcGUJeVxLUdIxY0alPKlKu6oZBhUVwwvshPDeo5xjABgBsZWVDHm8T9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
العضو في مجمع تشخيص مصلحة النظام الإيراني "علي آقامحمدي":
مجموعات مسلحة مدربة في الإمارات وإسرائيل دخلت البلاد، يجب على المواطنين في الأحياء السكنية أن يكونوا حذرين وأن يبلغوا عن أي شيء مريب.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/92033" target="_blank">📅 09:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية بقوة 3.5 ريختر في محافظة السليمانية، عند الحدود العراقية الإيرانية.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/92032" target="_blank">📅 09:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e265027d.mp4?token=NUQ9RpEnTBCWhp9SEnMDcbWtjaFWCHzgXKzxZGqbYFzHrqgjgAmxunr2emzUcSuVkarY9HUvBQdm-SmdcWLdA_KIIkMyFlVNZVjWEk6FUuUHxmrXQb_wYCx64-LUuhxcMs8aOaimYojCLQFwErZxaJKlwgbylr5hnp8S_ilEW95fF3cBu3BrqsNz4IEn6tqjJZjAgWnNhPcWczYPcrnF8Mh6sLh7kabILZF5Pt_Q9IgFG_kARilvB7PCpjTfMmTTvoeUMLUtyQqHIGZGLuY13iA52twv39fw77RerNtEDjvIL3OVwfeOO8kilom1IEnreD7KsPq-I1W7Ss-_Tl-ImTnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e265027d.mp4?token=NUQ9RpEnTBCWhp9SEnMDcbWtjaFWCHzgXKzxZGqbYFzHrqgjgAmxunr2emzUcSuVkarY9HUvBQdm-SmdcWLdA_KIIkMyFlVNZVjWEk6FUuUHxmrXQb_wYCx64-LUuhxcMs8aOaimYojCLQFwErZxaJKlwgbylr5hnp8S_ilEW95fF3cBu3BrqsNz4IEn6tqjJZjAgWnNhPcWczYPcrnF8Mh6sLh7kabILZF5Pt_Q9IgFG_kARilvB7PCpjTfMmTTvoeUMLUtyQqHIGZGLuY13iA52twv39fw77RerNtEDjvIL3OVwfeOO8kilom1IEnreD7KsPq-I1W7Ss-_Tl-ImTnPp-dggRC1GV0bFp8T6RCpjhNXDoFGYB0XB_KcoMTXTLREjAPn0isgxoeU2PUFRZvhucNGRaLDrZoK0WzaSGPcC9rM-0kdO2Lr0_vyqWBzC9Nw5AivU-Gv6S-YZgSmLQfQ8oVT78qcnIEu1JjuwEeevP1XYocOcuZvYuUS3pwzdRjTmA9y831sba996YCvTe8waeqqCS3UxVCVygB7RMaqQcXi7_qh6GzKE2xHP70COTCXiy360GpDqU6KgGKoYpvX7yDASSV5Q02nOTu1hmlJJHFSWfBZ6NZpegTpdDzbZV3s0UajRY1kJu4v3IjpP9v_tfdye8hl6iUqPOQ_WaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد من القاعدة الأمريكية في محافظة أربيل شمالي العراق، حيث تظهر إستمرار عملية الإنسحاب المذل من خلال النقل الجوي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92031" target="_blank">📅 08:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
اعلام اجنبي نقلاً عن مسؤول في البنتاغون:
الولايات المتحدة بصدد إنهاء عملياتها العسكرية الرسمية في العراق، عدد من عناصر مشاة البحرية سيبقون لحماية بعثاتنا الدبلوماسية ويذكر ان واشنطن ستحتفظ بقدرات استخباراتية واستطلاعية يمكن استخدامها داخل العراق.تم سحب بطارية صواريخ باتريوت للدفاع الجوي كانت متمركزة في محيط أربيل.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92030" target="_blank">📅 04:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8859995348.mp4?token=YmeMVMA9LQF4HuJ5fuxe8WxW2cix4V0NTYRCCHtXBEPDCTL_Oea8Hkxnjk_8MWaFpLY6OcF_wCWpuMAe0a6DPB6R0XXBx8_gXgJUyBaaw3-D-Li4MwXbESZwkFK77kB3YrqkyO6QMrRVptsgzaa8r2332JY477V0818FaHQJqPRkhImvx0lJMkdMbKrsPanjt7lkGGyyE_k4Ww6PkMinyt49Yz-AsKznj3EAVZHFupu9KyjG7tcs2V20WHYLM1eQXjKXeBSRZgISIIJpVG7GhVzkF_uVQ5gut6yA_z1jUXAotVdcmCNrt4ZTNEkd9f6rv6U8PvAj_7FtKS3xmhaMq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8859995348.mp4?token=YmeMVMA9LQF4HuJ5fuxe8WxW2cix4V0NTYRCCHtXBEPDCTL_Oea8Hkxnjk_8MWaFpLY6OcF_wCWpuMAe0a6DPB6R0XXBx8_gXgJUyBaaw3-D-Li4MwXbESZwkFK77kB3YrqkyO6QMrRVptsgzaa8r2332JY477V0818FaHQJqPRkhImvx0lJMkdMbKrsPanjt7lkGGyyE_k4Ww6PkMinyt49Yz-AsKznj3EAVZHFupu9KyjG7tcs2V20WHYLM1eQXjKXeBSRZgISIIJpVG7GhVzkF_uVQ5gut6yA_z1jUXAotVdcmCNrt4ZTNEkd9f6rv6U8PvAj_7FtKS3xmhaMq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لاجئ عراقي في كندا يشكو من ارتفاع أسعار الوقود والمواد الغذائية، محمّلًا سياسات ترامب مسؤولية ارتفاع تكاليف المعيشة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92029" target="_blank">📅 04:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇮🇷
اعلام اجنبي:
‏لم تحرز المحادثات التي توسطت فيها قطر بين الولايات المتحدة وإيران تقدماً يذكر، حيث رفض كلا الجانبين تقديم تنازلات وتزايدت المخاوف من تجدد القتال.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92028" target="_blank">📅 02:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1293457b8.mp4?token=KTy7OxTiHCAKcZ7KSFAyO2sNwvEPuW2OVLhsE3JF7B4ooS0SKF2SIYozelncwmdFlFEz4m0cYvD4Fn94vfGRcijeojk29A_Z9Z5tO11U2qsikOz-JtL_fxOLE072SvbIkER_voKiAz0GJIBZuch4v7PWwRbJL-G2bGsqI-LrqXgJ4AozU4iANvtS3xuuJvApcg4hXKFrKphRz0ZP1lYFB2D1qx6ueJAYDxxVDL4x3NUHGxxTDp5r33f6pxwq-gxBXCcknIyxe74jf-yoqfRx5OkXu7bhscrogHhtcoYXeRlzyDV0BozahbD1ASSsWkCJ53qcLE1VIRtgoBNcolzhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1293457b8.mp4?token=KTy7OxTiHCAKcZ7KSFAyO2sNwvEPuW2OVLhsE3JF7B4ooS0SKF2SIYozelncwmdFlFEz4m0cYvD4Fn94vfGRcijeojk29A_Z9Z5tO11U2qsikOz-JtL_fxOLE072SvbIkER_voKiAz0GJIBZuch4v7PWwRbJL-G2bGsqI-LrqXgJ4AozU4iANvtS3xuuJvApcg4hXKFrKphRz0ZP1lYFB2D1qx6ueJAYDxxVDL4x3NUHGxxTDp5r33f6pxwq-gxBXCcknIyxe74jf-yoqfRx5OkXu7bhscrogHhtcoYXeRlzyDV0BozahbD1ASSsWkCJ53qcLE1VIRtgoBNcolzhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تصعيد خطير في التون كوبري ودخول اشخاص مسلحين من اربيل شمالي العراق قامو بغلق الطريق وسط تفرج القوات الأمنية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92027" target="_blank">📅 01:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ازدياد حدة احتجاجات حزب البارتي في محافظة كركوك وسط رشق بالحجارة من قبل المحتجين.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92026" target="_blank">📅 01:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983ce94215.mp4?token=WNiv_OIXurP41d4b_2CnkqGP_kxH7CwwSaqPXXFRbzadzPifEP2N1ndV8rpBzgrdfCrcINrgY00tLJ3bBVjtLMQqg1O7yG4oGxYxHMvxti92GADVmUeecOPWpmwZ1cbObZHpSySnqY_lT3ioF0YGkwq9dZqk8YhYVeLXIq3t18i25zhypkj7GHAyrzmuGKD2UPVEERllrgh6_jhWqBZQeXbuDY0lKKZfddj2Tv_RjHNIleTy1GyKW1Olrji_AMsLupuxCDkM2TEeLu3M-wsOw19UkvjDTnnwoYJCRKWZUeX_NmfR2ClIEjhDMxPRN1i_6olYthZwFyek-LziOsw0PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983ce94215.mp4?token=WNiv_OIXurP41d4b_2CnkqGP_kxH7CwwSaqPXXFRbzadzPifEP2N1ndV8rpBzgrdfCrcINrgY00tLJ3bBVjtLMQqg1O7yG4oGxYxHMvxti92GADVmUeecOPWpmwZ1cbObZHpSySnqY_lT3ioF0YGkwq9dZqk8YhYVeLXIq3t18i25zhypkj7GHAyrzmuGKD2UPVEERllrgh6_jhWqBZQeXbuDY0lKKZfddj2Tv_RjHNIleTy1GyKW1Olrji_AMsLupuxCDkM2TEeLu3M-wsOw19UkvjDTnnwoYJCRKWZUeX_NmfR2ClIEjhDMxPRN1i_6olYthZwFyek-LziOsw0PTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار غلق المحتجين للشوارع في محافظة كركوك شمالي العراق وسط تعزيزات عسكرية تتجه نحو المحافظة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92025" target="_blank">📅 00:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇸🇦
الاعلام الرسمي السعودي: تم إبلاغ منتخب عُمان بالتأهل في أرضية الملعب بشكل خاطئ، ‏منتخبا العراق وعمان متعادلين بكل شي وسيتم اللجوء لقرعة لحسم المتأهل.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92024" target="_blank">📅 00:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998af4ba9e.mp4?token=aB4RVE-2L3AR0_TXfu5MazXgO3OjsxVhsPmDyVEceWAW0C8J7-O-RwcTYHtSqTiqSPp0H4j2GqRiZ3Mc2zGjMzN5sQKmWqJrlL6Lk63q4v3znRx4eunSVNFbDQ5sjAEVOXNYDZcmhp7_ov3UwQFlzN9Vgljp3TAtEEOrAgtlK8sU1ZMyrsGyblStMDM0CORJm7m1-5X8VExQL2ic2VO34wwo88kPXZ1vAVJJ0cxmnQxKr_Llq5qtkQCQ1EpsX5Xmn8YsAU_KWK6ubjFgRJQU447MeTrK62vvVTpY_aifdCHXVslnUyh-AXuPcwgOlEu4jTYMYmuzVZ1S_4UQRKh9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998af4ba9e.mp4?token=aB4RVE-2L3AR0_TXfu5MazXgO3OjsxVhsPmDyVEceWAW0C8J7-O-RwcTYHtSqTiqSPp0H4j2GqRiZ3Mc2zGjMzN5sQKmWqJrlL6Lk63q4v3znRx4eunSVNFbDQ5sjAEVOXNYDZcmhp7_ov3UwQFlzN9Vgljp3TAtEEOrAgtlK8sU1ZMyrsGyblStMDM0CORJm7m1-5X8VExQL2ic2VO34wwo88kPXZ1vAVJJ0cxmnQxKr_Llq5qtkQCQ1EpsX5Xmn8YsAU_KWK6ubjFgRJQU447MeTrK62vvVTpY_aifdCHXVslnUyh-AXuPcwgOlEu4jTYMYmuzVZ1S_4UQRKh9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
البرزاني يدفع بانصاره في محافظة كركوك لقطع الشوارع وتخريب الممتلكات العامة احتجاجا على استشهاد مدنيين اثنين اثناء عملية التون كوبري على ايدي جهاز مكافحة الارهاب حسب وصفهم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/92023" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHcZ-_HrwXajS1CCmK8-LOT-JFy-XlWAVkFUFOLhKZ2RsBc70VlYCHFEdmgwweFiDTeLRWywR55yuCHqMob6I6aynp2Ge_MTdZPUc_EjnZPmT9w5h-KKmVcRbM-SrRxFoa5HXzIuIMoTZjGyTxNta2zfM6EaVVc8CrmszhAJfffnCERWyRaMTqJjf6XYvJwoT8TUzp6luoVyu6QWDQlU8R2KLQ3FWeAvMg9_lw-zHD9m-MRc6yZIEGNgnYPk_2j1MWMqV7ewLaSQ5Y_deBjUexUtSSsLGbs3ksqmTvGJdeWZOTtoMdXiGmGwcxPm7HE1S10GWJRK7yCNXlz23gI3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
الشيخ حيدر الغراوي:
إنصاف الحشد وفاء للدماء، وحفظ حقوق مجاهديه مسؤولية دولة، وتشريع قانونه استحقاق لا ينبغي أن يبقى مؤجلاً.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92022" target="_blank">📅 00:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a911c60c57.mp4?token=mYbDNpduiLmFivSsR9W2CkCR2qEiTwRzJBII9cKOyH2yuPXrKrS3VSP53NdllY8IfH6QnG2bULBl1DLaZlXL9Zrscrx-f53mSJUndKWqkLVpt-H-P1vPHbYwBsGmrgM6rS7pZEt58hu2aOqWR_UZyU31T5rP1Eq-lBTRxHFOz-ecVBggfjGvIhx8hyvIJFvO8oVF9jOmkZETeNWRclIAU3YTMcbdGYuYGG8aNz8G2-hD78piR3aqX4fUtIj53EcWDE1zw7jhgervGkLvEtt13kFS67CtNqO193sXsrAjSBb8yRFpNBhSmlTnEoGEogbg7b85inaWsBIb-BBliI72Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a911c60c57.mp4?token=mYbDNpduiLmFivSsR9W2CkCR2qEiTwRzJBII9cKOyH2yuPXrKrS3VSP53NdllY8IfH6QnG2bULBl1DLaZlXL9Zrscrx-f53mSJUndKWqkLVpt-H-P1vPHbYwBsGmrgM6rS7pZEt58hu2aOqWR_UZyU31T5rP1Eq-lBTRxHFOz-ecVBggfjGvIhx8hyvIJFvO8oVF9jOmkZETeNWRclIAU3YTMcbdGYuYGG8aNz8G2-hD78piR3aqX4fUtIj53EcWDE1zw7jhgervGkLvEtt13kFS67CtNqO193sXsrAjSBb8yRFpNBhSmlTnEoGEogbg7b85inaWsBIb-BBliI72Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحزب الديمقراطي الكوردستاني يتهم جهاز مكافحة الإرهاب بقتل مدنيين اثنين في حادثة التون كوبري وتسليم جثمانيهما إلى ذويهما على أنهما من "قتلى داعش".</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92021" target="_blank">📅 23:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
الاعلام الاميركي:
تقوم المملكة العربية السعودية بإعادة تموضع بطاريات باتريوت حول الجسور والقواعد العسكرية ومحطات تحلية المياه بعد أن هددت مصادر مرتبطة بالحوثيين بنقل الحرب إلى عمق البنية التحتية السعودية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92020" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92019">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679f679452.mp4?token=NA7uI5bYIah0FP5prZkReFAZuS7DQ4UxDLAW9mTfMtgmvD0ZN3iHKXKiaWfbCW3l1h9dfJ0xXOYbdyIFtt0-ku88Sdii9wIIdQVONR-_t2tG9LNgPjX1PgZz_kTxzKR_n1RJNnhTli4QNunWcBzPxGjFfT_K-dkdr_45iyEShCUkzOY2aTa7ugj3C_abpeMgB9qFOf2CYVp4fqs8GomzaJ_0pChoyvi55daKm2bWcBX13Z8I21BYIG1Pz2hxl_S5O4fPJnnwlRJv3R8cB3BWWEfikBChR-5TDJLR82UN0gNlBACTO-BYvvNKjufGcUncF6_zVhCnOFSpdK_EcVpQ6rgunYT8CIUQJ1QeP01NYEBoeVnbCg7Rq1ZwBlI1MF0t4HmROiXktY-FlK0Et3CjANF8yLWzXYPd1hA6JdqWIa0PZtLm_ALJEkphllYNI-9VenRmsm_OgpssNeWKaPGouguFXtx5vrkVCHe8a9Cy3yn1qJ2vyeoBvKE39fCgXAhjU9Hi3MAwopGk834MM8hudJ95fMcPk6G3WRsWoEBeZbs88tbB1CFkwsVw8Mmd-r1F9p3eI_IRoaPHwGdMDkQSRMdCDlIuyNwtRsB1FSz86PWWD1aWVzSr5C1uVKQQzItlao1VYLArAD9farLs5Pevu5iVQikVRnK5m3GSUU8-LIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679f679452.mp4?token=NA7uI5bYIah0FP5prZkReFAZuS7DQ4UxDLAW9mTfMtgmvD0ZN3iHKXKiaWfbCW3l1h9dfJ0xXOYbdyIFtt0-ku88Sdii9wIIdQVONR-_t2tG9LNgPjX1PgZz_kTxzKR_n1RJNnhTli4QNunWcBzPxGjFfT_K-dkdr_45iyEShCUkzOY2aTa7ugj3C_abpeMgB9qFOf2CYVp4fqs8GomzaJ_0pChoyvi55daKm2bWcBX13Z8I21BYIG1Pz2hxl_S5O4fPJnnwlRJv3R8cB3BWWEfikBChR-5TDJLR82UN0gNlBACTO-BYvvNKjufGcUncF6_zVhCnOFSpdK_EcVpQ6rgunYT8CIUQJ1QeP01NYEBoeVnbCg7Rq1ZwBlI1MF0t4HmROiXktY-FlK0Et3CjANF8yLWzXYPd1hA6JdqWIa0PZtLm_ALJEkphllYNI-9VenRmsm_OgpssNeWKaPGouguFXtx5vrkVCHe8a9Cy3yn1qJ2vyeoBvKE39fCgXAhjU9Hi3MAwopGk834MM8hudJ95fMcPk6G3WRsWoEBeZbs88tbB1CFkwsVw8Mmd-r1F9p3eI_IRoaPHwGdMDkQSRMdCDlIuyNwtRsB1FSz86PWWD1aWVzSr5C1uVKQQzItlao1VYLArAD9farLs5Pevu5iVQikVRnK5m3GSUU8-LIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">س: هل يمكنك إخبارنا المزيد عن الحادث الذي وقع في القاعدة الجوية في المملكة المتحدة؟
ترامب: أنا أشعر بخيبة أمل فقط لأنهم قبضوا على إرهابيين ثم سمحوا لهم بالخروج.
كيف يمكن منح إرهابيين الكفالة؟ لذلك، لا أعرف.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92019" target="_blank">📅 23:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92018">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
اعلام الرياضي: قرعة بين العراق وعُمان لحسم المتأهل إلى نصف نهائي كأس الخليج العربي لكرة القدم «خليجي 27»، ستُجرى بعد قليل في فندق إنتركونتننتال بجدة، وذلك عقب فوز عُمان على الكويت 3-1، وخسارة العراق أمام السعودية 0-2.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92018" target="_blank">📅 23:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92017">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOUSjvl8akbJSmAE0m2Dns4RRNN1jtDyy8KCynk_piI3V6RV9hSaFfod1YNDGvaCOaGOnsbZSYRO9cVZiHfG9axqubrXMQBJEFNL5jHyBGXu7XvMmkVKo3Rnnc8ZjNejYi5Ip1ODLfzuo-i7tEP-skRikkv_OmCqW_9dXQMB6tsGbbGi2cGCQ4Gcfy1G9_yt4szH0SF2iTbfbkS-CY4B1x4zqqMkjIyKcv5fAQUi-i_VLgy4tvakFB5YIFKmSU7aAklTzstj2T3qhWaALm3pelEu0Nt9IcEyQ7x2La7UjA5kNHw2gbtvFlXL9WbDinty-TpQXGOvLuUE_v0tFZd_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس الوزراء الاسبق السيد عادل عبد المهدي:
نشعر بالخجل بان مكتب مراقبة الاصول الاجنبية". يملي علينا أوامره المذلة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92017" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92016">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب
: إيران تمر بأوضاع صعبة للغاية، ولا أعرف ما إذا كانت ستستسلم أم لا.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92016" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
العراق يودع بطولة الخليج بعد الخسارة امام السعودية بهدفين نظيفين.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92015" target="_blank">📅 23:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92014" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92013" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇶
🇸🇦
إنطلاق مباراة منتخبنا الوطني أمام نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92012" target="_blank">📅 22:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية تسجل الهدف الثاني في شباك العراق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92011" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية تسجل الهدف الاول في شباك العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92010" target="_blank">📅 22:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92009">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي في حركة النجباء الشيخ علي الأسدي: تحاورنا مع الإطار ورفضنا تسمية "حصر السلاح" وثبتنا أن المصطلح مضر وغيرناه إلى "تنظيم السلاح، نأسف لقرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في العراق، قرار السلطة العراقية منع الطائرات الإيرانية…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92009" target="_blank">📅 22:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92008">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
🇸🇦
إنطلاق مباراة منتخبنا الوطني أمام نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92008" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في غلاف غزة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92007" target="_blank">📅 22:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في غلاف غزة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92006" target="_blank">📅 22:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي في حركة النجباء الشيخ علي الأسدي:
تحاورنا مع الإطار ورفضنا تسمية "حصر السلاح" وثبتنا أن المصطلح مضر وغيرناه إلى "تنظيم السلاح، نأسف لقرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في العراق، قرار السلطة العراقية منع الطائرات الإيرانية من الهبوط في مطارات العراق انصياع للبلطجة الأميركية، لدينا معلومات عن كل التحركات الأميركية وعن الفرقة التي أنشأوها والتي تضم عراقيين بإشرافهم، لدينا معلومات أين موقع هذه الفرقة وما هي واجباتها في المرحلة المقبلة وكل هذا مرصود، إنشاء هذه الفرقة هو لتنفيذ الاغتيالات والفتنة وهي مثل "بلاك ووتر" بعنوان آخر، البيشمركة يجب أن تكون تحت قيادة القائد العام للقوات المسلحة، علاقتنا مع الرئيس الزيدي جيدة واجتمعنا به عدة مرات بشأن السلاح ونرى أن المشكلة في مستشاريه.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92005" target="_blank">📅 21:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نايا - NAYA
pinned a GIF</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/92004" target="_blank">📅 21:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=TywXejQirQNAIyOxPXE6mhGCcgDRZNbzzsmT-LpdF1hBzWY80YoUyL5k8LrE8F9SsevWFLH20Cyzfg4tN5gQoJGQyQD3Qj5y8F1K_Sva4BLAaufwk3srV3w8Wa1-VpFrqFs58awroRkho5iNXcfXrFcu_NcllAMOv5GtiGGHjWbj634jKAUhsYApuPsvoy3xoXs_JZtj61vH4ftanm1ZEItYDPlhSIP2jL5zVNduPp2WpzRAd1F1QupcMWApibjTfmPRHyO45AM8fE8P5I6ou5ma-K0VA7sbSHUM6KjhNcXD6fZY5HtRSNT9ehO9rvGaq1Jj4Hs_44-i7utHLlNq0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=TywXejQirQNAIyOxPXE6mhGCcgDRZNbzzsmT-LpdF1hBzWY80YoUyL5k8LrE8F9SsevWFLH20Cyzfg4tN5gQoJGQyQD3Qj5y8F1K_Sva4BLAaufwk3srV3w8Wa1-VpFrqFs58awroRkho5iNXcfXrFcu_NcllAMOv5GtiGGHjWbj634jKAUhsYApuPsvoy3xoXs_JZtj61vH4ftanm1ZEItYDPlhSIP2jL5zVNduPp2WpzRAd1F1QupcMWApibjTfmPRHyO45AM8fE8P5I6ou5ma-K0VA7sbSHUM6KjhNcXD6fZY5HtRSNT9ehO9rvGaq1Jj4Hs_44-i7utHLlNq0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وَيَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِينَ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92003" target="_blank">📅 21:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92002">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
الكيان الصهيوني يهدد باستهداف قيادات حركة حماس في قطر وتركيا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92002" target="_blank">📅 21:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92001">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
تشكيلة منتخبنا الوطنيّ لمواجهة نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92001" target="_blank">📅 21:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92000">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
احترمنا رأي فصائل ربطت تسليم السلاح بانسحاب التحالف، وبعض الفصائل ستنضم للحشد الشعبي بأسماء جديدة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92000" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91999">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
منذ ساعة، تمّت محاصرة مجموعة من اللصوص المسلحين من قبل قوات الشرطة في مدينة إيرانشهر بمحافظة سيستان وبلوشستان، وأصوات إطلاق النار التي سمعت في المدينة، تعود إلى هذه العملية الأمنية لاعتقالهم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/91999" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91998">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">▫️
الشرطة البريطانية:
لم يتم العثور على أي أجهزة متفجرة في قاعدة "فيرفورد" الجوية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91998" target="_blank">📅 20:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 35 غارةً جويةً من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف استهدفت الأعيان المدنية من شبكات اتصالات ومدارس وغيرها في محافظات تعز والجوف وعمران وصعدة والحديدة.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1158 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91997" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76dd2e40a0.mp4?token=ZI3142G0LSLympVbfUU9i-vXPKyjeOcNCbX4vvrbkAqVEAn5Y_zBUh4AJhJwgL8hmnp8EVit4gQPxLzO-ymqGJShkTNgo__0ooFkNDxAmnK4lEovLloHilRwl3ZW0er-yrSxobiMrH9YodauVdM3TjZrwbo8tuncZwNsMjh98Pvzg27W03Mr0ZXUhPSHBZT5cK7LCoNWbZStRhJf5-76iC3jF0T6PNYpmi9RYiU7yjBeMXsCXTo5GjaBvxq2avbl-87zIshTeL8Q4gcHG0akMCS3fwcc1lGLY5Su9aAXpkY6tQ-ccBRDrcH7isGyKb1YCPHTE_22eASrbqjJESoGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76dd2e40a0.mp4?token=ZI3142G0LSLympVbfUU9i-vXPKyjeOcNCbX4vvrbkAqVEAn5Y_zBUh4AJhJwgL8hmnp8EVit4gQPxLzO-ymqGJShkTNgo__0ooFkNDxAmnK4lEovLloHilRwl3ZW0er-yrSxobiMrH9YodauVdM3TjZrwbo8tuncZwNsMjh98Pvzg27W03Mr0ZXUhPSHBZT5cK7LCoNWbZStRhJf5-76iC3jF0T6PNYpmi9RYiU7yjBeMXsCXTo5GjaBvxq2avbl-87zIshTeL8Q4gcHG0akMCS3fwcc1lGLY5Su9aAXpkY6tQ-ccBRDrcH7isGyKb1YCPHTE_22eASrbqjJESoGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
إندلاع إشتباكات مسلحة، يرجح أنها بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة ايرانشهر جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91995" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية تعلن عن إطلاق مخزون النفط الاستراتيجي في بيان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91994" target="_blank">📅 20:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91993" target="_blank">📅 20:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91992" target="_blank">📅 19:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFEVUGBD6xyo5sTyhHEhXugU1NWMSN3r5dDhdVom4WaTQ35Fg3Q2qui3FEyEviHzjb1f4EGT8BUJdIzAHH_iZh8Cga17Y5SMpJxVYLJEDOeinbLpz4ylWPOus3aOsUFM_21WYs6xfkY44WX0T1OwFwrz8kCYEQ7XIA7lTXzeQHK-WQIsowfgVFE1x-Peg5qxmju2qEGeNI1yUB9BZaLf6kPNzrU1DytKpso3KopxoLEDZBuHL4LbOdm-XGAihn-5Og569Z8_XkcZkbuJQp2tlRnjHBCgveaxfAFDehwB-e0VG1652OyXbPhnMRVTaOxrDAWUwwSO85U6DxZZFxtXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
‏الملك المغربي يكلف فاطمة الزهراء المنصوري برئاسة الوزراء كأول امرأة تتقلد هذا المنصب.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91991" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBNlIDWJ4D-jKA47ewKDMPl2cTda0fxfKSaLhEx0IM-5ANI6cLhpilJix7vW9c5Jq_E7D--WuOBuJ8QBZZsiMfC4g9--ZSw9bSHyTRfYDfrT-SO9jTPmoW5dMnkstIwDjR_Sg2sPJl-V7dQpK_1e1h9gfFtMkmHDjVZ9umTSc3oktV8DMUcDBHrPAvpesmzYBT-k6TogudB03Z9NQK_ouvF7KkqeVRXmCrTJf42D4zyzIysCQsCSgm8iUYdhnZu2_v9rrEABDTymL_LJ3F5vf9sLuqtcV3Rl86GEixFnHpiECX2uM1GrULTIMd1TFSgaLqzEviFU5HVDbo0p8aUFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تمنع ظهور عماد المسافر في وسائل الإعلام لمدة 15 يوماً.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91990" target="_blank">📅 19:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
استشهاد طفل مدني من اهالي التون كوبري في محافظة كركوك على ايدي عصابات داعsh الارهابية اثناء الاشتباكات التي دارت عصر اليوم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91989" target="_blank">📅 19:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية تعلن عن إطلاق مخزون النفط الاستراتيجي في بيان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91988" target="_blank">📅 19:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oODZtXV0fBBOGmtgj-_RxkAG5jlfagst1sw1BI9Q8x_8g0X2Rs8bHsOg2I4xxSmXmwojzyHsViah972h0sMm6gu_AeJz16YZubp9lFbH3HabLvhLG4yRWkgSfWcny6sHLBhwgUxY4X8zqvcJA6ESimeuiGXXYWvpfx_SauLbaEGQFphlw24SIPYwjtPylHtyblT4HKcj09j-SC2NJUTPcUy1OkxDT2yNB4gf9moj6AV5RIGMtAcCSxf8P18oJOL6EfGe9BtQeVCHCuBdwdpr9LIPeBz1GFW_SlP1JjxHHray6WyFV85eLha8Aob8P5ZQJgAuoTuKR-ecaT15-1qC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تشكيلة منتخبنا الوطنيّ لمواجهة نظيره السعودي في خليجي 27.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91987" target="_blank">📅 19:17 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
