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
<img src="https://cdn4.telesco.pe/file/UiJuPDp7w3uPxgtQWiVdh1sE_fKT5y-_9xb14_OOQPyZBD0qg89hp13VlkWA6zupSDGnCsoQ_gBg2Cqu1hN_5iXHbnol_N8EcJBhpds1vxpkfmOPfsdgZlj-ziWamm6eYbcmu9BSSfnjOJdR-ByDcF6aDO8r82LFdzSbDCJ8-7ulVtGtAfm_yOW2C1Y44aQiwx-Q7SIgwKC4THaNrwQ1kThzlFnKEhZNV8aVtkfOnXS2WFUf0yl2jaorx2Ws4q9OQ53TPhBMsyZsGuerU7QbUOMohj3m0Pfc6ldcFYd6edm-3po-Naa7BhE3uATK66dFUfeRqkVEn33TbLWlqxkxPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 06:11:45</div>
<hr>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/91625" target="_blank">📅 04:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">النظام السعودي:الدفاع الجوي اعترض صاروخ باليستيي أطلقته قوات الحوثي تجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/naya_foriraq/91624" target="_blank">📅 04:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3PpqI8XmonpjLOU6GX0_pvtC3phMKVpFHGYEUxIxVvotuY2bGvDt24ya7xua7ZSLG48VZznFSCkoSDBLkh4RmscLs9RnUFdi7QM46-UhZUVFNAXmImirozhKE7A8dxTSXAks9weNG3vuV_ABk195clUfc7bob2l46OoTzvzxfCU2lCDG04WAKuDd0hdXxgyJO65cKBiCgj9TMjt3jCMWE7X0UBaiuqc4dYaNWz_OCMbTYgJFYT0NdsI6r9gmMjGEAfTk9fr05hYEGK1cD4ztkNJsEOgw73Kz1jeweeg3iW-V7OEFjRnFcVrsVUo02a7hxCNzirpddqTIT_UC_oxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد: جار تأديب وتربية عيال ابستين</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/91623" target="_blank">📅 04:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/naya_foriraq/91622" target="_blank">📅 04:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POZ-253ndDK6KCUdW5BuRLFxnFMLPGlcSIEg9_AUdJ1bpYrunG0PCWzk05qwiW7tCeACMDZOdTXgvm7OAqtFEBrKn5xBMzwHIwvgnu-6yv4-qUtXYPPh1_l_xj7LUTrYNcLBD79qSXWfrWYOXI3Au6fD6iEHuh-9WnTCcOV7mC2AgAoKki3qs_wfXfJ93DaKD5c0jEaLbqnJIoHLN7YcwgRqWmoLJ6rTcB-2yvzEregEX5v4ZpTdLJC0v_94EF07KiT0LMBdrMhl2hpePVQbk8O7iWXeyESSl8NNIIbbMBDBtVJl-5DXc3r_5vsSXQ4jyEtPnzlgpkuVK3Vp42pMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
ترامب ينشر مضيق هرمز تحت عنوان "مضيق ترامب" وسط توقعات بالرد من قبل هيبت الحلبوسي</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/91621" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/91620" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">النظام السعودي: هجوم على الرياض</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/91619" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏النظام السعودي: نرصد ونتابع تهديد صاروخي ومسيرات باتجاه المملكة.</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/91618" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تفعيل منظومة احذف تكفى في الجنوب السعودي</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/91617" target="_blank">📅 04:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ابها تحت القصف</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/91616" target="_blank">📅 04:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/91615" target="_blank">📅 04:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/91614" target="_blank">📅 04:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ول ستريت جورنال: ‏ترامب يرفض وقف إطلاق النار مع إيران ؛ ويتوقع تصعيداً في القصف بعد انتخابات التجديد النصفي</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/91613" target="_blank">📅 04:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/naya_foriraq/91612" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز الدمام الان</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/91611" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/91610" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ljh45Vthbrp6GpLiGHYhKRIFPxsptMrffjdTswfMt8FQZ9qmfuwVnpEkCxCOObgPpBdze4IluT015x5XWssn4yZZdSgf_yyd0fTfOwuETsR5DLOO2j-T7CXUQmnq_BpQrdENu_Ahq8TLQGIsAjDR_PplwIBRzHqy2HljZl3jn8CyA84YdZd5MHznzkkZhuYhKdrpf3AImpeEYKV9ffTEHv7b83BqSl-7FxyTECuZhpavaiKPhsBslYGHKRcUIFVNCb_UTX8f6h861O0YRauqfwVEXlNibD2-NLpd0-HCG_pfCJx_dZMtL-VqSxV7ZGJpLMBVol_yyOMDLlooI9mL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/91609" target="_blank">📅 03:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا
صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/91608" target="_blank">📅 03:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">والعتب موصول لسماحة السيد مقتدى الصدر
عرفنا السيد مقتدى الصدر انه مع دعاة استقلال العراق وتأثره وتبنيه بمقولة لا شرقية ولا غربية
فكيف يرضى ان يخضع العراق  للأمريكان ويشارك في حصار على الجمهورية الإسلامية الإيرانية المنصورة بأذن الله
واين تغريداته التي تعلمنا منها عن المشاركة في نصرة المظلوم على الظالم ؟!</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/91607" target="_blank">📅 03:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امر مستغرب جدا
لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن
والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري ؛ نوري المالكي ، محسن المندلاوي ، عبد الحسين الموسوي ، عامر الفايز ، الحاج ابو الاء
لديكم برلمان كامل وزارات ماذا تنتظرون  ؟</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/naya_foriraq/91606" target="_blank">📅 02:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
السيد صلاح المكصوصي :
لقد تعودنا أن تغلق الحدود وأن ترهن القرارات العراقية بإشارة من سفارة لا تمثل إلا الذلة فإذا كان منع الطيران يقطع رحم المحبة بين شعبين دمهما واحد فاعلموا أنكم لم تمنعوا طائرة بل منعتم الكرامة وأسقطتم ما تبقى من هيبة الدولة
من يظن أن منع الأجواء مسألة ممرات جوية فقط فهو إما جاهل بحياة الناس أو متعمد تغليب مصلحة السيد الأمريكي على مصلحة العراقيين
فبسبب هذا المنع المذل تقطع الزيارات المتبادلة للعتبات المقدسة آلاف الزائرين العراقيين الذين يزورون مشهد وقم وجمكران والعتبات في إيران وآلاف الإيرانيين الذين يقصدون كربلاء والنجف والكاظمية وسامراء اليوم يقفون بين حيرة الطرق البرية وكلفتها وتعبها وتحرم أرواحهم من زيارة أولياء الله
ويربك طلاب الكليات العراقيين والإيرانيين الذين يدرسون في جامعات البلدين طالب في كلية الفقه أو الطب أو الهندسة يمنع من العودة إلى مقعده أو من لقاء أهله لأن قرارا انبطاحيا أغلق عليه السماء
ويحرم مراجعو العلاج من السفر لتلقي العلاج في المستشفيات الإيرانية كما يحرم المرضى الإيرانيون من المجيء للعراق أرواح بشرية تدفع ثمنها لأن حكومة بغداد خافت أن تغضب واشنطن أكثر من خوفها أن تموت امرأة أو طفل على حدود البر
وتشل التجارة مع إيران السوق العراقي الذي يرتبط بالمنافذ والاستيراد والتبادل التجاري مع الجارة إيران يدفع فاتورة الشلل والغلاء وشركات النقل والتجار والأسواق تترك ضحية لابتزاز الدولار والتهديد الأمريكي
هذا هو وجه القرار الحقيقي
ليس أمنا ولا سيادة بل محاربة للزيارة وضرب للطلبة وتعطيل للعلاج وخنق للتجارة من أجل رضا سفارة لا تملك حقا على سماء العراق
الذين يدافعون اليوم عن هذا القرار تحت ذريعة أن الحكومة مجبرة وأن أمريكا ستضربنا وأن الدولار سينقطع هم أنفسهم حفظة مدرسة نخشى أن تصيبنا دائرة ومدرسة بيوتنا عورة لا نستطيع أن نغير
أي سيادة هذه التي تبنى على إذن أمريكي بعبور السماء
وأي حكومة هذه التي لا تعبر عن شجاعة الشعب العراقي حين تقف عاجزة أمام قطع رزق التاجر وعذاب المريض وحرمان الزائر وتشتيت الطالب
إن الحكومة التي اتخذت هذا القرار المذل تضع مصلحة الضغط الأمريكي فوق راحة شعبها وعمق علاقتها بجارتها إيران فقد خرجت من رحمة الموقف الوطني ولم تعد أهلا لأن تمثل من ضحى بدمه لئلا تدخل داعش بغداد
فلا عزاء لمن جعل سماء العراق مفتاحا بيد البيت الأبيض</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91605" target="_blank">📅 02:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة  أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية   وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91604" target="_blank">📅 02:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة
أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية
وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة اعتصامات داخل المطار، على خلفية الدعوات التي أطلقها الشيخ أكرم الكعبي لتنظيم اعتصامات، فيما أشارت المعلومات إلى أن الإجراء تم من دون علم الوزارة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91603" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avkVAMNgZCKoJD-bkz_Frc779HRpq5rlLAxadi8Cg_3oB51iMSj3uKcqE1MGv4kdWpyXB3hDFepGRntU8h6Hpz6UrFZYq4E53C-GpVh6cnY_urgaRlVGdPQ8zoZ9DDh2SawdBdT3ThV6tJX-85dzdJYrg0qf93Spscik2P1xykRp98PnlQP7-dtxwWCPcQWCvxaN31bTHcdNPmYsIFLz2-0ZoV-Hj4vPd1-1Uwz9C59n80gA2w6WiA7JqaDKDVVMTXSJK-sgdLKz7WH3O1LlTjjmc9Qq_UXE6yyMvxse2HyZ1a9VRFJGS-eAcKPPHm46vpH37aAi6r8qS2M5LLfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2103610717991563618?s=46</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91602" target="_blank">📅 01:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91601" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91600" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InCwQ270HGNUhQM_Xx1h9AqoaJFsJwAM6MihQo99Twp7LGxv20-B2d2cL6gng-JXE6IvjqxGWU4R9NXpbqhISy8lNbg7LmJAhOc19_dYm4PAHwi9rOX6_7JqQxzzTi3VY5Xm2R6QxFH1wEzDuYBe8Tv_8kJj0Y9KKPCYGzJIeNtnMNhjSAnUnLuBjGqx4Q7bySdTu40NNwCovuBMSegHit3Lpj8SMoCUoti-x4YaIovqu3bMIsUXOIuTpc1JkJtHlpMxN6ORyg0XXc7_xMSWp4GlTkznE7tPMuY0M9hm9GngkTxMGPXVEwCMH4c7KZm1dpl0QhT9F35CEJUearWhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابو جاسم الذي نحبه : كلا كلا للحصار على الجمهورية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91599" target="_blank">📅 00:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇷🇺
الغالبية العظمى من ناقلات النفط التي تعبر مضيق باب المندب حالياً مرتبطة بروسيا.
لا تمر أي ناقلة نفط مرتبطة بإسرائيل أو السعودية من هنا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91598" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
أضاف البنتاغون بهدوء 37 جندياً إلى حصيلته المعلنة من الأفراد المصابين خلال الحرب الإيرانية هذا الأسبوع، ليصل إجمالي عدد أفراد الخدمة الأمريكية المصابين إلى 861.
وتشمل هذه الزيادة 29 بحاراً من البحرية وثمانية من مشاة البحرية، لكن وزارة الدفاع لم توضح متى أو كيف وقعت الإصابات.
أعلنت البحرية أن البحارة عادوا إلى الخدمة بعد إصاباتهم التي لم يتم تحديدها.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91597" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91595" target="_blank">📅 23:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91594" target="_blank">📅 22:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXePME5tcT39ZXWVUY0eV1oKnOuyA00nQH-Z_L6p1b7RmEajEcFw3obPd0fKKNdswRyt_fzOgKZ0e7OZfkvuKfs0A59ksKLKM2y-HODQu1H275lF3gb5Q0V0flH7aqs2boZeZDbKFK19IMK04M0xFl2o7jzLdjv90ZSXrn5PJcIgfb9C11TYkdA4xpRKUysUKQQ5knnYc-9htgG10TTan0Y4bf-lorVNpw-Bf0XPb34TZxw8uFFlbr45BFrHLo5RM_AoLdPyFqR7dVaix4Vhbp0ArqywkW5ne1VkFo4sh_dzvnaoDkEAoeQfYdprLg0tXH99mFZgrVe3j2ky6Gg32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sH3zJOq0Mo9Rp1X4hibYnHxTpOh3ZOkJcd1XAGX0IcRHm8DwwGJXy0K8Y-6grAMvdFfQVXoA7JPNpUJCAVmZ_hTFMakHNluZFJzUuLia-gB5zaTLs8TTPrnYhMJ90f9NaOIFpigf7I6c0frFYyQZzGWnbGfdSXTbU8XlduK3VLVKDYBy5icGCVhskaEcD1_IIEbZv10FYpmN67eEfd5xHTR9q9p-zG6XY1Tra08lE3FqMBe41bRSNI5HN-DOZRbovMobXhvtGOuh0qlgCfdWoBciXsvhrqHksj_CACYQ5sH2pl_2VyZFO7amwtuRB1oEz8Byv8U9hsKnR2yh8V02QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhg1ft5iCD2UHYRz18itVtiElxR5aHiPKYgjsleWkbAaCFE6DBAYMiFo6xGRjLFFtqG0UYYyl0So_HVEsPNuBYRJ3o2V5E26LozhimYIS6s4DkgixMl2vElwGvBKZ_gYg8y5m8EmjjRmCm2ogtqppUiOq4EOMkxREKJzrIjBe1k1Wk67pqIAp4miB-lLm6V8FST-9MIfypwFHe8ndnZqm6abbMxKobMoVVa34FjpbW4RpH8rMEYMypXW9c4a7GbRO6OTnvXVYTkSPazM2F4dyP1b71xFOVzm0A9F89AFH2JnEvg32G-bKtAWCo0RFJuw4hXzYJxcvRef4GCSYte_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiWTghnpG4_gFVTLU2JlDH03Z5NGpWbnoaBPp3XzPVYwGZonmz_h0NwQp_PGz_B_UWUUD6rQIqzPoG1J09x9p1hkzzaHn2rZ7P1Yc1-kd_JxpOwBL-JZIV3ds07kbA115DGerDRIXhcdY9HqPcPplZklWcfN3XXo7PaApCKD6OnbcN14zTtTRLV0fVRBW58uFRecN7mBrQ2sZCtZupRQ-zmE51-KbFdFme6mqpErPxfCRxo6WwMBpSUD13iEzKJOYEHOs-HOGNrVg4Y8NaEfXvuFIIPnUtd-Jym4uzGiJyzpnYwc2zfLX-inyAJzliYi5jnc6hszXzn5dpnSszwkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد من المسلحين وأسر آخرين فضلاً عن الاستيلاء على أسلحتهم وتحرير الباخرة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91589" target="_blank">📅 22:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_4kOV2kFUxgTtBDOsV5l7G2YLiB02HeZoLIVNn0xQEQGTDnsoCVgciW2KLVhZHiCm13QwofMCpZtM6HM7ZgSowZJPhlx_nzUSgFL6zlSqhMAs5-OBQ02tdkyWEbVVewTPS_YnAfW0CemJFUo57e4LHqGozilo6MwSyl_7rt54MoNxb6wUHZ0mXgJSQXcC9OYMvor9iDg0vy3ylJPnNOsQfLc3OnBtijRBsZ81aOexVEuEnkDlh0hinmEt8fbOTbmPCM33mCq0BMeyVh9P0NMOKBf6xPrXiT2KMken5K7Te6FhvVh-eW0c4_pz-ly9v9XPGzFZiqYU4igz9p0fAHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جماهير البصرة الغيارى تستنكر وترفض
تخبط الإجراءات الحكومية الأخيرة وامتثالها للقرارات بحق الشعب الإيراني الشقيق.
موعدنا معكم
🗓
الزمان: يوم السبت 26/9/2026
⏰
الساعة: الرابعة عصرًا
📍
المكان: كورنيش البصرة
نقطة الانطلاق: من مقابل طوارئ المستشفى التعليمي، تحت الجسر، باتجاه النافورة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91588" target="_blank">📅 22:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
انباء عن انفجارات جديدة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91587" target="_blank">📅 22:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9abc32c86.mp4?token=Xm2K3vhoz6qhWdwFLSzPINzSWlFmGMEgWU9DIkW9zFbmkMh-mSZ6iKA2E_zx7haoCRzLLbu1o0cUKC3nVsE4wKZVE4VqovrXHpT5IxKsBKmFfxcbvtsj9k2w42rUkN7hdeS6Y6Cc35HYAR3HH9rw8WBnOvC8mvDn5j4nW1p0XrPyaIBIbrcbqstO9ghUdwuHj1_1BiHW7VBjsgfpoDmUTUEdh931o5XWH41lr9J0j7p1e_zZX4wki_wYYqc-uhmyN52H5e5RbH3L1-qpwC9TCD0AcA3BG3_AP-iAVQ1jKXX2xXFMcZRJgXNyyPMq5bzFWtdtd24H86EneXNgRxOiRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9abc32c86.mp4?token=Xm2K3vhoz6qhWdwFLSzPINzSWlFmGMEgWU9DIkW9zFbmkMh-mSZ6iKA2E_zx7haoCRzLLbu1o0cUKC3nVsE4wKZVE4VqovrXHpT5IxKsBKmFfxcbvtsj9k2w42rUkN7hdeS6Y6Cc35HYAR3HH9rw8WBnOvC8mvDn5j4nW1p0XrPyaIBIbrcbqstO9ghUdwuHj1_1BiHW7VBjsgfpoDmUTUEdh931o5XWH41lr9J0j7p1e_zZX4wki_wYYqc-uhmyN52H5e5RbH3L1-qpwC9TCD0AcA3BG3_AP-iAVQ1jKXX2xXFMcZRJgXNyyPMq5bzFWtdtd24H86EneXNgRxOiRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نزاع عشائري في محافظة ميسان جنوبي العراق مقتل شخص واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91585" target="_blank">📅 21:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ed9a3394.mp4?token=N2svZNoYGxLtIZnL7_Xp0xyU8yjezVISCh_HfKo7JLWSTr_nPbCe0b0vUEW9VuQ4x5fljvRf36zrdsbcd-T5ue1TF2QU2YOVUvNUfxQo0Aw6T2V4IJlQhGL_ugfhTL05au92QAfHKL5EukJcgGndFfg7t9L51UdhHf25kkoB23W0eLYM5WI9K3fbrebpGu5o2Djp8cJe-mhEeCewCRo68HHQDDKx4iRGaBGqfWZ07EYpaPpHokLwfic7Q8Oawu_VmqmLLTF7b4IXTg7LH1kmBqMp-hYpjfnbJ09nTT-quDaH_sT6HnurTZ_AtD-c1WwKk-wNCxERAbZJBQmuEYvBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ed9a3394.mp4?token=N2svZNoYGxLtIZnL7_Xp0xyU8yjezVISCh_HfKo7JLWSTr_nPbCe0b0vUEW9VuQ4x5fljvRf36zrdsbcd-T5ue1TF2QU2YOVUvNUfxQo0Aw6T2V4IJlQhGL_ugfhTL05au92QAfHKL5EukJcgGndFfg7t9L51UdhHf25kkoB23W0eLYM5WI9K3fbrebpGu5o2Djp8cJe-mhEeCewCRo68HHQDDKx4iRGaBGqfWZ07EYpaPpHokLwfic7Q8Oawu_VmqmLLTF7b4IXTg7LH1kmBqMp-hYpjfnbJ09nTT-quDaH_sT6HnurTZ_AtD-c1WwKk-wNCxERAbZJBQmuEYvBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇸🇦
🇾🇪
مشاهد حصرية لنايا...
من الانفجارات الاخيرة التي حدثت في سماء ارامكو بالسعودية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91584" target="_blank">📅 21:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-UDZ_DS_-u4ZK4FEHlxtlUvzsy8gXRIxxF_4t2h3y0XTMXP2BUK_HU88m91WM_JzZbfrHDgPK74ebzd6Lm25uwKKaLZG-JQdAGEC5swk6cHazp56w9HCixsMNc97B5MBv2hkW0HfwIx4SejusPnkDcU65DsUEoPVu_lDV1HwRJANkwEkGsBUOOPcvpqFs6k72ROjtXvmkBl9o1ior-3XvKQEFgky4rvzC7n7mueWsEtbUE-pDzd373ILw6iJzhCY70NqyfJGvaR5p35EGAEbSmsX3c2S7jfkZfqYic1jYpux_wks4GTOMR2t0y4GeJ2tfQBkz7vWWTuXmZv1t6GGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي:
في حال عدم عودة الانسيابية الطيران مع الجمهورية الاسلامية فسندعو الشعب العراقي ومضايف الامام الحسين والمواكب الحسينية للاستعداد الى الاعتصام في المطارات العراقية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91583" target="_blank">📅 21:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4eW08DKGycn4ozwcE9X2mdek3bGLPaV0J6LVoEoxC-newIlQpNCPnqfH9tvXfHUwwFvH74dHWrEGZunq5ose0n_3z9dfT7E16Mc8CY_BJM_7YbpvEI6hnlHoolTrv0pcfeS11ejqV6Ra2MwvIwBaT4ce5Hjwq7x3tWyvvGIv0PJExua3vJkpMNkOHjdQ75uY_JTuPL0aYPa1obPEzWC600lDkYSDctPXf4rsgsJwqJbgSiuno-gBs3D8x24oc9Al3Rr0X-9rFPDHJlx3Qvhspd0Lx9AelIS_7GyrzZmjD8e8qRCMWo_SyKOrmDvMcNDh78lcw8Jrx74WhyFHlRqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91582" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk1u6ukAQKKBuMYz_sfB5NrGUXwRSLg7ynWuSD2gIuh6UdUj7MX1_dw1-4QKP4mImh6pAftX50tuHEXatYfBUQ7GcmjK9Au1EYD8CcCKYDAbidqrel48iNyGok9SZOCmVX90u_Xdk-qn1Rj3k7Wi_IboYlKbqQiz_fcrexL6StN2tzXY1Ptz1gtQ9qRvlD2xk6UyxnqHva_lTgTPVmcKXv3Zg9cmnpdpL1IgxRxQqyHejvR3DKtlBMi-mJr5vy5bi6n3IyTkIxxDsAvO-Bh1WBDmV2t7_A8bU3xhPjD5S31D_cpfrvva1qCGLDdnjtlKGgAdE9ZFrd4N5EQ2W9QxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91581" target="_blank">📅 20:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
🇮🇶
الخارجية الأميركية:
نريد رؤية عراق ذي سيادة ونزع سلاح وكلاء إيران فيه.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91580" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يفيد بأن رئيس دولة الإمارات محمد بن زايد، حذر نتنياهو قبل السابع من أكتوبر بأن حركة حماس كانت تستعد لشن هجوم كبير.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91579" target="_blank">📅 20:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">إعلان
📣
🇮🇶
🔻
🇱🇧
*تجديد العهد..نرفع الصوت..لن ننسى الشهداء*
موعدنا غداً السبت ٢٠٢٦/٩/٢٦
الساعة ٣ عصراً الى الساعة ٦ مساءً
المكان بغداد - ساحة التحرير</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91578" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
🇺🇦
بوتين
: كانت روسيا مستعدة لاستئناف المفاوضات مع كييف بعد الانتخابات، ولكن أوكرانيا حاولت استهداف موسكو وهاجمت مراكز الاقتراع.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91577" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQaWZc2SS9SMdRqQxlLiLsIJ-bUN0pl6cd89tcwKZGslWJdeEbKN9p6vAYnhAmO3okr0kJJXn1ZTwZabHtbkoGFMW8IBJeN3x9AwFBZdV03k_1JQArHZj5claNj7kAb5FTf-3juLCiEY21WgtAaT_JeqF5VusRIeTPjs22IX_nfI_NOZG-6duhweQOU0oKPrRNmApjblO1u0nHCTp5D_WUyCt43VBPU_zJGqMT-Aad3ndfg6o9PR-3TZ08RiG-6kPGUN9kyzMkO9xUqEW5YcHUampw6gZqR628PwG3dpy1FMh2JDUc8L6dlOYXzR8-f5Z_n9DggO52mEVjHJ_aN3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
: ‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91576" target="_blank">📅 20:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
اطلاق صواريخ من ايران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91575" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
‏
مسؤول إيراني رفيع المستوى لوكالة رويترز:
سيظل مضيق هرمز مغلقاً، ولن تُجرى أي محادثات نووية مع الولايات المتحدة حتى يتم تلبية شروط إيران، إيران لن تقدم أي تنازلات بشأن برنامجها النووي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91574" target="_blank">📅 20:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
معاون الأمين العام لحركة النجباء للمعاونية الإعلامية حسين الموسوي:
طهران هي التي سمحت للنفط العراقي بالعبور الآمن من مضيق هرمز فهل هذا هو رد الدين والشكر العملي؟، طهران التي ما زالت أياديها البيضاء تطوق العراق هي التي فتحت حدودها للتجارة العراقية ومخازن أسلحتها للدفاع عن العراق.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91573" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق الاسبق السيد عادل عبد المهدي:
اغلاق المطارات العراقية خطأ كبير.. وتنازل عن السيادة الوطنية ..
والتضحية بمصالحنا الوطنية ومستقبلنا
والتراجع افضل من الاصرار على الخطأ.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91572" target="_blank">📅 19:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي: التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91571" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
وزير الخارجية العراقي:
التفاوض مع قيادات الفصائل بشأن تسليم السلاح مستمر.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91570" target="_blank">📅 19:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 14 غارةً جويةً وصاروخاً من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران، استهدفت محافظات تعز وعمران ومأرب وصعدة.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1032 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91569" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
🇨🇳
ترامب طلب من الرئيس الصيني التوقف عن دعم إيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91568" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🇮🇶
وكالة تسنيم بخصوص تعليق الرحلات الجوية بين النجف والجمهورية الاسلامية:
كما سبق وأعلنت إدارة مطار النجف، فإن القرارات من هذا النوع تقع ضمن اختصاص سلطة الطيران المدني ووزارة النقل العراقية.
في هذه الحالة، كان رئيس الوزراء العراقي علي الزيدي قد وجّه مكتبه بإصدار قرار حظر الرحلات الإيرانية؛ إلا أن هذا الأمر لم يكن يقع ضمن نطاق صلاحيات مكتبه.
وبناءً على ذلك، وبصفته رئيساً للوزراء، أصدر الزيدي أمراً لوزارة النقل بتعليق الرحلات الإيرانية، موجّهاً الوزارة بإبلاغ مطار النجف بهذا القرار.
في العراق، تُعد المسائل المتعلقة بعمليات الطيران في المطارات مسؤولية حصرية لسلطة الطيران المدني ووزارة النقل.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91567" target="_blank">📅 19:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91566" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي
: ساعدت صور الأقمار الصناعية ودعم المعلومات الاستخباراتية المقدم من جهات صينية إيرانَ في تهديد السفن في مضيق هرمز وشن ضربات دقيقة على قواعد عسكرية أمريكية في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91565" target="_blank">📅 18:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
🇾🇪
التلفزيون اليمني:
- تم بحمد الله طرد تحشيدات تابعة لعدو السعودي حاولت استهداف جبل نمان وما جاوره في مديرية الوازعية.
-
مصرع وإصابة عشرات القتلى والمصابين في أوساط التحشيدات التابعة للعدو السعودي قرب جبل نمان وما جاوره بالوازعية
-
إسقاط 3 طائرات مسيرة وإعطاب عدد من الآليات التابعة لتحشيدات العدو السعودي قرب جبل نمان وما جاوره
بالوازعية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91564" target="_blank">📅 18:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رئيس الوزراء العراقي خلال كلمته في الامم المتحدة: نؤكد تمسكنا بحقوقنا المائية المشروعة والعادلة وندعو إلى إدارة مشتركة لموارد المياه وفق مبادئ التعاون والقانون الدولي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91563" target="_blank">📅 17:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
رئيس مجلس محافظة النجف الاشرف:
نأمل من الحكومة الاتحادية عدم الموافقة على تنفيذ العقوبات الامريكية في مطار النجف الاشرف الدولي المتعلقة بحظر الطيران الايراني لما له من تداعيات اقتصادية على المحافظة ومعاناة كبيرة للطلبة والمرضى والتجار والزائرين.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91562" target="_blank">📅 17:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صحيفة فاينانشيال تايمز: الحوثيون ابلغوا الاتحاد الأوروبي بأنهم لن يستهدفوا السفن الأوروبية في البحر الأحمر، مؤكدين أن حملتهم تستهدف السعودية وليس إعاقة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91561" target="_blank">📅 16:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اردوغان: تركيا لا تكن أي عداء تجاه الشعب الإسرائيلي أو تجاه أي مجتمع آخر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91560" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=dtwKcDvcNj-trQF0UUiEaVGbyaG4Ue07cHQd4j0_Gsw7-4J7hrMLOrgmLeNGahxB1yN4UjTN0XqnfNo697AhHbIVhQYka45ltUyIKuUGegw9jxojLygaU_DMb0_jw2cFZnNk7gy9O5Q2kr6Zk1rWYDtK2hrJVW5zYexDxthNGn1VlltDLQCejEE4XGMI1qr6g2Y6fo2dAm9cMT0D8_nPkwY9va_m5Gj40axPd7xDF7jT0xMxy9yagjXqPYJ12oOOOHHDDRKVfDen1-dfxcurDER5guMAVdU2F7D3xcHNQkSfNQBC2dnXxSa2QEPJnhwhhzoDx9Y_YwZbkpt7tIVEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04466eb95.mp4?token=dtwKcDvcNj-trQF0UUiEaVGbyaG4Ue07cHQd4j0_Gsw7-4J7hrMLOrgmLeNGahxB1yN4UjTN0XqnfNo697AhHbIVhQYka45ltUyIKuUGegw9jxojLygaU_DMb0_jw2cFZnNk7gy9O5Q2kr6Zk1rWYDtK2hrJVW5zYexDxthNGn1VlltDLQCejEE4XGMI1qr6g2Y6fo2dAm9cMT0D8_nPkwY9va_m5Gj40axPd7xDF7jT0xMxy9yagjXqPYJ12oOOOHHDDRKVfDen1-dfxcurDER5guMAVdU2F7D3xcHNQkSfNQBC2dnXxSa2QEPJnhwhhzoDx9Y_YwZbkpt7tIVEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91559" target="_blank">📅 15:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الخارجية الباكستانية: باكستان والسعودية وتركيا تدين الهجمات التي تستهدف مكة المكرمة والمرافق السعودية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91558" target="_blank">📅 15:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91557" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تنها در برابر دشمن ایستاده‌ایم؛ این چه اسلامیست؟
به نام اسلام، و به نام محبت و ولایت علی بن ابی‌طالب(ع)، همان پیوندی که دل‌های ما را به یکدیگر گره زده است؛ و به نام ملت غیور و حسینی عراق، ملتی که تشییع «رهبر شهید» برای آنان نه صرفاً یک مراسم، بلکه صحنه‌ای آشکار از ابراز محبت و وفاداری به ایران بود.
با این حال، اگر قرار است در برابر دشمن تنها بایستیم، این پرسش همچنان پابرجاست: این کدام اسلام است که در آن، همبستگی و یاری متقابل تنها در شعار باقی بماند؟
از همین رو ما ملت عراق، خواستار توقف فوری جریان گاز ایران به عراق و مطالبه بی‌درنگ بدهی‌های مالی عراق به ایران، که بیش از سه میلیارد دلار برآورد می‌شود، هستیم.
همچنین باید معافیت عراق از محدودیت‌های مربوط به صادرات نفت از مسیر تنگه هرمز لغو شود و نفتکش‌های عراقی نیز، در چارچوب این سیاست، همچون منافع آمریکایی مورد برخورد قرار گیرند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91556" target="_blank">📅 15:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh8-XvJlvBYAzofGK7_B7L3Ne_2ji2ZTxsqRscID0j_PZdMV9RoK5Y9b-60zzp7vezSSrG6qsPFTDnfWH3-zztOCslH8HdqIxYO9e5q0jemX7WDYVGW6UyDzY3EFNigGCVpIRMfP8--Msf7sirwWqpw6IYBlfmJh-ZIIysM0HA1-y_jPTbHHbvOesdxfwu1pNEUtOeyjupAv244fNF2a3oU_RqdBnbQhsbmYMpZsCrqYJhn6kWYKpZ2xQKLLKHdiHIB84CJ7gyHvrAD9bytDVbZkcp8PEd48uxxgWOR-ZLcqQ1qQb3GInGb7o6wkP1C43nLOuLWXcWhk2UkLTcax_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ناشط إعلامي إيراني يخاطب الإطار التنسيقي الشيعي في العراق:
إلى متى تريدون أن تحنوا رؤوسكم أمام أمريكا؟! هذا الطريق ينتهي إلى المسلخ، لا إلى السلام والاستقرار</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91555" target="_blank">📅 15:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3CuMLZYbQ9pLCm3s9F-t1xvFEV3_JrQcSVBx2Y-VBoFJGK2hT0B7h8vRFu_B9J9KhgU0vNzgRHwY6yBp0r0IN3NGY7XoSR9Y7t-s2VFTc-e8gT1L7IMGkrkq0x125O0spqdzOPS2ZfzXFRvHX2itsP8BS86p7NAnQLLLURL9nTHCaKPl_fK0CqQjC-D0pmwBIOt_HZ-NIR1uCuwX49sVd3p1boHU5USroDUrlQYNMb82EMV1gP2AM5hu_j6FqyIgs-uf57lkp2UyEc9IVW9uoPrFmzELsQ8jVUYA3bFBUeys8_L47t9odFhVe5HkwWsZYDIkeV1IcDu7OTY_M_mJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في الشمال</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91554" target="_blank">📅 14:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سماع دوي انفجارات في شمال الكيان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91553" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سماع دوي انفجارات في شمال الكيان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91552" target="_blank">📅 14:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtFOIgd4unPcCjN-udSZ83APkZ__0WlhO5BCp1KwehwJW1BQgUdSGqPnrgdqJIqs4mc_sWdFI6xV0p9DUCkD7rbaFsadazzw9dMSkHDn-M81deh2yJCfDqtnMqa9Ya3AbqdLST6422eUVV1HlaLoI2khSZ7gU0wtCfobZ9ueUYOkOdDK3TXykeHSUdXqQ8ty2UtbrLsXNYaZPJ3W91CvB4hFnhdIpnXNKBt9uFpSBYm-z8SozKtZp3FBlJHU-o9v5bQCcmzcdBgdOKv4qUSVgKtsnGCkW-t4nKnEQ91uK4t1-VuEJzT8574OsHHy3ssIs_QD0Yne90hVdB__c_fCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستشار قائد الثورة
،
محمد مخبر:
التحالف مع أمريكا في تنفيذ سياسات عدائية سيبقى محفورًا في ذاكرة الشعب الإيراني، على الرغم من أن استراتيجيتنا في هذا الشأن واضحة: إما أن يكون الطيران في المنطقة متاحًا للجميع، أو غير متاح لأحد. إذا لم تتمكن إيران من الطيران وتلقي الخدمات الجوية، فلن تتمكن أي دولة أخرى في المنطقة من ذلك أيضًا.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91551" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇶
‏
رويترز:
مطارا أربيل والسليمانية علقا الرحلات الجوية الإيرانية بداية من اليوم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91550" target="_blank">📅 13:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
نائب رئيس البرلمان العراقي يهدد العراق:
دول الخليج لن تصمت طويلا على تكرار استهدافها.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91549" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني:
إخلاء معسكر بعشيقة سيكون تدريجياً وفق جدول زمني متفق عليه.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91548" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
🇮🇶
المدير التنفيذي لمطار الإمام الخميني:
حاليًا، لا يمكن إجراء رحلات إلى النجف، ولم يتم اتخاذ قرار جديد بشأن استئناف هذه الرحلات.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91547" target="_blank">📅 12:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
مسؤول أمني أوروبي:
الوضع في البحر الأحمر أصبح أكثر صعوبة وهذا يخلق مخاطر على الاقتصاد العالمي وعلى عملياتنا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91546" target="_blank">📅 12:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ-D6R-1q7rxSxdr77dt75hY9917XURyhpq3wv3A6SU1PFImZrSYItP2pn4Kl3j-M9KufnhzcoTuhb9iGKxyzDhIui04hNTTzvTackim-mL_VK9H-sZL_7bdFPPrhTQUrhi7VIcgjUDtBz0qZfia3e5pnQCNI-nWVuTSKxuyxOlPtDIYBVdkHbqbzkdFlOe4PdA4MrWMI2jwjtRcPKNW38vht6zjZDFmPsk9e-Bx2cQ8KGcEmMjgkymJ0f6zC0VPGCdimu-UvsUhAYqR14qAFg2HED2_Pqx1u0DgB4oPfhuyvTuHmNbvQCi3g2twgpWOo1puIwBk_YSqTK3TT3fIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93922a090.mp4?token=vwANXYB5rkv4zLeMAwbdgGtm-K8-QIaKaZ_UfcLTTlXLFgK90By2cmpxWwsSezVQl6HTyTVVJylZ3IBcyFo_6hejeh9jki_CMzjZTCzC1jzo1WFgBXNLo9PS6dgaSXQWYrnmwcMf4NVH2CBiee_Tf1ssf3nJjgBM5BtnihoevFh4E9izuQ1exW_tC2V4868jF5wpwyaODho-g6ztG3anxWsClP_kE9GOQBVNmrdiO2sBAnheBjhISrSa9E9om-ueY7fcID0UC6mbIj-mnh7qOAesDeG5P-IPUJebr91SaWE1Y9aOEW4jK0CS93qlonoR-NGR7r-hASXg31YjxzVD6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93922a090.mp4?token=vwANXYB5rkv4zLeMAwbdgGtm-K8-QIaKaZ_UfcLTTlXLFgK90By2cmpxWwsSezVQl6HTyTVVJylZ3IBcyFo_6hejeh9jki_CMzjZTCzC1jzo1WFgBXNLo9PS6dgaSXQWYrnmwcMf4NVH2CBiee_Tf1ssf3nJjgBM5BtnihoevFh4E9izuQ1exW_tC2V4868jF5wpwyaODho-g6ztG3anxWsClP_kE9GOQBVNmrdiO2sBAnheBjhISrSa9E9om-ueY7fcID0UC6mbIj-mnh7qOAesDeG5P-IPUJebr91SaWE1Y9aOEW4jK0CS93qlonoR-NGR7r-hASXg31YjxzVD6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
خاص لنايا.. مشاهد لهبوط الطائرة الإيرانية التابعة لشركة معراج القادمة من العاصمة طهران في مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91544" target="_blank">📅 11:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
🇮🇱
إعلام العدو يبث مشاهد حصرية للحظة وقوع قوة من الجيش الإسرائيلي في كمين لحزب الله عند تلة علي الطاهر وسقوط إصابات.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91543" target="_blank">📅 10:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f871abc343.mp4?token=OoBhDL6Yh1BBkcoaj7tmNI2u3tRvdpEdwHLhAkQuK1poBScxdXxJA_40E5GWMwGAirIUdFq05Pn4L6MzX7kAmHcddPfrXxwx3k1xMfEo0RwAES5Sevs6OHliJFguwbO_n66UiWTehgZ1dN99hYsyVBZyiPRy0Pp99wlp-_yLz6sfU8EVztdP2az53zvWKI1vHBg5Kp3EaZ05O6VNtzZhTQ2blUDbFXWWhsigXJ6fwDAaYqan0RMHcLN1F4AArdwIaDq1w1qcbObaG5x9ToVDqrKQezZPaGc7_eI-z2AZUH-vUousND4OQa-bAH2C7zQFBXOezwJYYsJL__y-y3MGzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f871abc343.mp4?token=OoBhDL6Yh1BBkcoaj7tmNI2u3tRvdpEdwHLhAkQuK1poBScxdXxJA_40E5GWMwGAirIUdFq05Pn4L6MzX7kAmHcddPfrXxwx3k1xMfEo0RwAES5Sevs6OHliJFguwbO_n66UiWTehgZ1dN99hYsyVBZyiPRy0Pp99wlp-_yLz6sfU8EVztdP2az53zvWKI1vHBg5Kp3EaZ05O6VNtzZhTQ2blUDbFXWWhsigXJ6fwDAaYqan0RMHcLN1F4AArdwIaDq1w1qcbObaG5x9ToVDqrKQezZPaGc7_eI-z2AZUH-vUousND4OQa-bAH2C7zQFBXOezwJYYsJL__y-y3MGzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
40 ألف دراجة نارية تشارك في مناورات "فدائيين إيران" بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91542" target="_blank">📅 10:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb4938f06.mp4?token=GPRTI4pR9v1uclmaYRKSmCbjAValhPo1TiYX2tVA4Vg4t4-UK0_yT2P-TKOsQkvM6si9hEaWwxEe6I2BaDSUwtciC9BjDl8G9Auej4jOs-0I3o5BA17i3x4uYyMPnTNu6Lf5GFbvDdAkrjukKMUhRyYKp1wtmbyd5uc3owMuYo2tFKq1fP1bRfAwsC7ck48Yi1JCDgC8FPS_hECmDASHeucTfHDgV27O3lGuCF2Yt8ckY8G7vXwI7ipXOCuYxvFtw80uMFvqOrQWW3IFk4z-Cmo5rmhlk2EgS-ZyonS6GSx_R2h5PZ9zQmBSaYrdK7OWDtnHClbLjg8-IkuhGvdaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb4938f06.mp4?token=GPRTI4pR9v1uclmaYRKSmCbjAValhPo1TiYX2tVA4Vg4t4-UK0_yT2P-TKOsQkvM6si9hEaWwxEe6I2BaDSUwtciC9BjDl8G9Auej4jOs-0I3o5BA17i3x4uYyMPnTNu6Lf5GFbvDdAkrjukKMUhRyYKp1wtmbyd5uc3owMuYo2tFKq1fP1bRfAwsC7ck48Yi1JCDgC8FPS_hECmDASHeucTfHDgV27O3lGuCF2Yt8ckY8G7vXwI7ipXOCuYxvFtw80uMFvqOrQWW3IFk4z-Cmo5rmhlk2EgS-ZyonS6GSx_R2h5PZ9zQmBSaYrdK7OWDtnHClbLjg8-IkuhGvdaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
على الرغم من إعلان إیقاف حركة الطيران بين مطار النجف وإيران.. طائرة قادمة من العاصمة طهران تحط في مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91541" target="_blank">📅 09:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXTUcpCNuSEzgPRLAcYROjpKQ6BTeRvkT9u7_M1kSYGd-JpO7Ky0URwoveMLd1SdUIT6wc45RYzkBdHajauuTHY7OQPWlA5d1b0AMiuwIggZj4tfhWqRC15zS_fBoeGhTqV1-8RXFU5IJHCDD4MA_JRCzYfWT2kYnPz00EXM-i5cSr_C_p3zcOEDh1ew_fFykLRnKeWixkiwYm3XHQKQnlHob_zpLykRnNVyIBYrH7k_K17Al5-S9OUyIgDkQ_yW681XREJ44VwJ6Mq_c9gUpBlw1vVBWu-OX3G7GfiB19llimp4-lR45O9d-fxjOnhY14MwZO5PA99qs1JHLSSJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91540" target="_blank">📅 09:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrlOIp0fO94K2YU-DjGs-_QVf7vndQjgr48nTM_2b4DCg9lsaqRR9Qu0wI7EFsh3vJqruSil4RO3D2rFJbS_ydQsW_yg_PfoK-UdGbdIKnq-9Xdw_OMKQve14h7XNBlR8btpWBJ1SA7l6YMeTazsbOOwVGas88GXm-qhTRgP6T7eldYb0_3QIv0pnJEnlP8ZhRuI7CWZvxYzZHBm_cDJHL3go8vOKz3nYYHOALNOqcCB4Ol7mEfyedqIKyxQweSwLcxslol_nVxnK2HXraFvHBIUrcySUn8tuXQ8CEyBVs6BIvODATovBGELn4wT99w8VtTlaLJYuEg2Gpe_17gmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fymRgLoYVpa9mfvrwDjdNPI84h7RG2vldtneBc2qx4NKGLk-llQosR8pe_5gHIC0fqRvibSH9rmAH0H5e6MY0wzZHuc-IvqyCoEFb_B8GcGruzlPLm0f_ogahG5DL1rAZaMkKoiYkLI6FA6hWFkA6au6VzSQsBMmlWMvHHKxyUH_u2ikuSOuVfmGnmzbcOcu4VJ2BQrp5JGqjwYklxnuruLc3yKILK393q6OwYOw62kRa4SrIqHYZiFvpTBtgVP3BgpmB6Hd6tXEKly5EvEXQ-HRiJDHImex_q0TAxToYCuaAetduy9vroaiyprXoeXm6BGJhgWsQZmEWJBixkKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني يعلن رسمياً عن مقتل جنديين وهويتهما إثر إنفجار مسيرة في قطاع غزة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91538" target="_blank">📅 08:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇷🇺
انفجارات عنيفة تضرب مدينة فورنيج الروسية</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91537" target="_blank">📅 04:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91536" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91535" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
بزشكيان
:
-انصار الله مسؤولون عن أفعالهم ولا يتلقون توجيهات منا
-سنتخلى عن اليورانيوم المخصب بنسبة 60% في إطار القانون الدولي ومعاهدة عدم الانتشار
-سنلتزم بكل ما تنص عليه التزاماتنا بموجب معاهدة عدم الانتشار النووي</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/91534" target="_blank">📅 01:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCGUpps2zW9qAlVtWg_VzrcrfzTY4FMIGb3jeqyQFSnjgywLP1AJ7a34WX4EEv1vEgpml1AKJhRQaGG41by5o6nbk_myyFrsw2QbYmHOY8-0ttI-QGSK3d0--kPygbmZQwnMvIZ9btF933MHZ2LhJ3lK1K4i6qg1scNf6oF38xK1mZbhjXfSxuAcg0Icf70S99ZsIY4FiFpxsRGe2SSjHTI7HKz3jI48uihrWIf-2oollJI5CBNw5apDSuZqnVaEJr0RS9vXg5IwtkMwPcwOTIOQVkYOCPPSl5fzpNsrEs2LH0Cmd3oJkG34SyAzMcDXlGSPtSmxzHckaFGcKAyKSA6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCGUpps2zW9qAlVtWg_VzrcrfzTY4FMIGb3jeqyQFSnjgywLP1AJ7a34WX4EEv1vEgpml1AKJhRQaGG41by5o6nbk_myyFrsw2QbYmHOY8-0ttI-QGSK3d0--kPygbmZQwnMvIZ9btF933MHZ2LhJ3lK1K4i6qg1scNf6oF38xK1mZbhjXfSxuAcg0Icf70S99ZsIY4FiFpxsRGe2SSjHTI7HKz3jI48uihrWIf-2oollJI5CBNw5apDSuZqnVaEJr0RS9vXg5IwtkMwPcwOTIOQVkYOCPPSl5fzpNsrEs2LH0Cmd3oJkG34SyAzMcDXlGSPtSmxzHckaFGcKAyKSA6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/91533" target="_blank">📅 01:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/il6-8Ib4r-brdMF4iNYw8lSIWC57LnRIOcjkG5bTENXbnLjCEntZVjHPdnb1-iTEokJB3PTglE4DPxsTl65JxmTwcl8bQzTkMdNfBNMg5SuMvwRIx5ynonBslnLGiUlb4CdJxGvQKxkT4Y1w0k6d2cy2zZALMItaokHXwvhUWI4w19xjFEqfRe31DM6CPFY88OF9qEvR9u03Cg9pcuxiQ06dM9Hxmvf65CnsxZba_R2MDRyviyh7UlgENrMcNLLSMnpz1esr9wFFjUyqe0jsTY372I1VOPb8aofTNZwBqOdR3OXTDv2c65TF3hPv_P08-L5oUXEdT0rnznTAWSKxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S--eJF9GBMdhVBC9aYHaMACDR6ZkK-TyqVfUvVmzLeMxGuUNQCzXgyBjLpDijopNMaU7LAMJNEKCaCTamwbAuIcHAtmh9L2IV22ktoXCqw5asz4DJwp2OkWsoPFclqfVPhzWWMZw2JWMnmAsiNc18LQu2frDGm_MeVudrf3ytmFK2lRjAzpsVUO5-cejUslYJ84jbBbC81SPuPqIWYKwhSJ4xGBZaVgbsJOTTvwL1O5Dn1IaRz9Q7VJgYJ_eU_V7olu1UQiUxrPgv53-cfo4IToC15GuFxWESMqR-0w7KMff9SfEF58sCREehfqg8FkD9xpDUoWWwTqldF4zJUA-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYSXKPCDuGMa4kzwIzYYH56Mg0gEfcHbCsHfSJNCeAMVgOKp699C_NOedfzPkYd_v0eeZBwU1rpqyIwmskivt2i5_ppUVcP6T8grikI4OFnAAnk6y8L3e57guOE_O_oVmG-AyJPgSj8_hPHfPfeD5iUHGK3kOMQ9gMj0-nf1ihG9uf-QUC-NClO-kbmT_Xb2mFbrl2HIjCGVVHzM8FpF0qSx3im_WT7Q5S2fqrL19n4mVYtcxh7-nGCnwjCMGKoWVxEzO0P0CO0bVoY3pMHf5S5DuJJhYEU5IG2f6XAjEVMpJRS4942P0BwN7wrPHwuTnM0vSNiduC2a9cAvE8zEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsRf2-gAyh5RT5IWdZJAb0tKVKBPDjGUE6mB6pQS5B0GFp8qBmWVGql630hJN1co93jx9--zLMTKte-itIp-Qo8tqLALnPYYUlf41mKHdzuqD9utLa-rk5oUsrHe5bxjYxLzca0m5TRtwlQBqBcbaz1b15HRu3cs3vYUHCaXK2BaTEecAfSGGXmUkiobxvVRxSvALRxj1UymzSmd9e3hgEBlHB35cuI6I23HjdUPPuQk8b_699zLWeTz_uGME8fFR7V72Ps6A-RGL2hjxsL3dWgrwJP0Qg0LeMHUAaqyXdeYOfWxOKt3sh4UTH4Sj1rJZEbZM8HsNnAclEA0rCGuvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
بعد فصل مناهج العرب والأكراد في سوريا..
نظام دمشق يبدأ بتوزيع المناهج الكردية الجديدة على الطلبة في شمال وشرق سوريا وتتضمن المناهج الجديدة أجزاء منها خرائط وتصورات لما يُسمى بـ"كردستان الكبرى" تشمل أجزاء من الأراضي العراقية إلى جانب أراضي من دول أخرى.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/91529" target="_blank">📅 00:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
🇺🇸
رفض مجلس الشيوخ الأمريكي قرارًا يهدف إلى تقييد صلاحيات الرئيس دونالد ترامب فيما يتعلق بإيران، حيث بلغت النتيجة 49 صوتًا مقابل 50.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91528" target="_blank">📅 00:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91527" target="_blank">📅 00:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🇺🇸
صواريخ كروز من طراز شهيد ابو مهدي المهندس باتجاه سفن معادية بمضيق هرمز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91526" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/91525" target="_blank">📅 00:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
مستشار عسكري من انصار الله لوكالة فرانس برس إن اليمن سيهاجم المصالح الأمريكية في الشرق الأوسط إذا تدخلت واشنطن عسكرياً في اليمن دعماً للسعودية أو حاولت السيطرة على مضيق باب المندب، واصفة إياه بأنه "خط أحمر".
‏وقال المستشار إن اليمن "سيغلقون باب المندب تماماً أمام السفن الأمريكية" وسيعتبرون أي مصالح أمريكية حولهم أهدافاً.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/91524" target="_blank">📅 23:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzjBJ74W3VNvP7vRik50VWtCx-BULkxXPGfrOoJRDYMqdPhPhGUpHUDWiwPwJRLZ2zMidIW-KLutY7a1EP7ZRVIfDJwPaEwhMxrcmdPvGfBxYrVpY6LpGEGanbK8apS4R6sXuI-71DGQ0q2F4B8xhP74mNg2t5Xc0jj-aUZ1czMrQr0pC1CZXnLfYxWhEJT7BhxIyvpCWMd5M-yZdqbn3HqcDdFo-mhcYMCeQNV6DwH3jpzubSbjXi05-_HLMmsub3K0IivV7UcCWZUTMFXORIo3wHD-0nzpU_as0keL4FotogMvZF6rFB7Adav4pqa6mb_E6QJ1CZYQps3dwJBZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏
مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
:
‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/91523" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
القوات الامنية ترصد طيران مسير مجهول يحوم حول مزرعة شخصية مهمة في منطقة ابو غريب جنوبي العاصمة بغداد .</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91522" target="_blank">📅 23:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=AmDYgHb-3stP1vvV9FmTNwMKeyp9u665z0_-oaNvVaekX6scn0cAa2s2noKI0OdblkSHq36GWKwvuYZa3bOEXXh1KCG-HwCSxLFi9_oEQkaLIZL_rjO4GbbQgrf1JNe5IauR7JN7qyx91GpGRo1QOkCr5YSCR2PU4fc3Gx4A0Vn3PjUb8bcx9TOos5V-T5SPUXgMmzb7ZukV6Ye9p6o26csyrN-B2rBbz5baf_2hwDkWtRGuzJQwcG66H93eZlZzPLS45LHhTYEeM_rC_yJixVOkL5CwrSURVO7VrABJjYhGC6dLRdLLVxpBt6R3qQ4seYMB7LfhbW6grNYU1I48NkeRbVZLR2Y1hqS9PCfuK2fv25xDQdaEpseVava4JBv_8dl0L--zJiotIw5xIpJX4qT9canVX2GU8L1BRq2Lh-Iwo2_VrYwI2KtMWn3y2SevHVrJ_zTu-Z-GliLnvPitD-_BPTafu70NJoKen1mlulStyBwjey41s8Cp58h0-e6tK9-2cKSM0bmkljr_A7IfXWpvbm2sv69EcQ31JrBxXpDHYPKB50I6YD_XY5sK79ZxT5IElKMxMH-23YEeT-_uqbtTTF_11S1onzQ6kRrfRftl1KXaZDczsfwrixYBHy9KGJc1YgMFUHOnhlHKcGTr30HKZz_WK0eoiH1FBc49Ea0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=AmDYgHb-3stP1vvV9FmTNwMKeyp9u665z0_-oaNvVaekX6scn0cAa2s2noKI0OdblkSHq36GWKwvuYZa3bOEXXh1KCG-HwCSxLFi9_oEQkaLIZL_rjO4GbbQgrf1JNe5IauR7JN7qyx91GpGRo1QOkCr5YSCR2PU4fc3Gx4A0Vn3PjUb8bcx9TOos5V-T5SPUXgMmzb7ZukV6Ye9p6o26csyrN-B2rBbz5baf_2hwDkWtRGuzJQwcG66H93eZlZzPLS45LHhTYEeM_rC_yJixVOkL5CwrSURVO7VrABJjYhGC6dLRdLLVxpBt6R3qQ4seYMB7LfhbW6grNYU1I48NkeRbVZLR2Y1hqS9PCfuK2fv25xDQdaEpseVava4JBv_8dl0L--zJiotIw5xIpJX4qT9canVX2GU8L1BRq2Lh-Iwo2_VrYwI2KtMWn3y2SevHVrJ_zTu-Z-GliLnvPitD-_BPTafu70NJoKen1mlulStyBwjey41s8Cp58h0-e6tK9-2cKSM0bmkljr_A7IfXWpvbm2sv69EcQ31JrBxXpDHYPKB50I6YD_XY5sK79ZxT5IElKMxMH-23YEeT-_uqbtTTF_11S1onzQ6kRrfRftl1KXaZDczsfwrixYBHy9KGJc1YgMFUHOnhlHKcGTr30HKZz_WK0eoiH1FBc49Ea0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ  يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91521" target="_blank">📅 23:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91520">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6411165378.mp4?token=q3ogFc5ev_6iCvyvk-niYzFPGRH5hk0Oy8-nM0Om-MjlmjoPybaUxpw2l6EF-JY_lZsQoN8jv6QDxnMypztVeAKAXHouSa6YWTvXaXW6AwICJjTo9gUYGCIGH-zUCzo-Ue8VWmfILUjMVCd2Za96OShGa4DoD9l9RJU5LN8HssXmNZM5GQk2zPrwV04TT8cJOQqYkZm6LLThn729nzT4Qmc0bRNCEHscsjWYXVF7ObD_BolTeeLVLlPSOkvtv3COAc3QSoQNZwc9MWwyE2gJFgn2vKlR6zlVQT9pcuNWooIDKvx9ENX6YKu4GgwfS1CXKFw2Zuy85C8XyNxx6cWNNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6411165378.mp4?token=q3ogFc5ev_6iCvyvk-niYzFPGRH5hk0Oy8-nM0Om-MjlmjoPybaUxpw2l6EF-JY_lZsQoN8jv6QDxnMypztVeAKAXHouSa6YWTvXaXW6AwICJjTo9gUYGCIGH-zUCzo-Ue8VWmfILUjMVCd2Za96OShGa4DoD9l9RJU5LN8HssXmNZM5GQk2zPrwV04TT8cJOQqYkZm6LLThn729nzT4Qmc0bRNCEHscsjWYXVF7ObD_BolTeeLVLlPSOkvtv3COAc3QSoQNZwc9MWwyE2gJFgn2vKlR6zlVQT9pcuNWooIDKvx9ENX6YKu4GgwfS1CXKFw2Zuy85C8XyNxx6cWNNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تاكر كارلسون:
القطريون أعطوا ترامب طائرة. وما الذي حصلوا عليه في المقابل؟ لم يحصلوا على شيء.
لم تدافع الولايات المتحدة عن قطر. نقلت الولايات المتحدة بطاريات نظام "ثاد" من الخليج إلى إسرائيل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91520" target="_blank">📅 23:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=v7RNAjQuuj5_3X33TLUj97s44ehl8Rv30b3ZhU5N31JvMMXoW_Z_ya7HKQLdM1Uyh6nMWQC0FGJyM2-Y37JMBZqEX7U7_SC4II_wrPzsi0eU4mVWCSKtWRf1E67hXQ9-YM8Ha3Ytnlm0XdskGqmOLRseyhRv8UOkYejNgGHhQJqTkcdU4_g6bkg7EqIV2wlJoE2LajoI47LIE0-X7icPGdjX10exa6jbQgHe7A7cm7XAQzmSY4oI-TbW3ErbHraNj_Tg5D43aI0vRywxgMZJTWh-LwFMsU6cNOS29FyWI3CnhVQH6k267kag4hBh-KBpj0v54aCb_XAukPwIZwOUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=v7RNAjQuuj5_3X33TLUj97s44ehl8Rv30b3ZhU5N31JvMMXoW_Z_ya7HKQLdM1Uyh6nMWQC0FGJyM2-Y37JMBZqEX7U7_SC4II_wrPzsi0eU4mVWCSKtWRf1E67hXQ9-YM8Ha3Ytnlm0XdskGqmOLRseyhRv8UOkYejNgGHhQJqTkcdU4_g6bkg7EqIV2wlJoE2LajoI47LIE0-X7icPGdjX10exa6jbQgHe7A7cm7XAQzmSY4oI-TbW3ErbHraNj_Tg5D43aI0vRywxgMZJTWh-LwFMsU6cNOS29FyWI3CnhVQH6k267kag4hBh-KBpj0v54aCb_XAukPwIZwOUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
أنباء عن اندلاع اشتباكات مسلحة وتحليق طيران حربي في أجواء الحدود الباكستانية الأفغانية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91518" target="_blank">📅 22:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
الأمين العام لحلف الناتو
: الحلفاء الأوروبيون مستعدون للهجمات الهجينة الروسية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91517" target="_blank">📅 22:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على شعبِنا من خلالِ حصارِه الظالمِ وشنِّ الغاراتِ الجويةِ العدوانيةِ والتي بلغت منذُ بدءِ التصعيدِ وحتى مساءِ اليومِ 1018 غارةً جويةً وصاروخًا من خلالِ طائراتِ F15 وتايفونَ أقلعتْ من قاعدتي خميسِ مشيطٍ والطائفِ والعدوانِ الصاروخيِّ من نجرانَ وجيزانَ استهدفَت محافظاتِ مأربَ وصعدةَ والحديدةَ وتعزَ والجوفَ والبيضاءَ وخلَّفت شهداءَ وجرحى بينهم نساءٌ وأطفالٌ وتسببت بخسائرَ في البنيةِ التحتيةِ المدنيةِ.
وفي إطارِ الردِّ على هذا العدوانِ نفذتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ تعالى عمليتينِ عسكريتينِ نوعيتينِ الأولى استهدفت هدفًا حساسًا في عاصمةِ العدوِّ السعوديِّ الرياضِ
والأخرى استهدفت شركةَ أرامكو في ينبعَ، وذلك بعددٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرة، وحققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ.
إنَّ استمرارَ العدوِّ السعوديِّ المجرمِ في شنِّ غاراتِه على شعبِنا وبلدِنا لن يثنيَ القواتِ المسلحةَ اليمنيةَ عن ممارسةِ حقِّها المشروعِ في الردِّ المباشرِ والمناسبِ على هذا العدوانِ فكلُّ اعتداءٍ سيتمُّ الردُّ عليهِ وكلُّ تصعيدٍ سيُقابَلُ بمثلِه وما مصيرُ المعتدينَ المجرمينَ الظالمينَ إلا الهزيمةُ بإذنِ اللهِ تعالى.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 13 ربيع الثاني 1448هـ
الموافقُ 24 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91516" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=vCM83VwKY7PPcev3XtJzte6l5U6sQ9c5Yn1CnqoxO9Hryfli8iywtNJ45hPz-j9bYtAJBZSgVjsH1HjP68U8bzXQr_b7LAk_ZMm2d9CkU0TSPnYqPksDqKwWtSmddr_ELQyxlPtSTmi7gCxyGtBbK0ZocyguPv1ssSyIB95w_ktKMDOhHOk9N8V9dr2PJpxrtZCP2Gvb29uzQcRMPflwPRTRzR70buVYkXSh_vpFlVsiVanW3-0or-2D0L7Ht_IMomkIRc0XD7ypNe_pQjswo_Y_rSpHybihAXjd-VOaU4hVCztaZ6fgt17fZ2eK2ABe29spJdl_pw5hxrkiWfnMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=vCM83VwKY7PPcev3XtJzte6l5U6sQ9c5Yn1CnqoxO9Hryfli8iywtNJ45hPz-j9bYtAJBZSgVjsH1HjP68U8bzXQr_b7LAk_ZMm2d9CkU0TSPnYqPksDqKwWtSmddr_ELQyxlPtSTmi7gCxyGtBbK0ZocyguPv1ssSyIB95w_ktKMDOhHOk9N8V9dr2PJpxrtZCP2Gvb29uzQcRMPflwPRTRzR70buVYkXSh_vpFlVsiVanW3-0or-2D0L7Ht_IMomkIRc0XD7ypNe_pQjswo_Y_rSpHybihAXjd-VOaU4hVCztaZ6fgt17fZ2eK2ABe29spJdl_pw5hxrkiWfnMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صورة الحاج قاسم سليماني تتوسط قاعة الجمعية العامة خلال كلمة نتنياهو.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91515" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=px6s2OxSvHf1YdMwnWoNsLktjwBDnLALxRKWwzrEkuNUmAQCCABKedqPVtbF6xRR5vaoyXU4fDvc_DidK_DBGMKfcMm70pJQOmP1cIEXkXrbo_h7Cf2L_1zaYWEug2Do37EDmUp3I7mjFnw68nN2Mj6MXZIyMBCgiKzVdMjnSbT4wRRewxwNci4xA6uJ43Bb38k_kyzXHOF0IRiwl8FgIlCbl2U1ttoV0jppRMb464T9sgImqvfmn83JmqKCim-_FJYJTDqM_shVXYa9nL7XV_Ic1LGoVOlDDsJQuwJxrlWKjdGZ1V-cwxDxxQ5mP-_zV0IKi9k-wxifZMRc9IASmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=px6s2OxSvHf1YdMwnWoNsLktjwBDnLALxRKWwzrEkuNUmAQCCABKedqPVtbF6xRR5vaoyXU4fDvc_DidK_DBGMKfcMm70pJQOmP1cIEXkXrbo_h7Cf2L_1zaYWEug2Do37EDmUp3I7mjFnw68nN2Mj6MXZIyMBCgiKzVdMjnSbT4wRRewxwNci4xA6uJ43Bb38k_kyzXHOF0IRiwl8FgIlCbl2U1ttoV0jppRMb464T9sgImqvfmn83JmqKCim-_FJYJTDqM_shVXYa9nL7XV_Ic1LGoVOlDDsJQuwJxrlWKjdGZ1V-cwxDxxQ5mP-_zV0IKi9k-wxifZMRc9IASmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
صورة لطاولة الوفد الإيراني خلال خطاب نتنياهو في الأمم المتحدة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91514" target="_blank">📅 22:15 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
