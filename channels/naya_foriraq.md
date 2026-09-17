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
<img src="https://cdn4.telesco.pe/file/g20pT_YVNV4WUu4jZEcPrShFIrBvPBUCAatYEtI3CoVW7DusHQXChgg3yFuaD5AfLnZGJO6a6FkhycYfLW6z39lOJU7Wx6bnfuwzGfNCH12WrlhpuxqEIL6ApcNC9XbW6o7Jlck_UsC99v-4i_sANwG7SFvnl6Dc_eEtEghjdjTQATTL-2Ql24hddbb-1W22ZGIg1kTiXSon8YjVtY5M7y0o6trRW7Ls3XxEGkIebgsG5iYyPXgB5Gr_zd5UeOi-hyqwg4h6kkUGt_WX5s7AYIbS3Dq_EemKruKxDFkYtXwYoRoN7MuHrgWmg_Ocq8rKuDFB1RjwVHVmaKbG13fg8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">السيد الحوثي: نحن كشعب يمني أنفسنا وأرواحنا وحياتنا وأموالنا وما نملك فداءً لمكة المكرمة فداءً للمقدسات الإسلامية بكلها.</div>
<div class="tg-footer">👁️ 389 · <a href="https://t.me/naya_foriraq/90807" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">السيد الحوثي: قارون العصر السعودي المفتري يحمل راية هذا البهتان ضد شعبنا وهو قرن الشيطان ومنبع الزلازل والفتن.</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/naya_foriraq/90806" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">السيد الحوثي يدعو الشعوب الاسلامية لرفض استخدام مكة المكرمة من قبل ال سعود لخدمة عدوانهم الظالم على الشعب اليمني.</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/naya_foriraq/90805" target="_blank">📅 17:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يسعى لحرب مباشرة تدخل فيها كل الاطراف الاقليمية.</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/naya_foriraq/90804" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/naya_foriraq/90803" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">السيد الحوثي: استهداف مكة المكرمة كذبة كبرى وقبيحة وشنيعة للغاية كررها العدو السعودي عسى ان تلقى بعض الرواج.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/naya_foriraq/90802" target="_blank">📅 17:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السيد الحوثي: المعتدي السعودي استهدف في بلدنا كل شيء ولم يرع أي حرمة على الإطلاق</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/90801" target="_blank">📅 17:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/90800" target="_blank">📅 17:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/90799" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">السيد الحوثي: شعبنا العزيز لم يقبل مصادرة حقوقه وتصدى للعدوان ولم يهاجم سوى القواعد العسكرية والثروة النفطية السعودية</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/naya_foriraq/90798" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يتصور ان قوته واستقراره وتحقيقه لطموحاته يكون بوضع شعبنا ضعيف ومستعبد ومقهورا تصادر حريته ويصادر استقراره ومشتت ومتفرقا</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/naya_foriraq/90797" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">السيد الحوثي: العدو السعودي ينفذ عدوانه على اليمن بدعم امريكي واشراف اسرائيلي</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/naya_foriraq/90796" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">السيد الحوثي يبارك للشعب اليمني انتصاراته</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/naya_foriraq/90795" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بدأ كلمة المرگض ال سعود السيد الحوثي</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/90794" target="_blank">📅 17:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الكلمة بعد دقائق عند الساعة 4:45م</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/90793" target="_blank">📅 17:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/90792" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90791" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/90791" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os1-A0eE2TE3Fqfm38TfMyLD5DLgIV21HfooET_oep_2GNNdICyc_wC-udtdC6hy6izLBFt-12N2DBDc86vXVZ4t2bN7X68FU5ejawAOswCY53FAgrn-Nm9JEhiiB_jPR5ooPbBnIdqWFOVMberRqESMjt2TFMQ0AJEVHIKXFq3fUTL_f_BsOjVTTquYb_ebvWPCaK_OoqXz3onmA2a00-LunaqeBGJSSqB_bOWVIAhpjq-VC1yFP4gP8ZDqxcEKD-OLyjjcuv5EuuWeqLwApC8C2Dd-yMylwWE5TK9895ibiFhacHC5JQ7TfJPUHxBH4Hl707-h7ftRTFasU4uLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/90790" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/90789" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اسقاط الطائرة المسيرة السعودية في اجواء محافظة ذمار</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/90788" target="_blank">📅 16:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/90787" target="_blank">📅 16:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/90786" target="_blank">📅 16:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/90785" target="_blank">📅 16:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1iSioW0NyDobVqhhq0eBbjnONcm_cfLaKx5jY49bRgHZCUg9e5vArJaFCoFo1xGzrRW_EOrr3ls4ajqH_F-h8lr7JX0GDSKf5l4GTLQ9xC8DThIupthR1_tjP1Z7-ScvyaCEswiVN5eerFxFMWatgWPUc2i2h43bZxyQeFY2wCxA3-t6_zizOqSdAe-9ioTrUi8dDU5ttt6xhI-7m08JXr_FCLPOX6l9wDFoYjstgHEr6iHpwufuNUxKCTKK_7m6DTaTL7G2rXSxmu2ZwkfIJMLaFPwTtCLDk7GmOuK5FWlvhkMnfTfsqCcg2_eRbUddlPDESL61pPbnVgOhVXBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/90784" target="_blank">📅 16:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية تقرر بدء الدوام المدرسي في 1 تشرين الأول بعد استكمال استعداداتها لانطلاق العام الدراسي الجديد.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90783" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وسائل اعلام: السعودية تطلب من سلطنة عمان التوسط لدى أنصار الله لهدنة لمدة أسبوعين يبحث خلالها كافة المطالب الإنسانية وتنتهي بنهاية الأسبوع بإعلان اتفاق</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90782" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns3tWI5PhLi4sZVsdj26lsbVBnkSbVBva_NKdFj5CWch-c1yuqQZpChB8Fdj2jU7gcTJ2Tzt4C_cH-a6NLUK0S_iPAKD3c9af3nJ0SGbCPaS9hyn-smn3y8yl6S193sYf7720l5JA4qyJIe7hvcNltJX6FlL1Ib5UArPIyCFm0ypr30c3f1uLUQxrpVCxMzyI2lGgmNFsO8IjFGtyNbXGmOCwsqrLwflBedx135n90rO7Y4PczLONPn2WNKZLMRgGXSA7N4Y7y4ZFanJmY_Unjkclfh_iNdFCfe_C1yzT_dHczUfis51z199OY491iWtf_9OvKsA32eo_xCJVuycYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90781" target="_blank">📅 15:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90780" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان في شمال الكيان بعد تسلل ناجح لطائرات مسيرة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/90779" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKPKiPOSwf4NSwLCz2InmGUqJCjgoOzTUHc6kUxTI7xxJh0Ne2vKBcBdorp9hTGcUKpA6-9qh-DtOKh73kepCC8qCrG_QPahKyE3WOEzTobflDWW7TRlKYehfzXbnh191mPxEbxkCu27e4Y_O0sgjvbOIt47FF08pRUSpOr1Fbto6NbYgp5aJyTkCBHVcDch1KXpl5ewY_pYs6zMzY-CoVZWYZFM3hRQZxvolKDjLZLGnV2o4RTPqcfNlAAytSPuHsn1MDn6ecdhdmkEpdWUkgqwIm4jwzXQXFExsTyDr7YHNgJjIKHXEcdKWtep16WeHjocqWpkM_EoG14YqqDlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من تفعيل الدفاعات الصهيونية في شمال الكيان</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90778" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يتصاعد من كيبوتس دان</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/90777" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اعمدة الدخان تتصاعد من شمال الكيان</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/90776" target="_blank">📅 15:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds_6LHKjsmSeSit4OG3u46rm1ZZzo6Yl8dNMxgL95ViFAv9gSaajKQFIGx8bl0VGLLe1ltJIyEeh4sippx61_MsCzIvVHuLYxE5raFCiZkBJW2GbbGZJBtS0M5oQ1WLCzgjTCRbx72fEuzAEW-uFoQsKwRB-jsrsqNqczXtlSkTFu2xFznXwv4nITeBhxBfnJpGg65fu4M5XhQHC0cwnMXirTqDAWLLo6dbw3w-TMDMFI7slbq7e1QOCTEBGQIsdgE6ZxUJp2DYWkWsoLV8JoFC2MvhVXb_bEzcLEls8RnK2PnGFx-1QKzkSo3VEymMkx3v6PYG0H_62P8zQakQ-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من شمال الكيان بعد تسلل طائرات مسيرة</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90775" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة تسمع شمال إصبع الجليل</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90774" target="_blank">📅 15:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محاولات للتصدي في شمال الكيان</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/90773" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWxkigrkil2DTmKoHbTZbYZG1DGEK5aK_APWxnpBhZJWnUh_zt9WI7lcV7ZtLghgBz3l1iIPGU6GirNTwXm52n2ojgjL1BAWxi2Zjblk2tgi6l1H5vex0ZZEpnNwzkiXEokYchB_ZQdCZ_bcN8Dy7hXWkerHut3zW6qcxn_JcVeO-7ZwUYMW7wmd4OR8ybEyewTOwk7RL9B3PDz23KPVt5bIkvHG1FnEpBbBW4aOMGwbTWiut5_qlJnLh9PVBuyWdlMQOV4TxTOzHqpv-dGv_07C_Se8T7UoVtKOIF4z3MfBqzJ2hnHHZCbvcJdYhpco-cd_prHowMAE9_QeHzsiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في المستوطنات الشمالية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90772" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تفعيل أنظمة الإنذار في منطقة منارة ومرجليوت</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90771" target="_blank">📅 15:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/90770" target="_blank">📅 15:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/90769" target="_blank">📅 15:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90768" target="_blank">📅 14:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي على منطقة الحوبان شرق تعز اليمنية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/90767" target="_blank">📅 14:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇷🇺
سكرتير مجلس الأمن الروسي سيرغي شويغو:
الولايات المتحدة الأميركية وأوروبا معنيتان بإضعاف موقعي روسيا وإيران وفرض قواعدهما الخاصة في جنوب القوقاز، خطط الغرب تتضمن تقليص تعاون روسيا مع دول الجنوب العالمي وعزلها عن العمليات العالمية.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90766" target="_blank">📅 14:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ موجة احتجاجات كبيرة جديدة في سوريا بسبب تعنت الجولاني وحكومته واصراراه على قرار رفع اسعار الوقود
اهم شي رجعت اصاله عالشام</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90765" target="_blank">📅 13:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
ندين قرار السويد منع أحد دبلوماسيينا من مواصلة مهامه في سفارتنا بستوكهولم وأبلغنا سفير السويد بأنه يتعين على أحد الدبلوماسيين السويديين مغادرة إيران خلال 48 ساعة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90764" target="_blank">📅 13:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يدعون لخروج جماهيري كبير يوم غد للشعب اليمني الابي في صنعاء والمحافظات اليمنية بعنوان (دعم القوات المسلحة ومعادلة الحصار بالحصار، وفضح أكذوبة استهداف مكة)</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90763" target="_blank">📅 12:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNYDoeCIS2bNkl_v_iskzzEfhq3LtJK0xbGoAMAenFA693DLcTK2631pMk8j3ABDOSBypKa24RmeVO46cXzCa3eNv8kWxA-ClelBx2ofajRN03XUIfmJSEhq8im-4gb5a_ov48OE4j90b5-tABC1PxBr0DQQUetfB5vMSJ4ZOAlJJ8Xy4uXLy5X8VatDRedhq16Evkvk7Bn-Lc7fMV6a2V38DbcyhF9oQoZ0WxY9Q2H0nSuuUZORWii0Xr4pCDu0UdE2Hh_3kJx6NTdZZrQ8UBDSId89RL9zJh4S692KOnNYU4MiOOaZ58c-6TJu8lP4EGOj78-vyHSVeZhhz9e6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر في الحكومة اليمنية لنايا
ندعو الشعب العراقي الكريم بأن يتريثوا هذا العام ولا يقدموا حجز او دفع مالي للحج عبر هيئة العمرة والحج العراقية فقد يكون هذا العام موسم الحج مجاني لكل المسلمين .</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90762" target="_blank">📅 12:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
🇷🇺
زلينسكي : استهدفنا مصفاة ياروسلافل النفطية. و مطار عسكري في روستوف، وزعم زلينسكي عن أضرار لحقت بطائرة أنتونوف An-12 وطائرتين من طراز An-26 وثلاث مروحيات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90761" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
🇸🇦
🇺🇸
🇨🇳
نييورك تايمز :
حذرت أجهزة الاستخبارات الأمريكية من أن بيع طائرات إف-35 المقاتلة للسعودية قد يُعرّض تكنولوجيا حساسة لخطر الاختراق من قِبل الصين، وقد تناول تقييمٌ أجراه البنتاغون قبل عدة أشهر إمكانية وصول الجيش الصيني إلى قواعد في السعودية، واستخدام الرياض للتكنولوجيا الصينية في بنيتها التحتية للاتصالات .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90760" target="_blank">📅 09:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94042c2176.mp4?token=uJypsnZXIsmFMI-tvXk8ZFprgW5W7ECNGiCgCnN0tomzV8LYtZd9PWrIoXrwx3rdivLuYpgN_dlglfG-3zm9ePs6vG7iMEn2VnY2oRbteE_dklPzDJXFp-wAWKlatOcjsj9tg2TyMn7b9hmtXUpMuWQk2sGtnkUHDDBExFU2TMRr4SClhRAdzRFDM9henCNVTULHkHzsu7fVF5szGxxA0BsAUtDKpm_jGnewDgJhRjgmego9vhWVq4whMuGteOMD5ewGBwZ56aeVDsmriIjP_-U4w0pXpNgSWKhuLfVY0e690HMdZoN5qPcj0Isz4odl5e0LHVlYTzESV85aHkpcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94042c2176.mp4?token=uJypsnZXIsmFMI-tvXk8ZFprgW5W7ECNGiCgCnN0tomzV8LYtZd9PWrIoXrwx3rdivLuYpgN_dlglfG-3zm9ePs6vG7iMEn2VnY2oRbteE_dklPzDJXFp-wAWKlatOcjsj9tg2TyMn7b9hmtXUpMuWQk2sGtnkUHDDBExFU2TMRr4SClhRAdzRFDM9henCNVTULHkHzsu7fVF5szGxxA0BsAUtDKpm_jGnewDgJhRjgmego9vhWVq4whMuGteOMD5ewGBwZ56aeVDsmriIjP_-U4w0pXpNgSWKhuLfVY0e690HMdZoN5qPcj0Isz4odl5e0LHVlYTzESV85aHkpcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
القيادي بالمعارضة السعودية
يكشف عن خطة " مبس " بعد فشل التحشيد حول فكرة قصف مكة، محمد بن سلمان قد يتسبب بعمل إرهابي في مكة أو المدينة ليلصقها بالحوثيين. على غرار محاولة ابو جهل بالاستعانة باليهود في الحديبية .</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90759" target="_blank">📅 09:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇸🇾
إندلاع إشتباكات مسلحة عنيفة بين عصابات الجولاني ومسلحين في مدينة الصنمين بريف محافظة درعا السورية؛ سقوط قتلى وجرحى من الطرفين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90758" target="_blank">📅 07:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=eX_elRKiZrUF-B6BoNXUCztoUFuG71b7Sa31V77ArJYI4fttsn3aXamkP6BrFRoFuHjo0IBYINBsvNrnPfGV9sRPbLZSgEnu8jHUY8bBdj_udEYMmB3PRXvvj5Lb_JLtxz65WCGtaVj90YD1gWJXG7GvPb8Og5Rzdp9Rzp5DZhSjo2vkiiWQFEH0AW9Zgf8karemm3Bu2mQYtKdxwR_JQ2U5fIuHopJoYnioLPTKRFIbd4OCtbpQZJHR8VaKXFZp5-lj7tSjty7dnPMOag2yKXbGL88n7coUCInegKz5pSY1VuQ_p54n7LHEZbu8QQ0WOuCk7_ytQEtdsQGIH7s5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران: بصراحة، الأمر سينتهي قريبًا لأنهم لا يستطيعون الاستمرار. أمتهم مدمرة.  قد يكون هناك ارتفاع طفيف في أسعار الوقود. لكن هذا سعر زهيد للغاية مقارنة بما فعلناه.  قد يكون الأمر أكثر من ذلك. وبصراحة، حتى لو كان الأمر أكثر بكثير، إلا أن هذا كله…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90757" target="_blank">📅 04:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b525552494.mp4?token=HAsul6Zh2TnOSLM60bhbg3hRPs26zZ82H_EmgjNdmw-Z3XBFFijOHileVaoLar02gde1kKHBNfxSPo13MwbcI9ZX0qYh6LgyUZ00CIkPryZP0bChy1SU0_5QPBGUuzFhhSuxsI-Hw7RtO_VCLCxzKXtni-5DBBZDYKuqsOFLwxzdLwo6UOCnzI_RygBXTOS4fj_7xa-OYhdmZYk2-xXDxXuskHBCtNm5t9-nAAc5GQKpR8gdEaFujbXHw7-kStrTXfKYOCOZBZNW0u3K1KDdFI6wxDjDjUFmnpKzy_7MK6oz8kI-xn66KYMNkVyZKNzwzPCz4-ui3oMvhQTze-bzYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
بعد أيام من إستحواذ إيران على قواصة وإستهداف سفن حربية أمريكية.. ترامب: كل شيء دمر في إيران وسلاحها البحري يقبع في قاع الخليج.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90756" target="_blank">📅 03:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90755" target="_blank">📅 03:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76ac567e2.mp4?token=iF1oYSY_pvlCzN8MapNEkLHakG_pLIni3IElpvqbfDPdL3iajhCfzoS0wMQWc2qfR538Vry_yBSPN5K0QytcWwISl3PQ_dyU0-S4s3Kzf8O3OdLxrr63PUSQTxp9xQjGw99jUcGdvK8iImdK5PFq45X-K2ksuoonV8AcRpTTp68JRlwKzWItpZyDeHTY76-NpvetennkE7mxq73xUjpLsvXqwoVryQ75a48x1PKf1Q-d8h7Ri42k4HNi1q2QQOV2vf7puqC02quGrdSH0ezZ1fMIi3Euxa7V41hLhL-tfwVynf7u-4TnVnIp_LLJeotcSuGQaG_A7q7hkHAsSjM5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🔻
ترامب: لماذا يجب علينا أن نتحمل عبء الكثير من الدول في أوروبا؟ نحن نتحمل أعباء الدول الأوروبية. كل ما علينا فعله هو أن نقول: "هل تعلمون ماذا؟ لن نتعامل معكم بعد الآن." نحن لا نحتاج إلى أي شيء لديهم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90754" target="_blank">📅 03:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b367be5.mp4?token=jRbgQgZtQia88r9cSe_mRGNa4PWzlygyZ4AM82X5LvmLU9w_dfXl_00qRd2cHnAa01XaWDggyZB3VWqdT-IvnbfvziyzwyQ-S0k71OpA5NGf0NXvCOVpK3zxqZ09wjLP0LmNDSia-wnX0Q2qwYCRflhwvvxM_UEwc_FZTulKhgee2Jp0h_uH70F5Rl-CJIftsJSKbxkeOhUOyjr1fCZ-6eJ6WnG9jJIZw-0dTivJIxDtBPZXbkMJ5_Rn9ZyDSE-fkukYg84VU0rJVOHXU0PkUi3tDHKnNQTd6eMxZ4-Gs--bsjyQxzFrRzK31mDjq8vktLiPrYSWNf0lp-WBvPcImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90753" target="_blank">📅 03:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a82a8098.mp4?token=gDP8B9Fvqeh3pimO8AXLVka8EL-XdNcP4UyW5rNvZEiARHyRi02bKsNjjZA6nK8EbFJeLldJ6OyDWdUIufYheDeKe2sjWWotxUbD1o3iKwsd6XNN9GnT1XO5o79txjd11y7-yZjh2CGKptvF0UDltOTDfS_eNGK2SZI4NJwpE3_NYKyG0GUZ3IsuWRf724dnZOFgxB122Mhe8M9WPuDSQE8S5QYAX4THiU-g-Mi0VI8HKc8eBH3Fti4xuzKdJrJOGAafU7NKMW16zbw2AsRDBv-5T9jvY5cbMo87FF1GcYV-r0qaCX5_fAoNnJoajFpDZ4sdnREU4ljHzGhQ8RbSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المراسل: هل تعترف بأنهم يرفعون الأسعار بهدف خفض التكاليف بسبب الحرب في إيران؟
🇺🇸
ترامب: لا، إنهم يرفعون الأسعار لجعلني أسوأ ما يمكن. المشكلة التي يواجهونها هي أن لدينا أقوى اقتصاد في التاريخ.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90752" target="_blank">📅 03:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8zZTbqxWUmB-5DaLGmqL_smfKILwUm1rDcQ1BbHKm90CPJW54-zv_IqtCEDGCeVuaYVO2jaYFncWQLHR0SogQ8dJFFafqUs9DXwW1nI0XT8-K9Eoi3g5_qOHPXNBQjE_XE-t27OM3UcpRB9NUwvtO0zIBf1AC6V5RrMQXWAoiOdvzLBir59181Q_Db76D-Y-CUPXgk0cCMqCvQv15qRiRUYz-eijJlB_OKsHFtfomGhzzBxbm5-oWuBoiWcLx-tBRBkWsaF8fnOF3Bx_LVolK2RCdYezVMEbkU9agyN95rD1rGUbc74JApVne679IFIHRVzRca0q6YdqKfZsuXWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e0c180b1.mp4?token=ru7YPlhf59Lt4TdNZiVtgokJRgzxtPN4RDBHzhwx4pTSCL15ec9lR3ZE1YN3s7TtnZVgsuA6ZLZu0j4yeLjx_hInFvG1ap7ui21AR4gOVTjY9nswh4qezLwIwlE9dzVqLFLA0iiH3ZF3Z_mm1b2pFONgHEE5Ny9FJOTEkDlFGYauSktOmflVMO_8XNyR3nv5CWKv7Ogim8F78Ple-dTap2xAjT-JZBD6nj7okeZxvpxrOyAWOYQgG3GJktR53NNNnL6VDdXI9-5D1EFydI2vilXP2yxwc5dx5qOWv87ITcV9HThLgqfF18zzzUi6Bp7LROCrXUFCk5KQWdP1G-Sbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90750" target="_blank">📅 03:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
‏
أكسيوس:
ترامب سيعقد مباحثات بشأن إيران مع قادة وفود دول الخليج بنيويورك الأسبوع المقبل.
‏ترامب سيطلع دول الخليج على أفكار لاستراتيجية ما بعد الحرب مع إيران.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90749" target="_blank">📅 03:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي يستهدف العاصمة كييف ومدن أوكرانية أخرى.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90748" target="_blank">📅 02:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec03755b2.mp4?token=cYR0hVqvJ1yFRxLt36289asHhpwhG0nt1I8lEDQldoZmagJGbxX76xX7VIXKfQUpO3ppoThLYza6Gpn992q_rkpwWTPYrwCxa1xsTv8ImmiVZ0flhrzvqibAaqf347Af02nmaSbwzFnzlvC7Ip3wzwF3M5VAj609Na3mralYHl4Ad8zIO8li1DiWwFAuiNCRSrunRwU4HrUmPluOdNWAMEo31YvmpbzTqnVEKlSKdWBTMVhb0tlj6oUW4rSqgyTqSaykRDMSYp5rkrOWi6koTjCFKcBmj9yCSbxUGWDXNYHflywvgGuiC_8zZWLst9slIjm4ubw-aiH2CMUZQxEkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.  نحن في آخر مراحل الحرب مع إيران.  ‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.   إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90747" target="_blank">📅 02:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
دوي إنفجار في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90746" target="_blank">📅 02:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90745">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9188e09e6.mp4?token=EzUg4jkoEefMubrTL4cSLcfae4UEUr-NMLWxuBuewR46s9_AtwE5SrEjq24ymWmIoPAoiTeegLIfVc-0p4Xtho2AwF9c_bBMkPkXpkFsiOOs6rAXG99hbsbXXjeeHtXZ1_zk1kgFKZYKCZVplr-Snd6Ka4twphFFGRf_VM7kvRep_rOmoUna7TDK6j9qEQ6HXw70AfKzeE8IXprGAYa1Z1I1OQXFmf_B24k_joJkP59wnWMcf9bcNIPyABx0jxJILMMJOKYphy6NUGNXCdj_Ink1w0a_8HVQdvXnECn9noSvgvQvsZf6TpnQw0PkXdCmUq8Oaw44jSB7P7R4X6wC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90745" target="_blank">📅 01:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90744">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
مجلس النواب الأميركي يصوت لصالح تشديد العقوبات وفرض رسوم على روسيا وإيران.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90744" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f566eb691.mp4?token=dUdoirDbWVkxRUnX0miemt65Ji0jxuKbNMF9vj4NpPAu-X_0JBHaFX52TEOffzr6dhX1fTEGsqJAiNix2LxkvYVW8r-SZeVjTxaOdMYEfTIphazqaoyzYWarkJb9Dih0O7a4Rr6qg6OC_n1hAdAR9ik3qf_9W7wF11CzKMd3IidCqQxs5jIo4AGxfF2aLkJAvbnP-qo1qF7chyjlCqoN51illNWjhWNJKypGnkxYpgCAcP_n7vLdUOCipfzlSpk725tJ7zgg8Fvua7bZZ4iCmuQOMjO6pPHIPKzmb0GF0B8744voLcm6ogxQH8MqlMaelIRvn7fb32ba67603YjheA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:
سعر الفائدة مرتفع للغاية ولا يعكس حقيقة الوضع الاقتصادي.
نحن في آخر مراحل الحرب مع إيران.
‏قد نفرض تعريفات جمركية باهظة على أوروبا إذا اعتبرنا منح كندا صفة دولة مراقبة عملاً عدائياً.
إيران تريد بشدة التوصل إلى اتفاق.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90743" target="_blank">📅 01:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6309a31e7c.mp4?token=iB9WhMtWiL5J07Ts15aionHe7bOA487NHg0x6p3HF1ds4I1qWEEG7NYI0msiOVcoYW8hjpk3F8Goy8-H-x81J_qyo8-Bl7p8fdpi-NbYsBEGEYlQyUetsz_Zhx6nEMsmtz6n7gmuSVvqcdmQrlhaW00qmzR1YG3libp-z3mA1zPHjZ3ZmFOvE8eo-NkL_3-P0k1j7DHs0pSG1-03gickDkx9xKXknwJdmXF9QtvHGRmcHb7Lmyk8s5Cyn9HW9IZbKYQnOiHBIq8xr1bhd6WTlyA4SrWj9m5Kjh22bU_tAbPYH3tCE9odhRhQ1k1qndcYejfjlvfCS3NkVBLPYws6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إرتفاع أعمدة الدخان في شارع فلسطين بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90742" target="_blank">📅 01:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3d57b4a1.mp4?token=jqE-1nXDTISJhQ_5IKR1N-tUSVmOWpAkOwAcyJJdbx9BIee5jFxgBXkO3yabmU7p0KYHceeL23-bDnwn1N-2Zh7unrFkNa3r5Pa2B8vl4HXvz3Y1Ye7C9GFTs35dFFJ1i_Ma3j7m_OAfOPZ1ZcFbUaDHEh4EPLSytKJNYRiefA0r9Q-H9jHF_S1OgfgCGbLeJtl7tCAbSo19fFtlDXISre3PVIkpasqv5sMzhXA-nOpKfPVJtU0cyR_VMDSDdNH8qg_O69luZj57-boExwv4lxo34jCmtjnHyfhlCikr2Jx1oIOYPzGY6Tdg2tZM-aBTmWpB5vAwj4KeKtdrpIPKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3d57b4a1.mp4?token=jqE-1nXDTISJhQ_5IKR1N-tUSVmOWpAkOwAcyJJdbx9BIee5jFxgBXkO3yabmU7p0KYHceeL23-bDnwn1N-2Zh7unrFkNa3r5Pa2B8vl4HXvz3Y1Ye7C9GFTs35dFFJ1i_Ma3j7m_OAfOPZ1ZcFbUaDHEh4EPLSytKJNYRiefA0r9Q-H9jHF_S1OgfgCGbLeJtl7tCAbSo19fFtlDXISre3PVIkpasqv5sMzhXA-nOpKfPVJtU0cyR_VMDSDdNH8qg_O69luZj57-boExwv4lxo34jCmtjnHyfhlCikr2Jx1oIOYPzGY6Tdg2tZM-aBTmWpB5vAwj4KeKtdrpIPKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إرتفاع أعمدة الدخان في شارع فلسطين بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90741" target="_blank">📅 01:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4875422f.mp4?token=AZnA9b8i5ROQYq92lMZcciDSKH09oqm8etotgryJFHlJx7XFXH888xtHROPuY5aL_Y8KMxm24kwIaBLdCEQV8J09yfNT7VLolBxBVYAld05w3yi2sae-ZHyidlWTJW3eykdonsiBk2w5sFixjl0lnC0TPBBawvzr2I5kKrf2e5CeNam00ka-GqTQ058zLB3UtBCitsmd6jBEAUHNPPOndQOMB_vjMMDOPsYV0bKI6kB6awC2xh41eYlddpE6Yz9rA1Gs4ujWVF1Qkjlh6gGP9CVc1IrnGcYgwlxOOEPj7bgK8LLgrfTeA6lBIAbB-axhDTlpfzr6Pn9aOywbMqXifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4875422f.mp4?token=AZnA9b8i5ROQYq92lMZcciDSKH09oqm8etotgryJFHlJx7XFXH888xtHROPuY5aL_Y8KMxm24kwIaBLdCEQV8J09yfNT7VLolBxBVYAld05w3yi2sae-ZHyidlWTJW3eykdonsiBk2w5sFixjl0lnC0TPBBawvzr2I5kKrf2e5CeNam00ka-GqTQ058zLB3UtBCitsmd6jBEAUHNPPOndQOMB_vjMMDOPsYV0bKI6kB6awC2xh41eYlddpE6Yz9rA1Gs4ujWVF1Qkjlh6gGP9CVc1IrnGcYgwlxOOEPj7bgK8LLgrfTeA6lBIAbB-axhDTlpfzr6Pn9aOywbMqXifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسريبات من زيارة بن سلمان لمصر ..</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90740" target="_blank">📅 01:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف مدينة المخا.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90739" target="_blank">📅 01:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711935c900.mp4?token=stAhjm_buvhfVrAr2ze-GSUvE-EhoImVuIckD1U401xkQ-5tFgBEk6FKNkHUU-aYyCN-lLZoEOL0k_QNsjT0_YRKyumZ3pjF_z7gCfKb9NOHlWgewXJLi4TlyLlrfSvz56b0hjP66qAI19If2IqxcKB2Qj48FCGMsMA7_5NGlomw1eUiAqIVQSP3JRJTGPSzRa-5fAilLNBrIktPW8_PPMNcISjBv0PjCQtQd3ox9mr_sgjvWTHb6yR2CMNJouq3PX9a5CfaqUr35ofAlzE-aPBVNg8XYByCd4ve0bIWVbrkpPO2btCIBkodrLnqISMC1JvUhQ4p4tydGG9oyiI5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711935c900.mp4?token=stAhjm_buvhfVrAr2ze-GSUvE-EhoImVuIckD1U401xkQ-5tFgBEk6FKNkHUU-aYyCN-lLZoEOL0k_QNsjT0_YRKyumZ3pjF_z7gCfKb9NOHlWgewXJLi4TlyLlrfSvz56b0hjP66qAI19If2IqxcKB2Qj48FCGMsMA7_5NGlomw1eUiAqIVQSP3JRJTGPSzRa-5fAilLNBrIktPW8_PPMNcISjBv0PjCQtQd3ox9mr_sgjvWTHb6yR2CMNJouq3PX9a5CfaqUr35ofAlzE-aPBVNg8XYByCd4ve0bIWVbrkpPO2btCIBkodrLnqISMC1JvUhQ4p4tydGG9oyiI5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مسير مجهول العائدية في سماء محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90738" target="_blank">📅 01:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
الشيخ د. الصادق الغرياني مفتي عام لليبيا: الحرب الجارية في اليمن حقيقتها هي حرب السعودية بالوكالة عن الأمريكان لا لدعم الشرعية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90737" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▫️
‏قررت الجزائر إغلاق مجالها الجوي أمام جميع طائرات الإمارات طائرة مدنية وعسكرية مسجلة اعتبارًا من 11 سبتمبر.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90736" target="_blank">📅 01:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ex2PJNZ4ZVR3OUndMpkRFBUuMJbcOfm57vJNTxQcv1jcIIiZ8Hi_smclE-URkCNdoilwbp7ELivjQVjUi913kaf8VaGH0M_DUPQR3kEdMTsMaJ8Gw9hfosFCYxghU4lF8w983uD-5g-xqNWDT1oS9ap2nzeCYffYUuWNGCUjZm5ZjWEejpedcEAr4i4-8aAZECrumwtFFdySMPPKr_0_Q9pNbauu6A9UMTYD6IkRw8i6bZAbbjzN1dD0m1kMYfLZ1RSKgvBOHLxE7Twkwaql4vnmkanXnt9r3MMQ4kfHFGqLFnNHPa6q1kWVHIwMj_hBizf9HRBb0jPrgBbZNoJvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tY84ctiojtVANtdgyoiJBQ-J-TF0jEodBKSx75dAfYdVdkb7-FyewB9q6yiuayPpnLcfCoi9meJ4tkGdJRw_jV-0_Eelpenvdkcw7J6zWKytpjfZlVOaXSd3k8ycG-S-nx_YabmAdf2QVUSnTyPKwzcXlJDiCda-1LsUWEapgrtCugPjVHLzkAqnrxjKJEC5mX1DdSAZJR8KZUyu7SPAumlVp44uls7oVzIoXKCZvKrCtQ1i9Z8CvNf_HNYNfX-2-Q9jWhRd8qH4nSqiRCFlO3KpQqIPe8aT_N_w4CaD73jYMHoagqx-n1MUEGLS4XdekSPEsiz6unq8tFx3Xh8jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX2XZUaQqmdMQETz8IBsvhq2-dyrCQ6sDfStDr-_Crb3gr0SrJrbr3BDKiv5LL4rt1MAHK0rKTZohvHOZi032eMl3mhc-ydddwtBZXRVLLNDOERot6NQHdL8XnIol2UvashPVRXiJPbmZ_aUKnzphYZekrDE1skjwXutqoPIMYpR1ATDTXYD0MSaXS5rAm_SHkHg35rBILDW1rx9vW0VB6pomyhyqY6aO0OfG4CFSABJxYt0_vaHWrD6ubyPAJqbhvajxSefZFD9Vp8PG_4gX_f8rED2CWbuJDJTRngG4-uWl9Rf-8AH8iDP62-wkvCyVDQBjd8m5eqt440A87vQDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏يُحرق ما يقارب 50 ميغاواط من الغاز في محطة ينبع حاليًا. وهذا أعلى مستوى له خلال الأيام العشرة الماضية، حتى أنه أعلى مما كان عليه الحال عند تعرض خط أنابيب الغاز للضرب.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90733" target="_blank">📅 00:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية
تدين اجتماع الوكالة الدولية للطاقة الذرية بشأن نزع السلاح النووي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90732" target="_blank">📅 00:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
في الاجتماع، الذي قال أحد المصادر إنه عُقد يوم الأحد، أبلغ الحوثيون المسؤولين الأمريكيين أنهم لا ينوون مهاجمة السفن الأمريكية وأنهم ملتزمون بوقف إطلاق النار مع الولايات المتحدة لعام 2025، وفقًا لمصدرين.
قال أحد المصادر، وهو يمني، إن الجماعة المسلحة قالت أيضًا إنها لن تهاجم السفن التجارية، باستثناء تلك التابعة للمملكة العربية السعودية.
وبحسب مصدرين، كان الجانب الأمريكي ممثلاً بموظفين من السفارة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90731" target="_blank">📅 00:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLSNM9aNgXYjskiYgNqiZLdH619ZUwTMFjEJDRkJUZWfON8j-q4blwfx6Bx-xHnWmPSaeZ2prcHV8a0F_8iznJnyOfNbnSijzGOS0tDL5vW043RhnJxeAyBtamekVlRdSERjbUIhB8k4WkrlcI5jghAeuRRnisbL_mApLjc475vOFD4EMTfWnoyjBbQRFcPH7eEnzs7H6Y0QXNW4DQrqYg3Izb2I9fAXotXHmalL6UdoV1x3dd9vZlQhwFPgzAEKnp7tZR3QOhIufeumuo8lkKMtXhJA6pGXeeeV7HTBRxQq6qUdzW_EoRpFjHX0Ql9k7fYzzSeVexbxs2jNBHfE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أسعار صرف الدولار في إقليم كوردستان تصل إلى 158 ألف دينار مقابل كل 100 دولار.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90730" target="_blank">📅 23:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3882df1f.mp4?token=NtNhVfF5_mpGENx7GVkNPV_HwKDOlKSUfqPbeYNf88GgpVDbR1DEaN5io6vHAx9XHjg-W1CwKbhHCg-ypopnlwmNCxvlaMiIJU2H8y17_mMIMJUCwwgC7XYm2vO_83rUmWEnt9JW1Iklpcz5YxxrxnwbludfQC3RufJcblIs6by3MFlKHbG03rCHxT4XW8E3DrfUVNi3hqZOZeEkA1jRVttTz87H7BPLPvHD1jumFmt8LuXne69gKkzJ1pggPIogP4FM4GwNk5t4Pgc9z2SnqUMRuKDlXy-JTSoHEsRAxQQ9y9atsukT04kw2mTJgTg5QjIv5GETj59Fd-e3OML0pD4HBjVK2c_28MKiWQONxczqUQsU8Mwt2G-GZw7zUEXfGLAvgl5Wz4NXUGsxmv5kL7BpSid-3ycAfpjWBIi_n6PVKdoL9ingij1ZTR1Yhzm2gopl-IN49JJ3zUAZfNO5xT2ZQ2pkhXrWBiK_eN1G58G_Pn48TPW5P2QQ7UxvEJmW1V-XJtDy1HzYCKMTUHlO-J1QGLiNGnO2xOMwMszR7eBfEnQIRRBCdEOynFmxSJEnBsyb3STJYA9GRPtIGxhzw6DgBKqUwr1FtTIX8frpwdSNhnuAV7VsKkQ5i6x1A4oxZaCYlUCbH1qugfRPz7SqNYUPwEj133UH7fpiQ2hS9W0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3882df1f.mp4?token=NtNhVfF5_mpGENx7GVkNPV_HwKDOlKSUfqPbeYNf88GgpVDbR1DEaN5io6vHAx9XHjg-W1CwKbhHCg-ypopnlwmNCxvlaMiIJU2H8y17_mMIMJUCwwgC7XYm2vO_83rUmWEnt9JW1Iklpcz5YxxrxnwbludfQC3RufJcblIs6by3MFlKHbG03rCHxT4XW8E3DrfUVNi3hqZOZeEkA1jRVttTz87H7BPLPvHD1jumFmt8LuXne69gKkzJ1pggPIogP4FM4GwNk5t4Pgc9z2SnqUMRuKDlXy-JTSoHEsRAxQQ9y9atsukT04kw2mTJgTg5QjIv5GETj59Fd-e3OML0pD4HBjVK2c_28MKiWQONxczqUQsU8Mwt2G-GZw7zUEXfGLAvgl5Wz4NXUGsxmv5kL7BpSid-3ycAfpjWBIi_n6PVKdoL9ingij1ZTR1Yhzm2gopl-IN49JJ3zUAZfNO5xT2ZQ2pkhXrWBiK_eN1G58G_Pn48TPW5P2QQ7UxvEJmW1V-XJtDy1HzYCKMTUHlO-J1QGLiNGnO2xOMwMszR7eBfEnQIRRBCdEOynFmxSJEnBsyb3STJYA9GRPtIGxhzw6DgBKqUwr1FtTIX8frpwdSNhnuAV7VsKkQ5i6x1A4oxZaCYlUCbH1qugfRPz7SqNYUPwEj133UH7fpiQ2hS9W0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الشيخ د. الصادق الغرياني مفتي عام لليبيا
: الحرب الجارية في اليمن حقيقتها هي حرب السعودية بالوكالة عن الأمريكان لا لدعم الشرعية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90729" target="_blank">📅 23:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇱
اعلام الاجنبي:
إسرائيل تعلن الاتفاق مع المغرب على تبادل فتح السفارات</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90728" target="_blank">📅 23:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9396a1dffc.mp4?token=IjFUx8j9lzHMDUQM7wWIdZrH1FbF6bNo-D7sAERoSBq6xmwLfGizinG3lrkZBF0WU8SKvPwHcuwyiEmkdE3gEadtXdmPSoeQqeXT34CguilSEWzrjiFodKZkXilhn7DsTOUmjy9v6dqP_N_jTxSCavCgS7IKGXMJX20Cyeq-feRkEt3YKzaUDR8Sk5bE4sWponU5Q3jnqsmFE4-u4uutx_9lsFeJklpChK6MpfFnIf033TtjSqQLkx4vqVdCuRzBinUyhb-IVC88JORmW9xESTqombTassi66cqBTbhtTocV2JUGPCWZ3b3IV0-gKswx8Fe3Bb4Wid7f7kcrycDB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9396a1dffc.mp4?token=IjFUx8j9lzHMDUQM7wWIdZrH1FbF6bNo-D7sAERoSBq6xmwLfGizinG3lrkZBF0WU8SKvPwHcuwyiEmkdE3gEadtXdmPSoeQqeXT34CguilSEWzrjiFodKZkXilhn7DsTOUmjy9v6dqP_N_jTxSCavCgS7IKGXMJX20Cyeq-feRkEt3YKzaUDR8Sk5bE4sWponU5Q3jnqsmFE4-u4uutx_9lsFeJklpChK6MpfFnIf033TtjSqQLkx4vqVdCuRzBinUyhb-IVC88JORmW9xESTqombTassi66cqBTbhtTocV2JUGPCWZ3b3IV0-gKswx8Fe3Bb4Wid7f7kcrycDB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مستودع نفطي بمنطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90727" target="_blank">📅 22:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb41645f5.mp4?token=GNbTt9kwWmRV3gPtOU6bvYVw--qLG3gQEdxuLJYD2h2Cko64bfRfJzuhZtb63xWtpdY_bvun_53H74h_4n2bWgkcqoIfZ2_gEPVUJYjcR1qr_eKCCtdXanEs_ggjGhPWmjgyj3g0uo_E3If9Rlydu-dBM7h2u42iX0qbF25W0pVnxVhHLSwvhQiJt7R2FVTaXGAvQmSqgHpWFd0Q4c3HI7SmJhcvEFPoVwlyhlw2Z2z0P0Riyf8I8Qz-tRbp4vN07FHsJvuJqXnlMww04LuJa83B3jgm9Uvvr-sK9u1hYyE22SmmxANQPHmek8TLkd2jeX9XnBzbfQa3vCEi9JiHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb41645f5.mp4?token=GNbTt9kwWmRV3gPtOU6bvYVw--qLG3gQEdxuLJYD2h2Cko64bfRfJzuhZtb63xWtpdY_bvun_53H74h_4n2bWgkcqoIfZ2_gEPVUJYjcR1qr_eKCCtdXanEs_ggjGhPWmjgyj3g0uo_E3If9Rlydu-dBM7h2u42iX0qbF25W0pVnxVhHLSwvhQiJt7R2FVTaXGAvQmSqgHpWFd0Q4c3HI7SmJhcvEFPoVwlyhlw2Z2z0P0Riyf8I8Qz-tRbp4vN07FHsJvuJqXnlMww04LuJa83B3jgm9Uvvr-sK9u1hYyE22SmmxANQPHmek8TLkd2jeX9XnBzbfQa3vCEi9JiHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مستودع نفطي بمنطقة التون كوبري بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90726" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
الاحتلال الاسرائيلي يقصف ريف دمشق بعدة قذائف.
جيش الثورة الالوف الالوف
😆</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90724" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
🇮🇷
الولايات المتحدة تحقق في علاقة بين إيران وهجمات إلكترونية استهدفت ناقلات متجهة إلى ولاية تكساس.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90723" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية
: ‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 40 غارة جوية بطائرات "F15" أقلعت من قاعدة خميس مشيط مستهدفاً محافظات تعز ومأرب وحجة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90722" target="_blank">📅 21:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
بعون الله وتوفيقه تمكنت القوات المسلحة اليمنية وعند الساعة 18:40  من اعتراض تشكيلين حربيين سعوديين نوع "F15" أقلعت من قاعدة خميس مشيط فوق أجواء المخا بمحافظة تعز بعدد من صواريخ أرض جو محلية الصنع وتم إجبارها على المغادرة فوراً قبل تنفيذ أى عمل عدائي بفضل الله.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90721" target="_blank">📅 20:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
🔻
وزارة الدفاع العراقية تنفي صدور برقية استخباراتية بشأن نية السعودية استهداف مقرات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90720" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇵🇰
وزارة الخارجية الباكستانية:
في الوقت الذي كانت فيه البحرية الباكستانية تجري تمرينًا دوريًا، قامت سفينة هندية بتنفيذ مناورات عدوانية في منطقة قريبة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90719" target="_blank">📅 20:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
العضو في المكتب السياسي لانصار الله في اليمن:
ستواصل قواتنا المسلحة، بعون الله تعالی و تأییده استهداف القواعد العسكرية والمنشآت النفطية والحيوية داخل مملكة آل سعود، حتى لو وضعت في كل منشأة منها مجسمات للكعبة المشرفة.
فنحن اليمانيين، أهل الإيمان والحكمة، وأحفاد الأنصار، وحماة المقدسات، أحرص على الحرمين الشريفين من عبيد جيفري إبستين و ترامب ونتنياهو.
و تهدف عمليات قواتنا المسلحة إلى رفع الحصار عن شعبنا اليمني المسلم، وإنهاء العدوان على بلدنا، ولن تثنينا محاولات التضليل أو التذرع زورا بحماية المقدسات عن مواصلة موقفنا المعلن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90717" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارة الخارجية النرويجية تصرح بخصوص قرار داخلي عراقي:
ندعم قرار دمج وحدات حماية سنجار ضمن القوات الحكومية العراقية.
بعد النرويج الحزب التركي حزب العدالة والتنمية:
اندماج قوات "مقاومة" سنجار الإيزيدية تحت سلطة الحكومة العراقية أمر بالغ الأهمية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90716" target="_blank">📅 19:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
🇸🇦
الاعلام الاميركي:
السعودية تسعى لإعادة نحو نصف سعة خط "شرق غرب" خلال أيام.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90715" target="_blank">📅 19:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPtj3WOKlmXzc2wT-MjqjZqTecVzH3Ow6Quq4t2j_63hsU1IOxU2oYxzH6b0GVne3z8WQShKFA84ytYb2YlNBkdq8hCVanH50zTurFd16QRxEywJ58UYksy2ianmr4vzngOa6Z4MWdBsDea8Oi3gV_Gk3xKSSgrIwFqRhyr9-RHKctWkdNjwZtdezkEwHxreFp7sznDKXG-V7uJbjdjwNyhNHErTw-o4hJI8Lj19K5ZqLi50spy0ARfQubSlZDXakRmzlwAIMa5TQhqlLY7KNgjNWgaIBRwVXr-I6QWjAre9vffTYJgdJZCTmMy6z63F8R50wO9n8dJHLA36P6rUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F-15 وحطامها في أجواء محافظة مأرب بصاروخ أرض-جو محلي الصنع</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90714" target="_blank">📅 18:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📰
رويترز:
تضرر محطتي ضخ على "خط أنابيب النفط شرق-غرب" في السعودية من جراء هجوم الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90713" target="_blank">📅 18:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAAFqqRZl4ucCmJkcX_lCVhSvAdMzjWVfQKZ2HuIMCHAM4aBiHOUiCuSaMPVMXudH5unZjmyWDFUXTtgJQ_J5bNL9C9gvaZSsTl0842Pv-7Kzt1tXi2nTj4v8tzeSLVLhQ0TEJjH75eN9OsQPqOO6xx7E4Yczp3uFc2gOsKQVHTWgxPVtkl8ItFp1OteNEZWQVUoFm98LAcTLJvkQq5NLfiqj7Sch9pDuDr3PI9XNUgGNK8MvEw05-jXXU1Dx437ZWpvBLSoznNGSDGpyQFpXhAXKtP2TrqUhdx1fZXAU9shaDCiq3pOMLn4_dBzJZ2P2b17vqc4qAIra-ahAWHdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
لا يمكن لرفع أسعار الفائدة فتح مضيق هرمز، ومخاطر المضيق تنعكس على علاوة المخاطر وأسعار النفط.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90712" target="_blank">📅 18:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUjiONE5mCb5NjTdK_wsbRthM1z5qAs7PzZ_ViLaGzUHeRz1hqngDIY1zWBArau0FeZPeGd5u60R1jSLuyR1-uybPdiP0OtdGuFolksoHF5HsKqhMbuxBRtAnoaSL8YRiaKA2KXyMzGm63F93-ZI1IbKFJeMbjAzpX1C-TrX7cKbHpS0yZfl6NuUMrT9y-tk9dbS3qUziwHauk6wFSOK8LPbBMoi7mMqNCiEyqoPouT__3rgGaKRZb6qnsR5xwdjF0fJhLF8I2eoixphW-oR4GWm-AWuKNJHEJq2J4LP7hTLhZ7k_JvanZGT_CyWI3DAqZsDUit3cx75pF6etGrlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس اركان عصابات الجولاني يلتقي قادة بالجيش الروسي في مطار حميميم باللاذقية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90711" target="_blank">📅 18:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
🇷🇺
🇮🇷
🇺🇸
🇸🇦
تقرير اعلام أمريكي : تم التحليق فوق قاعدة عسكرية أمريكية في السعودية من قبل 14 قمرًا صناعيًا روسيًا تجسسية قبل يومين من الهجوم المدمر الإيراني عليها. التوقيت وتسلسل المركبات الفضائية فتح الوصول إلى طيف واسع من البيانات. هذه البيانات، وفقًا للمصادر، ساعدت إيران في تنفيذ بعض هجماتها الأكثر دقة ضد الأصول الأمريكية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90710" target="_blank">📅 18:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
🇮🇷
هيئة المنافذ الحدودية العراقية:
سيتم إعادة فتح منفذ الشيب الحدودي مع الجمهورية الاسلامية يوم غداً الخميس.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90709" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1543a6daad.mp4?token=XJ1Nro_780hzttCSeHygPW0ZvkX8KonjMopaBEjAFwsAZsJn2Lvi7ntkDcsUFTpH_M_v_5_0r5iBGDQLsExMvpTgndwe1DKLwZ1j5Q7KTC8kgLly3XOsK9Vgyd5gkcqvxOXu05S2ZmIBBL_GyoTfSK0NWaxhANOwnsqrG3yaYsQb3zYWvbjBbWi66QxZPvN1EeOV7wqE-TZ1KSe6gN4uOiju6khPQrz-d6glPKmtrxC3_-iyyevNWcRCYk6jBtXW_TgWNqYMZCav7xPrDUX05lWV_OQGvymKb7h1yCQdFMAA3CUue8bpuXktm7iyBzh8txZGb0DdSjzDOalsoyzIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1543a6daad.mp4?token=XJ1Nro_780hzttCSeHygPW0ZvkX8KonjMopaBEjAFwsAZsJn2Lvi7ntkDcsUFTpH_M_v_5_0r5iBGDQLsExMvpTgndwe1DKLwZ1j5Q7KTC8kgLly3XOsK9Vgyd5gkcqvxOXu05S2ZmIBBL_GyoTfSK0NWaxhANOwnsqrG3yaYsQb3zYWvbjBbWi66QxZPvN1EeOV7wqE-TZ1KSe6gN4uOiju6khPQrz-d6glPKmtrxC3_-iyyevNWcRCYk6jBtXW_TgWNqYMZCav7xPrDUX05lWV_OQGvymKb7h1yCQdFMAA3CUue8bpuXktm7iyBzh8txZGb0DdSjzDOalsoyzIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇶
‏اقليم كردستان العراق يطلق سراح صهيوني محكوم بالاعدام لارتكابه جريمة قتل على الاراضي العراقية بعد تخفيف الحكم ثم العفو عنه وهو الان يتجه الى الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90708" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية تسترد من الإمارات مداناً هارباً بأربعة أحكام لاختلاسه أكثر من مليار دينار.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90707" target="_blank">📅 18:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇱
🇮🇶
‏اقليم كردستان العراق يطلق سراح صهيوني محكوم بالاعدام لارتكابه جريمة قتل على الاراضي العراقية بعد تخفيف الحكم ثم العفو عنه وهو الان يتجه الى الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90706" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
بعون الله وتوفيقه تمكنت القوات المسلحة اليمنية قبل قليل من إسقاط طائرة استطلاع مسلح نوع "وينق لونق2" تابعة للعدو السعودي المجرم أثناء قيامها بأعمال عدائية في أجواء محافظة مأرب وذلك بسلاح مناسب.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90705" target="_blank">📅 17:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5KhYFbh-RqNJ54BuRgrs9u8LtQNZQxZ67fhJwNTMs1QGlTE9OMu_fWgbfZiSZgGY28CKA0Yg-hdWYkDf-G6FcvaAucZ8kfVnatlcSPDzxXUDxKx8eeKSPIL2gTre6IfRJ1ztlftNFt4V5fJUZW7lltH_p4UD8OGgtumqSm1u2c1OdD8TTUzmS5ygsWR_Hg0Wwzdejonr3GgQweFVZZUZCKZVN2xtYG5t7fLO5rE4NJN6VQOl0H3sGWrl73g06jnOZO-2D_9vv4IiBKFVZ3Mh9bZuHyWlv-hNyjJ0H6NyQd7uMjP_zYoUpTY0AZbxpwRagI4hBRucGuLGbOAArjxCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMuY1znP0N-obxqUPnBzrxDHCdFGnWQ9OikcqI3VTdA5iE2abWsUzzcx1FZQtbQiXLCbpQ8YkDgSDDdha3A72QAJrffKviRr95AqE0WN0beKvkZvSP64TuatDlUqS5qz-VJQjHO_Eb1FWS1hvh79DpAdrjh39gkj2g6MbwTkYrqM8-Vz9nwXzrezHADigGJ3a5aB4yfuhm79Sa1Yr-j5kGtwu67gSV3lx68IhvVjDTD5Kavuo4p7qtQV6DyPRGw9nWB3qHT5xLw5t5L1Mh5bYOlrKzw4GXwHNkuZEeNQ888Ro4yvYCDFOZLLuDdfBLlaZovQD1kvzBW1Cz9rH8QT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOepW_VfIZcx7eQ9ufdBh6Ls8o_31tpyb12__kxr0hWKU9IylVNuK3dztXhnfTmkmgXc7YxuMZV0JCIwexe0MUqnRowDjI4tezs8gtW7Ell_pbEOXWeCtCABIeUn9kzJ1bUV-WkKxBfHH2AH0wgnqwmozkH-1JtDLXIV2SwlFx7VZ_7w5QkfD_4HDI2WLBXe5h_gvElTHzvMHWT2So7opg81D0Jy3dlIfOGLBi5TnPN4pS2De8X0lcV1QE8yLGRYqpkee0sxu8NYCVdU4eIr64C9-mvquH1HMxVv9bvEuBSKTPqiXy55_e30e2doKb2mxIqLLO2aqJnXeBLOG-3t4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbVLO7hxL2cjKyC2QYXyQJ1KLF-s0FFZ7kxa7WprZj_Regcj0EZdjKn-oSGlI8HKb4OzpwSP4Onq27k467EyFIVR87TH3xJgjWAmrWGL-u7SeiWA6kkAnEYIxh91WZi3gztPv58CDFI49DtsYuSf6c0Yr027njKJcLDpFltXJL0Tkwnj379q-QPf5WM5YtNbhYDcrw6Dg8vn1OAIHqWp6oJzqsVylrECqIlC_oFxebVPUr_jdkI1EWCuTU79CBGHWyT35Ns3YgsxGL4hAQa2H6DXfhpehQQMH78F9pi9XWFOTGHiWI8X2cSQQ1BqndWTA-spa0pRXpT-7VOHgMHuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0VQqmox-1eTHnwz_uAMGScVe10J63CYljYYH3fNxcXNjtPW46CpP9C0mPBy9G1Q5b7sRTGmLidbTZrYV5S3Evv6Y1kCblGgOAuS8KB4gkzUpcoJWs7cyPvOGCaLibvO38iausu33qAN-nu-pE6PQCoUz4bcDNQzB8LssjY6DBVnppOO8fwdac5VsVKFjwGlwc-PVvFMSsBT2mFKdS4Ggb8RRb4l6-z9gKvwbsvkwXFql-LX7rx0xzYtj0qXB_c6rqaUCA3EcOpHwVjDRrZQ1Y_5-Vqbj2KF9TMZiSRxV08VUvFRv8hC1BkcDhbGrnh6-ySr21mgKSf0nDR2Ka7cEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ_0HWcje-s_L9mD6KKcHQWukiDgdsv6p0JwfrAxnak8oCvwo96VusPRz_sUMGZcggKuyvrU0LogO2NPdMFMJCOldc7Zx18ZgmuhKFSOGihEkaaSxeCK5DTdEbhvzhqllc04GW49kEba5FChoPTahMQshRVqNB6x4a0F5h8qypavQqNuLtnDe9Qgng2KUIx1sL3bpFsBi89D1BzC8LhnkH7zoqQH5X1VXAHy521pZ_JoRAdCrrXLAb3NAjG9-qmUkWGy2UTwvT0phaOgCBJoXc0sx5CYg5isGwyfk2Vi-Zn9212DD_Ktb9jl1Ng-lq3EtVfHK13UrzI4dO3nqj25Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoJduKi9pR7If5WJ0hrb4BFwnwUK-bMfDXAVyoqQhUnOCi-e2GikROa69plb-07ozxUX0vlVHo3FssGrq6rIyft4_sStcETRzi8LTc4EGa9z-aTXv9g5jcBhUpNASBvgomAyRlozwL5_TRVxt4MCLUv2lJ2teb76dYGxCnU9Hh82NQlXYI6exEySCH6qrZsHMJ_yY-iexhNHnihaBSlrVfLv4uFRR9juESrC1r8L59i-iz21aljy58hHhC6RI2MGqOhVxz-Fmk7CnhBEipoqYS9OFpa7eW8dTbExABC1HVXQonIq_gjUGt72ErVKIV45AK_2j7l7HHMDAxNBnjcuIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد نوعية لإسقاط طائرة مقاتلة سعودية من نوع F15 وحطامها في محافظة مأرب</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90698" target="_blank">📅 17:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/90697" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
