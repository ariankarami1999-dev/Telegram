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
<img src="https://cdn4.telesco.pe/file/LzdhB48oBpMjxN6B4EdYKP32pXm30BffwhVGyWPTkUrddRkDOdP8fJhRnNy6ewifG5UIBn-g4A-V5R9PdewiBbGXxSx1sZLxlLjnhCewKOu_ovA67BvpR3nyzkdPyfYlnS5f9MNVJPA12Nx0TbxKDyCVpMSCtSiqhSGmKiJh7J24Ffj3-sAqgWlSMGdjLtCZI2eb9y7z5Cw-vLbKlwebex5KXt0jTvZvMkf_5aNO8x2mHOjX-X6s6_W4S_Rz2dasWhGd4UyQ1c4TcLuUst-5EpY2sFmI42bzYcw-jdEmGA4D0s_pb85nBo1E4ST4Pgzh_Bg5bliJ-vpe9WHrIFhSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 05:23:27</div>
<hr>

<div class="tg-post" id="msg-82433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/naya_foriraq/82433" target="_blank">📅 05:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الهيئة البحرية البريطانية: حادث على بعد 9 أميال بحرية شرق سلطنة عمان.   السلطات العسكرية تُفيد بتضرر مؤخرة سفينة حاويات واشتعال حريق على متنها.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/naya_foriraq/82432" target="_blank">📅 05:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
مساعد الأمن في محافظة خوزستان الإيرانية:
إن مقاطعات هندیجان وماهشهر و آبادان تعرضت لقصف من قبل العدو.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/naya_foriraq/82431" target="_blank">📅 05:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوي انفجارات في ميناء جاسك ضمن محافظة هرمزغان الإيرانية.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/82430" target="_blank">📅 04:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962ba7b5d9.mp4?token=AI0ugIhetutRYKW3X3lkQGl_J457mt3IMh6bJYc3sQzQ6auywffRTFziaLbLgGDo9ldrNvX_txzJucbSElxw0UicX-ObUwtc9AXwsuOXoh3noKvBB-zMmoDbl403B87l5BCYYCLG7AYf0c-SHJueI5G1pj_cQGcIKXLLuXzlPGC9DWLChvwzmDRC4sR_Ci8xgCtOdoJjYQ99xIC9N5gknJldTPA5XZNok04sCyjH1gSyPU9ljFm37RYRsh9ZA2tD411KruHVPVjXjsbY0tjRK4LMSSHLSVLkibH07nqelxWteeHycnDK3xOxa4jhwMjEQvAeCeNz0CY0UpypCJ0R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962ba7b5d9.mp4?token=AI0ugIhetutRYKW3X3lkQGl_J457mt3IMh6bJYc3sQzQ6auywffRTFziaLbLgGDo9ldrNvX_txzJucbSElxw0UicX-ObUwtc9AXwsuOXoh3noKvBB-zMmoDbl403B87l5BCYYCLG7AYf0c-SHJueI5G1pj_cQGcIKXLLuXzlPGC9DWLChvwzmDRC4sR_Ci8xgCtOdoJjYQ99xIC9N5gknJldTPA5XZNok04sCyjH1gSyPU9ljFm37RYRsh9ZA2tD411KruHVPVjXjsbY0tjRK4LMSSHLSVLkibH07nqelxWteeHycnDK3xOxa4jhwMjEQvAeCeNz0CY0UpypCJ0R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقتل 2 واصابة 5 خلال حادث إطلاق نار في مدينة تورنتو الكندية.</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/naya_foriraq/82429" target="_blank">📅 04:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
مصدر إيراني: نفي وقوع انفجار في ميناء ديلم بمحافظة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/naya_foriraq/82428" target="_blank">📅 04:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
الأوضاع هادئة في مدن بندر عباس وسيريك وجاسك بمحافظة هرمزغان جنوبي البلاد.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/82427" target="_blank">📅 04:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
نفي وقوع انفجار في ميناء ديلم بمحافظة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/82426" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82425" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82424" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e56b905c.mp4?token=bGICZef91eYZNq_QF4mQmqUmmSXP0-CzlqVNKNxd0yUAw7llLNPri-xPz77sLHt8Tn69ccq5_m04YxYVKZ7F33d-aVftmSLZkt5jViVdfJa32NgGqjpw1dRvUAyCSun1RZK8PB-XgTiL1dhlcugE5hwnIVZk7SqPilOw4HONES38OqjU_o6RN9Ac_Ia6EEJ_vIZfNmkCvda5G0oVJcBnLinynjX3ua9RiFToBJo8a10WzZScXH0pqTqymSrvcuPftP97mZ_VmzOSuEHh3_ddAETAjNc-2HWvISCeKtRPZ2hChtc71MotoWQVkkx-2r1AMe-EMdHMI-tXzhMGKHHfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e56b905c.mp4?token=bGICZef91eYZNq_QF4mQmqUmmSXP0-CzlqVNKNxd0yUAw7llLNPri-xPz77sLHt8Tn69ccq5_m04YxYVKZ7F33d-aVftmSLZkt5jViVdfJa32NgGqjpw1dRvUAyCSun1RZK8PB-XgTiL1dhlcugE5hwnIVZk7SqPilOw4HONES38OqjU_o6RN9Ac_Ia6EEJ_vIZfNmkCvda5G0oVJcBnLinynjX3ua9RiFToBJo8a10WzZScXH0pqTqymSrvcuPftP97mZ_VmzOSuEHh3_ddAETAjNc-2HWvISCeKtRPZ2hChtc71MotoWQVkkx-2r1AMe-EMdHMI-tXzhMGKHHfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان في بوشهر عقب العدوان الأمريكي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82423" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سيريك مجددا دوي انفجارات</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82422" target="_blank">📅 03:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات في بوشهر وجغادك وعسلوية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82421" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26690d832.mp4?token=dlKlX6sGOR7k5HoWeBdDVOAFniCyaQbv1odQVC9-GxyeT7H3kWif_Q0lR8cfMWcxSj23hKuhdzgqCfyz0Kfxy5SWKizZ_UjAftXScqQKqrztc9K9JxX9VJtun43bzonCfzXCHo38jMtu95XyJdwzYYCeJ_ZWB99wAJNSP7Gf8Tmkf_v41vimqnvYPVzNssi2FARPg_jrcXXo80qFVWLIHAG3JKOo3XjuJOshtyL2zg8a-nFWtZn0r5iLKYlFMkJDPnLdAd7h8A5om6BAc6ucQvepz__Z7tzOerl6u8NkY8HnggxEGvCXPK1ra-RtY29sapiYs601VKwM0GHanf6jgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26690d832.mp4?token=dlKlX6sGOR7k5HoWeBdDVOAFniCyaQbv1odQVC9-GxyeT7H3kWif_Q0lR8cfMWcxSj23hKuhdzgqCfyz0Kfxy5SWKizZ_UjAftXScqQKqrztc9K9JxX9VJtun43bzonCfzXCHo38jMtu95XyJdwzYYCeJ_ZWB99wAJNSP7Gf8Tmkf_v41vimqnvYPVzNssi2FARPg_jrcXXo80qFVWLIHAG3JKOo3XjuJOshtyL2zg8a-nFWtZn0r5iLKYlFMkJDPnLdAd7h8A5om6BAc6ucQvepz__Z7tzOerl6u8NkY8HnggxEGvCXPK1ra-RtY29sapiYs601VKwM0GHanf6jgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تنشط في جنوب البلاد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82420" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوي انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82419" target="_blank">📅 03:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مصدر مطلع: حتى هذه اللحظة، لم يُسمع أي صوت انفجار في مقاطعة ميناب جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82418" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
إعلام العدو:
حدث أمني تحت الرقابة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/82417" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مصدر إيراني مطلع: نفي شائعة الهجوم على الأهواز وآبادان.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82416" target="_blank">📅 03:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e160b066cb.mp4?token=p_aVq7T-lJ0fmhclELhWW1GHriaGHj9utCkG02LQ3voPqz6UVxnWMN8_JJsHt1527UW6OsjZG-d3U5CEfy986K3KnM-fgIdXShfC_JvxOBaxSWRrhIxsn_DP4jBx7zPAB3o7Q027snPug4fDUnVcp7_aYkQOtkBQsiLt4NKKBg5VnabK80q-9cgmp0xTcVPkIkQAlzFEP88iToioAu3wyF7e_hfnwQreX4K4g6mZzybmznYjQ_fSfZ4jEqeBspV-tfb_btbV-UDc0uc17l7lEbxKbyBrf2xTZMkILkulXjKF2BoOTPOphnUNqzDDMkx6eyYQEzM2c5VkT6Sn3sjqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e160b066cb.mp4?token=p_aVq7T-lJ0fmhclELhWW1GHriaGHj9utCkG02LQ3voPqz6UVxnWMN8_JJsHt1527UW6OsjZG-d3U5CEfy986K3KnM-fgIdXShfC_JvxOBaxSWRrhIxsn_DP4jBx7zPAB3o7Q027snPug4fDUnVcp7_aYkQOtkBQsiLt4NKKBg5VnabK80q-9cgmp0xTcVPkIkQAlzFEP88iToioAu3wyF7e_hfnwQreX4K4g6mZzybmznYjQ_fSfZ4jEqeBspV-tfb_btbV-UDc0uc17l7lEbxKbyBrf2xTZMkILkulXjKF2BoOTPOphnUNqzDDMkx6eyYQEzM2c5VkT6Sn3sjqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية البطلة تشتبك مع اهداف معادية في سماء مدينة ماهشهر ضمن محافظة خوزستان جنوبي إيران</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82415" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوي الانفجارات التي سمعت في قشم كانت نتيجة اشتباكات في مياه الخليج الفارسي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/82414" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82413" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سماع دوي انفجار في قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/82412" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Up6mFGhsuDEMZS-pTwnBSBTFh_IFVnCNvQVIvxohmZCx6OaZv36XmpIHUxNOn2CLsgS_t0XrW6Dgqh2ZkvboFz-jrj0a_NwO-xF3OkKoI576N5ENsG-j8-7kGonyr23J0DA-QwjkUfEHea6dnUNF4cJvj4WF10ddjoRpb0qbaDqss20L3ILJgP1_F67kExG0VuBh7btSVYVRjZSSS3whZQeJw_2MZyK6WWsOdvXp9h6AH749UErZniMI-AlnTgx0h0QFijZEPlibKA-X4is66dT9fPTREUQVx83_ahkEW5qe1JKJWI-WUWz7DIz0nh0lXWCx1vlDdkca2LwYybFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي انفجار في قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/82411" target="_blank">📅 03:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات في ميناء سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/82410" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
وزير الحرب الأمريكي: لقد اتخذت إيران خياراً خاطئاً. والآن تدفع الثمن.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82409" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4npElzHKSIRRI-PLURm-PTGUkXCz9-zqsk_bjDjbzbYIKOaeTjKG_6t9viZFr_SQ6PjbyRvz0VH39NVykgerCT8FclIasDXrO-vA2K5uezOXrG4GqGOTjN0KC_T9QRxDEFiJ02gUkklaOSrIEax1MZPYx4DZfsvcs_gVr7IkKcE7TiE02lJ-KzLf50l8FBppxbnKbFFcjops-EW4enwzPqILb2z7HZUBcu6owth5oez3rOaD6brKLWcTm5vEOdhKMMJ6avRczON8Ge2vZ-IYQv8E_CnsUUqgkXEeVD4EzsZR_EUTfZQg1K-cNswHFG_ARDjlVfNg99WE1b7T6-DRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/82408" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
الجيش الأمريكي: ‏ في تمام الساعة 7:15 مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية الجولة الثالثة من الضربات الجوية هذا الأسبوع ضد إيران، وذلك بعد أن هاجمت قوات الحرس الثوري الإسلامي بشكل سافر سفينة الحاويات "إم/في جي إف إس…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/82407" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مسؤول أمريكي: إن القوات المسلحة الأمريكية تشن ضربات على أهداف إيرانية في منطقة مضيق هرمز ردًا على إطلاق الحرس الثوري الإيراني النار على سفينة تجارية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/82406" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارات جديدة جنوبي إيران</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/82405" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82404" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82403" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82402" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
اعتقال النائب السابق طلال الزوبعي عقب اقتحام منزله الكائن في منطقة الحارثية شارع الزيتون من قبل قوة عسكرية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82401" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82400" target="_blank">📅 02:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
انباء متداولة عن اعتقال النائب السابق طلال الزوبعي في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82399" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28dfe9bce.mp4?token=SB4oITiYVZ_1DRs1w54SSfeilUeNibevT5_fJ7IvwEVVeJ_kgibCORIth3GuEw9D9wCRVkpnYeQ3FIF6SkfWZFqiPjTQe0ysFCzROaH6IX0tCRsim77tm3fzMImE0o1hCHfLgtuEvxoDkh6DGasIjr0uSV7MR6ABK03FmrfDLynrq46NU39en4i0UnXu7bc_jwIcFdUV6r8w_1rKHhUvgOe8r7JfAfm4MnDK7KdDDYOsoJlnlRAM8yf09eEvosPScN6sv4dgMQMe-Vm_ihiZ_SaC_tDZ-Q0L0cGaAHkZV6Zqy3AdK_Lx0-Nd15S9Yx4Ek5pVyNd-seKs6i2WR5OwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28dfe9bce.mp4?token=SB4oITiYVZ_1DRs1w54SSfeilUeNibevT5_fJ7IvwEVVeJ_kgibCORIth3GuEw9D9wCRVkpnYeQ3FIF6SkfWZFqiPjTQe0ysFCzROaH6IX0tCRsim77tm3fzMImE0o1hCHfLgtuEvxoDkh6DGasIjr0uSV7MR6ABK03FmrfDLynrq46NU39en4i0UnXu7bc_jwIcFdUV6r8w_1rKHhUvgOe8r7JfAfm4MnDK7KdDDYOsoJlnlRAM8yf09eEvosPScN6sv4dgMQMe-Vm_ihiZ_SaC_tDZ-Q0L0cGaAHkZV6Zqy3AdK_Lx0-Nd15S9Yx4Ek5pVyNd-seKs6i2WR5OwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر
🇮🇷
ايران تغلق مضيق هرمز مجددا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82398" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82397" target="_blank">📅 01:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
الحرس الثوري :
اغلاق مضيق هرمز حتى اشعار اخر.
بسم الله الرحمن الرحيم، قاسم الجبرين
في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.
قبل ساعات قليلة، تم تجاهل هذه التحذيرات، وبتحريض من جهات أجنبية، حاولت عدة سفن الإبحار في المسار غير المصرح به، متجاهلةً تحذيراتنا وتذكيراتنا بضرورة تصحيح المسار والالتزام بالمسار المصرح به.
وبالتالي، تعرضت إحدى السفن، التي عرّضت الأمن البحري للخطر بتعطيل أنظمتها، لإطلاق نار تحذيري، ما أدى إلى إيقافها.
ونتيجةً لهذا الحادث، ونظراً لظهور هذا الوضع الأمني ​​غير المستقر بسبب التدخل الأجنبي غير القانوني، سيتم إغلاق مضيق هرمز حتى إشعار آخر، وحتى انتهاء التدخلات الأمريكية في هذه المنطقة، ولن يُسمح لأي سفينة بالمرور عبره. ثانيًا، إذا أخطأ العدو المعتدي وشنّ عدوانًا جديدًا علينا متذرعًا بهذا الحادث الذي تسبب فيه بنفسه، فسوف نرد بقوة، وسنستهدف قواعد العدو الجديدة في المنطقة.
وتتحمل الدول التي سمحت بدخول العدو الأمريكي الصهيوني إلى أراضيها مسؤولية عواقب هذا التدخل.
والنصر من عند الله وحده، العلي القدير الحكيم.
الحرس الثوري الإسلامي - البحرية</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82396" target="_blank">📅 01:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
انباء متداولة عن اعتقال النائب السابق طلال الزوبعي في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82395" target="_blank">📅 01:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a05d62e2.mp4?token=sdZ7BGDqWuYZ5EDrIodu-bOEk4RntA9O6a1oFFIqNIisgMCpTQOx5rebPbNwrDtR2dm5ilNaqF8fZaL9K0tvwKuTnoJ4rri_VRVI_ogkPPqldGYU5JH6QFEVayT1ONWhsHWy0diavYAAZ9eTN7W5VMe3YKlWpr8MnefEuhpM_mjpYKTMIC0EHr4qOFhbzDK6FaVdKVvW4Dloh7hGJAHI78BQNMjXaX_FDO9fiLlz1i6kwexWsr1K69s_Uq88XA48nZDi8ekG3t1XZKRSnqDhd_Nlyw5ua2vA6hHbq_LuB12guLkQEaPdsoBS15y2fBky0RsdJDq3Dk8VLUVR3zR2BDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a05d62e2.mp4?token=sdZ7BGDqWuYZ5EDrIodu-bOEk4RntA9O6a1oFFIqNIisgMCpTQOx5rebPbNwrDtR2dm5ilNaqF8fZaL9K0tvwKuTnoJ4rri_VRVI_ogkPPqldGYU5JH6QFEVayT1ONWhsHWy0diavYAAZ9eTN7W5VMe3YKlWpr8MnefEuhpM_mjpYKTMIC0EHr4qOFhbzDK6FaVdKVvW4Dloh7hGJAHI78BQNMjXaX_FDO9fiLlz1i6kwexWsr1K69s_Uq88XA48nZDi8ekG3t1XZKRSnqDhd_Nlyw5ua2vA6hHbq_LuB12guLkQEaPdsoBS15y2fBky0RsdJDq3Dk8VLUVR3zR2BDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لمحة عن الذين يُراد لهم أن يحلوا مكان حزب الله ويتولوا الجنوب اللبناني بينما يفرطون بأوطانهم مقابل لا شيء.. إبراهيم الصقر أحد مسؤولي حزب القوات اللبنانية في تصريح له: إذا دخل الجولاني في حرب ضد حزب الله سأكون بجانبه وسأؤيده (
صدر البيت اله والعتبة النا
).</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82394" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
تقليص الدوام الرسمي في محافظة ميسان لمدة ساعة واحدة خلال شهري تموز وآب، ليكون من الساعة السابعة صباحاً وحتى الواحدة ظهراً، بسبب ارتفاع درجات الحرارة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82393" target="_blank">📅 00:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo2wEOHvVO3MMrJdrrJZuizefjIW5Ok4BSUpjXEQsVKGyR0RX3lPSsLQvxbAeTYsd53RdQ8oVAYwHgIyZSg9aV3VXDMwYx3ex_K_o5kkuhugP34fBHveWxZsd4zhOil43AJvYnPLQ3wrzxBTCkLYhYmyy9GxzME0YlnrQqeTDTwyxY8yLpxW0wWEkWMUJVx4n5gvLcu26z_XN3VchPz3mNkMVmUzmw5kEspb6Nn3e_V9Z3CRnHHX-wWNaYu1PxNf7J5h-Pd4Ybtnj1YVGv1loq9lWIhxlbL8lz7NIlyB3g5AQ4BUfQEfTj1EPTGU3JYwAInmHRcvr5iKi8MM_UmVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العثور على كدس قنابل في منطقة حي العامل بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82392" target="_blank">📅 00:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انباء عن نشاط دفاع الجوي في محافظة اصفهان الايرانية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82391" target="_blank">📅 23:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
الاعلام الاميركي:
المقترح العماني يتضمن إدارة المرور عبر مضيق هرمز عبر ممرين منفصلين</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82389" target="_blank">📅 22:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTUBm-kKnBNh9j7EkjHQKmdj1ME0g-LIjo8Xay-S1RxI4mkSKdWOKOuKymCucLvdpnZku-jaF6arxo5-0IlKM-WgPo6Oq95aY5SMC2eY2fCn15bSoQvd_gbyt-4CNhh_i_-jN3Ll5zVJV7KxEOiqb64llmpfmno3voUqxXVr99Blw094PSHIxai-c8iTWjQ26zFx4eOFdfpnAoOCdf39LV3TdCV1_XBc8kRLWJmCkcOESzbIg7W0nUFCEYFs9rcQWR0XlDY25kdPkaY46zJqLcZgIF1ICLvCWcvTVsxVv2E0sqyMN41OEeqONa9qdrJS_ywWz_1RYSF9ECk39M6uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عقب إقلاعها بدقائق..
طائرة إماراتية تطلق نداء الطوارئ فوق خليج عمان وتعود نحو مطار دبي.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/82388" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🇮🇷
‏
السفير الأميركي في إسرائيل:
لا نرى أدلة حقيقية على وجود جناح معتدل في إيران.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82387" target="_blank">📅 21:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
🔳
وزارة الخارجية العراقية:
تابعنا حادث إطلاق النار على زورق الصيد ووفاة الصياد منذ اللحظة الأولى لورود المعلومات بشأنه.
سنواصل متابعة نتائج التحقيقات مع الجهات الكويتية المختصة واتخاذ ما يلزم من إجراءات دبلوماسية وقنصلية بالتنسيق مع السلطات العراقية المعنية بما يكفل حفظ حقوق المواطنين العراقيين.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/82384" target="_blank">📅 20:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82383">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0718a341f3.mp4?token=HJS1cBjNI4G9Wl_bcIfR6ork-mJlz410AURxfJ6H1QPMsWcal0bZSn4ex_o-ataYE5tfxMWWMkNY4G6uzSG2SfaOIAzxZWlgca5pdZV359nWE13ehwLbQgQ-AzuccfBoppqP9_ZRTZd23ZrNHLxuTBN2NYMp762SNyaK9aFElq51bT2PscW7ShBPL4ebs7X_DtQkMQm4ivnRa_-uPaRa46pzH81PNSKyaHcC3Uxrihv8iv8QLeKiZVD7Lmi0P-bc8_pdAMSBx_UIOpNRzzyIUqN9ahiQc4fKGZ0HiUNhpJHdUEV7Ats7VvIG0l-QFf6sYYKNvBj8pkZirfbtVKuzJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0718a341f3.mp4?token=HJS1cBjNI4G9Wl_bcIfR6ork-mJlz410AURxfJ6H1QPMsWcal0bZSn4ex_o-ataYE5tfxMWWMkNY4G6uzSG2SfaOIAzxZWlgca5pdZV359nWE13ehwLbQgQ-AzuccfBoppqP9_ZRTZd23ZrNHLxuTBN2NYMp762SNyaK9aFElq51bT2PscW7ShBPL4ebs7X_DtQkMQm4ivnRa_-uPaRa46pzH81PNSKyaHcC3Uxrihv8iv8QLeKiZVD7Lmi0P-bc8_pdAMSBx_UIOpNRzzyIUqN9ahiQc4fKGZ0HiUNhpJHdUEV7Ats7VvIG0l-QFf6sYYKNvBj8pkZirfbtVKuzJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تشييع رمزي لجثمان الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه) في مدينة الكاظمية المقدسة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82383" target="_blank">📅 19:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز أربيل الان شمالي العراق</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82382" target="_blank">📅 19:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963a74de8c.mp4?token=Ti4jz4ebSipRgCD2oJ40lD-MIx2cqVtu1ORoyT2RKCBELS79UzYZIkPrs4DRed5VdsuZWA9XR-MvxgBEgGpFDGI3P5joVVlgj13iU3vsMLehJYIoQCKntyAccuEvF3FVPh6es9h1jCXL3C-Vy6GgYND5BA3aKLiNONrrMoww6aAaFOD4ZG-rFTOf37liY5M8VZ3CUchmqxB3MoUo6Iqj2YkF2ysLzm09mYpsWppvNbEFWPjIopQqU8hduHPE7pmkGQSxVyErzMlrCYjqndDu6nqe-l9PT-e-v3BliK7oorr69lQ1HlmUs7CnNOjGrsMoaU-y3B41lNX4JRwx_zA5gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963a74de8c.mp4?token=Ti4jz4ebSipRgCD2oJ40lD-MIx2cqVtu1ORoyT2RKCBELS79UzYZIkPrs4DRed5VdsuZWA9XR-MvxgBEgGpFDGI3P5joVVlgj13iU3vsMLehJYIoQCKntyAccuEvF3FVPh6es9h1jCXL3C-Vy6GgYND5BA3aKLiNONrrMoww6aAaFOD4ZG-rFTOf37liY5M8VZ3CUchmqxB3MoUo6Iqj2YkF2ysLzm09mYpsWppvNbEFWPjIopQqU8hduHPE7pmkGQSxVyErzMlrCYjqndDu6nqe-l9PT-e-v3BliK7oorr69lQ1HlmUs7CnNOjGrsMoaU-y3B41lNX4JRwx_zA5gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
دوي انفجار مجهول في محافظة السليمانية بالقرب من الحدود العراقية الإيرانية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82380" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_E8k8BxhU-v0OpkL5nHpMBB93mAf0hxdP9s7jXTsGU6V0EC5BENm7CKDFhLd4DAKEe_9E3QQj-jS4c6WWyvlIOGxx6F449D5SzTg2F2C5BuREJJopcP7yjNietZWgL0c7Mue-3TMCbMh0ir2HpueVNmTIcpxr5adg24jm0RFEX6ydeBcQuTtfIPZaWLehryZRooVCpJJFRYi_7w9O8DaOnzF_6d_zSXdlv2FLL3d7xLYyTnxB-bo53DIHlk3AKnzqqVvo9KElIVspT39L4B4oGCEDvg37ZUt7mtROFW66DGMXl8baJleKg1X98S_XCIXYX1SGP7rlmIDfOcYArTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82379" target="_blank">📅 18:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82378" target="_blank">📅 18:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
مسؤولين أمريكيين:
ترمب يمنح المفاوضين الأمريكيين وقتا محدودا للتوصل لاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82377" target="_blank">📅 18:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
دوي انفجار مجهول في محافظة السليمانية بالقرب من الحدود العراقية الإيرانية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82376" target="_blank">📅 17:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
إعلام العدو:
عملية إطلاق نار في شارع القدس بمنطقة يافا ضمن تل أبيب المحتلة؛ إصابة خطيرة كحصيلة أولية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82375" target="_blank">📅 17:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a715d83e0.mp4?token=WzIDcExvpTBirsPiR7q6xea3jL91C__AbVkt9vmBH7VaBxldtDtE35wh1XKBp886mVZpqujXwv033lEyY7LBRru8Yqg1kAvCo2iBQedojV6gI34NEB_FVTE2ofVbcK3iUq18Fi788edFInUGoO3yGiIk3ua2BgzsYcijJbWpdOtvgEUuMxYi9kMw8BQraMtfcC3lDZjkxXAsAbiOFquCb8XKYbymFREQUgbEqjTGKSf771bLx_E9rZWanQ5wjMwW2OAiD7DA28i3M33Figcy8DrRr6LL8SpqtaIBEk-vxeuTXDvhtZQXKDNgepK9Ir-v6GhZhfFz-s0H5MbYNOa-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a715d83e0.mp4?token=WzIDcExvpTBirsPiR7q6xea3jL91C__AbVkt9vmBH7VaBxldtDtE35wh1XKBp886mVZpqujXwv033lEyY7LBRru8Yqg1kAvCo2iBQedojV6gI34NEB_FVTE2ofVbcK3iUq18Fi788edFInUGoO3yGiIk3ua2BgzsYcijJbWpdOtvgEUuMxYi9kMw8BQraMtfcC3lDZjkxXAsAbiOFquCb8XKYbymFREQUgbEqjTGKSf771bLx_E9rZWanQ5wjMwW2OAiD7DA28i3M33Figcy8DrRr6LL8SpqtaIBEk-vxeuTXDvhtZQXKDNgepK9Ir-v6GhZhfFz-s0H5MbYNOa-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع حريق وتصاعد أعمدة الدخان في مخازن السكك بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82374" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f4c182d.mp4?token=bEfRcsLff0Tgg6tIpN-X15bnpDU2kSwLidwlK0g7Hds6HhcLIBglOZNKsi6L_KrWLfXRykXiK_18aWPDOSoVLmJ3uKXdXrUIr8xQU98SY_37wY103C96T-6PPJSmj_16j6smGkYKaUG33z0p0uzYNssaJ4Aafo_VpRi8YRXDGUscgizWD4MQD05MUATKC62rCA9cXOkwWNO5IsgVbVU1ySHJl3dc6XG65ZvcMCjQS6zEwL1-UDFb8GTqAhGFisaYUbp4qOiArxtgUu19uCJSWAnfQSirxGURbVikUtwpnpjS20FFjaCT0MEduf560-ZmbjAIm1wvNHYyu3Uoqubi2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f4c182d.mp4?token=bEfRcsLff0Tgg6tIpN-X15bnpDU2kSwLidwlK0g7Hds6HhcLIBglOZNKsi6L_KrWLfXRykXiK_18aWPDOSoVLmJ3uKXdXrUIr8xQU98SY_37wY103C96T-6PPJSmj_16j6smGkYKaUG33z0p0uzYNssaJ4Aafo_VpRi8YRXDGUscgizWD4MQD05MUATKC62rCA9cXOkwWNO5IsgVbVU1ySHJl3dc6XG65ZvcMCjQS6zEwL1-UDFb8GTqAhGFisaYUbp4qOiArxtgUu19uCJSWAnfQSirxGURbVikUtwpnpjS20FFjaCT0MEduf560-ZmbjAIm1wvNHYyu3Uoqubi2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🔳
قطاعات ‏الجيش العراقي تنتشر في محيط القنصلية الكويتية بمحافظة البصرة لتأمينها وسط تصاعد التوترات والاحتجاجات على خلفية استشهاد صياد عراقي على يد خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82373" target="_blank">📅 17:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يطالب وزارتي الخارجية والعدل بإنهاء الصمت الدبلوماسي وتقديم شكوى واستدعاء السفير وإجبار الكويت على الاعتذار والتعويض عن جريمة قتل الصياد العراقي</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82372" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e96c42f.mp4?token=S2ijzTv-VPmdOCR9z4n0GhrXC3816OqMNzjTDyAkYIPPME27LK2BU7j1FkZ28kIivh8UrltEXPv_6sArvDat8KkCA-jmiyteZKLytFUo8D8Qzl4PBJsQbrOsS0w7zcvUn_6-02PpwIxjwaLHXKv-xYKHIObfER7MiSztK8pcdAg7UNnyqcKwSB5QXzW_Uj9z6wt58sZES-5w8t6uJi5XfPtqAJWVeB7nzRPdoNRk1F9Zu4dLp_NcNGm_63_rZcNY5Mm72kElyzfXn3wah5SYSBW8wduEljmzcw9tc3mPIjbcwmHEP6cPQYweXoPJJamMA9eygv4xVUgqjjydFkEaWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e96c42f.mp4?token=S2ijzTv-VPmdOCR9z4n0GhrXC3816OqMNzjTDyAkYIPPME27LK2BU7j1FkZ28kIivh8UrltEXPv_6sArvDat8KkCA-jmiyteZKLytFUo8D8Qzl4PBJsQbrOsS0w7zcvUn_6-02PpwIxjwaLHXKv-xYKHIObfER7MiSztK8pcdAg7UNnyqcKwSB5QXzW_Uj9z6wt58sZES-5w8t6uJi5XfPtqAJWVeB7nzRPdoNRk1F9Zu4dLp_NcNGm_63_rZcNY5Mm72kElyzfXn3wah5SYSBW8wduEljmzcw9tc3mPIjbcwmHEP6cPQYweXoPJJamMA9eygv4xVUgqjjydFkEaWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🏴‍☠️
استهدفت مقذوفات "جيران 4 " الروسية، والمزودة بأنظمة توجيه كهروبصرية، مستودع نفط تابع لشركة "بي آر إس إم-نافتا" في مدينة بيريا سلاف، الواقعة في منطقة كييف. زيلينسكي أعلن اليوم ان بلاده نفذت منها صواريخ الباترويت الأمريكية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82371" target="_blank">📅 16:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">شعبٌ يُقاوِم الاحتلال لن يخون الشهداء.
شكراً يا عراق الوفاء، شكراً يا أشرف شعوب الأمة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82370" target="_blank">📅 16:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cdfd7d02.mp4?token=Zxtr7Z33QM6yRdE2F9k1I741ZwMqDofYTyqp5vvZjx3CmPRvs3V4-tjakjwBn4BrTLeqm-8rxymhK_2PYv4HUcDRl1xHlVYQgNpWqh8Aydd0LAnlcVMsl7YUFL3YIO68ag7rWrYCQV9RVfZ3JRrhx6_7fz1ZgdsjU2_BnPnIfGp6CFMRblqoGtQCKm7qU7CM0c1g9Y4kSBMoIBUbMeUN6983qD_MzAFXWK3biWLhH2_AW5wxmfmGCoBhVXH1hCqCw-OyvvBYeATMm0a4KA8bFBgpgO1axkE_51Pi1HeiVGx0dDnadyVQFmdHx1ypyvMpe8jcvIyEMtgwEFOObzszWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cdfd7d02.mp4?token=Zxtr7Z33QM6yRdE2F9k1I741ZwMqDofYTyqp5vvZjx3CmPRvs3V4-tjakjwBn4BrTLeqm-8rxymhK_2PYv4HUcDRl1xHlVYQgNpWqh8Aydd0LAnlcVMsl7YUFL3YIO68ag7rWrYCQV9RVfZ3JRrhx6_7fz1ZgdsjU2_BnPnIfGp6CFMRblqoGtQCKm7qU7CM0c1g9Y4kSBMoIBUbMeUN6983qD_MzAFXWK3biWLhH2_AW5wxmfmGCoBhVXH1hCqCw-OyvvBYeATMm0a4KA8bFBgpgO1axkE_51Pi1HeiVGx0dDnadyVQFmdHx1ypyvMpe8jcvIyEMtgwEFOObzszWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات البرزاني ترسل تعزيزات عسكرية الى قضاء خبات في محافظة اربيل بالتزامن مع تحركات لقبيلة الهركية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82368" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
نيويورك تايمز عن مسؤولين أمريكيين:
إذا لم تصدر إيران بيانا تقر فيه بفتح الممرات في مضيق هرمز فإن العواقب ليست في صالحها</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82367" target="_blank">📅 14:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/82366" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82366" target="_blank">📅 14:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">"سيتحقق هذا الأمر، وسينفذ قريبًا أحرار من جميع أنحاء العالم جزءًا من هذه المهمة الإلهية"</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82365" target="_blank">📅 14:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/82364" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/82363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇮🇷
البيان الكامل لقائد الثورة الاسلامية سماحة السيد مجتبى الحسيني الخامنئي.
بسم الله الرحمن الرحيم
السَّلامُ عليكَ يا ثارَ اللهِ وابنَ ثارِه، والوترَ الموتور. السَّلامُ عليكَ وعلى جدِّكَ وأبيكَ وأمِّكَ وأخيكَ والمعصومين من وُلدِكَ.
🔸
سلامٌ على الإمام الذي امتدّ نداءُ نهضته الذي يبث الحياة، صدىً عظيمًا مدوّيًا للبعثة النبوية، إلى أعماق التاريخ البعيدة، فانبثقت من أثره الثورة الإسلامية في إيران؛ تلك الثورة التي كانت حسينيةً من أساسها، وبُنيت وارتقت بشعار الحسين (ع) ونهجه. لقد نشأ شهيدُ إيران أيضًا على هذا النهج؛ فكان حسينيًا، وفكّر حسينيًا، وتحرّك حسينيًا، وجاهد وقاوم حسينيًا، وعاش حسينيًا، وبذلَ دمه حسينيًا في سبيل مدرسة الحسين، فنال الشهادة.
▪️
من بين الحسينيين رجالٌ، حين تُسفَكُ دماؤهم مظلومين في سبيل الحسين، ومن أجل مدرسته ونهجه (عليه السلام)، تنهض الأمة الإسلامية، فيتصل ذلك الزمان بعاشوراء، وذلك المكان بكربلاء. واليوم، الملحمة الحسينية ذاتها قد بعثت شعبنا، وأضفت على مدرسة الإمام الخميني الكبير والإمام الخامنئي الشهيد تجلّيًا جديدًا. هذه هي تلك الملحمة التي تبث الحياة، وهي الصدى لنداء مظلومية الحسين (عليه السلام)، ونداء: «هل من ناصرٍ ينصرني؟» في إيران، ثم في العراق وسائر البلدان، فتُزلزل الباطل.
⏺️
كما يجدر، في هذه المناسبة، أن أتقدّم بخالص الشكر والتقدير إلى عشرات الملايين من الناس الذين سجّلوا حضورًا مذهلًا، كاسرًا للأعداء، وتاريخيًا، في مدن إيران والعراق وقراهما، ولا سيما في طهران وقم والنجف وكربلاء ومشهد.
شعبنا يُنادي بالثأر لدماء الحسين (ع)؛ فلقد قدّم هذا الشعب العظيم، على مدى السّنين، أبناءه فداءً في سبيل الحسين (ع)، وفي الحرب ضد أعداء الحسين والغيرة الحسينية، وهو يطالب اليوم أيضًا بالثأر لدمائه ولدماء حسينيّي هذا الزمان.
🔻
والآن، أخاطب إمامنا الشهيد فأقول:
أيها القتيل المظلوم، أيها المظلوم الشامخ، أيها العبد الصالح لله، فيما نحن نودّع جثمانك بعيون دامعة وقلوب مكسورة، نعاهدك أن نصون مدرستك، وأن نسلك بثبات ذلك الصراط المستقيم الذي رسمته، وألّا نهاب مشقّات هذا الطريق، وأن نعقد القلوب، كما فعلت، على البشارات والوعود الإلهية.
⏺️
ونعاهدك أن نثأر لدمك الطاهر، ولدماء شهداء هاتين الحربين جميعهم، من القتلة المجرمين المَخزيين. فهذا الثأر مطلب شعبنا، ولا بدّ أن يتحقق حتمًا. إنّ هؤلاء المجرمين، الذين توجد قائمة كاملة بأسمائهم من أوّلهم إلى آخرهم، سيحملون معهم إلى قبورهم أمنيةَ أن يموتوا موتًا هانئًا على فراشهم. وعليهم أن يعلموا أنّ هذا الأمر لا يتوقف على وجودي أنا أو وجود سائر المسؤولين؛ فنحن، سواء أكنّا موجودين أم لم نكن، سيتحقق هذا الأمر، وقريبًا سيؤدي أفرادٌ من أحرار العالم، كلٌّ منهم، جزءًا من هذه المهمة الإلهية.
▪️
يا أبا الأمّة الشهيد، هنيئًا لك ارتشاف شهد الشهادة الذي كنت تتمناه عمرًا طويلًا. ومبارك عليك ارتداء ثوب الشهادة ببدن يحمل علامات من أمّك الزهراء الطهرى وجدّك أبي عبد الله الحسين وأبي الفضل العباس (عليهم السلام). وأنتم يا رفاقه المظلومين الذين تعرضتم لهجوم مباغت من العدو ونلتم الشهادة، طوبى لكم، إذ تحلّون الآن ضيوفًا على ذلك المولى الذي ربما تلمّستم رأفته ولطفه مرارًا وتكرارًا. إن ذلك السيد الذي يمثل باب الرحمة الإلهية للجميع، ولا سيما لأهل هذه الديار، هو المستضيف لكم الآن، وقد غدا جواره الآمن منزلًا لكم.
⏺️
أيها المولى العالي المقام، أيها الجليل، أيها الإمام الرؤوف، يا أبا الحسن الرضا المرتضى، عليك أفضل صلوات الله، يوارى الآن في هذا الثرى الطاهر الجثمانُ المقطع لخادم من خدّام حضرتك والعترة الطاهرة، بعد سنوات من الجد والجهد والجهاد الدؤوب، ومعه أبدان شهداء من عائلته، يُذكّر كل منهم بشهيد من شهداء صحراء كربلاء، ليرقدوا هنا إلى ذلك اليوم الذي يخرج فيه، بأمر الله، بقية الله (عج) الشَّمس الساطعة من خلف غيوم الغيبة، ليفيض بنور الرحمة الإلهية على أهل المعمورة. وفي ذلك اليوم الذي نرجو أن يكون قريبًا جدًا، سترافقه - عج - نجومٌ من الصدّيقين والشهداء والأولياء، ونأمل أن يكون سيدنا الشهيد أحد هؤلاء، ليعيد مجددًا رسم مشاهد واعدة وخالصة من الجهاد والوفاء بعهد «ألست»، ولعل هؤلاء المرافقين يصحبونه في ذلك اليوم أيضًا.
▪️
يا مولاي الرؤوف، إننا نستودعك سيّدَنا الذي بذل ما يملكه كله في سبيلكم، ومعه رفاقه الشهداء، ليتشرفوا بلطفكم وعنايتكم، وكما كانوا ينعمون بفيض لطفكم في حياتهم الدنيا، فليحظوا به من الآن فصاعدًا على نحو أكمل وأسمى بكثير.
وفي الختام، نتقدم مجددًا بالعزاء لسيدنا بقية الله (عج)، ونبتهل إلى ذلك المولى الرحيم أن يشمل بدعائه الزاكي سيد شهداء إيران ورفاقه الشهداء والشهداء كلهم، وأن يسأل الحق (جل وعلا) علو الدرجات للشهداء جميعهم، والصبر والأجر لذويهم، والفتح والنصر الحاسم والقريب للشعب الإيراني المظلوم، إن شاء الله.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82363" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قائد الثورة: أقول لراعينا الشهيد: يا قتيلًا مظلومًا! يا مظلومًا منتصرًا! يا عبدًا صالحًا لله! الآن، ونحن نودع جسدك بعيون دامعة وقلوب حزينة، نعهد إليك بأن نحافظ على مذهبك، وأن نسير بثبات على الطريق المستقيم الذي رسمته، وأن لا نخشى الصعاب في هذا الطريق، وأن…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82362" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي: نَعِدُ بأن ننتقم لدم القائد الشهيد ودم جميع الشهداء في الحربين من القتلة المجرمين عديمي الشرف.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82361" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي: أود أن أعرب عن خالص تقديري لحضور الملايين، وهذا الحضور المذهل والملهم الذي يحطم أعداء الثورة، في مدن وقرى إيران والعراق، وخاصة طهران، قم، النجف، كربلاء، ومشهد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82360" target="_blank">📅 14:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي:
أود أن أعرب عن خالص تقديري لحضور الملايين، وهذا الحضور المذهل والملهم الذي يحطم أعداء الثورة، في مدن وقرى إيران والعراق، وخاصة طهران، قم، النجف، كربلاء، ومشهد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82359" target="_blank">📅 14:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه وزارة الخارجية ورئاسة أركان الجيش والجهات الأمنية المعنية ميدانياً في محافظة البصرة بمتابعة تفاصيل حادثة مقتل الصياد العراقي نجم عبد الله واتخاذ الإجراءات القانونية التي تمنع تكرار مثل هذه الحوادث</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82358" target="_blank">📅 13:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏴‍☠️
أوكرانيا تنشر مشاهد من بحر آزوف تدعي فيه إصابة 28 سفينة روسية تابعة لـ "الأسطول الظل" خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82357" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff607673.mp4?token=NoFm0_p_CfXhzLRm8AumPcfQXbeXJLMwi0dYiJjn_vPHtcS381o-zeOgyKdeFiPhGyNwYClieCqd8cUlrckAac5mLHj7n7WAAf8gohbLSKVhQMlKVgGJOtXpfrLNqggxe53oJg9jg_f918nSlS9MYZIrxFr_2NwdNJGzLLHjchv3LKfgkVp3LGhvcfb4tBi3yBT2KIABIqBBI8d8Z1GkD84tCyWQy-u9kJoX8bFElDAtxWHmYhpkxlhHV32Wvh_411wMmdkiCPYPPI0XGLyw3S3rKuw9LN1C-bSY0p0Q5SwUEQeb62nEKcOP1QHa2msbvjS1wqIi07KsR4q2jZl9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff607673.mp4?token=NoFm0_p_CfXhzLRm8AumPcfQXbeXJLMwi0dYiJjn_vPHtcS381o-zeOgyKdeFiPhGyNwYClieCqd8cUlrckAac5mLHj7n7WAAf8gohbLSKVhQMlKVgGJOtXpfrLNqggxe53oJg9jg_f918nSlS9MYZIrxFr_2NwdNJGzLLHjchv3LKfgkVp3LGhvcfb4tBi3yBT2KIABIqBBI8d8Z1GkD84tCyWQy-u9kJoX8bFElDAtxWHmYhpkxlhHV32Wvh_411wMmdkiCPYPPI0XGLyw3S3rKuw9LN1C-bSY0p0Q5SwUEQeb62nEKcOP1QHa2msbvjS1wqIi07KsR4q2jZl9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الكويت لم تكتفي بقتل الصياد العراقي.. اعتداء جديد يوثقه أحد الصيادين العراقيين لخفر السواحل الكويتي أثناء مطاردته لهم في مياه خور عبد الله العراقية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82356" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز السخنة بريف حمص السورية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82354" target="_blank">📅 11:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز السخنة بريف حمص السورية</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82353" target="_blank">📅 11:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwt8ZFyW5F26npsBmY5g9kr3ZdFsrYGJ5PmDPJxgFMo2spQAkeM6bU7A6fPK53Y0eEHB1R1jb26asImMx6YPHJhmviwbypHcScRerpsSW1dIZ2IRtAIGxNH4THndT9NVwsWO2-nngk-D2_0vXP9kccc3kmn387ZkI78U5ssD97hPFU_PGRaOTGaa3o4-M3LmaCziyCeHPsBGM6N3OUBJoOW_WhL0j4mJtyjomp8n0rbwr_TyEylXwaFPpqhQvzE8otH6bybFllAkqwj2E8H01JiL65wMYpCLTOQJ1dkAX2Jiqs5cZBQn6kjKF4BknKlrl4yIBDs5iMYuTPpfuACyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
إدارة ترامب تصدر مذكرات استدعاء لصحفيي صحيفة نيويورك تايمز الذين كتبوا تقارير حول مخاوف أمنية تتعلق بطائرة "إير فورس وان" التي تبرعت بها قطر لترامب.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82352" target="_blank">📅 10:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82351" target="_blank">📅 09:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=C1zmi3QSPhuHUwbJJisOx5Z2zk9PLgH8jRGsdMGoVaGgQfmQjVl4jSo6itvFEoDsv9Lp0n3rF26PL_ji8Kmop9Wo9wEqkUT5ferGksUqy0pUbIBBi4D2VSuA-90u9BZchz8RUyQ1mkWm_BkOQ1R2XLzcU4275laas90L0mnxOxTb-9tySfiIHvj19ekmgBlg5pleFqGgUWK8m6kfQFDjBqfk9RiSgfgXcwmuvsVIenzbkgpmKl8fckQNRr0byD7i2H9N0inu06wjvMuKtci_kL5cEKJafEW0sQqmfemhHwW3bfUe71j2v06WdmVXq4u46iMu97SIdVDbfJFgEH5amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=C1zmi3QSPhuHUwbJJisOx5Z2zk9PLgH8jRGsdMGoVaGgQfmQjVl4jSo6itvFEoDsv9Lp0n3rF26PL_ji8Kmop9Wo9wEqkUT5ferGksUqy0pUbIBBi4D2VSuA-90u9BZchz8RUyQ1mkWm_BkOQ1R2XLzcU4275laas90L0mnxOxTb-9tySfiIHvj19ekmgBlg5pleFqGgUWK8m6kfQFDjBqfk9RiSgfgXcwmuvsVIenzbkgpmKl8fckQNRr0byD7i2H9N0inu06wjvMuKtci_kL5cEKJafEW0sQqmfemhHwW3bfUe71j2v06WdmVXq4u46iMu97SIdVDbfJFgEH5amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82349" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82348" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82347">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEWmQPm19GyBwafl5dYbd2aXDpnaFTjdwMhueGVjJSYaTnkcayCtyaH8grQ1_Hw1tfYKUtixknBD8vElHz91iMb3vUHH9llXdFn4b4nyILq8QEIVAKpTK8oy0Vi7dy4cPZSdlpBR4d95uJxSXpsg3IPyy3kMcLqRZtOsw9pWvd36dvF1Vc5ri_sJ7OnqnUZM0tQ_LoPQd7_psfquifGacVeJG18cUYnZSIr1m_Vmeo5jsx4L79R7UZtSyDie4fdNVSUyGhBM8stt9Aw6LAwW-Jy607Sdq0SxQwWTzViWn0RlZOJEm0Xl6xzmVZMR660707ocec3awNyERAEGv2-V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طائرة وزير الخارجية الإيراني عراقجي تهبط في مسقط عمان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82347" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knOHQZ-i_kU6qYnQmQa8XT3ity6IU-LCp7aMcfCDXEx_T7QaKgqfTvSK27o5g6Xc2tj6OWzFjHwgjAx9Fgq6RniIZG541dG437-G4hve5NfFLWnPq4cnd4ZT2m2apW1n1xa8kZnvYfJq5qoldIMhs76vLY9TV45OKJg3BzWug4rjANwpc-GGkqkbT0Ze5nkJT9zAy8F-nd4XALXXvlXVS5oFfv8DZainF8p6MfdhJRu5GUCv6QdnD5Oq9VSsVBes8nwsiwxf7h-S_cTwNH9r4F4OTRdwgZdb4fcX4h-UVdkUkt4qer-ivMaFZ4PPSEHYOz5JR3L2SV0Xmfgai4r1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
شركة شحن صينية عالقة بمضيق هرمز تسير بتباطؤ حاد حيث تتراوح سرعتها الحالية بين 0.1 إلى 0.4 عقدة بحرية فقط (شبه متوقفة) تشير المعلومات أنها قد تكون تعرضت لهجوم إيراني. لأنها مرت بالممر الأمريكي</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/82346" target="_blank">📅 08:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh47EP-A-dsfjf5-5s73EKrkjZIHyRKjd8__iPjEp6NpNtd5pLN0V79J4jVZfNQrTrlYwvxmbWp4exMpBNR615izjDkKL1q1rzdM4tqKfLG8SoiGpVJKxWbd7tPRyjYgG_ah2BYeNYfanH3MEK5Dl_lzVoeB9fF0HK_4eeR7tMAPMbX7Dxp3d0SOoE-qyblaa5lgFlD3sSxVdtL2hYCVM5Cej-WGvOI2lEYNQLIyF7RjVI0AO9yewVl9dCI9GJo5U3eiVbH8vipHnFFk0rRmJVgd2dvsM_eCU7hquCCiprBrjHGuM860DO3QUDIOa0kxgzc5KJEC2NENi5Bg-axI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
🇺🇸
قناة نيوز ماكس :
تم إيقاف تشغيل مؤقتًا حاملة الطائرات "يو. دي. كي. بوكسر" ومجموعة المشاة البحرية رقم 11 (MEU) التي كانت على متنها، في الأسابيع الأولى من الصراع مع إيران، بسبب عطل في نظام تبريد محركات السفينة، مما اضطر سفينة الإنزال إلى تغيير مسارها والتوجه إلى جزيرة دييغو غارسيا لإجراء الإصلاحات.
ويُذكر أن هذه المشكلة غير المتوقعة في الصيانة أدت إلى حرمان الولايات المتحدة  من قدرة استجابة سريعة مهمة، في الوقت الذي كان فيه البنتاغون يفرض حصارًا بحريًا على إيران ويدرس خيارات عسكرية إضافية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82345" target="_blank">📅 08:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📰
وول ستريت جورنال عن مسؤولين أمريكيين: إدارة ترمب ترى أن احتمالات التوصل لاتفاق نووي مع إيران تتضاءل</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/82344" target="_blank">📅 02:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
مالم تستطيع أمريكا أن تخفيه للوجهه القبيح لتنظيم النصرة الإرهابي
🔻
الصحفية الألمانية إيفا ماريا ميشلمان التي تم اعتقالها في سجون الجولاني في سوريا لمدة 6 أشهر تروي ما تعرضت له بمؤتمر صحفي في ألمانيا حيث حذرت المجتمع الأوروبي من حكومة الجولاني قائلة: "أرجوكم لا تصدقوا أن نظام هيئة تحرير الشام ديمقراطي بأي شكل من الأشكال".</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/82343" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الانفجارات في بلدتي الفوعة وكفريا حيث مكان تواجد الفصائل الإرهابية من الجنسيات الأجنبية</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/82342" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
رويترز عن مسؤولون أمريكيون كبار: ‏إذا لم نحصل على الغبار النووي، فلن يكون لدينا اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82341" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوي انفجارات تهز محافظة إدلب السورية</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82340" target="_blank">📅 00:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوي انفجارات تهز محافظة إدلب السورية</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/82339" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYnAwfUYy9ppi1iVB-6eIZkqNTYN1BWcOu5a6Wu8aIjU8FhIsYII0UYgEZxGsnbfy-TbOgAAKVOpX3h-3ByzUbxdT_ozifyNN24PfYOjHg_NtZjXXzVJToGVmKc60yzEi03awRhXCls49XrcREy22nxhocU8_qkFAKypjVaKp6ytGs3lb8ajeYsL3OJrl3nLs41Dmm7sQNdlBzI4XoK78mtpcGC3fB_e1CbQ8nGPE1C5zy9JPRxd5s2noHR4-vRWJUAiTtmlZTFRY7Qus3uRVZ6BoTaclRb8TS_woYjVsZPL-iU-qspZGGP5jG9YLYyfFkDeKVuRYiQrOmghzriHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/i/status/2075679676492558827</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/82338" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdItdjglb2qbdKMTtxORO4EpErLdXovGJ8IroJl7HfkSCPsdb-_rqIVv_TmTak27K_BcoZAFSevFYBW2FvyrhQBpU29a1MXjcRE0eEXxnM0xJVXi5q06A2UJjEIvE6boEcaGyH-vWqtgcODE7gnjObOJN0RMHOH1-Yd97JR4SeLA8NShkJqn3vncGvn1G4QngIdtsu-Cn-scHHxUc-9Otd1Z-IoopNqRToUksS2lkigHRRVqpTn0ASHkCReEvYOF_UwpNDc3DrIk8utsC4nF-j5q2CLeqPofsaVN_vSp1_mXsuux8kwHTPJpKuhHdFOnPOpmmlIX55onT5gZXvvLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم ﴿مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ فَمِنْهُمْ مَنْ قَضَى نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ وَمَا بَدَّلُوا تَبْدِيلاً﴾ في محطة تاريخية استثنائية تجلت فيها أسمى معاني الوفاء وتجديد العهد، سطرتم —أيها…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82337" target="_blank">📅 23:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
مراقبون لنايا  البيان قد يتضمن ثلاثة محاور ابرزها شكر الشعب العراقي بالتشيع و أيضا يتضمن رؤية المقاومة عن السلاح و  يبدو أن التنسيقية لم تعد موجودة حيث أن البيانات باتت تصدر بأسم المقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/82336" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
مراقبون لنايا  البيان قد يتضمن ثلاثة محاور ابرزها شكر الشعب العراقي بالتشيع و أيضا يتضمن رؤية المقاومة عن السلاح و  يبدو أن التنسيقية لم تعد موجودة حيث أن البيانات باتت تصدر بأسم المقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82335" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avgTvVXLoEMTddLIt72n6rd-SsKYG6Rf5QXG-j94YW8CSfUYH1AYyTZ2iN2M_ELy7ijHP32LHDq6xxAAzywhuznzaBdgb24RD12VRSciEghC-afsMuuNtU48sn_g325chatb9qjX9yZ3C1XLw565SKO4ScylV5jEVog3WHQjFmYWk8PKEE1PWHs-LJ0-pgr2rYP2PuwLhFWKH329gzZJ2FlWGYzbuVUiDVVH7P3Zfb-9Kf9FRKENl7_MRb18AM_s4DxxRUvU995ETVP54lBm_9cUNRUhfwa8a4BFnZ821YwvMZfPEH109I5ru--7lHcPBUK--rTgg2ldHSCrCYbqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ فَمِنْهُمْ مَنْ قَضَى نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ وَمَا بَدَّلُوا تَبْدِيلاً﴾
في محطة تاريخية استثنائية تجلت فيها أسمى معاني الوفاء وتجديد العهد، سطرتم —أيها الشعب العراقي الأبي— ملحمة تليق بعظمة سند المستضعفين الإمام الشهيد السيد علي الخامنئي (رضوان الله تعالى عليه)، وبحضوركم المليوني لتشييع جثمانه الطاهر في النجف الأشرف وكربلاء المقدسة؛ برهنتم أن الشعب العراقي الأصيل سيبقى متمسكًا بخطه المقاوم، ومكملاً لنهجه الجهادي في مقاومة الاستكبار العالمي.
إننا من أرض المقدسات نعلنها مجدداً ولتسمعها قوى الشر: إننا ثابتون، ومتمسكون بنهج المقاومة، وليعلم الأعداء أن قوى محور الحق كالجسد الواحد وفق الأطر الجهادية التي خطها لنا قائدنا الشهيد، ولن تثنينا الخطوب، ولن تزيدنا إلا إصراراً على مواصلة نهجنا لنصرة المستضعفين، وطرد المحتلين من العراق والمنطقة.
إن سلاحنا الذي تزينت به سواعد رجالنا في الميادين لم يكن يوماً خياراً للمساومة، بل هو عقيدة وعهد في أعناقنا، وأمانة الإمام المنتظر صاحب الأمر (عجل الله فرجه الشريف) ونائبه المفدى؛ وبه سنمضي لنكسر قيود الهيمنة، ونكبح جماح المستكبرين، فإما نصر عزيز تقر به أعين الصالحين، وإما شهادة تلحقنا بركب الأنبياء والصديقين.
وعليه، فإننا نؤكد للقاصي والداني أننا لن نقف عند حدود ما وصلنا إليه، بل سنعمل —بكل ما أوتينا من عزم وقوة— على تطوير قدراتنا العسكرية والأمنية كماً ونوعاً، ورفع الجاهزية بما يتناسب وحجم التحديات والتهديدات المتصاعدة التي يشكلها العدو الصهيوأمريكي؛ ولن يهدأ لنا بال، ولن تغمض لنا عين، حتى نبدد أوهام الطغاة، ونصون الكرامة، ونحفظ السيادة.
المقاومة الإسلامية في العراق</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82333" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بسبب الحر او الفگر وسط بغداد
اندلاع اشتباكات بمنطقة السنك وسط العاصمة بغداد ٥ جرحى كحصيلة أولية..</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82332" target="_blank">📅 23:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حصري لمكتب النائب حسين الدراجي
....................................
زيارة الصيادين العراقيين بعد عودتهم من أسر الكويت
((تم استهدافنا لأننا شيعة واتهمونا بأننا من الحششد الششعبي))</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82331" target="_blank">📅 23:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اندلاع حريق في قاعدة دبلن قرب مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82330" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82329">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حدث أمني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82329" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حدث أمني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82328" target="_blank">📅 23:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
تنويه:   المقاومة الإسلامية في العراق ستصدر بعد قليل بيان هام.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82327" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
تنويه:
المقاومة الإسلامية في العراق ستصدر بعد قليل بيان هام.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82326" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
