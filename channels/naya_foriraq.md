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
<img src="https://cdn4.telesco.pe/file/uTaIMdr-YgfQFrpbEsWQClbZ-9T7MzWhbMPkrZ21uNNbmEsn5zwmaCM_Ezgv24m6qICRXvAhAa7nxXR1f3ypexwniP4w3h33b7q7FgpsVbKBpPlyJp_J8EWpNWmbodwKsEECjj68v8jEg7NuSxTPZXu1FF4_7UnGmwpsRX3YY0s1UP8yQkTWq_jvX4FndsgB_nyTKu5hxqjQlY-OQSNNJx2BvrwQx6_NqzvlorHJUl1VztGjNNMjJWbf5dV1DkuiN4VCfZC9m8etrI9bl1ygNdil9iAgbNJoZSfQnvF8oxwBvqs_LkFEtTau8a1ytZJSlxzyvuCw0407_w7BVGlxKQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-79991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">السنغال تسجل الهدف الاول في مرمى منتخبنا الوطني</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/naya_foriraq/79991" target="_blank">📅 22:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79990">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2d55dce0.mp4?token=gsmH8uunb-lnIun2XhsdNqnBAtR8ftEN8E_ga5qPBruxs8l0wpf-gP_1UPa1BWhwoeHVblHLe1mlweQD4hbiviu_lMtBU0LxKEqgieWZU_NmZevcJx-dtWDMCnJfqh50VPh-M83xY1D3HA2NPUvs6my1sPXyd4mYAuSEpeom2yJebDqrWcGR4f5YAQLnUR5Uzez9_GBadC_WVZkLFppPoCBoN23L4c58HfD_uFdhAMEACCqcG9Mb74tHNO1CxphRz0dzMalEMasOq7WVAWNDr8PcDjrsCzehlFo8hpAXrpgLpYv4lWseP4akzNOErc2EAZ4k6rN7SP1kmoFtaC2cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة.. انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/79990" target="_blank">📅 22:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79989">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX8R-o56-wBxnBWpcZz3GYvnJ9k4DCg0ZFtirw1R7rfEKvlWjCzHefmqXsl-i3n8PVmcaOicnbRY5X90nsgfZ5mGH2Yq8Nxqv1ezDis0xi1FKB4Vfz5Pl9rBt19autWHxbx2ztTllicZaFPmFjdkjOR_2PxHrXCceHS2p2--vrzhrOf-wAPsxn5ybxeEwTX695MQjpkrU7F7FthMlIH8oP35oL4D0XrxCDw6DiWkFevHij5_q-zGMWSUKpQXf4-9ipj972YnvgXiE6lguU7fRMMHJ3ZM8UAjh3yy2fikd6PxA2RF7J5_SZIJelvU8mOWBaNPKSzxbRg5wNEFZO9sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
🇮🇷
النائب عن حركة حقوق حسين الدراجي :
اليوم ببركات الإمام الحسين "عليه السلام" تم ضخ الغاز من الجانب الإيراني بكمية 5 مليون متر مكعب باليوم علماً أن معدل إنتاج الكهرباء في البصرة تجاوز معدل الاستهلاك وإن التشغيل الحالي افضل بكثير من الشهر الماضي، وسنبقى نتابع الموقف كما وعدناكم أولاً بأول، ومن الله التوفيق.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/naya_foriraq/79989" target="_blank">📅 22:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">استخبارات قيادة عمليات نينوى للحشد الشعبي تعتقل شبكة مكونة من ثلاثة متهمين (اثنين من الجنسية العراقية وآخر سوري الجنسية) ​ضبط بحوزتهم مادة (اوكسيد الزئبق) شديدة الخطورة والمحظورة دولياً</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/naya_foriraq/79988" target="_blank">📅 22:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامب: لا تزال إيران تمتلك بعض القدرات، ولكن ليس الكثير.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/naya_foriraq/79987" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79986">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏ترامب يهاجم وسائل الاعلام الامريكية التي فضحت كذبه: ‏زعمت الأخبار الكاذبة أن إيران أقوى بكثير اليوم مما كانت عليه قبل أربعة أشهر. ‏إنهم يتوقون لإبرام صفقة.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/naya_foriraq/79986" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79985">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ترامب: ‏إسرائيل رفضت المشاركة في عملية اغتيال قاسم سليماني.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/79985" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79984">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب: سأكون صريحاً -- أعتقد أنني سأكون أعظم شيوعي في التاريخ.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/79984" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79983">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
التغطية الإعلامية ليوم عاشوراء
:
شهدت التغطية الاعلامية مشاركة واسعة، تمثلت بوجود (7) عجلات للبث المباشر، و(84) جهاز بث مباشر (LiveU)، و(676) كاميرا صحفية، فيما بلغ عدد الإعلاميين والصحفيين المشاركين (1011)، بينهم (102) إعلامي اجنبي
(12) إذاعات محلية و(82) قناة تلفزيونية شاركت في تغطية مراسم الزيارة، إلى جانب (26) وكالة أنباء عربية وأجنبية، فيما بلغ مجموع ساعات البث المباشر (1006) ساعات خلال عشرة أيام، كما نقلت (87) قناة محلية وأجنبية البث المباشر عبر خدمة (Feed Clean).</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/naya_foriraq/79983" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79982">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180ec771cc.mp4?token=SuMuZR9xa7ADmFeN9gyiRk-yLBqcdXxyxtFUqf0oJV-kHRtm8LHGQ5aRxOlcE6cREl4sGAwG6oQB8Thdj-VyTxT-L88m5bp0I6AWwtwMnpQG7MmenU7zMyrZE2R-VwN26YAQtghCuqLZAYjgVezK8aRfgsk-vW2PgeUHzRMXUiGtSP0XTRx_r_pYc7-oIWvnBh_veyiD-nc9r10TovMtZsMrdQOG-VBhQJ1QjHJEJ5vz9wVF9VYC4wMkQ_5SUV6Y2hkauieSvHCY_O-bSpSyIInJQVgo_8gz95ujbS01ipBwIzbWi-dZWlsVeYoJJxxqyCVf74-_k2YlghN13TF3WE33_Kd0TI-iFwrXdAcYHFH1Wqw_y1OlvxrsH65yfMeLnsykpwdsjhcs8ULcADKPzsEqAT8rW_2gUHDnekTKcrnoAHKlgvVQOi3I9I9uVKi02X0bR421ypY3XtLQJ5TK_APuxXk9e3RrUhG9LA5_xESwg03f59dTPm6KEX7ylkLDogBO_wRRDSKs_HNMA__94CMfC1o8cXaPH-7Y4jgmIlEmYM4OlwdKFiI5z_7lQbG8V4xlHDSUUuui_acXgh6O9gJ4H0F4X972uYUKbU5fz13QjLqnH21M_0L7_ja-hQOshOcMllp2w-HSxw1Qc4rjt1vMXSxAxnh6YIW--c54pSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني: ‏ لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً،…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/79982" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79981">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
🌟
بالتزامن مع ترويجها لسردية فصل الدين عن الدولة في بلداننا.. رئيس الولايات المتحدة ترامب في خطاب ديني:
‏
لكي تكون أمة عظيمة، يجب أن يكون لديك دين وإله. ‏إذا لم يكن لديك ذلك، فلن ينجح الأمر، أليس كذلك؟ الدين عاد بقوة. الدين في ازدهار ملحوظ. لو كان سهماً، لكنا أثرياء جداً. عندما بدأتُ العمل في عام ٢٠١٦، كانوا يريدون تجريد عيد الميلاد من روحه. لقد استشهد مؤسسو بلادنا بالخالق أربع مرات في إعلان الاستقلال. أربع مرات. ولم يُذكر اسمي ولو لمرة واحدة. أنا مستاء للغاية. ولا مرة واحدة، ‏في ظل حكم الديمقراطيين، استُهدف الكاثوليك من قبل مكتب التحقيقات الفيدرالي. ‏سُجنت الجدات المؤيدات للحياة بسبب الصلاة. ‏تم طرد أفراد من جيشنا من القوات المسلحة بسبب معتقداتهم الدينية. منذ فجر تأسيس بلادنا، بُنيت عظمة أمريكا على أيدي المؤمنين. أول المستوطنين الذين وطأت أقدامهم أرض هذا العالم الجديد في جيمستاون، نزلوا من سفينتهم، ورفعوا صليبًا، وسجدوا للرب في الصلاة. كان الإيمان هو الذي قوّى رجال الميليشيا الذين صمدوا في ليكسينغتون غرين وجسر كونكورد. ‏في فيلادلفيا، قبل 250 عامًا الأسبوع المقبل، استحضر مؤسسونا الخالق أربع مرات في إعلان الاستقلال... الإيمان دفع الرواد إلى السفر غربًا، والإيمان قاد الأمريكيين إلى إلغاء العبودية، والإيمان بنى هذا البلد ليصبح أكثر الدول تميزًا في تاريخ العالم.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/79981" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79980">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=kpD5XQbnhaCXkyQ4dGlM_mwHFi-hv_HzF542HdOM0_KKWOcLNpA9bbuXmNTmPdRgGwyf7_OafQ40Edk-NyqMp_8oPHTzM93Dot0F9rEU62FNai_DWGFKeFpxNKPn_4MXpIeyDPHdlHo1sGCK9a7HC191p9fThB8tIypOztGaBLMUFvw9x80w5BfxjegAUW17GWvcz7CTuTzwGnO2HHAT1PleXhP_lhnAXyxu3HZU3QKV_6Y6awwiRgp325iaGkHa3q_iC78QrBsOYvu75HiMtfevYcbuEQDmj3wUUBuXlNeuMe6H_V7eidLiuoy_OXfanncQamg8_4WkPpY0CEsgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1cc7c8a5.mp4?token=kpD5XQbnhaCXkyQ4dGlM_mwHFi-hv_HzF542HdOM0_KKWOcLNpA9bbuXmNTmPdRgGwyf7_OafQ40Edk-NyqMp_8oPHTzM93Dot0F9rEU62FNai_DWGFKeFpxNKPn_4MXpIeyDPHdlHo1sGCK9a7HC191p9fThB8tIypOztGaBLMUFvw9x80w5BfxjegAUW17GWvcz7CTuTzwGnO2HHAT1PleXhP_lhnAXyxu3HZU3QKV_6Y6awwiRgp325iaGkHa3q_iC78QrBsOYvu75HiMtfevYcbuEQDmj3wUUBuXlNeuMe6H_V7eidLiuoy_OXfanncQamg8_4WkPpY0CEsgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">في ليلة الوحشة..
انطلاق مسيرة الشموع في منطقة الكرادة الشرقية وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/naya_foriraq/79980" target="_blank">📅 21:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79979">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏مسؤول إسرائيلي: سنحافظ على الشريط الأمني على طول الحدود داخل الخط الأصفر بلبنان.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/79979" target="_blank">📅 21:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79978">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWpeii3eRLidLZbbZLxEgJ5__AGtA0kDZDtqhSFOa6Igu9S5k6q4nFpWawnrQJ_m5iBdS01vTRvTE_4jWhSzHh8Smhdox6Mo8ELhxjo0NUlW-cKNRLLmP_tGBg7g6H5LJnhEhKwcm_gCTnCaJecNi8THodjJli-zmU-k1KrN2qyomkTeBBY0zWWwf2Ebk6YCJmDAg75IFAKDg9OfBxjIFAwnwT2yT2eC0rXfC20FD5a3-CuCldkdj_5RGBU9cI1J_6Y0FGtKh4IklBDiTjw2y4F3RyzzX4NDZ9ioFRT2ZwKoFvV9z22Wj77U_drEeWNzepRIi4SgSpr_y_chWFdMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس الوزراء الباكستاني:
مع اقتراب يوم عاشوراء من نهايته، نُعرب عن أعمق مشاعر الاحترام والتقدير للتضحية الخالدة للإمام الحسين (رضي الله عنه) وشهداء كربلاء. إن ثباتهم الراسخ في سبيل الحق والعدل والكرامة الإنسانية يبقى مصدر إلهام خالد. ‏الحمد لله! لقد أُحيي هذا اليوم المبارك في جميع أنحاء باكستان بتفانٍ وصبر ووئام. نسأل الله أن تبقى روح كربلاء نهتدي بها نحو الوحدة والرحمة والعدل. ‏نسأل الله العلي القدير أن يبارك باكستان والأمة الإسلامية بالسلام والرخاء الدائمين. ‏آمين.</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/naya_foriraq/79978" target="_blank">📅 21:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79977">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_-BHztCNi48_-IIc2J4Ut9L4rn4V7xB8lhVB8AnKYB469Gu-5Lj89UNPb1CMJkoOH6D0R3PCy8SxJ-yTcibk1qkN2pV848ss_Ar3ptpePtSbPEsmIzXMSf6GaZt640LyrE6nFMl_PqBqiKa9n5LvWv_Xny9DerfODHBfhyTuUzfDEXonevmmkmxijacrIkTGrZe3vUUijUOTumdZneK94nIFgZnImBat6KHfReHQCFdPUoslHQK0zNIjX9847W6GXMhpUBLgWuVYuiwPG27jRP54GZG201NnjL1CK5nip0y6W4xYFUrJviYoZrZIwmpgngOPC1y-dfWrhkAZ7yU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرطة محافظة كركوك شمالي العراق تغلق الشوارع في محيط جامع صالح بهاء الدين في الحي العسكري بعد انباء عن وجود سيارة مفخخة</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/79977" target="_blank">📅 21:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79976">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
🌟
لبنان وإسرائيل يوقعان على ما يسمى بـ "الاتفاق إلاطاري" برعاية أمريكية.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/79976" target="_blank">📅 21:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79975">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw9Qa1Vxo22JYiUsoW6GE6V5Omg941knvcKnPdCGxZI03Yn_Da94M7WDQhadcME8yotZUwDe4RAh-WD8FplsY4wQ6TQ-CCG0Xd2BpiTUmRmIig_1T-aP_9Am1gCPCURWWP0zUL0Umhso5LlwtajJkPv_SSt1kAYRCal-P14gF6f9azzHldYka1n4GEtTnFOFvcGHuVFTr-7OgHYA8XjJQzWxE5rrsn5UTiUV7C3YDfaQiPfByiJsyqxiLQ8b7g1guyfi5jGZmNicJrQ1ILrW1036Twgs31aAdpa6w0Ee238PpC4C7cEB0sE008ezXbtmLNgGvZIV947YE42ljp1yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/naya_foriraq/79975" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3m1jpZZfb2I8-N_DIFs-xzXFIfqE4eyei7ktqZ2qCkdyluyrBMKCbZgBvbShhCv_3_M2oo1YhRNFfF5Ra6kZI487Ia5q01tDhjSJMLMBkBYwwKp94HdHGf4ae9Xrp4Z-mwRsBzo1kQoxfbL5n5hFP8V3OWObHC4v2fELkofykpkHFrf-ZtdORZRYtJRg4Q4hyLm_-ekEiZGUEScwoPEPYVIoe1vbyGmv5nJjuw3JyizwUyybV0CEWj5ckPHQ4CyXN75oDzm5580WeCWYf0XoqlV5Ndbt9TktnTl_mCgXkUqp1NnQaE5Qfohdkjat0ws3le-Hmc1WOFlhIjBVu5RDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سأتحدث في الساعة 1:30 مساء إلى تحالف الإيمان والحرية، وأحد البيانات التي سأدلي بها، ربما أهمها جميعا، يتعلق بالانتخابات الأخيرة للشيوعيين في بلدنا. من السهل جدا بيع الشيوعية. سأكون أعظم شيوعي في التاريخ. سأعطي إيجارا مجانيا، ومنازل مجانية، وطعاما مجانيا، كل شيء مجاني. لسوء الحظ، بعد عامين أو ثلاثة أعوام، سيفشل البلد الذي يحدث فيه ذلك. إنه يفعل ذلك دائما، ثم ستبدأ في العيش في البؤس. لن يكون هناك طعام، ولن يكون هناك سكن، ولن يكون هناك جيش، ولن يكون هناك شيء. ستكون العالم الثالث بكل الطرق، وسيعاني الجميع أو يموتون. يؤسفني أن أقول، لكن اغتيالات أولئك الذين يعارضونهم هي عنصر مهم جدا في أيديولوجيتهم.
إنهم حيوانات! في كثير من الحالات، ليسوا أذكياء، ولكن في بعض الحالات، هم كذلك. من السهل عليهم الحصول على متابعين لأنهم يقدمون وعودا يعرفون أنهم لا يستطيعون الوفاء بها، والدوموقراطيون لا يقاومون. من نواح كثيرة، يسمحون لهم بالسير في طريقهم الخاص. إنهم يخشون أن يخسروا انتخاباتهم، إنهم يخشون الصراع. إنهم ليسوا أذكياء بما فيه الكفاية أو أقوياء بما يكفي لمحاربة هذا الطاعون. إذا قاتلوهم بالطريقة التي يقاتلون بها الجمهوريين، أو أنا، فسيكونون منتصرين، ولكن ليس لديهم الشجاعة للقيام بذلك. هؤلاء ليسوا دوموقراطيين اجتماعيين، هؤلاء شيوعيون صلبون بلا إله. هذا هو أخطر تهديد لبلدنا منذ وجوده قبل 250 عاما. أليس من السخرية أننا نحتفل بعيد ميلاد مهم جدا، وبدلا من الحديث عن المسيح والحرية والانتصارات من جميع الأنواع المختلفة، نتحدث عن تهديد آخر لأسس أمريكا.
سيهاجم هؤلاء الشيوعيون الذين لا يرحمون جميع الأديان ولكن، على وجه الخصوص، المسيحية - يفعلون ذلك دائما. جميع الدول الشيوعية تهاجم الأديان بعنف. كما تعلمون، لقد ضربنا نيجيريا مؤخرا، وأنهينا إلى حد كبير ذبح سكانها المسيحيين العظماء. إنهم يعرفون أنه إذا ذهبوا إلى أبعد من ذلك، فسيكون الهجوم أكبر بكثير، وفي ذلك، لا يريدون التورط. أنا أنقذ المسيحيين في جميع أنحاء العالم، على الرغم من أننا لسنا في تلك البلدان المختلفة، من خلال ضرب هؤلاء الإرهابيين بعنف وقوة. سيغلقون كنائسك، وسيقتلون شعبك. هذا ما يدورون حوله. هذا هو أكبر تهديد لبلدنا منذ تأسيسه قبل 250 عاما!</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/naya_foriraq/79974" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو يعلن عن توصل لبنان وإسرائيل إلى اتفاقية إطارية</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/naya_foriraq/79973" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في ميادين الجهاد وميادين الشعائر حاضرون
انهم رجال المهمات الخاصة
#كتائب_سيد_الشهداء
#لن_نساوم</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/naya_foriraq/79972" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1sOUSXDHEhk8ghneA5zhbFyUwwF4WvP6L4_kEV43U2UrNbFHHnaIKGUTcX7LpJTZGw6L5wqHobEoG3qAQckdYJDrKH-jBkot8RrWaVHjR1yybKj4YTTGsGkMuu4W0d9-t-vKWQ_pfIDERhsUzPElyms9b6bf9IozapnowFC583FNGmQWI2upP-d9ciOEt3L_lC2Qc319fu2g_UepRrXXnrNBPtEAnmAzKjGbFey14pYVU2A_3POCOjvlbU7nn484N33kAZAQ_ztfUOlD85DLP3ynmb0vmETgRae3GPI-8DCFnCIs_Izq1MCAyYn52kPIS8X0ZhcLdN8cfNg4TSLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي في مواجهة السنغال ضمن الجولة الأخيرة لدور المجموعات في كأس العالم 2026</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/naya_foriraq/79971" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPOJDnFidkQ2_0XNNiqDofGpFiJdHWLPHLFmTyNm3JhvgRguci659ASbmMY1MaQ2_q_cLJhpYqXz-8ICDQzby32aZ2N3shUG_P87YsyfT8XHwWX9HhLuosVNCNd-PArc3bXC8gJe5eccdy_lghGXvIFzO-hRuaiUG9I0UNrGnHiNIxRgMwEmdfrxp03K4RpymwUF7nlcMosNlQTagvVE4K9PJ-fHntw5AaW9jckIcMUTs74kXIlYLNND9yBedByw5_2EwqIOHkNIvtK_3jMS9bfEqUuaN6waYdtLnDJ3CCooaT7Qg9MYZp2xH0mMaw806I94uYxkiTzUGcPuZVM3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي
:
-
في العاصمة بغداد نفذت مفارز الجهاز عمليتين منفصلتين حيث تمكنت في الأولى من تحديد هوية أحد الأشخاص في قضاء أبي غريب بعد رصده ينشر محتوى عبر منصة "تيك توك" يتضمن الترويج للفكر الداعشي المتطرف، وإثارة النعرات الطائفية، والإساءة إلى الرموز الدينية، فضلاً عن تمجيد الجرائم الإرهابية، وقد ضُبطت بحوزته ثلاثة هواتف نقالة وعدد من الكتب التي تدعو إلى الخطاب المتطرف.
- العملية الثانية، أسفرت عن إلقاء القبض على متهم أقدم على تمزيق راية خاصة بالشعائر الحسينية في منطقة حي الجهاد، في محاولة تهدف إلى الإخلال بالسلم المجتمعي.
- في محافظة كربلاء المقدسة، وبالتنسيق مع العتبة الحسينية المقدسة، تمكنت مفارز الجهاز من معالجة حادثة تجاوز وقعت بالقرب من مرقد الإمام الحسين (عليه السلام)، بعدما أقدمت مجموعة مكونة من (١٤) شخصاً من حملة الجنسية الأجنبية على الاعتداء على زائرين آخرين، في حادثة كادت أن تتسبب بإثارة فتنة بين الحشود الكبيرة في منطقة بين الحرمين.</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/naya_foriraq/79970" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
حزب الله:
تنفي المقاومة الإسلاميّة نفيًا قاطعًا ما نشرته جهات رسميّة تتبع لجيش العدو الإسرائيلي حول سيطرته على تلّة علي الطاهر عند الأطراف الشرقيّة لمدينة النبطية.</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/79969" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
‏الإعلام السعودي: إعلان عن اتفاقٍ إطاري بين لبنان والكيان الصهيوني بعد قليل.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/79968" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvelegl8DLp-9z0ECZ_njRY5sIpgCyxpjpemfnzEWRJ0QwgCWsgUqgCr28buz65BEEaCt5aTVUX0HulnsbpFTswmbbCy6vhoenCJdhQEdHxvMZjvF2d_mLsG6ZQ9S9SliYaAb3rmpEJI_ODopKs1rVzTQ9n-3LXBNP-QWmFkGs23q5l_-hWeGFIH4UdA2EOoNT-zKV_-hRMnh7C6uJ6CD56di3Dj6a2HbpyzddFgrIbK_023r8zgh81IRlR9StjsDR8Pm0MmGPenKmY0aychHAtLuHxPdVGE2BsptYAlweblj16lsyDjWPP7t8_rHS7U1Yirsdyk-Y2hiVjuzc9Cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.   ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.   وقد أسقطنا الثلاثة الأخرى.   من الواضح أن هذا انتهاك غبيًا لاتفاق وقف…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/79967" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvBp5kdY1-Yn0aVph24_1UjkZyGvbHXJ-469oLiZrJKtVLnh2eSvYSD4B66bbwM8631vvQ3jL-TijNhEtcSa7ixcP363QnGpvDZSr81NxmAHUcsylmodgOW47RTrhazOhGCSls0R3AyzgvHCEMAIHGR5cSjdAK9H_glzJA3GsDiTzDQ0zFIsQ9EiMv6t19xWJ0ouVhPcqCZljaj9vLejce7Buc8aRrEie_2xP16q7PjKkhyFjdaI49_ypr-o27HDRl0c7SIMXeBuPE8zQzNV3yqFEBlW-pQFpNRaRbhwLSnt8WfVF2vTyd-ZIgQgaDoKBozUKs2dJlMuQU9G2J537g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أطلقت إيران أربع طائرات بدون طيار من نوع One Way Attack على سفن في مضيق هرمز.
ضربت إحداها بقوة السطح العلوي لسفينة شحن كبيرة ومكلفة. لحقت أضرار، لكن السفينة استمرت في طريقها.
وقد أسقطنا الثلاثة الأخرى.
من الواضح أن هذا انتهاك غبيًا لاتفاق وقف إطلاق النار بيننا.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/79966" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نايا - NAYA
pinned «
🇮🇶
🔻
Dear brothers and sisters, in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79965" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
🔻
Dear brothers and sisters,
in light of the reports regarding the presence of the martyred leader Immam Sayyid Khamenei in Iraq during the funeral procession, Naya Channel has launched a dedicated channel for designs related to this occasion. Please join via the link below.
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79964" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭐️
مدير عام الوكالة الدولية للطاقة الذرية، حول ما إذا سيُسمح للمفتشين بدخول إيران:
من أجل الإشراف، نحن بحاجة إلى التفتيش. لا توجد طريقة أخرى.
هناك اتفاق، وللامتثال لهذا الاتفاق، سيتعين على الوكالة الدولية للطاقة الذرية أن تتمكن من الوصول والتفتيش.
أنا مستعد لمواصلة العمل الفني وأن أكون هناك في أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/79963" target="_blank">📅 19:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-4-JJnSGNh8Tur3cRz0Qt5ylxjksqfoyrROSMMfUeoRV-LkgXM4h7XnVjVXERBtsqGFFBJgefNkyqWQpNHUucufYl5agHVlJQzSVy2HFhn5FlZDOtw_pTDoCXzU6bDshojm5sG_OzIG7-0Pu7MQfLxLzzi3pjpyitgkQhUblCXNr_NG6l_oDapWfGIOCnPbbkgCRlYEhFovdvXZLfLILgVTL6t_9vvhxqmONfY9UuTjQpEo79xZf6cttqv2I1N9Fyo1_xzmHNsHuCchtC69BZzB6kggPYbOy1E0gUXnfGxofdH9ufFcU7JMX2GWYz4bDluRw6EoUCCafrpuKqVe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هناك شخصيات لا تختصرها الكلمات، ولا تكفي السطور لوصف أثرها. ومع اقتراب يوم التشييع، يستعيد الجميع ما تركته من حضور في وجدان الأمة..
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/79962" target="_blank">📅 19:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭐️
مصدر لنايا:
توجيه بخفض إنتاج حقل الرميلة في محافظة البصرة جنوبي العراق، بسبب استمرار الظروف القاهرة وتذبذب وصول الناقلات.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/79961" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7f73f33d.mp4?token=nJYOXcXn3CeMlyKHRxp6H4pcX1XPwjempwki40n9AoBCYdnEjuo0mdr4KK0JjJrixCpmqbZjJgEWYaJLPFet79oAZpvi1YUY0uZaFsOuI6C_Pzr5IaBNKpXbApbxD4-3bnW4v0IGcFz8nhyJDMUbyxe4e1Uxb7kVaFZv4BE30y7eIdpSf2EK5-O9p_ayM6dGOvCXJsHmPRWjUpZeNqSyno1Q9_FyY5wEM6IH6gQiv3apKg07QBbcfGckcTwlHY5_xI-W58cvCkn3zvGtxbhLfTe8ZYsnyCRVYE1ll_Y6b1AQuh6w4rHJyPSOmQqn43Nf3nDuJCDI5a31dM74tfi5DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية تنشر مشاهد لإستهداف محطة توليد الطاقة الحرارية في سلافيانسك الأوكرانية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79960" target="_blank">📅 18:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
بلومبرج:
أخبرت عُمان حلفاءها الأوروبيين أن السفن التي تعبر مضيق هرمز قد تضطر إلى دفع رسوم مقابل خدمات مثل المساعدة في الملاحة ومكافحة التلوث.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79959" target="_blank">📅 18:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭐️
المنظمة البحرية الدولية:
14 بحارا قتلوا منذ بداية الأزمة الحالية في مضيق هرمز.
نحقق في استهداف سفينة أمس بعد عبورها مضيق هرمز من المسار الجنوبي.
أغلب السفن تستخدم المسار الشمالي الذي تسيطر عليه إيران بمضيق هرمز.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79958" target="_blank">📅 18:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">إعلام اماراتي : انتهاء حالة الخطر !</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79957" target="_blank">📅 17:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية.. هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79956" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79955" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79954" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVuZkTOOyOq_qe2gfubXohjlVGhQzC4ZSvk260D11NEWIf_VKlXtJr91QVZlBwn234x64kGXwLMNaxBFfppmR7giRZeJ3Wtx6T605tbbm8bRvo53JMk1rUr63qvzwTBqJb-7TgHDiP2lvPV1gfdesrXt_1EhFZMBjQvX3OYBm483Tc49UP5v5Ac9_Z3ZJBieVnQcO2CZbnVwORckNf-FJ0gG39USmxjhp6Bi1Nanudm8ympihYbKNbNY_5wRMafEiNPmLVl8SQLL2bfq9ff6tlXjTVXuxLpo2PUJburAZFSqZtpi9T9LaqPmZRylktudmiYE34YO5h3Z00jRJH62GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79953" target="_blank">📅 16:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79952" target="_blank">📅 16:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اصوات انفجارات في دبي لم تعرف طبيعتها</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79951" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇷🇺
🇮🇷
‏
رئيس شركة روساتوم الروسية:
روساتوم ستعيد موظفيها إلى محطة بوشهر النووية الإيرانية في الأسابيع المقبلة إذا بقي الوضع مستقراً.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79950" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c90f612f.mp4?token=D9Qc4_Lyg44waNShA-8yLov_ShZ2TOO6B1J3XJX2M3e2ldtQWPHjgWsjdyt7mdgcAMxZHFCvKrID7Laxk4x62vBYAnUtsfbU2Sc4q-Mid_jTZb3lzsmAvfgAzkc--qhSkVgwHw6VTRjpUiqtoedQ5SiLuqmd5XoLkrsJwoZ_dXVcbV7p29faUTw6xOHKB8HoBQR1x-86lURiiFLjzF07r1OZpE2cInUnJfUb5VpqfO7LTe1jgqvbJLTtwDfPVaJAuvGy0Z2xWodlsJFN-0Cy0zVBpWff3SopZdLVtRCzjxvMcckFfwegbVIwZ5Kwtjt-6ymOtR2FKG46J1DtrmmwtEXEDEUQdq4CjwDwlX3mdq3xdtw2bxdWUWQB8AFAOw8kMTGO_7tEdL_x_Z3c3_i4TEVBi_Tz_UVo0weeFdjFvwmZ-yFa_TWi-O2QlwOh4O0SAw7BHgiy2bsfoVPvtyK4K5QU_JiVSyG7XwOdOt_vmc42tms-DL8_kvGu5ksCiSbiPVdWOP8fF_vtuHoBR52OFm-ZEFez9JgBjB0rZ31PJ6Dc6HFEpja1ehj_7Nihwq6U4COrqB1krZ4l7GyWVGwmdSAI849ksr7cTY4deRPi8eptTrsqU4C0-qwgo_xgUeDsQOrSQGv2NjHFtlfdfa4r4-XAhqw3bkOWqRg2Vv9DmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني ينشر مشاهد يزعم أنها لغارة إستهدفت النبطية الفوقا بجنوب لبنان صباح اليوم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79949" target="_blank">📅 16:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
قائد قوة القدس الإيرانية قاآني يكثر مؤخرًا من إرسال التهديدات تجاه إسرائيل.
إذا هاجمت إيران إسرائيل فستكون هذه أكبر خطأ ارتكبته حتى الآن.
هنا لن تساعدها أي هرمز أو إطلاق نار على السكان. لا شيء سيوقفنا.
قواتنا مستعدة لإكمال المهمة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79948" target="_blank">📅 16:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
🇮🇷
وسائل إعلام خليجية:
أميركا تسلّم باكستان 22 إيرانياً من طاقم ناقلة نفط احتجزتها خلال عملية قرصنة في وقت سابق.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79947" target="_blank">📅 15:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKZUABDCXiTGkxJoNkmdiMR-XBwqw9Yy6sch9RGofw5sfq9m9L0x1evs2c-czo0N89ej3mKa3n_fEsYRQnw7-8SIvoweTzjkZ-OLUpN2Kewk18L8lgVVNYSbz_DYVaXbd6a7tMiesUAq4QfgdXboNznEXKofx9p7b6TIBj7pSeOwDHZuM14j_Gmakz187uPP2qp5WM32Es0xc_iwYbgE_eR2_H1VmwXFaxQENxOZpZ3ofsV_JkeAItKdCKpExtx9QdELkV6k_TM4Zw45z8ZcixePENnke_JVQoQwg5yijZEXPXo645LB0VTuTwcOeJcviNGtdOzJ0Tw4YIRPEz2VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين   مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79946" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c558cbf6e9.mp4?token=ZkNRHSM2rr5PqhEzaotSOf6LCTFDpg_U_0gZVmSPkuCL-PRYmAv94hFyfub0J8a94CdhmNyLyOQCpqo-ZvBjENLCM0B5zb0J757KnE2iRoNjRfTdpxhspZ_i8GM_cybAKcqQm8ZDJLtoQfSd_bxQ5chaodE8QuN7YNn3RsPPiaX030BAYDZQ31Y8HIWV1DcIwQeZh1MaZTQ6VSChLoGI2WPOVUWE8jJW4mfLWEPiHMrZkdyf7IJcntHjyKt7lCeMihY29Wv2B8zUB_fczpCNHFCzTu2jA5YWtqM5cig33AKugjHZbdcDYaMLx3t31zair7mIxNQ1hewQ__uKztf7aopUrNiwuj5lEHLVaciyKRIRZ8jFLvUtXaUHm97nZFquYfgyXDAYt1qW1qKFdnt1yqEbm0ykSxiyzw8D27ZAMxWNe0txq9js5yDV_KaLuhyevSjXRxx5xSPQ5twqVJGW54pgfLrH8JGFUIo9eFmRovrQrpUDhbT3VifqXADe0exKHDxIB2fqceT8WPSTJr5oI-wrxCBvlQuJ-fjx72_W0lvhYDy-uVqfn8ILluZWpaGas5gjqfqxAplYCdv67sxXgh7BvsFW_bKUAUiSx_rj6D3_iXMfvgKLXaLcAZftFnecGsL6An0c6aOsKcTRZkQlnLndPNuAO2LO_59IGR2WFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متحديا الموت مثل اصحاب الحسين
مشاركة الحاج الامين ابو الاء الولائي في مراسم ( ركضة طويريج ) على الرغم من الملاحقات الامريكية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79945" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
استمرار الزلازل القوية في الكرة الأرضية..
هزة أرضية بقوة 6.5 ريختر تضرب الفلبين وأخرى بقوة 5.2 تهز باكستان و ثالثة بقوة 5.5 ريختر تضرب جمهورية نيكاراغوا، خلال أقل من ساعة.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/79944" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_ixa7o7fo_OsDrwbXf3VP4P_8khOrKh2goxFef_mTh0EHbc9ZOLzeQ9MGLMRvFHoxE7xS__HWp6IjlHeXlm85fUOw9XnkognSGd0vbWzdAfY3GLNpPK4dRGGXCD4gfDBZ48oesyULPZgdG4Ehpv8wFt8xbZMGcpBX-QOrHt_4QdHvPbP4hBTbvx8uxVsQQbLVtbUim2x2DVG2dm7n4qCyTYY4_mBSsWDmjXkk4bnop7bnJjCIVefQLycwu1BaoB6bBtJpxcHskSi1JLKkdnC7De3Snid1lUu4mHkKNBnVIJLFptUZRoF5uzewtro7-nD2Y-G5YGET8olBguVCz6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4tqdv4v6kveyt6IPA3QRO9bWnEKW1wjSKspFmbfU5psyy15-Sw6vBrkOkWrZtE-H3oqbPqc7Yc7Cvgn4gkxEJ5FMmn6z0pXHB4qeKxnxKs0uquejnx5LNZK3Dq-VPHj9kTUny9V_EPNFgaBafFrF4-yTjHZJ-u5JeLeuwTEKdC_ygplUyYuRCLQzduh40h7xSgqca0aumEYomPI7QFZ0Buzl90QtAioUMLBuf5NoivvNS3UayykA8I8Xx0rgSGEiR0z0q5gKZA_Ldr69WlD7zspaqadGWM4FdO-YAFN9pGaryHt5_MgdYPYGP4nN_D1x4b6Lr2HxTVgnON_i419ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnccruw24B75b-VZcaoetXqJrYHJl11z3ArhRqIA_8HQpFKGjRSHiNw7J01PLeqvf66S6RH0WrQRzjUZJxrecL7qBw7SKRNzHd5Zan7xb1wLfDpJMa7mztRinPVuT6YcCx6VruLS39m2NPYJZXAqVoKgPrpgEmriUCxHZPcu2sbwff9byO1zrOi9s0ShjrYzVNl4KbzV6iOcpigpoI1uJuxQ4qjWcz47maarvdAomZ_sd_apz01Zc4Suv0q0lC7J3IdMDa0L_p2JTpY97GB3nVBZxs3JRQ1yNe83rXMrlQviul1MSKXBvpU250dIKausNZp1NsCwjmHO4liGv9Z3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCCtSmdkpb_s7axGNv49wpZKNRmnyt5C3j4kvXcjFWmxu_qsi-cWlOAHBwalPusyI3pUFF6mH7WS63EQUTqbCfCrQQXlZjx804X_Qmcj3VATY56tmLR8Ap4BhwwQ-Sl1MgJZNGBNolaAC_ZlB78o9ZbF_wthjE1bE2k68iXN7c4S4ZBib4MGYBqntjTVtfMUB8NRb2q22GGDw770d8mURclwylSdnOdWSrvYYvH4hUClIkoRPQinoysHHWopxOndoYEHzJ9dhHdfMAtYseMQvhPh9ItFvzk3rVr1ws4i62616ot9sZLigbZatWYpBNHlnsxxIiF6GEDX6B0M8jRcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWFgqtudkJmhjH7Lotl0MiXrvQLUcUeKPXV4AfSKeL9PJadhYiDv_PbGcAVS9v5wpjlHSVriE4AoNf7F6QCaSgh1EHepOOaPSyDNKR9V2nyieuej-TUAVfyqGUX53WdPd1Hb5xvqv3FEd3MrI0VEJ2KSDZN-0zL2lhfAgriEowKE3XtENeLwQxyRc3gv8rJfXFbTya0SjJkFV_dJV3uPD3fOJ3PZ5hZ2dQmbam9asDVBEk5CR-WuvRH_TAySqv0DhRf8DCxYG9O-Goevt21-KgGunPq4lSQSH58WBLLg9YJhOQMVacwI2vptlszBuxyBWvC6XaMS8QikBDYFUsD4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxVdw5DBLaFQuAaB33LdB64UbvYO3cmPUDbsLGHU75I7YEem4MtwB2-lqjCG3oY7Enc4Eo-t1ia3Rdu3XOHWaHF9gF-3chcEE6YGZXyJ5lGh0N5vQyEVwiMI9lCIN29xLx27hpCUCjwkMS3J7lHg7dcBRhjehK9aED2E-MsKOl2f8iDqkbdsDGXh3JYa3fw7KcHCV_AU0D771b4sQNiSkSnnVQNSiPITM5HpIHJmmuB4FxE6li8V68Ylo9FZbSifXEMgnTCsSYjahJiH79QX7BmI7rICVFXfLB42xuf9WfeoMidvQmGwTD5j7O9A4j4vC1cTNHVXRHYtf1qw6LveeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
تصاویر رهبر شهید امت در مراسم طویریج در بین الحرمین
#قوموا_لله</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79938" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/79937" target="_blank">📅 15:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
🔻
تشارك سفارات الدول الأجنبية في العراق بتوزيع الطعام مجاناً ضمن نشاطات موكب خيمة الانصار في منطقة الجادرية بالعاصمة بغداد ؛ العراق هو الدولة الوحيدة بالعالم الذي يشارك مواطنون من مختلف الطبقات ؛ الطعام مجانا منذ بداية شهر محرم إلى يوم ١٠ من شهر صفر اي بمعدل ٤٠ يوم كصورة للبذل والعطاء وتضامنا مع الإمام الحسين الذي أعطى دمه من اجل القيم الإنسانية والاجتماعية ..</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/79936" target="_blank">📅 15:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
🇮🇷
مردم عزیز ایران، ای مایه افتخار جهان اسلام..  محرم امسال با سال‌های گذشته بسیار متفاوت است؛ زیرا بسیاری از هیئت‌های حسینی در عراق، یاد و خاطره شهادت امام حسین بن علی (ع) را با یاد و خاطره شهادت رهبر، سید علی خامنه‌ای، پیوند می‌زنند؛ در حالی که روزه بود…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/79935" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
ثلاث ناقلات نفط أجنبية حاولت عبور مضيق هرمز "بصورة غير مصرح بها" قد أُجبرت على العودة بعد تحذير من البحرية التابعة للحرس الثوري الإيراني.
يمكن عبور مضيق هرمز فقط من خلال المسارات التي أعلنتها طهران.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/79934" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2Ohb_ss40YxciPUcqhRkFcVu4mUYdT_JUL5XoZRwWnE-G-yqkccu-UtsgSsSrmL58un6OopFw3Sm1FQONJDSIp4efpjrUmMUDC-cf6JhU3o9dvP4C31_cBkJDgyad3vfy-8KbBCQSwGEtJL5DkFA6ZjXnLT8wWeEfrfOCPhuVrkBtoQzc-Flc30PLMfF9CkvLWm-q3rhh6tpHyeLtTn-2PvXPx3r3ZD_3y2180PCQecKnfc2HbOs5FY9h0HCchZ65kkS0bIGNG7pH0vTXKfjSzPjZKs9aaMVJgV29EzpFxIr-WJUPwbCYIZF2yZQrmRGrhIh2Syi3zZRtJ30byK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين عام المقاومة الإسلامية كتائب سيد الشهداء "الحاج أبو ألاء الولائي" مغرداً
: ما العدوان على الجمهورية الإسلامية في إيران ومحور المقاومة، إلا امتداد لذلك الصراع التاريخي، وإن اختلفت الوسائل وتبدلت العناوين.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/79933" target="_blank">📅 14:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إنفجار عبوة ناسفة في جزيرة راوة غربي محافظة الأنبار العراقية؛ إرتقاء 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/79932" target="_blank">📅 14:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9afd66d9.mp4?token=DWrxtTZjoTpXch2Gf9ymK0TP_2KOq1gw_IxN3G5HsIKUp9KM_2s0es3MrjSRFLjEDp561R-QfwpwUJhd2bpBc1sE_1YaBIYdEkYM1EvxOnbVMmdKFdbQEXehFU23uWFV3jU7pM1beYzQoEy4J4XhzFBwY5BTVseZDOQtN9WTJmeonQjv-kQF2oNfc4xsuTMOQlVeBIRCGLd0Y-uH-j64MgBBEgOluTYmavpDUOAblp4ce6HaKPqSGXX66jHZ8QN4JVyqKZ7SBTvfcSTcFABca2RyE9B6n5-d61YJEI15BG4SDopKJijwftISmr_GFDamqLq9IY1kqleS77mcHo3mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
هاليوم هاليوم نعزي فاطمة.. جانب أخر من شعيرة "ركضة طويريج" في منطقة بين الحرمين بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79931" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fc449821.mp4?token=NkBkjqn7GOF0OU7tWOkQ9OSlurDs6AdeoTEVVg8PNGYACcetKyndzexlYpxBHxvJq0TGJB0DNZM3fn02Y14d0uCz4NdLd-qbIozigeZf6CANNWxhaZfNwQvK6NO4ON4-VviWZPPy1lBuMydOivIqSeVOFmnIxZUD2LLKD2ciPHXv5X8c9XTMkov2YvVXcixnroetgWE9S6gcy3w2yNgZk3Wl7_siLAeWzqGpKGtJKU9VXZYJFua_ZfUuxTjRX43ThE8n7glsXbv_1UPfooGydAZInYHRPwTinJljx3vg6WNH_O6isbAcU68u9ehNK0ELGjOugRep9XUlzSDngfSirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من شعيرة "ركضة طويريج" الحسينية في حرم الإمام الحسين عليه السلام بكربلاء المقدسة، الرمز لنصرة الحق وعدم الحياد عند مواجهة الباطل ويزيد العصر.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/79930" target="_blank">📅 13:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1329577.mp4?token=iPza16SUSVekdoOK6srdVaxt9lS1JekSmhhosLrm7xnHQI31B1TbYwHKSchhJ3Y7XD70mQxSzkpBI1imZ1COH-7h5z3gZhfwoVrJyjCde4Tt32Xe2TVmPUW4LmKfxtjnjy9lx9WqoHLPrFZ3lOp-VRZe8BsS4DKp3UwWIOEbmlzjBmq_ya7Y9f_E-Tlj2tjXaD8aJD6Qo0oB34cNbFBkUkGWPJzJIqEU2TGGfx3ibUdeG1w7VzCH2l-eCNCpVptVZLzFM4_7D3oky-gKwpVsI6RndqOtLnQ1XZvQKolb7I1qYZpGgWHJWOxSzsSHlwWkubWodAaJqMdMsTGhXKBEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايةُ الحشد الشعبي تتصدّر حشودَ المعزّين خلال مراسم ركضة طويريج، في مشهدٍ مهيبٍ احتضنته كربلاء المقدسة .</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/79929" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/79928" target="_blank">📅 13:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2776bed0c7.mp4?token=mstoZuQd0WUn_VB5waYqWh8d_ZSsdZ9n_Ny4KdJ5VvAMgyq0iX2-yyd8TZM09ziReOGr53Ee0Rqi8SSucISts5Bx5hX1vHlrwxsE7-JJR1zmks-FJGxnlArCba7KLk6qIzgWJKEecHSPSeTrDkDTDrqdaiVwqK_YCYi_0Si4Z5ZAWghi19YZ-fDcP20dvNcropHhkUfVyNmo5edFw0jMDoJnCFfuxShZQZfPwLtCEdD7tuQyM_3Gnm3_tiSxS4-mezuMEgbI437yddIdgX9GvyVkJJOrsFxl-Zuyyrd70lrOxeqaHGOI0Fy0IEtoHgtFyIu15uQ2fHE4x5gTJ85WYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من كعبة الأحرار.. رايات محور الحق ترفرف في حرم سيد الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/naya_foriraq/79927" target="_blank">📅 13:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79925">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46bd0c99a.mp4?token=ZEVzrVjlxEAbamRNrBUpqlQR31clOp9yuqWgy1uEHF-WU6ltASD7Um17sc8-gNh7KxVJ2UPIy2pQ_vECSGHwImUU0M8JBIKnqcFWQQUwPY7YwXP7IZzr2bTJtvyhpEC4ocotzxzi00GhgZERo1MERTtLF3aMrzudnJo9yqCdRxz7KUhxk4GBSsEXAN5fCPeDkbXmZsxx3DpFCLepW45XzZkXc8eIdK9nBerSrXWESzAu0nGYOn5KimpWQu5qP7Rr26MMa9jsokobaRCDc9sRJ3nL1o1F-7L74NUbpu6p2QRYqffnSVxX_r63ngWfcuiCXFZT0TiAQK2pqno8h7QTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
حشود من الاف المعزين تشارك في إحياء شعائر سید الشهداء الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/79925" target="_blank">📅 13:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e68c8ab7b.mp4?token=QNhCJYx2WloQy2p0ejwPsnbX4d_3qjo46gLGpKLgWgW_iTWrbYdFvaaMOFYXdg32d42jYmsMOTL79B_FMV8ufNCb9wDU3cc-2_UKNUZJ8BoVv2k1kdCeEkghqzl4rpLRLf-PhH8dAbv8oSYOb92J-Ylhuf0irC2iVWbTf93dbE1VaOs6pbnDc_M1MOZUByCK6KkZxE-9GWK0SAKGyI99Aypr5oeUB63s0cSpRiR--47UQu4Mcw4AZ80Dd3If9MoXwsOrjtDsP1Ca98FagutcmFFqF3zi5g3qRazahbOsAG7-2J6qdBQqtVFJOqi3Lu5A1aNVgMGf-z9zuBARvnyrj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق شعيرة ركضة طويريج من كربلاء المقدسة بمشاركة جموع المعزين.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/79924" target="_blank">📅 13:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79923">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00048c27b.mp4?token=cXxmdUC9yLkD7wF7_GwgnCQUkG6JKZZWtTfRTWtHsHTRCp87mpugbfLtqgCuwnUwe6ExGqdmxbmiW8q5nNBQvDwd62J0flWm6KRNNWnV_D9A1HjUw3YtJ-kEjKkGuW-G_EoLblmoWLNQ4JNHEA8SJzjvVT1-Lmq9w4nkWgWE0L0Dnzn5ZHB1Ie45_D2rXaejVq1sNUnoYlvENTRKUOa7IbsxxN_Il5mEmcfKEpYYhCslvjTMP4SlJ-w3s9-rPAMqgEYAb5xabrMqpF41Eeb9uCFfUP6PEGaTZMgDz3vpF9hpw13jJeqbggg3myZJi4wAGVU7mzDD5NbXO_zVi1Yb_zgpMebrF1MJOA88sn7WyQtsSwC6zXu-Z9PUhlaZ-RDGiAs4kUnIKPq6y8GQ6mYFDmotuMmEwGkJAVQ41xymsUH1zTvVALbmgiyg7IC5RE4ZHvRo7i_gndJC-3DrHni-G4GxuQeZOFUsztshSfHmmgdHtAOSBc8G6-sSiEdbsSfqTNqmUXZTKx25XvtWX_-nLGjQzlOcV84ErfL5FeOZRGWhK-pvMQpEhx41-zVLDeF6jqFT7m7MpA6dBGZVfN_6ME9vubWRl751gw4N4bm947Mir0CwtS-0xewB5Ss354emhwyRQHeVGonml8Y1NAYhti6MmS4cIDAirPuiOyvCCm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/79923" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM3VAFkJ0PCkQfoh6nh-S05mMKB3ZuhyJpO0iwS_Pj0d6v3ayMLtSj0L7jWqrprImu4kSrJcIPs-XvUI7I3TgmnZuY_SnSiisuYApfhqf3Qzk2kXkuSTr5MpAL6ZepDBaI0LZDHtMuOGyxB_kKjUpBxqWfTU3_7NnaeQxB-hQ3lar6UKWFsapT5w_FpxrbvAwiJyuSY5IZ_30BL-11P6UuzNAyOXKSoQ4RYOpxZ21d97glTVXnetCtg3_StKu54QjKr7qdayNwP078FhEzdX_SWLv_lWaiz-GDYUFW0WOaa-_oZ9PLeiQ7H1zArBk8tkAX9_i25TuaSidce5-apbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انطلاق مراسم ركضة طويريج في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/79922" target="_blank">📅 12:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79921" target="_blank">📅 12:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEe-wqUY7fN4NflqM7CIreZdh43ju413muvemM4oR5CkD5bNbsIOwG86Cl5ohUPC4jH7FCBGjbrzCL4hketlmqMFdQQSG2uMccDOwSVj9dJPCq6jvQt92znU-C-CUEzULtMlx9nczrifkKFj9rhFvOZ6qwma-gsoz4eFhxdA5e4R7vawnRSuL2BCHJqUvSSdWDZaa6QCXm5kDhDoAQBUd3o8cPIQfEQ3Kqf0H9cukdHk62SHQF19YSGLIX523wc7wvYyPh8kVzQ5yWk0zeJzKXfH1xtX0HxAq-pl_LAqb391hWoOBbZlcl0Mt1fsqp7l8ZnXdMCx0OD5H5zR2TQ-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم ، كن انت المراسل وانضم الى فريقنا
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/79920" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0-mDi-UN3NIhOwMpw1OLcYhNEQOwOGujvac_HH0uPFptFMdDazKQzqu-tTch4MLPzs8VWfNU7javYXFy47bD7ddCElYdYOwZvF5r0E4iA9kLVo1Pu79_a9Q6RGCstzArMqbuInMQHZS2Mtb2mlBXSwkZeV86TbmDawgM7p1ke3JPVQ9-hmCZuQy3yMP3HQRAOJjmtoXUhLrvIeEZfJVr0AhUmTS7H5ZSnulRJY88_a7x5lYyrn6Jj-WaOS-B78rKXtkFk86V-1Bn1r5SWD6hs3gFaRt_ZWAWypz79S-lSKLTRfpQN3AvcGuFmL7qs8Wm7RRwCutRkoJs4_VH93krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQJTEOrvQydf3th1DmyaksAtwDbmNL21hL7Vj7YTtr9Mchu73P6e3gqkSqRuoVt17nXNzoWnCqRe4cZHS4rmryELaGS2FFVH8jTGGIrn_nW9QqpKRNYdTa-JjwYpDc9eG_TT99L6z08jC3zZfDhjanBY2jRZH7h6pCNncwcPFC5XmG3h4FknZBR9ScYtGl2oBM90WZOBmTH278avCmTZy1NJuxSKtmlYZ5HJT7WWVxhWU-ONzvdHl6IwvHdDcJhSNsYWq0Tq0QY6x_AovnVczXTlx_TKIg6b8B8f72y5IvQ4fKL_RrNJbCp-EiqRD02nOapVZLZ-DD80fIWaC8RjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeNBT9A27YmCSETZt30k-_sA8hnU70-19YEOdYCIjB4g3hltrOKTiCcXGP1JzOxBWrPsXq7lGl76tInTaoP_eqjqTl3IZpzC8aurIL481IGrAH8kNzbjnhvRIT8vP4GbJwS7_E88fVyFTr2gEi5LtYiTZVrk8eX8BSytP3wZHWv7kQGCtLCMjt9OU0EckSI1ICcrP_W6qvLdNtHjMFxz7a0_qMKguiMIRiEAocbVpRUpS_NzZeIejsAhLmfvp7m_-7AXC-yENHJs2XX9rVnasCsW8kz5YrBRkDz4_TU61DQlsnKGxatOYq-L8RlMKMwp2pkIIyWPMlCCWEKY0olRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zq36gUR1ELdDV2ptKab9id6JgiqOroTMPehqBlIT7BhQfF3A_T6DX4PQ5jImKakkS3V2FL9PRZ_m6AlL67xdR8QYsqMNxm6hLVyEMtMyaTdyhYMI7BrXjooOV6YQbEdpq77Zpro0EeAosMvCIQ7-bmyI9OQSZAkpooTWi7VtLId325HMzKa1DLpC_j68rq8lCVFufL8qg685xVtBZlQ2832nyqlVNz4UJXMAk4ChfEqZYr5N3rQcALDeyaNkCCfOpA7Bwb2QcqC4-_OKp7HrrIrx_Hler9vx_zHIZIbp7rrAo-81oWACmRs_zIwY8qWQwcXFI1xhkZ5r_yWcGFinbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد إيمانية من داخل العتبتين المقدستين، تزامنا مع اقتراب انطلاق شعيرة ركضة طويريج.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/79916" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79915">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=YHL-_CLaz96jKvlRD5QpZAXvnMsNXPCRqLAHpvm2IQfdFniFn0rkIVnR0ZCdhD3AVdlr0q22cZBwsOlLlyajI7bHwgCcraNToRlZJb7nw18xlb8zFiStlhUqoMwIGmlcilsA20fgS2FhYDOApgR2gpxoAnH5Hbcyoe6ayRwY2k4i90YfAeoI4I5R1b54d-i2nkWmavU-qlkdva7C-4rjhXiDjL1ZcF4i4tV58prnT1drJ8vO4ObNlZqtljFMP4bRjNs0oSU6XjB6fqXAzgJi9slPYOQrRYsCSBMxnDTmE6TLfACPNBKSjaED5d0QZsFl-3VJtym_E3EP4o2_YZixwhnhEMIxneP_iSXIM8plxsWkey37o-7DwgOfltyB6gO-hQ8sdKvv9SSYBJ0ijIYeDeRxzmV2fG-OoDWziqknchm5EBUC4jvnwP5KjeQvUsCegv8ZZ1E8oYibzgLYblCCF5UooRxEQ3BOZ4b5GaT3parcX9xM4FT7ya90r9lcQ3KATcYWGpmGkcKypq0s-plIfYAHGZyQeov9j5C_tqGvVJDHDmST5CQKuwlzJ0kaNIyykKuyiMe0CUcHmEpD96wHh70W_qDI5Bc-457JrnBDmLn81LfVtnoogV5_22bXg6Nhm7nCTKWMjllJCE84tL2m2IHVm1uEHCZzRR38ZFNFSmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1beabe075.mp4?token=YHL-_CLaz96jKvlRD5QpZAXvnMsNXPCRqLAHpvm2IQfdFniFn0rkIVnR0ZCdhD3AVdlr0q22cZBwsOlLlyajI7bHwgCcraNToRlZJb7nw18xlb8zFiStlhUqoMwIGmlcilsA20fgS2FhYDOApgR2gpxoAnH5Hbcyoe6ayRwY2k4i90YfAeoI4I5R1b54d-i2nkWmavU-qlkdva7C-4rjhXiDjL1ZcF4i4tV58prnT1drJ8vO4ObNlZqtljFMP4bRjNs0oSU6XjB6fqXAzgJi9slPYOQrRYsCSBMxnDTmE6TLfACPNBKSjaED5d0QZsFl-3VJtym_E3EP4o2_YZixwhnhEMIxneP_iSXIM8plxsWkey37o-7DwgOfltyB6gO-hQ8sdKvv9SSYBJ0ijIYeDeRxzmV2fG-OoDWziqknchm5EBUC4jvnwP5KjeQvUsCegv8ZZ1E8oYibzgLYblCCF5UooRxEQ3BOZ4b5GaT3parcX9xM4FT7ya90r9lcQ3KATcYWGpmGkcKypq0s-plIfYAHGZyQeov9j5C_tqGvVJDHDmST5CQKuwlzJ0kaNIyykKuyiMe0CUcHmEpD96wHh70W_qDI5Bc-457JrnBDmLn81LfVtnoogV5_22bXg6Nhm7nCTKWMjllJCE84tL2m2IHVm1uEHCZzRR38ZFNFSmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/79915" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b196168a39.mp4?token=lNED46bMQJ5egTvazsdCsY0AN79lJnF6T_jg8Clbu-iELRl_pWPnKmoNbHxvHcdzv-zyJJSRczz9LfQkxeLATIejoosZOcebhwODxKKapkMjjMHY-thurDm9Q_hHubZLuS-HttiFBKf8UXSfs52OsmvcIFMvrY_tysu84YiuDC58R19grv1pwKdvQsKI5iNFB-DO-X0LML80PdqB2HzMMYVLzaxBj4eO7UIcbdJYSWKtdAIMtV7tbAQSxMgxzqYyuObpJfafX3vDVoQGfVFJ8uMZLx6Q61zos89NtSHHl5GTaRW2yd546_wQKv2dHFPHXqL9QIlviWI8HnXR6dqbBwhE17Mp9BguYi4_oJIC5v-du6vCwSXlIlt1WTLNeyx-T1JqntayZXrgQ4tv80KE3Wn2RMIEfZ1qSsqttqE8h9GTzXcYLqXBw7vfgRQj7E-h1hCBUviIRnatnkeMzOuL1nwcMKTO4slA12Tp6xUkDQbk_B0HPPHH9H6pldPndvAR7BT532Crwtx9PEPPqjqv4R-YGaJuxgfKnOdu-9NpxbFFWExmjton2I_JVIId4PkhCMM3BYHRSKbzXqT53oqgnsT8PM8sne0xBCr-tGFWiB2nIBJ9zAaKf0HmZj2znDQxc7s0mf0pLeDDSJYkTJQMmE6G5lEmDDdrJZhAXIfX2gU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الآلاف من المعزين يبدأون بالتوافد إلى منطقة انطلاق ركضة طويريج، بانتظار الموعد الرسمي لانطلاق إحدى أكبر الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/79914" target="_blank">📅 11:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk3xP6sfAScrCOCZRmk-IHHe6urRVdvK1-SOLDYqNL8Fzw3HgHeO-ZCq3lktU1ZNyD398hUOnw-Nt-qk5LgnavNpOPxbNA0HYUjPCGzhrz-vpufYUwD8wEv9G7fp4-6p9vOBujA8JnXaazVJHFAEFikpD25_nQ7zbPmJTJ-0ehjVPV58zz3rh_B-3qgpOfR2kWaDphu4oT6UzizXmbmnbQswYFoJq1kXwqfXBi6raMYIVFus7l1t7lDhR1WqGgTdSOg2XYUgJlh7p_sDwp-UCDEcsgkrz3bwCox_VFf3k0_-or5gd_waR2WFnoGjFe698GfNTZ-tOS-7pRLms0JAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية بشأن البيان التدخلي لروبيو ومجلس التعاون الخليجي
تعتبر وزارة الخارجية لجمهورية إيران الإسلامية المواقف الواردة في البيان المشترك لوزير الخارجية الأمريكي ووزراء خارجية مجلس التعاون الخليجي - بتاريخ 25 يونيو 2026 - تدخلاً غير مسؤول واستفزازياً، وتحذر من استمرار السلوكيات العدائية والتدخلية في المنطقة.
إن الادعاء بـ «الالتزام الدائم لأمريكا بأمن دول مجلس التعاون الخليجي» ليس سوى كلام فارغ وتحريف للواقع. لقد أصبح واضحاً للجميع الآن أكثر من أي وقت مضى أن الوجود العسكري الأمريكي في دول المنطقة هو عبء على شعوب المنطقة وعامل لعدم الأمن والتفرقة في المنطقة.
إن استخدام أمريكا للقواعد والمرافق العسكرية الموجودة في دول المنطقة لارتكاب جريمة عدوان ضد جمهورية إيران الإسلامية خلال الفترة من 9 اسفند 1405 إلى 19 فروردين 1406 أظهر بوضوح أن أمريكا لا تعير أي قيمة لأمن دول المنطقة وللعلاقات فيما بينها.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/79913" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم: - تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.  - عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.  - سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/79912" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
أبرز ما جاء في كلمة الامين العام لحزب الله سماحة الشيخ نعيم قاسم
:
- تعاونّا مع إيران في فترة العدوان وكسرنا المشروع معًا.
- عملنا كمحور وشكرًا لإيران حتى يدخل الشكر الى النفوس المريضة.
- سنبقى مع إيران ونريد أن نكون وحدة حال لأنه تبيّن أن قوتكم مع قوة المقاومين في الميدان تساعد في إيجاد التوازن المناسب لكسر "اسرائيل" وطردها من أرضنا.
- لا خيار أمام "اسرائيل" إلّا الانسحاب الكامل من كلّ شبر وأرض لبنانية وإيقاف العدوان الذي فشل في تحقيق الأهداف التوسعية.
- أيّ التزام ضدّ سيادة لبنان لن يمرّ.
- سقف السيادة يمكن تحقيقه بأن نبقى في إطار اتفاق 27/11/2024، على قاعدة جنوب نهر الليطاني حصرًا.
- المقاومة مستمرة بوجودها، وحضورها، وقرارها.
- المقاومة هي عماد استقلال لبنان وتحريره.
- لا تستطيع السلطة أن تعادي أكثر من نصف الشعب اللبناني.
- على السلطة السياسية أن تعيد النظر في مسارها، وأن تعمل على جمع الكلمة، ووحدة الصف والموقف في مواجهة العدو الإسرائيلي، وأن تتوقف عن تنفيذ إملاءاته.
- نحن جاهزون ونمدّ اليد، فانتهزوا الفرصة، فالمقاومة قوية.
- هناك ضرورة لشحذ الهمم، وسدّ الفجوة الاجتماعية، وإعادة الإعمار.
- لضرورة الاستفادة من مسار التفاهم بين ايران وأميركا كداعم أساسي للسيادة اللبنانية أرسلها الله كهبة.
- لقد ثبت أن إيران طريق الخلاص.
- كفّوا أيدي الدول العربية والأجنبية التي تضغط عليكم للفتنة ولمصالح "اسرائيل"</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/79911" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=JG8bUcsWDud1OjOro0zdg5zfUeEhcXbpWvwPsZcRTFywx9Rw48waomP-5iPBU9kbii5RVTDazbsAlWsERTWzE8kDkmGaLdwqdTAgFrKbRoqzPyZ9avQtrkqCxnP8pYQxIs37aFsYOLQDaYaM0iiBm9DZ_5wVbhvvi9cwGg77BPWoI_HX_aGUHtB7_Z9hXNmx9_Ql-muP5ZfcOW9EsuPhmy9heLrPDbFgL2GsEUm2OWSZPVRVrv_m16ks5Zq_WiokSg9fGX22x4COtwk1t3Oqz4jQ06rv3eHOEjWNpzumafRgEh0vy_XYHZqqODj0o1_nNQlpnltobjMBqo0AuQh-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe1d0acb8.mp4?token=JG8bUcsWDud1OjOro0zdg5zfUeEhcXbpWvwPsZcRTFywx9Rw48waomP-5iPBU9kbii5RVTDazbsAlWsERTWzE8kDkmGaLdwqdTAgFrKbRoqzPyZ9avQtrkqCxnP8pYQxIs37aFsYOLQDaYaM0iiBm9DZ_5wVbhvvi9cwGg77BPWoI_HX_aGUHtB7_Z9hXNmx9_Ql-muP5ZfcOW9EsuPhmy9heLrPDbFgL2GsEUm2OWSZPVRVrv_m16ks5Zq_WiokSg9fGX22x4COtwk1t3Oqz4jQ06rv3eHOEjWNpzumafRgEh0vy_XYHZqqODj0o1_nNQlpnltobjMBqo0AuQh-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ازدواجية المعايير في ابهى صورة لها:
في الوقت الذي تُنبش فيه قبور الدروز والعلويين في سوريا تسارع جهات سورية تابعة للجولاني إلى ترميم قبور اليهود خشيةً من رد فعل نتنياهو.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79910" target="_blank">📅 10:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79909">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء:
نعتبر تحركات ووجود الطائرات العسكرية التابعة للكيان الصهيوني الإرهابي في سماء بعض الدول المجاورة باتجاه إيران عملاً خطيراً وتهديداً للجمهورية الإسلامية الإيرانية.
نعلن أنه إذا عجزت الولايات المتحدة عن احتواء الكيان الصهيوني والسيطرة عليه، فإن الجمهورية الإسلامية الإيرانية لن تتسامح مع أي تهديد يطالها، وتعتبر من حقها الرد على هذه الأعمال الخطيرة.</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/79909" target="_blank">📅 10:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔻
مرقد السيد حسن نصر الله قرب مطار بيروت يعج بالمعزين في يوم استشهاد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79908" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcnMovozaGC89p5YQ_qiEkmk1VMp8pmnGNql_sF67NL7mNxzvi-SfN5vV5WylpEBQgc7DVel9jOWB-yD38hL-w4BuXufyJ_k0J83EKIH98lA1D3HSFpvp_mFRYdFsGptuxtq8gf55bmrzxqif3O2SJH1yO8Yjjz_Zi4iSSafeznXoMRb4znX6TmwCtTNg6heFjlbVDwZCi33CRGZkKrbrAbIOdrJd5vpVnxSfso2taWAZ89LAiT9LQ_YPsxYOzpAw097NHLulfRYY5Dw-h7NJapDx1QdNcQT4LcFujVbgRyL7G_E8slkrQf2RaQOMsegJzP00tFb-HfkAi2rC6JyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7yLXN-FQaGcvYqkj3745p7dEsZHuSE2CDTp2y7ChucuJ-REYKrVyp_B3vdnmwt7A-TXwlJopoiUAO5aZzXuSXByL9-XsIqRhkhMdFvhXlReivbz-0QolLvYsO0Fxq2SwsqEZ3w66OQ7nowKQ5ESVpZflXTyG2NKOBtgqKIHTByyPm-MWSQogTOm9hK5uE3caefF6iPixDvaZJbOMlbq9g92HV9RJczNQSxrXyVMUaKUJaKiRTVI6SojF9DQ9SBI2Vo2YtsiBDaSt_D4hzLF8pUFn0VbL6IdcMW7vVF0M9o3a9wpB_vuhytOtsclPp4HByawjL5ULIgRvJlGV3C9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXsCuDbPMR6b1HDV1ommX6gJkPJvgNumuT8Sg_YpWg-rcfmXQHnWDUIqFGz1i-3wJiPPosXFFvACIgZdCtag7xRQ-BaU6lCb9k4Vp0Jq_MPHXNnBh4_4uMDfDsnkGAZsYMzv-z4xcSX8IPxgmE0naU0P0AP6IbETzVAyX2Th0reueSK3VYP6EDomi5ABxvFRbSxKqD9Dbvujhq78E3vX_cae6aQvSxsaRZynHkDXPLU2Px65ezD_sXk7Kr7JorCGTig2vlLID1vcY5jonEbeJhqT0U8Prc0Cg3AmxBTPazGOaUrPSc3mQIabaqZFM3Ue3mtarpwUh7e1v0Q7FIySzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جموع المعزين في الصحن الحسيني الشريف بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79905" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxqFMOkaQP1jTCoFjk3pAfOU-OR8QWtxoMfVLHUQe5IsChu8AKHZyGUIkEB5OgtmXmpeyYBrxe75e4UlyRiZdt0a_Y8azGSuK7-8cN8pcPrifAqG7QSOrvNktjcYv9EgF2n1kRpJi0Ohy9h4kLFcQ_BwkaT9i0x6wkEyxNQ9BTAuSUpJD0shBnaN3xqXP2JXmGps0XmxmPw0u5rOGCWnx1wdCa8ZdOe58vGrcHQ269kWbcFMJtIKj6WXSOu1z7CrfK1dSAidLrl_twFdai7_rQ7nXk91hPHZ9Mttx3MVxjKtzS6XU07-RVD9bJskycze-NPH8VtROW4KYgtKkGPGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
أربع هزات أرضية تضرب الحدود العراقية الإيرانية منذ صباح اليوم.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79904" target="_blank">📅 09:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=FhR6-arioH8Jv5ug5R3PHRjAakkdQkpNhldinps_6bskSQ_n9QE1YK_wGJiSa7QK0REuhwjH80GUgaonpXlaFiv_dXi52NzO1eUrkUPFWRuoy1UcqJajtuv-OMpcBcDAX3nyAQw70yk8iSZ0rWGd171G_oS7SIlddlWliJ_IoxWZdVsgmowl3akpE4RLklG9l8qI3EJ_C5BwqY-_LYubhbiwlW-sdFFn2E1yqX8f_YYY8J6g8MpxTTN4WUkLYdyU81tPkxBITVJmXcpxTP_fSETwWjxxLx6gAAZvA5yQQP8kv6kXqhDBuLx4x9J_PXqJAKb7lgJaSLTZ0cWE5uPWRIQr8JiYrGyUkrA7qa5vNUK0V7ELr5W5ReuZMcZESZxWkcYW0SZMD6DnnnZMvpGgvDIEc7lhFpzVC7x_OTGRasOaqzTLEcrR_92X1YTH8UM5hV5iBifxM16ZiSua_QcP1lrNj9XkuUQjB689x-LPIkk2LYeq6nphkVvuD9YDEJlWq2cwIfubPUi6fdfotr_h8_Vns0ETxiYnEoaGFTYNs4EBmiTOSh0U9vLwVE8t4A-S4i6OnD-amUeOY81o8w7BexCk3bNjmTv8ndwipepVPPW9ezeSqRHMHWLM4s4U-M47I9e6l9k2GlJuNxO95iIw6ulgEQVdBmT2H1UGR3HAG80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5381790f.mp4?token=FhR6-arioH8Jv5ug5R3PHRjAakkdQkpNhldinps_6bskSQ_n9QE1YK_wGJiSa7QK0REuhwjH80GUgaonpXlaFiv_dXi52NzO1eUrkUPFWRuoy1UcqJajtuv-OMpcBcDAX3nyAQw70yk8iSZ0rWGd171G_oS7SIlddlWliJ_IoxWZdVsgmowl3akpE4RLklG9l8qI3EJ_C5BwqY-_LYubhbiwlW-sdFFn2E1yqX8f_YYY8J6g8MpxTTN4WUkLYdyU81tPkxBITVJmXcpxTP_fSETwWjxxLx6gAAZvA5yQQP8kv6kXqhDBuLx4x9J_PXqJAKb7lgJaSLTZ0cWE5uPWRIQr8JiYrGyUkrA7qa5vNUK0V7ELr5W5ReuZMcZESZxWkcYW0SZMD6DnnnZMvpGgvDIEc7lhFpzVC7x_OTGRasOaqzTLEcrR_92X1YTH8UM5hV5iBifxM16ZiSua_QcP1lrNj9XkuUQjB689x-LPIkk2LYeq6nphkVvuD9YDEJlWq2cwIfubPUi6fdfotr_h8_Vns0ETxiYnEoaGFTYNs4EBmiTOSh0U9vLwVE8t4A-S4i6OnD-amUeOY81o8w7BexCk3bNjmTv8ndwipepVPPW9ezeSqRHMHWLM4s4U-M47I9e6l9k2GlJuNxO95iIw6ulgEQVdBmT2H1UGR3HAG80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً  إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79903" target="_blank">📅 09:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2kcMGMZx84sPC0a8gs5FUFOBlxB8Vn0Z-Q_S3tenID-YXb9iF01rQ8rziaOyX_0E73z3svIeAqsqlMyenfV0Rj_JVm528oJzB455cYmml6NhEUKuKmCPGv5ywKlkMXvjaaBXu6GdXTvI9wy577FInuTKyKkDccmKoSsYPJhzjYQYKYIKxHTj41DqRXHSdWF2KnVGH4g_lwR7EQmHJw-fcVKvtinZctRsWyG0TwsGBcDVDRi5khv-Zbv_yUjtZYA0gho0Qd4CHPvmREu9zdiCZlAFbjuY80N7b5pIOlXGdDi9tIo_RBl3u9-m8Hebc6PPB9kLh3wno2HdWPfkSXBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدة نييورك من احد المواكب الحسينية يستذكر الإمام الحسين بن علي</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79902" target="_blank">📅 08:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtLDGQ3j6Q1wHcBxqCOU7BjuBoldPg-yzeQKKLLMIGh8faqndp6HbJ0wNbHMymWJdL-DmySidhHU5OcqYWI1JV23p_wi8QajDjBTHZxBjy0QsPl0wo1QTV4JF5Jnufpug364d-3zx1t3o2kZ0oqZP2jTlOzmMHJW3f5tBY6-qi3OhpNGqzelh1_vqmA-u-7QrIZxykqMs9u3d3RvoMh3BwTBNdSX03OQE86ZVAeFyfP8kBJaePOCzQe_cpFuVoni6Z-1oDyK6fVhED1bIi940EFOQDMG5vvXX9uSlmyO_zgT88tEgG1W5U7v5-gX-BrF-nj84yfdSTotxB12El7McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSph3NxvJiLn_A-Iutvh2Saa83Lls05tdHBV9Esx6O0sO-2uCD_Qy_8IVPlrq_B_I1hEBUH6VvoeK0EbblBJUVXin7B8KDD6Fa4WPkrArf63YzgbnRjaRZYR9lHCPysNOpCNFQPS3tIHJjfE6yk0esPudmfqw77z7_ufeJytrmwKPqXVQWY9jfUhQlN8bp0xc7gSst2v73M0NCEc6-nR2au6HYe7gWlWX27vdzEWgJAq53PEJIzcx_oe2SCA4tGi1J36Xli46lnQSS3MHhAFCwjUV-pj5RP99rNS7mqvumn-PIFHBk76E2OWYCJmHAvjsSJnLhWco1FU8mRh3qtvBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇱🇧
🌟
رغم إعلان وقف إطلاق النار وأثناء إحياء العاشر من محرم الحرام.. غارات صهيونية مكثفة تستهدف النبطية الفوقا.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79900" target="_blank">📅 08:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgED-f2Do4EQZqwznkMrg7jxygNHFtJARXBydVPmYVCuny-9_mQ2Fn9ALV0B-e3mOq50_02aMWDptznbNcamz2HND8BkZp-1AxqjuDFA0tjI2MTi2G-1v58f1u4n9k6Y_G09Jhg8js7zwhiNRWs5DCNTmMgnO68rC7USrtE1kUsaBi8R2rmO6zw5B1X5B079eMqBrekHp8Vzj0llFeNyqJD6IlRgBQ__mFjr-cslOJkHhaGODCtbiTEoaWljE0MqYnXXuCXXqAotZKAteFiSrs1KlzXYCli9nC22C2VrGbHltri1htdTJudqAYAgWqr4Ce8TaiP1sx_rAWHrN3lx5-ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0ffd4d09.mp4?token=sD1SvOgAMR2u5ZBW_wUopUwaL6alBGOKiGlO_GItwNZaGOHRH2mYnFJPgrGJqiQYyl9PU-EUDbAPddYcj_fgVt73M4X09GTIQfA1RE50v2KMCdIs9ggMtqYEsbrjS18es1nqiese0xUSHQ5lkaWnUg6jg0kj4Q53HLeTSZSMy5InlAihXHl4VqAQObul80okjCtMBzB8HPhBVVPFplDtHnChbuDTJGX3EhrXILpR1JXcQHSAzyto3X3OCRLfDHJC3R9diZoW9kvNjJDuiR-QLQSe_V0h_DIvg2u1hFlxDQuf1AzeSR5EReaDRTsltJmyrMCaspNtA4WHFpTHNrocgED-f2Do4EQZqwznkMrg7jxygNHFtJARXBydVPmYVCuny-9_mQ2Fn9ALV0B-e3mOq50_02aMWDptznbNcamz2HND8BkZp-1AxqjuDFA0tjI2MTi2G-1v58f1u4n9k6Y_G09Jhg8js7zwhiNRWs5DCNTmMgnO68rC7USrtE1kUsaBi8R2rmO6zw5B1X5B079eMqBrekHp8Vzj0llFeNyqJD6IlRgBQ__mFjr-cslOJkHhaGODCtbiTEoaWljE0MqYnXXuCXXqAotZKAteFiSrs1KlzXYCli9nC22C2VrGbHltri1htdTJudqAYAgWqr4Ce8TaiP1sx_rAWHrN3lx5-ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سيد شباب أهل الجنة شهيداً وسيد الجنوب السيد حسن نصر الله شهيداً وإمام الأمة علي الخامنئي شهيداً
إحياء يوم العاشر من محرم الحرام بجوار ضريح السيد حسن نصر الله في الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79899" target="_blank">📅 08:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=JDvEybBQ-hHCdOFTAAnJUhhdcmX5Wd91C8PJPYsuAEo3hGt3ltna-HhSlDUGDgzkA3fmfR_TWSoSWmU2KZGHhChy5h93IOYCln8Ds4W3M1Q6W3S_w7JHK5jwtML6KzUKevLf7ijSzqkc1yDidxraHFmGGbpjoMG-v2DJHYX3D4M0sHNL8q89V5_iDREduHS8JPFxxqwaXugRs-kcdvj3ET9e9A_VO_FmHhG0klbQb_cIa6Hyoaymct8VzoqfFrAsAJB9PtLhZYP9l5yBk57cz8gsgYIX5UXvMwE0Ap098TAzkCet4J9Q9nb0NvQCIjXuMbiZrcIB3sE-bWe0DNJA5ATFimqsLyWuBNN7NBy5yYj9pinArDw-0nGE-4cjygep3hFlbTj3XGkwAPrHoJid6S6ICmTchuX4i-z5PfEb51fiVyFEu3711a0-sPC4WegXRs30JdR4xwW5e1lIXr-slJ2HKUabQICDyupfJfdHpuStEeI0JuSf8jVSweGmpQN86P6v0mnNAMM07AD_-yAz8NlZveefgQsMg3GJPNA0xk4gNqJr8ne5yDeACpO5WrngaiOH6Ai-sxvaE6h5GyQLtd9h3P_5K2l__vYwblizpX4bIjw8xXgZ1OcXXDvj0-byDJ3Z6NN9TiYJH5_RLgD1feIv4T0d5ZyZqCJD-8vRV1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc4b45ba3.mp4?token=JDvEybBQ-hHCdOFTAAnJUhhdcmX5Wd91C8PJPYsuAEo3hGt3ltna-HhSlDUGDgzkA3fmfR_TWSoSWmU2KZGHhChy5h93IOYCln8Ds4W3M1Q6W3S_w7JHK5jwtML6KzUKevLf7ijSzqkc1yDidxraHFmGGbpjoMG-v2DJHYX3D4M0sHNL8q89V5_iDREduHS8JPFxxqwaXugRs-kcdvj3ET9e9A_VO_FmHhG0klbQb_cIa6Hyoaymct8VzoqfFrAsAJB9PtLhZYP9l5yBk57cz8gsgYIX5UXvMwE0Ap098TAzkCet4J9Q9nb0NvQCIjXuMbiZrcIB3sE-bWe0DNJA5ATFimqsLyWuBNN7NBy5yYj9pinArDw-0nGE-4cjygep3hFlbTj3XGkwAPrHoJid6S6ICmTchuX4i-z5PfEb51fiVyFEu3711a0-sPC4WegXRs30JdR4xwW5e1lIXr-slJ2HKUabQICDyupfJfdHpuStEeI0JuSf8jVSweGmpQN86P6v0mnNAMM07AD_-yAz8NlZveefgQsMg3GJPNA0xk4gNqJr8ne5yDeACpO5WrngaiOH6Ai-sxvaE6h5GyQLtd9h3P_5K2l__vYwblizpX4bIjw8xXgZ1OcXXDvj0-byDJ3Z6NN9TiYJH5_RLgD1feIv4T0d5ZyZqCJD-8vRV1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من إحياء العاشر من محرم الحرام استذكاراً لفاجعة الطف واستشهاد الإمام الحسين عليه السلام في محافظة البصرة جنوب العراق.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79898" target="_blank">📅 07:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=i1MxL0COQ9ZatzFr6qJjtgSutMnKcFJMCh39oi-ofOkFVd7nO1P-BCq0_sOxKZs09JQNbHWy3tH13FifCmgY2hVtkbPotDEdj3SwnGw1TEV1MRjFPlKXUkDIpkb3clkhdjA9UEdW1CimN3N1kOPYN3qaNH4Fgre6se_mlgYEfIUddejiClrvCjEO9PaFR8RrdTFAdjklvQEN6KN1zRWT6NGR8eJZ_yQcfizgcWwAcDa_p4AJL4q7ZJYIJ121jmWDwNRe5ethaj0wFQZoJ6-5OjFE3J-qxR_BoD-EepLrrRRt8qlpwAIaPLjcvQLuWQgfjFV_XBv-oJ_ZTXTd0txjNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c4d9dc8a.mp4?token=i1MxL0COQ9ZatzFr6qJjtgSutMnKcFJMCh39oi-ofOkFVd7nO1P-BCq0_sOxKZs09JQNbHWy3tH13FifCmgY2hVtkbPotDEdj3SwnGw1TEV1MRjFPlKXUkDIpkb3clkhdjA9UEdW1CimN3N1kOPYN3qaNH4Fgre6se_mlgYEfIUddejiClrvCjEO9PaFR8RrdTFAdjklvQEN6KN1zRWT6NGR8eJZ_yQcfizgcWwAcDa_p4AJL4q7ZJYIJ121jmWDwNRe5ethaj0wFQZoJ6-5OjFE3J-qxR_BoD-EepLrrRRt8qlpwAIaPLjcvQLuWQgfjFV_XBv-oJ_ZTXTd0txjNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعداد هائلة من المعزين العراقيين في مدينة الناصرية يحيون يوم العاشر من محرم الحرام.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79897" target="_blank">📅 07:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=URW89muUAm7y4-4BPBlN-IEOPct3esPg60jaxrT9oJuqk8UUVNWCnwWMFqKyf8sUHvC4S0gTc8s8JzdFbtkSmwK5E27gInPghuWaWtbGYO7XocGRZnip-Bes2pzOn-EEKJzZnUvobVuEQs_toxvoeEHigjv8eTZ6_ceaGUZ9MiAjnJr46ksR0KNKiSwrNGwhnge2eZioZBM9kbE7SvUIhh9B7k-FY9v87qjsgIB8JKIT4AX0cS39tU0sj7IW6xGKtl_JsE2l4ozqHbXKrlGw0K0QKW70Nhk0N0uIEund3oI0QXLcmZIMDVZdwuXxYUNisoo7PuLgpAp5wpjNTUGdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9829a6056e.mp4?token=URW89muUAm7y4-4BPBlN-IEOPct3esPg60jaxrT9oJuqk8UUVNWCnwWMFqKyf8sUHvC4S0gTc8s8JzdFbtkSmwK5E27gInPghuWaWtbGYO7XocGRZnip-Bes2pzOn-EEKJzZnUvobVuEQs_toxvoeEHigjv8eTZ6_ceaGUZ9MiAjnJr46ksR0KNKiSwrNGwhnge2eZioZBM9kbE7SvUIhh9B7k-FY9v87qjsgIB8JKIT4AX0cS39tU0sj7IW6xGKtl_JsE2l4ozqHbXKrlGw0K0QKW70Nhk0N0uIEund3oI0QXLcmZIMDVZdwuXxYUNisoo7PuLgpAp5wpjNTUGdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد الزوار إلى مقام الامام زين العابدين عليه السلام لإحياء يوم العاشر من محرم في سهل نينوى شمال العراق.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79896" target="_blank">📅 06:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-text">تمزقت راية الحسين في طفّ كربلاء ولكنها لم تنكس، وتمزقت أشلاؤه ولم يركع،
وذبح اولاده واخوانه واصحابه ولم يهن
انها عزة الايمان في اعظم تجلياتها
السلام عليك يا سيدي ويا مولاي يا ابا عبدالله الحسين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79895" target="_blank">📅 04:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
كعبة الأحرار كربلاء المقدسة حيث ينطلق معنى الحق ومذهب المقاومة ومنها تُستلهم قيم التضحية والكرامة والإباء لتبقى منارةً للأحرار في كل زمان ومكان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/79894" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=lEKGCoSFoovN9U-ZMleTqBAGTja2pfsK2Hbg4ATOGV5iQ5p1cLysfPEp6BbeHxLTGemO4Av3vJxeiilueBcJ-QHLMKaeXjxl2urw58KOsAPubGS3X8RDHPv9WY12DFHYfW3xL5EQN6yn9W1a5OO75LpagmoEBoAVjH6PnmNyjl1I0_4kEwF4u8Tbj7kK6fJX_-Ov5O4xVpphsSDkmDXA1MEy4krxa_IC-SqBz7ECD9tPQqgOFMijzM2QZsFztXLHdMkvKpI-gLMemEGn11dpXs1HQDY8emkvdvbzQdW1RpvZ7_tDsu0ztT1UPVxkb1hqH6SzTik2sjjGswfKixBzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0907c324.mp4?token=lEKGCoSFoovN9U-ZMleTqBAGTja2pfsK2Hbg4ATOGV5iQ5p1cLysfPEp6BbeHxLTGemO4Av3vJxeiilueBcJ-QHLMKaeXjxl2urw58KOsAPubGS3X8RDHPv9WY12DFHYfW3xL5EQN6yn9W1a5OO75LpagmoEBoAVjH6PnmNyjl1I0_4kEwF4u8Tbj7kK6fJX_-Ov5O4xVpphsSDkmDXA1MEy4krxa_IC-SqBz7ECD9tPQqgOFMijzM2QZsFztXLHdMkvKpI-gLMemEGn11dpXs1HQDY8emkvdvbzQdW1RpvZ7_tDsu0ztT1UPVxkb1hqH6SzTik2sjjGswfKixBzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/79893" target="_blank">📅 00:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=gn76WlWmTNl83h6yTQ_7Ai3LHRq7rS2OX-v3B988wa42ZD7TRH0P-Ezy3LL2bDJB_AevvMPyhehoDAHfnVL1eDI76oEz77Pwm2y1AZ_esW-kb1xkD46TUVv0_dJyRCVcYwuAoHZCrRlgzCUBHZj2FJNlJM7ZFwko-ZFew0n7h5h_nS3NQz4xqhhbxIIdlTLeTz9Jxd02BJdB9K0zXH5OoGtRjaBCTrfhcAp3hn_ii46nbqNRAhQrGlU7vwWQh4rfLq_0NPyTFxX5LYW8HjvWnN7Ob59fFkRyAuGdFcArxMNaofotpN_oHXIjOsuU4EUA9-U5cMkRbVtvUgt7hH4YJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f0298c9d.mp4?token=gn76WlWmTNl83h6yTQ_7Ai3LHRq7rS2OX-v3B988wa42ZD7TRH0P-Ezy3LL2bDJB_AevvMPyhehoDAHfnVL1eDI76oEz77Pwm2y1AZ_esW-kb1xkD46TUVv0_dJyRCVcYwuAoHZCrRlgzCUBHZj2FJNlJM7ZFwko-ZFew0n7h5h_nS3NQz4xqhhbxIIdlTLeTz9Jxd02BJdB9K0zXH5OoGtRjaBCTrfhcAp3hn_ii46nbqNRAhQrGlU7vwWQh4rfLq_0NPyTFxX5LYW8HjvWnN7Ob59fFkRyAuGdFcArxMNaofotpN_oHXIjOsuU4EUA9-U5cMkRbVtvUgt7hH4YJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتباكات عنيفة بين عصابات الجولاني نتيجة خلافات داخلية تطورت إلى حرق المنازل والسيارات وعدة حالات قتل في مدينة الغزلانية بريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79892" target="_blank">📅 00:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
خيارنا بالعراق هو خيار حسيني،،  المواجهة مع أعداء العراق والإسلام وشعار هيهات منا الذلة مثلته ثلة عراقية شريفة رفضت الذلة والخنوع والخضوع امام مغريات يزيد هذا العصر
السلام على فصائل المقاومة العراقية الشريفة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79891" target="_blank">📅 22:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6tLYT5G9oiWdPHaAKOo7bwac4mhDxYqyWLeWeNVzy_4_iYFQiZ7xD5ZOTKdzrJWmg2i6sOI7C-oSWbSLXyE9Rox-GxbTHJfTGq3mio_JgHz--bxhj3X9c_AMb432EUEoKBdAWo-G6PkhvWdOpmsNEQFm2R3dJbepSVJZfkGe3b8yCTioj1N4KJSJmuyzDfUX_2peujJwbfF5fCxc3Yb8FqkPj-HV-jre_thLGtPYTPoj0F8WG6C5t1CIZrPt1C2pLZfrhMtJaJ9D7fS5HoolgYwAaLM5fNMJBO6OBOVJ6lw4J3E29NHz7Cel3KalcmkNngc_lh_1kE1Cz4TP26yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة إدارة الممر المائي للخليج الفارسي:
🔹
تقع المسؤولية الكاملة عن أي تبعات ناجمة عن الإبحار عبر المسارات غير المصرح بها على عاتق مالك السفينة ومشغّلها وقائدها.
🔹
إن أي حركة ملاحة خارج المسارات المحددة من قبل هيئة إدارة الخليج الفارسي (PGSA) لا تشملها ضمانات العبور الآمن، كما أنها لا تتمتع بأي تغطية تأمينية أو التزامات قانونية مرتبطة بذلك.
🔹
وتبقى جميع النتائج والتبعات المترتبة على استخدام المسارات غير المصرح بها مسؤولية مباشرة لمالك السفينة ومشغّلها وقائدها.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79890" target="_blank">📅 22:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1FCHIXdlK9ejkLkaxHxB6ZAqhmANKFDVl5iK9t4hVv5ef48Hjv39IsLLBqx-4H2TGRAglEawZc8qLDiPT8eHc_QGTmW3nt5Cju44Jh3nAliScdgm3txUlIYGzWAWg4GRRqaAk_ZThk89sq_PaLCZN4KxbXWzw3pVaNY64ed4QtB5jSpdBDsYMCdsLeJlQoZnH0t61qunjrfshK_H7xAECMM5c-5G9yNV-GNG5XGFIsEz0sN0rN2SIRf22oZ92O1SQDRyWxzCVzdjNZoUROwGRXCCd5LQYWRwEyLtSNfVpILCruYtatzBZNb10Go2tJaXz13I1E27LxNodSJdbqCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79889" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79888">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
من شارع الكفاح بالعاصمة العراقية بغداد معقل اللور والكورد الفيلية تتجدد في ليلة العاشر من محرم مشاهد الوفاء والولاء حيث يتجلى دعم ومساندة الجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79888" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePgX7mbfTEWrBI8oq6RwjoQU74UNQm8Y4qxwNMWzbyrnSsKdX-JLUFFQu8iEx-QS9ZZbxHhFtTbVEUXavx3mryRdJ5TW7aKvSPBUaa4R97MSKoUL8n4MBMFpt8ElSeciw6fN7hSUGsVf7psmrfflCMyWpvm5M4mqtPDLic6kBildG-OufxdKUaaa9BWPToRm66aVWiHUOdqd73RBbczA0sKxaVYoiRZWvwp4UjCHCrvdNDZqI81EB8myhmnkF2at47CZedqsxj1M-AwQdIUE2VRPLY6P2XjAZp8vfaUv66MIX8hfnuhoJNNPGidU-kSH2feQLB3svN2FZsNYBvn65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
مسؤولين أمريكيين: الحرس الثوري الإيراني هاجم اليوم بمضيق هرمز سفينة شحن ترفع علم سنغافورة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79887" target="_blank">📅 22:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79886" target="_blank">📅 21:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79885" target="_blank">📅 21:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79884" target="_blank">📅 21:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇹
🇮🇷
‏
رئيسة الوزراء الإيطالية ميلوني:
لم نشارك مطلقًا في حرب إيران ؛قدمنا دعمًا تقنيًّا ولوجستيًّا فقط.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79883" target="_blank">📅 20:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
🇮🇷
وزير الطاقة الأمريكي:
رفع العقوبات عن نفط إيران يتيح لها بيعه في أسواق أخرى وتقاضي الثمن بالدولار.
أموال إيران التي سيرفع عنها التجميد ستخضع لرقابة صارمة بشأن كيفية إنفاقها.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79882" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
14-06-2026
تجمعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79881" target="_blank">📅 20:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
هبوط اضطراري لطائرة هليكوبتر الرئيس هرتسوغ في قاعدة بلمحيم.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79880" target="_blank">📅 20:18 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
