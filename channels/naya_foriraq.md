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
<img src="https://cdn4.telesco.pe/file/GeTB2c5Is2Ktf6albDP-GXldD8WbLb7pkPpkm48tpTFsZvWRYDsUOBkBoNeuTxnz9DyBJzxfSpvs0BctmDcXrx2q-wO8iCGDsxxjrTHthSwTgyIZkKmPc1fT7_PhN9kfWb-dJShCAgUVgx2AO-xEl6CYi5Sv4dOZc0eJGKzIsHntDFLb7yorEbC4UXNg5AAZt5O5wVZ2vcqrh7_f1wG85ASDe5xt6vaL2kLRIop0lgOxVGeA-YBK39sOWXZA6ZJLwMh2KuIBzUMJz3bSSj30fndVHieUGtIu_N04HqAHCC0AaWkvePpyJyt8BQ_eTYH9i7xjtN9WTw9s5hwN2Y29QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 269K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-88639">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4-c3X0GWjRMpxPkM0FEFYuvRqF31RIyMZPo8boiF2IvisoHcICEYnksGSpdkxC34jMcXDtwYIozhJkfkA5BAiot9JCPt0MIq4E9fHbGnoSO9B1EMD-2wTIXUXrKNa36JAINxgOiG2vfdv3ljWF8rp0VloFfMYS9klDl5idyrT7RqDLvUEEX9Wyy9YcDWSDFFMNNVdZ605J43QGWQcsRjhvz1j6vJJi4CGvumOieBM6pVe1azd5gJH8PLy4HFpT8uF-_5Dp3PbFZ_U8YaWtVohV3WyuJAeU_9twBC_P9vIyTatVqiRGw7yi1vKEitACvjhgjwxII76hMqgwwwjPRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
بدلاً من ضخ مليارات الدولارات إلى وكيلها الإرهابي، إسرائيل، و750 قاعدة عسكرية، كان بإمكان هذه الإمبراطورية الفاشلة إنفاق تلك الأموال على شعبها، لكن لا، سيكون ذلك منطقياً للغاية بالنسبة لهذا النظام.
‏يا سكوتي، يا رجل، مصداقيتك على المحك. افعل شيئاً.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/naya_foriraq/88639" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88638">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني رضائي:
إذا بدأت أمريكا أي عمل ضدنا فستحل كارثة على مصالحها العسكرية والاقتصادية.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/naya_foriraq/88638" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88637">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da9299db7.mp4?token=ndwrgCaZpwuKzpuHyMgkOTgEbp0XOiNKyc2ctGWo-NrLwaOwsjhM6jwI4yJKOOi95ARksAV_uH4g-GYwWzqJALWQmb_p3rX2j6PcZG4MQrLV8Tjr7v2uyShPQWI9czubL4UMGlcZ4B06hdBAFOIv6tUlRDCM2xurJVEGhbyiAow8i23QPS7jAo-lKjV0AZyGrDm_IoCeXk0TtfXLo58Klt2m3Qdo2DRCNdzv-WEpU-Lgk8Qiqote7R_TeLhEz1RFIJHclZ1FJFngHLgOQqzt3EAPnVFOZJcbAjZ65ccIboSU4MSMUPf7X0H0ugcNLYp8_-uanl2p-_J-1KvRuJLiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد محزنة لواقع الشعب الكوردي في شمال العراق؛
مواطن يمسح شعاراً سياسياً كورديّاً عن سيارته أثناء محاولته تعبئة البنزين في إحدى محطات محافظة كركوك، بعد مطالبة المصطفين معه بذلك، ليستجيب ويمسحه دون تردد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/88637" target="_blank">📅 19:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88636">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇾🇪
الجيش اليمني يشن هجوما على جزر بالبحر الأحمر بالصواريخ الباليستية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/88636" target="_blank">📅 16:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88635">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
وزير النفط الإيراني:
حوالي 40٪ من القدرة الإنتاجية المتضررة في حقل "جنوب بارس" للغاز قد عادت إلى العمل.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/88635" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88634">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
لا توجد مفاوضات جارية حاليا مع إيران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88634" target="_blank">📅 16:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88633">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88633" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88632">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=PkC4HrAAIs0AwNlRaHJfhdBS5m_bAh9XkiYZjqhuNFW4Cb4vg3ntbqZlnrWuLoVyuqjxJ56ZTOopNJoMCaMgU9uxu0M9EO5XDPYK9eSbGbAgkCoklT82WkzD0bwx-pXSTWHXeI1_8_EmrfinVxq8Zqq0zDflB5TIJ8IspRrr_-p__2o-Nb36su7NNRRQZ3B3VZGy4q_TB1WO5CeP_J4TB7INIhgNlG6a8eo1hNmixMV9RzXX6rsCHtwWkcMTYEyvS5tfLirKZtUcN5mvOI-ygi8B0wEYJQXkZaQu1rxEBKF3sfsdWbT_qFjb2ZpH4KaqExhpGWWu6h-6-hXDtghEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a52181c7e.mp4?token=PkC4HrAAIs0AwNlRaHJfhdBS5m_bAh9XkiYZjqhuNFW4Cb4vg3ntbqZlnrWuLoVyuqjxJ56ZTOopNJoMCaMgU9uxu0M9EO5XDPYK9eSbGbAgkCoklT82WkzD0bwx-pXSTWHXeI1_8_EmrfinVxq8Zqq0zDflB5TIJ8IspRrr_-p__2o-Nb36su7NNRRQZ3B3VZGy4q_TB1WO5CeP_J4TB7INIhgNlG6a8eo1hNmixMV9RzXX6rsCHtwWkcMTYEyvS5tfLirKZtUcN5mvOI-ygi8B0wEYJQXkZaQu1rxEBKF3sfsdWbT_qFjb2ZpH4KaqExhpGWWu6h-6-hXDtghEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
صور الأقمار الصناعي تظهر أن هجمات انصار الله استهدفت قاعدة عسكرية تابعة لمرتزقة السعودية في الوديعة على بعد حوالي 23 كم من الحدود السعودية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88632" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88631">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ذا أتلانتيك:
يحاول البيت الأبيض إبعاد الحرب الإيرانية عن عناوين الأخبار قبل انتخابات التجديد النصفي. مع استمرار الصراع، وارتفاع أسعار الغاز، وقلق الجمهوريين من خسارة الكونغرس، يتجه ترامب نحو فرض العقوبات والضغوط الاقتصادية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88631" target="_blank">📅 14:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
المعارضة الايرانية الكردية المسلحة الأرهابية
: الحكومة الإيرانية تواجه عقوبات اقتصادية قاسية.. لن يقتصر دورنا في هذه المرحلة على دور المراقب وسيتم اتخاذ خطوات عسكرية وأمنية وتنظيمية ودبلوماسية. استعدوا ميدانيا</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88630" target="_blank">📅 14:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47828875e.mp4?token=cmrhPbR4eWO3JSyLJONk71znn6RBMWuuaGTWMLjc9f6CGGVriBHqP2swQZNQKXZYoyipglOaISBmiSUyKi5y2XNabjcVBVp_LkkVALhyRl1u__ejmIBfq3aMLgCeSfhOScbY8xjhDIEDGGnkIDu4Uy3jUa-7wBDe6AgBlkPEhp3AVMHUGTqh5MspB9w3GuDB06VOVcSKFJUBkRGXh5cjhbcJEANj4YgWBIf2GPNtUBfzdiuapEbuiqwdOCMBgC92eDVtgK6FwlQFNXHFfQxfvleRummXvZkT83WOTGSraUD2Y26bxZHXcTupEkWh_VMYgU7WYCd2de3hKwADoy20uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47828875e.mp4?token=cmrhPbR4eWO3JSyLJONk71znn6RBMWuuaGTWMLjc9f6CGGVriBHqP2swQZNQKXZYoyipglOaISBmiSUyKi5y2XNabjcVBVp_LkkVALhyRl1u__ejmIBfq3aMLgCeSfhOScbY8xjhDIEDGGnkIDu4Uy3jUa-7wBDe6AgBlkPEhp3AVMHUGTqh5MspB9w3GuDB06VOVcSKFJUBkRGXh5cjhbcJEANj4YgWBIf2GPNtUBfzdiuapEbuiqwdOCMBgC92eDVtgK6FwlQFNXHFfQxfvleRummXvZkT83WOTGSraUD2Y26bxZHXcTupEkWh_VMYgU7WYCd2de3hKwADoy20uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇮🇷
وزير الخارجية الايراني عباس عراقجي يستقبل رئيس الوزراء القطري وزير الخارجية في العاصمة طهران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88629" target="_blank">📅 14:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=laIkxtlWlPyTeTvALcNoERjV2xq6na6nyBuNpywTHen0bmnKvPHWxJ1C-yxqjsggnmwIG5YH2Sc5sP5I-YjCkhNQnGrvhse29L62c_T9Zng9Y6wxfkaA6y8VYs6-NZKgE34NuZ8OID2IHec5BXrdJCuScjA3Kl03Zr3bsYPCcofxmbn4qsuUhN-HmCzfR1yffEE245x-UCOby9RytHjjDZ0V5RSG74vVP9de1OBfDCyfZWJd_lOly6P3JFjdmRyRJUdEt2cIuZ2u3-rINiAPT6x6pLVRBd6Grjwr_-JP-Kjd09ogiPAX2hJyc0gEf_c54Ww2RE_g5pbOyPKU97asnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981ae7d7.mp4?token=laIkxtlWlPyTeTvALcNoERjV2xq6na6nyBuNpywTHen0bmnKvPHWxJ1C-yxqjsggnmwIG5YH2Sc5sP5I-YjCkhNQnGrvhse29L62c_T9Zng9Y6wxfkaA6y8VYs6-NZKgE34NuZ8OID2IHec5BXrdJCuScjA3Kl03Zr3bsYPCcofxmbn4qsuUhN-HmCzfR1yffEE245x-UCOby9RytHjjDZ0V5RSG74vVP9de1OBfDCyfZWJd_lOly6P3JFjdmRyRJUdEt2cIuZ2u3-rINiAPT6x6pLVRBd6Grjwr_-JP-Kjd09ogiPAX2hJyc0gEf_c54Ww2RE_g5pbOyPKU97asnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات أمنية كبيرة تتوجه نحو منطقة الدورة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88628" target="_blank">📅 13:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88623">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfQ5gmipLMM43Iorv_N04OiU209jqdGuCqOCL6dWMeclYGml0sEqRnbx3gVxMzCr3CCy4ckhyC2z8_w52K_mKPTaKIwhtMBrRqq1UsDpYV_8IFy1g7gBato0JwkQUrDMMbZyBVVHE9xlEr8NO89rDQSNWda3RsxB1KDOxod5zTHTDuMoVynZGiJxLsWSWGqcAjO_by1Gsa1zT428Y_ULysp4Ri7b-rgWuVdCJ0F2yVs-RzAppGLUI7OrENKIFAUNXiv-K1CmydcT7IJoQs_BmvPi5pnXd48j2NYH_7BC4zNU8YiLIsJJ0mg5qqGpWwEYM6O3Q_htGa6R8rAe5ahb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmJvMwogG-9HwMJrwI2eVUHLtzCkmoz50zn583YbEFiMBsovg15CeyXIkE2zoY0l_8_pxXeoxOUDgQ01qbDzuqP5gaV-lp1aORjx56lGXFR4jatN0az5chYVtkIKKAhkBwKjqaxq10mG4_cwXoiOKHOn3DTNVhxipYcRxXDaNxs2VMO6Nei9kwR_35yGFta-RaHJNzxbIzQoy2JYLG8DFGVrZbl-hqm4KVIEHqrINDMVrQxfnfvg-rnTnD5HSuVyO7qgouSHt1E0RQ3JayUyWSZB5G-MrwV4W6wRtjJtrOu8MZhUvNkgxaTd__w_mZ_Yis8suifNPyqE65dqg2ryZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjwd94huIkAE21XONIsHjkW5fKMKl2GiSq03k20QhSSLVxnh750hGtF6dIsvPFye22FgOQ3rbtXKpUphM3IETGoSt1NaoDD9haxko-sy_wkl8jxf-1vskONkGsmSW_ptaebo6BnG1XT52UNGwii2KYte5ZSIhJLIuI0q23lVM2ZpyYkPWmfThqZAi8edVao5Mb7lpbF7oYPmkhw2MYX1PX7nt0tMo6RHxgrGx9Wi_qylDNNddlfTy6JhGh8jtjf0Cd_sHlvpVvnsDDC2OLxR7PlGbEFKjydmyNEaErovRM18zfrDfPKe_j-X8ZNyPXxy7FNODCP9ihBxgmvc2c1T1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE9Y7E4FpSwjQiZ1avefvgqmqQgErLp9hPzPTgkzaipM75PH8oOCTOOT22FZdqNEmOedzOullkgbnGuERNs9DFB9d_9HUHgRZ9mIPXkZS8c51p6JPejfgiD62TqXb_LUCQa5JPa3M7CnRGG4wtTnRFnI-WVe8gldgJMtgGAwKncvAAFagrc4eHY2-ujY1bMc9pkI8N2NV3p2nTAykNm2-gxLpm26w2-RbDzgUW_IETWhDFauhJ4rNYq_mLo9FN3ZemQuoE5xUvErTM9Q73NBs7adwZrlTgUfHC_ZimlltsqkUwKKw8ynXvsKc3Y8mSEpjX_nfsbhrvnSLwQMA_0CeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEGlEpJHPeXHERXtt23ve7m0D2SaUdVmbO44xuF5E2Bq2PwcMsdnNHphxBvtW_BfYZZQFLNJ-aVdXjWZXToWBVlSGXkhApGxvFXPIaDlYi-o5NfUJa0_pabszRZHz30m_IqWceGWATKiFqLR6LdhUS3Wg0a2xd-goN3biH379r-MUMLA79fWgcWqPFvI2x_vi9tJicd5sx9kkD5c6PGaJQqBk27WpgTOGrkBZL50TsQXOY2hhnX3CSAGCCetXTSLC6GiCF4gD2Kj4r1iz6IXQn-69I7C8IQDrU6Drw4auJ-GxgLX0__GTnH2w9ttzLVObB9yMBJZxbaevA0OQa2XGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88623" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88622">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:  استشهاد ضابط برتبة عميد وأحد منتسبي شرطة بغداد الكرخ وإصابة أربعة منتسبين آخرين من الشرطة الاتحادية ومغاوير شرطة بغداد الكرخ أثناء أدائهم واجبهم ضمن حملة إزالة التجاوزات في منطقة الدورة ببغداد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88622" target="_blank">📅 12:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88621">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88621" target="_blank">📅 12:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88620">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMYfQN0DXTF3_W5OUHADbcxcw41lVulQiPYRR5bKWnzy2B83ErzDRsgdTzIrLs_APi6dPb-OAZGIYQLCfAhWwhB1jODUaeBgIeer8rV9YYFH0Gcd9vQTUbrPPzkSUJK6uJTK1tW-UFLLUXtBg25h3NwVLBAXuU4ZRk0PNhNP8TGPhPX-nd_TCDTRUxJxwGJ2WGscE3EvGN4ljyS4Ld4yNldpKENQeuHtUtYP7rAOwDV8IuhxWHhtUtatFjK1odOoLn6QP_TPLqjN0Dzn2KK6jv9VNh7qWVdN-lTVcfoqQGCUDhr82lLV_luX_UQsELfUgeBFSUjpDrwdOzJ1_6nNyyJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea96c0728.mp4?token=HSoK230r_-wyXeIXJwv2tRg7LBiUHmgG7-n9R7OePgSYGWa41gkErKM-C_Q8gl95af9JWGIfSN3mH499QBkw6vLENY6_cR-DVnfkKgupfkMlheRQ-0VrGVTacgs9__3r1i23V43C4ZGxdOth3V_QX53t1-McyescAvGyw61c5pSDm3Bmuch-a4gNtmwGK8Qhhap4QnZfuwTH5-wCZdemXLIsbUkH0U8Uz7Dn6l4AnSU-WF_frsAV0wg4y8Dh_QMxxe_Jgc1ZOVmvS9eZL5y0-06r5uUucS1NOLsaLZYT2UlIpBgRJUUx8GQPIXr3pNRhjiB-qt_jT7A98ESx86wxMYfQN0DXTF3_W5OUHADbcxcw41lVulQiPYRR5bKWnzy2B83ErzDRsgdTzIrLs_APi6dPb-OAZGIYQLCfAhWwhB1jODUaeBgIeer8rV9YYFH0Gcd9vQTUbrPPzkSUJK6uJTK1tW-UFLLUXtBg25h3NwVLBAXuU4ZRk0PNhNP8TGPhPX-nd_TCDTRUxJxwGJ2WGscE3EvGN4ljyS4Ld4yNldpKENQeuHtUtYP7rAOwDV8IuhxWHhtUtatFjK1odOoLn6QP_TPLqjN0Dzn2KK6jv9VNh7qWVdN-lTVcfoqQGCUDhr82lLV_luX_UQsELfUgeBFSUjpDrwdOzJ1_6nNyyJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88620" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88619">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX_QVA0w6zhxmZyczh9eYqnG706yXBkGSMC4xdX4w8gGC14LGpkEwZT28WDa5jw9IhBwaoel2gkXuXH2mt0wau9MIuuYslICzBnYxe1L4Szq7ORFn-_5SpKejeVS-iL-K1ywmiYxkfUxVKl0Ef3ByfOl7SqRkGmBdPG8K-zFOo8yX4zSbCPGaR4aP770r5NMy4DGhvyoVFPxYs1MmbZuIgDJBrS4YyJBFGcA7h3kdTNNaw1zdxhirm9uvAsAObax0S4Anf99clrxMvokjyd6p2hSQU1CCB-YeXodS0mJ5giWdQ2IunncA2RR03z2FxHz0UMqw1LUGpD5t-SjauwYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إشتباكات مسلحة عنيفة اثناء عملية ازالة التجاوزات في منطقة الدورة بالعاصمة العراقية بغداد؛ إستشهاد وإصابة عدد من عناصر الأمن.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88619" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88618">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇷🇺
الخارجية الروسية:
قد تتضمن ردود روسيا على الهجمات الأوكرانية باستخدام الأسلحة البريطانية استهداف المنشآت العسكرية البريطانية - سواء داخل أوكرانيا أو خارج حدودها.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88618" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تحديات عديدة تواجهنا. نحن نطور إجراءات القتال في جميع الجبهات، من إيران إلى لبنان وحتى غزة، ونحن في حالة تأهب عالية في مواجهة التهديدات المتعددة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88617" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88616">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=K7SERkoNdLth6oIQyv229Rv0GQDvHLIxIa8lVf3K5Mbx17cik-QgSSx9fs4aPuoKEXNZrOvycWvbqFbPLVca60R6-sPX1zs2L3ZWCgXwdW-4LhMm3c-51__BvWJIPCQ1XyNEW6aGuBQ77yghLgkcXnkrAM8Qefgg1F3924yNlyWdOLZdWlmzHrdCO9bX24cq0GOx9Gy28PONaiLRDgCZsdxLptsmxJmgf60mWPV1vg-E0bW2t0CnhZAnLeiC7EcR4JXlui4as5xoKbZ0jHAf-J-gHsMTb5veZpYh88_pfpN6HzFyu6NuWewg--S0Qdu3jJDtVAJqXRm0jkNgy3xa_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ea710ed1.mp4?token=K7SERkoNdLth6oIQyv229Rv0GQDvHLIxIa8lVf3K5Mbx17cik-QgSSx9fs4aPuoKEXNZrOvycWvbqFbPLVca60R6-sPX1zs2L3ZWCgXwdW-4LhMm3c-51__BvWJIPCQ1XyNEW6aGuBQ77yghLgkcXnkrAM8Qefgg1F3924yNlyWdOLZdWlmzHrdCO9bX24cq0GOx9Gy28PONaiLRDgCZsdxLptsmxJmgf60mWPV1vg-E0bW2t0CnhZAnLeiC7EcR4JXlui4as5xoKbZ0jHAf-J-gHsMTb5veZpYh88_pfpN6HzFyu6NuWewg--S0Qdu3jJDtVAJqXRm0jkNgy3xa_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجمات روسية مستمرة بالطائرات الإنتحارية وإنفجارات كبيرة تهز مناطق في العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88616" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
لا حقيقة لانسحاب قطعات الجيش من منطقة الدوز.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88615" target="_blank">📅 11:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر   هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88614" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88613">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
رئيس خلية الإعلام الأمني:
نرصد جميع من يقومون بخطاب الكراهية ونحاسبه وفق القانون.
الحكومة تتجه بخطوات ثابتة لتنظيم السلاح مع الفصائل بالحوار.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88613" target="_blank">📅 11:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88612">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88612" target="_blank">📅 11:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
إنقطاع الكهرباء عن منطقة الضجيج في الكويت لأسباب مجهولة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88611" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88608">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kY9uGJVTYA82B3003ncqvMDhfiAdBmWEpR05gHys2we7lWGII9MA_1-FLBj1KXNHuG6rJ0tgpeIt1KZ5HjMy2Pk2RWgVn6p7-gBfFJbWkPqJrNKIYxVJ419TgSz_AK3Y1dNazIIuYHkS-tRew8AjvuPY46nAGQ57IxEkATcHisIJVAUTHTe-N8lEWOouRPGwwVq0GrwhjpzJdBuuZVwgjGLzNMzN4gLpjz-65FMajxyxtTDnAyHhZ2CMAcmNSwcr_TWUALVA2-PhjDQrLmR_eYoPtOHxUOATfQKlsl1YgFnThGry9o6-5T8gkD20NTZEMGju_yOFpwfDUFe0CpSDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgePu87i05ZyGX47Ar4cLeOG08gdBIIZIWGaC3SFR7im-6DW_LDbqyKo4ebdRAkPRVJ03B-AOqpzAB06Jj5laQ8OyZxlADML0PY9ceesMPmzoP9m1Daax4sD30ul0CvYzmcpdcdET774Et7nteq7qS1XZGeVW7VuOZ7_iWz8PRvONUJxa2CvY56CoMCEJWlXZOjw7qqYQCLMrLdKxoXEKaWAaDhjOvVuCOlNqiKd1AUNvPXE-wuY0pq_lwLxTOHm_tavbXBioCYCBOvml9OI9PWGEM1o4dpsq8eGGoZ4CGqx4Gy_y66MZUXyKLHSIo9zdsrxwUg42ZLGzlXC7LvBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd4Jp1jHmgR6S4L7tXtAYAXVTTjxPk5oZa478yfPvjUDZ8M_6aYLNRhwvvaTuUjmzKnOaBMfLipfTdBij3BBHi6yhoYNXckNSlYyaW62SvAu9fFcibHsqb-PPuq1SoaPlTFsgWIrsK3uMn9eUUWuQoozlbPGyJLIEqr3J_Otw5awBEW1TN9OEhppnqEblNhE0PoLgoOWIXk35KtuTqVK3-xY7quyeyLPqUbArBGcl2_rtFiY_Vm-jZeR2hzwMDhEjGmIFN6VjfbNswPAvwlCgbZQCjdog4G-RNtvz2x4HeZoOjFLBYJS6E3NZZsL2e7A_4DlubG6FGSAaGhqhorhcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد تظهر تجمع السفن وتوقفها بالقرب من مضيق هرمز بإنتظار القرار الإيراني لعبورها.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88608" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇷🇺
🇩🇪
دير شبيغل الألمانية
:
‏يُعتبر حزب البديل من أجل ألمانيا، بقيادة المرشح أولريش سيغموند، حزباً موالياً لروسيا بشكل خاص. وفي حال وصوله إلى منصب رئيس الوزراء، قد يتمكن بوتين من الوصول إلى معلومات حساسة للغاية عن الدولة. وهناك بالفعل مؤشرات أولية على ذلك.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88607" target="_blank">📅 09:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇰🇵
‏
كوريا الديمقراطية:
العداء الأميركي المستمر تجاهنا بات واضحا.
سنرد بسرعة وحسم على الأفعال العدائية.
ندين خطوة الولايات المتحدة لتزويد كوريا الجنوبية بالأسلحة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88606" target="_blank">📅 08:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي بالطائرات المسيرة الإنقضاضية يستهدف مصانع أوكرانية في العاصمة كييف والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88605" target="_blank">📅 08:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله اكبر
هجوم على سفينة قبالة سواحل عمان منطقة خصب بطائرة مسيرة …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88604" target="_blank">📅 04:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🌟
لقطات جديدة من حرب رمضان تُظهر لحظة الإغارة على جسر B1 في كاراج الإيرانية من قبل الطيران الصهيوأميركي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88603" target="_blank">📅 02:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=jqnjJ2QLO7wpM2I3UDwIQYX73dhVuFTXEnFxjLHIUMRvuMQVqJualnedjjFNtgq1n23tblQ0Ib9v5HQfRbr5LbnvoqKYutIFfJmFfneSKzcdnitlwC3L439u6_xFGuXhchtpkxgECuaporvUMJYEMLKhQW3ftb-_RGF6_qQ1_ZEdjZdFa4J3n75vX51eGssJVe2dNG14oUS9q-gjNEGq4LdK0qidUTPAbotavXHMaUq8YzBhGmEAhn4QwWMJzjU7oqOKKE6imRIXrLFUCxPDRw4E2xlTWfJov_zjXM9jlqF8nfA9LJxhPuN7ulBByRhE6ZIrEnirTG9IKJDiegxD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f0f8deda.mp4?token=jqnjJ2QLO7wpM2I3UDwIQYX73dhVuFTXEnFxjLHIUMRvuMQVqJualnedjjFNtgq1n23tblQ0Ib9v5HQfRbr5LbnvoqKYutIFfJmFfneSKzcdnitlwC3L439u6_xFGuXhchtpkxgECuaporvUMJYEMLKhQW3ftb-_RGF6_qQ1_ZEdjZdFa4J3n75vX51eGssJVe2dNG14oUS9q-gjNEGq4LdK0qidUTPAbotavXHMaUq8YzBhGmEAhn4QwWMJzjU7oqOKKE6imRIXrLFUCxPDRw4E2xlTWfJov_zjXM9jlqF8nfA9LJxhPuN7ulBByRhE6ZIrEnirTG9IKJDiegxD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
توثيق أخر يظهر لحظة إسقاط الطائرة المعادية في سماء محافظة إب اليمنية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88602" target="_blank">📅 00:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=tJAMEkqy3fOE__3Jf8y_TMFatdQWmq_SiQRJWAzYGkNmr646Yoyl0OB_noy-j7GJC-97OK2YqTTLq4gPNxj4fs11IqxYZuSltFD0Z50u2KlW2ysmp5q6vz5LwK0oZqhtaPlL6k4jJSvOBwWHPsBzr8z42DA1P6Qp5xFCy-ySIRvD8pj7TW7Wjo4mbbZCRwrqUyNEJAuGh58dH_hzIGnn-_Fm-6Ap3qOpUWm8wA0VtMMWVo4_Du6Xko6PnTTzhodSJo-l87CXfDZ3p7TVRFRsKO5f-QjvJArMRjUUpSyCvpbuTcKBmtZfux6RDCPPArrL4rbZSJuI9vPvjtRxCE04TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e7b3f02f.mp4?token=tJAMEkqy3fOE__3Jf8y_TMFatdQWmq_SiQRJWAzYGkNmr646Yoyl0OB_noy-j7GJC-97OK2YqTTLq4gPNxj4fs11IqxYZuSltFD0Z50u2KlW2ysmp5q6vz5LwK0oZqhtaPlL6k4jJSvOBwWHPsBzr8z42DA1P6Qp5xFCy-ySIRvD8pj7TW7Wjo4mbbZCRwrqUyNEJAuGh58dH_hzIGnn-_Fm-6Ap3qOpUWm8wA0VtMMWVo4_Du6Xko6PnTTzhodSJo-l87CXfDZ3p7TVRFRsKO5f-QjvJArMRjUUpSyCvpbuTcKBmtZfux6RDCPPArrL4rbZSJuI9vPvjtRxCE04TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من إسقاط طائرة تجسسية معادية في أجواء مدينة إب اليمنية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88600" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
طيران حربي كثيف يحلق فوق محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88599" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=ozTx3Ob2w0cgf3Ec_22lWp3l012cPIrWr27arNaODShlrUafLP5RH8Xx5wSisf8XZWkd15BjgL-A1ii6IllnBEcfAKVi-O9IjrpRp5MtOeCbU4jDQkvJQi6_vpshvlOuE8ZlBcSy0uf5iyAvrwDSHgCuXtHWjUNaYnLzY-0apL0UVCN1ouzPRZKAHlxsXFXk7XZXg3XhsQkiUuawPRsn9a7nKf5PM8KREbvOArRw_tYZLbSuFsHC1qvkNV4LnnHp4iSu4jq1ev0uqf48vN5QVJsGwT6_Vf5XX9NErIMSNWUQU96B0qQR6btCnm9tUSN1uCUHJZ9gidUNqpTK3ddiRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6627f1fd9.mp4?token=ozTx3Ob2w0cgf3Ec_22lWp3l012cPIrWr27arNaODShlrUafLP5RH8Xx5wSisf8XZWkd15BjgL-A1ii6IllnBEcfAKVi-O9IjrpRp5MtOeCbU4jDQkvJQi6_vpshvlOuE8ZlBcSy0uf5iyAvrwDSHgCuXtHWjUNaYnLzY-0apL0UVCN1ouzPRZKAHlxsXFXk7XZXg3XhsQkiUuawPRsn9a7nKf5PM8KREbvOArRw_tYZLbSuFsHC1qvkNV4LnnHp4iSu4jq1ev0uqf48vN5QVJsGwT6_Vf5XX9NErIMSNWUQU96B0qQR6btCnm9tUSN1uCUHJZ9gidUNqpTK3ddiRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88597" target="_blank">📅 00:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88596">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=TB0mzNG9Gh4qJqeN2roXCTtqshvUU8X10gY32F_MvaJr1100jNiVKV8U-xcVLIp-Nd9jpo1US890yseSU86FR_phn0N6w5xw5BeihLZUIsHm0Iw09OeTbkPamEO4qSm9XnYQTXgNWRTUf_UXJ2o_YLIB6KGtY5Gbuw06GuIVJEyq-Uulb7lV8-FKsH2cPV1uHvmamQbbJXXv9owYQrDxqY_uBejH_PtP2JFI99eOm3gomX2x18X4rr4FT4-ilzZLemueBsy2dVaomskE541wdjjq4EjHApq72bjzCCdLhUPkxpLALhttV9Jv6ezmYJmkQvbZbZJRutUTlaOqD9XWyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed70602e4e.mp4?token=TB0mzNG9Gh4qJqeN2roXCTtqshvUU8X10gY32F_MvaJr1100jNiVKV8U-xcVLIp-Nd9jpo1US890yseSU86FR_phn0N6w5xw5BeihLZUIsHm0Iw09OeTbkPamEO4qSm9XnYQTXgNWRTUf_UXJ2o_YLIB6KGtY5Gbuw06GuIVJEyq-Uulb7lV8-FKsH2cPV1uHvmamQbbJXXv9owYQrDxqY_uBejH_PtP2JFI99eOm3gomX2x18X4rr4FT4-ilzZLemueBsy2dVaomskE541wdjjq4EjHApq72bjzCCdLhUPkxpLALhttV9Jv6ezmYJmkQvbZbZJRutUTlaOqD9XWyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به مقرهای تروریست های تجزیه طلب در اربیل عراق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88596" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88595">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=FPwmZ2BzZzF-GMZEFmqzyAL-RrfCHtZsc_WjXdaxF9YcdKer7BV-iJHHzeddurjXNpVTs8KKaszFqYz-tITr2viFCakkMjYKq0wU_7xWdgsbuU91zSwQ45Vt9YMU9Ttva0U14lWdEXl9Mo1HwxRzjUYsTXBtPSQ6P52SapKv9eim7wTau8ls6sLDPIPa8FS2ldDdMM04TT86S-2qAkd8ueg5Ulp0DSZLTrzCX7yxauLkZJmo9xQli6j6gy90AXdLThEVpaqBPCGDBuqAmDXyV1zoa0QKhbod13Yfe0rs80hlPKViekDjQTpyuNjBWfhOR4PbysOZE7XLDhcV74olhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d599cf5e06.mp4?token=FPwmZ2BzZzF-GMZEFmqzyAL-RrfCHtZsc_WjXdaxF9YcdKer7BV-iJHHzeddurjXNpVTs8KKaszFqYz-tITr2viFCakkMjYKq0wU_7xWdgsbuU91zSwQ45Vt9YMU9Ttva0U14lWdEXl9Mo1HwxRzjUYsTXBtPSQ6P52SapKv9eim7wTau8ls6sLDPIPa8FS2ldDdMM04TT86S-2qAkd8ueg5Ulp0DSZLTrzCX7yxauLkZJmo9xQli6j6gy90AXdLThEVpaqBPCGDBuqAmDXyV1zoa0QKhbod13Yfe0rs80hlPKViekDjQTpyuNjBWfhOR4PbysOZE7XLDhcV74olhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقرات الكوملة واليجاك في قضاء سوران بمحافظة أربيل تتعرض لهجوم بالطيران المسير الإنتحاري والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88595" target="_blank">📅 00:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88594">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f044086b32.mp4?token=XDxxCzmWv0AOMBHOvW7RkKL5hZ2rUscTvELjVPvh3lJjQafkds3CpA9uWXaO9c5fRR1QOzgrPSCh_UyPRSwGP03CohAdQS1bnRtFIxL-p9K3E5iBtIH7wVqWD9DNZEi7y3HmtGT_HKKhJOyzmOhKH1p2xdc58PQMi0YPq78OO2Hke_vESwswUZSD9GHj47bghXOQ_9LbbhUSffyJ1qPnLk1ON5YVmGzAviGxz6NB-2IJ9u-fLCrZJcpanLN0FMlJCE9hxxsnxGXWGYpZ3zM0h1tgdCC_-V-7LKT4qUJIwFqJGsh8Vc3v_BnolPTDJUQHJ8px7JLxPEplLfLXz0Vkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f044086b32.mp4?token=XDxxCzmWv0AOMBHOvW7RkKL5hZ2rUscTvELjVPvh3lJjQafkds3CpA9uWXaO9c5fRR1QOzgrPSCh_UyPRSwGP03CohAdQS1bnRtFIxL-p9K3E5iBtIH7wVqWD9DNZEi7y3HmtGT_HKKhJOyzmOhKH1p2xdc58PQMi0YPq78OO2Hke_vESwswUZSD9GHj47bghXOQ_9LbbhUSffyJ1qPnLk1ON5YVmGzAviGxz6NB-2IJ9u-fLCrZJcpanLN0FMlJCE9hxxsnxGXWGYpZ3zM0h1tgdCC_-V-7LKT4qUJIwFqJGsh8Vc3v_BnolPTDJUQHJ8px7JLxPEplLfLXz0Vkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم بالطيران المسير الإنتحاري يطال مقرات المعارضة الكردية في أربيل</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/88594" target="_blank">📅 00:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88593">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqfIuRQ1VPtoXYXYU_Ee9gAd-TBFORQXP2XHBCBxbUqmbBSyDNIMtaUnlj6bRI804RqEFf3zj83XNcPxzKBR_E7H99PopbhGoq2BOWA-Ds7LMvL-ys9h9SIyYtup6GTKGZUt6Sw_fRLe-l9lWukdtFZ_xoQyR6lGslD1Tb6kCtIxZuwekIOxNadnTWjcwzkwuJo5WNjnk-99h4kKj_FFLkuo16lvM1Ud_jxKOen5RszYoQQxbqH89kJd0dMXnyw0Fy0D4bsEGFfsVvUXMSL1f8um17rvNPnhvGBoLG-gzggKWSUlknoMlkxGyxw6BI9mX4jpbJd3156QXRrJAawBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد النيران واعمدة الدخان من مقرات الإنفصاليين في محافظة أربيل جراء استهدافهم بالطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88593" target="_blank">📅 00:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88592">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=GDEOgqHDvf0Kz4c-l6lrmo3w5TcHBejyjkanlUcX0TmHvyWzg1ObvNsbODL5hEF5z2g3n5_9KvNJKkvdQBxkXa4FQvfzjnqhcvAytfiW1sgR0c0e-oLZ7s7yl9wLNucVD3oZG4MIwzgsI8CZerY6DPkSsrvfGUhTrxLgjAEgVYZwGrAOUm9aFO7iYnhIIlqjsCwJmqpToBjfUgVrZdg3OTRG5eB_wvVwoO5uYHCG56jPUDk_iQhDjIPiB_umckfKWap2CZ_2CnBHEN0HgSgpKWdM3gXKhk-k-PYVc_dBwC2D0sF4CfTsDGaxWqODeBuf8D3Fb902_hLTgXZPEQTWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eff45189c.mp4?token=GDEOgqHDvf0Kz4c-l6lrmo3w5TcHBejyjkanlUcX0TmHvyWzg1ObvNsbODL5hEF5z2g3n5_9KvNJKkvdQBxkXa4FQvfzjnqhcvAytfiW1sgR0c0e-oLZ7s7yl9wLNucVD3oZG4MIwzgsI8CZerY6DPkSsrvfGUhTrxLgjAEgVYZwGrAOUm9aFO7iYnhIIlqjsCwJmqpToBjfUgVrZdg3OTRG5eB_wvVwoO5uYHCG56jPUDk_iQhDjIPiB_umckfKWap2CZ_2CnBHEN0HgSgpKWdM3gXKhk-k-PYVc_dBwC2D0sF4CfTsDGaxWqODeBuf8D3Fb902_hLTgXZPEQTWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/88592" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNirYUrU7MqpUSAY4zZ6yNkfk7Q9TCPOadBb3sWtO_pEPepJxyv-VpZT8VIBxX1g8K33397jIfCPRDgWa5bLJOrXG58Rn4NErNO2klzLINHwfsevArxOhp4s-tJ_hThCfyUAn0IGrbCJPsgAULO3bes_iFYeKUrWykjpoSuX_BH9wM-klrQFE3Mg_03C-yh-MHTghs95LjQj9oS-8bA9QKKaURJ8-AKcfmce2qNs0xvFiV_Rgl7j0vXcyK1NPZWktyv5QHgm22s-nBuEqZmA5fQz85qBcR1I5cX_j5xLi472Msq6x2kNXIPom6qUZ7u9M_KZ4L1Dlb0faYHMeDPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
دوي إنفجار عنيف في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/88591" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
الاستهدافات طالت ميناء المخا وبعض المواقع التي تتخذها المليشيات الموالية للسعودية ملاذا لهم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88590" target="_blank">📅 23:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88588">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=bz3vZvjjL4luf4QsodlUt9XX-SjuJJGD_aEwcTIZJnRvjGofKje0aE7638sty2VMbT_BBrWq_Sk3_RavgVz1RtmoABvxmS_-gUufv_M6lseqyPHErOdqRt50N0PpDhSzCfaasbWyPR9XCB-t3ilqqY_b6OiWMeMHw_ALxG3gZ_wtDKKZohXFuigcbMJIE_rZuxF8iBSr9Z_OknTttXs5K5h5FwRSC0DxsZbn4ktu79G7azDjudadhMLMFKaV8HO4OW56g9O_UBZHcGxRGl6-qHYL11Ps1iM-vjbRGA5mWvE6X3Zk6kstsV4T3cWdJy2hKdVv0eDo2Y-AwwvQW8zLpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc95e1665a.mp4?token=bz3vZvjjL4luf4QsodlUt9XX-SjuJJGD_aEwcTIZJnRvjGofKje0aE7638sty2VMbT_BBrWq_Sk3_RavgVz1RtmoABvxmS_-gUufv_M6lseqyPHErOdqRt50N0PpDhSzCfaasbWyPR9XCB-t3ilqqY_b6OiWMeMHw_ALxG3gZ_wtDKKZohXFuigcbMJIE_rZuxF8iBSr9Z_OknTttXs5K5h5FwRSC0DxsZbn4ktu79G7azDjudadhMLMFKaV8HO4OW56g9O_UBZHcGxRGl6-qHYL11Ps1iM-vjbRGA5mWvE6X3Zk6kstsV4T3cWdJy2hKdVv0eDo2Y-AwwvQW8zLpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88588" target="_blank">📅 23:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88587">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇾🇪
صواريخ انصار الله تستهدف المليشيات الموالية للسعودية في المخا.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88587" target="_blank">📅 23:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88586">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
الاستخارة تقترح بابتعاد العامري و تجلب حظوظ للفريجي العائد بقوة والمبعد قصرًا من اخوة يوسف ، اخوة يوسف يلوحون بالاستقالة بعد عودة الفريجي من سرير الموت..الأخير أسم عابر لحزبه وصاحب علاقات إقليمية ومحلية تجعل اسمه ناقوس خطر على الجميع .. من جهة اخرى أربعة وكالات استخباراتية استلموا منصبهم في فترة الشمري سيتم تغيرهم ..</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88586" target="_blank">📅 23:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88585">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7f179854.mp4?token=kaLqQnofJ-2VMJd-shTceAtOR0aNLrefHsikdFCkUhdUM2c7ThsxL4F5l576TUwgFUNJdCiGIcgKBen_L6ciZEF7r-AbYxGCh5erhod2OJvTDCupUA5FxKOR96XqJ4bT0x3o58SoIMdJuyVSq0d8VWyX9D4duNEBsUE2kpST30nOiiWjWDzLXLeStYdWlbAqXitsm-8OrKtvvR_75xMIR_DIzpGpC14-Zm7xk81nCqsk1FFoOsqUn6xEKQCsMFuDWv9tg4QhLXZxgPf6BdP8vYmy7vPWgcR5AnIJpjNAF_05etTL5-RNY5EyOa1x3Hzcsz9_u4yrIzt1tf2yyurKgkOBQJrIEkKIcI1c4bJ0C6Y-46RTSHy4i6g6tuD76HyvArdXb4Md4kkFIlleQ5u8twYM9BMYXMMuNcH6bYcV6Kh4AfW02GukCImxkTFXcMAwSdwoeeYxGp294R-0M-jq8A_NHrg-HNGnAAPeXE4XMnERPOuJCyOdNVKjhPMgFFuPz8BEtqfJ1oANNxltEkqtpCb1RyIjwUAIdeqV_cp7HHWMKqspxHca4dSukVPfXI376u5GNipz870g0Xmt0bEyeh4sKbPTEdQGk7llWS2mAkJsMmmJocZP-1lWCpgh0WpuEkH7c2tBCeGEiZexBk-l37-5KQo1Sd8JZMc3Glsl1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7f179854.mp4?token=kaLqQnofJ-2VMJd-shTceAtOR0aNLrefHsikdFCkUhdUM2c7ThsxL4F5l576TUwgFUNJdCiGIcgKBen_L6ciZEF7r-AbYxGCh5erhod2OJvTDCupUA5FxKOR96XqJ4bT0x3o58SoIMdJuyVSq0d8VWyX9D4duNEBsUE2kpST30nOiiWjWDzLXLeStYdWlbAqXitsm-8OrKtvvR_75xMIR_DIzpGpC14-Zm7xk81nCqsk1FFoOsqUn6xEKQCsMFuDWv9tg4QhLXZxgPf6BdP8vYmy7vPWgcR5AnIJpjNAF_05etTL5-RNY5EyOa1x3Hzcsz9_u4yrIzt1tf2yyurKgkOBQJrIEkKIcI1c4bJ0C6Y-46RTSHy4i6g6tuD76HyvArdXb4Md4kkFIlleQ5u8twYM9BMYXMMuNcH6bYcV6Kh4AfW02GukCImxkTFXcMAwSdwoeeYxGp294R-0M-jq8A_NHrg-HNGnAAPeXE4XMnERPOuJCyOdNVKjhPMgFFuPz8BEtqfJ1oANNxltEkqtpCb1RyIjwUAIdeqV_cp7HHWMKqspxHca4dSukVPfXI376u5GNipz870g0Xmt0bEyeh4sKbPTEdQGk7llWS2mAkJsMmmJocZP-1lWCpgh0WpuEkH7c2tBCeGEiZexBk-l37-5KQo1Sd8JZMc3Glsl1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
" السالفة المحد يكدرلها الكتائب تسويها"
قليلة التداول جانب من اشتباكات ابناء العراق الغيارى من مسافة صفر في احد قواطع المسوولية للدفاع عن الوطن والأرض ..</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88585" target="_blank">📅 22:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88584">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8OjIS43HakJ1pt_XMMmJxVs2VO908zKJVparBEZpTmah4tdBRU5DCxf4np9jwXMLmWFbbBqlNxQDl2ZITt1EAdcMEeSq_DzRzD_6hvyLqtRL0nkcQm1NGH_-QNuzZ8bq1Gy8dT7Fy3UOANgq_wgTN6O5qTA-ko-KrFjJccgA-BLwTnwl5UXRLPcGCXCBcGdhfeG-UT3oeIuRswMzTz12-gh7GojfNPnc9MMbt8lqJfLqDA66g2kOsqztKqy3cFyCfOmnIy7VBpT9IPSAXBjB7WoXOmzoB8KVkZuo20EBX4qF6nAEJCO5dE2_xAaPSPpq5nRWBCRSGeX3Tj6ofyvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية بقائي:
أرسلت أمريكا حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" إلى المنطقة لبسط نفوذها.
بعد شهور من الحرب - وأكثر من 200 يوم دون توقف في أي ميناء - تتجه الآن إلى تايلاند لراحة واستجمام الطاقم.
المهمة: مشروع القوة.
المهمة الحالية: مشروع العطلة.
"أنا متعب يا رئيس."</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88584" target="_blank">📅 22:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88583">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
اليوم، نُحيي ذكرى الأبطال الأمريكيين الثلاثة عشر الشجعان الذين قُتلوا بشكل مأساوي قبل خمس سنوات على يد إرهابيين جهاديين أشرار في كابول، أفغانستان. كانت هذه الكارثة نتيجة انسحاب جو بايدن الفاشل تمامًا من البلاد، والذي ترك جنودنا البواسل عُزّلًا، وسمح لحركة طالبان بإطلاق سراح آلاف الإرهابيين والمجرمين المتعطشين للدماء المحتجزين في سجن باغرام. كانت هذه واحدة من أبشع الفظائع في تاريخ أمتنا، ولن ننسى أبدًا أنها كانت نتيجة عدم كفاءة جو بايدن والديمقراطيين الذين كانوا في السلطة."
‏خلال حملتي الانتخابية لعام ٢٠٢٤، التقيتُ بعائلات ضحايا حادثة بوابة آبي، وهم أناس رائعون ووطنيون عظام، تجاهلهم الحزب الديمقراطي تمامًا ولم يحترمهم. وعدتهم بتحقيق العدالة عند عودتي إلى البيت الأبيض، وقد فعلنا! ألقينا القبض سريعًا على العقل المدبر الشرير المسؤول عن مقتل جنودنا، وكان ذلك من أعظم شرف لي كقائد أعلى للقوات المسلحة. بارك الله أمريكا، وبارك الله عائلات ضحايا حادثة بوابة آبي. لن ننساكم أبدًا! الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88583" target="_blank">📅 22:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88582">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رويترز
: يبدو أن إيران وعمان تتجهان نحو ممر ملاحي مؤقت بعد ما يقرب من ستة أشهر من الحصار. وفي الوقت نفسه، تظهر واشنطن علاماتها المؤقتة على وقف التصعيد، وتعيد الموظفين الدبلوماسيين بهدوء إلى السفارات في جميع أنحاء الشرق الأوسط.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88582" target="_blank">📅 22:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88581">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COpLS9KOpq66tpxfZC6F0SX5ua6cwjTcor0CRAIILweKA8dz0LyDJmhEww6uVfgAIl1m6C2NrSfx_G_r9ixuagSsFWkIsv_OqTCE5XLblbMESB9xN1VkYiFIsbfSnv0LoYUE5yF2oYaFkNai6RkVIcjYsGuW5f44ToZUT-D0x5bcYoe7F2bXTVgg1_wER0XOErdudoTj-XSW4ICFYtXeO2xeKo_sm4KcL1q2-RDa9JuRfU3CoCf3iADsJs0FQzYI6xBa1n03ysk48-yo35mGcN6_9_NFlxb1SOqIxNOngNs5c5xmxg_KtUOkcZvpgbtQjgtrjkOhHf_RTfKG2UkVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: نرحب بالبيان المبدئي للصين الذي يرفض العقوبات غير القانونية المفروضة على إيران.
تقوم الشراكة الاستراتيجية الشاملة بين إيران والصين على الاحترام المتبادل، والتعاون المثمر للطرفين، والرؤية المشتركة لعالم متعدد الأقطاب. هذه العلاقة لا تحتاج إلى موافقة أحد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88581" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88580">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه بتشكيل لجنة لتحديد شكل العلاقة مع التحالف الدولي بعد انسحابه، عملية انسحاب قوات التحالف تسير بوتيرة متسارعة وفقاً للجداول الزمنية المرسومة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88580" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88579">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3nZhyLDWrTekI0uz76k0M31ftVMvwpi2uQYRGYcWJogk3AtO7Sdo7l4XoL3RNr3VPp6InMihLjRP8Ozo-l_NmUErLjhZc5hgecrpLOJZsSt57AP9OOjtG2lvg9cjIJs1UKUOAUcGzgS8JPFExqW35CxGSxGV_s4vZSEUPV-6oLDmYxpjquLRRyZm72BVL6ApnDz8_eoQAtz3f0cou-h8C9-fjs4PNHaz4NdFWTuwVZ9QCN94GCNf9-0PfsHgCFfYZlKQG1qFCWis9sN8o8xrbEeE5Q05hLAfllSP-wTBrMmwyPRZmImVoAsjvThzaJA8DWWEhL22IfOXfMrI654hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء يلغي الأمر الولائي الخاص بشركة كورك ويُبقي قرار هيأة الإعلام والاتصالات بإيقاف العمل مع الشركة قائماً.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88579" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88578">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
‏
وزير الطاقة الأميركي:
رغبتنا قوية في إنهاء البرنامج النووي الإيراني عبر المفاوضات.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88578" target="_blank">📅 20:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88577">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIyYgTYlG6YXbsbM-8dy0ObOLM9QXrvW6j_amnYI0IjqYuEi6VRRaUy3zOVOBA5e8uB6L0Q8IdnBM04hfU2CFyOZpR2OcDjtPA0zi6jg9cGKGSlDB1My47hrfOTctTn3rfWfk59HC0AY6C-HX4rAK2pbCp0s0ENwi3PandV6Kyic-CvgZ5oiFhCziBrVcNyf_pTFndl-Oxp4_WFUNOFNd_xRVnINoAtuQurcFYPIIrj0es-HxNCTYiC__ClnJLksQVAY1iqMJeN8Nn2b3Jo5V0vnOj4zwo86wW27WxzCY4sqtt6-PwtxTLfoyhs_Fm_sxQ1LUhNRWSWgNFDEf6dZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: اكتملت المهمة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88577" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88576">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
🏴‍☠️
إعلام أمريكي : ‏بوتين يسعى لتصعيد الحرب في أوكرانيا بعد وصول المحادثات إلى طريق مسدود .</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88576" target="_blank">📅 19:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88575">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVXp-wsMl-pJzLzvDuQbrfAPG7qOlvibaHmIXMC38ZSnOiUs-OW5TfmIOz1FDz-z9UyKlrKt5RKiO053ktJzDqSJVdF9ZsadBA0NxTXcPQavzSMD1phL4UN5c-kHTgAC8-zl4PDeo-ceuxwWHiVXHUBpw1TzWFhqhjxWTmXauSN1XiWh1BSouMrYJghn16IcMrj4ZYe0mcG0ADkbJo6xAPnyJK17LG6PKabaslDMcMKqxZLKgQJ_s7yw9usSZiCJBI9iMeuSazRym_pvkLgAN1Rjzh8Sl5s8K2yiyJAszxpaH8ewk6LpXJzqA2c0i802KnbtwTcctbF8ngIbbUzeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
سفينة نفطية هندية باسم "HAANA" كانت تنوي العبور عبر المسار الجنوبي لمضيق هرمز المعروف باسم "الممر العماني"، ولكنها تراجعت بعد تلقي تحذير من حرس الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88575" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88574">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
وكالة الطاقة الذرية الايرانية:
‏إيران لا تزال في حالة حرب، ولم يتم تأمين مواقعها النووية للتفتيش.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88574" target="_blank">📅 18:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88573">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edhGER4NSUIap7IekQt6HvZd46Eg0GbOErS21qEVP41soBZjSRE7UwZN9Zj9qT6fGxZW1dFbkQpB-Sw_EgZrhfsdHUOkUa2QcQ7Ras5A-BEJrF_XHH_PnW-G8Wco0NMKz1ZtAIwNbRXEYxg4yFf6BHXtM5jFGpRKDM0RZXTAfNq5yVXDxuJjq02l9wD_nHaAPddZX2bd86ompFFcz5TMSoJ5eGVmVBFZhqVvaZbtqB6XshWK5ZfUhu-DB7VQ2jK1cMGlyo0twTinKIJfSHI8Qjn6VMY18FFzTNymr9jHy9ReMfoMvXYyeGPEiWv5uNaCqHV_7gdztaCJ2AiclIhuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای سربازِ روح‌الله، ما در (نايا) همواره از تو شنیده‌ایم ومی‌آموزیم که علی علیه السلام فرمود:
به جانت سوگند، آدمی چیزی جز گوهرِ دینش نیست؛
پس مبادا دینداری خویش را به اتکای نَسَب و تبار واگذاری.
نگر که قرآن چگونه «سلمانِ پارسی» را تا اوجِ والاآرمانی بالا کشید،
و چگونه شرک و کفر، «ابولهبِ» والاتبار را به خاکِ مذلّت فروفکند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88573" target="_blank">📅 18:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88572">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adIWCA8NL0l0BAlHokviTziAiuvUcUY9JGnav4B_nfDT5CLVMbwlrk1ypOUiqSkwFY1t5vEuX8nmo6hsHyMAsqqmhOKPHTi_OIY0Ft7zfMMt-8xitc5zXRXzTYej3YPPoANh2DlrsKpYXamyuM_yzpHzeJejaKAhLDxFLudYdaj3qZEAM8uFvFmvD5xHfIjoudV6e1aB6HMwB02xVo4N2xN60D1exfv4RsVI6DmHLenN7FJEfeoTkBubmlF8Jn_s5Vayk_VaGRKTUU2iR4PhsNGd4LpM6qonkRNmI6SaVmNK326W2npL_5N-SBv2YVNt0Zo4bLz4r29PuzZnhpySOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش السلطة اللبنانية الذي ينزح مع النازحين في كل حرب يزعم: إيقاف سوري أثناء محاولته تهريب قذائف صاروخية إلى الأراضي اللبنانية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88572" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVIHi3_yWgmniRrCWOX627PPBlXMnsxNiHDdCPqRRcCLsKSKGrilMImZm6y-AaybuSsHdrSxqjOx6WmWzCC2KLVvAFmunYCgt8V9J5UPuIRFFMcXPpVAGrpTZuhn0SBkfz5ztfsmwBtCLdWHHKv7izBYAv4xz63e8fxdkikiNqYlkNjWoLLTumjsgMHG24ORQtFQ1iLGYmH4G5SwMzgI1NjJKAE7p67VTjIk7hsCmY1hZmoDdyvP0fwdGSIOtONd2uzrxx70yig3FZkkR6F1Few8TDSF7Jlx_AAsb_kqsNKHhWoogs4Yt2JwwtLUPZZdulX1rT45ac7mRvzsOyrKwMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e4021968.mp4?token=RvriLnJ_ZdJlAU-Mzwv51cQlSwfU7f0sp-nOTo2uiTMr4pWHxfGxBqgx7irHBwLyg-_IzRrcv8TpyGMI5dUlOF6OPeq9oc1WDzt5ir_4MY-X8O-J3w-8ifCZEuDcZejwzfWumhhJeWbKMf9jlsun3EBVx0AOJ1SlyqRqb87zKO5XnxV7Kgi30PjcmKz5g5G0_HiRduqQUx5LN6qqZpmdPP7z4pxLaL1Cc5F4ymNRt0vVXJbQHPTyZFaVHXqcM4DbLgEDvK5OW_5ALQLGNWVivRgTbIfhOMX65FAxzaVEhCb1JYzPxD-kUZCyHWYIgNDCL0NilsSSQzaENdhhUtHpVIHi3_yWgmniRrCWOX627PPBlXMnsxNiHDdCPqRRcCLsKSKGrilMImZm6y-AaybuSsHdrSxqjOx6WmWzCC2KLVvAFmunYCgt8V9J5UPuIRFFMcXPpVAGrpTZuhn0SBkfz5ztfsmwBtCLdWHHKv7izBYAv4xz63e8fxdkikiNqYlkNjWoLLTumjsgMHG24ORQtFQ1iLGYmH4G5SwMzgI1NjJKAE7p67VTjIk7hsCmY1hZmoDdyvP0fwdGSIOtONd2uzrxx70yig3FZkkR6F1Few8TDSF7Jlx_AAsb_kqsNKHhWoogs4Yt2JwwtLUPZZdulX1rT45ac7mRvzsOyrKwMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88571" target="_blank">📅 18:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88570">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88570" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88569">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حدث امني في صحراء الانبار</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88569" target="_blank">📅 18:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88568">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة: عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88568" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88567">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
🇨🇳
الولايات المتحدة:
عرقلنا قراصنة صينيين اخترقوا وكالة ناسا والاحتياطي الفيدرالي والمعاهد الوطنية للصحة ومجلس الشيوخ.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88567" target="_blank">📅 17:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88566">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏امريكا تفرض عقوبات على موقع مجموعة العمل الفلسطينية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88566" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88565">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88565" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88564">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامب: ليس لدى كندا أي شيء نحتاجه وحان وقت الاستغناء عنها لتعليم كندا أنكم لا تستطيعون فعل هذا بعد الآن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88564" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88563">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74978db9a.mp4?token=D5AfvwZgOnUDujh49g8_0UPlB9dhi1MIg1H8ufivyFkNAZIpMmffC0Wxu2uXurmDwzr61Winh0QhEPpAy4fbmaip6L9k-ruvvDNBeAOYJR5moGeClcfYX1EPx_lCX-xutsBRNdqKPxN_jDfLZB6S4Bp2NqwNVh5EI_Wxoh4HlYknw2d42hce48NlNJz0_bp6JAIBoaRgLnbhZW6bVofbWD0K9yEqpaE82N5QLfeFOzBF9eFd0Frk2xBZECE5ineycbIksHfe2z-2wLrEvZ9Tdpk2fJb7ulxcNXeEGmsz0efshGebvr7iylBGzU8pggOxoFCTmIUhpxJ6TEHcf8Csp4mREUQH426Xegcyr2PxcNyIiOU3NwDieb5-b1xpFM_Z8KSuLF6t6iTr2qIztR8h5DNkyE_MT6Ndd9zazPgo25RoH00cJ4t4z1GMexaTzW8OdorN_gyFuyqz2ZvjrxKkzBpgGpL_pw5LdiR7E_ssI28WV3mLN0pBoR54vAzmQzW1hwiZe40v2ZZamnhq9WYeTxT1gNvmIc8k34K5BC-nfXFhyFlH4gWAfl4Ba6VPsu9EB8EDynqZ82gi51RgYymznu5CBFrkX0dzVEwN1TNpZwYZoeINADnJMWvofifxa0vli3x2qrUalJZ7yXm24oo7rwAIjZAk5cnIBF-Y_hgCR7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏سأمنع منعاً باتاً تطبيق الشريعة الإسلامية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88563" target="_blank">📅 16:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd317e66d.mp4?token=OqhAW24-apmyTSKDfM_ky00fCXs6u_bJlxDPgEorRFq_EQUXKM740XZcb1rz-Fpo6wcnkovx7h77VZUbNN7jeqI7uQ58wxL5ehubFdNir_YFuyUj_NvRA6yD2eQWQ2JqTap9_uxJ50QKNBS4w5DBZblx9X3NJqayKd8ymaJ2cFEEWyfttuwQS0XsnWlXH_eaj6yri3dMOeUe3sI9hxed_yLN7YjWTy2RXJ_HxaBR9LQO-CT5E1--NngXaUmzJqUeDNN1ZSqWNmtJfajdaceAr9pAP4-tGa2H-fZngReYbX-U8iXYvOkURX5M5D8__KV2pEhnXAN-BiFvqV_9EorGqTdNi6SyCUa9WkM7XjHccB5gOLH2y1yZazUqqh_aDR1xEmVpGHiS5_0e4I-IukZ5bzvV_xa-Try_3AzeHc7N0VXGMWan_AvyCwcKNHN_sMRFztwvHMIooxObphJdXrE5qj3Os-R2hzFYNbAk_ZcBWOxR0UbfVx8Ge9T4EzZ9_yzJotYeYfZgL8j0bC7mw1BTJ2UjzqmFWFoQOnw0f3yJIkNJptJ73mZ0-hSAMsfZSibcp5HKX73k4-udW9uvyFheKDlMcqNdyBkSbNh00tlnGbVUL0G9Chb5or5agw-nt12i6godXccVrPC_4D19yVsmlqXV-mQuY6sjA9lftqeQXvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الايرانيين غير محترمين</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88562" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88561">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=M2tNr_K5Hvl1cS5sDu0RdvpC7T3xJ5hQV2XZJXB1rAJ8o0yUrYhWsCuyJEdQegxCkfEsMUtKhgJLbL1jDGhsRmGc-ZL7xj72jpwrHT5n3XIK30YWXtyYXH-5NlorNGNfhdoT8rXpUJjIRkG3zpfmAcZJMlWG_cqFZBw_GRcFZ4JyH7jZx8_91oyeXbblbdy-N5k-kz0ERgbbxKeQcfyd7m_d0tYisr9ep5_fT6mQr6ycNmjjElFK6AjM1plNRhl2ShJ_ObjbJNpnRw_gL3mET2jvg08KE3z-ObMK8vrbkkQcC_3vfTM1nfqggDzR0h45hfniB2EfIaFMm7bagd4m0TexU1rO5cu0Y2qwi9qX4kj2uL8t_IWRNuZWRP33uLXcWZFys0Ny5rtw31nnNnaWWo-4wz7sGUGZcMk41q489KKR6560K4iAiSMMONQJxIMqoQn5jULsVOAZ47S1e_3RXwnfj_DNG_2HH8Sl5ZyohOLS4rRmEEmOW1WgHGeYUH978KotVcH9-62W3oHvLkDdSVYF_VtS0kn0zVl1bPT6rCkBQMcZJCpHgC8oVmM4-ryPu4d_ks-Z_nPeT74uLzxSGd9BBXHKr2W2bSa_DF6svCp5wUS7s7EHE9GRy2rT1kXU25TDFyPrwnmhVcY1-ZBBBxJY1dwNN98yMHhqLcLKhls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17c3fa946.mp4?token=M2tNr_K5Hvl1cS5sDu0RdvpC7T3xJ5hQV2XZJXB1rAJ8o0yUrYhWsCuyJEdQegxCkfEsMUtKhgJLbL1jDGhsRmGc-ZL7xj72jpwrHT5n3XIK30YWXtyYXH-5NlorNGNfhdoT8rXpUJjIRkG3zpfmAcZJMlWG_cqFZBw_GRcFZ4JyH7jZx8_91oyeXbblbdy-N5k-kz0ERgbbxKeQcfyd7m_d0tYisr9ep5_fT6mQr6ycNmjjElFK6AjM1plNRhl2ShJ_ObjbJNpnRw_gL3mET2jvg08KE3z-ObMK8vrbkkQcC_3vfTM1nfqggDzR0h45hfniB2EfIaFMm7bagd4m0TexU1rO5cu0Y2qwi9qX4kj2uL8t_IWRNuZWRP33uLXcWZFys0Ny5rtw31nnNnaWWo-4wz7sGUGZcMk41q489KKR6560K4iAiSMMONQJxIMqoQn5jULsVOAZ47S1e_3RXwnfj_DNG_2HH8Sl5ZyohOLS4rRmEEmOW1WgHGeYUH978KotVcH9-62W3oHvLkDdSVYF_VtS0kn0zVl1bPT6rCkBQMcZJCpHgC8oVmM4-ryPu4d_ks-Z_nPeT74uLzxSGd9BBXHKr2W2bSa_DF6svCp5wUS7s7EHE9GRy2rT1kXU25TDFyPrwnmhVcY1-ZBBBxJY1dwNN98yMHhqLcLKhls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🌟
ترامب:  لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88561" target="_blank">📅 16:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=mpnUTQW7xCVwMUtxGXPQtgVzwCdzPwxrWQCIT5h2blouIgGju8RTQ4qmBIR1Wub0ymSpEVt_yftlpvoxcXQcBdSZ3P5eFJlfMIHyqQ8nmoKJnHwJMCDhtIJj2yHr5LjTtaJgvdRoFSVoocRFz7PFV3YQ-atuBFfoNuOgdwLU7Kd362QFVgFasUP1y4AKFe6PM71KmxpbdBLHHGt_kyUCGgMHHuLVJBlp3KZgVBvNDzvyQr6iVG93SSjHXih2Jv8jhWlIX7EZanUCW5dfd-9rp_DyXWCY8qUEehuhVvV-GuQsbTWSij0dEoGJLszAOPxK3z9JOZO0pC-EjgoGiimHJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3bd09b95.mp4?token=mpnUTQW7xCVwMUtxGXPQtgVzwCdzPwxrWQCIT5h2blouIgGju8RTQ4qmBIR1Wub0ymSpEVt_yftlpvoxcXQcBdSZ3P5eFJlfMIHyqQ8nmoKJnHwJMCDhtIJj2yHr5LjTtaJgvdRoFSVoocRFz7PFV3YQ-atuBFfoNuOgdwLU7Kd362QFVgFasUP1y4AKFe6PM71KmxpbdBLHHGt_kyUCGgMHHuLVJBlp3KZgVBvNDzvyQr6iVG93SSjHXih2Jv8jhWlIX7EZanUCW5dfd-9rp_DyXWCY8qUEehuhVvV-GuQsbTWSij0dEoGJLszAOPxK3z9JOZO0pC-EjgoGiimHJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز تعز بعد هجوم لانصار الله على مرتزقة السعودية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88560" target="_blank">📅 16:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88559">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
لا أعتقد أن السيد مجتبى قد مات. لقد أصيب بجروح خطيرة للغاية، في الجانب الأيسر من جسده، في الذراع، والساق، وقد أصيبت كل هذه المناطق بجروح خطيرة. ولكنني لا أعتقد أنه مات. إذا كان قد مات، فهم يقدمون عرضًا جيدًا جدًا، لأنهم يتحدثون باستمرار عن العودة للتحدث إليه للحصول على بركاته الأخيرة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/88559" target="_blank">📅 16:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#تقني
🔻
القضاء الامريكي يصدر حكما يلزم شركة ميتا بوضع حدود يومية لاستخدام تطبيقاتها وحظر استخدام الإنترنت ليلاً لمستخدمي منصات التواصل الاجتماعي التابعة لها من المراهقين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88558" target="_blank">📅 16:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
🇮🇷
مصدر إيراني رفيع المستوى:
لم يتم التوصل إلى اتفاق نهائي مع سلطنة عمان بشأن مضيق هرمز حتى الآن. لا تزال إيران وعُمان تعملان على تفاصيل اتفاقية تتعلق بمضيق هرمز.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88557" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
وزارة المالية العراقية تباشر بتمويل رواتب الموظفين لشهر آب الحالي ابتداءً من اليوم.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88556" target="_blank">📅 15:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📰
وكالة رويترز:
تحقق السلطات الأمريكية في اختراق ايراني لبيانات شركة مصنعة لتكنولوجيا مرافق المياه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88555" target="_blank">📅 15:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSvRdiwTdAk0CKYyLLlaZ2IeWjuD_Yb-HhtGxFUndWTMq2w5EdISPo19vIbA_GkjrKQ3KwwWfDYls461_F8CdemkwVzDL6cx5j0u6zn4pIKrU5bbV1gZVNFiXCDaUHhK38UA_PNBWWftuOFN1GvALqoAhbH65UA1urmx8eoPVsafvtCLl0SYlTR4uVfpcgxNF0U9_h8X5bgtP3LKM8vyOuD5f04_R6ys8TOTutf2Ju_Mg8mdW0bF7LJOiBKNnV4IsOEmKPtV3qPt4nsH9LzAczj-1lXZcaZzcFT8qKs99EIghugCkZZdZTNdmqxRbIG4v7rsFVlZAzO0AwZuOcVOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يسمح بالنشر بعد قليل ..</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88554" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
حرس الثورة:
اتفقنا مع عمان بشأن حصة كل منا من مياه مضيق هرمز وحصص عائداته.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88553" target="_blank">📅 15:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
حرس الثورة:
مضيق هرمز تحت سيطرة الحرس الثوري، ولا توجد أي سفن حربية معادية في الخليج. جميع السفن الحربية المعادية على بُعد 400 كيلومتر من مضيق هرمز، ومن الناحية العسكرية والإقليمية، لا يمكن لأي سفينة عبور هذا المضيق دون إذن إيران وإدارتها.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88552" target="_blank">📅 14:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9092897d1.mp4?token=vouZuR3i3LsxcHJI4B_pH9CIdTH4RlyKaTEFNOHmjrgnLan3vFRHnD6fLYVtjTUs9_2tEnMvJqVORkvMC3X56LgQNNwX0oEsC7VSL2iaYQth1g0qclvz8JUOHaihof-VTjkQYzHi0o2yXxkNFIR5mqMfzEjAA62ys5zER9IyxoJ-CmazHbHSz07y5d9-GahL_n1Tz-ZLigW5rydkI1zbXjoQnzTItbKiFn_1cZXE6cdDBjIOcLqNcyoDl1aV7IEGAAZTdVTgTn9JV-7iuoZVbO4QH9lW8b-eMpFFvsb0dK9XxTN1reGzioZ6UZea8DZEt0sIDWs3nZr0mxEmpj7UNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9092897d1.mp4?token=vouZuR3i3LsxcHJI4B_pH9CIdTH4RlyKaTEFNOHmjrgnLan3vFRHnD6fLYVtjTUs9_2tEnMvJqVORkvMC3X56LgQNNwX0oEsC7VSL2iaYQth1g0qclvz8JUOHaihof-VTjkQYzHi0o2yXxkNFIR5mqMfzEjAA62ys5zER9IyxoJ-CmazHbHSz07y5d9-GahL_n1Tz-ZLigW5rydkI1zbXjoQnzTItbKiFn_1cZXE6cdDBjIOcLqNcyoDl1aV7IEGAAZTdVTgTn9JV-7iuoZVbO4QH9lW8b-eMpFFvsb0dK9XxTN1reGzioZ6UZea8DZEt0sIDWs3nZr0mxEmpj7UNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع كبير تشهده اسعار الوقود في محافظة اربيل شمالي العراق حيث وصل سعر لتر البانزين الى 2500 دينار.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88551" target="_blank">📅 14:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
قالیباف:
إذا لم نتمكن من تحقيق مطالبنا، فسنواجه الولايات المتحدة بسيف القوة.
يجب إيداع الأموال الإيرانية المحتجزة في حساباتنا ووضعها تحت تصرف البنك المركزي؛ فوجود خط ائتماني يعني أن بإمكان البنك المركزي فتح "اعتماد مستندي" (LC) لأي جهة يختارها وفي أي وقت يشاء.
إذا حاول العدو الغدر، فنحن رجال الميدان؛ إذ أن المسافة بين ساحة الصراع الدبلوماسي وساحة المواجهة العسكرية قصيرة بالنسبة لنا، وأصابعنا على الزناد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/88550" target="_blank">📅 13:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88549" target="_blank">📅 13:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
🇺🇸
دوي صافرات الإنذار بالسفارة الأميركية في بغداد وسط حالة من الرعب تصيب سكان مجمع بغداد رزدنتي الملاصق لمجمع السفارة !</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88548" target="_blank">📅 12:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1481148818.mp4?token=rNI79oTBuzqSFyZdGfGTO4nzOHJU_p5flfbQ_Zod74YY3b5kgTAec8mPs5fLqKFfeebanCEc9xmrN-vBCJoQLY5KIW2yfNYOlmdLhzNQ2KdBUR-8gIfZ9aJyZdx7N7Th3z3YlKL_wJu9n-fN54B0Kib1j-WeHXZyL48DGUJft33aTWzk9YUklS-8jq69sAXEzHx4CURLFVZJYqx91gFzLh9QNr_cKgKRGvcKG9lCVnTv14AYxuuk9Mppw1mobeCtCeSILvhoykKl7jfSABjgvgBF1ahiFM6jQZFJOBHK43sZrVToGyyEVS9Km6ePq8TgWYbJQ1A87pVhPh6jfN4gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1481148818.mp4?token=rNI79oTBuzqSFyZdGfGTO4nzOHJU_p5flfbQ_Zod74YY3b5kgTAec8mPs5fLqKFfeebanCEc9xmrN-vBCJoQLY5KIW2yfNYOlmdLhzNQ2KdBUR-8gIfZ9aJyZdx7N7Th3z3YlKL_wJu9n-fN54B0Kib1j-WeHXZyL48DGUJft33aTWzk9YUklS-8jq69sAXEzHx4CURLFVZJYqx91gFzLh9QNr_cKgKRGvcKG9lCVnTv14AYxuuk9Mppw1mobeCtCeSILvhoykKl7jfSABjgvgBF1ahiFM6jQZFJOBHK43sZrVToGyyEVS9Km6ePq8TgWYbJQ1A87pVhPh6jfN4gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حادث سير مروع في محافظة أربيل شمالي العراق ؛ مقتل 6 وإصابة أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88547" target="_blank">📅 12:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قالیباف:  دور إيران والعراق في إرساء النظام الإقليمي حاسم.  لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/88546" target="_blank">📅 12:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر
قالیباف:
دور إيران والعراق في إرساء النظام الإقليمي حاسم.
لقد أطلقت أمريكا حربًا ضد إيران بهدف الإطاحة بالنظام الإسلامي وتوسيع هيمنتها في غرب آسيا والعالم الإسلامي، ولكن بفضل دماء الشهداء وبجهود الشعب الإيراني الشجاع وجهود جبهة المقاومة، لقد منيوا بهزيمة واضحة، وأقر بذلك العالم أجمع.
إن انسحاب القوات الأمريكية المتحالفة من العراق هو مصدر فخر تاريخي للحكومة والشعب العراقي، ونأمل أن يتحقق هذا الانسحاب بشكل كامل من الأراضي والجو العراقي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88545" target="_blank">📅 12:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
نتنياهو: لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88544" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔻
إعلام العدو:
من يتوقع أن ترفع إيران الراية البيضاء فهو مخطئ، فهذا ليس من أيديولوجيتهم، وليس في حمضهم النووي، وأعتقد أن ما يفعلونه حاليا، هو أنهم يستعدون سرا للهجوم الكبير الذي يريدون شنه ضد الولايات المتحدة وضد حلفائها في المنطقة قبيل انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88543" target="_blank">📅 12:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
نتنياهو:
لا يمكن التوصل إلى اتفاق دبلوماسي مع إيران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88542" target="_blank">📅 12:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4 ريختر تضرب قضاء بنجوين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88541" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
مناطق شرق مضيق هرمز وشمال المحيط الهندي وبحر العرب وبحر عمان تخضع لسيطرتنا العملياتية.
السفن تخضع لمراقبتنا قبل وصولها لمضيق هرمز بمئات الكيلومترات ويمكنها العبور إذا حصلت على إذننا.
قواتنا البحرية لم تسمح لسفن العدو العسكرية بالاقتراب من سواحلنا.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88540" target="_blank">📅 10:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
رويترز:  انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.  فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88539" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔻
رويترز:
انخفضت صادرات قطر من الغاز الطبيعي المسال بنسبة 96٪ بعد إغلاق مضيق هرمز بشكل فعال، حيث تم تصدير 18 شحنة فقط مقارنة بـ 509 شحنة في العام السابق.
فقدت قطر ما يقرب من 24 مليار دولار من عائدات الغاز، بينما تساهم زيادة صادرات الغاز الطبيعي المسال الأمريكية في سد جزء من هذا النقص.
في الوقت نفسه، تبلغ مستويات تخزين الغاز في أوروبا أدنى مستوى لها في هذا الوقت من العام، مما يزيد من خطر ارتفاع الأسعار مع اقتراب فصل الشتاء.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88538" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
في مظهر غير حضاري..
ساحات الإحتفال بالمولد النبوي الشريف بمحافظة أربيل شمالي العراق تتحول إلى مكب للنفايات!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88537" target="_blank">📅 10:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
الإعلام الأمريكي:
تم إخلاء يائير نتنياهو سرًا من ميامي قبل عدة أشهر، وذلك بعد اكتشاف خلية إيرانية كانت تراقبه في اللحظات الأخيرة.
تم تهريبه بسرعة كبيرة لدرجة أن أغراضه بقيت خلفه، بعد تقديرات تشير إلى أن الخلية الإيرانية كانت بالفعل "موجودة" في منطقة ميامي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88536" target="_blank">📅 09:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
🇮🇷
إن بي سي:
تسببت الهجمات الصاروخية والطائرات المسيرة الإيرانية في أضرار بمليارات الدولارات لمواقع الاستخبارات الأمريكية ومعدات المراقبة في جميع أنحاء الشرق الأوسط.
لقد كشفت هذه الهجمات غير المسبوقة عن نقاط ضعف في دفاعات القواعد الأمريكية وأجبرت المسؤولين على إعادة التفكير في كيفية حماية المنشآت الحساسة.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88535" target="_blank">📅 01:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
🇸🇦
مسؤول في الإدارة الأمريكية:
إدارة ترامب أحالت إلى الكونغرس اتفاقاً مع السعودية بشأن الطاقة النووية المدنية.
ترامب لا يزال يعتقد أن الاتفاق النووي مع السعودية لن يتقدم إلا إذا انضمت السعودية إلى اتفاقيات ابراهام و اعترفت بإسرائيل.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88534" target="_blank">📅 01:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=ELZrHqQRc726i__ZAtF5Ee6AgVCJU-w2DKSWstsosgPNlCw3tm-DzWvP20dOaxzh3heuPgIXhto-xwSESWd6whCGOzjUMQjQ4J8VU5xcC7_aarb1Tm9PFawBrwp80NNd6s5SyEov1OyW6K4LzlalXhGLHWOIg1vXWDP6MnxjukltCChZPO32U1AnVrVBdc36L9_zUIoKVeY_nXU_0xbcbhlIeiUZYURs9CaUddZ6-YETHRYOXegfoDY1k2lPl7IAZMOzv1K06J6xLczENl8T_Y5WD6VbtHHr5z3YcypeJVpzv0lMA584OiIWU6JjQGIWBv4x6Z34A5o_Cit3n4abnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2ae12376.mp4?token=ELZrHqQRc726i__ZAtF5Ee6AgVCJU-w2DKSWstsosgPNlCw3tm-DzWvP20dOaxzh3heuPgIXhto-xwSESWd6whCGOzjUMQjQ4J8VU5xcC7_aarb1Tm9PFawBrwp80NNd6s5SyEov1OyW6K4LzlalXhGLHWOIg1vXWDP6MnxjukltCChZPO32U1AnVrVBdc36L9_zUIoKVeY_nXU_0xbcbhlIeiUZYURs9CaUddZ6-YETHRYOXegfoDY1k2lPl7IAZMOzv1K06J6xLczENl8T_Y5WD6VbtHHr5z3YcypeJVpzv0lMA584OiIWU6JjQGIWBv4x6Z34A5o_Cit3n4abnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الولايات المتحدة
: تحطمت مروحية في ولاية كنتاكي تابعة للجيش من طراز UH-60 Black Hawk، وكان على متنها أربعة أشخاص.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88533" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
صرح وزير الخارجية ماركو روبيو لعدد من نظرائه الأجانب في الأيام الأخيرة بأنه "في الوقت الراهن" لا يُتوقع أن تشنّ الولايات المتحدة ضربات جديدة ضد إيران، وأن تُركّز على الضغط الاقتصادي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88532" target="_blank">📅 01:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=S0J5HVKvhYsoqumQvpZBDZ09nHwrI5SZIfzL_rt5DVHgGekSaoq_OwzgwuI6Y7kO705jQ8IJJojvGNs3IOAW2qwZVhET1h_Zk7fGGNnJe1BlSx9Bbl8Oh-zdTt2L3T7XAKQaFUkbOtbXHb2dUqvNxc4jxdujF3I2J7ZzUhJ6twzSVRPN4ifALa7pDWleYPI9NZh09K-Omsgeoa7yHULoafjWJ8Z-bKyi8rWm4i44P8E4pDV46BMYcTxKrYkpv2-yc-sV0fxo7Ea8YwuzzPBes9cB6PGTMHxh3LouxxKZJTFayn_sqOm6QRcfco0qJl4JtKFkkgL1iEodIsFL1SdhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ff577c2b.mp4?token=S0J5HVKvhYsoqumQvpZBDZ09nHwrI5SZIfzL_rt5DVHgGekSaoq_OwzgwuI6Y7kO705jQ8IJJojvGNs3IOAW2qwZVhET1h_Zk7fGGNnJe1BlSx9Bbl8Oh-zdTt2L3T7XAKQaFUkbOtbXHb2dUqvNxc4jxdujF3I2J7ZzUhJ6twzSVRPN4ifALa7pDWleYPI9NZh09K-Omsgeoa7yHULoafjWJ8Z-bKyi8rWm4i44P8E4pDV46BMYcTxKrYkpv2-yc-sV0fxo7Ea8YwuzzPBes9cB6PGTMHxh3LouxxKZJTFayn_sqOm6QRcfco0qJl4JtKFkkgL1iEodIsFL1SdhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
إعلام أمريكي : ‏أفاد مسؤولون أمريكيون أن مدير وكالة الاستخبارات المركزية الأمريكية، جون راتكليف، توجه إلى موسكو، روسيا، في زيارة غير معلنة يوم الثلاثاء، وهي أول زيارة رسمية له إلى العاصمة الروسية. وقد أمضى راتكليف نحو أربع ساعات في موسكو قبل مغادرته.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88531" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
